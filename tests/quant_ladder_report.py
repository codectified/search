"""
mxbai-embed-large quantization ladder: latency vs retrieval quality.

Six variants of mxbai, same model family, stepped from full-precision down to
aggressively quantized — all querying the same small-model-eval ES index.

Ladder (large → small):
  F16     mxbai-embed-large F16        Ollama        1024-dim  335M
  Q4_K_M  mxbai-embed-large Q4_K_M    Ollama GGUF   1024-dim  335M
  INT8    mxbai-embed-large INT8       ONNX Runtime  1024-dim  335M
  XS-FP32 mxbai-embed-xsmall FP32     SentenceTransf 384-dim   33M
  XS-INT8 mxbai-embed-xsmall INT8     ONNX Runtime   384-dim   33M
  XS-INT4 mxbai-embed-xsmall INT4     ONNX Runtime   384-dim   33M

Run inside container:
  docker exec search-web-1 python3 /code/tests/quant_ladder_report.py

Output: /code/test results & reports/quant_ladder_report.md
"""
import os, re, json, time, subprocess, sys, urllib.request
import numpy as np
from elasticsearch import Elasticsearch

_HF_CACHE = "/tmp/hf_cache"
os.environ.setdefault("HF_HOME", _HF_CACHE)
os.environ.setdefault("HUGGINGFACE_HUB_CACHE", _HF_CACHE)
os.environ.setdefault("TRANSFORMERS_CACHE", _HF_CACHE)

OLLAMA_URL    = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
ES_HOST       = "http://172.31.250.10:9200"
EVAL_IDX      = "small-model-eval"
LEXICAL_INDEX = "english-mxbai"
REPORT        = "/code/test results & reports/quant_ladder_report.md"

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

# ── Ladder definition ─────────────────────────────────────────────────────────
LADDER = [
    {
        "key": "f16",
        "label": "mxbai-large F16",
        "sublabel": "1024-dim · 335M · Ollama (F16)",
        "embed_fn": "ollama",
        "embed_id": "mxbai-embed-large",
        "vec_field": "vec_mxbai",
        "note": "Production baseline. Full float16 weights via Ollama.",
    },
    {
        "key": "q4km",
        "label": "mxbai-large Q4_K_M",
        "sublabel": "1024-dim · 335M · Ollama GGUF",
        "embed_fn": "ollama",
        "embed_id": "mxbai-q4km",
        "vec_field": "vec_mxbai_q4km",
        "note": "4-bit GGUF quantization via llama.cpp. Smaller on disk, but Ollama still runs on CPU — no speedup expected.",
    },
    {
        "key": "int8",
        "label": "mxbai-large INT8 ONNX",
        "sublabel": "1024-dim · 335M · ONNX Runtime",
        "embed_fn": "onnx",
        "embed_id": "mixedbread-ai/mxbai-embed-large-v1",
        "onnx_file": "onnx/model_quantized.onnx",
        "vec_field": "vec_mxbai_q",
        "note": "INT8 dynamic quantization exported to ONNX. Same model, same dims — much faster inference on CPU.",
    },
    {
        "key": "xs_fp32",
        "label": "mxbai-xsmall FP32",
        "sublabel": "384-dim · 33M · SentenceTransformers",
        "embed_fn": "st",
        "embed_id": "mixedbread-ai/mxbai-embed-xsmall-v1",
        "vec_field": "vec_mxbai_xs",
        "note": "10× smaller model. Different dim (384 vs 1024). Vectors indexed separately.",
    },
    {
        "key": "xs_int8",
        "label": "mxbai-xsmall INT8 ONNX",
        "sublabel": "384-dim · 33M · ONNX Runtime",
        "embed_fn": "onnx",
        "embed_id": "mixedbread-ai/mxbai-embed-xsmall-v1",
        "onnx_file": "onnx/model_int8.onnx",
        "vec_field": "vec_mxbai_xs_q8",
        "note": "INT8 xsmall — closest analog to FP8 that ONNX Runtime supports on CPU.",
    },
    {
        "key": "xs_int4",
        "label": "mxbai-xsmall INT4 ONNX",
        "sublabel": "384-dim · 33M · ONNX Runtime",
        "embed_fn": "onnx",
        "embed_id": "mixedbread-ai/mxbai-embed-xsmall-v1",
        "onnx_file": "onnx/model_q4.onnx",
        "vec_field": "vec_mxbai_xs_q4",
        "note": "INT4 xsmall — maximum compression.",
    },
]

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

_st_cache = {}
_onnx_cache = {}
_st_ready = _onnx_ready = False
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
    import sentence_transformers as st
    repo = model_def["embed_id"]
    if repo not in _st_cache:
        _st_cache[repo] = st.SentenceTransformer(repo, cache_folder=_HF_CACHE)
    return _norm(_st_cache[repo].encode(query).tolist())

