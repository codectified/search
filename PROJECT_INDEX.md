# sunnah.com — Project Index

**Status:** Active, low priority
**Purpose:** Improve search UX, query routing, semantic retrieval, and graph exploration.

*(Filed 2026-08-02, dictated by Omar. Full detail lives here per his own
"Master Hub Role" spec below — HQ's own tracking stays to a status/
priority/next-actions/blockers/latest-report/links summary, see
`C:\dev\hq\projects\sunnah-com-search\overview.md`.)*

## 1. Faceted Search Integration

Build two front-end implementations so the team can compare both approaches.

### Option A — Search-Triggered Facet Pills
**Preferred approach**

- Facet controls appear only after a search returns results.
- Display them as compact pill-like buttons near the results.
- Selecting a pill opens or applies available facet values, such as grade
  or other indexed metadata.
- Keeps facets visibly tied to the current result set.
- Keeps collection filtering separate from result facets.

**Rationale:** Collection selection defines which corpus or collections
are searched, while facets refine the results returned by that search.
Users will not usually need to manipulate both in the same way or at the
same stage.

### Option B — Facets Inside the Existing Filter Menu
**Alternative requested by the team**

- Add facet controls to the menu that currently contains collection filters.
- Keep them hidden until the user opens the filter menu.
- Clearly separate:
  - Collections / search scope
  - Result facets / refinement
- Avoid presenting collection selection as though it were simply another facet.

**Tradeoff:** This produces a cleaner initial interface, but makes result
refinement less visible and conflates two conceptually different
functions unless the menu is carefully divided.

### Deliverable

- Create separate branches or pull requests for both implementations.
- Include screenshots or a brief comparison of:
  - discoverability
  - interaction flow
  - mobile behavior
  - conceptual separation between search scope and result refinement

## 2. Query Router

- Verify whether the diacritic-fix pull request was merged and deployed.
- Confirm whether the router is still operating through ghost sampling.
- Review sampled queries, routing decisions, and failure cases.
- Produce a concise current-state evaluation.

## 3. Semantic Graph

Produce a report covering:

- models and architectures tested
- ontology and graph experiments
- retrieval approaches evaluated
- major findings and failures
- current recommended direction

## 4. Narrator Graph

- Source data is largely ready for ingestion.
- Main blocker is the lack of defined use cases.
- Identify concrete semantic questions and graph-native workflows before
  implementation.
- Consider possible alignment with Mindroots graph concepts.

## Master Hub Role

The Master Hub (HQ) should track only:

- current status
- priority
- next actions
- blockers
- latest report
- repository and pull-request links

Detailed implementation and research artifacts should remain in this
repository (`sunnah.com/search`), not in HQ.
