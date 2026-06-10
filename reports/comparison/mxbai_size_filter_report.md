# mxbai HNSW Size & Filter Report

Index: `english-mxbai` | 48,703 docs | 1,574 chain-refs (3.2%) | 6,405 in dup groups (13.2%)

**Production config**: size=75, chain-ref filter=ON, dedup=ON (fetch 75×3=225, collapse to 75)

---

## 1. Filter combinations at size=75

Each row shows whether a result would survive production filters (chain-ref + dedup both ON).
⚠CHAIN = chain-reference hadith | [dup=N] = belongs to duplicate group N

### Query: *"aisha"*

No-filter top-10: **0 chain-refs**, **0 dup groups represented**

**No filters (raw)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.850 | bukhari 3894 |  Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then I got ill and my hair fell down. Later on my hair grew (again) and my mother, Um Ruman, came to me w |
| 2 | 0.847 | bukhari 277 |  Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head with one hand and rubbed the left side of the head with the other hand. |
| 3 | 0.845 | abudawud 4164 |  Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing with henna. She replied: There is no harm, but I do not like it. My beloved, the Messenger of Allah (s |
| 4 | 0.844 | bukhari 2661 |  Narrated Aisha: (the wife of the Prophet) "Whenever Allah's Apostle intended to go on a journey, he would draw lots amongst his wives and would take with him the one upon whom the lot fell. During a Ghazwa of his, he drew lots amongst us and the lot  |
| 5 | 0.843 | bukhari 1151 |  Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I said, "(She is) So and so. She does not sleep at night because she is engaged in prayer." The Prophet s |
| 6 | 0.842 | bukhari 902 |  Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of four miles or more from Medina). They used to pass through dust and used to be drenched with sweat an |
| 7 | 0.842 | bukhari 4573 |  Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of that and not because he loved her. So the Divine Verse came regarding his case: "If you fear that yo |
| 8 | 0.841 | bukhari 43 |  Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her (excessive) praying. He said disapprovingly, "Do (good) deeds which is within your capacity (withou |
| 9 | 0.839 | abudawud 3708 |  Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays, and asked her about mixing dried dates and raisins (for drink). She replied: I used to take a handful of dried dates and a handful |
| 10 | 0.838 | abudawud 288 |  'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, had a flow of blood for seven years. She asked the Messenger of Allah (saws) about it. The Messenger |

**Chain-ref filter ON only**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.850 | bukhari 3894 |  Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then I got ill and my hair fell down. Later on my hair grew (again) and my mother, Um Ruman, came to me w |
| 2 | 0.847 | bukhari 277 |  Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head with one hand and rubbed the left side of the head with the other hand. |
| 3 | 0.845 | abudawud 4164 |  Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing with henna. She replied: There is no harm, but I do not like it. My beloved, the Messenger of Allah (s |
| 4 | 0.844 | bukhari 2661 |  Narrated Aisha: (the wife of the Prophet) "Whenever Allah's Apostle intended to go on a journey, he would draw lots amongst his wives and would take with him the one upon whom the lot fell. During a Ghazwa of his, he drew lots amongst us and the lot  |
| 5 | 0.843 | bukhari 1151 |  Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I said, "(She is) So and so. She does not sleep at night because she is engaged in prayer." The Prophet s |
| 6 | 0.842 | bukhari 902 |  Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of four miles or more from Medina). They used to pass through dust and used to be drenched with sweat an |
| 7 | 0.842 | bukhari 4573 |  Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of that and not because he loved her. So the Divine Verse came regarding his case: "If you fear that yo |
| 8 | 0.841 | bukhari 43 |  Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her (excessive) praying. He said disapprovingly, "Do (good) deeds which is within your capacity (withou |
| 9 | 0.839 | abudawud 3708 |  Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays, and asked her about mixing dried dates and raisins (for drink). She replied: I used to take a handful of dried dates and a handful |
| 10 | 0.838 | abudawud 288 |  'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, had a flow of blood for seven years. She asked the Messenger of Allah (saws) about it. The Messenger |

**Dedup ON only (chain-refs still included)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.850 | bukhari 3894 |  Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then I got ill and my hair fell down. Later on my hair grew (again) and my mother, Um Ruman, came to me w |
| 2 | 0.847 | bukhari 277 |  Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head with one hand and rubbed the left side of the head with the other hand. |
| 3 | 0.845 | abudawud 4164 |  Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing with henna. She replied: There is no harm, but I do not like it. My beloved, the Messenger of Allah (s |
| 4 | 0.844 | bukhari 2661 |  Narrated Aisha: (the wife of the Prophet) "Whenever Allah's Apostle intended to go on a journey, he would draw lots amongst his wives and would take with him the one upon whom the lot fell. During a Ghazwa of his, he drew lots amongst us and the lot  |
| 5 | 0.843 | bukhari 1151 |  Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I said, "(She is) So and so. She does not sleep at night because she is engaged in prayer." The Prophet s |
| 6 | 0.842 | bukhari 902 |  Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of four miles or more from Medina). They used to pass through dust and used to be drenched with sweat an |
| 7 | 0.842 | bukhari 4573 |  Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of that and not because he loved her. So the Divine Verse came regarding his case: "If you fear that yo |
| 8 | 0.841 | bukhari 43 |  Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her (excessive) praying. He said disapprovingly, "Do (good) deeds which is within your capacity (withou |
| 9 | 0.839 | abudawud 3708 |  Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays, and asked her about mixing dried dates and raisins (for drink). She replied: I used to take a handful of dried dates and a handful |
| 10 | 0.838 | abudawud 288 |  'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, had a flow of blood for seven years. She asked the Messenger of Allah (saws) about it. The Messenger |

