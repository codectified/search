"""
Extracts the matn (body text) from English hadith text by stripping the isnad
(narrator chain) prefix. Creates english_matn_map.json for re-embedding.

Extraction patterns by collection:
  Bukhari          : "Narrated X: [matn]"               — colon boundary
  Nasai/IbnMajah/  : "It was narrated from/that X: ..." — colon boundary
  Ahmad/AbuDawud
  Muslim/Mishkat/  : "X reported/said: [matn]"          — colon after verb
  Riyadussalihin
  Tirmidhi         : "X narrated that/from Y: [matn]"   — colon boundary
  Malik            : "Yahya related to me from Malik..." — no reliable boundary;
                     heuristic first-colon used, marked as 'weak'
  hisn/forty/adab  : No isnad — full text IS the matn

Writes: /code/english_matn_map.json
        /code/english_matn_report.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/extract_english_matn.py
"""
import os, re, json, time
from collections import Counter, defaultdict
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=60)

INDEX    = "english-mxbai"
OUT_FILE = "/code/english_matn_map.json"
REPORT   = "/code/english_matn_report.md"

# Collections with no isnad structure — full text is already the matn
PURE_MATN_COLLECTIONS = {"hisn", "forty", "nawawi40"}


def strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


# ── Extraction patterns (tried in order) ─────────────────────────────────────

_P = [
    # P1 — Narrated X: (Bukhari, some AbuDawud/Tirmidhi)
    ("narrated_colon",
     re.compile(r'^(Narrated\s+[^:]{2,80}):\s+(.+)', re.DOTALL | re.I)),

    # P2 — It was narrated from/that X: (Nasai, IbnMajah, Ahmad, AbuDawud)
    ("itwas_colon",
     re.compile(r'^(It was narrated (?:from|that)\s+[^:]{2,100}):\s+(.+)', re.DOTALL | re.I)),

    # P3a — It is/has been narrated on the authority of X: (Muslim colon variant)
    ("authority_colon",
     re.compile(r'^(It (?:has been|is) narrated on the authority of\s+[^:]{2,100}):\s+(.+)', re.DOTALL | re.I)),

    # P3b — It is narrated on the authority of X that [matn] (Muslim "that" variant, no colon)
    ("authority_that",
     re.compile(r'^It (?:has been|is) narrated on the authority of\s+[^,\.]{2,120}\s+that\s+(.+)', re.DOTALL | re.I)),

    # P4 — It has been reported/related that X: / It has been related that X:
    ("ithas_colon",
     re.compile(r'^(It has been (?:reported|related|mentioned|said)\s+[^:]{0,80}):\s+(.+)', re.DOTALL | re.I)),

    # P5 — X (may Allah...) reported/said/related/narrated: [matn]
    #       Covers Muslim, Riyadussalihin, Mishkat, Adab, etc.
    ("reported_colon",
     re.compile(
         r'^(.{3,160}?\s+(?:reported|said|related|told us|informed us|narrated|stated|mentioned))\s*:\s+(.+)',
         re.DOTALL | re.I)),

    # P6 — X narrated that/from/to us Y ... : (Tirmidhi "X narrated from Y that Z said:")
    ("narrated_chain_colon",
     re.compile(r'^(.{3,200}?\s+(?:narrated|transmitted)\s+.{0,80}):\s+(.+)', re.DOTALL | re.I)),

    # P7 — X said/reported ... as saying, "[matn]" (Mishkat, Adab comma+quote pattern)
    #       "X reported God's messenger as saying, 'blah'"
    ("as_saying_quote",
     re.compile(
         r'^.{3,200}?\s+as saying,\s*["‘“\'](.+)',
         re.DOTALL | re.I)),

    # P8 — X said, "[matn]" (Adab: "Ibn Umar said, 'The pleasure...'")
    #       Only if the comma is within the first 100 chars (narrator is short)
    ("said_comma_quote",
     re.compile(
         r'^(.{3,100}?\s+said),\s*["‘“\'](.+)',
         re.DOTALL | re.I)),

    # P9 — Text begins directly with a quote (Bulugh: '"None of you should..."')
    ("leading_quote",
     re.compile(r'^["“‘](.+)', re.DOTALL)),
]


def extract_matn(text, collection=""):
    """
    Returns (isnad, matn, pattern_name).
    isnad may be empty for pure-matn collections or failed extractions.
    """
    if not text:
        return "", "", "empty"

    if collection in PURE_MATN_COLLECTIONS:
        return "", text, "pure_matn"

    for pattern_name, regex in _P:
        m = regex.match(text)
        if not m:
            continue
        # Single-group patterns (authority_that, leading_quote): matn is group 1
        if pattern_name in ("authority_that", "leading_quote"):
            matn  = m.group(1).strip()
            isnad = text[:m.start(1)].strip()
        elif pattern_name == "as_saying_quote":
            matn  = m.group(1).strip()
            isnad = text[:m.start(1)].strip()
        else:
            isnad = m.group(1).strip().rstrip(":")
            matn  = m.group(2).strip()
        # Sanity: matn must be at least 20 chars
        # Reject if extracted matn still looks like an isnad chain (Malik false-match guard)
        _CHAIN_PHRASES = ("related to me from", "narrated to me from", "transmitted to me from")
        if len(matn) >= 20 and not any(p in matn[:80].lower() for p in _CHAIN_PHRASES):
            return isnad, matn, pattern_name

    # P7 — Weak heuristic: first colon within 220 chars, followed by ≥20 chars of content
    early = text[:220]
    pos   = early.find(":")
    if pos > 8:
        candidate_matn = text[pos + 1:].strip()
        if len(candidate_matn) >= 30:
            return text[:pos].strip(), candidate_matn, "first_colon_weak"

    # No extraction possible
    return "", text, "no_extract"


