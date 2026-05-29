# Sunnah.com Knowledge Graph — Design Decisions Log

Significant architectural decisions, their reasoning, and trade-offs.
Add new entries at the top.

On the graph — proposed nomenclature for approval:

  Node labels:
  - Narrator — individual narrator (links to Narrators table)
  - Hadith — individual narration, carries both Arabic matn and English text as properties
  - Collection — Bukhari, Muslim, etc.
  - Book — Kitab al-Salat, etc.
  - Chapter — Bab
  - SemanticCluster — data-driven topic group (our k-means output)
  - TopicConcept — scholar-defined abstract node (you define these: Worship, Legal, Ethics…)

  Relationship types:
  - (Narrator)-[:NARRATED_FROM]->(Narrator) — student learned from teacher
  - (Narrator)-[:APPEARS_IN {role, position}]->(Hadith) — narrator is in this chain
  - (Hadith)-[:IN_COLLECTION]->(Collection)
  - (Hadith)-[:IN_BOOK]->(Book)
  - (Hadith)-[:IN_CHAPTER]->(Chapter)
  - (Hadith)-[:SIMILAR_TO {score}]->(Hadith) — cross-collection near-duplicate
  - (Hadith)-[:IN_CLUSTER]->(SemanticCluster)
  - (Book)-[:CATEGORIZED_AS]->(TopicConcept)
  - (TopicConcept)-[:SUBCONCEPT_OF]->(TopicConcept) — hierarchy within concepts

---

## 2026-05-28 — k=75 chosen as final cluster count

**k-sweep results** (v3 vectors, 131,728 hadiths, MiniBatchKMeans, random_state=42):

| k | Pairs>0.93 | Max sim | Cohesion | Median size |
|---|---|---|---|---|
| 50 | 2 | 0.936 | 0.624 | 2,531 |
| **75** | **2** | **0.932** | **0.638** | **1,635** |
| 100 | 7 | 0.947 | 0.639 | 1,158 |
| 125 | 4 | 0.966 | 0.648 | 1,007 |
| 150 | 12 | 0.952 | 0.652 | 872 |
| 175 | 9 | 0.955 | 0.661 | 770 |
| 200 | 9 | 0.951 | 0.665 | 673 |

**Finding:** The floor is 2 pairs above 0.93 — both k=50 and k=75 hit this floor. Those 2 pairs are irreducible: genuinely adjacent topics (e.g. related prayer sub-topics) that no k separates. From k=100 upward the count spikes to 7-12, meaning real over-splitting.

**Decision: k=75.** Rationale:
- Same pairs>0.93 as k=50 (the floor) — no benefit going lower
- Cohesion 0.638 — solid, well above the 0.60 floor
- Median cluster size 1,635 — large enough for meaningful two-stage pre-filtering
- Max centroid similarity 0.932 — the 2 close pairs are just barely above threshold, not the 0.975 crisis from v2
- Two-stage search speedup: top 2 centroids → ~3,270 docs vs 131k = **40x** reduction in search space

**Final artifacts:** `arabic_cluster_map_final.json`, `arabic_cluster_centroids_final.json`, `arabic_cluster_report_final.md`; `clusterIdFinal` field on all ES docs in `arabic-openai`.

---

## 2026-05-28 — Cluster comparison: v2 (mixed isnad) vs v3 (clean matn)

**Setup:** Both runs used k=150 MiniBatchKMeans on the same 131,728 hadiths. The only difference is the vectors: v2 used full arabicText for the 30k untagged Sunan hadiths; v3 re-embedded those 30k using regex-extracted matn.

| Metric | v2 | v3 | Interpretation |
|---|---|---|---|
| Avg cohesion | 0.668 | 0.652 | ↓ slightly — isnad shared phrases provided false cohesion in v2 |
| Centroid pairs > 0.93 | 38 | **12** | ↓ 68% — near-duplicate over-splitting mostly resolved |
| Centroid pairs > 0.85 | 347 | 233 | ↓ 33% |
| Max centroid pair similarity | 0.975 | 0.952 | Former Sunan super-cluster dissolved |
| Centroid pairs > 0.75 | 1,835 | 2,105 | ↑ mild overlap — clusters now span wider content space |

**v2 problem (now fixed):** Clusters 14/49/107/34/95/25 all had centroids 0.94–0.97 similar to each other — k-means was fragmenting one topic into 6 clusters because the shared isnad text (`حَدَّثَنَا`, `عَنْ`, transmission vocabulary) pulled same-topic hadiths into slightly different vector positions depending on which isnad chain they used.

**v3 result:** Cross-collection mixing is working. Example: v3 cluster 76 (size 1,828, cohesion 0.667) = nasai(270) + ibnabishayba(258) + muslim(221) + tirmidhi + abudawud — 43% editorial tags, 56% regex-extracted. Same topic content from both primary Sunan and secondary collections now clustering together.

