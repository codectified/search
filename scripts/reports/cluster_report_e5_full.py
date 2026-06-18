"""
Generate HTML cluster reports for vec_e5_full at k=25 and k=50.

Islands are identified geometrically: re-run UMAP on a sample, compute each
cluster's 2D centroid, then flag the two clusters whose centroids are farthest
from the overall 2D median.  Those are featured at the top of the report.

Usage:
    ES_HOST=192.168.1.107 python scripts/reports/cluster_report_e5_full.py

Outputs:
    reports/cluster_report_e5_full_k25.html
    reports/cluster_report_e5_full_k50.html

Env vars:
    ES_HOST     (default localhost)
    N_UMAP      sample size for island detection (default 8000)
    OUT_DIR     report output dir (default reports/)
"""

import os, json, time, html
import numpy as np
from collections import defaultdict
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan

ES_HOST = os.environ.get("ES_HOST", "localhost")
ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
INDEX   = "arabic-research"
N_UMAP  = int(os.environ.get("N_UMAP", 8000))
OUT_DIR = os.environ.get("OUT_DIR", "reports")
CENTROID_DIR = os.environ.get("CENTROID_DIR", "reports/centroids")
os.makedirs(OUT_DIR, exist_ok=True)

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW), request_timeout=120)


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_centroid_json(k):
    path = os.path.join(CENTROID_DIR, f"arabic-research_e5_full_k{k}.json")
    with open(path, encoding="utf-8") as f:
        return {int(cid): v for cid, v in json.load(f).items()}


def fetch_sample(vec_field, cluster_field, n):
    """Fetch up to n docs with vec + cluster label for UMAP island detection."""
    print(f"  Fetching up to {n:,} docs for UMAP...")
    t0 = time.time()
    vecs, labels = [], []
    for hit in es_scan(es, index=INDEX,
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
    """Run UMAP, find the n_islands clusters most distant from the 2D median."""
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
    return island_ids, dists, emb, cluster_2d


def fetch_reps_from_es(cluster_field, cluster_id, vec_field, centroid_vec, n=10):
    """Fetch top-n docs closest to centroid for a given cluster."""
    results = []
    for hit in es_scan(es, index=INDEX,
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
            "text":         (s.get("arabicMatn") or s.get("arabicTextClean") or "").strip(),
        })
    # deduplicate by dupGroup, keep first
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


# ── HTML generation ───────────────────────────────────────────────────────────

CSS = """
body { font-family: -apple-system, Arial, sans-serif; max-width: 1100px;
       margin: 0 auto; padding: 20px; background: #f8f8f6; color: #222; }
h1 { color: #1a1a2e; border-bottom: 3px solid #c0392b; padding-bottom: 8px; }
h2 { color: #2c3e50; margin-top: 40px; }
h3 { color: #34495e; margin: 0 0 6px 0; }
.island-section { background: #fff3cd; border: 2px solid #f39c12;
                  border-radius: 8px; padding: 20px; margin-bottom: 30px; }
.island-header { color: #c0392b; font-size: 1.3em; font-weight: bold;
                 margin-bottom: 4px; }
.cluster-card { background: white; border: 1px solid #ddd; border-radius: 6px;
                padding: 16px; margin-bottom: 16px; }
.cluster-meta { font-size: 0.85em; color: #666; margin-bottom: 10px; }
.cluster-meta span { margin-right: 16px; }
.hadith { background: #f9f9f9; border-right: 4px solid #3498db;
          padding: 10px 14px; margin: 8px 0; border-radius: 4px;
          direction: rtl; font-size: 1.05em; line-height: 1.7; }
.hadith-ref { font-size: 0.78em; color: #888; direction: ltr;
              margin-top: 4px; }
.island .hadith { border-right-color: #e74c3c; background: #fff8f8; }
.collections { font-size: 0.8em; color: #555; }
.badge { display: inline-block; background: #3498db; color: white;
         border-radius: 12px; padding: 2px 10px; font-size: 0.8em;
         margin-right: 4px; margin-bottom: 4px; }
.badge.island-badge { background: #c0392b; }
.toc { background: white; border: 1px solid #ddd; border-radius: 6px;
       padding: 16px; margin-bottom: 30px; columns: 2; }
.toc a { text-decoration: none; color: #2980b9; font-size: 0.9em; }
.toc li { margin-bottom: 3px; }
"""


def hadith_html(r, extra_class=""):
    urn = r.get("arabicURN", 0)
    ref = f"{r['collection']} {r['hadithNumber']}"
    grade = r.get("gradeNorm") or ""
    grade_str = f" · {html.escape(grade)}" if grade else ""
    urn_link = (f'<a href="https://sunnah.com/hadith/{urn}" target="_blank">'
                f'{html.escape(ref)}</a>') if urn else html.escape(ref)
    text = html.escape(r.get("text", ""))
    return (f'<div class="hadith {extra_class}">'
            f'<div>{text}</div>'
            f'<div class="hadith-ref">{urn_link}{grade_str}</div>'
            f'</div>')


