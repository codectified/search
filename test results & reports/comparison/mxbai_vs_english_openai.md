# mxbai vs english-openai: Side-by-Side Comparison

Queries: 10 | size=10 | chain-ref filter=ON | dedup=ON

| Model | Corpus | Dim | Pre-filter |
|---|---|---|---|
| mxbai | English text (Ollama mxbai-embed-large) | 1024 | HNSW only |
| english-openai | English text (OpenAI text-embedding-3-small) | 1536 | Centroid k=75 → kNN |

---

## Query: *"comparing yourself to others"*

**Overlap:** 2/10 results in common | mxbai: 1040ms | english-openai: 1039ms (embed 990.4ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 | 0.815 | `forty 18` The felicitous person takes lessons from (the actions of) others. | 0.688 | `adab 328` Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faul |
| 2 | 0.802 | `bukhari 6490` Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was m | 0.687 | `riyadussalihin 466` Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Lo |
| 3 | 0.793 | `muslim 2963 a` Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you  | 0.678 | `bukhari 497` Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was m |
| 4 ✓ | 0.787 | `riyadussalihin 466` Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Lo | 0.666 | `muslim 7068` Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you  |
| 5 | 0.785 | `muslim 2536` 'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amo | 0.664 | `adab 592` Abu Hurayra said, "One of you looks at the mote in his brother's eye while forgetting the  |
| 6 | 0.782 | `abudawud 4092` Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messeng | 0.663 | `muslim 7070` Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those wh |
| 7 ✓ | 0.782 | `tirmidhi 2513` Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower  | 0.663 | `bulugh 1514` Ibn ’Umar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “He who imitates any |
| 8 | 0.781 | `adab 898` Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you fro | 0.662 | `hisn 231` If any of you praises his companion then let him say: Aḥsibu fulānan wallāhu ḥasībuh wa lā |
| 9 | 0.779 | `riyadussalihin 7` Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Al | 0.658 | `tirmidhi 2513` Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower  |
| 10 | 0.775 | `forty 19` On the authority of Abu Abbas Abdullah bin Abbas (may Allah be pleased with him) who said: | 0.656 | `bukhari 619` Narrated Abu Huraira: Allah's Apostle said, "Not to wish to be the like of except the like |

## Query: *"forgiveness of sins"*

**Overlap:** 2/10 results in common | mxbai: 1073ms | english-openai: 444ms (embed 410.4ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 | 0.876 | `forty 28` One who repents from sin is like someone without sin. | 0.752 | `hisn 57` Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfi |
| 2 | 0.852 | `riyadussalihin 423` Abu Ayyub Khalid bin Zaid (May Allah be pleased with him) reported: Messenger of Allah (PB | 0.749 | `bukhari 657` Narrated Abu Huraira: The Prophet said, "Allah forgives my followers those (evil deeds) th |
| 3 | 0.851 | `bukhari 7507` Narrated Abu Huraira: I heard the Prophet saying, "If somebody commits a sin and then says | 0.749 | `forty 33` On the authority of Abu Hurayrah (may Allah be pleased with him) that the Prophet (PBUH),  |
| 4 | 0.850 | `bukhari 41` Narrated Abu Sa'id Al Khudri: Allah's Messenger (saws) said, "If a person embraces Islam s | 0.746 | `mishkat 2331` Abu Huraira said that God’s messenger told of a man who committed a sin and said, "My Lord |
| 5 ✓ | 0.850 | `riyadussalihin 442` Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the | 0.745 | `riyadussalihin 442` Anas (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Allah, the |
| 6 | 0.850 | `bulugh 319` Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplica | 0.745 | `mishkat 2475` Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: |
| 7 | 0.848 | `ibnmajah 3821` It was narrated from Abu Dharr that : the Messenger of Allah (saas) said: "Allah, the Bles | 0.743 | `mishkat 2328` 'A’isha reported God’s messenger as saying, "When a servant acknowledges his sin and repen |
| 8 ✓ | 0.848 | `riyadussalihin 421` Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, th | 0.743 | `riyadussalihin 421` Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Allah, th |
| 9 | 0.848 | `mishkat 2482` Abu Musa al-Ash‘ari told on the Prophet’s authority that he used to use this supplication: | 0.742 | `tirmidhi 3397` Abu Sa`eed (ra) narrated that : the Prophet (saws) said: “Whoever says, when he goes to hi |
| 10 | 0.846 | `bukhari 2449` Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerni | 0.741 | `muslim 6642` Abu Huraira reported from Allah's Messenger (may peace be upon him) that his Lord, the Exa |

## Query: *"visiting the sick"*

**Overlap:** 3/10 results in common | mxbai: 1173ms | english-openai: 788ms (embed 761.8ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 | 0.825 | `muslim 2568 a` Abu Rabi' reported directly from Allah's Apostle (may peace upon him) as saying: The one w | 0.756 | `ahmad 975` It was narrated that ‘Abdullah bin Nafi’ said: Abu Moosa al-Ash’ari visited al-Hasan bin ‘ |
| 2 ✓ | 0.820 | `ahmad 975` It was narrated that ‘Abdullah bin Nafi’ said: Abu Moosa al-Ash’ari visited al-Hasan bin ‘ | 0.755 | `abudawud 3101` Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: When a man comes to visit a |
| 3 | 0.819 | `riyadussalihin 902` 'Aishah (May Allah be pleased with her) reported: When the Prophet (PBUH) visited any aili | 0.752 | `tirmidhi 2008` Abu Hurairah narrated that the Messenger of Allah said: "Whoever visits the sick, or visit |
| 4 ✓ | 0.818 | `ahmad 612` It was narrated that ‘AbdurRahman bin Abi Laila said: Abu Moosa came to al-Hasan bin `Ali  | 0.751 | `riyadussalihin 894` Al-Bara' bin `Azib (May Allah be pleased with them) reported: Messenger of Allah (PBUH) ha |
| 5 | 0.817 | `bukhari 5689` Narrated 'Urwa: Aisha used to recommend at-Talbina for the sick and for such a person as g | 0.750 | `muslim 6227` Abu Rabi' reported directly from Allah's Apostle (may peace upon him) as saying: The one w |
| 6 | 0.817 | `ibnmajah 1777` It was narrated that Anas bin Malik said: “The Messenger of Allah (saw) said: ‘The person  | 0.745 | `riyadussalihin 907` Ibn 'Abbas (May Allah be pleased with them) reported: The Prophet (PBUH) visited a bedouin |
| 7 | 0.817 | `tirmidhi 2087` Abu Sa'eed Al-Khudri narrated that the Messenger of Allah (S.A.W) said: "When one of you v | 0.744 | `ahmad 612` It was narrated that ‘AbdurRahman bin Abi Laila said: Abu Moosa came to al-Hasan bin `Ali  |
| 8 | 0.815 | `bukhari 3046` Narrated Abu Musa: The Prophet said, "Free the captives, feed the hungry and pay a visit t | 0.743 | `ahmad 1166` It was narrated from a man among the Ansar, from `Ali (رضي الله عنه), that the Prophet (ﷺ) |
| 9 | 0.813 | `ahmad 955` It was narrated from ‘Amr bin Huraith that he visited Hasan [when he was sick and ‘Ali was | 0.740 | `adab 518` Abu Sa'id reported that the Prophet, may Allah bless him and grant him peace, said, "Visit |
| 10 ✓ | 0.812 | `riyadussalihin 894` Al-Bara' bin `Azib (May Allah be pleased with them) reported: Messenger of Allah (PBUH) ha | 0.739 | `mishkat 2100` She said that the Prophet used to visit the sick while engaged in a period of private devo |

## Query: *"honoring one's parents"*

**Overlap:** 3/10 results in common | mxbai: 878ms | english-openai: 240ms (embed 206.0ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 ✓ | 0.843 | `adab 35` Abu Usayd said, "We were with the Messenger of Allah, may Allah bless him and grant him pe | 0.760 | `ibnmajah 3657` Ibn Salamah As-Sulami narrated that the Prophet (saws) said: "I enjoin each one to honor h |
| 2 ✓ | 0.826 | `adab 94` Ibn 'Umar said, "Allah has called them the 'dutiful' (al-Abrar) because they are dutiful ( | 0.743 | `adab 35` Abu Usayd said, "We were with the Messenger of Allah, may Allah bless him and grant him pe |
| 3 | 0.824 | `abudawud 4435` Narrated Al-Lajlaj al-Amiri: I was working in the market. A woman passed carrying a child. | 0.741 | `ibnmajah 2089` It was narrated from 'Abdur-Rahman that: a man's father or mother - Shu'bah (one of the na |
| 4 | 0.823 | `adab 22` Mu'adh said, "Bliss belongs to someone who is dutiful towards his parents. Allah Almighty  | 0.730 | `ibnmajah 3664` It was narrated that Abu Usaid, Malik bin Rabi'ah, said: "While we were with the Prophet(S |
| 5 | 0.821 | `mishkat 1768` Muhammad b. an-Nu‘man who traced the tradition back to the Prophet reported him as saying, | 0.729 | `riyadussalihin 343` Abu Usaid Malik bin Rabi'ah As-Sa'idi (May Allah be pleased with him) reported: We were si |
| 6 | 0.816 | `ahmad 1408` It was narrated that az-Zubair said: The Messenger of Allah (ﷺ) mentioned both of his pare | 0.724 | `adab 94` Ibn 'Umar said, "Allah has called them the 'dutiful' (al-Abrar) because they are dutiful ( |
| 7 | 0.815 | `nasai 2559` It was narrated from 'Amr bin Shu'aib, from his father, that his grandfather said: "Eat, g | 0.721 | `tirmidhi 3189` Narrated Mus'ab bin Sa'd: that his father, Sa'd, said: "Four Ayat were revealed about me"  |
| 8 | 0.812 | `adab 1037` Mu'awiya ibn Qurra said that his father said to him, "My son, when a man passes by you and | 0.713 | `ibnmajah 3661` Miqdam bin Ma'dikarib, may Allah be pleased with them, narrated that: Allah's Messenger sa |
| 9 | 0.812 | `abudawud 5142` Narrated AbuUsayd Malik ibn Rabi'ah as-Sa'idi: While we were with the Messenger of Allah!  | 0.710 | `bulugh 1503` 'Abdullah bin 'Amro bin al-As (RAA) narrated that the Messenger of Allah (P.B.U.H.) said,  |
| 10 ✓ | 0.811 | `ibnmajah 3664` It was narrated that Abu Usaid, Malik bin Rabi'ah, said: "While we were with the Prophet(S | 0.709 | `riyadussalihin 341` 'Abdullah bin 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said, "T |

## Query: *"fasting in Ramadan"*

**Overlap:** 0/10 results in common | mxbai: 440ms | english-openai: 401ms (embed 378.8ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 | 0.889 | `muslim 1162 a` Abu Qatada reported that a person came to the Apostle of Allah (may peace be upon him) and | 0.820 | `tirmidhi 723` Abu Hurairah narrated that : the Messenger of Allah said: "Whoever breaks the fast during  |
| 2 | 0.889 | `mishkat 1973` Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days | 0.813 | `mishkat 1972` Abu Huraira reported God’s messenger as saying, “None of you must fast one day or two days |
| 3 | 0.887 | `bukhari 1914` Narrated Abu Huraira: The Prophet said, "None of you should fast a day or two before the m | 0.810 | `abudawud 2320` Narrated Abdullah ibn Abbas: The Prophet (saws) said: Do not fast one day or two days just |
| 4 | 0.886 | `muslim 1082 a` Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) | 0.809 | `abudawud 2426` Narrated Muslim al-Qurashi: I asked or someone asked the Prophet (saws) about perpetual fa |
| 5 | 0.886 | `muslim 1159 o` 'Abdullah b. 'Amr (Allah be pleased with them) reported that the Messenger of Allah (may p | 0.809 | `muslim 2378` Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Whenever you sig |
| 6 | 0.885 | `tirmidhi 759` Abu Ayub narrated that : the Messenger of Allah said: "Whoever fasts Ramadan, then follows | 0.809 | `riyadussalihin 1224` Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Do not ob |
| 7 | 0.885 | `abudawud 2335` Narrated Abu Hurairah: The Messenger of Allah (saws) as saying: Do not fast one day or two | 0.807 | `muslim 2382` Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) |
| 8 | 0.885 | `mishkat 2028` ‘Abd ar-Rahman b. ‘Auf reported God’s messenger as saying, “One who fasts in Ramadan while | 0.805 | `abudawud 1370` Narrated AbuDharr: We fasted with the Messenger of Allah (saws) during Ramadan, but he did |
| 9 | 0.885 | `mishkat 2047` Abu Ayyub al-Ansari told that God’s messenger said, “If anyone fasts during Ramadan, then  | 0.804 | `mishkat 2059` Muslim al-Qurashi said that he or someone else asked God's messenger about perpetual fasti |
| 10 | 0.885 | `bukhari 1900` Narrated Ibn `Umar: I heard Allah's Apostle saying, "When you see the crescent (of the mon | 0.803 | `abudawud 2427` Narrated Abu Ayyub: The Prophet (saws) as saying: If anyone fasts during Ramadan, then fol |

## Query: *"prayer before sleeping"*

**Overlap:** 1/10 results in common | mxbai: 774ms | english-openai: 219ms (embed 198.1ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 | 0.875 | `bukhari 212` Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he sho | 0.780 | `riyadussalihin 814` Al-Bara' bin 'Azib (May Allah be pleased with them) reported: Messenger of Allah (PBUH) di |
| 2 | 0.870 | `muslim 786` 'A'isha reported Allah's Apostle (may peace be upon him) as saying: When anyone amongst yo | 0.779 | `bukhari 211` Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he sho |
| 3 | 0.864 | `bukhari 997` Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across i | 0.777 | `riyadussalihin 1462` Al-Bara' bin 'Azib (May Allah be pleased with them) reported: The Messenger of Allah (PBUH |
| 4 | 0.858 | `mishkat 604` Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is onl | 0.775 | `abudawud 1305` Narrated 'Aishah, wife of Prophet (saws): When one of you dozes in prayer he should sleep  |
| 5 | 0.857 | `bukhari 512` Narrated `Aisha: The Prophet used to pray while I was sleeping across in his bed in front  | 0.775 | `ibnmajah 1187` It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fear |
| 6 | 0.856 | `bukhari 213` Narrated Anas: The Prophet said, "If anyone of you feels drowsy while praying, he should s | 0.772 | `riyadussalihin 1464` Hudhaifah (May Allah be pleased with him) reported: Whenever the Messenger of Allah (PBUH) |
| 7 | 0.853 | `muslim 787` Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When any one of  | 0.772 | `muslim 6544` Al-Bara' b. 'Azib reported that Allah's, Messenger (may peace be upon said: When you go to |
| 8 | 0.852 | `abudawud 856` Abu Hurairah said: When the Messenger of Allah(may peace be upon him) entered the mosque,  | 0.767 | `ibnmajah 1344` It was narrated that Abu Darda’ conveyed that the Prophet (saw) said: “Whoever goes to bed |
| 9 | 0.852 | `muslim 755 a` Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid th | 0.764 | `riyadussalihin 80` Al-Bara' bin 'Azib (May Allah be pleased with them) said: Messenger of Allah (PBUH) asked  |
| 10 ✓ | 0.852 | `ibnmajah 1187` It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fear | 0.764 | `mishkat 0` Abu Qatada reported God’s Messenger as saying, “There is no remissness in sleep, it is onl |

## Query: *"giving charity"*

**Overlap:** 0/10 results in common | mxbai: 921ms | english-openai: 213ms (embed 185.2ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 | 0.861 | `bukhari 2748` Narrated Abu Huraira: A man asked the Prophet, "O Allah's Apostle! What kind of charity is | 0.771 | `tirmidhi 1956` Abu Dharr narrated that the Messenger of Allah said : "Your smiling in the face of your br |
| 2 | 0.849 | `bukhari 7120` Narrated Haritha bin Wahb: I heard Allah's Apostle saying, "Give in charity because there  | 0.770 | `bukhari 507` Narrated Abu Huraira: The Prophet (p.b.u.h) said, "The best charity is that which is pract |
| 3 | 0.845 | `muslim 1032 b` Abu Huraira reported that a person came to the Apostle of Allah (may peace be upon him) an | 0.765 | `riyadussalihin 90` Abu Hurairah (May Allah be pleased with him) said: There came a man to the Prophet (PBUH)  |
| 4 | 0.845 | `nasai 3611` It was narrated that Abu Hurairah said: "A man came to the Prophet and said: 'O Messenger  | 0.765 | `riyadussalihin 248` Abu Hurairah (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "On |
| 5 | 0.844 | `bukhari 1424` Narrated Haritha bin Wahab Al-Khuza`i: I heard the Prophet (p.b.u.h) saying, "(O people!)  | 0.764 | `bukhari 141` Narrated Abu Huraira: The Prophet said, "Charity is obligatory everyday on every joint of  |
| 6 | 0.844 | `forty 5` The person guiding (someone) to do a good deed, is like the one performing the good deed. | 0.759 | `forty 26` On the authority of Abu Hurayrah (may Allah be pleased with him) who said: The Messenger o |
| 7 | 0.844 | `bukhari 1427, 1428` Narrated Hakim bin Hizam: The Prophet said, "The upper hand is better than the lower hand  | 0.756 | `bukhari 11` Narrated Abu Huraira: A man asked the Prophet, "O Allah's Apostle! What kind of charity is |
| 8 | 0.843 | `nasai 2538` It was narrated from Abu Musa that the Prophet said: "Every Muslim must give charity." It  | 0.753 | `muslim 1557` Abu Dharr reported Allah's Apostle (may peace be upon him) as saying: In the morning chari |
| 9 | 0.843 | `bulugh 634` Hakim bin Hizam (RAA) narrated that The Messenger of Allah (P.B.U.H.) said, ”The upper han | 0.753 | `nasai 3641` It was narrated that Abu Hurairah said: "A man came to the Prophet and said: 'O Messenger  |
| 10 | 0.842 | `bukhari 2773` Narrated Ibn `Umar: `Umar got some property in Khaibar and he came to the Prophet and info | 0.753 | `muslim 2250` Abu Huraira reported that there came a person to the Messenger of Allah (may peace be upon |

## Query: *"patience during hardship"*

**Overlap:** 2/10 results in common | mxbai: 1098ms | english-openai: 191ms (embed 144.2ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 | 0.854 | `bukhari 1302` Narrated Anas: The Prophet said, "The real patience is at the first stroke of a calamity." | 0.757 | `bukhari 389` Narrated Anas: The Prophet said, "The real patience is at the first stroke of a calamity." |
| 2 | 0.840 | `tirmidhi 987` Anas narrated that: The Messenger of Allah said: "(Real) Patience is at the first stroke o | 0.753 | `tirmidhi 988` Anas bin Malik narrated that: The Messenger of Alllah said: "(Real) Patience is at the fir |
| 3 | 0.826 | `bukhari 6470` Narrated Abu Sa`id: Some people from the Ansar asked Allah's Apostle (to give them somethi | 0.741 | `tirmidhi 2464` 'Abdur-Rahman bin 'Awf said: "We were tested along with the Messenger of Allah(s.a.w) by a |
| 4 | 0.825 | `bukhari 3401` Narrated Sa`id bin Jubair: I said to Ibn `Abbas, "Nauf Al-Bukah claims that Moses, the com | 0.731 | `ibnmajah 1596` It was narrated from Anas bin Malik that the Messenger of Allah (SAW) said: "Patience shou |
| 5 | 0.825 | `malik 1850` Malik related to me from Malik from Ibn Shihab from Ata ibn Yazid al-Laythi from Abu Said  | 0.720 | `tirmidhi 2024` Abu Sa'eed narrated: "Some persons from the Ansar asked for (something) from the Messenger |
| 6 | 0.824 | `nasai 2588` It was narrated from Abu Sa'eed Al-Khudri that: some of the Ansar asked the Messenger of A | 0.719 | `riyadussalihin 37` Abu Sa'id and Abu Hurairah (May Allah be pleased with him) reported that the Prophet (PBUH |
| 7 | 0.821 | `bukhari 1469` Narrated Abu Sa`id Al-Khudri: Some Ansari persons asked for (something) from Allah's Apost | 0.718 | `nasai 2589` It was narrated from Abu Sa'eed Al-Khudri that: some of the Ansar asked the Messenger of A |
| 8 | 0.820 | `bukhari 3026` Narrated Abu Huraira: The Prophet said: "Do not wish to meet the enemy, but when you meet  | 0.716 | `bukhari 548` Narrated Abu Sa`id Al-Khudri: Some Ansari persons asked for (something) from Allah's Apost |
| 9 ✓ | 0.820 | `tirmidhi 2024` Abu Sa'eed narrated: "Some persons from the Ansar asked for (something) from the Messenger | 0.712 | `riyadussalihin 31` Anas (May Allah be pleased with him) reported: The Prophet (PBUH) passed by a woman who wa |
| 10 ✓ | 0.819 | `riyadussalihin 31` Anas (May Allah be pleased with him) reported: The Prophet (PBUH) passed by a woman who wa | 0.711 | `malik 7` Malik related to me from Malik from Ibn Shihab from Ata ibn Yazid al-Laythi from Abu Said  |

## Query: *"rights of a neighbour"*

**Overlap:** 1/10 results in common | mxbai: 949ms | english-openai: 231ms (embed 188.4ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 | 0.850 | `bulugh 901` Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be | 0.762 | `abudawud 3511` Narrated Jabir ibn Abdullah: The Prophet (saws) said: The neighbour is most entitled to th |
| 2 | 0.849 | `abudawud 3517` Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or  | 0.754 | `abudawud 3510` Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or  |
| 3 | 0.849 | `abudawud 3513` Narrated Jabir: The Messenger of Allah (saws) as saying: There is the right of option rega | 0.748 | `bulugh 905` Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be |
| 4 ✓ | 0.848 | `tirmidhi 1368` Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has mor | 0.748 | `bulugh 907` Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the r |
| 5 | 0.845 | `nasai 4703` It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger o | 0.737 | `tirmidhi 1368` Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has mor |
| 6 | 0.844 | `nasai 4702` It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more r | 0.734 | `nasai 4707` It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger o |
| 7 | 0.842 | `mishkat 2967` Jabir reported God’s Messenger as saying, “The neighbour is most entitled to the right of  | 0.733 | `adab 109` Al-Hasan was asked about the neighbour and said, "The term 'neighbour' includes the forty  |
| 8 | 0.841 | `abudawud 3518` Narrated Jabir ibn Abdullah: The Prophet (saws) said: The neighbour is most entitled to th | 0.730 | `mishkat 2966` Jabir reported God’s Messenger as saying, “The neighbour is most entitled to the right of  |
| 9 | 0.840 | `malik 1400` Malik related to me that he heard the like of that from Sulayman ibn Yasar. Malik spoke ab | 0.730 | `nasai 4706` It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more r |
| 10 | 0.837 | `bulugh 903` Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the r | 0.723 | `abudawud 3509` Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim |

## Query: *"seeking knowledge"*

**Overlap:** 2/10 results in common | mxbai: 1083ms | english-openai: 239ms (embed 206.9ms, clusters=?)

| # | mxbai score | mxbai result | openai score | openai result |
|---|---|---|---|---|
| 1 ✓ | 0.810 | `ibnmajah 224` It was narrated from Anas bin Malik that the Messenger of Allah (saws) said: "Seeking know | 0.735 | `ibnmajah 224` It was narrated from Anas bin Malik that the Messenger of Allah (saws) said: "Seeking know |
| 2 | 0.804 | `ibnmajah 247` Abu Sa'eed Al-Khudri narrated that: The Messenger of Allah said: "People will come to you  | 0.729 | `ibnmajah 254` It was narrated from Jabir bin 'Abdullah that: The Prophet said: "Do not seek knowledge in |
| 3 | 0.797 | `bukhari 7307` Narrated `Abdullah bin `Amr: I heard the Prophet saying, "Allah will not deprive you of kn | 0.725 | `abudawud 3656` Narrated Abu Hurayrah: The Prophet (saws) said: If anyone acquires knowledge that should b |
| 4 ✓ | 0.795 | `tirmidhi 2648` Narrated 'Abdullah bin Sakhbarah: narrated that the Prophet (SAW) said: "Whoever seeks kno | 0.721 | `riyadussalihin 1391` Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah(PBUH) said,  |
| 5 | 0.793 | `bukhari 3524` Narrated Ibn `Abbas: If you wish to know about the ignorance of the Arabs, refer to Surat- | 0.721 | `tirmidhi 2648` Narrated 'Abdullah bin Sakhbarah: narrated that the Prophet (SAW) said: "Whoever seeks kno |
| 6 | 0.791 | `abudawud 2885` Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Knowledge has three categor | 0.720 | `mishkat 263` Al-Hasan said that knowledge is of two kinds: knowledge in the heart, which is the benefic |
| 7 | 0.788 | `adab 789` Ibn Mas'ud was heard to say, "You are living at a time when there are many men of understa | 0.715 | `ibnmajah 228` It was narrated that Abu Umamah said: "The Messenger of Allah said: 'You must acquire this |
| 8 | 0.788 | `bulugh 1565` Anas (RAA) narrated that the Messenger of Allah (P.B.U.H.) used to say, “O Allah! Grant me | 0.715 | `tirmidhi 2647` Narrated Anas bin Malik: that the Messenger of Allah (SAW) said: "Whoever goes out seeking |
| 9 | 0.788 | `bukhari 3607` Narrated Hudhaifa: My companions learned (something about) good (through asking the Prophe | 0.715 | `mishkat 259` Sufyan said that ‘Umar b. al-Khattab asked Ka‘b who were the lords of knowledge, and he re |
| 10 | 0.787 | `mishkat 3033` Zaid b. Khalid told that when a man came to God's Messenger and asked him about a find he  | 0.714 | `tirmidhi 2654` Narrated Ibn Ka'b bin Malik: from his father that he heard the Messenger of Allah (SAW) sa |

---

## Summary

| Query | mxbai top score | openai top score | Overlap |
|---|---|---|---|
| comparing yourself to others | 0.815 | 0.688 | 2/10 |
| forgiveness of sins | 0.876 | 0.752 | 2/10 |
| visiting the sick | 0.825 | 0.756 | 3/10 |
| honoring one's parents | 0.843 | 0.760 | 3/10 |
| fasting in Ramadan | 0.889 | 0.820 | 0/10 |
| prayer before sleeping | 0.875 | 0.780 | 1/10 |
| giving charity | 0.861 | 0.771 | 0/10 |
| patience during hardship | 0.854 | 0.757 | 2/10 |
| rights of a neighbour | 0.850 | 0.762 | 1/10 |
| seeking knowledge | 0.810 | 0.735 | 2/10 |
