# Arabic Text Extraction Report

## What's Running

| Job | Status | Details |
|-----|--------|---------|
| `embed_e5_clean.py` — `vec_e5_matn` | **Running** | ~89k docs (hadMatnTag=True only) at ~3 docs/sec on CPU |
| `embed_e5_clean.py` — `vec_e5_full` | **Queued** | ~131k docs, starts automatically after matn finishes |
| `fix_clean_text_fields.py` | **Running** | Fixes word-boundary bug in `arabicTextClean` (see below) |

Estimated total embedding time: ~20 hours on CPU.

---

## Source Fields

Everything comes from the `arabic-openai` index (the original Arabic hadith data).

| Field | Type | Description |
|-------|------|-------------|
| `arabicText` | text | Full hadith in Arabic **with markup tags** (isnad + matn + commentary) |
| `arabicMatn` | text | Hadith body extracted from `arabicText`, may have inline markup |
| `hadMatnTag` | boolean | `true` if the source had explicit `[matn]...[/matn]` tags (reliable extraction) |
| `isChainRef` | boolean | `true` if this doc is chain-reference only (no substantive matn) |

---

## Markup Tag Types Found in arabicText

| Tag | Count | Purpose |
|-----|-------|---------|
| `[narrator]` / `[/narrator]` | 896,986 | Narrator name in isnad, with `id`, `role`, `tooltip` attributes |
| `[prematn]` / `[/prematn]` | 180,333 | Text before the matn (isnad block) |
| `[matn]` / `[/matn]` | 178,664 | Matn boundaries (present in ~89k docs) |
| `[postmatn]` / `[/postmatn]` | 40,383 | Text after matn (commentary, other narrations) |
| `[quran]` / `[/quran]` | 23,926 | Quranic verse reference |
| `[place]` / `[/place]` | 18,032 | Place name |
| `[verse]` / `[/verse]` | 9,831 | Verse reference |
| `[name]` / `[/name]` | 7,069 | Proper name |
| `[poem]` / `[/poem]` | 2,653 | Poetry |
| `[commentary]` / `[/commentary]` | 24 | Editorial commentary |

---

## hadMatnTag Coverage by Collection

| Collection | Total | hadMatnTag=True | hadMatnTag=False |
|------------|-------|-----------------|------------------|
| ibnabishayba | 37,240 | 36,427 (97.8%) | 813 |
| abdurrazzaq | 18,777 | 18,777 (100%) | 0 |
| hakim | 8,907 | 8,906 (100%) | 1 |
| ibnhibban | 7,651 | 7,651 (100%) | 0 |
| **muslim** | **7,459** | **0 (0%)** | **7,459** |
| bukhari | 7,277 | 7,023 (96.5%) | 254 |
| **nasai** | **5,768** | **0 (0%)** | **5,768** |
| mishkat | 5,319 | 0 | 5,319 |
| **abudawud** | **5,276** | **0 (0%)** | **5,276** |
| **ibnmajah** | **4,345** | **0 (0%)** | **4,345** |
| daraqutni | 4,263 | 4,263 (100%) | 0 |
| **tirmidhi** | **4,053** | **0 (0%)** | **4,053** |
| darimi | 3,406 | 3,406 (100%) | 0 |
| ibnkhuzayma | 2,879 | 2,879 (100%) | 0 |
| riyadussalihin | 1,896 | 0 | 1,896 |
| malik | 1,860 | 0 | 1,860 |
| bulugh | 1,767 | 0 | 1,767 |
| ahmad | 1,374 | 0 | 1,374 |
| adab | 1,326 | 0 | 1,326 |
| shamail | 402 | 0 | 402 |
| hisn | 268 | 0 | 268 |
| forty | 122 | 0 | 122 |
| virtues | 93 | 0 | 93 |
| **TOTAL** | **131,728** | **89,332 (67.8%)** | **42,396 (32.2%)** |

**Key insight:** The six major canonical collections (muslim, nasai, abudawud, ibnmajah, tirmidhi) and most smaller collections have zero matn tags. Only the musannaf-style collections (ibnabishayba, abdurrazzaq, daraqutni etc.) and ibnhibban/hakim used the tagging system.

---

## New Clean Fields

### `arabicMatnClean`
- **Source:** `arabicMatn` with all markup stripped
- **Only set for `hadMatnTag=True` docs** (89,332 docs)
- **NULL for `hadMatnTag=False` docs** — their matn extraction was unreliable
- **Used for:** `vec_e5_matn` embedding

