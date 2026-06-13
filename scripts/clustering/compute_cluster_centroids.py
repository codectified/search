"""
Compute per-cluster centroid vectors from any index that has an `embedding`
field and a cluster-ID field, then find representative hadiths and write
both a JSON artifact and a markdown report.

Usage (run natively against host ES):
    python3 scripts/clustering/compute_cluster_centroids.py

Env vars (all optional — defaults shown):
    ES_HOST          localhost
    ES_PORT          9200
    ELASTIC_PASSWORD 123
    INDEX            english-openai
    CLUSTER_FIELD    clusterIdFinal
    TEXT_FIELD       englishText
    OUT_DIR          reports/clusters/english-openai
"""
import os, json, time
from collections import defaultdict
from elasticsearch import Elasticsearch, helpers

ES_HOST     = os.environ.get("ES_HOST", "localhost")
ES_PORT     = os.environ.get("ES_PORT", "9200")
ES_PW       = os.environ.get("ELASTIC_PASSWORD", "123")
INDEX       = os.environ.get("INDEX", "english-openai")
CLUSTER_FLD = os.environ.get("CLUSTER_FIELD", "clusterIdFinal")
TEXT_FLD    = os.environ.get("TEXT_FIELD", "englishText")
OUT_DIR     = os.environ.get("OUT_DIR", f"reports/clusters/{INDEX}")

os.makedirs(OUT_DIR, exist_ok=True)

es = Elasticsearch(f"http://{ES_HOST}:{ES_PORT}", basic_auth=("elastic", ES_PW))

# ── Step 1: scan all docs with an embedding and a cluster ID ──────────────────
print(f"Scanning {INDEX} (cluster_field={CLUSTER_FLD}, text_field={TEXT_FLD})...")
t0 = time.time()

clusters = defaultdict(lambda: {"vectors": [], "docs": []})
skipped = 0

for hit in helpers.scan(
    es, index=INDEX,
    query={"query": {"exists": {"field": CLUSTER_FLD}}},
    _source_includes=["embedding", CLUSTER_FLD, TEXT_FLD, "collection",
                      "hadithNumber", "gradeNorm", "isChainRef", "urn",
                      "englishURN", "arabicURN", "dupGroup"],
    size=500,
):
    s = hit["_source"]
    vec = s.get("embedding")
    cid = s.get(CLUSTER_FLD)
    if not vec or cid is None:
        skipped += 1
        continue
    text = (s.get(TEXT_FLD) or "").replace("<p>", "").replace("\n", " ").strip()
    clusters[int(cid)]["vectors"].append(vec)
    clusters[int(cid)]["docs"].append({
        "urn":          s.get("urn") or s.get("englishURN"),
        "collection":   s.get("collection", ""),
        "hadithNumber": s.get("hadithNumber", ""),
        "gradeNorm":    s.get("gradeNorm", ""),
        "isChainRef":   s.get("isChainRef", False),
        "dupGroup":     s.get("dupGroup"),
        "text":         text,
    })

total = sum(len(c["vectors"]) for c in clusters.values())
print(f"  {total:,} docs across {len(clusters)} clusters, {skipped} skipped — {time.time()-t0:.0f}s")

# ── Step 2: compute centroids ─────────────────────────────────────────────────
def mean_vec(vecs):
    dim = len(vecs[0])
    c = [0.0] * dim
    for v in vecs:
        for i in range(dim):
            c[i] += v[i]
    return [x / len(vecs) for x in c]

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na  = sum(x * x for x in a) ** 0.5
    nb  = sum(x * x for x in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0

print("Computing centroids...")
centroids = {}
for cid, data in sorted(clusters.items()):
    vecs = data["vectors"]
    docs = data["docs"]
    centroid = mean_vec(vecs)
    scores = [cosine(centroid, v) for v in vecs]
    cohesion = sum(scores) / len(scores)

    # collection breakdown
    coll_counts = defaultdict(int)
    for d in docs:
        coll_counts[d["collection"]] += 1
    top_colls = dict(sorted(coll_counts.items(), key=lambda x: -x[1])[:8])

    # representative hadiths: highest cosine to centroid, skip chain-refs
    ranked = sorted(
        [(scores[i], docs[i]) for i in range(len(docs)) if not docs[i].get("isChainRef")],
        key=lambda x: -x[0]
    )

    centroids[cid] = {
        "size":     len(vecs),
        "cohesion": round(cohesion, 4),
        "top_collections": top_colls,
        "centroid": centroid,
        "representative_hadiths": [
            {"score": round(s, 4), **d} for s, d in ranked[:5]
        ],
    }

print(f"  {len(centroids)} centroids computed")

# ── Step 3: write JSON ────────────────────────────────────────────────────────
json_path = os.path.join(OUT_DIR, f"{INDEX}_centroids.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(centroids, f, ensure_ascii=False)
print(f"Written: {json_path}")

# ── Step 4: write markdown report ────────────────────────────────────────────
by_cohesion = sorted(centroids.items(), key=lambda x: -x[1]["cohesion"])
by_size     = sorted(centroids.items(), key=lambda x: -x[1]["size"])

lines = [
    f"# Cluster Centroids — {INDEX}",
    f"",
    f"**Index:** `{INDEX}` | **Cluster field:** `{CLUSTER_FLD}` | "
    f"**k:** {len(centroids)} | **Total docs:** {total:,}",
    f"",
    "---",
    "",
    "## Clusters by cohesion (most focused first)",
    "",
    "| Cluster | Size | Cohesion | Top collections | Top hadith snippet |",
    "|---------|------|----------|-----------------|--------------------|",
]
for cid, c in by_cohesion:
    colls = ", ".join(f"{k}({v})" for k, v in list(c["top_collections"].items())[:3])
    snippet = c["representative_hadiths"][0]["text"][:120].replace("|", "/") if c["representative_hadiths"] else ""
    lines.append(f"| {cid} | {c['size']} | {c['cohesion']} | {colls} | {snippet}… |")

lines += [
    "",
    "---",
    "",
    "## Cluster details",
    "",
]
for cid, c in by_cohesion:
    colls = ", ".join(f"{k}: {v}" for k, v in c["top_collections"].items())
    lines += [
        f"### Cluster {cid}  (size={c['size']}, cohesion={c['cohesion']})",
        f"**Collections:** {colls}",
        "",
        "**Representative hadiths:**",
    ]
    for rh in c["representative_hadiths"]:
        grade = f" [{rh['gradeNorm']}]" if rh.get("gradeNorm") else ""
        lines.append(
            f"- **{rh['collection']} #{rh['hadithNumber']}**{grade} "
            f"(score {rh['score']}, urn {rh['urn']}): {rh['text'][:300]}"
        )
    lines.append("")

md_path = os.path.join(OUT_DIR, f"{INDEX}_cluster_report.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Written: {md_path}")
print("Done.")
