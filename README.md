# sunnah.com Search API

Flask + Elasticsearch search service for sunnah.com. Supports lexical (BM25) and semantic search.

---

## Query routing

Every query is classified before dispatch. The client-specified `mode` is overridden when the query shape makes the intent unambiguous:

| Query shape | Route | Example |
|---|---|---|
| Wrapped in double quotes | Lexical phrase (`match_phrase`) | `"angel of death"` |
| Collection slug + number | Direct reference lookup (`term` filter) | `bukhari 1`, `muslim 100a` |
| Multi-word Arabic | Arabic BM25 (`match` with `custom_arabic` analyzer) | `الصلاة في المسجد` |
| Everything else | Client `mode` (`semantic` or `lexical`) | `prayer at night` |

Phrase and reference routes always fire regardless of `mode`. Single Arabic words fall through to the client mode (semantic by default).

The `_meta` field in every response indicates which path was taken: `reference`, `lexical_phrase`, `lexical_arabic`, or absent for semantic/standard BM25.

---

## Semantic search filters (mxbai)

The mxbai semantic search path (`_mxbai_search`) applies two filters by default that are not active in lexical mode.

### Chain-reference filter

Some hadiths are **chain-reference entries** — they contain no actual hadith text (matn). They exist because Sahih Muslim records multiple transmission chains for the same hadith; each variant beyond the first looks like:

> *"This hadith has been narrated through another chain of transmitters..."*

These have no meaningful content, so they should never appear in search results. The filter is:

```json
{ "bool": { "must_not": { "term": { "isChainRef": true } } } }
```

**Why `must_not: true` rather than `term: false`?**
The `isChainRef` field is only stored on documents that were explicitly flagged. Documents without the field at all (the majority) don't have a stored `false` — they simply have no value. A `term: false` filter would exclude all of those. `must_not: true` correctly passes through both `false` docs and docs where the field is absent.

### Duplicate deduplication

~12,471 hadiths (~25.6%) belong to a **duplicate group** — the same matn narrated through different chains, or the same hadith appearing across multiple collections. Each group has a shared `dupGroup` integer ID (the smallest URN in the group).

By default, results are deduplicated: only the **most authoritative** representative of each group is shown.

**How the representative is chosen (`_dedup_hits`):**

1. Fetch `size × 3` results from ES (to have enough candidates after collapsing groups).
2. Walk all fetched hits. For each `dupGroup`, keep the hit with the highest `(collection_boost, score)` pair — collection authority first, vector similarity as tiebreaker:

   | Collection | Boost |
   |---|---|
   | Bukhari | 5.0 |
   | Muslim | 4.8 |
   | Nawawi 40 | 3.3 |
   | Nasai | 3.5 |
   | Abu Dawud | 3.0 |
   | *(others)* | 1.0–2.5 |

3. Singletons (no `dupGroup`) pass through unchanged.
4. Merge group representatives + singletons, re-sort by raw ES score, return top `size`.

This means if the same hadith appears in both Bukhari and a weaker collection, the Bukhari version is always shown — even if the weaker collection's version had a marginally higher vector similarity score.

**Accuracy caveat:** `dupGroup` is computed from mxbai vectors over `englishMatn`. Because isnad stripping is not 100% accurate for all collections (~14% of hadiths fall back to a weak heuristic or full text), a small number of groups may be wrong — either false positives (dissimilar hadiths grouped together due to shared isnad wording) or false negatives (true duplicates not caught). Treat the count as approximate until a manual validation pass is done.

**To bypass deduplication** (useful for inspection):
```
/english/search?q=...&mode=semantic&model=mxbai&show_dupes=1
```

### Size and HNSW traversal depth

The ES `semantic_text` field uses **HNSW approximate nearest-neighbor** internally. Requesting a larger `size` forces the HNSW graph walker to explore more of the graph, which can surface hadiths that a smaller traversal would miss.

Because dedup fetches `size × 3` candidates before collapsing, a `size=10` request actually searches over 30 candidates, while `size=20` searches over 60. The result sets can differ meaningfully — hadiths ranked 11–30 in the HNSW traversal at `size=10` may include better matches than the last few results at smaller sizes.

**Practical implication:** if you want to ensure high-quality top-10 results, passing `size=20` or `size=30` and letting dedup trim to 10 gives the HNSW graph more room to find the best candidates.

---

## Architecture

```
Browser / PHP website
        │
        ▼
  Flask API (this repo)
        │
        ├── query router (_route_query)
        │       ├── reference lookup  → english-mxbai (term filter)
        │       ├── phrase search     → english-mxbai (match_phrase)
        │       ├── Arabic BM25       → english-mxbai (custom_arabic analyzer)
        │       ├── semantic          → english-mxbai (mxbai kNN)
        │       └── standard BM25     → english-mxbai (cross_fields)
        │
        └── Elasticsearch
                └── english-mxbai
                        ├── BM25 paths use: hadithText (English, HTML-stripped)
                        │                  arabicText (Arabic, custom analyzer)
                        └── Semantic path uses: semantic_text (mxbai-embed-large, 1024-dim)
                                                embedded text: englishMatn (isnad-stripped)

  Ollama (runs on host, port 11434) — serves mxbai-embed-large
```

