# Sunnah.com Knowledge Graph — Schema v1

Graph database: Neo4j Aura (`NEO4J_URI` in `.env`)

---

## Node Labels

### `Hadith`
One node per narration. Arabic and English versions are properties on the same node,
linked by `matchingArabicURN` / `matchingEnglishURN` from `HadithTable`.

| Property | Type | Source | Notes |
|---|---|---|---|
| `arabicURN` | int, unique | `ArabicHadithTable.arabicURN` | Primary key |
| `englishURN` | int | `HadithTable.englishURN` | May be 0 if no English translation |
| `collection` | string | `HadithTable.collection` | e.g. "bukhari" |
| `hadithNumber` | string | `HadithTable.hadithNumber` | e.g. "1", "1657 c" |
| `arabicMatn` | string | extracted from `[matn]...[/matn]` in `arabicText` | null if no tag |
| `arabicText` | string | full `ArabicHadithTable.hadithText` | includes isnad markup |
| `englishText` | string | `HadithTable.englishText` | full text incl. attribution line |
| `gradeArabic` | string | `ArabicHadithTable.grade1` | e.g. "صحيح" |
| `gradeEnglish` | string | `HadithTable.englishgrade1` | e.g. "Sahih" |
| `hasMatnTag` | bool | derived | true if `[matn]` present in arabicText |
| `hasNarratorTags` | bool | derived | true if `[narrator]` tags present |
| `isnAdNarratorCount` | int | derived | number of `[narrator]` tags in chain |
| `xrefs` | string | `HadithTable.xrefs` | cross-references to other hadiths |

---

### `Narrator`
One node per person in the isnad chain. Rich biographical data.

| Property | Type | Source | Notes |
|---|---|---|---|
| `narratorId` | int, unique | `Narrators.narrator_id` | Primary key |
| `name` | string | `Narrators.name` | Arabic name |
| `altName` | string | `Narrators.alt_name` | |
| `kunya` | string | `Narrators.kunya` | e.g. "أبو هريرة" |
| `epithet` | string | `Narrators.epithet` | e.g. "الفاروق" |
| `generation` | int | `Narrators.generation` | 1=Sahabi, 2=Tabi'i, 3=Tabi' al-Tabi'in… |
| `reliabilityGrade` | int | `Narrators.reliability_grade` | numeric scale |
| `reliabilityLabel` | string | `Narrators.reliability_label` | e.g. "صحابي", "ثقة" |
| `deathYear` | string | `Narrators.death_year` | AH |
| `residence` | string | `Narrators.residence` | |
| `inBukhari` | bool | `Narrators.in_bukhari` | |
| `inMuslim` | bool | `Narrators.in_muslim` | |
| `narrationCount` | int | `Narrators.narration_count` | total narrations attributed |
| `prominenceScore` | float | `Narrators.prominence_score` | pre-computed centrality |
| `numSahih` | int | `Narrators.num_sahih` | |
| `numHasan` | int | `Narrators.num_hasan` | |
| `numDaeef` | int | `Narrators.num_daeef` | |
| `numMawdu` | int | `Narrators.num_mawdu` | |

---

### `Collection`
One node per hadith collection.

| Property | Type | Source |
|---|---|---|
| `name` | string, unique | `Collections.name` (e.g. "bukhari") |
| `englishTitle` | string | `Collections.englishTitle` |
| `arabicTitle` | string | `Collections.arabicTitle` |
| `type` | string | `Collections.type` (primary_collection / secondary_collection / selection) |
| `numHadith` | int | `Collections.numhadith` |
| `status` | string | `Collections.status` (complete / incomplete) |

---

### `Book`
One node per book (Kitab) within a collection.

| Property | Type | Source |
|---|---|---|
| `bookKey` | string, unique | `"{collection}:{ourBookID}"` |
| `collection` | string | |
| `ourBookID` | decimal | `BookData.ourBookID` |
| `englishBookNumber` | string | `BookData.englishBookNumber` |
| `englishName` | string | `BookData.englishBookName` |
| `arabicName` | string | `BookData.arabicBookName` |
| `hadithCount` | int | `BookData.totalNumber` |

---

### `Chapter`
One node per chapter (Bab) within a book.

| Property | Type | Source |
|---|---|---|
| `chapterKey` | string, unique | `"{collection}:{englishBookID}:{babID}"` |
| `collection` | string | |
| `englishBabNumber` | string | |
| `englishName` | string | `ChapterData.englishBabName` |
| `arabicName` | string | `ChapterData.arabicBabName` |

---

### `SemanticCluster`
Data-driven topic grouping from embedding clustering. Versioned so multiple
clustering runs can coexist.

