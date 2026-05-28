"""
Auto-tags [matn] boundaries in untagged Arabic hadiths.

Strategy: the isnad always ends at the last verb of saying (قال / يقول / فقال)
in the chain — find that, everything after is the matn.

Uses diacritic-flexible regex so it matches both fully-vowelled and bare text.
Validates against 89k tagged hadiths before applying to untagged ones.

Run inside container:
    docker exec search-web-1 python3 /code/tests/tag_matn_boundary.py
    docker exec search-web-1 python3 /code/tests/tag_matn_boundary.py --apply
"""
import os, re, sys, json
import pymysql

APPLY = "--apply" in sys.argv

# ── Diacritic-flexible matching ────────────────────────────────────────────────
# Arabic tashkeel (diacritics) appear as combining chars after the base letter.
# D* inserted between base chars means the pattern matches with or without vowels.
D = r'[ً-ٰٟ]*'

def ar(s):
    """Make regex fragment that matches an Arabic string with or without diacritics."""
    return D.join(list(s)) + D

# Prophet reference (bare root + optional diacritics between letters)
_PROPHET = (
    ar('رسول') + r'\s+' + ar('الله')
    + r'|' + ar('النبي')
    + r'|ﷺ'
    + r'|' + ar('صلى') + r'.{0,40}?' + ar('وسلم')
)

_SEP = r'(?:\s*[:”«“”‘’،])*\s*'

# Priority 1: “قال رسول الله ﷺ [يقول] :” — full attribution phrase
_P1 = (
    r'(?:' + ar('قال') + r'|' + ar('فقال') + r'|' + ar('سمعت') + r')'
    r'\s+(?:' + _PROPHET + r').{0,50}?'
    r'(?:(?:' + ar('قال') + r'|' + ar('يقول') + r')' + _SEP + r'|' + _SEP + r')'
)

# Priority 2: “النبي ﷺ قال :” — prophet reference then verb
_P2 = (
    r'(?:' + _PROPHET + r').{0,50}?'
    r'(?:' + ar('قال') + r'|' + ar('يقول') + r')' + _SEP
)

# Priority 3: simple “قال :” / “فقال :” at chain end
_P3 = (
    r'(?:' + ar('فقال') + r'|' + ar('قال') + r'|' + ar('يقول') + r'|' + ar('سمعت') + r')'
    + _SEP
)

# Two-tier: prophet-attribution patterns first (precise), simple قال fallback
PROPHET_RE = re.compile(r'(?:' + _P1 + r'|' + _P2 + r')', re.DOTALL)
SIMPLE_RE  = re.compile(r'(?:' + _P3 + r')', re.DOTALL)

# Narrator markup to strip before applying (same state as untagged hadiths)
MARKUP_RE = re.compile(r'\[/?(?:prematn|matn|narrator[^\]]*|name[^\]]*)\]', re.DOTALL)

def predict_matn(raw_text):
    """
    Return (matn_text, boundary_pos_in_clean) or (None, None).
    Uses prophet-attribution patterns first to avoid grabbing قال inside the matn.
    Falls back to last simple قال only when no attribution pattern found.
    """
    clean = MARKUP_RE.sub('', raw_text).strip()

    # Try prophet-attribution patterns first (last match = nearest to matn)
    matches = list(PROPHET_RE.finditer(clean))
    if matches:
        m = matches[-1]
        return clean[m.end():].strip(), m.end()

    # Fallback: last simple قال / فقال in text
    matches = list(SIMPLE_RE.finditer(clean))
    if matches:
        m = matches[-1]
        return clean[m.end():].strip(), m.end()

    return None, None

# ── DB ─────────────────────────────────────────────────────────────────────────
conn = pymysql.connect(
    host=os.environ["MYSQL_HOST"], user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"], database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
)
cur = conn.cursor(pymysql.cursors.DictCursor)

# ── VALIDATION ─────────────────────────────────────────────────────────────────
print("Loading tagged hadiths for validation...")
cur.execute("""
    SELECT arabicURN, collection, hadithText
    FROM ArabicHadithTable
    WHERE hadithText LIKE '%[matn]%'
    ORDER BY arabicURN
""")
tagged = cur.fetchall()
print(f"  {len(tagged):,} tagged hadiths")

