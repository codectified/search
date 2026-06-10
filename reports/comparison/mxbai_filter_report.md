# mxbai Filter & Dedup Report

Index: `english-mxbai` | Total docs: 48,703

- Chain-ref docs (`isChainRef=True`): **1,574** (3.2%)
- Docs in a dup group (`dupGroup>0`): **6,405** (13.2%)

---

## 1. Chain-ref filter: ON vs OFF

Chain-reference hadiths have no matn content — they're isnad-variant notes like *"This hadith has been narrated through another chain of transmitters."* Without the filter these can rank highly for queries whose terms appear in that phrase.

### Query: *"comparing yourself to others"*

Chain-refs in top-10 (filter OFF): **0** | filter OFF: 1464ms | filter ON: 67ms

**Filter OFF** (raw — chain-refs highlighted)
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.815 | forty 18 | The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | bukhari 6490 | Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him  |
| 3 | 0.793 | muslim 2963 a | Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who sta |
| 4 | 0.787 | riyadussalihin 466 | Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are  |
| 5 | 0.785 | muslim 2536 | 'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were |
| 6 | 0.782 | abudawud 4092 | Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a  |
| 7 | 0.782 | tirmidhi 2513 | Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not |
| 8 | 0.781 | adab 898 | Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a femal |
| 9 | 0.779 | riyadussalihin 7 | Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does not look at |
| 10 | 0.775 | forty 19 | On the authority of Abu Abbas Abdullah bin Abbas (may Allah be pleased with him) who said: One day I was behin |

**Filter ON**
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.815 | forty 18 | The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | bukhari 6490 | Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him  |
| 3 | 0.793 | muslim 2963 a | Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who sta |
| 4 | 0.791 | adab 159 | Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise  |
| 5 | 0.787 | riyadussalihin 466 | Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are  |
| 6 | 0.785 | muslim 2536 | 'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were |
| 7 | 0.782 | abudawud 4092 | Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a  |
| 8 | 0.782 | tirmidhi 2513 | Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not |
| 9 | 0.781 | adab 898 | Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a femal |
| 10 | 0.779 | riyadussalihin 7 | Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does not look at |

### Query: *"forgiveness of sins"*

Chain-refs in top-10 (filter OFF): **0** | filter OFF: 53ms | filter ON: 85ms

**Filter OFF** (raw — chain-refs highlighted)
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.876 | forty 28 | One who repents from sin is like someone without sin. |
| 2 | 0.852 | riyadussalihin 423 | Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Were you  |
| 3 | 0.851 | bukhari 7507 | Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lord! I have |
| 4 | 0.850 | riyadussalihin 442 | `[dup=1604380]` Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted, has said:  |
| 5 | 0.850 | bulugh 319 | Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my pr |
| 6 | 0.848 | ibnmajah 3821 | It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Exalted, sai |
| 7 | 0.848 | riyadussalihin 421 | Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, and Glori |
| 8 | 0.848 | mishkat 2482 | Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, forgive me  |
| 9 | 0.846 | mishkat 1958 | Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward |
| 10 | 0.846 | bukhari 6069 | Narrated Abu Huraira: I heard Allah's Apostle saying. "All the sins of my followers will be forgiven except th |

**Filter ON**
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.876 | forty 28 | One who repents from sin is like someone without sin. |
| 2 | 0.852 | riyadussalihin 423 | Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Were you  |
| 3 | 0.851 | bukhari 7507 | Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lord! I have |
| 4 | 0.850 | riyadussalihin 442 | `[dup=1604380]` Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted, has said:  |
| 5 | 0.850 | bulugh 319 | Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my pr |
| 6 | 0.848 | ibnmajah 3821 | It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Exalted, sai |
| 7 | 0.848 | riyadussalihin 421 | Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, and Glori |
| 8 | 0.848 | mishkat 2482 | Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, forgive me  |
| 9 | 0.846 | mishkat 1958 | Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward |
| 10 | 0.846 | bukhari 6069 | Narrated Abu Huraira: I heard Allah's Apostle saying. "All the sins of my followers will be forgiven except th |

### Query: *"prayer before sleeping"*

Chain-refs in top-10 (filter OFF): **0** | filter OFF: 90ms | filter ON: 77ms

**Filter OFF** (raw — chain-refs highlighted)
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.875 | bukhari 212 | Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep |
| 2 | 0.870 | muslim 786 | 'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in prayer, h |
| 3 | 0.864 | bukhari 997 | Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever  |
| 4 | 0.858 | mishkat 604 | Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one is awake  |
| 5 | 0.857 | bukhari 512 | Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Whenever he  |
| 6 | 0.856 | bukhari 213 | Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till he underst |
| 7 | 0.853 | muslim 787 | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets up at night |
| 8 | 0.853 | bulugh 390 | `[dup=216500]` Narrated Jabir (RA): Allah's Messenger (SAW) said, "If anyone is afraid that he may not get up in the latter p |
| 9 | 0.852 | abudawud 856 | Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also entered i |
| 10 | 0.852 | muslim 755 a | `[dup=216500]` Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up |

**Filter ON**
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.875 | bukhari 212 | Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep |
| 2 | 0.870 | muslim 786 | 'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in prayer, h |
| 3 | 0.864 | bukhari 997 | Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever  |
| 4 | 0.858 | mishkat 604 | Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one is awake  |
| 5 | 0.857 | bukhari 512 | Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Whenever he  |
| 6 | 0.856 | bukhari 213 | Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till he underst |
| 7 | 0.853 | muslim 787 | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets up at night |
| 8 | 0.853 | bulugh 390 | `[dup=216500]` Narrated Jabir (RA): Allah's Messenger (SAW) said, "If anyone is afraid that he may not get up in the latter p |
| 9 | 0.852 | abudawud 856 | Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also entered i |
| 10 | 0.852 | muslim 755 a | `[dup=216500]` Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up |

### Query: *"fasting in Ramadan"*

Chain-refs in top-10 (filter OFF): **0** | filter OFF: 81ms | filter ON: 78ms