****PRODUCTION: chain-ref + dedup both ON****
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.850 | bukhari 3894 |  Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then I got ill and my hair fell down. Later on my hair grew (again) and my mother, Um Ruman, came to me w |
| 2 | 0.847 | bukhari 277 |  Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head with one hand and rubbed the left side of the head with the other hand. |
| 3 | 0.845 | abudawud 4164 |  Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing with henna. She replied: There is no harm, but I do not like it. My beloved, the Messenger of Allah (s |
| 4 | 0.844 | bukhari 2661 |  Narrated Aisha: (the wife of the Prophet) "Whenever Allah's Apostle intended to go on a journey, he would draw lots amongst his wives and would take with him the one upon whom the lot fell. During a Ghazwa of his, he drew lots amongst us and the lot  |
| 5 | 0.843 | bukhari 1151 |  Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I said, "(She is) So and so. She does not sleep at night because she is engaged in prayer." The Prophet s |
| 6 | 0.842 | bukhari 902 |  Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of four miles or more from Medina). They used to pass through dust and used to be drenched with sweat an |
| 7 | 0.842 | bukhari 4573 |  Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of that and not because he loved her. So the Divine Verse came regarding his case: "If you fear that yo |
| 8 | 0.841 | bukhari 43 |  Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her (excessive) praying. He said disapprovingly, "Do (good) deeds which is within your capacity (withou |
| 9 | 0.839 | abudawud 3708 |  Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays, and asked her about mixing dried dates and raisins (for drink). She replied: I used to take a handful of dried dates and a handful |
| 10 | 0.838 | abudawud 288 |  'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, had a flow of blood for seven years. She asked the Messenger of Allah (saws) about it. The Messenger |

### Query: *"comparing yourself to others"*

No-filter top-10: **1 chain-refs**, **0 dup groups represented**

**No filters (raw)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.815 | forty 18 |  The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | bukhari 6490 |  Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him. |
| 3 | 0.793 | muslim 2963 a |  Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you in reg |
| 4 | 0.791 | adab 159 |  Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. The best of you is the one whose good is hoped for and the one whose evil you are safe from. As for t |
| 5 | 0.787 | riyadussalihin 466 |  Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you." This is the |
| 6 | 0.785 | muslim 2536 |  'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to which I belong, then of the second generation (generation adjacent to my generation), then of the t |
| 7 | 0.783 | nasai 384b | `⚠CHAIN` (Another chain) with similarity. |
| 8 | 0.782 | abudawud 4092 |  Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been given some of it, as you see. And I do not like that anyone excels me (in respect of beauty). Perhaps  |
| 9 | 0.782 | tirmidhi 2513 |  Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indeed that is more worthy(so that you will) not belittle Allah's favors upon you." |
| 10 | 0.781 | adab 898 |  Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes so that you might come to know each other. The noblest among you in Allah's sight is the one with th |

**Chain-ref filter ON only**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.815 | forty 18 |  The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | bukhari 6490 |  Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him. |
| 3 | 0.793 | muslim 2963 a |  Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you in reg |
| 4 | 0.791 | adab 159 |  Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. The best of you is the one whose good is hoped for and the one whose evil you are safe from. As for t |
| 5 | 0.787 | riyadussalihin 466 |  Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you." This is the |
| 6 | 0.785 | muslim 2536 |  'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to which I belong, then of the second generation (generation adjacent to my generation), then of the t |
| 7 | 0.782 | abudawud 4092 |  Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been given some of it, as you see. And I do not like that anyone excels me (in respect of beauty). Perhaps  |
| 8 | 0.782 | tirmidhi 2513 |  Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indeed that is more worthy(so that you will) not belittle Allah's favors upon you." |
| 9 | 0.781 | adab 898 |  Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes so that you might come to know each other. The noblest among you in Allah's sight is the one with th |
| 10 | 0.779 | riyadussalihin 7 |  Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does not look at your figures, nor at your attire but He looks at your hearts and accomplishments". [Muslim] . |

**Dedup ON only (chain-refs still included)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.815 | forty 18 |  The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | bukhari 6490 |  Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him. |
| 3 | 0.793 | muslim 2963 a |  Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you in reg |
| 4 | 0.791 | adab 159 |  Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. The best of you is the one whose good is hoped for and the one whose evil you are safe from. As for t |
| 5 | 0.787 | riyadussalihin 466 |  Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you." This is the |
| 6 | 0.785 | muslim 2536 |  'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to which I belong, then of the second generation (generation adjacent to my generation), then of the t |
| 7 | 0.783 | nasai 384b | `⚠CHAIN` (Another chain) with similarity. |
| 8 | 0.782 | abudawud 4092 |  Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been given some of it, as you see. And I do not like that anyone excels me (in respect of beauty). Perhaps  |
| 9 | 0.782 | tirmidhi 2513 |  Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indeed that is more worthy(so that you will) not belittle Allah's favors upon you." |
| 10 | 0.781 | adab 898 |  Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes so that you might come to know each other. The noblest among you in Allah's sight is the one with th |

****PRODUCTION: chain-ref + dedup both ON****
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.815 | forty 18 |  The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.802 | bukhari 6490 |  Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him. |
| 3 | 0.793 | muslim 2963 a |  Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you in reg |
| 4 | 0.791 | adab 159 |  Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. The best of you is the one whose good is hoped for and the one whose evil you are safe from. As for t |
| 5 | 0.787 | riyadussalihin 466 |  Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you." This is the |
| 6 | 0.785 | muslim 2536 |  'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to which I belong, then of the second generation (generation adjacent to my generation), then of the t |
| 7 | 0.782 | abudawud 4092 |  Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been given some of it, as you see. And I do not like that anyone excels me (in respect of beauty). Perhaps  |
| 8 | 0.782 | tirmidhi 2513 |  Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indeed that is more worthy(so that you will) not belittle Allah's favors upon you." |
| 9 | 0.781 | adab 898 |  Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes so that you might come to know each other. The noblest among you in Allah's sight is the one with th |
| 10 | 0.779 | riyadussalihin 7 |  Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does not look at your figures, nor at your attire but He looks at your hearts and accomplishments". [Muslim] . |

