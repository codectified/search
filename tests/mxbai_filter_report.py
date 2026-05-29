"""
Comprehensive comparison report for the english-mxbai index.

Tests three orthogonal dimensions:
  1. Chain-ref filter ON vs OFF  — do bare isnad hadiths pollute results?
  2. Dedup ON vs OFF             — how many chain/collection duplicates are collapsed?
  3. Size effect on HNSW         — does requesting more results change the top-N?

Writes: /code/test results & reports/mxbai_filter_report.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/mxbai_filter_report.py
"""
import os, re, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

ES_HOST  = "http://172.31.250.10:9200"
INDEX    = "english-mxbai"
FIELD    = "semantic_text"
REPORT   = "/code/test results & reports/mxbai_filter_report.md"

QUERIES = [
    "comparing yourself to others",
    "forgiveness of sins",
    "prayer before sleeping",
    "fasting in Ramadan",
    "visiting the sick",
    "honoring one's parents",
    "This hadith has been narrated",   # deliberate chain-ref trap query
]

SIZES = [5, 10, 20, 50]

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

# ── helpers ───────────────────────────────────────────────────────────────────

COLLECTION_BOOSTS = {
    "bukhari": 5.0, "muslim": 4.8, "nasai": 3.5, "abudawud": 3.0,
    "tirmidhi": 2.5, "ibnmajah": 2.0, "malik": 2.5, "ahmad": 2.5,
    "darimi": 2.0, "mishkat": 2.5, "nawawi40": 3.3, "riyadussalihin": 2.5,
}

CHAIN_FILTER = {"bool": {"must_not": {"term": {"isChainRef": True}}}}


def strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


def build_query(user_query, chain_filter=True, extra_filters=None):
    filters = []
    if chain_filter:
        filters.append(CHAIN_FILTER)
    if extra_filters:
        filters.extend(extra_filters)
    return {
        "bool": {
            "filter": filters,
            "must": [{"semantic": {"field": FIELD, "query": user_query}}],
        }
    }


def search(query_text, size, chain_filter=True):
    t0 = time.perf_counter()
    result = es.options(request_timeout=60).search(
        index=INDEX, size=size,
        query=build_query(query_text, chain_filter=chain_filter),
        _source={"excludes": [FIELD]},
    )
    ms = round((time.perf_counter() - t0) * 1000)
    hits = result["hits"]["hits"]
    return hits, ms


def dedup_hits(hits, size):
    groups = {}
    singletons = []
    for h in hits:
        gid = h["_source"].get("dupGroup", 0)
        if gid == 0:
            singletons.append(h)
        else:
            coll = h["_source"].get("collection", "")
            key = (COLLECTION_BOOSTS.get(coll, 1.0), h["_score"])
            if gid not in groups or key > groups[gid][1]:
                groups[gid] = (h, key)
    merged = singletons + [h for h, _ in groups.values()]
    merged.sort(key=lambda h: h["_score"], reverse=True)
    return merged[:size]


def fmt_hit(h, rank):
    s = h["_source"]
    text = strip_html(s.get("hadithText", ""))[:110]
    ic = "⚠CHAIN" if s.get("isChainRef") else ""
    dg = f"dup={s['dupGroup']}" if s.get("dupGroup") else ""
    tags = " ".join(filter(None, [ic, dg]))
    tags_str = f" `[{tags}]`" if tags else ""
    return f"| {rank} | {h['_score']:.3f} | {s.get('collection','')} {s.get('hadithNumber','')} |{tags_str} {text} |"


def hit_key(h):
    s = h["_source"]
    return (s.get("collection", ""), str(s.get("hadithNumber", "")))


# ── fetch index stats ──────────────────────────────────────────────────────────

total       = es.count(index=INDEX)["count"]
chain_count = es.count(index=INDEX, body={"query": {"term": {"isChainRef": True}}})["count"]
dup_count   = es.count(index=INDEX, body={"query": {"range": {"dupGroup": {"gt": 0}}}})["count"]