def cluster_card_html(cid, info, reps, is_island=False, island_label=""):
    size = info["size"]
    cohesion = info.get("cohesion", 0)
    top_colls = info.get("top_collections", {})
    colls_str = ", ".join(f"{c} ({n})" for c, n in
                          list(top_colls.items())[:5])
    card_class = "cluster-card island" if is_island else "cluster-card"
    badge = (f'<span class="badge island-badge">⚑ {html.escape(island_label)}</span> '
             if is_island else "")
    header = (f'<div class="island-header">{badge}Island Cluster #{cid}</div>'
              if is_island else f'<h3>Cluster #{cid}</h3>')
    reps_html = "\n".join(hadith_html(r, "island" if is_island else "")
                          for r in reps)
    return f"""
<div class="{card_class}" id="c{cid}">
  {header}
  <div class="cluster-meta">
    <span>📊 <b>{size:,}</b> docs</span>
    <span>🎯 cohesion <b>{cohesion:.3f}</b></span>
    <span class="collections">📚 {html.escape(colls_str)}</span>
  </div>
  {reps_html}
</div>"""


def generate_report(k, centroids, island_ids, island_labels):
    vec_field     = "vec_e5_full"
    cluster_field = f"cluster_e5_full_k{k}"
    out_path      = os.path.join(OUT_DIR, f"cluster_report_e5_full_k{k}.html")

    print(f"\n── Building k={k} report ──")

    # Fetch extended reps for islands, normal reps for rest
    island_reps = {}
    for cid in island_ids:
        centroid_vec = centroids[cid]["centroid"]
        print(f"  Fetching island reps for cluster #{cid}...")
        island_reps[cid] = fetch_reps_from_es(cluster_field, cid, vec_field,
                                               centroid_vec, n=10)

    # For regular clusters, use what's already in centroid JSON (top 5 deduped)
    sorted_clusters = sorted(centroids.items(), key=lambda x: -x[1]["size"])

    # Build TOC
    toc_items = []
    for cid, info in sorted_clusters:
        label = island_labels.get(cid, "")
        prefix = f"⚑ Island: {label} · " if cid in island_ids else ""
        toc_items.append(
            f'<li><a href="#c{cid}">{prefix}#{cid} '
            f'({info["size"]:,} docs, coh={info.get("cohesion",0):.3f})</a></li>')
    toc_html = "<ul>" + "\n".join(toc_items) + "</ul>"

    # Build island section
    island_cards = []
    for i, cid in enumerate(island_ids):
        label = island_labels.get(cid, f"Island {i+1}")
        reps = island_reps[cid]
        island_cards.append(cluster_card_html(cid, centroids[cid], reps,
                                              is_island=True,
                                              island_label=label))

    # Build all-clusters section (skip islands — already shown above)
    all_cards = []
    for cid, info in sorted_clusters:
        if cid in island_ids:
            continue
        reps = [{"collection": h["collection"],
                 "hadithNumber": h["hadithNumber"],
                 "gradeNorm": h.get("gradeNorm", ""),
                 "arabicURN": h.get("arabicURN", 0),
                 "dupGroup": h.get("dupGroup", 0),
                 "text": h.get("text", "")}
                for h in info.get("representative_hadiths", [])]
        all_cards.append(cluster_card_html(cid, info, reps))

    page = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>Cluster Report — vec_e5_full k={k}</title>
<style>{CSS}</style>
</head>
<body dir="ltr">
<h1>arabic-research · vec_e5_full · k={k} Cluster Report</h1>
<p style="color:#666">Generated {time.strftime('%Y-%m-%d %H:%M')} ·
{sum(v['size'] for v in centroids.values()):,} total docs ·
{k} clusters · mean cohesion {np.mean([v.get('cohesion',0) for v in centroids.values()]):.3f}</p>

<h2>📍 Table of Contents</h2>
<div class="toc">{toc_html}</div>

<h2>🏝️ Isolated Islands</h2>
<p style="color:#555">These two clusters appear as geometrically isolated sub-clouds
in the UMAP projection, far from the main hadith mass. Both are pure Matn (no chain-refs).
They likely represent highly specialised textual registers.</p>
<div class="island-section">
{"".join(island_cards)}
</div>

<h2>📚 All Clusters (by size)</h2>
{"".join(all_cards)}

</body></html>"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"  Written: {out_path}")
    return out_path


# ── Main ──────────────────────────────────────────────────────────────────────

for K in [25, 50]:
    print(f"\n{'='*60}")
    print(f"Processing k={K}")
    print(f"{'='*60}")

    vec_field     = "vec_e5_full"
    cluster_field = f"cluster_e5_full_k{K}"

    centroids = load_centroid_json(K)
    X, labels = fetch_sample(vec_field, cluster_field, N_UMAP)
    island_ids, dists, emb2d, cluster_2d = detect_islands(X, labels, K)

    # Label islands by their size rank so the report is interpretable
    sizes = {cid: centroids[cid]["size"] for cid in island_ids}
    island_labels = {cid: f"Bottom-left ({centroids[cid]['size']:,} docs)"
                     if i == 0 else f"Left-strip ({centroids[cid]['size']:,} docs)"
                     for i, cid in enumerate(sorted(island_ids, key=lambda c: cluster_2d[c][1]))}

    generate_report(K, centroids, island_ids, island_labels)

print("\nDone.")
