# English Matn Extraction Report

Total hadiths: 48,703  

| Coverage tier | Count | % |
|---|---|---|
| Clean extraction | 37,873 | 77.8% |
| Weak heuristic (first colon) | 3,272 | 6.7% |
| No extraction (full text used) | 7,558 | 15.5% |

## Per-Collection Breakdown

| Collection | Total | Clean | Weak | No-extract | Top patterns |
|---|---|---|---|---|---|
| muslim | 7459 | 3387(45%) | 1929(25%) | 2143(28%) | reported_colon=2859, no_extract=2142, first_colon_weak=1929 |
| bukhari | 7277 | 7195(98%) | 28(0%) | 54(0%) | narrated_colon=7120, no_extract=54, said_comma_quote=38 |
| nasai | 5768 | 5436(94%) | 147(2%) | 185(3%) | itwas_colon=4458, reported_colon=810, no_extract=185 |
| mishkat | 5319 | 3373(63%) | 158(2%) | 1788(33%) | as_saying_quote=1911, no_extract=1788, reported_colon=609 |
| abudawud | 5276 | 4224(80%) | 459(8%) | 593(11%) | narrated_colon=2952, reported_colon=1061, no_extract=593 |
| ibnmajah | 4345 | 4067(93%) | 81(1%) | 197(4%) | itwas_colon=3557, reported_colon=442, no_extract=197 |
| tirmidhi | 4053 | 3909(96%) | 84(2%) | 60(1%) | reported_colon=2039, narrated_colon=1662, narrated_chain_colon=189 |
| malik | 1973 | 401(20%) | 6(0%) | 1566(79%) | no_extract=1566, said_comma_quote=401, first_colon_weak=6 |
| riyadussalihin | 1896 | 1854(97%) | 26(1%) | 16(0%) | reported_colon=1828, first_colon_weak=26, said_comma_quote=21 |
| bulugh | 1767 | 1106(62%) | 177(10%) | 484(27%) | narrated_colon=799, no_extract=484, said_comma_quote=268 |
| ahmad | 1359 | 1193(87%) | 62(4%) | 104(7%) | itwas_colon=997, reported_colon=181, no_extract=104 |
| adab | 1326 | 960(72%) | 26(1%) | 340(25%) | said_comma_quote=942, no_extract=340, first_colon_weak=26 |
| shamail | 402 | 315(78%) | 79(19%) | 8(1%) | reported_colon=313, first_colon_weak=79, no_extract=8 |
| hisn | 268 | 268(100%) | 0(0%) | 0(0%) | pure_matn=268 |
| forty | 122 | 122(100%) | 0(0%) | 0(0%) | pure_matn=122 |
| virtues | 93 | 63(67%) | 10(10%) | 20(21%) | reported_colon=42, no_extract=20, said_comma_quote=16 |

## Partial-Coverage Examples

These hadiths fell back to the weak heuristic or no-extract. Full text shown so the pattern gaps are visible.

### abudawud

**abudawud 1669** — pattern: `first_colon_weak`  
Full text: Buhaysah reported on the authority of his father: My father sought permission from the Prophet (saws). (When permission was granted and he came near him) he lifted his shirt, and began to kiss him and embrace him (out of love for him). He asked: Messenger of Allah, what is the thing which it is unla  
Extracted matn: My father sought permission from the Prophet (saws). (When permission was granted and he came near him) he lifted his shirt, and began to kiss him and embrace him (out of love for him). He asked: Mess

**abudawud 1772** — pattern: `first_colon_weak`  
Full text: Ubayd ibn Jurayj said to Abdullah ibn Umar: AbuAbdurRahman, I saw you doing things which I did not see being done by your companions. He asked: What are they, Ibn Jurayj? He replied: I saw you touching only the two Yamani corners; and I saw you wearing shoes having no hair; I saw you dyeing in yello  
Extracted matn: AbuAbdurRahman, I saw you doing things which I did not see being done by your companions. He asked: What are they, Ibn Jurayj? He replied: I saw you touching only the two Yamani corners; and I saw you

**abudawud 1803** — pattern: `first_colon_weak`  
Full text: Ibn Abbas said that Mu'awiyah told him: do you not know that I clipped the hair of the head of the Messenger of Allah (saws) with a broad iron arrowhead at al-Marwah? Al-Hasan added in his version: "during his hajj."  
Extracted matn: do you not know that I clipped the hair of the head of the Messenger of Allah (saws) with a broad iron arrowhead at al-Marwah? Al-Hasan added in his version: "during his hajj."

**abudawud 1849** — pattern: `first_colon_weak`  
Full text: Abdullah ibn al-Harith reported on the authority of his father al-Harith: (My father) al-Harith was the governor of at-Ta'if under the caliph Uthman. He prepared food for Uthman which contained birds and the flesh of wild ass. He sent it to Ali (may Allah be pleased with him). When the Messenger cam  
Extracted matn: (My father) al-Harith was the governor of at-Ta'if under the caliph Uthman. He prepared food for Uthman which contained birds and the flesh of wild ass. He sent it to Ali (may Allah be pleased with hi

