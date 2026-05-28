"""
v2 Arabic matn clustering using OpenAI text-embedding-3-small vectors.
MiniBatchKMeans on 131k Arabic matn embeddings (1536-dim).

v1 used k=75 on 48k English hadiths.
v2 uses k=150 on 131k Arabic hadiths — same cluster density, 2.75x more hadiths.

Outputs:
  /code/arabic_cluster_map.json      — {arabicURN: cluster_id}
  /code/arabic_cluster_centroids.json — [centroid_vector, ...]
  /code/arabic_cluster_report.md     — per-cluster stats

Run inside container (requires numpy + sklearn):
    docker exec -u root search-web-1 pip install numpy scikit-learn
    docker exec search-web-1 python3 /code/tests/cluster_arabic_matn.py
"""
import json, time, os
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from collections import Counter

K = 150
VECTORS_FILE = "/code/arabic_matn_embeddings.json"
MAP_OUT     = "/code/arabic_cluster_map.json"
CENTS_OUT   = "/code/arabic_cluster_centroids.json"
REPORT_OUT  = "/code/arabic_cluster_report.md"

# ── Load vectors ───────────────────────────────────────────────────────────────
print(f"Loading vectors from {VECTORS_FILE}...")
t0 = time.time()
with open(VECTORS_FILE) as f:
    data = json.load(f)

urns       = list(data.keys())
vectors    = np.array([data[u]["vector"] for u in urns], dtype=np.float32)
had_tags   = [data[u]["had_matn_tag"] for u in urns]
collections = [data[u]["collection"] for u in urns]
print(f"  {len(urns):,} vectors loaded, shape {vectors.shape} ({time.time()-t0:.1f}s)")

# ── L2-normalize (cosine → euclidean on unit sphere) ──────────────────────────
vectors = normalize(vectors, norm="l2")

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
labels = km.fit_predict(vectors)
centroids = km.cluster_centers_
print(f"  Done in {time.time()-t1:.1f}s")

# ── Compute per-cluster cohesion ───────────────────────────────────────────────
print("Computing cohesion scores...")
cohesion = np.zeros(K)
counts   = Counter(labels.tolist())
for k_idx in range(K):
    mask = labels == k_idx
    if mask.sum() == 0:
        continue
    c = centroids[k_idx] / (np.linalg.norm(centroids[k_idx]) + 1e-10)
    sims = vectors[mask] @ c
    cohesion[k_idx] = float(sims.mean())

# ── Save cluster map ───────────────────────────────────────────────────────────
cluster_map = {urns[i]: int(labels[i]) for i in range(len(urns))}
with open(MAP_OUT, "w") as f:
    json.dump(cluster_map, f)
print(f"Saved cluster map: {MAP_OUT}")

# ── Save centroids ─────────────────────────────────────────────────────────────
with open(CENTS_OUT, "w") as f:
    json.dump(centroids.tolist(), f)
print(f"Saved centroids: {CENTS_OUT}")

# ── Build report ───────────────────────────────────────────────────────────────
# Per-cluster collection distribution
cluster_collections = [[] for _ in range(K)]
cluster_tagged = [0] * K
for i, lbl in enumerate(labels):
    cluster_collections[lbl].append(collections[i])
    if had_tags[i]:
        cluster_tagged[lbl] += 1

lines = [
    "# v2 Arabic Matn Cluster Report",
    f"\nModel: OpenAI text-embedding-3-small (1536-dim)  \nk={K}, MiniBatchKMeans, L2-normalized  \nCorpus: {len(urns):,} hadiths\n",
    "| Cluster | Size | Cohesion | Tagged% | Top Collections |",
    "|---|---|---|---|---|",
]
for k_idx in sorted(range(K), key=lambda x: -counts[x]):
    sz = counts[k_idx]
    coh = cohesion[k_idx]
    tag_pct = 100 * cluster_tagged[k_idx] / sz if sz else 0
    top_cols = Counter(cluster_collections[k_idx]).most_common(3)
    top_str = ", ".join(f"{c}({n})" for c, n in top_cols)
    lines.append(f"| {k_idx} | {sz} | {coh:.3f} | {tag_pct:.0f}% | {top_str} |")

with open(REPORT_OUT, "w") as f:
    f.write("\n".join(lines))
print(f"Saved report: {REPORT_OUT}")

elapsed = time.time() - t0
print(f"\nTotal: {elapsed:.0f}s | Avg cluster size: {len(urns)//K:,} | Avg cohesion: {cohesion.mean():.3f}")