**Why lower cohesion is correct:** In v2, isnad shared phrases created false within-cluster similarity — hadiths in the same cluster because they used the same transmitters, not because they were about the same thing. In v3, cohesion reflects actual content similarity. A cluster of 0.652 cohesion with genuine content agreement is more useful than a cluster of 0.668 held together by transmission vocabulary.

**Centroid pairs for retrieval:** Pairs > 0.93 should be merged at query time — if a query matches centroid A, also search cluster B if sim(A,B) > 0.93. The 12 remaining pairs at this threshold are safe to treat as super-clusters. This is preferable to reducing k, which would make clusters too coarse.

---

## 2026-05-28 — Corpus state: what is clean vs. mixed (as of v2)

**Full corpus:** 131,728 Arabic hadiths (ArabicHadithTable) + 44,895 English hadiths (HadithTable, translations). Together ~176k but they share URNs — English rows are translations of Arabic rows, not separate hadiths.

**Vector quality breakdown by collection:**

| State | Collections | Count | English? | Notes |
|---|---|---|---|---|
| **Clean** — matn-only vector | ibnabishayba, abdurrazzaq, hakim, ibnhibban, daraqutni, darimi, ibnkhuzayma | ~83k | None | `[matn]` tag present, embedded clean |
| **Mostly clean** | bukhari | 7,277 | All | 97% tagged (7,023); 254 untagged |
| **Problematic** — isnad noise in vector | muslim, nasai, abudawud, ibnmajah, tirmidhi | 26,901 | All | 0% tagged; regex matn in text field but vector = full text |
| **Problematic** | ahmad, adab, shamail, malik | ~5k | Most | 0% tagged |
| **Acceptable** — no real isnad | mishkat, riyadussalihin, bulugh, hisn, forty, virtues | ~10k | Most | Selection books, content starts directly |

**The critical gap:** The 5 major Sunan collections (Muslim, Nasai, Abu Dawud, Ibn Majah, Tirmidhi) = 26,901 hadiths — the most-searched collections on sunnah.com, all with English translations, all with 0% matn tagging. These have the dirtiest v2 vectors.

**What v3 requires:** Re-embed the ~30k untagged Sunan hadiths using `matn_boundaries.json` (regex-extracted matn). Cost: ~$0.03. This would make the multilingual index clean across the full corpus.

---

## 2026-05-28 — Arabic matn tag coverage is editorial, not random

**Finding:** The 67%/33% matn tag split follows strict collection lines, not random coverage:

| Coverage | Collections |
|---|---|
| 97–100% tagged | ibnabishayba, abdurrazzaq, hakim, ibnhibban, daraqutni, darimi, ibnkhuzayma |
| 96% tagged | bukhari |
| 0% tagged | muslim, nasai, abudawud, ibnmajah, tirmidhi, riyadussalihin, mishkat, malik, ahmad, adab, shamail, hisn, forty, virtues, bulugh |

**Why:** The `[prematn]...[/prematn][matn]...[/matn]` and `[narrator id="..." role="..."]` markup is editorial work added by the sunnah.com team — it is not in the original source material. The secondary collections (ibnabishayba, abdurrazzaq, etc.) appear to have been processed first or more completely, while most of the major primary Sunan collections (Muslim, Nasai, Abu Dawud, Ibn Majah, Tirmidhi) have no structural markup yet.

**Consequence for v2 embeddings:** We are NOT splitting the corpus into two separate jobs by tag presence. Instead:
- Hadiths WITH `[matn]` tag → embed matn-only text (clean signal)
- Hadiths WITHOUT `[matn]` tag → embed full arabicText after stripping narrator markup (includes isnad noise)

Both go into the same `arabic_matn_embeddings.json` with a `had_matn_tag: true/false` flag, so downstream clustering can weight or filter accordingly.

**SemanticCluster versioning rationale:**
- `v0` — book-level centroids (follows existing scholarly taxonomy, not data-driven)
- `v1` — k=75 MiniBatchKMeans on English mxbai-embed-large, full `hadithText` (isnad+matn mixed, English only)
- `v2` — k=? MiniBatchKMeans on OpenAI text-embedding-3-small, Arabic text (`[matn]` where available, full text fallback, `had_matn_tag` flag preserved)

---

## 2026-05-28 — Using vectors to strip isnad from untagged hadiths

**Idea (proposed, not yet implemented):** The 89k hadiths with `[matn]` tags give us a labeled dataset: for each, we know exactly which text is isnad and which is matn. This can be used to teach a model to find the boundary in the 42k untagged hadiths.

**How it would work:**
1. Split each tagged hadith into sentences/clauses
2. Label each sentence: isnad (pre-matn) or matn (post-tag boundary)
3. Embed each sentence using text-embedding-3-small
4. The isnad sentences cluster together (all about transmission: حدثنا، أخبرنا، عن، قال)
5. The matn sentences cluster differently (about content: prayer, ethics, law, narrative)
6. Compute two centroids: `isnad_centroid` and `matn_centroid`
7. For untagged hadiths: split into sentences, embed each, find the transition point where similarity flips from isnad-like to matn-like — that's the cut

