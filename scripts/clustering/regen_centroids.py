"""
Re-generate centroid JSON files from cluster labels already stored in ES.
Does NOT re-cluster — reads cluster_{slug}_k{K} field directly.

Usage (inside container):
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 -e K=25 \\
        search-web-1 python3 /code/scripts/clustering/regen_centroids.py

Env vars:
    K       cluster count to regen (default 25)
    FIELDS  comma-separated subset (default: all four)
"""
import os, json, time
import numpy as np
from collections import defaultdict
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
K       = int(os.environ.get("K", 25))
INDEX   = "arabic-research"
OUT_DIR = "/code/reports/centroids"
os.makedirs(OUT_DIR, exist_ok=True)

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


def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))


def dedup_reps(mds_with_scores):
    """Return up to 5 hadiths, one per dupGroup, highest score first."""
    seen: set = set()
    out = []
    for item in mds_with_scores:
        g = item.get("dupGroup") or 0
        if g and g in seen:
            continue
        if g:
            seen.add(g)
        out.append(item)
        if len(out) >= 5:
            break
    return out


def regen_standard(vec_field, cluster_field, slug):
    """For ≤1024-dim fields: load vectors + labels into RAM, compute centroids."""
    print(f"Scanning {INDEX} for {vec_field} + {cluster_field}...")
    t0 = time.time()
    doc_ids, vectors, labels, metas = [], [], [], []

    for hit in es_scan(es, index=INDEX,
            query={"query": {"exists": {"field": cluster_field}}},
            _source=[vec_field, cluster_field, "arabicMatn", "collection",
                     "hadithNumber", "gradeNorm", "isChainRef", "arabicURN", "dupGroup"],
            size=500):
        s = hit["_source"]
        vec = s.get(vec_field)
        cid = s.get(cluster_field)
        if vec is None or cid is None:
            continue
        doc_ids.append(hit["_id"])
        vectors.append(vec)
        labels.append(int(cid))
        metas.append({
            "collection":   s.get("collection", ""),
            "hadithNumber": s.get("hadithNumber", ""),
            "gradeNorm":    s.get("gradeNorm", ""),
            "isChainRef":   s.get("isChainRef", False),
            "arabicURN":    s.get("arabicURN", 0),
            "dupGroup":     s.get("dupGroup", 0),
            "text":         (s.get("arabicMatn") or "").strip(),
        })

    print(f"  {len(doc_ids):,} docs | {time.time()-t0:.0f}s")

    X = np.array(vectors, dtype=np.float32)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    X /= np.maximum(norms, 1e-9)
    del vectors

    # Group by cluster
    clusters = defaultdict(lambda: {"vecs": [], "metas": []})
    for i, cid in enumerate(labels):
        clusters[cid]["vecs"].append(X[i])
        clusters[cid]["metas"].append(metas[i])

    out = {}
    for cid, data in sorted(clusters.items()):
        vecs = np.array(data["vecs"])
        mds  = data["metas"]
        cent = vecs.mean(axis=0)
        cent /= np.linalg.norm(cent) + 1e-9
        scores = [cosine(cent, v) for v in vecs]
        coll_counts = defaultdict(int)
        for m in mds:
            coll_counts[m["collection"]] += 1
        ranked = sorted(
            [(scores[i], mds[i]) for i in range(len(mds)) if not mds[i].get("isChainRef")],
            key=lambda x: -x[0]
        )
        deduped = dedup_reps([{"score": round(s, 4), **m} for s, m in ranked])
        out[cid] = {
            "size":     len(vecs),
            "cohesion": round(float(np.mean(scores)), 4),
            "top_collections": dict(sorted(coll_counts.items(), key=lambda x: -x[1])[:8]),
            "centroid": cent.tolist(),
            "representative_hadiths": deduped,
        }

    _write_json(out, slug)
    print(f"  Done in {time.time()-t0:.0f}s")


def regen_streaming(vec_field, cluster_field, slug):
    """For 3072-dim field: stream all docs, accumulate centroid sums."""
    DIM = 3072
    ES_BATCH = 300
    print(f"Streaming {INDEX} for {vec_field} + {cluster_field} (3072-dim)...")
    t0 = time.time()

    cent_sums   = np.zeros((K, DIM), dtype=np.float64)
    cent_counts = np.zeros(K, dtype=np.int64)
    cluster_metas = defaultdict(list)

    for hit in es_scan(es, index=INDEX,
            query={"query": {"exists": {"field": cluster_field}}},
            _source=[vec_field, cluster_field, "arabicMatn", "collection",
                     "hadithNumber", "gradeNorm", "isChainRef", "arabicURN", "dupGroup"],
            size=ES_BATCH):
        s = hit["_source"]
        v = s.get(vec_field)
        cid = s.get(cluster_field)
        if v is None or cid is None:
            continue
        cid = int(cid)
        arr = np.array(v, dtype=np.float64)
        norm = np.linalg.norm(arr)
        if norm > 0:
            arr /= norm
        cent_sums[cid] += arr
        cent_counts[cid] += 1
        cluster_metas[cid].append({
            "collection":   s.get("collection", ""),
            "hadithNumber": s.get("hadithNumber", ""),
            "gradeNorm":    s.get("gradeNorm", ""),
            "isChainRef":   s.get("isChainRef", False),
            "arabicURN":    s.get("arabicURN", 0),
            "dupGroup":     s.get("dupGroup", 0),
            "text":         (s.get("arabicMatn") or "").strip(),
        })
        if sum(cent_counts) % 20000 == 0 and sum(cent_counts) > 0:
            print(f"    {sum(cent_counts):,} docs — {time.time()-t0:.0f}s")

    out = {}
    for cid in range(K):
        count = int(cent_counts[cid])
        if count == 0:
            continue
        cent = cent_sums[cid] / count
        norm = np.linalg.norm(cent)
        if norm > 0:
            cent /= norm
        mds = cluster_metas[cid]
        coll_counts = defaultdict(int)
        for m in mds:
            coll_counts[m["collection"]] += 1
        deduped = dedup_reps([{"score": 0.0, **m} for m in mds if not m.get("isChainRef")])
        out[cid] = {
            "size":     count,
            "cohesion": 0.0,
            "top_collections": dict(sorted(coll_counts.items(), key=lambda x: -x[1])[:8]),
            "centroid": cent.astype(np.float32).tolist(),
            "representative_hadiths": deduped,
        }

    _write_json(out, slug)
    print(f"  Done in {time.time()-t0:.0f}s")


def _write_json(centroids, slug):
    path = f"{OUT_DIR}/arabic-research_{slug}_k{K}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(centroids, f, ensure_ascii=False)
    print(f"  Written: {path}")


for vec_field in FIELDS:
    slug = FIELD_SLUG[vec_field]
    cluster_field = f"cluster_{slug}_k{K}"
    print(f"\n{'='*60}")
    print(f"Regen: {cluster_field}  →  arabic-research_{slug}_k{K}.json")
    print(f"{'='*60}")
    if vec_field == "vec_openai_large":
        regen_streaming(vec_field, cluster_field, slug)
    else:
        regen_standard(vec_field, cluster_field, slug)

print("\nAll centroid JSONs regenerated.")
