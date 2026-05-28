"""
v3 embeddings: re-embeds the ~30k untagged Sunan hadiths using regex-extracted
matn from matn_boundaries.json instead of full isnad+matn text.

Updates both:
  - arabic_matn_embeddings.json (so future ES rebuilds use clean vectors)
  - arabic-openai ES index (patches the embedding field in-place)

Cost: ~30k × 50 tokens × $0.02/1M ≈ $0.03

Run inside container:
    docker exec search-web-1 python3 /code/tests/embed_v3_clean_matn.py
"""
import os, json, time
from openai import OpenAI
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

MODEL      = "text-embedding-3-small"
INDEX      = "arabic-openai"
BATCH_SIZE = 200
SLEEP      = 0.3
VEC_FILE   = "/code/arabic_matn_embeddings.json"
MATN_FILE  = "/code/matn_boundaries.json"

# ── Load existing vectors (to patch in-place) ──────────────────────────────────
print("Loading existing vectors...")
with open(VEC_FILE) as f:
    vectors = json.load(f)
print(f"  {len(vectors):,} existing vectors")

# ── Load matn boundaries ───────────────────────────────────────────────────────
print("Loading matn boundaries...")
with open(MATN_FILE, encoding="utf-8") as f:
    boundaries = json.load(f)
print(f"  {len(boundaries):,} extracted matns")

# ── Filter to hadiths that need re-embedding ───────────────────────────────────
# Only re-embed if: has a boundary extraction AND currently has had_matn_tag=False
todo = [
    (urn, entry["matn"])
    for urn, entry in boundaries.items()
    if urn in vectors and not vectors[urn]["had_matn_tag"]
]
print(f"  {len(todo):,} hadiths to re-embed")
est = len(todo) * 50
print(f"  Estimated cost: ~${est/1_000_000*0.02:.3f} USD")

# ── Embed in batches ───────────────────────────────────────────────────────────
t0 = time.time()
embedded = errors = 0

for i in range(0, len(todo), BATCH_SIZE):
    batch = todo[i:i + BATCH_SIZE]
    urns  = [b[0] for b in batch]
    texts = [b[1][:5000] if b[1] else "." for b in batch]

    try:
        resp = client.embeddings.create(model=MODEL, input=texts)
    except Exception as e:
        print(f"  ERROR batch {i//BATCH_SIZE}: {e}")
        errors += 1
        time.sleep(5)
        continue

    # Update in-memory vectors dict
    for j, emb_obj in enumerate(resp.data):
        vectors[urns[j]]["vector"] = emb_obj.embedding
        # had_matn_tag stays False — vector is now regex-matn, not tag-matn
        # but mark it as v3 so we know it's been improved
        vectors[urns[j]]["v3_clean"] = True

    embedded += len(batch)
    time.sleep(SLEEP)

    if (i // BATCH_SIZE) % 10 == 0:
        elapsed = time.time() - t0
        rate = embedded / elapsed if elapsed > 0 else 0
        rem = (len(todo) - embedded) / rate if rate > 0 else 0
        print(f"  [{embedded:,}/{len(todo):,}] {rate:.0f} docs/s | ~{rem/60:.1f} min | {errors} errors")

# ── Save updated vectors file ──────────────────────────────────────────────────
print(f"\nSaving updated vectors to {VEC_FILE}...")
with open(VEC_FILE, "w") as f:
    json.dump(vectors, f)
print("  Saved.")

# ── Update ES index with new vectors ──────────────────────────────────────────
print("Updating ES index with new vectors...")
batch_urns = [urn for urn, _ in todo]
es_updated = es_errors = 0

for i in range(0, len(batch_urns), 500):
    chunk = batch_urns[i:i + 500]
    actions = [
        {
            "_op_type": "update",
            "_index": INDEX,
            "_id": f"arabic:{urn}",
            "doc": {"embedding": vectors[urn]["vector"]},
        }
        for urn in chunk if urn in vectors and "v3_clean" in vectors[urn]
    ]
    try:
        ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        es_updated += ok
        if errs:
            es_errors += len(errs)
    except Exception as e:
        print(f"  ES ERROR chunk {i//500}: {e}")
        es_errors += 1

    if (i // 500) % 10 == 0:
        print(f"  ES update: [{es_updated:,}/{len(batch_urns):,}]")

es.indices.refresh(index=INDEX)

elapsed = time.time() - t0
print(f"\nDone: {embedded:,} re-embedded, {errors} API errors")
print(f"ES:   {es_updated:,} docs updated, {es_errors} ES errors")
print(f"Time: {elapsed:.0f}s")
