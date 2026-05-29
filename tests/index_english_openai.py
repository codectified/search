"""
Builds the 'english-openai' ES index from english_openai_embeddings.json.

Fields:
  embedding    — 1536-dim dense_vector (OpenAI text-embedding-3-small on English text)
  isChainRef   — boolean: True for chain-variant notes with no real matn content
  dupGroup     — integer: shared ID for near-duplicate hadiths (same matn, diff chain)
                 0 = not in any duplicate group

Run inside container:
    docker exec search-web-1 python3 /code/tests/index_english_openai.py
"""
import os, json, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, scan as es_scan

INDEX      = "english-openai"
BATCH_SIZE = 150
SLEEP      = 0.4
EMB_FILE   = "/code/english_openai_embeddings.json"

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Create index ───────────────────────────────────────────────────────────────
if not es.indices.exists(index=INDEX):
    es.indices.create(index=INDEX, body={
        "settings": {
            "refresh_interval": "-1",
            "number_of_replicas": 0,
        },
        "mappings": {
            "properties": {
                "englishURN":   {"type": "integer"},
                "arabicURN":    {"type": "integer"},
                "collection":   {"type": "keyword"},
                "hadithNumber": {"type": "keyword"},
                "englishText":  {"type": "text"},
                "gradeEnglish": {"type": "keyword"},
                "gradeArabic":  {"type": "keyword"},
                "isChainRef":   {"type": "boolean"},
                "dupGroup":     {"type": "integer"},
                "embedding": {
                    "type": "dense_vector",
                    "dims": 1536,
                    "index": True,
                    "similarity": "cosine",
                    "index_options": {"type": "int8_hnsw", "m": 16, "ef_construction": 100},
                },
            }
        },
    })
    print(f"Created index '{INDEX}'")
else:
    print(f"Index '{INDEX}' already exists — resuming")

# ── Find already-indexed URNs ──────────────────────────────────────────────────
print("Scanning existing docs...")
existing = set()
for hit in es_scan(es, index=INDEX, query={"_source": False}):
    existing.add(hit["_id"])
print(f"  Already indexed: {len(existing):,}")

# ── Load embeddings ────────────────────────────────────────────────────────────
print(f"Loading {EMB_FILE}...")
with open(EMB_FILE) as f:
    data = json.load(f)
print(f"  {len(data):,} records")

urns_to_index = [u for u in data if u not in existing]
print(f"  To index: {len(urns_to_index):,}")

# ── Bulk index ─────────────────────────────────────────────────────────────────
indexed = errors = 0
t0 = time.time()

for i in range(0, len(urns_to_index), BATCH_SIZE):
    batch_urns = urns_to_index[i : i + BATCH_SIZE]
    actions = []
    for urn in batch_urns:
        rec = data[urn]
        actions.append({
            "_id": urn,
            "_source": {
                "englishURN":   rec["englishURN"],
                "arabicURN":    rec["arabicURN"],
                "collection":   rec["collection"],
                "hadithNumber": rec["hadithNumber"],
                "englishText":  rec["englishText"],
                "gradeEnglish": rec["gradeEnglish"],
                "gradeArabic":  rec["gradeArabic"],
                "isChainRef":   rec["isChainRef"],
                "dupGroup":     0,
                "embedding":    rec["vector"],
            },
        })

    ok, errs = bulk(es, actions, index=INDEX,
                    request_timeout=60, raise_on_error=False, raise_on_exception=False)
    indexed += ok
    errors  += len(errs)

    done = i + len(batch_urns)
    rate = done / max(time.time() - t0, 1)
    eta  = (len(urns_to_index) - done) / rate if rate > 0 else 0
    print(f"  {done:,}/{len(urns_to_index):,} | errors: {errors} | ETA {eta/60:.1f}m", end="\r")
    time.sleep(SLEEP)

# ── Restore refresh ────────────────────────────────────────────────────────────
es.indices.put_settings(index=INDEX, body={"refresh_interval": "1s"})
es.indices.refresh(index=INDEX)

elapsed = time.time() - t0
count = es.count(index=INDEX)["count"]
print(f"\n\nDone in {elapsed:.0f}s | Indexed: {indexed:,} | Errors: {errors} | Total in index: {count:,}")
print(f"Chain-refs flagged: {sum(1 for v in data.values() if v.get('isChainRef'))}")
