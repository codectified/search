# ES Index Inventory

*Generated 2026-05-31 · indexes: english-mxbai, english-openai, english-openai-large, arabic-openai, arabic-openai-large, multilingual-e5*

## Summary

| Index | Docs | Size | Vector dims | Embedded text | Cluster field | gradeNorm |
|---|---|---|---|---|---|---|
| **english-mxbai** | 48,703 | 870MB | native | `englishMatn` (isnad-stripped English matn) — embedded automatically by ES inference | — | ✓ |
| **english-openai** | 48,703 | 1,946MB | 1536 | `englishMatn` (isnad-stripped clean matn) | clusterIdFinal | ✓ |
| **english-openai-large** | 48,703 | 1,995MB | 3072 | `englishMatn` (isnad-stripped) | clusterIdLarge | ✗ |
| **arabic-openai** | 131,728 | 3,139MB | 1536 | `arabicMatn` (Arabic matn) with English translation used for query embedding | clusterIdFinal, clusterIdTranslated, clusterIdV2, clusterIdV3 | ✓ |
| **arabic-openai-large** | 131,728 | 5,792MB | 3072 | `arabicMatn` | clusterIdLarge | ✗ |
| **multilingual-e5** | 129,664 | 2,785MB | 1024 | `englishMatn` + `arabicMatn` (instruction-prefixed, shared embedding space) | clusterIdShared | ✗ |

---

## Per-Index Detail

### english-mxbai

**Purpose:** English semantic search via ES native `semantic_text` (mxbai-embed-large inference endpoint)

**What is embedded:** `englishMatn` (isnad-stripped English matn) — embedded automatically by ES inference

**Search field / method:** `semantic_text` (ES kNN semantic search) or `hadithText` (BM25 lexical fallback)

**Language scope:** English only (48,703 hadiths)

**Clustering:** None

**All fields:**

| Field | ES type | Notes |
|---|---|---|
| `arabicGrade` | text | Raw Arabic grade (mxbai index) |
| `arabicText` | text | Full Arabic text |
| `collection` | text | Collection slug (bukhari, muslim, etc.) |
| `contentHash` | keyword | Hash of content for change detection |
| `dupGroup` | integer | Dedup group ID (0 = singleton, else min URN of group) |
| `englishMatn` | text | Isnad-stripped clean English matn — embedded for semantic search |
| `grade` | text | Raw grade field (mxbai index) |
| `gradeNorm` | text | Normalized grade: Sahih / Hasan / Da'if / Maudu' / Uncategorized |
| `hadithNumber` | text | Hadith number string |
| `hadithText` | text | Full hadith text including isnad (HTML) — BM25 source |
| `isChainRef` | boolean | True if doc is a chain-reference (isnad-only, no matn) |
| `lang` | text | Language code (en / ar) |
| `matchingArabicURN` | text | URN pointer to Arabic counterpart in arabic-openai |
| `semantic_text` | semantic_text | ES inference field — triggers mxbai-embed-large automatically |
| `urn` | text | Unique reference number |

**Consolidation note:** Only index with ES-native inference; cannot bulk-update without re-triggering inference. Has `hadithText` for BM25 so doubles as the lexical baseline index.

---

### english-openai

**Purpose:** English semantic search via OpenAI `text-embedding-3-small` (1536-dim)

**What is embedded:** `englishMatn` (isnad-stripped clean matn)

**Search field / method:** `embedding` (kNN HNSW), centroid pre-filter

**Language scope:** English only (48,703 hadiths)

**Clustering:** `clusterIdFinal` (75 clusters, centroid method)

**All fields:**

| Field | ES type | Notes |
|---|---|---|
| `arabicURN` | integer | Arabic doc URN |
| `clusterIdFinal` | integer | Cluster assignment (all docs) |
| `collection` | keyword | Collection slug (bukhari, muslim, etc.) |
| `dupGroup` | integer | Dedup group ID (0 = singleton, else min URN of group) |
| `embedding` | dense_vector | Dense vector for kNN search |
| `englishText` | text | English translation (may include isnad) |
| `englishURN` | integer | English doc URN |
| `gradeArabic` | keyword | Raw Arabic grade string |
| `gradeEnglish` | keyword | Raw English grade string from source data |
| `gradeNorm` | text | Normalized grade: Sahih / Hasan / Da'if / Maudu' / Uncategorized |
| `hadithNumber` | keyword | Hadith number string |
| `isChainRef` | boolean | True if doc is a chain-reference (isnad-only, no matn) |

