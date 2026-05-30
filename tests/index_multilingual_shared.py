"""
Builds a single shared multilingual index for E5-large-multilingual, BGE-M3,
or Qwen3-Embedding. One index covers both English and Arabic corpora:

  - Hadiths with English translations: embedded on englishMatn
  - Arabic-only hadiths: embedded on arabicMatn
  - English-only hadiths (hisn, forty, nawawi40): embedded on englishMatn

Requires sentence-transformers:
    pip install sentence-transformers

Usage (inside container):
    python3 /code/tests/index_multilingual_shared.py multilingual-e5-large
    python3 /code/tests/index_multilingual_shared.py BAAI/bge-m3
    python3 /code/tests/index_multilingual_shared.py Qwen/Qwen3-Embedding

Index names:
    multilingual-e5-large  → multilingual-e5
    BAAI/bge-m3            → bge-m3
    Qwen/Qwen3-Embedding   → qwen3-embed
"""
import os, sys, json, re, time
# sentence-transformers may be installed to /tmp/stpkg if the container user
# doesn't have write access to site-packages
sys.path.insert(0, "/tmp/stpkg")
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk as es_bulk

# ── Model → index name ────────────────────────────────────────────────────────
MODEL_TO_INDEX = {
    "intfloat/multilingual-e5-large": "multilingual-e5",
    "multilingual-e5-large":          "multilingual-e5",
    "BAAI/bge-m3":                    "bge-m3",
    "bge-m3":                         "bge-m3",
    "Qwen/Qwen3-Embedding":           "qwen3-embed",
    "Qwen3-Embedding":                "qwen3-embed",
}

# Some models need query/passage prefixes for best performance
MODEL_PASSAGE_PREFIX = {
    "intfloat/multilingual-e5-large": "passage: ",
    "multilingual-e5-large":          "passage: ",
    "BAAI/bge-m3":                    "",          # BGE-M3 uses no prefix for passages
    "Qwen/Qwen3-Embedding":           "",          # Qwen3 uses task instructions, handled separately
}

BATCH_SIZE = 256    # ONNX backend saturates well at 256; larger gives diminishing returns
MAP_FILE   = "/code/english_matn_map.json"
CKPT_DIR   = "/code"


def strip_html(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t or '')).strip()


def get_model_name():
    if len(sys.argv) < 2:
        print("Usage: index_multilingual_shared.py <model_name>")
        print("  e.g. multilingual-e5-large  |  BAAI/bge-m3  |  Qwen/Qwen3-Embedding")
        sys.exit(1)
    return sys.argv[1]


def load_model(model_name):
    from sentence_transformers import SentenceTransformer
    print(f"Loading model: {model_name}")
    # Prefer INT8 ONNX → FP32 ONNX → PyTorch (fastest to slowest on CPU)
    onnx_candidates = [
        "onnx/model_qint8_avx512_vnni.onnx",
        "onnx/model_qint8_arm64.onnx",
        "onnx/model.onnx",
    ]
    for onnx_file in onnx_candidates:
        try:
            model = SentenceTransformer(model_name, backend="onnx",
                model_kwargs={"file_name": onnx_file}, trust_remote_code=True)
            dim = model.get_sentence_embedding_dimension()
            print(f"  ONNX backend ({onnx_file.split('/')[-1]}) | dim={dim}")
            return model, dim
        except Exception as e:
            print(f"  {onnx_file.split('/')[-1]} unavailable: {e}")
    model = SentenceTransformer(model_name, trust_remote_code=True)
    dim = model.get_sentence_embedding_dimension()
    print(f"  PyTorch backend | dim={dim}")
    return model, dim


def encode(model, model_name, texts, batch_size=BATCH_SIZE):
    """Encode texts, applying model-specific prefix if needed."""
    prefix = MODEL_PASSAGE_PREFIX.get(model_name, "")
    if prefix:
        texts = [prefix + t for t in texts]

    # Qwen3 uses a prompt_name parameter for passage encoding
    if "Qwen3" in model_name or "qwen3" in model_name.lower():
        vecs = model.encode(texts, batch_size=batch_size, normalize_embeddings=True,
                            prompt_name="text")
    else:
        vecs = model.encode(texts, batch_size=batch_size, normalize_embeddings=True,
                            show_progress_bar=False)

    return vecs


