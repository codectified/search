"""
Generate Markdown cluster reports for vec_e5_full at k=25 and k=50.

Images are referenced with relative paths to the already-committed PNGs in
reports/viz/ — renders correctly on GitHub without any hosting.

Islands are identified geometrically: re-run UMAP on a sample, compute each
cluster's 2D centroid, then flag the two clusters whose centroids are farthest
from the overall 2D median.

Usage:
    ES_HOST=192.168.1.107 python scripts/reports/cluster_report_e5_full.py

Outputs:
    reports/cluster_report_e5_full_k25.md
    reports/cluster_report_e5_full_k50.md

Env vars:
    ES_HOST       (default localhost)
    N_UMAP        sample size for island detection (default 8000)
    OUT_DIR       report output dir (default reports/)
    CENTROID_DIR  centroid JSON dir (default reports/centroids)
    VIZ_RELPATH   relative path from OUT_DIR to viz folder (default viz)
"""

import os, json, time
import numpy as np
from collections import defaultdict
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

ES_HOST      = os.environ.get("ES_HOST", "localhost")
ES_PW        = os.environ.get("ELASTIC_PASSWORD", "docker123")
INDEX        = "arabic-research"
N_UMAP       = int(os.environ.get("N_UMAP", 8000))
OUT_DIR      = os.environ.get("OUT_DIR", "reports")
CENTROID_DIR = os.environ.get("CENTROID_DIR", "reports/centroids")
VIZ_REL      = os.environ.get("VIZ_RELPATH", "viz")  # relative to OUT_DIR

# Known island cluster IDs from previous UMAP run (set to "" to re-detect via ES)
KNOWN_ISLANDS = os.environ.get("KNOWN_ISLANDS", "")

os.makedirs(OUT_DIR, exist_ok=True)

_es = None
def get_es():
    global _es
    if _es is None:
        _es = Elasticsearch(f"http://{ES_HOST}:9200",
                            basic_auth=("elastic", ES_PW), request_timeout=120)
    return _es


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_centroid_json(k):
    path = os.path.join(CENTROID_DIR, f"arabic-research_e5_full_k{k}.json")
    with open(path, encoding="utf-8") as f:
        return {int(cid): v for cid, v in json.load(f).items()}


def fetch_sample(vec_field, cluster_field, n):
    print(f"  Fetching up to {n:,} docs for UMAP...")
    t0 = time.time()
    vecs, labels = [], []
    for hit in es_scan(get_es(), index=INDEX,
            query={"query": {"bool": {"must": [
                {"exists": {"field": vec_field}},
                {"exists": {"field": cluster_field}},
            ]}}},
            _source=[vec_field, cluster_field], size=500):
        s = hit["_source"]
        v = s.get(vec_field)
        c = s.get(cluster_field)
        if v is None or c is None:
            continue
        vecs.append(v)
        labels.append(c)
        if len(vecs) >= n:
            break
    X = np.array(vecs, dtype=np.float32)
    X /= np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-9)
    labels = np.array(labels, dtype=np.int32)
    print(f"  {len(X):,} docs fetched in {time.time()-t0:.0f}s")
    return X, labels


def detect_islands(X, labels, k, n_islands=2):
    from umap import UMAP
    print(f"  Running UMAP on {len(X):,} points...")
    t0 = time.time()
    reducer = UMAP(n_components=2, n_neighbors=15, min_dist=0.1,
                   metric="cosine", random_state=42, n_jobs=1, verbose=False)
    emb = reducer.fit_transform(X)
    print(f"  UMAP done in {time.time()-t0:.0f}s")

    global_med = np.median(emb, axis=0)
    cluster_2d = {}
    for cid in range(k):
        mask = labels == cid
        if mask.sum() < 2:
            continue
        cluster_2d[cid] = emb[mask].mean(axis=0)

    dists = {cid: float(np.linalg.norm(c2d - global_med))
             for cid, c2d in cluster_2d.items()}
    island_ids = sorted(dists, key=lambda c: -dists[c])[:n_islands]
    print(f"  Island cluster IDs: {island_ids} "
          f"(distances: {[round(dists[i],2) for i in island_ids]})")
    return island_ids, cluster_2d