**Filter OFF** (raw — chain-refs highlighted)
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.889 | muslim 1162 a | `[dup=226020]` Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How do you fa |
| 2 | 0.889 | mishkat 1973 | Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just before Ramadan |
| 3 | 0.887 | bukhari 1914 | Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ramadan unle |
| 4 | 0.886 | muslim 1082 a | Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: Do not o |
| 5 | 0.886 | muslim 1159 o | 'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be upon him) sa |
| 6 | 0.885 | tirmidhi 759 | Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with six from Sh |
| 7 | 0.885 | abudawud 2335 | Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just before Ra |
| 8 | 0.885 | mishkat 2028 | ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travelling is like  |
| 9 | 0.885 | mishkat 2047 | Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it with six  |
| 10 | 0.885 | bukhari 1900 | Narrated Ibn `Umar: I heard Allah's Apostle saying, "When you see the crescent (of the month of Ramadan), star |

**Filter ON**
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.889 | muslim 1162 a | `[dup=226020]` Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How do you fa |
| 2 | 0.889 | mishkat 1973 | Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just before Ramadan |
| 3 | 0.887 | bukhari 1914 | Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ramadan unle |
| 4 | 0.886 | muslim 1082 a | Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: Do not o |
| 5 | 0.886 | muslim 1159 o | 'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be upon him) sa |
| 6 | 0.885 | tirmidhi 759 | Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with six from Sh |
| 7 | 0.885 | abudawud 2335 | Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just before Ra |
| 8 | 0.885 | mishkat 2028 | ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travelling is like  |
| 9 | 0.885 | mishkat 2047 | Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it with six  |
| 10 | 0.885 | bukhari 1900 | Narrated Ibn `Umar: I heard Allah's Apostle saying, "When you see the crescent (of the month of Ramadan), star |

### Query: *"visiting the sick"*

Chain-refs in top-10 (filter OFF): **0** | filter OFF: 68ms | filter ON: 98ms

