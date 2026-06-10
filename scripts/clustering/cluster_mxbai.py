"""
Clusters 48,703 mxbai-embed-large vectors (1024-dim) from the english-mxbai ES index.

Uses k=50 based on the English k-sweep: at 48k docs, k=50 gives the best balance
(pairs>0.93=8, top-2 coverage ~6.5%, cohesion=0.726). k=75 over-splits (pairs>0.93=22).

Writes: /code/mxbai_cluster_map.json       — {englishURN_str: cluster_id}
        /code/mxbai_cluster_centroids.json  — list of 50 × 1024 floats (L2-normalized)
        /code/mxbai_cluster_report.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/cluster_mxbai.py
"""
import os, json, time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from collections import Counter
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

K     = 50
INDEX = "english-mxbai"

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Fetch mxbai vectors from ES ────────────────────────────────────────────────
# mxbai stores vectors inside semantic_text.inference.chunks[0].embeddings
print(f"Fetching mxbai vectors from {INDEX}...")
t0 = time.time()

urns        = []
vectors_raw = []
collections = []
skipped     = 0

for hit in es_scan(
    es,
    index=INDEX,
    query={"query": {"match_all": {}}, "_source": ["urn", "collection", "semantic_text"]},
    size=200,
):
    s = hit["_source"]
    chunks = s.get("semantic_text", {}).get("inference", {}).get("chunks", [])
    if not chunks or not chunks[0].get("embeddings"):
        skipped += 1
        continue
    urns.append(str(s.get("urn", hit["_id"])))
    vectors_raw.append(chunks[0]["embeddings"])
    collections.append(s.get("collection", ""))

print(f"  {len(urns):,} vectors loaded, {skipped} skipped ({time.time()-t0:.0f}s)")
print(f"  Dim: {len(vectors_raw[0])} (expect 1024)")

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

# ── Cohesion + near-duplicate centroid pairs ───────────────────────────────────
counts   = Counter(labels.tolist())
cohesion = np.zeros(K)
for k_idx in range(K):
    mask = labels == k_idx
    if mask.sum() == 0:
        continue
    c = centroids[k_idx] / (np.linalg.norm(centroids[k_idx]) + 1e-10)
    cohesion[k_idx] = float((vectors[mask] @ c).mean())

norms      = np.linalg.norm(centroids, axis=1, keepdims=True)
norm_cents = centroids / np.maximum(norms, 1e-9)
cent_sim   = norm_cents @ norm_cents.T
pairs_93   = sum(1 for i in range(K) for j in range(i+1, K) if cent_sim[i,j] > 0.93)

sizes  = sorted(counts.values(), reverse=True)
top2   = sum(sizes[:2])
top2_pct = 100 * top2 / len(urns)
print(f"  cohesion={cohesion.mean():.3f} | pairs>0.93={pairs_93} | median={sizes[len(sizes)//2]} | top2={top2:,} ({top2_pct:.1f}%)")

# ── Save cluster map ───────────────────────────────────────────────────────────
cluster_map = {urns[i]: int(labels[i]) for i in range(len(urns))}
MAP_OUT = "/code/mxbai_cluster_map.json"
with open(MAP_OUT, "w") as f:
    json.dump(cluster_map, f)
print(f"Saved cluster map: {MAP_OUT}")

# ── Save L2-normalized centroids ───────────────────────────────────────────────
CENTS_OUT = "/code/mxbai_cluster_centroids.json"
with open(CENTS_OUT, "w") as f:
    json.dump(norm_cents.tolist(), f)
print(f"Saved centroids: {CENTS_OUT}")

# ── Report ─────────────────────────────────────────────────────────────────────
cluster_collections = [[] for _ in range(K)]
for i, lbl in enumerate(labels):
    cluster_collections[lbl].append(collections[i])

lines = [
    "# mxbai Cluster Report",
    f"\nModel: mxbai-embed-large (1024-dim)  \nk={K}, MiniBatchKMeans, L2-normalized  \nCorpus: {len(urns):,} hadiths\n",
    f"Cohesion: {cohesion.mean():.3f} | Pairs>0.93: {pairs_93} | Avg cluster size: {len(urns)//K:,}\n",
    "| Cluster | Size | Cohesion | Top Collections |",
    "|---|---|---|---|",
]
for k_idx in sorted(range(K), key=lambda x: -counts[x]):
    sz       = counts[k_idx]
    coh      = cohesion[k_idx]
    top_cols = Counter(cluster_collections[k_idx]).most_common(3)
    top_str  = ", ".join(f"{c}({n})" for c, n in top_cols)
    lines.append(f"| {k_idx} | {sz} | {coh:.3f} | {top_str} |")

REPORT_OUT = "/code/mxbai_cluster_report.md"
with open(REPORT_OUT, "w") as f:
    f.write("\n".join(lines))
print(f"Saved report: {REPORT_OUT}")

elapsed = time.time() - t0
print(f"\nTotal: {elapsed:.0f}s")
