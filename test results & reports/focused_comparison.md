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

**Latency:** **Mixedbread** 137ms · **English OpenAI** 584ms · **Arabic OpenAI** 401ms

## Rank 1

### Mixedbread &nbsp;&nbsp; `shamail 173` &nbsp; score: 0.8567

Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the superiority of tharid [a dish of sopped bread, meat and broth] over all other food.”

**Arabic:** ‏:‏ فَضْلُ عَائِشَةَ عَلَى النِّسَاءِ كَفَضْلِ الثَّرِيدِ عَلَى سَائِرِ الطَّعَامِ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 275` &nbsp; score: 0.7848

Narrated Um Ruman: Aisha's mother, When `Aisha was accused, she fell down Unconscious.

**Arabic:** فَخَرَجَ إِلَيْنَا رَسُولُ اللَّهِ صلى الله عليه وسلم فَلَمَّا قَامَ فِي مُصَلاَّهُ ذَكَرَ أَنَّهُ جُنُبٌ فَقَالَ لَنَا ‏:‏ ‏"‏ مَكَانَكُمْ ‏"‏‏.‏ ثُمَّ رَجَعَ فَاغْتَسَلَ، ثُمَّ خَرَجَ إِلَيْنَا وَرَأْسُهُ يَقْطُرُ، فَكَبَّرَ فَصَلَّيْنَا مَعَهُ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `bukhari 4752` &nbsp; score: 0.6892 · clusters: [27, 74]

Narrated Ibn Abi Mulaika: I heard `Aisha reciting: "When you invented a lie (and carry it) on your tongues." (24.15)

**Arabic:** عَائِشَةَ، تَقْرَأُ ‏[quran sura="24" aya_start="15" aya_end="15"]{‏إِذْ تَلِقُونَهُ بِأَلْسِنَتِكُمْ‏}[/quran]‏

---

## Rank 2

### Mixedbread &nbsp;&nbsp; `bukhari 2046` &nbsp; score: 0.8452

Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch out his head towards her while she was in her chamber.

**Arabic:** تُرَجِّلُ النَّبِيَّ صلى الله عليه وسلم وَهِيَ حَائِضٌ وَهْوَ مُعْتَكِفٌ فِي الْمَسْجِدِ وَهْىَ فِي حُجْرَتِهَا، يُنَاوِلُهَا رَأْسَهُ‏.‏

### English OpenAI &nbsp;&nbsp; `abudawud 2909` &nbsp; score: 0.7828

Narrated Ibn 'Umar: 'Aishah, mother of believers (ra), intended to buy a slave-girl to set her free. Her people said: We shall sell her to you on one condition that we shall inherit from her. 'Aishah mentioned it to the Messenger of Allah (saws). He said: That should not prevent you, for the right of inheritance belongs to the one who has set a person free.

**Arabic:** ‏"‏ لاَ يَرِثُ الْمُسْلِمُ الْكَافِرَ وَلاَ الْكَافِرُ الْمُسْلِمَ ‏"‏ ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `muslim 1452 c` &nbsp; score: 0.6790 · clusters: [27, 74]

Ahadith like this is transmitted by 'A'isha through another chain of narrators.

**Arabic:** عَائِشَةَ، تَقُولُ ‏.‏ بِمِثْلِهِ ‏.‏

---

## Rank 3

### Mixedbread &nbsp;&nbsp; `abudawud 269` &nbsp; score: 0.8410

Narrated Aisha, Ummul Mu'minin: Khallas al-Hujari reported: Aisha said: I and the Messenger of Allah (saws) used to pass night in one (piece of) cloth (on me) while I menstruated profusely. If anything from me (i.e. blood) smeared him (i.e. his body), he would wash that spot and would not exceed it (in washing), then he would offer prayer with it.

**Arabic:** عَائِشَةَ، - رضى الله عنها - تَقُولُ كُنْتُ أَنَا وَرَسُولُ اللَّهِ، صلى الله عليه وسلم نَبِيتُ فِي الشِّعَارِ الْوَاحِدِ وَأَنَا حَائِضٌ طَامِثٌ فَإِنْ أَصَابَهُ مِنِّي شَىْءٌ غَسَلَ مَكَانَهُ وَلَمْ يَعْدُهُ ثُمَّ صَلَّى فِيهِ وَإِنْ أَصَابَ - تَعْنِي ثَوْبَهُ - مِنْهُ شَىْءٌ غَسَلَ مَكَانَهُ وَلَمْ يَعْدُهُ ثُمَّ صَلَّى فِيهِ ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 842` &nbsp; score: 0.7818

Narrated Anas: Aisha had a thick curtain (having pictures on it) and she screened the side of her i house with it. The Prophet said to her, "Remove it from my sight, for its pictures are still coming to my mind in my prayers."

**Arabic:** انْقِضَاءَ صَلاَةِ النَّبِيِّ صلى الله عليه وسلم بِالتَّكْبِيرِ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `bukhari 2628` &nbsp; score: 0.6754 · clusters: [27, 74]

Narrated Aiman: I went to `Aisha and she was wearing a coarse dress costing five Dirhams. `Aisha said, "Look up and see my slave-girl who refuses to wear it in the house though during the lifetime of Allah's Apostle I had a similar dress which no woman desiring to appear elegant (before her husband) failed to borrow from me."

