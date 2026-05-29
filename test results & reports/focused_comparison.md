# Focused Comparison: "aisha" and "comparing yourself to others"

Three semantic models tested head-to-head.

| Model | Corpus | Pre-filter | Notes |
|---|---|---|---|
| arabic-openai | Arabic matn vectors | Centroid k=75 (translated-only, 44,896 docs) + `exists:englishText` | Cross-lingual; designed for Arabic queries |
| english-openai | English text vectors | Full HNSW (48,703 docs) | text-embedding-3-small, 1536-dim |
| mxbai | English text vectors | Full HNSW (48,703 docs) | mxbai-embed-large, 1024-dim, local/free |

---

## Query: *"aisha"*

**Overlaps:** arabic ∩ english = 0 | arabic ∩ mxbai = 0 | english ∩ mxbai = 0

### arabic-openai (wall=432ms | embed=412.6ms | clusters=[67, 50])

| # | Score | Hadith | Text |
|---|---|---|---|
| 1 | 0.693 | `nasai 2966` | Ibn Umar said: "When the Messenger of Allah arrived in Makkah he circumambulated the House seven times, then he prayed t |
| 2 | 0.689 | `bukhari 4752` | Narrated Ibn Abi Mulaika: I heard `Aisha reciting: "When you invented a lie (and carry it) on your tongues." (24.15) |
| 3 | 0.681 | `ahmad 37` | It was narrated from Muhammad bin Jubair bin Mut'im that 'Uthman said: I wish that I had asked the Messenger of Allah (ﷺ |
| 4 | 0.680 | `muslim 2307 c` | This hadith has been transmitted on the authority of Anas with a slight variation of wording. |
| 5 | 0.680 | `adab 489` | Abu'd-Duha said: "Masruq and Shutayr ibn Shakal met in the mosque. The people sitting in circles in the mosque moved tow |
| 6 | 0.678 | `muslim 1452 c` | Ahadith like this is transmitted by 'A'isha through another chain of narrators. |
| 7 | 0.678 | `muslim 555 b` | Sa'd b. Yazid Abu Mas'ama reported: I said to Anas like (that mentioned above). |
| 8 | 0.675 | `bukhari 2628` | Narrated Aiman: I went to `Aisha and she was wearing a coarse dress costing five Dirhams. `Aisha said, "Look up and see  |
| 9 | 0.671 | `bukhari 1641, 1642` | Narrated Muhammad bin `Abdur-Rahman bin Nawfal Al-Qurashi: I asked `Urwa bin Az-Zubair (regarding the Hajj of the Prophe |
| 10 | 0.670 | `bukhari 1983` | Narrated Mutarrif from `Imran Ibn Husain: That the Prophet asked him (Imran) or asked a man and `Imran was listening, "O |

### english-openai (wall=197ms | embed=179.0ms | full-index)

| # | Score | Hadith | Text |
|---|---|---|---|
| 1 | 0.785 | `bukhari 251` | Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house  |
| 2 | 0.784 | `abudawud 2758` | Narrated Aisha, Ummul Mu'minin: A woman would give security from the believers and it would be allowed. |
| 3 | 0.783 | `bukhari 92` | Narrated 'Aisha: that she prepared a lady for a man from the Ansar as his bride and the Prophet said, "O 'Aisha! Haven't |
| 4 | 0.782 | `bukhari 748` | Narrated Aisha: The people used to look forward for the days of my (`Aisha's) turn to send gifts to Allah's Apostle in o |
| 5 | 0.778 | `bukhari 24` | Narrated `Aisha: (the wife of the Prophet) A lady along with her two daughters came to me asking me (for some alms), but |
| 6 | 0.778 | `mishkat 3150` | ‘A’isha said: I had a girl of the Ansar whom I gave in marriage, and God's Messenger said, "Why do you not sing, ‘A’isha |
| 7 | 0.778 | `bukhari 815` | Narrated Aisha: Once the Prophet came to me while a man was in my house. He said, "O `Aisha! Who is this (man)?" I repli |
| 8 | 0.775 | `adab 613` | 'Ikrima heard 'A'isha, may Allah be pleased with her, say that she saw the Prophet, may Allah bless him and grant him pe |
| 9 | 0.772 | `mishkat 3224` | ‘A’isha told that when Sauda became old she said, “Messenger of God, I appoint to ‘A'isha the day you visit me” (Cf. the |
| 10 | 0.770 | `abudawud 4880` | Narrated Aisha, Ummul Mu'minin: Ibn Awn said: I asked about the meaning of intisar (revenge) in the Qur'anic verse: "But |

### mxbai (wall=579ms | full-index)

| # | Score | Hadith | Text |
|---|---|---|---|
| 1 | 0.850 | `bukhari 3894` | Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Ban |
| 2 | 0.847 | `bukhari 277` | Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rub |
| 3 | 0.845 | `abudawud 4164` | Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) |
| 4 | 0.844 | `bukhari 2661` | Narrated Aisha: (the wife of the Prophet) "Whenever Allah's Apostle intended to go on a journey, he would draw lots amon |
| 5 | 0.843 | `bukhari 1151` | Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house  |
| 6 | 0.842 | `bukhari 902` | Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts o |
| 7 | 0.842 | `bukhari 4573` | Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). H |
| 8 | 0.841 | `bukhari 43` | Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so a |
| 9 | 0.839 | `abudawud 3708` | Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays,  |
| 10 | 0.838 | `abudawud 288` | 'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wi |