**Filter OFF** (raw — chain-refs highlighted)
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.825 | muslim 2568 a | Abu Rabi' reported directly from Allah's Apostle (may peace upon him) as saying: The one who visits the sick i |
| 2 | 0.820 | ahmad 975 | `[dup=5009750]` It was narrated that ‘Abdullah bin Nafi’ said: Abu Moosa al-Ash’ari visited al-Hasan bin ‘Ali when he was sick |
| 3 | 0.818 | ahmad 612 | It was narrated that ‘AbdurRahman bin Abi Laila said: Abu Moosa came to al-Hasan bin `Ali to visit him when he |
| 4 | 0.817 | bukhari 5689 | Narrated 'Urwa: Aisha used to recommend at-Talbina for the sick and for such a person as grieved over a dead p |
| 5 | 0.817 | ibnmajah 1777 | It was narrated that Anas bin Malik said: “The Messenger of Allah (saw) said: ‘The person observing I’tikaf ma |
| 6 | 0.817 | tirmidhi 2087 | Abu Sa'eed Al-Khudri narrated that the Messenger of Allah (S.A.W) said: "When one of you visits the ill, then  |
| 7 | 0.815 | bukhari 3046 | Narrated Abu Musa: The Prophet said, "Free the captives, feed the hungry and pay a visit to the sick." |
| 8 | 0.813 | ahmad 955 | It was narrated from ‘Amr bin Huraith that he visited Hasan [when he was sick and ‘Ali was with him. `Ali (رضي |
| 9 | 0.811 | ibnmajah 1438 | It was narrated from Abu Sa’eed Al-Khudri that the Messenger of Allah (SAW) said: “When you enter upon one who |
| 10 | 0.811 | bukhari 5724 | Narrated Fatima bint Al-Mundhir: Whenever a lady suffering from fever was brought to Asma' bint Abu Bakr, she  |

**Filter ON**
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.825 | muslim 2568 a | Abu Rabi' reported directly from Allah's Apostle (may peace upon him) as saying: The one who visits the sick i |
| 2 | 0.820 | ahmad 975 | `[dup=5009750]` It was narrated that ‘Abdullah bin Nafi’ said: Abu Moosa al-Ash’ari visited al-Hasan bin ‘Ali when he was sick |
| 3 | 0.818 | ahmad 612 | It was narrated that ‘AbdurRahman bin Abi Laila said: Abu Moosa came to al-Hasan bin `Ali to visit him when he |
| 4 | 0.817 | bukhari 5689 | Narrated 'Urwa: Aisha used to recommend at-Talbina for the sick and for such a person as grieved over a dead p |
| 5 | 0.817 | ibnmajah 1777 | It was narrated that Anas bin Malik said: “The Messenger of Allah (saw) said: ‘The person observing I’tikaf ma |
| 6 | 0.817 | tirmidhi 2087 | Abu Sa'eed Al-Khudri narrated that the Messenger of Allah (S.A.W) said: "When one of you visits the ill, then  |
| 7 | 0.813 | ahmad 955 | It was narrated from ‘Amr bin Huraith that he visited Hasan [when he was sick and ‘Ali was with him. `Ali (رضي |
| 8 | 0.811 | ibnmajah 1438 | It was narrated from Abu Sa’eed Al-Khudri that the Messenger of Allah (SAW) said: “When you enter upon one who |
| 9 | 0.811 | bukhari 5724 | Narrated Fatima bint Al-Mundhir: Whenever a lady suffering from fever was brought to Asma' bint Abu Bakr, she  |
| 10 | 0.809 | muslim 2191 a | 'A'isha reported: When any person amongst us fell ill, Allah's Messenger (may peace he upon him) used to rub h |

### Query: *"honoring one's parents"*

Chain-refs in top-10 (filter OFF): **0** | filter OFF: 65ms | filter ON: 62ms

**Filter OFF** (raw — chain-refs highlighted)
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.843 | adab 35 | Abu Usayd said, "We were with the Messenger of Allah, may Allah bless him and grant him peace, when a man aske |
| 2 | 0.826 | adab 94 | Ibn 'Umar said, "Allah has called them the 'dutiful' (al-Abrar) because they are dutiful (birr) to their paren |
| 3 | 0.823 | adab 22 | Mu'adh said, "Bliss belongs to someone who is dutiful towards his parents. Allah Almighty will prolong his lif |
| 4 | 0.821 | mishkat 1768 | Muhammad b. an-Nu‘man who traced the tradition back to the Prophet reported him as saying, “If anyone visits t |
| 5 | 0.816 | ahmad 1408 | It was narrated that az-Zubair said: The Messenger of Allah (ﷺ) mentioned both of his parents together for me  |
| 6 | 0.815 | nasai 2559 | It was narrated from 'Amr bin Shu'aib, from his father, that his grandfather said: "Eat, give charity and clot |
| 7 | 0.812 | abudawud 5142 | Narrated AbuUsayd Malik ibn Rabi'ah as-Sa'idi: While we were with the Messenger of Allah! (saws) a man of Banu |
| 8 | 0.811 | ibnmajah 3664 | It was narrated that Abu Usaid, Malik bin Rabi'ah, said: "While we were with the Prophet(SAW), a man from the  |
| 9 | 0.811 | tirmidhi 1897 | Bahz bin Hakim narrated from his father, from his grandfather who said: "I said: 'O Messenger of Allah! Who mo |
| 10 | 0.808 | ibnmajah 2089 | It was narrated from 'Abdur-Rahman that: a man's father or mother - Shu'bah (one of the namators) was not sure |

**Filter ON**
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.843 | adab 35 | Abu Usayd said, "We were with the Messenger of Allah, may Allah bless him and grant him peace, when a man aske |
| 2 | 0.826 | adab 94 | Ibn 'Umar said, "Allah has called them the 'dutiful' (al-Abrar) because they are dutiful (birr) to their paren |
| 3 | 0.823 | adab 22 | Mu'adh said, "Bliss belongs to someone who is dutiful towards his parents. Allah Almighty will prolong his lif |
| 4 | 0.821 | mishkat 1768 | Muhammad b. an-Nu‘man who traced the tradition back to the Prophet reported him as saying, “If anyone visits t |
| 5 | 0.816 | ahmad 1408 | It was narrated that az-Zubair said: The Messenger of Allah (ﷺ) mentioned both of his parents together for me  |
| 6 | 0.815 | nasai 2559 | It was narrated from 'Amr bin Shu'aib, from his father, that his grandfather said: "Eat, give charity and clot |
| 7 | 0.812 | abudawud 5142 | Narrated AbuUsayd Malik ibn Rabi'ah as-Sa'idi: While we were with the Messenger of Allah! (saws) a man of Banu |
| 8 | 0.811 | ibnmajah 3664 | It was narrated that Abu Usaid, Malik bin Rabi'ah, said: "While we were with the Prophet(SAW), a man from the  |
| 9 | 0.811 | tirmidhi 1897 | Bahz bin Hakim narrated from his father, from his grandfather who said: "I said: 'O Messenger of Allah! Who mo |
| 10 | 0.808 | ibnmajah 2089 | It was narrated from 'Abdur-Rahman that: a man's father or mother - Shu'bah (one of the namators) was not sure |

### Query: *"This hadith has been narrated"*

Chain-refs in top-10 (filter OFF): **6** | filter OFF: 102ms | filter ON: 74ms

**Filter OFF** (raw — chain-refs highlighted)
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.950 | muslim 1444 c | `[⚠CHAIN]` The above hadith is narrated through another chain. |
| 2 | 0.949 | adab 830 | Part of previous hadith. |
| 3 | 0.943 | bukhari 1444 | See previous hadith. |
| 4 | 0.942 | ibnmajah 2490 | `[⚠CHAIN]` Another chain narrates a hadith similar to the previous one. |
| 5 | 0.942 | ibnmajah 2497 | `[⚠CHAIN]` Another chain narrates a hadith similar to the previous one. |
| 6 | 0.941 | muslim 673 b | `[⚠CHAIN]` A hadith like this has been narrated by A'mash by the same chain of transmitters |
| 7 | 0.941 | muslim 1869 d | `[dup=246095]` The above hadith has been narrated through several other chains with slight differences of wording. |
| 8 | 0.940 | muslim 1548 c | `[⚠CHAIN]` Another chain narrated the same as the above hadith. |
| 9 | 0.939 | muslim 1471 t | `[⚠CHAIN]` The story in the above hadith has likewise been narrated through another chain. |
| 10 | 0.939 | muslim 127 c | The same hadith has been narrated by Zuhair b. Harb, Waki, Ishaq b. Mansur, Husain b. 'Ali. |

**Filter ON**
| # | Score | Collection Hadith# | Tags | Text |
|---|---|---|---|---|
| 1 | 0.949 | adab 830 | Part of previous hadith. |
| 2 | 0.943 | bukhari 1444 | See previous hadith. |
| 3 | 0.941 | muslim 1869 d | `[dup=246095]` The above hadith has been narrated through several other chains with slight differences of wording. |
| 4 | 0.939 | muslim 127 c | The same hadith has been narrated by Zuhair b. Harb, Waki, Ishaq b. Mansur, Husain b. 'Ali. |
| 5 | 0.938 | muslim 1831 d | Abu Huraira has narrated this hadith similar to the above mentioned hadith. |
| 6 | 0.937 | muslim 1831 c | Abu Huraira has narrated this hadith with a slight variation of words. |
| 7 | 0.936 | muslim 1992 b | `[dup=246095]` The above hadith is narrated through a different chain with slight variation in wording. |

---

## 2. Dedup: ON vs OFF

Dedup collapses near-identical hadiths (`dupGroup>0`, cosine>0.93 in the english-openai index). Within each group the member with the highest collection authority wins (Bukhari > Muslim > … using COLLECTION_BOOSTS, score as tiebreaker).

### Query: *"comparing yourself to others"*

Raw top-10: 0 hits belonged to a dup group | After dedup: 10 results, 0 groups represented

**Dedup OFF** (raw top-10, chain-refs excluded)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.815 | forty 18 | — | The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | bukhari 6490 | — | Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superi |
| 3 | 0.793 | muslim 2963 a | — | Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at o |
| 4 | 0.787 | riyadussalihin 466 | — | Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at thos |
| 5 | 0.785 | muslim 2536 | — | 'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the p |
| 6 | 0.782 | abudawud 4092 | — | Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Alla |
| 7 | 0.782 | tirmidhi 2513 | — | Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you,  |
| 8 | 0.781 | adab 898 | — | Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male a |
| 9 | 0.779 | riyadussalihin 7 | — | Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does n |
| 10 | 0.775 | forty 19 | — | On the authority of Abu Abbas Abdullah bin Abbas (may Allah be pleased with him) who said: One day I |

**Dedup ON** (collection-boosted representative per group)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.815 | forty 18 | — | The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | bukhari 6490 | — | Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superi |
| 3 | 0.793 | muslim 2963 a | — | Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at o |
| 4 | 0.787 | riyadussalihin 466 | — | Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at thos |
| 5 | 0.785 | muslim 2536 | — | 'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the p |
| 6 | 0.782 | abudawud 4092 | — | Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Alla |
| 7 | 0.782 | tirmidhi 2513 | — | Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you,  |
| 8 | 0.781 | adab 898 | — | Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male a |
| 9 | 0.779 | riyadussalihin 7 | — | Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does n |
| 10 | 0.775 | forty 19 | — | On the authority of Abu Abbas Abdullah bin Abbas (may Allah be pleased with him) who said: One day I |

### Query: *"forgiveness of sins"*

Raw top-10: 1 hits belonged to a dup group | After dedup: 10 results, 1 groups represented

**Dedup OFF** (raw top-10, chain-refs excluded)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.876 | forty 28 | — | One who repents from sin is like someone without sin. |
| 2 | 0.852 | riyadussalihin 423 | — | Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said,  |
| 3 | 0.851 | bukhari 7507 | — | Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lo |
| 4 | 0.850 | bukhari 41 | — | Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embraces Islam sincerely,  |
| 5 | 0.850 | riyadussalihin 442 | 1604380 | Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted,  |
| 6 | 0.850 | bulugh 319 | — | Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to us |
| 7 | 0.848 | ibnmajah 3821 | — | It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Ex |
| 8 | 0.848 | riyadussalihin 421 | — | Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, |
| 9 | 0.848 | mishkat 2482 | — | Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, f |
| 10 | 0.846 | bukhari 2449 | — | Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his rep |

**Dedup ON** (collection-boosted representative per group)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.876 | forty 28 | — | One who repents from sin is like someone without sin. |
| 2 | 0.852 | riyadussalihin 423 | — | Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said,  |
| 3 | 0.851 | bukhari 7507 | — | Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lo |
| 4 | 0.850 | bukhari 41 | — | Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embraces Islam sincerely,  |
| 5 | 0.850 | riyadussalihin 442 | 1604380 | Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted,  |
| 6 | 0.850 | bulugh 319 | — | Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to us |
| 7 | 0.848 | ibnmajah 3821 | — | It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Ex |
| 8 | 0.848 | riyadussalihin 421 | — | Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, |
| 9 | 0.848 | mishkat 2482 | — | Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, f |
| 10 | 0.846 | bukhari 2449 | — | Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his rep |

### Query: *"prayer before sleeping"*

Raw top-10: 2 hits belonged to a dup group | After dedup: 10 results, 1 groups represented

**Dedup OFF** (raw top-10, chain-refs excluded)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.875 | bukhari 212 | — | Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to  |
| 2 | 0.870 | muslim 786 | — | 'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in |
| 3 | 0.864 | bukhari 997 | — | Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. |
| 4 | 0.858 | mishkat 604 | — | Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one |
| 5 | 0.857 | bukhari 512 | — | Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Wh |
| 6 | 0.856 | bukhari 213 | — | Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till  |
| 7 | 0.853 | muslim 787 | — | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets u |
| 8 | 0.853 | bulugh 390 | 216500 | Narrated Jabir (RA): Allah's Messenger (SAW) said, "If anyone is afraid that he may not get up in th |
| 9 | 0.852 | abudawud 856 | — | Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also |
| 10 | 0.852 | muslim 755 a | 216500 | Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may  |

**Dedup ON** (collection-boosted representative per group)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.875 | bukhari 212 | — | Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to  |
| 2 | 0.870 | muslim 786 | — | 'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in |
| 3 | 0.864 | bukhari 997 | — | Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. |
| 4 | 0.858 | mishkat 604 | — | Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one |
| 5 | 0.857 | bukhari 512 | — | Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Wh |
| 6 | 0.856 | bukhari 213 | — | Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till  |
| 7 | 0.853 | muslim 787 | — | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets u |
| 8 | 0.852 | abudawud 856 | — | Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also |
| 9 | 0.852 | muslim 755 a | 216500 | Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may  |
| 10 | 0.852 | ibnmajah 1187 | — | It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fears that he  |

### Query: *"fasting in Ramadan"*

Raw top-10: 1 hits belonged to a dup group | After dedup: 10 results, 1 groups represented

**Dedup OFF** (raw top-10, chain-refs excluded)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.889 | muslim 1162 a | 226020 | Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How |
| 2 | 0.889 | mishkat 1973 | — | Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just befo |
| 3 | 0.887 | bukhari 1914 | — | Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ra |
| 4 | 0.886 | nasai 2309 | — | Abu Saeed said: "We were traveling in Ramadan and among us were some who were fasting and some who w |
| 5 | 0.886 | muslim 1082 a | — | Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying |
| 6 | 0.886 | muslim 1159 o | — | 'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be up |
| 7 | 0.885 | tirmidhi 759 | — | Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with s |
| 8 | 0.885 | abudawud 2335 | — | Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just |
| 9 | 0.885 | mishkat 2028 | — | ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travellin |
| 10 | 0.885 | mishkat 2047 | — | Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it |

**Dedup ON** (collection-boosted representative per group)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.889 | muslim 1162 a | 226020 | Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How |
| 2 | 0.889 | mishkat 1973 | — | Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just befo |
| 3 | 0.887 | bukhari 1914 | — | Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ra |
| 4 | 0.886 | nasai 2309 | — | Abu Saeed said: "We were traveling in Ramadan and among us were some who were fasting and some who w |
| 5 | 0.886 | muslim 1082 a | — | Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying |
| 6 | 0.886 | muslim 1159 o | — | 'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be up |
| 7 | 0.885 | tirmidhi 759 | — | Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with s |
| 8 | 0.885 | abudawud 2335 | — | Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just |
| 9 | 0.885 | mishkat 2028 | — | ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travellin |
| 10 | 0.885 | mishkat 2047 | — | Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it |

### Query: *"visiting the sick"*

Raw top-10: 1 hits belonged to a dup group | After dedup: 10 results, 1 groups represented

**Dedup OFF** (raw top-10, chain-refs excluded)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.825 | muslim 2568 a | — | Abu Rabi' reported directly from Allah's Apostle (may peace upon him) as saying: The one who visits  |
| 2 | 0.820 | ahmad 975 | 5009750 | It was narrated that ‘Abdullah bin Nafi’ said: Abu Moosa al-Ash’ari visited al-Hasan bin ‘Ali when h |
| 3 | 0.819 | riyadussalihin 902 | — | 'Aishah (May Allah be pleased with her) reported: When the Prophet (PBUH) visited any ailing member  |
| 4 | 0.818 | ahmad 612 | — | It was narrated that ‘AbdurRahman bin Abi Laila said: Abu Moosa came to al-Hasan bin `Ali to visit h |
| 5 | 0.817 | bukhari 5689 | — | Narrated 'Urwa: Aisha used to recommend at-Talbina for the sick and for such a person as grieved ove |
| 6 | 0.817 | ibnmajah 1777 | — | It was narrated that Anas bin Malik said: “The Messenger of Allah (saw) said: ‘The person observing  |
| 7 | 0.817 | tirmidhi 2087 | — | Abu Sa'eed Al-Khudri narrated that the Messenger of Allah (S.A.W) said: "When one of you visits the  |
| 8 | 0.815 | bukhari 3046 | — | Narrated Abu Musa: The Prophet said, "Free the captives, feed the hungry and pay a visit to the sick |
| 9 | 0.813 | ahmad 955 | — | It was narrated from ‘Amr bin Huraith that he visited Hasan [when he was sick and ‘Ali was with him. |
| 10 | 0.812 | riyadussalihin 894 | — | Al-Bara' bin `Azib (May Allah be pleased with them) reported: Messenger of Allah (PBUH) has ordered  |

**Dedup ON** (collection-boosted representative per group)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.825 | muslim 2568 a | — | Abu Rabi' reported directly from Allah's Apostle (may peace upon him) as saying: The one who visits  |
| 2 | 0.820 | ahmad 975 | 5009750 | It was narrated that ‘Abdullah bin Nafi’ said: Abu Moosa al-Ash’ari visited al-Hasan bin ‘Ali when h |
| 3 | 0.819 | riyadussalihin 902 | — | 'Aishah (May Allah be pleased with her) reported: When the Prophet (PBUH) visited any ailing member  |
| 4 | 0.818 | ahmad 612 | — | It was narrated that ‘AbdurRahman bin Abi Laila said: Abu Moosa came to al-Hasan bin `Ali to visit h |
| 5 | 0.817 | bukhari 5689 | — | Narrated 'Urwa: Aisha used to recommend at-Talbina for the sick and for such a person as grieved ove |
| 6 | 0.817 | ibnmajah 1777 | — | It was narrated that Anas bin Malik said: “The Messenger of Allah (saw) said: ‘The person observing  |
| 7 | 0.817 | tirmidhi 2087 | — | Abu Sa'eed Al-Khudri narrated that the Messenger of Allah (S.A.W) said: "When one of you visits the  |
| 8 | 0.815 | bukhari 3046 | — | Narrated Abu Musa: The Prophet said, "Free the captives, feed the hungry and pay a visit to the sick |
| 9 | 0.813 | ahmad 955 | — | It was narrated from ‘Amr bin Huraith that he visited Hasan [when he was sick and ‘Ali was with him. |
| 10 | 0.812 | riyadussalihin 894 | — | Al-Bara' bin `Azib (May Allah be pleased with them) reported: Messenger of Allah (PBUH) has ordered  |

### Query: *"honoring one's parents"*

Raw top-10: 0 hits belonged to a dup group | After dedup: 10 results, 0 groups represented

**Dedup OFF** (raw top-10, chain-refs excluded)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.843 | adab 35 | — | Abu Usayd said, "We were with the Messenger of Allah, may Allah bless him and grant him peace, when  |
| 2 | 0.826 | adab 94 | — | Ibn 'Umar said, "Allah has called them the 'dutiful' (al-Abrar) because they are dutiful (birr) to t |
| 3 | 0.824 | abudawud 4435 | — | Narrated Al-Lajlaj al-Amiri: I was working in the market. A woman passed carrying a child. The peopl |
| 4 | 0.823 | adab 22 | — | Mu'adh said, "Bliss belongs to someone who is dutiful towards his parents. Allah Almighty will prolo |
| 5 | 0.821 | mishkat 1768 | — | Muhammad b. an-Nu‘man who traced the tradition back to the Prophet reported him as saying, “If anyon |
| 6 | 0.816 | ahmad 1408 | — | It was narrated that az-Zubair said: The Messenger of Allah (ﷺ) mentioned both of his parents togeth |
| 7 | 0.815 | nasai 2559 | — | It was narrated from 'Amr bin Shu'aib, from his father, that his grandfather said: "Eat, give charit |
| 8 | 0.812 | adab 1037 | — | Mu'awiya ibn Qurra said that his father said to him, "My son, when a man passes by you and says, 'Pe |
| 9 | 0.812 | abudawud 5142 | — | Narrated AbuUsayd Malik ibn Rabi'ah as-Sa'idi: While we were with the Messenger of Allah! (saws) a m |
| 10 | 0.811 | ibnmajah 3664 | — | It was narrated that Abu Usaid, Malik bin Rabi'ah, said: "While we were with the Prophet(SAW), a man |

**Dedup ON** (collection-boosted representative per group)
| # | Score | Collection Hadith# | DupGroup | Text |
|---|---|---|---|---|
| 1 | 0.843 | adab 35 | — | Abu Usayd said, "We were with the Messenger of Allah, may Allah bless him and grant him peace, when  |
| 2 | 0.826 | adab 94 | — | Ibn 'Umar said, "Allah has called them the 'dutiful' (al-Abrar) because they are dutiful (birr) to t |
| 3 | 0.824 | abudawud 4435 | — | Narrated Al-Lajlaj al-Amiri: I was working in the market. A woman passed carrying a child. The peopl |
| 4 | 0.823 | adab 22 | — | Mu'adh said, "Bliss belongs to someone who is dutiful towards his parents. Allah Almighty will prolo |
| 5 | 0.821 | mishkat 1768 | — | Muhammad b. an-Nu‘man who traced the tradition back to the Prophet reported him as saying, “If anyon |
| 6 | 0.816 | ahmad 1408 | — | It was narrated that az-Zubair said: The Messenger of Allah (ﷺ) mentioned both of his parents togeth |
| 7 | 0.815 | nasai 2559 | — | It was narrated from 'Amr bin Shu'aib, from his father, that his grandfather said: "Eat, give charit |
| 8 | 0.812 | adab 1037 | — | Mu'awiya ibn Qurra said that his father said to him, "My son, when a man passes by you and says, 'Pe |
| 9 | 0.812 | abudawud 5142 | — | Narrated AbuUsayd Malik ibn Rabi'ah as-Sa'idi: While we were with the Messenger of Allah! (saws) a m |
| 10 | 0.811 | ibnmajah 3664 | — | It was narrated that Abu Usaid, Malik bin Rabi'ah, said: "While we were with the Prophet(SAW), a man |

---

## 3. Size effect on HNSW traversal

The ES `semantic_text` query uses HNSW approximate nearest-neighbor internally. Requesting a larger `size` forces the HNSW graph walker to explore further, which can surface hadiths that a smaller traversal misses entirely. This table shows which top-10 results *change* as size increases.

> Dedup=ON throughout (fetch_size = size × 3). Chain-ref filter=ON.

### Query: *"comparing yourself to others"*

**Latency** (fetch_size = size × 3, then deduped)
| size | fetch_size | latency |
|---|---|---|
| 5 | 15 | 50ms |
| 10 | 30 | 91ms |
| 20 | 60 | 72ms |
| 50 | 150 | 105ms |

**Top-10 result stability across sizes**
Shows rank position (or — if absent) for each hadith across different size values.

| Collection/# | Text | size=5 | size=10 | size=20 | size=50 |
|---|---|---|---|---|---|
| bukhari 6490 | Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person | 1 | 2 | 2 | 2 |
| muslim 2963 a | Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When o | 2 | 3 | 3 | 3 |
| riyadussalihin 466 | Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) | 3 | 4 | 5 | 5 |
| muslim 2536 | 'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as  | 4 | 5 | 6 | 6 |
| abudawud 4092 | Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He sai | 5 | 6 | 7 | 7 |
| forty 18 | The felicitous person takes lessons from (the actions of) others. | — | 1 | 1 | 1 |
| tirmidhi 2513 | Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who | — | 7 | 8 | 8 |
| adab 898 | Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We creat | — | 8 | 9 | 9 |
| riyadussalihin 7 | Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) | — | 9 | 10 | 10 |
| forty 19 | On the authority of Abu Abbas Abdullah bin Abbas (may Allah be pleased with him) | — | 10 | — | — |
| adab 159 | Abu'd-Darda' used to say to people. "We know you better than the veterinarian kn | — | — | 4 | 4 |

