"""
Build the arabic-research consolidated index.

Merges vectors from three existing indexes into one document per Arabic hadith:
  - arabic-openai       → vec_openai      (1536-dim)
  - arabic-openai-large → vec_openai_large (3072-dim)
  - multilingual-e5     → vec_e5_crosslingual (1024-dim, Arabic docs only)

All three indexes share the same _id format ("arabic:NNNNNN"), so the join
is a direct _id lookup — no urn matching needed.

The vec_e5_arabic field (Arabic-matn-only E5 embeddings) is NOT written here;
run embed_e5_arabic.py after this script to backfill that field.

Usage (host machine, targeting localhost:9200):
    ELASTIC_PASSWORD=docker123 python3 scripts/indexing/create_arabic_research_index.py

Env vars:
    ELASTIC_PASSWORD   (default: docker123)
    ES_HOST            (default: localhost)
    BATCH_SIZE         (default: 500)
    RECREATE           set to 1 to drop and recreate the index
"""
import os, time, json
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
BATCH   = int(os.environ.get("BATCH_SIZE", 500))
RECREATE = os.environ.get("RECREATE", "0") == "1"
TARGET  = "arabic-research"

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW),
                   request_timeout=120)

# ── Index mapping ──────────────────────────────────────────────────────────────
MAPPING = {
    "mappings": {
        "properties": {
            "arabicMatn":        {"type": "text"},
            "arabicText":        {"type": "text", "index": False},
            "arabicURN":         {"type": "long"},
            "collection":        {"type": "keyword"},
            "hadithNumber":      {"type": "keyword"},
            "gradeNorm":         {"type": "keyword"},
            "gradeArabic":       {"type": "keyword"},
            "isChainRef":        {"type": "boolean"},
            "dupGroup":          {"type": "long"},
            "hadMatnTag":        {"type": "boolean"},
            "vec_openai":        {"type": "dense_vector", "dims": 1536,
                                  "index": True, "similarity": "cosine"},
            "vec_openai_large":  {"type": "dense_vector", "dims": 3072,
                                  "index": True, "similarity": "cosine"},
            "vec_e5_crosslingual": {"type": "dense_vector", "dims": 1024,
                                    "index": True, "similarity": "cosine"},
            "vec_e5_arabic":     {"type": "dense_vector", "dims": 1024,
                                  "index": True, "similarity": "cosine"},
            # Cluster IDs — populated by clustering scripts
            "cluster_openai":        {"type": "integer"},
            "cluster_openai_large":  {"type": "integer"},
            "cluster_e5_crosslingual": {"type": "integer"},
            "cluster_e5_arabic":     {"type": "integer"},
        }
    },
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
    }
}

if RECREATE:
    if es.indices.exists(index=TARGET):
        es.indices.delete(index=TARGET)
        print(f"Deleted existing index: {TARGET}")

if not es.indices.exists(index=TARGET):
    es.indices.create(index=TARGET, body=MAPPING)
    print(f"Created index: {TARGET}")
else:
    print(f"Index {TARGET} already exists — will upsert docs")

# ── Step 1: Load large-model vectors into memory (by _id) ────────────────────
# arabic-openai-large has 131k docs at 3072-dim — too big to hold entirely in RAM
# as raw floats (~1.5GB), so we load lazily in the merge loop via mget batching.
# For multilingual-e5 Arabic docs we also do mget per batch.
print("Ready to merge. Will mget large+e5 vectors per batch during scan...")

# ── Step 2: Scan arabic-openai and merge ──────────────────────────────────────
print(f"Scanning arabic-openai...")
t0 = time.time()
batch_docs = []
ok_total = err_total = 0
processed = 0


def flush(batch_docs):
    global ok_total, err_total
    if not batch_docs:
        return
    # Collect _ids for mget lookups
    ids = [d["_id"] for d in batch_docs]

    # Fetch vec_openai_large from arabic-openai-large
    large_resp = es.mget(index="arabic-openai-large",
                         body={"docs": [{"_id": i, "_source": {"includes": ["embedding"]}}
                                        for i in ids]})
    large_map = {}
    for item in large_resp["docs"]:
        if item.get("found"):
            large_map[item["_id"]] = item["_source"].get("embedding")

    # Fetch vec_e5_crosslingual from multilingual-e5
    e5_resp = es.mget(index="multilingual-e5",
                      body={"docs": [{"_id": i, "_source": {"includes": ["embedding"]}}
                                     for i in ids]})
    e5_map = {}
    for item in e5_resp["docs"]:
        if item.get("found"):
            e5_map[item["_id"]] = item["_source"].get("embedding")

    # Build bulk actions
    actions = []
    for d in batch_docs:
        doc = d["doc"]
        doc_id = d["_id"]
        if large_map.get(doc_id):
            doc["vec_openai_large"] = large_map[doc_id]
        if e5_map.get(doc_id):
            doc["vec_e5_crosslingual"] = e5_map[doc_id]
        actions.append({
            "_op_type": "index",
            "_index": TARGET,
            "_id": doc_id,
            "_source": doc,
        })

    ok, errors = bulk(es, actions, chunk_size=len(actions), raise_on_error=False)
    ok_total += ok
    err_total += len(errors)


for hit in es_scan(es, index="arabic-openai",
                   query={"query": {"match_all": {}}},
                   _source_excludes=["clusterIdFinal", "clusterIdV2", "clusterIdV3",
                                     "englishText", "englishURN"],
                   size=BATCH):
    s = hit["_source"]
    emb = s.pop("embedding", None)
    if not emb:
        continue

    doc = {k: v for k, v in s.items() if v not in (None, "", [])}
    doc["vec_openai"] = emb

    batch_docs.append({"_id": hit["_id"], "doc": doc})

    if len(batch_docs) >= BATCH:
        flush(batch_docs)
        processed += len(batch_docs)
        batch_docs = []
        if processed % 10000 == 0:
            print(f"  {processed:,} processed, {ok_total:,} ok, {err_total} errors"
                  f" — {time.time()-t0:.0f}s")

flush(batch_docs)
processed += len(batch_docs)

print(f"\nDone: {processed:,} docs scanned, {ok_total:,} indexed, {err_total} errors"
      f" — {time.time()-t0:.0f}s")

# ── Step 3: Report coverage ───────────────────────────────────────────────────
time.sleep(2)
for field in ["vec_openai", "vec_openai_large", "vec_e5_crosslingual", "vec_e5_arabic"]:
    r = es.count(index=TARGET, query={"exists": {"field": field}})
    print(f"  {field:30s}: {r['count']:,}")
