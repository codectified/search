"""
Builds the 'arabic-openai' ES index from arabic_matn_embeddings.json.
Uses OpenAI text-embedding-3-small vectors (1536-dim, multilingual).
Cross-lingual: English queries hit Arabic matn vectors natively.

Throttled bulk indexing (batch=150, 0.5s sleep) to keep ES heap stable.
Resumable: skips docs already in the index.

Run inside container:
    docker exec search-web-1 python3 /code/tests/index_arabic_openai.py
"""
import os, json, re, time
import pymysql
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

INDEX = "arabic-openai"
BATCH_SIZE = 150
SLEEP_BETWEEN = 0.5  # seconds between batches

MATN_RE = re.compile(r'\[matn\](.*?)\[/matn\]', re.DOTALL)

def extract_matn(text):
    if not text:
        return "", False
    m = MATN_RE.search(text)
    if m:
        return m.group(1).strip(), True
    cleaned = re.sub(r'\[/?(?:prematn|matn|narrator[^\]]*)\]', '', text).strip()
    return cleaned, False

# ── Connect ────────────────────────────────────────────────────────────────────
es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

conn = pymysql.connect(
    host=os.environ["MYSQL_HOST"], user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"], database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
)

# ── Create index if needed ─────────────────────────────────────────────────────
if not es.indices.exists(index=INDEX):
    es.indices.create(index=INDEX, body={
        "settings": {
            "refresh_interval": "-1",       # disable during bulk load
            "number_of_replicas": 0,
        },
        "mappings": {
            "properties": {
                "arabicURN":    {"type": "integer"},
                "englishURN":   {"type": "integer"},
                "collection":   {"type": "keyword"},
                "hadithNumber": {"type": "keyword"},
                "arabicMatn":   {"type": "text", "analyzer": "arabic"},
                "arabicText":   {"type": "text", "analyzer": "arabic"},
                "englishText":  {"type": "text"},
                "gradeArabic":  {"type": "keyword"},
                "gradeEnglish": {"type": "keyword"},
                "hadMatnTag":   {"type": "boolean"},
                "embedding": {
                    "type": "dense_vector",
                    "dims": 1536,
                    "index": True,
                    "similarity": "cosine",
                },
            }
        },
    })
    print(f"Created index '{INDEX}'")
else:
    print(f"Index '{INDEX}' already exists")

# ── Find already-indexed URNs (for resumability) ───────────────────────────────
print("Checking already-indexed docs...")
existing = set()
from elasticsearch.helpers import scan as es_scan
for hit in es_scan(es, index=INDEX, query={"_source": ["arabicURN"]}, size=1000):
    existing.add(hit["_source"]["arabicURN"])
print(f"  {len(existing):,} already indexed")

# ── Load vectors ───────────────────────────────────────────────────────────────
print("Loading vectors from arabic_matn_embeddings.json...")
with open("/code/arabic_matn_embeddings.json") as f:
    vectors = json.load(f)
print(f"  {len(vectors):,} vectors loaded")

# ── Load hadith metadata from DB ───────────────────────────────────────────────
print("Loading hadith metadata from DB...")
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("""
    SELECT
        a.arabicURN, a.collection, a.hadithText AS arabicText, a.grade1 AS gradeArabic,
        h.englishURN, h.hadithNumber, h.englishText, h.englishgrade1 AS gradeEnglish
    FROM ArabicHadithTable a
    LEFT JOIN HadithTable h ON h.arabicURN = a.arabicURN
    ORDER BY a.arabicURN
""")
rows = cur.fetchall()
conn.close()
print(f"  {len(rows):,} rows loaded")

todo = [r for r in rows if r["arabicURN"] not in existing and str(r["arabicURN"]) in vectors]
print(f"  {len(todo):,} remaining to index")

# ── Bulk index in throttled batches ────────────────────────────────────────────
t0 = time.time()
indexed = 0
errors = 0

for i in range(0, len(todo), BATCH_SIZE):
    batch = todo[i:i + BATCH_SIZE]
    actions = []
    for row in batch:
        urn_str = str(row["arabicURN"])
        vec_entry = vectors[urn_str]
        matn, had_tag = extract_matn(row["arabicText"])
        actions.append({
            "_index": INDEX,
            "_id": f"arabic:{row['arabicURN']}",
            "_source": {
                "arabicURN":    row["arabicURN"],
                "englishURN":   row["englishURN"] or 0,
                "collection":   row["collection"],
                "hadithNumber": row["hadithNumber"] or "",
                "arabicMatn":   matn[:5000],
                "arabicText":   (row["arabicText"] or "")[:10000],
                "englishText":  (row["englishText"] or "")[:10000],
                "gradeArabic":  row["gradeArabic"] or "",
                "gradeEnglish": row["gradeEnglish"] or "",
                "hadMatnTag":   vec_entry["had_matn_tag"],
                "embedding":    vec_entry["vector"],
            },
        })

    try:
        ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        indexed += ok
        if errs:
            errors += len(errs)
            print(f"  batch {i//BATCH_SIZE} errors: {errs[:2]}")
    except Exception as e:
        print(f"  ERROR batch {i//BATCH_SIZE}: {e}")
        errors += 1

    time.sleep(SLEEP_BETWEEN)

    if (i // BATCH_SIZE) % 20 == 0:
        elapsed = time.time() - t0
        rate = indexed / elapsed if elapsed > 0 else 0
        remaining = (len(todo) - indexed) / rate if rate > 0 else 0
        print(f"  [{indexed:,}/{len(todo):,}] {rate:.0f} docs/s | ~{remaining/60:.1f} min remaining | {errors} errors")

# ── Restore refresh interval ───────────────────────────────────────────────────
es.indices.put_settings(index=INDEX, body={"refresh_interval": "1s"})
es.indices.refresh(index=INDEX)

elapsed = time.time() - t0
count = es.count(index=INDEX)["count"]
print(f"\nDone: {indexed:,} indexed, {errors} errors, {elapsed:.0f}s ({indexed/elapsed:.0f} docs/s)")
print(f"Total in index: {count:,}")
