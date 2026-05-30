# Focused Comparison — Rank-by-Rank

Queries: **"aisha"** · **"comparing yourself to others"**  
Filters: chain-ref ON · dedup ON · extended pool to maintain N=10 valid results per model  

| Model | Corpus | Method | Filters |
|---|---|---|---|
| **mxbai** | English matn | Full HNSW (48,703 docs) | chain-ref + dedup |
| **english-openai** | English matn | Full HNSW (48,703 docs) | chain-ref + dedup |
| **arabic-openai** | Arabic matn | Translated centroids k=75 (44,896 docs) | englishText + dedup |

---

# Query: "aisha"

**Latency:** **Mixedbread** 1167ms · **English OpenAI** 1066ms · **Arabic OpenAI** 462ms

## Rank 1

### Mixedbread &nbsp;&nbsp; `bukhari 3894` &nbsp; score: 0.8499

Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then I got ill and my hair fell down. Later on my hair grew (again) and my mother, Um Ruman, came to me while I was playing in a swing with some of my girl friends. She called me, and I went to her, not knowing what she wanted to do to me. She caught me by the hand and made me stand at the door of the house. I was breathless then, and when my breathing became Allright, she took some water and rubbed my face and head with it. Then she took me into the house. There in the house I saw some Ansari women who said, "Best wishes and Allah's Blessing and a good luck." Then she entrusted me to them and they prepared me (for the marriage). Unexpectedly Allah's Apostle came to me in the forenoon and my mother handed me over to him, and at that time I was a girl of nine years of age.

**Arabic:** تَزَوَّجَنِي النَّبِيُّ صلى الله عليه وسلم وَأَنَا بِنْتُ سِتِّ سِنِينَ، فَقَدِمْنَا [place]الْمَدِينَةَ [/place]فَنَزَلْنَا فِي بَنِي الْحَارِثِ بْنِ خَزْرَجٍ، فَوُعِكْتُ فَتَمَرَّقَ شَعَرِي فَوَفَى جُمَيْمَةً، فَأَتَتْنِي أُمِّي أُمُّ رُومَانَ وَإِنِّي لَفِي أُرْجُوحَةٍ وَمَعِي صَوَاحِبُ لِي، فَصَرَخَتْ بِي فَأَتَيْتُهَا لاَ أَدْرِي مَا تُرِيدُ بِي فَأَخَذَتْ بِيَدِي حَتَّى أَوْقَفَتْنِي عَلَى باب الدَّارِ، وَإِنِّي لأَنْهَجُ، حَتَّى سَكَنَ بَعْضُ نَفَسِي، ثُمَّ أَخَذَتْ شَيْئًا مِنْ مَاءٍ فَمَسَحَتْ بِهِ وَجْهِي وَرَأْسِي ثُمَّ أَدْخَلَتْنِي الدَّارَ فَإِذَا نِسْوَةٌ مِنَ الأَنْصَارِ فِي الْبَيْتِ فَقُلْنَ عَلَى الْخَيْرِ وَالْبَرَكَةِ، وَعَلَى خَيْرِ طَائِرٍ‏.‏ فَأَسْلَمَتْنِي إِلَيْهِنَّ فَأَصْلَحْنَ مِنْ شَأْنِي، فَلَمْ يَرُعْنِي إِلاَّ رَسُولُ اللَّهِ صلى الله عليه وسلم ضُحًى، فَأَسْلَمَتْنِي إِلَيْهِ، وَأَنَا يَوْمَئِذٍ بِنْتُ تِسْعِ سِنِينَ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 251` &nbsp; score: 0.7851

Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I said, "(She is) So and so. She does not sleep at night because she is engaged in prayer." The Prophet said disapprovingly: Do (good) deeds which is within your capacity as Allah never gets tired of giving rewards till you get tired of doing good deeds."

**Arabic:** فَدَعَتْ بِإِنَاءٍ نَحْوًا مِنْ صَاعٍ، فَاغْتَسَلَتْ وَأَفَاضَتْ عَلَى رَأْسِهَا، وَبَيْنَنَا وَبَيْنَهَا حِجَابٌ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `bukhari 4752` &nbsp; score: 0.6892 · clusters: [27, 74]

Narrated Ibn Abi Mulaika: I heard `Aisha reciting: "When you invented a lie (and carry it) on your tongues." (24.15)

**Arabic:** عَائِشَةَ، تَقْرَأُ ‏[quran sura="24" aya_start="15" aya_end="15"]{‏إِذْ تَلِقُونَهُ بِأَلْسِنَتِكُمْ‏}[/quran]‏

---

## Rank 2

### Mixedbread &nbsp;&nbsp; `bukhari 277` &nbsp; score: 0.8473

Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head with one hand and rubbed the left side of the head with the other hand.

**Arabic:** إِذَا أَصَابَتْ إِحْدَانَا جَنَابَةٌ، أَخَذَتْ بِيَدَيْهَا ثَلاَثًا فَوْقَ رَأْسِهَا، ثُمَّ تَأْخُذُ بِيَدِهَا عَلَى شِقِّهَا الأَيْمَنِ، وَبِيَدِهَا الأُخْرَى عَلَى شِقِّهَا الأَيْسَرِ‏.‏

### English OpenAI &nbsp;&nbsp; `abudawud 2758` &nbsp; score: 0.7837

Narrated Aisha, Ummul Mu'minin: A woman would give security from the believers and it would be allowed.

**Arabic:** بُكَيْرٌ وَأَخْبَرَنِي أَنَّ أَبَا رَافِعٍ كَانَ قِبْطِيًّا ‏.‏ قَالَ أَبُو دَاوُدَ هَذَا كَانَ فِي ذَلِكَ الزَّمَانِ فَأَمَّا الْيَوْمَ فَلاَ يَصْلُحُ ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `muslim 1452 c` &nbsp; score: 0.6790 · clusters: [27, 74]

Ahadith like this is transmitted by 'A'isha through another chain of narrators.

**Arabic:** عَائِشَةَ، تَقُولُ ‏.‏ بِمِثْلِهِ ‏.‏

---

## Rank 3

### Mixedbread &nbsp;&nbsp; `abudawud 4164` &nbsp; score: 0.8454

Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing with henna. She replied: There is no harm, but I do not like it. My beloved, the Messenger of Allah (saws), disliked its odour. Abu Dawud said: She meant the colour of hair of the head.

