"""
Cluster all four vector fields in the arabic-research index and write
cluster IDs + centroid JSONs for each.

Cluster field names include the k value: cluster_{model}_k{K}
Centroid files:                         arabic-research_{model}_k{K}.json

vec_openai_large (3072d) uses streaming partial_fit to avoid loading
~1.6 GB into RAM at once — all other fields load fully.

Run inside container:
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 \\
        search-web-1 python3 /code/scripts/clustering/cluster_arabic_research.py

Env vars:
    K       number of clusters (default 150)
    FIELDS  comma-separated subset (default: all four)
"""
import os, json, time
import numpy as np
from collections import defaultdict
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
K       = int(os.environ.get("K", 150))
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


def build_centroids_json(labels, X, metas, K):
    clusters = defaultdict(lambda: {"vectors": [], "metas": []})
    for i, cid in enumerate(labels):
        clusters[int(cid)]["vectors"].append(X[i])
        clusters[int(cid)]["metas"].append(metas[i])

    out = {}
    for cid, data in sorted(clusters.items()):
        vecs = np.array(data["vectors"])
        mds  = data["metas"]
        cent = vecs.mean(axis=0)
        cent = cent / (np.linalg.norm(cent) + 1e-9)
        scores = [cosine(cent, v) for v in vecs]
        coll_counts = defaultdict(int)
        for m in mds:
            coll_counts[m["collection"]] += 1
        ranked = sorted(
            [(scores[i], mds[i]) for i in range(len(mds)) if not mds[i].get("isChainRef")],
            key=lambda x: -x[0]
        )
        seen_groups: set = set()
        deduped = []
        for s, m in ranked:
            g = m.get("dupGroup") or 0
            if g and g in seen_groups:
                continue
            if g:
                seen_groups.add(g)
            deduped.append((s, m))
            if len(deduped) >= 5:
                break
        out[cid] = {
            "size":     len(vecs),
            "cohesion": round(float(np.mean(scores)), 4),
            "top_collections": dict(sorted(coll_counts.items(), key=lambda x: -x[1])[:8]),
            "centroid": cent.tolist(),
            "representative_hadiths": [
                {"score": round(s, 4), **m} for s, m in deduped
            ],
        }
    return out


def run_standard(vec_field, cluster_field, slug):
    """Load all vectors into RAM, cluster, write back. For ≤1024-dim fields."""
    print(f"Scanning {INDEX} for {vec_field}...")
    t0 = time.time()
    doc_ids, vectors, metas = [], [], []

    for hit in es_scan(es, index=INDEX,
            query={"query": {"exists": {"field": vec_field}}},
            _source=[vec_field, "arabicMatn", "collection", "hadithNumber",
                     "gradeNorm", "isChainRef", "arabicURN", "dupGroup"],
            size=500):
        s = hit["_source"]
        vec = s.get(vec_field)
        if not vec:
            continue
        doc_ids.append(hit["_id"])
        vectors.append(vec)
        metas.append({
            "collection":   s.get("collection", ""),
            "hadithNumber": s.get("hadithNumber", ""),
            "gradeNorm":    s.get("gradeNorm", ""),
            "isChainRef":   s.get("isChainRef", False),
            "arabicURN":    s.get("arabicURN", 0),
            "dupGroup":     s.get("dupGroup", 0),
            "text":         (s.get("arabicMatn") or "").strip(),
        })

    X = normalize(np.array(vectors, dtype=np.float32), norm="l2")
    print(f"  {len(doc_ids):,} docs | dim={X.shape[1]} | {time.time()-t0:.0f}s")
    del vectors

    print(f"Clustering k={K}...")
    t1 = time.time()
    km = MiniBatchKMeans(n_clusters=K, batch_size=4096, max_iter=300,
                         n_init=5, random_state=42, verbose=0)
    labels = km.fit_predict(X)
    print(f"  inertia={km.inertia_:.2f} | {time.time()-t1:.0f}s")

    _write_labels(doc_ids, labels, cluster_field)
    centroids = build_centroids_json(labels, X, metas, K)
    _write_json(centroids, slug)
    print(f"  Done in {time.time()-t0:.0f}s total")


