"""
Clusters the 48k Arabic embeddings that have English translations (englishURN > 0).

Problem: the current arabic_cluster_centroids_final.json was computed over ALL 131k
Arabic hadiths. English queries route to centroids dominated by untranslated collections
(ibnabishayba, abdurrazzaq, hakim), so results are polluted even if we post-filter.

Fix: recompute centroids using only the translated subset so cluster pre-selection
stays within the translated corpus.

Reads:  ES arabic-openai index (fetches embedding + englishURN fields)
Writes: /code/arabic_translated_cluster_map.json      — {arabicURN_str: cluster_id}
        /code/arabic_translated_cluster_centroids.json — list of k × 1536 floats
        /code/arabic_translated_cluster_report.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/cluster_arabic_translated.py
"""
import os, json, time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from collections import Counter
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

K     = 75
INDEX = "arabic-openai"

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Fetch translated Arabic embeddings from ES ─────────────────────────────────
print("Fetching translated Arabic embeddings from ES (englishURN > 0)...")
t0 = time.time()

urns        = []
vectors_raw = []
collections = []

for hit in es_scan(
    es,
    index=INDEX,
    query={
        "query": {"range": {"englishURN": {"gt": 0}}},
        "_source": ["arabicURN", "collection", "embedding"],
    },
    size=500,
):
    s = hit["_source"]
    emb = s.get("embedding")
    if not emb:
        continue
    urns.append(str(s["arabicURN"]))
    vectors_raw.append(emb)
    collections.append(s.get("collection", ""))

print(f"  {len(urns):,} translated Arabic embeddings loaded ({time.time()-t0:.0f}s)")

vectors = normalize(np.array(vectors_raw, dtype=np.float32), norm="l2")
del vectors_raw

# ── Cluster ───────────────────────────────────────────────────────────────────
print(f"Running MiniBatchKMeans k={K}...")
t1 = time.time()
km = MiniBatchKMeans(
    n_clusters=K,
    batch_size=4096,
    max_iter=200,
    n_init=5,
    random_state=42,
    verbose=0,
)
labels    = km.fit_predict(vectors)
centroids = km.cluster_centers_
print(f"  Done in {time.time()-t1:.1f}s")

# ── Cohesion ───────────────────────────────────────────────────────────────────
counts   = Counter(labels.tolist())
cohesion = np.zeros(K)
for k_idx in range(K):
    mask = labels == k_idx
    if mask.sum() == 0:
        continue
    c = centroids[k_idx] / (np.linalg.norm(centroids[k_idx]) + 1e-10)
    cohesion[k_idx] = float((vectors[mask] @ c).mean())

# ── Save cluster map ───────────────────────────────────────────────────────────
cluster_map = {urns[i]: int(labels[i]) for i in range(len(urns))}
MAP_OUT = "/code/arabic_translated_cluster_map.json"
with open(MAP_OUT, "w") as f:
    json.dump(cluster_map, f)
print(f"Saved cluster map: {MAP_OUT}")

# ── Save L2-normalized centroids ───────────────────────────────────────────────
norms      = np.linalg.norm(centroids, axis=1, keepdims=True)
norm_cents = centroids / np.maximum(norms, 1e-9)
CENTS_OUT  = "/code/arabic_translated_cluster_centroids.json"
with open(CENTS_OUT, "w") as f:
    json.dump(norm_cents.tolist(), f)
print(f"Saved centroids: {CENTS_OUT}")

# ── Write cluster IDs back to ES (new field: clusterIdTranslated) ─────────────
print("Writing clusterIdTranslated to ES...")
es.indices.put_mapping(index=INDEX, body={"properties": {"clusterIdTranslated": {"type": "integer"}}})

from elasticsearch.helpers import bulk
BATCH = 500
urn_list = list(cluster_map.keys())
updated = errors = 0
t2 = time.time()

for i in range(0, len(urn_list), BATCH):
    batch = urn_list[i:i+BATCH]
    actions = [
        {
            "_op_type": "update",
            "_index": INDEX,
            "_id": f"arabic:{urn_str}",
            "doc": {"clusterIdTranslated": cluster_map[urn_str]},
        }
        for urn_str in batch
    ]
    ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
    updated += ok
    errors  += len(errs) if errs else 0
    if (i // BATCH) % 20 == 0:
        print(f"  {updated:,}/{len(urn_list):,} updated")

es.indices.refresh(index=INDEX)
print(f"ES update done in {time.time()-t2:.0f}s — updated={updated:,} errors={errors}")

# ── Report ─────────────────────────────────────────────────────────────────────
cluster_collections = [[] for _ in range(K)]
for i, lbl in enumerate(labels):
    cluster_collections[lbl].append(collections[i])

lines = [
    "# Arabic Translated-Only Cluster Report",
    f"\nModel: OpenAI text-embedding-3-small (1536-dim)  \nk={K}, MiniBatchKMeans, L2-normalized  \nCorpus: {len(urns):,} hadiths (englishURN > 0 only)\n",
    "| Cluster | Size | Cohesion | Top Collections |",
    "|---|---|---|---|",
]
for k_idx in sorted(range(K), key=lambda x: -counts[x]):
    sz       = counts[k_idx]
    coh      = cohesion[k_idx]
    top_cols = Counter(cluster_collections[k_idx]).most_common(3)
    top_str  = ", ".join(f"{c}({n})" for c, n in top_cols)
    lines.append(f"| {k_idx} | {sz} | {coh:.3f} | {top_str} |")

REPORT_OUT = "/code/arabic_translated_cluster_report.md"
with open(REPORT_OUT, "w") as f:
    f.write("\n".join(lines))
print(f"Saved report: {REPORT_OUT}")

elapsed = time.time() - t0
print(f"\nTotal: {elapsed:.0f}s | Avg cluster size: {len(urns)//K:,} | Avg cohesion: {cohesion.mean():.3f}")
