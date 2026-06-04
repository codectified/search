# Query Router — Design Document

## Problem

Before the router, every query went through a single code path regardless of its
nature. This caused three concrete problems:

1. **Collection + number queries** (`bukhari 1`, `nasai 200`) returned BM25 results
   ranked by term frequency — the correct hadith was usually in the top 10 but not
   always at rank 1, and irrelevant hadiths scored alongside it.

2. **Quoted phrases** (`"actions are by intention"`) were treated as unquoted BM25
   queries — the phrase was tokenised and each word competed independently, so
   results could match any subset of the words in any order.

3. **Arabic text** was processed by the English analyser — tokenised incorrectly,
   stemming broken, no Arabic-specific normalisation applied.

---

## How it works

`_route_query(query, mode)` runs once per request before any ES call. It inspects
the raw query string and returns a 3-tuple `(route, variant, extra)`. The `search()`
handler then branches on `route`.

Rules are applied **in strict priority order** — earlier rules always win:

```
query string
    │
    ├─ starts and ends with " " (≥3 chars)?
    │       → route: lexical  │  variant: phrase
    │
    ├─ matches <collection> <number>?
    │       → route: reference  │  extra: {collection, number}
    │
    ├─ contains any Arabic Unicode character?
    │       → route: lexical  │  variant: arabic
    │
    └─ otherwise
            → route: mode (whatever ?mode= says, default lexical)
                    variant: None
```

### Detection code

```python
_REF_RE   = re.compile(r'^(?P<coll>[a-z0-9]+)\s+(?P<num>\d+[a-z]?)$', re.I)
_ARABIC_RE = re.compile(r'[؀-ۿ]')

def _route_query(query, mode):
    q = query.strip()
    if len(q) >= 3 and q[0] == '"' and q[-1] == '"':
        return "lexical", "phrase", {"phrase_text": q[1:-1]}
    m = _REF_RE.match(q)
    if m:
        coll = _COLLECTION_ALIAS.get(m.group("coll").lower(), m.group("coll").lower())
        return "reference", None, {"collection": coll, "number": m.group("num")}
    if _ARABIC_RE.search(q):
        return "lexical", "arabic", {}
    return mode, None, {}
```

Priority is absolute: Arabic text inside quotes (`"صلاة"`) routes to phrase, not Arabic.
A collection+number query with `?mode=semantic` still routes to reference.

---

## Route: `reference`

**Triggered by:** A query that is exactly a recognised collection slug followed by
a space and a hadith number (optionally with a letter suffix: `59a`).

**Examples:** `bukhari 1`, `nasai 200`, `nawawi40 1`, `bulugh 5a`

**Collection aliases:** `nawawi40` and `nawawi` resolve to `forty` (the actual DB
slug). Recognised slugs: bukhari, muslim, nasai, abudawud, tirmidhi, ibnmajah,
malik, ahmad, forty, riyadussalihin, bulugh, hisn, mishkat, darimi, ibnhibban,
baghawi, adab, shamail, virtues.

**ES query:** Pure `filter` — no scoring, no BM25.

Example for query `bukhari 1`:

```json
GET /english-mxbai/_search
{
  "size": 10,
  "query": {
    "bool": {
      "filter": [
        {"term": {"collection": "bukhari"}},
        {"term": {"hadithNumber": "1"}}
      ]
    }
  }
}
```

Example for query `nawawi40 13` (alias resolved, letter suffix):

```json
GET /english-mxbai/_search
{
  "query": {
    "bool": {
      "filter": [
        {"term": {"collection": "forty"}},
        {"term": {"hadithNumber": "13"}}
      ]
    }
  }
}
```

**Why no BM25:** A user typing `bukhari 1` wants exactly that hadith. Scoring would
introduce noise from other hadiths that match the token "1" across all collections.

**Response `_meta`:** `{"route": "reference"}`

**Facet aggs:** NOT included — reference results are a single known hadith, not a
search over a population.

---

## Route: `lexical` / variant `phrase`

**Triggered by:** Query wrapped in double quotes: `"actions are by intention"`.

**ES query:** `match_phrase` on both `hadithText` and `arabicText` (minimum one
must match). Requires all tokens to appear in order with no gaps.

Example for query `"actions are by intention"`:

```json
GET /english-mxbai/_search
{
  "query": {
    "bool": {
      "should": [
        {"match_phrase": {"hadithText": "actions are by intention"}},
        {"match_phrase": {"arabicText": "actions are by intention"}}
      ],
      "minimum_should_match": 1
    }
  }
}
```

