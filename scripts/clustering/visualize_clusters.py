"""
Cluster visualizations for a given index.

Generates 4 plots saved to /code/test results & reports/viz/:
  1. UMAP 2D projection colored by cluster ID
  2. Cluster size distribution (histogram)
  3. Cluster cohesion distribution (mean cosine to centroid, per cluster)
  4. INT8 vs simulated-FP32 routing agreement heatmap (top-mismatch clusters)

Usage (inside container):
    python3 /code/tests/visualize_clusters.py <index_name> [n_docs]

    index_name: multilingual-e5 | arabic-openai | english-openai | ...
    n_docs:     sample size for UMAP (default 5000; full set for other plots)

Examples:
    python3 /code/tests/visualize_clusters.py multilingual-e5 5000
    python3 /code/tests/visualize_clusters.py arabic-openai 5000
"""
import os, sys, json, time
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan
from sklearn.cluster import MiniBatchKMeans

sys.path.insert(0, "/tmp/stpkg")
import matplotlib
matplotlib.use("Agg")  # no display needed
import matplotlib.pyplot as plt
import matplotlib.cm as cm

INDEX = sys.argv[1] if len(sys.argv) > 1 else "multilingual-e5"
N_UMAP = int(sys.argv[2]) if len(sys.argv) > 2 else 5000

OUT_DIR = f"/code/reports/clusters/{INDEX}/viz"
os.makedirs(OUT_DIR, exist_ok=True)

es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=120)

# ── Which cluster field does this index use? ──────────────────────────────────
CLUSTER_FIELD_MAP = {
    "arabic-openai":            "clusterIdTranslated",   # translated-only (production)
    "arabic-openai-all":        "clusterIdFinal",        # all Arabic hadiths (pass --all flag)
    "english-openai":           "clusterIdFinal",        # English matn-only (48k)
    "english-mxbai":            None,                    # no clustering
    "english-openai-large":     "clusterIdLarge",
    "arabic-openai-large":      "clusterIdLarge",
    "multilingual-e5":          "clusterIdShared",
    "bge-m3":                   "clusterIdShared",
    "qwen3-embed":              "clusterIdShared",
}
# When index alias ends in -all, use the real index name but alternate field
INDEX_ALIAS = {
    "arabic-openai-all": "arabic-openai",
}
cluster_field = CLUSTER_FIELD_MAP.get(INDEX, "clusterIdShared")
# Resolve alias (e.g. arabic-openai-all → real index arabic-openai)
ES_INDEX = INDEX_ALIAS.get(INDEX, INDEX)

# ── Fetch embeddings (+ cluster labels if available) ──────────────────────────
print(f"Fetching embeddings from {ES_INDEX} (field: {cluster_field})...")
t0 = time.time()
ids, X, labels_stored, langs = [], [], [], []

source_fields = ["embedding"]
if cluster_field:
    source_fields.append(cluster_field)
source_fields.append("lang")

# Filter to docs that actually have the cluster field populated.
# Avoids fetching docs with no label (e.g. Arabic-only hadiths lack clusterIdTranslated).
es_query = ({"query": {"exists": {"field": cluster_field}}}
            if cluster_field else {"query": {"match_all": {}}})

# For size/cohesion plots we want all docs; for UMAP we only need N_UMAP.
# Fetch up to MAX_FETCH docs; UMAP sub-samples from these.
# Keeps transfer small for large indexes (131k × 1536-dim is ~800MB of JSON).
MAX_FETCH = max(N_UMAP * 3, 20_000)

for hit in es_scan(es, index=ES_INDEX,
        query=es_query,
        _source=source_fields, size=500):
    emb = hit["_source"].get("embedding")
    if not emb:
        continue
    ids.append(hit["_id"])
    X.append(emb)
    if cluster_field:
        labels_stored.append(hit["_source"].get(cluster_field, -1))
    langs.append(hit["_source"].get("lang", "?"))
    if len(ids) >= MAX_FETCH:
        print(f"  Reached MAX_FETCH={MAX_FETCH:,} — stopping scan early")
        break

X = np.array(X, dtype=np.float32)
X /= np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-9)
n_docs = len(X)
print(f"  {n_docs:,} docs | dim={X.shape[1]} | {time.time()-t0:.0f}s")

# ── Run k-means if no stored labels ───────────────────────────────────────────
if not labels_stored or labels_stored[0] == -1:
    K = 200
    print(f"No stored cluster labels — running MiniBatchKMeans k={K}...")
    km = MiniBatchKMeans(n_clusters=K, batch_size=4096, n_init=5,
                         max_iter=200, random_state=42)
    labels = km.fit_predict(X)
    centroids = km.cluster_centers_.astype(np.float32)
    centroids /= np.maximum(np.linalg.norm(centroids, axis=1, keepdims=True), 1e-9)
    print(f"  Fitted k={K}")
else:
    labels = np.array(labels_stored, dtype=np.int32)
    valid = labels >= 0
    K = labels[valid].max() + 1 if valid.any() else 200
    # Recompute centroids from stored labels
    centroids = np.zeros((K, X.shape[1]), dtype=np.float32)
    for k in range(K):
        mask = labels == k
        if mask.any():
            centroids[k] = X[mask].mean(axis=0)
    centroids /= np.maximum(np.linalg.norm(centroids, axis=1, keepdims=True), 1e-9)
    print(f"  Using stored cluster labels (k={K})")

# ── Plot 1: Cluster size distribution ────────────────────────────────────────
print("Plotting cluster size distribution...")
sizes = np.bincount(labels[labels >= 0], minlength=K)

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(range(K), np.sort(sizes)[::-1], color="steelblue", alpha=0.8, width=1.0)
ax.set_xlabel("Cluster (sorted by size)")
ax.set_ylabel("Documents")
ax.set_title(f"{INDEX} — Cluster Size Distribution (k={K}, n={n_docs:,})")
ax.axhline(sizes.mean(), color="red", linestyle="--", linewidth=1,
           label=f"Mean: {sizes.mean():.0f}")
