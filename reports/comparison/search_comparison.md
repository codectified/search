# Arabic kNN Search Comparison — Centroid-Filtered vs Straight

**Model:** OpenAI `text-embedding-3-small` | **Index:** `arabic-openai` | **k=20**

**Centroid pre-filter:** top 2 clusters ≈ 3,512 docs vs 131,728 full corpus

★ = result unique to that method (not in the other top-20)

`[ar-matn]` = Arabic matn shown (no English translation) · `[ar-full]` = full Arabic text (no matn tag)


## Summary

| Query | Embed ms | Centroid ES ms | Straight ES ms | Overlap/20 | Jaccard | Clusters |
|---|---|---|---|---|---|---|
| prayer times | 1541 | 114 | 16 | 20/20 | 1.0 | [9, 61] |
| comparing yourself to others | 365 | 30 | 17 | 5/20 | 0.143 | [66, 12] |
| zakah on wealth | 341 | 19 | 18 | 10/20 | 0.333 | [59, 31] |
| treatment of parents | 403 | 27 | 17 | 13/20 | 0.481 | [30, 37] |
| aisha | 157 | 33 | 18 | 5/20 | 0.143 | [39, 16] |

---

## "prayer times"

Embed: **1541ms** | Clusters selected: **[9, 61]** | Centroid ES: **114ms** | Straight ES: **16ms** | Overlap: **20/20** (Jaccard 1.0)

#### Centroid-filtered kNN

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.7331 | muslim | 612 e | C61 | ~ | 'Abdullah b. 'Amr b. al-'As reported: The Messenger of Allah (may peace be upon him) was asked about the times of prayers. He said: The time for the morning prayer (lasts) as long as the first visible part of the rising sun does not appear and the ti |
| 2 | 0.7294 | nasai | 522 | C61 | ~ | It was narrated from 'Abdullah bin 'Amr - and (one of the narrators) Shu'bah said: "Sometimes he (Qatadah, his teacher) narrated it as a Marfu' report and sometimes he did not" - "The time for Zuhr prayer is until 'Asr comes, and the time for 'Asr pr |
| 3 | 0.7174 | nasai | 642 | C9 | ~ | It was narrated from Anas that someone asked the Messenger of Allah (S.A.W) about the time of Subh. The Messenger of Allah (S.A.W) commanded Bilal to call the Adhan when dawn broke. Then the next day he delayed Fajr until it was very light, then he t |
| 4 | 0.7154 | daraqutni |  | C9 | ✓ | خَيْرُ الأَعْمَالِ الصَّلاةُ فِي أَوَّلِ وَقْتِهَا " `[ar-matn]` |
| 5 | 0.7148 | bukhari | 581 | C61 | ✓ | Narrated `Umar: "The Prophet forbade praying after the Fajr prayer till the sun rises and after the `Asr prayer till the sun sets." Narrated Ibn `Abbas: Some people told me the same narration (as above). |
| 6 | 0.7132 | nasai | 572 | C61 | ~ | Abu Yahya Sulaim bin 'Amir, Damrah bin Habib and Abu Talhah Nu'aim bin Ziyad said: "We heard Abu Umamah Al-Bahili say: 'I heard 'Amrah bin 'Abasah say: I said: 'O Messenger of Allah, is there any moment which brings one close to Allah than another, o |
| 7 | 0.7113 | abdurrazzaq |  | C61 | ✓ | عَنِ الصَّلاةِ فِي سَاعَتَيْنِ , بَعْدَ الْعَصْرِ حَتَّى تَغْرُبَ الشَّمْسُ , وَبَعْدَ الصُّبْحِ حَتَّى تَطْلُعَ الشَّمْسُ " `[ar-matn]` |
| 8 | 0.7112 | ibnabishayba |  | C9 | ✓ | " صَلُّوا الصَّلَاةَ لِوَقْتِهَا " `[ar-matn]` |
| 9 | 0.7103 | ibnmajah | 1249 | C61 | ~ | It was narrated from Abu Sa’eed Al-Khudri that the Prophet (saw) said: “There is no prayer after the ‘Asr until the sun has set, and there is no prayer after the Fajr until the sun has risen.” |
| 10 | 0.7101 | abudawud | 428 | C61 | ~ | Narrated Fudalah: The Messenger of Allah (saws) taught me and what he taught me is this: Observe the five prayers regularly. He said: I told (him): I have many works at these times; so give me a comprehensive advice which, if I follow, should be enou |
| 11 | 0.7101 | hakim |  | C61 | ✓ | " فَإِذَا صَلَّيْتَ الصُّبْحَ ، فَدَعِ الصَّلاةَ حَتَّى تَطْلُعَ الشَّمْسُ ، فَإِنَّهَا تَطْلُعُ لِقَرْنَيْ شَيْطَانٍ ، ثُمَّ صَلِّ فَالصَّلاةُ مُتَقَبَّلَةٌ حَتَّى تَسْتَوِيَ الشَّمْسُ عَلَى رَأْسِكَ كَالرُّمْحِ ، فَإِذَا كَانَتْ عَلَى رَأْسِكَ كَال `[ar-matn]` |
| 12 | 0.7090 | malik |  | C61 | ~ | ‏"‏ إِذَا بَدَا حَاجِبُ الشَّمْسِ فَأَخِّرُوا الصَّلاَةَ حَتَّى تَبْرُزَ وَإِذَا غَابَ حَاجِبُ الشَّمْسِ فَأَخِّرُوا الصَّلاَةَ حَتَّى تَغِيبَ ‏"‏ ‏.‏ `[ar-matn]` |
| 13 | 0.7080 | nasai | 518 | C61 | ~ | It was narrated from Nasr bin 'Abdur-Rahman, from his grandfather Mu'adh, that he performed Tawaf with Mu'adh bin 'Afra' but he did not pray. "I said: 'Are you not going to pray?' He said: 'The Messenger of Allah (PBUH) said: 'There is no prayer afte |
| 14 | 0.7067 | abdurrazzaq |  | C9 | ✓ | لا تَقْصُرِ الصَّلاةَ " `[ar-matn]` |
| 15 | 0.7067 | daraqutni |  | C9 | ✓ | أَفْضَلُ الْعَمَلِ الصَّلاةُ عَلَى وَقْتِهَا " `[ar-matn]` |
| 16 | 0.7062 | ahmad | 130 | C61 | ~ | It was narrated that Ibn 'Abbas said: Some righteous men, including ‘Umar - and the most righteous of them in my view was 'Umar - confirmed when I was present that the Messenger of Allah ﷺ said: `There is no prayer after Fajr until the sun rises and  |
| 17 | 0.7060 | ibnmajah | 1250 | C61 | ~ | It was narrated that Ibn ‘Abbas said: “Good men among whom was ‘Umar bin Khattab, and the best of them in my view is ‘Umar, testified before me that the Messenger of Allah (saw) said: ‘There is no prayer after Fajr until the sun has risen, and there  |
| 18 | 0.7049 | hakim |  | C9 | ✓ | " خَيْرُ الأَعْمَالِ الصَّلاةُ فِي أَوَّلِ وَقْتِهَا " `[ar-matn]` |
| 19 | 0.7045 | abdurrazzaq |  | C9 | ✓ | صَلُّوا كُلَّ صَلاةٍ لِوَقْتِهَا " `[ar-matn]` |
| 20 | 0.7044 | ibnhibban |  | C61 | ✓ | إِذَا صَلَّيْتَ الصُّبْحَ ، فَدَعِ الصَّلاةَ حَتَّى تَطْلُعَ الشَّمْسُ لِقَرْنِ الشَّيْطَانِ ، ثُمَّ صَلِّ وَالصَّلاةُ مُتَقَبَّلَةٌ حَتَّى تَسْتَوِيَ الشَّمْسُ عَلَى رَأْسِكَ كَالرُّمْحِ ، فَإِذَا كَانَتْ عَلَى رَأْسِكَ كَالرُّمْحِ فَدَعِ الصَّلاةَ  `[ar-matn]` |

#### Straight kNN (full index)

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.7331 | muslim | 612 e | C61 | ~ | 'Abdullah b. 'Amr b. al-'As reported: The Messenger of Allah (may peace be upon him) was asked about the times of prayers. He said: The time for the morning prayer (lasts) as long as the first visible part of the rising sun does not appear and the ti |
| 2 | 0.7294 | nasai | 522 | C61 | ~ | It was narrated from 'Abdullah bin 'Amr - and (one of the narrators) Shu'bah said: "Sometimes he (Qatadah, his teacher) narrated it as a Marfu' report and sometimes he did not" - "The time for Zuhr prayer is until 'Asr comes, and the time for 'Asr pr |
| 3 | 0.7174 | nasai | 642 | C9 | ~ | It was narrated from Anas that someone asked the Messenger of Allah (S.A.W) about the time of Subh. The Messenger of Allah (S.A.W) commanded Bilal to call the Adhan when dawn broke. Then the next day he delayed Fajr until it was very light, then he t |
| 4 | 0.7154 | daraqutni |  | C9 | ✓ | خَيْرُ الأَعْمَالِ الصَّلاةُ فِي أَوَّلِ وَقْتِهَا " `[ar-matn]` |
| 5 | 0.7148 | bukhari | 581 | C61 | ✓ | Narrated `Umar: "The Prophet forbade praying after the Fajr prayer till the sun rises and after the `Asr prayer till the sun sets." Narrated Ibn `Abbas: Some people told me the same narration (as above). |
| 6 | 0.7132 | nasai | 572 | C61 | ~ | Abu Yahya Sulaim bin 'Amir, Damrah bin Habib and Abu Talhah Nu'aim bin Ziyad said: "We heard Abu Umamah Al-Bahili say: 'I heard 'Amrah bin 'Abasah say: I said: 'O Messenger of Allah, is there any moment which brings one close to Allah than another, o |
| 7 | 0.7113 | abdurrazzaq |  | C61 | ✓ | عَنِ الصَّلاةِ فِي سَاعَتَيْنِ , بَعْدَ الْعَصْرِ حَتَّى تَغْرُبَ الشَّمْسُ , وَبَعْدَ الصُّبْحِ حَتَّى تَطْلُعَ الشَّمْسُ " `[ar-matn]` |
| 8 | 0.7112 | ibnabishayba |  | C9 | ✓ | " صَلُّوا الصَّلَاةَ لِوَقْتِهَا " `[ar-matn]` |
| 9 | 0.7103 | ibnmajah | 1249 | C61 | ~ | It was narrated from Abu Sa’eed Al-Khudri that the Prophet (saw) said: “There is no prayer after the ‘Asr until the sun has set, and there is no prayer after the Fajr until the sun has risen.” |
| 10 | 0.7101 | abudawud | 428 | C61 | ~ | Narrated Fudalah: The Messenger of Allah (saws) taught me and what he taught me is this: Observe the five prayers regularly. He said: I told (him): I have many works at these times; so give me a comprehensive advice which, if I follow, should be enou |
| 11 | 0.7101 | hakim |  | C61 | ✓ | " فَإِذَا صَلَّيْتَ الصُّبْحَ ، فَدَعِ الصَّلاةَ حَتَّى تَطْلُعَ الشَّمْسُ ، فَإِنَّهَا تَطْلُعُ لِقَرْنَيْ شَيْطَانٍ ، ثُمَّ صَلِّ فَالصَّلاةُ مُتَقَبَّلَةٌ حَتَّى تَسْتَوِيَ الشَّمْسُ عَلَى رَأْسِكَ كَالرُّمْحِ ، فَإِذَا كَانَتْ عَلَى رَأْسِكَ كَال `[ar-matn]` |
| 12 | 0.7090 | malik |  | C61 | ~ | ‏"‏ إِذَا بَدَا حَاجِبُ الشَّمْسِ فَأَخِّرُوا الصَّلاَةَ حَتَّى تَبْرُزَ وَإِذَا غَابَ حَاجِبُ الشَّمْسِ فَأَخِّرُوا الصَّلاَةَ حَتَّى تَغِيبَ ‏"‏ ‏.‏ `[ar-matn]` |
| 13 | 0.7080 | nasai | 518 | C61 | ~ | It was narrated from Nasr bin 'Abdur-Rahman, from his grandfather Mu'adh, that he performed Tawaf with Mu'adh bin 'Afra' but he did not pray. "I said: 'Are you not going to pray?' He said: 'The Messenger of Allah (PBUH) said: 'There is no prayer afte |
| 14 | 0.7067 | abdurrazzaq |  | C9 | ✓ | لا تَقْصُرِ الصَّلاةَ " `[ar-matn]` |
| 15 | 0.7067 | daraqutni |  | C9 | ✓ | أَفْضَلُ الْعَمَلِ الصَّلاةُ عَلَى وَقْتِهَا " `[ar-matn]` |
| 16 | 0.7062 | ahmad | 130 | C61 | ~ | It was narrated that Ibn 'Abbas said: Some righteous men, including ‘Umar - and the most righteous of them in my view was 'Umar - confirmed when I was present that the Messenger of Allah ﷺ said: `There is no prayer after Fajr until the sun rises and  |
| 17 | 0.7060 | ibnmajah | 1250 | C61 | ~ | It was narrated that Ibn ‘Abbas said: “Good men among whom was ‘Umar bin Khattab, and the best of them in my view is ‘Umar, testified before me that the Messenger of Allah (saw) said: ‘There is no prayer after Fajr until the sun has risen, and there  |
| 18 | 0.7049 | hakim |  | C9 | ✓ | " خَيْرُ الأَعْمَالِ الصَّلاةُ فِي أَوَّلِ وَقْتِهَا " `[ar-matn]` |
| 19 | 0.7045 | abdurrazzaq |  | C9 | ✓ | صَلُّوا كُلَّ صَلاةٍ لِوَقْتِهَا " `[ar-matn]` |
| 20 | 0.7044 | ibnhibban |  | C61 | ✓ | إِذَا صَلَّيْتَ الصُّبْحَ ، فَدَعِ الصَّلاةَ حَتَّى تَطْلُعَ الشَّمْسُ لِقَرْنِ الشَّيْطَانِ ، ثُمَّ صَلِّ وَالصَّلاةُ مُتَقَبَّلَةٌ حَتَّى تَسْتَوِيَ الشَّمْسُ عَلَى رَأْسِكَ كَالرُّمْحِ ، فَإِذَا كَانَتْ عَلَى رَأْسِكَ كَالرُّمْحِ فَدَعِ الصَّلاةَ  `[ar-matn]` |

