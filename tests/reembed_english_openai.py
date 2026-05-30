"""
Re-embeds english-openai using extracted englishMatn (isnad-stripped) instead
of full hadithText. Reads english_matn_map.json, calls OpenAI API, updates the
embedding field in the english-openai ES index.

Cost: ~48k × 50 tokens × $0.02/1M ≈ $0.05 USD

Run inside container:
    docker exec search-web-1 python3 /code/tests/reembed_english_openai.py
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
INDEX      = "english-openai"
MAP_FILE   = "/code/english_matn_map.json"
CKPT_FILE  = "/code/reembed_english_openai_done.json"
BATCH_SIZE = 200

# ── Load extraction map ────────────────────────────────────────────────────────
print(f"Loading {MAP_FILE}...")
with open(MAP_FILE, encoding="utf-8") as f:
    matn_map = json.load(f)
print(f"  {len(matn_map):,} entries")

# ── Load checkpoint ────────────────────────────────────────────────────────────
if os.path.exists(CKPT_FILE):
    with open(CKPT_FILE) as f:
        done = json.load(f)
    print(f"  Resuming: {len(done):,} already done")
else:
    done = {}

# english-openai _id = raw urn string (no prefix)
todo = [(urn, entry["matn"] or entry.get("full_text","") or ".")
        for urn, entry in matn_map.items()
        if urn not in done]
print(f"  {len(todo):,} remaining")
est = len(todo) * 50
print(f"  Estimated cost: ~${est/1_000_000*0.02:.4f} USD")

# ── Embed + update ─────────────────────────────────────────────────────────────
t0 = time.time()
embedded = api_errors = es_errors_total = 0

for i in range(0, len(todo), BATCH_SIZE):
    batch = todo[i:i + BATCH_SIZE]
    texts = [b[1][:8000] if b[1] else "." for b in batch]

    try:
        resp = client.embeddings.create(model=MODEL, input=texts)
    except Exception as e:
        print(f"  API ERROR batch {i//BATCH_SIZE}: {e}")
        api_errors += 1
        time.sleep(5)
        continue

    actions = []
    for j, emb_obj in enumerate(resp.data):
        urn = batch[j][0]
        actions.append({
            "_op_type": "update",
            "_index":   INDEX,
            "_id":      urn,
            "doc":      {"embedding": emb_obj.embedding},
        })

    try:
        ok, errs = bulk(es, actions, raise_on_error=False, raise_on_exception=False)
        es_errors_total += len(errs) if errs else 0
        for urn, _ in [(b[0], None) for b in batch]:
            done[urn] = True
    except Exception as e:
        print(f"  ES BULK ERROR batch {i//BATCH_SIZE}: {e}")
        es_errors_total += 1

    embedded += len(batch)

    if (i // BATCH_SIZE) % 20 == 0:
        with open(CKPT_FILE, "w") as f:
            json.dump(done, f)
        elapsed = time.time() - t0
        rate    = embedded / elapsed if elapsed > 0 else 0
        rem     = (len(todo) - embedded) / rate if rate > 0 else 0
        print(f"  [{embedded:,}/{len(todo):,}] {rate:.0f}/s | ~{rem/60:.1f} min | api_err={api_errors} es_err={es_errors_total}")

with open(CKPT_FILE, "w") as f:
    json.dump(done, f)
es.indices.refresh(index=INDEX)

elapsed = time.time() - t0
print(f"\nDone: {embedded:,} in {elapsed:.0f}s | api_err={api_errors} | es_err={es_errors_total}")
