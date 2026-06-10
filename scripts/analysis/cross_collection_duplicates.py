"""
Finds semantically near-duplicate hadiths across collections by anchoring on Bukhari,
running kNN for each hadith, and clustering cross-collection matches above a score threshold.

Run inside the search container:
    docker exec search-web-1 python3 /code/tests/cross_collection_duplicates.py
Copy result back:
    docker cp search-web-1:/code/cross_collection_duplicates.md "test results & reports/cross_collection_duplicates.md"
"""
import os, json, time
from elasticsearch import Elasticsearch, helpers
from collections import defaultdict

es = Elasticsearch("http://elasticsearch:9200", basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]))

THRESHOLD = 0.93
ANCHOR_COLLECTION = "bukhari"
INDEX = "english-mxbai"

def clean(text):
    if not text:
        return ""
    return text.replace("<p>", "").replace("</p>", "").replace("\n", " ").strip()

print(f"Scanning {ANCHOR_COLLECTION}...")
t0 = time.time()

seen_pairs = set()
groups = []

for hit in helpers.scan(es, index=INDEX, query={
    "_source": True,
    "query": {"term": {"collection.keyword": ANCHOR_COLLECTION}}
}, size=50):
    s = hit["_source"]
    chunks = s.get("semantic_text", {}).get("inference", {}).get("chunks", [])
    if not chunks:
        continue
    vector = chunks[0]["embeddings"]
    anchor_urn = s["urn"]

    res = es.search(index=INDEX, body={
        "_source": {"excludes": ["semantic_text"]},
        "size": 15,
        "knn": {
            "field": "semantic_text.inference.chunks.embeddings",
            "query_vector": vector,
            "k": 15,
            "num_candidates": 100,
        }
    })

    matches = []
    for kh in res["hits"]["hits"]:
        ks = kh["_source"]
        score = round(kh["_score"], 4)
        if score < THRESHOLD:
            continue
        if ks["collection"] == ANCHOR_COLLECTION:
            continue
        pair = tuple(sorted([anchor_urn, ks["urn"]]))
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)
        matches.append({"score": score, "doc": ks})

    if matches:
        # Sort matches by score desc
        matches.sort(key=lambda x: x["score"], reverse=True)
        groups.append({
            "anchor": {
                "urn": s["urn"],
                "collection": s["collection"],
                "hadithNumber": s.get("hadithNumber", ""),
                "hadithText": clean(s.get("hadithText", "")),
                "arabicText": (s.get("arabicText") or "").strip(),
                "grade": s.get("grade") or "",
            },
            "matches": [
                {
                    "score": m["score"],
                    "urn": m["doc"]["urn"],
                    "collection": m["doc"]["collection"],
                    "hadithNumber": m["doc"].get("hadithNumber", ""),
                    "hadithText": clean(m["doc"].get("hadithText", "")),
                    "arabicText": (m["doc"].get("arabicText") or "").strip(),
                    "grade": m["doc"].get("grade") or "",
                }
                for m in matches
            ]
        })

    if len(groups) % 50 == 0 and len(groups) > 0:
        elapsed = time.time() - t0
        print(f"  {len(groups)} groups found ({elapsed:.0f}s elapsed)")

elapsed = time.time() - t0
print(f"Done: {len(groups)} groups in {elapsed:.0f}s")

# Sort groups by highest match score
groups.sort(key=lambda g: g["matches"][0]["score"], reverse=True)

# ── Write report ──────────────────────────────────────────────────────────────
out = []
out.append("# Cross-Collection Near-Duplicate Hadiths")
out.append(f"\nAnchor collection: **{ANCHOR_COLLECTION}** | Similarity threshold: **{THRESHOLD}** | {len(groups)} groups found\n")
out.append("Each group shows a Bukhari hadith alongside its near-duplicates in other collections, sorted by similarity score.\n")
out.append("---\n")

for i, g in enumerate(groups, 1):
    a = g["anchor"]
    top_score = g["matches"][0]["score"]
    collections_matched = ", ".join(sorted({m["collection"] for m in g["matches"]}))

    out.append(f"## {i}. Bukhari #{a['hadithNumber']} ↔ {collections_matched} (top score: {top_score})")
    out.append(f"\n**URN:** {a['urn']} | **Grade:** {a['grade'] or '—'}\n")
    out.append(f"**Bukhari text:**")
    out.append(f"> {a['hadithText']}\n")
    if a["arabicText"]:
        out.append(f"**Arabic:** {a['arabicText'][:300]}\n")

    for m in g["matches"]:
        out.append(f"---\n**{m['collection']} #{m['hadithNumber']}** — score: {m['score']} | URN: {m['urn']} | Grade: {m['grade'] or '—'}")
        out.append(f"> {m['hadithText']}\n")
        if m["arabicText"]:
            out.append(f"**Arabic:** {m['arabicText'][:300]}\n")

    out.append("\n---\n")

report = "\n".join(out)
with open("/code/cross_collection_duplicates.md", "w", encoding="utf-8") as f:
    f.write(report)

print(f"Written: /code/cross_collection_duplicates.md ({len(report):,} chars)")
