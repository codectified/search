"""
Generate cluster visualizations for all four vector fields in arabic-research.

Outputs to type-organized folders under /code/reports/viz/:
  umap/     — UMAP 2D projections
  sizes/    — cluster size distributions
  cohesion/ — cluster cohesion distributions

Filenames include the k value: arabic-research_{model}_k{K}.png

Usage (inside container):
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 \\
        -e MPLCONFIGDIR=/tmp/mpl -e NUMBA_CACHE_DIR=/tmp/numba -e HOME=/tmp \\
        -e K=50 \\
        search-web-1 python3 /code/scripts/clustering/visualize_arabic_research.py

Env vars:
    K       cluster count used (default 150) — used for field names and filenames
    N_UMAP  sample size for UMAP (default 5000)
    FIELDS  comma-separated subset to visualize (default: all four)
"""
import os, sys, time
import numpy as np

sys.path.insert(0, "/tmp/stpkg")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
K       = int(os.environ.get("K", 150))
N_UMAP  = int(os.environ.get("N_UMAP", 5000))
INDEX   = "arabic-research"

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW), request_timeout=120)

ALL_FIELDS = ["vec_openai", "vec_openai_large", "vec_e5_crosslingual", "vec_e5_arabic"]
FIELDS = [f.strip() for f in os.environ.get("FIELDS", ",".join(ALL_FIELDS)).split(",")]

FIELD_SLUG = {
    "vec_openai":          "openai",
    "vec_openai_large":    "openai_large",
    "vec_e5_crosslingual": "e5_crosslingual",
    "vec_e5_arabic":       "e5_arabic",
}
FIELD_LABEL = {
    "vec_openai":          "OpenAI 1536d",
    "vec_openai_large":    "OpenAI 3072d",
    "vec_e5_crosslingual": "E5 cross-lingual 1024d",
    "vec_e5_arabic":       "E5 Arabic-matn 1024d",
}

BASE = "/code/reports/viz"
for d in ["umap", "sizes", "cohesion"]:
    os.makedirs(f"{BASE}/{d}", exist_ok=True)


for vec_field in FIELDS:
    slug = FIELD_SLUG[vec_field]
    cluster_field = f"cluster_{slug}_k{K}"
    label = FIELD_LABEL[vec_field]
    fname_base = f"arabic-research_{slug}_k{K}"
    print(f"\n── {label} (k={K}) ──")

    MAX_FETCH = max(N_UMAP * 3, 20_000)
    t0 = time.time()
    ids, X, labels_stored = [], [], []

    for hit in es_scan(es, index=INDEX,
            query={"query": {"bool": {"must": [
                {"exists": {"field": vec_field}},
                {"exists": {"field": cluster_field}},
            ]}}},
            _source=[vec_field, cluster_field], size=500):
        s = hit["_source"]
        vec = s.get(vec_field)
        if not vec:
            continue
        ids.append(hit["_id"])
        X.append(vec)
        labels_stored.append(s.get(cluster_field, -1))
        if len(ids) >= MAX_FETCH:
            break

    if not ids:
        print(f"  No docs found with {cluster_field} — skipping")
        continue

    X = np.array(X, dtype=np.float32)
    X /= np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-9)
    labels = np.array(labels_stored, dtype=np.int32)
    k_actual = labels[labels >= 0].max() + 1 if (labels >= 0).any() else K
    n_docs = len(X)
    print(f"  {n_docs:,} docs | k={k_actual} | {time.time()-t0:.0f}s")

    # Recompute centroids from sample
    centroids = np.zeros((k_actual, X.shape[1]), dtype=np.float32)
    for k in range(k_actual):
        mask = labels == k
        if mask.any():
            centroids[k] = X[mask].mean(axis=0)
    centroids /= np.maximum(np.linalg.norm(centroids, axis=1, keepdims=True), 1e-9)

    # Size distribution
    sizes = np.bincount(labels[labels >= 0], minlength=k_actual)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(range(k_actual), np.sort(sizes)[::-1], color="steelblue", alpha=0.8, width=1.0)
    ax.axhline(sizes.mean(), color="red", linestyle="--", linewidth=1,
               label=f"Mean: {sizes.mean():.0f}")
    ax.set_xlabel("Cluster (sorted by size)")
    ax.set_ylabel("Documents")
    ax.set_title(f"arabic-research — {label} — Cluster Sizes (k={k_actual}, n={n_docs:,})")
    ax.legend()
    plt.tight_layout()
    out = f"{BASE}/sizes/{fname_base}.png"
    plt.savefig(out, dpi=150); plt.close()
    print(f"  Saved: {out}")

    # Cohesion distribution (skip for 3072d — cohesion not computed)
    cohesions = []
    for k in range(k_actual):
        mask = labels == k
        if mask.sum() < 2:
            continue
        sims = (X[mask] * centroids[k]).sum(axis=1)
        cohesions.append(sims.mean())
    if cohesions:
        cohesions = np.array(cohesions)
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.hist(cohesions, bins=max(10, k_actual // 3), color="teal", alpha=0.8, edgecolor="white")
        ax.axvline(cohesions.mean(), color="red", linestyle="--", linewidth=1.5,
                   label=f"Mean: {cohesions.mean():.3f}")
        ax.axvline(cohesions.min(), color="orange", linestyle=":", linewidth=1.5,
                   label=f"Min: {cohesions.min():.3f}")
        ax.set_xlabel("Mean cosine similarity to centroid")
        ax.set_ylabel("Number of clusters")
        ax.set_title(f"arabic-research — {label} — Cohesion (k={k_actual})")
        ax.legend()
        plt.tight_layout()
        out = f"{BASE}/cohesion/{fname_base}.png"
        plt.savefig(out, dpi=150); plt.close()
        print(f"  Saved: {out}")

    # UMAP
    try:
        from umap import UMAP
        idx = np.random.choice(n_docs, min(N_UMAP, n_docs), replace=False)
        X_sub = X[idx]
        labels_sub = labels[idx]
        t1 = time.time()
        reducer = UMAP(n_components=2, n_neighbors=15, min_dist=0.1,
                       metric="cosine", random_state=42, n_jobs=1, verbose=False)
        emb2d = reducer.fit_transform(X_sub)
        print(f"  UMAP done in {time.time()-t1:.0f}s")

        fig, ax = plt.subplots(figsize=(12, 10))
        sc = ax.scatter(emb2d[:, 0], emb2d[:, 1],
                        c=labels_sub, cmap="tab20", s=4, alpha=0.6, linewidths=0)
        ax.set_title(f"arabic-research — {label} — UMAP k={k_actual} (n={len(X_sub):,})")
        ax.set_xticks([]); ax.set_yticks([])
        plt.colorbar(sc, ax=ax, label="Cluster ID", fraction=0.03)
        plt.tight_layout()
        out = f"{BASE}/umap/{fname_base}.png"
        plt.savefig(out, dpi=150); plt.close()
        print(f"  Saved: {out}")
    except ImportError:
        print("  umap-learn not available — skipping UMAP")
    except Exception as e:
        print(f"  UMAP failed: {e}")

print(f"\nDone. Plots in: {BASE}/{{umap,sizes,cohesion}}/")
