"""
Normalize hadith grades across all ES indexes and write a gradeNorm field.

gradeNorm values (for facets):
  Sahih | Hasan | Da'if | Maudu' | Uncategorized

Strategy per doc:
  1. Has raw grade → clean + normalize → gradeNorm
  2. Collection is bukhari or muslim → Sahih (auto-tag)
  3. Has matchingArabicURN → look up arabic-openai gradeEnglish → normalize
  4. Has dupGroup > 0 → look up another english doc's grade from lookup table
  5. Else → Uncategorized

Indexes updated: arabic-openai, english-openai, english-mxbai

Usage (inside container):
    python3 /code/tests/normalize_grades.py [--dry-run]
"""
import os, sys, json, re, time
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

DRY_RUN = "--dry-run" in sys.argv
es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=120)

# ── Normalization map ─────────────────────────────────────────────────────────
# Keys are lowercase, diacritic-flattened, strip-cleaned variants.
# Values are the canonical gradeNorm string.
NORM_MAP = {
    # Sahih
    "sahih":                              "Sahih",
    "sahih isnad":                        "Sahih",
    "sahih isnAd":                        "Sahih",
    "sahih in chain":                     "Sahih",
    "sahih maqtu'":                       "Sahih",
    "sahih mauquf":                       "Sahih",
    "sahih hadeeth":                      "Sahih",
    "sahih hadith":                       "Sahih",
    "sahih hadeeth.":                     "Sahih",
    "a sahih hadeeth":                    "Sahih",
    "a sahih hadith":                     "Sahih",
    "its isnad is sahih":                 "Sahih",
    "lts isnad is sahih":                 "Sahih",   # OCR l→I
    "its isnad is qawi":                  "Sahih",
    "lts isnad is qawi":                  "Sahih",
    "qawi":                               "Sahih",
    "sahih li ghairih":                   "Sahih",
    "sahih lighairihi":                   "Sahih",
    "sahih (li ghairih)":                 "Sahih",
    "sahih because of corroborating evidence": "Sahih",
    "sahih because of corroborating evidences": "Sahih",
    "sahih hadeeth and its isnad is hasan": "Sahih",
    "muttafaqun 'alayh":                  "Sahih",
    "muttafaqun 'alayh ":                 "Sahih",
    # Hasan
    "hasan":                              "Hasan",
    "hasan sahih":                        "Hasan",
    "a hasan hadeeth":                    "Hasan",
    "a hasan hadith":                     "Hasan",
    "hasan isnad":                        "Hasan",
    "hasan isnAd":                        "Hasan",
    "hasan in chain":                     "Hasan",
    "hasan maqtu'":                       "Hasan",
    "hasan li ghairih":                   "Hasan",
    "hasan lighairihi":                   "Hasan",
    "hasan (li ghairih)":                 "Hasan",
    "hasan because of corroborating evidence": "Hasan",
    "hasan because of corroborating evidences": "Hasan",
    "hasan because of corroborating evidence; this is a da'if isnad": "Hasan",
    "hasan because of corroborating evidence; this is a da'eef isnad": "Hasan",
    "hasan because of corroborating evidence, this is a da'if isnad": "Hasan",
    "its isnad is hasan":                 "Hasan",
    "lts isnad is hasan":                 "Hasan",
    "sanad da'if wal-hadith hasan":       "Hasan",
    "sanad da'if wal-hadith hasan":       "Hasan",
    # Da'if
    "da'if":                              "Da'if",
    "da if":                              "Da'if",
    "daif":                               "Da'if",
    "da'if isnad":                        "Da'if",
    "da'if isnAd":                        "Da'if",
    "isnad da'if":                        "Da'if",
    "da'if in chain":                     "Da'if",
    "da'if maqtu'":                       "Da'if",
    "da'if mauquf":                       "Da'if",
    "da'if mursal":                       "Da'if",
    "da'if jiddan":                       "Da'if",
    "sanad da'if jiddan":                 "Da'if",
    "its isnad is da'if":                 "Da'if",
    "lts isnad is da'if":                 "Da'if",
    "munkar":                             "Da'if",
    "shadh":                              "Da'if",
    # Maudu' (fabricated — kept separate since it's categorically different)
    "maudu'":                             "Maudu'",
    "maudu":                              "Maudu'",
    "maudu (fabricated)":                 "Maudu'",
}

_DIACRITIC = str.maketrans("āīūĀĪŪāīū", "aiuAIUaiu")

