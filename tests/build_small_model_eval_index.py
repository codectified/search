"""
Builds the `small-model-eval` ES index — 11 candidate embedding models compared
side-by-side using a single index with one dense_vector field per model.

Vector fields
─────────────
Ollama (from existing index or live embed):
  vec_mxbai        1024-dim  mxbai-embed-large F16 — extracted from english-mxbai (no re-embed)
  vec_nomic         768-dim  nomic-embed-text
  vec_snowflake     768-dim  snowflake-arctic-embed:m
  vec_miniLM        384-dim  all-MiniLM-L6-v2

sentence_transformers (HuggingFace — HF_TOKEN required for Gemma):
  vec_gemma         768-dim  google/embeddinggemma-300m
  vec_gemma_q8      768-dim  google/embeddinggemma-300m-qat-q8_0-unquantized
  vec_gemma_q4      768-dim  google/embeddinggemma-300m-qat-q4_0-unquantized
  vec_mxbai_xs      384-dim  mixedbread-ai/mxbai-embed-xsmall-v1  (FP32 baseline)

ONNX Runtime (HuggingFace):
  vec_mxbai_q      1024-dim  mixedbread-ai/mxbai-embed-large-v1   onnx/model_quantized.onnx (INT8)
  vec_mxbai_xs_q8   384-dim  mixedbread-ai/mxbai-embed-xsmall-v1  onnx/model_int8.onnx      (INT8)
  vec_mxbai_xs_q4   384-dim  mixedbread-ai/mxbai-embed-xsmall-v1  onnx/model_q4.onnx        (INT4)

Note on FP8: FP8 requires H100-class GPU hardware; CPUs have no native FP8 execution.
INT8 (Q8_0) is the practical equivalent — same 8-bit width, CPU-executable.

Strategy
────────
All 48k texts are collected into RAM first (≈30MB text + ≈200MB mxbai vecs as numpy).
Ollama models are embedded during the initial scroll in streaming batches.
ST and ONNX models are loaded one at a time (model weights freed after each) to
cap peak RAM. Final index build happens in one bulk pass.

Prerequisites:
  - english-mxbai index must be clean (run Flask /index?model=mxbai&rebuild=true first)
  - Ollama running with: nomic-embed-text, snowflake-arctic-embed:m, all-minilm
  - HF_TOKEN env var set for gated Gemma models

Run inside container:
  docker exec -e HF_TOKEN=hf_xxx search-web-1 python3 /code/tests/build_small_model_eval_index.py

Force clean rebuild:
  docker exec -e HF_TOKEN=hf_xxx search-web-1 python3 /code/tests/build_small_model_eval_index.py --rebuild
"""
import os, sys, json, time, subprocess, urllib.request
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

# ── Config ────────────────────────────────────────────────────────────────────

HF_TOKEN   = os.environ.get("HF_TOKEN", "")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
ES_HOST    = "http://172.31.250.10:9200"
SOURCE_IDX = "english-mxbai"
DEST_IDX   = "small-model-eval"

OLLAMA_BATCH = 32    # texts per Ollama /v1/embeddings call
ST_BATCH     = 16    # texts per SentenceTransformer.encode() call
ONNX_BATCH   = 32    # texts per ONNX session.run() call
BULK_SIZE    = 200   # docs per ES bulk request

REBUILD = "--rebuild" in sys.argv

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

# ── Model registry ────────────────────────────────────────────────────────────

OLLAMA_MODELS = [
    # (key,  ollama_model_id,           dims)
    ("nomic",     "nomic-embed-text",        768),
    ("snowflake", "snowflake-arctic-embed:m", 768),
    ("miniLM",    "all-minilm",              384),
]

ST_MODELS = [
    # (key,        hf_repo,                                              dims, trust_remote_code)
    ("gemma",    "google/embeddinggemma-300m",                       768,  True),
    ("gemma_q8", "google/embeddinggemma-300m-qat-q8_0-unquantized",  768,  True),
    ("gemma_q4", "google/embeddinggemma-300m-qat-q4_0-unquantized",  768,  True),
    ("mxbai_xs", "mixedbread-ai/mxbai-embed-xsmall-v1",             384,  False),
]