### Query: *"forgiveness of sins"*

No-filter top-10: **0 chain-refs**, **1 dup groups represented**

**No filters (raw)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.876 | forty 28 |  One who repents from sin is like someone without sin. |
| 2 | 0.852 | riyadussalihin 423 |  Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Were you not to commit sins, Allah would create people who would commit sins and ask for forgiveness and He would forgive them". [Muslim] . |
| 3 | 0.851 | bukhari 7507 |  Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lord! I have sinned, please forgive me!' and his Lord says, 'My slave has known that he has a Lord who forgives sins and punishes for it, I therefore ha |
| 4 | 0.850 | bukhari 41 |  Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embraces Islam sincerely, then Allah shall forgive all his past sins, and after that starts the settlement of accounts, the reward of his good deeds will be ten times to seven  |
| 5 | 0.850 | riyadussalihin 442 | `[dup-rep=1604380]` Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted, has said: 'O son of adam, I forgive you as long as you pray to Me and hope for My forgiveness, whatever sins you have committed. O son of 'Adam, I do  |
| 6 | 0.850 | bulugh 319 |  Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I have greatly wronged myself, and no one forgives sins except You, so grant me forgiveness from You an |
| 7 | 0.848 | ibnmajah 3821 |  It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Exalted, said: 'Whoever does one good deed will have (the reward of) ten like it and more, and whoever does a bad deed will have one like it, or I will  |
| 8 | 0.848 | riyadussalihin 421 |  Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, and Glorious said: 'A slave committed a sin and he said: O Allah, forgive my sin,' and Allah said: 'My slave committed a sin and then he realized tha |
| 9 | 0.848 | mishkat 2482 |  Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, forgive me my sin, my ignorance, my extravagance in my affairs, and what Thou knowest better than I do. O God, forgive me my serious and my frivolous s |
| 10 | 0.846 | bukhari 2449 |  Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his reputation or anything else, he should beg him to forgive him before the Day of Resurrection when there will be no money (to compensate for wrong deeds), |

**Chain-ref filter ON only**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.876 | forty 28 |  One who repents from sin is like someone without sin. |
| 2 | 0.852 | riyadussalihin 423 |  Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Were you not to commit sins, Allah would create people who would commit sins and ask for forgiveness and He would forgive them". [Muslim] . |
| 3 | 0.851 | bukhari 7507 |  Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lord! I have sinned, please forgive me!' and his Lord says, 'My slave has known that he has a Lord who forgives sins and punishes for it, I therefore ha |
| 4 | 0.850 | bukhari 41 |  Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embraces Islam sincerely, then Allah shall forgive all his past sins, and after that starts the settlement of accounts, the reward of his good deeds will be ten times to seven  |
| 5 | 0.850 | riyadussalihin 442 | `[dup-rep=1604380]` Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted, has said: 'O son of adam, I forgive you as long as you pray to Me and hope for My forgiveness, whatever sins you have committed. O son of 'Adam, I do  |
| 6 | 0.850 | bulugh 319 |  Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I have greatly wronged myself, and no one forgives sins except You, so grant me forgiveness from You an |
| 7 | 0.848 | ibnmajah 3821 |  It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Exalted, said: 'Whoever does one good deed will have (the reward of) ten like it and more, and whoever does a bad deed will have one like it, or I will  |
| 8 | 0.848 | riyadussalihin 421 |  Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, and Glorious said: 'A slave committed a sin and he said: O Allah, forgive my sin,' and Allah said: 'My slave committed a sin and then he realized tha |
| 9 | 0.848 | mishkat 2482 |  Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, forgive me my sin, my ignorance, my extravagance in my affairs, and what Thou knowest better than I do. O God, forgive me my serious and my frivolous s |
| 10 | 0.846 | bukhari 2449 |  Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his reputation or anything else, he should beg him to forgive him before the Day of Resurrection when there will be no money (to compensate for wrong deeds), |

**Dedup ON only (chain-refs still included)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.876 | forty 28 |  One who repents from sin is like someone without sin. |
| 2 | 0.852 | riyadussalihin 423 |  Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Were you not to commit sins, Allah would create people who would commit sins and ask for forgiveness and He would forgive them". [Muslim] . |
| 3 | 0.851 | bukhari 7507 |  Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lord! I have sinned, please forgive me!' and his Lord says, 'My slave has known that he has a Lord who forgives sins and punishes for it, I therefore ha |
| 4 | 0.850 | bukhari 41 |  Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embraces Islam sincerely, then Allah shall forgive all his past sins, and after that starts the settlement of accounts, the reward of his good deeds will be ten times to seven  |
| 5 | 0.850 | riyadussalihin 442 | `[dup-rep=1604380]` Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted, has said: 'O son of adam, I forgive you as long as you pray to Me and hope for My forgiveness, whatever sins you have committed. O son of 'Adam, I do  |
| 6 | 0.850 | bulugh 319 |  Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I have greatly wronged myself, and no one forgives sins except You, so grant me forgiveness from You an |
| 7 | 0.848 | ibnmajah 3821 |  It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Exalted, said: 'Whoever does one good deed will have (the reward of) ten like it and more, and whoever does a bad deed will have one like it, or I will  |
| 8 | 0.848 | riyadussalihin 421 |  Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, and Glorious said: 'A slave committed a sin and he said: O Allah, forgive my sin,' and Allah said: 'My slave committed a sin and then he realized tha |
| 9 | 0.848 | mishkat 2482 |  Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, forgive me my sin, my ignorance, my extravagance in my affairs, and what Thou knowest better than I do. O God, forgive me my serious and my frivolous s |
| 10 | 0.846 | bukhari 2449 |  Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his reputation or anything else, he should beg him to forgive him before the Day of Resurrection when there will be no money (to compensate for wrong deeds), |

