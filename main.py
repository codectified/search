import hashlib
import logging
import sys
import threading
import time
import uuid
from flask import Flask, request, jsonify, g
from werkzeug.exceptions import HTTPException
import pymysql
import os
from dotenv import load_dotenv
import json

import numpy as np
from openai import OpenAI
from elasticsearch import Elasticsearch, helpers, BadRequestError, NotFoundError
from pythonjsonlogger import jsonlogger

from utils.shortcode_pattern import SHORTCODE_PATTERN

load_dotenv(".env.local")


_log_handler = logging.StreamHandler(sys.stdout)
_log_handler.setFormatter(
    jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
)
access_log = logging.getLogger("search.access")
access_log.setLevel(logging.INFO)
access_log.addHandler(_log_handler)
access_log.propagate = False


app = Flask(__name__)


@app.before_request
def _record_request_start():
    g.request_start = time.perf_counter()
    g.request_id = request.headers.get("X-Request-Id") or uuid.uuid4().hex


@app.after_request
def _emit_access_log(response):
    duration_ms = (time.perf_counter() - g.request_start) * 1000
    access_log.info(
        "request",
        extra={
            "request_id": g.request_id,
            "method": request.method,
            "path": request.path,
            "status": response.status_code,
            "duration_ms": round(duration_ms, 2),
            "remote_addr": request.headers.get("X-Forwarded-For", request.remote_addr),
            "query": request.args.to_dict(flat=False),
            "user_agent": request.headers.get("User-Agent"),
        },
    )
    response.headers["X-Request-Id"] = g.request_id
    return response


es_auth = ("elastic", os.environ.get("ELASTIC_PASSWORD"))
es_base_url = f"http://elasticsearch:{os.environ.get('ES_PORT')}"
es_client = Elasticsearch(
    es_base_url,
    http_auth=es_auth,
    max_retries=3,
    retry_on_timeout=True,
    request_timeout=10,
)


def _is_truthy(value):
    return (value or "").lower() in ("1", "true", "yes")


# ── OpenAI centroid search (Arabic + English) ─────────────────────────────────

_OPENAI_ENABLED = _is_truthy(os.environ.get("OPENAI_ENABLED"))
_openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY")) if _OPENAI_ENABLED else None

ARABIC_OPENAI_INDEX      = "arabic-openai"
_ARABIC_EMBED_MODEL      = "text-embedding-3-small"
_ARABIC_CENTROIDS_PATH            = "/code/arabic_cluster_centroids_final.json"
# Centroids computed over the ~48k translated-only Arabic hadiths (englishURN > 0).
# Eliminates cluster pollution from Arabic-only collections (ibnabishayba, etc.).
_ARABIC_TRANSLATED_CENTROIDS_PATH = "/code/arabic_translated_cluster_centroids.json"
_ENGLISH_CENTROIDS_PATH           = "/code/english_cluster_centroids.json"
_TOP_N_CLUSTERS                   = 2  # 2 × ~649 avg ≈ 1,300 docs vs 48k

# ── New model centroid paths ───────────────────────────────────────────────────
# Keyed by model key — centroids for each shared/large index.
# Files are written by tests/cluster_new_models.py after indexing completes.
_NEW_MODEL_CENTROID_PATHS = {
    "english-openai-large": "/code/english-openai-large_centroids.json",
    "arabic-openai-large":  "/code/arabic-openai-large_centroids.json",
    "multilingual-e5":      "/code/multilingual-e5_centroids.json",
    "bge-m3":               "/code/bge-m3_centroids.json",
    "qwen3-embed":          "/code/qwen3-embed_centroids.json",
}

# Shape: (k, 1536), L2-normalized — loaded once at startup, None if file absent.
_ARABIC_CENTROIDS            = None
_ARABIC_TRANSLATED_CENTROIDS = None
_ENGLISH_CENTROIDS           = None
_NEW_MODEL_CENTROIDS         = {}    # {model_key: np.ndarray | None}


def _load_centroids(path, label):
    if not os.path.exists(path):
        access_log.warning("centroids_missing", extra={"path": path})
        return None
    with open(path) as f:
        raw = json.load(f)
    mat   = np.array(raw, dtype=np.float32)
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    mat   = mat / np.maximum(norms, 1e-9)
    access_log.info("centroids_loaded", extra={"label": label, "n_clusters": len(mat)})
    return mat


def _load_arabic_centroids():
    global _ARABIC_CENTROIDS, _ARABIC_TRANSLATED_CENTROIDS
    _ARABIC_CENTROIDS            = _load_centroids(_ARABIC_CENTROIDS_PATH, "arabic-all")
    _ARABIC_TRANSLATED_CENTROIDS = _load_centroids(_ARABIC_TRANSLATED_CENTROIDS_PATH, "arabic-translated")