# ── build report ──────────────────────────────────────────────────────────────

lines = []
W = lines.append

W("# mxbai Filter & Dedup Report\n")
W(f"Index: `{INDEX}` | Total docs: {total:,}\n")
W(f"- Chain-ref docs (`isChainRef=True`): **{chain_count:,}** ({chain_count/total*100:.1f}%)")
W(f"- Docs in a dup group (`dupGroup>0`): **{dup_count:,}** ({dup_count/total*100:.1f}%)\n")
W("---\n")

# ═══════════════════════════════════════════════════════════
# SECTION 1: Chain-ref filter ON vs OFF
# ═══════════════════════════════════════════════════════════
W("## 1. Chain-ref filter: ON vs OFF\n")
W("Chain-reference hadiths have no matn content — they're isnad-variant notes like "
  "*\"This hadith has been narrated through another chain of transmitters.\"* "
  "Without the filter these can rank highly for queries whose terms appear in that phrase.\n")

for q in QUERIES:
    W(f"### Query: *\"{q}\"*\n")

    hits_off, ms_off = search(q, size=10, chain_filter=False)
    hits_on,  ms_on  = search(q, size=10, chain_filter=True)

    chains_in_raw = [h for h in hits_off if h["_source"].get("isChainRef")]
    W(f"Chain-refs in top-10 (filter OFF): **{len(chains_in_raw)}** | "
      f"filter OFF: {ms_off}ms | filter ON: {ms_on}ms\n")

    W("**Filter OFF** (raw — chain-refs highlighted)")
    W("| # | Score | Collection Hadith# | Tags | Text |")
    W("|---|---|---|---|---|")
    for i, h in enumerate(hits_off[:10], 1):
        W(fmt_hit(h, i))

    W("\n**Filter ON**")
    W("| # | Score | Collection Hadith# | Tags | Text |")
    W("|---|---|---|---|---|")
    for i, h in enumerate(hits_on[:10], 1):
        W(fmt_hit(h, i))
    W("")

W("---\n")

# ═══════════════════════════════════════════════════════════
# SECTION 2: Dedup ON vs OFF
# ═══════════════════════════════════════════════════════════
W("## 2. Dedup: ON vs OFF\n")
W("Dedup collapses near-identical hadiths (`dupGroup>0`, cosine>0.93 in the english-openai "
  "index). Within each group the member with the highest collection authority wins "
  "(Bukhari > Muslim > … using COLLECTION_BOOSTS, score as tiebreaker).\n")

for q in QUERIES[:6]:   # skip the trap query for dedup section
    W(f"### Query: *\"{q}\"*\n")

    raw_hits, ms_raw   = search(q, size=30, chain_filter=True)
    deduped            = dedup_hits(raw_hits, 10)

    dup_hits_raw  = [h for h in raw_hits[:10] if h["_source"].get("dupGroup", 0)]
    collapsed     = len(raw_hits) - len(deduped)  # rough proxy
    groups_shown  = len({h["_source"].get("dupGroup", 0) for h in deduped if h["_source"].get("dupGroup")})

    W(f"Raw top-10: {len([h for h in raw_hits[:10] if h['_source'].get('dupGroup',0)])} hits "
      f"belonged to a dup group | After dedup: {len(deduped)} results, {groups_shown} groups represented\n")

    W("**Dedup OFF** (raw top-10, chain-refs excluded)")
    W("| # | Score | Collection Hadith# | DupGroup | Text |")
    W("|---|---|---|---|---|")
    for i, h in enumerate(raw_hits[:10], 1):
        s = h["_source"]
        dg = s.get("dupGroup", 0) or "—"
        text = strip_html(s.get("hadithText", ""))[:100]
        W(f"| {i} | {h['_score']:.3f} | {s.get('collection','')} {s.get('hadithNumber','')} | {dg} | {text} |")

    W("\n**Dedup ON** (collection-boosted representative per group)")
    W("| # | Score | Collection Hadith# | DupGroup | Text |")
    W("|---|---|---|---|---|")
    for i, h in enumerate(deduped, 1):
        s = h["_source"]
        dg = s.get("dupGroup", 0) or "—"
        text = strip_html(s.get("hadithText", ""))[:100]
        W(f"| {i} | {h['_score']:.3f} | {s.get('collection','')} {s.get('hadithNumber','')} | {dg} | {text} |")
    W("")