| Property | Type | Notes |
|---|---|---|
| `clusterId` | string, unique | `"{version}:{k}:{cluster_index}"` e.g. `"v1:75:23"` |
| `version` | string | See versioning below |
| `k` | int | Number of clusters in this run |
| `clusterIndex` | int | 0-based index within run |
| `size` | int | Number of hadiths in cluster |
| `cohesion` | float | Avg cosine similarity of members to centroid |
| `topCollections` | string | JSON — collection distribution |

**Cluster version history:**

| Version | Embedding model | Text used | Notes |
|---|---|---|---|
| `v0` | mxbai-embed-large | Full `hadithText` (English) grouped by existing book | Book-level centroids — follows scholarly taxonomy |
| `v1` | mxbai-embed-large | Full `hadithText` (English, isnad+matn mixed) | k=75 cross-collection, English only, isnad noise present |
| `v2` | text-embedding-3-small (OpenAI) | Arabic `[matn]` only where available, full text fallback | Cross-collection, Arabic-first, matn-only where tagged (67% of corpus) |

---

### `TopicConcept`
Scholar-defined abstract category nodes. Manually curated.
Not yet populated — awaiting definition from Omar.

| Property | Type | Notes |
|---|---|---|
| `conceptId` | string, unique | slug e.g. "worship", "legal-transactions" |
| `label` | string | Human-readable e.g. "Worship & Ritual" |
| `labelArabic` | string | |
| `level` | int | 1 = top-level, 2 = sub-concept, etc. |

---

## Relationship Types

### `(Narrator)-[:NARRATED_FROM]->(Narrator)`
Teacher → student direction (knowledge flows from teacher to student, so student narrated FROM teacher).

| Property | Type | Source |
|---|---|---|
| (none yet) | | `Narrators.teachers` / `Narrators.students` adjacency lists |

---

### `(Narrator)-[:APPEARS_IN]->(Hadith)`
Narrator is part of this hadith's isnad chain.

| Property | Type | Notes |
|---|---|---|
| `role` | string | "sahabi", "chain", "first" — from `[narrator role="..."]` tag |
| `position` | int | 1-based position in chain |

---

### `(Hadith)-[:IN_COLLECTION]->(Collection)`

### `(Hadith)-[:IN_BOOK]->(Book)`

### `(Hadith)-[:IN_CHAPTER]->(Chapter)`

---

### `(Hadith)-[:SIMILAR_TO]->(Hadith)`
Cross-collection near-duplicate. Undirected in practice (both directions stored).

| Property | Type | Notes |
|---|---|---|
| `score` | float | Cosine similarity, 0.93–1.0 |
| `model` | string | Embedding model used e.g. "mxbai-embed-large" |

---

### `(Hadith)-[:IN_CLUSTER]->(SemanticCluster)`

| Property | Type | Notes |
|---|---|---|
| `version` | string | Matches `SemanticCluster.version` |

---

### `(Book)-[:IN_COLLECTION]->(Collection)`

### `(Chapter)-[:IN_BOOK]->(Book)`

### `(Book)-[:CATEGORIZED_AS]->(TopicConcept)`

### `(TopicConcept)-[:SUBCONCEPT_OF]->(TopicConcept)`

---

## Suggested Indexes

```cypher
CREATE CONSTRAINT hadith_arabic_urn IF NOT EXISTS FOR (h:Hadith) REQUIRE h.arabicURN IS UNIQUE;
CREATE CONSTRAINT narrator_id IF NOT EXISTS FOR (n:Narrator) REQUIRE n.narratorId IS UNIQUE;
CREATE CONSTRAINT collection_name IF NOT EXISTS FOR (c:Collection) REQUIRE c.name IS UNIQUE;
CREATE CONSTRAINT book_key IF NOT EXISTS FOR (b:Book) REQUIRE b.bookKey IS UNIQUE;
CREATE CONSTRAINT chapter_key IF NOT EXISTS FOR (ch:Chapter) REQUIRE ch.chapterKey IS UNIQUE;
CREATE CONSTRAINT cluster_id IF NOT EXISTS FOR (sc:SemanticCluster) REQUIRE sc.clusterId IS UNIQUE;
CREATE CONSTRAINT concept_id IF NOT EXISTS FOR (tc:TopicConcept) REQUIRE tc.conceptId IS UNIQUE;
CREATE INDEX hadith_collection IF NOT EXISTS FOR (h:Hadith) ON (h.collection);
CREATE INDEX narrator_generation IF NOT EXISTS FOR (n:Narrator) ON (n.generation);
CREATE INDEX narrator_reliability IF NOT EXISTS FOR (n:Narrator) ON (n.reliabilityGrade);
```
