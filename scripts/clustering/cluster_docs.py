"""
Generate cluster representative documents for a given index.

Fetches a sample of docs with embeddings + text fields, recomputes centroids
from stored cluster labels, then finds the top-3 nearest docs per cluster.
Outputs a ranked markdown report organized by cluster size.

Usage (inside container):
    python3 /code/tests/cluster_docs.py <index_name> [max_fetch]

    index_name: english-openai | arabic-openai | arabic-openai-all
                arabic-openai-large | multilingual-e5 | bge-m3 | qwen3-embed
    max_fetch:  max docs to sample (default 30000)

Output:
    /code/test results & reports/clusters/<index_name>/cluster_representatives.md
"""
import os, sys, json, time
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

INDEX     = sys.argv[1] if len(sys.argv) > 1 else "english-openai"
MAX_FETCH = int(sys.argv[2]) if len(sys.argv) > 2 else 30_000

es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=120)

# ── Index configuration ───────────────────────────────────────────────────────
CONFIGS = {
    "english-openai": {
        "es_index":      "english-openai",
        "cluster_field": "clusterIdFinal",
        "text_field":    "englishText",
        "arabic_field":  None,
    },
    "arabic-openai": {
        "es_index":      "arabic-openai",
        "cluster_field": "clusterIdTranslated",
        "text_field":    "englishText",
        "arabic_field":  "arabicMatn",
    },
    "arabic-openai-all": {
        "es_index":      "arabic-openai",
        "cluster_field": "clusterIdFinal",
        "text_field":    "englishText",
        "arabic_field":  "arabicMatn",
    },
    "arabic-openai-large": {
        "es_index":      "arabic-openai-large",
        "cluster_field": "clusterIdLarge",
        "text_field":    "englishText",
        "arabic_field":  "arabicMatn",
    },
    "multilingual-e5": {
        "es_index":      "multilingual-e5",
        "cluster_field": "clusterIdShared",
        "text_field":    "englishText",
        "arabic_field":  "arabicMatn",
    },
    "bge-m3": {
        "es_index":      "bge-m3",
        "cluster_field": "clusterIdShared",
        "text_field":    "englishText",
        "arabic_field":  "arabicMatn",
    },
    "qwen3-embed": {
        "es_index":      "qwen3-embed",
        "cluster_field": "clusterIdShared",
        "text_field":    "englishText",
        "arabic_field":  "arabicMatn",
    },
}

cfg = CONFIGS.get(INDEX)
if not cfg:
    print(f"Unknown index: {INDEX}. Known: {list(CONFIGS)}")
    sys.exit(1)

ES_INDEX      = cfg["es_index"]
CLUSTER_FIELD = cfg["cluster_field"]
TEXT_FIELD    = cfg["text_field"]
ARABIC_FIELD  = cfg["arabic_field"]

OUT_DIR = f"/code/test results & reports/clusters/{INDEX}"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_FILE = f"{OUT_DIR}/cluster_representatives.md"

# ── Fetch sample with embeddings + text ───────────────────────────────────────
print(f"Fetching up to {MAX_FETCH:,} docs from {ES_INDEX} (cluster_field={CLUSTER_FIELD})...")
t0 = time.time()

source_fields = ["embedding", CLUSTER_FIELD, "collection", "hadithNumber", TEXT_FIELD]
if ARABIC_FIELD:
    source_fields.append(ARABIC_FIELD)

ids, X, labels, texts, arabics, refs = [], [], [], [], [], []

for hit in es_scan(es, index=ES_INDEX,
        query={"query": {"exists": {"field": CLUSTER_FIELD}}},
        _source=source_fields, size=500):
    src = hit["_source"]
    emb = src.get("embedding")
    if not emb:
        continue
    lbl = src.get(CLUSTER_FIELD, -1)
    if lbl < 0:
        continue
    ids.append(hit["_id"])
    X.append(emb)
    labels.append(lbl)
    texts.append(src.get(TEXT_FIELD, "") or "")
    arabics.append(src.get(ARABIC_FIELD, "") if ARABIC_FIELD else "")
    refs.append(f"{src.get('collection','?')}:{src.get('hadithNumber','?')}")
    if len(ids) >= MAX_FETCH:
        print(f"  Reached MAX_FETCH={MAX_FETCH:,} — stopping scan")
        break

X = np.array(X, dtype=np.float32)
X /= np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-9)
labels = np.array(labels, dtype=np.int32)
n_docs = len(X)
K = labels.max() + 1
print(f"  {n_docs:,} docs | dim={X.shape[1]} | k={K} | {time.time()-t0:.0f}s")

# ── Recompute centroids from stored labels ────────────────────────────────────
centroids = np.zeros((K, X.shape[1]), dtype=np.float32)
for k in range(K):
    mask = labels == k
    if mask.any():
        centroids[k] = X[mask].mean(axis=0)
centroids /= np.maximum(np.linalg.norm(centroids, axis=1, keepdims=True), 1e-9)

sizes = np.bincount(labels, minlength=K)

# ── Find top-3 representatives per cluster ────────────────────────────────────
print("Computing representatives...")
cluster_reps = {}
for k in range(K):
    mask = np.where(labels == k)[0]
    if len(mask) == 0:
        continue
    sims = (X[mask] * centroids[k]).sum(axis=1)
    top3_local = np.argsort(sims)[::-1][:3]
    top3_global = mask[top3_local]
    reps = []
    for gi, li in zip(top3_global, top3_local):
        reps.append({
            "ref":    refs[gi],
            "score":  float(sims[li]),
            "text":   texts[gi],
            "arabic": arabics[gi],
        })
    cohesion = float(sims.mean())
    cluster_reps[k] = {"size": int(sizes[k]), "cohesion": cohesion, "reps": reps}

# ── Write markdown ────────────────────────────────────────────────────────────
print(f"Writing {OUT_FILE}...")
sorted_clusters = sorted(cluster_reps.items(), key=lambda kv: kv[1]["size"], reverse=True)

lines = [
    f"# {INDEX} — Cluster Representatives\n",
    f"*{n_docs:,} docs sampled · k={K} clusters · sorted by cluster size*\n",
    f"*Generated: {time.strftime('%Y-%m-%d')}*\n",
    "",
]

for k, info in sorted_clusters:
    size     = info["size"]
    cohesion = info["cohesion"]
    lines.append(f"## Cluster {k} &nbsp; (n={size:,} · cohesion={cohesion:.3f})\n")
    for rank, rep in enumerate(info["reps"], 1):
        ref   = rep["ref"]
        score = rep["score"]
        text  = rep["text"].strip()
        arabic = rep["arabic"].strip() if rep["arabic"] else ""

        # Truncate long text
        if len(text) > 300:
            text = text[:297] + "..."
        if len(arabic) > 120:
            arabic = arabic[:117] + "..."

        lines.append(f"{rank}. **{ref}** (cos={score:.3f})")
        if text:
            lines.append(f"   {text}")
        if arabic:
            lines.append(f"   *{arabic}*")
        lines.append("")
    lines.append("")

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Done → {OUT_FILE}")
print(f"  {len(sorted_clusters)} clusters written")
