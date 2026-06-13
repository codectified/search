"""
Copy clusterIdLarge from arabic-openai-large → cluster_openai_large in arabic-research,
then compute centroids for vec_openai_large by streaming (avoids loading 1.6GB at once).

Run inside container:
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 \\
        search-web-1 python3 /code/scripts/clustering/copy_cluster_ids_large.py
"""
import os, json, time
import numpy as np
from collections import defaultdict
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
OUT_DIR = "/code/reports/centroids"
os.makedirs(OUT_DIR, exist_ok=True)

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW), request_timeout=120)

# ── Step 1: Copy cluster IDs from arabic-openai-large ────────────────────────
print("Copying clusterIdLarge → cluster_openai_large in arabic-research...")
t0 = time.time()

def copy_actions():
    for hit in es_scan(es, index="arabic-openai-large",
            query={"query": {"exists": {"field": "clusterIdLarge"}}},
            _source=["clusterIdLarge"], size=500):
        yield {
            "_op_type": "update",
            "_index": "arabic-research",
            "_id": hit["_id"],
            "doc": {"cluster_openai_large": hit["_source"]["clusterIdLarge"]},
        }

ok, errors = bulk(es, copy_actions(), chunk_size=500, raise_on_error=False)
print(f"  {ok:,} updated, {len(errors)} errors — {time.time()-t0:.0f}s")

# ── Step 2: Stream vec_openai_large to accumulate centroids ───────────────────
# Two-pass streaming: accumulate sum + count per cluster, then normalize.
print("Computing centroids for vec_openai_large via streaming...")
t1 = time.time()

# First pass: get K
r = es.search(index="arabic-research", size=0, aggs={
    "max_cluster": {"max": {"field": "cluster_openai_large"}}
})
K = int(r["aggregations"]["max_cluster"]["value"]) + 1
print(f"  k={K}")

DIM = 3072
centroid_sums  = np.zeros((K, DIM), dtype=np.float64)
centroid_counts = np.zeros(K, dtype=np.int64)
metas_by_cluster = defaultdict(list)
scores_by_cluster = defaultdict(list)

batch_n = 0
for hit in es_scan(es, index="arabic-research",
        query={"query": {"bool": {"must": [
            {"exists": {"field": "vec_openai_large"}},
            {"exists": {"field": "cluster_openai_large"}},
        ]}}},
        _source=["vec_openai_large", "cluster_openai_large",
                 "arabicMatn", "collection", "hadithNumber",
                 "gradeNorm", "isChainRef", "arabicURN"],
        size=200):
    s = hit["_source"]
    vec = s.get("vec_openai_large")
    cid = s.get("cluster_openai_large")
    if vec is None or cid is None:
        continue
    v = np.array(vec, dtype=np.float64)
    norm = np.linalg.norm(v)
    if norm > 0:
        v /= norm
    centroid_sums[cid] += v
    centroid_counts[cid] += 1
    metas_by_cluster[cid].append({
        "collection":   s.get("collection", ""),
        "hadithNumber": s.get("hadithNumber", ""),
        "gradeNorm":    s.get("gradeNorm", ""),
        "isChainRef":   s.get("isChainRef", False),
        "arabicURN":    s.get("arabicURN", 0),
        "text":         (s.get("arabicMatn") or "").strip()[:300],
    })
    # Store normalized vec for scoring (keep only for representative selection)
    scores_by_cluster[cid].append((v, len(metas_by_cluster[cid]) - 1))

    batch_n += 1
    if batch_n % 20000 == 0:
        print(f"  {batch_n:,} streamed — {time.time()-t1:.0f}s")

print(f"  {batch_n:,} docs streamed — {time.time()-t1:.0f}s")

# ── Step 3: Normalize centroids and compute cohesion ─────────────────────────
print("Building centroid JSON...")
centroids_out = {}
for cid in range(K):
    count = int(centroid_counts[cid])
    if count == 0:
        continue
    cent = centroid_sums[cid] / count
    norm = np.linalg.norm(cent)
    if norm > 0:
        cent /= norm
    cent_f32 = cent.astype(np.float32)

    # Cohesion: mean cosine to centroid (sample up to 500 for speed)
    vecs_and_idx = scores_by_cluster[cid]
    sample = vecs_and_idx[:500]
    sims = [float(np.dot(cent, v)) for v, _ in sample]
    cohesion = float(np.mean(sims)) if sims else 0.0

    mds = metas_by_cluster[cid]
    coll_counts = defaultdict(int)
    for m in mds:
        coll_counts[m["collection"]] += 1
    top_colls = dict(sorted(coll_counts.items(), key=lambda x: -x[1])[:8])

    ranked = sorted(
        [(sims[i], mds[vecs_and_idx[i][1]]) for i in range(len(sample))
         if not mds[vecs_and_idx[i][1]].get("isChainRef")],
        key=lambda x: -x[0]
    )[:5]

    centroids_out[cid] = {
        "size":     count,
        "cohesion": round(cohesion, 4),
        "top_collections": top_colls,
        "centroid": cent_f32.tolist(),
        "representative_hadiths": [
            {"score": round(s, 4), **m} for s, m in ranked
        ],
    }

json_path = f"{OUT_DIR}/arabic-research_openai_large.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(centroids_out, f, ensure_ascii=False)
print(f"  Written: {json_path}")
print(f"Done in {time.time()-t0:.0f}s total")
