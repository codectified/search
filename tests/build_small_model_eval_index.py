"""
Builds the `small-model-eval` ES index — a single index with one dense_vector
field per model, so all four small-model candidates can be compared side-by-side
without managing separate indexes.

Vector fields:
  vec_mxbai       1024-dim  — extracted from existing english-mxbai (no re-embed)
  vec_nomic        768-dim  — nomic-embed-text via Ollama
  vec_snowflake    768-dim  — snowflake-arctic-embed:m via Ollama
  vec_miniLM       384-dim  — all-minilm via Ollama

Prerequisites:
  - english-mxbai index must be clean (run Flask /index?model=mxbai&rebuild=true first)
  - Ollama models pulled: nomic-embed-text, snowflake-arctic-embed:m, all-minilm

Run inside container:
  docker exec search-web-1 python3 /code/tests/build_small_model_eval_index.py

To force a clean rebuild:
  docker exec search-web-1 python3 /code/tests/build_small_model_eval_index.py --rebuild
"""
import os, sys, json, time, urllib.request, numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

OLLAMA_URL  = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
ES_HOST     = "http://172.31.250.10:9200"
SOURCE_IDX  = "english-mxbai"
DEST_IDX    = "small-model-eval"
BATCH_SIZE  = 32     # docs per Ollama embed call
BULK_SIZE   = 200    # docs per ES bulk request

REBUILD = "--rebuild" in sys.argv

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

OLLAMA_MODELS = [
    ("nomic",     "nomic-embed-text",      768),
    ("snowflake", "snowflake-arctic-embed:m", 768),
    ("miniLM",    "all-minilm",            384),
]

# ── Index setup ───────────────────────────────────────────────────────────────

MAPPINGS = {
    "properties": {
        "urn":          {"type": "long",    "index": False},
        "collection":   {"type": "keyword"},
        "hadithNumber": {"type": "keyword"},
        "hadithText":   {"type": "text"},
        "arabicText":   {"type": "text"},
        "englishMatn":  {"type": "text",    "index": False},
        "isChainRef":   {"type": "boolean"},
        "dupGroup":     {"type": "long"},
        "gradeNorm":    {"type": "keyword"},
        "grade":        {"type": "keyword"},
        # One dense_vector field per model. index=True enables kNN.
        "vec_mxbai":      {"type": "dense_vector", "dims": 1024, "index": True, "similarity": "cosine"},
        "vec_nomic":      {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
        "vec_snowflake":  {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
        "vec_miniLM":     {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
    }
}

def create_index():
    if es.indices.exists(index=DEST_IDX):
        if REBUILD:
            print(f"Deleting existing {DEST_IDX}...")
            es.indices.delete(index=DEST_IDX)
        else:
            print(f"{DEST_IDX} already exists. Pass --rebuild to recreate.")
            return False
    es.indices.create(index=DEST_IDX, mappings=MAPPINGS)
    print(f"Created {DEST_IDX}")
    return True


# ── Ollama embedding ──────────────────────────────────────────────────────────

def ollama_embed(model_id, texts):
    """Embed a batch of texts. Returns list of float vectors."""
    payload = json.dumps({"model": model_id, "input": texts}).encode()
    req = urllib.request.Request(
        f"{OLLAMA_URL}/v1/embeddings",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        body = json.loads(r.read())
    # Sort by index to maintain order
    data = sorted(body["data"], key=lambda x: x["index"])
    return [d["embedding"] for d in data]


def extract_mxbai_vector(source):
    """Average over all chunks (most hadiths have 1) and L2-normalise."""
    chunks = source.get("semantic_text", {}).get("inference", {}).get("chunks", [])
    if not chunks:
        return None
    vecs = [np.array(c["embeddings"], dtype=np.float32) for c in chunks]
    v = np.mean(vecs, axis=0)
    norm = np.linalg.norm(v)
    if norm > 0:
        v = v / norm
    return v.tolist()


# ── Main indexing loop ────────────────────────────────────────────────────────

def run():
    if not create_index():
        return

    print(f"Scanning {SOURCE_IDX}...")
    t0 = time.time()

    # Fields we need from source
    source_fields = [
        "urn", "collection", "hadithNumber", "hadithText", "arabicText",
        "englishMatn", "isChainRef", "dupGroup", "gradeNorm", "grade",
        "semantic_text",
    ]

    # Buffer for batching
    buf_ids      = []   # ES _id strings
    buf_sources  = []   # raw _source dicts
    buf_texts    = []   # text to embed with Ollama models
    buf_mxbai    = []   # extracted mxbai vectors

    actions_pending = []
    total = 0
    errors = 0

    def flush_batch():
        nonlocal errors
        if not buf_texts:
            return

        # Embed with each Ollama model
        embedded = {}
        for key, model_id, _ in OLLAMA_MODELS:
            try:
                embedded[key] = ollama_embed(model_id, buf_texts)
            except Exception as e:
                print(f"  Ollama error [{model_id}]: {e}")
                embedded[key] = [None] * len(buf_texts)

        for i, (doc_id, src, mxbai_vec) in enumerate(zip(buf_ids, buf_sources, buf_mxbai)):
            doc = {k: src[k] for k in source_fields[:-1] if k in src}  # exclude semantic_text
            if mxbai_vec:
                doc["vec_mxbai"] = mxbai_vec
            for key, _, _ in OLLAMA_MODELS:
                if embedded[key][i] is not None:
                    doc[f"vec_{key}"] = embedded[key][i]
            actions_pending.append({"_index": DEST_IDX, "_id": doc_id, "_source": doc})

        buf_ids.clear(); buf_sources.clear(); buf_texts.clear(); buf_mxbai.clear()

        # Flush to ES when we have enough
        if len(actions_pending) >= BULK_SIZE:
            flush_bulk()

    def flush_bulk():
        nonlocal errors
        if not actions_pending:
            return
        ok, errs = bulk(es, actions_pending, raise_on_error=False, raise_on_exception=False)
        errors += len(errs)
        actions_pending.clear()

    for hit in es_scan(
        es, index=SOURCE_IDX,
        query={"query": {"match_all": {}}},
        _source=source_fields,
        size=100,
    ):
        src = hit["_source"]
        # Use hadithText for all models — mxbai vectors were built from hadithText,
        # so using the same field keeps the comparison fair (same input, different model).
        text = src.get("hadithText") or ""
        if not text:
            continue

        mxbai_vec = extract_mxbai_vector(src)

        buf_ids.append(hit["_id"])
        buf_sources.append(src)
        buf_texts.append(text)
        buf_mxbai.append(mxbai_vec)
        total += 1

        if len(buf_texts) >= BATCH_SIZE:
            flush_batch()

        if total % 1000 == 0:
            elapsed = time.time() - t0
            rate = total / elapsed
            remaining = (48703 - total) / rate if rate > 0 else 0
            print(f"  {total:>6} docs | {elapsed:.0f}s elapsed | ~{remaining:.0f}s remaining")

    # Flush remainder
    flush_batch()
    flush_bulk()

    elapsed = time.time() - t0
    count = es.count(index=DEST_IDX)["count"]
    print(f"\nDone: {total} processed → {count} indexed | {errors} errors | {elapsed:.0f}s")
    print(f"Index ready: {DEST_IDX}")


if __name__ == "__main__":
    run()