---

## "comparing yourself to others"

Embed: **365ms** | Clusters selected: **[66, 12]** | Centroid ES: **30ms** | Straight ES: **17ms** | Overlap: **5/20** (Jaccard 0.143)

#### Centroid-filtered kNN

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.6645 | ibnhibban |  | C66 | ✓ | " لا تَسُبُّوا أَحَدًا مِنْ أَصْحَابِي ، فَإِِنَّ أَحَدَكُمْ لَوْ أَنْفَقَ مِثْلَ أُحُدٍ ذَهَبًا مَا أَدْرَكَ مُدَّ أَحَدِهِمْ وَلا نَصِيفَهُ " `[ar-matn]` |
| 2 | 0.6600 | abdurrazzaq |  | C66 | ✓ | إِذَا تَثَاوَبَ أَحَدُكُمْ فَلْيَضُمَّ مَا اسْتَطَاعَ " `[ar-matn]` |
| 3 | 0.6599 | darimi |  | C12 | ✓ | " إِذَا رَأَيْتُمْ الَّذِينَ يَتَّبِعُونَ مَا تَشَابَهَ مِنْهُ، فَاحْذَرُوهُمْ " `[ar-matn]` |
| 4 | 0.6565 | ibnhibban |  | C12 | ✓ | " خَيْرُكُمْ خَيْرُكُمْ لأَهْلِهِ ، وَأَنَا مِنْ خَيْرِكُمْ لأَهْلِي " `[ar-matn]` |
| 5 | 0.6542 | ibnhibban |  | C12 | ✓ | " إِِنِّي لأَنْظُرُ إِِلَى مَا وَرَائِي كَمَا أَنْظُرُ إِِلَى مَا بَيْنَ يَدَيَّ ، فَأَقِيمُوا صُفُوفَكُمْ ، وَحَسِّنُوا رُكُوعَكُمْ وَسُجُودَكُمْ " `[ar-matn]` |
| 6 ★ | 0.6416 | nasai | 516 | C66 | ~ | It was narrated from Abu Hurairah that the Prophet (PBUH) said: "If any one of you catches the first prostration of 'Asr prayer before the sun sets, let him complete his prayer, and if he catches up with the first prostration of Fajr prayer before th |
| 7 ★ | 0.6411 | ibnabishayba |  | C12 | ✓ | يَكْرَهُونَ أَنْ يَقُولَ أَحَدُهُمْ لِصَاحِبِهِ : أَسْبِقُكَ عَلَى أَنْ تَسْبِقَنِي , فَإِنْ سَبَقْتُكَ ، فَهُوَ لِي , وَإِلَّا كَانَ عَلَيْكَ , وَهُوَ الْقِمَارُ " `[ar-matn]` |
| 8 ★ | 0.6408 | abdurrazzaq |  | C12 | ✓ | يَرْكَعُ الْمَرْءُ حَاذِيًا قَدَمَيْهِ , يَفُوقُ إِحْدَاهُمَا الأُخْرَى ؟ , قَالَ : لا بَأْسَ بِذَلِكَ " `[ar-matn]` |
| 9 ★ | 0.6373 | ibnhibban |  | C66 | ✓ | " إِذَا صَلَّى أَحَدُكُمْ فِي الثَّوْبِ الْوَاحِدِ فَلْيُخَالِفْ بَيْنَ طَرَفَيْهِ عَلَى عَاتِقِهِ " `[ar-matn]` |
| 10 ★ | 0.6368 | nasai | 813 | C12 | ~ | It was narrated from Anas that the Prophet (saws) used to say: "Make your rows straight, make your rows straight, make your rows straight. By the One in Whose Hand is my soul! I can see you behind me as I can see you in front of me." |
| 11 ★ | 0.6352 | adab | 942 | C66 | ~ | Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "When one of you yawns, he should repress it as much as possible." |
| 12 ★ | 0.6339 | muslim | 632 b | C12 | ~ | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels take turns among you by night and by day, and the rest of the hadith is the same. |
| 13 ★ | 0.6338 | abdurrazzaq |  | C66 | ✓ | " إِذَا صَلَّى أَحَدُكُمْ فِي ثَوْبٍ وَاحِدٍ , فَلْيُخَالِفْ بَيْنَ طَرَفَيْهِ عَلَى عَاتِقِهِ " `[ar-matn]` |
| 14 ★ | 0.6337 | nasai | 3782 | C66 | ~ | It was narrated from 'Abdur-Rahman bin Samurah that the Messenger of Allah said: "If any one of you swears an oath, then he sees something better than it, let him offer expiation for his oath, and look at what is better and do it." |
| 15 ★ | 0.6331 | ibnmajah | 161 | C66 | ~ | It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Do not revile my Companions, for by The One in Whose Hand is my soul! If any one of you were to spend the equivalent of Mount Uhud in gold, it would not equal a Mudd spent by anyo |
| 16 ★ | 0.6327 | ahmad | 1398 | C66 | ~ | It was narrated from Moosa bin Talhah, from his father, that The Prophet (ﷺ) said: “Let one of you put something in front of him the height of the back of a saddle, then pray.` |
| 17 ★ | 0.6326 | ibnabishayba |  | C12 | ✓ | إِذَا أُذِنَ لِأَوَّلِكُمْ ، أُذِنَ لِآخِرِكُمْ " `[ar-matn]` |
| 18 ★ | 0.6319 | bukhari | 704 | C12 | ✓ | Narrated Abu Mas`ud: A man came and said, "O Allah's Apostle! I keep away from the morning prayer because so-and-so (Imam) prolongs it too much." Allah's Apostle became furious and I had never seen him more furious than he was on that day. The Prophe |
| 19 ★ | 0.6317 | ibnkhuzayma |  | C66 | ✓ | " إِذَا قَامَ أَحَدُكُمْ يُصَلِّي فَإِنَّهُ يَسْتُرُهُ إِذَا كَانَ بَيْنَ يَدَيْهِ مِثْلُ آخِرَةِ الرَّحْلِ " `[ar-matn]` |
| 20 ★ | 0.6316 | bukhari | 2559 | C66 | ✓ | Narrated Abu Huraira: The Prophet said, "If somebody fights (or beats somebody) then he should avoid the face." |