**Consolidation note:** Has gradeNorm, dupGroup, isChainRef. Most complete English index. Missing arabicMatn (looked up from arabic-openai at query time).

---

### english-openai-large

**Purpose:** English semantic search via OpenAI `text-embedding-3-large` (3072-dim)

**What is embedded:** `englishMatn` (isnad-stripped)

**Search field / method:** `embedding` (kNN HNSW), centroid pre-filter

**Language scope:** English only (48,703 hadiths)

**Clustering:** `clusterIdLarge` (cluster count TBD)

**All fields:**

| Field | ES type | Notes |
|---|---|---|
| `clusterIdLarge` | integer | Cluster from large-model embeddings |
| `collection` | keyword | Collection slug (bukhari, muslim, etc.) |
| `dupGroup` | long | Dedup group ID (0 = singleton, else min URN of group) |
| `embedding` | dense_vector | Dense vector for kNN search |
| `hadithNumber` | keyword | Hadith number string |
| `isChainRef` | boolean | True if doc is a chain-reference (isnad-only, no matn) |
| `urn` | long | Unique reference number |

**Consolidation note:** Sparse: missing gradeNorm, arabicText, englishText. Mainly a quality benchmark vs english-openai.

---

### arabic-openai

**Purpose:** Arabic + translated-English semantic search via OpenAI `text-embedding-3-small` (1536-dim)

**What is embedded:** `arabicMatn` (Arabic matn) with English translation used for query embedding

**Search field / method:** `embedding` (kNN HNSW), centroid pre-filter

**Language scope:** All languages (131,728 docs: Arabic + English + translated)

**Clustering:** `clusterIdFinal` (148 clusters, all docs); `clusterIdTranslated` (75 clusters, translated subset)

**All fields:**

| Field | ES type | Notes |
|---|---|---|
| `arabicMatn` | text | Arabic matn (isnad-stripped) |
| `arabicText` | text | Full Arabic text |
| `arabicURN` | integer | Arabic doc URN |
| `clusterIdFinal` | integer | Cluster assignment (all docs) |
| `clusterIdTranslated` | integer | Cluster assignment (translated subset only) |
| `clusterIdV2` | integer | Legacy cluster field (v2 experiment) |
| `clusterIdV3` | integer | Legacy cluster field (v3 experiment) |
| `collection` | keyword | Collection slug (bukhari, muslim, etc.) |
| `embedding` | dense_vector | Dense vector for kNN search |
| `englishText` | text | English translation (may include isnad) |
| `englishURN` | integer | English doc URN |
| `gradeArabic` | keyword | Raw Arabic grade string |
| `gradeEnglish` | keyword | Raw English grade string from source data |
| `gradeNorm` | text | Normalized grade: Sahih / Hasan / Da'if / Maudu' / Uncategorized |
| `hadMatnTag` | boolean | True if matn HTML tag present in source |
| `hadithNumber` | keyword | Hadith number string |
| `isChainRef` | boolean | True if doc is a chain-reference (isnad-only, no matn) |

**Consolidation note:** Richest index: arabicMatn, arabicText, englishText, gradeNorm, both cluster fields. Central store for Arabic text lookup.

---

### arabic-openai-large

**Purpose:** Arabic semantic search via OpenAI `text-embedding-3-large` (3072-dim)

**What is embedded:** `arabicMatn`

**Search field / method:** `embedding` (kNN HNSW), centroid pre-filter

**Language scope:** All languages (131,728 docs)

**Clustering:** `clusterIdLarge` (clustering in progress)

**All fields:**

| Field | ES type | Notes |
|---|---|---|
| `arabicMatn` | text | Arabic matn (isnad-stripped) |
| `arabicText` | text | Full Arabic text |
| `clusterIdLarge` | integer | Cluster from large-model embeddings |
| `collection` | keyword | Collection slug (bukhari, muslim, etc.) |
| `dupGroup` | long | Dedup group ID (0 = singleton, else min URN of group) |
| `embedding` | dense_vector | Dense vector for kNN search |
| `englishText` | text | English translation (may include isnad) |
| `englishURN` | long | English doc URN |
| `hadMatnTag` | boolean | True if matn HTML tag present in source |
| `hadithNumber` | keyword | Hadith number string |
| `isChainRef` | boolean | True if doc is a chain-reference (isnad-only, no matn) |
| `urn` | long | Unique reference number |