**Arabic:** دَخَلْتُ عَلَى [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةَ[/narrator] ـ رضى الله عنها ـ وَعَلَيْهَا دِرْعُ قِطْرٍ ثَمَنُ خَمْسَةِ دَرَاهِمَ، فَقَالَتِ ارْفَعْ بَصَرَكَ إِلَى جَارِيَتِي، انْظُرْ إِلَيْهَا فَإِنَّهَا تُزْهَى أَنْ تَلْبَسَهُ فِي الْبَيْتِ، وَقَدْ كَانَ لِي مِنْهُنَّ دِرْعٌ عَلَى عَهْدِ رَسُولِ اللَّهِ صلى الله عليه وسلم، فَمَا كَانَتِ امْرَأَةٌ تُقَيَّنُ [place]بِالْمَدِينَةِ [/place]إِلاَّ أَرْسَلَتْ إِلَىَّ تَسْتَعِيرُهُ‏.‏

---

## Rank 4

### Mixedbread &nbsp;&nbsp; `bukhari 5818` &nbsp; score: 0.8383

Narrated Abu Burda: Aisha brought out to us a Kisa and an Izar and said, "The Prophet died while wearing these two." (Kisa, a square black piece of woolen cloth. Izar, a sheet cloth garment covering the lower half of the body).

**Arabic:** قُبِضَ رُوحُ النَّبِيِّ صلى الله عليه وسلم فِي هَذَيْنِ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 467` &nbsp; score: 0.7757

Narrated Masruq: We went to `Aisha while Hassan bin Thabit was with her reciting poetry to her from some of his poetic verses, saying "A chaste wise lady about whom nobody can have suspicion. She gets up with an empty stomach because she never eats the flesh of indiscreet (ladies)." `Aisha said to him, "But you are not like that." I said to her, "Why do you grant him admittance, though Allah said:-- "and as for him among them, who had the greater share therein, his will be a severe torment." (24.11) On that, `Aisha said, "And what punishment is more than blinding?" She, added, "Hassan used to defend or say poetry on behalf of Allah's Apostle (against the infidels).

**Arabic:** إِنَّهُ لَيْسَ مِنَ النَّاسِ أَحَدٌ أَمَنَّ عَلَىَّ فِي نَفْسِهِ وَمَالِهِ مِنْ أَبِي بَكْرِ بْنِ أَبِي قُحَافَةَ، وَلَوْ كُنْتُ مُتَّخِذًا مِنَ النَّاسِ خَلِيلاً لاَتَّخَذْتُ أَبَا بَكْرٍ خَلِيلاً، وَلَكِنْ خُلَّةُ الإِسْلاَمِ أَفْضَلُ، سُدُّوا عَنِّي كُلَّ خَوْخَةٍ فِي هَذَا الْمَسْجِدِ غَيْرَ خَوْخَةِ أَبِي بَكْرٍ ‏"

### Arabic OpenAI &nbsp;&nbsp; `bukhari 1641, 1642` &nbsp; score: 0.6709 · clusters: [27, 74]

Narrated Muhammad bin `Abdur-Rahman bin Nawfal Al-Qurashi: I asked `Urwa bin Az-Zubair (regarding the Hajj of the Prophet ). `Urwa replied, "Aisha narrated, 'When the Prophet reached Mecca, the first thing he started with was the ablution, then he performed Tawaf of the Ka`ba and his intention was not `Umra alone (but Hajj and `Umra together).' " Later Abu Bakr I performed the Hajj and the first thing he started with was Tawaf of the Ka`ba and it was not `Umra alone (but Hajj and `Umra together). And then `Umar did the same. Then `Uthman performed the Hajj and the first thing he started with was Tawaf of the Ka`ba and it was not `Umra alone. And then Muawiya and `Abdullah bin `Umar did the same. I performed Hajj with Ibn Az-Zubair and the first thing he started with was Tawaf of the Ka`ba and it was not `Umra alone, (but Hajj and `Umra together). Then I saw the Muhajirin (Emigrants) and Ansar doing the same and it was not `Umra alone. And the last person I saw doing the same was Ibn `Umar, and he did not do another `Umra after finishing the first. Now here is Ibn `Umar present amongst the people! They neither ask him nor anyone of the previous ones. And all these people, on entering Mecca, would not start with anything unless they had performed Tawaf of the Ka`ba, and would not finish their Ihram. And no doubt, I saw my mother and my aunt, on entering Mecca doing nothing before performing Tawaf of the Ka`ba, and they would not finish their lhram. And my mother informed me that she, her sister, Az-Zubair and such and such persons had assumed lhram for `Umra and after passing their hands over the Corner (the Black Stone) (i.e. finishing their Umra) they finished their Ihram."

