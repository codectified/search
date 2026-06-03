"""
Query router integration tests — runs against the live Flask API on localhost:5001.

Tests four routes:
  1. Reference lookup  — "bukhari 1", "muslim 100", etc.
  2. Phrase search     — "prayer at night" (quoted)
  3. Arabic BM25       — صلاة الليل
  4. Semantic/lexical  — normal English query, both modes

Also tests:
  - isChainRef filtering (chain-only entries should not appear)
  - gradeNorm facet aggregation returned on every search
  - collection facet aggregation returned on every search
  - gradeNorm filter param works

Run from the host (Flask is exposed at localhost:5001):
    python3 tests/test_query_router.py

Or inside the container (Flask on localhost:5000):
    python3 /code/tests/test_query_router.py
"""

import json
import sys
import urllib.request
import urllib.parse
from dataclasses import dataclass, field
from typing import Optional

# ── Config ─────────────────────────────────────────────────────────────────────
BASE = "http://localhost:5001"   # override via TEST_BASE env
import os
BASE = os.environ.get("TEST_BASE", BASE)
LANG = "english"

PASS = "\033[32mPASS\033[0m"
FAIL = "\033[31mFAIL\033[0m"


# ── Helpers ────────────────────────────────────────────────────────────────────
def get(path, **params):
    qs = urllib.parse.urlencode(params, doseq=True)
    url = f"{BASE}{path}?{qs}" if qs else f"{BASE}{path}"
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read())


def search(q, mode="lexical", **extra):
    return get(f"/{LANG}/search", q=q, mode=mode, **extra)


def hits(resp):
    return resp.get("hits", {}).get("hits", [])


def first_hit(resp):
    h = hits(resp)
    return h[0] if h else None


def source(hit):
    return hit.get("_source", {}) if hit else {}


def aggs(resp):
    return resp.get("aggregations", {})


def meta(resp):
    return resp.get("_meta", {})


# ── Test runner ────────────────────────────────────────────────────────────────
results = []

def check(name, condition, detail=""):
    ok = bool(condition)
    tag = PASS if ok else FAIL
    msg = f"  [{tag}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    results.append((name, ok))
    return ok


def section(title):
    print(f"\n{'─'*60}")
    print(f"  {title}")
    print(f"{'─'*60}")


# ══════════════════════════════════════════════════════════════════
# 1. REFERENCE LOOKUP
# ══════════════════════════════════════════════════════════════════
section("1. Reference lookup  (collection + hadith number)")

cases = [
    ("bukhari 1",    "bukhari", "1"),
    ("bukhari 6594", "bukhari", "6594"),
    ("muslim 1",     "muslim",  "1"),
    ("nasai 3",      "nasai",   "3"),
    ("abudawud 1",   "abudawud","1"),
    ("ibnmajah 1",   "ibnmajah","1"),
    ("forty 1",      "forty",   "1"),
    ("nawawi40 1",   "forty",   "1"),   # alias → forty
]

for query, expected_coll, expected_num in cases:
    try:
        resp = search(query)
        m = meta(resp)
        h = first_hit(resp)
        s = source(h)
        check(
            f'"{query}" → reference route',
            m.get("route") == "reference",
            f'route={m.get("route")}'
        )
        check(
            f'"{query}" → correct collection',
            s.get("collection") == expected_coll,
            f'collection={s.get("collection")}'
        )
        check(
            f'"{query}" → correct hadith number',
            s.get("hadithNumber") == expected_num or str(s.get("hadithNumber")) == expected_num,
            f'hadithNumber={s.get("hadithNumber")}'
        )
    except Exception as e:
        check(f'"{query}" → no exception', False, str(e))

# Edge: number with letter suffix
try:
    resp = search("bukhari 59a")
    m = meta(resp)
    check(
        '"bukhari 59a" → reference route',
        m.get("route") == "reference",
        f'route={m.get("route")}'
    )
except Exception as e:
    check('"bukhari 59a" → no exception', False, str(e))

# Negative: non-reference queries should NOT route to reference
for q in ["the prayer", "prayer forgiveness", "night worship"]:
    try:
        resp = search(q)
        m = meta(resp)
        check(
            f'"{q}" → NOT reference route',
            m.get("route") != "reference",
            f'route={m.get("route")}'
        )
    except Exception as e:
        check(f'"{q}" not-reference → no exception', False, str(e))


