"""
Side-by-side comparison of all 9 embedding model candidates from `small-model-eval`.

Queries ES directly — no Flask dependency. For each query, embeds with each model
and runs kNN against the appropriate dense_vector field.

Models compared (11 total):
  Ollama (F16 / default quant):
    mxbai-embed-large        1024-dim  335M params  (prod baseline)
    nomic-embed-text          768-dim  137M params
    snowflake-arctic-embed:m  768-dim  110M params
    all-MiniLM-L6-v2          384-dim   22M params

  sentence_transformers / HF:
    embeddinggemma-300m       768-dim  300M params  (base)
    embeddinggemma-qat-q8     768-dim  300M params  (QAT-Q8, stored in fp32)
    embeddinggemma-qat-q4     768-dim  300M params  (QAT-Q4, stored in fp32)
    mxbai-embed-xsmall-v1     384-dim   33M params  (FP32 baseline)

  ONNX quantized:
    mxbai-embed-large INT8   1024-dim  335M params  (INT8 vs F16 baseline)
    mxbai-embed-xsmall INT8   384-dim   33M params  (INT8 — closest CPU analog to FP8)
    mxbai-embed-xsmall INT4   384-dim   33M params  (INT4 — max compression)

Prerequisites:
  - small-model-eval index built (run tests/build_small_model_eval_index.py first)
  - Ollama running with all four Ollama models pulled
  - HF_TOKEN env var set (for Gemma query embedding)

Run inside container:
  docker exec -e HF_TOKEN=hf_xxx search-web-1 python3 /code/tests/small_model_comparison.py

Output: /code/test results & reports/small_model_comparison.md
"""
import os, re, json, time, subprocess, sys, urllib.request
import numpy as np
from elasticsearch import Elasticsearch

# Must precede any huggingface import — container has no /home/appuser
_HF_CACHE = "/tmp/hf_cache"
os.environ.setdefault("HF_HOME", _HF_CACHE)
os.environ.setdefault("HUGGINGFACE_HUB_CACHE", _HF_CACHE)
os.environ.setdefault("TRANSFORMERS_CACHE", _HF_CACHE)

HF_TOKEN   = os.environ.get("HUGGING_FACE_KEY") or os.environ.get("HF_TOKEN", "")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
ES_HOST    = "http://172.31.250.10:9200"
EVAL_IDX      = "small-model-eval"
LEXICAL_INDEX = "english-mxbai"
REPORT        = "/code/test results & reports/small_model_comparison.md"

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

# ── Models ────────────────────────────────────────────────────────────────────