**New hadiths surfaced at larger sizes** (not in size=5 top-10):
- First seen at size=10: **forty 19** (score 0.775) — On the authority of Abu Abbas Abdullah bin Abbas (may Allah be pleased with him) who said: One day I
- First seen at size=10: **tirmidhi 2513** (score 0.782) — Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, 
- First seen at size=10: **forty 18** (score 0.815) — The felicitous person takes lessons from (the actions of) others.
- First seen at size=10: **adab 898** (score 0.781) — Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male a
- First seen at size=10: **riyadussalihin 7** (score 0.779) — Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does n
- First seen at size=20: **adab 159** (score 0.791) — Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We 

### Query: *"forgiveness of sins"*

**Latency** (fetch_size = size × 3, then deduped)
| size | fetch_size | latency |
|---|---|---|
| 5 | 15 | 98ms |
| 10 | 30 | 84ms |
| 20 | 60 | 65ms |
| 50 | 150 | 123ms |

**Top-10 result stability across sizes**
Shows rank position (or — if absent) for each hadith across different size values.

| Collection/# | Text | size=5 | size=10 | size=20 | size=50 |
|---|---|---|---|---|---|
| forty 28 | One who repents from sin is like someone without sin. | 1 | 1 | 1 | 1 |
| riyadussalihin 423 | Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of | 2 | 2 | 2 | 2 |
| bukhari 7507 | Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and | 3 | 3 | 3 | 3 |
| bukhari 41 | Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embrac | 4 | 4 | 4 | 4 |
| riyadussalihin 442 | Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, " | 5 | 5 | 5 | 5 |
| bulugh 319 | Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me  | — | 6 | 6 | 6 |
| ibnmajah 3821 | It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah | — | 7 | 7 | 7 |
| riyadussalihin 421 | Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said,  | — | 8 | 8 | 8 |
| mishkat 2482 | Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this sup | — | 9 | 9 | 9 |
| bukhari 2449 | Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another perso | — | 10 | 10 | 10 |