****PRODUCTION: chain-ref + dedup both ON****
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.876 | forty 28 |  One who repents from sin is like someone without sin. |
| 2 | 0.852 | riyadussalihin 423 |  Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Were you not to commit sins, Allah would create people who would commit sins and ask for forgiveness and He would forgive them". [Muslim] . |
| 3 | 0.851 | bukhari 7507 |  Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lord! I have sinned, please forgive me!' and his Lord says, 'My slave has known that he has a Lord who forgives sins and punishes for it, I therefore ha |
| 4 | 0.850 | bukhari 41 |  Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embraces Islam sincerely, then Allah shall forgive all his past sins, and after that starts the settlement of accounts, the reward of his good deeds will be ten times to seven  |
| 5 | 0.850 | riyadussalihin 442 | `[dup-rep=1604380]` Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted, has said: 'O son of adam, I forgive you as long as you pray to Me and hope for My forgiveness, whatever sins you have committed. O son of 'Adam, I do  |
| 6 | 0.850 | bulugh 319 |  Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I have greatly wronged myself, and no one forgives sins except You, so grant me forgiveness from You an |
| 7 | 0.848 | ibnmajah 3821 |  It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Exalted, said: 'Whoever does one good deed will have (the reward of) ten like it and more, and whoever does a bad deed will have one like it, or I will  |
| 8 | 0.848 | riyadussalihin 421 |  Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, and Glorious said: 'A slave committed a sin and he said: O Allah, forgive my sin,' and Allah said: 'My slave committed a sin and then he realized tha |
| 9 | 0.848 | mishkat 2482 |  Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, forgive me my sin, my ignorance, my extravagance in my affairs, and what Thou knowest better than I do. O God, forgive me my serious and my frivolous s |
| 10 | 0.846 | bukhari 2449 |  Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his reputation or anything else, he should beg him to forgive him before the Day of Resurrection when there will be no money (to compensate for wrong deeds), |

### Query: *"prayer before sleeping"*

No-filter top-10: **0 chain-refs**, **1 dup groups represented**

**No filters (raw)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.875 | bukhari 212 |  Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep) till his slumber is over because in praying while drowsy one does not know whether one is asking for forgiveness or for a bad thing for on |
| 2 | 0.870 | muslim 786 |  'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in prayer, he should sleep, till sleep is gone, for when one of you prays while dozing he does not know whether he may be asking pardon or vilifying him |
| 3 | 0.864 | bukhari 997 |  Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he used to wake me up and I would offer the witr prayer too. |
| 4 | 0.858 | mishkat 604 |  Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one is awake that there is remissness; so when any of you forgets a stated prayer or oversleeps, he should observe it when he remembers it, for God has s |
| 5 | 0.857 | bukhari 512 |  Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Whenever he wanted to pray witr, he would wake me up and I would pray witr. |
| 6 | 0.856 | bukhari 213 |  Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till he understands what he is saying (reciting). |
| 7 | 0.853 | muslim 787 |  Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets up at night (for prayer) and his tongue falters in (the recitation) of the Qar'an, and he does not know what he is reciting, he should go to sleep. |
| 8 | 0.853 | bulugh 390 | `[dup-rep=216500]` Narrated Jabir (RA): Allah's Messenger (SAW) said, "If anyone is afraid that he may not get up in the latter part of the night, he should offer Witr in the first part of it; and if anyone expects to get up in the last part of it, he should offer Witr |
| 9 | 0.852 | abudawud 856 |  Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also entered it and prayed. He then came and saluted the Messenger of Allah(may peace be upon him). The Messenger of Allah(may peace be upon him) returned |
| 10 | 0.852 | muslim 755 a | `[dup-rep=216500]` Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he should observe Witr in the first part of it; and if anyone is eager to get up in the last part of it, h |

**Chain-ref filter ON only**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.875 | bukhari 212 |  Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep) till his slumber is over because in praying while drowsy one does not know whether one is asking for forgiveness or for a bad thing for on |
| 2 | 0.870 | muslim 786 |  'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in prayer, he should sleep, till sleep is gone, for when one of you prays while dozing he does not know whether he may be asking pardon or vilifying him |
| 3 | 0.864 | bukhari 997 |  Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he used to wake me up and I would offer the witr prayer too. |
| 4 | 0.858 | mishkat 604 |  Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one is awake that there is remissness; so when any of you forgets a stated prayer or oversleeps, he should observe it when he remembers it, for God has s |
| 5 | 0.857 | bukhari 512 |  Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Whenever he wanted to pray witr, he would wake me up and I would pray witr. |
| 6 | 0.856 | bukhari 213 |  Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till he understands what he is saying (reciting). |
| 7 | 0.853 | muslim 787 |  Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets up at night (for prayer) and his tongue falters in (the recitation) of the Qar'an, and he does not know what he is reciting, he should go to sleep. |
| 8 | 0.853 | bulugh 390 | `[dup-rep=216500]` Narrated Jabir (RA): Allah's Messenger (SAW) said, "If anyone is afraid that he may not get up in the latter part of the night, he should offer Witr in the first part of it; and if anyone expects to get up in the last part of it, he should offer Witr |
| 9 | 0.852 | abudawud 856 |  Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also entered it and prayed. He then came and saluted the Messenger of Allah(may peace be upon him). The Messenger of Allah(may peace be upon him) returned |
| 10 | 0.852 | muslim 755 a | `[dup-rep=216500]` Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he should observe Witr in the first part of it; and if anyone is eager to get up in the last part of it, h |