def build_corpus(es, matn_map):
    """
    Build the full corpus for the shared multilingual index.

    Returns list of dicts:
      { doc_id, text, lang, collection, hadithNumber, urn, isChainRef, dupGroup,
        englishMatn, arabicMatn, englishText }
    """
    print("Building shared corpus from arabic-openai + english-only hadiths...")

    corpus = []
    arabic_urns = set()

    # ── Pass 1: all Arabic hadiths (131k) ────────────────────────────────────
    for hit in es_scan(es, index="arabic-openai",
            query={"query": {"match_all": {}}},
            _source={"excludes": ["embedding"]}, size=500):
        s      = hit["_source"]
        doc_id = hit["_id"]                         # "arabic:NNNNNN"
        urn    = s.get("urn", 0)
        arabic_urns.add(urn)

        en_urn = s.get("englishURN", 0)
        en_matn = ""
        if en_urn:
            entry   = matn_map.get(str(en_urn), {})
            en_matn = (entry.get("matn") or "").strip()

        ar_matn = strip_html(s.get("arabicMatn") or s.get("arabicText") or "")

        # Prefer English matn for translated hadiths; Arabic otherwise
        if en_matn:
            text = en_matn
            lang = "en"
        elif ar_matn:
            text = ar_matn
            lang = "ar"
        else:
            text = "."
            lang = "ar"

        corpus.append({
            "doc_id":      doc_id,
            "text":        text[:8000],
            "lang":        lang,
            "collection":  s.get("collection", ""),
            "hadithNumber": s.get("hadithNumber", ""),
            "urn":         urn,
            "isChainRef":  s.get("isChainRef", False),
            "dupGroup":    s.get("dupGroup", 0),
            "englishMatn": en_matn,
            "arabicMatn":  ar_matn,
            "englishText": strip_html(s.get("englishText", "")),
        })

    print(f"  {len(corpus):,} Arabic hadiths")

    # ── Pass 2: English-only hadiths not in arabic-openai ────────────────────
    en_only = 0
    for hit in es_scan(es, index="english-mxbai",
            query={"query": {"match_all": {}}},
            _source={"excludes": ["semantic_text"]}, size=500):
        s   = hit["_source"]
        urn = s.get("urn", 0)
        if urn in arabic_urns:
            continue    # already covered

        doc_id  = hit["_id"]   # "en:NNNNNN"
        en_matn = s.get("englishMatn") or strip_html(s.get("hadithText", ""))
        if not en_matn:
            continue

        corpus.append({
            "doc_id":      doc_id,
            "text":        en_matn[:8000],
            "lang":        "en",
            "collection":  s.get("collection", ""),
            "hadithNumber": s.get("hadithNumber", ""),
            "urn":         urn,
            "isChainRef":  s.get("isChainRef", False),
            "dupGroup":    s.get("dupGroup", 0),
            "englishMatn": en_matn,
            "arabicMatn":  "",
            "englishText": "",
        })
        en_only += 1

    print(f"  {en_only:,} English-only hadiths added (hisn, forty, etc.)")
    print(f"  Total corpus: {len(corpus):,} docs")
    return corpus