MODELS = [
    # ── Ollama ──────────────────────────────────────────────────────────────────
    {
        "key":       "mxbai",
        "label":     "mxbai-embed-large",
        "sublabel":  "1024-dim · 335M · F16",
        "embed_fn":  "ollama",
        "embed_id":  "mxbai-embed-large",
        "vec_field": "vec_mxbai",
    },
    {
        "key":       "nomic",
        "label":     "nomic-embed-text",
        "sublabel":  "768-dim · 137M · Ollama",
        "embed_fn":  "ollama",
        "embed_id":  "nomic-embed-text",
        "vec_field": "vec_nomic",
    },
    {
        "key":       "snowflake",
        "label":     "snowflake-arctic-embed:m",
        "sublabel":  "768-dim · 110M · Ollama",
        "embed_fn":  "ollama",
        "embed_id":  "snowflake-arctic-embed:m",
        "vec_field": "vec_snowflake",
    },
    {
        "key":       "miniLM",
        "label":     "all-MiniLM-L6-v2",
        "sublabel":  "384-dim · 22M · Ollama",
        "embed_fn":  "ollama",
        "embed_id":  "all-minilm",
        "vec_field": "vec_miniLM",
    },
    # ── sentence_transformers ────────────────────────────────────────────────────
    {
        "key":       "gemma",
        "label":     "embeddinggemma-300m",
        "sublabel":  "768-dim · 300M · base",
        "embed_fn":  "st",
        "embed_id":  "google/embeddinggemma-300m",
        "vec_field": "vec_gemma",
        "trust_remote_code": True,
    },
    {
        "key":       "gemma_q8",
        "label":     "embeddinggemma-300m-qat-q8",
        "sublabel":  "768-dim · 300M · QAT-Q8",
        "embed_fn":  "st",
        "embed_id":  "google/embeddinggemma-300m-qat-q8_0-unquantized",
        "vec_field": "vec_gemma_q8",
        "trust_remote_code": True,
    },
    {
        "key":       "gemma_q4",
        "label":     "embeddinggemma-300m-qat-q4",
        "sublabel":  "768-dim · 300M · QAT-Q4",
        "embed_fn":  "st",
        "embed_id":  "google/embeddinggemma-300m-qat-q4_0-unquantized",
        "vec_field": "vec_gemma_q4",
        "trust_remote_code": True,
    },
    {
        "key":       "mxbai_xs",
        "label":     "mxbai-embed-xsmall-v1",
        "sublabel":  "384-dim · 33M · ST",
        "embed_fn":  "st",
        "embed_id":  "mixedbread-ai/mxbai-embed-xsmall-v1",
        "vec_field": "vec_mxbai_xs",
        "trust_remote_code": False,
    },
    # ── Ollama GGUF quantized ────────────────────────────────────────────────────
    {
        "key":       "mxbai_q4km",
        "label":     "mxbai-embed-large (Q4_K_M)",
        "sublabel":  "1024-dim · 335M · Q4_K_M",
        "embed_fn":  "ollama",
        "embed_id":  "mxbai-q4km",
        "vec_field": "vec_mxbai_q4km",
    },
    # ── ONNX quantized ───────────────────────────────────────────────────────────
    {
        "key":       "mxbai_q",
        "label":     "mxbai-embed-large (INT8 ONNX)",
        "sublabel":  "1024-dim · 335M · INT8",
        "embed_fn":  "onnx",
        "embed_id":  "mixedbread-ai/mxbai-embed-large-v1",
        "onnx_file": "onnx/model_quantized.onnx",
        "vec_field": "vec_mxbai_q",
    },
    {
        "key":       "mxbai_xs_q8",
        "label":     "mxbai-embed-xsmall (INT8 ONNX)",
        "sublabel":  "384-dim · 33M · INT8",
        "embed_fn":  "onnx",
        "embed_id":  "mixedbread-ai/mxbai-embed-xsmall-v1",
        "onnx_file": "onnx/model_int8.onnx",
        "vec_field": "vec_mxbai_xs_q8",
    },
    {
        "key":       "mxbai_xs_q4",
        "label":     "mxbai-embed-xsmall (INT4 ONNX)",
        "sublabel":  "384-dim · 33M · INT4",
        "embed_fn":  "onnx",
        "embed_id":  "mixedbread-ai/mxbai-embed-xsmall-v1",
        "onnx_file": "onnx/model_q4.onnx",
        "vec_field": "vec_mxbai_xs_q4",
    },
]

# ── _matn variants (same models, englishMatn input) ───────────────────────────
# Generated automatically from MODELS — appends _matn to key and vec_field.
MODELS_MATN = []
for _m in MODELS:
    _mm = dict(_m)
    _mm["key"]       = _m["key"] + "_matn"
    _mm["label"]     = _m["label"] + " [matn]"
    _mm["vec_field"] = _m["vec_field"] + "_matn"
    MODELS_MATN.append(_mm)

# ── HF Serverless API variants ────────────────────────────────────────────────
# Same vec_fields as Ollama counterparts — only the query embed path differs.
# Used to compare local Ollama latency vs HF GPU-backed inference latency.
HF_MODELS = [
    {
        "key":       "mxbai_hf",
        "label":     "mxbai-embed-large (HF API)",
        "sublabel":  "1024-dim · 335M · HF Serverless",
        "embed_fn":  "hf_api",
        "embed_id":  "mixedbread-ai/mxbai-embed-large-v1",
        "vec_field": "vec_mxbai",
    },
    {
        "key":       "snowflake_hf",
        "label":     "snowflake-arctic-embed:m (HF API)",
        "sublabel":  "768-dim · 110M · HF Serverless",
        "embed_fn":  "hf_api",
        "embed_id":  "Snowflake/snowflake-arctic-embed-m",
        "vec_field": "vec_snowflake",
    },
    {
        "key":       "miniLM_hf",
        "label":     "all-MiniLM-L6-v2 (HF API)",
        "sublabel":  "384-dim · 22M · HF Serverless",
        "embed_fn":  "hf_api",
        "embed_id":  "sentence-transformers/all-MiniLM-L6-v2",
        "vec_field": "vec_miniLM",
    },
]