**Dedup ON only (chain-refs still included)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.875 | bukhari 212 |  Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep) till his slumber is over because in praying while drowsy one does not know whether one is asking for forgiveness or for a bad thing for on |
| 2 | 0.870 | muslim 786 |  'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in prayer, he should sleep, till sleep is gone, for when one of you prays while dozing he does not know whether he may be asking pardon or vilifying him |
| 3 | 0.864 | bukhari 997 |  Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he used to wake me up and I would offer the witr prayer too. |
| 4 | 0.858 | mishkat 604 |  Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one is awake that there is remissness; so when any of you forgets a stated prayer or oversleeps, he should observe it when he remembers it, for God has s |
| 5 | 0.857 | bukhari 512 |  Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Whenever he wanted to pray witr, he would wake me up and I would pray witr. |
| 6 | 0.856 | bukhari 213 |  Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till he understands what he is saying (reciting). |
| 7 | 0.853 | muslim 787 |  Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets up at night (for prayer) and his tongue falters in (the recitation) of the Qar'an, and he does not know what he is reciting, he should go to sleep. |
| 8 | 0.852 | abudawud 856 |  Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also entered it and prayed. He then came and saluted the Messenger of Allah(may peace be upon him). The Messenger of Allah(may peace be upon him) returned |
| 9 | 0.852 | muslim 755 a | `[dup-rep=216500]` Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he should observe Witr in the first part of it; and if anyone is eager to get up in the last part of it, h |
| 10 | 0.852 | ibnmajah 1187 |  It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fears that he will not wake up at the end of the night, let him pray Witr at the beginning of the night, then go to sleep. Whoever hopes that he will wake up at the |

****PRODUCTION: chain-ref + dedup both ON****
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.875 | bukhari 212 |  Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep) till his slumber is over because in praying while drowsy one does not know whether one is asking for forgiveness or for a bad thing for on |
| 2 | 0.870 | muslim 786 |  'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in prayer, he should sleep, till sleep is gone, for when one of you prays while dozing he does not know whether he may be asking pardon or vilifying him |
| 3 | 0.864 | bukhari 997 |  Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he used to wake me up and I would offer the witr prayer too. |
| 4 | 0.858 | mishkat 604 |  Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one is awake that there is remissness; so when any of you forgets a stated prayer or oversleeps, he should observe it when he remembers it, for God has s |
| 5 | 0.857 | bukhari 512 |  Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Whenever he wanted to pray witr, he would wake me up and I would pray witr. |
| 6 | 0.856 | bukhari 213 |  Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till he understands what he is saying (reciting). |
| 7 | 0.853 | muslim 787 |  Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets up at night (for prayer) and his tongue falters in (the recitation) of the Qar'an, and he does not know what he is reciting, he should go to sleep. |
| 8 | 0.852 | abudawud 856 |  Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also entered it and prayed. He then came and saluted the Messenger of Allah(may peace be upon him). The Messenger of Allah(may peace be upon him) returned |
| 9 | 0.852 | muslim 755 a | `[dup-rep=216500]` Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he should observe Witr in the first part of it; and if anyone is eager to get up in the last part of it, h |
| 10 | 0.852 | ibnmajah 1187 |  It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fears that he will not wake up at the end of the night, let him pray Witr at the beginning of the night, then go to sleep. Whoever hopes that he will wake up at the |

### Query: *"fasting in Ramadan"*

No-filter top-10: **0 chain-refs**, **1 dup groups represented**

**No filters (raw)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.889 | muslim 1162 a | `[dup-rep=226020]` Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How do you fast? The Messenger of Allah (may peace be upon him) felt annoyed. When 'Umar (Allah be pleased with him) noticed his annoyance, he said: We a |
| 2 | 0.889 | mishkat 1973 |  Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing a particular fast, for he may fast on that day.”* *If a man is in the h |
| 3 | 0.887 | bukhari 1914 |  Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ramadan unless he has the habit of fasting (Nawafil) (and if his fasting coincides with that day) then he can fast that day." |
| 4 | 0.886 | nasai 2309 |  Abu Saeed said: "We were traveling in Ramadan and among us were some who were fasting and some who were not. Those who were fasting did not criticize those who were not, and those who were not fasting did not criticize those who were." |
| 5 | 0.886 | muslim 1082 a |  Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: Do not observe fast for a day, or two days ahead of Ramadan except a person who is in the habit of observing a particular fast; he may fast on that  |
| 6 | 0.886 | muslim 1159 o |  'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be upon him) said to me! 'Abdullah b. 'Amr, it has been conveyed to me that you observe fast during the day and stand in prayer during the whole night. Don |
| 7 | 0.885 | tirmidhi 759 |  Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with six from Shawwal, then that is (equal in reward) to fasting everyday." |
| 8 | 0.885 | abudawud 2335 |  Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing the particular fast, for he may fast on that day. |
| 9 | 0.885 | mishkat 2028 |  ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travelling is like one who breaks his fast when not travelling.” Ibn Majah transmitted it. |
| 10 | 0.885 | mishkat 2047 |  Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it with six days in Shawwal, it will be like a perpetual fast.” Muslim transmitted it. |

**Chain-ref filter ON only**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.889 | muslim 1162 a | `[dup-rep=226020]` Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How do you fast? The Messenger of Allah (may peace be upon him) felt annoyed. When 'Umar (Allah be pleased with him) noticed his annoyance, he said: We a |
| 2 | 0.889 | mishkat 1973 |  Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing a particular fast, for he may fast on that day.”* *If a man is in the h |
| 3 | 0.887 | bukhari 1914 |  Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ramadan unless he has the habit of fasting (Nawafil) (and if his fasting coincides with that day) then he can fast that day." |
| 4 | 0.886 | nasai 2309 |  Abu Saeed said: "We were traveling in Ramadan and among us were some who were fasting and some who were not. Those who were fasting did not criticize those who were not, and those who were not fasting did not criticize those who were." |
| 5 | 0.886 | muslim 1082 a |  Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: Do not observe fast for a day, or two days ahead of Ramadan except a person who is in the habit of observing a particular fast; he may fast on that  |
| 6 | 0.886 | muslim 1159 o |  'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be upon him) said to me! 'Abdullah b. 'Amr, it has been conveyed to me that you observe fast during the day and stand in prayer during the whole night. Don |
| 7 | 0.885 | tirmidhi 759 |  Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with six from Shawwal, then that is (equal in reward) to fasting everyday." |
| 8 | 0.885 | abudawud 2335 |  Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing the particular fast, for he may fast on that day. |
| 9 | 0.885 | mishkat 2028 |  ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travelling is like one who breaks his fast when not travelling.” Ibn Majah transmitted it. |
| 10 | 0.885 | mishkat 2047 |  Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it with six days in Shawwal, it will be like a perpetual fast.” Muslim transmitted it. |

