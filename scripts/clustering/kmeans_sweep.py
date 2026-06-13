"""
K-means sweep to find optimal k for arabic-research vector fields.

Tests k = 25, 50, 75, 100, 125, 150, 175, 200, 250, 300
Plots inertia (elbow) and silhouette score for each k.

Runs on a single field (default: vec_e5_arabic) since the shape of the
elbow is consistent across fields of the same corpus.

Run inside container:
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 \\
        -e MPLCONFIGDIR=/tmp/mpl -e HOME=/tmp \\
        search-web-1 python3 /code/scripts/clustering/kmeans_sweep.py

Env vars:
    VEC_FIELD   vector field to sweep (default: vec_e5_arabic)
    MAX_DOCS    cap on docs loaded (default: all)
"""
import os, sys, time
import numpy as np
sys.path.insert(0, "/tmp/stpkg")
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import normalize
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
FIELD   = os.environ.get("VEC_FIELD", "vec_e5_arabic")
MAX_DOCS = int(os.environ.get("MAX_DOCS", 999_999))
OUT_DIR = "/code/reports/viz"
os.makedirs(OUT_DIR, exist_ok=True)

K_VALUES = [25, 50, 75, 100, 125, 150, 175, 200, 250, 300]
# Silhouette is O(n²) — use a sample for speed
SILHOUETTE_SAMPLE = 5000

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW), request_timeout=120)

# ── Load vectors ──────────────────────────────────────────────────────────────
print(f"Loading {FIELD} from arabic-research...")
t0 = time.time()
vecs = []
for hit in es_scan(es, index="arabic-research",
        query={"query": {"exists": {"field": FIELD}}},
        _source=[FIELD], size=500):
    v = hit["_source"].get(FIELD)
    if v:
        vecs.append(v)
    if len(vecs) >= MAX_DOCS:
        break

X = normalize(np.array(vecs, dtype=np.float32), norm="l2")
del vecs
print(f"  {len(X):,} docs | dim={X.shape[1]} | {time.time()-t0:.0f}s")

# Silhouette sample (fixed subset for consistency across k values)
rng = np.random.default_rng(42)
sil_idx = rng.choice(len(X), min(SILHOUETTE_SAMPLE, len(X)), replace=False)
X_sil = X[sil_idx]

# ── Sweep ─────────────────────────────────────────────────────────────────────
inertias, silhouettes = [], []

for k in K_VALUES:
    t1 = time.time()
    km = MiniBatchKMeans(n_clusters=k, batch_size=4096, max_iter=300,
                         n_init=5, random_state=42, verbose=0)
    labels = km.fit_predict(X)
    inertia = km.inertia_

    sil_labels = labels[sil_idx]
    # Skip silhouette if any cluster has < 2 members in sample
    unique, counts = np.unique(sil_labels, return_counts=True)
    if (counts < 2).any() or len(unique) < 2:
        sil = float("nan")
    else:
        sil = silhouette_score(X_sil, sil_labels, metric="cosine",
                               sample_size=min(2000, len(X_sil)))

    inertias.append(inertia)
    silhouettes.append(sil)
    print(f"  k={k:>3} | inertia={inertia:,.1f} | silhouette={sil:.4f} | {time.time()-t1:.0f}s")

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Elbow
ax1.plot(K_VALUES, inertias, "o-", color="steelblue", linewidth=2, markersize=6)
ax1.set_ylabel("Inertia (lower = tighter clusters)")
ax1.set_title(f"K-means sweep — arabic-research / {FIELD} (n={len(X):,})")
ax1.grid(True, alpha=0.3)
# Annotate each point
for k, v in zip(K_VALUES, inertias):
    ax1.annotate(f"{v:,.0f}", (k, v), textcoords="offset points",
                 xytext=(0, 8), ha="center", fontsize=7)

# Silhouette
valid = [(k, s) for k, s in zip(K_VALUES, silhouettes) if not np.isnan(s)]
if valid:
    ks, ss = zip(*valid)
    ax2.plot(ks, ss, "o-", color="teal", linewidth=2, markersize=6)
    best_k = ks[np.argmax(ss)]
    best_s = max(ss)
    ax2.axvline(best_k, color="red", linestyle="--", linewidth=1,
                label=f"Best k={best_k} (sil={best_s:.4f})")
    ax2.legend()
    for k, s in zip(ks, ss):
        ax2.annotate(f"{s:.3f}", (k, s), textcoords="offset points",
                     xytext=(0, 8), ha="center", fontsize=7)

ax2.set_xlabel("k (number of clusters)")
ax2.set_ylabel("Silhouette score (higher = better separation)")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
out = f"{OUT_DIR}/kmeans_sweep_{FIELD}.png"
plt.savefig(out, dpi=150)
plt.close()
print(f"\nSaved: {out}")
print(f"\nSummary:")
for k, i, s in zip(K_VALUES, inertias, silhouettes):
    marker = " ← best silhouette" if (not np.isnan(s) and s == max(
        x for x in silhouettes if not np.isnan(x))) else ""
    print(f"  k={k:>3}: inertia={i:>10,.1f}  silhouette={s:.4f}{marker}")
