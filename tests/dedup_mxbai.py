"""
Find duplicate hadiths in english-mxbai using mxbai-embed-large vectors.

Same hadith reported via different narrator chains gets the same dupGroup id
(= smallest URN in the group). Singletons are left with no dupGroup field.

Algorithm: load all non-chain-ref vectors, normalize, batch dot-product,
union-find at cosine similarity >= THRESHOLD.

Run inside prod container after snapshot restore:
    python3 /code/tests/dedup_mxbai.py
"""
import os, time
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import numpy as np
from sklearn.preprocessing import normalize
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

INDEX     = "english-mxbai"
THRESHOLD = 0.93   # tune down to 0.91 if too few groups, up to 0.95 if too many false positives
BATCH_SZ  = 500
THREADS   = 16

es = Elasticsearch(
    os.environ.get("ES_HOST", "http://172.31.250.10:9200"),
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Load vectors ───────────────────────────────────────────────────────────────
print(f"Loading vectors from {INDEX}...")
t0 = time.time()

ids, vecs = [], []

for hit in es_scan(es, index=INDEX,
        query={"query": {"bool": {"must_not": {"term": {"isChainRef": True}}}}},
        _source=["semantic_text"],
        size=200):
    chunks = (
        hit["_source"].get("semantic_text") or {}
    ).get("inference", {}).get("chunks", [])
    chunk_vecs = [c["embeddings"] for c in chunks if c.get("embeddings")]
    if not chunk_vecs:
        continue
    # Average multi-chunk docs into a single representative vector
    vec = np.mean(chunk_vecs, axis=0) if len(chunk_vecs) > 1 else chunk_vecs[0]
    ids.append(hit["_id"])
    vecs.append(vec)

print(f"  {len(ids):,} docs loaded ({time.time()-t0:.0f}s)")

mat = normalize(np.array(vecs, dtype=np.float32), norm="l2")

# ── Union-Find ─────────────────────────────────────────────────────────────────
parent = {i: i for i in range(len(ids))}

def _find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def _union(x, y):
    px, py = _find(x), _find(y)
    if px != py:
        # root = smaller index (maps to smaller URN after sorting)
        if px < py:
            parent[py] = px
        else:
            parent[px] = py

# ── Batch cosine similarity ────────────────────────────────────────────────────
print(f"Computing pairwise similarities (threshold={THRESHOLD})...")
t0 = time.time()
pairs = 0

for start in range(0, len(ids), BATCH_SZ):
    batch = mat[start : start + BATCH_SZ]
    sims  = batch @ mat.T                     # (B, N)
    for bi, row in enumerate(sims):
        gi      = start + bi
        matches = np.where(row > THRESHOLD)[0]
        for mi in matches:
            if mi != gi:
                _union(gi, int(mi))
                pairs += 1

    done = min(start + BATCH_SZ, len(ids))
    if done % 5000 < BATCH_SZ or done == len(ids):
        print(f"  {done:,}/{len(ids):,} | pairs: {pairs:,}", end="\r")

print(f"\n  Done in {time.time()-t0:.0f}s | {pairs:,} pairs above threshold")

# ── Build groups ───────────────────────────────────────────────────────────────
groups: dict[int, list[int]] = defaultdict(list)
for i in range(len(ids)):
    groups[_find(i)].append(i)

dup_groups = {root: idxs for root, idxs in groups.items() if len(idxs) > 1}
print(f"Duplicate groups (≥2 members): {len(dup_groups):,}")

# Group id = smallest integer URN in the group (fallback: smallest _id string)
def _urn_int(doc_id):
    try:
        return int(doc_id)
    except ValueError:
        return 0

idx_to_group: dict[int, int] = {}
for root, idxs in dup_groups.items():
    sorted_idxs = sorted(idxs, key=lambda i: _urn_int(ids[i]))
    group_id    = _urn_int(ids[sorted_idxs[0]])
    for i in sorted_idxs:
        idx_to_group[i] = group_id

size_dist = Counter(len(v) for v in dup_groups.values())
print("Group size distribution:")
for sz in sorted(size_dist):
    print(f"  {sz} members: {size_dist[sz]:,} groups")

# ── Write dupGroup back ────────────────────────────────────────────────────────
print(f"\nWriting dupGroup to {INDEX} with {THREADS} threads...")
t0   = time.time()
done = err = 0

def _update(args):
    doc_id, gid = args
    es.update(index=INDEX, id=doc_id, body={"doc": {"dupGroup": gid}})
    return 1

updates = [(ids[i], gid) for i, gid in idx_to_group.items()]

with ThreadPoolExecutor(max_workers=THREADS) as pool:
    futures = {pool.submit(_update, u): u for u in updates}
    for fut in as_completed(futures):
        try:
            done += fut.result()
        except Exception as e:
            err += 1
            if err <= 5:
                print(f"  update error: {e}")
        if done % 2000 == 0 and done > 0:
            print(f"  {done:,}/{len(updates):,} | errors={err}", end="\r")

print(f"\nDone: {done:,} docs assigned dupGroup | {err} errors | {time.time()-t0:.0f}s")
print(f"\nTotal hadiths in duplicate groups: {len(updates):,}")
print(f"Singletons (no dupGroup): {len(ids) - len(updates):,}")