**Arabic:** حَجَّ النَّبِيُّ صلى الله عليه وسلم فَأَخْبَرَتْنِي [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةُ[/narrator] ـ رضى الله عنها ـ أَنَّهُ أَوَّلُ شَىْءٍ بَدَأَ بِهِ حِينَ قَدِمَ أَنَّهُ تَوَضَّأَ ثُمَّ طَافَ [place]بِالْبَيْتِ[/place] ثُمَّ لَمْ تَكُنْ عُمْرَةً

---

## Rank 5

### Mixedbread &nbsp;&nbsp; `nasai 773` &nbsp; score: 0.8380

Khilas bin 'Amr said: "I heard Aisha (ra) say: 'The Messenger of Allah (saws), Abii Al-Qbim, and I were beneath a single blanket, and I was menstruating. If something got on him from me, he would wash whatever had got on him and he did not wash anywhere else, and he prayed in it then came back to me.And if anything got on him from me,he would do exactly the same and he did not wash anywhere else."'

**Arabic:** عَائِشَةَ، تَقُولُ كُنْتُ أَنَا وَرَسُولُ اللَّهِ، صلى الله عليه وسلم أَبُو الْقَاسِمِ فِي الشِّعَارِ الْوَاحِدِ وَأَنَا حَائِضٌ، طَامِثٌ فَإِنْ أَصَابَهُ مِنِّي شَىْءٌ غَسَلَ مَا أَصَابَهُ لَمْ يَعْدُهُ إِلَى غَيْرِهِ وَصَلَّى فِيهِ ثُمَّ يَعُودُ مَعِي فَإِنْ أَصَابَهُ مِنِّي شَىْءٌ فَعَلَ مِثْلَ ذَلِكَ لَمْ يَعْدُهُ إِلَى غَيْرِهِ ‏.‏

### English OpenAI &nbsp;&nbsp; `adab 613` &nbsp; score: 0.7752

'Ikrima heard 'A'isha, may Allah be pleased with her, say that she saw the Prophet, may Allah bless him and grant him peace, raise his hands in supplication, saying, 'O Allah, I am only a man, so do not punish me. If I harm or revile a Muslim man, do not punish me for it!'"

**Arabic:** ‏:‏ اللَّهُمَّ إِنَّمَا أَنَا بَشَرٌ فَلاَ تُعَاقِبْنِي، أَيُّمَا رَجُلٌ مِنَ الْمُؤْمِنِينَ آذَيْتُهُ أَوْ شَتَمْتُهُ فَلا تُعَاقِبْنِي فِيهِ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `muslim 738 e` &nbsp; score: 0.6687 · clusters: [27, 74]

It is reported on the authority of 'A'isha that the prayer of Allah's Messenger (may peace be upon him) in the night consisted of ten rak'ahs. He observed a Witr and two rak'ahs (of Sunan) of the dawn prayer, and thus the total comes to thirteen rak'ahs.

**Arabic:** عَائِشَةَ، تَقُولُ كَانَتْ صَلاَةُ رَسُولِ اللَّهِ صلى الله عليه وسلم مِنَ اللَّيْلِ عَشَرَ رَكَعَاتٍ وَيُوتِرُ بِسَجْدَةٍ وَيَرْكَعُ رَكْعَتَىِ الْفَجْرِ فَتِلْكَ ثَلاَثَ عَشْرَةَ رَكْعَةً ‏.‏

---

## Rank 6

### Mixedbread &nbsp;&nbsp; `bukhari 6757` &nbsp; score: 0.8359 · dup-rep: 20400

Narrated Ibn `Umar: That Aisha, the mother of the Believers, intended to buy a slave girl in order to manumit her. The slave girl's master said, "We are ready to sell her to you on the condition that her Wala should be for us." Aisha mentioned that to Allah's Apostle who said, "This (condition) should not prevent you from buying her, for the Wala is for the one who manumits (the slave)."

**Arabic:** الْوَلاَءُ لِمَنْ أَعْتَقَ ‏"

### English OpenAI &nbsp;&nbsp; `abudawud 2285` &nbsp; score: 0.7749

Urwah said: Aisha (Allah be pleased with her) severely objected to the tradition of Fatimah daughter of Qays. She said: Fatimah lived in a desolate house and she feared for her loneliness there. Hence the Messenger of Allah (saws) accorded permission to her (to leave the place).

**Arabic:** وا يَا نَبِيَّ اللَّهِ إِنَّ أَبَا حَفْصِ بْنَ الْمُغِيرَةِ طَلَّقَ امْرَأَتَهُ ثَلاَثًا وَإِنَّهُ تَرَكَ لَهَا نَفَقَةً يَسِيرَةً فَقَالَ ‏"‏ لاَ نَفَقَةَ لَهَا ‏"‏ ‏.‏ وَسَاقَ الْحَدِيثَ وَحَدِيثُ مَالِكٍ أَتَمُّ ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `bukhari 4872` &nbsp; score: 0.6679 · clusters: [27, 74]

Narrated `Abdullah bin Masud: The Prophet used to recite: "Fahal-min-Maddakir (then is there any that will receive admonition?")

**Arabic:** ‏[quran sura="54" aya_start="15" aya_end="15"]{‏فَهَلْ مِنْ مُدَّكِرٍ‏}[/quran]‏ الآيَةَ‏.‏

---

## Rank 7

### Mixedbread &nbsp;&nbsp; `tirmidhi 3889` &nbsp; score: 0.8356

Narrated 'Ammar bin Yasir: "She is his wife in the world and in the Hereafter." - meaning: 'Aishah [may Allah be pleased with her].

**Arabic:** هِيَ زَوْجَتُهُ فِي الدُّنْيَا وَالآخِرَةِ ‏.‏ يَعْنِي عَائِشَةَ رضى الله عنها ‏.‏ هَذَا حَدِيثٌ حَسَنٌ صَحِيحٌ ‏.‏ وَفِي الْبَابِ عَنْ عَلِيِّ ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 378` &nbsp; score: 0.7744 · dup-rep: 20400

Narrated `Abdullah bin `Umar: Aisha, (mother of the faithful believers) wanted to buy a slave girl and manumit her, but her masters said that they would sell her only on the condition that her Wala' would be for them. `Aisha told Allah's Apostle of that. He said, "What they stipulate should not hinder you from buying her, as the Wala' is for the manumitted."

**Arabic:** إِنَّمَا جُعِلَ الإِمَامُ لِيُؤْتَمَّ بِهِ، فَإِذَا كَبَّرَ فَكَبِّرُوا، وَإِذَا رَكَعَ فَارْكَعُوا، وَإِذَا سَجَدَ فَاسْجُدُوا، وَإِنْ صَلَّى قَائِمًا فَصَلُّوا قِيَامًا ‏"‏‏.‏ وَنَزَلَ لِتِسْعٍ وَعِشْرِينَ فَقَالُوا يَا رَسُولَ اللَّهِ إِنَّكَ آلَيْتَ شَهْرًا فَقَالَ ‏"‏ إِنَّ الشَّهْرَ تِسْعٌ وَعِشْرُونَ ‏"

