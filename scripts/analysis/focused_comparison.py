"""
Focused side-by-side comparison for the two priority queries:
  - "aisha"
  - "comparing yourself to others"

Eight semantic models compared — split into two groups:

  English-side (embed English matn):
    mxbai, english-openai, english-openai-large

  Multilingual / Arabic-side:
    arabic-openai, arabic-openai-large,
    multilingual-e5, bge-m3, qwen3-embed

Report format:
  - Two tables per query (English-side / Multilingual-side)
  - RANK as rows, MODEL as columns
  - Each cell: reference + score, full English text, Arabic text
  - Filters and dedup applied consistently

Filters:
  - Chain-ref filter ON for all models
  - Dedup ON for all models

Writes: /code/test results & reports/focused_comparison.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/focused_comparison.py
"""
import urllib.request, urllib.parse, json, re, time, os
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

BASE   = "http://localhost:5000"
REPORT = "/code/test results & reports/focused_comparison.md"
INDEX_ARABIC = "arabic-openai"

ES_HOST = "http://172.31.250.10:9200"
es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

QUERIES = ["aisha", "comparing yourself to others"]

# Table 1: BM25 + mxbai (clean/dirty) — the lexical-vs-semantic story
MXBAI_MODELS = ["english-lexical", "mxbai-dirty", "mxbai"]
# Table 2: English OpenAI (small + large)
EN_OPENAI_MODELS = ["english-openai", "english-openai-large"]
# Table 3: Arabic / Multilingual OpenAI
ML_MODELS = ["arabic-openai", "arabic-openai-large",
             "multilingual-e5", "bge-m3", "qwen3-embed"]

# Flat list for fetching — order matters for the English-side Arabic text lookup
EN_MODELS  = MXBAI_MODELS + EN_OPENAI_MODELS
ALL_MODELS = EN_MODELS + ML_MODELS

N      = 10   # valid results to show per model
FETCH  = 50   # fetch pool — large enough that N survive filtering/dedup

COLLECTION_BOOSTS = {
    "bukhari": 5.0, "muslim": 4.8, "nasai": 3.5, "abudawud": 3.0,
    "tirmidhi": 2.5, "ibnmajah": 2.0, "malik": 2.5, "ahmad": 2.5,
    "darimi": 2.0, "mishkat": 2.5, "nawawi40": 3.3, "riyadussalihin": 2.5,
}

MODEL_LABEL = {
    "english-lexical":     "BM25 Lexical (full text)",
    "mxbai-dirty":         "Mixedbread (dirty — full hadithText)",
    "mxbai":               "Mixedbread (clean matn)",
    "english-openai":      "English OpenAI small (clean matn)",
    "english-openai-large": "English OpenAI large (clean matn)",
    "arabic-openai":       "Arabic OpenAI (small)",
    "arabic-openai-large": "Arabic OpenAI (large)",
    "multilingual-e5":     "E5 Multilingual",
    "bge-m3":              "BGE-M3",
    "qwen3-embed":         "Qwen3-Embed",
}


_SHORTCODE = re.compile(r'\[/?(?:quran|narrator|prematn|matn|footnote|hadith)[^\]]*\]')