# ══════════════════════════════════════════════════════════════════
# 2. PHRASE SEARCH
# ══════════════════════════════════════════════════════════════════
section('2. Phrase search  ("quoted query")')

phrase_cases = [
    '"prayer at night"',
    '"Messenger of Allah"',
    '"Day of Judgement"',
]

for q in phrase_cases:
    try:
        resp = search(q)
        m = meta(resp)
        h = hits(resp)
        check(
            f'{q} → lexical/phrase route',
            m.get("route") == "lexical_phrase",
            f'route={m.get("route")}'
        )
        # Every hit should contain the unquoted phrase text
        inner = q.strip('"')
        if h:
            # match_phrase covers hadithText + arabicText, so check either field
            def phrase_in_hit(hit):
                s = source(hit)
                return (inner.lower() in s.get("hadithText", "").lower()
                        or inner.lower() in s.get("arabicText", "").lower())
            match_count = sum(phrase_in_hit(hit) for hit in h[:5])
            check(
                f'{q} → ≥4/5 top hits contain phrase',
                match_count >= 4,
                f'{match_count}/5 hits match'
            )
    except Exception as e:
        check(f'{q} → no exception', False, str(e))


# ══════════════════════════════════════════════════════════════════
# 3. ARABIC BM25
# ══════════════════════════════════════════════════════════════════
section("3. Arabic text → BM25 on arabicText")

arabic_cases = [
    ("صلاة الليل", "night prayer"),
    ("الزكاة",     "zakat"),
    ("رمضان",      "ramadan"),
]

for arabic_q, hint in arabic_cases:
    try:
        resp = search(arabic_q)
        m = meta(resp)
        h = hits(resp)
        check(
            f'"{arabic_q}" ({hint}) → lexical/arabic route',
            m.get("route") == "lexical_arabic",
            f'route={m.get("route")}'
        )
        # Hits should have arabicText populated
        if h:
            check(
                f'"{arabic_q}" → hits have arabicText',
                bool(source(h[0]).get("arabicText")),
                f'first hit arabicText present: {bool(source(h[0]).get("arabicText"))}'
            )
    except Exception as e:
        check(f'"{arabic_q}" → no exception', False, str(e))


# ══════════════════════════════════════════════════════════════════
# 4. SEMANTIC vs LEXICAL PASSTHROUGH
# ══════════════════════════════════════════════════════════════════
section("4. Semantic / lexical mode passthrough")

query = "prayer during travel"

try:
    lex = search(query, mode="lexical")
    sem = search(query, mode="semantic")
    lex_ids = [h["_id"] for h in hits(lex)[:10]]
    sem_ids = [h["_id"] for h in hits(sem)[:10]]
    check(
        "lexical and semantic return results",
        bool(lex_ids) and bool(sem_ids),
        f"lex={len(lex_ids)}, sem={len(sem_ids)}"
    )
    overlap = len(set(lex_ids) & set(sem_ids))
    check(
        "semantic and lexical top-10 are not identical (different ranking)",
        lex_ids != sem_ids,
        f"overlap={overlap}/10"
    )
except Exception as e:
    check("semantic/lexical passthrough → no exception", False, str(e))


# ══════════════════════════════════════════════════════════════════
# 5. isChainRef FILTERING
# ══════════════════════════════════════════════════════════════════
section("5. isChainRef filtering (chain-only entries excluded)")

try:
    resp = search("narrated to me from")
    h = hits(resp)
    chain_ref_hits = [hit for hit in h if source(hit).get("isChainRef") is True]
    check(
        "no isChainRef=True docs in results",
        len(chain_ref_hits) == 0,
        f"{len(chain_ref_hits)} chain-ref hits in top {len(h)}"
    )
except Exception as e:
    check("isChainRef filter → no exception", False, str(e))


# ══════════════════════════════════════════════════════════════════
# 6. GRADE FACETS
# ══════════════════════════════════════════════════════════════════
section("6. gradeNorm + collection facet aggregations")

