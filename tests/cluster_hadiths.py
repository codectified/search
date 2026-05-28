"""
K-means clustering across all hadith vectors — data-driven topic groupings
that cross collection/book boundaries.

Outputs:
  - cluster_report.md   — human-readable: top hadiths per cluster, book distribution
  - cluster_map.json    — {urn: cluster_id} mapping for ES filtering

Run inside the search container:
    docker exec search-web-1 python3 /code/tests/cluster_hadiths.py
Copy results back:
    docker cp search-web-1:/code/cluster_report.md "test results & reports/cluster_report.md"
    docker cp search-web-1:/code/cluster_map.json "test results & reports/cluster_map.json"
"""
import os, json, time
from collections import defaultdict
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://elasticsearch:9200", basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]))
INDEX = "english-mxbai"
K = 75  # number of clusters — adjust to taste

# ── Fetch all vectors ─────────────────────────────────────────────────────────
print(f"Fetching all vectors from ES...")
t0 = time.time()

urns, vectors, meta = [], [], []
for hit in helpers.scan(es, index=INDEX, query={"_source": True, "query": {"match_all": {}}}, size=100):
    s = hit["_source"]
    chunks = s.get("semantic_text", {}).get("inference", {}).get("chunks", [])
    if not chunks:
        continue
    urns.append(s["urn"])
    vectors.append(chunks[0]["embeddings"])
    meta.append({
        "urn": s["urn"],
        "collection": s.get("collection", ""),
        "hadithNumber": s.get("hadithNumber", ""),
        "hadithText": (s.get("hadithText") or "").replace("<p>", "").replace("\n", " ").strip()[:250],
        "grade": s.get("grade") or "",
    })

X = np.array(vectors, dtype=np.float32)
X = normalize(X)  # L2 normalize so cosine sim = dot product
print(f"  {len(urns):,} docs, matrix {X.shape}, {time.time()-t0:.0f}s")

# ── K-means ───────────────────────────────────────────────────────────────────
print(f"Running MiniBatchKMeans with k={K}...")
t1 = time.time()
km = MiniBatchKMeans(n_clusters=K, random_state=42, batch_size=2048, n_init=5, max_iter=200, verbose=0)
labels = km.fit_predict(X)
centroids = km.cluster_centers_  # shape (K, 1024), already normalized by sklearn
print(f"  Done in {time.time()-t1:.0f}s | inertia: {km.inertia_:.2f}")

# ── Build cluster data ────────────────────────────────────────────────────────
clusters = defaultdict(lambda: {"docs": [], "collection_counts": defaultdict(int)})
for i, (label, doc) in enumerate(zip(labels, meta)):
    clusters[int(label)]["docs"].append({"vec_idx": i, **doc})
    clusters[int(label)]["collection_counts"][doc["collection"]] += 1

# For each cluster: find top-5 docs nearest to centroid
for cid, data in clusters.items():
    c = centroids[cid]
    scored = []
    for doc in data["docs"]:
        sim = float(np.dot(c, X[doc["vec_idx"]]))
        scored.append((sim, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    data["representative"] = [{"score": round(s, 4), **d} for s, d in scored[:5]]
    data["size"] = len(data["docs"])
    # intra-cluster cohesion
    sims = [s for s, _ in scored]
    data["cohesion"] = round(float(np.mean(sims)), 4)

# Sort clusters by size descending
sorted_clusters = sorted(clusters.items(), key=lambda x: x[1]["size"], reverse=True)

# ── Cross-cluster similarity (top-level structure) ────────────────────────────
C = centroids  # (K, 1024)
sim_matrix = C @ C.T  # cosine similarities between all cluster pairs

# ── Write cluster_map.json ────────────────────────────────────────────────────
cluster_map = {str(doc["urn"]): int(label) for label, doc in zip(labels, meta)}
with open("/code/cluster_map.json", "w") as f:
    json.dump(cluster_map, f)

# Also write centroid vectors for use in two-stage search
centroid_data = {
    str(cid): {
        "size": data["size"],
        "cohesion": data["cohesion"],
        "top_collections": dict(sorted(data["collection_counts"].items(), key=lambda x: x[1], reverse=True)[:5]),
        "centroid": centroids[cid].tolist(),
        "representative_hadiths": data["representative"],
    }
    for cid, data in sorted_clusters
}
with open("/code/cluster_centroids.json", "w") as f:
    json.dump(centroid_data, f, ensure_ascii=False)

# ── Write markdown report ─────────────────────────────────────────────────────
out = []
out.append(f"# Hadith Corpus — {K} Semantic Clusters\n")
out.append(f"_{len(urns):,} hadiths clustered by mxbai embedding similarity, crossing collection boundaries._\n")
out.append("**Cohesion** = avg cosine similarity of hadiths to their cluster centroid.\n\n---\n")

out.append("## Cluster Overview\n")
out.append("| Cluster | Size | Cohesion | Top Collections | Top Hadith Preview |")
out.append("|---------|------|----------|-----------------|--------------------|")
for cid, data in sorted_clusters:
    top_colls = ", ".join(f"{c}({n})" for c, n in sorted(data["collection_counts"].items(), key=lambda x: x[1], reverse=True)[:3])
    preview = data["representative"][0]["hadithText"][:80] if data["representative"] else ""
    out.append(f"| {cid} | {data['size']} | {data['cohesion']} | {top_colls} | {preview} |")

out.append("\n---\n")
out.append("## Cluster Detail\n")

for cid, data in sorted_clusters:
    coll_dist = ", ".join(f"{c}: {n}" for c, n in sorted(data["collection_counts"].items(), key=lambda x: x[1], reverse=True))
    out.append(f"### Cluster {cid} — {data['size']} hadiths | cohesion {data['cohesion']}")
    out.append(f"**Collections:** {coll_dist}\n")
    out.append("**Most representative hadiths (nearest to centroid):**\n")
    for rh in data["representative"]:
        out.append(f"- **{rh['collection']} #{rh['hadithNumber']}** [sim {rh['score']}] | Grade: {rh['grade'] or '—'}")
        out.append(f"  > {rh['hadithText']}\n")
    out.append("")

report = "\n".join(out)
with open("/code/cluster_report.md", "w", encoding="utf-8") as f:
    f.write(report)

print(f"\nWritten: cluster_report.md ({len(report):,} chars)")
print(f"         cluster_map.json ({len(cluster_map):,} entries)")
print(f"         cluster_centroids.json ({K} centroids)")
print(f"\nCluster size range: {min(d['size'] for _,d in sorted_clusters)} – {max(d['size'] for _,d in sorted_clusters)}")
print(f"Cohesion range:     {min(d['cohesion'] for _,d in sorted_clusters):.4f} – {max(d['cohesion'] for _,d in sorted_clusters):.4f}")
