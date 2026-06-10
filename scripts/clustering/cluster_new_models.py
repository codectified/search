"""
Builds k-means cluster centroids for each new model index and writes
clusterIdShared / clusterIdLarge field to every doc.

Usage (inside container):
    python3 /code/tests/cluster_new_models.py <index_name> [k]

    index_name: multilingual-e5 | bge-m3 | qwen3-embed
                english-openai-large | arabic-openai-large

Writes:
    /code/<index_name>_centroids.json   — k×dim L2-normalized centroids
    /code/<index_name>_cluster_map.json — {doc_id: cluster_id}
"""
import os, sys, json, time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=120)

INDEX      = sys.argv[1] if len(sys.argv) > 1 else None
if not INDEX:
    print("Usage: cluster_new_models.py <index_name> [k]")
    sys.exit(1)

# Default k: 150 for smaller indexes, 200 for larger
K_DEFAULT  = 200 if "arabic" in INDEX or "multilingual" in INDEX or "bge" in INDEX or "qwen" in INDEX else 150
K          = int(sys.argv[2]) if len(sys.argv) > 2 else K_DEFAULT
CLUSTER_FIELD = "clusterIdShared" if "openai-large" not in INDEX else "clusterIdLarge"

CENTROIDS_FILE  = f"/code/{INDEX}_centroids.json"
CLUSTER_MAP_FILE = f"/code/{INDEX}_cluster_map.json"


print(f"Index: {INDEX} | k={K} | cluster_field={CLUSTER_FIELD}")

# ── Fetch all embeddings ──────────────────────────────────────────────────────
print("Fetching embeddings from ES...")
t0  = time.time()
ids = []
X   = []

for hit in es_scan(es, index=INDEX,
        query={"query": {"match_all": {}}},
        _source=["embedding"], size=200):
    emb = hit["_source"].get("embedding")
    if emb:
        ids.append(hit["_id"])
        X.append(emb)

X = np.array(X, dtype=np.float32)
print(f"  {len(ids):,} docs fetched in {time.time()-t0:.0f}s | dim={X.shape[1]}")

# ── Cluster ───────────────────────────────────────────────────────────────────
print(f"Running MiniBatchKMeans k={K}...")
t1  = time.time()
km  = MiniBatchKMeans(n_clusters=K, batch_size=4096, n_init=5,
                      max_iter=200, random_state=42)
labels = km.fit_predict(X)
print(f"  Fitted in {time.time()-t1:.0f}s")

# L2-normalize centroids for cosine similarity
cents = km.cluster_centers_.astype(np.float32)
norms = np.linalg.norm(cents, axis=1, keepdims=True)
cents = cents / np.where(norms > 0, norms, 1)

# Cohesion check
sample = min(5000, len(X))
idx    = np.random.choice(len(X), sample, replace=False)
sims   = (X[idx] * cents[labels[idx]]).sum(axis=1)
print(f"  Mean cosine to centroid (sample): {sims.mean():.4f}")

# ── Save centroids ────────────────────────────────────────────────────────────
with open(CENTROIDS_FILE, "w") as f:
    json.dump(cents.tolist(), f)
print(f"Saved: {CENTROIDS_FILE}")

cluster_map = {doc_id: int(lbl) for doc_id, lbl in zip(ids, labels)}
with open(CLUSTER_MAP_FILE, "w") as f:
    json.dump(cluster_map, f)
print(f"Saved: {CLUSTER_MAP_FILE}")

# ── Write cluster IDs back to ES ──────────────────────────────────────────────
print(f"Writing {CLUSTER_FIELD} to {len(ids):,} docs in ES...")
t2 = time.time()

WRITE_BATCH = 500
ok_total = err_total = 0

for i in range(0, len(ids), WRITE_BATCH):
    batch_ids    = ids[i:i + WRITE_BATCH]
    batch_labels = labels[i:i + WRITE_BATCH]
    actions = [
        {"_op_type": "update", "_index": INDEX, "_id": doc_id,
         "doc": {CLUSTER_FIELD: int(lbl)}}
        for doc_id, lbl in zip(batch_ids, batch_labels)
    ]
    try:
        ok, errs = es_bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        ok_total  += ok
        err_total += len(errs) if errs else 0
    except Exception as e:
        print(f"  Bulk error at {i}: {e}")
        err_total += 1

    if (i // WRITE_BATCH) % 20 == 0:
        print(f"  [{ok_total:,}/{len(ids):,}] err={err_total}")

es.indices.refresh(index=INDEX)
print(f"Updated: {ok_total:,} | errors: {err_total} | {time.time()-t2:.0f}s")
print(f"\nTotal time: {time.time()-t0:.0f}s")