### Arabic OpenAI &nbsp;&nbsp; `abudawud 1341` &nbsp; score: 0.6675 · clusters: [27, 74]

Abu Salamah b. 'Abd al-Rahman asked 'Aishah, the wife of the Prophet (saws): How did the Messenger of Allah (saws) pray during Ramadhan ? She said: The Messenger of Allah (saws) did not pray more than eleven rak'ahs during Ramadhan and other than Ramadhan. He would pray four rak'ahs. Do not ask about their elegance and length. He then would pray for rak'ahs. Do not ask about their alegance and length. Then he would pray three rak'ahs. 'Aishah said: I asked: Messenger of Allah, do you sleep before observing witr ? He replied: 'Aishah, my eyes sleep, but my heart does not sleep.

**Arabic:** ‏:‏ ‏"‏ يَا عَائِشَةُ إِنَّ عَيْنَىَّ تَنَامَانِ وَلاَ يَنَامُ قَلْبِي ‏"‏ ‏.‏

---

## Rank 8

### Mixedbread &nbsp;&nbsp; `bukhari 3108` &nbsp; score: 0.8350

Narrated Abu Burda: `Aisha brought out to us a patched wool Len garment, and she said, "(It chanced that) the soul of Allah's Apostle was taken away while he was wearing this." Abu-Burda added, "Aisha brought out to us a thick waist sheet like the ones made by the Yemenites, and also a garment of the type called Al- Mulabbada."

**Arabic:** ـ كِسَاءً مُلَبَّدًا وَقَالَتْ فِي هَذَا نُزِعَ رُوحُ النَّبِيِّ صلى الله عليه وسلم‏.‏ وَزَادَ [narrator id="3570" role="chain" tooltip="سليمان بن المغيرة القيسي"]سُلَيْمَانُ[/narrator] عَنْ [narrator id="2553" role="chain" tooltip="حميد بن هلال العدوي"]حُمَيْدٍ[/narrator] عَنْ [narrator id="4108" role="chain" tooltip="أبو بردة بن أبي موسى الأشعري"]أَبِي بُرْدَةَ[/narrator] قَالَ أَخْرَجَتْ إِلَيْنَا [narrator id="4049" role="sahabi" tooltip="عائشة بنت أبي بكر الصديق"]عَائِشَةُ[/narrator] إِزَارًا غَلِيظًا مِمَّا يُصْنَعُ [place]بِالْيَمَنِ، [/place]وَكِسَاءً مِنْ هَذِهِ الَّتِي يَدْعُونَهَا الْمُلَبَّدَةَ‏.‏

### English OpenAI &nbsp;&nbsp; `muslim 464` &nbsp; score: 0.7743

Salim, the freed slave of Shaddad, said: I came to 'A'isha, the wife of the Holy Prophet (may peace be upon him), on the day when Sa'db. Abi Waqqas died. 'Abd al-Rahman b. Abu Bakr also came there and he performed ablution in her presence. She (Hadrat 'A'isha) said: Abd al-Rahman, complete the ablution as I heard the Allah's Messenger (may peace be upon him) say: Woe to the heels because of hell-fire.

### Arabic OpenAI &nbsp;&nbsp; `tirmidhi 588` &nbsp; score: 0.6652 · clusters: [27, 74]

Sa'eed bin Abi Hind narrated from some of the companions of Ikrimah: "The Prophet would glance during Salat" and he mentioned a similar narration.

**Arabic:** وَفِي الْبَابِ عَنْ أَنَسٍ وَعَائِشَةَ ‏.‏

---

## Rank 9

### Mixedbread &nbsp;&nbsp; `ibnmajah 1877` &nbsp; score: 0.8331

It was narrated that: Abdullah said: “The Prophet married Aishah when she was seven years old, and consummated the marriage with her when she was nine, and he passed away when she was eighteen.”

**Arabic:** تَزَوَّجَ النَّبِيُّ ـ صلى الله عليه وسلم ـ عَائِشَةَ وَهِيَ بِنْتُ سَبْعٍ وَبَنَى بِهَا وَهِيَ بِنْتُ تِسْعٍ وَتُوُفِّيَ عَنْهَا وَهِيَ بِنْتُ ثَمَانِي عَشْرَةَ سَنَةً ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 280` &nbsp; score: 0.7710

Narrated Masruq: Hassan came to Aisha and said the following poetic Verse: 'A chaste pious woman who arouses no suspicion. She never talks against chaste heedless women behind their backs.' `Aisha said, "But you are not," I said (to `Aisha), "Why do you allow such a person to enter upon you after Allah has revealed: "...and as for him among them who had the greater share therein'?" (24.11) She said, "What punishment is worse than blindness?" She added, "And he used to defend Allah's Apostle against the pagans (in his poetry).

**Arabic:** يَغْتَسِلُ وَفَاطِمَةُ تَسْتُرُهُ فَقَالَ ‏"‏ مَنْ هَذِهِ ‏"‏‏.‏ فَقُلْتُ أَنَا أُمُّ هَانِئٍ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `tirmidhi 1839` &nbsp; score: 0.6651 · clusters: [27, 74]

Narrated Jabir: That the Prophet (saws) said: "What an excellent condiment vinegar is."

**Arabic:** ‏"‏ نِعْمَ الإِدَامُ الْخَلُّ ‏"‏ ‏.‏ قَالَ وَفِي الْبَابِ عَنْ عَائِشَةَ وَأُمِّ هَانِئٍ ‏.‏

---

## Rank 10

