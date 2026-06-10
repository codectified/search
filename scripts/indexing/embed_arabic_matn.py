"""
Embeds Arabic hadith text using OpenAI text-embedding-3-small.
Extracts [matn]...[/matn] where tagged (67% of corpus), falls back to full arabicText.

Saves results to /code/arabic_matn_embeddings.json — resumable (skips already-done URNs).

Run inside the search container:
    docker exec search-web-1 python3 /code/tests/embed_arabic_matn.py
Copy result back:
    docker cp search-web-1:/code/arabic_matn_embeddings.json "test results & reports/arabic_matn_embeddings.json"
"""
import os, re, json, time
import pymysql
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

MODEL = "text-embedding-3-small"
BATCH_SIZE = 200
OUT_FILE = "/code/arabic_matn_embeddings.json"

MATN_RE = re.compile(r'\[matn\](.*?)\[/matn\]', re.DOTALL)

def extract_matn(text):
    """Return (matn_text, had_tag). Falls back to full text if no [matn] tag."""
    if not text:
        return "", False
    m = MATN_RE.search(text)
    if m:
        return m.group(1).strip(), True
    # Strip narrator/prematn markup if no matn tag
    cleaned = re.sub(r'\[/?(?:prematn|matn|narrator[^\]]*)\]', '', text).strip()
    return cleaned, False

# ── Load existing results (for resumability) ──────────────────────────────────
if os.path.exists(OUT_FILE):
    with open(OUT_FILE) as f:
        results = json.load(f)
    print(f"Resuming: {len(results):,} already embedded")
else:
    results = {}

# ── Load hadiths from DB ──────────────────────────────────────────────────────
print("Loading hadiths from DB...")
conn = pymysql.connect(
    host=os.environ["MYSQL_HOST"], user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"], database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
)
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("SELECT arabicURN, collection, hadithText FROM ArabicHadithTable ORDER BY arabicURN")
rows = cur.fetchall()
conn.close()
print(f"  {len(rows):,} hadiths loaded")

# ── Filter to not-yet-embedded ────────────────────────────────────────────────
todo = [r for r in rows if str(r["arabicURN"]) not in results]
print(f"  {len(todo):,} remaining to embed")

# ── Estimate cost ─────────────────────────────────────────────────────────────
# text-embedding-3-small: $0.02 / 1M tokens. Arabic ~1.5 tokens/word, ~30 words matn avg.
est_tokens = len(todo) * 50
print(f"  Estimated tokens: ~{est_tokens:,} (~${est_tokens/1_000_000*0.02:.3f} USD)")

# ── Embed in batches ──────────────────────────────────────────────────────────
t0 = time.time()
done = 0
errors = 0

for i in range(0, len(todo), BATCH_SIZE):
    batch = todo[i:i + BATCH_SIZE]

    MAX_CHARS = 5000  # ~3300 Arabic tokens, well under the 8192-token API limit

    texts, urns, had_tags = [], [], []
    for row in batch:
        matn, had_tag = extract_matn(row["hadithText"])
        if not matn:
            matn = "."  # OpenAI requires non-empty string
        texts.append(matn[:MAX_CHARS])
        urns.append(str(row["arabicURN"]))
        had_tags.append(had_tag)

    try:
        response = client.embeddings.create(model=MODEL, input=texts)
        for j, emb_obj in enumerate(response.data):
            results[urns[j]] = {
                "vector": emb_obj.embedding,
                "had_matn_tag": had_tags[j],
                "collection": batch[j]["collection"],
            }
        done += len(batch)
    except Exception as e:
        print(f"  ERROR batch {i//BATCH_SIZE}: {e}")
        errors += 1
        time.sleep(5)
        continue

    # Save checkpoint every 10 batches
    if (i // BATCH_SIZE) % 10 == 0:
        with open(OUT_FILE, "w") as f:
            json.dump(results, f)
        elapsed = time.time() - t0
        rate = done / elapsed if elapsed > 0 else 0
        remaining = (len(todo) - done) / rate if rate > 0 else 0
        print(f"  [{done:,}/{len(todo):,}] {rate:.0f} docs/s | ~{remaining/60:.1f} min remaining | {errors} errors")

# Final save
with open(OUT_FILE, "w") as f:
    json.dump(results, f)

elapsed = time.time() - t0
print(f"\nDone: {done:,} embedded, {errors} errors, {elapsed:.0f}s ({done/elapsed:.0f} docs/s)")
print(f"Total in file: {len(results):,}")
print(f"Written: {OUT_FILE}")
