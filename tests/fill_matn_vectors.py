"""
Fills `_matn`-suffixed dense_vector fields in the existing `small-model-eval` index.

Rather than rebuilding from scratch, this script adds a parallel set of embeddings
where the input text is the isnad-stripped English matn instead of raw hadithText.
Comparing `vec_X` (hadithText) vs `vec_X_matn` (englishMatn) shows how much
isnad noise affects retrieval for each model.

New fields added (11 total, one per model):
  Ollama:
    vec_mxbai_matn      1024-dim  mxbai-embed-large re-embedded on matn
    vec_nomic_matn       768-dim  nomic-embed-text
    vec_snowflake_matn   768-dim  snowflake-arctic-embed:m
    vec_miniLM_matn      384-dim  all-MiniLM-L6-v2

  sentence_transformers:
    vec_gemma_matn       768-dim  google/embeddinggemma-300m
    vec_gemma_q8_matn    768-dim  google/embeddinggemma-300m-qat-q8_0-unquantized
    vec_gemma_q4_matn    768-dim  google/embeddinggemma-300m-qat-q4_0-unquantized
    vec_mxbai_xs_matn    384-dim  mixedbread-ai/mxbai-embed-xsmall-v1

  ONNX Runtime:
    vec_mxbai_q_matn     1024-dim  mxbai-embed-large-v1  onnx/model_quantized.onnx
    vec_mxbai_xs_q8_matn  384-dim  mxbai-embed-xsmall-v1 onnx/model_int8.onnx
    vec_mxbai_xs_q4_matn  384-dim  mxbai-embed-xsmall-v1 onnx/model_q4.onnx

Prerequisites:
  - small-model-eval index already built and populated
  - english_matn_map.json present at /code/english_matn_map.json
  - Ollama running with all four models pulled
  - HF_TOKEN env var set for gated Gemma models

Run inside container (safe to re-run — skips models already filled):
  docker exec -e HF_TOKEN=hf_xxx search-web-1 python3 /code/tests/fill_matn_vectors.py

Force refill a specific model key (e.g. after a failure):
  docker exec -e HF_TOKEN=hf_xxx search-web-1 python3 /code/tests/fill_matn_vectors.py --force gemma
"""
import os, sys, json, time, subprocess, urllib.request
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

# ── HF cache — must precede any huggingface import ───────────────────────────
_HF_CACHE = "/tmp/hf_cache"
os.environ.setdefault("HF_HOME", _HF_CACHE)
os.environ.setdefault("HUGGINGFACE_HUB_CACHE", _HF_CACHE)
os.environ.setdefault("TRANSFORMERS_CACHE", _HF_CACHE)

# ── Config ────────────────────────────────────────────────────────────────────

HF_TOKEN    = os.environ.get("HF_TOKEN", "")
OLLAMA_URL  = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
ES_HOST     = "http://172.31.250.10:9200"
DEST_IDX    = "small-model-eval"
MATN_MAP    = "/code/english_matn_map.json"

OLLAMA_BATCH = 32
ST_BATCH     = 16
ONNX_BATCH   = 32
BULK_SIZE    = 200

# --force <key> re-runs that model even if already filled
FORCE_KEY = None
for i, arg in enumerate(sys.argv[1:]):
    if arg == "--force" and i + 1 < len(sys.argv) - 1:
        FORCE_KEY = sys.argv[i + 2]

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

# ── Model registry ────────────────────────────────────────────────────────────

OLLAMA_MODELS = [
    ("mxbai",     "mxbai-embed-large",        1024),
    ("nomic",     "nomic-embed-text",          768),
    ("snowflake", "snowflake-arctic-embed:m",  768),
    ("miniLM",    "all-minilm",               384),
]

ST_MODELS = [
    ("gemma",    "google/embeddinggemma-300m",                       768,  True),
    ("gemma_q8", "google/embeddinggemma-300m-qat-q8_0-unquantized",  768,  True),
    ("gemma_q4", "google/embeddinggemma-300m-qat-q4_0-unquantized",  768,  True),
    ("mxbai_xs", "mixedbread-ai/mxbai-embed-xsmall-v1",             384,  False),
]

ONNX_MODELS = [
    ("mxbai_q",     "mixedbread-ai/mxbai-embed-large-v1",  "onnx/model_quantized.onnx", 1024),
    ("mxbai_xs_q8", "mixedbread-ai/mxbai-embed-xsmall-v1", "onnx/model_int8.onnx",       384),
    ("mxbai_xs_q4", "mixedbread-ai/mxbai-embed-xsmall-v1", "onnx/model_q4.onnx",         384),
]

# ── Mapping update ────────────────────────────────────────────────────────────

