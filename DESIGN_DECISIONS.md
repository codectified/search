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
