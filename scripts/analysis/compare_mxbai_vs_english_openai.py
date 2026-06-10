"""
Side-by-side comparison of mxbai (local Ollama, 1024-dim) vs
english-openai (OpenAI text-embedding-3-small, 1536-dim, centroid pre-filter).

Both models use English text, chain-ref filter, and dedup by default.

Writes: /code/test results & reports/mxbai_vs_english_openai.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/compare_mxbai_vs_english_openai.py
"""
import urllib.request, urllib.parse, json, re, time, os

BASE   = "http://localhost:5000"
REPORT = "/code/test results & reports/mxbai_vs_english_openai.md"

QUERIES = [
    "comparing yourself to others",
    "forgiveness of sins",
    "visiting the sick",
    "honoring one's parents",
    "fasting in Ramadan",
    "prayer before sleeping",
    "giving charity",
    "patience during hardship",
    "rights of a neighbour",
    "seeking knowledge",
]

MODELS = ["mxbai", "english-openai"]
SIZE   = 10


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
            all_results[q][model] = {
                "hits": hits, "wall_ms": wall_ms, "meta": meta, "error": None
            }
        except Exception as e:
            all_results[q][model] = {"hits": [], "wall_ms": 0, "meta": {}, "error": str(e)}


# ── Build report ───────────────────────────────────────────────────────────────
lines = []
W = lines.append

W("# mxbai vs english-openai: Side-by-Side Comparison\n")
W(f"Queries: {len(QUERIES)} | size={SIZE} | chain-ref filter=ON | dedup=ON\n")
W("| Model | Corpus | Dim | Pre-filter |\n|---|---|---|---|")
W("| mxbai | English text (Ollama mxbai-embed-large) | 1024 | Full HNSW (48k) |")
W("| english-openai | English text (OpenAI text-embedding-3-small) | 1536 | Full HNSW (48k) — centroid pre-filter removed: hurt recall at this corpus size |")
W("\n---\n")

for q in QUERIES:
    W(f"## Query: *\"{q}\"*\n")

    res = all_results[q]
    mxbai_hits  = res["mxbai"]["hits"]
    openai_hits = res["english-openai"]["hits"]

    mxbai_keys  = [(h["_source"].get("collection",""), str(h["_source"].get("hadithNumber",""))) for h in mxbai_hits]
    openai_keys = [(h["_source"].get("collection",""), str(h["_source"].get("hadithNumber",""))) for h in openai_hits]
    overlap     = set(mxbai_keys) & set(openai_keys)

    mxbai_meta  = res["mxbai"]["meta"]
    openai_meta = res["english-openai"]["meta"]

    W(f"**Overlap:** {len(overlap)}/{SIZE} results in common "
      f"| mxbai: {res['mxbai']['wall_ms']}ms "
      f"| english-openai: {res['english-openai']['wall_ms']}ms "
      f"(embed {openai_meta.get('embed_ms','?')}ms, clusters={openai_meta.get('clusters','?')})\n")

    W("| # | mxbai score | mxbai result | openai score | openai result |")
    W("|---|---|---|---|---|")
    for i in range(SIZE):
        if i < len(mxbai_hits):
            mh = mxbai_hits[i]
            ms = mh["_source"]
            m_text = strip_html(ms.get("hadithText",""))[:90]
            m_cell = f"`{ms.get('collection','')} {ms.get('hadithNumber','')}` {m_text}"
        else:
            m_cell = "—"
        if i < len(openai_hits):
            oh = openai_hits[i]
            os_ = oh["_source"]
            o_text = strip_html(os_.get("englishText",""))[:90]
            o_cell = f"`{os_.get('collection','')} {os_.get('hadithNumber','')}` {o_text}"
        else:
            o_cell = "—"
        m_score = f"{mxbai_hits[i]['_score']:.3f}" if i < len(mxbai_hits) else "—"
        o_score = f"{openai_hits[i]['_score']:.3f}" if i < len(openai_hits) else "—"
        shared = " ✓" if i < len(mxbai_keys) and mxbai_keys[i] in set(openai_keys) else ""
        W(f"| {i+1}{shared} | {m_score} | {m_cell} | {o_score} | {o_cell} |")
    W("")

W("---\n")
W("## Summary\n")
W("| Query | mxbai top score | openai top score | Overlap |")
W("|---|---|---|---|")
for q in QUERIES:
    res = all_results[q]
    mh  = res["mxbai"]["hits"]
    oh  = res["english-openai"]["hits"]
    m_top = f"{mh[0]['_score']:.3f}" if mh else "—"
    o_top = f"{oh[0]['_score']:.3f}" if oh else "—"
    mk  = set((h["_source"].get("collection",""), str(h["_source"].get("hadithNumber",""))) for h in mh)
    ok  = set((h["_source"].get("collection",""), str(h["_source"].get("hadithNumber",""))) for h in oh)
    overlap = len(mk & ok)
    W(f"| {q} | {m_top} | {o_top} | {overlap}/{SIZE} |")

W("")
os.makedirs(os.path.dirname(REPORT), exist_ok=True)
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report written: {REPORT}")
print("Summary:")
for q in QUERIES:
    res = all_results[q]
    mh  = res["mxbai"]["hits"]
    oh  = res["english-openai"]["hits"]
    m_top = f"{mh[0]['_score']:.3f}" if mh else "err"
    o_top = f"{oh[0]['_score']:.3f}" if oh else "err"
    mk  = set((h["_source"].get("collection",""), str(h["_source"].get("hadithNumber",""))) for h in mh)
    ok_ = set((h["_source"].get("collection",""), str(h["_source"].get("hadithNumber",""))) for h in oh)
    print(f"  {q[:40]:40s} mxbai={m_top} openai={o_top} overlap={len(mk&ok_)}")