**Why this works conceptually:** The isnad has a universal semantic signature across all collections and translators — it is always about chains of authority and transmission verbs. The matn is about content. These are geometrically separable in embedding space even across languages (Arabic isnad and English "Narrated X:" both cluster together because they mean the same thing).

**Why not do it yet:** The v2 embeddings are document-level (one vector per hadith). Sentence-level segmentation requires per-sentence embeddings — a separate pass, more expensive, and not needed for the current clustering goals. Tag first, segment later.

**Alternative (simpler for English):** The English attribution line almost always ends at the first `<p>` tag or colon — collection-specific regex handles ~80% of cases. The vector approach is better for Arabic and for edge cases.

---

## 2026-05-28 — Al-Zuhri as the critical isnad bridge

**Finding from narrator hub analysis:** Muhammad ibn Shihab al-Zuhri (Gen 4, d. 124 AH) has the highest bridgeness score in the graph (331,662 = 501 teachers × 662 students). He is not just a high-volume narrator — he is a structural bridge. The Sahabah generation (Gen 1) narrated to a relatively small group of Tabi'un (Gen 2), who narrated to Tabi' al-Tabi'in (Gen 3). Al-Zuhri sits at Gen 4 and personally connected 501 earlier-generation scholars to 662 later scholars. Removing him would fragment enormous portions of the isnad graph.

**Why this matters for the graph:** Al-Zuhri is the highest-value node to index first — his ego network (immediate teachers + students) alone covers a significant fraction of the entire corpus. When building the narrator subgraph, start from him and expand outward.

**To watch for:** Other high-bridgeness narrators who are structural rather than just prolific. Sufyan al-Thawri (Gen 7, bridgeness 472,546) has an even higher raw score but that is partly inflated by having 677 teachers — he is a hub, not a pure bridge. Al-Zuhri's ratio of teachers to students (501:662) at an early generation is the more structurally significant pattern.

---

## 2026-05-28 — Arabic + OpenAI for cross-lingual semantic search

**Decision:** Use OpenAI `text-embedding-3-small` for Arabic matn embeddings (v2).

**Why OpenAI over local Ollama models for Arabic:**
- mxbai-embed-large is English-first — Arabic vectors are poor quality
- nomic-embed-text has some multilingual support but weak Arabic
- multilingual-e5-large via Ollama would be the local alternative but is not currently pulled
- text-embedding-3-small has strong Arabic support and the corpus (~130k hadiths × ~50 tokens avg) costs ~$0.13 total — negligible

**Cross-lingual retrieval without translation:** text-embedding-3-small is a truly multilingual model — an English query and an Arabic matn embed into the same 1536-dim space. A user querying "prayer times" in English will retrieve hadiths whose Arabic matn is about salat times, without any translation step. This is the correct architecture.

**Why not translate queries to Arabic:** Translation adds errors and latency. A multilingual embedding model handles this natively. Translation would only be preferable if using a monolingual Arabic-only model, which would require a separate English index anyway.

---

## 2026-05-28 — Single `Hadith` node for Arabic+English pair

**Decision:** Arabic and English versions of the same narration are stored as a single `Hadith` node with both as properties, not as two separate nodes.

**Why:** The `matchingArabicURN` / `matchingEnglishURN` linkage in `HadithTable` already treats them as one entity. Separate nodes would require a `TRANSLATION_OF` relationship traversal for every query that needs both languages. Most graph queries (narrator chains, cross-collection similarity, topic clustering) operate on the narration as a unit, not on the translation as distinct.

**Trade-off:** Hadiths with no English translation get an `englishURN = 0` and null English properties. This is acceptable — the secondary collections (ibnabishayba, abdurrazzaq, etc.) are largely untranslated anyway. If a full multilingual graph is needed later, the node can be split.

---

## 2026-05-28 — `NARRATED_FROM` direction: student → teacher

**Decision:** `(student)-[:NARRATED_FROM]->(teacher)` — the relationship reads in the direction of attribution ("Abu Hurairah narrated FROM the Prophet").

**Alternative considered:** `(teacher)-[:TAUGHT]->(student)` — knowledge flows teacher to student.

**Why student→teacher:** The natural query in hadith science is "who did X narrate from?" — tracing a chain backward toward the Prophet. With student→teacher direction, this is a simple outgoing traversal from any narrator. Most isnad analysis tools follow this convention. The `Narrators.teachers` field in the DB is also structured this way (each narrator lists who they learned from).

---

## 2026-05-28 — `SemanticCluster.clusterId` format

**Decision:** `"{version}:{k}:{index}"` e.g. `"v1:75:23"`

**Why:** Allows multiple clustering runs to coexist in the graph simultaneously without collision. Querying all v1 clusters: `MATCH (sc:SemanticCluster {version: "v1"})`. Comparing v1 vs v2 for the same hadith: `MATCH (h:Hadith)-[:IN_CLUSTER]->(sc) WHERE sc.version IN ["v1","v2"]`.