def run_streaming(vec_field, cluster_field, slug):
    """Streaming partial_fit for 3072-dim field to avoid ~1.6 GB RAM spike."""
    SAMPLE_SIZE = 60_000
    ES_BATCH    = 300           # ES scroll page size
    FIT_BATCH   = max(512, K * 4)  # partial_fit batch — must be >= K

    print(f"Streaming {vec_field} (3072-dim, partial_fit)...")
    t0 = time.time()

    km = MiniBatchKMeans(n_clusters=K, batch_size=2048, max_iter=300,
                         n_init=5, random_state=42, verbose=0)
    sampled = 0
    buf = []

    print(f"  Pass 1: partial_fit in batches of {FIT_BATCH} on up to {SAMPLE_SIZE:,} docs...")
    for hit in es_scan(es, index=INDEX,
            query={"query": {"exists": {"field": vec_field}}},
            _source=[vec_field], size=ES_BATCH):
        v = hit["_source"].get(vec_field)
        if not v:
            continue
        buf.append(v)
        sampled += 1
        if len(buf) >= FIT_BATCH:
            arr = np.array(buf, dtype=np.float32)
            arr /= np.maximum(np.linalg.norm(arr, axis=1, keepdims=True), 1e-9)
            km.partial_fit(arr)
            buf = []
        if sampled >= SAMPLE_SIZE:
            break
    if buf:  # flush remainder
        arr = np.array(buf, dtype=np.float32)
        arr /= np.maximum(np.linalg.norm(arr, axis=1, keepdims=True), 1e-9)
        km.partial_fit(arr)
        buf = []

    print(f"  Fitted on {sampled:,} docs | inertia={km.inertia_:.2f} | {time.time()-t0:.0f}s")

    # Pass 2: predict labels for ALL docs + collect metas
    print(f"  Pass 2: predicting labels for all docs...")
    t1 = time.time()
    doc_ids, labels_list, metas = [], [], []

    for hit in es_scan(es, index=INDEX,
            query={"query": {"exists": {"field": vec_field}}},
            _source=[vec_field, "arabicMatn", "collection", "hadithNumber",
                     "gradeNorm", "isChainRef", "arabicURN", "dupGroup"],
            size=ES_BATCH):
        s = hit["_source"]
        v = s.get(vec_field)
        if not v:
            continue
        arr = np.array([v], dtype=np.float32)
        arr /= np.maximum(np.linalg.norm(arr, axis=1, keepdims=True), 1e-9)
        cid = int(km.predict(arr)[0])
        doc_ids.append(hit["_id"])
        labels_list.append(cid)
        metas.append({
            "collection":   s.get("collection", ""),
            "hadithNumber": s.get("hadithNumber", ""),
            "gradeNorm":    s.get("gradeNorm", ""),
            "isChainRef":   s.get("isChainRef", False),
            "arabicURN":    s.get("arabicURN", 0),
            "dupGroup":     s.get("dupGroup", 0),
            "text":         (s.get("arabicMatn") or "").strip(),
        })
        if len(doc_ids) % 20000 == 0:
            print(f"    {len(doc_ids):,} predicted — {time.time()-t1:.0f}s")

    labels = np.array(labels_list, dtype=np.int32)
    print(f"  {len(doc_ids):,} predicted | {time.time()-t1:.0f}s")

    _write_labels(doc_ids, labels, cluster_field)

    # Centroids: stream again to accumulate (avoid holding 3072-dim X in RAM)
    print("  Pass 3: streaming centroids...")
    t2 = time.time()
    DIM = 3072
    cent_sums   = np.zeros((K, DIM), dtype=np.float64)
    cent_counts = np.zeros(K, dtype=np.int64)
    label_map   = {doc_id: lbl for doc_id, lbl in zip(doc_ids, labels)}

    for hit in es_scan(es, index=INDEX,
            query={"query": {"exists": {"field": vec_field}}},
            _source=[vec_field], size=ES_BATCH):
        doc_id = hit["_id"]
        v = hit["_source"].get(vec_field)
        cid = label_map.get(doc_id)
        if v is None or cid is None:
            continue
        arr = np.array(v, dtype=np.float64)
        norm = np.linalg.norm(arr)
        if norm > 0:
            arr /= norm
        cent_sums[cid] += arr
        cent_counts[cid] += 1

    # Build centroid JSON from accumulated sums
    centroids_out = {}
    # Group metas by cluster
    cluster_metas = defaultdict(list)
    for doc_id, cid, m in zip(doc_ids, labels, metas):
        cluster_metas[int(cid)].append(m)

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
        seen_groups: set = set()
        deduped = []
        for m in mds:
            g = m.get("dupGroup") or 0
            if g and g in seen_groups:
                continue
            if g:
                seen_groups.add(g)
            deduped.append(m)
            if len(deduped) >= 5:
                break
        centroids_out[cid] = {
            "size":     count,
            "cohesion": 0.0,  # skip full cohesion for 3072-dim (expensive)
            "top_collections": dict(sorted(coll_counts.items(), key=lambda x: -x[1])[:8]),
            "centroid": cent.astype(np.float32).tolist(),
            "representative_hadiths": [
                {"score": 0.0, **m} for m in deduped
            ],
        }

    _write_json(centroids_out, slug)
    print(f"  Centroids done | {time.time()-t2:.0f}s")
    print(f"  Total: {time.time()-t0:.0f}s")


def _write_labels(doc_ids, labels, cluster_field):
    print(f"Writing {cluster_field} back to ES...")
    t = time.time()
    actions = (
        {"_op_type": "update", "_index": INDEX, "_id": doc_id,
         "doc": {cluster_field: int(cid)}}
        for doc_id, cid in zip(doc_ids, labels)
    )
    ok, errors = bulk(es, actions, chunk_size=500, raise_on_error=False)
    print(f"  {ok:,} updated, {len(errors)} errors — {time.time()-t:.0f}s")


def _write_json(centroids, slug):
    path = f"{OUT_DIR}/arabic-research_{slug}_k{K}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(centroids, f, ensure_ascii=False)
    print(f"  Written: {path}")


# ── Main ──────────────────────────────────────────────────────────────────────
for vec_field in FIELDS:
    slug = FIELD_SLUG[vec_field]
    cluster_field = f"cluster_{slug}_k{K}"
    print(f"\n{'='*60}")
    print(f"Field: {vec_field}  →  {cluster_field}")
    print(f"{'='*60}")

    if vec_field == "vec_openai_large":
        run_streaming(vec_field, cluster_field, slug)
    else:
        run_standard(vec_field, cluster_field, slug)

print("\nAll fields clustered.")