def run(model_name):
    index_name = MODEL_TO_INDEX.get(model_name)
    if not index_name:
        index_name = model_name.split("/")[-1].lower().replace("_", "-")
        print(f"  Warning: unrecognised model — using index name '{index_name}'")

    ckpt_file = os.path.join(CKPT_DIR, f"{index_name}_done.json")

    es = Elasticsearch("http://172.31.250.10:9200",
        basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]), request_timeout=120)

    # Load model first (downloads if needed)
    st_model, dim = load_model(model_name)

    # Load matn map
    print(f"Loading {MAP_FILE}...")
    with open(MAP_FILE, encoding="utf-8") as f:
        matn_map = json.load(f)
    print(f"  {len(matn_map):,} English matn entries")

    # Build corpus
    corpus = build_corpus(es, matn_map)

    # Create index if needed
    mapping = {
        "properties": {
            "embedding":    {"type": "dense_vector", "dims": dim, "index": True, "similarity": "cosine"},
            "collection":   {"type": "keyword"},
            "hadithNumber": {"type": "keyword"},
            "urn":          {"type": "long"},
            "lang":         {"type": "keyword"},
            "isChainRef":   {"type": "boolean"},
            "dupGroup":     {"type": "long"},
            "englishMatn":  {"type": "text"},
            "arabicMatn":   {"type": "text"},
            "englishText":  {"type": "text"},
            "clusterIdShared": {"type": "integer"},
        }
    }
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body={
            "settings": {"number_of_shards": 1, "number_of_replicas": 0},
            "mappings": mapping,
        })
        print(f"Created index: {index_name}")

    # Load checkpoint
    if os.path.exists(ckpt_file):
        with open(ckpt_file) as f:
            done_ids = set(json.load(f))
        print(f"Checkpoint: {len(done_ids):,} already indexed")
    else:
        done_ids = set()

    todo = [d for d in corpus if d["doc_id"] not in done_ids]
    print(f"{len(todo):,} remaining to embed and index")

    if not todo:
        print("Nothing to do — index is complete")
        return

    # Warmup: first ONNX inference call triggers JIT compilation (~60s cold).
    # Running it before the timed loop keeps the rate estimate clean.
    print("Warming up model...")
    _ = encode(st_model, model_name, [todo[0]["text"]])
    print("  Warmup done")

    # Embed and index
    t0 = indexed = es_errs = 0
    t0 = time.time()

    for i in range(0, len(todo), BATCH_SIZE):
        batch = todo[i:i + BATCH_SIZE]
        texts = [b["text"] for b in batch]

        try:
            vecs = encode(st_model, model_name, texts)
        except Exception as e:
            print(f"  Encode error batch {i//BATCH_SIZE}: {e}")
            continue

        actions = []
        for j, doc in enumerate(batch):
            actions.append({
                "_op_type": "index",
                "_index":   index_name,
                "_id":      doc["doc_id"],
                "_source":  {
                    "collection":  doc["collection"],
                    "hadithNumber": doc["hadithNumber"],
                    "urn":         doc["urn"],
                    "lang":        doc["lang"],
                    "isChainRef":  doc["isChainRef"],
                    "dupGroup":    doc["dupGroup"],
                    "englishMatn": doc["englishMatn"],
                    "arabicMatn":  doc["arabicMatn"],
                    "englishText": doc["englishText"],
                    "embedding":   vecs[j].tolist(),
                },
            })

        try:
            ok, errs = es_bulk(es, actions, raise_on_error=False, raise_on_exception=False)
            indexed += ok
            es_errs += len(errs) if errs else 0
            for doc in batch:
                done_ids.add(doc["doc_id"])
        except Exception as e:
            print(f"  ES error batch {i//BATCH_SIZE}: {e}")
            es_errs += 1

        # Save checkpoint every 50 batches
        if (i // BATCH_SIZE) % 50 == 0:
            with open(ckpt_file, "w") as f:
                json.dump(list(done_ids), f)
            el   = time.time() - t0
            rate = indexed / el if el > 0 else 0
            rem  = (len(todo) - indexed) / rate / 60 if rate > 0 else 0
            print(f"  [{indexed:,}/{len(todo):,}] {rate:.1f}/s | ~{rem:.0f} min | es_err={es_errs}")

    with open(ckpt_file, "w") as f:
        json.dump(list(done_ids), f)

    es.indices.refresh(index=index_name)
    count = es.count(index=index_name)["count"]
    elapsed = time.time() - t0
    print(f"\nDone: {indexed:,} indexed | es_err={es_errs} | {elapsed:.0f}s")
    print(f"Verified count: {count:,} in {index_name}")


if __name__ == "__main__":
    run(get_model_name())