def _load_english_centroids():
    global _ENGLISH_CENTROIDS
    _ENGLISH_CENTROIDS = _load_centroids(_ENGLISH_CENTROIDS_PATH, "english")


def _load_new_model_centroids():
    global _NEW_MODEL_CENTROIDS
    for key, path in _NEW_MODEL_CENTROID_PATHS.items():
        _NEW_MODEL_CENTROIDS[key] = _load_centroids(path, key)


_load_arabic_centroids()
_load_english_centroids()
_load_new_model_centroids()

# ── Sentence-transformers lazy loading ────────────────────────────────────────
# Models are loaded on first request to avoid startup memory pressure.
# /tmp/stpkg is the install target used by the indexing scripts.
_ST_MODELS: dict = {}
_ST_LOCK = threading.Lock()
_OPENAI_LARGE_MODEL = "text-embedding-3-large"


def _get_st_model(model_key):
    if model_key in _ST_MODELS:
        return _ST_MODELS[model_key]
    with _ST_LOCK:
        if model_key in _ST_MODELS:
            return _ST_MODELS[model_key]
        sys.path.insert(0, "/tmp/stpkg")
        os.environ.setdefault("HF_HOME", "/tmp/hf_cache")
        from sentence_transformers import SentenceTransformer  # noqa: PLC0415
        embed_model = EMBEDDING_MODELS[model_key]["embed_model"]
        st = SentenceTransformer(embed_model, trust_remote_code=True)
        _ST_MODELS[model_key] = st
        return st


def _embed_with_st(model_key, query):
    """Embed a single query string using a sentence-transformers model."""
    model_cfg = EMBEDDING_MODELS[model_key]
    prefix = model_cfg.get("query_prefix", "")
    embed_model_name = model_cfg["embed_model"]
    st = _get_st_model(model_key)
    text = prefix + query
    if "Qwen3" in embed_model_name or "qwen3" in embed_model_name.lower():
        vec = st.encode([text], normalize_embeddings=True, prompt_name="query")[0]
    else:
        vec = st.encode([text], normalize_embeddings=True)[0]
    return np.array(vec, dtype=np.float32)


def _embed_openai_large(query):
    """Embed query with text-embedding-3-large and L2-normalize."""
    resp = _openai_client.embeddings.create(model=_OPENAI_LARGE_MODEL, input=query)
    vec = np.array(resp.data[0].embedding, dtype=np.float32)
    norm = np.linalg.norm(vec)
    return vec / norm if norm > 0 else vec


# Pure lexical index — no embeddings, fast to rebuild.
LEXICAL_INDEX = "english-lexical"

# Each model gets its own ES index so you can index and switch independently.
# The semantic field is always called "semantic_text" inside each model's index.
SEMANTIC_FIELD = "semantic_text"

_OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")

EMBEDDING_MODELS = {
    "mxbai": {
        "label": "mxbai-embed-large",
        "index": "english-mxbai",
        "inference_id": "mxbai-embed-large",
        "enabled": _is_truthy(os.environ.get("MXBAI_ENABLED")),
        "multilingual": False,
        # Ollama exposes an OpenAI-compatible API — use that since ES 8.16 has no native ollama service.
        "service": "openai",
        "service_settings": {
            "api_key": "ollama",  # Ollama doesn't require auth; ES requires a non-empty value
            "url": f"{_OLLAMA_URL}/v1/embeddings",
            "model_id": "mxbai-embed-large",
            "similarity": "cosine",
        },
    },
    "arabic-openai": {
        "label": "text-embedding-3-small (Arabic matn, cross-lingual)",
        "index": ARABIC_OPENAI_INDEX,
        "enabled": _OPENAI_ENABLED,
        "multilingual": True,
        "custom_knn": True,
    },
    "english-openai": {
        "label": "text-embedding-3-small (English text)",
        "index": "english-openai",
        "enabled": _OPENAI_ENABLED,
        "multilingual": False,
        "custom_knn": True,
    },
    # ── New models ─────────────────────────────────────────────────────────────
    "english-openai-large": {
        "label": "text-embedding-3-large (English matn)",
        "index": "english-openai-large",
        "enabled": _OPENAI_ENABLED,
        "multilingual": False,
        "custom_knn": True,
    },
    "arabic-openai-large": {
        "label": "text-embedding-3-large (Arabic matn)",
        "index": "arabic-openai-large",
        "enabled": _OPENAI_ENABLED,
        "multilingual": True,
        "custom_knn": True,
    },
    "multilingual-e5": {
        "label": "multilingual-e5-large (shared English+Arabic)",
        "index": "multilingual-e5",
        "enabled": True,
        "multilingual": True,
        "custom_knn": True,
        "embed_model": "intfloat/multilingual-e5-large",
        "query_prefix": "query: ",
    },
    "bge-m3": {
        "label": "BGE-M3 (shared English+Arabic)",
        "index": "bge-m3",
        "enabled": True,
        "multilingual": True,
        "custom_knn": True,
        "embed_model": "BAAI/bge-m3",
        "query_prefix": "",
    },
    "qwen3-embed": {
        "label": "Qwen3-Embedding (shared English+Arabic)",
        "index": "qwen3-embed",
        "enabled": True,
        "multilingual": True,
        "custom_knn": True,
        "embed_model": "Qwen/Qwen3-Embedding",
        "query_prefix": "",
    },
}

