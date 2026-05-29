"""
Writes clusterIdFinal (int) from english_cluster_map.json to the english-openai ES index.

english-openai uses a plain dense_vector field (no inference), so bulk updates work fine.

Run inside container:
    docker exec search-web-1 python3 /code/tests/update_english_openai_clusters.py
"""
import os, json, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

INDEX      = "english-openai"
MAP_FILE   = "/code/english_cluster_map.json"
BATCH_SIZE = 1000

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Ensure field exists in mapping ─────────────────────────────────────────────
es.indices.put_mapping(index=INDEX, body={"properties": {"clusterIdFinal": {"type": "integer"}}})
print("Mapping: clusterIdFinal field ensured")

# ── Load cluster map {englishURN_str: cluster_id} ─────────────────────────────
with open(MAP_FILE) as f:
    cluster_map = json.load(f)
print(f"Loaded {len(cluster_map):,} entries from {MAP_FILE}")

urns = list(cluster_map.keys())
t0   = time.time()
updated = errors = 0

for i in range(0, len(urns), BATCH_SIZE):
    batch = urns[i : i + BATCH_SIZE]
    actions = [
        {
            "_op_type": "update",
            "_index":   INDEX,
            "_id":      urn_str,          # english-openai _id = raw URN string
            "doc":      {"clusterIdFinal": cluster_map[urn_str]},
        }
        for urn_str in batch
    ]
    ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
    updated += ok
    errors  += len(errs) if errs else 0

    if (i // BATCH_SIZE) % 10 == 0:
        print(f"  {updated:,}/{len(urns):,} ok={updated} err={errors}")

es.indices.refresh(index=INDEX)
elapsed = time.time() - t0
print(f"\nDone in {elapsed:.0f}s — updated: {updated:,} | errors: {errors}")

# Quick verify
count = es.count(index=INDEX, body={"query": {"exists": {"field": "clusterIdFinal"}}})["count"]
print(f"Verified — clusterIdFinal set on: {count:,} docs")