MATN_EXTRACT = re.compile(r'\[matn\](.*?)\[/matn\]', re.DOTALL)

found = missed = exact = close = 0
collection_stats = {}

for row in tagged:
    text = row["hadithText"]
    col  = row["collection"]

    m = MATN_EXTRACT.search(text)
    if not m:
        continue
    true_matn = MARKUP_RE.sub('', m.group(1)).strip()

    pred_matn, _ = predict_matn(text)

    if col not in collection_stats:
        collection_stats[col] = {"n": 0, "found": 0, "exact": 0, "close": 0}
    collection_stats[col]["n"] += 1

    if pred_matn is None:
        missed += 1
        continue

    found += 1
    collection_stats[col]["found"] += 1

    # Compare first 40 chars of predicted vs actual matn
    pred40 = pred_matn[:40].strip()
    true40 = true_matn[:40].strip()

    if pred40 == true40:
        exact += 1
        collection_stats[col]["exact"] += 1
    elif true40[:20] in pred_matn[:80] or pred40[:20] in true_matn[:80]:
        close += 1
        collection_stats[col]["close"] += 1

total = len(tagged)
print(f"\nValidation (n={total:,}):")
print(f"  Boundary found:  {found:,}  ({100*found/total:.1f}%)")
print(f"  Exact matn start:{exact:,}  ({100*exact/total:.1f}%)")
print(f"  Close (<80 char):{close:,}  ({100*close/total:.1f}%)")
print(f"  Missed:          {missed:,}  ({100*missed/total:.1f}%)")
print(f"  Precision (found+exact+close): {100*(exact+close)/max(found,1):.1f}% of found are correct")

print("\nPer-collection:")
print(f"  {'Collection':<20} {'n':>7} {'Found%':>8} {'Exact%':>8} {'Close%':>8}")
for col, s in sorted(collection_stats.items(), key=lambda x: -x[1]['n']):
    n = s['n']
    print(f"  {col:<20} {n:>7}  {100*s['found']/n:>6.1f}%  {100*s['exact']/n:>6.1f}%  {100*s['close']/n:>6.1f}%")

# ── Sample misses for debugging ────────────────────────────────────────────────
print("\nSample missed hadiths (no boundary found):")
miss_count = 0
for row in tagged:
    if miss_count >= 5:
        break
    pred, _ = predict_matn(row["hadithText"])
    if pred is not None:
        continue
    m = MATN_EXTRACT.search(row["hadithText"])
    if not m:
        continue
    clean = MARKUP_RE.sub('', row["hadithText"])
    print(f"  URN {row['arabicURN']} ({row['collection']}): ...{clean[-150:].strip()[:100]!r}")
    miss_count += 1

# ── APPLY ──────────────────────────────────────────────────────────────────────
if not APPLY:
    print(f"\nDry run. Pass --apply to tag untagged hadiths.")
    conn.close()
    sys.exit(0)

print("\n\nApplying to untagged Sunan collections...")
cur.execute("""
    SELECT arabicURN, collection, hadithText
    FROM ArabicHadithTable
    WHERE hadithText NOT LIKE '%[matn]%'
      AND collection IN ('muslim','nasai','abudawud','ibnmajah','tirmidhi',
                         'ahmad','adab','shamail','malik','bukhari')
    ORDER BY arabicURN
""")
untagged = cur.fetchall()
conn.close()
print(f"  {len(untagged):,} hadiths to process")

results = {}
applied = skipped = 0

for row in untagged:
    matn, _ = predict_matn(row["hadithText"] or "")
    if matn:
        results[str(row["arabicURN"])] = {
            "collection": row["collection"],
            "matn": matn[:5000],
        }
        applied += 1
    else:
        skipped += 1

OUT = "/code/matn_boundaries.json"
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False)

print(f"  Tagged:  {applied:,}")
print(f"  Skipped: {skipped:,}")
print(f"  Written: {OUT}")