_ENABLED_MODELS = {k: v for k, v in EMBEDDING_MODELS.items() if v["enabled"]}
SEMANTIC_ENABLED = bool(_ENABLED_MODELS)

# Bulk timeout — embedding calls during indexing are slow.
BULK_REQUEST_TIMEOUT = 300 if SEMANTIC_ENABLED else 60

SEARCH_MODES = ("lexical", "semantic")
SEMANTIC_MODES = ("semantic",)

COLLECTION_BOOSTS = [
    ("bukhari", 5.0),
    ("muslim", 4.8),
    ("nasai", 3.5),
    ("abudawud", 3.0),
    ("tirmidhi", 2.5),
    ("ibnmajah", 2.0),
    ("malik", 2.5),
    ("ahmad", 2.5),
    ("darimi", 2.0),
    ("mishkat", 2.5),
    ("nawawi40", 3.3),
    ("riyadussalihin", 2.5),
]

_COLLECTION_BOOST_MAP = {k: v for k, v in COLLECTION_BOOSTS}

# chain-ref filter: exclude hadiths that are pure isnad references with no matn.
# must_not:true (not term:false) so docs without the field still pass through.
_CHAIN_REF_FILTER = {"bool": {"must_not": {"term": {"isChainRef": True}}}}


def _dedup_hits(hits, size):
    """Collapse duplicate groups, choosing the best representative per group.

    Within each dupGroup, prefer the member from the most authoritative collection
    (using COLLECTION_BOOSTS); use raw ES score as tiebreaker. Singletons
    (dupGroup=0) are kept as-is. Final list is re-sorted by ES score and trimmed
    to `size`.
    """
    groups = {}    # gid -> best hit so far
    singletons = []

    for h in hits:
        gid = h["_source"].get("dupGroup", 0)
        if gid == 0:
            singletons.append(h)
        else:
            coll = h["_source"].get("collection", "")
            key = (_COLLECTION_BOOST_MAP.get(coll, 1.0), h["_score"])
            if gid not in groups or key > groups[gid][1]:
                groups[gid] = (h, key)

    merged = singletons + [h for h, _ in groups.values()]
    merged.sort(key=lambda h: h["_score"], reverse=True)
    return merged[:size]


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    if isinstance(exc, HTTPException):
        return exc
    access_log.exception(
        "unhandled_exception",
        extra={"request_id": getattr(g, "request_id", None), "exception": type(exc).__name__},
    )
    return jsonify({"error": "internal server error"}), 500


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to sunnah.com search api.</h1>"


# ── Index management ──────────────────────────────────────────────────────────

def _ensure_inference_endpoint(model):
    try:
        es_client.inference.get(task_type="text_embedding", inference_id=model["inference_id"])
        return
    except NotFoundError:
        pass
    es_client.options(request_timeout=60).inference.put(
        task_type="text_embedding",
        inference_id=model["inference_id"],
        inference_config={
            "service": model["service"],
            "service_settings": model["service_settings"],
        },
    )


