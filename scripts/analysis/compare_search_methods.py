"""
Compares two kNN search approaches on the arabic-openai index:
  1. Centroid-filtered  — top-2 cluster pre-filter (~3,500 docs)
  2. Straight kNN       — full index, no filter (131,728 docs)

Run inside container:
    docker exec search-web-1 python3 /code/tests/compare_search_methods.py

Output: /code/test results & reports/search_comparison.md
"""
import json, os, re, time
import numpy as np
from openai import OpenAI
from elasticsearch import Elasticsearch
from sklearn.preprocessing import normalize

# ── Config ────────────────────────────────────────────────────────────────────

OPENAI_MODEL    = "text-embedding-3-small"
ARABIC_INDEX    = "arabic-openai"
CENTROIDS_PATH  = "/code/arabic_cluster_centroids_final.json"
TOP_N_CLUSTERS  = 2
TOP_K           = 20
MAX_TEXT        = 250   # chars of hadith body to show

QUERIES = [
    "prayer times",
    "comparing yourself to others",
    "zakah on wealth",
    "treatment of parents",
    "aisha",
]

# ── Clients ───────────────────────────────────────────────────────────────────

openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
es = Elasticsearch(
    "http://elasticsearch:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
)

with open(CENTROIDS_PATH) as f:
    CENTROIDS = normalize(np.array(json.load(f), dtype=np.float32), norm="l2")


# ── Helpers ───────────────────────────────────────────────────────────────────

def embed(query):
    resp = openai_client.embeddings.create(model=OPENAI_MODEL, input=query)
    vec = np.array(resp.data[0].embedding, dtype=np.float32)
    return vec / np.linalg.norm(vec)


def top_clusters(qvec, n=TOP_N_CLUSTERS):
    scores = CENTROIDS @ qvec
    return np.argsort(scores)[::-1][:n].tolist()


def knn_search(qvec, filter_clause=None, k=TOP_K):
    body = {
        "field": "embedding",
        "query_vector": qvec.tolist(),
        "k": k,
        "num_candidates": min(k * 20, 1000),
    }
    if filter_clause:
        body["filter"] = filter_clause
    t0 = time.perf_counter()
    resp = es.search(
        index=ARABIC_INDEX,
        knn=body,
        size=k,
        _source={"excludes": ["embedding"]},
    )
    ms = round((time.perf_counter() - t0) * 1000)
    return resp["hits"]["hits"], ms


def clean_text(raw):
    if not raw:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)       # strip HTML tags
    text = re.sub(r"\s+", " ", text).strip()
    return text[:MAX_TEXT]


def hadith_body(src):
    """Return best available text: English, then Arabic matn, then Arabic full."""
    eng = clean_text(src.get("englishText") or "")
    if eng:
        return eng, "en"
    ar_matn = clean_text(src.get("arabicMatn") or "")
    if ar_matn:
        return ar_matn, "ar-matn"
    ar_full = clean_text(src.get("arabicText") or "")
    return ar_full[:MAX_TEXT], "ar-full"


def urn_key(hit):
    s = hit["_source"]
    return s.get("arabicURN") or s.get("englishURN")


# ── Per-query comparison ──────────────────────────────────────────────────────

def compare_query(query):
    print(f"  Embedding '{query}' ...", end=" ", flush=True)
    t0 = time.perf_counter()
    qvec = embed(query)
    embed_ms = round((time.perf_counter() - t0) * 1000)
    print(f"{embed_ms}ms")

    clusters = top_clusters(qvec)

    print(f"    centroid kNN (clusters {clusters}) ...", end=" ", flush=True)
    c_hits, c_ms = knn_search(qvec, filter_clause={"terms": {"clusterIdFinal": clusters}})
    print(f"{c_ms}ms")

    print(f"    straight kNN ...", end=" ", flush=True)
    s_hits, s_ms = knn_search(qvec)
    print(f"{s_ms}ms")

    c_urns = {urn_key(h) for h in c_hits}
    s_urns = {urn_key(h) for h in s_hits}
    shared = c_urns & s_urns
    jaccard = round(len(shared) / len(c_urns | s_urns), 3) if c_urns | s_urns else 0

    return {
        "query": query,
        "embed_ms": embed_ms,
        "clusters": clusters,
        "centroid": {"hits": c_hits, "ms": c_ms},
        "straight": {"hits": s_hits, "ms": s_ms},
        "shared_urns": shared,
        "overlap": len(shared),
        "jaccard": jaccard,
    }