### Mixedbread &nbsp;&nbsp; `ibnmajah 626` &nbsp; score: 0.8321

It was narrated from 'Urwah bin Zubair and 'Amrah bint 'Abdur-Rahman that : 'Aishah the wife of the Prophet said: "Umm Habibah Jahsh experienced prolonged non-menstrual bleeding for seven years when she was married to 'Abdur-Rahman bin 'Awf. She complained about that to the Prophet and the Prophet said: 'That is not menstruation, rather it is a vein, so when the time of your period comes, leave the prayer, and when it is over, take a bath and perform prayer.'" 'Aishah said: "She used to bathe for every prayer and then perform the prayer. She used to sit in a washtub belonging to her sister Zainab bint Jahsh and the blood would turn the water red."

**Arabic:** النَّبِيُّ ـ صلى الله عليه وسلم ـ ‏"‏ إِنَّ هَذِهِ لَيْسَتْ بِالْحَيْضَةِ وَإِنَّمَا هُوَ عِرْقٌ فَإِذَا أَقْبَلَتِ الْحَيْضَةُ فَدَعِي الصَّلاَةَ وَإِذَا أَدْبَرَتْ فَاغْتَسِلِي وَصَلِّي ‏"‏ ‏.‏ قَالَتْ عَائِشَةُ فَكَانَتْ تَغْتَسِلُ لِكُلِّ صَلاَةٍ ثُمَّ تُصَلِّي وَكَانَتْ تَقْعُدُ فِي مِرْكَنٍ لأُخْتِهَا زَيْنَبَ بِنْتِ جَحْشٍ حَتَّى إِنَّ حُمْرَةَ الدَّمِ لَتَعْلُو الْمَاءَ ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 262` &nbsp; score: 0.7708

Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch out his head towards her while she was in her chamber.

**Arabic:** إِذَا اغْتَسَلَ مِنَ الْجَنَابَةِ غَسَلَ يَدَهُ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `muslim 1479 d` &nbsp; score: 0.6647 · clusters: [27, 74]

Ibn Abbas (Allah be pleased with them) is reported to have said: I intended to ask Umar about those two ladies who had pressed for (worldly riches) during the lifetime of the Holy Prophet (may peace be upon him), and I kept waiting for one year, but found no suitable opportunity with him until I happened to accompany him to Mecca. And as he reached Marr al Zahran he went away to answer the call of nature, and he said (to me): Bring me a jug of water, and I took that to him. After having answered the call of nature, as he came back, I began to pour water (over his hands and feet), and I remembered (this event of separation of Allah's Apostle [may peace be upon him] from his wives). So I said to him: Commander of the Faithful, who are the two ladies (who had pressed the Holy Prophet [may peace be upon him] for providing comforts of life) and I had not yet finished my talk when he said: They were 'A'isha and Hafsa.

**Arabic:** عَائِشَةُ وَحَفْصَةُ ‏.‏

---


# Query: "comparing yourself to others"

**Latency:** **Mixedbread** 89ms · **English OpenAI** 293ms · **Arabic OpenAI** 168ms

## Rank 1

### Mixedbread &nbsp;&nbsp; `muslim 2963 a` &nbsp; score: 0.8624

Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you in regard to these things (in which he stands) at a higher level (as compared to him).

**Arabic:** ‏"‏ إِذَا نَظَرَ أَحَدُكُمْ إِلَى مَنْ فُضِّلَ عَلَيْهِ فِي الْمَالِ وَالْخَلْقِ فَلْيَنْظُرْ إِلَى مَنْ هُوَ أَسْفَلَ مِنْهُ مِمَّنْ فُضِّلَ عَلَيْهِ ‏"‏ ‏.‏

### English OpenAI &nbsp;&nbsp; `adab 328` &nbsp; score: 0.7202

Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faults."

**Arabic:** ‏:‏ إِذَا أَرَدْتَ أَنْ تَذْكُرَ عُيُوبَ صَاحِبِكَ، فَاذْكُرْ عُيُوبَ نَفْسِكَ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `ibnmajah 1977` &nbsp; score: 0.6552 · clusters: [70, 64]

It was narrated from Ibn 'Abbas that: the Prophet said: "The best of you is the one who is best to his wife, and I am the best of you to my wives."

**Arabic:** ‏"‏ خَيْرُكُمْ خَيْرُكُمْ لأَهْلِهِ وَأَنَا خَيْرُكُمْ لأَهْلِي ‏"‏ ‏.‏

---

## Rank 2

### Mixedbread &nbsp;&nbsp; `bukhari 6490` &nbsp; score: 0.8144

Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him.

**Arabic:** إِذَا نَظَرَ أَحَدُكُمْ إِلَى مَنْ فُضِّلَ عَلَيْهِ فِي الْمَالِ وَالْخَلْقِ، فَلْيَنْظُرْ إِلَى مَنْ هُوَ أَسْفَلَ مِنْهُ ‏"

### English OpenAI &nbsp;&nbsp; `muslim 7068` &nbsp; score: 0.7152

Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard to wealth and physical structure he should also see one who stands at a lower level than you in regard to these things (in which he stands) at a higher level (as compared to him).

### Arabic OpenAI &nbsp;&nbsp; `abudawud 879` &nbsp; score: 0.6475 · clusters: [70, 64]

‘A’ishah said; one night I missed the Messenger of Allah (may peace be upon him) and when I sought him on the spot of prayer I found him in prostration with his feet raised, and he was saying:”(O Allah), I seek refuge in Your good pleasure from Your anger, and in Your Mercy from Your Punishment, and I seek refuge from You in You; I am not able to praise You (the way that You deserve to be praised), for You are as You have praised Yourself”.

**Arabic:** ‏"‏ أَعُوذُ بِرِضَاكَ مِنْ سَخَطِكَ وَأَعُوذُ بِمُعَافَاتِكَ مِنْ عُقُوبَتِكَ وَأَعُوذُ بِكَ مِنْكَ لاَ أُحْصِي ثَنَاءً عَلَيْكَ أَنْتَ كَمَا أَثْنَيْتَ عَلَى نَفْسِكَ ‏"‏ ‏.‏

---

## Rank 3

### Mixedbread &nbsp;&nbsp; `forty 18` &nbsp; score: 0.8142

The felicitous person takes lessons from (the actions of) others.

**Arabic:** عَنْ أَبِي ذَرٍّ جُنْدَبِ بْنِ جُنَادَةَ، وَأَبِي عَبْدِ الرَّحْمَنِ مُعَاذِ بْنِ جَبَلٍ رَضِيَ اللَّهُ عَنْهُمَا، عَنْ رَسُولِ اللَّهِ صلى الله عليه و سلم قَالَ: "اتَّقِ اللَّهَ حَيْثُمَا كُنْت، وَأَتْبِعْ السَّيِّئَةَ الْحَسَنَةَ تَمْحُهَا، وَخَالِقْ النَّاسَ بِخُلُقٍ حَسَنٍ" . رَوَاهُ التِّرْمِذِيُّ [رقم:1987] وَقَالَ: حَدِيثٌ حَسَنٌ، وَفِي بَعْضِ النُّسَخِ: حَسَنٌ صَحِيحٌ.

### English OpenAI &nbsp;&nbsp; `riyadussalihin 466` &nbsp; score: 0.6908

Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those who are superior to you, for this will keep you from belittling Allah's favour to you." This is the wording in Sahih Muslim. [Al-Bukhari and Muslim] . The narration in Al-Bukhari is: Messenger of Allah (PBUH) said: "When one of you looks at someone who is superior to him in property and appearance, he should look at someone who is inferior to him".

**Arabic:** - وعنه قال‏:‏ قال رسول الله صلى الله عليه وسلم انظروا إلى من هو أسفل منكم ولا تنظروا إلى من هو فوقكم فهو أجدر أن لا تزدروا نعمة الله عليكم‏"‏ ‏(‏‏(‏متفق عليه وهذا لفظ مسلم‏)‏‏)‏‏.‏ وفي رواية البخاري‏:‏ ‏"‏إذا نظر أحدكم إلى من فضل عليه في المال والخلق، فلينظر إلى من هو أسفل منه‏"‏‏.‏ وفي رواية البخاري‏:‏ ‏"‏إذا نظر أحدكم إلى من فضل عليه في المال والخلق، فلينظر إلى من هو أسفل منه‏"‏‏.‏

### Arabic OpenAI &nbsp;&nbsp; `nasai 169` &nbsp; score: 0.6472 · clusters: [70, 64]

It was narrated from Abu Hurairah that 'Aishah said: "I noticed the Prophet (PBUH) was not there one night, so I started looking for him with my hand. My hand touched his feet and they were held upright, and he was prostrating and saying: 'I seek refuge in Your pleasure from Your anger, in Your forgiveness from Your punishment, and I seek refuge in You from You. I cannot praise You enough, You are as You have praised yourself.'"

**Arabic:** ‏"‏ أَعُوذُ بِرِضَاكَ مِنْ سَخَطِكَ وَبِمُعَافَاتِكَ مِنْ عُقُوبَتِكَ وَأَعُوذُ بِكَ مِنْكَ لاَ أُحْصِي ثَنَاءً عَلَيْكَ أَنْتَ كَمَا أَثْنَيْتَ عَلَى نَفْسِكَ ‏"‏ ‏.‏

---

## Rank 4

### Mixedbread &nbsp;&nbsp; `ibnmajah 4032` &nbsp; score: 0.8127

It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The believer who mixes with people and bears their annoyance with patience will have a greater reward than the believer who does not mix with people and does not put up with their annoyance.”

**Arabic:** ـ صلى الله عليه وسلم ـ ‏"‏ الْمُؤْمِنُ الَّذِي يُخَالِطُ النَّاسَ وَيَصْبِرُ عَلَى أَذَاهُمْ أَعْظَمُ أَجْرًا مِنَ الْمُؤْمِنِ الَّذِي لاَ يُخَالِطُ النَّاسَ وَلاَ يَصْبِرُ عَلَى أَذَاهُمْ ‏"‏ ‏.‏

### English OpenAI &nbsp;&nbsp; `ibnmajah 2171` &nbsp; score: 0.6833

It was narrated from Ibn 'Umar that the Messenger of Allah (SAW) said: "Let one of you not undersell another."[1]

**Arabic:** ‏"‏ لاَ يَبِيعُ بَعْضُكُمْ عَلَى بَيْعِ بَعْضٍ ‏"‏ ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `nasai 1130` &nbsp; score: 0.6450 · clusters: [70, 64]

It was narrated that 'Aishah said: "I noticed the Messenger of Allah (SAW) was missing one night and I found him prostrating with the tops of his feet facing toward the Qiblah. I heard him saying: 'A'udhu biridaka min sakhatika, wa a'udhu bimu 'afatika min 'uqubatika wa a'udhu bika minka la uhsi thana'an 'alaika anta kama athnaita 'ala nafsik (I seek refuge in Your pleasure from Your wrath; I seek refuge in Your forgiveness from Your punishment; I seek refuge in You from You. I cannot praise You enough, You are as You have praised Yourself.)"

**Arabic:** ‏"‏ أَعُوذُ بِرِضَاكَ مِنْ سَخَطِكَ وَأَعُوذُ بِمُعَافَاتِكَ مِنْ عُقُوبَتِكَ وَأَعُوذُ بِكَ مِنْكَ لاَ أُحْصِي ثَنَاءً عَلَيْكَ أَنْتَ كَمَا أَثْنَيْتَ عَلَى نَفْسِكَ ‏"‏ ‏.‏

---

## Rank 5

### Mixedbread &nbsp;&nbsp; `ibnmajah 4179` &nbsp; score: 0.8118

It was narrated from ‘Iyad bin Himar that the Prophet (saw) addressed them and said: “Allah has revealed to me that you should be humble towards one another so that none of you boasts to another.”

**Arabic:** ‏"‏ إِنَّ اللَّهَ عَزَّ وَجَلَّ أَوْحَى إِلَىَّ أَنْ تَوَاضَعُوا حَتَّى لاَ يَفْخَرَ أَحَدٌ عَلَى أَحَدٍ ‏"‏ ‏.‏

### English OpenAI &nbsp;&nbsp; `muslim 6696` &nbsp; score: 0.6826

Ibn Umar reported Allah's Apostle (may peace be upon him) as saying: The similitude of a hypocrite is that of a sheep which roams aimlessly between two flocks. She goes to one at one time and to the other at another time.

### Arabic OpenAI &nbsp;&nbsp; `muslim 19 b` &nbsp; score: 0.6395 · clusters: [70, 64]

The above hadith has been mentioned with a different chain with a slightly different wording at the beginning, then follows the same.

**Arabic:** ‏"‏ إِنَّكَ سَتَأْتِي قَوْمًا ‏"‏ بِمِثْلِ حَدِيثِ وَكِيعٍ ‏.‏

---

## Rank 6

### Mixedbread &nbsp;&nbsp; `nasai 4725` &nbsp; score: 0.8074

A similar report was narrated from 'Alqamah bin Wa'il from his father, from the Prophet. Yahya (one of the narrators) said: "He is better than him." [1]

**Arabic:** يَحْيَى وَهُوَ أَحْسَنُ مِنْهُ ‏.‏

### English OpenAI &nbsp;&nbsp; `bulugh 1482` &nbsp; score: 0.6819

Abu Hurairah (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Look at those who are lower than you (financially) but do not look at those who are higher than you, lest you belittle the favors Allah conferred upon you.” Agreed upon.

### Arabic OpenAI &nbsp;&nbsp; `nasai 813` &nbsp; score: 0.6363 · clusters: [70, 64]

It was narrated from Anas that the Prophet (saws) used to say: "Make your rows straight, make your rows straight, make your rows straight. By the One in Whose Hand is my soul! I can see you behind me as I can see you in front of me."

**Arabic:** ‏"‏ اسْتَوُوا اسْتَوُوا اسْتَوُوا فَوَالَّذِي نَفْسِي بِيَدِهِ إِنِّي لأَرَاكُمْ مِنْ خَلْفِي كَمَا أَرَاكُمْ مِنْ بَيْنِ يَدَىَّ ‏"‏ ‏.‏

---

## Rank 7

### Mixedbread &nbsp;&nbsp; `ibnmajah 4214` &nbsp; score: 0.8055

It was narrated from Anas bin Malik that the Messenger of Allah (saw) said: “Allah has revealed to me that you should be humble towards one another and should not wrong one another.”

**Arabic:** ـ صلى الله عليه وسلم ـ ‏"‏ إِنَّ اللَّهَ أَوْحَى إِلَىَّ أَنْ تَوَاضَعُوا وَلاَ يَبْغِي بَعْضُكُمْ عَلَى بَعْضٍ ‏"‏ ‏.‏

### English OpenAI &nbsp;&nbsp; `adab 592` &nbsp; score: 0.6799

Abu Hurayra said, "One of you looks at the mote in his brother's eye while forgetting the stump in his own eye."

**Arabic:** ‏:‏ يُبْصِرُ أَحَدُكُمُ الْقَذَاةَ فِي عَيْنِ أَخِيهِ، وَيَنْسَى الْجِذْلَ، أَوِ الْجِذْعَ، فِي عَيْنِ نَفْسِهِ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `adab 942` &nbsp; score: 0.6354 · clusters: [70, 64]

Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "When one of you yawns, he should repress it as much as possible."

**Arabic:** ‏:‏ إِذَا تَثَاءَبَ أَحَدُكُمْ فَلْيَكْظِمْ مَا اسْتَطَاعَ‏.‏

---

## Rank 8

### Mixedbread &nbsp;&nbsp; `ibnmajah 2171` &nbsp; score: 0.7991

It was narrated from Ibn 'Umar that the Messenger of Allah (SAW) said: "Let one of you not undersell another."[1]

**Arabic:** ‏"‏ لاَ يَبِيعُ بَعْضُكُمْ عَلَى بَيْعِ بَعْضٍ ‏"‏ ‏.‏

### English OpenAI &nbsp;&nbsp; `bukhari 497` &nbsp; score: 0.6796

Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, then he should also look at the one who is inferior to him.

**Arabic:** كَانَ جِدَارُ الْمَسْجِدِ عِنْدَ الْمِنْبَرِ مَا كَادَتِ الشَّاةُ تَجُوزُهَا‏.‏

### Arabic OpenAI &nbsp;&nbsp; `muslim 632 b` &nbsp; score: 0.6345 · clusters: [70, 64]

Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels take turns among you by night and by day, and the rest of the hadith is the same.

**Arabic:** ‏"‏ وَالْمَلاَئِكَةُ يَتَعَاقَبُونَ فِيكُمْ ‏"‏ ‏.‏ بِمِثْلِ حَدِيثِ أَبِي الزِّنَادِ ‏.‏

---

## Rank 9

### Mixedbread &nbsp;&nbsp; `bulugh 1438` &nbsp; score: 0.7976

Abu Hurairah (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Look at those who are lower than you (financially) but do not look at those who are higher than you, lest you belittle the favors Allah conferred upon you.” Agreed upon.

### English OpenAI &nbsp;&nbsp; `bulugh 1514` &nbsp; score: 0.6772

Ibn ’Umar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “He who imitates any people (in their actions) is considered to be one of them.” Related by Abu Dawud and Ibn Hibban graded it as Sahih.

### Arabic OpenAI &nbsp;&nbsp; `ahmad 1398` &nbsp; score: 0.6329 · clusters: [70, 64]

It was narrated from Moosa bin Talhah, from his father, that The Prophet (ﷺ) said: “Let one of you put something in front of him the height of the back of a saddle, then pray.`

