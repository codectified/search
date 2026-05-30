# Search Index Design — Decisions & Findings

> Living document — updated as experiments complete.  
> Branch: `feature/semantic-graph`

---

## 1. Index Catalog

### Current state (as of 2026-05-30)

| Index | Model | Dim | Docs | Text embedded | Status |
|---|---|---|---|---|---|
| `english-lexical` | BM25 | — | 131,853 | English + Arabic-only hadith text | ✅ live |
| `english-mxbai` | Ollama `mxbai-embed-large` | 1024 | 48,703 | `englishMatn` (isnad-stripped) | ✅ live |
| `english-openai` | OpenAI `text-embedding-3-small` | 1536 | 48,703 | `englishMatn` (isnad-stripped) | ✅ live |
| `arabic-openai` | OpenAI `text-embedding-3-small` | 1536 | 131,728 | `arabicMatn` (Arabic matn) | ✅ live |
| `english-openai-large` | OpenAI `text-embedding-3-large` | 3072 | 48,703 | `englishMatn` (isnad-stripped) | ✅ live |
| `arabic-openai-large` | OpenAI `text-embedding-3-large` | 3072 | 131,728 | `arabicMatn` | ✅ complete |
| `multilingual-e5` | `intfloat/multilingual-e5-large` | 1024 | ~28k | shared corpus (see §3) | 🔄 indexing (~14h) |
| `bge-m3` | `BAAI/bge-m3` | 1024 | 0 | shared corpus | ⏳ not started |
| `qwen3-embed` | `Qwen/Qwen3-Embedding` | TBD | 0 | shared corpus | ⏳ not started |

### Infrastructure
- ES not exposed to host — must run scripts inside `search-web-1` container
- ES host from inside container: `http://172.31.250.10:9200` (bridge IP) or `http://elasticsearch:9200`
- Indexes survive container restarts (Docker volume `es-data`)
- sentence-transformers installed to `/tmp/stpkg` (container user has no write access to site-packages)
- HuggingFace model cache: `/tmp/hf_cache`

---

## 2. Text Extraction — Why `englishMatn`

**Problem:** Raw English hadith text includes the full isnad (chain of transmission) before the matn (actual content). Example:

> *"Narrated Abu Huraira: The Prophet (ﷺ) said: ..."*

Embedding the full text buries the semantic content under narrator names, which are irrelevant to meaning-based retrieval.

**Solution:** `english_matn_map.json` — keyed by English URN, built by `tests/build_english_matn_map.py`.

**Extraction pipeline (9 patterns in priority order):**

1. `pure_matn` field (pre-existing clean field where present)
2. Stripping `Narrated X:` prefixes
3. Stripping `It was narrated from X that:` patterns
4. … (6 more patterns)
5. Fallback: full hadith text

**Coverage on 48,703 hadiths:**
- 77% clean matn extraction
- 6% weak (heuristic fallback)
- 15% full-text fallback (very short hadiths or unusual formats)