**abudawud 1859** — pattern: `no_extract`  
Full text: A man from the Ansar said on the authority of Ka'b ibn Ujrah that he was feeling pain in his head (due to lice); so he shaved his head. The Prophet (saws) ordered him to sacrifice a cow as offering.  
Extracted matn: A man from the Ansar said on the authority of Ka'b ibn Ujrah that he was feeling pain in his head (due to lice); so he shaved his head. The Prophet (saws) ordered him to sacrifice a cow as offering.

### adab

**adab 9** — pattern: `no_extract`  
Full text: Hisham ibn 'Urwa related this ayat from his father, "Take them under your wing, out of mercy, with due humility." (17:24)  
Extracted matn: Hisham ibn 'Urwa related this ayat from his father, "Take them under your wing, out of mercy, with due humility." (17:24)

**adab 12** — pattern: `no_extract`  
Full text: Marwan used to make Abu Hurayra his agent and he used to be located in Dhu'l-Hulayfa. His mother was in one house and he was in another. When he wanted to go out, he would stop at her door and say, "Peace be upon you, mother, and the mercy of Allah and His blessing." She would reply, "And peace be u  
Extracted matn: Marwan used to make Abu Hurayra his agent and he used to be located in Dhu'l-Hulayfa. His mother was in one house and he was in another. When he wanted to go out, he would stop at her door and say, "P

**adab 14** — pattern: `no_extract`  
Full text: Abu Hazim reported that Abu Murra, the mawla of Umm Hani' bint Abi Talib had told him that he rode with Abu Hurayra to his land in al-'Aqiq. When he entered his land, he shouted out in his loudest voice, "Peace be upon you, mother, and the mercy of Allah and His blessing!" She replied, "And peace be  
Extracted matn: Abu Hazim reported that Abu Murra, the mawla of Umm Hani' bint Abi Talib had told him that he rode with Abu Hurayra to his land in al-'Aqiq. When he entered his land, he shouted out in his loudest voi

**adab 23** — pattern: `no_extract`  
Full text: Ibn 'Abbas mentioned the words of the Almighty, "When one or both of them reach old age with you, do not say 'Ugh!' to them out of irritation and do not be harsh with them but speak to them with gentleness and generosity. Take them under your wing, out of mercy, with due humility and say: 'Lord, sho  
Extracted matn: Ibn 'Abbas mentioned the words of the Almighty, "When one or both of them reach old age with you, do not say 'Ugh!' to them out of irritation and do not be harsh with them but speak to them with gentl

**adab 33** — pattern: `no_extract`  
Full text: Abu Hurayra reported that he heard the Messenger of Allah, may Allah bless him and grant him peace, say, "No human child has ever spoken in the cradle except for 'Isa ibn Maryam, may Allah bless him and grant him peace, and the companion of Jurayj." Abu Hurayra asked, "Prophet of Allah, who was the   
Extracted matn: Abu Hurayra reported that he heard the Messenger of Allah, may Allah bless him and grant him peace, say, "No human child has ever spoken in the cradle except for 'Isa ibn Maryam, may Allah bless him a

### ahmad

**ahmad 24** — pattern: `first_colon_weak`  
Full text: Uthman bin 'Affan narrated that when the Messenger of Allah (ﷺ) died, some of the Companions of the Prophet (ﷺ) grieved for him so much that they were almost unaware of what was going on around thern. 'Uthman said: I was one of them... and he narrated a hadeeth similar to that of Abul Yaman from Shu  
Extracted matn: I was one of them... and he narrated a hadeeth similar to that of Abul Yaman from Shu'aib.

**ahmad 25** — pattern: `no_extract`  
Full text: Urwah bin az-Zubair narrated that 'A'ishah, the wife of the Prophet (ﷺ) told him that Fatimah, the daughter of the Messenger of Allah (ﷺ), asked Abu Bakr, after the death of the Messenger of Allah (ﷺ), to give her her share of inheritance from that which the Messenger of Allah (ﷺ) had left behind, o  
Extracted matn: Urwah bin az-Zubair narrated that 'A'ishah, the wife of the Prophet (ﷺ) told him that Fatimah, the daughter of the Messenger of Allah (ﷺ), asked Abu Bakr, after the death of the Messenger of Allah (ﷺ)

**ahmad 76** — pattern: `first_colon_weak`  
Full text: Ibn as-Sabbaq said that Zaid bin Thabit told him that Abu Bakr sent for him to tell him that a large number of people at al-Yamamah had been killed. He found ʼUmar with him and Abu Bakr said: ‘Umar has come to me and told me that casualties were heavy at al-Yamamah among the Muslims who knew the Qur  
Extracted matn: ‘Umar has come to me and told me that casualties were heavy at al-Yamamah among the Muslims who knew the Qur'an by heart, and I am afraid that more heavy casualties may take place among the Muslims wh

