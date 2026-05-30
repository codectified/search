"""
Focused side-by-side comparison for the two priority queries:
  - "aisha"
  - "comparing yourself to others"

Three semantic models compared:
  - mxbai          (English matn vectors, full HNSW, chain-ref + dedup ON)
  - english-openai (English matn vectors, full HNSW, chain-ref + dedup ON)
  - arabic-openai  (Arabic matn vectors, translated centroids k=75, englishText filter)

Report format:
  - Grouped by RANK (not by model) for direct side-by-side evaluation
  - English text primary, Arabic text secondary
  - Full hadith text (no artificial truncation)
  - Metadata (collection, number, score, clusters) on header line

Filters:
  - Chain-ref filter ON for all models
  - Dedup ON for all models (when filtered results reduce top-N, pool is extended)

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

QUERIES  = ["aisha", "comparing yourself to others"]
MODELS   = ["mxbai", "english-openai", "arabic-openai"]
N        = 10   # valid results to show per model
FETCH    = 50   # fetch pool — large enough that N survive filtering/dedup

COLLECTION_BOOSTS = {
    "bukhari": 5.0, "muslim": 4.8, "nasai": 3.5, "abudawud": 3.0,
    "tirmidhi": 2.5, "ibnmajah": 2.0, "malik": 2.5, "ahmad": 2.5,
    "darimi": 2.0, "mishkat": 2.5, "nawawi40": 3.3, "riyadussalihin": 2.5,
}


def strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


def search_api(model, query, size):
    url = (BASE + "/en/search"
           + "?q="     + urllib.parse.quote(query)
           + "&model="  + model
           + "&mode=semantic"
           + "&size="   + str(size))
    t0 = time.perf_counter()
    with urllib.request.urlopen(url, timeout=60) as r:
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
    for model in MODELS:
        try:
            hits, meta, wall_ms = search_api(model, q, FETCH)

            # Apply chain-ref filter (mxbai/english-openai handle internally,
            # but arabic-openai may not — belt-and-suspenders)
            hits = chain_filter(hits)

            # Apply dedup (mxbai/english-openai already deduped by API,
            # but arabic-openai doesn't dedup — apply here for consistency)
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


# ── Prefetch Arabic text for all non-arabic-openai results ────────────────────
print("Fetching Arabic text for mxbai and english-openai results...")
arabic_text_cache = {}

for q in QUERIES:
    for model in ["mxbai", "english-openai"]:
        for h in all_results[q][model]["hits"]:
            s   = h["_source"]
            key = (s.get("collection", ""), str(s.get("hadithNumber", "")))
            if key not in arabic_text_cache:
                arabic_text_cache[key] = get_arabic_text(*key)


# ── Build report ───────────────────────────────────────────────────────────────
lines = []
W = lines.append

W("# Focused Comparison — Rank-by-Rank")
W("")
W("Queries: **\"aisha\"** · **\"comparing yourself to others\"**  ")
W("Filters: chain-ref ON · dedup ON · extended pool to maintain N=10 valid results per model  ")
W("")
W("| Model | Corpus | Method | Filters |")
W("|---|---|---|---|")
W("| **mxbai** | English matn | Full HNSW (48,703 docs) | chain-ref + dedup |")
W("| **english-openai** | English matn | Full HNSW (48,703 docs) | chain-ref + dedup |")
W("| **arabic-openai** | Arabic matn | Translated centroids k=75 (44,896 docs) | englishText + dedup |")
W("")
W("---")
W("")

MODEL_LABEL = {
    "mxbai":          "Mixedbread",
    "english-openai": "English OpenAI",
    "arabic-openai":  "Arabic OpenAI",
}

for q in QUERIES:
    W(f"# Query: \"{q}\"")
    W("")

    # Latency summary
    latencies = []
    for model in MODELS:
        r = all_results[q][model]
        latencies.append(f"**{MODEL_LABEL[model]}** {r['wall_ms']}ms")
    W("**Latency:** " + " · ".join(latencies))
    W("")

    # Rank-by-rank
    for rank in range(1, N + 1):
        W(f"## Rank {rank}")
        W("")

        for model in MODELS:
            r    = all_results[q][model]
            hits = r["hits"]
            meta = r["meta"]

            if r["error"]:
                W(f"### {MODEL_LABEL[model]}")
                W(f"> ERROR: {r['error']}")
                W("")
                continue

            if rank - 1 >= len(hits):
                W(f"### {MODEL_LABEL[model]}")
                W("> *(no result at this rank)*")
                W("")
                continue

            h = hits[rank - 1]
            s = h["_source"]

            coll     = s.get("collection", "")
            num      = s.get("hadithNumber", "")
            score    = h["_score"]
            dup_grp  = s.get("dupGroup") or ""
            clusters = meta.get("clusters", "")
            cluster_str = f" · clusters: {clusters}" if clusters else ""
            dup_str     = f" · dup-rep: {dup_grp}" if dup_grp else ""

            # Header line: model name + metadata
            W(f"### {MODEL_LABEL[model]} &nbsp;&nbsp; `{coll} {num}` &nbsp; score: {score:.4f}{cluster_str}{dup_str}")
            W("")

            # English text (primary)
            en_text = strip_html(s.get("hadithText") or s.get("englishText") or "")
            if en_text:
                W(en_text)
                W("")

            # Arabic text (secondary)
            if model == "arabic-openai":
                ar_text = strip_html(s.get("arabicMatn") or s.get("arabicText") or "")
            else:
                key     = (coll, str(num))
                ar_text = arabic_text_cache.get(key, "")

            if ar_text:
                W(f"**Arabic:** {ar_text}")
                W("")

        W("---")
        W("")

    W("")

# ── Summary table ──────────────────────────────────────────────────────────────
W("# Summary — Top-3 per Query")
W("")
for q in QUERIES:
    W(f"## \"{q}\"")
    W("")
    W(f"| Rank | {' | '.join(MODEL_LABEL[m] for m in MODELS)} |")
    W(f"|---|{'|'.join('---' for _ in MODELS)}|")
    for rank in range(1, 4):
        row = [f"**{rank}**"]
        for model in MODELS:
            hits = all_results[q][model]["hits"]
            if rank - 1 < len(hits):
                h = hits[rank - 1]
                s = h["_source"]
                ref  = f"{s.get('collection','')} {s.get('hadithNumber','')}"
                text = strip_html(s.get("hadithText") or s.get("englishText", ""))[:80]
                row.append(f"`{ref}` {text}")
            else:
                row.append("—")
        W("| " + " | ".join(row) + " |")
    W("")

W("---")
W(f"*Generated by `tests/focused_comparison.py`*")

# ── Write report ───────────────────────────────────────────────────────────────
os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nReport written: {REPORT}")