def fetch_reps_from_es(cluster_field, cluster_id, n=10):
    results = []
    for hit in es_scan(get_es(), index=INDEX,
            query={"query": {"bool": {"must": [
                {"term": {cluster_field: cluster_id}},
            ], "must_not": [{"term": {"isChainRef": True}}]}}},
            _source=["arabicTextClean", "arabicMatn", "collection",
                     "hadithNumber", "gradeNorm", "arabicURN", "dupGroup"],
            size=200):
        s = hit["_source"]
        results.append({
            "collection":   s.get("collection", ""),
            "hadithNumber": s.get("hadithNumber", ""),
            "gradeNorm":    s.get("gradeNorm", ""),
            "arabicURN":    s.get("arabicURN", 0),
            "dupGroup":     s.get("dupGroup", 0),
            # Prefer full clean text; fall back to matn only
            "fullText":     (s.get("arabicTextClean") or "").strip(),
            "matn":         (s.get("arabicMatn") or "").strip(),
        })
    seen, deduped = set(), []
    for r in results:
        g = r["dupGroup"] or 0
        if g and g in seen:
            continue
        if g:
            seen.add(g)
        deduped.append(r)
        if len(deduped) >= n:
            break
    return deduped


def es_available():
    try:
        get_es().info()
        return True
    except Exception:
        return False


# ── Markdown helpers ──────────────────────────────────────────────────────────

def img(rel_path, alt=""):
    return f"![{alt}]({rel_path})"


def hadith_md(r):
    # Full clean text preferred; matn as fallback for offline centroid-JSON reps
    full_text = r.get("fullText", "").strip()
    matn      = r.get("matn", r.get("text", "")).strip()
    display   = full_text or matn

    coll      = r.get("collection", "")
    num       = r.get("hadithNumber", "")
    urn       = r.get("arabicURN", 0)
    grade     = r.get("gradeNorm", "")

    ref_label = f"{coll} {num}".strip()
    ref_link  = (f"[{ref_label}](https://sunnah.com/hadith/{urn})"
                 if urn else ref_label)
    grade_str = f" · *{grade}*" if grade else ""

    # Bold ref line above the Arabic block, grade after
    header = f"**{ref_link}**{grade_str}"

    return (f'{header}\n\n'
            f'<div dir="rtl" style="border-right:4px solid #3498db;'
            f'padding:8px 12px;margin:4px 0 12px 0;background:#f9f9f9;">\n\n'
            f'{display}\n\n'
            f'</div>\n')


def cluster_section_md(cid, info, reps, is_island=False):
    size     = info["size"]
    cohesion = info.get("cohesion", 0)
    top_colls = info.get("top_collections", {})
    colls_str = " · ".join(f"{c} ({n})" for c, n in list(top_colls.items())[:5])

    if is_island:
        header = f"### 🏝️ Island Cluster #{cid}"
    else:
        header = f"### Cluster #{cid}"

    meta = (f"**{size:,} docs** · cohesion **{cohesion:.3f}** · "
            f"collections: {colls_str}")

    reps_md = "\n".join(hadith_md(r) for r in reps)
    return f"{header}\n\n{meta}\n\n{reps_md}\n\n---\n"


# ── Report generation ─────────────────────────────────────────────────────────

