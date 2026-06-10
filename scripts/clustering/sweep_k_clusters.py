"""
Sweeps k values for MiniBatchKMeans on the v3 Arabic matn vectors.
Reports cohesion, near-duplicate centroid pairs, and size distribution
for each k to find the optimal cluster count.

Run inside container:
    docker exec search-web-1 python3 /code/tests/sweep_k_clusters.py
"""
import json, time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from collections import Counter

K_VALUES    = [50, 75, 100, 125, 150, 175, 200]
VECTORS_FILE = "/code/arabic_matn_embeddings.json"
REPORT_OUT   = "/code/k_sweep_report.md"

# ── Load vectors once ──────────────────────────────────────────────────────────
print("Loading vectors...")
t0 = time.time()
with open(VECTORS_FILE) as f:
    data = json.load(f)
urns    = list(data.keys())
vectors = np.array([data[u]["vector"] for u in urns], dtype=np.float32)
vectors = normalize(vectors, norm="l2")
print(f"  {len(urns):,} vectors loaded in {time.time()-t0:.1f}s")

def pair_counts(cents, thresholds):
    sim = cents @ cents.T
    K = len(cents)
    out = {}
    for t in thresholds:
        out[t] = sum(1 for i in range(K) for j in range(i+1,K) if sim[i,j] > t)
    out["max"] = float(np.max(sim - np.eye(K)))
    return out

THRESHOLDS = [0.75, 0.85, 0.93]

results = []

for k in K_VALUES:
    print(f"\nClustering k={k}...")
    t1 = time.time()
    km = MiniBatchKMeans(n_clusters=k, batch_size=4096, max_iter=200,
                         n_init=5, random_state=42, verbose=0)
    labels = km.fit_predict(vectors)
    cents  = normalize(km.cluster_centers_, norm="l2")

    counts = Counter(labels.tolist())

    # Cohesion
    cohesion = []
    for ki in range(k):
        mask = labels == ki
        if mask.sum() == 0:
            continue
        c = cents[ki]
        sims = vectors[mask] @ c
        cohesion.append(float(sims.mean()))
    avg_coh = np.mean(cohesion)

    pairs = pair_counts(cents, THRESHOLDS)

    sizes = sorted(counts.values(), reverse=True)
    size_p90 = sizes[int(len(sizes)*0.10)]   # 90th percentile (top 10%)
    size_p10 = sizes[int(len(sizes)*0.90)]   # 10th percentile (bottom 10%)

    elapsed = time.time() - t1
    print(f"  k={k}: cohesion={avg_coh:.3f} | pairs>0.93={pairs[0.93]} | "
          f"pairs>0.85={pairs[0.85]} | max_sim={pairs['max']:.3f} | {elapsed:.0f}s")

    results.append({
        "k": k,
        "cohesion": avg_coh,
        "pairs_93": pairs[0.93],
        "pairs_85": pairs[0.85],
        "pairs_75": pairs[0.75],
        "max_sim": pairs["max"],
        "size_median": sizes[len(sizes)//2],
        "size_p90": size_p90,
        "size_p10": size_p10,
        "elapsed": elapsed,
    })

# ── Write report ───────────────────────────────────────────────────────────────
lines = [
    "# k-Sweep Report — Arabic Matn v3 Vectors",
    f"\nCorpus: {len(urns):,} hadiths | Model: OpenAI text-embedding-3-small | L2-normalized\n",
    "## Summary Table\n",
    "| k | Cohesion | Pairs>0.93 | Pairs>0.85 | Pairs>0.75 | Max sim | Median size | P90 size | P10 size |",
    "|---|---|---|---|---|---|---|---|---|",
]
for r in results:
    lines.append(
        f"| {r['k']} | {r['cohesion']:.3f} | {r['pairs_93']} | {r['pairs_85']} | "
        f"{r['pairs_75']} | {r['max_sim']:.3f} | {r['size_median']} | {r['size_p90']} | {r['size_p10']} |"
    )

lines += [
    "\n## Guidance\n",
    "- **Pairs>0.93**: near-zero means no meaningful over-splitting. >20 suggests k is too high.",
    "- **Cohesion**: higher = tighter clusters. Should not drop below 0.60.",
    "- **Median size**: should be large enough to be useful as a filter (>500 hadiths).",
    "- **Max sim**: should be below 0.95 ideally — two centroids at 0.97 are the same topic.",
]

report = "\n".join(lines)
with open(REPORT_OUT, "w") as f:
    f.write(report)
print(f"\n\nReport written: {REPORT_OUT}")
print(report)
