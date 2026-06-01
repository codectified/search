# Embedding Model Evaluation — Full Registry

All evaluation indexes live in the local Docker ES cluster (`http://172.31.250.10:9200`).

---

## 1. small-model-eval (candidate comparison index)

Single index, one `dense_vector` field per model. All 11 candidates embedded on the
same 48,702 docs so scores are directly comparable.

**Current input text:** raw `hadithText` for all models (includes isnad + matn).
**Planned:** re-run with `englishMatn` (isnad-stripped) as a parallel set of `_matn`
fields — see §4 below.

### 1a. Ollama — F16, served locally

| Model | ES Field | Dims | Params | Notes |
|---|---|---|---|---|
| mxbai-embed-large | `vec_mxbai` | 1024 | 335M | **Prod baseline.** Vectors extracted from `english-mxbai` — no re-embed. |
| nomic-embed-text | `vec_nomic` | 768 | 137M | |
| snowflake-arctic-embed:m | `vec_snowflake` | 768 | 110M | |
| all-MiniLM-L6-v2 | `vec_miniLM` | 384 | 22M | |

### 1b. sentence_transformers / HuggingFace — FP32, CPU inference

| Model | ES Field | Dims | Params | Notes |
|---|---|---|---|---|
| google/embeddinggemma-300m | `vec_gemma` | 768 | 300M | Base model. |
| google/embeddinggemma-300m-qat-q8_0-unquantized | `vec_gemma_q8` | 768 | 300M | QAT-trained for INT8; weights in FP32. |
| google/embeddinggemma-300m-qat-q4_0-unquantized | `vec_gemma_q4` | 768 | 300M | QAT-trained for INT4; weights in FP32. |
| mixedbread-ai/mxbai-embed-xsmall-v1 | `vec_mxbai_xs` | 384 | 33M | FP32 baseline for xsmall. |

### 1c. Ollama GGUF — quantized, community conversion

| Model | ES Field | Dims | Params | GGUF | Quantization |
|---|---|---|---|---|---|
| mxbai-embed-large (mxbai-q4km) | `vec_mxbai_q4km` | 1024 | 335M | `ChristianAzinn/mxbai-embed-large-v1-gguf` | Q4_K_M |

> Q4_K_M = K-quant: mixed precision, ~4.5 bits avg. Attention layers kept at higher precision,
> feed-forward layers compressed harder. Smarter than naive INT4.
> Model size: F16 ~1.3GB → Q4_K_M ~153MB.

### 1d. ONNX Runtime — quantized, CPU-executable

| Model | ES Field | Dims | Params | ONNX file | Quantization |
|---|---|---|---|---|---|
| mixedbread-ai/mxbai-embed-large-v1 | `vec_mxbai_q` | 1024 | 335M | `onnx/model_quantized.onnx` | INT8 |
| mixedbread-ai/mxbai-embed-xsmall-v1 | `vec_mxbai_xs_q8` | 384 | 33M | `onnx/model_int8.onnx` | INT8 |
| mixedbread-ai/mxbai-embed-xsmall-v1 | `vec_mxbai_xs_q4` | 384 | 33M | `onnx/model_q4.onnx` | INT4 |

> **Note on FP8:** requires H100-class GPU — not CPU-executable.
> INT8 is the practical CPU equivalent: same 8-bit width, ~2× memory reduction, no special hardware.

---

## 2. English large-model indexes (production / research)

Separate indexes, each with a single `embedding` field. Used as quality ceilings for the
small-model comparison.

| ES Index | Model | Dims | Params | Docs | Disk | Input text |
|---|---|---|---|---|---|---|
| `english-mxbai` | mxbai-embed-large (Ollama F16) | 1024 | 335M | 48,703 | ~870MB | `hadithText` |
| `english-openai` | OpenAI text-embedding-ada-002 | 1536 | — | 48,703 | 1.9GB | `hadithText` |
| `english-openai-large` | OpenAI text-embedding-3-large | 3072 | — | 48,703 | 1.9GB | `hadithText` |

---

## 3. Arabic-only indexes (research)

Arabic hadiths embedded independently. Higher doc count (131k) because Arabic covers all
collections without the English dedup pass.

| ES Index | Model | Dims | Docs | Disk | Input text |
|---|---|---|---|---|---|
| `arabic-openai` | OpenAI text-embedding-ada-002 | 1536 | 131,728 | 3GB | `arabicText` |
| `arabic-openai-large` | OpenAI text-embedding-3-large | 3072 | 131,728 | 7GB | `arabicText` |

---

## 4. Multilingual index (research)

| ES Index | Model | Dims | Docs | Disk | Input text |
|---|---|---|---|---|---|
| `multilingual-e5` | multilingual-e5-large | 1024 | 129,664 | 2.6GB | Arabic + English combined |

---

## 5. Planned: englishMatn variant

All `small-model-eval` vectors currently use raw `hadithText` (isnad + matn).
The isnad (chain of narrators) is noise for semantic search — queries like
"good character" should match the matn only.

Plan: strip isnad using `tests/extract_english_matn.py`, then add a parallel set
of `_matn`-suffixed fields to `small-model-eval`:

| Proposed field | Source field | Notes |
|---|---|---|
| `vec_mxbai_matn` | `englishMatn` | Compare vs `vec_mxbai` to quantify isnad noise |
| `vec_nomic_matn` | `englishMatn` | |
| `vec_gemma_matn` | `englishMatn` | |
| *(etc.)* | | |

Requires: backfill `englishMatn` in the source index, or supply a precomputed
`english_matn_map.json` (keyed by URN) to the indexer.

---

## 6. Questions each comparison answers

| Question | Fields compared |
|---|---|
| Can a small model replace mxbai-large for prod? | `vec_nomic`, `vec_snowflake`, `vec_miniLM`, `vec_mxbai_xs` vs `vec_mxbai` |
| Does quantizing mxbai-large hurt retrieval? | `vec_mxbai` (F16) vs `vec_mxbai_q` (INT8 ONNX) |
| xsmall quantization ladder | `vec_mxbai_xs` (FP32) → `vec_mxbai_xs_q8` (INT8) → `vec_mxbai_xs_q4` (INT4) |
| Gemma QAT robustness | `vec_gemma` vs `vec_gemma_q8` vs `vec_gemma_q4` — should be near-identical |
| Does isnad noise matter? | `vec_X` (hadithText) vs `vec_X_matn` (englishMatn) — once §5 is built |
| How do small models compare to OpenAI ceiling? | `small-model-eval` results vs `english-openai` / `english-openai-large` |
| Arabic semantic search quality | `arabic-openai` vs `arabic-openai-large` |

---

## 7. Scripts

| Script | Purpose |
|---|---|
| `tests/build_small_model_eval_index.py` | Builds/rebuilds `small-model-eval`. |
| `tests/small_model_comparison.py` | Runs 8 queries across all 11 models → `test results & reports/small_model_comparison.md` |

```bash
# Full rebuild (takes ~4-6h on CPU — Gemma models are large)
docker exec -e HF_TOKEN=hf_xxx search-web-1 \
  python3 /code/tests/build_small_model_eval_index.py --rebuild

# Run comparison report (requires small-model-eval to be populated)
docker exec -e HF_TOKEN=hf_xxx search-web-1 \
  python3 /code/tests/small_model_comparison.py
```
