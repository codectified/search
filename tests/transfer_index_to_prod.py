"""
Transfer english-mxbai from dev ES to prod ES via scroll + bulk,
preserving pre-computed semantic_text inference chunks so Ollama
inference does NOT need to re-run on the t3.medium.

ES accepts pre-populated inference chunks when the inference_id and
model settings already exist on the target instance — no re-embedding.

Prerequisites on PROD before running:
  1. mxbai-embed-large inference endpoint registered (same inference_id)
     POST prod-ES/_inference/text_embedding/mxbai-embed-large  { ... }
  2. english-mxbai index created on prod with correct mapping
     (or let this script create it via reindex — it copies the mapping)

Usage:
    # Set env vars, then:
    python3 tests/transfer_index_to_prod.py

    DEV_ES_HOST   — dev Elasticsearch host  (default: http://172.31.250.10:9200)
    PROD_ES_HOST  — prod Elasticsearch host
    ELASTIC_PASSWORD — shared password (or set DEV_PASS / PROD_PASS separately)

This script runs from outside the container (or inside dev container with
prod ES reachable via VPN/SSH tunnel).
"""
import os, sys, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

SRC_INDEX  = "english-mxbai"
DST_INDEX  = "english-mxbai"
BATCH_SIZE = 100   # smaller batches — semantic_text docs are large
SEMANTIC_FIELD = "semantic_text"

DEV_HOST  = os.environ.get("DEV_ES_HOST",  "http://172.31.250.10:9200")
PROD_HOST = os.environ.get("PROD_ES_HOST")
if not PROD_HOST:
    print("ERROR: PROD_ES_HOST env var not set")
    sys.exit(1)

dev_pass  = os.environ.get("DEV_PASS",  os.environ.get("ELASTIC_PASSWORD", ""))
prod_pass = os.environ.get("PROD_PASS", os.environ.get("ELASTIC_PASSWORD", ""))

dev_es  = Elasticsearch(DEV_HOST,  basic_auth=("elastic", dev_pass),  request_timeout=120)
prod_es = Elasticsearch(PROD_HOST, basic_auth=("elastic", prod_pass), request_timeout=120)

# ── Copy mapping + settings from dev ─────────────────────────────────────────
print(f"Reading mapping from dev {SRC_INDEX}...")
raw_map  = dev_es.indices.get_mapping(index=SRC_INDEX)
actual   = list(raw_map.keys())[0]
mapping  = raw_map[actual]["mappings"]

raw_set  = dev_es.indices.get_settings(index=SRC_INDEX)
idx_set  = raw_set[actual]["settings"]["index"]
settings = {"number_of_shards": 1, "number_of_replicas": 0}
if "analysis" in idx_set:
    settings["analysis"] = idx_set["analysis"]

if prod_es.indices.exists(index=DST_INDEX):
    print(f"  {DST_INDEX} already exists on prod — skipping creation")
else:
    prod_es.indices.create(index=DST_INDEX, mappings=mapping, settings=settings)
    print(f"  Created {DST_INDEX} on prod")

# ── Scroll dev, bulk-write prod ───────────────────────────────────────────────
print(f"\nScrolling dev {SRC_INDEX} → prod {DST_INDEX}...")
t0    = time.time()
done  = errors = 0
total = dev_es.count(index=SRC_INDEX, query={"match_all": {}})["count"]
print(f"  {total:,} docs to transfer")

batch = []
for hit in es_scan(dev_es, index=SRC_INDEX,
                   query={"query": {"match_all": {}}},
                   _source=True, size=BATCH_SIZE):
    doc = {
        "_index": DST_INDEX,
        "_id":    hit["_id"],
        **hit["_source"],    # includes semantic_text with pre-computed chunks
    }
    batch.append(doc)

    if len(batch) >= BATCH_SIZE:
        ok, errs = es_bulk(prod_es, batch, raise_on_error=False, raise_on_exception=False)
        done   += ok
        errors += len(errs) if errs else 0
        batch   = []

        if done % 5000 < BATCH_SIZE:
            elapsed = time.time() - t0
            rate    = done / elapsed
            eta_m   = (total - done) / rate / 60
            pct     = done / total * 100
            print(f"  {done:,}/{total:,} ({pct:.1f}%) | {rate:.0f} doc/s | ETA {eta_m:.1f}min | errors={errors}")

if batch:
    ok, errs = es_bulk(prod_es, batch, raise_on_error=False, raise_on_exception=False)
    done   += ok
    errors += len(errs) if errs else 0

elapsed = time.time() - t0
print(f"\nDone: {done:,} transferred, {errors} errors | {elapsed/60:.1f} min")
print(f"\nNext steps:")
print(f"  1. Verify on prod: GET {PROD_HOST}/{DST_INDEX}/_count")
print(f"  2. Create alias if needed: POST {PROD_HOST}/_aliases")
print(f"  3. Run tests/backfill_prod_fields.py to add gradeNorm + englishMatn")
