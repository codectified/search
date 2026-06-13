"""
Embed arabicMatn with multilingual-e5-large into the vec_e5_arabic field
of the arabic-research index.

Unlike vec_e5_crosslingual (which used English matn for translated hadiths),
this always uses arabicMatn — giving a pure Arabic-signal embedding.

Skips docs that already have vec_e5_arabic populated (safe to resume).

Install deps first (if needed):
    pip3 install sentence-transformers torch

Usage:
    ELASTIC_PASSWORD=docker123 python3 scripts/indexing/embed_e5_arabic.py

Env vars:
    ELASTIC_PASSWORD   (default: docker123)
    ES_HOST            (default: localhost)
    BATCH_SIZE         embedding batch size (default: 32)
    ES_BATCH           ES bulk batch size (default: 200)
"""
import os, sys, time
import numpy as np

ES_PW    = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST  = os.environ.get("ES_HOST", "localhost")
BATCH    = int(os.environ.get("BATCH_SIZE", 32))
ES_BATCH = int(os.environ.get("ES_BATCH", 200))
MODEL_ID = "intfloat/multilingual-e5-large"
PREFIX   = "passage: "
TARGET   = "arabic-research"

# Persistent cache dir mounted from host: ./data/hf-cache → /code/data/hf-cache
# Model downloads here once and survives container restarts/rebuilds.
HF_CACHE = os.environ.get("HF_HOME", "/code/data/hf-cache")
os.environ["HF_HOME"] = HF_CACHE
os.makedirs(HF_CACHE, exist_ok=True)

# Install sentence-transformers to persistent cache dir if not available
ST_PKG = os.path.join(HF_CACHE, "stpkg")
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    import subprocess
    print(f"Installing sentence-transformers to {ST_PKG}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install",
                           "sentence-transformers", "--target", ST_PKG, "-q"])
    sys.path.insert(0, ST_PKG)
    from sentence_transformers import SentenceTransformer

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW),
                   request_timeout=120)

# ── Load model ────────────────────────────────────────────────────────────────
print(f"Loading model: {MODEL_ID}")
t0 = time.time()
model = SentenceTransformer(MODEL_ID)
dim = model.get_sentence_embedding_dimension()
print(f"  dim={dim} | loaded in {time.time()-t0:.0f}s")


def encode_batch(texts):
    prefixed = [PREFIX + t for t in texts]
    vecs = model.encode(prefixed, batch_size=BATCH, normalize_embeddings=True,
                        show_progress_bar=False)
    return vecs.tolist()


# ── Scan docs that need embedding ─────────────────────────────────────────────
print("Scanning arabic-research for docs without vec_e5_arabic...")
query = {
    "query": {
        "bool": {
            "must": {"exists": {"field": "arabicMatn"}},
            "must_not": {"exists": {"field": "vec_e5_arabic"}},
        }
    }
}

batch_ids, batch_texts = [], []
ok_total = err_total = 0
processed = 0
t1 = time.time()


def flush(ids, texts):
    global ok_total, err_total
    vecs = encode_batch(texts)
    actions = [
        {
            "_op_type": "update",
            "_index": TARGET,
            "_id": doc_id,
            "doc": {"vec_e5_arabic": vec},
        }
        for doc_id, vec in zip(ids, vecs)
    ]
    ok, errors = bulk(es, actions, chunk_size=len(actions), raise_on_error=False)
    ok_total += ok
    err_total += len(errors)


for hit in es_scan(es, index=TARGET, query=query,
                   _source=["arabicMatn"], size=ES_BATCH):
    matn = (hit["_source"].get("arabicMatn") or "").strip()
    if not matn:
        continue
    batch_ids.append(hit["_id"])
    batch_texts.append(matn)

    if len(batch_ids) >= ES_BATCH:
        flush(batch_ids, batch_texts)
        processed += len(batch_ids)
        batch_ids, batch_texts = [], []
        if processed % 5000 == 0:
            elapsed = time.time() - t1
            rate = processed / elapsed
            print(f"  {processed:,} embedded | {rate:.0f}/s | {ok_total:,} ok"
                  f" | {err_total} errors")

if batch_ids:
    flush(batch_ids, batch_texts)
    processed += len(batch_ids)

print(f"\nDone: {processed:,} embedded, {ok_total:,} updated, {err_total} errors"
      f" — {time.time()-t1:.0f}s")

# ── Final coverage ────────────────────────────────────────────────────────────
r = es.count(index=TARGET, query={"exists": {"field": "vec_e5_arabic"}})
print(f"vec_e5_arabic coverage: {r['count']:,}")
