"""
Re-embeds the ~42k Arabic hadiths whose vectors were built from full arabicText
(isnad + matn). Uses arabicMatn from ES instead, which is already correctly extracted.

Works entirely in ES — does NOT load the 3.9GB arabic_matn_embeddings.json file.
Writes a lightweight checkpoint file so it can be resumed if interrupted.

Cost: ~42k × 50 tokens × $0.02/1M ≈ $0.04 USD

Run inside container:
    docker exec search-web-1 python3 /code/tests/reembed_arabic_untagged.py
"""
import os, json, time
from openai import OpenAI
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan as es_scan, bulk

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
es = Elasticsearch(
    "http://172.31.250.10:9200",
    basic_auth=("elastic", os.environ["ELASTIC_PASSWORD"]),
    request_timeout=60,
)

MODEL      = "text-embedding-3-small"
INDEX      = "arabic-openai"
BATCH_SIZE = 200
CKPT_FILE  = "/code/reembed_untagged_done.json"  # lightweight: just {"doc_id": True}

# ── Load checkpoint (resumability) ────────────────────────────────────────────
if os.path.exists(CKPT_FILE):
    with open(CKPT_FILE) as f:
        done_ids = json.load(f)
    print(f"Resuming: {len(done_ids):,} already done")
else:
    done_ids = {}

# ── Scan ES for untagged hadiths ──────────────────────────────────────────────
print("Scanning ES for hadMatnTag=False hadiths...")
todo = []  # list of (doc_id, matn_text)

for hit in es_scan(
    es,
    index=INDEX,
    query={"query": {"term": {"hadMatnTag": False}}},
    _source=["arabicMatn", "arabicText"],
    size=500,
):
    doc_id = hit["_id"]
    if doc_id in done_ids:
        continue
    matn = (hit["_source"].get("arabicMatn") or "").strip()
    if not matn:
        matn = (hit["_source"].get("arabicText") or ".").strip()[:5000]
    todo.append((doc_id, matn[:5000]))

print(f"  {len(todo):,} remaining (skipped {len(done_ids):,} already done)")
est = len(todo) * 50
print(f"  Estimated cost: ~${est/1_000_000*0.02:.4f} USD")

# ── Embed + update ES in batches ──────────────────────────────────────────────
t0 = time.time()
embedded = api_errors = es_errors_total = 0

for i in range(0, len(todo), BATCH_SIZE):
    batch = todo[i:i + BATCH_SIZE]
    texts = [b[1] if b[1] else "." for b in batch]

    try:
        resp = client.embeddings.create(model=MODEL, input=texts)
    except Exception as e:
        print(f"  API ERROR batch {i//BATCH_SIZE}: {e}")
        api_errors += 1
        time.sleep(5)
        continue

    # Build bulk update actions
    actions = []
    for j, emb_obj in enumerate(resp.data):
        doc_id = batch[j][0]
        actions.append({
            "_op_type": "update",
            "_index":   INDEX,
            "_id":      doc_id,
            "doc":      {"embedding": emb_obj.embedding},
        })

    try:
        ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        es_errors_total += len(errs) if errs else 0
        for doc_id, _ in [(batch[j][0], None) for j in range(len(batch))]:
            done_ids[doc_id] = True
    except Exception as e:
        print(f"  ES BULK ERROR batch {i//BATCH_SIZE}: {e}")
        es_errors_total += 1

    embedded += len(batch)

    # Save checkpoint every 20 batches
    if (i // BATCH_SIZE) % 20 == 0:
        with open(CKPT_FILE, "w") as f:
            json.dump(done_ids, f)
        elapsed = time.time() - t0
        rate = embedded / elapsed if elapsed > 0 else 0
        rem  = (len(todo) - embedded) / rate if rate > 0 else 0
        print(f"  [{embedded:,}/{len(todo):,}] {rate:.0f}/s | ~{rem/60:.1f} min | api_err={api_errors} es_err={es_errors_total}")

# Final checkpoint save + ES refresh
with open(CKPT_FILE, "w") as f:
    json.dump(done_ids, f)
es.indices.refresh(index=INDEX)

elapsed = time.time() - t0
print(f"\nDone: {embedded:,} re-embedded in {elapsed:.0f}s")
print(f"API errors: {api_errors} | ES errors: {es_errors_total}")
print(f"Checkpoint: {CKPT_FILE} ({len(done_ids):,} entries)")
print("Next steps: re-run cluster_hadiths.py and cluster_arabic_translated.py")
