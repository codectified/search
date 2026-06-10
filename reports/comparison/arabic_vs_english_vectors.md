# Arabic Matn Vectors vs English Text Vectors

**Model:** OpenAI `text-embedding-3-small` (same for all)

**arabic-openai:** Arabic matn embedded (clean matn where ✓, regex-extracted where ~) · filtered to ~44.9k bilingual hadiths

**mxbai baseline:** English text embedded · ~48k English hadiths · mxbai-embed-large · scores 0.78–0.81

**openai-small-en baseline:** English text embedded · ~48k English hadiths · same model · scores 0.67–0.69


> Baseline data from `lexical vs hybrid vs semantic/report1.md` (2026-05-20, query: comparing yourself to others)


## Summary

| Query | Embed ms | kNN ms | Top score | Score range |
|---|---|---|---|---|
| prayer times | 1805 | 55 | 0.7330 | 0.6947–0.7330 |
| comparing yourself to others | 1003 | 44 | 0.6555 | 0.6404–0.6555 |
| zakah on wealth | 979 | 29 | 0.6946 | 0.6724–0.6946 |
| treatment of parents | 325 | 33 | 0.6641 | 0.6294–0.6641 |
| aisha | 376 | 41 | 0.6957 | 0.6695–0.6957 |

---

## "prayer times"

Embed: **1805ms** · kNN (English-filtered, 20 results): **55ms**

### arabic-openai — Arabic matn vectors (English-only hadiths)

