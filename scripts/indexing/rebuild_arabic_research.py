"""
Rebuild arabic-research index from scratch with clean text fields.

Drops the old index (all buggy embeddings and cluster IDs gone),
creates a fresh one, and copies hadith data from arabic-openai while
computing two clean text fields on the fly:

  arabicMatnClean  — arabicMatn with all markup stripped, only for
                     docs where hadMatnTag=True (otherwise null)
  arabicTextClean  — arabicText with all markup stripped (every doc)

Vector fields (vec_e5_matn, vec_e5_full) are defined in the mapping
but left empty; run embed_e5_clean.py afterward to fill them.

Run inside container:
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 \\
        search-web-1 python3 /code/scripts/indexing/rebuild_arabic_research.py
"""
import os, re, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
SOURCE  = "arabic-openai"
TARGET  = "arabic-research"
CHUNK   = 500

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW), request_timeout=120)

TAG_RE = re.compile(r'\[/?[a-zA-Z][^\]]*\]')

def strip_markup(text):
    if not text:
        return ""
    cleaned = TAG_RE.sub(' ', text)          # space, not empty — preserves word boundaries
    return re.sub(r'\s+', ' ', cleaned).strip()


MAPPING = {
    "mappings": {
        "properties": {
            # ── Identifiers ────────────────────────────────────────────
            "arabicURN":       {"type": "long"},
            "englishURN":      {"type": "long"},
            "collection":      {"type": "keyword"},
            "hadithNumber":    {"type": "keyword"},
            # ── Grades ─────────────────────────────────────────────────
            "gradeNorm":       {"type": "keyword"},
            "gradeArabic":     {"type": "keyword"},
            "gradeEnglish":    {"type": "keyword"},
            # ── Flags ──────────────────────────────────────────────────
            "hadMatnTag":      {"type": "boolean"},
            "isChainRef":      {"type": "boolean"},
            # ── Original text (with markup) ────────────────────────────
            "arabicText":      {"type": "text", "index": False},
            "arabicMatn":      {"type": "text", "index": False},
            "englishText":     {"type": "text", "index": False},
            # ── Clean text (markup stripped) ───────────────────────────
            "arabicMatnClean": {"type": "text", "index": False},
            "arabicTextClean": {"type": "text", "index": False},
            # ── Vectors ────────────────────────────────────────────────
            "vec_e5_matn": {
                "type": "dense_vector", "dims": 1024,
                "index": True, "similarity": "cosine"
            },
            "vec_e5_full": {
                "type": "dense_vector", "dims": 1024,
                "index": True, "similarity": "cosine"
            },
        }
    },
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "30s",
    }
}

# ── Delete and recreate ────────────────────────────────────────────────────────
print(f"Deleting {TARGET}...")
if es.indices.exists(index=TARGET):
    es.indices.delete(index=TARGET)
    print("  Deleted.")

print(f"Creating {TARGET}...")
es.indices.create(index=TARGET, body=MAPPING)
print("  Created.")

# ── Copy and clean ─────────────────────────────────────────────────────────────
print(f"\nCopying from {SOURCE}...")
t0 = time.time()
ok_total = err_total = 0

SOURCE_FIELDS = [
    "arabicURN", "englishURN", "collection", "hadithNumber",
    "gradeNorm", "gradeArabic", "gradeEnglish",
    "hadMatnTag", "isChainRef",
    "arabicText", "arabicMatn", "englishText",
]

def generate(hits):
    for hit in hits:
        s = hit["_source"]
        arabic_text = s.get("arabicText") or ""
        arabic_matn = s.get("arabicMatn") or ""
        had_matn_tag = bool(s.get("hadMatnTag", False))

        doc = {k: s[k] for k in SOURCE_FIELDS if k in s}
        doc["arabicTextClean"] = strip_markup(arabic_text)
        doc["arabicMatnClean"] = strip_markup(arabic_matn) if had_matn_tag else None

        yield {
            "_op_type": "index",
            "_index": TARGET,
            "_id": hit["_id"],
            "_source": doc,
        }

hits = es_scan(es, index=SOURCE,
               query={"query": {"match_all": {}}},
               _source=SOURCE_FIELDS, size=CHUNK)

ok, errors = bulk(es, generate(hits), chunk_size=CHUNK,
                  raise_on_error=False, request_timeout=120)
ok_total += ok
err_total += len(errors)

if errors:
    print(f"  Sample errors: {errors[:3]}")

elapsed = time.time() - t0
print(f"\nDone: {ok_total:,} indexed, {err_total} errors — {elapsed:.0f}s")

# Refresh
es.indices.refresh(index=TARGET)
count = es.count(index=TARGET)["count"]
print(f"Total docs in {TARGET}: {count:,}")
print("\nNext: run embed_e5_clean.py to add vec_e5_matn and vec_e5_full")