**Decision:** All three English-side indexes (`english-mxbai`, `english-openai`, `english-openai-large`) were rebuilt using `englishMatn`. The Arabic indexes embed `arabicMatn` directly (Arabic doesn't have the same isnad-embedding problem for our use case).

---

## 3. Shared Multilingual Corpus

For `multilingual-e5`, `bge-m3`, `qwen3-embed` — a single index covers both languages.

**Corpus construction (`tests/index_multilingual_shared.py`):**

```
Pass 1: arabic-openai index (131,728 hadiths)
  ├─ If hadith has englishURN → embed englishMatn (looked up from english_matn_map.json)
  └─ Else → embed arabicMatn

Pass 2: english-mxbai index (English-only collections not in Pass 1)
  └─ hisn, forty, nawawi40, riyadussalihin, etc. → embed englishMatn
```

**Total corpus: 180,430 documents**

**Why one index, not separate English/Arabic indexes?**
- These models are trained to embed both languages into the same semantic space
- A single index means one query retrieves across both languages automatically
- Avoids the routing problem of deciding which language index to query

**Why use englishMatn for translated hadiths instead of arabicMatn?**
- For English-language queries, English matn gives better semantic alignment
- The English matn is the cleaned, isnad-stripped version
- Arabic-only hadiths (no translation) still embed arabicMatn

---

## 4. Clustering & Centroid Pre-Filter

**Why clustering?** The Arabic hadith corpus has 131k docs. HNSW kNN over 131k with a tight filter (translated-only, ~44k) is fast enough without clustering. But for 180k-doc shared indexes and as corpus size grows, centroid pre-filtering is useful to:
- Reduce the effective search space from 131k/180k → ~2k per query
- Improve recall on the filtered subset (HNSW finds better candidates in a smaller space)

**How it works:**
1. `cluster_new_models.py` runs MiniBatchKMeans (k=200) on all embeddings
2. Centroids saved as `/code/{index}_centroids.json` (L2-normalized, k×dim float32)
3. `clusterIdShared` (multilingual indexes) or `clusterIdLarge` (openai-large) written to each ES doc
4. At query time: embed query → dot-product with all k centroids → top-2 closest clusters → filter kNN to those cluster docs

**Cluster field names by index:**

| Index | Cluster field | k | Centroid file |
|---|---|---|---|
| `arabic-openai` | `clusterIdTranslated` | 75 | `arabic_translated_cluster_centroids.json` |
| `arabic-openai-large` | `clusterIdLarge` | 200 | `arabic-openai-large_centroids.json` |
| `english-openai-large` | `clusterIdLarge` | 200 | `english-openai-large_centroids.json` |
| `multilingual-e5` | `clusterIdShared` | 200 | `multilingual-e5_centroids.json` |
| `bge-m3` | `clusterIdShared` | 200 | `bge-m3_centroids.json` |
| `qwen3-embed` | `clusterIdShared` | 200 | `qwen3-embed_centroids.json` |

**Note:** `english-openai` and `english-mxbai` (48k docs) do **not** use clustering — full HNSW over 48k is fast enough (<200ms) and clustering at this scale doesn't help recall.

---

## 5. Filtering Logic (Applied to All Models)

### Chain-reference filter
**What:** `isChainRef=True` marks hadiths that are pure isnad variant references with no matn. Example: *"This hadith has been narrated through another chain of transmitters"*.

**How detected:** Matched against `english-mxbai` hadiths using 8 patterns (short length, specific phrases).
- 1,572 flagged in `english-mxbai`
- 1,555 backfilled to `arabic-openai` by (collection, hadithNumber) match

**Applied as:** `{"bool": {"must_not": {"term": {"isChainRef": True}}}}`  
`must_not:true` (not `must:false`) so docs without the field still pass through.

### Deduplication
**What:** Near-duplicate hadiths (same matn, different chain) are collapsed to one representative per group.

**How:** Union-Find groups via cosine > 0.93 threshold. `dupGroup` field = 0 (singleton) or smallest URN in group.

**Representative selection:** Within each group, prefer the most authoritative collection (using `COLLECTION_BOOSTS` weights); score as tiebreaker.

**Applied:** Client-side in `_dedup_hits()` after fetching `size*3` candidates.

### Translation filter (Arabic-side models only)
`{"exists": {"field": "englishText"}}` — restricts results to hadiths with English translations. Applied to `arabic-openai` and `arabic-openai-large` (not multilingual shared indexes, which embed English matn directly).

---

## 6. Query Embedding

### OpenAI models
- `english-openai`, `english-openai-large`: embed query with same model as the index (small or large)
- `arabic-openai`, `arabic-openai-large`: embed query with same model — cross-lingual because text-embedding-3-small/large handles Arabic and English in a shared space

### sentence-transformers models (multilingual-e5, bge-m3, qwen3-embed)
- Lazy-loaded in Flask on first request (`_get_st_model()`)
- Model cached in `_ST_MODELS` dict (thread-safe with `threading.Lock`)
- Uses PyTorch FP32 backend for queries (indexing used INT8 ONNX — see §7)
- Query prefix: E5 uses `"query: "`, BGE-M3 and Qwen3 use no prefix
- Qwen3: uses `prompt_name="query"` parameter

---

## 7. ONNX INT8 for Indexing — Findings

**Context:** sentence-transformers on CPU (no GPU/MPS in Docker container) was too slow for full-corpus indexing.

### Speed benchmarks (E5 Multilingual Large, batch=64)

| Backend | Input | Throughput | Notes |
|---|---|---|---|
| PyTorch FP32 | "test sentence" (2 tokens) | — | baseline |
| PyTorch FP32 | Real hadiths (avg ~300 tokens) | ~1.3 docs/s | true production speed |
| ONNX FP32 (`model.onnx`) | "test sentence" | 18.7 docs/s | benchmark |
| ONNX INT8 (`model_qint8_avx512_vnni.onnx`) | "test sentence" | 55.2 docs/s | benchmark |
| ONNX INT8 | Real hadiths | **~3.1 docs/s** | actual indexing rate |

**Key lesson:** The benchmark with 2-token inputs was 18× optimistic vs real hadith texts (attention is O(seq_len²); real hadiths hit the 512-token max).

**ONNX JIT warmup issue:** ONNX compiles a separate execution plan per batch size. Warmup at batch=1 then running batch=64 triggers a second JIT compilation on the first real batch (~80s overhead). Fix: warm up at the actual `BATCH_SIZE`.

### Vector quality check (FP32 vs INT8, N=500 real hadith texts)

| Metric | Value |
|---|---|
| Mean cosine similarity | 0.9943 |
| Median cosine similarity | 0.9945 |
| Min cosine similarity | 0.9876 |
| % within 0.01 of 1.0 | 99.6% |
| Mean L2 distance | 0.106 |
| Max L2 distance | 0.158 |

**Conclusion:** INT8 quantization introduces ~0.6% angular error. Rankings are unaffected because the noise is small, uncorrelated with any query direction, and applied uniformly to all indexed documents.

**Production impact:** Queries embed with FP32 PyTorch; documents indexed with INT8 ONNX. The cross-backend mismatch adds ~0.6% cosine offset but **ranking order is preserved** (relative differences between candidates swamp the quantization noise).

---

## 8. Cluster Assignment Stability (INT8 vs FP32)

*(Results from `tests/cluster_comparison.py` on 10k-doc sample — 2026-05-30)*

[TO BE FILLED after experiment completes]

---

## 9. API Search Functions

### Route dispatch (`main.py /<language>/search`)

| model= param | Function | Index | Centroids |
|---|---|---|---|
| `mxbai` | `_mxbai_search` | `english-mxbai` | none (full HNSW) |
| `english-openai` | `_english_openai_search` | `english-openai` | none (full HNSW) |
| `arabic-openai` | `_arabic_openai_search` | `arabic-openai` | `arabic_translated_cluster_centroids.json` |
| `english-openai-large` | `_english_openai_large_search` | `english-openai-large` | `english-openai-large_centroids.json` (optional) |
| `arabic-openai-large` | `_arabic_openai_large_search` | `arabic-openai-large` | `arabic-openai-large_centroids.json` (required) |
| `multilingual-e5` | `_multilingual_shared_search` | `multilingual-e5` | `multilingual-e5_centroids.json` (optional) |
| `bge-m3` | `_multilingual_shared_search` | `bge-m3` | `bge-m3_centroids.json` (optional) |
| `qwen3-embed` | `_multilingual_shared_search` | `qwen3-embed` | `qwen3-embed_centroids.json` (optional) |

**Centroid loading:** Optional means search falls back to full HNSW if centroid file absent. Required means returns 503 until clustering is run.

### Standard parameters (all semantic endpoints)
- `size=N` — number of results to return (default 10)
- `show_dupes=1` — disable deduplication
- `collection=X` — filter to collection (repeatable)

---

## 10. Comparison Report Setup

Script: `tests/focused_comparison.py`  
Output: `test results & reports/focused_comparison.md`

**Query pool:** Two queries covering different retrieval challenges:
- `"aisha"` — proper noun, tests entity recall across collections
- `"comparing yourself to others"` — thematic English query, tests semantic understanding

**Report format:** Two perpendicular tables per query:
- Table 1: English-side models (mxbai, english-openai small, english-openai large)
- Table 2: Multilingual/Arabic-side (arabic-openai small, arabic-openai large, e5, bge-m3, qwen3)
- Rows = rank, Columns = model
- Each cell: collection/number, score, full English text, Arabic text (italic)

**Fetch pool:** 50 candidates → dedup + chain-ref filter → top 10 displayed

---

## 11. Outstanding Work

| Task | Blocked on |
|---|---|
| Run `cluster_new_models.py multilingual-e5` | E5 indexing finishing (~14h) |
| Deploy E5 centroids, test E5 search | Above |
| Arabic OpenAI Large: index remaining ~8k docs | OpenAI API credit top-up |
| Run `cluster_new_models.py arabic-openai-large` | Ready — run now |
| Start BGE-M3 indexing | Decision: worth ~17h? |
| Start Qwen3 indexing | Decision: worth ~17h? |
| Regenerate focused_comparison.md with all working models | All above |
