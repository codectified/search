"""
Side-by-side comparison of small Ollama-backed embedding models vs mxbai.

Models:
  mxbai              mxbai-embed-large (1024-dim)   — current prod baseline
  nomic              nomic-embed-text  (768-dim)
  snowflake-arctic-m snowflake-arctic-embed:m (768-dim)
  all-minilm         all-MiniLM-L6-v2  (384-dim)

Prerequisites — pull models in Ollama before indexing:
  ollama pull nomic-embed-text
  ollama pull snowflake-arctic-embed:m
  ollama pull all-minilm

Build indexes:
  http://localhost:5001/index?password=index123&targets=nomic,all-minilm,snowflake-arctic-m

Run inside container:
  docker exec search-web-1 python3 /code/tests/small_model_comparison.py

Output: /code/test results & reports/small_model_comparison.md
"""
import urllib.request, urllib.parse, json, re, time, os
from elasticsearch import Elasticsearch

BASE   = "http://localhost:5000"
REPORT = "/code/test results & reports/small_model_comparison.md"

ES_HOST = "http://172.31.250.10:9200"
es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

# ── Queries ───────────────────────────────────────────────────────────────────
# Chosen to exercise different retrieval challenges:
#   conceptual/abstract, person-based, ritual/practice, negative framing, short
QUERIES = [
    "good character and manners",          # virtue — lots of hadiths, hard to rank well
    "angels recording deeds",             # specific concept, moderate vocabulary overlap
    "prayer at night",                    # common ritual query
    "forgiving someone who wronged you",  # abstract/relational
    "comparing yourself to others",       # abstract, low keyword overlap with hadiths
    "aisha",                              # person-based, high recall needed
    "fasting expiation sins",             # practice + consequence
    "neighbor rights",                    # social/ethical concept
]

MODELS = ["mxbai", "nomic", "snowflake-arctic-m", "all-minilm"]

MODEL_LABEL = {
    "mxbai":              "mxbai-embed-large<br><small>1024-dim · 335M params</small>",
    "nomic":              "nomic-embed-text<br><small>768-dim · 137M params</small>",
    "snowflake-arctic-m": "snowflake-arctic-embed:m<br><small>768-dim · 110M params</small>",
    "all-minilm":         "all-MiniLM-L6-v2<br><small>384-dim · 22M params</small>",
}

COLLECTION_BOOSTS = {
    "bukhari": 5.0, "muslim": 4.8, "nasai": 3.5, "abudawud": 3.0,
    "tirmidhi": 2.5, "ibnmajah": 2.0, "malik": 2.5, "ahmad": 2.5,
    "darimi": 2.0, "mishkat": 2.5, "nawawi40": 3.3, "riyadussalihin": 2.5,
}

N      = 10   # results to show per model
FETCH  = 50   # fetch pool before dedup/filter

_SHORTCODE = re.compile(r'\[/?(?:quran|narrator|prematn|matn|footnote|hadith)[^\]]*\]')

