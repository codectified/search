"""
Parses narrator tags from ArabicHadithTable.hadithText and joins with the Narrators table.
Produces stats on chain lengths, narrator frequency, and graph structure.

Run inside the search container:
    docker exec search-web-1 python3 /code/tests/narrator_stats.py
Copy result back:
    docker cp search-web-1:/code/narrator_stats.md "test results & reports/narrator_stats.md"
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

# ── 1. Parse narrator chains from every hadith ────────────────────────────────
print("Parsing narrator chains from ArabicHadithTable...")
cur.execute("SELECT arabicURN, collection, hadithText FROM ArabicHadithTable")

chain_lengths = []           # list of int — narrators per hadith
narrator_freq = Counter()    # narrator_id → how many hadiths they appear in
role_freq = Counter()        # role → count
hadith_narrator_map = {}     # arabicURN → [narrator_id, ...]
no_isnad = 0

for row in cur:
    text = row["hadithText"] or ""
    narrators = NARRATOR_RE.findall(text)  # [(id, role), ...]
    if not narrators:
        no_isnad += 1
        continue
    ids = [int(nid) for nid, _ in narrators]
    roles = [role for _, role in narrators]
    chain_lengths.append(len(ids))
    for nid, role in zip(ids, roles):
        narrator_freq[nid] += 1
        role_freq[role] += 1
    hadith_narrator_map[row["arabicURN"]] = ids

total_hadiths = len(chain_lengths) + no_isnad
with_isnad = len(chain_lengths)
print(f"  {total_hadiths:,} hadiths total | {with_isnad:,} have narrator tags | {no_isnad:,} no isnad")

# chain length distribution
from collections import Counter as C
chain_dist = C(chain_lengths)
avg_chain = sum(chain_lengths) / len(chain_lengths) if chain_lengths else 0

# ── 2. Load Narrators table ───────────────────────────────────────────────────
print("Loading Narrators table...")
cur.execute("""
    SELECT narrator_id, name, alt_name, kunya, reliability_label, reliability_grade,
           generation, narration_count, prominence_score,
           in_bukhari, in_muslim, teachers, students,
           num_sahih, num_hasan, num_daeef, num_mawdu
    FROM Narrators
