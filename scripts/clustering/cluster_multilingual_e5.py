"""
Cluster multilingual-e5 embeddings (1024-dim, English + Arabic combined)
using MiniBatchKMeans, then write cluster IDs back to ES and compute centroids.

Cross-lingual: Arabic and English hadiths share one embedding space, so
clusters reflect topic structure across both languages simultaneously.

Run inside the search container (has ES access + sklearn):
    docker exec search-web-1 python3 /code/scripts/clustering/cluster_multilingual_e5.py

Env vars (optional):
    ELASTIC_PASSWORD   (default: 123)
    K                  number of clusters (default: 150)
    BATCH_SIZE         ES scroll batch size (default: 500)
"""
import os, json, time
import numpy as np
from collections import defaultdict
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import normalize
from elasticsearch import Elasticsearch, helpers

ES_PW  = os.environ.get("ELASTIC_PASSWORD", "123")
INDEX  = "multilingual-e5"
K      = int(os.environ.get("K", 150))
BATCH  = int(os.environ.get("BATCH_SIZE", 500))
OUT_DIR = "/code/reports/clusters/multilingual-e5"
os.makedirs(OUT_DIR, exist_ok=True)

es = Elasticsearch("http://elasticsearch:9200", basic_auth=("elastic", ES_PW))

# ── Step 1: scan all embeddings ───────────────────────────────────────────────
print(f"Scanning {INDEX} for embeddings...")
t0 = time.time()

doc_ids, vectors_list, metas = [], [], []

for hit in helpers.scan(
    es, index=INDEX,
    query={"query": {"exists": {"field": "embedding"}}},
    _source_includes=["embedding", "urn", "lang", "collection", "hadithNumber",
                      "englishMatn", "arabicMatn", "isChainRef", "dupGroup", "gradeNorm"],
    size=BATCH,
):
    s = hit["_source"]
    vec = s.get("embedding")
    if not vec:
        continue
    doc_ids.append(hit["_id"])   # use actual ES _id, not urn
    vectors_list.append(vec)
    metas.append({
        "urn":         s.get("urn"),
        "lang":        s.get("lang", ""),
        "collection":  s.get("collection", ""),
        "hadithNumber":s.get("hadithNumber", ""),
        "isChainRef":  s.get("isChainRef", False),
        "dupGroup":    s.get("dupGroup"),
        "gradeNorm":   s.get("gradeNorm", ""),
        "text":        (s.get("englishMatn") or s.get("arabicMatn") or "").strip()[:300],
    })

print(f"  {len(doc_ids):,} docs loaded — {time.time()-t0:.0f}s")

# ── Step 2: normalize + cluster ───────────────────────────────────────────────
print(f"Running MiniBatchKMeans k={K}...")
t1 = time.time()
X = normalize(np.array(vectors_list, dtype=np.float32), norm="l2")
km = MiniBatchKMeans(
    n_clusters=K,
    batch_size=4096,
    max_iter=300,
    n_init=5,
    random_state=42,
    verbose=0,
)
labels = km.fit_predict(X)
print(f"  Clustered in {time.time()-t1:.0f}s  |  inertia={km.inertia_:.2f}")

# ── Step 3: write cluster IDs back to ES ─────────────────────────────────────
print("Writing clusterIdShared back to ES...")
t2 = time.time()

def bulk_updates(doc_ids, labels):
    for doc_id, cid in zip(doc_ids, labels):
        yield {
            "_op_type": "update",
            "_index": INDEX,
            "_id": doc_id,
            "doc": {"clusterIdShared": int(cid)},
        }

ok, errors = helpers.bulk(es, bulk_updates(doc_ids, labels), chunk_size=500, raise_on_error=False)
print(f"  {ok:,} updated, {len(errors)} errors — {time.time()-t2:.0f}s")

