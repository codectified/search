"""
Embeds English hadith text using OpenAI text-embedding-3-small.
Saves to /code/english_openai_embeddings.json — resumable.

Also detects and flags chain-reference hadiths (isChainRef=True):
  - Muslim sub-hadiths like "This hadith has been narrated through another chain..."
  - Very short entries that are pure isnad references with no matn content

Cost estimate: ~44,900 hadiths × 100 tokens avg × $0.02/1M = ~$0.09

Run inside container:
    docker exec search-web-1 python3 /code/tests/embed_english_openai.py
"""
import os, re, json, time
import pymysql
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

MODEL      = "text-embedding-3-small"
BATCH_SIZE = 200
MAX_CHARS  = 5000
OUT_FILE   = "/code/english_openai_embeddings.json"

# ── Chain-reference detection ─────────────────────────────────────────────────
# These hadiths have no matn content — they're isnad-variant notes in the text.

_CHAIN_PREFIX = re.compile(
    r'^\s*(<p>\s*)?(This hadith has been narrated|A hadith like this has been'
    r'|A similar hadith has been|The same has been narrated|The previous hadith is narrated'
    r'|Another chain of transmitters|This is narrated by another chain'
    r'|This hadith is narrated (?:likewise|through)|A hadith narrated through'
    r'|\(Another chain\)|With a similar chain)',
    re.IGNORECASE,
)

_CHAIN_SHORT = re.compile(r'chain of transmitters|chain of narrators|another chain', re.IGNORECASE)


def is_chain_ref(raw_text: str) -> bool:
    """True if this hadith's English text is a chain-variant note with no matn."""
    if not raw_text:
        return False
    plain = re.sub(r'<[^>]+>', ' ', raw_text)
    plain = re.sub(r'\s+', ' ', plain).strip()
    if _CHAIN_PREFIX.match(plain):
        return True
    # Short text (< 250 chars) that's primarily a chain reference
    if len(plain) < 250 and _CHAIN_SHORT.search(plain):
        return True
    return False


def clean_english(raw: str) -> str:
    """Strip HTML tags, normalise whitespace."""
    if not raw:
        return ""
    t = re.sub(r'<[^>]+>', ' ', raw)
    return re.sub(r'\s+', ' ', t).strip()


# ── Load existing results (resumable) ─────────────────────────────────────────
if os.path.exists(OUT_FILE):
    with open(OUT_FILE) as f:
        results = json.load(f)
    print(f"Resuming: {len(results):,} already embedded")
else:
    results = {}

# ── Fetch bilingual hadiths from DB ───────────────────────────────────────────
print("Loading hadiths from DB...")
conn = pymysql.connect(
    host=os.environ["MYSQL_HOST"], user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"], database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
)
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("""
    SELECT h.englishURN, h.collection, h.hadithNumber, h.hadithText AS englishText,
           h.matchingArabicURN AS arabicURN, h.grade1 AS gradeEnglish,
           a.grade1 AS gradeArabic
    FROM EnglishHadithTable h
    LEFT JOIN ArabicHadithTable a ON a.arabicURN = h.matchingArabicURN
    ORDER BY h.englishURN
""")
rows = cur.fetchall()
conn.close()
print(f"  {len(rows):,} bilingual hadiths loaded")

todo = [r for r in rows if str(r["englishURN"]) not in results]
print(f"  {len(todo):,} to embed")

# Cost estimate
avg_chars = sum(len(clean_english(r["englishText"] or "")) for r in todo[:500]) / max(len(todo[:500]), 1)
est_tokens = avg_chars / 4  # rough chars-to-tokens ratio
est_cost = len(todo) * est_tokens / 1_000_000 * 0.02
print(f"  Avg chars: {avg_chars:.0f} | Est cost: ${est_cost:.3f}\n")

# ── Embed in batches ──────────────────────────────────────────────────────────
chain_ref_count = 0
t_start = time.time()

for batch_start in range(0, len(todo), BATCH_SIZE):
    batch = todo[batch_start : batch_start + BATCH_SIZE]
    texts, urns, flags = [], [], []

    for row in batch:
        raw = row["englishText"] or ""
        chain_ref = is_chain_ref(raw)
        text = clean_english(raw)[:MAX_CHARS] or "."
        texts.append(text)
        urns.append(str(row["englishURN"]))
        flags.append(chain_ref)
        if chain_ref:
            chain_ref_count += 1

    resp = client.embeddings.create(model=MODEL, input=texts)
    vectors = [e.embedding for e in resp.data]

    for i, (urn, flag, vec) in enumerate(zip(urns, flags, vectors)):
        row = batch[i]
        results[urn] = {
            "englishURN":    int(urn),
            "arabicURN":     row["arabicURN"] or 0,
            "collection":    row["collection"],
            "hadithNumber":  row["hadithNumber"],
            "englishText":   clean_english(row["englishText"] or ""),
            "gradeEnglish":  row["gradeEnglish"] or "",
            "gradeArabic":   row["gradeArabic"] or "",
            "isChainRef":    flag,
            "vector":        vec,
        }

    done = batch_start + len(batch)
    elapsed = time.time() - t_start
    rate = done / elapsed
    remaining = (len(todo) - done) / rate if rate > 0 else 0
    print(f"  {done:,}/{len(todo):,} | chain-refs so far: {chain_ref_count} | "
          f"ETA {remaining/60:.1f}m", end="\r")

    # Save checkpoint every 10 batches
    if (batch_start // BATCH_SIZE) % 10 == 9:
        with open(OUT_FILE, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False)

    time.sleep(0.3)

# ── Final save ────────────────────────────────────────────────────────────────
with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False)

elapsed = time.time() - t_start
print(f"\n\nDone: {len(results):,} embedded in {elapsed/60:.1f}m")
print(f"Chain-reference hadiths flagged: {chain_ref_count}")
print(f"Output: {OUT_FILE}")