**Why override mode:** A quoted query is an explicit user signal that word order
matters. Running it through a semantic model would ignore that signal and return
"similar" hadiths rather than exact-phrase matches.

**Response `_meta`:** `{"route": "lexical_phrase"}`

**Facet aggs:** Included — phrase results are a real search population.

---

## Route: `lexical` / variant `arabic`

**Triggered by:** Query contains any character in the Arabic Unicode block
(`U+0600–U+06FF`). A single Arabic character is enough — even a mixed query
like `aisha عائشة` routes here.

**ES query:** `match` on `arabicText` using the `custom_arabic` analyser.

Example for query `صلاة الليل`:

```json
GET /english-mxbai/_search
{
  "query": {
    "bool": {
      "must": [
        {"match": {"arabicText": {"query": "صلاة الليل", "analyzer": "custom_arabic"}}}
      ]
    }
  }
}
```

Example for mixed query `aisha عائشة` (Arabic chars present → Arabic route):

```json
GET /english-mxbai/_search
{
  "query": {
    "bool": {
      "must": [
        {"match": {"arabicText": {"query": "aisha عائشة", "analyzer": "custom_arabic"}}}
      ]
    }
  }
}
```

**Why BM25 over an Arabic semantic model:** Arabic semantic models (multilingual-e5,
arabic-openai) live in separate indexes and require a separate embed call. BM25
on a well-configured Arabic analyser is fast, exact, and covers morphological
variants well enough for Arabic text search. Multilingual semantic search is
planned as a parallel comparison path, not a replacement.

**All docs are searched:** Arabic-only (`lang:ar`) and bilingual (`lang:en`) hadiths
both have `arabicText` populated. No lang filter is applied — an Arabic query can
return any hadith in any language.

**Arabic analyser normalisation:** Handles alef variants (`أ/إ/آ` → `ا`), tatweel,
hamza, taa marbuta. Does NOT normalise dagger alef (`الرحمٰن`) — known gap,
not yet addressed.

**Response `_meta`:** `{"route": "lexical_arabic"}`

**Facet aggs:** Included.

---

## Route: `lexical` (standard BM25)

**Triggered by:** Any query that didn't match the three rules above.

**ES query:** Cross-field BM25 wrapped in `function_score` for collection boosts.
Tries `query_string` first (supports `AND`/`OR`/`-` operators); falls back to
`simple_query_string` if the query has syntax that `query_string` rejects.

Example for query `prayer at night`:

```json
GET /english-mxbai/_search
{
  "query": {
    "function_score": {
      "query": {
        "bool": {
          "must": [
            {"query_string": {
              "query": "prayer at night",
              "fields": ["hadithNumber^2", "hadithText", "arabicText", "collection^2"],
              "type": "cross_fields"
            }}
          ]
        }
      },
      "functions": [
        {"filter": {"term": {"collection": "bukhari"}},         "weight": 3.5},
        {"filter": {"term": {"collection": "muslim"}},          "weight": 3.5},
        {"filter": {"term": {"collection": "forty"}},           "weight": 3.3},
        {"filter": {"term": {"collection": "riyadussalihin"}},  "weight": 3.3},
        {"filter": {"term": {"collection": "mishkat"}},         "weight": 2.5},
        {"filter": {"term": {"collection": "malik"}},           "weight": 2.5},
        {"filter": {"term": {"collection": "ahmad"}},           "weight": 2.5},
        {"filter": {"term": {"collection": "tirmidhi"}},        "weight": 2.5},
        {"filter": {"term": {"collection": "ibnmajah"}},        "weight": 2.0},
        {"filter": {"term": {"collection": "darimi"}},          "weight": 2.0}
      ],
      "score_mode": "sum",
      "boost_mode": "sum"
    }
  }
}
```

**query_string → simple_query_string fallback:** If the query contains syntax that
`query_string` rejects (unmatched `"`, stray `(`, reserved operators in unexpected
positions), ES returns a 400. The handler catches this and retries with
`simple_query_string`, which is lenient. The fallback is logged server-side but not
exposed in `_meta`.

**Collection boosts:** Bukhari and Muslim are weighted 3.5×, Nawawi 40 / Riyad
3.3×, Mishkat / Malik / Ahmad / Tirmidhi 2.5×, Ibn Majah / Darimi 2.0×. These
lift authoritative collections above identical term matches in weaker ones.

**Response `_meta`:** `{"route": "lexical"}`

