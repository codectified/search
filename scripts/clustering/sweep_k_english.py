"""
k-sweep for English OpenAI centroid search.
Tests k values proportional to 48k corpus (vs k=150 for 131k Arabic).

Run inside container:
    docker exec search-web-1 python3 /code/tests/sweep_k_english.py
"""
import json, time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from collections import Counter

K_VALUES     = [25, 40, 50, 75, 100, 125]
VECTORS_FILE = "/code/english_openai_embeddings.json"
REPORT_OUT   = "/code/k_sweep_english_report.md"

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
        out[t] = sum(1 for i in range(K) for j in range(i+1, K) if sim[i,j] > t)
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
    size_median = sizes[len(sizes)//2]
    size_p90    = sizes[int(len(sizes)*0.10)]
    size_p10    = sizes[int(len(sizes)*0.90)]
    elapsed = time.time() - t1

    # What % of corpus is covered by top-2 clusters?
    top2 = sum(sorted(counts.values(), reverse=True)[:2])
    top2_pct = 100 * top2 / len(urns)

    print(f"  k={k}: cohesion={avg_coh:.3f} | pairs>0.93={pairs[0.93]} | "
          f"median={size_median} | top2={top2:,} ({top2_pct:.1f}%) | {elapsed:.0f}s")

    results.append({
        "k": k, "cohesion": avg_coh, "pairs_93": pairs[0.93],
        "pairs_85": pairs[0.85], "pairs_75": pairs[0.75],
        "max_sim": pairs["max"], "size_median": size_median,
        "size_p90": size_p90, "size_p10": size_p10,
        "top2_count": top2, "top2_pct": top2_pct,
    })

lines = [
    "# k-Sweep Report — English OpenAI Vectors",
    f"\nCorpus: {len(urns):,} hadiths | Model: OpenAI text-embedding-3-small | L2-normalized",
    "Pre-filter strategy: top-2 clusters → kNN within that subset\n",
    "## Summary Table\n",
    "| k | Cohesion | Pairs>0.93 | Pairs>0.85 | Max sim | Median size | Top-2 coverage | P90 | P10 |",
    "|---|---|---|---|---|---|---|---|---|",
]
for r in results:
    lines.append(
        f"| {r['k']} | {r['cohesion']:.3f} | {r['pairs_93']} | {r['pairs_85']} | "
        f"{r['max_sim']:.3f} | {r['size_median']} | {r['top2_count']:,} ({r['top2_pct']:.1f}%) | "
        f"{r['size_p90']} | {r['size_p10']} |"
    )

lines += [
    "\n## Guidance\n",
    "- **Cohesion**: higher = tighter clusters. Target ≥ 0.65 for good semantic grouping.",
    "- **Pairs>0.93**: near-zero means clusters are well-separated. >10 = over-splitting.",
    "- **Top-2 coverage**: how many docs the pre-filter lets through. Sweet spot: 1,000–3,000.",
    "- **Median size**: should be ≥ 300 to give kNN enough candidates after filtering.",
    "- **Note**: Arabic used k=150 on 131k (≈873/cluster). Same density on 48k = k≈55.",
]

with open(REPORT_OUT, "w") as f:
    f.write("\n".join(lines))
print(f"\nReport written: {REPORT_OUT}")
print("\n".join(lines))