def _clean_raw(raw):  # str -> Optional[str]
    """Strip artifacts, parse JSON wrappers, return cleaned lowercase key."""
    if not raw or not raw.strip():
        return None
    raw = raw.strip()

    # Parse JSON-encoded grade objects: [{"grade": "Sahih", ...}]
    if raw.startswith("[{") or raw.startswith("{"):
        try:
            data = json.loads(raw)
            if isinstance(data, list):
                data = data[0]
            raw = data.get("grade", raw)
        except Exception:
            pass

    # Strip trailing bracket junk and cross-reference notes: [ Muslim (123)]
    raw = re.sub(r"\s*\[.*", "", raw)
    # Strip leading [
    raw = raw.lstrip("[")
    # Strip trailing ] ) . ,
    raw = raw.strip("] ).,; \t")
    # Strip publisher suffixes like (Darussalam)
    raw = re.sub(r"\s*\(darussalam\)\s*", "", raw, flags=re.IGNORECASE).strip()
    raw = re.sub(r"\s*\(darussalam\)\s*", "", raw, flags=re.IGNORECASE).strip()

    if not raw:
        return None

    # Lowercase + flatten diacritics for map lookup
    key = raw.lower().translate(_DIACRITIC)
    return key

def normalize(raw):  # str -> Optional[str]
    """Return gradeNorm string or None if raw is empty/unrecognized."""
    key = _clean_raw(raw)
    if key is None:
        return None
    result = NORM_MAP.get(key)
    if result:
        return result
    # Partial prefix matching for edge cases
    for prefix, grade in [
        ("sahih", "Sahih"), ("hasan", "Hasan"),
        ("da'if", "Da'if"), ("daif", "Da'if"), ("maudu", "Maudu'"),
    ]:
        if key.startswith(prefix):
            return grade
    return None  # genuinely unrecognized

# ── Phase 1: build Arabic URN → gradeNorm lookup from arabic-openai ───────────
print("Phase 1: scanning arabic-openai for graded docs...")
t0 = time.time()
ar_urn_to_norm: dict[int, str] = {}

for hit in es_scan(es, index="arabic-openai",
        query={"query": {"bool": {"must_not": {"term": {"gradeEnglish": ""}}}}},
        _source=["arabicURN", "gradeEnglish"], size=500):
    src = hit["_source"]
    aurn = src.get("arabicURN")
    raw  = src.get("gradeEnglish", "")
    if aurn and raw:
        norm = normalize(raw)
        if norm:
            ar_urn_to_norm[int(aurn)] = norm

print(f"  {len(ar_urn_to_norm):,} arabic URNs with recognized grades ({time.time()-t0:.0f}s)")

# ── Phase 2: scan english-mxbai — resolve gradeNorm for every doc ─────────────
print("\nPhase 2: scanning english-mxbai...")
t1 = time.time()

# First pass: build urn→norm for graded docs (needed for dupGroup cross-refs)
en_urn_to_norm: dict[int, str] = {}
mxbai_docs: list[dict] = []   # (es_id, urn, collection, grade_raw, dupGroup, matchArabicURN)

AUTO_SAHIH = {"bukhari", "muslim"}

for hit in es_scan(es, index="english-mxbai",
        _source=["urn", "collection", "grade", "dupGroup", "matchingArabicURN"],
        query={"query": {"match_all": {}}}, size=500):
    src  = hit["_source"]
    urn  = int(src.get("urn", 0) or 0)
    coll = src.get("collection", "") or ""
    raw  = src.get("grade", "") or ""
    dup  = int(src.get("dupGroup", 0) or 0)
    mar  = src.get("matchingArabicURN", "") or ""
    try:
        mar = int(mar) if mar else 0
    except (ValueError, TypeError):
        mar = 0

    norm = normalize(raw)
    if norm is None and coll in AUTO_SAHIH:
        norm = "Sahih"

    if norm and urn:
        en_urn_to_norm[urn] = norm

    mxbai_docs.append({
        "id": hit["_id"], "urn": urn, "coll": coll,
        "raw": raw, "norm": norm, "dup": dup, "mar": mar
    })

# Second pass: resolve remaining via matchingArabicURN or dupGroup
forty_stats = {"total": 0, "ar_match": 0, "dup_match": 0, "uncat": 0}

for doc in mxbai_docs:
    if doc["norm"] is not None:
        continue
    coll = doc["coll"]

    # Try Arabic cross-match first (Nawawi, etc.)
    if doc["mar"] and doc["mar"] in ar_urn_to_norm:
        doc["norm"] = ar_urn_to_norm[doc["mar"]]
        doc["source"] = "arabic_xmatch"
        if coll == "forty":
            forty_stats["ar_match"] += 1
        continue

    # Try dupGroup cross-match
    if doc["dup"] and doc["dup"] in en_urn_to_norm:
        doc["norm"] = en_urn_to_norm[doc["dup"]]
        doc["source"] = "dup_xmatch"
        if coll == "forty":
            forty_stats["dup_match"] += 1
        continue

    doc["norm"] = "Uncategorized"
    if coll == "forty":
        forty_stats["uncat"] += 1

    if coll == "forty":
        forty_stats["total"] += 1

# Recount forty total
forty_stats["total"] = sum(1 for d in mxbai_docs if d["coll"] == "forty")

print(f"  {len(mxbai_docs):,} docs processed ({time.time()-t1:.0f}s)")

