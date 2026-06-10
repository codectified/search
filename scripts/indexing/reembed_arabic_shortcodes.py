"""
Re-embeds Arabic docs whose arabicMatn contains shortcode tags
([quran...], [narrator...], etc.) that pollute the stored vectors.

Strips shortcodes, re-calls OpenAI embedding API, updates the embedding
field in place for affected docs in arabic-openai and arabic-openai-large.

Affected docs: ~7,558 (5.7% of 131,728)

Run inside container:
    python3 /code/tests/reembed_arabic_shortcodes.py
    python3 /code/tests/reembed_arabic_shortcodes.py arabic-openai-large
"""
import os, re, sys, time
import numpy as np
from openai import OpenAI
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

TARGET = sys.argv[1] if len(sys.argv) > 1 else "arabic-openai"
BATCH  = 200

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
es     = Elasticsearch("http://172.31.250.10:9200",
           basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=60)

MODEL_MAP = {
    "arabic-openai":       "text-embedding-3-small",
    "arabic-openai-large": "text-embedding-3-large",
}
EMBED_MODEL = MODEL_MAP.get(TARGET)
if not EMBED_MODEL:
    print(f"Unknown index: {TARGET}. Expected: {list(MODEL_MAP)}")
    sys.exit(1)

# Shortcodes present in arabicMatn: [quran ...], [narrator ...], [/narrator], etc.
SHORTCODE = re.compile(r'\[/?(?:quran|narrator|prematn|matn|footnote|hadith)[^\]]*\]')
_WS       = re.compile(r'\s+')

def clean(text):
    return _WS.sub(' ', SHORTCODE.sub(' ', text or '')).strip()

def has_shortcode(text):
    return bool(SHORTCODE.search(text or ''))

# ── Scan for affected docs ────────────────────────────────────────────────────
print(f"Scanning {TARGET} for shortcode-contaminated arabicMatn...")
t0 = time.time()

affected = []
for hit in es_scan(es, index=TARGET,
        _source=["arabicMatn"],
        query={"query": {"match_all": {}}}, size=500):
    am = hit["_source"].get("arabicMatn") or ""
    if has_shortcode(am):
        affected.append((hit["_id"], clean(am)))

print(f"  {len(affected):,} docs with shortcodes (scan: {time.time()-t0:.0f}s)")
if not affected:
    print("Nothing to do.")
    sys.exit(0)

# ── Re-embed and update ────────────────────────────────────────────────────────
print(f"Re-embedding with {EMBED_MODEL} and updating {TARGET}...")
t0    = time.time()
done  = api_err = es_err = 0

for i in range(0, len(affected), BATCH):
    batch     = affected[i:i + BATCH]
    doc_ids   = [b[0] for b in batch]
    texts     = [b[1] for b in batch]

    try:
        resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
        vecs = [r.embedding for r in resp.data]
    except Exception as e:
        print(f"  API error batch {i//BATCH}: {e}")
        api_err += 1
        time.sleep(5)
        continue

    actions = [
        {"_op_type": "update", "_index": TARGET, "_id": doc_id,
         "doc": {"embedding": vec}}
        for doc_id, vec in zip(doc_ids, vecs)
    ]
    try:
        ok, errs = es_bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        done   += ok
        es_err += len(errs) if errs else 0
    except Exception as e:
        print(f"  ES error batch {i//BATCH}: {e}")
        es_err += 1

    if done % 1000 < BATCH or i + BATCH >= len(affected):
        elapsed = time.time() - t0
        rate    = done / elapsed if elapsed > 0 else 0
        print(f"  {done:,}/{len(affected):,} | {rate:.0f} doc/s | api_err={api_err} es_err={es_err}")

print(f"\nDone: {done:,} re-embedded | api_err={api_err} es_err={es_err} | {time.time()-t0:.0f}s")