def _content_hash(doc):
    payload = {k: v for k, v in doc.items() if k not in ("_id", "contentHash", SEMANTIC_FIELD)}
    encoded = json.dumps(payload, sort_keys=True, default=str, ensure_ascii=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _prepare_documents(documents):
    for doc in documents:
        doc["_id"] = f"{doc['lang']}:{doc['urn']}"
        doc["contentHash"] = _content_hash(doc)


def _bulk_index(actions, index, timeout=None):
    return helpers.bulk(
        es_client,
        actions,
        index=index,
        request_timeout=timeout or BULK_REQUEST_TIMEOUT,
        raise_on_error=False,
        raise_on_exception=False,
    )


def _index_is_incremental(index_name):
    """True if the index has a contentHash field (built by this indexer)."""
    try:
        mapping = es_client.indices.get_mapping(index=index_name)
    except NotFoundError:
        return False
    return all(
        "contentHash" in idx.get("mappings", {}).get("properties", {})
        for idx in mapping.values()
    )


def _make_settings():
    return {
        "index": {
            "number_of_shards": 1,
            "search.slowlog.threshold.query.warn": "1s",
            "search.slowlog.threshold.query.info": "500ms",
            "search.slowlog.threshold.fetch.warn": "500ms",
            "analysis": {
                "analyzer": {
                    "trigram": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "char_filter": ["html_strip", "shortcode_strip"],
                        "filter": ["lowercase", "stop", "shingle"],
                    },
                    "synonym": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "char_filter": ["html_strip", "shortcode_strip"],
                        "filter": ["lowercase", "stop", "synonyms_filter", "stemmer"],
                    },
                    "custom_arabic": {
                        "tokenizer": "standard",
                        "char_filter": ["html_strip", "shortcode_strip"],
                        "filter": ["lowercase", "decimal_digit", "arabic_normalization", "arabic_stemmer", "shingle"],
                    },
                },
                "char_filter": {
                    "shortcode_strip": {
                        "type": "pattern_replace",
                        "pattern": SHORTCODE_PATTERN,
                        "replacement": " ",
                    }
                },
                "filter": {
                    "shingle": {"type": "shingle", "min_shingle_size": 2, "max_shingle_size": 3, "output_unigrams": True},
                    "synonyms_filter": {"type": "synonym", "lenient": True, "synonyms_path": "synonyms.txt"},
                    "arabic_stemmer": {"type": "stemmer", "language": "arabic"},
                    "arabic_stop": {"type": "stop", "stopwords": "_arabic_"},
                },
            },
        }
    }


def _make_mappings(non_indexed_fields, model=None):
    props = {field: {"type": "text", "index": False} for field in non_indexed_fields}
    props["hadithText"] = {
        "type": "text",
        "analyzer": "synonym",
        "fields": {"trigram": {"type": "text", "analyzer": "trigram"}},
    }
    props["arabicText"] = {"type": "text", "analyzer": "custom_arabic"}
    props["contentHash"] = {"type": "keyword", "index": False}
    if model:
        props[SEMANTIC_FIELD] = {
            "type": "semantic_text",
            "inference_id": model["inference_id"],
        }
    return {"properties": props}


def _rebuild_index(index_name, documents, non_indexed_fields, model=None):
    new_index = f"{index_name}-{int(time.time())}"
    timeout = BULK_REQUEST_TIMEOUT if model else 60
    es_client.indices.create(
        index=new_index,
        mappings=_make_mappings(non_indexed_fields, model),
        settings=_make_settings(),
    )
    success, errors = _bulk_index(documents, new_index, timeout=timeout)
    if success == 0:
        es_client.indices.delete(index=new_index, ignore_unavailable=True)
        return {"mode": "rebuild", "success_count": 0, "errors": errors}

    old_indices = []
    if es_client.indices.exists_alias(name=index_name):
        old_indices = list(es_client.indices.get_alias(name=index_name).keys())
    elif es_client.indices.exists(index=index_name):
        es_client.indices.delete(index=index_name)

    actions = [{"add": {"index": new_index, "alias": index_name}}]
    for old in old_indices:
        actions.append({"remove": {"index": old, "alias": index_name}})
    es_client.indices.update_aliases(actions=actions)
    for old in old_indices:
        es_client.indices.delete(index=old, ignore_unavailable=True)

    return {"mode": "rebuild", "success_count": success, "errors": errors}


def _incremental_index(index_name, documents, model=None):
    incoming = {doc["_id"]: doc for doc in documents}
    existing_hashes = {}
    for hit in helpers.scan(
        es_client, index=index_name, query={"_source": ["contentHash"]}, size=2000
    ):
        existing_hashes[hit["_id"]] = hit["_source"].get("contentHash")

    to_index = [doc for doc_id, doc in incoming.items()
                if existing_hashes.get(doc_id) != doc["contentHash"]]
    to_delete = [doc_id for doc_id in existing_hashes if doc_id not in incoming]
    actions = to_index + [{"_op_type": "delete", "_id": did} for did in to_delete]

    timeout = BULK_REQUEST_TIMEOUT if model else 60
    success, errors = 0, []
    if actions:
        success, errors = _bulk_index(actions, index_name, timeout=timeout)

    return {
        "mode": "incremental",
        "indexed": len(to_index),
        "deleted": len(to_delete),
        "unchanged": len(incoming) - len(to_index),
        "success_count": success,
        "errors": errors,
    }