**Arabic:** يَجْعَلُ أَحَدُكُمْ بَيْنَ يَدَيْهِ مِثْلَ مُؤْخِرَةِ الرَّحْلِ ثُمَّ يُصَلِّي‏.‏

---

## Rank 10

### Mixedbread &nbsp;&nbsp; `forty 3` &nbsp; score: 0.7974

A Muslim is a mirror of the Muslim.

**Arabic:** عَنْ أَبِي عَبْدِ الرَّحْمَنِ عَبْدِ اللَّهِ بْنِ عُمَرَ بْنِ الْخَطَّابِ رَضِيَ اللَّهُ عَنْهُمَا قَالَ: سَمِعْت رَسُولَ اللَّهِ صلى الله عليه و سلم يَقُولُ: " بُنِيَ الْإِسْلَامُ عَلَى خَمْسٍ: شَهَادَةِ أَنْ لَا إلَهَ إلَّا اللَّهُ وَأَنَّ مُحَمَّدًا رَسُولُ اللَّهِ، وَإِقَامِ الصَّلَاةِ، وَإِيتَاءِ الزَّكَاةِ، وَحَجِّ الْبَيْتِ، وَصَوْمِ رَمَضَانَ". [رَوَاهُ الْبُخَارِيُّ] ، [وَمُسْلِمٌ] .