**Dedup ON only (chain-refs still included)**
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.889 | muslim 1162 a | `[dup-rep=226020]` Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How do you fast? The Messenger of Allah (may peace be upon him) felt annoyed. When 'Umar (Allah be pleased with him) noticed his annoyance, he said: We a |
| 2 | 0.889 | mishkat 1973 |  Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing a particular fast, for he may fast on that day.”* *If a man is in the h |
| 3 | 0.887 | bukhari 1914 |  Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ramadan unless he has the habit of fasting (Nawafil) (and if his fasting coincides with that day) then he can fast that day." |
| 4 | 0.886 | nasai 2309 |  Abu Saeed said: "We were traveling in Ramadan and among us were some who were fasting and some who were not. Those who were fasting did not criticize those who were not, and those who were not fasting did not criticize those who were." |
| 5 | 0.886 | muslim 1082 a |  Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: Do not observe fast for a day, or two days ahead of Ramadan except a person who is in the habit of observing a particular fast; he may fast on that  |
| 6 | 0.886 | muslim 1159 o |  'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be upon him) said to me! 'Abdullah b. 'Amr, it has been conveyed to me that you observe fast during the day and stand in prayer during the whole night. Don |
| 7 | 0.885 | tirmidhi 759 |  Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with six from Shawwal, then that is (equal in reward) to fasting everyday." |
| 8 | 0.885 | abudawud 2335 |  Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing the particular fast, for he may fast on that day. |
| 9 | 0.885 | mishkat 2028 |  ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travelling is like one who breaks his fast when not travelling.” Ibn Majah transmitted it. |
| 10 | 0.885 | mishkat 2047 |  Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it with six days in Shawwal, it will be like a perpetual fast.” Muslim transmitted it. |

****PRODUCTION: chain-ref + dedup both ON****
| # | Score | Ref | Tags | Text (250 chars) |
|---|---|---|---|---|
| 1 | 0.889 | muslim 1162 a | `[dup-rep=226020]` Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How do you fast? The Messenger of Allah (may peace be upon him) felt annoyed. When 'Umar (Allah be pleased with him) noticed his annoyance, he said: We a |
| 2 | 0.889 | mishkat 1973 |  Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing a particular fast, for he may fast on that day.”* *If a man is in the h |
| 3 | 0.887 | bukhari 1914 |  Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ramadan unless he has the habit of fasting (Nawafil) (and if his fasting coincides with that day) then he can fast that day." |
| 4 | 0.886 | nasai 2309 |  Abu Saeed said: "We were traveling in Ramadan and among us were some who were fasting and some who were not. Those who were fasting did not criticize those who were not, and those who were not fasting did not criticize those who were." |
| 5 | 0.886 | muslim 1082 a |  Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: Do not observe fast for a day, or two days ahead of Ramadan except a person who is in the habit of observing a particular fast; he may fast on that  |
| 6 | 0.886 | muslim 1159 o |  'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be upon him) said to me! 'Abdullah b. 'Amr, it has been conveyed to me that you observe fast during the day and stand in prayer during the whole night. Don |
| 7 | 0.885 | tirmidhi 759 |  Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with six from Shawwal, then that is (equal in reward) to fasting everyday." |
| 8 | 0.885 | abudawud 2335 |  Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing the particular fast, for he may fast on that day. |
| 9 | 0.885 | mishkat 2028 |  ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travelling is like one who breaks his fast when not travelling.” Ibn Majah transmitted it. |
| 10 | 0.885 | mishkat 2047 |  Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it with six days in Shawwal, it will be like a perpetual fast.” Muslim transmitted it. |

---

## 2. HNSW size sweep — production filters ON (chain-ref + dedup)

Fetch size = size × 3, then dedup to `size`. Shows which hadiths only surface at larger sizes.

### Query: *"aisha"*

| size | fetch_size | latency |
|---|---|---|
| 10 | 30 | 98ms |
| 20 | 60 | 77ms |
| 30 | 90 | 64ms |
| 50 | 150 | 98ms |
| 75 | 225 | 135ms |
| 100 | 300 | 129ms |

**Top-10 stability** — rank at each size (— = not in top-10 at that size)

| Ref | First seen | size=10 | size=20 | size=30 | size=50 | size=75 | size=100 | Text |
|---|---|---|---|---|---|---|---|---|
| bukhari 3894 | size=10 | 1 | 1 | 1 | 1 | 1 | 1 | Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then I got ill and my hair fell down. Later on my hair  |
| bukhari 277 | size=10 | 2 | 2 | 2 | 2 | 2 | 2 | Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head with one hand and rubbed the left side of the hea |
| abudawud 4164 | size=10 | 3 | 3 | 3 | 3 | 3 | 3 | Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing with henna. She replied: There is no harm, but I do  |
| bukhari 2661 | size=10 | 4 | 4 | 4 | 4 | 4 | 4 | Narrated Aisha: (the wife of the Prophet) "Whenever Allah's Apostle intended to go on a journey, he would draw lots amongst his wives and would take with him the one upon whom the lot fell. During a G |
| bukhari 1151 | size=10 | 5 | 5 | 5 | 5 | 5 | 5 | Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I said, "(She is) So and so. She does not sleep at nigh |
| bukhari 902 | size=10 | 6 | 6 | 6 | 6 | 6 | 6 | Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of four miles or more from Medina). They used to pass  |
| bukhari 4573 | size=10 | 7 | 7 | 7 | 7 | 7 | 7 | Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of that and not because he loved her. So the Divine V |
| bukhari 43 | size=10 | 8 | 8 | 8 | 8 | 8 | 8 | Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her (excessive) praying. He said disapprovingly, "Do  |
| abudawud 3708 | size=10 | 9 | 9 | 9 | 9 | 9 | 9 | Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays, and asked her about mixing dried dates and raisins (for drink). She replied: I u |
| abudawud 288 | size=10 | 10 | 10 | 10 | 10 | 10 | 10 | 'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, had a flow of blood for seven years. She asked the |