# Nawawi/forty breakdown
print(f"\n  forty (Nawawi 40) cross-match results:")
print(f"    Total:              {forty_stats['total']}")
print(f"    Arabic URN match:   {forty_stats['ar_match']}")
print(f"    DupGroup match:     {forty_stats['dup_match']}")
print(f"    Uncategorized:      {forty_stats['uncat']}")

# Distribution summary
from collections import Counter
mxbai_dist = Counter(d["norm"] for d in mxbai_docs)
print("\n  english-mxbai gradeNorm distribution:")
for k, v in sorted(mxbai_dist.items(), key=lambda x: -x[1]):
    print("    %7d  %5.1f%%  %s" % (v, v/len(mxbai_docs)*100, k))

# ── Phase 3: scan english-openai ─────────────────────────────────────────────
print("\nPhase 3: scanning english-openai...")
t2 = time.time()

# english-openai uses englishURN + gradeEnglish; dupGroup also present
en_openai_docs: list[dict] = []
en_urn_to_norm_eoai: dict[int, str] = {}

for hit in es_scan(es, index="english-openai",
        _source=["englishURN", "arabicURN", "collection", "gradeEnglish", "dupGroup"],
        query={"query": {"match_all": {}}}, size=500):
    src  = hit["_source"]
    eurn = int(src.get("englishURN", 0) or 0)
    aurn = int(src.get("arabicURN", 0) or 0)
    coll = src.get("collection", "") or ""
    raw  = src.get("gradeEnglish", "") or ""
    dup  = int(src.get("dupGroup", 0) or 0)

    norm = normalize(raw)
    if norm is None and coll in AUTO_SAHIH:
        norm = "Sahih"
    if norm and eurn:
        en_urn_to_norm_eoai[eurn] = norm

    en_openai_docs.append({
        "id": hit["_id"], "eurn": eurn, "aurn": aurn,
        "coll": coll, "raw": raw, "norm": norm, "dup": dup
    })

# Resolve remaining
for doc in en_openai_docs:
    if doc["norm"] is not None:
        continue
    if doc["aurn"] and doc["aurn"] in ar_urn_to_norm:
        doc["norm"] = ar_urn_to_norm[doc["aurn"]]
        continue
    if doc["dup"] and doc["dup"] in en_urn_to_norm_eoai:
        doc["norm"] = en_urn_to_norm_eoai[doc["dup"]]
        continue
    doc["norm"] = "Uncategorized"

print(f"  {len(en_openai_docs):,} docs processed ({time.time()-t2:.0f}s)")
eoai_dist = Counter(d["norm"] for d in en_openai_docs)
print("  english-openai gradeNorm distribution:")
for k, v in sorted(eoai_dist.items(), key=lambda x: -x[1]):
    print("    %7d  %5.1f%%  %s" % (v, v/len(en_openai_docs)*100, k))

# ── Phase 4: scan arabic-openai ──────────────────────────────────────────────
print("\nPhase 4: scanning arabic-openai...")
t3 = time.time()
ar_docs: list[dict] = []

for hit in es_scan(es, index="arabic-openai",
        _source=["arabicURN", "collection", "gradeEnglish", "gradeArabic"],
        query={"query": {"match_all": {}}}, size=500):
    src  = hit["_source"]
    aurn = int(src.get("arabicURN", 0) or 0)
    coll = src.get("collection", "") or ""
    raw  = src.get("gradeEnglish", "") or ""

    norm = normalize(raw)
    if norm is None and coll in AUTO_SAHIH:
        norm = "Sahih"
    if norm is None:
        norm = "Uncategorized"

    ar_docs.append({"id": hit["_id"], "norm": norm})

print(f"  {len(ar_docs):,} docs processed ({time.time()-t3:.0f}s)")
ar_dist = Counter(d["norm"] for d in ar_docs)
print("  arabic-openai gradeNorm distribution:")
for k, v in sorted(ar_dist.items(), key=lambda x: -x[1]):
    print("    %7d  %5.1f%%  %s" % (v, v/len(ar_docs)*100, k))

if DRY_RUN:
    print("\n[DRY RUN] No writes performed.")
    sys.exit(0)

# ── Phase 5: bulk write gradeNorm ─────────────────────────────────────────────
def bulk_update(index, docs, norm_key="norm", id_key="id"):
    actions = [
        {"_op_type": "update", "_index": index, "_id": d[id_key],
         "doc": {"gradeNorm": d[norm_key]}}
        for d in docs
    ]
    ok, errors = es_bulk(es, actions, chunk_size=500, raise_on_error=False)
    if errors:
        print(f"  WARNING: {len(errors)} errors in {index}")
    return ok

print("\nPhase 5: writing gradeNorm...")
t4 = time.time()

ok = bulk_update("english-mxbai", mxbai_docs)
print(f"  english-mxbai: {ok:,} updated")

ok = bulk_update("english-openai", en_openai_docs)
print(f"  english-openai: {ok:,} updated")

ok = bulk_update("arabic-openai", ar_docs)
print(f"  arabic-openai: {ok:,} updated")

print(f"\nDone. Total time: {time.time()-t0:.0f}s")