### English OpenAI &nbsp;&nbsp; `tirmidhi 2513` &nbsp; score: 0.6771

Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indeed that is more worthy(so that you will) not belittle Allah's favors upon you."

**Arabic:** صلى الله عليه وسلم ‏"‏ انْظُرُوا إِلَى مَنْ هُوَ أَسْفَلَ مِنْكُمْ وَلاَ تَنْظُرُوا إِلَى مَنْ هُوَ فَوْقَكُمْ فَإِنَّهُ أَجْدَرُ أَنْ لاَ تَزْدَرُوا نِعْمَةَ اللَّهِ عَلَيْكُمْ ‏"‏ ‏.‏ هَذَا حَدِيثٌ صَحِيحٌ ‏.‏

### Arabic OpenAI &nbsp;&nbsp; `ibnmajah 161` &nbsp; score: 0.6326 · clusters: [70, 64]

It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Do not revile my Companions, for by The One in Whose Hand is my soul! If any one of you were to spend the equivalent of Mount Uhud in gold, it would not equal a Mudd spent by anyone of them, nor even half a Mudd."

**Arabic:** ـ صلى الله عليه وسلم ـ ‏"‏ لاَ تَسُبُّوا أَصْحَابِي فَوَالَّذِي نَفْسِي بِيَدِهِ لَوْ أَنَّ أَحَدَكُمْ أَنْفَقَ مِثْلَ أُحُدٍ ذَهَبًا مَا أَدْرَكَ مُدَّ أَحَدِهِمْ وَلاَ نَصِيفَهُ ‏"‏ ‏.‏