### `arabicTextClean`
- **Source:** `arabicText` with all markup stripped
- **Set for all 131,728 docs**
- Contains isnad + matn + postmatn as continuous clean text
- **Used for:** `vec_e5_full` embedding

### Markup stripping rule
Tags are replaced with a **space** (not empty string) to preserve word boundaries:
```python
TAG_RE.sub(' ', text)  # then normalize whitespace
```
This prevents adjacent tags like `فِي[/prematn][matn]التَّمَاثِيلِ` from concatenating into `فِيالتَّمَاثِيلِ`.

---

## Before / After Examples

### Case 1: hadMatnTag=True — ibnabishayba (properly tagged, clean extraction)

**arabicText (raw):**
```
[prematn]حَدَّثَنَا أَبُو بَكْرٍ ، قَالَ : حَدَّثَنَا [narrator role="first"]عَبْدُ الرَّحِيمِ بْنُ سُلَيْمَانَ[/narrator] ،
عَنْ [narrator role="chain"]عَبْدِ الْمَلِكِ[/narrator] ، عَنْ [narrator role="chain"]عَطَاءٍ[/narrator] ، فِي
[/prematn][matn]التَّمَاثِيلِ , " مَا كَانَ مَبْسُوطًا يُوطَأُ وَيُبْسَطُ فَلا بَأْسَ بِهِ , وَمَا كَانَ يُنْصَبُ فَإِنِّي أَكْرَهُهَا "[/matn]
```

**arabicMatn (already extracted, may have inline markup):**
```
التَّمَاثِيلِ , " مَا كَانَ مَبْسُوطًا يُوطَأُ وَيُبْسَطُ فَلا بَأْسَ بِهِ , وَمَا كَانَ يُنْصَبُ فَإِنِّي أَكْرَهُهَا "
```

**arabicMatnClean** (→ vec_e5_matn):
```
التَّمَاثِيلِ , " مَا كَانَ مَبْسُوطًا يُوطَأُ وَيُبْسَطُ فَلا بَأْسَ بِهِ , وَمَا كَانَ يُنْصَبُ فَإِنِّي أَكْرَهُهَا "
```

**arabicTextClean** (→ vec_e5_full):
```
حَدَّثَنَا أَبُو بَكْرٍ ، قَالَ : حَدَّثَنَا عَبْدُ الرَّحِيمِ بْنُ سُلَيْمَانَ ، عَنْ عَبْدِ الْمَلِكِ ، عَنْ عَطَاءٍ ،
فِي التَّمَاثِيلِ , " مَا كَانَ مَبْسُوطًا يُوطَأُ وَيُبْسَطُ فَلا بَأْسَ بِهِ , وَمَا كَانَ يُنْصَبُ فَإِنِّي أَكْرَهُهَا "
```

---

### Case 2: hadMatnTag=False — tirmidhi (grade commentary contamination)

**arabicText (raw, no markup tags):**
```
حَدَّثَنَا قُتَيْبَةُ، حَدَّثَنَا عَبْدُ الْوَارِثِ بْنُ سَعِيدٍ ... قَالَ سَمِعْتُ رَسُولَ اللَّهِ صلى الله عليه وسلم
يَخْطُبُ يَقُولُ ‏"‏ مَنْ كَاتَبَ عَبْدَهُ عَلَى مِائَةِ أُوقِيَّةٍ ... فَهُوَ رَقِيقٌ ‏"‏ ‏.‏
قَالَ أَبُو عِيسَى هَذَا حَدِيثٌ غَرِيبٌ ‏.‏ وَالْعَمَلُ عَلَى هَذَا عِنْدَ بَعْضِ أَهْلِ الْعِلْمِ ...
```

**arabicMatn (BUGGED — includes grade commentary):**
```
‏"‏ مَنْ كَاتَبَ عَبْدَهُ ... فَهُوَ رَقِيقٌ ‏"‏ ‏.‏ قَالَ أَبُو عِيسَى هَذَا حَدِيثٌ غَرِيبٌ ‏.‏
```

**arabicMatnClean:** `null` — field is null because `hadMatnTag=False`