def embed_onnx(model_def, query):
    _ensure_onnx()
    import onnxruntime as ort
    from transformers import AutoTokenizer
    from huggingface_hub import hf_hub_download

    repo  = model_def["embed_id"]
    ofile = model_def["onnx_file"]
    ckey  = (repo, ofile)
    if ckey not in _onnx_cache:
        onnx_path = hf_hub_download(repo_id=repo, filename=ofile, cache_dir=_HF_CACHE)
        tok  = AutoTokenizer.from_pretrained(repo, cache_dir=_HF_CACHE)
        sess = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])
        _onnx_cache[ckey] = (sess, tok)
    sess, tok = _onnx_cache[ckey]
    enc = tok(query, return_tensors="np", padding=True, truncation=True, max_length=512)
    out = sess.run(None, {k: v for k, v in enc.items() if k in
                          [i.name for i in sess.get_inputs()]})
    token_embs = out[0]
    att  = enc["attention_mask"]
    mask = att[..., None].astype(np.float32)
    vec  = (token_embs * mask).sum(1) / mask.sum(1)
    return _norm(vec[0].tolist())

def embed_query(m, query):
    fn = m["embed_fn"]
    if fn == "ollama": return embed_ollama(m["embed_id"], query)
    if fn == "st":     return embed_st(m, query)
    if fn == "onnx":   return embed_onnx(m, query)
    raise ValueError(f"Unknown embed_fn: {fn}")

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
            index=LEXICAL_INDEX, size=n,
            query={"bool": {
                "filter": [{"exists": {"field": "hadithText"}}],
                "must": [{"query_string": {
                    "query": query,
                    "fields": ["hadithNumber^2", "hadithText", "arabicText", "collection^2"],
                    "type": "cross_fields", "default_operator": "OR",
                }}],
            }},
            _source={"excludes": ["semantic_text"]},
        )
    except Exception:
        r = es.search(
            index=LEXICAL_INDEX, size=n,
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

# ── Warmup — load ST/ONNX weights into Python cache ──────────────────────────
print("Loading ST/ONNX models into cache ...")
_warmed = set()
for m in LADDER:
    if m["embed_fn"] == "ollama":
        continue
    wk = (m["embed_fn"], m.get("embed_id", ""), m.get("onnx_file", ""))
    if wk not in _warmed:
        try:
            embed_query(m, "prayer")
            print(f"  loaded  [{m['key']:10s}]")
        except Exception as e:
            print(f"  ERROR   [{m['key']}]: {e}")
        _warmed.add(wk)
print("ST/ONNX loaded. Ollama models will be touched before each batch.")
print("")

# ── Run all queries — model-major order ───────────────────────────────────────
# Each model runs all 8 queries before switching, so Ollama never evicts a model
# mid-batch. Re-touch immediately before each Ollama model's batch.
results = {q: {} for q in QUERIES}

print("BM25 baseline ...")
for q in QUERIES:
    t0 = time.perf_counter()
    try:
        hits = bm25_search(q, FETCH)
        hits = dedup(hits, N)
        results[q]["bm25"] = {"hits": hits, "embed_ms": None,
                               "search_ms": round((time.perf_counter() - t0) * 1000), "error": None}
        print(f"  [{'bm25':10s}] '{q[:35]}' → {len(hits)} hits | search={results[q]['bm25']['search_ms']}ms")
    except Exception as e:
        results[q]["bm25"] = {"hits": [], "embed_ms": None, "search_ms": 0, "error": str(e)}

print("")
for m in LADDER:
    if m["embed_fn"] == "ollama":
        try:
            embed_query(m, "prayer")
            print(f"  [{m['key']:10s}] Ollama ready")
        except Exception as e:
            print(f"  [{m['key']:10s}] warmup ERROR: {e}")
    for q in QUERIES:
        try:
            t0 = time.perf_counter()
            vec = embed_query(m, q)
            embed_ms = round((time.perf_counter() - t0) * 1000)
            t1 = time.perf_counter()
            hits = knn_search(m["vec_field"], vec, FETCH)
            hits = dedup(hits, N)
            search_ms = round((time.perf_counter() - t1) * 1000)
            results[q][m["key"]] = {"hits": hits, "embed_ms": embed_ms,
                                     "search_ms": search_ms, "error": None}
            print(f"  [{m['key']:10s}] '{q[:35]}' → {len(hits)} hits | embed={embed_ms}ms search={search_ms}ms")
        except Exception as e:
            results[q][m["key"]] = {"hits": [], "embed_ms": 0, "search_ms": 0, "error": str(e)}
            print(f"  ERROR [{m['key']}] '{q[:35]}': {e}")

# ── Build report ──────────────────────────────────────────────────────────────
def _anchor(label, query=""):
    s = (label + ("-" + query if query else "")).lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

lines = []
W = lines.append

W("# mxbai Quantization Ladder")
W("")
W("Six variants of `mxbai-embed-large` / `mxbai-embed-xsmall`, stepped from full F16")
W("through GGUF 4-bit down to ONNX INT4. All variants query the `small-model-eval`")
W("index (48,702 docs); BM25 on `english-mxbai` is the lexical baseline.")
W("")

# ── TOC ───────────────────────────────────────────────────────────────────────
W("## Contents")
W("")
W("**Summary**")
W("")
W("- [Methodology](#methodology)")
W("- [Latency Summary](#latency-summary)")
W("")
W("**Results**")
W("")
for q in QUERIES:
    W(f"- [{q}](#{_anchor('query', q)})")
W("")
W("---")
W("")

# ── Methodology ───────────────────────────────────────────────────────────────
W("## Methodology")
W("")
W("### What is timed")
W("")
W("Each query runs through two measured steps. Timing is wall-clock via `time.perf_counter()`.")
W("")
W("| Field | What is measured |")
W("|---|---|")
W("| **Embed (ms)** | Tokenisation + forward pass on CPU, or the Ollama HTTP round-trip to `host.docker.internal:11434`. Network to ES is excluded. |")
W("| **ES search (ms)** | The ES kNN call: HNSW graph traversal with `num_candidates=250`, `isChainRef` filter applied inside kNN, post-retrieval `dupGroup` dedup, and network to/from the ES container. |")
W("| **Total (ms)** | Embed + search. End-to-end for a single query, excluding model load time. |")
W("")
W("BM25 (`query_string` on `english-mxbai`) has no embed step — total equals search time only.")
W("")
W("### Warmup protocol")
W("")
W("**ONNX / ST models** are loaded into the Python process cache (`_onnx_cache`, `_st_cache`)")
W("before any timed query runs. The first call downloads weights and initialises the ONNX")
W("runtime session; all timed queries use the already-loaded session.")
W("")
W("**Ollama models** are re-touched (one dummy embed call) immediately before each model's")
W("timed batch. This causes Ollama to load that model into its in-memory serving layer.")
W("Subsequent queries for that model are served from RAM.")
W("")
W("> Post-warmup means weights are in memory. Numbers do not include cold-start load time")
W("> — roughly 200 ms for small ONNX models, 1–3 s for large Ollama models from disk.")
W("")
W("### Loop order and Ollama cache")
W("")
W("The script uses **model-major** order: all 8 queries for one model complete before")
W("switching to the next. This ladder has only 2 Ollama models (F16 + Q4_K_M), so both")
W("can stay resident in Ollama's cache simultaneously — there is no inter-query eviction.")
W("")
W("This is different from the full small-model comparison, where 5 Ollama models compete")
W("and evict each other between queries, adding ~440 ms reload overhead per switch.")
W("**The numbers here are more representative of single-model production latency.**")
W("")
W("Speedup column is relative to F16 embed time (embed dominates for CPU inference).")
W("")
W("### Filters and collection boosts")
W("")
W("All runs use production-equivalent settings:")
W("")
W("| Setting | Value |")
W("|---|---|")
W("| `isChainRef` exclusion | **ON** — chain-reference hadiths removed from kNN candidates via filter |")
W("| Candidate pool | `num_candidates=250`, `k=50`, then dedup to top 10 |")
W("| Dedup by `dupGroup` | **ON** — highest collection-boosted member wins per duplicate group |")
W("| Collection boosts | bukhari 5×, muslim 4.8×, nawawi40 3.3×, nasai 3.5×, abudawud 3×, tirmidhi/malik/ahmad/riyadussalihin 2.5×, ibnmajah/darimi/mishkat 2× |")
W("")
W("---")
W("")

# ── Latency Summary ───────────────────────────────────────────────────────────
W("## Latency Summary")
W("")
W("Post-warmup averages across 8 queries. See [Methodology](#methodology) for how these are measured.")
W("")

_BACKEND_LABELS = {
    "ollama": "Ollama", "st": "SentenceTransformers",
    "onnx": "ONNX Runtime", "hf_api": "HF Serverless",
}

# Compute averages
bm25_st = [results[q]["bm25"]["search_ms"] for q in QUERIES if not results[q]["bm25"].get("error")]
avg_bm25 = round(sum(bm25_st) / len(bm25_st)) if bm25_st else "?"

# Reference = F16 embed time for speedup column
f16_times = [results[q]["f16"]["embed_ms"] for q in QUERIES if results[q].get("f16") and not results[q]["f16"].get("error")]
avg_f16_embed = sum(f16_times) / len(f16_times) if f16_times else 1

W("| Step | Model | Dims | Backend | Avg Embed | Avg Search | Avg Total | Speedup vs F16 |")
W("|---|---|---|---|---|---|---|---|")
W(f"| — | BM25 Lexical | — | ES query_string | — | {avg_bm25}ms | {avg_bm25}ms | — |")

for i, m in enumerate(LADDER, 1):
    et = [results[q][m["key"]]["embed_ms"] for q in QUERIES
          if results[q].get(m["key"]) and not results[q][m["key"]].get("error")]
    st_ = [results[q][m["key"]]["search_ms"] for q in QUERIES
           if results[q].get(m["key"]) and not results[q][m["key"]].get("error")]
    if not et:
        W(f"| {i} | {m['label']} | — | — | ERROR | ERROR | ERROR | — |")
        continue
    ae = round(sum(et) / len(et))
    as_ = round(sum(st_) / len(st_))
    speedup = f"{avg_f16_embed / ae:.1f}×" if ae > 0 else "—"
    if m["key"] == "f16":
        speedup = "baseline"
    _parts = m["sublabel"].split("·")
    _dims = _parts[0].strip() if _parts else "—"
    _backend = _BACKEND_LABELS.get(m["embed_fn"], m["embed_fn"])
    W(f"| {i} | {m['label']} | {_dims} | {_backend} | {ae}ms | {as_}ms | {ae + as_}ms | {speedup} |")

W("")
W("---")
W("")

# ── Per-query results ─────────────────────────────────────────────────────────
W("## Per-Query Results")
W("")

ALL_MODELS_DISPLAY = [
    {"key": "bm25", "label": "BM25 Lexical", "sublabel": "no encoding · query_string"},
] + LADDER

def build_cell(model_key, rank, q):
    r    = results[q][model_key]
    hits = r["hits"]
    if r.get("error"):
        return f"<em>ERROR: {html_escape(r['error'][:100])}</em>"
    if rank - 1 >= len(hits):
        return "<em>—</em>"

    h     = hits[rank - 1]
    s     = h["_source"]
    coll  = s.get("collection", "")
    num   = s.get("hadithNumber", "")
    score = h["_score"]
    grade = s.get("gradeNorm") or s.get("grade") or ""
    dup   = s.get("dupGroup") or ""

    ref = f"<strong>{html_escape(str(coll))} {html_escape(str(num))}</strong>&nbsp; {score:.4f}"
    if dup:   ref += f" <small>· dup:{dup}</small>"
    if grade: ref += f" <small>· {html_escape(grade)}</small>"

    matn = strip_html(s.get("englishMatn") or "")
    full = strip_html(s.get("hadithText") or matn)
    isnad = ""
    if matn and full and matn != full:
        idx = full.find(matn[:60])
        if idx > 5:
            isnad = full[:idx].strip()

    parts = [ref]
    if matn:
        parts.append(html_escape(matn[:150]))
    elif full:
        parts.append(html_escape(full[:150]))
    return "<br><br>".join(parts)

def build_table(q):
    rw    = 2
    col_w = (100 - rw) // len(ALL_MODELS_DISPLAY)
    W('<table width="100%"><thead><tr>')
    W(f'<th width="{rw}%">#</th>')
    for m in ALL_MODELS_DISPLAY:
        W(f'<th width="{col_w}%"><strong>{html_escape(m["label"])}</strong>'
          f'<br><small>{html_escape(m["sublabel"])}</small></th>')
    W('</tr></thead><tbody>')
    for rank in range(1, N + 1):
        W('<tr>')
        W(f'<td align="center" valign="top"><strong>{rank}</strong></td>')
        for m in ALL_MODELS_DISPLAY:
            W(f'<td valign="top">{build_cell(m["key"], rank, q)}</td>')
        W('</tr>')
    W('</tbody></table>')
    W('')

for q in QUERIES:
    W(f"## Query: {q}")
    W("")

    # Per-query latency mini-table
    W("| Model | Embed | ES search |")
    W("|---|---|---|")
    r0 = results[q].get("bm25", {})
    W(f"| BM25 Lexical | — | {r0.get('search_ms', '?')}ms |")
    for m in LADDER:
        r = results[q].get(m["key"], {})
        if not r or r.get("error"):
            W(f"| {m['label']} | ERROR | — |")
        else:
            W(f"| {m['label']} | {r['embed_ms']}ms | {r['search_ms']}ms |")
    W("")

    build_table(q)
    W("---")
    W("")

W(f"*Generated by `tests/quant_ladder_report.py` · pool={FETCH} · N={N}*")
W("")

os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"\nReport written: {REPORT}")
