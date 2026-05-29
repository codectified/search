"""
Finds near-duplicate hadiths in the english-openai index (same matn, different chain).
Uses cosine similarity > 0.93 threshold on English text vectors.

Groups duplicates and writes a dupGroup integer back to every doc in each group.
Group ID = smallest englishURN in the group.

Also writes a report: /code/test results & reports/english_duplicate_groups.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/find_english_duplicates.py

Expected output: ~4,000-6,000 groups covering Muslim a/b/c/d variants,
cross-collection parallel narrations, etc.
"""
import os, json, time
import numpy as np
from sklearn.preprocessing import normalize
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, scan as es_scan

INDEX     = "english-openai"
THRESHOLD = 0.93
BATCH_SZ  = 500      # docs per kNN lookup pass
KNN_K     = 15       # neighbors to retrieve per hadith
REPORT    = "/code/test results & reports/english_duplicate_groups.md"

es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

# ── Load all vectors + metadata from index ─────────────────────────────────────
print("Loading all docs from index...")
urns, vecs, meta = [], [], {}
for hit in es_scan(es, index=INDEX,
                   query={"_source": ["englishURN", "collection", "hadithNumber",
                                      "englishText", "isChainRef", "embedding"]}):
    s  = hit["_source"]
    u  = str(hit["_id"])
    em = s.get("embedding")
    if em and not s.get("isChainRef"):   # skip chain-ref docs
        urns.append(u)
        vecs.append(em)
        meta[u] = {
            "collection":   s.get("collection", ""),
            "hadithNumber": s.get("hadithNumber", ""),
            "englishText":  (s.get("englishText") or "")[:120],
            "englishURN":   s.get("englishURN", 0),
        }

print(f"  Loaded {len(urns):,} non-chain-ref docs")

mat = normalize(np.array(vecs, dtype=np.float32), norm="l2")

# ── Find duplicate groups via Union-Find ──────────────────────────────────────
print("Computing pairwise similarities (batched dot-product)...")

parent = {u: u for u in urns}

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        # smaller URN becomes root so group ID = smallest URN
        if int(px) < int(py):
            parent[py] = px
        else:
            parent[px] = py

pairs_found = 0
t0 = time.time()

# Process in batches: each batch dot-products against the full matrix
for start in range(0, len(urns), BATCH_SZ):
    batch_mat = mat[start : start + BATCH_SZ]    # (B, 1536)
    sims      = batch_mat @ mat.T                  # (B, N)

    for bi, row in enumerate(sims):
        gi = start + bi
        # Find all docs with sim > threshold (excluding self)
        matches = np.where(row > THRESHOLD)[0]
        for mi in matches:
            if mi != gi:
                union(urns[gi], urns[mi])
                pairs_found += 1

    done = min(start + BATCH_SZ, len(urns))
    print(f"  {done:,}/{len(urns):,} | pairs found: {pairs_found:,}", end="\r")

print(f"\nTotal pairs above {THRESHOLD}: {pairs_found:,}")

# ── Build groups ───────────────────────────────────────────────────────────────
from collections import defaultdict
groups: dict[str, list[str]] = defaultdict(list)
for u in urns:
    groups[find(u)].append(u)

dup_groups = {root: members for root, members in groups.items() if len(members) > 1}
print(f"Duplicate groups (≥2 members): {len(dup_groups):,}")

# Sort each group by englishURN, assign group ID = smallest URN
final_groups = {}
for root, members in dup_groups.items():
    sorted_members = sorted(members, key=lambda u: int(u))
    group_id = int(sorted_members[0])
    final_groups[group_id] = sorted_members

# ── Write dupGroup back to ES ──────────────────────────────────────────────────
print("Writing dupGroup field to index...")
urn_to_group = {}
for gid, members in final_groups.items():
    for u in members:
        urn_to_group[u] = gid

actions = []
for urn, gid in urn_to_group.items():
    actions.append({
        "_op_type": "update",
        "_id": urn,
        "doc": {"dupGroup": gid},
    })

for i in range(0, len(actions), 500):
    bulk(es, actions[i:i+500], index=INDEX,
         request_timeout=60, raise_on_error=False, raise_on_exception=False)
    print(f"  Updated {min(i+500, len(actions)):,}/{len(actions):,}", end="\r")

es.indices.refresh(index=INDEX)
print(f"\nWrote dupGroup to {len(urn_to_group):,} docs")

# ── Build report ───────────────────────────────────────────────────────────────
print("Building report...")

# Sort groups by size descending
sorted_groups = sorted(final_groups.items(), key=lambda x: -len(x[1]))

lines = [
    "# English Vector Duplicate Groups\n",
    f"Index: `{INDEX}` | Threshold: {THRESHOLD} | k={KNN_K}\n",
    f"Total groups: {len(final_groups):,} | Total hadiths in groups: {len(urn_to_group):,}\n",
    "\n## Group size distribution\n",
]

from collections import Counter
size_dist = Counter(len(m) for m in final_groups.values())
for sz in sorted(size_dist):
    lines.append(f"- {sz} members: {size_dist[sz]:,} groups")

lines.append(f"\n\n## Top 30 largest groups\n")
for gid, members in sorted_groups[:30]:
    size = len(members)
    lines.append(f"\n### Group {gid} — {size} hadiths\n")
    lines.append("| URN | Collection | Hadith# | Text (truncated) |")
    lines.append("|---|---|---|---|")
    for u in members:
        m = meta.get(u, {})
        text = m.get("englishText", "").replace("|", "｜")
        lines.append(f"| {u} | {m.get('collection','?')} | {m.get('hadithNumber','')} | {text} |")

os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

elapsed = time.time() - t0
print(f"Report written: {REPORT}")
print(f"\nTotal time: {elapsed/60:.1f}m")
print(f"Groups: {len(final_groups):,} | Hadiths in groups: {len(urn_to_group):,}")
print(f"\nSize distribution:")
for sz in sorted(size_dist):
    print(f"  {sz} members: {size_dist[sz]:,} groups")