W("---\n")

# ═══════════════════════════════════════════════════════════
# SECTION 3: Size effect on HNSW result quality
# ═══════════════════════════════════════════════════════════
W("## 3. Size effect on HNSW traversal\n")
W("The ES `semantic_text` query uses HNSW approximate nearest-neighbor internally. "
  "Requesting a larger `size` forces the HNSW graph walker to explore further, "
  "which can surface hadiths that a smaller traversal misses entirely. "
  "This table shows which top-10 results *change* as size increases.\n")
W("> Dedup=ON throughout (fetch_size = size × 3). Chain-ref filter=ON.\n")

for q in QUERIES[:6]:
    W(f"### Query: *\"{q}\"*\n")

    size_results = {}
    for sz in SIZES:
        raw, ms = search(q, size=sz * 3, chain_filter=True)
        deduped = dedup_hits(raw, sz)
        size_results[sz] = (deduped, ms)

    # Show latency table
    W("**Latency** (fetch_size = size × 3, then deduped)")
    W("| size | fetch_size | latency |")
    W("|---|---|---|")
    for sz in SIZES:
        _, ms = size_results[sz]
        W(f"| {sz} | {sz*3} | {ms}ms |")

    W("\n**Top-10 result stability across sizes**")
    W("Shows rank position (or — if absent) for each hadith across different size values.\n")

    # Collect all unique hadiths seen in top-10 across all sizes
    all_keys = {}
    for sz in SIZES:
        for rank, h in enumerate(size_results[sz][0][:10], 1):
            k = hit_key(h)
            if k not in all_keys:
                s = h["_source"]
                all_keys[k] = strip_html(s.get("hadithText", ""))[:80]

    W("| Collection/# | Text | " + " | ".join(f"size={sz}" for sz in SIZES) + " |")
    W("|---|---|" + "|".join("---" for _ in SIZES) + "|")

    for k, text in all_keys.items():
        ranks = []
        for sz in SIZES:
            hits_sz = size_results[sz][0][:10]
            pos = next((str(i) for i, h in enumerate(hits_sz, 1) if hit_key(h) == k), "—")
            ranks.append(pos)
        W(f"| {k[0]} {k[1]} | {text} | " + " | ".join(ranks) + " |")

    # Highlight first-appearance ranks (hadiths that only appear at larger sizes)
    latecomers = []
    base_keys = {hit_key(h) for h in size_results[SIZES[0]][0][:10]}
    for sz in SIZES[1:]:
        new_keys = {hit_key(h) for h in size_results[sz][0][:10]} - base_keys
        for k in new_keys:
            for h in size_results[sz][0][:10]:
                if hit_key(h) == k:
                    latecomers.append((sz, h))
                    break
        base_keys |= new_keys

    if latecomers:
        W(f"\n**New hadiths surfaced at larger sizes** (not in size={SIZES[0]} top-10):")
        for sz, h in latecomers:
            s = h["_source"]
            text = strip_html(s.get("hadithText", ""))[:100]
            W(f"- First seen at size={sz}: **{s.get('collection','')} {s.get('hadithNumber','')}** "
              f"(score {h['_score']:.3f}) — {text}")
    else:
        W(f"\n*Top-10 fully stable across all sizes for this query.*")
    W("")

W("---\n")
W(f"*Generated by `tests/mxbai_filter_report.py`*\n")

# ── write ─────────────────────────────────────────────────────────────────────
os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report written: {REPORT}")
print(f"Index stats: {total:,} total | {chain_count:,} chain-refs | {dup_count:,} in dup groups")
