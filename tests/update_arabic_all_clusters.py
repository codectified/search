"""
Writes clusterIdFinal (int) from arabic_all_cluster_map.json to arabic-openai ES index.
Uses individual es.update() calls (bulk blocked by inference-field index).

Run inside container:
    docker exec search-web-1 python3 /code/tests/update_arabic_all_clusters.py
"""
import os, json, time
from elasticsearch import Elasticsearch

INDEX    = "arabic-openai"
MAP_FILE = "/code/arabic_all_cluster_map.json"

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

es.indices.put_mapping(index=INDEX, body={"properties": {"clusterIdFinal": {"type": "integer"}}})
print("Mapping: clusterIdFinal field ensured")

with open(MAP_FILE) as f:
    cluster_map = json.load(f)
print(f"Loaded {len(cluster_map):,} entries from {MAP_FILE}")

t0      = time.time()
updated = errors = 0

for i, (urn_str, cluster_id) in enumerate(cluster_map.items()):
    doc_id = f"arabic:{urn_str}"
    try:
        es.update(index=INDEX, id=doc_id, body={"doc": {"clusterIdFinal": cluster_id}})
        updated += 1
    except Exception as e:
        errors += 1
        if errors <= 5:
            print(f"  ERROR {doc_id}: {e}")

    if (i + 1) % 10000 == 0:
        print(f"  {i+1:,}/{len(cluster_map):,} ok={updated} err={errors}")

es.indices.refresh(index=INDEX)
elapsed = time.time() - t0
print(f"\nDone in {elapsed:.0f}s — updated: {updated:,} | errors: {errors}")

count = es.count(index=INDEX, body={"query": {"exists": {"field": "clusterIdFinal"}}})["count"]
print(f"Verified — clusterIdFinal set on: {count:,} docs")