**New hadiths surfaced at larger sizes** (not in size=5 top-10):
- First seen at size=10: **mishkat 2482** (score 0.848) — Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, f
- First seen at size=10: **bulugh 319** (score 0.850) — Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to us
- First seen at size=10: **bukhari 2449** (score 0.846) — Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his rep
- First seen at size=10: **riyadussalihin 421** (score 0.848) — Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted,
- First seen at size=10: **ibnmajah 3821** (score 0.848) — It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Ex

### Query: *"prayer before sleeping"*

**Latency** (fetch_size = size × 3, then deduped)
| size | fetch_size | latency |
|---|---|---|
| 5 | 15 | 116ms |
| 10 | 30 | 57ms |
| 20 | 60 | 96ms |
| 50 | 150 | 93ms |

**Top-10 result stability across sizes**
Shows rank position (or — if absent) for each hadith across different size values.

| Collection/# | Text | size=5 | size=10 | size=20 | size=50 |
|---|---|---|---|---|---|
| bukhari 212 | Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while pray | 1 | 1 | 1 | 1 |
| muslim 786 | 'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone  | 2 | 2 | 2 | 2 |
| bukhari 997 | Narrated `A'isha: The Prophet used to offer his night prayer while I was sleepin | 3 | 3 | 3 | 3 |
| mishkat 604 | Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, | 4 | 4 | 4 | 4 |
| bukhari 512 | Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed | 5 | 5 | 5 | 5 |
| bukhari 213 | Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, h | — | 6 | 6 | 6 |
| muslim 787 | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When a | — | 7 | 7 | 7 |
| abudawud 856 | Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered th | — | 8 | 8 | 8 |
| muslim 755 a | Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is | — | 9 | 9 | 9 |
| ibnmajah 1187 | It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever amon | — | 10 | 10 | 10 |

**New hadiths surfaced at larger sizes** (not in size=5 top-10):
- First seen at size=10: **ibnmajah 1187** (score 0.852) — It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fears that he 
- First seen at size=10: **bukhari 213** (score 0.856) — Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till 
- First seen at size=10: **muslim 787** (score 0.853) — Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets u
- First seen at size=10: **abudawud 856** (score 0.852) — Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also
- First seen at size=10: **muslim 755 a** (score 0.852) — Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may 

### Query: *"fasting in Ramadan"*

**Latency** (fetch_size = size × 3, then deduped)
| size | fetch_size | latency |
|---|---|---|
| 5 | 15 | 103ms |
| 10 | 30 | 67ms |
| 20 | 60 | 84ms |
| 50 | 150 | 122ms |

**Top-10 result stability across sizes**
Shows rank position (or — if absent) for each hadith across different size values.

| Collection/# | Text | size=5 | size=10 | size=20 | size=50 |
|---|---|---|---|---|---|
| muslim 1162 a | Abu Qatada reported that a person came to the Apostle of Allah (may peace be upo | 1 | 1 | 1 | 1 |
| mishkat 1973 | Abu Huraira reported God’s messenger as saying, “None of you must fast one day o | 2 | 2 | 2 | 2 |
| bukhari 1914 | Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two be | 3 | 3 | 3 | 3 |
| muslim 1082 a | Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be | 4 | 4 | 4 | 5 |
| muslim 1159 o | 'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Al | 5 | 5 | 5 | 6 |
| tirmidhi 759 | Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, th | — | 6 | 6 | 7 |
| abudawud 2335 | Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one  | — | 7 | 7 | 8 |
| mishkat 2028 | ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ram | — | 8 | 8 | 9 |
| mishkat 2047 | Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Rama | — | 9 | 9 | 10 |
| bukhari 1900 | Narrated Ibn `Umar: I heard Allah's Apostle saying, "When you see the crescent ( | — | 10 | 10 | — |
| nasai 2309 | Abu Saeed said: "We were traveling in Ramadan and among us were some who were fa | — | — | — | 4 |

