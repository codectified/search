"""
Ego-network analysis of the narrator graph.
For the top hubs, shows their immediate teachers and students with full stats.
Also computes approximate betweenness (in_degree × out_degree) to find
bridge/bottleneck narrators.

Run inside the search container:
    docker exec search-web-1 python3 /code/tests/narrator_hub_analysis.py
Copy result back:
    docker cp search-web-1:/code/narrator_hub_analysis.md "test results & reports/narrator_hub_analysis.md"
"""
import os, re, json
from collections import defaultdict, Counter
import pymysql

conn = pymysql.connect(
    host=os.environ["MYSQL_HOST"], user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"], database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
)
cur = conn.cursor(pymysql.cursors.DictCursor)

NARRATOR_RE = re.compile(r'\[narrator id="(\d+)" role="([^"]+)"')

# ── Load narrators ────────────────────────────────────────────────────────────
print("Loading narrators...")
cur.execute("""
    SELECT narrator_id, name, alt_name, kunya, reliability_label, reliability_grade,
           generation, narration_count, prominence_score,
           in_bukhari, in_muslim, teachers, students,
           num_sahih, num_hasan, num_daeef, num_mawdu, death_year
    FROM Narrators
""")
narrators = {r["narrator_id"]: r for r in cur.fetchall()}

# ── Build adjacency from teacher/student lists ────────────────────────────────
print("Building graph...")
out_neighbors = defaultdict(set)   # nid → set of student IDs
in_neighbors  = defaultdict(set)   # nid → set of teacher IDs

for nid, n in narrators.items():
    for sid in (n["students"] or "").split(","):
        sid = sid.strip()
        if sid.isdigit():
            out_neighbors[nid].add(int(sid))
            in_neighbors[int(sid)].add(nid)
    for tid in (n["teachers"] or "").split(","):
        tid = tid.strip()
        if tid.isdigit():
            in_neighbors[nid].add(int(tid))
            out_neighbors[int(tid)].add(nid)

out_degree = {nid: len(s) for nid, s in out_neighbors.items()}
in_degree  = {nid: len(t) for nid, t in in_neighbors.items()}

# ── Parse narrator frequency from hadith chains ───────────────────────────────
print("Parsing hadith chains...")
cur.execute("SELECT arabicURN, collection, hadithText FROM ArabicHadithTable")
narrator_freq = Counter()
collection_freq = defaultdict(Counter)  # nid → {collection: count}

for row in cur:
    hits = NARRATOR_RE.findall(row["hadithText"] or "")
    for nid_str, role in hits:
        nid = int(nid_str)
        narrator_freq[nid] += 1
        collection_freq[nid][row["collection"]] += 1

conn.close()

# ── Hub metrics ───────────────────────────────────────────────────────────────
def fmt_name(n):
    name = n["name"] or "Unknown"
    kunya = f" ({n['kunya']})" if n["kunya"] else ""
    return f"{name}{kunya}"

def hub_row(nid):
    n = narrators.get(nid, {})
    if not n:
        return None
    return {
        "id": nid,
        "name": fmt_name(n),
        "generation": n.get("generation") or "?",
        "reliability": n.get("reliability_label") or "—",
        "death_year": n.get("death_year") or "—",
        "in_bukhari": bool(n.get("in_bukhari")),
        "in_muslim": bool(n.get("in_muslim")),
        "hadith_appearances": narrator_freq.get(nid, 0),
        "out_degree": out_degree.get(nid, 0),
        "in_degree": in_degree.get(nid, 0),
        "prominence": n.get("prominence_score") or 0,
        "num_sahih": n.get("num_sahih") or 0,
        "num_hasan": n.get("num_hasan") or 0,
        "num_daeef": n.get("num_daeef") or 0,
        "top_collections": dict(collection_freq[nid].most_common(4)),
    }

# ── Approximate betweenness: in_degree × out_degree ─────────────────────────
# Narrators with many teachers AND many students are bridges between generations.
bridgeness = {nid: in_degree.get(nid, 0) * out_degree.get(nid, 0)
              for nid in narrators if in_degree.get(nid, 0) > 0 and out_degree.get(nid, 0) > 0}
top_bridges = sorted(bridgeness, key=bridgeness.get, reverse=True)[:30]

# Top hubs by out-degree (most students)
top_by_students = sorted(out_degree, key=out_degree.get, reverse=True)[:10]
# Top hubs by hadith appearances
top_by_freq = [nid for freq, nid in sorted(((v,k) for k,v in narrator_freq.items()), reverse=True)[:10]]

# ── Write report ──────────────────────────────────────────────────────────────
out = []
out.append("# Narrator Hub Analysis — Ego Networks\n")
out.append("Examining the most central narrators in the isnad graph and their immediate networks.\n")
out.append("**Bridgeness** = in_degree × out_degree — narrators who connect many teachers to many students.\n\n---\n")

