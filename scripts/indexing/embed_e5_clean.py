"""
Embed arabicMatnClean → vec_e5_matn and arabicTextClean → vec_e5_full
using intfloat/multilingual-e5-large (1024d).

Skips docs that already have the target vector (safe to resume).
Run AFTER rebuild_arabic_research.py.

Run inside container:
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 \\
        -e HUGGING_FACE_KEY=<token> \\
        search-web-1 python3 /code/scripts/indexing/embed_e5_clean.py

Env vars:
    FIELD   which field to embed: "matn", "full", or "both" (default: both)
    BATCH   encode batch size (default 32)
"""
import os, sys, time
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
FIELD   = os.environ.get("FIELD", "both")   # "matn", "full", or "both"
BATCH_SIZE = int(os.environ.get("BATCH", 32))
INDEX   = "arabic-research"
MODEL_NAME = "intfloat/multilingual-e5-large"
PREFIX  = "passage: "

_default_cache = os.path.join(os.path.expanduser("~"), ".cache", "huggingface") \
    if os.name == "nt" else "/code/data/hf-cache"
HF_CACHE = os.environ.get("HF_HOME", _default_cache)
os.environ["HF_HOME"] = HF_CACHE
ST_PKG = os.path.join(HF_CACHE, "stpkg")

# Install sentence-transformers if missing
try:
    sys.path.insert(0, ST_PKG)
    from sentence_transformers import SentenceTransformer
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install",
                           "sentence-transformers", "-q",
                           "--target", ST_PKG])
    sys.path.insert(0, ST_PKG)
    from sentence_transformers import SentenceTransformer

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW), request_timeout=120)

print(f"Loading {MODEL_NAME}...")
model = SentenceTransformer(MODEL_NAME, cache_folder=HF_CACHE)
print("  Model ready.")
print("  Warming up CUDA kernels...")
_ = model.encode(["passage: warm up"] * min(BATCH_SIZE, 8),
                 batch_size=min(BATCH_SIZE, 8),
                 normalize_embeddings=True, show_progress_bar=False)
print("  CUDA warm-up done.")

DO_MATN = FIELD in ("matn", "both")
DO_FULL = FIELD in ("full", "both")


def embed_batch(texts):
    padded = [PREFIX + t for t in texts]
    vecs = model.encode(padded, batch_size=BATCH_SIZE,
                        normalize_embeddings=True, show_progress_bar=False)
    return vecs.tolist()


def run(src_field, vec_field):
    print(f"\n── Embedding {src_field} → {vec_field} ──")
    t0 = time.time()
    buf_ids, buf_texts = [], []
    done = skipped = errors = 0

    # vec fields ARE indexed; src text fields have index:False so can't use exists on them
    query = {"bool": {"must_not": [{"exists": {"field": vec_field}}]}}

    def flush():
        nonlocal done, errors
        if not buf_ids:
            return
        try:
            vecs = embed_batch(buf_texts)
            actions = [
                {"_op_type": "update", "_index": INDEX, "_id": doc_id,
                 "doc": {vec_field: vec}}
                for doc_id, vec in zip(buf_ids, vecs)
            ]
            ok, errs = bulk(es, actions, chunk_size=len(actions),
                            raise_on_error=False)
            done += ok
            errors += len(errs)
        except Exception as e:
            print(f"  Batch error: {e}")
            errors += len(buf_ids)
        buf_ids.clear()
        buf_texts.clear()

    for hit in es_scan(es, index=INDEX, query={"query": query},
                       _source=[src_field], size=200, scroll="120m"):
        text = (hit["_source"].get(src_field) or "").strip()
        if not text:
            skipped += 1
            continue
        buf_ids.append(hit["_id"])
        buf_texts.append(text)
        if len(buf_ids) >= BATCH_SIZE:
            flush()
        total = done + skipped + errors
        if total % 5000 == 0 and total > 0:
            rate = done / (time.time() - t0 + 1e-9)
            print(f"  {done:,} embedded | {skipped} skipped | {rate:.1f} doc/s")

    flush()
    print(f"  Done: {done:,} embedded | {skipped} skipped | {errors} errors "
          f"| {time.time()-t0:.0f}s")


if DO_MATN:
    run("arabicMatnClean", "vec_e5_matn")

if DO_FULL:
    run("arabicTextClean", "vec_e5_full")

print("\nAll done. Run cluster_arabic_research.py next.")
