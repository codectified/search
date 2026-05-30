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

# English-side models (embed English matn, look up Arabic from arabic-openai)
EN_MODELS  = ["mxbai", "english-openai", "english-openai-large"]
# Multilingual / Arabic-side models
ML_MODELS  = ["arabic-openai", "arabic-openai-large",
               "multilingual-e5", "bge-m3", "qwen3-embed"]

ALL_MODELS = EN_MODELS + ML_MODELS

N      = 10   # valid results to show per model
FETCH  = 50   # fetch pool — large enough that N survive filtering/dedup

COLLECTION_BOOSTS = {
    "bukhari": 5.0, "muslim": 4.8, "nasai": 3.5, "abudawud": 3.0,
    "tirmidhi": 2.5, "ibnmajah": 2.0, "malik": 2.5, "ahmad": 2.5,
    "darimi": 2.0, "mishkat": 2.5, "nawawi40": 3.3, "riyadussalihin": 2.5,
}

MODEL_LABEL = {
    "mxbai":               "Mixedbread",
    "english-openai":      "English OpenAI (small)",
    "english-openai-large": "English OpenAI (large)",
    "arabic-openai":       "Arabic OpenAI (small)",
    "arabic-openai-large": "Arabic OpenAI (large)",
    "multilingual-e5":     "E5 Multilingual",
    "bge-m3":              "BGE-M3",
    "qwen3-embed":         "Qwen3-Embed",
}


def strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


def cell_safe(t):
    """Escape pipe characters and replace newlines for use in a markdown table cell."""
    return t.replace("|", "\\|").replace("\n", " ")


def search_api(model, query, size):
    url = (BASE + "/en/search"
           + "?q="     + urllib.parse.quote(query)
           + "&model="  + model
           + "&mode=semantic"
           + "&size="   + str(size))
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


# ── Prefetch Arabic text for English-side models ───────────────────────────────
# arabic-side / multilingual models store arabicMatn directly in the source doc.
print("Fetching Arabic text for English-side model results...")
arabic_text_cache = {}

for q in QUERIES:
    for model in EN_MODELS:
        for h in all_results[q][model]["hits"]:
            s   = h["_source"]
            key = (s.get("collection", ""), str(s.get("hadithNumber", "")))
            if key not in arabic_text_cache:
                arabic_text_cache[key] = get_arabic_text(*key)


# ── Build report ───────────────────────────────────────────────────────────────
lines = []
W = lines.append

# Models whose Arabic text comes from source doc directly
ARABIC_IN_SOURCE = set(ML_MODELS)


def build_cell(model, rank, q):
    r    = all_results[q][model]
    hits = r["hits"]

    if r["error"]:
        return f"*ERROR: {r['error'][:80]}*"
    if rank - 1 >= len(hits):
        return "—"

    h = hits[rank - 1]
    s = h["_source"]

    coll    = s.get("collection", "")
    num     = s.get("hadithNumber", "")
    score   = h["_score"]
    dup_grp = s.get("dupGroup") or ""

    ref_line = f"**`{coll} {num}`** &nbsp; {score:.4f}"
    if dup_grp:
        ref_line += f" · dup:{dup_grp}"

    en_text = cell_safe(strip_html(s.get("hadithText") or s.get("englishText") or
                                   s.get("englishMatn") or ""))

    if model in ARABIC_IN_SOURCE:
        ar_raw = strip_html(s.get("arabicMatn") or s.get("arabicText") or "")
    else:
        ar_raw = arabic_text_cache.get((coll, str(num)), "")
    ar_text = cell_safe(ar_raw)

    parts = [ref_line]
    if en_text:
        parts.append(en_text)
    if ar_text:
        parts.append(f"*{ar_text}*")

    return "<br><br>".join(parts)


def build_table(models, q):
    W("| Rank | " + " | ".join(MODEL_LABEL[m] for m in models) + " |")
    W("|:---:|" + "|".join("---" for _ in models) + "|")
    for rank in range(1, N + 1):
        cells = [f"**{rank}**"] + [build_cell(m, rank, q) for m in models]
        W("| " + " | ".join(cells) + " |")
    W("")


W("# Focused Comparison")
W("")
W("Queries: **\"aisha\"** · **\"comparing yourself to others\"**")
W("")
W("## Models and filters")
W("")
W("| Model | Corpus | Search method | Chain-ref filter | Dedup | Pool → results |")
W("|---|---|---|---|---|---|")
W(f"| **Mixedbread** | English matn (48,703) | Full HNSW | API | API | {FETCH} → {N} |")
W(f"| **English OpenAI (small)** | English matn (48,703) | Full HNSW | API | API | {FETCH} → {N} |")
W(f"| **English OpenAI (large)** | English matn (48,703) | Full HNSW / centroid if ready | API | API | {FETCH} → {N} |")
W(f"| **Arabic OpenAI (small)** | Arabic matn, translated 44,896 | Centroid k=75 → HNSW | API | Client-side | {FETCH} → {N} |")
W(f"| **Arabic OpenAI (large)** | Arabic matn, 131,728 | Centroid → HNSW | API | Client-side | {FETCH} → {N} |")
W(f"| **E5 Multilingual** | Shared EN+AR corpus 180,430 | Centroid → HNSW | API | API | {FETCH} → {N} |")
W(f"| **BGE-M3** | Shared EN+AR corpus 180,430 | Centroid → HNSW | API | API | {FETCH} → {N} |")
W(f"| **Qwen3-Embed** | Shared EN+AR corpus 180,430 | Centroid → HNSW | API | API | {FETCH} → {N} |")
W("")
W("---")
W("")

for q in QUERIES:
    W(f"# Query: \"{q}\"")
    W("")

    # Latency row
    lat_parts = [f"**{MODEL_LABEL[m]}** {all_results[q][m]['wall_ms']}ms"
                 for m in ALL_MODELS if not all_results[q][m]["error"]]
    W("**Latency:** " + " · ".join(lat_parts) + "  ")

    # Cluster info for centroid models
    for m in ["arabic-openai", "arabic-openai-large", "multilingual-e5", "bge-m3", "qwen3-embed"]:
        clusters = all_results[q][m]["meta"].get("clusters")
        if clusters:
            W(f"**{MODEL_LABEL[m]} clusters:** {clusters}  ")
    W("")

    W("## English-side models")
    W("")
    build_table(EN_MODELS, q)

    W("## Multilingual / Arabic-side models")
    W("")
    build_table(ML_MODELS, q)

    W("---")
    W("")

W(f"*Generated by `tests/focused_comparison.py` · pool={FETCH} · N={N}*")

# ── Write report ───────────────────────────────────────────────────────────────
os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nReport written: {REPORT}")