All query paths hit the same `english-mxbai` index. BM25 paths query the text fields; the semantic path queries the vector field. The index was intentionally built with both so a separate lexical-only index is not needed.

Each index name in ES is an **alias** (e.g. `english-mxbai`) pointing to a timestamped backing index. Reindexing builds a new backing index and atomically swaps the alias — the live index keeps serving traffic during the rebuild.

---

## Local development setup

### Prerequisites

- Docker + Docker Compose
- [Ollama](https://ollama.com) installed and running on your machine

### 1. Configure environment

```bash
cp .env.sample .env
```

Set `MXBAI_ENABLED=true` in `.env`. `OLLAMA_URL` defaults to `http://host.docker.internal:11434`, which works on Docker Desktop (Mac/Windows) — leave it unset locally.

### 2. Pull the model

```bash
ollama pull mxbai-embed-large
```

### 3. Start the stack

```bash
docker compose up --build
```

Flask is exposed on **port 5001**.

### 4. Build the indexes

```
http://localhost:5001/index?password=index123
```

This reads all hadiths from MySQL and builds both the lexical and mxbai indexes. Embedding ~48k English hadiths takes a few minutes.

To index only one at a time:
```
http://localhost:5001/index?password=index123&model=mxbai
http://localhost:5001/index?password=index123&model=lexical
```

To force a full rebuild instead of incremental:
```
http://localhost:5001/index?password=index123&rebuild=true
```

Check index status (doc counts):
```
http://localhost:5001/index/status
```

---

## Production deployment

Production uses `docker-compose.prod.yml` directly. Key differences from local:
- **No MySQL service** — connects to the existing external DB via env vars
- **uwsgi** instead of Flask dev server, exposed on **port 7650**
- **Persistent ES data** in a named Docker volume (`es-data`)
- **Explicit ES JVM memory limits** (`-Xms600m -Xmx1g`)

### 1. Configure environment

```bash
cp .env.sample .env
```

Fill in production values — at minimum:

```env
MYSQL_HOST=<prod db host>
MYSQL_USER=<user>
MYSQL_PASSWORD=<password>
MYSQL_DATABASE=hadithdb

ELASTIC_PASSWORD=<strong password>
INDEXING_PASSWORD=<strong password>

MXBAI_ENABLED=true
```

### 2. Ollama on Linux

Install [Ollama](https://ollama.com) on the host and pull the model before starting the stack:

```bash
ollama pull mxbai-embed-large
```

`host.docker.internal` only works on Docker Desktop (Mac/Windows), not on Linux. The prod compose file adds `host-gateway` so this hostname resolves correctly on Linux too — the default `OLLAMA_URL` works without any extra `.env` changes.

### 3. Start the stack

```bash
docker compose -f docker-compose.prod.yml up -d --build
```

### 4. Get the index onto prod

The `english-mxbai` index holds ~49k hadiths with pre-computed 1024-dim vectors. Building it from scratch requires Ollama running on the prod host and takes several hours on a t3.medium. There are two faster alternatives:

#### Option A — ES snapshot restore (preferred if transferring from another server)

Copies the raw Lucene segments — no re-embedding, no backfill scripts needed. The pre-computed inference chunks travel with the snapshot.

```bash
# On the source server (dev/staging):
# 1. Register a filesystem snapshot repository
curl -X PUT "http://localhost:9200/_snapshot/my_backup" \
  -H 'Content-Type: application/json' \
  -d '{"type":"fs","settings":{"location":"/usr/share/elasticsearch/snapshots"}}'

# 2. Take the snapshot
curl -X PUT "http://localhost:9200/_snapshot/my_backup/english-mxbai-snap?wait_for_completion=true" \
  -d '{"indices":"english-mxbai"}'

# 3. Copy snapshot files to prod (path must match the repo location in docker-compose.prod.yml)
rsync -avz /path/to/es-snapshots/ prod-server:/path/to/es-snapshots/

# On prod:
# 4. Register the same repo path, then restore
curl -X PUT "http://localhost:9200/_snapshot/my_backup"  \
  -d '{"type":"fs","settings":{"location":"/usr/share/elasticsearch/snapshots"}}'
curl -X POST "http://localhost:9200/_snapshot/my_backup/english-mxbai-snap/_restore"
```

After restore all index fields (`englishMatn`, `gradeNorm`, `dupGroup`, `isChainRef`) are already populated — no further steps needed.

#### Option B — Fresh index from MySQL + backfill + dedup

Use this if you are doing a clean production install without access to another server's data.

```bash
# 1. Build the index (embeds ~49k hadiths via Ollama — slow on t3.medium)
http://<server>:7650/index?password=<INDEXING_PASSWORD>&model=mxbai

# 2. Compute duplicate groups using the mxbai vectors (runs in ~2-3 min)
docker exec search-web-1 python3 /code/tests/dedup_mxbai.py

# 3. Backfill gradeNorm, englishMatn, isChainRef (self-contained, no external deps)
docker exec search-web-1 python3 /code/tests/backfill_prod_fields.py
```

`backfill_prod_fields.py` is safe to re-run — it skips docs where fields are already set.

Check index status:
```
http://<server>:7650/index/status
```

---

## Embedding model

| Key | Model | Served by | Dimensions |
|---|---|---|---|
| `mxbai` | mxbai-embed-large | Ollama (host) | 1024 |

mxbai runs via **Ollama on the host machine**, not inside Docker. The container reaches it at `http://host.docker.internal:11434`. Ollama exposes an OpenAI-compatible API, which ES 8.16's inference endpoint uses to embed queries and index documents.

### Adding a model

1. Add an entry to `EMBEDDING_MODELS` in `main.py` — copy the mxbai entry as a template (~8 lines).
2. Add `NEWMODEL_ENABLED=false` to `.env.sample`.
3. Pull the model: `ollama pull your-model-name`
4. Hit `/index?password=...&model=newmodel` to build its index.
5. Add the alias name to `SEMANTIC_INDEXES` in `tests/batch_search.py`.

---

## Search modes

| Mode | What it does |
|---|---|
| `lexical` | BM25 full-text search with collection boosts. Fast, exact keyword matching. Default. |
| `semantic` | Embedding similarity via HNSW approximate nearest-neighbor. Finds conceptually related hadiths even without keyword overlap. |

Mode is passed as a query parameter:
```
/english/search?q=prayer&mode=semantic&model=mxbai
/english/search?q=prayer&mode=lexical
```

---

## API endpoints

| Endpoint | Description |
|---|---|
| `GET /<language>/search?q=...` | Main search endpoint (consumed by PHP website) |
| `GET /index?password=...` | Build/rebuild ES indexes from MySQL |
| `GET /index/status` | Doc counts for all indexes |

### Search query parameters

| Parameter | Values | Default | Description |
|---|---|---|---|
| `q` | string | — | Search query |
| `mode` | `lexical`, `semantic` | `lexical` | Search mode |
| `model` | `mxbai` | — | Which semantic model (required when `mode=semantic`) |
| `size` | integer | 10 | Number of results to return |
| `show_dupes` | `0`, `1` | `0` | When `1`, bypass dedup and return all dup-group members unfiltered |
| `collection` | collection slug | — | Filter to a specific collection |
| `gradeNorm` | `Sahih`, `Hasan`, `Da'if`, `Maudu'`, `Uncategorized` | — | Filter by normalised grade (preferred) |
| `grade` | grade string | — | Filter by raw grade field (legacy fallback) |

---

## Docker Compose files

| File | When to use |
|---|---|
| `docker-compose.yml` | Local development. `docker compose up --build`. |
| `docker-compose.prod.yml` | Production. Run with `-f docker-compose.prod.yml`. Uses uwsgi, persistent ES data volume, explicit JVM memory limits, no MySQL service. |

**Why Elasticsearch has a fixed IP** (`172.31.250.10`): at high request rates, Docker's embedded DNS resolver becomes a bottleneck and throws `EAI_AGAIN` errors. Hardcoding the IP in `/etc/hosts` via `extra_hosts` makes every lookup instant.

**Observability services** (`es-exporter`, `alloy`) ship ES metrics and logs to Grafana Cloud. They require Grafana Cloud credentials in `.env` — if you don't have them, these services will fail to connect but won't break the rest of the stack.

---

## Batch evaluation

`tests/batch_search.py` runs a fixed set of queries across lexical and semantic and produces a CSV and markdown report for side-by-side comparison.

```bash
# Copy script into container, run it, copy results back
docker cp tests/batch_search.py search-web-1:/code/batch_search.py && \
docker exec search-web-1 python3 /code/batch_search.py && \
docker cp search-web-1:/code/batch_results.csv tests/batch_results.csv && \
docker cp search-web-1:/code/batch_report.md tests/batch_report.md
```

The script runs inside the container because ES is not exposed to the host — it's only reachable at `http://elasticsearch:9200` from within the Docker network.

Edit `QUERIES` in `tests/batch_search.py` to change which queries are tested.

**Note:** always use commas between query strings in the list. Python silently concatenates adjacent string literals without a comma, producing wrong queries with no error.

### Filter/dedup/size comparison report

`tests/mxbai_filter_report.py` runs a deeper comparison across three dimensions:
- **Chain-ref filter ON vs OFF** — shows how bare isnad hadiths pollute results without filtering
- **Dedup ON vs OFF** — shows which dup-group members get collapsed and which representative wins
- **Size effect** — shows how `size=5/10/20/50` changes which hadiths appear in the top-10

```bash
docker exec search-web-1 python3 /code/tests/mxbai_filter_report.py
docker cp search-web-1:"/code/test results & reports/mxbai_filter_report.md" "tests/mxbai_filter_report.md"
```