**ahmad 88** — pattern: `first_colon_weak`  
Full text: It was narrated from ‘Abdullah bin 'Umar, from Sa'd bin Abi Waqqas that the Messenger of Allah (ﷺ) used to wipe over his khuffain. 'Abdullah bin 'Umar asked 'Umar about that and he said: Yes, if Sa'd narrates some-thing to you from the Messenger of Allah (ﷺ), do not ask anyone else about it.  
Extracted matn: Yes, if Sa'd narrates some-thing to you from the Messenger of Allah (ﷺ), do not ask anyone else about it.

**ahmad 89** — pattern: `first_colon_weak`  
Full text: It was narrated from Ma'dan bin Abi Talhah that 'Umar bin al Khattab delivered a khutbah on Friday, and he mentioned the Prophet of Allah ﷺ and Abu Bakr رضي الله عنه . He said: I saw a dream that I can only interpret as meaning that my death is near; I saw as if a rooster pecked me twice, and I was   
Extracted matn: I saw a dream that I can only interpret as meaning that my death is near; I saw as if a rooster pecked me twice, and I was told that it was a red rooster. I told this dream to Asma’ bint 'Umais, the w

### bukhari

**bukhari 991** — pattern: `no_extract`  
Full text: Nafi` told that `Abdullah bin `Umar used to say Taslim between (the first) two Rak`at and (the third) odd one in the Witr prayer, when he wanted to attend to a certain matter (during that interval between the Rak`at).  
Extracted matn: Nafi` told that `Abdullah bin `Umar used to say Taslim between (the first) two Rak`at and (the third) odd one in the Witr prayer, when he wanted to attend to a certain matter (during that interval bet

**bukhari 4** — pattern: `first_colon_weak`  
Full text: Narrated Jabir bin 'Abdullah Al-Ansari (while talking about the period of pause in revelation) reporting the speech of the Prophet: "While I was walking, all of a sudden I heard a voice from the sky. I looked up and saw the same angel who had visited me at the cave of Hira' sitting on a chair betwee  
Extracted matn: "While I was walking, all of a sudden I heard a voice from the sky. I looked up and saw the same angel who had visited me at the cave of Hira' sitting on a chair between the sky and the earth. I got a

**bukhari 3906** — pattern: `no_extract`  
Full text: The nephew of Suraqa bin Ju'sham said that his father informed him that he heard Suraqa bin Ju'sham saying, "The messengers of the heathens of Quraish came to us declaring that they had assigned for the persons why would kill or arrest Allah's Apostle and Abu Bakr, a reward equal to their bloodmoney  
Extracted matn: The nephew of Suraqa bin Ju'sham said that his father informed him that he heard Suraqa bin Ju'sham saying, "The messengers of the heathens of Quraish came to us declaring that they had assigned for t

**bukhari 3669, 3670** — pattern: `no_extract`  
Full text: 'Aisha said (in another narration), ("When the Prophet was on his death-bed) he looked up and said thrice, (Amongst) the Highest Companion (See Qur'an 4.69)' Aisha said, Allah benefited the people by their two speeches. 'Umar frightened the people some of whom were hypocrites whom Allah caused to ab  
Extracted matn: 'Aisha said (in another narration), ("When the Prophet was on his death-bed) he looked up and said thrice, (Amongst) the Highest Companion (See Qur'an 4.69)' Aisha said, Allah benefited the people by 

**bukhari 3706** — pattern: `no_extract`  
Full text: And narrated Sad that the Prophet said to 'Ali, "Will you not be pleased from this that you are to me like Aaron was to Moses?"  
Extracted matn: And narrated Sad that the Prophet said to 'Ali, "Will you not be pleased from this that you are to me like Aaron was to Moses?"

### bulugh

**bulugh 6** — pattern: `first_colon_weak`  
Full text: Another version of Al-Bukhari has: “None of you should urinate in stagnant water that is not flowing, and then take bath in it”. A version of Muslim has the words “from it (i.e. the water)”. A version of Abu Da’ud has: “One should not take bath in it from sexual impurity”.  
Extracted matn: “None of you should urinate in stagnant water that is not flowing, and then take bath in it”. A version of Muslim has the words “from it (i.e. the water)”. A version of Abu Da’ud has: “One should not 

**bulugh 9** — pattern: `no_extract`  
Full text: And Ashab As-Sunan (compilers of the prophet’s sayings) reported that one of the wives of the Prophet (saw) took bath from a vessel, then came the Prophet (saw) and when he wanted to take bath from that (vessel), she said, “I was sexually impure”. He said, “Water does not become sexually impure”. [A  
Extracted matn: And Ashab As-Sunan (compilers of the prophet’s sayings) reported that one of the wives of the Prophet (saw) took bath from a vessel, then came the Prophet (saw) and when he wanted to take bath from th

**bulugh 10** — pattern: `first_colon_weak`  
Full text: Another version has: “he should spill the content”.  
Extracted matn: “he should spill the content”.

**bulugh 10** — pattern: `no_extract`  
Full text: At-Tirmidhi’s version has “using soil at the first or last time”.  
Extracted matn: At-Tirmidhi’s version has “using soil at the first or last time”.

**bulugh 14** — pattern: `first_colon_weak`  
Full text: and Abu Da’ud who added: “It (the fly) protects itself with the diseased wing (by dipping it first in a drink).  
Extracted matn: “It (the fly) protects itself with the diseased wing (by dipping it first in a drink).

### ibnmajah

**ibnmajah 11** — pattern: `first_colon_weak`  
Full text: Jabir bin 'Abdullah said that: We were with the Prophet (SAW), and he drew a line (in the sand), then he drew two lines to its right and two to its left. Then he put his hand on the middle line and said : 'This is the path of Allah. Then he recited the Verse: And verily, this (i.e. Allah's Commandme  
Extracted matn: We were with the Prophet (SAW), and he drew a line (in the sand), then he drew two lines to its right and two to its left. Then he put his hand on the middle line and said : 'This is the path of Allah

**ibnmajah 316** — pattern: `first_colon_weak`  
Full text: Salman said that one of the idolaters said to him, while they were making fun of him: "I see that your companion (the Prophet) is teaching you everything, even how to relieve yourselves?" He said: "Yes indeed. He has ordered us not to face the Qiblah (prayer direction) nor to clean ourselves with ou  
Extracted matn: "I see that your companion (the Prophet) is teaching you everything, even how to relieve yourselves?" He said: "Yes indeed. He has ordered us not to face the Qiblah (prayer direction) nor to clean our

**ibnmajah 434** — pattern: `first_colon_weak`  
Full text: 'Amr bin Yahya narrated that his father said to 'Abdullah bin Zaid who was the grandfather of 'Amr bin Yahya: "Can you show me how the Messenger of Allah used to perform ablution?" 'Abdullah bin Zaid said: "Yes," So he called for water, poured it over his hands and washed his hands twice. Then he ra  
Extracted matn: "Can you show me how the Messenger of Allah used to perform ablution?" 'Abdullah bin Zaid said: "Yes," So he called for water, poured it over his hands and washed his hands twice. Then he raised his m

**ibnmajah 557** — pattern: `first_colon_weak`  
Full text: It was narrated from Ubayy bin 'Imarah, in whose house the Messenger of Allah performed prayer facing both prayer direction, that : He said to the Messenger of Allah: "Can I wipe over my leather socks?" He said: "Yes." He said: "For one day?" He said: "For two days?" He said: "For three?" And so on,  
Extracted matn: He said to the Messenger of Allah: "Can I wipe over my leather socks?" He said: "Yes." He said: "For one day?" He said: "For two days?" He said: "For three?" And so on, until the number reached seven.

**ibnmajah 3804** — pattern: `first_colon_weak`  
Full text: It was narratd from Abu Hurairah that : the Prophet (SAW) used to say: "Al-hamdu lillahi 'ala kulli hal. Rabbi a'udhu bika min hali ahlin-nar (Praise is to Allah in all circumstances, O Allah, I seek refuge with You from the situation of the people of Hell)."  
Extracted matn: the Prophet (SAW) used to say: "Al-hamdu lillahi 'ala kulli hal. Rabbi a'udhu bika min hali ahlin-nar (Praise is to Allah in all circumstances, O Allah, I seek refuge with You from the situation of th

### malik

**malik 1** — pattern: `no_extract`  
Full text: He said, "Yahya ibn Yahya al-Laythi related to me from Malik ibn Anas from Ibn Shihab that one day Umar ibn Abdal-Aziz delayed the prayer. Urwa ibn az-Zubayr came and told him that al-Mughira ibn Shuba had delayed the prayer one day while he was in Kufa and Abu Masud al- Ansari had come to him and s  
Extracted matn: He said, "Yahya ibn Yahya al-Laythi related to me from Malik ibn Anas from Ibn Shihab that one day Umar ibn Abdal-Aziz delayed the prayer. Urwa ibn az-Zubayr came and told him that al-Mughira ibn Shub

**malik 2** — pattern: `no_extract`  
Full text: Urwa said that A'isha, the wife of the Prophet, may Allah bless him and grant him peace used to pray asr while the sunlight was pouring into her room, before the sun itself had become visible (i.e. because it was still high in the sky).  
Extracted matn: Urwa said that A'isha, the wife of the Prophet, may Allah bless him and grant him peace used to pray asr while the sunlight was pouring into her room, before the sun itself had become visible (i.e. be

**malik 4** — pattern: `no_extract`  
Full text: Yahya related to me from Malik from Yahya ibn Said from Amra bint Abd ar-Rahman that A'isha, the wife of the Prophet, may Allah bless him and grant him peace, said, "The Messenger of Allah, may Allah bless him and grant him peace, used to pray subh and the women would leave wrapped in their garments  
Extracted matn: Yahya related to me from Malik from Yahya ibn Said from Amra bint Abd ar-Rahman that A'isha, the wife of the Prophet, may Allah bless him and grant him peace, said, "The Messenger of Allah, may Allah 

**malik 5** — pattern: `no_extract`  
Full text: Yahya related to me from Malik from Zayd ibn Aslam from Ata ibn Yasar and from Busr ibn Said and from al-Araj-all of whom related it from Abu Hurayra - that the Messenger of Allah, may Allah bless him and grant him peace, said, "Whoever manages to do a raka of subh before the sun has risen has done   
Extracted matn: Yahya related to me from Malik from Zayd ibn Aslam from Ata ibn Yasar and from Busr ibn Said and from al-Araj-all of whom related it from Abu Hurayra - that the Messenger of Allah, may Allah bless him

**malik 6** — pattern: `no_extract`  
Full text: Yahya related to me from Malik from Nafi', the mawla of Abdullah ibn Umar, that Umar ibn al-Khattab wrote to his governors saying, "The most important of your affairs in my view is the prayer. Whoever protects it and observes it carefully is protecting his deen, while whoever is negligent about it w  
Extracted matn: Yahya related to me from Malik from Nafi', the mawla of Abdullah ibn Umar, that Umar ibn al-Khattab wrote to his governors saying, "The most important of your affairs in my view is the prayer. Whoever

### mishkat

**mishkat 208** — pattern: `no_extract`  
Full text: Anas said that when the Prophet made a statement he repeated it three times so that it would be understood, and that when he met a company and gave them a salutation he did it three times. Bukhari transmitted it.  
Extracted matn: Anas said that when the Prophet made a statement he repeated it three times so that it would be understood, and that when he met a company and gave them a salutation he did it three times. Bukhari tra

**mishkat 210** — pattern: `first_colon_weak`  
Full text: Jarir said that: One early morning when they were with God’s messenger some people came to him who were scantily clad, wearing striped woollen garments,* with swords over their shoulders; most, nay all of them, belonging to Mudar. God’s messenger showed signs of anger on his face because of the pove  
Extracted matn: One early morning when they were with God’s messenger some people came to him who were scantily clad, wearing striped woollen garments,* with swords over their shoulders; most, nay all of them, belong

**mishkat 212** — pattern: `no_extract`  
Full text: Kathir b. Qais told how, when he was sitting with Abu Darda' in the mosque of Damascus, a man came to him and said, “Abu Darda', I have come to you from the town of the Messenger for a tradition I have heard that you relate from God's messenger. I have come for no other purpose.” He replied that he   
Extracted matn: Kathir b. Qais told how, when he was sitting with Abu Darda' in the mosque of Damascus, a man came to him and said, “Abu Darda', I have come to you from the town of the Messenger for a tradition I hav

**mishkat 213, 214** — pattern: `first_colon_weak`  
Full text: Abu Umama al-Bahili said that: Two men, one learned and the other devout, were mentioned to God’s messenger, who then said, “The superiority of the learned man over the devout man is like mine over the most contemptible among you,” adding, “God, His angels, the inhabitants of the heavens and the ear  
Extracted matn: Two men, one learned and the other devout, were mentioned to God’s messenger, who then said, “The superiority of the learned man over the devout man is like mine over the most contemptible among you,”

**mishkat 230, 231** — pattern: `no_extract`  
Full text: Ibn Mas'ud said that he heard God’s messenger saying, “God brighten a man who hears something from us and conveys it to others as he heard it, for many a one to whom it is brought retains it better than the one who heard it.” Tirmidhi and Ibn Majah transmitted it, and Darimi transmitted it from Abu   
Extracted matn: Ibn Mas'ud said that he heard God’s messenger saying, “God brighten a man who hears something from us and conveys it to others as he heard it, for many a one to whom it is brought retains it better th

### muslim

**muslim 8 a** — pattern: `no_extract`  
Full text: It is narrated on the authority of Yahya b. Ya'mur that the first man who discussed qadr (Divine Decree) in Basra was Ma'bad al-Juhani. I along with Humaid b. 'Abdur-Rahman Himyari set out for pilgrimage or for 'Umrah and said: Should it so happen that we come into contact with one of the Companions  
Extracted matn: It is narrated on the authority of Yahya b. Ya'mur that the first man who discussed qadr (Divine Decree) in Basra was Ma'bad al-Juhani. I along with Humaid b. 'Abdur-Rahman Himyari set out for pilgrim

**muslim 9** — pattern: `no_extract`  
Full text: This hadith is narrated to us on the authority of Muhammad b. 'Abdullah b. Numair, on the authority of Muhammad b. Bishr, on the authority of Abd Hayyan al-Taymi with the exception that in this narration (instead of the words (Iza Waladat al'amah rabbaha), the words are (Iza Waladat al'amah Ba'laha)  
Extracted matn: This hadith is narrated to us on the authority of Muhammad b. 'Abdullah b. Numair, on the authority of Muhammad b. Bishr, on the authority of Abd Hayyan al-Taymi with the exception that in this narrat

**muslim 11 b** — pattern: `first_colon_weak`  
Full text: Another hadith, the like of which has been narrated by Malik (b. Anas) (and mentioned above) is also reported by Talha b. 'Ubaidullah, with the only variation that the Holy Prophet remarked: By his father, he shall succeed if he were true (to what he professed), or: By his father, he would enter hea  
Extracted matn: By his father, he shall succeed if he were true (to what he professed), or: By his father, he would enter heaven if he were true (to what he professed).

**muslim 13 b** — pattern: `no_extract`  
Full text: This hadith is transmitted by Muhammad b. Hatim on the authority of Abu Ayyub Ansari.  
Extracted matn: This hadith is transmitted by Muhammad b. Hatim on the authority of Abu Ayyub Ansari.

**muslim 16 d** — pattern: `first_colon_weak`  
Full text: It is reported on the authority of Ta'us that a man said to 'Abdullah son of 'Umar (may Allah be pleased with him). Why don't you carry out a military expedition? Upon which he replied: I heard the messenger of Allah (may peace be upon him) say: Verily, al-Islam is founded on five (pillars): testify  
Extracted matn: I heard the messenger of Allah (may peace be upon him) say: Verily, al-Islam is founded on five (pillars): testifying the fact that there is no god but Allah, establishment of prayer, payment of Zakat

### nasai

**nasai 823** — pattern: `first_colon_weak`  
Full text: It was narrated from Abu Hurairah that the Prophet (saws)said:"When any one of you leads the people in prayer, let him make it short, for among them are the sick, the weak and the elderly. And when any one of you prays by himself, let him make it as long as he wishes."  
Extracted matn: "When any one of you leads the people in prayer, let him make it short, for among them are the sick, the weak and the elderly. And when any one of you prays by himself, let him make it as long as he w

**nasai 824** — pattern: `no_extract`  
Full text: It was narrated from Anas that the Prophet (saws) used to make his prayer very brief but still complete when leading people.  
Extracted matn: It was narrated from Anas that the Prophet (saws) used to make his prayer very brief but still complete when leading people.

**nasai 505** — pattern: `no_extract`  
Full text: It was narrated from 'Aishah that the Messenger of Allah (PBUH) prayed 'Asr when the sun was in her room and the shadow had not appeared on her wall.  
Extracted matn: It was narrated from 'Aishah that the Messenger of Allah (PBUH) prayed 'Asr when the sun was in her room and the shadow had not appeared on her wall.

**nasai 511** — pattern: `first_colon_weak`  
Full text: Al-'Ala' narrated to us that he entered upon Anas bin Malik in his house in Al-Basrah, when he had finished Zuhr, and his house was beside the Masjid. "When we entered upon him, he said: 'Have you prayed 'Asr?' We said: 'No, we have just finished Zuhr.' He said: 'Pray 'Asr.' So we got up and prayed,  
Extracted matn: 'Have you prayed 'Asr?' We said: 'No, we have just finished Zuhr.' He said: 'Pray 'Asr.' So we got up and prayed, and when we finished he said: 'I heard the Messenger of Allah (PBUH) say: "That is the

**nasai 832** — pattern: `no_extract`  
Full text: It was narrated from Anas bin Malik that the Messenger of Allah (saws) rode a horse and fell from it, and sustained an injury on his right side. He led one of the prayers sitting, and we prayed behind him sitting. When he had finished he said: "The Imam is appointed to be followed. If he prays stand  
Extracted matn: It was narrated from Anas bin Malik that the Messenger of Allah (saws) rode a horse and fell from it, and sustained an injury on his right side. He led one of the prayers sitting, and we prayed behind

### riyadussalihin

**riyadussalihin 247** — pattern: `first_colon_weak`  
Full text: Ibn 'Abbas (May Allah bepleased with them), reported in connection with the case of Barirah (May Allah bepleased with her) and her husband: The Prophet (PBUH) said to her, "It is better for you to go back to your husband." She asked: "O Messenger of Allah, do you order me to do so." He replied, "I o  
Extracted matn: The Prophet (PBUH) said to her, "It is better for you to go back to your husband." She asked: "O Messenger of Allah, do you order me to do so." He replied, "I only intercede" She then said: "I have no

**riyadussalihin 274** — pattern: `no_extract`  
Full text: 'Abdullah bin Zam'ah (May Allah be pleased with him) reported that he heard the Prophet (PBUH) giving a speech when he mentioned the she- camel (of Prophet Salih) and the man who had killed her. Messenger of Allah (PBUH) said: "When the most wicked man among them went forth (to kill the she-camel).'  
Extracted matn: 'Abdullah bin Zam'ah (May Allah be pleased with him) reported that he heard the Prophet (PBUH) giving a speech when he mentioned the she- camel (of Prophet Salih) and the man who had killed her. Messe

**riyadussalihin 276** — pattern: `no_extract`  
Full text: 'Amr bin Al-Ahwas Al-Jushami (May Allah be pleased with him) reported that he had heard the Prophet (PBUH) saying on his Farewell Pilgrimage, after praising and glorifying Allah and admonishing people, "Treat women kindly, they are like captives in your hands; you do not owe anything else from them.  
Extracted matn: 'Amr bin Al-Ahwas Al-Jushami (May Allah be pleased with him) reported that he had heard the Prophet (PBUH) saying on his Farewell Pilgrimage, after praising and glorifying Allah and admonishing people

**riyadussalihin 292** — pattern: `no_extract`  
Full text: Sa'd bin Abu Waqqas (May Allah be pleased with him) reported in a Hadith included in the chapter of Intention, that Messenger of Allah (PBUH) said, "Whatever you spend seeking thereby the Pleasure of Allah, will have its reward, even the morsel which you put in the mouth of your wife". [Al-Bukhari a  
Extracted matn: Sa'd bin Abu Waqqas (May Allah be pleased with him) reported in a Hadith included in the chapter of Intention, that Messenger of Allah (PBUH) said, "Whatever you spend seeking thereby the Pleasure of 

**riyadussalihin 324** — pattern: `no_extract`  
Full text: It has been narrated that Maimuna bint Al-Harith (May Allah be pleased with her) had set free a slave-girl without the Prophet's permission. When her turn came (the Prophet (PBUH) used to visit his wives in turns), she made mention of that to him saying, "Did you know I have set slave-girl free?" He  
Extracted matn: It has been narrated that Maimuna bint Al-Harith (May Allah be pleased with her) had set free a slave-girl without the Prophet's permission. When her turn came (the Prophet (PBUH) used to visit his wi

### shamail

**shamail 7** — pattern: `first_colon_weak`  
Full text: On the authority of 'Umar ibn 'Abdi’llah, the Mawla of Ghufra: 1 have been told by Ibrahim ibn Muhammad, one of the offspring of 'Ali ibn Abi Talib (may Allah be well pleased with him): “When 'Ali described Allah’s Messenger (Allah bless him and give him peace),he said: "Allah’s Messenger (Allah ble  
Extracted matn: 1 have been told by Ibrahim ibn Muhammad, one of the offspring of 'Ali ibn Abi Talib (may Allah be well pleased with him): “When 'Ali described Allah’s Messenger (Allah bless him and give him peace),h

**shamail 13** — pattern: `first_colon_weak`  
Full text: On the authority of Jabir ibn ‘Abdi’llah, that Allah’s Messenger said (Allah bless him and give him peace): "The Prophets were presented to me, and there was Moses (peace be upon him), a specimen of the men of distinction, as if he were among the men of pure lineage and manly virtue [shanu’a]. I als  
Extracted matn: "The Prophets were presented to me, and there was Moses (peace be upon him), a specimen of the men of distinction, as if he were among the men of pure lineage and manly virtue [shanu’a]. I also saw Je

**shamail 19** — pattern: `first_colon_weak`  
Full text: Ibrahim ibn Muhammad, one of the offspring of 'Ali ibn Abi Talib, told me: “When 'Ali described Allah’s Messenger (Allah bless him and give him peace)— then he related the tradition in full—he said: 'Between his shoulders was the Seal of Prophethood, for he is the Seal of the Prophets'."  
Extracted matn: “When 'Ali described Allah’s Messenger (Allah bless him and give him peace)— then he related the tradition in full—he said: 'Between his shoulders was the Seal of Prophethood, for he is the Seal of th

**shamail 20** — pattern: `first_colon_weak`  
Full text: Abu Zaid 'Amr ibn Akhtab al-Ansari told me: “Allah’s Messenger (Allah bless him and give him peace) said to me: ‘O Abu Zaid, come close to me and stroke my back!’ I duly stroked his back, whereupon my fingers touched the Seal. I said: ‘What is the Seal?’ He said; ‘Intertwined hairs.’”  
Extracted matn: “Allah’s Messenger (Allah bless him and give him peace) said to me: ‘O Abu Zaid, come close to me and stroke my back!’ I duly stroked his back, whereupon my fingers touched the Seal. I said: ‘What is 

**shamail 36** — pattern: `first_colon_weak`  
Full text: Humaid ibn 'Abd ar-Rahman relates on the authority of a man from among the Companions of the Prophet (Allah bless him and give him peace): "The Prophet (Allah bless him and give him peace) used to comb his hair at intervals.”  
Extracted matn: "The Prophet (Allah bless him and give him peace) used to comb his hair at intervals.”

### tirmidhi

**tirmidhi 2514** — pattern: `first_colon_weak`  
Full text: Abu 'Uthman narrated from Hanzalah Al-Usaidi – and he was one of the scribes of the Messenger of Allah (s.a.w)- that he passed by Abu Bakr while he was crying, so he(Abu Bakr) said to him: “What is wrong with you, O Hanzalah?” He replied: “Hanzalah has become a hypocrite O Abu Bakr! When we are with  
Extracted matn: “What is wrong with you, O Hanzalah?” He replied: “Hanzalah has become a hypocrite O Abu Bakr! When we are with the Messenger of Allah (s.a.w) we remember the Fire and Paradise as if we are looking at

**tirmidhi 2519** — pattern: `no_extract`  
Full text: Muhammad bin Al-Munkadir narrated from Jabir, that a man was mentioned in the presence of the Prophet (s.a.w) for his worship and striving in it, and another man was mentioned for his cautious piety. So the Prophet (s.a.w) said: "Nothing is equal to cautious piety."  
Extracted matn: Muhammad bin Al-Munkadir narrated from Jabir, that a man was mentioned in the presence of the Prophet (s.a.w) for his worship and striving in it, and another man was mentioned for his cautious piety. 

**tirmidhi 2534** — pattern: `first_colon_weak`  
Full text: (Another chain:) From 'Abdullah bin Mas'ud, similar in meaning, and he did not report it in Marfu' form. And this is more correct than the narration of 'Abidah bin Humaid (a narrator in no.2533), and it has been reported like this by Jarir and more than one from 'Ata' bin As-Sa'ib, and they did not   
Extracted matn: ) From 'Abdullah bin Mas'ud, similar in meaning, and he did not report it in Marfu' form. And this is more correct than the narration of 'Abidah bin Humaid (a narrator in no.2533), and it has been rep

**tirmidhi 1342** — pattern: `no_extract`  
Full text: Ibn 'Abbas narrated that the Messenger of Allah (saws) judged that the oath is due from the one the claim is made against.  
Extracted matn: Ibn 'Abbas narrated that the Messenger of Allah (saws) judged that the oath is due from the one the claim is made against.

**tirmidhi 1360** — pattern: `no_extract`  
Full text: Anas narrated that the Messenger of Allah (saws) borrowed a bowl which broke, so he guaranteed (compensated) it for them.  
Extracted matn: Anas narrated that the Messenger of Allah (saws) borrowed a bowl which broke, so he guaranteed (compensated) it for them.

### virtues

**virtues 1** — pattern: `no_extract`  
Full text: Abu Sa’id bin al-Mu’alla (RA) reported, “I was praying when the Messenger of Allah ﷺ passed by me and called me. I didn’t come to him until I finished praying. Then I came to him and he said, “What prevented you from coming? Didn’t Allah say, ‘O you who believe, respond to Allah and to the Messenger  
Extracted matn: Abu Sa’id bin al-Mu’alla (RA) reported, “I was praying when the Messenger of Allah ﷺ passed by me and called me. I didn’t come to him until I finished praying. Then I came to him and he said, “What pr

**virtues 4** — pattern: `no_extract`  
Full text: Abdullāh b. Abbās reported that while Angel Jibreel was sitting with the Messenger of Allah ﷺ, he heard a sound above him. He lifted his head, and said, “This is a gate which has been opened in heaven today. It was never opened before.” Then an Angel descended through it, he said, “This is an Angel   
Extracted matn: Abdullāh b. Abbās reported that while Angel Jibreel was sitting with the Messenger of Allah ﷺ, he heard a sound above him. He lifted his head, and said, “This is a gate which has been opened in heaven

**virtues 33** — pattern: `no_extract`  
Full text: Abu Dāwūd mentioned that it was reported with a variation through Qatādah, “…whoever memorizes the concluding verses of Sūrat al-Kahf,” and from Shu’bah via Qatādah, “from the end of Al-Kahf…” Reference: Sunan ad-Darimi 4323  
Extracted matn: Abu Dāwūd mentioned that it was reported with a variation through Qatādah, “…whoever memorizes the concluding verses of Sūrat al-Kahf,” and from Shu’bah via Qatādah, “from the end of Al-Kahf…” Referen

**virtues 34** — pattern: `first_colon_weak`  
Full text: It was also reported via Khalid b. Ma’dān: “Whoever recites ten verses from Sūrat al-Kahf, will not fear Al-Dajjāl.” Reference: Sunan ad-Darimi 3310  
Extracted matn: “Whoever recites ten verses from Sūrat al-Kahf, will not fear Al-Dajjāl.” Reference: Sunan ad-Darimi 3310

**virtues 67** — pattern: `first_colon_weak`  
Full text: The Messenger of Allah ﷺ would pray two rakʿahs after witr while sitting, reciting in the two rakʿahs “Idhā zulzilat al-ardhu…” (Sūrah al-Zalzalah) and “Qul Ya Ayyuhal-Kafirun” (Sūrat al-Kāfirūn). Reference: Zad al-Ma`ad 1/322 Is Sūrat al-Zalzalah equivalent to one-fourth of the Qur’an? The reports   
Extracted matn: Zad al-Ma`ad 1/322 Is Sūrat al-Zalzalah equivalent to one-fourth of the Qur’an? The reports about Sūrat Al-Zalzalah being equivalent to one-fourth of the Qur’an have some weakness in them, although th