---

## Query: *"comparing yourself to others"*

**Overlaps:** arabic ∩ english = 0 | arabic ∩ mxbai = 0 | english ∩ mxbai = 2

### arabic-openai (wall=372ms | embed=350.4ms | clusters=[74, 29])

| # | Score | Hadith | Text |
|---|---|---|---|
| 1 | 0.655 | `ibnmajah 1977` | It was narrated from Ibn 'Abbas that: the Prophet said: "The best of you is the one who is best to his wife, and I am th |
| 2 | 0.648 | `nasai 1130` | It was narrated that 'Aishah said: "I noticed the Messenger of Allah (SAW) was missing one night and I found him prostra |
| 3 | 0.647 | `abudawud 879` | ‘A’ishah said; one night I missed the Messenger of Allah (may peace be upon him) and when I sought him on the spot of pr |
| 4 | 0.647 | `nasai 169` | It was narrated from Abu Hurairah that 'Aishah said: "I noticed the Prophet (PBUH) was not there one night, so I started |
| 5 | 0.639 | `ahmad 957` | It was narrated from ‘Ali (رضي الله عنه) that The Messenger of Allah (ﷺ) used to say at the end of his Witr: `O Allah, I |
| 6 | 0.637 | `abudawud 5230` | Narrated AbuUmamah: The Messenger of Allah (saws) came out to us leaning on a stick. We stood up to show respect to him. |
| 7 | 0.637 | `ahmad 751` | It was narrated from `Ali (رضي الله عنه) that The Prophet (ﷺ) used to say at the end of his Witr `O Allah, I seek refuge |
| 8 | 0.636 | `nasai 813` | It was narrated from Anas that the Prophet (saws) used to say: "Make your rows straight, make your rows straight, make y |
| 9 | 0.635 | `ahmad 1295` | It was narrated from ‘Ali (رضي الله عنه) that The Prophet (ﷺ) used to say at the end of his Witr. “O Allah, I seek refug |
| 10 | 0.635 | `adab 942` | Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "When one of you yawns, he should  |

### english-openai (wall=197ms | embed=170.8ms | full-index)

| # | Score | Hadith | Text |
|---|---|---|---|
| 1 | 0.688 | `adab 328` | Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faults." |
| 2 ✓ | 0.687 | `riyadussalihin 466` | Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior t |
| 3 | 0.678 | `bukhari 497` | Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in propert |
| 4 | 0.666 | `muslim 7068` | Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a h |
| 5 | 0.664 | `adab 592` | Abu Hurayra said, "One of you looks at the mote in his brother's eye while forgetting the stump in his own eye." |
| 6 | 0.663 | `muslim 7070` | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than  |
| 7 | 0.663 | `bulugh 1514` | Ibn ’Umar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “He who imitates any people (in their actions) is  |
| 8 | 0.662 | `hisn 231` | If any of you praises his companion then let him say: Aḥsibu fulānan wallāhu ḥasībuh wa lā uzakkī `alallāhi aḥada. If an |
| 9 ✓ | 0.658 | `tirmidhi 2513` | Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to o |
| 10 | 0.656 | `bukhari 619` | Narrated Abu Huraira: Allah's Apostle said, "Not to wish to be the like of except the like of two men: a man whom Allah  |

### mxbai (wall=83ms | full-index)

| # | Score | Hadith | Text |
|---|---|---|---|
| 1 | 0.815 | `forty 18` | The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | `bukhari 6490` | Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in propert |
| 3 | 0.793 | `muslim 2963 a` | Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a h |
| 4 ✓ | 0.787 | `riyadussalihin 466` | Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior t |
| 5 | 0.785 | `muslim 2536` | 'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. |
| 6 | 0.782 | `abudawud 4092` | Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who li |
| 7 ✓ | 0.782 | `tirmidhi 2513` | Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to o |
| 8 | 0.781 | `adab 898` | Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and mad |
| 9 | 0.779 | `riyadussalihin 7` | Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does not look at your figu |
| 10 | 0.775 | `forty 19` | On the authority of Abu Abbas Abdullah bin Abbas (may Allah be pleased with him) who said: One day I was behind the Prop |

---

## Summary

| Query | Model | Top score | Top result | Clusters/Filter |
|---|---|---|---|---|
| aisha | arabic-openai | 0.693 | `nasai 2966` — Ibn Umar said: "When the Messenger of Allah arrived in Makkah he circu | [67, 50] |
| aisha | english-openai | 0.785 | `bukhari 251` — Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with  | full-HNSW |
| aisha | mxbai | 0.850 | `bukhari 3894` — Narrated Aisha: The Prophet engaged me when I was a girl of six (years | full-HNSW |
| comparing yourself to others | arabic-openai | 0.655 | `ibnmajah 1977` — It was narrated from Ibn 'Abbas that: the Prophet said: "The best of y | [74, 29] |
| comparing yourself to others | english-openai | 0.688 | `adab 328` — Ibn 'Abbas said, "When you want to mention your companion's faults, re | full-HNSW |
| comparing yourself to others | mxbai | 0.815 | `forty 18` — The felicitous person takes lessons from (the actions of) others. | full-HNSW |
