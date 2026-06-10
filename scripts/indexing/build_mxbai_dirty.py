"""
Creates english-mxbai-dirty: same structure as english-mxbai but
semantic_text embeds hadithText (full text with isnad, HTML-stripped)
instead of englishMatn (clean matn).

Lets us compare clean vs dirty mxbai vectors directly at search time.
Estimated time: 8-12 hours (mxbai inference endpoint is the bottleneck).

Run inside container (background):
    nohup python3 /code/tests/build_mxbai_dirty.py > /tmp/mxbai_dirty.log 2>&1 &

Progress:
    tail -f /tmp/mxbai_dirty.log
"""
import os, re, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

SOURCE_INDEX  = "english-mxbai"
DIRTY_INDEX   = "english-mxbai-dirty"
INFERENCE_ID  = "mxbai-embed-large"
SEMANTIC_FIELD = "semantic_text"
BATCH_SIZE    = 50     # small — each batch waits for mxbai inference
BULK_TIMEOUT  = 300    # seconds; mxbai can be slow on large text

es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=BULK_TIMEOUT)

_HTML = re.compile(r"<[^>]+>")
_WS   = re.compile(r"\s+")

def strip_html(s):
    return _WS.sub(" ", _HTML.sub(" ", s or "")).strip()


# ── Replicate index settings from source ──────────────────────────────────────
print(f"Reading mapping and settings from {SOURCE_INDEX}...")

raw_settings = es.indices.get_settings(index=SOURCE_INDEX)
actual_src   = list(raw_settings.keys())[0]
idx_settings = raw_settings[actual_src]["settings"]["index"]

# Only carry over the fields a new index accepts
settings = {"number_of_shards": 1, "number_of_replicas": 0}
if "analysis" in idx_settings:
    settings["analysis"] = idx_settings["analysis"]

raw_mapping = es.indices.get_mapping(index=SOURCE_INDEX)
props = raw_mapping[list(raw_mapping.keys())[0]]["mappings"]["properties"].copy()

# ── Create dirty index ────────────────────────────────────────────────────────
if es.indices.exists(index=DIRTY_INDEX):
    print(f"  {DIRTY_INDEX} already exists — deleting and rebuilding")
    es.indices.delete(index=DIRTY_INDEX)

es.indices.create(index=DIRTY_INDEX,
                  mappings={"properties": props},
                  settings=settings)
print(f"  Created {DIRTY_INDEX}")

# ── Scan source index ─────────────────────────────────────────────────────────
SOURCE_FIELDS = [
    "hadithText", "englishMatn", "arabicText", "arabicGrade",
    "collection", "hadithNumber", "dupGroup", "isChainRef",
    "matchingArabicURN", "gradeNorm", "grade", "lang", "urn",
]

print(f"Scanning {SOURCE_INDEX}...")
t_scan = time.time()
docs = []
for hit in es_scan(es, index=SOURCE_INDEX, _source=SOURCE_FIELDS,
                   query={"query": {"match_all": {}}}, size=500):
    s   = hit["_source"]
    raw = strip_html(s.get("hadithText") or "")
    if not raw:
        continue
    doc = {k: v for k, v in s.items() if k != SEMANTIC_FIELD}
    doc[SEMANTIC_FIELD] = raw   # embed full hadithText (with isnad)
    doc["_id"] = hit["_id"]
    docs.append(doc)

print(f"  {len(docs):,} docs in {time.time()-t_scan:.0f}s")

# ── Bulk index in small batches ───────────────────────────────────────────────
print(f"Indexing into {DIRTY_INDEX} — ETA ~8-12h ...")
t0 = time.time()
done = errors = 0
n = len(docs)

for i in range(0, n, BATCH_SIZE):
    batch = docs[i:i + BATCH_SIZE]
    actions = [{"_index": DIRTY_INDEX, "_id": d["_id"],
                **{k: v for k, v in d.items() if k != "_id"}}
               for d in batch]
    try:
        ok, errs = es_bulk(es, actions, request_timeout=BULK_TIMEOUT,
                           raise_on_error=False)
        done   += ok
        errors += len(errs)
        if errs:
            print(f"  batch {i//BATCH_SIZE}: {len(errs)} errors — {errs[0]}")
    except Exception as e:
        errors += len(batch)
        print(f"  batch {i//BATCH_SIZE} exception: {e}")

    if done > 0 and done % 1000 < BATCH_SIZE:
        elapsed = time.time() - t0
        rate    = done / elapsed
        eta_h   = (n - done) / rate / 3600
        pct     = done / n * 100
        print(f"  {done:,}/{n:,} ({pct:.1f}%) | {rate:.1f} doc/s | ETA {eta_h:.1f}h | errors={errors}")

elapsed = time.time() - t0
print(f"\nDone: {done:,} indexed, {errors} errors | total {elapsed/3600:.2f}h")
print(f"Index: {DIRTY_INDEX}")