# ── Queries ───────────────────────────────────────────────────────────────────

QUERIES = [
    "good character and manners",
    "angels recording deeds",
    "prayer at night",
    "forgiving someone who wronged you",
    "comparing yourself to others",
    "aisha",
    "fasting expiation sins",
    "neighbor rights",
]

COLLECTION_BOOSTS = {
    "bukhari": 5.0, "muslim": 4.8, "nasai": 3.5, "abudawud": 3.0,
    "tirmidhi": 2.5, "ibnmajah": 2.0, "malik": 2.5, "ahmad": 2.5,
    "darimi": 2.0, "mishkat": 2.5, "nawawi40": 3.3, "riyadussalihin": 2.5,
}

N     = 10
FETCH = 50

_SHORTCODE = re.compile(r'\[/?(?:quran|narrator|prematn|matn|footnote|hadith)[^\]]*\]')

def strip_html(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    t = _SHORTCODE.sub(' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def html_escape(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ── Embedding backends ────────────────────────────────────────────────────────

def _norm(v):
    a = np.array(v, dtype=np.float32)
    n = np.linalg.norm(a)
    return (a / n).tolist() if n > 0 else a.tolist()

def embed_ollama(model_id, query):
    payload = json.dumps({"model": model_id, "input": query}).encode()
    req = urllib.request.Request(
        f"{OLLAMA_URL}/v1/embeddings",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.loads(r.read())
    return _norm(body["data"][0]["embedding"])


def embed_hf_api(model_id, query):
    """HuggingFace Serverless Inference API — feature-extraction pipeline.
    Uses GPU-backed inference on HF's servers; latency includes network round-trip."""
    if not HF_TOKEN:
        raise RuntimeError("HUGGING_FACE_KEY not set")
    payload = json.dumps({"inputs": query}).encode()
    req = urllib.request.Request(
        f"https://router.huggingface.co/hf-inference/models/{model_id}/pipeline/feature-extraction",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {HF_TOKEN}",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        body = json.loads(r.read())
    # HF returns [[vec]] for batch=1 or [vec] for single input
    vec = body[0] if isinstance(body[0], list) else body
    return _norm(vec)


# Lazy-loaded ST/ONNX state: one model at a time per process
_st_cache   = {}   # hf_repo → SentenceTransformer instance
_onnx_cache = {}   # (hf_repo, onnx_file) → (session, tokenizer)
_st_ready   = False
_onnx_ready = False
_PIP_TARGET = "/tmp/pip_extra"

def _pip_install(*packages):
    os.makedirs(_PIP_TARGET, exist_ok=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "--no-cache-dir", "-q",
                    "-t", _PIP_TARGET, *packages], check=True)
    if _PIP_TARGET not in sys.path:
        sys.path.insert(0, _PIP_TARGET)

def _ensure_st():
    global _st_ready
    if not _st_ready:
        _pip_install("sentence-transformers>=3.0", "huggingface_hub")
        _st_ready = True

def _ensure_onnx():
    global _onnx_ready
    if not _onnx_ready:
        _pip_install("onnxruntime", "transformers", "huggingface_hub")
        _onnx_ready = True

def embed_st(model_def, query):
    _ensure_st()
    from sentence_transformers import SentenceTransformer
    repo = model_def["embed_id"]
    if repo not in _st_cache:
        kwargs = {
            "trust_remote_code": model_def.get("trust_remote_code", False),
            "cache_folder": _HF_CACHE,
        }
        if HF_TOKEN:
            kwargs["token"] = HF_TOKEN
        _st_cache[repo] = SentenceTransformer(repo, **kwargs)
    model = _st_cache[repo]
    vec = model.encode([query], normalize_embeddings=True, show_progress_bar=False)[0]
    return vec.tolist()

def embed_onnx(model_def, query):
    _ensure_onnx()
    import onnxruntime as ort
    from transformers import AutoTokenizer
    from huggingface_hub import hf_hub_download

    repo  = model_def["embed_id"]
    ofile = model_def["onnx_file"]
    ckey  = (repo, ofile)
    if ckey not in _onnx_cache:
        os.makedirs(_HF_CACHE, exist_ok=True)
        path = hf_hub_download(repo, filename=ofile, token=HF_TOKEN or None,
                               cache_dir=_HF_CACHE)
        sess = ort.InferenceSession(path, providers=["CPUExecutionProvider"])
        tok  = AutoTokenizer.from_pretrained(repo, token=HF_TOKEN or None,
                                             cache_dir=_HF_CACHE)
        _onnx_cache[ckey] = (sess, tok)

    sess, tok = _onnx_cache[ckey]
    input_names = {inp.name for inp in sess.get_inputs()}
    enc = tok([query], padding=True, truncation=True, max_length=512, return_tensors="np")
    inputs = {k: v for k, v in enc.items() if k in input_names}
    outputs = sess.run(None, inputs)
    hidden = outputs[0]  # (1, S, D)
    mask   = enc["attention_mask"][:, :, None]
    v = (hidden * mask).sum(axis=1) / mask.sum(axis=1).clip(min=1)
    v = v[0].astype(np.float32)
    return _norm(v.tolist())

def embed_query(model_def, query):
    fn = model_def["embed_fn"]
    if fn == "ollama":
        return embed_ollama(model_def["embed_id"], query)
    elif fn == "st":
        return embed_st(model_def, query)
    elif fn == "onnx":
        return embed_onnx(model_def, query)
    elif fn == "hf_api":
        return embed_hf_api(model_def["embed_id"], query)
    raise ValueError(f"Unknown embed_fn: {fn}")


# ── ES kNN search ─────────────────────────────────────────────────────────────

def knn_search(vec_field, query_vec, size):
    r = es.search(
        index=EVAL_IDX,
        knn={
            "field":          vec_field,
            "query_vector":   query_vec,
            "k":              size,
            "num_candidates": size * 5,
            "filter": {"bool": {"must_not": {"term": {"isChainRef": True}}}},
        },
        size=size,
        _source=[
            "urn", "collection", "hadithNumber",
            "hadithText", "arabicText", "englishMatn",
            "isChainRef", "dupGroup", "gradeNorm", "grade",
        ],
    )
    return r["hits"]["hits"]


def bm25_search(query, n):
    try:
        r = es.search(
            index=LEXICAL_INDEX,
            size=n,
            query={"bool": {
                "filter": [{"exists": {"field": "hadithText"}}],
                "must": [{"query_string": {
                    "query": query,
                    "fields": ["hadithNumber^2", "hadithText", "arabicText", "collection^2"],
                    "type": "cross_fields",
                    "default_operator": "OR",
                }}],
            }},
            _source={"excludes": ["semantic_text"]},
        )
    except Exception:
        r = es.search(
            index=LEXICAL_INDEX,
            size=n,
            query={"bool": {
                "filter": [{"exists": {"field": "hadithText"}}],
                "must": [{"simple_query_string": {
                    "query": query,
                    "fields": ["hadithNumber^2", "hadithText", "arabicText", "collection^2"],
                }}],
            }},
            _source={"excludes": ["semantic_text"]},
        )
    return r["hits"]["hits"]


def dedup(hits, n):
    groups, singletons = {}, []
    for h in hits:
        gid = h["_source"].get("dupGroup")
        if not gid:
            singletons.append(h)
        else:
            coll = h["_source"].get("collection", "")
            key  = (COLLECTION_BOOSTS.get(coll, 1.0), h["_score"])
            if gid not in groups or key > groups[gid][1]:
                groups[gid] = (h, key)
    merged = singletons + [h for h, _ in groups.values()]
    merged.sort(key=lambda h: h["_score"], reverse=True)
    return merged[:n]


# ── Fetch all results ─────────────────────────────────────────────────────────

def check_matn_filled():
    """Return True if _matn fields are populated (>5% coverage on any field)."""
    sample = es.count(index=EVAL_IDX,
                      query={"exists": {"field": "vec_mxbai_matn"}})["count"]
    return sample > 1000

USE_MATN = check_matn_filled()
if USE_MATN:
    print("_matn fields detected — will run both hadithText and englishMatn comparisons.")
else:
    print("_matn fields not yet populated — run fill_matn_vectors.py first to enable matn comparison.")

ALL_MODEL_SETS = [("hadithText", MODELS)]
if USE_MATN:
    ALL_MODEL_SETS.append(("englishMatn", MODELS_MATN))
if HF_TOKEN:
    ALL_MODEL_SETS.append(("HF Serverless API", HF_MODELS))
else:
    print("HUGGING_FACE_KEY not set — skipping HF API section.")

# ── Warmup — load ST/ONNX weights into Python cache ──────────────────────────
# Only ST/ONNX and HF models are warmed here. Ollama models are re-touched
# immediately before each model's own query batch (see model-major loop below),
# so they never compete with each other during timed runs.
print("Loading ST/ONNX models into cache ...")
_warmed = set()
for _il, ms in ALL_MODEL_SETS:
    for m in ms:
        if m["embed_fn"] in ("ollama", "hf_api"):
            continue
        wk = (m["embed_fn"], m.get("embed_id", ""), m.get("onnx_file", ""))
        if wk not in _warmed:
            try:
                embed_query(m, "prayer")
                print(f"  loaded  [{m['key']:14s}]")
            except Exception as e:
                print(f"  warmup ERROR [{m['key']}]: {e}")
            _warmed.add(wk)
print("ST/ONNX loaded. Ollama models will be touched before each batch.")
print("")

all_results = {q: {} for q in QUERIES}

# ── BM25 baseline — no embedding, query_string on lexical index ───────────────
print("BM25 baseline ...")
for q in QUERIES:
    t1 = time.perf_counter()
    try:
        hits = bm25_search(q, FETCH)
        hits = dedup(hits, N)
        search_ms = round((time.perf_counter() - t1) * 1000)
        all_results[q]["bm25"] = {
            "hits": hits, "embed_ms": None, "search_ms": search_ms, "error": None,
        }
        print(f"  [{'bm25':14s}] '{q[:35]}' → {len(hits)} hits | search={search_ms}ms")
    except Exception as e:
        all_results[q]["bm25"] = {
            "hits": [], "embed_ms": None, "search_ms": 0, "error": str(e),
        }
        print(f"  ERROR [bm25] '{q}': {e}")

# ── Semantic models — model-major order ───────────────────────────────────────
# Running all queries for one model before switching means each Ollama model
# stays resident in Ollama's cache for its entire batch. Eviction only happens
# between models, not between queries — matching single-model production latency.
print("")
for _input_label, model_set in ALL_MODEL_SETS:
    for m in model_set:
        # Re-touch Ollama model immediately before its batch so it's warm for q[0]
        if m["embed_fn"] == "ollama":
            try:
                embed_query(m, "prayer")
                print(f"  [{m['key']:14s}] Ollama ready")
            except Exception as e:
                print(f"  [{m['key']:14s}] warmup ERROR: {e}")
        for q in QUERIES:
            try:
                t0 = time.perf_counter()
                vec = embed_query(m, q)
                embed_ms = round((time.perf_counter() - t0) * 1000)

                t1 = time.perf_counter()
                hits = knn_search(m["vec_field"], vec, FETCH)
                search_ms = round((time.perf_counter() - t1) * 1000)

                hits = dedup(hits, N)
                all_results[q][m["key"]] = {
                    "hits": hits, "embed_ms": embed_ms,
                    "search_ms": search_ms, "error": None,
                }
                print(f"  [{m['key']:14s}] '{q[:35]}' → {len(hits)} hits "
                      f"| embed={embed_ms}ms search={search_ms}ms")
            except Exception as e:
                all_results[q][m["key"]] = {
                    "hits": [], "embed_ms": 0, "search_ms": 0, "error": str(e)
                }
                print(f"  ERROR [{m['key']}] '{q}': {e}")


# ── Report ────────────────────────────────────────────────────────────────────

def _anchor(section_label, query=""):
    """GitHub-compatible anchor: lowercase, non-alphanumeric → hyphen."""
    s = (section_label + ("-" + query if query else "")).lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

lines = []
W = lines.append

# ── Table of contents ────────────────────────────────────────────────────────
W("# Small Model Comparison")
W("")
W("## Contents")
W("")
for _sec_label, _ in ALL_MODEL_SETS:
    W(f"**{_sec_label}**")
    for _q in QUERIES:
        W(f"- [{_q}](#{_anchor(_sec_label, _q)})")
    W("")
W("---")
W("")

# ── Latency summary ───────────────────────────────────────────────────────────
W("## Latency Summary")
W("")
W("Average embed + ES search time across all 8 queries (post-warmup steady state).")
W("")
W("| Model | Avg Embed | Avg Search | Avg Total |")
W("|---|---|---|---|")
_bm25_s = [all_results[q]["bm25"]["search_ms"] for q in QUERIES
           if not all_results[q]["bm25"].get("error")]
_avg_bm25 = round(sum(_bm25_s) / len(_bm25_s)) if _bm25_s else "?"
W(f"| BM25 Lexical | — | {_avg_bm25}ms | {_avg_bm25}ms |")
_hf_set = next((ms for lbl, ms in ALL_MODEL_SETS if lbl == "HF Serverless API"), [])
for _m in list(ALL_MODEL_SETS[0][1]) + list(_hf_set):
    _et = [all_results[q][_m["key"]]["embed_ms"]  for q in QUERIES
           if all_results[q].get(_m["key"]) and not all_results[q][_m["key"]].get("error")]
    _st = [all_results[q][_m["key"]]["search_ms"] for q in QUERIES
           if all_results[q].get(_m["key"]) and not all_results[q][_m["key"]].get("error")]
    if not _et:
        W(f"| {_m['label']} | ERROR | ERROR | ERROR |")
        continue
    _ae, _as = round(sum(_et) / len(_et)), round(sum(_st) / len(_st))
    W(f"| {_m['label']} | {_ae}ms | {_as}ms | {_ae + _as}ms |")
W("")
W("---")
W("")


def build_cell(model_key, rank, q):
    r    = all_results[q][model_key]
    hits = r["hits"]

    if r["error"]:
        return f"<em>ERROR: {html_escape(r['error'][:120])}</em>"
    if rank - 1 >= len(hits):
        return "<em>—</em>"

    h       = hits[rank - 1]
    s       = h["_source"]
    coll    = s.get("collection", "")
    num     = s.get("hadithNumber", "")
    score   = h["_score"]
    dup_grp = s.get("dupGroup") or ""
    grade   = s.get("gradeNorm") or s.get("grade") or ""

    ref = f"<strong>{html_escape(str(coll))} {html_escape(str(num))}</strong>&nbsp; {score:.4f}"
    if dup_grp:
        ref += f" <small>· dup:{dup_grp}</small>"
    if grade:
        ref += f" <small>· {html_escape(grade)}</small>"

    matn = strip_html(s.get("englishMatn") or "")
    full = strip_html(s.get("hadithText") or matn)

    isnad = ""
    if matn and full and matn != full:
        probe = matn[:60]
        idx   = full.find(probe)
        if idx > 5:
            isnad = full[:idx].strip()

    parts = [ref]
    if isnad:
        parts.append(f'<em><small>⛓ {html_escape(isnad[:250])}</small></em>')
    if matn:
        parts.append(html_escape(matn[:500]))
    elif full:
        parts.append(html_escape(full[:500]))

    ar = strip_html(s.get("arabicText") or "")
    if ar:
        parts.append(f'<span dir="rtl" lang="ar"><big>{html_escape(ar[:300])}</big></span>')

    return "<br><br>".join(parts)


def build_table(q, model_set):
    n     = len(model_set)
    rw    = 2
    col_w = (100 - rw) // n

    W('<table width="100%"><thead><tr>')
    W(f'<th width="{rw}%">#</th>')
    for m in model_set:
        W(f'<th width="{col_w}%"><strong>{html_escape(m["label"])}</strong><br>'
          f'<small>{html_escape(m["sublabel"])}</small></th>')
    W('</tr></thead><tbody>')

    for rank in range(1, N + 1):
        W('<tr>')
        W(f'<td align="center" valign="top"><strong>{rank}</strong></td>')
        for m in model_set:
            W(f'<td valign="top">{build_cell(m["key"], rank, q)}</td>')
        W('</tr>')

    W('</tbody></table>')
    W('')


_BOOST_NOTE = (
    "bukhari 5×, muslim 4.8×, nawawi40 3.3×, malik/ahmad/riyadussalihin 2.5×, "
    "nasai 3.5×, abudawud 3×, tirmidhi 2.5×, ibnmajah/darimi/mishkat 2×"
)

def build_section(input_label, model_set):
    backend_labels = {"ollama": "Ollama", "st": "sentence_transformers",
                      "onnx": "ONNX Runtime", "hf_api": "HF Serverless API"}
    is_hf = input_label == "HF Serverless API"

    W(f"# Small Model Comparison — {input_label}")
    W("")
    if input_label == "hadithText":
        W("Input: raw `hadithText` (isnad + matn). Identical to production semantic search.")
    elif input_label == "englishMatn":
        W("Input: `englishMatn` (matn only, isnad stripped). Same production filters/boosts as hadithText.")
        W("Compare with hadithText section to see the effect of noisy isnad chains on retrieval.")
    else:
        W("HuggingFace Serverless Inference API — GPU-backed, latency includes network round-trip.")
        W("Latency summary only (no result tables). Vectors queried against `small-model-eval`.")
    W("")

    # ── Filters & boosts table ────────────────────────────────────────────────
    W("**Filters & boosts**")
    W("")
    W("| Setting | Status |")
    W("|---|---|")
    W("| `isChainRef` exclusion | **ON** — chain-reference hadiths excluded from results |")
    W("| Dedup by `dupGroup` | **ON** — highest collection-boosted member wins per group |")
    W(f"| Collection boosts | **ON** — {_BOOST_NOTE} |")
    W("| Embed times | Post-warmup — models loaded into memory before measurement |")
    W("")

    if not is_hf:
        W("| # | Model | Vec field | Dims | Size | Backend |")
        W("|---|---|---|---|---|---|")
        for i, m in enumerate(model_set, 1):
            parts = m["sublabel"].split("·")
            W(f"| {i} | {m['label']} | `{m['vec_field']}` | "
              f"{parts[0].strip()} | "
              f"{parts[1].strip() if len(parts) > 1 else '—'} | "
              f"{backend_labels.get(m['embed_fn'], m['embed_fn'])} |")
        W("")

    W("---")
    W("")

    bm25_model = {
        "key": "bm25", "label": "BM25 Lexical",
        "sublabel": "— · no encoding · query_string", "embed_fn": "bm25", "vec_field": None,
    }
    display_set = [bm25_model] + list(model_set)

    for q in QUERIES:
        W(f"## {input_label}: {q}")
        W("")

        W("| Model | Embed | ES search |")
        W("|---|---|---|")
        r0 = all_results[q].get("bm25", {})
        W(f"| BM25 Lexical | — | {r0.get('search_ms', '?')}ms |")
        for m in model_set:
            r = all_results[q].get(m["key"], {})
            if not r or r.get("error"):
                W(f"| {m['label']} | ERROR | — |")
            else:
                W(f"| {m['label']} | {r['embed_ms']}ms | {r['search_ms']}ms |")
        W("")

        if not is_hf:
            build_table(q, display_set)
        W("---")
        W("")

    W(f"*Generated by `tests/small_model_comparison.py` · pool={FETCH} · N={N}*")
    W("")


for input_label, model_set in ALL_MODEL_SETS:
    build_section(input_label, model_set)

os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nReport written: {REPORT}")