MATN_FIELDS = {
    "vec_mxbai_matn":       {"type": "dense_vector", "dims": 1024, "index": True, "similarity": "cosine"},
    "vec_nomic_matn":       {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
    "vec_snowflake_matn":   {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
    "vec_miniLM_matn":      {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
    "vec_gemma_matn":       {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
    "vec_gemma_q8_matn":    {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
    "vec_gemma_q4_matn":    {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
    "vec_mxbai_xs_matn":    {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
    "vec_mxbai_q_matn":     {"type": "dense_vector", "dims": 1024, "index": True, "similarity": "cosine"},
    "vec_mxbai_xs_q8_matn": {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
    "vec_mxbai_xs_q4_matn": {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
}

def ensure_mapping():
    """Add _matn fields to the index mapping if not already present."""
    existing = es.indices.get_mapping(index=DEST_IDX)[DEST_IDX]["mappings"]["properties"]
    new_fields = {k: v for k, v in MATN_FIELDS.items() if k not in existing}
    if new_fields:
        es.indices.put_mapping(index=DEST_IDX, properties=new_fields)
        print(f"Added {len(new_fields)} new _matn fields to mapping.")
    else:
        print("All _matn fields already in mapping.")


# ── Helpers: check if a model is already filled ───────────────────────────────

def is_filled(field):
    if FORCE_KEY and field == f"vec_{FORCE_KEY}_matn":
        return False
    count = es.count(index=DEST_IDX, query={"exists": {"field": field}})["count"]
    total = es.count(index=DEST_IDX)["count"]
    if count > total * 0.95:
        print(f"  {field}: {count:,}/{total:,} — already filled, skipping.")
        return True
    print(f"  {field}: {count:,}/{total:,} — needs fill.")
    return False


# ── Collect all docs from index ───────────────────────────────────────────────

def collect_docs():
    print("Collecting doc IDs and URNs from small-model-eval ...")
    docs = []  # (es_id, urn_str)
    for hit in es_scan(es, index=DEST_IDX,
                       query={"query": {"match_all": {}}},
                       _source=["urn"], size=200):
        urn = str(hit["_source"].get("urn", ""))
        docs.append((hit["_id"], urn))
    print(f"  {len(docs):,} docs collected.")
    return docs


# ── Load matn texts ───────────────────────────────────────────────────────────

def load_matn_map():
    print(f"Loading {MATN_MAP} ...")
    with open(MATN_MAP, encoding="utf-8") as f:
        raw = json.load(f)
    # raw keys are URN strings, values are {'matn': '...'}
    return {k: v.get("matn", "") for k, v in raw.items()}


# ── pip helpers ───────────────────────────────────────────────────────────────

_PIP_TARGET = "/tmp/pip_extra"
_st_ready   = False
_onnx_ready = False

def _pip_install(*packages):
    os.makedirs(_PIP_TARGET, exist_ok=True)
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--no-cache-dir", "-q",
         "-t", _PIP_TARGET, *packages],
        check=True
    )
    if _PIP_TARGET not in sys.path:
        sys.path.insert(0, _PIP_TARGET)

def _ensure_st():
    global _st_ready
    if not _st_ready:
        print("  pip install sentence-transformers huggingface_hub ...")
        _pip_install("sentence-transformers>=3.0", "huggingface_hub")
        _st_ready = True

def _ensure_onnx():
    global _onnx_ready
    if not _onnx_ready:
        print("  pip install onnxruntime transformers huggingface_hub ...")
        _pip_install("onnxruntime", "transformers", "huggingface_hub")
        _onnx_ready = True


# ── Embedding functions ───────────────────────────────────────────────────────

def ollama_embed_batch(model_id, texts):
    payload = json.dumps({"model": model_id, "input": texts}).encode()
    req = urllib.request.Request(
        f"{OLLAMA_URL}/v1/embeddings",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        body = json.loads(r.read())
    data = sorted(body["data"], key=lambda x: x["index"])
    return [d["embedding"] for d in data]


def embed_ollama_all(model_id, texts):
    """Embed all texts via Ollama in OLLAMA_BATCH chunks."""
    result = [None] * len(texts)
    for i in range(0, len(texts), OLLAMA_BATCH):
        batch = texts[i : i + OLLAMA_BATCH]
        try:
            vecs = ollama_embed_batch(model_id, batch)
            for j, v in enumerate(vecs):
                result[i + j] = v
        except Exception as e:
            print(f"    Ollama error batch {i}: {e}")
        if i % (OLLAMA_BATCH * 200) == 0 and i > 0:
            print(f"    {i:,}/{len(texts):,} ...")
    return result


def embed_st_all(hf_repo, texts, trust_remote_code=False):
    _ensure_st()
    from sentence_transformers import SentenceTransformer
    os.makedirs(_HF_CACHE, exist_ok=True)
    kwargs = {"trust_remote_code": trust_remote_code, "cache_folder": _HF_CACHE}
    if HF_TOKEN:
        kwargs["token"] = HF_TOKEN
    print(f"  Loading {hf_repo} ...")
    try:
        model = SentenceTransformer(hf_repo, **kwargs)
    except Exception as e:
        print(f"  Load failed: {e}")
        return None
    t0 = time.time()
    vecs = model.encode(texts, normalize_embeddings=True,
                        batch_size=ST_BATCH, show_progress_bar=True)
    print(f"  Encoded {len(texts):,} in {time.time()-t0:.0f}s")
    del model
    return vecs.tolist()


def embed_onnx_all(hf_repo, onnx_file, texts):
    _ensure_onnx()
    import onnxruntime as ort
    from transformers import AutoTokenizer
    from huggingface_hub import hf_hub_download

    os.makedirs(_HF_CACHE, exist_ok=True)
    print(f"  Downloading {onnx_file} ...")
    try:
        onnx_path = hf_hub_download(hf_repo, filename=onnx_file,
                                    token=HF_TOKEN or None, cache_dir=_HF_CACHE)
    except Exception as e:
        print(f"  Download failed: {e}")
        return None

    sess = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
    input_names = {inp.name for inp in sess.get_inputs()}
    tokenizer = AutoTokenizer.from_pretrained(hf_repo, token=HF_TOKEN or None,
                                              cache_dir=_HF_CACHE)
    result = []
    t0 = time.time()
    for i in range(0, len(texts), ONNX_BATCH):
        batch = texts[i : i + ONNX_BATCH]
        enc = tokenizer(batch, padding=True, truncation=True,
                        max_length=512, return_tensors="np")
        inputs = {k: v for k, v in enc.items() if k in input_names}
        outputs = sess.run(None, inputs)
        hidden = outputs[0]
        mask   = enc["attention_mask"][:, :, None]
        v = (hidden * mask).sum(axis=1) / mask.sum(axis=1).clip(min=1)
        v = v.astype(np.float32)
        norms = np.linalg.norm(v, axis=1, keepdims=True).clip(min=1e-9)
        result.extend((v / norms).tolist())
        if i % (ONNX_BATCH * 200) == 0 and i > 0:
            print(f"    {i:,}/{len(texts):,} ...")
    print(f"  Encoded {len(texts):,} in {time.time()-t0:.0f}s")
    del sess
    return result


# ── Bulk update ───────────────────────────────────────────────────────────────

def bulk_update(ids, vecs, field):
    """Update existing ES docs with a single new field."""
    if vecs is None:
        print(f"  Skipping {field} — no vectors.")
        return
    actions = []
    errors  = 0
    for doc_id, vec in zip(ids, vecs):
        if vec is None:
            continue
        actions.append({
            "_op_type": "update",
            "_index":   DEST_IDX,
            "_id":      doc_id,
            "doc":      {field: vec},
        })
        if len(actions) >= BULK_SIZE:
            ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
            errors += len(errs)
            actions.clear()
    if actions:
        ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        errors += len(errs)
    filled = es.count(index=DEST_IDX, query={"exists": {"field": field}})["count"]
    print(f"  {field}: {filled:,} docs filled | {errors} errors")


# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    ensure_mapping()

    docs    = collect_docs()
    matn_map = load_matn_map()

    ids   = [d[0] for d in docs]
    urns  = [d[1] for d in docs]
    texts = [matn_map.get(u, "") for u in urns]

    empty = sum(1 for t in texts if not t.strip())
    print(f"Matn texts: {len(texts)-empty:,} non-empty, {empty} empty")

    t0 = time.time()

    # ── Ollama ─────────────────────────────────────────────────────────────────
    print("\n── Ollama models ─────────────────────────────────────────────────────")
    for key, model_id, dims in OLLAMA_MODELS:
        field = f"vec_{key}_matn"
        print(f"\n[{key}] {model_id}")
        if is_filled(field):
            continue
        vecs = embed_ollama_all(model_id, texts)
        bulk_update(ids, vecs, field)

    # ── sentence_transformers ──────────────────────────────────────────────────
    print("\n── sentence_transformers models ──────────────────────────────────────")
    for key, hf_repo, dims, trust_rc in ST_MODELS:
        field = f"vec_{key}_matn"
        print(f"\n[{key}] {hf_repo}")
        if is_filled(field):
            continue
        vecs = embed_st_all(hf_repo, texts, trust_rc)
        bulk_update(ids, vecs, field)

    # ── ONNX ───────────────────────────────────────────────────────────────────
    print("\n── ONNX models ───────────────────────────────────────────────────────")
    for key, hf_repo, onnx_file, dims in ONNX_MODELS:
        field = f"vec_{key}_matn"
        print(f"\n[{key}] {hf_repo} / {onnx_file}")
        if is_filled(field):
            continue
        vecs = embed_onnx_all(hf_repo, onnx_file, texts)
        bulk_update(ids, vecs, field)

    # ── Coverage summary ───────────────────────────────────────────────────────
    elapsed = time.time() - t0
    total   = es.count(index=DEST_IDX)["count"]
    print(f"\nDone in {elapsed:.0f}s. Coverage:")
    for field in MATN_FIELDS:
        c = es.count(index=DEST_IDX, query={"exists": {"field": field}})["count"]
        print(f"  {field:25s}  {c:>6,} / {total:,}")


if __name__ == "__main__":
    run()