**Facet aggs:** Included.

---

## Route: `semantic`

**Triggered by:** `?mode=semantic` (or `hybrid`) in the request, AND the query
didn't match reference, phrase, or Arabic rules (those always override mode).

**ES query:** `semantic` query on the `semantic_text` field, which calls the
configured inference endpoint (Ollama → mxbai-embed-large) at query time.

Example for query `comparing yourself to others` with `?mode=semantic`:

```json
GET /english-mxbai/_search
{
  "query": {
    "bool": {
      "must": [
        {"semantic": {"field": "semantic_text", "query": "comparing yourself to others"}}
      ]
    }
  }
}
```

The `semantic` query type is handled by the ES inference plugin — it embeds the
query string at search time using the same model used at index time
(mxbai-embed-large via Ollama). No client-side embedding needed.

**Response `_meta`:** `{"route": "semantic"}`

**Facet aggs:** Not included on this branch. Added by the facets branch.

---

## `_meta.route` field

Every response includes `_meta.route`. Values:

| Value | Path |
|-------|------|
| `reference` | Direct filter lookup by collection + number |
| `lexical_phrase` | `match_phrase` on quoted query |
| `lexical_arabic` | Arabic analyser BM25 on `arabicText` |
| `lexical` | Standard cross-field BM25 with collection boosts |
| `semantic` | Vector similarity via inference endpoint |

---

## What downstream branches add

This document covers what `feature/query-router` ships. Subsequent branches layer on additional features:

| Branch | Adds |
|--------|------|
| `feature/corpus-normalization` | `isChainRef: true` exclusion filter on all routes; `dupGroup` dedup in semantic; `gradeNorm` normalisation backfill |
| `feature/facets` | `gradeNorm` and `collection` facet aggregations on all routes except reference; `?gradeNorm=` filter param |

The ES query examples above are accurate for this branch only. With corpus-normalization merged, every query gains a `must_not: {term: {isChainRef: true}}` clause. With facets merged, non-reference queries gain `aggs: {gradeNorm: …, collection: …}`.

---

## Production rollout

The router is a pure code change — no index rebuild required. The `english-mxbai` index is unchanged.

**Recommended steps:**

1. Deploy with `ROUTER_LOG=true` in `.env`. Every request emits a structured log line:
   ```json
   {
     "message": "router_decision",
     "query": "bukhari 1",
     "mode_requested": "lexical",
     "route": "reference",
     "variant": null,
     "overridden": true,
     "collection": "bukhari",
     "hadith_number": "1"
   }
   ```

2. Review a day of real queries. Focus on:
   - `overridden: true` — router chose a different path than `?mode=` asked for. Legitimate for reference/Arabic/phrase; investigate if English queries appear here.
   - `route: lexical_arabic` on queries that look English — a stray Arabic character in the input will trigger this.
   - Reference hits returning rank 1 for `bukhari N` style queries.

3. If shadow sampling is enabled, `routing_decision` in `search_metrics` records the route for each sampled request alongside full result bodies.

4. Disable `ROUTER_LOG` once routing looks stable.

5. Rollback: redeploy previous image. Index is untouched; rollback is instant.

---

## Reference route: comparison with BM25

The reference route was evaluated against straight BM25 across 15 collection+number queries (see `tests/report_query_router.py`). Key findings:

- **BM25 ranked the target hadith #1 on 9/15 queries** — it works most of the time due to collection and number fields being boosted.
- **Reference route returned the target hadith at #1 on 15/15 queries** by definition — it's a pure filter, no ranking ambiguity.
- **Where BM25 failed:** Short hadith numbers (`bukhari 1`, `ibnmajah 1`) matched too many docs — BM25 ranked a higher-scoring keyword match above the exact target. Numbers like `1` appear in hadithText frequently.
- **Conclusion:** Reference route is worth keeping. The cost is negligible (filter-only, no scoring), and it eliminates ranking uncertainty for an explicit lookup intent.

---

## Known limitations

| Issue | Impact | Status |
|-------|--------|--------|
| Dagger alef (`الرحمٰن`) not normalised | 0 results for that spelling | Known gap, not addressed |
| Single Arabic character routes to Arabic path | `aisha عائشة` goes Arabic even though intent may be English | Acceptable — Arabic tokens dominate intent |
| `query_string` → `simple_query_string` fallback is silent | Client can't tell which was used | Logged server-side |
| Reference path has no fuzzy match | `bukahri 1` returns nothing | Intentional — reference must be exact |