def strip_html(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    t = _SHORTCODE.sub(' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def html_escape(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def search_api(model, query, size):
    url = (BASE + "/en/search"
           + "?q="    + urllib.parse.quote(query)
           + "&mode=semantic"
           + "&model=" + model
           + "&size=" + str(size))
    t0 = time.perf_counter()
    with urllib.request.urlopen(url, timeout=120) as r:
        body = json.loads(r.read())
    wall_ms = round((time.perf_counter() - t0) * 1000)
    hits = body.get("hits", {}).get("hits", [])
    return hits, wall_ms


def dedup_hits(hits, n):
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


def chain_filter(hits):
    return [h for h in hits if not h["_source"].get("isChainRef")]


# ── Prefetch Arabic text ───────────────────────────────────────────────────────
def get_arabic_text(collection, hadith_number):
    try:
        r = es.search(index="english-mxbai", size=1,
            query={"bool": {"must": [
                {"term": {"collection": collection}},
                {"term": {"hadithNumber": str(hadith_number)}},
            ]}},
            _source=["arabicText"])
        hits = r["hits"]["hits"]
        if hits:
            return strip_html(hits[0]["_source"].get("arabicText") or "")
    except Exception:
        pass
    return ""


# ── Fetch ─────────────────────────────────────────────────────────────────────
print("Fetching results...")
all_results = {}   # {query: {model: {hits, wall_ms, error}}}

for q in QUERIES:
    all_results[q] = {}
    for model in MODELS:
        try:
            hits, wall_ms = search_api(model, q, FETCH)
            hits = chain_filter(hits)
            hits = dedup_hits(hits, N)
            all_results[q][model] = {"hits": hits, "wall_ms": wall_ms, "error": None}
            print(f"  [{model:20s}] '{q[:40]}': {len(hits)} hits | {wall_ms}ms")
        except Exception as e:
            all_results[q][model] = {"hits": [], "wall_ms": 0, "error": str(e)}
            print(f"  ERROR [{model}] '{q}': {e}")


# ── Prefetch Arabic text ───────────────────────────────────────────────────────
print("Fetching Arabic text...")
arabic_cache = {}

for q in QUERIES:
    for model in MODELS:
        for h in all_results[q][model]["hits"]:
            s   = h["_source"]
            key = (s.get("collection", ""), str(s.get("hadithNumber", "")))
            if key not in arabic_cache:
                arabic_cache[key] = get_arabic_text(*key)


# ── Build report ───────────────────────────────────────────────────────────────
lines = []
W = lines.append


def build_cell(model, rank, q):
    r    = all_results[q][model]
    hits = r["hits"]

    if r["error"]:
        return f"<em>ERROR: {html_escape(r['error'][:80])}</em>"
    if rank - 1 >= len(hits):
        return "<em>—</em>"

    h       = hits[rank - 1]
    s       = h["_source"]
    coll    = s.get("collection", "")
    num     = s.get("hadithNumber", "")
    score   = h["_score"]
    dup_grp = s.get("dupGroup") or ""

    ref = f"<strong>{html_escape(str(coll))} {html_escape(str(num))}</strong>&nbsp; {score:.4f}"
    if dup_grp:
        ref += f" <small>· dup:{dup_grp}</small>"

    matn = strip_html(s.get("englishMatn") or "")
    full = strip_html(s.get("hadithText") or s.get("englishText") or matn)

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

    ar = arabic_cache.get((coll, str(num)), "")
    if ar:
        parts.append(f'<span dir="rtl" lang="ar"><big>{html_escape(ar[:350])}</big></span>')

    return "<br><br>".join(parts)


def build_table(q):
    n     = len(MODELS)
    rw    = 4
    col_w = (100 - rw) // n

    W('<table width="100%"><thead><tr>')
    W(f'<th width="{rw}%">#</th>')
    for m in MODELS:
        W(f'<th width="{col_w}%">{MODEL_LABEL[m]}</th>')
    W('</tr></thead><tbody>')

    for rank in range(1, N + 1):
        W('<tr>')
        W(f'<td align="center" valign="top"><strong>{rank}</strong></td>')
        for m in MODELS:
            W(f'<td valign="top">{build_cell(m, rank, q)}</td>')
        W('</tr>')

    W('</tbody></table>')
    W('')


W("# Small Model Comparison")
W("")
W("Evaluating small Ollama-backed embedding models as prod candidates for `english-mxbai`.")
W("")
W("| Model | Dims | Params | Ollama pull |")
W("|---|---|---|---|")
W("| mxbai-embed-large | 1024 | ~335M | `mxbai-embed-large` (baseline) |")
W("| nomic-embed-text | 768 | ~137M | `nomic-embed-text` |")
W("| snowflake-arctic-embed:m | 768 | ~110M | `snowflake-arctic-embed:m` |")
W("| all-MiniLM-L6-v2 | 384 | ~22M | `all-minilm` |")
W("")
W("*Filters: chain-ref OFF · Dedup ON · `englishMatn` shown (isnad stripped)*")
W("")
W("---")
W("")

for q in QUERIES:
    W(f"## Query: \"{q}\"")
    W("")
    lat = " · ".join(
        f"**{m}** {all_results[q][m]['wall_ms']}ms"
        for m in MODELS if not all_results[q][m]["error"]
    )
    W(f"*Latency: {lat}*  ")
    W("")
    build_table(q)
    W("---")
    W("")

W(f"*Generated by `tests/small_model_comparison.py` · pool={FETCH} · N={N}*")

os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nReport written: {REPORT}")