try:
    resp = search("prayer")
    agg = aggs(resp)
    check(
        "aggregations key present in response",
        bool(agg),
        f"keys: {list(agg.keys())}"
    )
    grade_agg = agg.get("gradeNorm", {})
    buckets = grade_agg.get("buckets", [])
    bucket_keys = [b["key"] for b in buckets]
    check(
        "gradeNorm agg has expected buckets",
        any(k in bucket_keys for k in ["Sahih", "Hasan", "Da'if"]),
        f"buckets: {bucket_keys}"
    )
    coll_agg = agg.get("collection", {})
    coll_buckets = coll_agg.get("buckets", [])
    check(
        "collection agg has buckets",
        len(coll_buckets) > 0,
        f"{len(coll_buckets)} collections"
    )
    check(
        "bukhari appears in collection agg",
        any(b["key"] == "bukhari" for b in coll_buckets),
        f"collections: {[b['key'] for b in coll_buckets[:5]]}"
    )
except Exception as e:
    check("grade facets → no exception", False, str(e))

# gradeNorm filter param
try:
    resp_sahih = search("prayer", gradeNorm="Sahih")
    h = hits(resp_sahih)
    all_sahih = all(source(hit).get("gradeNorm") in ("Sahih", None) for hit in h)
    check(
        "gradeNorm=Sahih filter returns only Sahih/Bukhari/Muslim",
        all_sahih,
        f"{len(h)} results, non-sahih: {[source(hit).get('gradeNorm') for hit in h if source(hit).get('gradeNorm') not in ('Sahih', None)][:3]}"
    )
except Exception as e:
    check("gradeNorm filter → no exception", False, str(e))


# ══════════════════════════════════════════════════════════════════
# 7. ROUTE META VALUES — explicit route checks
# ══════════════════════════════════════════════════════════════════
section("7. Explicit route values in _meta")

# Standard English → route: lexical
for q in ["prayer forgiveness", "comparing yourself to others", "aisha"]:
    try:
        resp = search(q, mode="lexical")
        m = meta(resp)
        check(
            f'"{q}" → route: lexical',
            m.get("route") == "lexical",
            f'route={m.get("route")}'
        )
    except Exception as e:
        check(f'"{q}" lexical route → no exception', False, str(e))

# Standard English with mode=semantic → route: semantic
try:
    resp = search("prayer forgiveness", mode="semantic")
    m = meta(resp)
    check(
        '"prayer forgiveness" mode=semantic → route: semantic',
        m.get("route") == "semantic",
        f'route={m.get("route")}'
    )
except Exception as e:
    check("semantic route → no exception", False, str(e))


# ══════════════════════════════════════════════════════════════════
# 8. MODE OVERRIDE PRIORITY
# ══════════════════════════════════════════════════════════════════
section("8. Mode override priority  (arabic/phrase/reference beat mode param)")

# Arabic query + mode=semantic → must still go lexical_arabic (not semantic)
try:
    resp = search("صلاة الليل", mode="semantic")
    m = meta(resp)
    check(
        'Arabic query + mode=semantic → lexical_arabic (not semantic)',
        m.get("route") == "lexical_arabic",
        f'route={m.get("route")}'
    )
except Exception as e:
    check("arabic overrides semantic → no exception", False, str(e))

# Quoted query + mode=semantic → must still go lexical_phrase
try:
    resp = search('"actions are by intention"', mode="semantic")
    m = meta(resp)
    check(
        'quoted query + mode=semantic → lexical_phrase (not semantic)',
        m.get("route") == "lexical_phrase",
        f'route={m.get("route")}'
    )
except Exception as e:
    check("phrase overrides semantic → no exception", False, str(e))

# Collection+number + mode=semantic → must still go reference
try:
    resp = search("bukhari 1", mode="semantic")
    m = meta(resp)
    check(
        'collection+number + mode=semantic → reference (not semantic)',
        m.get("route") == "reference",
        f'route={m.get("route")}'
    )
except Exception as e:
    check("reference overrides semantic → no exception", False, str(e))

# Mixed Arabic+English → routes to arabic (Arabic chars dominate)
try:
    resp = search("aisha عائشة", mode="lexical")
    m = meta(resp)
    check(
        '"aisha عائشة" (mixed) → lexical_arabic',
        m.get("route") == "lexical_arabic",
        f'route={m.get("route")}'
    )
except Exception as e:
    check("mixed arabic+english → no exception", False, str(e))

# Single Arabic character is enough to trigger Arabic route
try:
    resp = search("و", mode="lexical")
    m = meta(resp)
    check(
        '"و" (single arabic char) → lexical_arabic',
        m.get("route") == "lexical_arabic",
        f'route={m.get("route")}'
    )
