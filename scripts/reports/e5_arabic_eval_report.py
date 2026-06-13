"""
Generate a rich evaluation report for e5_arabic clusters.

Fetches full arabicText + arabicMatn + hadMatnTag from ES for each
representative hadith so you can visually evaluate matn extraction quality
and check why certain clusters are isolated (e.g. bad extractions).

Usage (inside container):
    docker exec -e ELASTIC_PASSWORD=docker123 -e ES_HOST=172.31.250.10 -e K=25 \\
        search-web-1 python3 /code/scripts/reports/e5_arabic_eval_report.py

Env vars:
    K           cluster count to report (default 25)
    OUTLIER_ID  cluster ID to highlight as outlier (auto-detected if not set)
    REPS        number of representative hadiths per cluster (default 8)
    OUT_DIR     output directory (default /code/reports/cluster_reports)
"""
import os, json, sys
from collections import defaultdict
from elasticsearch import Elasticsearch

ES_PW   = os.environ.get("ELASTIC_PASSWORD", "docker123")
ES_HOST = os.environ.get("ES_HOST", "localhost")
K       = int(os.environ.get("K", 25))
REPS    = int(os.environ.get("REPS", 8))
OUT_DIR = os.environ.get("OUT_DIR", "/code/reports/cluster_reports")
os.makedirs(OUT_DIR, exist_ok=True)

CENTROID_PATH = f"/code/reports/centroids/arabic-research_e5_arabic_k{K}.json"

es = Elasticsearch(f"http://{ES_HOST}:9200",
                   basic_auth=("elastic", ES_PW), request_timeout=120)

with open(CENTROID_PATH, encoding="utf-8") as f:
    data = json.load(f)


def find_outlier(data):
    """Return the cluster ID most isolated from other centroids."""
    try:
        import numpy as np
        cids = [int(k) for k in data]
        centroids = [data[str(c)]["centroid"] for c in cids]
        C = __import__("numpy").array(centroids, dtype="float32")
        C /= (__import__("numpy").linalg.norm(C, axis=1, keepdims=True) + 1e-9)
        sim = C @ C.T
        __import__("numpy").fill_diagonal(sim, -1.0)
        nearest = sim.max(axis=1)
        return str(cids[int(nearest.argmin())])
    except Exception:
        return None


OUTLIER_ID = os.environ.get("OUTLIER_ID") or find_outlier(data)
print(f"Outlier cluster: {OUTLIER_ID}")


def fetch_full(urn):
    """Fetch full hadith fields from ES by arabicURN."""
    doc_id = f"arabic:{urn}"
    try:
        r = es.get(index="arabic-research", id=doc_id,
                   _source=["arabicText", "arabicMatn", "hadMatnTag",
                            "gradeArabic", "gradeEnglish", "gradeNorm",
                            "collection", "hadithNumber"])
        return r["_source"]
    except Exception:
        return {}


def mark_boundary(full_text, matn):
    """
    Try to find where matn starts in full_text.
    Returns (isnad_part, matn_part) or (None, None) if not found.
    """
    if not full_text or not matn:
        return None, None
    # Strip whitespace and try substring search
    matn_stripped = matn.strip()
    full_stripped = full_text.strip()
    idx = full_stripped.find(matn_stripped[:40])  # search by first 40 chars
    if idx > 0:
        return full_stripped[:idx].strip(), full_stripped[idx:].strip()
    return None, None


# Sort clusters: outlier first, then by cohesion descending
def sort_key(item):
    cid, c = item
    if str(cid) == str(OUTLIER_ID):
        return (0, -c["cohesion"])
    return (1, -c["cohesion"])

sorted_clusters = sorted(data.items(), key=sort_key)

total = sum(c["size"] for c in data.values())
lines = [
    f"# e5_arabic Cluster Evaluation Report — k={K}",
    "",
    f"**Total docs:** {total:,} | **Clusters:** {len(data)} | "
    f"**Mean size:** {total // len(data):,}",
    "",
    f"> **Outlier cluster:** {OUTLIER_ID} "
    f"(most isolated centroid — check for matn extraction errors)",
    "",
    "---",
    "",
]

for cid, c in sorted_clusters:
    is_outlier = str(cid) == str(OUTLIER_ID)
    flag = " ⚠️ OUTLIER ISLAND" if is_outlier else ""
    colls_str = " | ".join(f"{k}: {v}" for k, v in c["top_collections"].items())
    pct = 100 * c["size"] / total

    lines += [
        f"## Cluster {cid}{flag}",
        f"**Size:** {c['size']:,} ({pct:.1f}%) | "
        f"**Cohesion:** {c['cohesion']} | "
        f"**Collections:** {colls_str}",
        "",
    ]

    if is_outlier:
        lines += [
            "> This cluster is spatially isolated in UMAP — it likely contains "
            "hadiths with systematically different text structure (e.g. grade "
            "comments extracted as matn, or a distinct genre).",
            "",
        ]

    # Fetch up to REPS representatives from ES
    reps = c["representative_hadiths"][:REPS]
    fetched_urns = set()

    for rep in reps:
        urn = rep.get("arabicURN", 0)
        if not urn or urn in fetched_urns:
            continue
        fetched_urns.add(urn)

        full = fetch_full(urn)
        arabic_text  = (full.get("arabicText") or "").strip()
        arabic_matn  = (full.get("arabicMatn") or rep.get("text") or "").strip()
        had_matn_tag = full.get("hadMatnTag", False)
        grade_norm   = full.get("gradeNorm") or rep.get("gradeNorm") or ""
        grade_ar     = (full.get("gradeArabic") or "").strip()
        grade_en     = (full.get("gradeEnglish") or "").strip()
        collection   = rep.get("collection", "")
        hadith_num   = rep.get("hadithNumber", "")

        grade_parts = []
        if grade_norm and grade_norm != "Uncategorized":
            grade_parts.append(f"`{grade_norm}`")
        if grade_ar:
            grade_parts.append(grade_ar)
        if grade_en:
            grade_parts.append(f"*{grade_en}*")
        grade_str = "  ".join(grade_parts) if grade_parts else ""

        matn_tag_str = "✅ matn tagged" if had_matn_tag else "❌ no matn tag"

        lines.append(
            f"### {collection} #{hadith_num}  |  {grade_str}  |  {matn_tag_str}"
        )
        lines.append("")

        if arabic_text:
            isnad_part, matn_part = mark_boundary(arabic_text, arabic_matn)
            if isnad_part and matn_part:
                lines += [
                    "**Full text (isnad + matn):**",
                    "",
                    f"*[ISNAD]* {isnad_part}",
                    "",
                    f"**[MATN]** {matn_part}",
                    "",
                ]
            else:
                lines += [
                    "**Full text:**",
                    "",
                    arabic_text,
                    "",
                ]
            if arabic_matn and arabic_matn != arabic_text:
                lines += [
                    "**Extracted matn** (arabicMatn field):",
                    "",
                    f"> {arabic_matn}",
                    "",
                ]
        else:
            lines += [
                "**Extracted matn** (no arabicText in index):",
                "",
                arabic_matn,
                "",
            ]

        lines.append("---")
        lines.append("")

    lines.append("")

out_path = f"{OUT_DIR}/arabic-research_e5_arabic_k{K}_eval.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Written: {out_path}")
