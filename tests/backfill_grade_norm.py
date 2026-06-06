"""
Backfills gradeNorm, englishMatn, and isChainRef into english-mxbai on prod.

Fully self-contained — no external files, no arabic-openai index required.
Run AFTER dedup_mxbai.py (which handles dupGroup separately).

  gradeNorm  — normalised from grade/arabicGrade on each doc; auto-Sahih for
               Bukhari/Muslim; falls back to "Uncategorized"
  englishMatn — extracted from hadithText by stripping the isnad prefix using
               collection-specific regex patterns (same logic as dev)
  isChainRef — True when matn extraction yields nothing (pure isnad chain, no body)

Safe to re-run: skips docs where all three fields are already set.

Run inside prod container:
    python3 /code/tests/backfill_prod_fields.py
"""
import os, re, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

INDEX   = "english-mxbai"
THREADS = 16

es = Elasticsearch(
    os.environ.get("ES_HOST", "http://172.31.250.10:9200"),
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Grade normalisation ────────────────────────────────────────────────────────
_NORM_MAP = {
    "sahih": "Sahih", "صحيح": "Sahih",
    "hasan": "Hasan", "حسن": "Hasan",
    "hasan sahih": "Hasan", "sahih hasan": "Hasan",
    "da'if": "Da'if", "daif": "Da'if", "weak": "Da'if", "ضعيف": "Da'if",
    "maudu'": "Maudu'", "maudu": "Maudu'", "fabricated": "Maudu'", "موضوع": "Maudu'",
}
_BUKHARI_MUSLIM = {"bukhari", "muslim"}


def _normalize_grade(raw):
    if not raw:
        return None
    cleaned = raw.strip().strip("]").strip()
    if cleaned.startswith("[") or cleaned.startswith("{"):
        m = re.search(r'"grade"\s*:\s*"([^"]+)"', cleaned)
        cleaned = m.group(1) if m else cleaned
    cleaned = re.sub(r'\s*\([^)]+\)', '', cleaned).lower().strip()
    if cleaned in _NORM_MAP:
        return _NORM_MAP[cleaned]
    for k, v in _NORM_MAP.items():
        if cleaned.startswith(k):
            return v
    return None


# ── Matn extraction ────────────────────────────────────────────────────────────
_PURE_MATN_COLLS = {"hisn", "forty", "nawawi40"}

_PATTERNS = [
    ("narrated_colon",
     re.compile(r'^(Narrated\s+[^:]{2,80}):\s+(.+)', re.DOTALL | re.I)),

    ("itwas_colon",
     re.compile(r'^(It was narrated (?:from|that)\s+[^:]{2,100}):\s+(.+)', re.DOTALL | re.I)),

    ("authority_colon",
     re.compile(r'^(It (?:has been|is) narrated on the authority of\s+[^:]{2,100}):\s+(.+)', re.DOTALL | re.I)),

    ("authority_that",
     re.compile(r'^It (?:has been|is) narrated on the authority of\s+[^,\.]{2,120}\s+that\s+(.+)', re.DOTALL | re.I)),

    ("ithas_colon",
     re.compile(r'^(It has been (?:reported|related|mentioned|said)\s+[^:]{0,80}):\s+(.+)', re.DOTALL | re.I)),

    ("reported_colon",
     re.compile(
         r'^(.{3,160}?\s+(?:reported|said|related|told us|informed us|narrated|stated|mentioned))\s*:\s+(.+)',
         re.DOTALL | re.I)),

    ("narrated_chain_colon",
     re.compile(r'^(.{3,200}?\s+(?:narrated|transmitted)\s+.{0,80}):\s+(.+)', re.DOTALL | re.I)),

    ("as_saying_quote",
     re.compile(r'^.{3,200}?\s+as saying,\s*["‘“](.+)', re.DOTALL | re.I)),
]

_CHAIN_PHRASES = ("related to me from", "narrated to me from", "transmitted to me from")


def _strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


def _extract_matn(text, collection=""):
    """Return (matn, is_chain_ref). matn is empty string for pure chain refs."""
    if not text:
        return "", True

    if collection in _PURE_MATN_COLLS:
        return text, False

    for name, pat in _PATTERNS:
        m = pat.match(text)
        if not m:
            continue
        if name in ("authority_that", "as_saying_quote"):
            matn = m.group(1).strip()
        else:
            matn = m.group(2).strip()
        if len(matn) >= 20 and not any(p in matn[:80].lower() for p in _CHAIN_PHRASES):
            return matn, False

    # Weak fallback: first colon within 220 chars
    early = text[:220]
    pos   = early.find(":")
    if pos > 8:
        candidate = text[pos + 1:].strip()
        if len(candidate) >= 30:
            return candidate, False

    # No extraction — full text with no clear matn boundary is likely a chain ref
    # Use a length heuristic: very short texts with no body = chain ref
    if len(text) < 80:
        return "", True

    return text, False


# ── Scan index ─────────────────────────────────────────────────────────────────
print(f"Scanning {INDEX}...")
t0 = time.time()

updates = []   # [(doc_id, patch_dict)]

for hit in es_scan(es, index=INDEX,
        _source=["collection", "grade", "arabicGrade", "gradeNorm",
                 "hadithText", "englishMatn", "isChainRef"],
        query={"query": {"match_all": {}}},
        size=500):
    s      = hit["_source"]
    doc_id = hit["_id"]
    coll   = s.get("collection", "")
    patch  = {}

    # gradeNorm
    if not s.get("gradeNorm"):
        if coll in _BUKHARI_MUSLIM:
            norm = "Sahih"
        else:
            norm = (_normalize_grade(s.get("grade")) or
                    _normalize_grade(s.get("arabicGrade")) or
                    "Uncategorized")
        patch["gradeNorm"] = norm

    # englishMatn + isChainRef
    needs_matn  = not s.get("englishMatn")
    needs_chain = s.get("isChainRef") is None

    if needs_matn or needs_chain:
        raw_text   = _strip_html(s.get("hadithText") or "")
        matn, is_chain = _extract_matn(raw_text, coll)

        if needs_matn and matn:
            patch["englishMatn"] = matn
        if needs_chain and is_chain:
            patch["isChainRef"] = True

    if patch:
        updates.append((doc_id, patch))

elapsed = time.time() - t0
print(f"  {len(updates):,} docs need updates ({elapsed:.0f}s)")

if not updates:
    print("Nothing to do.")
    raise SystemExit(0)

# ── Apply updates ──────────────────────────────────────────────────────────────
# english-mxbai uses semantic_text — must use individual es.update() calls,
# bulk partial updates are blocked by ES on semantic_text indexes.
print(f"Updating with {THREADS} threads...")
t0   = time.time()
done = err = 0


def _do_update(args):
    doc_id, patch = args
    es.update(index=INDEX, id=doc_id, body={"doc": patch})
    return 1


with ThreadPoolExecutor(max_workers=THREADS) as pool:
    futures = {pool.submit(_do_update, u): u for u in updates}
    for fut in as_completed(futures):
        try:
            done += fut.result()
        except Exception as e:
            err += 1
            if err <= 5:
                print(f"  update error: {e}")
        if done % 5000 == 0 and done > 0:
            elapsed = time.time() - t0
            print(f"  {done:,}/{len(updates):,} | {done/elapsed:.0f} doc/s | errors={err}")

print(f"\nDone: {done:,} updated, {err} errors | {time.time()-t0:.0f}s")