# ── Step 4: compute centroids + stats ─────────────────────────────────────────
print("Computing centroids...")
clusters = defaultdict(lambda: {"vectors": [], "metas": []})
for i, cid in enumerate(labels):
    clusters[int(cid)]["vectors"].append(X[i])
    clusters[int(cid)]["metas"].append(metas[i])

def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))

centroids_out = {}
for cid, data in sorted(clusters.items()):
    vecs  = np.array(data["vectors"])
    mds   = data["metas"]
    cent  = vecs.mean(axis=0)
    cent  = cent / (np.linalg.norm(cent) + 1e-9)
    scores = [cosine(cent, v) for v in vecs]
    cohesion = float(np.mean(scores))

    lang_counts = defaultdict(int)
    coll_counts = defaultdict(int)
    for m in mds:
        lang_counts[m["lang"]] += 1
        coll_counts[m["collection"]] += 1

    top_colls = dict(sorted(coll_counts.items(), key=lambda x: -x[1])[:8])

    ranked = sorted(
        [(scores[i], mds[i]) for i in range(len(mds)) if not mds[i].get("isChainRef")],
        key=lambda x: -x[0]
    )

    centroids_out[cid] = {
        "size":       len(vecs),
        "cohesion":   round(cohesion, 4),
        "lang_split": dict(lang_counts),
        "top_collections": top_colls,
        "centroid":   cent.tolist(),
        "representative_hadiths": [
            {"score": round(s, 4), **m} for s, m in ranked[:5]
        ],
    }

# ── Step 5: write JSON ────────────────────────────────────────────────────────
json_path = f"{OUT_DIR}/multilingual-e5_centroids.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(centroids_out, f, ensure_ascii=False)
print(f"Written: {json_path}")

# ── Step 6: markdown report ───────────────────────────────────────────────────
by_cohesion = sorted(centroids_out.items(), key=lambda x: -x[1]["cohesion"])
lines = [
    f"# Cluster Centroids — multilingual-e5",
    f"",
    f"**k:** {K} | **Total docs:** {len(doc_ids):,} "
    f"(en: {sum(1 for m in metas if m['lang']=='en'):,} / "
    f"ar: {sum(1 for m in metas if m['lang']=='ar'):,})",
    f"",
    "---",
    "",
    "## Clusters by cohesion",
    "",
    "| Cluster | Size | Cohesion | en | ar | Top collections | Top snippet |",
    "|---------|------|----------|----|----|-----------------|-------------|",
]
for cid, c in by_cohesion:
    colls = ", ".join(f"{k}({v})" for k, v in list(c["top_collections"].items())[:3])
    en = c["lang_split"].get("en", 0)
    ar = c["lang_split"].get("ar", 0)
    snippet = (c["representative_hadiths"][0]["text"][:100].replace("|", "/") + "…") if c["representative_hadiths"] else ""
    lines.append(f"| {cid} | {c['size']} | {c['cohesion']} | {en} | {ar} | {colls} | {snippet} |")

lines += ["", "---", "", "## Cluster details", ""]
for cid, c in by_cohesion:
    en = c["lang_split"].get("en", 0)
    ar = c["lang_split"].get("ar", 0)
    colls = ", ".join(f"{k}: {v}" for k, v in c["top_collections"].items())
    lines += [
        f"### Cluster {cid}  (size={c['size']}, cohesion={c['cohesion']}, en={en}, ar={ar})",
        f"**Collections:** {colls}",
        "",
        "**Representative hadiths:**",
    ]
    for rh in c["representative_hadiths"]:
        lang_tag = f"[{rh['lang']}]"
        grade = f" [{rh['gradeNorm']}]" if rh.get("gradeNorm") else ""
        lines.append(
            f"- {lang_tag} **{rh['collection']} #{rh['hadithNumber']}**{grade} "
            f"(score {rh['score']}): {rh['text'][:250]}"
        )
    lines.append("")

md_path = f"{OUT_DIR}/multilingual-e5_cluster_report.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Written: {md_path}")
print("Done.")