""")
narrators = {r["narrator_id"]: r for r in cur.fetchall()}
print(f"  {len(narrators):,} narrators loaded")

# ── 3. Graph stats from teacher/student adjacency lists ───────────────────────
print("Computing graph stats...")
edges = set()
out_degree = Counter()   # narrator → num students
in_degree = Counter()    # narrator → num teachers

for nid, n in narrators.items():
    teachers_raw = (n["teachers"] or "").strip()
    students_raw = (n["students"] or "").strip()
    teachers = [int(x) for x in teachers_raw.split(",") if x.strip().isdigit()]
    students = [int(x) for x in students_raw.split(",") if x.strip().isdigit()]
    for t in teachers:
        edges.add((t, nid))
        in_degree[nid] += 1
    for s in students:
        edges.add((nid, s))
        out_degree[nid] += 1

conn.close()

# ── 4. Top narrators by frequency in hadiths ─────────────────────────────────
top_by_freq = [(narrator_freq[nid], nid) for nid in narrator_freq]
top_by_freq.sort(reverse=True)

# ── 5. Write report ───────────────────────────────────────────────────────────
out = []
out.append("# Narrator Graph — Statistics\n")

out.append("## Coverage\n")
out.append(f"| Metric | Value |")
out.append(f"|--------|-------|")
out.append(f"| Total hadiths | {total_hadiths:,} |")
out.append(f"| Hadiths with narrator tags | {with_isnad:,} ({100*with_isnad//total_hadiths}%) |")
out.append(f"| Hadiths without isnad tags | {no_isnad:,} |")
out.append(f"| Unique narrators in DB | {len(narrators):,} |")
out.append(f"| Unique narrators seen in chains | {len(narrator_freq):,} |")
out.append(f"| Graph edges (teacher→student) | {len(edges):,} |")
out.append(f"| Avg chain length | {avg_chain:.2f} narrators |")
out.append("")

out.append("## Chain Length Distribution\n")
out.append("| Chain Length | Hadiths | % |")
out.append("|---|---|---|")
for length in sorted(chain_dist):
    count = chain_dist[length]
    out.append(f"| {length} | {count:,} | {100*count//with_isnad}% |")
out.append("")

out.append("## Narrator Role Frequency\n")
out.append("| Role | Count |")
out.append("|------|-------|")
for role, count in role_freq.most_common():
    out.append(f"| {role} | {count:,} |")
out.append("")

out.append("## Top 50 Narrators by Hadith Frequency\n")
out.append("_(how many hadith chains they appear in across all collections)_\n")
out.append("| Rank | Name | Kunya | Generation | Reliability | In Bukhari | In Muslim | Hadith Appearances | Sahih | Hasan | Da'if | Mawdu | Out-degree (students) |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for rank, (freq, nid) in enumerate(top_by_freq[:50], 1):
    n = narrators.get(nid)
    if not n:
        continue
    gen = f"Gen {n['generation']}" if n["generation"] else "—"
    out.append(
        f"| {rank} | {n['name'] or '—'} | {n['kunya'] or '—'} | {gen} | "
        f"{n['reliability_label'] or '—'} | {'✓' if n['in_bukhari'] else ''} | "
        f"{'✓' if n['in_muslim'] else ''} | {freq:,} | "
        f"{n['num_sahih']} | {n['num_hasan']} | {n['num_daeef']} | {n['num_mawdu']} | "
        f"{out_degree[nid]} |"
    )
out.append("")

out.append("## Top 30 Most Connected Narrators (by student count)\n")
out.append("_(high out-degree = many students narrated from them = central node in graph)_\n")
out.append("| Name | Kunya | Generation | Reliability | Students | Teachers | Hadith Appearances | Prominence Score |")
out.append("|---|---|---|---|---|---|---|---|")
for nid, student_count in out_degree.most_common(30):
    n = narrators.get(nid)
    if not n:
        continue
    gen = f"Gen {n['generation']}" if n["generation"] else "—"
    out.append(
        f"| {n['name'] or '—'} | {n['kunya'] or '—'} | {gen} | "
        f"{n['reliability_label'] or '—'} | {student_count} | {in_degree[nid]} | "
        f"{narrator_freq.get(nid, 0):,} | {n['prominence_score'] or '—'} |"
    )
out.append("")

out.append("## Generation Distribution (Tabaqat)\n")
out.append("| Generation | Narrators | Avg Prominence |")
out.append("|---|---|---|")
gen_groups = defaultdict(list)
for n in narrators.values():
    if n["generation"]:
        gen_groups[n["generation"]].append(n["prominence_score"] or 0)
for gen in sorted(gen_groups):
    scores = gen_groups[gen]
    avg = sum(scores) / len(scores) if scores else 0
    out.append(f"| {gen} | {len(scores):,} | {avg:.1f} |")
out.append("")

out.append("## Graph Summary\n")
out.append(f"- **{len(narrators):,} nodes** (narrators)\n")
out.append(f"- **{len(edges):,} directed edges** (teacher → student relationships)\n")
avg_out = sum(out_degree.values()) / len(out_degree) if out_degree else 0
avg_in = sum(in_degree.values()) / len(in_degree) if in_degree else 0
out.append(f"- Avg out-degree (students per narrator): **{avg_out:.1f}**\n")
out.append(f"- Avg in-degree (teachers per narrator): **{avg_in:.1f}**\n")
out.append(f"- {len([n for n in narrators.values() if n['generation'] == 1]):,} Sahabah (Gen 1)\n")
out.append(f"- {len([n for n in narrators.values() if n['generation'] == 2]):,} Tabi'un (Gen 2)\n")
out.append(f"- {len([n for n in narrators.values() if n['generation'] == 3]):,} Tabi' al-Tabi'in (Gen 3)\n")

report = "\n".join(out)
with open("/code/narrator_stats.md", "w", encoding="utf-8") as f:
    f.write(report)
print(f"Written: /code/narrator_stats.md ({len(report):,} chars)")