**New hadiths surfaced at larger sizes** (not in size=5 top-10):
- First seen at size=10: **mishkat 2028** (score 0.885) — ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travellin
- First seen at size=10: **abudawud 2335** (score 0.885) — Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just
- First seen at size=10: **mishkat 2047** (score 0.885) — Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it
- First seen at size=10: **bukhari 1900** (score 0.885) — Narrated Ibn `Umar: I heard Allah's Apostle saying, "When you see the crescent (of the month of Rama
- First seen at size=10: **tirmidhi 759** (score 0.885) — Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with s
- First seen at size=50: **nasai 2309** (score 0.886) — Abu Saeed said: "We were traveling in Ramadan and among us were some who were fasting and some who w

### Query: *"visiting the sick"*

**Latency** (fetch_size = size × 3, then deduped)
| size | fetch_size | latency |
|---|---|---|
| 5 | 15 | 106ms |
| 10 | 30 | 74ms |
| 20 | 60 | 79ms |
| 50 | 150 | 91ms |

**Top-10 result stability across sizes**
Shows rank position (or — if absent) for each hadith across different size values.

| Collection/# | Text | size=5 | size=10 | size=20 | size=50 |
|---|---|---|---|---|---|
| muslim 2568 a | Abu Rabi' reported directly from Allah's Apostle (may peace upon him) as saying: | 1 | 1 | 1 | 1 |
| ahmad 975 | It was narrated that ‘Abdullah bin Nafi’ said: Abu Moosa al-Ash’ari visited al-H | 2 | 2 | 2 | 2 |
| riyadussalihin 902 | 'Aishah (May Allah be pleased with her) reported: When the Prophet (PBUH) visite | 3 | 3 | 3 | 3 |
| ahmad 612 | It was narrated that ‘AbdurRahman bin Abi Laila said: Abu Moosa came to al-Hasan | 4 | 4 | 4 | 4 |
| bukhari 5689 | Narrated 'Urwa: Aisha used to recommend at-Talbina for the sick and for such a p | 5 | 5 | 5 | 5 |
| ibnmajah 1777 | It was narrated that Anas bin Malik said: “The Messenger of Allah (saw) said: ‘T | — | 6 | 6 | 6 |
| tirmidhi 2087 | Abu Sa'eed Al-Khudri narrated that the Messenger of Allah (S.A.W) said: "When on | — | 7 | 7 | 7 |
| bukhari 3046 | Narrated Abu Musa: The Prophet said, "Free the captives, feed the hungry and pay | — | 8 | 8 | 8 |
| ahmad 955 | It was narrated from ‘Amr bin Huraith that he visited Hasan [when he was sick an | — | 9 | 9 | 9 |
| riyadussalihin 894 | Al-Bara' bin `Azib (May Allah be pleased with them) reported: Messenger of Allah | — | 10 | 10 | — |
| forty 6 | Seek help for any needs discreetly. | — | — | — | 10 |