**Consolidation note:** Quality benchmark vs arabic-openai. Missing gradeNorm, dupGroup. Expensive (5.8GB).

---

### multilingual-e5

**Purpose:** Multilingual semantic search via `intfloat/multilingual-e5-large` (1024-dim)

**What is embedded:** `englishMatn` + `arabicMatn` (instruction-prefixed, shared embedding space)

**Search field / method:** `embedding` (kNN HNSW), centroid pre-filter

**Language scope:** Shared EN+AR space (129,216 docs, indexing ~85% complete)

**Clustering:** `clusterIdShared` (75 clusters across EN+AR)

**All fields:**

| Field | ES type | Notes |
|---|---|---|
| `arabicMatn` | text | Arabic matn (isnad-stripped) |
| `clusterIdShared` | integer | Cluster in shared EN+AR space |
| `collection` | keyword | Collection slug (bukhari, muslim, etc.) |
| `dupGroup` | long | Dedup group ID (0 = singleton, else min URN of group) |
| `embedding` | dense_vector | Dense vector for kNN search |
| `englishMatn` | text | Isnad-stripped clean English matn — embedded for semantic search |
| `englishText` | text | English translation (may include isnad) |
| `hadithNumber` | keyword | Hadith number string |
| `isChainRef` | boolean | True if doc is a chain-reference (isnad-only, no matn) |
| `lang` | keyword | Language code (en / ar) |
| `urn` | long | Unique reference number |

**Consolidation note:** Only index embedding both languages in the same space. Has englishMatn + arabicMatn. Missing gradeNorm, dupGroup.

---

## Consolidation Analysis

### What we have

| Concern | Current state |
|---|---|
| BM25 lexical | `english-mxbai` (hadithText field) — no separate lexical index needed |
| English semantic small | `english-openai` (OpenAI small, 1536-dim) |
| English semantic large | `english-openai-large` (OpenAI large, 3072-dim) — benchmark only |
| Arabic semantic small | `arabic-openai` (OpenAI small on arabicMatn) |
| Arabic semantic large | `arabic-openai-large` (OpenAI large on arabicMatn) — benchmark only |
| Multilingual shared | `multilingual-e5` (EN+AR same space, E5 model) |
| ES-native inference | `english-mxbai` (mxbai-embed-large via ES inference endpoint) |

### Redundancies and gaps

**Redundant pairs (small vs large of same corpus):**
- `english-openai` vs `english-openai-large` — same 48,703 docs, same englishMatn, different embedding size
- `arabic-openai` vs `arabic-openai-large` — same 131,728 docs, same arabicMatn, different embedding size

**Gaps:**
- `english-openai-large` missing: gradeNorm, arabicText/arabicMatn, dupGroup
- `arabic-openai-large` missing: gradeNorm, dupGroup
- `multilingual-e5` missing: gradeNorm, dupGroup
- BGE-M3 and Qwen3-Embed: not yet indexed

**Potential consolidations:**
- Drop `english-openai-large` after benchmarking (3072-dim, ~2GB, marginal quality gain)
- Drop `arabic-openai-large` after benchmarking (3072-dim, ~5.8GB)
- `english-mxbai` could replace `english-openai` if ES-native inference performs well (avoids external embedding call at query time)
- Fill gradeNorm + dupGroup into `multilingual-e5` (copy from arabic-openai via URN match) for production use

### Recommended production set (minimal)

| Role | Index | Rationale |
|---|---|---|
| Lexical baseline | `english-mxbai` | Has hadithText; BM25 via `LEXICAL_INDEX` |
| English semantic | `english-mxbai` or `english-openai` | mxbai: no external embed call; openai: richer metadata |
| Arabic/multilingual semantic | `arabic-openai` | Richest metadata, both cluster fields, gradeNorm |
| Cross-lingual / shared | `multilingual-e5` | After adding gradeNorm + dupGroup |
