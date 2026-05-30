"""
Indexes english-openai-large and arabic-openai-large using text-embedding-3-large
(3072-dim). Mirrors the existing english-openai / arabic-openai indexes but with
the large model.

english-openai-large: 48,703 hadiths embedded on englishMatn
arabic-openai-large:  131,728 hadiths embedded on arabicMatn

Run inside container:
    docker exec search-web-1 python3 /code/tests/index_openai_large.py

Cost: ~$0.60 total (English ~$0.20, Arabic ~$0.40)
"""
import os, json, time
import numpy as np
from openai import OpenAI
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=60)

MODEL      = "text-embedding-3-large"
DIM        = 3072
BATCH_SIZE = 200
MAP_FILE   = "/code/english_matn_map.json"

ENGLISH_SRC   = "english-openai"      # copy metadata from here
ARABIC_SRC    = "arabic-openai"       # copy metadata from here
ENGLISH_INDEX = "english-openai-large"
ARABIC_INDEX  = "arabic-openai-large"

MAPPING = {
    "properties": {
        "embedding":    {"type": "dense_vector", "dims": DIM, "index": True, "similarity": "cosine"},
        "collection":   {"type": "keyword"},
        "hadithNumber": {"type": "keyword"},
        "urn":          {"type": "long"},
        "isChainRef":   {"type": "boolean"},
        "dupGroup":     {"type": "long"},
        "clusterIdLarge": {"type": "integer"},
    }
}

SETTINGS = {"number_of_shards": 1, "number_of_replicas": 0}


def create_index(name):
    if es.indices.exists(index=name):
        print(f"  Index {name} already exists — skipping creation")
        return
    es.indices.create(index=name, body={"settings": SETTINGS, "mappings": MAPPING})
    print(f"  Created index: {name}")


def embed_batch(texts):
    resp = client.embeddings.create(model=MODEL, input=texts)
    return [r.embedding for r in resp.data]