ONNX_MODELS = [
    # (key,            hf_repo,                              onnx_file,                  dims)
    ("mxbai_q",     "mixedbread-ai/mxbai-embed-large-v1",  "onnx/model_quantized.onnx", 1024),
    ("mxbai_xs_q8", "mixedbread-ai/mxbai-embed-xsmall-v1", "onnx/model_int8.onnx",       384),
    ("mxbai_xs_q4", "mixedbread-ai/mxbai-embed-xsmall-v1", "onnx/model_q4.onnx",         384),
]

# ── Index mapping ─────────────────────────────────────────────────────────────

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
        # ── Ollama ──────────────────────────────────────────────
        "vec_mxbai":      {"type": "dense_vector", "dims": 1024, "index": True, "similarity": "cosine"},
        "vec_nomic":      {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
        "vec_snowflake":  {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
        "vec_miniLM":     {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
        # ── sentence_transformers ────────────────────────────────
        "vec_gemma":      {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
        "vec_gemma_q8":   {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
        "vec_gemma_q4":   {"type": "dense_vector", "dims": 768,  "index": True, "similarity": "cosine"},
        "vec_mxbai_xs":   {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
        # ── ONNX quantized ───────────────────────────────────────
        "vec_mxbai_q":      {"type": "dense_vector", "dims": 1024, "index": True, "similarity": "cosine"},
        "vec_mxbai_xs_q8":  {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
        "vec_mxbai_xs_q4":  {"type": "dense_vector", "dims": 384,  "index": True, "similarity": "cosine"},
    }
}

# ── Index setup ───────────────────────────────────────────────────────────────

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


def extract_mxbai_vector(source):
    """Average chunk embeddings from ES semantic_text field and L2-normalise."""
    chunks = source.get("semantic_text", {}).get("inference", {}).get("chunks", [])
    if not chunks:
        return None
    vecs = [np.array(c["embeddings"], dtype=np.float32) for c in chunks]
    v = np.mean(vecs, axis=0)
    norm = np.linalg.norm(v)
    if norm > 0:
        v = v / norm
    return v


# ── sentence_transformers embedding ──────────────────────────────────────────

_st_ready = False

def _ensure_st():
    global _st_ready
    if not _st_ready:
        print("  pip install sentence-transformers huggingface_hub ...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-q",
             "sentence-transformers>=3.0", "huggingface_hub"],
            check=True
        )
        _st_ready = True

def st_embed_all(hf_repo, texts, dims, trust_remote_code=False):
    """Load model, embed all texts, return numpy (N, dims), then free model."""
    _ensure_st()
    from sentence_transformers import SentenceTransformer

    kwargs = {"trust_remote_code": trust_remote_code}
    if HF_TOKEN:
        kwargs["token"] = HF_TOKEN

    print(f"  Loading {hf_repo} ...")
    try:
        model = SentenceTransformer(hf_repo, **kwargs)
    except Exception as e:
        print(f"  SentenceTransformer load failed: {e}")
        print("  Falling back to raw transformers ...")
        return _transformers_embed_all(hf_repo, texts, dims)

    t0 = time.time()
    vecs = model.encode(
        texts,
        normalize_embeddings=True,
        batch_size=ST_BATCH,
        show_progress_bar=True,
    )
    elapsed = time.time() - t0
    print(f"  Encoded {len(texts)} docs in {elapsed:.0f}s  shape={vecs.shape}")
    del model
    return vecs.astype(np.float32)


def _transformers_embed_all(hf_repo, texts, dims):
    """Fallback: raw transformers mean-pool + L2-normalise."""
    import torch
    from transformers import AutoTokenizer, AutoModel

    kw = {}
    if HF_TOKEN:
        kw["token"] = HF_TOKEN
    tokenizer = AutoTokenizer.from_pretrained(hf_repo, **kw)
    model     = AutoModel.from_pretrained(hf_repo, trust_remote_code=True, **kw)
    model.eval()

    all_vecs = []
    t0 = time.time()
    for i in range(0, len(texts), ST_BATCH):
        batch = texts[i : i + ST_BATCH]
        enc = tokenizer(batch, padding=True, truncation=True,
                        max_length=512, return_tensors="pt")
        with torch.no_grad():
            out = model(**enc)
        mask = enc["attention_mask"][:, :, None].float()
        v = (out.last_hidden_state * mask).sum(1) / mask.sum(1).clamp(min=1)
        v = torch.nn.functional.normalize(v, p=2, dim=1)
        all_vecs.append(v.cpu().numpy())
        if (i // ST_BATCH) % 100 == 0:
            print(f"    {i}/{len(texts)} ...")

    elapsed = time.time() - t0
    result = np.concatenate(all_vecs, axis=0).astype(np.float32)
    print(f"  Encoded {len(texts)} docs in {elapsed:.0f}s  shape={result.shape}")
    del model
    return result


# ── ONNX Runtime embedding ────────────────────────────────────────────────────

_onnx_ready = False

def _ensure_onnx():
    global _onnx_ready
    if not _onnx_ready:
        print("  pip install onnxruntime transformers huggingface_hub ...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-q",
             "onnxruntime", "transformers", "huggingface_hub"],
            check=True
        )
        _onnx_ready = True


def onnx_embed_all(hf_repo, onnx_file, texts, dims):
    """Download ONNX model, embed all texts, return numpy (N, dims), then free session."""
    _ensure_onnx()
    import onnxruntime as ort
    from transformers import AutoTokenizer
    from huggingface_hub import hf_hub_download

    print(f"  Downloading {onnx_file} from {hf_repo} ...")
    onnx_path = hf_hub_download(
        hf_repo, filename=onnx_file,
        token=HF_TOKEN or None,
    )
    sess = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
    input_names = {inp.name for inp in sess.get_inputs()}

    print(f"  Loading tokenizer from {hf_repo} ...")
    tokenizer = AutoTokenizer.from_pretrained(hf_repo, token=HF_TOKEN or None)

    all_vecs = []
    t0 = time.time()
    for i in range(0, len(texts), ONNX_BATCH):
        batch = texts[i : i + ONNX_BATCH]
        enc = tokenizer(batch, padding=True, truncation=True,
                        max_length=512, return_tensors="np")
        inputs = {k: v for k, v in enc.items() if k in input_names}
        outputs = sess.run(None, inputs)
        # outputs[0]: last_hidden_state (B, S, D)
        hidden = outputs[0]
        mask   = enc["attention_mask"][:, :, None]  # (B, S, 1)
        summed = (hidden * mask).sum(axis=1)
        counts = mask.sum(axis=1).clip(min=1)
        v = (summed / counts).astype(np.float32)
        norms = np.linalg.norm(v, axis=1, keepdims=True).clip(min=1e-9)
        all_vecs.append(v / norms)
        if (i // ONNX_BATCH) % 100 == 0:
            print(f"    {i}/{len(texts)} ...")

    elapsed = time.time() - t0
    result = np.concatenate(all_vecs, axis=0)
    print(f"  Encoded {len(texts)} docs in {elapsed:.0f}s  shape={result.shape}")
    del sess
    return result


# ── Main ──────────────────────────────────────────────────────────────────────

SOURCE_FIELDS = [
    "urn", "collection", "hadithNumber", "hadithText", "arabicText",
    "englishMatn", "isChainRef", "dupGroup", "gradeNorm", "grade",
    "semantic_text",
]


def run():
    if not create_index():
        return

    # ── Phase 1: collect all docs ──────────────────────────────────────────────
    print(f"\nPhase 1 — Scanning {SOURCE_IDX} ...")
    t_phase = time.time()
    ids, texts, mxbai_vecs, sources = [], [], [], []

    for hit in es_scan(
        es, index=SOURCE_IDX,
        query={"query": {"match_all": {}}},
        _source=SOURCE_FIELDS,
        size=100,
    ):
        src  = hit["_source"]
        text = src.get("hadithText") or ""
        if not text:
            continue
        mxvec = extract_mxbai_vector(src)
        ids.append(hit["_id"])
        texts.append(text)
        mxbai_vecs.append(mxvec)
        sources.append(src)
        if len(ids) % 5000 == 0:
            print(f"  collected {len(ids):,} docs ...")

    n = len(ids)
    print(f"Collected {n:,} docs in {time.time()-t_phase:.0f}s")

    # ── Phase 2: Ollama embeddings (streaming, in OLLAMA_BATCH chunks) ─────────
    print(f"\nPhase 2 — Ollama embeddings ({', '.join(k for k,*_ in OLLAMA_MODELS)}) ...")
    ollama_vecs = {key: [None] * n for key, _, _ in OLLAMA_MODELS}

    for i in range(0, n, OLLAMA_BATCH):
        batch = texts[i : i + OLLAMA_BATCH]
        for key, model_id, _ in OLLAMA_MODELS:
            try:
                vecs = ollama_embed(model_id, batch)
                for j, v in enumerate(vecs):
                    ollama_vecs[key][i + j] = v
            except Exception as e:
                print(f"  Ollama error [{model_id}] batch {i}: {e}")
        if i % (OLLAMA_BATCH * 100) == 0 and i > 0:
            print(f"  {i:,}/{n:,} ...")

    print(f"  Ollama done in {time.time()-t_phase:.0f}s cumulative")

    # ── Phase 3: sentence_transformers embeddings ──────────────────────────────
    print(f"\nPhase 3 — sentence_transformers embeddings ...")
    st_vecs = {}
    for key, hf_repo, dims, trust_rc in ST_MODELS:
        print(f"\n  [{key}] {hf_repo}")
        try:
            st_vecs[key] = st_embed_all(hf_repo, texts, dims, trust_rc)
        except Exception as e:
            print(f"  FAILED [{key}]: {e}")
            st_vecs[key] = None

    # ── Phase 4: ONNX embeddings ───────────────────────────────────────────────
    print(f"\nPhase 4 — ONNX embeddings ...")
    onnx_vecs = {}
    for key, hf_repo, onnx_file, dims in ONNX_MODELS:
        print(f"\n  [{key}] {hf_repo} / {onnx_file}")
        try:
            onnx_vecs[key] = onnx_embed_all(hf_repo, onnx_file, texts, dims)
        except Exception as e:
            print(f"  FAILED [{key}]: {e}")
            onnx_vecs[key] = None

    # ── Phase 5: bulk index ────────────────────────────────────────────────────
    print(f"\nPhase 5 — Indexing {n:,} docs to {DEST_IDX} ...")
    meta_fields = SOURCE_FIELDS[:-1]  # exclude semantic_text
    actions = []
    errors  = 0

    def flush_bulk():
        nonlocal errors
        if not actions:
            return
        ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        errors += len(errs)
        actions.clear()

    for i, (doc_id, src) in enumerate(zip(ids, sources)):
        doc = {k: src[k] for k in meta_fields if k in src}

        # mxbai (extracted from index)
        if mxbai_vecs[i] is not None:
            doc["vec_mxbai"] = mxbai_vecs[i].tolist()

        # Ollama
        for key, _, _ in OLLAMA_MODELS:
            if ollama_vecs[key][i] is not None:
                doc[f"vec_{key}"] = ollama_vecs[key][i]

        # sentence_transformers
        for key, _, _, _ in ST_MODELS:
            arr = st_vecs.get(key)
            if arr is not None:
                doc[f"vec_{key}"] = arr[i].tolist()

        # ONNX
        for key, _, _, _ in ONNX_MODELS:
            arr = onnx_vecs.get(key)
            if arr is not None:
                doc[f"vec_{key}"] = arr[i].tolist()

        actions.append({"_index": DEST_IDX, "_id": doc_id, "_source": doc})
        if len(actions) >= BULK_SIZE:
            flush_bulk()

    flush_bulk()

    elapsed = time.time() - t_phase
    count   = es.count(index=DEST_IDX)["count"]
    print(f"\nDone: {n:,} processed → {count:,} indexed | {errors} errors | {elapsed:.0f}s total")
    print(f"Index ready: {DEST_IDX}")

    # Coverage report
    print("\nVector field coverage:")
    all_keys = (["mxbai"] +
                [k for k, *_ in OLLAMA_MODELS] +
                [k for k, *_ in ST_MODELS] +
                [k for k, *_ in ONNX_MODELS])
    for key in all_keys:
        field = f"vec_{key}"
        r = es.count(index=DEST_IDX, query={"exists": {"field": field}})
        print(f"  {field:20s}  {r['count']:>6,} / {count:,}")


if __name__ == "__main__":
    run()