# ── Scan all hadiths ──────────────────────────────────────────────────────────
print(f"Scanning {INDEX}...")
t0 = time.time()

matn_map = {}          # {urn_str: {matn, isnad, pattern, collection}}
pattern_by_coll  = defaultdict(Counter)
examples_partial = defaultdict(list)   # collection → [example dicts]
total = 0

for hit in es_scan(
    es, index=INDEX,
    query={"query": {"match_all": {}},
           "_source": ["urn", "collection", "hadithNumber", "hadithText"]},
    size=500,
):
    s    = hit["_source"]
    urn  = str(s.get("urn", hit["_id"]))
    coll = s.get("collection", "")
    num  = s.get("hadithNumber", "")
    text = strip_html(s.get("hadithText", ""))

    isnad, matn, pattern = extract_matn(text, coll)

    matn_map[urn] = {
        "matn":       matn,
        "isnad":      isnad,
        "pattern":    pattern,
        "collection": coll,
    }
    pattern_by_coll[coll][pattern] += 1
    total += 1

    # Collect examples for partial-coverage collections
    if pattern in ("first_colon_weak", "no_extract") and len(examples_partial[coll]) < 5:
        examples_partial[coll].append({
            "hadithNumber": num,
            "pattern":      pattern,
            "full_text":    text[:300],
            "extracted_matn": matn[:200] if matn else "(none)",
        })

print(f"  {total:,} hadiths processed in {time.time()-t0:.0f}s")

# ── Save map ──────────────────────────────────────────────────────────────────
with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(matn_map, f, ensure_ascii=False)
print(f"Saved: {OUT_FILE}")

# ── Coverage summary ──────────────────────────────────────────────────────────
CLEAN_PATTERNS   = {"narrated_colon","itwas_colon","authority_colon","authority_that",
                    "ithas_colon","reported_colon","narrated_chain_colon","pure_matn",
                    "as_saying_quote","said_comma_quote","leading_quote"}
PARTIAL_PATTERNS = {"first_colon_weak"}
FAILED_PATTERNS  = {"no_extract","empty"}

lines = ["# English Matn Extraction Report", ""]
lines.append(f"Total hadiths: {total:,}  \n")

# Overall
clean = sum(1 for v in matn_map.values() if v["pattern"] in CLEAN_PATTERNS)
weak  = sum(1 for v in matn_map.values() if v["pattern"] in PARTIAL_PATTERNS)
fail  = sum(1 for v in matn_map.values() if v["pattern"] in FAILED_PATTERNS)
lines.append(f"| Coverage tier | Count | % |")
lines.append("|---|---|---|")
lines.append(f"| Clean extraction | {clean:,} | {clean/total*100:.1f}% |")
lines.append(f"| Weak heuristic (first colon) | {weak:,} | {weak/total*100:.1f}% |")
lines.append(f"| No extraction (full text used) | {fail:,} | {fail/total*100:.1f}% |")
lines.append("")

# Per collection
lines.append("## Per-Collection Breakdown")
lines.append("")
lines.append("| Collection | Total | Clean | Weak | No-extract | Top patterns |")
lines.append("|---|---|---|---|---|---|")

for coll in sorted(pattern_by_coll, key=lambda c: -sum(pattern_by_coll[c].values())):
    ctr  = pattern_by_coll[coll]
    tot  = sum(ctr.values())
    cl   = sum(ctr[p] for p in CLEAN_PATTERNS)
    wk   = sum(ctr[p] for p in PARTIAL_PATTERNS)
    fl   = sum(ctr[p] for p in FAILED_PATTERNS)
    tops = ", ".join(f"{p}={n}" for p, n in ctr.most_common(3))
    lines.append(f"| {coll} | {tot} | {cl}({cl*100//tot}%) | {wk}({wk*100//tot}%) | {fl}({fl*100//tot}%) | {tops} |")

lines.append("")

# Examples for partial-coverage collections
lines.append("## Partial-Coverage Examples")
lines.append("")
lines.append("These hadiths fell back to the weak heuristic or no-extract. "
             "Full text shown so the pattern gaps are visible.\n")

for coll in sorted(examples_partial):
    if not examples_partial[coll]:
        continue
    lines.append(f"### {coll}")
    lines.append("")
    for ex in examples_partial[coll]:
        lines.append(f"**{coll} {ex['hadithNumber']}** — pattern: `{ex['pattern']}`  ")
        lines.append(f"Full text: {ex['full_text']}  ")
        lines.append(f"Extracted matn: {ex['extracted_matn']}")
        lines.append("")

with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Saved: {REPORT}")

# Console summary
print(f"\nOverall: clean={clean:,}({clean*100//total}%) weak={weak:,}({weak*100//total}%) fail={fail:,}({fail*100//total}%)")
print("\nPer-collection (clean%):")
for coll in sorted(pattern_by_coll, key=lambda c: -sum(pattern_by_coll[c].values())):
    ctr = pattern_by_coll[coll]
    tot = sum(ctr.values())
    cl  = sum(ctr[p] for p in CLEAN_PATTERNS)
    print(f"  {coll:<20} {cl:>5}/{tot:<5} ({cl*100//tot:>3}%) — {dict(ctr.most_common(2))}")