# Summary comparison table
out.append("## Top 15 Hubs — Multi-Metric Comparison\n")
out.append("| Rank | Name | Gen | Death | Reliability | Appearances | Students | Teachers | Bridgeness | Sahih | Hasan | Da'if |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
all_nids_ranked = sorted(narrator_freq, key=narrator_freq.get, reverse=True)[:15]
for rank, nid in enumerate(all_nids_ranked, 1):
    h = hub_row(nid)
    if not h: continue
    bridge = bridgeness.get(nid, 0)
    out.append(
        f"| {rank} | {h['name']} | {h['generation']} | {h['death_year']} AH | "
        f"{h['reliability'][:30] if h['reliability'] else '—'} | "
        f"{h['hadith_appearances']:,} | {h['out_degree']} | {h['in_degree']} | "
        f"{bridge:,} | {h['num_sahih']} | {h['num_hasan']} | {h['num_daeef']} |"
    )
out.append("\n---\n")

# Top bridges
out.append("## Top 20 Bridge Narrators (in_degree × out_degree)\n")
out.append("These narrators sit between the most teachers and the most students — removing them would fragment the graph.\n")
out.append("| Rank | Name | Gen | Death | Teachers | Students | Bridgeness | Reliability |")
out.append("|---|---|---|---|---|---|---|---|")
for rank, nid in enumerate(top_bridges[:20], 1):
    h = hub_row(nid)
    if not h: continue
    out.append(
        f"| {rank} | {h['name']} | {h['generation']} | {h['death_year']} AH | "
        f"{h['in_degree']} | {h['out_degree']} | {bridgeness[nid]:,} | {h['reliability'][:35] if h['reliability'] else '—'} |"
    )
out.append("\n---\n")

# Ego networks for top 8 hubs
out.append("## Ego Networks — Top 8 Hubs\n")
out.append("For each hub: who they learned from (teachers) and who narrated from them (students), with key stats.\n")

for nid in all_nids_ranked[:8]:
    h = hub_row(nid)
    if not h: continue
    n = narrators[nid]
    colls = ", ".join(f"{c}({cnt})" for c, cnt in h["top_collections"].items())

    out.append(f"### {h['name']}")
    out.append(f"**Generation:** {h['generation']} | **Died:** {h['death_year']} AH | "
               f"**Reliability:** {h['reliability']} | **Prominence:** {h['prominence']:.1f}")
    out.append(f"**Hadith appearances:** {h['hadith_appearances']:,} | "
               f"**Students:** {h['out_degree']} | **Teachers:** {h['in_degree']}")
    out.append(f"**Grade breakdown:** Sahih {h['num_sahih']} / Hasan {h['num_hasan']} / "
               f"Da'if {h['num_daeef']} / Mawdu {narrators[nid].get('num_mawdu', 0)}")
    out.append(f"**Top collections:** {colls}\n")

    # Teachers (in-neighbors)
    teacher_ids = list(in_neighbors.get(nid, []))
    teacher_details = [(narrator_freq.get(t, 0), t) for t in teacher_ids if t in narrators]
    teacher_details.sort(reverse=True)
    out.append(f"**Teachers ({len(teacher_ids)} total) — top 10 by hadith appearances:**\n")
    out.append("| Name | Gen | Reliability | Appearances | Students |")
    out.append("|---|---|---|---|---|")
    for freq, tid in teacher_details[:10]:
        tn = narrators[tid]
        out.append(f"| {fmt_name(tn)} | {tn['generation'] or '?'} | "
                   f"{(tn['reliability_label'] or '—')[:30]} | {freq:,} | {out_degree.get(tid, 0)} |")
    out.append("")

    # Students (out-neighbors)
    student_ids = list(out_neighbors.get(nid, []))
    student_details = [(narrator_freq.get(s, 0), s) for s in student_ids if s in narrators]
    student_details.sort(reverse=True)
    out.append(f"**Students ({len(student_ids)} total) — top 10 by hadith appearances:**\n")
    out.append("| Name | Gen | Reliability | Appearances | Students |")
    out.append("|---|---|---|---|---|")
    for freq, sid in student_details[:10]:
        sn = narrators[sid]
        out.append(f"| {fmt_name(sn)} | {sn['generation'] or '?'} | "
                   f"{(sn['reliability_label'] or '—')[:30]} | {freq:,} | {out_degree.get(sid, 0)} |")
    out.append("\n---\n")

# Generation-level flow
out.append("## Knowledge Flow by Generation\n")
out.append("Avg hadith appearances and graph degree per generation (tabaqat).\n")
out.append("| Generation | Narrators | Avg Appearances | Avg Students | Avg Teachers | Top Name |")
out.append("|---|---|---|---|---|---|")
gen_data = defaultdict(list)
for nid, n in narrators.items():
    g = n.get("generation")
    if g:
        gen_data[g].append(nid)
for g in sorted(gen_data)[:20]:
    nids = gen_data[g]
    avg_app = sum(narrator_freq.get(nid, 0) for nid in nids) / len(nids)
    avg_out = sum(out_degree.get(nid, 0) for nid in nids) / len(nids)
    avg_in  = sum(in_degree.get(nid, 0)  for nid in nids) / len(nids)
    top_nid = max(nids, key=lambda x: narrator_freq.get(x, 0))
    top_name = narrators[top_nid]["name"] or "?"
    out.append(f"| {g} | {len(nids):,} | {avg_app:.1f} | {avg_out:.1f} | {avg_in:.1f} | {top_name} |")

report = "\n".join(out)
with open("/code/narrator_hub_analysis.md", "w", encoding="utf-8") as f:
    f.write(report)
print(f"Written: /code/narrator_hub_analysis.md ({len(report):,} chars)")