**New hadiths surfaced at larger sizes** (not in size=5 top-10):
- First seen at size=10: **ibnmajah 1777** (score 0.817) — It was narrated that Anas bin Malik said: “The Messenger of Allah (saw) said: ‘The person observing 
- First seen at size=10: **bukhari 3046** (score 0.815) — Narrated Abu Musa: The Prophet said, "Free the captives, feed the hungry and pay a visit to the sick
- First seen at size=10: **ahmad 955** (score 0.813) — It was narrated from ‘Amr bin Huraith that he visited Hasan [when he was sick and ‘Ali was with him.
- First seen at size=10: **riyadussalihin 894** (score 0.812) — Al-Bara' bin `Azib (May Allah be pleased with them) reported: Messenger of Allah (PBUH) has ordered 
- First seen at size=10: **tirmidhi 2087** (score 0.817) — Abu Sa'eed Al-Khudri narrated that the Messenger of Allah (S.A.W) said: "When one of you visits the 
- First seen at size=50: **forty 6** (score 0.812) — Seek help for any needs discreetly.

### Query: *"honoring one's parents"*

**Latency** (fetch_size = size × 3, then deduped)
| size | fetch_size | latency |
|---|---|---|
| 5 | 15 | 51ms |
| 10 | 30 | 88ms |
| 20 | 60 | 89ms |
| 50 | 150 | 100ms |

**Top-10 result stability across sizes**
Shows rank position (or — if absent) for each hadith across different size values.

| Collection/# | Text | size=5 | size=10 | size=20 | size=50 |
|---|---|---|---|---|---|
| adab 35 | Abu Usayd said, "We were with the Messenger of Allah, may Allah bless him and gr | 1 | 1 | 1 | 1 |
| adab 94 | Ibn 'Umar said, "Allah has called them the 'dutiful' (al-Abrar) because they are | 2 | 2 | 2 | 2 |
| abudawud 4435 | Narrated Al-Lajlaj al-Amiri: I was working in the market. A woman passed carryin | 3 | 3 | 3 | 3 |
| adab 22 | Mu'adh said, "Bliss belongs to someone who is dutiful towards his parents. Allah | 4 | 4 | 4 | 4 |
| mishkat 1768 | Muhammad b. an-Nu‘man who traced the tradition back to the Prophet reported him  | 5 | 5 | 5 | 5 |
| ahmad 1408 | It was narrated that az-Zubair said: The Messenger of Allah (ﷺ) mentioned both o | — | 6 | 6 | 6 |
| nasai 2559 | It was narrated from 'Amr bin Shu'aib, from his father, that his grandfather sai | — | 7 | 7 | 10 |
| adab 1037 | Mu'awiya ibn Qurra said that his father said to him, "My son, when a man passes  | — | 8 | 8 | — |
| abudawud 5142 | Narrated AbuUsayd Malik ibn Rabi'ah as-Sa'idi: While we were with the Messenger  | — | 9 | 9 | — |
| ibnmajah 3664 | It was narrated that Abu Usaid, Malik bin Rabi'ah, said: "While we were with the | — | 10 | 10 | — |
| muslim 2552 b | 'Abdullah b. Umar reported Allah's Apostle (may peace be upon him) as saying: Th | — | — | — | 7 |
| hisn 145 | Bārakallāhu laka fi ‘l-mawhūbi lak, wa shakarta ‘l-wāhib, wa balagha ashuddah, w | — | — | — | 8 |
| mishkat 1319 | ‘A’isha used to pray eight rak'as in the forenoon, then say, “If my parents were | — | — | — | 9 |

**New hadiths surfaced at larger sizes** (not in size=5 top-10):
- First seen at size=10: **ahmad 1408** (score 0.816) — It was narrated that az-Zubair said: The Messenger of Allah (ﷺ) mentioned both of his parents togeth
- First seen at size=10: **nasai 2559** (score 0.815) — It was narrated from 'Amr bin Shu'aib, from his father, that his grandfather said: "Eat, give charit
- First seen at size=10: **ibnmajah 3664** (score 0.811) — It was narrated that Abu Usaid, Malik bin Rabi'ah, said: "While we were with the Prophet(SAW), a man
- First seen at size=10: **adab 1037** (score 0.812) — Mu'awiya ibn Qurra said that his father said to him, "My son, when a man passes by you and says, 'Pe
- First seen at size=10: **abudawud 5142** (score 0.812) — Narrated AbuUsayd Malik ibn Rabi'ah as-Sa'idi: While we were with the Messenger of Allah! (saws) a m
- First seen at size=50: **hisn 145** (score 0.815) — Bārakallāhu laka fi ‘l-mawhūbi lak, wa shakarta ‘l-wāhib, wa balagha ashuddah, wa ruziqta birrah. Th
- First seen at size=50: **muslim 2552 b** (score 0.815) — 'Abdullah b. Umar reported Allah's Apostle (may peace be upon him) as saying: The finest act of good
- First seen at size=50: **mishkat 1319** (score 0.815) — ‘A’isha used to pray eight rak'as in the forenoon, then say, “If my parents were brought back to lif

---

*Generated by `tests/mxbai_filter_report.py`*