def _index_one(index_name, documents, non_indexed_fields, model=None, force_rebuild=False):
    """Rebuild or incrementally update a single index."""
    if force_rebuild or not _index_is_incremental(index_name):
        return _rebuild_index(index_name, documents, non_indexed_fields, model)
    return _incremental_index(index_name, documents, model)


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/index", methods=["GET"])
def index():
    start = time.time()
    if request.args.get("password") != os.environ.get("INDEXING_PASSWORD"):
        return "Must provide valid password to index", 401

    target_model = request.args.get("model")  # index only this model when specified
    force_rebuild = _is_truthy(request.args.get("rebuild"))

    connection = pymysql.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE"),
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(
        """SELECT arabicURN as urn, collection, hadithNumber, hadithText as arabicText,
                    matchingEnglishURN, "ar" as lang, grade1 as grade FROM ArabicHadithTable"""
    )
    arabicHadiths = cursor.fetchall()

    arabicOnlyHadiths, matchingArabicHadiths = [], {}
    for h in arabicHadiths:
        if h["matchingEnglishURN"] == 0:
            arabicOnlyHadiths.append(h)
        else:
            matchingArabicHadiths[h["matchingEnglishURN"]] = h

    cursor.execute(
        """SELECT englishURN as urn, collection, hadithText,
                    matchingArabicURN, "en" as lang, grade1 as grade FROM EnglishHadithTable"""
    )
    englishHadiths = cursor.fetchall()
    for h in englishHadiths:
        if h["urn"] in matchingArabicHadiths:
            ar = matchingArabicHadiths[h["urn"]]
            h["arabicText"] = ar["arabicText"]
            h["arabicGrade"] = ar["grade"]
            h["hadithNumber"] = ar["hadithNumber"]

    connection.close()

    non_indexed = ["urn", "matchingArabicURN", "lang"]

    # Prepare IDs and content hashes. arabicHadiths is a superset of arabicOnlyHadiths
    # (same dict objects), so preparing arabicHadiths covers both.
    _prepare_documents(arabicHadiths)
    _prepare_documents(englishHadiths)

    # Lexical index: English + Arabic-only (avoids duplicate hits for paired hadiths).
    lexical_docs = englishHadiths + arabicOnlyHadiths

    # Semantic index: full multilingual corpus — every Arabic doc gets its Arabic text
    # embedded, every English doc gets its English text embedded. This lets a multilingual
    # model like text-embedding-3-small retrieve across both languages from one index.
    results = {}

    # Lexical index — built when no model is specified, or when model=lexical.
    if not target_model or target_model == "lexical":
        results["lexical"] = _index_one(LEXICAL_INDEX, lexical_docs, non_indexed,
                                         model=None, force_rebuild=force_rebuild)

    # Model indexes — skip entirely when model=lexical.
    models_to_index = (
        {}
        if target_model == "lexical"
        else {target_model: _ENABLED_MODELS[target_model]}
        if target_model and target_model in _ENABLED_MODELS
        else _ENABLED_MODELS
    )
    for model_key, model in models_to_index.items():
        if model.get("custom_knn"):
            results[model_key] = {"skipped": "pre-built index, use test scripts to index"}
            continue
        _ensure_inference_endpoint(model)
        if model.get("multilingual"):
            # Full corpus: every Arabic doc embeds Arabic text, every English doc embeds English.
            en_docs = [{**doc, SEMANTIC_FIELD: doc["hadithText"]} for doc in englishHadiths]
            ar_docs = [{**doc, SEMANTIC_FIELD: doc["arabicText"]} for doc in arabicHadiths]
            model_docs = en_docs + ar_docs
        else:
            # English-only — replicates colleague's original PR approach.
            model_docs = [{**doc, SEMANTIC_FIELD: doc["hadithText"]} for doc in englishHadiths]
        results[model_key] = _index_one(
            model["index"], model_docs, non_indexed, model=model, force_rebuild=force_rebuild
        )
        results[model_key]["failed"] = json.dumps(results[model_key].pop("errors"))

    if "lexical" in results:
        results["lexical"]["failed"] = json.dumps(results["lexical"].pop("errors"))

    results["arabic_only_count"] = len(arabicOnlyHadiths)
    results["timeInSeconds"] = round(time.time() - start, 1)
    return jsonify(results)


@app.route("/index/status", methods=["GET"])
def index_status():
    out = {}
    for index_name in [LEXICAL_INDEX] + [m["index"] for m in EMBEDDING_MODELS.values()]:
        try:
            r = es_client.search(index=index_name, size=0, track_total_hits=True)
            out[index_name] = {"indexed": True, "count": r["hits"]["total"]["value"]}
        except NotFoundError:
            out[index_name] = {"indexed": False}
    return jsonify(out)


# ── Search helpers ────────────────────────────────────────────────────────────

def get_suggest_query(field):
    return {
        "field": field, "size": 3, "gram_size": 3,
        "direct_generator": [{"field": field, "suggest_mode": "missing"}],
        "highlight": {"pre_tag": "<em>", "post_tag": "</em>"},
        "collate": {"query": {"source": {"match": {field: "{{suggestion}}"}}}, "prune": False},
    }


def get_suggest_block(query):
    return {
        "text": query,
        "english": {"phrase": get_suggest_query("hadithText.trigram")},
        "arabic": {"phrase": get_suggest_query("arabicText")},
    }


