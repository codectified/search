"""
Clusters 48,703 English OpenAI embeddings (text-embedding-3-small, 1536-dim)
using MiniBatchKMeans k=75 — same density as the original v1 English clustering.

Reads:  /code/english_openai_embeddings.json  (URN → {vector, collection, ...})
Writes: /code/english_cluster_map.json        — {englishURN_str: cluster_id}
        /code/english_cluster_centroids.json  — list of 75 × 1536 floats (L2-normalized)
        /code/english_cluster_report.md       — per-cluster stats

Run inside container:
    docker exec search-web-1 python3 /code/tests/cluster_english_openai.py
"""
import json, time, os
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from collections import Counter

K            = 75
VECTORS_FILE = "/code/english_openai_embeddings.json"
MAP_OUT      = "/code/english_cluster_map.json"
CENTS_OUT    = "/code/english_cluster_centroids.json"
REPORT_OUT   = "/code/english_cluster_report.md"

# ── Load vectors ───────────────────────────────────────────────────────────────
print(f"Loading vectors from {VECTORS_FILE}...")
t0 = time.time()
with open(VECTORS_FILE) as f:
    data = json.load(f)

urns        = list(data.keys())          # englishURN strings
vectors     = np.array([data[u]["vector"] for u in urns], dtype=np.float32)
collections = [data[u]["collection"] for u in urns]
chain_refs  = [data[u].get("isChainRef", False) for u in urns]
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
labels    = km.fit_predict(vectors)
centroids = km.cluster_centers_
print(f"  Done in {time.time()-t1:.1f}s")

# ── Per-cluster cohesion ───────────────────────────────────────────────────────
print("Computing cohesion scores...")
cohesion = np.zeros(K)
counts   = Counter(labels.tolist())
for k_idx in range(K):
    mask = labels == k_idx
    if mask.sum() == 0:
        continue
    c = centroids[k_idx] / (np.linalg.norm(centroids[k_idx]) + 1e-10)
    cohesion[k_idx] = float((vectors[mask] @ c).mean())

# ── Save cluster map {englishURN_str: cluster_id} ─────────────────────────────
cluster_map = {urns[i]: int(labels[i]) for i in range(len(urns))}
with open(MAP_OUT, "w") as f:
    json.dump(cluster_map, f)
print(f"Saved cluster map: {MAP_OUT}")

# ── Save L2-normalized centroids ───────────────────────────────────────────────
norms     = np.linalg.norm(centroids, axis=1, keepdims=True)
norm_cents = centroids / np.maximum(norms, 1e-9)
with open(CENTS_OUT, "w") as f:
    json.dump(norm_cents.tolist(), f)
print(f"Saved centroids: {CENTS_OUT}")

# ── Build report ───────────────────────────────────────────────────────────────
cluster_collections = [[] for _ in range(K)]
cluster_chain_refs  = [0] * K
for i, lbl in enumerate(labels):
    cluster_collections[lbl].append(collections[i])
    if chain_refs[i]:
        cluster_chain_refs[lbl] += 1

lines = [
    "# English OpenAI Cluster Report",
    f"\nModel: OpenAI text-embedding-3-small (1536-dim)  \nk={K}, MiniBatchKMeans, L2-normalized  \nCorpus: {len(urns):,} hadiths\n",
    f"Chain-ref hadiths (isChainRef=True): {sum(chain_refs):,}\n",
    "| Cluster | Size | Cohesion | ChainRef% | Top Collections |",
    "|---|---|---|---|---|",
]
for k_idx in sorted(range(K), key=lambda x: -counts[x]):
    sz  = counts[k_idx]
    coh = cohesion[k_idx]
    cr_pct  = 100 * cluster_chain_refs[k_idx] / sz if sz else 0
    top_cols = Counter(cluster_collections[k_idx]).most_common(3)
    top_str  = ", ".join(f"{c}({n})" for c, n in top_cols)
    lines.append(f"| {k_idx} | {sz} | {coh:.3f} | {cr_pct:.0f}% | {top_str} |")

with open(REPORT_OUT, "w") as f:
    f.write("\n".join(lines))
print(f"Saved report: {REPORT_OUT}")

elapsed = time.time() - t0
print(f"\nTotal: {elapsed:.0f}s | Avg cluster size: {len(urns)//K:,} | Avg cohesion: {cohesion.mean():.3f}")
