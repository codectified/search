"""
Computes a centroid vector per book from the english-mxbai index.
Joins ES vectors with DB book metadata, then for each book centroid finds
the 5 most representative hadiths (nearest to the centroid).

Run inside the search container:
    docker exec search-web-1 python3 /code/tests/compute_centroids.py
Copy results back:
    docker cp search-web-1:/code/book_centroids.md "test results & reports/book_centroids.md"
    docker cp search-web-1:/code/book_centroids.json "test results & reports/book_centroids.json"
"""
import os, json, time
from collections import defaultdict
import pymysql
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://elasticsearch:9200", basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]))
INDEX = "english-mxbai"

# ── Step 1: fetch book metadata from DB (englishURN → book info) ──────────────
print("Fetching book map from DB...")
conn = pymysql.connect(
    host=os.environ["MYSQL_HOST"], user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"], database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
)
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("""
    SELECT h.englishURN, h.collection, h.bookNumber,
           b.englishBookName, b.arabicBookName, b.ourBookID
    FROM HadithTable h
    JOIN BookData b ON h.collection = b.collection
        AND h.bookNumber = b.englishBookNumber
    WHERE h.englishURN > 0
""")
urn_to_book = {}
for row in cur.fetchall():
    urn_to_book[row["englishURN"]] = {
        "collection": row["collection"],
        "bookNumber": row["bookNumber"],
        "ourBookID": row["ourBookID"],
        "bookName_en": (row["englishBookName"] or "").strip(),
        "bookName_ar": (row["arabicBookName"] or "").strip(),
    }
conn.close()
print(f"  {len(urn_to_book):,} hadiths mapped to books")

# ── Step 2: fetch all vectors from ES ────────────────────────────────────────
print("Fetching all vectors from ES (this takes ~30s)...")
t0 = time.time()

# {(collection, ourBookID): {"meta": {...}, "vectors": [...], "docs": [...]}}
books = defaultdict(lambda: {"meta": {}, "vectors": [], "docs": []})
unmatched = 0

for hit in helpers.scan(es, index=INDEX, query={"_source": True, "query": {"match_all": {}}}, size=100):
    s = hit["_source"]
    chunks = s.get("semantic_text", {}).get("inference", {}).get("chunks", [])
    if not chunks:
        continue
    urn = s.get("urn")
    book_info = urn_to_book.get(urn)
    if not book_info:
        unmatched += 1
        continue

    key = (book_info["collection"], book_info["ourBookID"])
    books[key]["meta"] = book_info
    books[key]["vectors"].append(chunks[0]["embeddings"])
    books[key]["docs"].append({
        "urn": urn,
        "collection": book_info["collection"],
        "hadithNumber": s.get("hadithNumber", ""),
        "hadithText": (s.get("hadithText") or "").replace("<p>", "").replace("\n", " ").strip()[:250],
        "grade": s.get("grade") or "",
    })

print(f"  {sum(len(b['vectors']) for b in books.values()):,} matched, {unmatched} unmatched, "
      f"{len(books)} books, {time.time()-t0:.0f}s")

# ── Step 3: compute centroids ─────────────────────────────────────────────────
def mean_vector(vectors):
    n, dim = len(vectors), len(vectors[0])
    c = [0.0] * dim
    for v in vectors:
        for i in range(dim):
            c[i] += v[i]
    return [x / n for x in c]

def cosine_sim(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(x * x for x in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0

print("Computing centroids and finding representative hadiths...")
centroids = {}
for key, data in books.items():
    if len(data["vectors"]) < 2:
        continue
    c = mean_vector(data["vectors"])
    scored = sorted(
        zip([cosine_sim(c, v) for v in data["vectors"]], data["docs"]),
        key=lambda x: x[0], reverse=True
    )
    meta = data["meta"]
    centroids[key] = {
        "collection": meta["collection"],
        "ourBookID": meta["ourBookID"],
        "bookName_en": meta["bookName_en"],
        "bookName_ar": meta["bookName_ar"],
        "hadith_count": len(data["vectors"]),
        "centroid": c,
        "representative_hadiths": [{"score": round(s, 4), **d} for s, d in scored[:5]],
        # cohesion = avg similarity of all hadiths to centroid (how tight is this book?)
        "cohesion": round(sum(s for s, _ in scored) / len(scored), 4),
    }

print(f"  {len(centroids)} book centroids computed")

# ── Step 4: cross-centroid similarity (collection level) ─────────────────────
# Aggregate book centroids up to collection level for the similarity matrix
coll_vecs = defaultdict(list)
for data in centroids.values():
    coll_vecs[data["collection"]].append(data["centroid"])
coll_centroids = {c: mean_vector(vecs) for c, vecs in coll_vecs.items()}

# ── Step 5: write outputs ─────────────────────────────────────────────────────
# JSON — full centroid vectors for downstream use
json_data = {
    f"{v['collection']}:{v['ourBookID']}": {
        "collection": v["collection"],
        "bookName_en": v["bookName_en"],
        "bookName_ar": v["bookName_ar"],
        "hadith_count": v["hadith_count"],
        "cohesion": v["cohesion"],
        "centroid": v["centroid"],
        "representative_hadiths": v["representative_hadiths"],
    }
    for v in centroids.values()
}
with open("/code/book_centroids.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False)

# Markdown report
out = []
out.append("# Book-Level Centroids\n")
out.append(f"_{len(centroids)} books with 2+ hadiths | centroid = mean of all hadith vectors in that book_\n")
out.append("**Cohesion** = average cosine similarity of hadiths to their book centroid. ")
out.append("High cohesion = tight, focused book. Low = diverse topics.\n\n---\n")

# Cross-collection similarity matrix
colls = sorted(coll_centroids.keys())
out.append("## Cross-Collection Centroid Similarity\n")
out.append("| | " + " | ".join(f"**{c[:10]}**" for c in colls) + " |")
out.append("|---|" + "---|" * len(colls))
for a in colls:
    row = f"| **{a}** |"
    for b in colls:
        sim = cosine_sim(coll_centroids[a], coll_centroids[b])
        row += f" {sim:.3f} |"
    out.append(row)

out.append("\n---\n")
out.append("## Books by Collection\n")
out.append("Sorted by cohesion descending within each collection.\n")

for coll in sorted(set(v["collection"] for v in centroids.values())):
    coll_books = sorted(
        [v for v in centroids.values() if v["collection"] == coll],
        key=lambda x: x["cohesion"], reverse=True
    )
    out.append(f"### {coll} ({len(coll_books)} books)\n")
    out.append("| Book | Hadiths | Cohesion |")
    out.append("|------|---------|---------|")
    for b in coll_books:
        out.append(f"| {b['bookName_en'] or '—'} | {b['hadith_count']} | {b['cohesion']} |")
    out.append("")

    out.append("#### Representative hadiths per book\n")
    for b in coll_books:
        out.append(f"**{b['bookName_en'] or 'Untitled'}** (cohesion: {b['cohesion']})")
        for rh in b["representative_hadiths"][:3]:
            out.append(f"- #{rh['hadithNumber']} [{rh['score']}] {rh['hadithText'][:180]}")
        out.append("")

report = "\n".join(out)
with open("/code/book_centroids.md", "w", encoding="utf-8") as f:
    f.write(report)

print(f"Written: book_centroids.md ({len(report):,} chars) + book_centroids.json")
