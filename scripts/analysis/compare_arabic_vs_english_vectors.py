"""
Compares Arabic matn vectors vs English text vectors on the same corpus.

arabic-openai (Arabic matn embedded, English-filtered)
  — straight kNN filtered to hadiths with English translations only
  — Arabic text was embedded (matn-only where tagged/regex-extracted)
  — same OpenAI text-embedding-3-small model as openai-small-en

Baselines from existing report (lexical vs hybrid vs semantic/report1.md):
  — mxbai:          English text embedded, 48k English docs, score range 0.78-0.81
  — openai-small-en: English text embedded, 48k English docs, score range 0.67-0.69

Key question: Does clean Arabic matn give stronger semantic signal than English text
for the same query, given that we removed isnad noise from the vectors?

Run inside container:
    docker exec search-web-1 python3 /code/tests/compare_arabic_vs_english_vectors.py

Output: /code/test results & reports/arabic_vs_english_vectors.md
"""
import json, os, re, time
import numpy as np
from openai import OpenAI
from elasticsearch import Elasticsearch
from sklearn.preprocessing import normalize

# ── Config ────────────────────────────────────────────────────────────────────

OPENAI_MODEL   = "text-embedding-3-small"
ARABIC_INDEX   = "arabic-openai"
TOP_K          = 20
MAX_TEXT       = 350

# Filter: only hadiths that have an English translation
ENGLISH_FILTER = {"range": {"englishURN": {"gt": 0}}}

QUERIES = [
    "prayer times",
    "comparing yourself to others",
    "zakah on wealth",
    "treatment of parents",
    "aisha",
]

# ── Hardcoded baselines from report1.md (2026-05-20) ──────────────────────────
# For "comparing yourself to others" only — the one query tested in the old report.
# Scores are pure semantic (no lexical boost).

MXBAI_BASELINE = [
    (0.8147, "forty 18",           "✅", "The felicitous person takes lessons from (the actions of) others."),
    (0.8022, "bukhari 6490",       "✅", "Allah's Apostle said, 'If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him.'"),
    (0.7969, "forty 3",            "〰",  "A Muslim is a mirror of the Muslim."),
    (0.7940, "muslim 2963a",       "✅", "When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you."),
    (0.7920, "ibnmajah 4336",      "〰",  "Lengthy hadith about the marketplace of Paradise; passages on people of different status meeting without inferiority."),
    (0.7897, "adab 159",           "〰",  "Abu'd-Darda' said: We know you better than the veterinarian knows his animals. The best is the one whose good is hoped for and whose evil you are safe from."),
    (0.7864, "riyadussalihin 466", "✅", "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you."),
    (0.7854, "muslim 2536",        "〰",  "'A'isha reported: The Prophet said the best people are of the generation to which I belong, then the second, then the third."),
    (0.7821, "tirmidhi 2513",      "✅", "Look to one who is lower than you, and do not look to one who is above you. For that is more worthy that you not belittle Allah's favors."),
    (0.7821, "abudawud 4092",      "〰",  "A man said: I like beauty and do not like that anyone excels me. Is it pride? The Prophet replied: No, pride is disdaining what is true and despising people."),
]

OPENAI_EN_BASELINE = [
    (0.6896, "adab 328",           "✅", "Ibn 'Abbas said: When you want to mention your companion's faults, remember your own faults."),
    (0.6896, "bukhari 6490",       "✅", "Allah's Apostle said: If anyone of you looked at a person who was made superior to him in property and appearance, then he should also look at the one who is inferior to him."),
    (0.6851, "riyadussalihin 466", "✅", "Look at those who are inferior to you and do not look at those who are superior to you."),
    (0.6775, "ahmad 111",          "〰",  "'Umar: I am afraid that if you tell them stories you will think you are better than them, until you imagine you are as far above them as the Pleiades."),
    (0.6753, "forty 18",           "✅", "The felicitous person takes lessons from (the actions of) others."),
    (0.6708, "muslim 2963c",       "✅", "Look at those who stand at a lower level than you but don't look at those who stand at a higher level, for that is better-suited that you do not disparage Allah's favors."),
    (0.6669, "adab 592",           "✅", "Abu Hurayra said: One of you looks at the mote in his brother's eye while forgetting the stump in his own eye."),
]

# ── Clients ───────────────────────────────────────────────────────────────────

openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
es = Elasticsearch(
    "http://elasticsearch:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
)

# ── Helpers ───────────────────────────────────────────────────────────────────

def embed(query):
    resp = openai_client.embeddings.create(model=OPENAI_MODEL, input=query)
    vec = np.array(resp.data[0].embedding, dtype=np.float32)
    return vec / np.linalg.norm(vec)


def knn_search(qvec, extra_filter=None, k=TOP_K):
    filters = [ENGLISH_FILTER]
    if extra_filter:
        filters.append(extra_filter)
    knn_filter = {"bool": {"must": filters}} if len(filters) > 1 else filters[0]

    t0 = time.perf_counter()
    resp = es.search(
        index=ARABIC_INDEX,
        knn={
            "field": "embedding",
            "query_vector": qvec.tolist(),
            "k": k,
            "num_candidates": min(k * 30, 2000),
            "filter": knn_filter,
        },
        size=k,
        _source={"excludes": ["embedding", "arabicText"]},
    )
    ms = round((time.perf_counter() - t0) * 1000)
    return resp["hits"]["hits"], ms


