"""
Updates existing 'arabic-openai' ES docs with:
  - clusterIdV2: from arabic_cluster_map.json (all 131k docs)
  - arabicMatn:  improved extraction for 30k untagged Sunan hadiths
                 from matn_boundaries.json

Does NOT re-index vectors — just patches existing documents.

Run inside container:
    docker exec search-web-1 python3 /code/tests/update_arabic_openai.py
"""
import os, json, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

INDEX = "arabic-openai"
BATCH_SIZE = 500
SLEEP_BETWEEN = 0.3

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Add clusterIdV2 to mapping (safe to run even if field exists) ──────────────
es.indices.put_mapping(index=INDEX, body={
    "properties": {
        "clusterIdV2": {"type": "integer"},
    }
})
print("Mapping updated: clusterIdV2 field added")

# ── Load cluster map {arabicURN_str: cluster_index} ───────────────────────────
print("Loading cluster map...")
with open("/code/arabic_cluster_map.json") as f:
    cluster_map = json.load(f)  # keys are arabicURN strings
print(f"  {len(cluster_map):,} entries")

# ── Load improved matn boundaries {arabicURN_str: {matn, collection}} ─────────
print("Loading matn boundaries...")
with open("/code/matn_boundaries.json", encoding="utf-8") as f:
    matn_boundaries = json.load(f)
print(f"  {len(matn_boundaries):,} improved matn extractions")

# ── Build update actions ───────────────────────────────────────────────────────
print("Building update actions...")
all_urns = list(cluster_map.keys())
print(f"  {len(all_urns):,} docs to update")

t0 = time.time()
updated = errors = 0

for i in range(0, len(all_urns), BATCH_SIZE):
    batch_urns = all_urns[i:i + BATCH_SIZE]
    actions = []
    for urn_str in batch_urns:
        doc = {"clusterIdV2": cluster_map[urn_str]}
        if urn_str in matn_boundaries:
            doc["arabicMatn"] = matn_boundaries[urn_str]["matn"]
        actions.append({
            "_op_type": "update",
            "_index": INDEX,
            "_id": f"arabic:{urn_str}",
            "doc": doc,
        })

    try:
        ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        updated += ok
        if errs:
            errors += len(errs)
    except Exception as e:
        print(f"  ERROR batch {i//BATCH_SIZE}: {e}")
        errors += 1

    time.sleep(SLEEP_BETWEEN)

    if (i // BATCH_SIZE) % 20 == 0:
        elapsed = time.time() - t0
        rate = updated / elapsed if elapsed > 0 else 0
        remaining = (len(all_urns) - updated) / rate if rate > 0 else 0
        print(f"  [{updated:,}/{len(all_urns):,}] {rate:.0f} docs/s | ~{remaining/60:.1f} min remaining | {errors} errors")

es.indices.refresh(index=INDEX)
elapsed = time.time() - t0
print(f"\nDone: {updated:,} updated, {errors} errors, {elapsed:.0f}s")
print(f"  clusterIdV2 set on all docs")
print(f"  arabicMatn improved on {len(matn_boundaries):,} untagged Sunan hadiths")