def build_semantic_query(query, filter_clauses):
    return {
        "bool": {
            "filter": filter_clauses,
            "must": [{"semantic": {"field": SEMANTIC_FIELD, "query": query}}],
        }
    }


def get_filter_from_args(args):
    filters = []
    if collection := args.getlist("collection"):
        filters.append({"terms": {"collection": collection}})
    if grade := args.getlist("grade"):
        filters.append({"terms": {"grade": grade}})
    return filters


def _resolve_mode(args):
    mode = args.get("mode", "lexical").lower()
    if mode not in SEARCH_MODES:
        mode = "lexical"
    if mode in SEMANTIC_MODES and not SEMANTIC_ENABLED:
        mode = "lexical"
    return mode


def _resolve_model_key(args):
    key = args.get("model")
    if key in _ENABLED_MODELS:
        return key
    return next(iter(_ENABLED_MODELS), None)


def malformed_query_response(exc):
    access_log.warning("malformed_query", extra={"request_id": getattr(g, "request_id", None), "detail": str(exc)})
    return jsonify({"error": "malformed query"}), 400


@app.route("/<language>/search", methods=["GET"])
def search(language):
    query = request.args.get("q")
    filters = get_filter_from_args(request.args)
    mode = _resolve_mode(request.args)
    model_key = _resolve_model_key(request.args) if mode in SEMANTIC_MODES else None
    model = _ENABLED_MODELS.get(model_key) if model_key else None
    search_index = model["index"] if model else LEXICAL_INDEX

    fields = ["hadithNumber^2", "hadithText", "arabicText", "collection^2"]

    def build_lexical(query_type):
        inner = {"query": query, "fields": fields}
        if query_type == "query_string":
            inner["type"] = "cross_fields"
        return {
            "function_score": {
                "query": {"bool": {"filter": filters, "must": [{query_type: inner}]}},
                "functions": [
                    {"filter": {"term": {"collection": name}}, "weight": w}
                    for name, w in COLLECTION_BOOSTS
                ],
                "score_mode": "sum",
                "boost_mode": "sum",
            }
        }

    if mode in SEMANTIC_MODES:
        access_log.info("semantic_search", extra={
            "request_id": getattr(g, "request_id", None),
            "mode": mode, "model": model_key, "query": query,
        })
        if model_key == "arabic-openai":
            return _arabic_openai_search(query, filters)
        if model_key == "english-openai":
            return _english_openai_search(query, filters)
        if model_key == "english-openai-large":
            return _english_openai_large_search(query, filters)
        if model_key == "arabic-openai-large":
            return _arabic_openai_large_search(query, filters)
        if model_key in ("multilingual-e5", "bge-m3", "qwen3-embed"):
            return _multilingual_shared_search(model_key, query, filters)
        if model_key == "mxbai":
            return _mxbai_search(search_index, query, filters)
        return _semantic_search(search_index, query, filters)

    # Lexical path
    kwargs = {
        "index": LEXICAL_INDEX,
        "from_": request.args.get("from", 0),
        "size": request.args.get("size", 10),
        "_source": {"excludes": [SEMANTIC_FIELD]},
        "highlight": {"number_of_fragments": 0, "fields": {"*": {}}},
        "suggest": get_suggest_block(query),
    }
    try:
        try:
            result = es_client.search(query=build_lexical("query_string"), **kwargs)
        except BadRequestError:
            result = es_client.search(query=build_lexical("simple_query_string"), **kwargs)
    except BadRequestError as e:
        return malformed_query_response(e)
    return jsonify(result.body)


def _semantic_search(search_index, query, filters):
    try:
        result = es_client.options(request_timeout=130).search(
            index=search_index,
            from_=int(request.args.get("from", 0)),
            size=int(request.args.get("size", 10)),
            query=build_semantic_query(query, filters),
            _source={"excludes": [SEMANTIC_FIELD]},
            suggest=get_suggest_block(query),
        )
    except BadRequestError as e:
        return malformed_query_response(e)
    return jsonify(result.body)


def _embed_arabic_query(query):
    """Embed query with text-embedding-3-small and L2-normalize."""
    resp = _openai_client.embeddings.create(model=_ARABIC_EMBED_MODEL, input=query)
    vec = np.array(resp.data[0].embedding, dtype=np.float32)
    norm = np.linalg.norm(vec)
    return vec / norm if norm > 0 else vec


def _top_clusters(centroids, query_vec, n=_TOP_N_CLUSTERS):
    """Return the n cluster IDs whose centroids are closest to query_vec."""
    scores = centroids @ query_vec  # cosine sims via dot on unit vectors
    return np.argsort(scores)[::-1][:n].tolist()


