# Grade Normalization and Search Facets

## Overview

Hadith grades in the database are inconsistently formatted — raw strings like
`"Sahih"`, `"صحيح"`, `"Hasan Sahih"`, `'[{"grade":"Da\'if","graded_by":"Al-Albani"}]'`,
or empty. The grade normalization pipeline converts all of these into one of five
canonical labels used for faceted filtering in search.

---

## 1. Raw Grade Data

The source of truth is the `grade1` column in `EnglishHadithTable` and
`ArabicHadithTable`. These are free-form strings entered by different contributors
over the years. Common shapes:

| Shape | Example |
|---|---|
| Plain English | `"Sahih"`, `"Da'if"`, `"Hasan"` |
| Arabic | `"صحيح"`, `"ضعيف"`, `"حسن"` |
| JSON array of objects | `[{"grade":"Sahih","graded_by":"Al-Albani"}]` |
| Compound | `"Hasan Sahih"`, `"Sahih (Darussalam)"` |
| Chain qualifier | `"Its chain is Sahih"` |
| Empty / null | — |

---

## 2. Normalization Process (`_normalize_grade`)

Called at **index time** (during `/index`), not at query time. The result is stored
as `gradeNorm` on each ES document alongside the raw `grade` field.

**Step-by-step:**

```
raw grade1 string
      │
      ▼
1. Bukhari / Muslim override
   → Always "Sahih" (their entire corpora are definitionally authenticated)
      │
      ▼
2. Empty / null check
   → "Uncategorized"
      │
      ▼
3. JSON extraction
   If raw starts with '[' or '{', extract the first "grade" value from the JSON.
   e.g. '[{"grade":"Da\'if","graded_by":"Al-Albani"}]' → "Da'if"
      │
      ▼
4. Strip parenthetical qualifiers
   "Sahih (Darussalam)" → "sahih"
   "Da'if (Al-Albani)" → "da'if"
      │
      ▼
5. Strip chain/isnad prefixes
   "Its chain is Sahih" → "sahih"
   "lts isnad is Hasan" → "hasan"
      │
      ▼
6. Exact map lookup (case-insensitive)
   "sahih" → "Sahih", "صحيح" → "Sahih"
   "muttafaqun 'alayh" → "Sahih"
   "hasan sahih" / "sahih hasan" → "Hasan"
   "qawi" → "Hasan"
   "munkar" / "shadh" / "shaz" → "Da'if"
   "maudu" / "fabricated" / "موضوع" → "Maudu'"
      │
      ▼
7. Prefix match (catches e.g. "sahih li ghayrihi")
   cleaned.startswith(key) → value
      │
      ▼
8. No match → "Uncategorized"
```

**Canonical output values:**

| Label | Meaning |
|---|---|
| `Sahih` | Authentic |
| `Hasan` | Good |
| `Da'if` | Weak |
| `Maudu'` | Fabricated |
| `Uncategorized` | Grade missing or unrecognized |

The `missing: "Uncategorized"` in the ES aggregation config also catches any documents
where the `gradeNorm` field was not indexed at all (e.g., from older partial indexes).

---

## 3. How Facets Work

### Index time

Every document in the search index has two grade fields:

```json
{
  "grade": "Hasan Sahih (Darussalam)",
  "gradeNorm": "Hasan"
}
```

`grade` preserves the original string for display; `gradeNorm` is the keyword field
used for filtering and aggregation.

### Aggregation config (`_FACET_AGGS`)

```python
_FACET_AGGS = {
    "gradeNorm": {
        "terms": {"field": "gradeNorm", "size": 10, "missing": "Uncategorized"},
    },
    "collection": {
        "terms": {"field": "collection.keyword", "size": 30},
    },
}
```

This is attached to every search request. ES returns both the result hits **and**
bucket counts for each grade and collection in the same response. The PHP website
reads `aggregations.gradeNorm.buckets` and renders one pill per bucket.

### UI rendering

Grade pills are ordered by a fixed editorial priority (Sahih → Hasan → Da'if →
Maudu' → Uncategorized), not by count. Clicking a pill adds `?gradeNorm=Sahih` to
the URL. Multiple grades can be selected simultaneously (multi-value `?gradeNorm=`).
The "All" pill clears the filter.

---

## 4. `post_filter` vs Query Filter

This is the critical design decision for faceted search. There are two places in ES
where a filter can live:

### Query filter (wrong for facets)

```
GET /index/_search
{
  "query": {
    "bool": {
      "filter": [{"terms": {"gradeNorm": ["Sahih"]}}],   ← filter here
      "must": [{"match": {"hadithText": "prayer"}}]
    }
  },
  "aggs": {"gradeNorm": {"terms": {"field": "gradeNorm"}}}
}
```

ES executes: **filter first, then aggregate over the filtered set.**

Result: only Sahih documents exist for the aggregation to count. The Hasan, Da'if,
Maudu', and Uncategorized buckets return empty — and the PHP renderer skips empty
buckets — so **all other grade pills disappear when one is selected.** The user sees
only their chosen filter pill with its count; all context is gone.

### `post_filter` (correct for facets)

```
GET /index/_search
{
  "query": {
    "bool": {
      "must": [{"match": {"hadithText": "prayer"}}]    ← no grade filter here
    }
  },
  "aggs": {"gradeNorm": {"terms": {"field": "gradeNorm"}}},
  "post_filter": {"terms": {"gradeNorm": ["Sahih"]}}   ← filter applied after aggs
}
```

ES executes in this order:
1. Run the text query, score all matching documents.
2. Run aggregations over **all matched documents** (grade filter not yet applied).
3. Apply `post_filter` to the hit list before returning it.

Result: aggregations always reflect the full query result set, so all grade buckets
have accurate counts regardless of which grade is selected. Hits are still filtered
correctly. The user can see "Sahih (4458), Hasan (444), Da'if (317)..." at all times,
giving them a complete picture of the result distribution before and after filtering.

### What does and doesn't use `post_filter`

| Filter type | Location | Rationale |
|---|---|---|
| `gradeNorm` / `grade` | `post_filter` | Facet filter — must not affect agg counts |
| `collection` | main query filter | Also a facet, but currently always-on; could move to post_filter if multi-select collection filtering is added |
| `isChainRef=False` | main query filter | Not a user-visible facet; always excluded |

---

## 5. Implementation Notes

- `grade_filter` (the gradeNorm/grade term filter) is separated from `filters`
  (collection + isChainRef) inside `get_filter_from_args()` and threaded through
  both `_execute_lexical_search` and `_execute_semantic_search` as a keyword arg.
- Shadow sampling does not forward `grade_filter` — the comparative telemetry
  is for ranking quality, not facet behavior.
- The PHP website also supports filtering by the raw `grade` field (`?grade=...`)
  as a legacy fallback, though the UI only exposes `gradeNorm`.
