"""
Comprehensive mxbai HNSW size + filter report.

For each query shows:
  - Filter combinations: no filters | chain-ref only | dedup only | both (production)
  - Size sweep: 10, 20, 30, 50, 75, 100  (production is 75)

Priority queries: "aisha", "comparing yourself to others"
Additional queries: "forgiveness of sins", "prayer before sleeping", "fasting in Ramadan"

Text excerpts: 250 chars so the hadith is actually readable.

Writes: /code/test results & reports/mxbai_size_filter_report.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/mxbai_size_filter_report.py
"""
import os, re, time
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

ES_HOST = "http://172.31.250.10:9200"
INDEX   = "english-mxbai"
FIELD   = "semantic_text"
REPORT  = "/code/test results & reports/mxbai_size_filter_report.md"

PRIORITY_QUERIES = [
    "aisha",
    "comparing yourself to others",
]
EXTRA_QUERIES = [
    "forgiveness of sins",
    "prayer before sleeping",
    "fasting in Ramadan",
]
QUERIES = PRIORITY_QUERIES + EXTRA_QUERIES

SIZES = [10, 20, 30, 50, 75, 100]

COLLECTION_BOOSTS = {
    "bukhari": 5.0, "muslim": 4.8, "nasai": 3.5, "abudawud": 3.0,
    "tirmidhi": 2.5, "ibnmajah": 2.0, "malik": 2.5, "ahmad": 2.5,
    "darimi": 2.0, "mishkat": 2.5, "nawawi40": 3.3, "riyadussalihin": 2.5,
}

CHAIN_FILTER = {"bool": {"must_not": {"term": {"isChainRef": True}}}}

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)


def strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


def build_query(user_query, chain_filter=False):
    if chain_filter:
        return {"bool": {
            "filter": [CHAIN_FILTER],
            "must": [{"semantic": {"field": FIELD, "query": user_query}}],
        }}
    return {"bool": {"must": [{"semantic": {"field": FIELD, "query": user_query}}]}}


def search_raw(query_text, size, chain_filter=False):
    t0 = time.perf_counter()
    r = es.options(request_timeout=60).search(
        index=INDEX, size=size,
        query=build_query(query_text, chain_filter=chain_filter),
        _source={"excludes": [FIELD]},
    )
    ms = round((time.perf_counter() - t0) * 1000)
    return r["hits"]["hits"], ms


def dedup(hits, size):
    groups, singletons = {}, []
    for h in hits:
        gid = h["_source"].get("dupGroup", 0)
        if not gid:
            singletons.append(h)
        else:
            coll = h["_source"].get("collection", "")
            key  = (COLLECTION_BOOSTS.get(coll, 1.0), h["_score"])
            if gid not in groups or key > groups[gid][1]:
                groups[gid] = (h, key)
    merged = singletons + [h for h, _ in groups.values()]
    merged.sort(key=lambda h: h["_score"], reverse=True)
    return merged[:size]


def fmt(h, rank, flag=""):
    s    = h["_source"]
    text = strip_html(s.get("hadithText", ""))[:250]
    cr   = "⚠CHAIN" if s.get("isChainRef") else ""
    # [dup-rep=N] means this IS the chosen representative of group N (others collapsed)
    dup  = f"[dup-rep={s['dupGroup']}]" if s.get("dupGroup") else ""
    tags = f"`{' '.join(filter(None,[cr,dup]))}`" if (cr or dup) else ""
    ref  = f"{s.get('collection','')} {s.get('hadithNumber','')}"
    return f"| {rank}{flag} | {h['_score']:.3f} | {ref} | {tags} {text} |"


lines = []
W = lines.append

# ── Index stats ────────────────────────────────────────────────────────────────
total  = es.count(index=INDEX)["count"]
chains = es.count(index=INDEX, body={"query": {"term": {"isChainRef": True}}})["count"]
dups   = es.count(index=INDEX, body={"query": {"range": {"dupGroup": {"gt": 0}}}})["count"]

W("# mxbai HNSW Size & Filter Report\n")
W(f"Index: `{INDEX}` | {total:,} docs | {chains:,} chain-refs ({chains/total*100:.1f}%) | {dups:,} in dup groups ({dups/total*100:.1f}%)\n")
W("**Production config**: size=75, chain-ref filter=ON, dedup=ON (fetch 75×3=225, collapse to 75)\n")
W("---\n")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — Filter combinations (at size=75)
# ══════════════════════════════════════════════════════════════════════════════
W("## 1. Filter combinations at size=75\n")
W("Each row shows whether a result would survive production filters (chain-ref + dedup both ON).")
W("⚠CHAIN = chain-reference hadith | [dup=N] = belongs to duplicate group N\n")