**Arabic:** أَبُو دَاوُدَ تَعْنِي خِضَابَ شَعْرِ الرَّأْسِ ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 92` &nbsp; score: 0.7825

Narrated 'Aisha: that she prepared a lady for a man from the Ansar as his bride and the Prophet said, "O 'Aisha! Haven't you got any amusement (during the marriage ceremony) as the Ansar like amusement?"

**Arabic:** سَلُونِي عَمَّا شِئْتُمْ ‏"‏‏.‏ قَالَ رَجُلٌ مَنْ أَبِي قَالَ ‏"‏ أَبُوكَ حُذَافَةُ ‏"‏‏.‏ فَقَامَ آخَرُ فَقَالَ مَنْ أَبِي يَا رَسُولَ اللَّهِ فَقَالَ ‏"‏ أَبُوكَ سَالِمٌ مَوْلَى شَيْبَةَ ‏"‏‏.‏ فَلَمَّا رَأَى عُمَرُ مَا فِي وَجْهِهِ قَالَ يَا رَسُولَ اللَّهِ، إِنَّا نَتُوبُ إِلَى اللَّهِ عَزَّ وَجَلَّ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `bukhari 2628` &nbsp; score: 0.6754 · clusters: [27, 74]

Narrated Aiman: I went to `Aisha and she was wearing a coarse dress costing five Dirhams. `Aisha said, "Look up and see my slave-girl who refuses to wear it in the house though during the lifetime of Allah's Apostle I had a similar dress which no woman desiring to appear elegant (before her husband) failed to borrow from me."

**Arabic:** دَخَلْتُ عَلَى [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةَ[/narrator] ـ رضى الله عنها ـ وَعَلَيْهَا دِرْعُ قِطْرٍ ثَمَنُ خَمْسَةِ دَرَاهِمَ، فَقَالَتِ ارْفَعْ بَصَرَكَ إِلَى جَارِيَتِي، انْظُرْ إِلَيْهَا فَإِنَّهَا تُزْهَى أَنْ تَلْبَسَهُ فِي الْبَيْتِ، وَقَدْ كَانَ لِي مِنْهُنَّ دِرْعٌ عَلَى عَهْدِ رَسُولِ اللَّهِ صلى الله عليه وسلم، فَمَا كَانَتِ امْرَأَةٌ تُقَيَّنُ [place]بِالْمَدِينَةِ [/place]إِلاَّ أَرْسَلَتْ إِلَىَّ تَسْتَعِيرُهُ‏.‏

---

## Rank 4

### Mixedbread &nbsp;&nbsp; `bukhari 2661` &nbsp; score: 0.8442

Narrated Aisha: (the wife of the Prophet) "Whenever Allah's Apostle intended to go on a journey, he would draw lots amongst his wives and would take with him the one upon whom the lot fell. During a Ghazwa of his, he drew lots amongst us and the lot fell upon me, and I proceeded with him after Allah had decreed the use of the veil by women. I was carried in a Howdah (on the camel) and dismounted while still in it. When Allah's Apostle was through with his Ghazwa and returned home, and we approached the city of Medina, Allah's Apostle ordered us to proceed at night. When the order of setting off was given, I walked till I was past the army to answer the call of nature. After finishing I returned (to the camp) to depart (with the others) and suddenly realized that my necklace over my chest was missing. So, I returned to look for it and was delayed because of that. The people who used to carry me on the camel, came to my Howdah and put it on the back of the camel, thinking that I was in it, as, at that time, women were light in weight, and thin and lean, and did not use to eat much. So, those people did not feel the difference in the heaviness of the Howdah while lifting it, and they put it over the camel. At that time I was a young lady. They set the camel moving and proceeded on. I found my necklace after the army had gone, and came to their camp to find nobody. So, I went to the place where I used to stay, thinking that they would discover my absence and come back in my search. While in that state, I felt sleepy and slept. Safwan bin Mu'attal As-Sulami Adh-Dhakwani was behind the army and reached my abode in the morning. When he saw a sleeping person, he came to me, and he used to see me before veiling. So, I got up when I heard him saying, "Inna lil-lah-wa inn a ilaihi rajiun (We are for Allah, and we will return to Him)." He made his camel knell down. He got down from his camel, and put his leg on the front legs of the camel and then I rode and sat over it. Safwan set out walking, leading the camel by the rope till we reached the army who had halted to take rest at midday. Then whoever was meant for destruction, fell into destruction, (some people accused me falsely) and the leader of the false accusers was `Abdullah bin Ubai bin Salul. After that we returned to Medina, and I became ill for one month while the people were spreading the forged statements of the false accusers. I was feeling during my ailment as if I were not receiving the usual kindness from the Prophet which I used to receive from him when I got sick. But he would come, greet and say, 'How is that (girl)?' I did not know anything of what was going on till I recovered from my ailment and went out with Um Mistah to the Manasi where we used to answer the call of nature, and we used not to go to answer the call of nature except from night to night and that was before we had lavatories near to our houses. And this habit of ours was similar to the habit of the old 'Arabs in the open country (or away from houses). So. I and Um Mistah bint Ruhm went out walking. Um Mistah stumbled because of her long dress and on that she said, 'Let Mistah be ruined.' I said, 'You are saying a bad word. Why are you abusing a man who took part in (the battle of) Badr?' She said, 'O Hanata (you there) didn't you hear what they said?' Then she told me the rumors of the false accusers. My sickness was aggravated, and when I returned home, Allah's Apostle came to me, and after greeting he said, 'How is that (girl)?' I requested him to allow me to go to my parents. I wanted then to be sure of the news through them I Allah's Apostle allowed me, and I went to my parents and asked my mother, 'What are the people talking about?' She said, 'O my daughter! Don't worry much about this matter. By Allah, never is there a charming woman loved by her husband who has other wives, but the women would forge false news about her.' I said, 'Glorified be Allah! Are the people really taking of this matter?' That night I kept on weeping and could not sleep till morning. In the morning Allah's Apostle called `Ali bin Abu Talib and Usama bin Zaid when he saw the Divine Inspiration delayed, to consul them about divorcing his wife (i.e. `Aisha). Usama bin Zaid said what he knew of the good reputation of his wives and added, 'O Allah's Apostle! Keep you wife, for, by Allah, we know nothing about her but good.' `Ali bin Abu Talib said, 'O Allah's Apostle! Allah has no imposed restrictions on you, and there are many women other than she, yet you may ask the woman-servant who will tell you the truth.' On that Allah's Apostle called Barirah and said, 'O Barirah. Did you ever see anything which roused your suspicions about her?' Barirah said, 'No, by Allah Who has sent you with the Truth, I have never seen in her anything faulty except that she is a girl of immature age, who sometimes sleeps and leaves the dough for the goats to eat.' On that day Allah's Apostle ascended the pulpit and requested that somebody support him in punishing `Abdullah bin Ubai bin Salul. Allah's Apostle said, 'Who will support me to punish that person (`Abdullah bin Ubai bin Salul) who has hurt me by slandering the reputation of my family? By Allah, I know nothing about my family but good, and they have accused a person about whom I know nothing except good, and he never entered my house except in my company.' Sa`d bin Mu`adh got up and said, 'O Allah's Apostle! by Allah, I will relieve you from him. If that man is from the tribe of the Aus, then we will chop his head off, and if he is from our brothers, the Khazraj, then order us, and we will fulfill your order.' On that Sa`d bin 'Ubada, the chief of the Khazraj and before this incident, he had been a pious man, got up, motivated by his zeal for his tribe and said, 'By Allah, you have told a lie; you cannot kill him, and you will never be able to kill him.' On that Usaid bin Al-Hadir got up and said (to Sa`d bin 'Ubada), 'By Allah! you are a liar. By Allah, we will kill him; and you are a hypocrite, defending the hypocrites.' On this the two tribes of Aus and Khazraj got excited and were about to fight each other, while Allah's Apostle was standing on the pulpit. He got down and quieted them till they became silent and he kept quiet. On that day I kept on weeping so much so that neither did my tears stop, nor could I sleep. In the morning my parents were with me and I had wept for two nights and a day, till I thought my liver would burst from weeping. While they were sitting with me and I was weeping, an Ansari woman asked my permission to enter, and I allowed her to come in. She sat down and started weeping with me. While we were in this state, Allah's Apostle came and sat down and he had never sat with me since the day they forged the accusation. No revelation regarding my case came to him for a month. He recited Tashah-hud (i.e. None has the right to be worshipped but Allah and Muhammad is His Apostle) and then said, 'O `Aisha! I have been informed such-and-such about you; if you are innocent, then Allah will soon reveal your innocence, and if you have committed a sin, then repent to Allah and ask Him to forgive you, for when a person confesses his sin and asks Allah for forgiveness, Allah accepts his repentance.' When Allah's Apostle finished his speech my tears ceased completely and there remained not even a single drop of it. I requested my father to reply to Allah's Apostle on my behalf. My father said, By Allah, I do not know what to say to Allah's Apostle.' I said to my mother, 'Talk to Allah's Apostle on my behalf.' She said, 'By Allah, I do not know what to say to Allah's Apostle. I was a young girl and did not have much knowledge of the Qur'an. I said. 'I know, by Allah, that you have listened to what people are saying and that has been planted in your minds and you have taken it as a truth. Now, if I told you that I am innocent and Allah knows that I am innocent, you would not believe me and if I confessed to you falsely that I am guilty, and Allah knows that I am innocent you would believe me. By Allah, I don't compare my situation with you except to the situation of Joseph's father (i.e. Jacob) who said, 'So (for me) patience is most fitting against that which you assert and it is Allah (Alone) whose help can be sought.' Then I turned to the other side of my bed hoping that Allah would prove my innocence. By Allah I never thought that Allah would reveal Divine Inspiration in my case, as I considered myself too inferior to be talked of in the Holy Qur'an. I had hoped that Allah's Apostle might have a dream in which Allah would prove my innocence. By Allah, Allah's Apostle had not got up and nobody had left the house before the Divine Inspiration came to Allah's Apostle. So, there overtook him the same state which used to overtake him, (when he used to have, on being inspired divinely). He was sweating so much so that the drops of the sweat were dropping like pearls though it was a (cold) wintry day. When that state of Allah's Apostle was over, he was smiling and the first word he said, `Aisha! Thank Allah, for Allah has declared your innocence.' My mother told me to go to Allah's Apostle . I replied, 'By Allah I will not go to him and will not thank but Allah.' So Allah revealed: "Verily! They who spread the slander are a gang among you . . ." (24.11) When Allah gave the declaration of my Innocence, Abu Bakr, who used to provide for Mistah bin Uthatha for he was his relative, said, 'By Allah, I will never provide Mistah with anything because of what he said about Aisha.' But Allah later revealed: -- "And let not those who are good and wealthy among you swear not to help their kinsmen, those in need and those who left their homes in Allah's Cause. Let them forgive and overlook. Do you not wish that Allah should forgive you? Verily! Allah is Oft-forgiving, Most Merciful." (24.22) After that Abu Bakr said, 'Yes ! By Allah! I like that Allah should forgive me,' and resumed helping Mistah whom he used to help before. Allah's Apostle also asked Zainab bint Jahsh (i.e. the Prophet's wife about me saying, 'What do you know and what did you see?' She replied, 'O Allah's Apostle! I refrain to claim hearing or seeing what I have not heard or seen. By Allah, I know nothing except goodness about Aisha." Aisha further added "Zainab was competing with me (in her beauty and the Prophet's love), yet Allah protected her (from being malicious), for she had piety."

**Arabic:** إِذَا أَرَادَ أَنْ يَخْرُجَ سَفَرًا أَقْرَعَ بَيْنَ أَزْوَاجِهِ، فَأَيَّتُهُنَّ خَرَجَ سَهْمُهَا خَرَجَ بِهَا مَعَهُ، فَأَقْرَعَ بَيْنَنَا فِي غَزَاةٍ غَزَاهَا فَخَرَجَ سَهْمِي، فَخَرَجْتُ مَعَهُ بَعْدَ مَا أُنْزِلَ الْحِجَابُ، فَأَنَا أُحْمَلُ فِي هَوْدَجٍ وَأُنْزَلُ فِيهِ، فَسِرْنَا حَتَّى إِذَا فَرَغَ رَسُولُ اللَّهِ صلى الله عليه وسلم مِنْ غَزْوَتِهِ تِلْكَ، وَقَفَلَ وَدَنَوْنَا مِنَ [place]الْمَدِينَةِ، [/place]آذَنَ لَيْلَةً بِالرَّحِيلِ، فَقُمْتُ حِينَ آذَنُوا بِالرَّحِيلِ، فَمَشَيْتُ حَتَّى جَاوَزْتُ الْجَيْشَ، فَلَمَّا قَضَيْتُ شَأْنِي أَقْبَلْتُ إِلَى الرَّحْلِ، فَلَمَسْتُ صَدْرِي، فَإِذَا عِقْدٌ لِي مِنْ جَزْعِ أَظْفَارٍ قَدِ انْقَطَعَ، فَرَجَعْتُ فَالْتَمَسْتُ عِقْدِي، فَحَبَسَنِي ابْتِغَاؤُهُ، فَأَقْبَلَ الَّذِينَ يَرْحَلُونَ لِي، فَاحْتَمَلُوا هَوْدَجِي فَرَحَلُوهُ عَلَى بَعِيرِي الَّذِي كُنْتُ أَرْكَبُ، وَهُمْ يَحْسِبُونَ أَنِّي فِيهِ، وَكَانَ النِّسَاءُ إِذْ ذَاكَ خِفَافًا لَمْ يَثْقُلْنَ وَلَمْ يَغْشَهُنَّ اللَّحْمُ، وَإِنَّمَا يَأْكُلْنَ الْعُلْقَةَ مِنَ الطَّعَامِ، فَلَمْ يَسْتَنْكِرِ الْقَوْمُ حِينَ رَفَعُوهُ ثِقَلَ الْهَوْدَجِ فَاحْتَمَلُوهُ وَكُنْتُ جَارِيَةً حَدِيثَةَ السِّنِّ، فَبَعَثُوا الْجَمَلَ وَسَارُوا، فَوَجَدْتُ عِقْدِي بَعْدَ مَا اسْتَمَرَّ الْجَيْشُ، فَجِئْتُ مَنْزِلَهُمْ وَلَيْسَ فِيهِ أَحَدٌ، فَأَمَمْتُ مَنْزِلِي الَّذِي كُنْتُ بِهِ فَظَنَنْتُ أَنَّهُمْ سَيَفْقِدُونِي فَيَرْجِعُونَ إِلَىَّ، فَبَيْنَا أَنَا جَالِسَةٌ غَلَبَتْنِي عَيْنَاىَ فَنِمْتُ، وَكَانَ صَفْوَانُ بْنُ الْمُعَطَّلِ السُّلَمِيُّ ثُمَّ الذَّكْوَانِيُّ مِنْ وَرَاءِ الْجَيْشِ، فَأَصْبَحَ عِنْدَ مَنْزِلِي فَرَأَى سَوَادَ إِنْسَانٍ نَائِمٍ فَأَتَانِي، وَكَانَ يَرَانِي قَبْلَ الْحِجَابِ فَاسْتَيْقَظْتُ بِاسْتِرْجَاعِهِ حِينَ أَنَاخَ رَاحِلَتَهُ، فَوَطِئَ يَدَهَا فَرَكِبْتُهَا فَانْطَلَقَ يَقُودُ بِي الرَّاحِلَةَ، حَتَّى أَتَيْنَا الْجَيْشَ بَعْدَ مَا نَزَلُوا مُعَرِّسِينَ فِي نَحْرِ الظَّهِيرَةِ، فَهَلَكَ مَنْ هَلَكَ، وَكَانَ الَّذِي تَوَلَّى الإِفْكَ عَبْدُ اللَّهِ بْنُ أُبَىٍّ ابْنُ سَلُولَ، فَقَدِمْنَا [place]الْمَدِينَةَ [/place]فَاشْتَكَيْتُ بِهَا شَهْرًا، يُفِيضُونَ مِنْ قَوْلِ أَصْحَابِ الإِفْكِ، وَيَرِيبُنِي فِي وَجَعِي أَنِّي لاَ أَرَى مِنَ النَّبِيِّ صلى الله عليه وسلم اللُّطْفَ الَّذِي كُنْتُ أَرَى مِنْهُ حِينَ أَمْرَضُ، إِنَّمَا يَدْخُلُ فَيُسَلِّمُ ثُمَّ يَقُولُ ‏"‏ كَيْفَ تِيكُمْ ‏"‏‏.‏ لاَ أَشْعُرُ بِشَىْءٍ مِنْ ذَلِكَ حَتَّى نَقَهْتُ، فَخَرَجْتُ أَنَا وَأُمُّ مِسْطَحٍ قِبَلَ الْمَنَاصِعِ مُتَبَرَّزُنَا، لاَ نَخْرُجُ إِلاَّ لَيْلاً إِلَى لَيْلٍ، وَذَلِكَ قَبْلَ أَنْ نَتَّخِذَ الْكُنُفَ قَرِيبًا مِنْ بُيُوتِنَا، وَأَمْرُنَا أَمْرُ الْعَرَبِ الأُوَلِ فِي الْبَرِّيَّةِ أَوْ فِي التَّنَزُّهِ، فَأَقْبَلْتُ أَنَا وَأُمُّ مِسْطَحٍ بِنْتُ أَبِي رُهْمٍ نَمْشِي، فَعَثُرَتْ فِي مِرْطِهَا فَقَالَتْ تَعِسَ مِسْطَحٌ، فَقُلْتُ لَهَا بِئْسَ مَا قُلْتِ، أَتَسُبِّينَ رَجُلاً شَهِدَ بَدْرًا فَقَالَتْ يَا هَنْتَاهْ أَلَمْ تَسْمَعِي مَا قَالُوا فَأَخْبَرَتْنِي بِقَوْلِ أَهْلِ الإِفْكِ، فَازْدَدْتُ مَرَضًا إِلَى مَرَضِي، فَلَمَّا رَجَعْتُ إِلَى بَيْتِي دَخَلَ عَلَىَّ رَسُولُ اللَّهِ صلى الله عليه وسلم فَسَلَّمَ فَقَالَ ‏"‏ كَيْفَ تِيكُمْ ‏"‏‏.‏ فَقُلْتُ ائْذَنْ لِي إِلَى أَبَوَىَّ‏.‏ قَالَتْ وَأَنَا حِينَئِذٍ أُرِيدُ أَنْ أَسْتَيْقِنَ الْخَبَرَ مِنْ قِبَلِهِمَا، فَأَذِنَ لِي رَسُولُ اللَّهِ صلى الله عليه وسلم فَأَتَيْتُ أَبَوَىَّ فَقُلْتُ لأُمِّي مَا يَتَحَدَّثُ بِهِ النَّاسُ فَقَالَتْ يَا بُنَيَّةُ هَوِّنِي عَلَى نَفْسِكِ الشَّأْنَ، فَوَاللَّهِ لَقَلَّمَا كَانَتِ امْرَأَةٌ قَطُّ وَضِيئَةٌ عِنْدَ رَجُلٍ يُحِبُّهَا وَلَهَا ضَرَائِرُ إِلاَّ أَكْثَرْنَ عَلَيْهَا‏.‏ فَقُلْتُ سُبْحَانَ اللَّهِ وَلَقَدْ يَتَحَدَّثُ النَّاسُ بِهَذَا قَالَتْ فَبِتُّ تِلْكَ اللَّيْلَةَ حَتَّى أَصْبَحْتُ لاَ يَرْقَأُ لِي دَمْعٌ وَلاَ أَكْتَحِلُ بِنَوْمٍ، ثُمَّ أَصْبَحْتُ فَدَعَا رَسُولُ اللَّهِ صلى الله عليه وسلم عَلِيَّ بْنَ أَبِي طَالِبٍ وَأُسَامَةَ بْنَ زَيْدٍ حِينَ اسْتَلْبَثَ الْوَحْىُ، يَسْتَشِيرُهُمَا فِي فِرَاقِ أَهْلِهِ، فَأَمَّا أُسَامَةُ فَأَشَارَ عَلَيْهِ بِالَّذِي يَعْلَمُ فِي نَفْسِهِ مِنَ الْوُدِّ لَهُمْ، فَقَالَ أُسَامَةُ أَهْلُكَ يَا رَسُولَ اللَّهِ وَلاَ نَعْلَمُ وَاللَّهِ إِلاَّ خَيْرًا، وَأَمَّا عَلِيُّ بْنُ أَبِي طَالِبٍ فَقَالَ يَا رَسُولَ اللَّهِ لَمْ يُضَيِّقِ اللَّهُ عَلَيْكَ وَالنِّسَاءُ سِوَاهَا كَثِيرٌ، وَسَلِ الْجَارِيَةَ تَصْدُقْكَ‏.‏ فَدَعَا رَسُولُ اللَّهِ صلى الله عليه وسلم بَرِيرَةَ فَقَالَ ‏"‏ يَا بَرِيرَةُ هَلْ رَأَيْتِ فِيهَا شَيْئًا يَرِيبُكِ ‏"‏‏.‏ فَقَالَتْ بَرِيرَةُ لاَ وَالَّذِي بَعَثَكَ بِالْحَقِّ، إِنْ رَأَيْتُ مِنْهَا أَمْرًا أَغْمِصُهُ عَلَيْهَا أَكْثَرَ مِنْ أَنَّهَا جَارِيَةٌ حَدِيثَةُ السِّنِّ تَنَامُ عَنِ الْعَجِينَ فَتَأْتِي الدَّاجِنُ فَتَأْكُلُهُ‏.‏ فَقَامَ رَسُولُ اللَّهِ صلى الله عليه وسلم مِنْ يَوْمِهِ، فَاسْتَعْذَرَ مِنْ عَبْدِ اللَّهِ بْنِ أُبَىٍّ ابْنِ سَلُولَ فَقَالَ رَسُولُ اللَّهِ صلى الله عليه وسلم ‏"‏ مَنْ يَعْذِرُنِي مِنْ رَجُلٍ بَلَغَنِي أَذَاهُ فِي أَهْلِي، فَوَاللَّهِ مَا عَلِمْتُ عَلَى أَهْلِي إِلاَّ خَيْرًا، وَقَدْ ذَكَرُوا رَجُلاً مَا عَلِمْتُ عَلَيْهِ إِلاَّ خَيْرًا، وَمَا كَانَ يَدْخُلُ عَلَى أَهْلِي إِلاَّ مَعِي ‏"‏‏.‏ فَقَامَ سَعْدُ بْنُ مُعَاذٍ فَقَالَ يَا رَسُولَ اللَّهِ أَنَا وَاللَّهِ أَعْذِرُكَ مِنْهُ، إِنْ كَانَ مِنَ الأَوْسِ ضَرَبْنَا عُنُقَهُ، وَإِنْ كَانَ مِنْ إِ

### English OpenAI &nbsp;&nbsp; `bukhari 748` &nbsp; score: 0.7822

Narrated Aisha: The people used to look forward for the days of my (`Aisha's) turn to send gifts to Allah's Apostle in order to please him.

**Arabic:** إِنِّي أُرِيتُ الْجَنَّةَ، فَتَنَاوَلْتُ مِنْهَا عُنْقُودًا، وَلَوْ أَخَذْتُهُ لأَكَلْتُمْ مِنْهُ مَا بَقِيَتِ الدُّنْيَا ‏"

### Arabic OpenAI &nbsp;&nbsp; `bukhari 1641, 1642` &nbsp; score: 0.6709 · clusters: [27, 74]

Narrated Muhammad bin `Abdur-Rahman bin Nawfal Al-Qurashi: I asked `Urwa bin Az-Zubair (regarding the Hajj of the Prophet ). `Urwa replied, "Aisha narrated, 'When the Prophet reached Mecca, the first thing he started with was the ablution, then he performed Tawaf of the Ka`ba and his intention was not `Umra alone (but Hajj and `Umra together).' " Later Abu Bakr I performed the Hajj and the first thing he started with was Tawaf of the Ka`ba and it was not `Umra alone (but Hajj and `Umra together). And then `Umar did the same. Then `Uthman performed the Hajj and the first thing he started with was Tawaf of the Ka`ba and it was not `Umra alone. And then Muawiya and `Abdullah bin `Umar did the same. I performed Hajj with Ibn Az-Zubair and the first thing he started with was Tawaf of the Ka`ba and it was not `Umra alone, (but Hajj and `Umra together). Then I saw the Muhajirin (Emigrants) and Ansar doing the same and it was not `Umra alone. And the last person I saw doing the same was Ibn `Umar, and he did not do another `Umra after finishing the first. Now here is Ibn `Umar present amongst the people! They neither ask him nor anyone of the previous ones. And all these people, on entering Mecca, would not start with anything unless they had performed Tawaf of the Ka`ba, and would not finish their Ihram. And no doubt, I saw my mother and my aunt, on entering Mecca doing nothing before performing Tawaf of the Ka`ba, and they would not finish their lhram. And my mother informed me that she, her sister, Az-Zubair and such and such persons had assumed lhram for `Umra and after passing their hands over the Corner (the Black Stone) (i.e. finishing their Umra) they finished their Ihram."

**Arabic:** حَجَّ النَّبِيُّ صلى الله عليه وسلم فَأَخْبَرَتْنِي [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةُ[/narrator] ـ رضى الله عنها ـ أَنَّهُ أَوَّلُ شَىْءٍ بَدَأَ بِهِ حِينَ قَدِمَ أَنَّهُ تَوَضَّأَ ثُمَّ طَافَ [place]بِالْبَيْتِ[/place] ثُمَّ لَمْ تَكُنْ عُمْرَةً

---

## Rank 5

### Mixedbread &nbsp;&nbsp; `bukhari 1151` &nbsp; score: 0.8425

Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I said, "(She is) So and so. She does not sleep at night because she is engaged in prayer." The Prophet said disapprovingly: Do (good) deeds which is within your capacity as Allah never gets tired of giving rewards till you get tired of doing good deeds."

**Arabic:** مَهْ عَلَيْكُمْ مَا تُطِيقُونَ مِنَ الأَعْمَالِ، فَإِنَّ اللَّهَ لاَ يَمَلُّ حَتَّى تَمَلُّوا ‏"

### English OpenAI &nbsp;&nbsp; `bukhari 24` &nbsp; score: 0.7780 · dup-rep: 13370

Narrated `Aisha: (the wife of the Prophet) A lady along with her two daughters came to me asking me (for some alms), but she found nothing with me except one date which I gave to her and she divided it between her two daughters, and then she got up and went away. Then the Prophet came in and I informed him about this story. He said, "Whoever is in charge of (put to test by) these daughters and treats them generously, then they will act as a shield for him from the (Hell) Fire."

**Arabic:** فَإِنَّ الْحَيَاءَ مِنَ الإِيمَانِ ‏"

### Arabic OpenAI &nbsp;&nbsp; `muslim 738 e` &nbsp; score: 0.6687 · clusters: [27, 74]

It is reported on the authority of 'A'isha that the prayer of Allah's Messenger (may peace be upon him) in the night consisted of ten rak'ahs. He observed a Witr and two rak'ahs (of Sunan) of the dawn prayer, and thus the total comes to thirteen rak'ahs.

**Arabic:** عَائِشَةَ، تَقُولُ كَانَتْ صَلاَةُ رَسُولِ اللَّهِ صلى الله عليه وسلم مِنَ اللَّيْلِ عَشَرَ رَكَعَاتٍ وَيُوتِرُ بِسَجْدَةٍ وَيَرْكَعُ رَكْعَتَىِ الْفَجْرِ فَتِلْكَ ثَلاَثَ عَشْرَةَ رَكْعَةً ‏.‏

---

## Rank 6

### Mixedbread &nbsp;&nbsp; `bukhari 902` &nbsp; score: 0.8425

Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of four miles or more from Medina). They used to pass through dust and used to be drenched with sweat and covered with dust; so sweat used to trickle from them. One of them came to Allah's Apostle who was in my house. The Prophet said to him, "I wish that you keep yourself clean on this day of yours (i.e. take a bath)."

**Arabic:** لَوْ أَنَّكُمْ تَطَهَّرْتُمْ لِيَوْمِكُمْ هَذَا ‏"

### English OpenAI &nbsp;&nbsp; `mishkat 3150` &nbsp; score: 0.7778

‘A’isha said: I had a girl of the Ansar whom I gave in marriage, and God's Messenger said, "Why do you not sing, ‘A’isha, for this clan of the Ansar like singing?” Ibn Hibban transmitted it in his Sahih .

**Arabic:** وَعَنْ أَبِي هُرَيْرَةَ قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «كُلُّ خُطْبَةٍ لَيْسَ فِيهَا تَشَهُّدٌ فَهِيَ كَالْيَدِ الْجَذْمَاءِ» . رَوَاهُ التِّرْمِذِيُّ وَقَالَ: هَذَا حَدِيثٌ حَسَنٌ غَرِيبٌ

### Arabic OpenAI &nbsp;&nbsp; `bukhari 4872` &nbsp; score: 0.6679 · clusters: [27, 74]

Narrated `Abdullah bin Masud: The Prophet used to recite: "Fahal-min-Maddakir (then is there any that will receive admonition?")

**Arabic:** ‏[quran sura="54" aya_start="15" aya_end="15"]{‏فَهَلْ مِنْ مُدَّكِرٍ‏}[/quran]‏ الآيَةَ‏.‏

---

## Rank 7

### Mixedbread &nbsp;&nbsp; `bukhari 4573` &nbsp; score: 0.8423

Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of that and not because he loved her. So the Divine Verse came regarding his case: "If you fear that you shall not be able to deal justly with the orphan girls..." (4.3) The sub-narrator added: I think he (i.e. another sub-narrator) said, "That orphan girl was his partner in that datepalm (garden) and in his property."

**Arabic:** أَنَّ رَجُلاً، كَانَتْ لَهُ يَتِيمَةٌ فَنَكَحَهَا، وَكَانَ لَهَا عَذْقٌ، وَكَانَ يُمْسِكُهَا عَلَيْهِ، وَلَمْ يَكُنْ لَهَا مِنْ نَفْسِهِ شَىْءٌ فَنَزَلَتْ فِيهِ ‏{‏وَإِنْ خِفْتُمْ أَنْ لاَ تُقْسِطُوا فِي الْيَتَامَى‏}‏ أَحْسِبُهُ قَالَ كَانَتْ شَرِيكَتَهُ فِي ذَلِكَ الْعَذْقِ وَفِي مَالِهِ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 815` &nbsp; score: 0.7775

Narrated Aisha: Once the Prophet came to me while a man was in my house. He said, "O `Aisha! Who is this (man)?" I replied, "My foster brothers" He said, "O `Aisha! Be sure about your foster brothers, as fostership is only valid if it takes place in the suckling period (before two years of age).

**Arabic:** يَسْجُدَ عَلَى سَبْعَةِ أَعْظُمٍ، وَلاَ يَكُفَّ ثَوْبَهُ وَلاَ شَعَرَهُ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `abudawud 1341` &nbsp; score: 0.6675 · clusters: [27, 74]

Abu Salamah b. 'Abd al-Rahman asked 'Aishah, the wife of the Prophet (saws): How did the Messenger of Allah (saws) pray during Ramadhan ? She said: The Messenger of Allah (saws) did not pray more than eleven rak'ahs during Ramadhan and other than Ramadhan. He would pray four rak'ahs. Do not ask about their elegance and length. He then would pray for rak'ahs. Do not ask about their alegance and length. Then he would pray three rak'ahs. 'Aishah said: I asked: Messenger of Allah, do you sleep before observing witr ? He replied: 'Aishah, my eyes sleep, but my heart does not sleep.

**Arabic:** ‏:‏ ‏"‏ يَا عَائِشَةُ إِنَّ عَيْنَىَّ تَنَامَانِ وَلاَ يَنَامُ قَلْبِي ‏"‏ ‏.‏

---

## Rank 8

### Mixedbread &nbsp;&nbsp; `bukhari 43` &nbsp; score: 0.8411

Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her (excessive) praying. He said disapprovingly, "Do (good) deeds which is within your capacity (without being overtaxed) as Allah does not get tired (of giving rewards) but (surely) you will get tired and the best deed (act of Worship) in the sight of Allah is that which is done regularly."

**Arabic:** مَهْ، عَلَيْكُمْ بِمَا تُطِيقُونَ، فَوَاللَّهِ لاَ يَمَلُّ اللَّهُ حَتَّى تَمَلُّوا ‏"‏‏.‏ وَكَانَ أَحَبَّ الدِّينِ إِلَيْهِ مَا دَامَ عَلَيْهِ صَاحِبُهُ‏.‏

### English OpenAI &nbsp;&nbsp; `adab 613` &nbsp; score: 0.7751

'Ikrima heard 'A'isha, may Allah be pleased with her, say that she saw the Prophet, may Allah bless him and grant him peace, raise his hands in supplication, saying, 'O Allah, I am only a man, so do not punish me. If I harm or revile a Muslim man, do not punish me for it!'"

**Arabic:** ‏:‏ اللَّهُمَّ إِنَّمَا أَنَا بَشَرٌ فَلاَ تُعَاقِبْنِي، أَيُّمَا رَجُلٌ مِنَ الْمُؤْمِنِينَ آذَيْتُهُ أَوْ شَتَمْتُهُ فَلا تُعَاقِبْنِي فِيهِ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `tirmidhi 588` &nbsp; score: 0.6652 · clusters: [27, 74]

Sa'eed bin Abi Hind narrated from some of the companions of Ikrimah: "The Prophet would glance during Salat" and he mentioned a similar narration.

**Arabic:** وَفِي الْبَابِ عَنْ أَنَسٍ وَعَائِشَةَ ‏.‏

---

## Rank 9

### Mixedbread &nbsp;&nbsp; `abudawud 3708` &nbsp; score: 0.8386

Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays, and asked her about mixing dried dates and raisins (for drink). She replied: I used to take a handful of dried dates and a handful or raisins and put them in a vessel, and then crush them (and soak in water). Then I would give it to the Prophet (saws) to drink.

**Arabic:** تْ كُنْتُ آخُذُ قَبْضَةً مِنْ تَمْرٍ وَقَبْضَةً مِنْ زَبِيبٍ فَأُلْقِيهِ فِي إِنَاءٍ فَأَمْرُسُهُ ثُمَّ أَسْقِيهِ النَّبِيَّ صلى الله عليه وسلم ‏.‏

### English OpenAI &nbsp;&nbsp; `mishkat 3224` &nbsp; score: 0.7723

‘A’isha told that when Sauda became old she said, “Messenger of God, I appoint to ‘A'isha the day you visit me” (Cf. the last tradition in this chapter). So God’s Messenger allotted two days to ‘A’isha, hers and Sauda’s. (Bukhari and Muslim.)

**Arabic:** قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «طَعَامُ أَوَّلِ يَوْمٍ حق وَطَعَام يَوْم الثَّانِي سنة وَطَعَام يَوْم الثَّالِثِ سُمْعَةٌ وَمَنْ سَمَّعَ سَمَّعَ اللَّهُ بِهِ» . رَوَاهُ التِّرْمِذِيّ

### Arabic OpenAI &nbsp;&nbsp; `tirmidhi 1839` &nbsp; score: 0.6651 · clusters: [27, 74]

Narrated Jabir: That the Prophet (saws) said: "What an excellent condiment vinegar is."

**Arabic:** ‏"‏ نِعْمَ الإِدَامُ الْخَلُّ ‏"‏ ‏.‏ قَالَ وَفِي الْبَابِ عَنْ عَائِشَةَ وَأُمِّ هَانِئٍ ‏.‏

---

## Rank 10

### Mixedbread &nbsp;&nbsp; `abudawud 288` &nbsp; score: 0.8383

'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, had a flow of blood for seven years. She asked the Messenger of Allah (saws) about it. The Messenger of Allah (saws) said: This is not menstruation but only vein; so you should take a bath and pray. 'Aishah said: She used to take bath in a wash-tub in the apartment of her sister Zainab daughter of Jahsh ; the redness of (her) blood dominated the water.

**Arabic:** رَسُولُ اللَّهِ صلى الله عليه وسلم ‏"‏ إِنَّ هَذِهِ لَيْسَتْ بِالْحَيْضَةِ وَلَكِنْ هَذَا عِرْقٌ فَاغْتَسِلِي وَصَلِّي ‏"‏ ‏.‏ قَالَتْ عَائِشَةُ فَكَانَتْ تَغْتَسِلُ فِي مِرْكَنٍ فِي حُجْرَةِ أُخْتِهَا زَيْنَبَ بِنْتِ جَحْشٍ حَتَّى تَعْلُوَ حُمْرَةُ الدَّمِ الْمَاءَ ‏.‏

### English OpenAI &nbsp;&nbsp; `abudawud 4880` &nbsp; score: 0.7702

Narrated Aisha, Ummul Mu'minin: Ibn Awn said: I asked about the meaning of intisar (revenge) in the Qur'anic verse: "But indeed if any do help and defend themselves (intasara) after a wrong (done) to them, against them there is no cause of blame." Then Ali ibn Zayd ibn Jad'an told me on the authority of Umm Muhammad, the wife of his father. Ibn Awn said: It was believed that she used to go to the Mother of the Faithful (i.e. Aisha). She said: The Mother of the Faithful said: The Messenger of Allah (saws) came upon me while Zaynab, daughter of Jahsh, was with us. He began to do something with his hand. I signalled to him until I made him understand about her. So he stopped. Zaynab came on and began to abuse Aisha. She tried to prevent her but she did not stop. So he (the Prophet) said to Aisha: Abuse her. So she abused her and dominated her. Zaynab then went to Ali and said: Aisha abused you and did (such and such). Then Fatimah came (to the Prophet) and he said to her: She is the favourite of your father, by the Lord of the Ka'bah! She then returned and said to them: I said to him such and such, and he said to me such and such. Then Ali came to the Prophet (saws) and spoke to him about that.

**Arabic:** صلى الله عليه وسلم ‏"‏ يَا مَعْشَرَ مَنْ آمَنَ بِلِسَانِهِ وَلَمْ يَدْخُلِ الإِيمَانُ قَلْبَهُ لاَ تَغْتَابُوا الْمُسْلِمِينَ وَلاَ تَتَّبِعُوا عَوْرَاتِهِمْ فَإِنَّهُ مَنِ اتَّبَعَ عَوْرَاتِهِمْ يَتَّبِعِ اللَّهُ عَوْرَتَهُ وَمَنْ يَتَّبِعِ اللَّهُ عَوْرَتَهُ يَفْضَحْهُ فِي بَيْتِهِ ‏"‏ ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `muslim 1479 d` &nbsp; score: 0.6647 · clusters: [27, 74]

Ibn Abbas (Allah be pleased with them) is reported to have said: I intended to ask Umar about those two ladies who had pressed for (worldly riches) during the lifetime of the Holy Prophet (may peace be upon him), and I kept waiting for one year, but found no suitable opportunity with him until I happened to accompany him to Mecca. And as he reached Marr al Zahran he went away to answer the call of nature, and he said (to me): Bring me a jug of water, and I took that to him. After having answered the call of nature, as he came back, I began to pour water (over his hands and feet), and I remembered (this event of separation of Allah's Apostle [may peace be upon him] from his wives). So I said to him: Commander of the Faithful, who are the two ladies (who had pressed the Holy Prophet [may peace be upon him] for providing comforts of life) and I had not yet finished my talk when he said: They were 'A'isha and Hafsa.

**Arabic:** عَائِشَةُ وَحَفْصَةُ ‏.‏

---


# Query: "comparing yourself to others"

**Latency:** **Mixedbread** 127ms · **English OpenAI** 251ms · **Arabic OpenAI** 455ms

## Rank 1

### Mixedbread &nbsp;&nbsp; `forty 18` &nbsp; score: 0.8147

The felicitous person takes lessons from (the actions of) others.

**Arabic:** عَنْ أَبِي ذَرٍّ جُنْدَبِ بْنِ جُنَادَةَ، وَأَبِي عَبْدِ الرَّحْمَنِ مُعَاذِ بْنِ جَبَلٍ رَضِيَ اللَّهُ عَنْهُمَا، عَنْ رَسُولِ اللَّهِ صلى الله عليه و سلم قَالَ: "اتَّقِ اللَّهَ حَيْثُمَا كُنْت، وَأَتْبِعْ السَّيِّئَةَ الْحَسَنَةَ تَمْحُهَا، وَخَالِقْ النَّاسَ بِخُلُقٍ حَسَنٍ" . رَوَاهُ التِّرْمِذِيُّ [رقم:1987] وَقَالَ: حَدِيثٌ حَسَنٌ، وَفِي بَعْضِ النُّسَخِ: حَسَنٌ صَحِيحٌ.

### English OpenAI &nbsp;&nbsp; `adab 328` &nbsp; score: 0.6876

Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faults."

**Arabic:** ‏:‏ إِذَا أَرَدْتَ أَنْ تَذْكُرَ عُيُوبَ صَاحِبِكَ، فَاذْكُرْ عُيُوبَ نَفْسِكَ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `ibnmajah 1977` &nbsp; score: 0.6552 · clusters: [70, 64]

It was narrated from Ibn 'Abbas that: the Prophet said: "The best of you is the one who is best to his wife, and I am the best of you to my wives."

**Arabic:** ‏"‏ خَيْرُكُمْ خَيْرُكُمْ لأَهْلِهِ وَأَنَا خَيْرُكُمْ لأَهْلِي ‏"‏ ‏.‏

---

## Rank 2

### Mixedbread &nbsp;&nbsp; `bukhari 6490` &nbsp; score: 0.8022

Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him.

**Arabic:** إِذَا نَظَرَ أَحَدُكُمْ إِلَى مَنْ فُضِّلَ عَلَيْهِ فِي الْمَالِ وَالْخَلْقِ، فَلْيَنْظُرْ إِلَى مَنْ هُوَ أَسْفَلَ مِنْهُ ‏"

### English OpenAI &nbsp;&nbsp; `riyadussalihin 466` &nbsp; score: 0.6874

Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you." This is the wording in Sahih Muslim. [Al-Bukhari and Muslim] . The narration in Al-Bukhari is: Messenger of Allah (PBUH) said: "When one of you looks at someone who is superior to him in property and appearance, he should look at someone who is inferior to him".

**Arabic:** - وعنه قال‏:‏ قال رسول الله صلى الله عليه وسلم انظروا إلى من هو أسفل منكم ولا تنظروا إلى من هو فوقكم فهو أجدر أن لا تزدروا نعمة الله عليكم‏"‏ ‏(‏‏(‏متفق عليه وهذا لفظ مسلم‏)‏‏)‏‏.‏ وفي رواية البخاري‏:‏ ‏"‏إذا نظر أحدكم إلى من فضل عليه في المال والخلق، فلينظر إلى من هو أسفل منه‏"‏‏.‏ وفي رواية البخاري‏:‏ ‏"‏إذا نظر أحدكم إلى من فضل عليه في المال والخلق، فلينظر إلى من هو أسفل منه‏"‏‏.‏

### Arabic OpenAI &nbsp;&nbsp; `abudawud 879` &nbsp; score: 0.6474 · clusters: [70, 64]

‘A’ishah said; one night I missed the Messenger of Allah (may peace be upon him) and when I sought him on the spot of prayer I found him in prostration with his feet raised, and he was saying:”(O Allah), I seek refuge in Your good pleasure from Your anger, and in Your Mercy from Your Punishment, and I seek refuge from You in You; I am not able to praise You (the way that You deserve to be praised), for You are as You have praised Yourself”.

**Arabic:** ‏"‏ أَعُوذُ بِرِضَاكَ مِنْ سَخَطِكَ وَأَعُوذُ بِمُعَافَاتِكَ مِنْ عُقُوبَتِكَ وَأَعُوذُ بِكَ مِنْكَ لاَ أُحْصِي ثَنَاءً عَلَيْكَ أَنْتَ كَمَا أَثْنَيْتَ عَلَى نَفْسِكَ ‏"‏ ‏.‏

---

## Rank 3

### Mixedbread &nbsp;&nbsp; `muslim 2963 a` &nbsp; score: 0.7931

Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you in regard to these things (in which he stands) at a higher level (as compared to him).

**Arabic:** ‏"‏ إِذَا نَظَرَ أَحَدُكُمْ إِلَى مَنْ فُضِّلَ عَلَيْهِ فِي الْمَالِ وَالْخَلْقِ فَلْيَنْظُرْ إِلَى مَنْ هُوَ أَسْفَلَ مِنْهُ مِمَّنْ فُضِّلَ عَلَيْهِ ‏"‏ ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 497` &nbsp; score: 0.6779

Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him.

**Arabic:** كَانَ جِدَارُ الْمَسْجِدِ عِنْدَ الْمِنْبَرِ مَا كَادَتِ الشَّاةُ تَجُوزُهَا‏.‏

### Arabic OpenAI &nbsp;&nbsp; `nasai 169` &nbsp; score: 0.6472 · clusters: [70, 64]

It was narrated from Abu Hurairah that 'Aishah said: "I noticed the Prophet (PBUH) was not there one night, so I started looking for him with my hand. My hand touched his feet and they were held upright, and he was prostrating and saying: 'I seek refuge in Your pleasure from Your anger, in Your forgiveness from Your punishment, and I seek refuge in You from You. I cannot praise You enough, You are as You have praised yourself.'"

**Arabic:** ‏"‏ أَعُوذُ بِرِضَاكَ مِنْ سَخَطِكَ وَبِمُعَافَاتِكَ مِنْ عُقُوبَتِكَ وَأَعُوذُ بِكَ مِنْكَ لاَ أُحْصِي ثَنَاءً عَلَيْكَ أَنْتَ كَمَا أَثْنَيْتَ عَلَى نَفْسِكَ ‏"‏ ‏.‏

---

## Rank 4

### Mixedbread &nbsp;&nbsp; `adab 159` &nbsp; score: 0.7907

Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. The best of you is the one whose good is hoped for and the one whose evil you are safe from. As for the worst of you, that is the person whose good is not hoped for and whose evil you are not safe from and he does not free slaves."

**Arabic:** لِلنَّاسِ‏:‏ نَحْنُ أَعْرَفُ بِكُمْ مِنَ الْبَيَاطِرَةِ بِالدَّوَابِّ، قَدْ عَرَفْنَا خِيَارَكُمْ مِنْ شِرَارِكُمْ‏.‏ أَمَّا خِيَارُكُمُ‏:‏ الَّذِي يُرْجَى خَيْرُهُ، وَيُؤْمَنُ شَرُّهُ‏.‏ وَأَمَّا شِرَارُكُمْ‏:‏ فَالَّذِي لاَ يُرْجَى خَيْرُهُ، وَلاَ يُؤْمَنُ شَرُّهُ، وَلاَ يُعْتَقُ مُحَرَّرُهُ‏.‏

### English OpenAI &nbsp;&nbsp; `muslim 7068` &nbsp; score: 0.6656

Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you in regard to these things (in which he stands) at a higher level (as compared to him).

### Arabic OpenAI &nbsp;&nbsp; `nasai 1130` &nbsp; score: 0.6450 · clusters: [70, 64]

It was narrated that 'Aishah said: "I noticed the Messenger of Allah (SAW) was missing one night and I found him prostrating with the tops of his feet facing toward the Qiblah. I heard him saying: 'A'udhu biridaka min sakhatika, wa a'udhu bimu 'afatika min 'uqubatika wa a'udhu bika minka la uhsi thana'an 'alaika anta kama athnaita 'ala nafsik (I seek refuge in Your pleasure from Your wrath; I seek refuge in Your forgiveness from Your punishment; I seek refuge in You from You. I cannot praise You enough, You are as You have praised Yourself.)"

**Arabic:** ‏"‏ أَعُوذُ بِرِضَاكَ مِنْ سَخَطِكَ وَأَعُوذُ بِمُعَافَاتِكَ مِنْ عُقُوبَتِكَ وَأَعُوذُ بِكَ مِنْكَ لاَ أُحْصِي ثَنَاءً عَلَيْكَ أَنْتَ كَمَا أَثْنَيْتَ عَلَى نَفْسِكَ ‏"‏ ‏.‏

---

## Rank 5

### Mixedbread &nbsp;&nbsp; `riyadussalihin 466` &nbsp; score: 0.7867

Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you." This is the wording in Sahih Muslim. [Al-Bukhari and Muslim] . The narration in Al-Bukhari is: Messenger of Allah (PBUH) said: "When one of you looks at someone who is superior to him in property and appearance, he should look at someone who is inferior to him".

**Arabic:** - وعنه قال‏:‏ قال رسول الله صلى الله عليه وسلم انظروا إلى من هو أسفل منكم ولا تنظروا إلى من هو فوقكم فهو أجدر أن لا تزدروا نعمة الله عليكم‏"‏ ‏(‏‏(‏متفق عليه وهذا لفظ مسلم‏)‏‏)‏‏.‏ وفي رواية البخاري‏:‏ ‏"‏إذا نظر أحدكم إلى من فضل عليه في المال والخلق، فلينظر إلى من هو أسفل منه‏"‏‏.‏ وفي رواية البخاري‏:‏ ‏"‏إذا نظر أحدكم إلى من فضل عليه في المال والخلق، فلينظر إلى من هو أسفل منه‏"‏‏.‏

### English OpenAI &nbsp;&nbsp; `adab 592` &nbsp; score: 0.6640

Abu Hurayra said, "One of you looks at the mote in his brother's eye while forgetting the stump in his own eye."

**Arabic:** ‏:‏ يُبْصِرُ أَحَدُكُمُ الْقَذَاةَ فِي عَيْنِ أَخِيهِ، وَيَنْسَى الْجِذْلَ، أَوِ الْجِذْعَ، فِي عَيْنِ نَفْسِهِ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `muslim 19 b` &nbsp; score: 0.6397 · clusters: [70, 64]

The above hadith has been mentioned with a different chain with a slightly different wording at the beginning, then follows the same.

**Arabic:** ‏"‏ إِنَّكَ سَتَأْتِي قَوْمًا ‏"‏ بِمِثْلِ حَدِيثِ وَكِيعٍ ‏.‏

---

## Rank 6

### Mixedbread &nbsp;&nbsp; `muslim 2536` &nbsp; score: 0.7850

'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to which I belong, then of the second generation (generation adjacent to my generation), then of the third generation (generation adjacent to the second generation).

**Arabic:** ‏"‏ الْقَرْنُ الَّذِي أَنَا فِيهِ ثُمَّ الثَّانِي ثُمَّ الثَّالِثُ ‏"‏ ‏.‏

### English OpenAI &nbsp;&nbsp; `muslim 7070` &nbsp; score: 0.6634

Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those who stand at a higher level than you, for that is better-suited that you do not disparage Allah's favors. In the chain narrated by Abu Mu'awiya's he said: Upon you.

### Arabic OpenAI &nbsp;&nbsp; `nasai 813` &nbsp; score: 0.6362 · clusters: [70, 64]

It was narrated from Anas that the Prophet (saws) used to say: "Make your rows straight, make your rows straight, make your rows straight. By the One in Whose Hand is my soul! I can see you behind me as I can see you in front of me."

**Arabic:** ‏"‏ اسْتَوُوا اسْتَوُوا اسْتَوُوا فَوَالَّذِي نَفْسِي بِيَدِهِ إِنِّي لأَرَاكُمْ مِنْ خَلْفِي كَمَا أَرَاكُمْ مِنْ بَيْنِ يَدَىَّ ‏"‏ ‏.‏

---

## Rank 7

### Mixedbread &nbsp;&nbsp; `abudawud 4092` &nbsp; score: 0.7821

Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been given some of it, as you see. And I do not like that anyone excels me (in respect of beauty). Perhaps he said: "even to the extent of thong of my sandal (shirak na'li)", or he he said: "to the extent of strap of my sandal (shis'i na'li)". Is it pride? He replied: No, pride is disdaining what is true and despising people.

**Arabic:** يَا رَسُولَ اللَّهِ إِنِّي رَجُلٌ حُبِّبَ إِلَىَّ الْجَمَالُ وَأُعْطِيتُ مِنْهُ مَا تَرَى حَتَّى مَا أُحِبُّ أَنْ يَفُوقَنِي أَحَدٌ - إِمَّا قَالَ بِشِرَاكِ نَعْلِي ‏.‏ وَإِمَّا قَالَ بِشِسْعِ نَعْلِي - أَفَمِنَ الْكِبْرِ ذَلِكَ قَالَ ‏"‏ لاَ وَلَكِنَّ الْكِبْرَ مَنْ بَطَرَ الْحَقَّ وَغَمَطَ النَّاسَ ‏"‏ ‏.‏

### English OpenAI &nbsp;&nbsp; `bulugh 1514` &nbsp; score: 0.6632

Ibn ’Umar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “He who imitates any people (in their actions) is considered to be one of them.” Related by Abu Dawud and Ibn Hibban graded it as Sahih.

### Arabic OpenAI &nbsp;&nbsp; `adab 942` &nbsp; score: 0.6354 · clusters: [70, 64]

Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "When one of you yawns, he should repress it as much as possible."

**Arabic:** ‏:‏ إِذَا تَثَاءَبَ أَحَدُكُمْ فَلْيَكْظِمْ مَا اسْتَطَاعَ‏.‏

---

## Rank 8

### Mixedbread &nbsp;&nbsp; `tirmidhi 2513` &nbsp; score: 0.7818

Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indeed that is more worthy(so that you will) not belittle Allah's favors upon you."

**Arabic:** صلى الله عليه وسلم ‏"‏ انْظُرُوا إِلَى مَنْ هُوَ أَسْفَلَ مِنْكُمْ وَلاَ تَنْظُرُوا إِلَى مَنْ هُوَ فَوْقَكُمْ فَإِنَّهُ أَجْدَرُ أَنْ لاَ تَزْدَرُوا نِعْمَةَ اللَّهِ عَلَيْكُمْ ‏"‏ ‏.‏ هَذَا حَدِيثٌ صَحِيحٌ ‏.‏

### English OpenAI &nbsp;&nbsp; `hisn 231` &nbsp; score: 0.6617

If any of you praises his companion then let him say: Aḥsibu fulānan wallāhu ḥasībuh wa lā uzakkī `alallāhi aḥada. If any of you praises his companion then let him say: I consider (such and such a person), and Allah is his Assessor, (meaning: and I cannot claim anyone to be pious before Allah) if you know of this (good character trait in the person) to be such and such (saying what he thinks is praiseworthy in that person). Reference: Muslim 4/2296.

**Arabic:** قال صلى الله عليه وسلم: "إِذَا كَانَ أَحَدُكُم مَادِحاً صَاحِبَهُ لاَ مَحَالَةَ فَلْيَقُلْ: أَحْسِبُ فُلاَناً وَاللَّهُ حَسِيبُهُ، وَلاَ أُزَكِّي عَلَى اللَّهِ أَحَداً، أَحْسِبُهُ – إِنْ كَانَ يَعْلَمُ ذَاكَ – كَذَا وَكَذَا"

### Arabic OpenAI &nbsp;&nbsp; `muslim 632 b` &nbsp; score: 0.6345 · clusters: [70, 64]

Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels take turns among you by night and by day, and the rest of the hadith is the same.

**Arabic:** ‏"‏ وَالْمَلاَئِكَةُ يَتَعَاقَبُونَ فِيكُمْ ‏"‏ ‏.‏ بِمِثْلِ حَدِيثِ أَبِي الزِّنَادِ ‏.‏

---

## Rank 9

### Mixedbread &nbsp;&nbsp; `adab 898` &nbsp; score: 0.7815

Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes so that you might come to know each other. The noblest among you in Allah's sight is the one with the most taqwa.' (49:13) One man says to another man, 'I am more noble than you are.' No one is nobler than another person except by taqwa."

**Arabic:** الرَّجُلُ لِلرَّجُلِ‏:‏ أَنَا أَكْرَمُ مِنْكَ، فَلَيْسَ أَحَدٌ أَكْرَمَ مِنْ أَحَدٍ إِلا بِتَقْوَى اللهِ‏.‏

### English OpenAI &nbsp;&nbsp; `tirmidhi 2513` &nbsp; score: 0.6581

Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indeed that is more worthy(so that you will) not belittle Allah's favors upon you."

**Arabic:** صلى الله عليه وسلم ‏"‏ انْظُرُوا إِلَى مَنْ هُوَ أَسْفَلَ مِنْكُمْ وَلاَ تَنْظُرُوا إِلَى مَنْ هُوَ فَوْقَكُمْ فَإِنَّهُ أَجْدَرُ أَنْ لاَ تَزْدَرُوا نِعْمَةَ اللَّهِ عَلَيْكُمْ ‏"‏ ‏.‏ هَذَا حَدِيثٌ صَحِيحٌ ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `ahmad 1398` &nbsp; score: 0.6328 · clusters: [70, 64]

It was narrated from Moosa bin Talhah, from his father, that The Prophet (ﷺ) said: “Let one of you put something in front of him the height of the back of a saddle, then pray.`

**Arabic:** يَجْعَلُ أَحَدُكُمْ بَيْنَ يَدَيْهِ مِثْلَ مُؤْخِرَةِ الرَّحْلِ ثُمَّ يُصَلِّي‏.‏

---

## Rank 10

### Mixedbread &nbsp;&nbsp; `riyadussalihin 7` &nbsp; score: 0.7793

Abu Hurairah (May Allah be pleased with him) narrated: Messenger of Allah (PBUH) said, "Allah does not look at your figures, nor at your attire but He looks at your hearts and accomplishments". [Muslim] .

**Arabic:** - وعن أبي هريرة عبد الرحمن بن صخر رضي الله عنه قال قال رسول الله صلى الله عليه وسلم‏:‏ ‏"‏ إن الله لا ينظر إلى أجسامكم ، ولا إلى صوركم، ولكن ينظر إلى قلوبكم وأعمالكم‏"‏ ‏(‏‏(‏رواه مسلم‏)‏‏)‏‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 619` &nbsp; score: 0.6557 · dup-rep: 47000

Narrated Abu Huraira: Allah's Apostle said, "Not to wish to be the like of except the like of two men: a man whom Allah has given the Qur'an and he recites it during the hours of the night and the hours of the day, in which case one may say, "If I were given the same as this man has been given, I would do the same as he is doing.' The other is a man whom Allah has given wealth and he spends it in the right way, in which case one may say, 'If I were given the same as he has been given, I would do the same as he is doing."

**Arabic:** يُصَلِّي رَكْعَتَيْنِ خَفِيفَتَيْنِ بَيْنَ النِّدَاءِ وَالإِقَامَةِ مِنْ صَلاَةِ الصُّبْحِ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `ibnmajah 161` &nbsp; score: 0.6327 · clusters: [70, 64]

It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Do not revile my Companions, for by The One in Whose Hand is my soul! If any one of you were to spend the equivalent of Mount Uhud in gold, it would not equal a Mudd spent by anyone of them, nor even half a Mudd."

**Arabic:** ـ صلى الله عليه وسلم ـ ‏"‏ لاَ تَسُبُّوا أَصْحَابِي فَوَالَّذِي نَفْسِي بِيَدِهِ لَوْ أَنَّ أَحَدَكُمْ أَنْفَقَ مِثْلَ أُحُدٍ ذَهَبًا مَا أَدْرَكَ مُدَّ أَحَدِهِمْ وَلاَ نَصِيفَهُ ‏"‏ ‏.‏

---


# Summary — Top-3 per Query

## "aisha"

| Rank | Mixedbread | English OpenAI | Arabic OpenAI |
|---|---|---|---|
| **1** | `bukhari 3894` Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went | `bukhari 251` Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and All | `bukhari 4752` Narrated Ibn Abi Mulaika: I heard `Aisha reciting: "When you invented a lie (and |
| **2** | `bukhari 277` Narrated Aisha: Whenever any one of us was Junub, she poured water over her head | `abudawud 2758` Narrated Aisha, Ummul Mu'minin: A woman would give security from the believers a | `muslim 1452 c` Ahadith like this is transmitted by 'A'isha through another chain of narrators. |
| **3** | `abudawud 4164` Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman c | `bukhari 92` Narrated 'Aisha: that she prepared a lady for a man from the Ansar as his bride  | `bukhari 2628` Narrated Aiman: I went to `Aisha and she was wearing a coarse dress costing five |

## "comparing yourself to others"

| Rank | Mixedbread | English OpenAI | Arabic OpenAI |
|---|---|---|---|
| **1** | `forty 18` The felicitous person takes lessons from (the actions of) others. | `adab 328` Ibn 'Abbas said, "When you want to mention your companion's faults, remember you | `ibnmajah 1977` It was narrated from Ibn 'Abbas that: the Prophet said: "The best of you is the  |
| **2** | `bukhari 6490` Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person | `riyadussalihin 466` Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) | `abudawud 879` ‘A’ishah said; one night I missed the Messenger of Allah (may peace be upon him) |
| **3** | `muslim 2963 a` Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When o | `bukhari 497` Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person | `nasai 169` It was narrated from Abu Hurairah that 'Aishah said: "I noticed the Prophet (PBU |

---
*Generated by `tests/focused_comparison.py`*