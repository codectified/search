"""
Focused side-by-side comparison for the two priority queries:
  - "aisha"
  - "comparing yourself to others"

Tests all three semantic models:
  - arabic-openai  (Arabic vectors, translated-only centroids k=75, exists:englishText filter)
  - english-openai (English vectors, full HNSW, chain-ref + dedup)
  - mxbai          (English vectors, full HNSW, chain-ref + dedup)

Writes: /code/test results & reports/focused_comparison.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/focused_comparison.py
"""
import urllib.request, urllib.parse, json, re, time, os

BASE   = "http://localhost:5000"
REPORT = "/code/test results & reports/focused_comparison.md"

QUERIES = ["aisha", "comparing yourself to others"]
MODELS  = ["arabic-openai", "english-openai", "mxbai"]
SIZE    = 10


def strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


def search(model, query, size=SIZE):
    url = (BASE + "/en/search?q=" + urllib.parse.quote(query)
           + "&model=" + model + "&mode=semantic&size=" + str(size))
    t0 = time.perf_counter()
    with urllib.request.urlopen(url, timeout=45) as r:
        body = json.loads(r.read())
    wall_ms = round((time.perf_counter() - t0) * 1000)
    return body, wall_ms


# ── Collect results ────────────────────────────────────────────────────────────
all_results = {}
for q in QUERIES:
    all_results[q] = {}
    for model in MODELS:
        try:
            body, wall_ms = search(model, q)
            hits = body.get("hits", {}).get("hits", [])
            meta = body.get("_meta", {})
            all_results[q][model] = {"hits": hits, "wall_ms": wall_ms, "meta": meta, "error": None}
        except Exception as e:
            all_results[q][model] = {"hits": [], "wall_ms": 0, "meta": {}, "error": str(e)}
            print(f"  ERROR [{model}] {q}: {e}")


def hit_key(h):
    s = h["_source"]
    return (s.get("collection", ""), str(s.get("hadithNumber", "")))


def fmt_hit(h, rank, mark=""):
    s = h["_source"]
    text = strip_html(s.get("hadithText") or s.get("englishText", ""))[:120]
    return f"| {rank}{mark} | {h['_score']:.3f} | `{s.get('collection','')} {s.get('hadithNumber','')}` | {text} |"


# ── Build report ───────────────────────────────────────────────────────────────
lines = []
W = lines.append

W("# Focused Comparison: \"aisha\" and \"comparing yourself to others\"\n")
W("Three semantic models tested head-to-head.\n")
W("| Model | Corpus | Pre-filter | Notes |")
W("|---|---|---|---|")
W("| arabic-openai | Arabic matn vectors | Centroid k=75 (translated-only, 44,896 docs) + `exists:englishText` | Cross-lingual; designed for Arabic queries |")
W("| english-openai | English text vectors | Full HNSW (48,703 docs) | text-embedding-3-small, 1536-dim |")
W("| mxbai | English text vectors | Full HNSW (48,703 docs) | mxbai-embed-large, 1024-dim, local/free |")
W("\n---\n")

for q in QUERIES:
    W(f"## Query: *\"{q}\"*\n")

    res = all_results[q]

    # Collect all hit keys per model for overlap analysis
    keys_by_model = {}
    for m in MODELS:
        keys_by_model[m] = [hit_key(h) for h in res[m]["hits"]]

    # Pairwise overlaps
    pairs = []
    for i, m1 in enumerate(MODELS):
        for m2 in MODELS[i+1:]:
            overlap = len(set(keys_by_model[m1]) & set(keys_by_model[m2]))
            pairs.append(f"{m1.split('-')[0]} ∩ {m2.split('-')[0]} = {overlap}")
    W("**Overlaps:** " + " | ".join(pairs) + "\n")

    for model in MODELS:
        r = res[model]
        meta = r["meta"]
        hits = r["hits"]

        clusters_str = f"clusters={meta['clusters']}" if meta.get("clusters") else "full-index"
        embed_str    = f"embed={meta.get('embed_ms','?')}ms" if meta.get("embed_ms") else ""
        info = " | ".join(filter(None, [f"wall={r['wall_ms']}ms", embed_str, clusters_str]))

        W(f"### {model} ({info})\n")

        if r["error"]:
            W(f"> ERROR: {r['error']}\n")
            continue

        # Mark hadiths shared with at least one other model
        all_other_keys = set()
        for m2 in MODELS:
            if m2 != model:
                all_other_keys.update(keys_by_model[m2])

        W("| # | Score | Hadith | Text |")
        W("|---|---|---|---|")
        for i, h in enumerate(hits, 1):
            shared = " ✓" if hit_key(h) in all_other_keys else ""
            W(fmt_hit(h, i, shared))
        W("")

    W("---\n")

W("## Summary\n")
W("| Query | Model | Top score | Top result | Clusters/Filter |")
W("|---|---|---|---|---|")
for q in QUERIES:
    for model in MODELS:
        r = all_results[q][model]
        hits = r["hits"]
        meta = r["meta"]
        if hits:
            s = hits[0]["_source"]
            top_text = strip_html(s.get("hadithText") or s.get("englishText",""))[:70]
            top_ref  = f"{s.get('collection','')} {s.get('hadithNumber','')}"
        else:
            top_text, top_ref = "—", "—"
        top_score = f"{hits[0]['_score']:.3f}" if hits else "—"
        clusters  = str(meta.get("clusters", "full-HNSW"))
        W(f"| {q} | {model} | {top_score} | `{top_ref}` — {top_text} | {clusters} |")

W("")
os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report written: {REPORT}")
print()
for q in QUERIES:
    print(f"=== {q} ===")
    for model in MODELS:
        r = all_results[q][model]
        hits = r["hits"]
        meta = r["meta"]
        print(f"  [{model}] clusters={meta.get('clusters','full-HNSW')} wall={r['wall_ms']}ms")
        for i, h in enumerate(hits[:5], 1):
            s = h["_source"]
            text = strip_html(s.get("hadithText") or s.get("englishText",""))[:90]
            print(f"    {i}. [{h['_score']:.3f}] {s.get('collection','')} {s.get('hadithNumber','')} — {text}")
    print()