def _top_arabic_clusters(query_vec, n=_TOP_N_CLUSTERS):
    # Prefer translated-only centroids: avoids routing to Arabic-only collection clusters.
    # Falls back to all-hadith centroids if translated file not yet generated.
    cents = _ARABIC_TRANSLATED_CENTROIDS if _ARABIC_TRANSLATED_CENTROIDS is not None else _ARABIC_CENTROIDS
    return _top_clusters(cents, query_vec, n)


def _top_english_clusters(query_vec, n=_TOP_N_CLUSTERS):
    return _top_clusters(_ENGLISH_CENTROIDS, query_vec, n)


def _mxbai_search(search_index, query, filters):
    size = int(request.args.get("size", 10))
    dedup = not _is_truthy(request.args.get("show_dupes", "0"))
    fetch_size = size * 3 if dedup else size

    all_filters = [_CHAIN_REF_FILTER] + filters

    try:
        result = es_client.options(request_timeout=130).search(
            index=search_index,
            size=fetch_size,
            query=build_semantic_query(query, all_filters),
            _source={"excludes": [SEMANTIC_FIELD]},
        )
    except BadRequestError as e:
        return malformed_query_response(e)

    if dedup:
        deduped = _dedup_hits(result.body["hits"]["hits"], size)
        result.body["hits"]["hits"] = deduped
        result.body["hits"]["total"]["value"] = len(deduped)

    result.body["_meta"] = {"dedup": dedup}
    return jsonify(result.body)


def _english_openai_search(query, filters):
    size  = int(request.args.get("size", 10))
    dedup = not _is_truthy(request.args.get("show_dupes", "0"))

    t0        = time.perf_counter()
    query_vec = _embed_arabic_query(query)   # same model (text-embedding-3-small)
    embed_ms  = round((time.perf_counter() - t0) * 1000, 1)

    # Full HNSW over 48k English docs — no centroid pre-filter needed at this scale.
    fetch_size   = size * 3 if dedup else size
    base_filters = [_CHAIN_REF_FILTER] + filters
    knn_filter   = {"bool": {"must": base_filters}} if len(base_filters) > 1 else base_filters[0]

    try:
        result = es_client.options(request_timeout=30).search(
            index="english-openai",
            knn={
                "field": "embedding",
                "query_vector": query_vec.tolist(),
                "k": fetch_size,
                "num_candidates": min(fetch_size * 20, 1000),
                "filter": knn_filter,
            },
            size=fetch_size,
            _source={"excludes": ["embedding"]},
        )
    except BadRequestError as e:
        return malformed_query_response(e)

    if dedup:
        deduped = _dedup_hits(result.body["hits"]["hits"], size)
        result.body["hits"]["hits"] = deduped
        result.body["hits"]["total"]["value"] = len(deduped)

    result.body["_meta"] = {"embed_ms": embed_ms, "dedup": dedup}
    return jsonify(result.body)


def _arabic_openai_search(query, filters):
    if _ARABIC_CENTROIDS is None and _ARABIC_TRANSLATED_CENTROIDS is None:
        return jsonify({"error": "arabic centroid index not loaded"}), 503

    size = int(request.args.get("size", 10))
    t0   = time.perf_counter()
    query_vec   = _embed_arabic_query(query)
    cluster_ids = _top_arabic_clusters(query_vec)
    embed_ms    = round((time.perf_counter() - t0) * 1000, 1)

    # Use clusterIdTranslated when available (translated-only centroids); else fall back.
    cluster_field  = "clusterIdTranslated" if _ARABIC_TRANSLATED_CENTROIDS is not None else "clusterIdFinal"
    cluster_filter = {"terms": {cluster_field: cluster_ids}}
    # Only return hadiths with an English translation.
    translated_filter = {"exists": {"field": "englishText"}}
    all_filters = [cluster_filter, translated_filter, _CHAIN_REF_FILTER] + filters
    knn_filter  = {"bool": {"must": all_filters}}

    try:
        result = es_client.options(request_timeout=30).search(
            index=ARABIC_OPENAI_INDEX,
            knn={
                "field": "embedding",
                "query_vector": query_vec.tolist(),
                "k": size,
                "num_candidates": min(size * 20, 500),
                "filter": knn_filter,
            },
            size=size,
            _source={"excludes": ["embedding"]},
        )
    except BadRequestError as e:
        return malformed_query_response(e)

    body = result.body
    body["_meta"] = {
        "clusters": cluster_ids,
        "cluster_field": cluster_field,
        "embed_ms": embed_ms,
    }
    return jsonify(body)


