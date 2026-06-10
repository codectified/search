"""
Writes clusterIdFinal (int) from mxbai_cluster_map.json to the english-mxbai ES index.

Note: english-mxbai has semantic_text inference fields, so bulk updates are blocked.
Must use individual es.update() calls (same workaround as the isChainRef/dupGroup writes).

Run inside container:
    docker exec search-web-1 python3 /code/tests/update_mxbai_clusters.py
"""
import os, json, time
from elasticsearch import Elasticsearch

INDEX    = "english-mxbai"
MAP_FILE = "/code/mxbai_cluster_map.json"

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Ensure mapping has the field ───────────────────────────────────────────────
es.indices.put_mapping(index=INDEX, body={"properties": {"clusterIdFinal": {"type": "integer"}}})
print("Mapping: clusterIdFinal field ensured")

# ── Load cluster map {englishURN_str: cluster_id} ─────────────────────────────
with open(MAP_FILE) as f:
    cluster_map = json.load(f)
print(f"Loaded {len(cluster_map):,} entries from {MAP_FILE}")

# ── Update one doc at a time (bulk blocked on inference-field indexes) ─────────
urns    = list(cluster_map.keys())
t0      = time.time()
updated = errors = 0
REPORT_EVERY = 500

for i, urn_str in enumerate(urns):
    doc_id = f"en:{urn_str}"   # english-mxbai _id format
    try:
        es.update(index=INDEX, id=doc_id, body={"doc": {"clusterIdFinal": cluster_map[urn_str]}})
        updated += 1
    except Exception as e:
        errors += 1
        if errors <= 5:
            print(f"  ERROR {doc_id}: {e}")

    if (i + 1) % REPORT_EVERY == 0:
        print(f"  {i+1:,}/{len(urns):,} ok={updated} err={errors}")

es.indices.refresh(index=INDEX)
elapsed = time.time() - t0
print(f"\nDone in {elapsed:.0f}s — updated: {updated:,} | errors: {errors}")

count = es.count(index=INDEX, body={"query": {"exists": {"field": "clusterIdFinal"}}})["count"]
print(f"Verified — clusterIdFinal set on: {count:,} docs")