def strip_html(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    t = _SHORTCODE.sub(' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def html_escape(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def extract_isnad_prefix(full_text, clean_matn):
    """Return the isnad prefix that was stripped, or empty string."""
    full  = (full_text or "").strip()
    matn  = (clean_matn or "").strip()
    if not full or not matn or full == matn:
        return ""
    probe = matn[:60]
    idx   = full.find(probe)
    if idx > 5:
        return full[:idx].strip()
    return ""


def search_api(model, query, size):
    mode = "lexical" if model == "english-lexical" else "semantic"
    url = (BASE + "/en/search"
           + "?q="    + urllib.parse.quote(query)
           + "&mode=" + mode
           + "&size=" + str(size))
    if mode == "semantic":
        url += "&model=" + model
    t0 = time.perf_counter()
    with urllib.request.urlopen(url, timeout=120) as r:
        body = json.loads(r.read())
    wall_ms = round((time.perf_counter() - t0) * 1000)
    hits = body.get("hits", {}).get("hits", [])
    meta = body.get("_meta", {})
    return hits, meta, wall_ms


def dedup_hits(hits, n, boosts):
    """Collapse dup groups (keep best-collection representative), return top-n."""
    groups, singletons = {}, []
    for h in hits:
        gid = h["_source"].get("dupGroup", 0)
        if not gid:
            singletons.append(h)
        else:
            coll = h["_source"].get("collection", "")
            key  = (boosts.get(coll, 1.0), h["_score"])
            if gid not in groups or key > groups[gid][1]:
                groups[gid] = (h, key)
    merged = singletons + [h for h, _ in groups.values()]
    merged.sort(key=lambda h: h["_score"], reverse=True)
    return merged[:n]


def chain_filter(hits):
    return [h for h in hits if not h["_source"].get("isChainRef")]


def get_arabic_text(collection, hadith_number):
    """Look up arabicMatn from arabic-openai index by collection+hadithNumber."""
    try:
        r = es.search(index=INDEX_ARABIC, size=1,
            query={"bool": {"must": [
                {"term": {"collection": collection}},
                {"term": {"hadithNumber": str(hadith_number)}},
            ]}},
            _source=["arabicMatn", "arabicText"])
        hits = r["hits"]["hits"]
        if hits:
            s = hits[0]["_source"]
            return strip_html(s.get("arabicMatn") or s.get("arabicText") or "")
    except Exception:
        pass
    return ""


def get_english_text_by_id(doc_id):
    """Look up englishMatn + hadithText from english-mxbai by _id.
    Used for models whose source docs don't store text (english-openai-large).
    Returns (matn, full_text).
    """
    try:
        r = es.get(index="english-mxbai", id=doc_id,
                   _source=["englishMatn", "hadithText"])
        s = r["_source"]
        return (strip_html(s.get("englishMatn") or ""),
                strip_html(s.get("hadithText") or ""))
    except Exception:
        pass
    return ("", "")


def get_english_text_by_urn(english_urn):
    """Look up englishMatn + hadithText from english-mxbai by englishURN.
    Used for Arabic-side model results.
    Returns (matn, full_text).
    """
    if not english_urn:
        return ("", "")
    try:
        doc_id = f"en:{english_urn}"
        r = es.get(index="english-mxbai", id=doc_id,
                   _source=["englishMatn", "hadithText"])
        s = r["_source"]
        return (strip_html(s.get("englishMatn") or ""),
                strip_html(s.get("hadithText") or ""))
    except Exception:
        pass
    return ("", "")


# ── Fetch all results ──────────────────────────────────────────────────────────
print("Fetching results...")
all_results = {}

for q in QUERIES:
    all_results[q] = {}
    for model in ALL_MODELS:
        try:
            hits, meta, wall_ms = search_api(model, q, FETCH)
            hits = chain_filter(hits)
            hits = dedup_hits(hits, N, COLLECTION_BOOSTS)
            all_results[q][model] = {
                "hits": hits[:N],
                "meta": meta,
                "wall_ms": wall_ms,
                "error": None,
            }
            print(f"  [{model}] '{q}': {len(hits[:N])} results | wall={wall_ms}ms | meta={meta}")
        except Exception as e:
            all_results[q][model] = {"hits": [], "meta": {}, "wall_ms": 0, "error": str(e)}
            print(f"  ERROR [{model}] '{q}': {e}")


# ── Prefetch Arabic text for English-side models ──────────────────────────────
print("Fetching Arabic text for English-side model results...")
arabic_text_cache = {}   # {(coll, num): ar_text}

for q in QUERIES:
    for model in EN_MODELS:
        for h in all_results[q][model]["hits"]:
            s   = h["_source"]
            key = (s.get("collection", ""), str(s.get("hadithNumber", "")))
            if key not in arabic_text_cache:
                arabic_text_cache[key] = get_arabic_text(*key)

# ── Prefetch English text for models without text in source ───────────────────
# english-openai-large docs store no text — look up by _id from english-mxbai.
# Arabic-side models have englishText (full) but need englishMatn for clean display.
print("Fetching English text for sparse/Arabic-side model results...")
english_by_id  = {}    # {doc_id: (matn, full_text)} — for english-openai-large
english_by_urn = {}    # {urn:    (matn, full_text)} — for ML_MODELS

TEXT_SPARSE_MODELS = {"english-openai-large"}

for q in QUERIES:
    for model in ALL_MODELS:
        for h in all_results[q][model]["hits"]:
            s      = h["_source"]
            doc_id = h["_id"]
            urn    = s.get("englishURN") or s.get("urn")

            if model in TEXT_SPARSE_MODELS and doc_id not in english_by_id:
                english_by_id[doc_id] = get_english_text_by_id(doc_id)

            if model in set(ML_MODELS) and urn and urn not in english_by_urn:
                english_by_urn[urn] = get_english_text_by_urn(urn)


# ── Build report ───────────────────────────────────────────────────────────────
lines = []
W = lines.append

ARABIC_IN_SOURCE = set(ML_MODELS)


def resolve_english(model, h):
    """Return (matn, full_text) for a hit, regardless of model type."""
    s      = h["_source"]
    doc_id = h["_id"]
    urn    = s.get("englishURN") or s.get("urn")

    if model in TEXT_SPARSE_MODELS:
        return english_by_id.get(doc_id, ("", ""))
    elif model in ARABIC_IN_SOURCE:
        matn, full = english_by_urn.get(urn, ("", ""))
        if not full:
            full = strip_html(s.get("englishText") or "")
        return (matn, full)
    elif model == "english-lexical":
        full = strip_html(s.get("hadithText") or s.get("englishText") or "")
        return (full, full)   # no clean matn for lexical; show full as-is
    else:
        matn = strip_html(s.get("englishMatn") or "")
        full = strip_html(s.get("hadithText") or s.get("englishText") or matn)
        return (matn, full)


def build_html_cell(model, rank, q):
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

    matn, full = resolve_english(model, h)

    parts = [ref]

    # Isnad prefix (what the parser stripped)
    if model != "english-lexical":
        isnad = extract_isnad_prefix(full, matn)
        if isnad:
            parts.append(f'<em><small>⛓ {html_escape(isnad[:300])}</small></em>')

    # Clean matn (or full text for lexical)
    if matn:
        parts.append(html_escape(matn[:600]))
    elif full:
        parts.append(html_escape(full[:600]))

    # Arabic text
    if model in ARABIC_IN_SOURCE:
        ar = strip_html(s.get("arabicMatn") or s.get("arabicText") or "")
    else:
        ar = arabic_text_cache.get((coll, str(num)), "")
    if ar:
        parts.append(f'<span dir="rtl" lang="ar"><big>{html_escape(ar[:400])}</big></span>')

    return "<br><br>".join(parts)


def build_html_table(models, q):
    n      = len(models)
    rank_w = 4
    col_w  = (100 - rank_w) // n

    W('<table width="100%"><thead><tr>')
    W(f'<th width="{rank_w}%">#</th>')
    for m in models:
        W(f'<th width="{col_w}%">{html_escape(MODEL_LABEL[m])}</th>')
    W('</tr></thead><tbody>')

    for rank in range(1, N + 1):
        W('<tr>')
        W(f'<td align="center" valign="top"><strong>{rank}</strong></td>')
        for m in models:
            W(f'<td valign="top">{build_html_cell(m, rank, q)}</td>')
        W('</tr>')

    W('</tbody></table>')
    W('')


W("# Focused Comparison")
W("")
W("Queries: **\"aisha\"** · **\"comparing yourself to others\"**")
W("")
W("## Models")
W("")
W("| Model | Text embedded | Isnad stripped | Search method | Pool → shown |")
W("|---|---|---|---|---|")
W(f"| **BM25 Lexical** | `hadithText` full text | ✗ | BM25 full-text | {FETCH} → {N} |")
W(f"| **Mixedbread dirty** | `hadithText` full text | ✗ | Semantic HNSW (mxbai-embed-large) | {FETCH} → {N} |")
W(f"| **Mixedbread clean** | `englishMatn` clean matn | ✓ | Semantic HNSW (mxbai-embed-large) | {FETCH} → {N} |")
W(f"| **English OpenAI small** | `englishMatn` clean matn | ✓ | Centroid k=75 → HNSW | {FETCH} → {N} |")
W(f"| **English OpenAI large** | `englishMatn` clean matn | ✓ | Centroid k=150 → HNSW | {FETCH} → {N} |")
W(f"| **Arabic OpenAI small** | `arabicMatn` (44,896 translated) | ✓* | Centroid k=75 → HNSW | {FETCH} → {N} |")
W(f"| **Arabic OpenAI large** | `arabicMatn` (131,728 all) | ✓* | Centroid k=150 → HNSW | {FETCH} → {N} |")
W(f"| **E5 Multilingual** | `englishMatn` + `arabicMatn` shared | ✓ | Centroid k=75 → HNSW | {FETCH} → {N} |")
W("")
W("\\* Arabic matn extraction: ~94% clean via HTML matn tags, ~5.7% have residual shortcode tags — re-embed fix pending.")
W("")
W("*Chain-ref filter ON · Dedup ON · English text shown is `englishMatn` (isnad-stripped) for all models*")
W("")
W("---")
W("")

for q in QUERIES:
    W(f"# Query: \"{q}\"")
    W("")

    # Latency row — only working models
    lat_parts = [f"**{MODEL_LABEL[m]}** {all_results[q][m]['wall_ms']}ms"
                 for m in ALL_MODELS if not all_results[q][m]["error"]]
    W("**Latency:** " + " · ".join(lat_parts) + "  ")

    # Cluster info for centroid models
    for m in ["arabic-openai", "arabic-openai-large", "multilingual-e5", "bge-m3", "qwen3-embed"]:
        clusters = all_results[q][m]["meta"].get("clusters")
        if clusters:
            W(f"**{MODEL_LABEL[m]} clusters:** {clusters}  ")
    W("")

    W("## BM25 · Mixedbread")
    W("")
    build_html_table(MXBAI_MODELS, q)

    W("## English OpenAI")
    W("")
    build_html_table(EN_OPENAI_MODELS, q)

    W("## Arabic / Multilingual OpenAI")
    W("")
    build_html_table(ML_MODELS, q)

    W("---")
    W("")

W(f"*Generated by `tests/focused_comparison.py` · pool={FETCH} · N={N}*")

# ── Write report ───────────────────────────────────────────────────────────────
os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nReport written: {REPORT}")