def index_english():
    print("\n=== english-openai-large ===")
    print(f"Loading {MAP_FILE}...")
    with open(MAP_FILE, encoding="utf-8") as f:
        matn_map = json.load(f)
    print(f"  {len(matn_map):,} entries")

    create_index(ENGLISH_INDEX)

    # Check how many already indexed
    done_count = es.count(index=ENGLISH_INDEX)["count"]
    if done_count > 0:
        print(f"  {done_count:,} already indexed")
        # Build done set from existing docs
        done_ids = set()
        for hit in es_scan(es, index=ENGLISH_INDEX,
                query={"query": {"match_all": {}}}, _source=False, size=500):
            done_ids.add(hit["_id"])
    else:
        done_ids = set()

    # Fetch all English hadiths with their metadata
    print("  Fetching English hadiths from source index...")
    todo = []
    for hit in es_scan(es, index=ENGLISH_SRC,
            query={"query": {"match_all": {}}},
            _source={"excludes": ["embedding"]}, size=500):
        doc_id = hit["_id"]
        if doc_id in done_ids:
            continue
        s = hit["_source"]
        urn = str(s.get("urn", ""))
        entry = matn_map.get(urn, {})
        text = (entry.get("matn") or s.get("hadithText") or s.get("englishMatn") or ".").strip()
        todo.append((doc_id, text[:8000], s))

    print(f"  {len(todo):,} to embed")
    if not todo:
        print("  Nothing to do")
        return

    t0 = time.time()
    indexed = api_errs = es_errs = 0

    for i in range(0, len(todo), BATCH_SIZE):
        batch = todo[i:i + BATCH_SIZE]
        texts = [b[1] for b in batch]
        try:
            vecs = embed_batch(texts)
        except Exception as e:
            print(f"  API error batch {i//BATCH_SIZE}: {e}")
            api_errs += 1
            time.sleep(5)
            continue

        actions = []
        for j, (doc_id, _, src) in enumerate(batch):
            actions.append({
                "_op_type": "index",
                "_index":   ENGLISH_INDEX,
                "_id":      doc_id,
                "_source":  {
                    **{k: src[k] for k in ["collection","hadithNumber","urn","isChainRef","dupGroup",
                                           "englishMatn","hadithText"] if k in src},
                    "embedding": vecs[j],
                },
            })

        try:
            ok, errs = es_bulk(es, actions, raise_on_error=False, raise_on_exception=False)
            indexed += ok
            es_errs += len(errs) if errs else 0
        except Exception as e:
            print(f"  ES error batch {i//BATCH_SIZE}: {e}")
            es_errs += 1

        if (i // BATCH_SIZE) % 20 == 0:
            el = time.time() - t0
            rate = indexed / el if el > 0 else 0
            rem  = (len(todo) - indexed) / rate / 60 if rate > 0 else 0
            print(f"  [{indexed:,}/{len(todo):,}] {rate:.0f}/s | ~{rem:.1f} min | api_err={api_errs} es_err={es_errs}")

    es.indices.refresh(index=ENGLISH_INDEX)
    print(f"  Done: {indexed:,} | api_err={api_errs} | es_err={es_errs}")
    print(f"  Verified count: {es.count(index=ENGLISH_INDEX)['count']:,}")


def index_arabic():
    print("\n=== arabic-openai-large ===")
    create_index(ARABIC_INDEX)

    done_count = es.count(index=ARABIC_INDEX)["count"]
    if done_count > 0:
        done_ids = set()
        for hit in es_scan(es, index=ARABIC_INDEX,
                query={"query": {"match_all": {}}}, _source=False, size=500):
            done_ids.add(hit["_id"])
        print(f"  {len(done_ids):,} already indexed")
    else:
        done_ids = set()

    print("  Fetching Arabic hadiths from source index...")
    todo = []
    for hit in es_scan(es, index=ARABIC_SRC,
            query={"query": {"match_all": {}}},
            _source={"excludes": ["embedding"]}, size=500):
        doc_id = hit["_id"]
        if doc_id in done_ids:
            continue
        s = hit["_source"]
        text = (s.get("arabicMatn") or s.get("arabicText") or ".").strip()
        todo.append((doc_id, text[:8000], s))

    print(f"  {len(todo):,} to embed")
    if not todo:
        print("  Nothing to do")
        return

    t0 = time.time()
    indexed = api_errs = es_errs = 0

    for i in range(0, len(todo), BATCH_SIZE):
        batch = todo[i:i + BATCH_SIZE]
        texts = [b[1] for b in batch]
        try:
            vecs = embed_batch(texts)
        except Exception as e:
            print(f"  API error batch {i//BATCH_SIZE}: {e}")
            api_errs += 1
            time.sleep(5)
            continue

        actions = []
        for j, (doc_id, _, src) in enumerate(batch):
            actions.append({
                "_op_type": "index",
                "_index":   ARABIC_INDEX,
                "_id":      doc_id,
                "_source":  {
                    **{k: src[k] for k in ["collection","hadithNumber","urn","isChainRef","dupGroup",
                                           "arabicMatn","arabicText","englishText","englishURN",
                                           "hadMatnTag"] if k in src},
                    "embedding": vecs[j],
                },
            })

        try:
            ok, errs = es_bulk(es, actions, raise_on_error=False, raise_on_exception=False)
            indexed += ok
            es_errs += len(errs) if errs else 0
        except Exception as e:
            print(f"  ES error batch {i//BATCH_SIZE}: {e}")
            es_errs += 1

        if (i // BATCH_SIZE) % 20 == 0:
            el = time.time() - t0
            rate = indexed / el if el > 0 else 0
            rem  = (len(todo) - indexed) / rate / 60 if rate > 0 else 0
            print(f"  [{indexed:,}/{len(todo):,}] {rate:.0f}/s | ~{rem:.1f} min | api_err={api_errs} es_err={es_errs}")

    es.indices.refresh(index=ARABIC_INDEX)
    print(f"  Done: {indexed:,} | api_err={api_errs} | es_err={es_errs}")
    print(f"  Verified count: {es.count(index=ARABIC_INDEX)['count']:,}")


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "both"
    if target in ("english", "both"):
        index_english()
    if target in ("arabic", "both"):
        index_arabic()
    print("\nAll done.")