#### Straight kNN (full index)

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.6645 | ibnhibban |  | C66 | ✓ | " لا تَسُبُّوا أَحَدًا مِنْ أَصْحَابِي ، فَإِِنَّ أَحَدَكُمْ لَوْ أَنْفَقَ مِثْلَ أُحُدٍ ذَهَبًا مَا أَدْرَكَ مُدَّ أَحَدِهِمْ وَلا نَصِيفَهُ " `[ar-matn]` |
| 2 | 0.6600 | abdurrazzaq |  | C66 | ✓ | إِذَا تَثَاوَبَ أَحَدُكُمْ فَلْيَضُمَّ مَا اسْتَطَاعَ " `[ar-matn]` |
| 3 | 0.6599 | darimi |  | C12 | ✓ | " إِذَا رَأَيْتُمْ الَّذِينَ يَتَّبِعُونَ مَا تَشَابَهَ مِنْهُ، فَاحْذَرُوهُمْ " `[ar-matn]` |
| 4 ★ | 0.6580 | hakim |  | C16 | ✓ | " خَيْرُكُمْ خَيْرُكُمْ لأَهْلِي مِنْ بَعْدِي " `[ar-matn]` |
| 5 | 0.6565 | ibnhibban |  | C12 | ✓ | " خَيْرُكُمْ خَيْرُكُمْ لأَهْلِهِ ، وَأَنَا مِنْ خَيْرِكُمْ لأَهْلِي " `[ar-matn]` |
| 6 ★ | 0.6554 | ibnmajah | 1977 | C16 | ~ | It was narrated from Ibn 'Abbas that: the Prophet said: "The best of you is the one who is best to his wife, and I am the best of you to my wives." |
| 7 | 0.6542 | ibnhibban |  | C12 | ✓ | " إِِنِّي لأَنْظُرُ إِِلَى مَا وَرَائِي كَمَا أَنْظُرُ إِِلَى مَا بَيْنَ يَدَيَّ ، فَأَقِيمُوا صُفُوفَكُمْ ، وَحَسِّنُوا رُكُوعَكُمْ وَسُجُودَكُمْ " `[ar-matn]` |
| 8 ★ | 0.6532 | muslim | 2684 d | C16 | ~ | A hadith like this has been narrated on the authority of A'isha through another chain of transmitters. |
| 9 ★ | 0.6511 | muslim | 2540 | C23 | ~ | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Do not revile my Companions, do not revile my Companions. By Him in Whose Hand is my life, if one amongst you would have spent as much gold as Uhud it would not amount to as mu |
| 10 ★ | 0.6493 | abdurrazzaq |  | C6 | ✓ | تِبَاعًا " `[ar-matn]` |
| 11 ★ | 0.6493 | abdurrazzaq |  | C6 | ✓ | تِبَاعًا " `[ar-matn]` |
| 12 ★ | 0.6493 | abdurrazzaq |  | C6 | ✓ | تِبَاعًا " `[ar-matn]` |
| 13 ★ | 0.6482 | bukhari | 4547 | C24 | ✓ | Narrated `Aisha: Allah's Apostle recited the Verse:-- "It is He who has sent down to you the Book. In it are Verses that are entirely clear, they are the foundation of the Book, others not entirely clear. So as for those in whose hearts there is a de |
| 14 ★ | 0.6475 | nasai | 1130 | C64 | ~ | It was narrated that 'Aishah said: "I noticed the Messenger of Allah (SAW) was missing one night and I found him prostrating with the tops of his feet facing toward the Qiblah. I heard him saying: 'A'udhu biridaka min sakhatika, wa a'udhu bimu 'afati |
| 15 ★ | 0.6475 | abudawud | 879 | C64 | ~ | ‘A’ishah said; one night I missed the Messenger of Allah (may peace be upon him) and when I sought him on the spot of prayer I found him in prostration with his feet raised, and he was saying:”(O Allah), I seek refuge in Your good pleasure from Your  |
| 16 ★ | 0.6471 | mishkat | 4347 | C54 | ~ | He reported God’s messenger as saying, “He who copies any people is one of them.” Ahmad and Abu Dawud transmitted it. |
| 17 ★ | 0.6470 | nasai | 169 | C64 | ~ | It was narrated from Abu Hurairah that 'Aishah said: "I noticed the Prophet (PBUH) was not there one night, so I started looking for him with my hand. My hand touched his feet and they were held upright, and he was prostrating and saying: 'I seek ref |
| 18 ★ | 0.6449 | muslim | 2541 a | C23 | ~ | Abu Sa'id reported there was some altercation between Khalid b. Walid and Abd al-Rahman b. 'Auf and Khalid reviled him. Thereupon Allah's Messwger (may peace be upon him) said: None should revile my Companions. for if one amongst you were to spend as |
| 19 ★ | 0.6448 | ibnabishayba |  | C59 | ✓ | " لَا تَسُبُّوا أَصْحَابِي فَوَالَّذِي نَفْسِي بِيَدِهِ لَوْ أَنَّ أَحَدَكُمْ أَنْفَقَ مثل أُحُدٍ ذَهَبًا مَا أَدْرَكَ مُدَّ أَحَدِهِمْ وَلَا نَصِيفَهُ " `[ar-matn]` |
| 20 ★ | 0.6442 | nasai | 3614 | C63 | ~ | Abu Habibah At-Ta'i said: "A man made a will leaving some Dinars (to be spent) in the cause of Allah. Abu Ad-Darda' was asked about that, and he narrated that the Prophet said: 'The likeness of the one who frees a slave or gives some charity when he  |

---

## "zakah on wealth"

Embed: **341ms** | Clusters selected: **[59, 31]** | Centroid ES: **19ms** | Straight ES: **18ms** | Overlap: **10/20** (Jaccard 0.333)

#### Centroid-filtered kNN

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.7014 | ibnabishayba |  | C59 | ✓ | رَضَاعِ صَبِيٍّ فَجَعَلَ رَضَاعَهُ مِنْ مَالِهِ ، وَقَالَ لِوَلِيِّهِ : " لَوْ لَمْ يَكُنْ لَهُ مَالٌ ؛ لَجَعَلْنَا رَضَاعَهُ فِي مَالِكَ , أَلَا تَرَاهُ يَقُولُ : [quran sura="2" aya_start="233" aya_end="233"] وَعَلَى الْوَارِثِ مِثْلُ ذَلِكَ [/qura `[ar-matn]` |
| 2 | 0.6991 | ibnabishayba |  | C59 | ✓ | " فِي الْمَالِ حَقٌّ سِوَى الزَّكَاةِ " `[ar-matn]` |
| 3 | 0.6991 | ibnabishayba |  | C59 | ✓ | " فِي الْمَالِ حَقٌّ سِوَى الزَّكَاةِ " `[ar-matn]` |
| 4 | 0.6954 | ibnabishayba |  | C59 | ✓ | " زَكَاةُ أَمْوَالِكُمْ حَوْلٌ إلَى حَوْلٍ ، وَمَا كَانَ مِنْ دَيْنِ ثِقَةٍ فَزَكُّوهُ ، وَمَا كَانَ مِنْ دَيْنِ ظَنُونٍ فَلَا زَكَاةَ فِيهِ حَتَّى يَقْضِيَهُ صَاحِبُهُ " `[ar-matn]` |
| 5 | 0.6942 | malik |  | C59 | ~ | هُوَ الْمَالُ الَّذِي لاَ تُؤَدَّى مِنْهُ الزَّكَاةُ ‏.‏ `[ar-matn]` |
| 6 | 0.6917 | ibnabishayba |  | C59 | ✓ | لِي مَالًا فَإِلَى مَنْ أَدْفَعُ زَكَاتَهُ قَالَ : " ادْفَعْهَا إلَى هَؤُلَاءِ الْقَوْمِ " يَعني الْأُمَرَاءَ ، قُلْتُ : إذًا يَتَّخِذُونَ بِهَا ثِيَابًا وَطِيبًا قَالَ : " وَإِنِ اتَّخَذُوا ثِيَابًا وَطِيبًا ، وَلَكِنْ فِي مَالِكَ حَقٌّ سِوَى الزَّك `[ar-matn]` |
| 7 | 0.6883 | ibnmajah | 4130 | C59 | ~ | It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “The wealthiest will be the lowest on the Day of Resurrection, except those who do such and such with their money, and earn it from good sources.” |
| 8 | 0.6879 | abdurrazzaq |  | C59 | ✓ | الْمَالُ الْغَائِبُ أَفِيهِ زَكَاةٌ ؟ قَالَ : إِذَا لَمْ يَكُنْ ضُمَارًا أَوْ فِي تُوًى فَزَكِّهِ " `[ar-matn]` |
| 9 | 0.6864 | ibnabishayba |  | C59 | ✓ | إِضَاعَةِ الْمَالِ , قَالَ : أَنْ يَرْزُقَكَ اللَّهُ رِزْقًا ، فَتُنْفِقُهُ فِيمَا حَرَّمَ عَلَيْكَ " `[ar-matn]` |
| 10 | 0.6862 | ibnabishayba |  | C59 | ✓ | " مَنْ أَدَّى زَكَاةَ مَالِهِ أَدَّى الْحَقَّ الَّذِي عَلَيْهِ ، وَمَنْ زَادَ فَهُوَ خَيْرٌ لَهُ " `[ar-matn]` |
| 11 ★ | 0.6858 | abdurrazzaq |  | C59 | ✓ | الضَّمَانُ عَلَى مَنْ تَعَدَّى ، وَالرِّبْحُ لِصَاحِبِ الْمَالِ " `[ar-matn]` |
| 12 ★ | 0.6850 | abdurrazzaq |  | C59 | ✓ | فَإِذَا كَانَ لِرَجُلٍ مَالٌ قَدْرَ زَكَاةٍ ، ثُمَّ ذَهَبَ مَالُهُ ذَلِكَ فَبَقِيَ مِنْهُ دِرْهَمٌ وَاحِدٌ ، وَبَقْيَ بَيْنَهُ وَبَيْنَ الْوَقْتِ الَّذِي كَانَ يُزَكِّي فِيهِ شَهْرٌ ، ثُمَّ اسْتَفَادَ مَالا زَكَّى الَّذِي أَفَادَ مِنَ الْمَالِ مَعَ ذ `[ar-matn]` |
| 13 ★ | 0.6806 | ibnabishayba |  | C59 | ✓ | مَنْ ضَمِنَ مَالًا ، فَهُوَ رِبْحُهُ " `[ar-matn]` |
| 14 ★ | 0.6804 | adab | 444 | C31 | ~ | Abu'l-'Ubaydayn said, "I asked 'Abdullah about those who squander and he said, 'They are those who spend incorrectly.'" |
| 15 ★ | 0.6803 | ibnabishayba |  | C31 | ✓ | اللَّهَ يَقُولُ : [quran sura="2" aya_start="180" aya_end="180"] إِنْ تَرَكَ خَيْرًا [/quran] وَإِنَّكَ لَمْ تَدَعْ مَالًا , فَدَعْهُ لِعِيَالِكَ " `[ar-matn]` |
| 16 ★ | 0.6801 | ibnabishayba |  | C59 | ✓ | " لَا يَطِيبُ هَذَا الْمَالُ إلَّا مِنْ أَرْبَعِ خِلَالٍ : سَهْمٌ فِي الْمُسْلِمِينَ , أَوْ تِجَارَةٌ مِنْ حَلَالٍ , أَوْ إعْطَاءٌ مِنْ أَخٍ مُسْلِمٍ عَنْ ظَهْرِ يَدٍ , أَوْ مِيرَاثٌ فِي كِتَابِ اللَّهِ " `[ar-matn]` |
| 17 ★ | 0.6799 | muslim | 1568 a | C59 | ~ | Rafi b. Khadij (Allah be pleased with him) reported: I heard Allah's Apostle (may peace be upon him) as saying: The worst earning is the earning of a prostitute, the price of a dog and the earning of a cupper. |
| 18 ★ | 0.6799 | daraqutni |  | C31 | ✓ | فَقَضَى رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ عَلَى أَهْلِ الأَمْوَالِ حِفْظَ أَمْوَالِهِمْ بِالنَّهَارِ , وَعَلَى أَهْلِ الْمَاشِيَةِ حِفْظَهُمْ بِاللَّيْلِ " `[ar-matn]` |
| 19 ★ | 0.6794 | ibnabishayba |  | C59 | ✓ | " لَا رِبْحَ لِمَالٍ مَضْمُونٍ " `[ar-matn]` |
| 20 ★ | 0.6790 | daraqutni |  | C59 | ✓ | لَوْ كَانَ عِنْدِي شَيْءٌ أَوْ كُنْتُ أَقْدِرُ عَلَى شَيْءٍ , وَيْلِي هَذَا الْمَالَ قَدِ اجْتَمَعَ عِنْدِي , فَخُذَاهُ فَاشْتَرِيَا بِهِ مَتَاعًا , فَإِذَا قَدِمْتُمَا عَلَى عُمَرَ فَبِيعَاهُ وَلَكُمَا الرِّبْحُ , وَادْفَعَا إِلَى عُمَرَ رَضِيَ اللّ `[ar-matn]` |

#### Straight kNN (full index)

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 ★ | 0.7037 | abdurrazzaq |  | C15 | ✓ | [quran sura="2" aya_start="177" aya_end="177"] وَآتَى الْمَالَ عَلَى حُبِّهِ [/quran] , قَالَ : قَالَ [narrator id="5079" role="sahabi" tooltip="عبد الله بن مسعود"]ابْنُ مَسْعُودٍ[/narrator] : " أَنْ تُؤْتِيَهُ وَأَنْتَ صَحِيحٌ , شَحِيحٌ , تَأْمَلُ ا `[ar-matn]` |
| 2 ★ | 0.7028 | ibnabishayba |  | C15 | ✓ | [quran sura="70" aya_start="24" aya_end="24"] وَالَّذِينَ فِي أَمْوَالِهِمْ حَقٌّ مَعْلُومٌ [/quran] ، قَالَ : " الزَّكَاةُ " `[ar-matn]` |
| 3 ★ | 0.7021 | ibnabishayba |  | C15 | ✓ | [quran sura="24" aya_start="31" aya_end="31"] وَلا يُبْدِينَ زِينَتَهُنَّ إِلا مَا ظَهَرَ مِنْهَا [/quran] قَالَ : " الثِّيَابُ " `[ar-matn]` |
| 4 | 0.7014 | ibnabishayba |  | C59 | ✓ | رَضَاعِ صَبِيٍّ فَجَعَلَ رَضَاعَهُ مِنْ مَالِهِ ، وَقَالَ لِوَلِيِّهِ : " لَوْ لَمْ يَكُنْ لَهُ مَالٌ ؛ لَجَعَلْنَا رَضَاعَهُ فِي مَالِكَ , أَلَا تَرَاهُ يَقُولُ : [quran sura="2" aya_start="233" aya_end="233"] وَعَلَى الْوَارِثِ مِثْلُ ذَلِكَ [/qura `[ar-matn]` |
| 5 ★ | 0.7003 | ibnabishayba |  | C15 | ✓ | [quran sura="70" aya_start="24" aya_end="24"] وَالَّذِينَ فِي أَمْوَالِهِمْ حَقٌّ مَعْلُومٌ [/quran] ، قَالَ : " الزَّكَاةُ الْمَفْرُوضَةُ " `[ar-matn]` |
| 6 | 0.6991 | ibnabishayba |  | C59 | ✓ | " فِي الْمَالِ حَقٌّ سِوَى الزَّكَاةِ " `[ar-matn]` |
| 7 | 0.6991 | ibnabishayba |  | C59 | ✓ | " فِي الْمَالِ حَقٌّ سِوَى الزَّكَاةِ " `[ar-matn]` |
| 8 ★ | 0.6967 | ibnabishayba |  | C15 | ✓ | [quran sura="70" aya_start="24" aya_end="24"] فِي أَمْوَالِهِمْ حَقٌّ مَعْلُومٌ [/quran] قَالَ : " سِوَى الزَّكَاةِ " `[ar-matn]` |
| 9 | 0.6954 | ibnabishayba |  | C59 | ✓ | " زَكَاةُ أَمْوَالِكُمْ حَوْلٌ إلَى حَوْلٍ ، وَمَا كَانَ مِنْ دَيْنِ ثِقَةٍ فَزَكُّوهُ ، وَمَا كَانَ مِنْ دَيْنِ ظَنُونٍ فَلَا زَكَاةَ فِيهِ حَتَّى يَقْضِيَهُ صَاحِبُهُ " `[ar-matn]` |
| 10 ★ | 0.6945 | ibnmajah | 1789 | C25 | ~ | Fatima bint Qais narrated that: she heard him, meaning the Prophet say: “There is nothing due on wealth other then Zakat.” |
| 11 | 0.6942 | malik |  | C59 | ~ | هُوَ الْمَالُ الَّذِي لاَ تُؤَدَّى مِنْهُ الزَّكَاةُ ‏.‏ `[ar-matn]` |
| 12 ★ | 0.6923 | ibnabishayba |  | C15 | ✓ | " [quran sura="2" aya_start="180" aya_end="180"] إِنْ تَرَكَ خَيْرًا الْوَصِيَّةُ [/quran] ، قَالَ : خَيْرُ الْمَالِ , كَانَ يُقَالُ : أَلْفُ دِرْهَمٍ فَصَاعِدًا " `[ar-matn]` |
| 13 | 0.6917 | ibnabishayba |  | C59 | ✓ | لِي مَالًا فَإِلَى مَنْ أَدْفَعُ زَكَاتَهُ قَالَ : " ادْفَعْهَا إلَى هَؤُلَاءِ الْقَوْمِ " يَعني الْأُمَرَاءَ ، قُلْتُ : إذًا يَتَّخِذُونَ بِهَا ثِيَابًا وَطِيبًا قَالَ : " وَإِنِ اتَّخَذُوا ثِيَابًا وَطِيبًا ، وَلَكِنْ فِي مَالِكَ حَقٌّ سِوَى الزَّك `[ar-matn]` |
| 14 ★ | 0.6901 | ibnabishayba |  | C15 | ✓ | [quran sura="2" aya_start="245" aya_end="245"] مَنْ ذَا الَّذِي يُقْرِضُ اللَّهَ قَرْضًا حَسَنًا [/quran] ، قَالَ : " النَّفَقَةُ فِي سَبِيلِ اللَّهِ " `[ar-matn]` |
| 15 ★ | 0.6883 | abdurrazzaq |  | C15 | ✓ | [quran sura="24" aya_start="33" aya_end="33"] إِنْ عَلِمْتُمْ فِيهِمْ خَيْرًا [/quran] الْخَيْرُ : الْمَالُ `[ar-matn]` |
| 16 | 0.6883 | ibnmajah | 4130 | C59 | ~ | It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “The wealthiest will be the lowest on the Day of Resurrection, except those who do such and such with their money, and earn it from good sources.” |
| 17 | 0.6879 | abdurrazzaq |  | C59 | ✓ | الْمَالُ الْغَائِبُ أَفِيهِ زَكَاةٌ ؟ قَالَ : إِذَا لَمْ يَكُنْ ضُمَارًا أَوْ فِي تُوًى فَزَكِّهِ " `[ar-matn]` |
| 18 ★ | 0.6864 | abdurrazzaq |  | C15 | ✓ | [quran sura="111" aya_start="2" aya_end="2"] مَا أَغْنَى عَنْهُ مَالُهُ وَمَا كَسَبَ [/quran] , " وَلَدُهُ كَسْبُهُ " `[ar-matn]` |
| 19 | 0.6864 | ibnabishayba |  | C59 | ✓ | إِضَاعَةِ الْمَالِ , قَالَ : أَنْ يَرْزُقَكَ اللَّهُ رِزْقًا ، فَتُنْفِقُهُ فِيمَا حَرَّمَ عَلَيْكَ " `[ar-matn]` |
| 20 | 0.6862 | ibnabishayba |  | C59 | ✓ | " مَنْ أَدَّى زَكَاةَ مَالِهِ أَدَّى الْحَقَّ الَّذِي عَلَيْهِ ، وَمَنْ زَادَ فَهُوَ خَيْرٌ لَهُ " `[ar-matn]` |

---

## "treatment of parents"

Embed: **403ms** | Clusters selected: **[30, 37]** | Centroid ES: **27ms** | Straight ES: **17ms** | Overlap: **13/20** (Jaccard 0.481)

#### Centroid-filtered kNN

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.6528 | ibnabishayba |  | C30 | ✓ | " عَلَيْكُمْ أَنْ تَسْتَأْذِنُوا عَلَى أُمَّهَاتِكُمْ " `[ar-matn]` |
| 2 | 0.6517 | bukhari | 448 | C30 | ✓ | Narrated Sahl: Allah's Apostle sent someone to a woman telling her to "Order her slave, carpenter, to prepare a wooden pulpit for him to sit on." |
| 3 | 0.6500 | adab | 2 | C30 | ~ | 'Abdullah ibn 'Umar said, "The pleasure of the Lord lies in the pleasure of the parent. The anger of the Lord lies in the anger of the parent." |
| 4 | 0.6462 | ibnmajah | 3863 | C30 | ~ | It was narrated that Umm Haim bint Wadda' Al-Khuza'iyyah said: "I heard the Messenger of Allah (saas) say: 'The supplication of a father reaches the Veil (i.e. the place of repentance).'" |
| 5 | 0.6448 | riyadussalihin | 897 | C37 | ~ | Abu Musa (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "Visit the sick, feed the hungry, and (arrange for the) release of the captive.'' [Al-Bukhari] . |
| 6 | 0.6436 | riyadussalihin | 239 | C37 | ~ | Al-Bara' bin 'Azib (May Allah bepleased with them) reported: The Prophet (PBUH) commanded us to observe seven things and forbade us seven. He ordered us to visit the sick; to follow funeral processions; to respond to a sneezer with 'Yarhamuk-Allah (M |
| 7 | 0.6430 | ibnhibban |  | C30 | ✓ | " رِضَاءُ اللَّهِ فِي رِضَاءِ الْوَالِدِ ، وَسَخَطُ اللَّهِ فِي سَخَطِ الْوَالِدِ " `[ar-matn]` |
| 8 | 0.6419 | ibnabishayba |  | C30 | ✓ | اشْتَرِ مِائَةَ أَهْلِ بَيْتٍ , وَلَا تُفَرِّقْ بَيْنَ وَالِدٍ وَوَلَدِهِ " `[ar-matn]` |
| 9 | 0.6416 | ibnhibban |  | C30 | ✓ | بِرَّ أَبَاكَ ، وَأَحْسِنْ صُحْبَتَهُ " `[ar-matn]` |
| 10 | 0.6402 | ahmad | 346 | C30 | ~ | It was narrated from ‘Amr bin Shu`aib from his father that his grandfather said: A man killed his (own) son deliberately and the case was referred to `Umar bin al Khattab (رضي الله عنه), who ruled that the murderer should pay one hundred camels (as d |
| 11 | 0.6394 | ibnabishayba |  | C30 | ✓ | عَلَى الْوَلَدِ أَنْ يَبَرَّ وَالِدَهُ , وَكُلُّ إنْسَانٍ أَحَقُّ بِالَّذِي لَهُ " `[ar-matn]` |
| 12 | 0.6387 | daraqutni |  | C30 | ✓ | أَنْ يُفَرَّقَ بَيْنَ الأَخِ وَأَخِيهِ ، وَالْوَالِدِ وَوَلَدِهِ " `[ar-matn]` |
| 13 | 0.6386 | abdurrazzaq |  | C30 | ✓ | حَافِظُوا عَلَى أَبْنَائِكُمْ فِي الصَّلاةِ " `[ar-matn]` |
| 14 ★ | 0.6383 | adab | 1064 | C30 | ~ | 'Abdullah said, "A man asks permission of his father, his mother, his brother and his sister." |
| 15 ★ | 0.6358 | hakim |  | C30 | ✓ | " رِضَا الرَّبِّ فِي رِضَا الْوَالِدِ ، وَسَخِطُ الرَّبِّ فِي سَخَطِ الْوَالِدِ " `[ar-matn]` |
| 16 ★ | 0.6357 | daraqutni |  | C30 | ✓ | لا يُقْتَلُ الْوَالِدُ بِالْوَلَدِ " `[ar-matn]` |
| 17 ★ | 0.6357 | abdurrazzaq |  | C30 | ✓ | [quran sura="2" aya_start="233" aya_end="233"] لا تُضَارَّ وَالِدَةٌ بِوَلَدِهَا [/quran] ، قَالَ : فَتَرْمِي بِوَلَدِهَا وَلا تُرْضِعُهُ ، [quran sura="2" aya_start="233" aya_end="233"] وَلا مَوْلُودٌ لَهُ [/quran] ، قَالَ : يَقُولُ : وَلا الْوَالِد `[ar-matn]` |
| 18 ★ | 0.6353 | ibnmajah | 2662 | C30 | ~ | It was narrated from 'Amr bin Shu'aib, from his father, from his grandfather, that 'Umar bin Khattab said: “I heard the Messenger of Allah (SAW) say: 'A father should not be killed for his son.'” |
| 19 ★ | 0.6346 | abdurrazzaq |  | C30 | ✓ | مَا : [quran sura="2" aya_start="233" aya_end="233"] الْوَالِدَاتُ يُرْضِعْنَ أَوْلادَهُنَّ حَوْلَيْنِ كَامِلَيْنِ [/quran] ؟ قَالَ : إِذَا أَرَادَتِ امْرَأَةٌ أَنْ تُقْصِرَ عَنْ حَوْلَيْنِ كَانَ حَقًّا عَلَى أُمِّهِ أَنْ تُبَلِّغَهُ ، وَلا يَزِيدُ ع `[ar-matn]` |
| 20 ★ | 0.6331 | abdurrazzaq |  | C30 | ✓ | إِذَا أَرَادَ وَأَرَادَتِ الْوَالِدَةُ أَنْ يَفْصِلا وَلْدَهُمَا قَبْلَ الْحَوْلَيْنِ ، فَكَانَ ذَلِكَ : [quran sura="2" aya_start="233" aya_end="233"] عَنْ تَرَاضٍ مِنْهُمَا وَتَشَاوُرٍ [/quran] ، فَلا بَأْسَ " `[ar-matn]` |

#### Straight kNN (full index)

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 ★ | 0.6641 | riyadussalihin | 846 | C54 | ~ | Al-Bara' bin 'Azib (May Allah be pleased with them) reported: The Messenger of Allah (PBUH) commanded us to do seven things: to visit the sick, to follow the funeral (of a dead believer), to invoke the Mercy of Allah upon one who sneezes (i.e., by sa |
| 2 | 0.6528 | ibnabishayba |  | C30 | ✓ | " عَلَيْكُمْ أَنْ تَسْتَأْذِنُوا عَلَى أُمَّهَاتِكُمْ " `[ar-matn]` |
| 3 | 0.6517 | bukhari | 448 | C30 | ✓ | Narrated Sahl: Allah's Apostle sent someone to a woman telling her to "Order her slave, carpenter, to prepare a wooden pulpit for him to sit on." |
| 4 | 0.6500 | adab | 2 | C30 | ~ | 'Abdullah ibn 'Umar said, "The pleasure of the Lord lies in the pleasure of the parent. The anger of the Lord lies in the anger of the parent." |
| 5 ★ | 0.6475 | ibnmajah | 794 | C12 | ~ | Ibn 'Abbas and Ibn 'Umar narrated that: They heard the Prophet say on his pulpit: "People should desist from failing to attend the congregations, otherwise Allah will seal their hearts, and they will be among the negligent." |
| 6 ★ | 0.6468 | hakim |  | C15 | ✓ | [quran] نَدْعُ أَبْنَاءَنَا وَأَبْنَاءَكُمْ وَنِسَاءَنَا وَنِسَاءَكُمْ وَأَنْفُسَنَا وَأَنْفُسَكُمْ سورة آل عمران آية 61 [/quran] دَعَا رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَآلِهِ وَسَلَّمَ عَلِيًّا وَفَاطِمَةَ وَحَسَنًا وَحُسَيْنًا رَضِيَ اللَّه `[ar-matn]` |
| 7 ★ | 0.6466 | ibnabishayba |  | C12 | ✓ | سَتَحْرِصُونَ عَلَى الْإِمَارَةِ , وَسَتَصِيرُ حَسْرَةً وَنَدَامَةً , فَنِعْمَتِ الْمُرْضِعَةُ وَبِئْسَتِ الْفَاطِمَةُ " `[ar-matn]` |
| 8 | 0.6462 | ibnmajah | 3863 | C30 | ~ | It was narrated that Umm Haim bint Wadda' Al-Khuza'iyyah said: "I heard the Messenger of Allah (saas) say: 'The supplication of a father reaches the Veil (i.e. the place of repentance).'" |
| 9 ★ | 0.6454 | ibnhibban |  | C65 | ✓ | أَبِي وَأَبَاكَ فِي النَّارِ " `[ar-matn]` |
| 10 | 0.6448 | riyadussalihin | 897 | C37 | ~ | Abu Musa (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "Visit the sick, feed the hungry, and (arrange for the) release of the captive.'' [Al-Bukhari] . |
| 11 | 0.6436 | riyadussalihin | 239 | C37 | ~ | Al-Bara' bin 'Azib (May Allah bepleased with them) reported: The Prophet (PBUH) commanded us to observe seven things and forbade us seven. He ordered us to visit the sick; to follow funeral processions; to respond to a sneezer with 'Yarhamuk-Allah (M |
| 12 | 0.6430 | ibnhibban |  | C30 | ✓ | " رِضَاءُ اللَّهِ فِي رِضَاءِ الْوَالِدِ ، وَسَخَطُ اللَّهِ فِي سَخَطِ الْوَالِدِ " `[ar-matn]` |
| 13 ★ | 0.6424 | abdurrazzaq |  | C12 | ✓ | لَكُمْ نَصِيبٌ فِي الْجَاهِلِيَّةِ , فَخُذُوا نَصِيبَكُمْ مِنَ الإِسْلامِ , فَصَالَحَهُ عَلَى أَنْ أُضَعِّفَ عَلَيْهِمُ الْجِزْيَةَ , وَأَلا يُنَصِّرُوا الأَبْنَاءَ " `[ar-matn]` |
| 14 | 0.6419 | ibnabishayba |  | C30 | ✓ | اشْتَرِ مِائَةَ أَهْلِ بَيْتٍ , وَلَا تُفَرِّقْ بَيْنَ وَالِدٍ وَوَلَدِهِ " `[ar-matn]` |
| 15 | 0.6416 | ibnhibban |  | C30 | ✓ | بِرَّ أَبَاكَ ، وَأَحْسِنْ صُحْبَتَهُ " `[ar-matn]` |
| 16 | 0.6402 | ahmad | 346 | C30 | ~ | It was narrated from ‘Amr bin Shu`aib from his father that his grandfather said: A man killed his (own) son deliberately and the case was referred to `Umar bin al Khattab (رضي الله عنه), who ruled that the murderer should pay one hundred camels (as d |
| 17 | 0.6394 | ibnabishayba |  | C30 | ✓ | عَلَى الْوَلَدِ أَنْ يَبَرَّ وَالِدَهُ , وَكُلُّ إنْسَانٍ أَحَقُّ بِالَّذِي لَهُ " `[ar-matn]` |
| 18 | 0.6387 | daraqutni |  | C30 | ✓ | أَنْ يُفَرَّقَ بَيْنَ الأَخِ وَأَخِيهِ ، وَالْوَالِدِ وَوَلَدِهِ " `[ar-matn]` |
| 19 ★ | 0.6386 | hakim |  | C12 | ✓ | " بَرُّوا آبَاءَكُمْ ، تَبَرَّكُمْ أَبْنَاؤُكُمْ ، وَعِفِّوا عَنْ نِسَاءِ النَّاسِ ، تَعِفَّ نِسَاؤُكُمْ ، وَمَنْ تُنُصِّلَ إِلَيْهِ فَلَمْ يَقْبَلْ ، لَمْ يَرِدْ عَلَيَّ الْحَوْضَ " `[ar-matn]` |
| 20 | 0.6386 | abdurrazzaq |  | C30 | ✓ | حَافِظُوا عَلَى أَبْنَائِكُمْ فِي الصَّلاةِ " `[ar-matn]` |

---

## "aisha"

Embed: **157ms** | Clusters selected: **[39, 16]** | Centroid ES: **33ms** | Straight ES: **18ms** | Overlap: **5/20** (Jaccard 0.143)

#### Centroid-filtered kNN

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.6921 | nasai | 2966 | C16 | ~ | Ibn Umar said: "When the Messenger of Allah arrived in Makkah he circumambulated the House seven times, then he prayed two Rakahs behind the Maqam. Then, he went out to As-Safa through the gate that is usually used to exit, and performed Sai between  |
| 2 | 0.6801 | muslim | 2307 c | C16 | ~ | This hadith has been transmitted on the authority of Anas with a slight variation of wording. |
| 3 | 0.6797 | ahmad | 37 | C16 | ~ | It was narrated from Muhammad bin Jubair bin Mut'im that 'Uthman said: I wish that I had asked the Messenger of Allah (ﷺ) what would save us from what the Shaitan whispers into our hearts. Abu Bakr said: I asked him about that and he said: `What can  |
| 4 | 0.6797 | adab | 489 | C16 | ~ | Abu'd-Duha said: "Masruq and Shutayr ibn Shakal met in the mosque. The people sitting in circles in the mosque moved towards them. Masruq said, 'I can only think that these people are gathering around us in order to hear good from us. If you relate f |
| 5 | 0.6779 | muslim | 555 b | C16 | ~ | Sa'd b. Yazid Abu Mas'ama reported: I said to Anas like (that mentioned above). |
| 6 ★ | 0.6721 | bukhari | 1983 | C16 | ✓ | Narrated Mutarrif from `Imran Ibn Husain: That the Prophet asked him (Imran) or asked a man and `Imran was listening, "O Abu so-and-so! Have you fasted the last days of this month?" (The narrator thought that he said, "the month of Ramadan"). The man |
| 7 ★ | 0.6709 | tirmidhi | 279 | C16 | ~ | Al-Bara bin Azib narrated: "The Salat of Allah's Messenger (was such that) when he bowed, and when he raised his head from bowing, and when he prostrated, and when he raised his head from prostration it (all) was nearly the same." |
| 8 ★ | 0.6709 | tirmidhi | 1756 | C16 | ~ | Another chain with similar meaning. [Abu 'Eisa said:] This Hadith is Hasan Sahih. He said: There is something on this topic from Anas. |
| 9 ★ | 0.6709 | darimi |  | C16 | ✓ | لِأُمٍّ " `[ar-matn]` |
| 10 ★ | 0.6703 | ibnabishayba |  | C39 | ✓ | " كُنَّ [narrator role="sahabi"]أُمَّهَاتُ الْمُؤْمِنِينَ[/narrator] يَتَهَادَيْنَ الْجَرَادَ " `[ar-matn]` |
| 11 ★ | 0.6702 | abdurrazzaq |  | C39 | ✓ | يُسِرُّ آمِينَ " `[ar-matn]` |
| 12 ★ | 0.6697 | nasai | 886 | C16 | ~ | It was narrated that Ibn Umar said: "While we were praying with the Messenger of Allah (SAW), a man among the people said: 'Allahu Akbaru kabira, wal-hamdu Lillahi kathira, wa subhan-Allahi bukratan was asila (Allah is Most Great and much praise be t |
| 13 ★ | 0.6697 | muslim | 1146 c | C16 | ~ | In another version of the previous hadith, the words are:" Yahya said: I think it was due to the regard for the Apostle of Allah (may peace be upon him)." |
| 14 ★ | 0.6697 | ibnmajah | 1702 | C16 | ~ | It was narrated that ‘Abdullah bin ‘Amr Al-Qari said: “I heard Abu hurairah say: ‘No, by the Lord of the Ka’bah! I did not say: “Whoever wakes up in a state of sexual impurity (and wants to fast) then he must not fast.” Muhammad (saw) said it.’” |
| 15 ★ | 0.6697 | tirmidhi | 799 | C16 | ~ | Muhammad bin Ka'b narrated: "I went to Anas bin Malik during Ramadan and he was about to travel. His mount was prepared for him, and he put on his traveling clothes, then he called for some food to eat, and I said to him: 'Is it Sunnah?' He said: 'It |
| 16 ★ | 0.6695 | nasai | 1456 | C16 | ~ | It was narrated from 'Aishah that: She performed Umrah with the Messenger of Allah (SAW), traveling from Al-Madinah to Makkah. Then, when she came to Makkah, she said: "O Messenger of Allah (SAW), may my father and mother be ransomed for you, you sho |
| 17 ★ | 0.6688 | hakim |  | C16 | ✓ | " أَمِتْ أَمِتْ " `[ar-matn]` |
| 18 ★ | 0.6688 | hakim |  | C16 | ✓ | " أَمِتْ أَمِتْ " `[ar-matn]` |
| 19 ★ | 0.6678 | muslim | 1701 b | C16 | ~ | This hadith has been transmitted on the authority of Juraij with a slight variation of words. |
| 20 ★ | 0.6672 | abudawud | 1341 | C39 | ~ | Abu Salamah b. 'Abd al-Rahman asked 'Aishah, the wife of the Prophet (saws): How did the Messenger of Allah (saws) pray during Ramadhan ? She said: The Messenger of Allah (saws) did not pray more than eleven rak'ahs during Ramadhan and other than Ram |

#### Straight kNN (full index)

| # | Score | Collection | Hadith | Cluster | Tag | Text |
|---|---|---|---|---|---|---|
| 1 ★ | 0.6957 | bukhari | 1713 | C2 | ✓ | Narrated Ziyad bin Jubair: I saw Ibn `Umar passing by a man who had made his Badana sit to slaughter it. Ibn `Umar said, "Slaughter it while it is standing with one leg tied up as is the tradition of Muhammad." |
| 2 ★ | 0.6942 | abdurrazzaq |  | C15 | ✓ | [quran sura="4" aya_start="6" aya_end="6"] فَإِنْ آنَسْتُمْ مِنْهُمْ رُشْدًا [/quran] ، قَالَ : " عَقْلا " `[ar-matn]` |
| 3 | 0.6921 | nasai | 2966 | C16 | ~ | Ibn Umar said: "When the Messenger of Allah arrived in Makkah he circumambulated the House seven times, then he prayed two Rakahs behind the Maqam. Then, he went out to As-Safa through the gate that is usually used to exit, and performed Sai between  |
| 4 ★ | 0.6902 | abdurrazzaq |  | C62 | ✓ | رَأَتْ [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةَ[/narrator] أُمَّ الْمُؤْمِنِينَ ، مُخَضَّبَةً عَلَيْهَا ثِيَابُ مُضْرَجَةٌ ، قَالَ : وَرَأَيْتُ أَنَا [narrator id="3954" role="sahabi" tooltip="صفية بنت شيبة القرش `[ar-matn]` |
| 5 ★ | 0.6900 | bukhari | 4752 | C62 | ~ | Narrated Ibn Abi Mulaika: I heard `Aisha reciting: "When you invented a lie (and carry it) on your tongues." (24.15) |
| 6 ★ | 0.6857 | ibnabishayba |  | C2 | ✓ | " رَأَيْتُ [narrator role="sahabi"]أَنَسًا[/narrator] عِنْدَ الْبَابِ الْأَوَّلِ يَوْمَ الْجُمُعَةِ قَدِ اسْتَقْبَلَ الْمِنْبَرَ " `[ar-matn]` |
| 7 ★ | 0.6819 | daraqutni |  | C7 | ✓ | قَالَ : [quran sura="1" aya_start="7" aya_end="7"] وَلا الضَّالِّينَ [/quran] , قَالَ : " آمِينَ " , مَدَّ بِهَا صَوْتَهُ `[ar-matn]` |
| 8 ★ | 0.6814 | ibnabishayba |  | C62 | ✓ | قَبَّلَ رَأْسَ عَائِشَةَ " `[ar-matn]` |
| 9 | 0.6801 | muslim | 2307 c | C16 | ~ | This hadith has been transmitted on the authority of Anas with a slight variation of wording. |
| 10 | 0.6797 | ahmad | 37 | C16 | ~ | It was narrated from Muhammad bin Jubair bin Mut'im that 'Uthman said: I wish that I had asked the Messenger of Allah (ﷺ) what would save us from what the Shaitan whispers into our hearts. Abu Bakr said: I asked him about that and he said: `What can  |
| 11 | 0.6797 | adab | 489 | C16 | ~ | Abu'd-Duha said: "Masruq and Shutayr ibn Shakal met in the mosque. The people sitting in circles in the mosque moved towards them. Masruq said, 'I can only think that these people are gathering around us in order to hear good from us. If you relate f |
| 12 ★ | 0.6796 | abdurrazzaq |  | C62 | ✓ | اعْتَكَفَتْ [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةُ[/narrator] بَيْنَ حِرَاءَ وَثَبِيرٍ ، فَكُنَّا نَأْتِيهَا هُنَاكَ ، وَعَبْدٌ لَهَا يَؤُمُّهَا " `[ar-matn]` |
| 13 ★ | 0.6793 | daraqutni |  | C62 | ✓ | أَمَّتْنَا [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةُ[/narrator] , فَقَامَتْ بَيْنَهُنَّ فِي الصَّلاةِ الْمَكْتُوبَةِ " `[ar-matn]` |
| 14 ★ | 0.6788 | ibnabishayba |  | C12 | ✓ | فَإِنْ آنَسْتُمْ مِنْهُمْ رُشْدًا " ، قَالَ : عَقْلا `[ar-matn]` |
| 15 ★ | 0.6788 | abdurrazzaq |  | C62 | ✓ | يَتَامَى فِي حِجْرِ [narrator role="sahabi"]عَائِشَةَ[/narrator] ، فَكَانَتْ تُزَكِّي أَمْوَالَنَا ، ثُمَّ دَفَعَتْهُ مُقَارَضَةً فَبُورِكَ لَنَا فِيهِ " `[ar-matn]` |
| 16 ★ | 0.6784 | shamail | 209 | C7 | ~ | Anas ibn Malik said (may Allah be well pleased with him): "The Prophet (Allah bless him and give him peace) used to breathe into the vessel three times when he drank, and he would say: 'It is more wholesome and more thirst-quenching!’” |
| 17 ★ | 0.6782 | muslim | 1452 c | C62 | ~ | Ahadith like this is transmitted by 'A'isha through another chain of narrators. |
| 18 | 0.6779 | muslim | 555 b | C16 | ~ | Sa'd b. Yazid Abu Mas'ama reported: I said to Anas like (that mentioned above). |
| 19 ★ | 0.6768 | ibnabishayba |  | C7 | ✓ | عَلَى [narrator role="chain"]أَبِي عُبَيْدَةَ[/narrator] عِمَامَةً سَوْدَاءَ " `[ar-matn]` |
| 20 ★ | 0.6767 | ibnabishayba |  | C62 | ✓ | يَسْمُرُ بَعْدَ الْعِشَاءِ ، حَتَّى تَقُولَ [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةُ[/narrator] : قَدْ أَصْبَحْتُمْ " `[ar-matn]` |