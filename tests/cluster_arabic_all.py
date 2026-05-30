"""
Clusters all 131k Arabic hadiths using OpenAI text-embedding-3-small vectors.
Reads embeddings from the arabic-openai ES index (not the 3.9GB JSON file).
k=150 — same cluster density as English k=75 on 48k docs (131k/48k × 75 ≈ 205,
but k=150 was validated previously as a good balance).

Writes:
  /code/arabic_cluster_centroids_final.json  — list of k × 1536 L2-norm floats
  /code/arabic_all_cluster_map.json          — {arabicURN_str: cluster_id}
  /code/arabic_all_cluster_report.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/cluster_arabic_all.py
"""
import os, json, time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from collections import Counter
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

K     = 150
INDEX = "arabic-openai"

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Fetch all Arabic embeddings from ES ───────────────────────────────────────
print(f"Fetching all Arabic embeddings from {INDEX}...")
t0 = time.time()

urns        = []
vectors_raw = []
collections = []
skipped     = 0

for hit in es_scan(
    es,
    index=INDEX,
    query={"query": {"match_all": {}}, "_source": ["arabicURN", "collection", "embedding"]},
    size=500,
):
    s   = hit["_source"]
    emb = s.get("embedding")
    if not emb:
        skipped += 1
        continue
    urns.append(str(s.get("arabicURN", hit["_id"])))
    vectors_raw.append(emb)
    collections.append(s.get("collection", ""))

print(f"  {len(urns):,} vectors loaded, {skipped} skipped ({time.time()-t0:.0f}s)")
print(f"  Dim: {len(vectors_raw[0])} (expect 1536)")

vectors = normalize(np.array(vectors_raw, dtype=np.float32), norm="l2")
del vectors_raw

# ── Cluster ───────────────────────────────────────────────────────────────────
print(f"Running MiniBatchKMeans k={K}...")
t1 = time.time()
km = MiniBatchKMeans(n_clusters=K, batch_size=4096, max_iter=300, n_init=5,
                     random_state=42, verbose=0)
labels    = km.fit_predict(vectors)
centroids = km.cluster_centers_
print(f"  Done in {time.time()-t1:.1f}s")

# ── Cohesion + near-duplicate centroid pairs ──────────────────────────────────
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

sizes    = sorted(counts.values(), reverse=True)
top2     = sum(sizes[:2])
top2_pct = 100 * top2 / len(urns)
print(f"  cohesion={cohesion.mean():.3f} | pairs>0.93={pairs_93} | median={sizes[len(sizes)//2]} | top2={top2:,} ({top2_pct:.1f}%)")

# ── Save cluster map ──────────────────────────────────────────────────────────
cluster_map = {urns[i]: int(labels[i]) for i in range(len(urns))}
MAP_OUT = "/code/arabic_all_cluster_map.json"
with open(MAP_OUT, "w") as f:
    json.dump(cluster_map, f)
print(f"Saved cluster map: {MAP_OUT}")

# ── Save L2-normalized centroids (replaces arabic_cluster_centroids_final.json)
CENTS_OUT = "/code/arabic_cluster_centroids_final.json"
with open(CENTS_OUT, "w") as f:
    json.dump(norm_cents.tolist(), f)
print(f"Saved centroids: {CENTS_OUT}")

# ── Report ────────────────────────────────────────────────────────────────────
cluster_collections = [[] for _ in range(K)]
for i, lbl in enumerate(labels):
    cluster_collections[lbl].append(collections[i])

lines = [
    "# Arabic All-Hadith Cluster Report (clean matn embeddings)",
    f"\nModel: text-embedding-3-small (1536-dim)  \nk={K}, MiniBatchKMeans, L2-normalized  \nCorpus: {len(urns):,} hadiths\n",
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

REPORT_OUT = "/code/arabic_all_cluster_report.md"
with open(REPORT_OUT, "w") as f:
    f.write("\n".join(lines))
print(f"Saved report: {REPORT_OUT}")

elapsed = time.time() - t0
print(f"\nTotal: {elapsed:.0f}s")
print("Next: run tests/update_arabic_all_clusters.py to write clusterIdFinal to ES")