---


# Summary — Top-3 per Query

## "aisha"

| Rank | Mixedbread | English OpenAI | Arabic OpenAI |
|---|---|---|---|
| **1** | `shamail 173` Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him pea | `bukhari 275` Narrated Um Ruman: Aisha's mother, When `Aisha was accused, she fell down Uncons | `bukhari 4752` Narrated Ibn Abi Mulaika: I heard `Aisha reciting: "When you invented a lie (and |
| **2** | `bukhari 2046` Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Pro | `abudawud 2909` Narrated Ibn 'Umar: 'Aishah, mother of believers (ra), intended to buy a slave-g | `muslim 1452 c` Ahadith like this is transmitted by 'A'isha through another chain of narrators. |
| **3** | `abudawud 269` Narrated Aisha, Ummul Mu'minin: Khallas al-Hujari reported: Aisha said: I and th | `bukhari 842` Narrated Anas: Aisha had a thick curtain (having pictures on it) and she screene | `bukhari 2628` Narrated Aiman: I went to `Aisha and she was wearing a coarse dress costing five |

## "comparing yourself to others"

| Rank | Mixedbread | English OpenAI | Arabic OpenAI |
|---|---|---|---|
| **1** | `muslim 2963 a` Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When o | `adab 328` Ibn 'Abbas said, "When you want to mention your companion's faults, remember you | `ibnmajah 1977` It was narrated from Ibn 'Abbas that: the Prophet said: "The best of you is the  |
| **2** | `bukhari 6490` Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person | `muslim 7068` Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When o | `abudawud 879` ‘A’ishah said; one night I missed the Messenger of Allah (may peace be upon him) |
| **3** | `forty 18` The felicitous person takes lessons from (the actions of) others. | `riyadussalihin 466` Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) | `nasai 169` It was narrated from Abu Hurairah that 'Aishah said: "I noticed the Prophet (PBU |

---
*Generated by `tests/focused_comparison.py`*