def generate_report(k, centroids, island_ids, island_labels):
    cluster_field = f"cluster_e5_full_k{k}"
    slug          = f"e5_full_k{k}"
    out_path      = os.path.join(OUT_DIR, f"cluster_report_e5_full_k{k}.md")
    vp            = VIZ_REL  # relative path prefix from reports/

    print(f"\n── Building k={k} Markdown report ──")

    use_es = es_available()
    print(f"  ES available: {use_es} — {'fetching full text' if use_es else 'using centroid JSON reps (matn only)'}")

    def get_reps(cid, n=5):
        if use_es:
            return fetch_reps_from_es(cluster_field, cid, n=n)
        # Offline: convert centroid JSON reps (matn stored as "text")
        return [{"collection":   h["collection"],
                 "hadithNumber": h["hadithNumber"],
                 "gradeNorm":    h.get("gradeNorm", ""),
                 "arabicURN":    h.get("arabicURN", 0),
                 "dupGroup":     h.get("dupGroup", 0),
                 "fullText":     "",
                 "matn":         h.get("text", "")}
                for h in centroids[cid].get("representative_hadiths", [])]

    # Fetch reps for islands (more reps when online)
    island_reps = {cid: get_reps(cid, n=10 if use_es else 5)
                   for cid in island_ids}

    sorted_clusters = sorted(centroids.items(), key=lambda x: -x[1]["size"])
    mean_coh = np.mean([v.get("cohesion", 0) for v in centroids.values()])
    total    = sum(v["size"] for v in centroids.values())

    # TOC
    toc_lines = []
    for cid, info in sorted_clusters:
        prefix = "🏝️ Island: " if cid in island_ids else ""
        anchor = f"cluster-{cid}"
        toc_lines.append(
            f"- [{prefix}#{cid} — {info['size']:,} docs, "
            f"coh={info.get('cohesion',0):.3f}](#{anchor})")
    toc = "\n".join(toc_lines)

    # Island sections
    island_sections = []
    for cid in island_ids:
        label = island_labels.get(cid, f"Island {cid}")
        info  = centroids[cid]
        reps  = island_reps[cid]
        island_sections.append(
            f"> **🏝️ {label}** — {info['size']:,} docs · "
            f"cohesion {info.get('cohesion',0):.3f}\n\n" +
            cluster_section_md(cid, info, reps, is_island=True))
    island_block = "\n".join(island_sections)

    # All clusters
    all_sections = []
    for cid, info in sorted_clusters:
        if cid in island_ids:
            continue
        if use_es:
            reps = get_reps(cid, n=5)
        else:
            reps = [{"collection":   h["collection"],
                     "hadithNumber": h["hadithNumber"],
                     "gradeNorm":    h.get("gradeNorm", ""),
                     "arabicURN":    h.get("arabicURN", 0),
                     "dupGroup":     h.get("dupGroup", 0),
                     "fullText":     "",
                     "matn":         h.get("text", "")}
                    for h in info.get("representative_hadiths", [])]
        all_sections.append(cluster_section_md(cid, info, reps))
    all_block = "\n".join(all_sections)

    md = f"""# arabic-research · vec_e5_full · k={k} Cluster Report

*{time.strftime('%Y-%m-%d')} · {total:,} docs · {k} clusters · mean cohesion {mean_coh:.3f}*

## Visualizations

| UMAP (by cluster) | UMAP (by collection) |
|---|---|
| {img(f"{vp}/umap/arabic-research_{slug}.png", "UMAP clusters")} | {img(f"{vp}/umap/arabic-research_{slug}_by_collection.png", "UMAP by collection")} |

| UMAP (by matn length) | UMAP (matn vs chain-ref) |
|---|---|
| {img(f"{vp}/umap/arabic-research_{slug}_by_length.png", "UMAP by length")} | {img(f"{vp}/umap/arabic-research_{slug}_chainrefs.png", "UMAP chain-refs")} |

| Cluster sizes | Cohesion distribution |
|---|---|
| {img(f"{vp}/sizes/arabic-research_{slug}.png", "Cluster sizes")} | {img(f"{vp}/cohesion/arabic-research_{slug}.png", "Cohesion")} |

---

## 🏝️ Isolated Islands

These two clusters appear as geometrically isolated sub-clouds in the UMAP projection,
far from the main hadith mass. Both are pure Matn (no chain-refs) — likely highly
specialised textual registers.

{island_block}

---

## 📚 All Clusters (by size)

{toc}

---

{all_block}
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  Written: {out_path}")
    return out_path


# ── Known islands per k (from prior UMAP run; avoids needing live ES) ─────────
ISLANDS_BY_K = {
    25: [5, 12],
    50: [41, 11],
}

# ── Main ──────────────────────────────────────────────────────────────────────

for K in [25, 50]:
    print(f"\n{'='*60}")
    print(f"Processing k={K}")
    print(f"{'='*60}")

    vec_field     = "vec_e5_full"
    cluster_field = f"cluster_e5_full_k{K}"
    centroids     = load_centroid_json(K)

    if KNOWN_ISLANDS:
        island_ids = [int(x) for x in KNOWN_ISLANDS.split(",")]
        print(f"  Using provided island IDs: {island_ids}")
        # label by size (smallest = the tighter island)
        island_ids_sorted = sorted(island_ids, key=lambda c: centroids[c]["size"])
        island_labels = {
            island_ids_sorted[0]: f"Bottom-left island ({centroids[island_ids_sorted[0]]['size']:,} docs)",
            island_ids_sorted[1]: f"Left-strip island ({centroids[island_ids_sorted[1]]['size']:,} docs)",
        }
    elif K in ISLANDS_BY_K:
        island_ids = ISLANDS_BY_K[K]
        print(f"  Using cached island IDs for k={K}: {island_ids}")
        island_ids_sorted = sorted(island_ids, key=lambda c: centroids[c]["size"])
        island_labels = {
            island_ids_sorted[0]: f"Bottom-left island ({centroids[island_ids_sorted[0]]['size']:,} docs)",
            island_ids_sorted[1]: f"Left-strip island ({centroids[island_ids_sorted[1]]['size']:,} docs)",
        }
    else:
        print("  Re-detecting islands via ES+UMAP...")
        X, labels = fetch_sample(vec_field, cluster_field, N_UMAP)
        island_ids, cluster_2d = detect_islands(X, labels, K)
        island_ids_sorted = sorted(island_ids, key=lambda c: cluster_2d[c][1])
        island_labels = {
            island_ids_sorted[0]: f"Bottom-left island ({centroids[island_ids_sorted[0]]['size']:,} docs)",
            island_ids_sorted[1]: f"Left-strip island ({centroids[island_ids_sorted[1]]['size']:,} docs)",
        }

    generate_report(K, centroids, island_ids, island_labels)

print("\nDone.")