except Exception as e:
    check("single arabic char → no exception", False, str(e))


# ══════════════════════════════════════════════════════════════════
# 9. ARABIC ROUTE — no language filter applied
# ══════════════════════════════════════════════════════════════════
section("9. Arabic route — no language restriction (searches full index)")

# Note: english-mxbai is a bilingual index (all docs have hadithText + arabicText).
# There are no lang:ar-only docs in this index, so we verify the filter isn't
# applied by checking that common Arabic terms return a large result set
# (i.e., the full corpus is being searched, not a restricted subset).
try:
    resp = search("الصلاة")   # "prayer" — extremely common term
    total_hits = resp.get("hits", {}).get("total", {}).get("value", 0)
    h = hits(resp)
    check(
        "Arabic query returns results",
        len(h) > 0,
        f"{len(h)} hits returned"
    )
    check(
        "Arabic query searches full corpus (>1000 total hits for 'الصلاة')",
        total_hits > 1000,
        f"total hits = {total_hits:,}"
    )
except Exception as e:
    check("arabic no-restriction → no exception", False, str(e))

# Verify Arabic route doesn't restrict to a subset of collections
try:
    resp = search("رمضان")   # "ramadan" — appears across all collections
    agg = aggs(resp)
    coll_buckets = agg.get("collection", {}).get("buckets", [])
    check(
        "Arabic query hits multiple collections (no collection restriction)",
        len(coll_buckets) >= 5,
        f"{len(coll_buckets)} collections in results"
    )
except Exception as e:
    check("arabic multi-collection → no exception", False, str(e))


# ══════════════════════════════════════════════════════════════════
# 10. FACETS PRESENT ON ALL ROUTES EXCEPT REFERENCE
# ══════════════════════════════════════════════════════════════════
section("10. Facet aggs present on phrase / arabic / semantic routes; absent on reference")

# Phrase route — aggs present
try:
    resp = search('"Messenger of Allah"')
    agg = aggs(resp)
    check(
        "phrase route has gradeNorm agg",
        bool(agg.get("gradeNorm", {}).get("buckets")),
        f"buckets: {len(agg.get('gradeNorm', {}).get('buckets', []))}"
    )
    check(
        "phrase route has collection agg",
        bool(agg.get("collection", {}).get("buckets")),
        f"buckets: {len(agg.get('collection', {}).get('buckets', []))}"
    )
except Exception as e:
    check("phrase route facets → no exception", False, str(e))

# Arabic route — aggs present
try:
    resp = search("الزكاة")
    agg = aggs(resp)
    check(
        "arabic route has gradeNorm agg",
        bool(agg.get("gradeNorm", {}).get("buckets")),
        f"buckets: {len(agg.get('gradeNorm', {}).get('buckets', []))}"
    )
    check(
        "arabic route has collection agg",
        bool(agg.get("collection", {}).get("buckets")),
        f"buckets: {len(agg.get('collection', {}).get('buckets', []))}"
    )
except Exception as e:
    check("arabic route facets → no exception", False, str(e))

# Semantic route — aggs present
try:
    resp = search("fear of Allah", mode="semantic")
    agg = aggs(resp)
    check(
        "semantic route has gradeNorm agg",
        bool(agg.get("gradeNorm", {}).get("buckets")),
        f"buckets: {len(agg.get('gradeNorm', {}).get('buckets', []))}"
    )
except Exception as e:
    check("semantic route facets → no exception", False, str(e))

# Reference route — aggs NOT present (single known hadith, no population)
try:
    resp = search("bukhari 1")
    agg = aggs(resp)
    check(
        "reference route has no gradeNorm agg",
        not agg.get("gradeNorm"),
        f"gradeNorm agg present: {bool(agg.get('gradeNorm'))}"
    )
    check(
        "reference route has no collection agg",
        not agg.get("collection"),
        f"collection agg present: {bool(agg.get('collection'))}"
    )
except Exception as e:
    check("reference no-aggs → no exception", False, str(e))


# ══════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════
print(f"\n{'═'*60}")
passed = sum(1 for _, ok in results if ok)
total  = len(results)
print(f"  {passed}/{total} checks passed")
if passed < total:
    print("\n  FAILED:")
    for name, ok in results:
        if not ok:
            print(f"    • {name}")
print(f"{'═'*60}\n")
sys.exit(0 if passed == total else 1)