| # | Score | Collection | Hadith | Cluster | Matn tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.7330 | muslim | 612 e | C61 | ~ regex | 'Abdullah b. 'Amr b. al-'As reported: The Messenger of Allah (may peace be upon him) was asked about the times of prayers. He said: The time for the morning prayer (lasts) as long as the first visible part of the rising sun does not appear and the time of the noon prayer is when the sun declines from the zenith and there is not a time for the after |
| 2 | 0.7293 | nasai | 522 | C61 | ~ regex | It was narrated from 'Abdullah bin 'Amr - and (one of the narrators) Shu'bah said: "Sometimes he (Qatadah, his teacher) narrated it as a Marfu' report and sometimes he did not" - "The time for Zuhr prayer is until 'Asr comes, and the time for 'Asr prayer is until the sun turns yellow. the time for Maghrib is until the twilight disappears, and the t |
| 3 | 0.7172 | nasai | 642 | C9 | ~ regex | It was narrated from Anas that someone asked the Messenger of Allah (S.A.W) about the time of Subh. The Messenger of Allah (S.A.W) commanded Bilal to call the Adhan when dawn broke. Then the next day he delayed Fajr until it was very light, then he told him to call the Adhan and he prayed. Then he said: "This is the time for the prayer." |
| 4 | 0.7148 | bukhari | 581 | C61 | ✓ clean | Narrated `Umar: "The Prophet forbade praying after the Fajr prayer till the sun rises and after the `Asr prayer till the sun sets." Narrated Ibn `Abbas: Some people told me the same narration (as above). |
| 5 | 0.7132 | nasai | 572 | C61 | ~ regex | Abu Yahya Sulaim bin 'Amir, Damrah bin Habib and Abu Talhah Nu'aim bin Ziyad said: "We heard Abu Umamah Al-Bahili say: 'I heard 'Amrah bin 'Abasah say: I said: 'O Messenger of Allah, is there any moment which brings one close to Allah than another, or any moment that should be sought out for remembering Allah? He said: 'Yes, the closest that the Lo |
| 6 | 0.7103 | ibnmajah | 1249 | C61 | ~ regex | It was narrated from Abu Sa’eed Al-Khudri that the Prophet (saw) said: “There is no prayer after the ‘Asr until the sun has set, and there is no prayer after the Fajr until the sun has risen.” |
| 7 | 0.7100 | abudawud | 428 | C61 | ~ regex | Narrated Fudalah: The Messenger of Allah (saws) taught me and what he taught me is this: Observe the five prayers regularly. He said: I told (him): I have many works at these times; so give me a comprehensive advice which, if I follow, should be enough for me. He said: Observe the two afternoon prayers (al-asrayn). But the term al-asrayn (two after |
| 8 | 0.7079 | nasai | 518 | C61 | ~ regex | It was narrated from Nasr bin 'Abdur-Rahman, from his grandfather Mu'adh, that he performed Tawaf with Mu'adh bin 'Afra' but he did not pray. "I said: 'Are you not going to pray?' He said: 'The Messenger of Allah (PBUH) said: 'There is no prayer after 'Asr until the sun has set, nor after Subh until the sun has risen.'" |
| 9 | 0.7061 | ahmad | 130 | C61 | ~ regex | It was narrated that Ibn 'Abbas said: Some righteous men, including ‘Umar - and the most righteous of them in my view was 'Umar - confirmed when I was present that the Messenger of Allah ﷺ said: `There is no prayer after Fajr until the sun rises and there is no prayer after 'Asr until the sun sets.` |
| 10 | 0.7059 | ibnmajah | 1250 | C61 | ~ regex | It was narrated that Ibn ‘Abbas said: “Good men among whom was ‘Umar bin Khattab, and the best of them in my view is ‘Umar, testified before me that the Messenger of Allah (saw) said: ‘There is no prayer after Fajr until the sun has risen, and there is no prayer after the ‘Asr until the sun has set.’” |
| 11 | 0.7016 | nasai | 571 | C23 | ~ regex | Ibn 'Umar said: "The Messenger of Allah (PBUH) said: 'When the edge of the sun rises, then delay prayer until it has fully risen, and when the edge of the sun starts to set, delay prayer until it has fully set.'" |
| 12 | 0.7009 | abudawud | 1276 | C61 | ~ regex | Narrated Abdullah ibn Abbas: Some reliable people testified before me, and among them was Umar ibn al-Khattab, and most reliable in my eyes was Umar: The Prophet of Allah (saws) said: There is no prayer after the dawn prayer until the sun rises; and there is no prayer after the 'Asr prayer until the sun sets. |
| 13 | 0.7008 | bukhari | 214 | C9 | ✓ clean | Narrated `Amr bin `Amir: Anas said, "The Prophet used to perform ablution for every prayer." I asked Anas, "What did you used to do?' Anas replied, "We used to pray with the same ablution until we break it with Hadath." |
| 14 | 0.6999 | bukhari | 586 | C61 | ✓ clean | Narrated Abu Sa`id Al-Khudri: I heard Allah's Apostle saying, "There is no prayer after the morning prayer till the sun rises, and there is no prayer after the `Asr prayer till the sun sets." |
| 15 | 0.6997 | ahmad | 110 | C61 | ~ regex | It was narrated that Ibn ‘Abbas said: Some men of good character, among whom was ‘Umar, testified before me, and the best of them in my view was ‘Umar, that the Prophet of Allah ﷺ used to say: `There is no prayer after 'Asr prayer until the sun sets, and there is no prayer after Fajr prayer until the sun rises.` |
| 16 | 0.6988 | nasai | 567 | C61 | ~ regex | It was narrated from 'Ata' bin Yazid that he heard Abu Sa'eed Al-Khudri say: "I heard the Messenger of Allah (PBUH) say: 'There is no prayer after Fajr until the sun has clearly risen, and no prayer after 'Asr until the sun has fully set.'" |
| 17 | 0.6968 | muslim | 829 | C23 | ~ regex | Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: When the rim of the sun starts appearing defer prayer till it completely appears, and when the rim of the sun disappears defer prayer till it completely disappears. |
| 18 | 0.6960 | muslim | 612 a | C61 | ~ regex | It was narrated from 'Abdullah bin 'Amr that the Prophet (saws) said: "When you pray Fajr, its time is until the first part of the sun appears. When you pray Zuhr, its time is until 'Asr comes. When you pray 'Asr, its time is until the sun turns yellow. When you pray Maghrib, its time is until the twilight has disappeared. When you pray 'Isha, its  |
| 19 | 0.6952 | ibnmajah | 1252 | C61 | ~ regex | It was narrated that Abu Hurairah said: “Safwan bin Mu’attal asked the Messenger of Allah (saw): ‘O Messenger of Allah, I want to ask you about something of which you have knowledge and I know nothing.’ He said: ‘What is it?’ He said: ‘Is there any time of the night or day when it is disliked to perform prayer? He said: ‘Yes, when you have prayed t |
| 20 | 0.6947 | ibnmajah | 1413 | C9 | ~ regex | It was narrated that Anas bin Malik said: “The Messenger of Allah (saw) said: ‘A man’s prayer in his house is equal (in reward) to one prayer; his prayer in the mosque of the tribes is equal to twenty-five prayers; his prayer in the mosque in which Friday prayer is offered is equal to five-hundred prayers; his prayer in Aqsa Mosque is equal to fift |

---

## "comparing yourself to others"

Embed: **1003ms** · kNN (English-filtered, 20 results): **44ms**

### arabic-openai — Arabic matn vectors (English-only hadiths)

| # | Score | Collection | Hadith | Cluster | Matn tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.6555 | ibnmajah | 1977 | C16 | ~ regex | It was narrated from Ibn 'Abbas that: the Prophet said: "The best of you is the one who is best to his wife, and I am the best of you to my wives." |
| 2 | 0.6531 | muslim | 2684 d | C16 | ~ regex | A hadith like this has been narrated on the authority of A'isha through another chain of transmitters. |
| 3 | 0.6511 | muslim | 2540 | C23 | ~ regex | Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Do not revile my Companions, do not revile my Companions. By Him in Whose Hand is my life, if one amongst you would have spent as much gold as Uhud it would not amount to as much as one much on behalf of one of them or half of it. |
| 4 | 0.6482 | bukhari | 4547 | C24 | ✓ clean | Narrated `Aisha: Allah's Apostle recited the Verse:-- "It is He who has sent down to you the Book. In it are Verses that are entirely clear, they are the foundation of the Book, others not entirely clear. So as for those in whose hearts there is a deviation (from the Truth ). follow thereof that is not entirely clear seeking affliction and searchin |
| 5 | 0.6475 | nasai | 1130 | C64 | ~ regex | It was narrated that 'Aishah said: "I noticed the Messenger of Allah (SAW) was missing one night and I found him prostrating with the tops of his feet facing toward the Qiblah. I heard him saying: 'A'udhu biridaka min sakhatika, wa a'udhu bimu 'afatika min 'uqubatika wa a'udhu bika minka la uhsi thana'an 'alaika anta kama athnaita 'ala nafsik (I se |
| 6 | 0.6475 | abudawud | 879 | C64 | ~ regex | ‘A’ishah said; one night I missed the Messenger of Allah (may peace be upon him) and when I sought him on the spot of prayer I found him in prostration with his feet raised, and he was saying:”(O Allah), I seek refuge in Your good pleasure from Your anger, and in Your Mercy from Your Punishment, and I seek refuge from You in You; I am not able to p |
| 7 | 0.6471 | mishkat | 4347 | C54 | ~ regex | He reported God’s messenger as saying, “He who copies any people is one of them.” Ahmad and Abu Dawud transmitted it. |
| 8 | 0.6470 | nasai | 169 | C64 | ~ regex | It was narrated from Abu Hurairah that 'Aishah said: "I noticed the Prophet (PBUH) was not there one night, so I started looking for him with my hand. My hand touched his feet and they were held upright, and he was prostrating and saying: 'I seek refuge in Your pleasure from Your anger, in Your forgiveness from Your punishment, and I seek refuge in |
| 9 | 0.6449 | muslim | 2541 a | C23 | ~ regex | Abu Sa'id reported there was some altercation between Khalid b. Walid and Abd al-Rahman b. 'Auf and Khalid reviled him. Thereupon Allah's Messwger (may peace be upon him) said: None should revile my Companions. for if one amongst you were to spend as much gold as Uhud, it would not amount to as much as one mudd of one of them or half of it. |
| 10 | 0.6442 | nasai | 3614 | C63 | ~ regex | Abu Habibah At-Ta'i said: "A man made a will leaving some Dinars (to be spent) in the cause of Allah. Abu Ad-Darda' was asked about that, and he narrated that the Prophet said: 'The likeness of the one who frees a slave or gives some charity when he is dying, is that of a man who gives a gift after he has eaten his fill.'" |
| 11 | 0.6439 | muslim | 2665 | C23 | ~ regex | 'A'isha reported that Allah's Messenger (may peace be upon him) recited (these verses of the Qur'an): "He it is Who revealed to thee (Muhammad) the Book (the Qur'an) wherein there are clear revelations-these are the substance of the Book and others are allegorical (verses). And as for those who have a yearning for error they go after the allegorica |
| 12 | 0.6437 | muslim | 572 l | C35 | ~ regex | 'Abdullah (b. Mas'ud) reported: The Messenger of Allah (may peace be upon him) said prayer and he omitted or committed (something). Ibrahim (one of the narrators of this hadith) said: It is my doubt, and it was said: Messenger of Allah, has there been any addition to the prayer? He (the Holy Prophet) said: Verily I am a human being like you. I forg |
| 13 | 0.6432 | muslim | 1102 b | C16 | ~ regex | Ibn 'Umar reported that the Messenger of Allah (may peace be upon him) observed fasts uninterruptedly in Ramadan and the people (in his wake) did this. But he forbade them to do so. It was said to him (to the Holy Prophet): You yourself observe the fasts uninterruptedly (but you forbid us to do so) Upon this he said: I am not like you; I am fed and |
| 14 | 0.6426 | nasai | 905 | C9 | ~ regex | It was narrated that Nu'aim Al-Mujmir said: "I prayed behind Abu Hurairah and he recited: In the Name of Allah, the Most Gracious, the Most Merciful, then he recited Umm Al-Qur'an (Al Fatihah), and when he reached: not (the way) of those who earned Your anger, nor of those who went astray, he said: 'Amin and the people said 'Amin. And every time he |
| 15 | 0.6426 | nasai | 1023 | C9 | ~ regex | It was narrated from Abu Salamah bin Abdur-Rahman that: Marwan appointed Abu Hurairah as governor of Al-Madinah. When he stood to offer an obligatory prayer, he would say the takbir, then he said the takbir when he bowed, and when he raised his head from bowing he said: "Sami' Allahu liman hamidah, Rabbana wa lakal-hamd (Allah hears those who prais |
| 16 | 0.6426 | muslim | 392 d | C9 | ~ regex | Abu Salama b. 'Abd al-Rahman reported.. When Marwan appointed Abu Huraira as his deputy in Medina, he recited takbir whenever he got up for obligatory prayer, and the rest of the hadith is the same as transmitted by Ibn Juraij (but with the addition of these words): On completing the prayer with salutation, and he turned to the people in the mosque |
| 17 | 0.6416 | nasai | 516 | C66 | ~ regex | It was narrated from Abu Hurairah that the Prophet (PBUH) said: "If any one of you catches the first prostration of 'Asr prayer before the sun sets, let him complete his prayer, and if he catches up with the first prostration of Fajr prayer before the sub rises, let him complete his prayer." |
| 18 | 0.6405 | ibnmajah | 1540 | C16 | ~ regex | It was narrated from Thawban that the Messenger of Allah (SAW) said: “Whoever offers the funeral prayer will have one Qirat and whoever attends the burial will have two Qirat.” The Prophet (SAW) was asked about the Qirat and he said: “(It is) like Uhud.” |
| 19 | 0.6405 | muslim | 946 b | C16 | ~ regex | This hadith has been narrated by Qatada with the same chain of transmitters. And in the hadith transmitted by Sa'id and Hisham, (the words are):" The Apostle of Allah (may peace be upon him) was asked about qirat, and he said: It is equivalent to Uhud." |
| 20 | 0.6404 | adab | 328 | C71 | ~ regex | Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faults." |

### mxbai baseline — English vectors (top 10)

*Source: lexical vs hybrid vs semantic/report1.md — mxbai-embed-large semantic (pure vector, no lexical boost)*

| # | Score | Hadith | Relevance | Text |
|---|---|---|---|---|
| 1 | 0.8147 | forty 18 | ✅ | The felicitous person takes lessons from (the actions of) others. |
| 2 | 0.8022 | bukhari 6490 | ✅ | Allah's Apostle said, 'If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him.' |
| 3 | 0.7969 | forty 3 | 〰 | A Muslim is a mirror of the Muslim. |
| 4 | 0.7940 | muslim 2963a | ✅ | When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you. |
| 5 | 0.7920 | ibnmajah 4336 | 〰 | Lengthy hadith about the marketplace of Paradise; passages on people of different status meeting without inferiority. |
| 6 | 0.7897 | adab 159 | 〰 | Abu'd-Darda' said: We know you better than the veterinarian knows his animals. The best is the one whose good is hoped for and whose evil you are safe from. |
| 7 | 0.7864 | riyadussalihin 466 | ✅ | Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you. |
| 8 | 0.7854 | muslim 2536 | 〰 | 'A'isha reported: The Prophet said the best people are of the generation to which I belong, then the second, then the third. |
| 9 | 0.7821 | tirmidhi 2513 | ✅ | Look to one who is lower than you, and do not look to one who is above you. For that is more worthy that you not belittle Allah's favors. |
| 10 | 0.7821 | abudawud 4092 | 〰 | A man said: I like beauty and do not like that anyone excels me. Is it pride? The Prophet replied: No, pride is disdaining what is true and despising people. |

### openai-small-en baseline — English vectors (top 7)

*Source: lexical vs hybrid vs semantic/report1.md — openai text-embedding-3-small, English corpus semantic (pure vector, no lexical boost)*

| # | Score | Hadith | Relevance | Text |
|---|---|---|---|---|
| 1 | 0.6896 | adab 328 | ✅ | Ibn 'Abbas said: When you want to mention your companion's faults, remember your own faults. |
| 2 | 0.6896 | bukhari 6490 | ✅ | Allah's Apostle said: If anyone of you looked at a person who was made superior to him in property and appearance, then he should also look at the one who is inferior to him. |
| 3 | 0.6851 | riyadussalihin 466 | ✅ | Look at those who are inferior to you and do not look at those who are superior to you. |
| 4 | 0.6775 | ahmad 111 | 〰 | 'Umar: I am afraid that if you tell them stories you will think you are better than them, until you imagine you are as far above them as the Pleiades. |
| 5 | 0.6753 | forty 18 | ✅ | The felicitous person takes lessons from (the actions of) others. |
| 6 | 0.6708 | muslim 2963c | ✅ | Look at those who stand at a lower level than you but don't look at those who stand at a higher level, for that is better-suited that you do not disparage Allah's favors. |
| 7 | 0.6669 | adab 592 | ✅ | Abu Hurayra said: One of you looks at the mote in his brother's eye while forgetting the stump in his own eye. |

---

## "zakah on wealth"

Embed: **979ms** · kNN (English-filtered, 20 results): **29ms**

### arabic-openai — Arabic matn vectors (English-only hadiths)

| # | Score | Collection | Hadith | Cluster | Matn tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.6946 | ibnmajah | 1789 | C25 | ~ regex | Fatima bint Qais narrated that: she heard him, meaning the Prophet say: “There is nothing due on wealth other then Zakat.” |
| 2 | 0.6884 | ibnmajah | 4130 | C59 | ~ regex | It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “The wealthiest will be the lowest on the Day of Resurrection, except those who do such and such with their money, and earn it from good sources.” |
| 3 | 0.6841 | nasai | 4294 | C23 | ~ regex | It was narrated that Waqi bin Khadij said: "The Messenger of Allah said: 'The worst of earnings arte the gift of a female fornicator, the price of a dog and the earnings of a cupper."" |
| 4 | 0.6808 | mishkat | 2763 | C54 | ~ regex | Rafi' b. Khadij reported God’s Messenger as saying, "The price paid for a dog is impure, the hire paid to a prostitute is impure, and the earnings of a cupper are impure.” Muslim transmitted it. |
| 5 | 0.6806 | adab | 444 | C31 | ~ regex | Abu'l-'Ubaydayn said, "I asked 'Abdullah about those who squander and he said, 'They are those who spend incorrectly.'" |
| 6 | 0.6802 | muslim | 1568 a | C59 | ~ regex | Rafi b. Khadij (Allah be pleased with him) reported: I heard Allah's Apostle (may peace be upon him) as saying: The worst earning is the earning of a prostitute, the price of a dog and the earning of a cupper. |
| 7 | 0.6794 | ibnmajah | 1472 | C5 | ~ regex | It was narrated from Ibn ‘Abbas that the Messenger of Allah (SAW) said: “The best of your garments are those which are white, so shroud your dead in them, and wear them.” |
| 8 | 0.6784 | ibnmajah | 4219 | C23 | ~ regex | It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’ |
| 9 | 0.6782 | ibnmajah | 3566 | C5 | ~ regex | It was narrated from Ibn ‘Abbas that the Messenger of Allah (saw) said: “The best of your garments are the white ones, so wear them and shroud your dead in them.” |
| 10 | 0.6778 | muslim | 21 c | C31 | ~ regex | It is narrated on the authority of Jabir that the Messenger of Allah said: I have been commanded that I should fight against people till they declare that there is no god but Allah, and when they profess it that there is no god but Allah, their blood and riches are guaranteed protection on my behalf except where it is justified by law, and their af |
| 11 | 0.6758 | abudawud | 866 | C59 | ~ regex | Narrated Tamim ad-Dari: Tamim reported this tradition from the Prophet (saws) as (Hadith No 863). This version adds: Then zakat will be considered in a similar way. Then all the actions will be considered accordingly. |
| 12 | 0.6745 | muslim | 1588 c | C23 | ~ regex | Abu Huraira (Allah be pleased with him) reported Allah's Mess-., nger (may peace be upon him) as saying: Gold is to be paid for by gold with equal weight, like for like, and silver is to be paid for by silver with equal weight, like for like. He who made an addition to it or demanded an addition dealt in usury. |
| 13 | 0.6744 | muslim | 1568 b | C73 | ~ regex | Rafi b. Khadij reported Allah'& Messenger (may peace be upon him) as saying: The price of a dog is evil, the earning of a prostitute is evil and the earning of a cupper is evil. |
| 14 | 0.6743 | abudawud | 2916 | C23 | ~ regex | Narrated 'Aishah: The Messenger of Allah (saws) as saying: The right of inheritance belongs to only to the one who paid the price (of the slave) and patronised him by doing an act of gratitude. |
| 15 | 0.6741 | abudawud | 4063 | C31 | ~ regex | Abu al-Ahwas quoted his father saying: I came to the Prophet (saws) wearing a poor garment and he said (to me): Have you any property? He replied: Yes. He asked: What kind is it? He said: Allah has given me camels. Sheep, horses and slaves. He then said: When Allah gives you property, let the mark of Allah's favour and honour to you be seen. |
| 16 | 0.6737 | nasai | 5224 | C31 | ~ regex | It was narrated from Abu Al-Ahwas, from his father, : That he came to the Prophet [SAW] wearing shabby clothes. The Prophet [SAW] said to him: "Do you have any wealth?" He said: "Yes, all kinds of wealth." He said: "What kinds of wealth?" He said: "Allah has given me camels, cattle, sheep, horses and slaves." He said: "If Allah has given you wealth |
| 17 | 0.6733 | nasai | 5418 | C59 | ~ regex | It was narrated that Jabir bin 'Abdullah said: "A man among the Ansar stated that his salve was to be set free after he died; he was in need, and he owed a debt. The Messenger of Allah [SAW] sold him (the slave) for eight hundred Dirhams, and he gave (the money) to him and said: 'Pay off your debt and spend on your dependents.'" |
| 18 | 0.6731 | bukhari | 5962 | C73 | ✓ clean | Narrated Abu Juhaifa: that he had bought a slave whose profession was cupping. The Prophet forbade taking the price of blood and the price of a dog and the earnings of a prostitute, and cursed the one who took or gave (Riba') usury, and the lady who tattooed others or got herself tattooed, and the picture-maker. |
| 19 | 0.6728 | riyadussalihin | 1824 | C54 | ~ regex | Abu Sa'id Al-Khudri (May Allah be pleased with him) said: The Prophet (PBUH) said, "From your caliphs there will be one in the Last Days who will distribute wealth without counting it." [Muslim] . |
| 20 | 0.6724 | nasai | 4569 | C23 | ~ regex | It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Gold for gold, weight for weight, like for like; and silver for silver, weight for weight, like for like. Whoever gives more or takes more has engaged in Riba."' |

---

## "treatment of parents"

Embed: **325ms** · kNN (English-filtered, 20 results): **33ms**

### arabic-openai — Arabic matn vectors (English-only hadiths)

| # | Score | Collection | Hadith | Cluster | Matn tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.6641 | riyadussalihin | 846 | C54 | ~ regex | Al-Bara' bin 'Azib (May Allah be pleased with them) reported: The Messenger of Allah (PBUH) commanded us to do seven things: to visit the sick, to follow the funeral (of a dead believer), to invoke the Mercy of Allah upon one who sneezes (i.e., by saying to him: Yarhamuk- Allah), to support the weak, to help the oppressed, to promote the greeting o |
| 2 | 0.6518 | bukhari | 448 | C30 | ✓ clean | Narrated Sahl: Allah's Apostle sent someone to a woman telling her to "Order her slave, carpenter, to prepare a wooden pulpit for him to sit on." |
| 3 | 0.6501 | adab | 2 | C30 | ~ regex | 'Abdullah ibn 'Umar said, "The pleasure of the Lord lies in the pleasure of the parent. The anger of the Lord lies in the anger of the parent." |
| 4 | 0.6475 | ibnmajah | 794 | C12 | ~ regex | Ibn 'Abbas and Ibn 'Umar narrated that: They heard the Prophet say on his pulpit: "People should desist from failing to attend the congregations, otherwise Allah will seal their hearts, and they will be among the negligent." |
| 5 | 0.6463 | ibnmajah | 3863 | C30 | ~ regex | It was narrated that Umm Haim bint Wadda' Al-Khuza'iyyah said: "I heard the Messenger of Allah (saas) say: 'The supplication of a father reaches the Veil (i.e. the place of repentance).'" |
| 6 | 0.6448 | riyadussalihin | 897 | C37 | ~ regex | Abu Musa (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "Visit the sick, feed the hungry, and (arrange for the) release of the captive.'' [Al-Bukhari] . |
| 7 | 0.6436 | riyadussalihin | 239 | C37 | ~ regex | Al-Bara' bin 'Azib (May Allah bepleased with them) reported: The Prophet (PBUH) commanded us to observe seven things and forbade us seven. He ordered us to visit the sick; to follow funeral processions; to respond to a sneezer with 'Yarhamuk-Allah (May Allah have mercy on you)' when he says 'Al-hamdu lillah (Praise be to Allah),' to help the oppres |
| 8 | 0.6402 | ahmad | 346 | C30 | ~ regex | It was narrated from ‘Amr bin Shu`aib from his father that his grandfather said: A man killed his (own) son deliberately and the case was referred to `Umar bin al Khattab (رضي الله عنه), who ruled that the murderer should pay one hundred camels (as diyah): thirty three-year-old she-camels, thirty four-year-old she-camels and forty five-year-old she |
| 9 | 0.6383 | adab | 1064 | C30 | ~ regex | 'Abdullah said, "A man asks permission of his father, his mother, his brother and his sister." |
| 10 | 0.6382 | riyadussalihin | 906 | C54 | ~ regex | Ibn 'Abbas (May Allah be pleased with them) reported: The Prophet (PBUH) said, "He who visits a sick person who is not on the point of death and supplicates seven times: As'alullahal-'Azima Rabbal-'Arshil-'Azimi, an yashfiyaka (I beseech Allah the Great, the Rubb of the Great Throne, to heal you), Allah will certainly heal him from that sickness."  |
| 11 | 0.6373 | ibnmajah | 3670 | C56 | ~ regex | It was narrated from Ibn Abbas that the Messenger of Allah(SAW) said: "There is no man whose two daughters reach the age of puberty and he treats them kindly for the time they are together, but they will gain him admittance to Paradise." |
| 12 | 0.6363 | muslim | 865 | C12 | ~ regex | Abdullah b. Umar and Abu Huraira said that they heard Allah's Messenger (may peace be upon him) say on the planks of his pulpit: People must cease to neglect the Friday prayer or Allah will seal their hearts and then they will be among the negligent. |
| 13 | 0.6353 | ibnmajah | 2662 | C30 | ~ regex | It was narrated from 'Amr bin Shu'aib, from his father, from his grandfather, that 'Umar bin Khattab said: “I heard the Messenger of Allah (SAW) say: 'A father should not be killed for his son.'” |
| 14 | 0.6347 | ibnmajah | 4234 | C70 | ~ regex | It was narrated from Anas that the Messenger of Allah (saw) said: “The son of Adam grows old but two things remain young in him: His craving for wealth and his craving for a long life.” |
| 15 | 0.6343 | nasai | 4211 | C12 | ~ regex | it was narrated from Abu Hurairah that the Prophet said: "You will become keen for positions of authority, but that will become a regret and loss. What a good life they will live, but how hard it will be for them when they die." |
| 16 | 0.6312 | riyadussalihin | 1803 | C37 | ~ regex | Abu Hurairah (May Allah be pleased with him) said: The Prophet (PBUH) said, "Do not turn away from your fathers, for he who turns away from his father, will be guilty of committing an act of disbelief." [Al-Bukhari and Muslim] |
| 17 | 0.6311 | nasai | 610 | C9 | ~ regex | Al-Walid bin Al'Ayzar said: "I heard Abu 'Amr Ash-Shaibani say: 'The owner of this house - and he pointed to the house of 'Abdullah - said: I asked the Messenger of Allah (PBUH): 'Which deed is most beloved to Allah, may He be exalted?' He said: 'Prayer offered on time, honoring one's parents, and Jihad in the cause of Allah.'" |
| 18 | 0.6307 | riyadussalihin | 895 | C37 | ~ regex | Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "Every Muslim has five rights over another Muslim (i.e., he has to perform five duties for another Muslim): to return the greetings, to visit the sick, to accompany funeral processions, to accept an invitation, to respond to the sneezer [i.e., to say: 'Yarham |
| 19 | 0.6299 | ahmad | 1147 | C7 | ~ regex | It was narrated that Sa`d bin Ibraheem said: I heard ‘Abdullah bin Shaddad say: `Ali (رضي الله عنه) said: I never saw the Messenger of Allah (ﷺ) mention both of his parents for anyone except Sa`d bin Malik (رضي الله عنه). On the day of Uhud he started saying: `Shoot, may my father and mother be sacrificed for you!” |
| 20 | 0.6294 | nasai | 3689 | C23 | ~ regex | It was narrated from 'Amr bin Shu'aib, from his father, that his grandfather said: "The Messenger of Allah said: 'No one should take back his gift except a father (taking back a gift) from his son. The one who takes back his gift is like one who goes back to his vomit.'" |

---

## "aisha"

Embed: **376ms** · kNN (English-filtered, 20 results): **41ms**

### arabic-openai — Arabic matn vectors (English-only hadiths)

| # | Score | Collection | Hadith | Cluster | Matn tag | Text |
|---|---|---|---|---|---|---|
| 1 | 0.6957 | bukhari | 1713 | C2 | ✓ clean | Narrated Ziyad bin Jubair: I saw Ibn `Umar passing by a man who had made his Badana sit to slaughter it. Ibn `Umar said, "Slaughter it while it is standing with one leg tied up as is the tradition of Muhammad." |
| 2 | 0.6921 | nasai | 2966 | C16 | ~ regex | Ibn Umar said: "When the Messenger of Allah arrived in Makkah he circumambulated the House seven times, then he prayed two Rakahs behind the Maqam. Then, he went out to As-Safa through the gate that is usually used to exit, and performed Sai between As-Safa and Al-Marwah." (One of the narrators Shubah said: Ayub informed me from Amr bin Dinar from  |
| 3 | 0.6899 | bukhari | 4752 | C62 | ~ regex | Narrated Ibn Abi Mulaika: I heard `Aisha reciting: "When you invented a lie (and carry it) on your tongues." (24.15) |
| 4 | 0.6800 | muslim | 2307 c | C16 | ~ regex | This hadith has been transmitted on the authority of Anas with a slight variation of wording. |
| 5 | 0.6797 | ahmad | 37 | C16 | ~ regex | It was narrated from Muhammad bin Jubair bin Mut'im that 'Uthman said: I wish that I had asked the Messenger of Allah (ﷺ) what would save us from what the Shaitan whispers into our hearts. Abu Bakr said: I asked him about that and he said: `What can save you from that is to say what I told my uncle to say but he did not say it.` |
| 6 | 0.6797 | adab | 489 | C16 | ~ regex | Abu'd-Duha said: "Masruq and Shutayr ibn Shakal met in the mosque. The people sitting in circles in the mosque moved towards them. Masruq said, 'I can only think that these people are gathering around us in order to hear good from us. If you relate from 'Abdullah, I will confirm you. If I relate from 'Abdullah, you can confirm me.' He said, 'Abu 'A |
| 7 | 0.6784 | shamail | 209 | C7 | ~ regex | Anas ibn Malik said (may Allah be well pleased with him): "The Prophet (Allah bless him and give him peace) used to breathe into the vessel three times when he drank, and he would say: 'It is more wholesome and more thirst-quenching!’” |
| 8 | 0.6782 | muslim | 1452 c | C62 | ~ regex | Ahadith like this is transmitted by 'A'isha through another chain of narrators. |
| 9 | 0.6779 | muslim | 555 b | C16 | ~ regex | Sa'd b. Yazid Abu Mas'ama reported: I said to Anas like (that mentioned above). |
| 10 | 0.6750 | bukhari | 2628 | C62 | ✓ clean | Narrated Aiman: I went to `Aisha and she was wearing a coarse dress costing five Dirhams. `Aisha said, "Look up and see my slave-girl who refuses to wear it in the house though during the lifetime of Allah's Apostle I had a similar dress which no woman desiring to appear elegant (before her husband) failed to borrow from me." |
| 11 | 0.6721 | bukhari | 1983 | C16 | ✓ clean | Narrated Mutarrif from `Imran Ibn Husain: That the Prophet asked him (Imran) or asked a man and `Imran was listening, "O Abu so-and-so! Have you fasted the last days of this month?" (The narrator thought that he said, "the month of Ramadan"). The man replied, "No, O Allah's Apostle!" The Prophet said to him, "When you finish your fasting (of Ramada |
| 12 | 0.6709 | muslim | 2078 f | C51 | ~ regex | 'Ali b. Abu Talib reported that he (Allah'. s Apostle) forbade or forbade me. the rest of the hadith is the same. |
| 13 | 0.6708 | tirmidhi | 279 | C16 | ~ regex | Al-Bara bin Azib narrated: "The Salat of Allah's Messenger (was such that) when he bowed, and when he raised his head from bowing, and when he prostrated, and when he raised his head from prostration it (all) was nearly the same." |
| 14 | 0.6708 | tirmidhi | 1756 | C16 | ~ regex | Another chain with similar meaning. [Abu 'Eisa said:] This Hadith is Hasan Sahih. He said: There is something on this topic from Anas. |
| 15 | 0.6701 | bukhari | 1641, 1642 | C62 | ✓ clean | Narrated Muhammad bin `Abdur-Rahman bin Nawfal Al-Qurashi: I asked `Urwa bin Az-Zubair (regarding the Hajj of the Prophet ). `Urwa replied, "Aisha narrated, 'When the Prophet reached Mecca, the first thing he started with was the ablution, then he performed Tawaf of the Ka`ba and his intention was not `Umra alone (but Hajj and `Umra together).' " L |
| 16 | 0.6697 | nasai | 886 | C16 | ~ regex | It was narrated that Ibn Umar said: "While we were praying with the Messenger of Allah (SAW), a man among the people said: 'Allahu Akbaru kabira, wal-hamdu Lillahi kathira, wa subhan-Allahi bukratan was asila (Allah is Most Great and much praise be to Allah and glorified be Allah at the beginning and end of the day).' The Messenger of Allah (SAW) s |
| 17 | 0.6697 | muslim | 1146 c | C16 | ~ regex | In another version of the previous hadith, the words are:" Yahya said: I think it was due to the regard for the Apostle of Allah (may peace be upon him)." |
| 18 | 0.6696 | ibnmajah | 1702 | C16 | ~ regex | It was narrated that ‘Abdullah bin ‘Amr Al-Qari said: “I heard Abu hurairah say: ‘No, by the Lord of the Ka’bah! I did not say: “Whoever wakes up in a state of sexual impurity (and wants to fast) then he must not fast.” Muhammad (saw) said it.’” |
| 19 | 0.6696 | tirmidhi | 799 | C16 | ~ regex | Muhammad bin Ka'b narrated: "I went to Anas bin Malik during Ramadan and he was about to travel. His mount was prepared for him, and he put on his traveling clothes, then he called for some food to eat, and I said to him: 'Is it Sunnah?' He said: 'It is Sunnah.' Then he rode." |
| 20 | 0.6695 | nasai | 1456 | C16 | ~ regex | It was narrated from 'Aishah that: She performed Umrah with the Messenger of Allah (SAW), traveling from Al-Madinah to Makkah. Then, when she came to Makkah, she said: "O Messenger of Allah (SAW), may my father and mother be ransomed for you, you shortened you prayers and I offered them in full, you did not fast and I fasted. He said: 'Well done, O |