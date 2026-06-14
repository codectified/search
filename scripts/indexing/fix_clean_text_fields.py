"""
Fix arabicMatnClean and arabicTextClean in arabic-research:
replace markup tags with a space (not empty string) so words on either
side of a tag boundary stay separated.

Safe to run while embed_e5_clean.py is running — only updates text fields,
does not touch vec_e5_matn or vec_e5_full.

Run inside container:
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 \\
        search-web-1 python3 /code/scripts/indexing/fix_clean_text_fields.py
"""
import os, re, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
INDEX   = "arabic-research"
CHUNK   = 500

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW), request_timeout=120)

TAG_RE = re.compile(r'\[/?[a-zA-Z][^\]]*\]')

def strip_markup(text):
    if not text:
        return ""
    cleaned = TAG_RE.sub(' ', text)          # space, not empty string
    return re.sub(r'\s+', ' ', cleaned).strip()


t0 = time.time()
ok_total = err_total = 0

def generate(hits):
    for hit in hits:
        s = hit["_source"]
        arabic_text = s.get("arabicText") or ""
        arabic_matn = s.get("arabicMatn") or ""
        had_matn_tag = bool(s.get("hadMatnTag", False))
        yield {
            "_op_type": "update",
            "_index": INDEX,
            "_id": hit["_id"],
            "doc": {
                "arabicTextClean": strip_markup(arabic_text),
                "arabicMatnClean": strip_markup(arabic_matn) if had_matn_tag else None,
            }
        }

hits = es_scan(es, index=INDEX,
               query={"query": {"match_all": {}}},
               _source=["arabicText", "arabicMatn", "hadMatnTag"],
               size=CHUNK)

ok, errors = bulk(es, generate(hits), chunk_size=CHUNK,
                  raise_on_error=False, request_timeout=120)
ok_total += ok
err_total += len(errors)

print(f"Done: {ok_total:,} updated, {err_total} errors — {time.time()-t0:.0f}s")
