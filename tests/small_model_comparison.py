"""
Side-by-side comparison of small embedding models from the `small-model-eval` index.

Queries ES directly — no Flask dependency. For each query, embeds with all four
models via Ollama and runs kNN against the appropriate dense_vector field.

Models compared:
  mxbai-embed-large   (1024-dim) — prod baseline
  nomic-embed-text     (768-dim)
  snowflake-arctic-embed:m  (768-dim)
  all-MiniLM-L6-v2    (384-dim)

Prerequisites:
  - small-model-eval index built (run tests/build_small_model_eval_index.py first)
  - Ollama running with all four models pulled

Run inside container:
  docker exec search-web-1 python3 /code/tests/small_model_comparison.py

Output: /code/test results & reports/small_model_comparison.md
"""
import os, re, json, time, urllib.request, numpy as np
from elasticsearch import Elasticsearch

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
ES_HOST    = "http://172.31.250.10:9200"
EVAL_IDX   = "small-model-eval"
REPORT     = "/code/test results & reports/small_model_comparison.md"

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

# ── Models ────────────────────────────────────────────────────────────────────
MODELS = [
    {
        "key":        "mxbai",
        "label":      "mxbai-embed-large",
        "sublabel":   "1024-dim · 335M params",
        "ollama_id":  "mxbai-embed-large",
        "vec_field":  "vec_mxbai",
    },
    {
        "key":        "nomic",
        "label":      "nomic-embed-text",
        "sublabel":   "768-dim · 137M params",
        "ollama_id":  "nomic-embed-text",
        "vec_field":  "vec_nomic",
    },
    {
        "key":        "snowflake",
        "label":      "snowflake-arctic-embed:m",
        "sublabel":   "768-dim · 110M params",
        "ollama_id":  "snowflake-arctic-embed:m",
        "vec_field":  "vec_snowflake",
    },
    {
        "key":        "miniLM",
        "label":      "all-MiniLM-L6-v2",
        "sublabel":   "384-dim · 22M params",
        "ollama_id":  "all-minilm",
        "vec_field":  "vec_miniLM",
    },
]

# ── Queries ───────────────────────────────────────────────────────────────────
# Mix of conceptual, person-based, practice-specific, and abstract —
# chosen to expose retrieval quality differences between models.
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

N     = 10   # results to display per model
FETCH = 50   # pool size before dedup/filter

_SHORTCODE = re.compile(r'\[/?(?:quran|narrator|prematn|matn|footnote|hadith)[^\]]*\]')

def strip_html(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    t = _SHORTCODE.sub(' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def html_escape(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ── Ollama ────────────────────────────────────────────────────────────────────

def embed_query(ollama_id, query):
    payload = json.dumps({"model": ollama_id, "input": query}).encode()
    req = urllib.request.Request(
        f"{OLLAMA_URL}/v1/embeddings",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.loads(r.read())
    vec = np.array(body["data"][0]["embedding"], dtype=np.float32)
    norm = np.linalg.norm(vec)
    return (vec / norm).tolist() if norm > 0 else vec.tolist()


# ── ES kNN search ─────────────────────────────────────────────────────────────

def knn_search(vec_field, query_vec, size):
    r = es.search(
        index=EVAL_IDX,
        knn={
            "field":        vec_field,
            "query_vector": query_vec,
            "k":            size,
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

print("Embedding queries and searching...")
all_results = {}   # {query: {model_key: {hits, embed_ms, search_ms, error}}}

for q in QUERIES:
    all_results[q] = {}
    for m in MODELS:
        try:
            t0 = time.perf_counter()
            vec = embed_query(m["ollama_id"], q)
            embed_ms = round((time.perf_counter() - t0) * 1000)

            t1 = time.perf_counter()
            hits = knn_search(m["vec_field"], vec, FETCH)
            search_ms = round((time.perf_counter() - t1) * 1000)

            hits = dedup(hits, N)
            all_results[q][m["key"]] = {
                "hits": hits, "embed_ms": embed_ms,
                "search_ms": search_ms, "error": None,
            }
            print(f"  [{m['key']:12s}] '{q[:35]}' → {len(hits)} hits | embed={embed_ms}ms search={search_ms}ms")
        except Exception as e:
            all_results[q][m["key"]] = {"hits": [], "embed_ms": 0, "search_ms": 0, "error": str(e)}
            print(f"  ERROR [{m['key']}] '{q}': {e}")


# ── Report ────────────────────────────────────────────────────────────────────

lines = []
W = lines.append


def build_cell(model_key, rank, q):
    r    = all_results[q][model_key]
    hits = r["hits"]

    if r["error"]:
        return f"<em>ERROR: {html_escape(r['error'][:100])}</em>"
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

    # Show stripped isnad prefix in grey
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
    rw    = 3
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


W("# Small Model Comparison")
W("")
W("Single `small-model-eval` index — four dense_vector fields, one per model.")
W("All models embed `englishMatn` (isnad-stripped) when available, else `hadithText`.")
W("")
W("| Model | Ollama ID | Dims | Params |")
W("|---|---|---|---|")
for m in MODELS:
    W(f"| {m['label']} | `{m['ollama_id']}` | {m['sublabel'].split('·')[0].strip()} | {m['sublabel'].split('·')[1].strip()} |")
W("")
W("*Filters: isChainRef=true excluded · Dedup ON (collection-boost priority)*")
W("")
W("---")
W("")

for q in QUERIES:
    W(f"## Query: \"{q}\"")
    W("")

    # Latency table
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
