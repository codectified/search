"""
Index inventory report — documents every ES index with:
  - doc count, disk size
  - all fields and their types
  - what text is embedded / which vector field
  - cluster fields present
  - grade fields present
  - which Flask search paths use this index
  - consolidation notes

Output: /code/test results & reports/analysis/index_inventory.md

Run inside container:
    docker exec search-web-1 python3 /code/tests/index_inventory.py
"""
import os, time
from elasticsearch import Elasticsearch

es = Elasticsearch("http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=120)

OUT = "/code/test results & reports/analysis/index_inventory.md"

INDEXES = [
    "english-mxbai",
    "english-openai",
    "english-openai-large",
    "arabic-openai",
    "arabic-openai-large",
    "multilingual-e5",
]

# Human-readable notes about each index
NOTES = {
    "english-mxbai": {
        "purpose": "English semantic search via ES native `semantic_text` (mxbai-embed-large inference endpoint)",
        "embedded": "`englishMatn` (isnad-stripped English matn) — embedded automatically by ES inference",
        "search_field": "`semantic_text` (ES kNN semantic search) or `hadithText` (BM25 lexical fallback)",
        "lang": "English only (48,703 hadiths)",
        "cluster": "None",
        "consolidation": "Only index with ES-native inference; cannot bulk-update without re-triggering inference. Has `hadithText` for BM25 so doubles as the lexical baseline index.",
    },
    "english-openai": {
        "purpose": "English semantic search via OpenAI `text-embedding-3-small` (1536-dim)",
        "embedded": "`englishMatn` (isnad-stripped clean matn)",
        "search_field": "`embedding` (kNN HNSW), centroid pre-filter",
        "lang": "English only (48,703 hadiths)",
        "cluster": "`clusterIdFinal` (75 clusters, centroid method)",
        "consolidation": "Has gradeNorm, dupGroup, isChainRef. Most complete English index. Missing arabicMatn (looked up from arabic-openai at query time).",
    },
    "english-openai-large": {
        "purpose": "English semantic search via OpenAI `text-embedding-3-large` (3072-dim)",
        "embedded": "`englishMatn` (isnad-stripped)",
        "search_field": "`embedding` (kNN HNSW), centroid pre-filter",
        "lang": "English only (48,703 hadiths)",
        "cluster": "`clusterIdLarge` (cluster count TBD)",
        "consolidation": "Sparse: missing gradeNorm, arabicText, englishText. Mainly a quality benchmark vs english-openai.",
    },
    "arabic-openai": {
        "purpose": "Arabic + translated-English semantic search via OpenAI `text-embedding-3-small` (1536-dim)",
        "embedded": "`arabicMatn` (Arabic matn) with English translation used for query embedding",
        "search_field": "`embedding` (kNN HNSW), centroid pre-filter",
        "lang": "All languages (131,728 docs: Arabic + English + translated)",
        "cluster": "`clusterIdFinal` (148 clusters, all docs); `clusterIdTranslated` (75 clusters, translated subset)",
        "consolidation": "Richest index: arabicMatn, arabicText, englishText, gradeNorm, both cluster fields. Central store for Arabic text lookup.",
    },
    "arabic-openai-large": {
        "purpose": "Arabic semantic search via OpenAI `text-embedding-3-large` (3072-dim)",
        "embedded": "`arabicMatn`",
        "search_field": "`embedding` (kNN HNSW), centroid pre-filter",
        "lang": "All languages (131,728 docs)",
        "cluster": "`clusterIdLarge` (clustering in progress)",
        "consolidation": "Quality benchmark vs arabic-openai. Missing gradeNorm, dupGroup. Expensive (5.8GB).",
    },
    "multilingual-e5": {
        "purpose": "Multilingual semantic search via `intfloat/multilingual-e5-large` (1024-dim)",
        "embedded": "`englishMatn` + `arabicMatn` (instruction-prefixed, shared embedding space)",
        "search_field": "`embedding` (kNN HNSW), centroid pre-filter",
        "lang": "Shared EN+AR space (129,216 docs, indexing ~85% complete)",
        "cluster": "`clusterIdShared` (75 clusters across EN+AR)",
        "consolidation": "Only index embedding both languages in the same space. Has englishMatn + arabicMatn. Missing gradeNorm, dupGroup.",
    },
}

lines = []
W = lines.append

W("# ES Index Inventory")
W("")
W(f"*Generated {time.strftime('%Y-%m-%d')} · indexes: {', '.join(INDEXES)}*")
W("")

# Summary table
W("## Summary")
W("")
W("| Index | Docs | Size | Vector dims | Embedded text | Cluster field | gradeNorm |")
W("|---|---|---|---|---|---|---|")

details = {}
for idx in INDEXES:
    try:
        stats = es.indices.stats(index=idx, metric="docs,store")
        actual = list(stats["indices"].keys())[0]
        doc_count = es.count(index=idx, query={"match_all": {}})["count"]
        size_mb = stats["indices"][actual]["total"]["store"]["size_in_bytes"] // (1024*1024)

        mapping = es.indices.get_mapping(index=idx)
        actual_m = list(mapping.keys())[0]
        props = mapping[actual_m]["mappings"].get("properties", {})

        # Vector info
        vector_fields = {k: v for k, v in props.items() if v.get("type") in ("dense_vector", "semantic_text")}
        dims = None
        for k, v in vector_fields.items():
            dims = v.get("dims") or ("native" if v.get("type") == "semantic_text" else "?")

        # Cluster fields
        cluster_fields = [k for k in props if "cluster" in k.lower()]
        grade_norm = "gradeNorm" in props

        n = NOTES.get(idx, {})
        embedded = n.get("embedded", "?")

        W(f"| **{idx}** | {doc_count:,} | {size_mb:,}MB | {dims} | {embedded} | {', '.join(cluster_fields) or '—'} | {'✓' if grade_norm else '✗'} |")
        details[idx] = {"doc_count": doc_count, "size_mb": size_mb, "props": props, "vector_fields": vector_fields}
    except Exception as e:
        W(f"| **{idx}** | ERROR | — | — | — | — | — |")
        print(f"ERROR {idx}: {e}")

W("")
W("---")
W("")

# Per-index detail
W("## Per-Index Detail")
W("")

for idx in INDEXES:
    if idx not in details:
        continue
    d = details[idx]
    props = d["props"]
    n = NOTES.get(idx, {})

    W(f"### {idx}")
    W("")
    W(f"**Purpose:** {n.get('purpose', '—')}")
    W("")
    W(f"**What is embedded:** {n.get('embedded', '—')}")
    W("")
    W(f"**Search field / method:** {n.get('search_field', '—')}")
    W("")
    W(f"**Language scope:** {n.get('lang', '—')}")
    W("")
    W(f"**Clustering:** {n.get('cluster', '—')}")
    W("")

    W("**All fields:**")
    W("")
    W("| Field | ES type | Notes |")
    W("|---|---|---|")

    FIELD_NOTES = {
        "hadithText": "Full hadith text including isnad (HTML) — BM25 source",
        "englishMatn": "Isnad-stripped clean English matn — embedded for semantic search",
        "arabicMatn": "Arabic matn (isnad-stripped)",
        "arabicText": "Full Arabic text",
        "englishText": "English translation (may include isnad)",
        "semantic_text": "ES inference field — triggers mxbai-embed-large automatically",
        "embedding": "Dense vector for kNN search",
        "gradeNorm": "Normalized grade: Sahih / Hasan / Da'if / Maudu' / Uncategorized",
        "gradeEnglish": "Raw English grade string from source data",
        "gradeArabic": "Raw Arabic grade string",
        "grade": "Raw grade field (mxbai index)",
        "arabicGrade": "Raw Arabic grade (mxbai index)",
        "dupGroup": "Dedup group ID (0 = singleton, else min URN of group)",
        "isChainRef": "True if doc is a chain-reference (isnad-only, no matn)",
        "matchingArabicURN": "URN pointer to Arabic counterpart in arabic-openai",
        "clusterIdFinal": "Cluster assignment (all docs)",
        "clusterIdTranslated": "Cluster assignment (translated subset only)",
        "clusterIdShared": "Cluster in shared EN+AR space",
        "clusterIdLarge": "Cluster from large-model embeddings",
        "clusterIdV2": "Legacy cluster field (v2 experiment)",
        "clusterIdV3": "Legacy cluster field (v3 experiment)",
        "collection": "Collection slug (bukhari, muslim, etc.)",
        "hadithNumber": "Hadith number string",
        "hadithNumberNumeric": "Numeric hadith number for sorting",
        "urn": "Unique reference number",
        "arabicURN": "Arabic doc URN",
        "englishURN": "English doc URN",
        "lang": "Language code (en / ar)",
        "contentHash": "Hash of content for change detection",
        "hadMatnTag": "True if matn HTML tag present in source",
    }

    for field in sorted(props.keys()):
        ftype = props[field].get("type", "object")
        note = FIELD_NOTES.get(field, "")
        W(f"| `{field}` | {ftype} | {note} |")

    W("")
    W(f"**Consolidation note:** {n.get('consolidation', '—')}")
    W("")
    W("---")
    W("")

# Consolidation analysis
W("## Consolidation Analysis")
W("")
W("### What we have")
W("")
W("| Concern | Current state |")
W("|---|---|")
W("| BM25 lexical | `english-mxbai` (hadithText field) — no separate lexical index needed |")
W("| English semantic small | `english-openai` (OpenAI small, 1536-dim) |")
W("| English semantic large | `english-openai-large` (OpenAI large, 3072-dim) — benchmark only |")
W("| Arabic semantic small | `arabic-openai` (OpenAI small on arabicMatn) |")
W("| Arabic semantic large | `arabic-openai-large` (OpenAI large on arabicMatn) — benchmark only |")
W("| Multilingual shared | `multilingual-e5` (EN+AR same space, E5 model) |")
W("| ES-native inference | `english-mxbai` (mxbai-embed-large via ES inference endpoint) |")
W("")
W("### Redundancies and gaps")
W("")
W("**Redundant pairs (small vs large of same corpus):**")
W("- `english-openai` vs `english-openai-large` — same 48,703 docs, same englishMatn, different embedding size")
W("- `arabic-openai` vs `arabic-openai-large` — same 131,728 docs, same arabicMatn, different embedding size")
W("")
W("**Gaps:**")
W("- `english-openai-large` missing: gradeNorm, arabicText/arabicMatn, dupGroup")
W("- `arabic-openai-large` missing: gradeNorm, dupGroup")
W("- `multilingual-e5` missing: gradeNorm, dupGroup")
W("- BGE-M3 and Qwen3-Embed: not yet indexed")
W("")
W("**Potential consolidations:**")
W("- Drop `english-openai-large` after benchmarking (3072-dim, ~2GB, marginal quality gain)")
W("- Drop `arabic-openai-large` after benchmarking (3072-dim, ~5.8GB)")
W("- `english-mxbai` could replace `english-openai` if ES-native inference performs well (avoids external embedding call at query time)")
W("- Fill gradeNorm + dupGroup into `multilingual-e5` (copy from arabic-openai via URN match) for production use")
W("")
W("### Recommended production set (minimal)")
W("")
W("| Role | Index | Rationale |")
W("|---|---|---|")
W("| Lexical baseline | `english-mxbai` | Has hadithText; BM25 via `LEXICAL_INDEX` |")
W("| English semantic | `english-mxbai` or `english-openai` | mxbai: no external embed call; openai: richer metadata |")
W("| Arabic/multilingual semantic | `arabic-openai` | Richest metadata, both cluster fields, gradeNorm |")
W("| Cross-lingual / shared | `multilingual-e5` | After adding gradeNorm + dupGroup |")
W("")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Written: {OUT}")