def _english_openai_large_search(query, filters):
    size  = int(request.args.get("size", 10))
    dedup = not _is_truthy(request.args.get("show_dupes", "0"))

    t0        = time.perf_counter()
    query_vec = _embed_openai_large(query)
    embed_ms  = round((time.perf_counter() - t0) * 1000, 1)

    fetch_size   = size * 3 if dedup else size
    base_filters = [_CHAIN_REF_FILTER] + filters
    knn_filter   = {"bool": {"must": base_filters}} if len(base_filters) > 1 else base_filters[0]

    cents = _NEW_MODEL_CENTROIDS.get("english-openai-large")
    if cents is not None:
        cluster_ids    = _top_clusters(cents, query_vec)
        cluster_filter = {"terms": {"clusterIdLarge": cluster_ids}}
        knn_filter     = {"bool": {"must": [cluster_filter] + base_filters}}

    try:
        result = es_client.options(request_timeout=30).search(
            index="english-openai-large",
            knn={
                "field": "embedding",
                "query_vector": query_vec.tolist(),
                "k": fetch_size,
                "num_candidates": min(fetch_size * 20, 1000),
                "filter": knn_filter,
            },
            size=fetch_size,
            _source={"excludes": ["embedding"]},
        )
    except NotFoundError:
        return jsonify({"error": "english-openai-large index not found — not yet indexed"}), 404
    except BadRequestError as e:
        return malformed_query_response(e)

    if dedup:
        deduped = _dedup_hits(result.body["hits"]["hits"], size)
        result.body["hits"]["hits"] = deduped
        result.body["hits"]["total"]["value"] = len(deduped)

    result.body["_meta"] = {"embed_ms": embed_ms, "dedup": dedup}
    return jsonify(result.body)


def _arabic_openai_large_search(query, filters):
    cents = _NEW_MODEL_CENTROIDS.get("arabic-openai-large")
    if cents is None:
        return jsonify({"error": "arabic-openai-large centroid index not loaded"}), 503

    size = int(request.args.get("size", 10))
    t0   = time.perf_counter()
    query_vec   = _embed_openai_large(query)
    cluster_ids = _top_clusters(cents, query_vec)
    embed_ms    = round((time.perf_counter() - t0) * 1000, 1)

    cluster_filter    = {"terms": {"clusterIdLarge": cluster_ids}}
    translated_filter = {"exists": {"field": "englishText"}}
    all_filters       = [cluster_filter, translated_filter, _CHAIN_REF_FILTER] + filters
    knn_filter        = {"bool": {"must": all_filters}}

    try:
        result = es_client.options(request_timeout=30).search(
            index="arabic-openai-large",
            knn={
                "field": "embedding",
                "query_vector": query_vec.tolist(),
                "k": size,
                "num_candidates": min(size * 20, 500),
                "filter": knn_filter,
            },
            size=size,
            _source={"excludes": ["embedding"]},
        )
    except NotFoundError:
        return jsonify({"error": "arabic-openai-large index not found — not yet indexed"}), 404
    except BadRequestError as e:
        return malformed_query_response(e)

    body = result.body
    body["_meta"] = {"clusters": cluster_ids, "embed_ms": embed_ms}
    return jsonify(body)


def _multilingual_shared_search(model_key, query, filters):
    size  = int(request.args.get("size", 10))
    dedup = not _is_truthy(request.args.get("show_dupes", "0"))

    t0        = time.perf_counter()
    query_vec = _embed_with_st(model_key, query)
    embed_ms  = round((time.perf_counter() - t0) * 1000, 1)

    fetch_size   = size * 3 if dedup else size
    base_filters = [_CHAIN_REF_FILTER] + filters

    cents = _NEW_MODEL_CENTROIDS.get(model_key)
    if cents is not None:
        cluster_ids    = _top_clusters(cents, query_vec)
        cluster_filter = {"terms": {"clusterIdShared": cluster_ids}}
        knn_filter     = {"bool": {"must": [cluster_filter] + base_filters}}
    else:
        knn_filter = {"bool": {"must": base_filters}} if len(base_filters) > 1 else base_filters[0]

    index_name = EMBEDDING_MODELS[model_key]["index"]
    try:
        result = es_client.options(request_timeout=60).search(
            index=index_name,
            knn={
                "field": "embedding",
                "query_vector": query_vec.tolist(),
                "k": fetch_size,
                "num_candidates": min(fetch_size * 20, 1000),
                "filter": knn_filter,
            },
            size=fetch_size,
            _source={"excludes": ["embedding"]},
        )
    except NotFoundError:
        return jsonify({"error": f"{index_name} index not found — not yet indexed"}), 404
    except BadRequestError as e:
        return malformed_query_response(e)

    if dedup:
        deduped = _dedup_hits(result.body["hits"]["hits"], size)
        result.body["hits"]["hits"] = deduped
        result.body["hits"]["total"]["value"] = len(deduped)

    result.body["_meta"] = {"embed_ms": embed_ms, "dedup": dedup, "model": model_key}
    return jsonify(result.body)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