ax.legend()
plt.tight_layout()
out = f"{OUT_DIR}/{INDEX}_cluster_sizes.png"
plt.savefig(out, dpi=150)
plt.close()
print(f"  Saved: {out}")

# ── Plot 2: Cluster cohesion distribution ─────────────────────────────────────
print("Plotting cluster cohesion distribution...")
# Per-cluster mean cosine similarity to centroid
cohesions = []
for k in range(K):
    mask = labels == k
    if mask.sum() < 2:
        continue
    sims = (X[mask] * centroids[k]).sum(axis=1)
    cohesions.append(sims.mean())
cohesions = np.array(cohesions)

fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(cohesions, bins=40, color="teal", alpha=0.8, edgecolor="white")
ax.axvline(cohesions.mean(), color="red", linestyle="--", linewidth=1.5,
           label=f"Mean: {cohesions.mean():.3f}")
ax.axvline(cohesions.min(), color="orange", linestyle=":", linewidth=1.5,
           label=f"Min: {cohesions.min():.3f}")
ax.set_xlabel("Mean cosine similarity to centroid")
ax.set_ylabel("Number of clusters")
ax.set_title(f"{INDEX} — Cluster Cohesion Distribution")
ax.legend()
plt.tight_layout()
out = f"{OUT_DIR}/{INDEX}_cluster_cohesion.png"
plt.savefig(out, dpi=150)
plt.close()
print(f"  Saved: {out}")

# ── Plot 3: Language distribution per cluster (if lang field present) ──────────
if langs and set(langs) - {"?"}:
    print("Plotting language distribution per cluster...")
    langs_arr = np.array(langs)
    unique_langs = sorted(set(langs_arr) - {"?"})

    # Take top-20 most populous clusters
    top20 = np.argsort(sizes)[::-1][:20]
    lang_counts = {lg: [] for lg in unique_langs}
    for k in top20:
        mask = labels == k
        for lg in unique_langs:
            lang_counts[lg].append((langs_arr[mask] == lg).sum())

    fig, ax = plt.subplots(figsize=(12, 5))
    x = np.arange(20)
    width = 0.8 / len(unique_langs)
    colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]
    for i, lg in enumerate(unique_langs):
        ax.bar(x + i*width, lang_counts[lg], width, label=lg,
               color=colors[i % len(colors)], alpha=0.85)
    ax.set_xticks(x + width*(len(unique_langs)-1)/2)
    ax.set_xticklabels([f"C{top20[j]}" for j in range(20)], rotation=45, fontsize=8)
    ax.set_ylabel("Documents")
    ax.set_title(f"{INDEX} — Top-20 Clusters: Language Mix")
    ax.legend()
    plt.tight_layout()
    out = f"{OUT_DIR}/{INDEX}_cluster_langs.png"
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"  Saved: {out}")

# ── Plot 4: UMAP 2D projection ────────────────────────────────────────────────
print(f"Running UMAP on {min(N_UMAP, n_docs):,} docs...")
try:
    from umap import UMAP

    idx = np.random.choice(n_docs, min(N_UMAP, n_docs), replace=False)
    X_sub = X[idx]
    labels_sub = labels[idx]
    langs_sub = np.array(langs)[idx] if langs else None

    t1 = time.time()
    reducer = UMAP(n_components=2, n_neighbors=30, min_dist=0.1,
                   metric="cosine", random_state=42, n_jobs=4, verbose=False)
    emb2d = reducer.fit_transform(X_sub)
    print(f"  UMAP done in {time.time()-t1:.0f}s")

    # Color by cluster
    fig, ax = plt.subplots(figsize=(12, 10))
    sc = ax.scatter(emb2d[:, 0], emb2d[:, 1],
                    c=labels_sub, cmap="tab20", s=3, alpha=0.5, linewidths=0)
    ax.set_title(f"{INDEX} — UMAP (n={len(X_sub):,}, colored by cluster)")
    ax.set_xticks([]); ax.set_yticks([])
    plt.colorbar(sc, ax=ax, label="Cluster ID", fraction=0.03)
    plt.tight_layout()
    out = f"{OUT_DIR}/{INDEX}_umap_clusters.png"
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"  Saved: {out}")

    # Color by language (if available)
    if langs_sub is not None and len(set(langs_sub) - {"?"}) > 1:
        lang_to_int = {lg: i for i, lg in enumerate(sorted(set(langs_sub)))}
        colors_lang = np.array([lang_to_int[lg] for lg in langs_sub])
        cmap_lang = plt.cm.get_cmap("Set1", len(lang_to_int))
        fig, ax = plt.subplots(figsize=(12, 10))
        for lg, i in lang_to_int.items():
            mask = colors_lang == i
            ax.scatter(emb2d[mask, 0], emb2d[mask, 1],
                       c=[cmap_lang(i)], s=3, alpha=0.5, label=lg, linewidths=0)
        ax.set_title(f"{INDEX} — UMAP (n={len(X_sub):,}, colored by language)")
        ax.set_xticks([]); ax.set_yticks([])
        ax.legend(markerscale=5)
        plt.tight_layout()
        out = f"{OUT_DIR}/{INDEX}_umap_langs.png"
        plt.savefig(out, dpi=150)
        plt.close()
        print(f"  Saved: {out}")

except ImportError:
    print("  umap-learn not available — skipping UMAP plot")
except Exception as e:
    print(f"  UMAP failed: {e}")

print(f"\nDone. Plots in: {OUT_DIR}")
