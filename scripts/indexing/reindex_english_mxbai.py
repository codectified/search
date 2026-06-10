"""
Full reindex of english-mxbai using extracted englishMatn as the semantic_text
value (instead of full hadithText). ES Ollama inference pipeline re-embeds all docs.

Preserves all metadata: isChainRef, dupGroup, urn, collection, hadithNumber, etc.
Deletes and recreates the index — all prior embeddings are replaced.

Run inside container:
    docker exec search-web-1 python3 /code/tests/reindex_english_mxbai.py
"""
import os, json, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=300,
)

OLD_INDEX  = "english-mxbai"
MAP_FILE   = "/code/english_matn_map.json"
BATCH_SIZE = 200   # smaller batches — each triggers Ollama inference

# ── Load extraction map ────────────────────────────────────────────────────────
print(f"Loading {MAP_FILE}...")
with open(MAP_FILE, encoding="utf-8") as f:
    matn_map = json.load(f)
print(f"  {len(matn_map):,} entries")

# ── Fetch current index config (mapping + settings) ───────────────────────────
print("Fetching current index config...")
old_info     = es.indices.get(index=OLD_INDEX)
old_alias    = list(old_info.keys())[0]   # resolves alias to real index name
old_settings = old_info[old_alias]["settings"]["index"]
old_mapping  = old_info[old_alias]["mappings"]

# ── Fetch all current docs (to preserve metadata) ────────────────────────────
print("Fetching all docs from current index (this may take a minute)...")
t0   = time.time()
docs = []
EXCLUDE_FROM_SOURCE = ["semantic_text"]   # will be replaced with clean matn

for hit in es_scan(
    es,
    index=OLD_INDEX,
    query={"query": {"match_all": {}}},
    _source={"excludes": EXCLUDE_FROM_SOURCE},
    size=500,
):
    docs.append({"_id": hit["_id"], "_source": hit["_source"]})

print(f"  {len(docs):,} docs fetched in {time.time()-t0:.0f}s")

# ── Build new index name (swap alias) ─────────────────────────────────────────
import hashlib, datetime
suffix   = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
new_name = f"english-mxbai-{suffix}"
print(f"New index name: {new_name}")

# ── Get inference endpoint id from old mapping ────────────────────────────────
sem_props  = old_mapping.get("properties", {}).get("semantic_text", {})
inf_id     = (sem_props.get("inference_id")
              or sem_props.get("model_settings", {}).get("inference_id")
              or "mxbai-embed-large")
print(f"Inference endpoint: {inf_id}")

# ── Create new index with same structure ──────────────────────────────────────
new_settings = {
    "number_of_shards":   old_settings.get("number_of_shards", 1),
    "number_of_replicas": old_settings.get("number_of_replicas", 0),
}
if "analysis" in old_settings:
    new_settings["analysis"] = old_settings["analysis"]
new_mapping = old_mapping.copy()

es.indices.create(index=new_name, body={
    "settings": new_settings,
    "mappings": new_mapping,
})
print(f"Created index: {new_name}")

# ── Index docs with new semantic_text = englishMatn ───────────────────────────
print("Indexing with clean matn (Ollama will embed each batch)...")
t1       = time.time()
indexed  = errors = 0

def make_actions(batch):
    for item in batch:
        doc_id = item["_id"]
        source = item["_source"]
        urn    = str(source.get("urn", doc_id))

        entry  = matn_map.get(urn, {})
        matn   = (entry.get("matn") or source.get("hadithText") or "").strip()
        if not matn:
            matn = source.get("hadithText", ".")

        yield {
            "_op_type": "index",
            "_index":   new_name,
            "_id":      doc_id,
            "_source":  {
                **source,
                "englishMatn":  matn,          # stored for reference
                "semantic_text": matn[:8000],   # triggers Ollama inference
            },
        }

for i in range(0, len(docs), BATCH_SIZE):
    batch = docs[i:i + BATCH_SIZE]
    try:
        ok, errs = es_bulk(
            es, make_actions(batch),
            raise_on_error=False,
            raise_on_exception=False,
            request_timeout=300,
            chunk_size=BATCH_SIZE,
        )
        indexed += ok
        errors  += len(errs) if errs else 0
        if errs:
            for e in errs[:2]:
                print(f"  BULK ERR: {e}")
    except Exception as e:
        print(f"  BATCH ERROR i={i}: {e}")
        errors += 1

    if (i // BATCH_SIZE) % 10 == 0:
        elapsed = time.time() - t1
        rate    = indexed / elapsed if elapsed > 0 else 0
        rem     = (len(docs) - indexed) / rate if rate > 0 else 0
        print(f"  [{indexed:,}/{len(docs):,}] {rate:.1f}/s | ~{rem/60:.1f} min | err={errors}")

es.indices.refresh(index=new_name)
final_count = es.count(index=new_name)["count"]
print(f"\nIndexed: {indexed:,} | errors: {errors} | verified count: {final_count:,}")

# ── Swap alias ────────────────────────────────────────────────────────────────
# Check if OLD_INDEX is an alias or real index
aliases = es.indices.get_alias(name=OLD_INDEX, ignore_unavailable=True)
if aliases:
    # OLD_INDEX is an alias — update it
    real_old = list(aliases.keys())[0]
    es.indices.update_aliases(body={
        "actions": [
            {"remove": {"index": real_old, "alias": OLD_INDEX}},
            {"add":    {"index": new_name,  "alias": OLD_INDEX}},
        ]
    })
    print(f"Alias '{OLD_INDEX}' → {new_name}")
    # Delete old index
    es.indices.delete(index=real_old)
    print(f"Deleted old index: {real_old}")
else:
    # OLD_INDEX is a real index — delete it and create alias
    es.indices.delete(index=OLD_INDEX)
    es.indices.put_alias(index=new_name, name=OLD_INDEX)
    print(f"Replaced real index '{OLD_INDEX}' with alias → {new_name}")

elapsed = time.time() - t0
print(f"\nTotal time: {elapsed:.0f}s ({elapsed/60:.1f} min)")
print(f"New index '{new_name}' now live as '{OLD_INDEX}'")