*Top-10 fully stable across all sizes.*

### Query: *"comparing yourself to others"*

| size | fetch_size | latency |
|---|---|---|
| 10 | 30 | 104ms |
| 20 | 60 | 71ms |
| 30 | 90 | 70ms |
| 50 | 150 | 101ms |
| 75 | 225 | 138ms |
| 100 | 300 | 138ms |

**Top-10 stability** — rank at each size (— = not in top-10 at that size)

| Ref | First seen | size=10 | size=20 | size=30 | size=50 | size=75 | size=100 | Text |
|---|---|---|---|---|---|---|---|---|
| forty 18 | size=10 | 1 | 1 | 1 | 1 | 1 | 1 | The felicitous person takes lessons from (the actions of) others. |
| bukhari 6490 | size=10 | 2 | 2 | 2 | 2 | 2 | 2 | Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior  |
| muslim 2963 a | size=10 | 3 | 3 | 3 | 3 | 3 | 4 | Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also s |
| riyadussalihin 466 | size=10 | 4 | 5 | 5 | 5 | 5 | 6 | Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you f |
| muslim 2536 | size=10 | 5 | 6 | 6 | 6 | 6 | 7 | 'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to which I belong, then of the second generation (ge |
| abudawud 4092 | size=10 | 6 | 7 | 7 | 7 | 7 | 8 | Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been given some of it, as you see. And I do not like that |
| tirmidhi 2513 | size=10 | 7 | 8 | 8 | 8 | 8 | 9 | Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indeed that is more worthy(so that you will) not belitt |
| adab 898 | size=10 | 8 | 9 | 9 | 9 | 9 | 10 | Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes so that you might come to know each other. The nob |
| riyadussalihin 7 | size=10 | 9 | 10 | 10 | 10 | 10 | — | Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does not look at your figures, nor at your attire but He looks at your hearts and accomplishments". [Musli |
| forty 19 | size=10 | 10 | — | — | — | — | — | On the authority of Abu Abbas Abdullah bin Abbas (may Allah be pleased with him) who said: One day I was behind the Prophet (peace and blessings of Allah be upon him) [riding on the same mount] and he |
| adab 159 | 🆕@20 | — | 4 | 4 | 4 | 4 | 5 | Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. The best of you is the one whose good is hoped for  |
| forty 3 | 🆕@100 | — | — | — | — | — | 3 | A Muslim is a mirror of the Muslim. |

**New results that only appear at larger sizes:**
- First at size=20: **adab 159** (score 0.791) — Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. The best of you is the one whose good is hoped for 
- First at size=100: **forty 3** (score 0.797) — A Muslim is a mirror of the Muslim.

### Query: *"forgiveness of sins"*

| size | fetch_size | latency |
|---|---|---|
| 10 | 30 | 97ms |
| 20 | 60 | 84ms |
| 30 | 90 | 74ms |
| 50 | 150 | 78ms |
| 75 | 225 | 110ms |
| 100 | 300 | 145ms |

**Top-10 stability** — rank at each size (— = not in top-10 at that size)

| Ref | First seen | size=10 | size=20 | size=30 | size=50 | size=75 | size=100 | Text |
|---|---|---|---|---|---|---|---|---|
| forty 28 | size=10 | 1 | 1 | 1 | 1 | 1 | 1 | One who repents from sin is like someone without sin. |
| riyadussalihin 423 | size=10 | 2 | 2 | 2 | 2 | 2 | 2 | Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Were you not to commit sins, Allah would create people who would commit sins and ask for forgivenes |
| bukhari 7507 | size=10 | 3 | 3 | 3 | 3 | 3 | 3 | Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says, 'O my Lord! I have sinned, please forgive me!' and his Lord says, 'My slave has known that he has a Lord who |
| bukhari 41 | size=10 | 4 | 4 | 4 | 4 | 4 | 4 | Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embraces Islam sincerely, then Allah shall forgive all his past sins, and after that starts the settlement of accounts, the re |
| riyadussalihin 442 | size=10 | 5 | 5 | 5 | 5 | 5 | 5 | Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the Exalted, has said: 'O son of adam, I forgive you as long as you pray to Me and hope for My forgiveness, whate |
| bulugh 319 | size=10 | 6 | 6 | 6 | 6 | 6 | 6 | Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I have greatly wronged myself, and no one forgives si |
| ibnmajah 3821 | size=10 | 7 | 7 | 7 | 7 | 7 | 7 | It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Blessed and Exalted, said: 'Whoever does one good deed will have (the reward of) ten like it and more, and whoever |
| riyadussalihin 421 | size=10 | 8 | 8 | 8 | 8 | 8 | 8 | Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, the Exalted, and Glorious said: 'A slave committed a sin and he said: O Allah, forgive my sin,' and Allah said:  |
| mishkat 2482 | size=10 | 9 | 9 | 9 | 9 | 9 | 9 | Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: “O God, forgive me my sin, my ignorance, my extravagance in my affairs, and what Thou knowest better than I d |
| bukhari 2449 | size=10 | 10 | 10 | 10 | 10 | 10 | 10 | Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his reputation or anything else, he should beg him to forgive him before the Day of Resurrection when there |