# ── Report ────────────────────────────────────────────────────────────────────

def result_table(hits, shared_urns, label):
    lines = []
    lines.append(f"#### {label}\n")
    lines.append("| # | Score | Collection | Hadith | Cluster | Tag | Text |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, h in enumerate(hits, 1):
        s = h["_source"]
        score  = f"{h['_score']:.4f}"
        coll   = s.get("collection", "?")
        num    = s.get("hadithNumber") or ""
        clust  = s.get("clusterIdFinal", "?")
        matn   = "✓" if s.get("hadMatnTag") else "~"
        text, lang = hadith_body(s)
        # Mark rows shared between methods
        shared_marker = "" if urn_key(h) in shared_urns else " ★"
        lang_tag = f" `[{lang}]`" if lang != "en" else ""
        text_cell = text.replace("|", "｜")  # avoid breaking table
        lines.append(
            f"| {i}{shared_marker} | {score} | {coll} | {num} | C{clust} | {matn} | "
            f"{text_cell}{lang_tag} |"
        )
    return "\n".join(lines)


def build_report(all_results):
    lines = [
        "# Arabic kNN Search Comparison — Centroid-Filtered vs Straight\n",
        f"**Model:** OpenAI `{OPENAI_MODEL}` | **Index:** `{ARABIC_INDEX}` | **k={TOP_K}**\n",
        f"**Centroid pre-filter:** top {TOP_N_CLUSTERS} clusters ≈ {TOP_N_CLUSTERS * 1756:,} docs vs 131,728 full corpus\n",
        "★ = result unique to that method (not in the other top-20)\n",
        "`[ar-matn]` = Arabic matn shown (no English translation) · `[ar-full]` = full Arabic text (no matn tag)\n",
    ]

    # Summary table
    lines.append("\n## Summary\n")
    lines.append("| Query | Embed ms | Centroid ES ms | Straight ES ms | Overlap/20 | Jaccard | Clusters |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in all_results:
        lines.append(
            f"| {r['query']} | {r['embed_ms']} | {r['centroid']['ms']} | {r['straight']['ms']} "
            f"| {r['overlap']}/{TOP_K} | {r['jaccard']} | {r['clusters']} |"
        )

    # Per-query sections
    for r in all_results:
        lines.append(f"\n---\n\n## \"{r['query']}\"\n")
        lines.append(
            f"Embed: **{r['embed_ms']}ms** | Clusters selected: **{r['clusters']}** | "
            f"Centroid ES: **{r['centroid']['ms']}ms** | Straight ES: **{r['straight']['ms']}ms** | "
            f"Overlap: **{r['overlap']}/{TOP_K}** (Jaccard {r['jaccard']})\n"
        )
        lines.append(result_table(r["centroid"]["hits"], r["shared_urns"], "Centroid-filtered kNN"))
        lines.append("")
        lines.append(result_table(r["straight"]["hits"], r["shared_urns"], "Straight kNN (full index)"))

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    OUT = "/code/test results & reports/search_comparison.md"
    all_results = []

    for q in QUERIES:
        print(f"\nQuery: '{q}'")
        all_results.append(compare_query(q))

    print("\nBuilding report...")
    report = build_report(all_results)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Written: {OUT}\n")

    print("Summary:")
    print(f"  {'Query':<35} {'EmbMs':>6} {'CentMs':>7} {'StrMs':>6} {'J':>6}  Clusters")
    print("  " + "-" * 75)
    for r in all_results:
        print(
            f"  {r['query']:<35} {r['embed_ms']:>6} {r['centroid']['ms']:>7} "
            f"{r['straight']['ms']:>6} {r['jaccard']:>6}  {r['clusters']}"
        )
