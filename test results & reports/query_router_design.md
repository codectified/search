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
    ├─ contains any Arabic Unicode character?
    │       → route: lexical  │  variant: arabic
    │
    └─ otherwise
            → route: mode (whatever ?mode= says, default lexical)
                    variant: None
```

### Detection code

```python
_ARABIC_RE = re.compile(r'[؀-ۿ]')

def _route_query(query, mode):
    q = query.strip()
    if len(q) >= 3 and q[0] == '"' and q[-1] == '"':
        return "lexical", "phrase", {"phrase_text": q[1:-1]}
    if _ARABIC_RE.search(q):
        return "lexical", "arabic", {}
    return mode, None, {}
```

Priority is absolute: Arabic text inside quotes (`"صلاة"`) routes to phrase, not Arabic.
An Arabic query with `?mode=semantic` still routes to `lexical_arabic`.

**Collection+number queries** (`bukhari 1`, `nasai 200`) fall through to standard lexical BM25. Both `hadithNumber^2` and `collection^2` are boosted fields in the cross-field query, and each collection carries an additional `function_score` weight, so the correct hadith reliably surfaces at or near rank 1. Misspellings (`bukahri 1`) degrade gracefully via BM25 rather than returning zero results.

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
| `lexical_phrase` | `match_phrase` on quoted query |
| `lexical_arabic` | Arabic analyser BM25 on `arabicText` |
| `lexical` | Standard cross-field BM25 with collection boosts (including collection+number queries) |
| `semantic` | Vector similarity via inference endpoint |

---

## What downstream branches add

This document covers what `feature/query-router` ships. Subsequent branches layer on additional features:

| Branch | Adds |
|--------|------|
| `feature/corpus-normalization` | `isChainRef: true` exclusion filter on all routes; `dupGroup` dedup in semantic; `gradeNorm` normalisation backfill |
| `feature/facets` | `gradeNorm` and `collection` facet aggregations on all routes; `?gradeNorm=` filter param |

The ES query examples above are accurate for this branch only. With corpus-normalization merged, every query gains a `must_not: {term: {isChainRef: true}}` clause. With facets merged, all routes gain `aggs: {gradeNorm: …, collection: …}`.

---

## Production rollout

The router is a pure code change — no index rebuild required. The `english-mxbai` index is unchanged.

**Recommended steps:**

1. Deploy with `ROUTER_LOG=true` in `.env`. Every request emits a structured log line:
   ```json
   {
     "message": "router_decision",
     "query": "صلاة الليل",
     "mode_requested": "semantic",
     "route": "lexical_arabic",
     "variant": "arabic",
     "overridden": true
   }
   ```

2. Review a day of real queries. Focus on:
   - `overridden: true` — Arabic or phrase routing blocked a `?mode=semantic` request. Investigate if English-looking queries appear here.
   - `route: lexical_arabic` on queries that look English — a stray Arabic character in the input will trigger this.

3. If shadow sampling is enabled, `routing_decision` in `search_metrics` records the route for each sampled request alongside full result bodies.

4. Disable `ROUTER_LOG` once routing looks stable.

5. Rollback: redeploy previous image. Index is untouched; rollback is instant.

---

## Collection+number queries and BM25

`bukhari 1`, `nasai 200`, and similar queries are handled by standard lexical BM25. The cross-field query includes `hadithNumber^2` and `collection^2` as boosted fields, and each collection carries an additional `function_score` weight (Bukhari/Muslim: 3.5×, Nawawi 40/Riyad: 3.3×, etc.).

For specific numbers (e.g. `bukhari 7563`) this is highly precise — few docs in any collection have that exact number. For common numbers (`bukhari 1`) the collection boost keeps Bukhari ranked first even when "1" appears throughout `hadithText`. Misspellings (`bukahri 1`) fall through to the same BM25 path and return imperfect-but-non-empty results, which is strictly better than a dedicated filter path that returns zero on any mismatch.

An earlier design had a dedicated reference route (exact term filter). It was removed because:
- Misspellings silently returned zero results
- BM25 with field boosts is accurate enough for well-formed queries
- Fewer code paths means fewer edge cases to test and maintain

---

## Known limitations

| Issue | Impact | Status |
|-------|--------|--------|
| Dagger alef (`الرحمٰن`) not normalised | 0 results for that spelling | Known gap, not addressed |
| Single Arabic character routes to Arabic path | `aisha عائشة` goes Arabic even though intent may be English | Acceptable — Arabic tokens dominate intent |
| `query_string` → `simple_query_string` fallback is silent | Client can't tell which was used | Logged server-side |
| Multi-word collection names not handled | `abu dawud 1` or `ibn majah 1` go to standard BM25 (same as all other queries); BM25 field boosts still surface the right hadith near rank 1 | Acceptable — no silent zero-results |