def clean_text(raw):
    if not raw:
        return ""
    t = re.sub(r"<[^>]+>", " ", raw)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:MAX_TEXT]


def hadith_display(src):
    eng = clean_text(src.get("englishText") or "")
    if eng:
        return eng, "en"
    ar = clean_text(src.get("arabicMatn") or src.get("arabicText") or "")
    return ar, "ar"


# ── Per-query run ──────────────────────────────────────────────────────────────

def run_query(query):
    print(f"  Embedding ...", end=" ", flush=True)
    t0 = time.perf_counter()
    qvec = embed(query)
    embed_ms = round((time.perf_counter() - t0) * 1000)
    print(f"{embed_ms}ms", end="  kNN ...", flush=True)

    hits, knn_ms = knn_search(qvec)
    print(f"{knn_ms}ms  ({len(hits)} results)")

    return {
        "query":    query,
        "embed_ms": embed_ms,
        "knn_ms":   knn_ms,
        "hits":     hits,
    }


# ── Report builder ─────────────────────────────────────────────────────────────

def fmt_score(s):
    return f"{s:.4f}"


def result_block(hits, show_vector_type=True):
    lines = []
    lines.append("| # | Score | Collection | Hadith | Cluster | Matn tag | Text |")
    lines.append("|---|---|---|---|---|---|---|")
    for i, h in enumerate(hits, 1):
        s     = h["_source"]
        score = fmt_score(h["_score"])
        coll  = s.get("collection", "?")
        num   = s.get("hadithNumber") or ""
        clust = s.get("clusterIdFinal", "?")
        matn  = "✓ clean" if s.get("hadMatnTag") else "~ regex"
        text, lang = hadith_display(s)
        text  = text.replace("|", "｜")
        lang_note = f" `[{lang}]`" if lang == "ar" else ""
        lines.append(f"| {i} | {score} | {coll} | {num} | C{clust} | {matn} | {text}{lang_note} |")
    return "\n".join(lines)


def baseline_block(rows, model_label):
    lines = []
    lines.append(f"*Source: lexical vs hybrid vs semantic/report1.md — {model_label} semantic (pure vector, no lexical boost)*\n")
    lines.append("| # | Score | Hadith | Relevance | Text |")
    lines.append("|---|---|---|---|---|")
    for i, (score, ref, rel, text) in enumerate(rows, 1):
        lines.append(f"| {i} | {fmt_score(score)} | {ref} | {rel} | {text[:200].replace('|','｜')} |")
    return "\n".join(lines)


def build_report(all_results):
    lines = [
        "# Arabic Matn Vectors vs English Text Vectors\n",
        f"**Model:** OpenAI `{OPENAI_MODEL}` (same for all)\n",
        "**arabic-openai:** Arabic matn embedded (clean matn where ✓, regex-extracted where ~) · filtered to ~44.9k bilingual hadiths\n",
        "**mxbai baseline:** English text embedded · ~48k English hadiths · mxbai-embed-large · scores 0.78–0.81\n",
        "**openai-small-en baseline:** English text embedded · ~48k English hadiths · same model · scores 0.67–0.69\n",
        "\n> Baseline data from `lexical vs hybrid vs semantic/report1.md` (2026-05-20, query: comparing yourself to others)\n",
    ]

    # Summary
    lines.append("\n## Summary\n")
    lines.append("| Query | Embed ms | kNN ms | Top score | Score range |")
    lines.append("|---|---|---|---|---|")
    for r in all_results:
        top = r["hits"][0]["_score"] if r["hits"] else 0
        bot = r["hits"][-1]["_score"] if r["hits"] else 0
        lines.append(
            f"| {r['query']} | {r['embed_ms']} | {r['knn_ms']} "
            f"| {fmt_score(top)} | {fmt_score(bot)}–{fmt_score(top)} |"
        )

    # Per-query detail
    for r in all_results:
        lines.append(f"\n---\n\n## \"{r['query']}\"\n")
        lines.append(
            f"Embed: **{r['embed_ms']}ms** · kNN (English-filtered, {TOP_K} results): **{r['knn_ms']}ms**\n"
        )

        lines.append("### arabic-openai — Arabic matn vectors (English-only hadiths)\n")
        lines.append(result_block(r["hits"]))

        if r["query"] == "comparing yourself to others":
            lines.append("\n### mxbai baseline — English vectors (top 10)\n")
            lines.append(baseline_block(MXBAI_BASELINE, "mxbai-embed-large"))
            lines.append("\n### openai-small-en baseline — English vectors (top 7)\n")
            lines.append(baseline_block(OPENAI_EN_BASELINE, "openai text-embedding-3-small, English corpus"))

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    OUT = "/code/test results & reports/arabic_vs_english_vectors.md"
    all_results = []
    for q in QUERIES:
        print(f"\nQuery: '{q}'")
        all_results.append(run_query(q))

    print("\nBuilding report...")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(build_report(all_results))
    print(f"Written: {OUT}")