*Top-10 fully stable across all sizes.*

### Query: *"prayer before sleeping"*

| size | fetch_size | latency |
|---|---|---|
| 10 | 30 | 95ms |
| 20 | 60 | 89ms |
| 30 | 90 | 81ms |
| 50 | 150 | 72ms |
| 75 | 225 | 89ms |
| 100 | 300 | 94ms |

**Top-10 stability** — rank at each size (— = not in top-10 at that size)

| Ref | First seen | size=10 | size=20 | size=30 | size=50 | size=75 | size=100 | Text |
|---|---|---|---|---|---|---|---|---|
| bukhari 212 | size=10 | 1 | 1 | 1 | 1 | 1 | 1 | Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep) till his slumber is over because in praying while drowsy one does not know whether one i |
| muslim 786 | size=10 | 2 | 2 | 2 | 2 | 2 | 2 | 'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst you dozes in prayer, he should sleep, till sleep is gone, for when one of you prays while dozing he does not kno |
| bukhari 997 | size=10 | 3 | 3 | 3 | 3 | 3 | 3 | Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he used to wake me up and I would offer the witr pra |
| mishkat 604 | size=10 | 4 | 4 | 4 | 4 | 4 | 4 | Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is only when one is awake that there is remissness; so when any of you forgets a stated prayer or oversleeps, he sho |
| bukhari 512 | size=10 | 5 | 5 | 5 | 5 | 5 | 5 | Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front of him. Whenever he wanted to pray witr, he would wake me up and I would pray witr. |
| bukhari 213 | size=10 | 6 | 6 | 6 | 6 | 6 | 6 | Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should sleep till he understands what he is saying (reciting). |
| muslim 787 | size=10 | 7 | 7 | 7 | 7 | 7 | 7 | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of you gets up at night (for prayer) and his tongue falters in (the recitation) of the Qar'an, and he does not kn |
| abudawud 856 | size=10 | 8 | 8 | 8 | 8 | 8 | 8 | Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque, a man also entered it and prayed. He then came and saluted the Messenger of Allah(may peace be upon him). The  |
| muslim 755 a | size=10 | 9 | 9 | 9 | 9 | 9 | 9 | Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he should observe Witr in the first part of it; and if a |
| ibnmajah 1187 | size=10 | 10 | 10 | 10 | 10 | 10 | 10 | It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fears that he will not wake up at the end of the night, let him pray Witr at the beginning of the night, then go t |

*Top-10 fully stable across all sizes.*

### Query: *"fasting in Ramadan"*

| size | fetch_size | latency |
|---|---|---|
| 10 | 30 | 102ms |
| 20 | 60 | 93ms |
| 30 | 90 | 87ms |
| 50 | 150 | 83ms |
| 75 | 225 | 131ms |
| 100 | 300 | 88ms |

**Top-10 stability** — rank at each size (— = not in top-10 at that size)

| Ref | First seen | size=10 | size=20 | size=30 | size=50 | size=75 | size=100 | Text |
|---|---|---|---|---|---|---|---|---|
| muslim 1162 a | size=10 | 1 | 1 | 1 | 1 | 1 | 1 | Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and said: How do you fast? The Messenger of Allah (may peace be upon him) felt annoyed. When 'Umar (Allah be plea |
| mishkat 1973 | size=10 | 2 | 2 | 2 | 2 | 2 | 2 | Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing a particular fast, fo |
| bukhari 1914 | size=10 | 3 | 3 | 3 | 3 | 3 | 3 | Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the month of Ramadan unless he has the habit of fasting (Nawafil) (and if his fasting coincides with that day) then |
| nasai 2309 | size=10 | 4 | — | 4 | 4 | 4 | 4 | Abu Saeed said: "We were traveling in Ramadan and among us were some who were fasting and some who were not. Those who were fasting did not criticize those who were not, and those who were not fasting |
| muslim 1082 a | size=10 | 5 | 4 | 5 | 5 | 5 | 5 | Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: Do not observe fast for a day, or two days ahead of Ramadan except a person who is in the habit of |
| muslim 1159 o | size=10 | 6 | 5 | 6 | 6 | 6 | 6 | 'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may peace be upon him) said to me! 'Abdullah b. 'Amr, it has been conveyed to me that you observe fast during the d |
| tirmidhi 759 | size=10 | 7 | 6 | 7 | 7 | 7 | 7 | Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows it with six from Shawwal, then that is (equal in reward) to fasting everyday." |
| abudawud 2335 | size=10 | 8 | 7 | 8 | 8 | 8 | 8 | Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two days just before Ramadan, except in the case of a man who has been in the habit of observing the particular f |
| mishkat 2028 | size=10 | 9 | 8 | 9 | 9 | 9 | 9 | ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while travelling is like one who breaks his fast when not travelling.” Ibn Majah transmitted it. |
| mishkat 2047 | size=10 | 10 | 9 | 10 | 10 | 10 | 10 | Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then follows it with six days in Shawwal, it will be like a perpetual fast.” Muslim transmitted it. |
| bukhari 1900 | 🆕@20 | — | 10 | — | — | — | — | Narrated Ibn `Umar: I heard Allah's Apostle saying, "When you see the crescent (of the month of Ramadan), start fasting, and when you see the crescent (of the month of Shawwal), stop fasting; and if t |

**New results that only appear at larger sizes:**
- First at size=20: **bukhari 1900** (score 0.885) — Narrated Ibn `Umar: I heard Allah's Apostle saying, "When you see the crescent (of the month of Ramadan), start fasting, and when you see the crescent (of the month of Shawwal), stop fasting; and if t

---

*Generated by `tests/mxbai_size_filter_report.py`*
