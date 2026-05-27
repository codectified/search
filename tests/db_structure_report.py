"""
Unique organizational names in the hadith DB.
Collections → unique book names → unique chapter names

Run inside the search container:
    docker exec search-web-1 python3 /code/tests/db_structure_report.py
Copy result back:
    docker cp search-web-1:/code/db_structure_report.md "test results & reports/db_structure_report.md"
"""
import os
import pymysql

conn = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
)
cur = conn.cursor(pymysql.cursors.DictCursor)

out = []

# ── Collections ───────────────────────────────────────────────────────────────
out.append("# Hadith DB — Unique Organizational Names\n")
out.append("## Collections (24 total)\n")
out.append("| Name | English Title | Arabic Title | Type | Hadith | Status |")
out.append("|------|--------------|--------------|------|--------|--------|")

cur.execute("""
    SELECT name, englishTitle, arabicTitle, type, numhadith, status
    FROM Collections ORDER BY collectionID
""")
collections = cur.fetchall()

for c in collections:
    out.append(
        f"| {c['name']} | {c['englishTitle']} | {c['arabicTitle']} | {c['type']} "
        f"| {c['numhadith']} | {c['status'] or ''} |"
    )

# ── Unique book names ─────────────────────────────────────────────────────────
out.append("\n---\n")
out.append("## Unique Book Names\n")

cur.execute("""
    SELECT DISTINCT TRIM(englishBookName) AS en, TRIM(arabicBookName) AS ar
    FROM BookData
    WHERE englishBookName IS NOT NULL AND TRIM(englishBookName) != ''
    ORDER BY TRIM(englishBookName)
""")
books = cur.fetchall()
out.append(f"_{len(books)} unique English book names_\n")
for b in books:
    out.append(f"- {b['en']} / {b['ar']}")

# ── Unique chapter names ──────────────────────────────────────────────────────
out.append("\n---\n")
out.append("## Unique Chapter (Bab) Names\n")

cur.execute("""
    SELECT COUNT(*) AS total FROM ChapterData
""")
total_chapters = cur.fetchone()["total"]

cur.execute("""
    SELECT DISTINCT TRIM(englishBabName) AS en, TRIM(arabicBabName) AS ar
    FROM ChapterData
    WHERE englishBabName IS NOT NULL AND TRIM(englishBabName) != ''
    ORDER BY TRIM(englishBabName)
""")
chapters = cur.fetchall()
out.append(f"_{total_chapters:,} total chapter rows; {len(chapters):,} unique non-empty English chapter names_\n")
for ch in chapters:
    out.append(f"- {ch['en']} / {ch['ar']}")

conn.close()

report = "\n".join(out) + "\n"
with open("/code/db_structure_report.md", "w", encoding="utf-8") as f:
    f.write(report)

print(f"Written: /code/db_structure_report.md ({len(report):,} chars, {report.count(chr(10))} lines)")