**arabicTextClean** (→ vec_e5_full):
```
حَدَّثَنَا قُتَيْبَةُ، حَدَّثَنَا عَبْدُ الْوَارِثِ ... قَالَ سَمِعْتُ رَسُولَ اللَّهِ صلى الله عليه وسلم
يَخْطُبُ يَقُولُ ‏"‏ مَنْ كَاتَبَ عَبْدَهُ ... فَهُوَ رَقِيقٌ ‏"‏ ‏.‏ قَالَ أَبُو عِيسَى هَذَا حَدِيثٌ غَرِيبٌ ‏.‏ ...
```

> Note: `arabicTextClean` for tirmidhi still includes the grade commentary because it's part of the full text. The matn boundary cannot be reliably extracted without tagging.

---

### Case 3: hadMatnTag=False — muslim (no markup, no tagging system)

Sahih Muslim uses no markup at all — `arabicText` is plain Arabic prose with isnad and matn undifferentiated:

**arabicText:**
```
حَدَّثَنَا مُحَمَّدُ بْنُ رَافِعٍ، حَدَّثَنَا عَبْدُ الرَّزَّاقِ ... عَنْ أَبِي هُرَيْرَةَ، عَنْ رَسُولِ اللَّهِ
صلى الله عليه وسلم ‏"‏ وَاللَّهِ لأَنْ يَلَجَّ أَحَدُكُمْ بِيَمِينِهِ فِي أَهْلِهِ آثَمُ لَهُ عِنْدَ اللَّهِ
مِنْ أَنْ يُعْطِيَ كَفَّارَتَهُ الَّتِي فَرَضَ اللَّهُ ‏"‏ ‏.‏
```

**arabicMatn** (heuristically extracted, no `[matn]` tag):
```
رَسُولُ اللَّهِ صلى الله عليه وسلم ‏"‏ وَاللَّهِ لأَنْ يَلَجَّ أَحَدُكُمْ ...
```

**arabicMatnClean:** `null`

**arabicTextClean** (→ vec_e5_full): full clean text identical to arabicText (no markup to strip)

> Muslim's `arabicMatn` looks reasonable in most cases (extracted from after the isnad), but without a tag we can't guarantee it's clean. `arabicTextClean` covers all Muslim hadiths for the full-text embedding.

---

## ⚠️ The Tirmidhi Grade Commentary Set — Future Work

**What we found:** ~977 hadiths at k=25 (cluster 12) formed an isolated outlier island in UMAP — completely separate from all other content. Every doc in this cluster had `arabicMatn` = `أَبُو عِيسَى هَذَا حَدِيثٌ حَسَنٌ صَحِيحٌ...` (Tirmidhi's grade commentary) instead of the actual prophetic text.

**Why it happened:** Tirmidhi hadiths end with `قَالَ` followed by Imam Tirmidhi's personal grade evaluation. When the `arabicMatn` boundary was not tagged, the extraction algorithm sometimes picked up only the grade commentary (starting at the final `قَالَ`) rather than the prophetic text.

**What `arabicTextClean` does:** For tirmidhi the full clean text is correct (isnad + hadith text + grade commentary all included). The grade commentary is still present at the end of `arabicTextClean` for tirmidhi docs, but now the actual hadith text is dominant.

**Future field needed: `scholarGrade`**

The `قَالَ أَبُو عِيسَى...` commentary contains valuable structured information:

- **Authenticity grade:** `حَسَنٌ صَحِيحٌ` (Hasan Sahih), `حَسَنٌ` (Hasan), `غَرِيبٌ` (Gharib), etc.
- **Cross-references:** `وَفِي الْبَابِ عَنْ...` (other narrators on this topic)
- **Transmission notes:** `وَقَدْ رُوِيَ مِنْ غَيْرِ وَجْهٍ` (narrated via multiple chains)

This commentary should be extracted into a separate field (e.g. `scholarGrade` or `tirmidiComment`) using a boundary rule: split on the pattern `‏.‏\s*قَالَ أَبُو عِيسَى` or `‏.‏\s*قَالَ` at the end of tirmidhi hadiths. This would:
1. Give us clean matn for tirmidhi without the grade appended
2. Preserve the grade commentary as a queryable/filterable field
3. Eliminate the semantic contamination in the `vec_e5_full` embeddings for tirmidhi

---

## Vector Fields

| Field | Dims | Source | Docs covered |
|-------|------|--------|--------------|
| `vec_e5_matn` | 1024 | `arabicMatnClean` | ~89,332 (hadMatnTag=True only) |
| `vec_e5_full` | 1024 | `arabicTextClean` | ~131,728 (all docs) |

Model: `intfloat/multilingual-e5-large` with `"passage: "` prefix.
