"""
Generate a markdown cluster report from a centroid JSON file.

Usage (inside container):
    python3 /code/scripts/clustering/generate_cluster_report.py \\
        /code/reports/centroids/arabic-research_e5_arabic_k50.json

Output: /code/reports/cluster_reports/arabic-research_e5_arabic_k50.md
"""
import sys, json, os

if len(sys.argv) < 2:
    print("Usage: generate_cluster_report.py <centroids_json>")
    sys.exit(1)

json_path = sys.argv[1]
basename  = os.path.splitext(os.path.basename(json_path))[0]  # e.g. arabic-research_e5_arabic_k50

OUT_DIR = "/code/reports/cluster_reports"
os.makedirs(OUT_DIR, exist_ok=True)
out_path = f"{OUT_DIR}/{basename}.md"

with open(json_path, encoding="utf-8") as f:
    data = json.load(f)

by_cohesion = sorted(data.items(), key=lambda x: -x[1]["cohesion"])
by_size     = sorted(data.items(), key=lambda x: -x[1]["size"])
total = sum(c["size"] for c in data.values())
K = len(data)

# Parse model and k from filename
parts = basename.split("_")  # arabic-research_e5_arabic_k50
k_str = [p for p in parts if p.startswith("k") and p[1:].isdigit()]
model_str = basename.replace("arabic-research_", "").replace(f"_{k_str[0]}" if k_str else "", "")
k_val = k_str[0] if k_str else "k?"

lines = [
    f"# Cluster Report — arabic-research / {model_str} / {k_val}",
    "",
    f"**Total docs:** {total:,} | **Clusters:** {K} | "
    f"**Mean size:** {total//K:,} | "
    f"**Min:** {min(c['size'] for c in data.values())} | "
    f"**Max:** {max(c['size'] for c in data.values())}",
    "",
    "---",
    "",
    "## Summary (sorted by cohesion — tightest clusters first)",
    "",
    "| Rank | ID | Size | % corpus | Cohesion | Top collections | Representative snippet |",
    "|------|----|------|----------|----------|-----------------|------------------------|",
]

for rank, (cid, c) in enumerate(by_cohesion, 1):
    colls = ", ".join(f"{k}({v})" for k, v in list(c["top_collections"].items())[:3])
    rh = c["representative_hadiths"]
    snippet = (rh[0]["text"][:70].replace("|", "/") + "…") if rh else ""
    pct = 100 * c["size"] / total
    lines.append(
        f"| {rank} | {cid} | {c['size']:,} | {pct:.1f}% | {c['cohesion']} | {colls} | {snippet} |"
    )

lines += [
    "",
    "---",
    "",
    "## Cluster details",
    "",
    "> Sorted by cohesion (highest = most semantically tight).",
    "> 🔴 = top 5 tightest clusters (most likely visually isolated in UMAP).",
    "",
]

for rank, (cid, c) in enumerate(by_cohesion, 1):
    flag = " 🔴" if rank <= 5 else ""
    colls_detail = " | ".join(f"{k}: {v}" for k, v in c["top_collections"].items())
    pct = 100 * c["size"] / total

    lines += [
        f"### Cluster {cid}{flag} — rank #{rank} by cohesion",
        f"**Size:** {c['size']:,} ({pct:.1f}% of corpus) | "
        f"**Cohesion:** {c['cohesion']}",
        f"**Collections:** {colls_detail}",
        "",
        "**Representative hadiths** (closest to cluster centroid):",
        "",
    ]
    for rh in c["representative_hadiths"]:
        grade = f" `{rh['gradeNorm']}`" if rh.get("gradeNorm") and rh["gradeNorm"] != "Uncategorized" else ""
        score_str = f"(score {rh['score']})" if rh.get("score") else ""
        lines.append(
            f"- **{rh['collection']}**{grade} {score_str}  \n"
            f"  {rh['text'][:400]}"
        )
    lines.append("")

lines += [
    "---",
    "",
    "## Clusters by size (largest first)",
    "",
    "| Rank | ID | Size | % corpus | Cohesion | Top collections |",
    "|------|----|------|----------|----------|-----------------|",
]
for rank, (cid, c) in enumerate(by_size, 1):
    colls = ", ".join(f"{k}({v})" for k, v in list(c["top_collections"].items())[:3])
    pct = 100 * c["size"] / total
    lines.append(
        f"| {rank} | {cid} | {c['size']:,} | {pct:.1f}% | {c['cohesion']} | {colls} |"
    )

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Written: {out_path}  ({len(lines)} lines)")