for q in QUERIES:
    W(f"### Query: *\"{q}\"*\n")

    # Fetch a generous pool for all variants
    raw_all,  ms1 = search_raw(q, size=225, chain_filter=False)
    raw_cr,   ms2 = search_raw(q, size=225, chain_filter=True)
    deduped_all   = dedup(raw_all, 75)
    deduped_cr    = dedup(raw_cr, 75)

    top10_all  = raw_all[:10]
    top10_cr   = raw_cr[:10]
    top10_dd   = dedup(raw_all[:225], 10)
    top10_prod = dedup(raw_cr[:225], 10)

    # Count issues in no-filter top-10
    n_chain = sum(1 for h in top10_all if h["_source"].get("isChainRef"))
    n_dup   = len({h["_source"].get("dupGroup",0) for h in top10_all if h["_source"].get("dupGroup",0)})

    W(f"No-filter top-10: **{n_chain} chain-refs**, **{n_dup} dup groups represented**\n")

    for label, hits in [
        ("No filters (raw)", top10_all),
        ("Chain-ref filter ON only", top10_cr),
        ("Dedup ON only (chain-refs still included)", top10_dd),
        ("**PRODUCTION: chain-ref + dedup both ON**", top10_prod),
    ]:
        W(f"**{label}**")
        W("| # | Score | Ref | Tags | Text (250 chars) |")
        W("|---|---|---|---|---|")
        for i, h in enumerate(hits, 1):
            W(fmt(h, i))
        W("")

W("---\n")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — Size sweep (production filters ON)
# ══════════════════════════════════════════════════════════════════════════════
W("## 2. HNSW size sweep — production filters ON (chain-ref + dedup)\n")
W("Fetch size = size × 3, then dedup to `size`. Shows which hadiths only surface at larger sizes.\n")

for q in QUERIES:
    W(f"### Query: *\"{q}\"*\n")

    size_hits = {}
    size_ms   = {}
    for sz in SIZES:
        raw, ms = search_raw(q, size=sz * 3, chain_filter=True)
        size_hits[sz] = dedup(raw, sz)
        size_ms[sz]   = ms

    # Latency table
    W("| size | fetch_size | latency |")
    W("|---|---|---|")
    for sz in SIZES:
        W(f"| {sz} | {sz*3} | {size_ms[sz]}ms |")
    W("")

    # Collect all unique hadiths seen across sizes (by ref)
    def hit_ref(h):
        s = h["_source"]
        return (s.get("collection",""), str(s.get("hadithNumber","")))

    seen = {}
    for sz in SIZES:
        for rank, h in enumerate(size_hits[sz][:10], 1):
            k = hit_ref(h)
            if k not in seen:
                seen[k] = (strip_html(h["_source"].get("hadithText",""))[:200], sz)

    W("**Top-10 stability** — rank at each size (— = not in top-10 at that size)\n")
    W("| Ref | First seen | " + " | ".join(f"size={sz}" for sz in SIZES) + " | Text |")
    W("|---|---|" + "|".join("---" for _ in SIZES) + "|---|")

    for k, (text, first_sz) in seen.items():
        ranks = []
        for sz in SIZES:
            pos = next((str(i) for i, h in enumerate(size_hits[sz][:10], 1) if hit_ref(h) == k), "—")
            ranks.append(pos)
        new_marker = f"🆕@{first_sz}" if first_sz > SIZES[0] else ""
        W(f"| {k[0]} {k[1]} | {new_marker or 'size='+str(SIZES[0])} | " + " | ".join(ranks) + f" | {text} |")

    # Summarise late arrivals
    base = {hit_ref(h) for h in size_hits[SIZES[0]][:10]}
    latecomers = []
    for sz in SIZES[1:]:
        for h in size_hits[sz][:10]:
            k = hit_ref(h)
            if k not in base:
                latecomers.append((sz, h))
                base.add(k)

    if latecomers:
        W(f"\n**New results that only appear at larger sizes:**")
        for sz, h in latecomers:
            s = h["_source"]
            text = strip_html(s.get("hadithText",""))[:200]
            W(f"- First at size={sz}: **{s.get('collection','')} {s.get('hadithNumber','')}** (score {h['_score']:.3f}) — {text}")
    else:
        W(f"\n*Top-10 fully stable across all sizes.*")
    W("")

W("---\n")
W("*Generated by `tests/mxbai_size_filter_report.py`*\n")

os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report written: {REPORT}")
print(f"Index: {total:,} | chain-refs: {chains:,} | dup groups: {dups:,}")
