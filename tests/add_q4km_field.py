"""
Adds mxbai-embed-large Q4_K_M GGUF vectors to the existing `small-model-eval` index.

Fills two new fields:
  vec_mxbai_q4km      1024-dim  mxbai-q4km Ollama model on hadithText
  vec_mxbai_q4km_matn 1024-dim  mxbai-q4km Ollama model on englishMatn

This is an incremental update — no index rebuild needed. Safe to re-run.

Prerequisites:
  - small-model-eval index populated
  - Ollama model `mxbai-q4km` registered:
      ollama create mxbai-q4km -f /tmp/mxbai-q4km.Modelfile
      (Modelfile: FROM /tmp/mxbai-q4km.gguf)
  - english_matn_map.json at /code/english_matn_map.json

Run inside container:
  docker exec search-web-1 python3 /code/tests/add_q4km_field.py
"""
import os, sys, json, time, urllib.request
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
ES_HOST    = "http://172.31.250.10:9200"
DEST_IDX   = "small-model-eval"
MATN_MAP   = "/code/english_matn_map.json"

BATCH_SIZE = 32
BULK_SIZE  = 200

es = Elasticsearch(ES_HOST, basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
                   request_timeout=60)

NEW_FIELDS = {
    "vec_mxbai_q4km":      {"type": "dense_vector", "dims": 1024, "index": True, "similarity": "cosine"},
    "vec_mxbai_q4km_matn": {"type": "dense_vector", "dims": 1024, "index": True, "similarity": "cosine"},
}


def ensure_mapping():
    existing = es.indices.get_mapping(index=DEST_IDX)[DEST_IDX]["mappings"]["properties"]
    new = {k: v for k, v in NEW_FIELDS.items() if k not in existing}
    if new:
        es.indices.put_mapping(index=DEST_IDX, properties=new)
        print(f"Added fields: {list(new.keys())}")
    else:
        print("Fields already in mapping.")


def is_filled(field):
    count = es.count(index=DEST_IDX, query={"exists": {"field": field}})["count"]
    total = es.count(index=DEST_IDX)["count"]
    if count > total * 0.95:
        print(f"  {field}: {count:,}/{total:,} — already filled, skipping.")
        return True
    print(f"  {field}: {count:,}/{total:,} — needs fill.")
    return False


def ollama_embed_batch(texts):
    payload = json.dumps({"model": "mxbai-q4km", "input": texts}).encode()
    req = urllib.request.Request(
        f"{OLLAMA_URL}/v1/embeddings",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        body = json.loads(r.read())
    data = sorted(body["data"], key=lambda x: x["index"])
    return [d["embedding"] for d in data]


def embed_and_fill(ids, texts, field):
    actions = []
    errors  = 0
    t0      = time.time()

    for i in range(0, len(texts), BATCH_SIZE):
        batch_ids   = ids[i : i + BATCH_SIZE]
        batch_texts = texts[i : i + BATCH_SIZE]
        try:
            vecs = ollama_embed_batch(batch_texts)
        except Exception as e:
            print(f"  Ollama error batch {i}: {e}")
            continue

        for doc_id, vec in zip(batch_ids, vecs):
            actions.append({
                "_op_type": "update",
                "_index":   DEST_IDX,
                "_id":      doc_id,
                "doc":      {field: vec},
            })

        if len(actions) >= BULK_SIZE:
            ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
            errors += len(errs)
            actions.clear()

        if i % (BATCH_SIZE * 100) == 0 and i > 0:
            elapsed = time.time() - t0
            rate    = i / elapsed
            eta     = (len(texts) - i) / rate if rate > 0 else 0
            print(f"  {i:,}/{len(texts):,} | {elapsed:.0f}s elapsed | ~{eta:.0f}s remaining")

    if actions:
        ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        errors += len(errs)

    filled = es.count(index=DEST_IDX, query={"exists": {"field": field}})["count"]
    print(f"  {field}: {filled:,} docs filled | {errors} errors | {time.time()-t0:.0f}s")


def run():
    ensure_mapping()

    # Collect all docs
    print("Collecting docs from small-model-eval ...")
    ids, had_texts, urns = [], [], []
    for hit in es_scan(es, index=DEST_IDX,
                       query={"query": {"match_all": {}}},
                       _source=["urn", "hadithText"], size=200):
        src = hit["_source"]
        ids.append(hit["_id"])
        had_texts.append(src.get("hadithText") or "")
        urns.append(str(src.get("urn", "")))
    print(f"  {len(ids):,} docs")

    # Load matn map
    print(f"Loading {MATN_MAP} ...")
    with open(MATN_MAP, encoding="utf-8") as f:
        raw = json.load(f)
    matn_texts = [raw.get(u, {}).get("matn", "") or h
                  for u, h in zip(urns, had_texts)]  # fallback to hadithText if matn missing

    # Fill hadithText field
    print(f"\n── vec_mxbai_q4km (hadithText) ──")
    if not is_filled("vec_mxbai_q4km"):
        embed_and_fill(ids, had_texts, "vec_mxbai_q4km")

    # Fill matn field
    print(f"\n── vec_mxbai_q4km_matn (englishMatn) ──")
    if not is_filled("vec_mxbai_q4km_matn"):
        embed_and_fill(ids, matn_texts, "vec_mxbai_q4km_matn")

    # Summary
    total = es.count(index=DEST_IDX)["count"]
    print("\nCoverage:")
    for field in NEW_FIELDS:
        c = es.count(index=DEST_IDX, query={"exists": {"field": field}})["count"]
        print(f"  {field:28s}  {c:>6,} / {total:,}")


if __name__ == "__main__":
    run()
