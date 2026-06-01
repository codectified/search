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

HF_TOKEN   = os.environ.get("HF_TOKEN", "")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
ES_HOST    = "http://172.31.250.10:9200"
EVAL_IDX   = "small-model-eval"
REPORT     = "/code/test results & reports/small_model_comparison.md"

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

print("Embedding queries and searching ...")
all_results = {}   # {query: {model_key: {hits, embed_ms, search_ms, error}}}

for q in QUERIES:
    all_results[q] = {}
    for m in MODELS:
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
            print(f"  [{m['key']:12s}] '{q[:35]}' → {len(hits)} hits "
                  f"| embed={embed_ms}ms search={search_ms}ms")
        except Exception as e:
            all_results[q][m["key"]] = {
                "hits": [], "embed_ms": 0, "search_ms": 0, "error": str(e)
            }
            print(f"  ERROR [{m['key']}] '{q}': {e}")


# ── Report ────────────────────────────────────────────────────────────────────

lines = []
W = lines.append


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


def build_table(q):
    n     = len(MODELS)
    rw    = 2
    col_w = (100 - rw) // n

    W('<table width="100%"><thead><tr>')
    W(f'<th width="{rw}%">#</th>')
    for m in MODELS:
        W(f'<th width="{col_w}%"><strong>{html_escape(m["label"])}</strong><br>'
          f'<small>{html_escape(m["sublabel"])}</small></th>')
    W('</tr></thead><tbody>')

    for rank in range(1, N + 1):
        W('<tr>')
        W(f'<td align="center" valign="top"><strong>{rank}</strong></td>')
        for m in MODELS:
            W(f'<td valign="top">{build_cell(m["key"], rank, q)}</td>')
        W('</tr>')

    W('</tbody></table>')
    W('')


# ── Header ────────────────────────────────────────────────────────────────────
W("# Small Model Comparison — Full Sweep")
W("")
W("Single `small-model-eval` index. All models embed raw `hadithText` (same input for fair comparison).")
W("")
W("| # | Model | Vec field | Dims | Size | Backend |")
W("|---|---|---|---|---|---|")
backend_labels = {"ollama": "Ollama", "st": "sentence_transformers", "onnx": "ONNX Runtime"}
for i, m in enumerate(MODELS, 1):
    W(f"| {i} | {m['label']} | `{m['vec_field']}` | "
      f"{m['sublabel'].split('·')[0].strip()} | "
      f"{m['sublabel'].split('·')[1].strip()} | "
      f"{backend_labels.get(m['embed_fn'], m['embed_fn'])} |")
W("")
W("*Filters: isChainRef=true excluded · Dedup ON (collection-boost priority)*")
W("")
W("---")
W("")

# ── Per-query sections ────────────────────────────────────────────────────────
for q in QUERIES:
    W(f"## Query: \"{q}\"")
    W("")

    W("| Model | Embed | kNN search |")
    W("|---|---|---|")
    for m in MODELS:
        r = all_results[q][m["key"]]
        if r["error"]:
            W(f"| {m['label']} | ERROR | — |")
        else:
            W(f"| {m['label']} | {r['embed_ms']}ms | {r['search_ms']}ms |")
    W("")

    build_table(q)
    W("---")
    W("")

W(f"*Generated by `tests/small_model_comparison.py` · pool={FETCH} · N={N}*")

os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nReport written: {REPORT}")
