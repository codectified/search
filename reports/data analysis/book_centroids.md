# Book-Level Centroids

_415 books with 2+ hadiths | centroid = mean of all hadith vectors in that book_

**Cohesion** = average cosine similarity of hadiths to their book centroid. 
High cohesion = tight, focused book. Low = diverse topics.

---

## Cross-Collection Centroid Similarity

| | **abudawud** | **adab** | **ahmad** | **bukhari** | **bulugh** | **forty** | **hisn** | **ibnmajah** | **mishkat** | **muslim** | **nasai** | **riyadussal** | **shamail** | **tirmidhi** | **virtues** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **abudawud** | 1.000 | 0.961 | 0.976 | 0.985 | 0.982 | 0.951 | 0.915 | 0.987 | 0.970 | 0.978 | 0.970 | 0.963 | 0.956 | 0.991 | 0.948 |
| **adab** | 0.961 | 1.000 | 0.965 | 0.959 | 0.956 | 0.959 | 0.900 | 0.962 | 0.953 | 0.970 | 0.956 | 0.962 | 0.971 | 0.966 | 0.924 |
| **ahmad** | 0.976 | 0.965 | 1.000 | 0.973 | 0.974 | 0.949 | 0.906 | 0.984 | 0.968 | 0.974 | 0.966 | 0.967 | 0.960 | 0.980 | 0.956 |
| **bukhari** | 0.985 | 0.959 | 0.973 | 1.000 | 0.974 | 0.945 | 0.910 | 0.975 | 0.963 | 0.972 | 0.962 | 0.961 | 0.953 | 0.980 | 0.944 |
| **bulugh** | 0.982 | 0.956 | 0.974 | 0.974 | 1.000 | 0.952 | 0.917 | 0.981 | 0.974 | 0.977 | 0.968 | 0.965 | 0.953 | 0.986 | 0.957 |
| **forty** | 0.951 | 0.959 | 0.949 | 0.945 | 0.952 | 1.000 | 0.923 | 0.950 | 0.952 | 0.960 | 0.931 | 0.960 | 0.942 | 0.951 | 0.923 |
| **hisn** | 0.915 | 0.900 | 0.906 | 0.910 | 0.917 | 0.923 | 1.000 | 0.899 | 0.922 | 0.918 | 0.889 | 0.925 | 0.914 | 0.907 | 0.942 |
| **ibnmajah** | 0.987 | 0.962 | 0.984 | 0.975 | 0.981 | 0.950 | 0.899 | 1.000 | 0.969 | 0.974 | 0.973 | 0.959 | 0.956 | 0.991 | 0.944 |
| **mishkat** | 0.970 | 0.953 | 0.968 | 0.963 | 0.974 | 0.952 | 0.922 | 0.969 | 1.000 | 0.971 | 0.948 | 0.966 | 0.956 | 0.966 | 0.958 |
| **muslim** | 0.978 | 0.970 | 0.974 | 0.972 | 0.977 | 0.960 | 0.918 | 0.974 | 0.971 | 1.000 | 0.963 | 0.977 | 0.965 | 0.978 | 0.954 |
| **nasai** | 0.970 | 0.956 | 0.966 | 0.962 | 0.968 | 0.931 | 0.889 | 0.973 | 0.948 | 0.963 | 1.000 | 0.958 | 0.951 | 0.978 | 0.940 |
| **riyadussalihin** | 0.963 | 0.962 | 0.967 | 0.961 | 0.965 | 0.960 | 0.925 | 0.959 | 0.966 | 0.977 | 0.958 | 1.000 | 0.964 | 0.964 | 0.958 |
| **shamail** | 0.956 | 0.971 | 0.960 | 0.953 | 0.953 | 0.942 | 0.914 | 0.956 | 0.956 | 0.965 | 0.951 | 0.964 | 1.000 | 0.955 | 0.949 |
| **tirmidhi** | 0.991 | 0.966 | 0.980 | 0.980 | 0.986 | 0.951 | 0.907 | 0.991 | 0.966 | 0.978 | 0.978 | 0.964 | 0.955 | 1.000 | 0.949 |
| **virtues** | 0.948 | 0.924 | 0.956 | 0.944 | 0.957 | 0.923 | 0.942 | 0.944 | 0.958 | 0.954 | 0.940 | 0.958 | 0.949 | 0.949 | 1.000 |

---

## Books by Collection

Sorted by cohesion descending within each collection.

### abudawud (42 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Wills (Kitab Al-Wasaya) | 18 | 0.904 |
| Prayer (Kitab Al-Salat): Prostration while reciting the Qur'an | 15 | 0.8971 |
| The Book Of The Prayer For Rain (Kitab al-Istisqa') | 37 | 0.8872 |
| Clothing (Kitab Al-Libas) | 11 | 0.8811 |
| Prayer (Kitab Al-Salat): Detailed Injunctions about Ramadan | 30 | 0.8803 |
| Battles (Kitab Al-Malahim) | 13 | 0.8778 |
| Prayer (Kitab Al-Salat): Detailed Rules of Law about the Prayer during Journey | 52 | 0.8694 |
| Prayer (Kitab Al-Salat): Voluntary Prayers | 121 | 0.8689 |
| Dialects and Readings of the Qur'an (Kitab Al-Huruf Wa Al-Qira'at) | 43 | 0.8672 |
| The Rites of Hajj (Kitab Al-Manasik Wa'l-Hajj) | 20 | 0.867 |
| Shares of Inheritance (Kitab Al-Fara'id) | 23 | 0.8664 |
| Tribute, Spoils, and Rulership (Kitab Al-Kharaj, Wal-Fai' Wal-Imarah) | 43 | 0.8663 |
| Game (Kitab Al-Said) | 56 | 0.865 |
| Trials and Fierce Battles (Kitab Al-Fitan Wa Al-Malahim) | 26 | 0.8618 |
| Commercial Transactions (Kitab Al-Buyu) | 84 | 0.8591 |
| Jihad (Kitab Al-Jihad) | 164 | 0.8576 |
| Foods (Kitab Al-At'imah) | 67 | 0.8572 |
| Types of Blood-Wit (Kitab Al-Diyat) | 143 | 0.8536 |
| Signet-Rings (Kitab Al-Khatam) | 55 | 0.8529 |
| Divorce (Kitab Al-Talaq) | 129 | 0.8518 |
| Purification (Kitab Al-Taharah) | 390 | 0.8506 |
| Hot Baths (Kitab Al-Hammam) | 40 | 0.8498 |
| Medicine (Kitab Al-Tibb) | 119 | 0.8491 |
| The Promised Deliverer (Kitab Al-Mahdi) | 39 | 0.8488 |
| Model Behavior of the Prophet (Kitab Al-Sunnah) | 102 | 0.8485 |
| Drinks (Kitab Al-Ashribah) | 28 | 0.8481 |
| Prayer (Kitab Al-Salat): Detailed Injunctions about Witr | 140 | 0.8479 |
| Fasting (Kitab Al-Siyam) | 138 | 0.8475 |
| The Office of the Judge (Kitab Al-Aqdiyah) | 155 | 0.8445 |
| Divination and Omens (Kitab Al-Kahanah Wa Al-Tatayyur) | 49 | 0.8443 |
| Knowledge (Kitab Al-Ilm) | 70 | 0.8441 |
| Prayer (Kitab Al-Salat) | 771 | 0.8437 |
| The Book of Lost and Found Items | 145 | 0.8433 |
| Wages (Kitab Al-Ijarah) | 90 | 0.8431 |
| The Book of Manumission of Slaves | 22 | 0.842 |
| Funerals (Kitab Al-Jana'iz) | 161 | 0.8417 |
| Oaths and Vows (Kitab Al-Aiman Wa Al-Nudhur) | 153 | 0.8401 |
| Sacrifice (Kitab Al-Dahaya) | 311 | 0.8397 |
| Combing the Hair (Kitab Al-Tarajjul) | 139 | 0.8362 |
| Marriage (Kitab Al-Nikah) | 325 | 0.8357 |
| Prescribed Punishments (Kitab Al-Hudud) | 60 | 0.8355 |
| General Behavior (Kitab Al-Adab) | 177 | 0.83 |

#### Representative hadiths per book

**Wills (Kitab Al-Wasaya)** (cohesion: 0.904)
- #2857 [0.9553] Narrated Abdullah ibn Amr ibn al-'As: </p>      There was a bedouin called AbuTha'labah. He said: Messenger of Allah, I have trained dogs, so tell me your opinion about (eating) th
- #2847 [0.9502] Narrated 'Abi b. Hatim: I asked the Prophet (saws) ,and said: I set off my trained dogs, and they catch (something) for me: may I eat (it)? He said: When you set off trained dogs a
- #2849 [0.941] Narrated 'Adi b. Hatim: The Prophet (saws) as saying: When you shoot your arrow and mention Allah's name, and you find it (the game) after a day, and you do not find it in water, a

**Prayer (Kitab Al-Salat): Prostration while reciting the Qur'an** (cohesion: 0.8971)
- #1413 [0.9285] Narrated Abdullah ibn Umar: </p>      The Messenger of Allah (saws) used to recite the Qur'an to us. When he came upon the verse containing prostration, he would utter the takbir (
- #1412 [0.928] Narrated Ibn 'Umar: The Messenger of Allah (saws) would recite to us a surah (according to the version of Ibn Numair) outside the prayer (the agreed version goes), then he would pr
- #1410 [0.9243] Narrated Sa'id al-Khudri: </p>      The Messenger of Allah (saws) recited surah Sad on the pulpit. When he reached the place of prostration (in the surah), he descended and prostra

**The Book Of The Prayer For Rain (Kitab al-Istisqa')** (cohesion: 0.8872)
- #1189 [0.9439] Narrated Ibn 'Abbas: An eclipse of the sun took place.  the Messenger of Allah (may peace be upon him) prayed along with the people.  He stood up for a long time nearly equal to th
- #1178 [0.9419] Narrated Jabir b. Abd Allah: There was an eclipse of the sun in the time of the Messenger of Allah (may peace be upon him) had died.  The people began to to say that there was an e
- #1177 [0.9378] Narrated A'ishah (May Allah be pleased with her): There was an eclipse of the sun in the time of the Prophet (may peace be upon him).  The Prophet stood for a long time, accompanie

**Clothing (Kitab Al-Libas)** (cohesion: 0.8811)
- #4012 [0.911] Narrated Ya'la: </p>      The Messenger of Allah (saws) saw a man washing in a public place without a lower garment. So he mounted the pulpit, praised and extolled Allah and said: 
- #4018 [0.9075] Narrated AbuSa'id al-Khudri: </p>      The Prophet (saws) said: A man should not look at the private parts of another man, and a woman should not look at the private parts of anoth
- #4019 [0.8998] Narrated AbuHurayrah: </p>      The Prophet (saws) said: A man should not lie with another man and a woman should not lie with another woman without covering their private parts ex

**Prayer (Kitab Al-Salat): Detailed Injunctions about Ramadan** (cohesion: 0.8803)
- #1382 [0.9151] Narrated Abu Sa’id Al Khudri : The Messenger of Allah (saws) used to spend the middle ten days of Ramadan in retirement and devotion (i'tikaf) in the mosque. One year he had retire
- #1389 [0.9111] Narrated 'Abd Allah b. 'Amr: The Messenger of Allah (saws) said to me: Keep fast for three days of month, and finish the recitation of the Qur'an in one month. I and he differed am
- #1375 [0.901] Narrated AbuDharr: </p>      We fasted with the Messenger of Allah (saws) during Ramadan, but he did not make us get up at night for prayer at any time during the month till seven 

**Battles (Kitab Al-Malahim)** (cohesion: 0.8778)
- #4282 [0.9173] Narrated Abdullah ibn Mas'ud: </p>      The Prophet (saws) said: If only one day of this world remained. Allah would lengthen that day (according to the version of Za'idah), till H
- #4279 [0.8948] Narrated Jabir ibn Samurah: </p>      The Prophet (saws) said: The religion will continue to be established till there are twelve caliphs over you, and the whole community will agr
- #4286 [0.8913] Narrated Umm Salamah, Ummul Mu'minin: </p>      The Prophet (saws) said: Disagreement will occur at the death of a caliph and a man of the people of Medina will come flying forth t

**Prayer (Kitab Al-Salat): Detailed Rules of Law about the Prayer during Journey** (cohesion: 0.8694)
- #1212 [0.9231] Narrated Abdullah ibn Waqid: </p>      The mu'adhdhin of Ibn Umar said: prayer (i.e. the time of prayer has come). He said: Go ahead. He then alighted before the disappearance. He 
- #1244 [0.9207] Narrated Abdullah ibn Mas'ud: </p>      The Messenger of Allah (saws) led us in prayer in the time of danger. They (the people) stood in two rows. One row was behind the Messenger 
- #1223 [0.9157] Narrated Hafs b. 'Asim: I accompanied Ibn 'Umar on the way (on a journey). He led us in two rak'ah's of (the noon) prayer. Then he proceeded and saw some people standing. He asked:

**Prayer (Kitab Al-Salat): Voluntary Prayers** (cohesion: 0.8689)
- #1336 [0.9365] Narrated 'Aishah: Between the time when the Messenger of Allah (saws) finished the night prayer till the dawn broke, he used to pray eleven rak'ahs, uttering the salutation at the 
- #1352 [0.9347] Narrated Aisha, Ummul Mu'minin: </p>      Sa'd ibn Hisham said: I came to Medina and called upon Aisha, and said to her: Tell me about the prayer of the Messenger of Allah (saws). 
- #1338 [0.9342] Narrated 'Aishah: The Messenger of Allah (saws) used to pray thirteen rak'ahs during the night, observing a witr out of that with five, he did not sit during the five except the la

**Dialects and Readings of the Qur'an (Kitab Al-Huruf Wa Al-Qira'at)** (cohesion: 0.8672)
- #3935 [0.926] Qatadah narrated with his chain of narrators: The Prophet (saws) said: If a man emancipates a slave shared by him with another man, his emancipation rests with him (who emancipated
- #3942 [0.9233] The tradition mentioned above has also been narrated by Ibn 'Umar from the Prophet (saws). The narrator Ayyub said: I do not know whether the following words are part of the tradit
- #3938 [0.9184] Abu Hurairah reported the Prophet (saws) as saying: If anyone emancipates his share in a slave, he is to be completely emancipated by his money if he has money. But if he has no mo

**The Rites of Hajj (Kitab Al-Manasik Wa'l-Hajj)** (cohesion: 0.867)
- #1707 [0.9303] The aforesaid tradition has also been transmitted by Zaid bin Khalid al-Juhani through a different chain of narrators. This version has: The Messenger of Allah (SWAS) was asked abo
- #1710 [0.9145] Narrated Abdullah ibn Amr ibn al-'As: </p>      The Messenger of Allah (saws) was asked about the hanging fruit. He replied: If a needy person takes some and does not take a supply
- #1712 [0.913] The aforesaid tradition has also been transmitted by ‘Amr bin Shu’aib through a different chain of narrators.  This version has: He said about the stray sheep: You, your brother or

**Shares of Inheritance (Kitab Al-Fara'id)** (cohesion: 0.8664)
- #2864 [0.9124] Narrated 'Amir b. Sa'd: On the authority of his father (Sa'd b. Abi Waqqas): When he (Sa'd) fell ill at Mecca (according to the version of Ibn Abi Kkalaf) - then the agreed version
- #2882 [0.9072] Narrated Ibn 'Abbas: A man said: Messenger of Allah, my mother has died ; will it benefit her if I give sadaqah on her behalf ? He said: Yes. He said: I have a garden, and I call y
- #2867 [0.8908] Narrated AbuHurayrah: </p>      The Prophet (saws) said: A man or a woman acts in obedience to Allah for sixty years, then when they are about to die they cause injury by their wil

**Tribute, Spoils, and Rulership (Kitab Al-Kharaj, Wal-Fai' Wal-Imarah)** (cohesion: 0.8663)
- #2905 [0.9212] Narrated Abdullah ibn Abbas: </p>      A man died leaving no heir but a slave whom he had emancipated. The Messenger of Allah (saws) asked: Has he any heir? They replied: No, excep
- #2902 [0.9162] Narrated Aisha, Ummul Mu'minin: </p>      A client of the Prophet (saws) died and left some property, but he left no child or relative. The Messenger of Allah (saws) said: Give wha
- #2901 [0.9161] Narrated Al-Miqdam: </p>      I heard the Messenger of Allah (saws) say: I am the heirs of Him who has none, freeing him from his liabilities, and inheriting what he possesses. A m

**Game (Kitab Al-Said)** (cohesion: 0.865)
- #2800 [0.9205] Narrated Al-Bara' bin 'Azib: The Messenger of Allah (saws) delivered a sermon to us on the day of sacrifice after the prayer. He said: If anyone prays like our prayer, and sacrific
- #2801 [0.9126] Narrated Al-Bara' ibn Azib: </p>      A maternal uncle of mine called AbuBurdah sacrificed before the prayer (for 'Id). The Messenger of Allah (saws) said: Your goat is meant for f
- #2830 [0.9111] Narrated Nubayshah: </p>      A man called the Messenger of Allah (saws): We used to sacrifice Atirah in pre-Islamic days during Rajab; so what do you command us? He said: Sacrific

**Trials and Fierce Battles (Kitab Al-Fitan Wa Al-Malahim)** (cohesion: 0.8618)
- #4218 [0.9237] Narrated Ibn 'Umar:  The Messenger of Allah (saws) took a signet-ring of gold, and put the stone next the palm of his hand. He engraved on it "Muhammad, the Messenger of Allah". Th
- #4227 [0.9192] Narrated Abdullah ibn Umar: </p>      The Prophet (saws) used to wear the signet-ring on his left hand, and put its stone next the palm of his hand. </p>   Abu Dawud said: Ibn Isha
- #4221 [0.919] Anas b. Malik said that he saw a silver signet-ring on the hand of the Prophet (saws) only for a day. The people then fashioned and wore (rings). The Prophet (saws) then threw it a

**Commercial Transactions (Kitab Al-Buyu)** (cohesion: 0.8591)
- #3243 [0.9186] Narrated Abdullah ibn Mas'ud: </p>      The Messenger of Allah (saws) said: He who swears an oath in which he tells a lie to take the property of a Muslim by unfair means, will mee
- #3274 [0.9034] Narrated Abdullah ibn Amr ibn al-'As: </p>      The Messenger of Allah (saws)  said: An oath or a vow about something over which a human being has no control, and to disobey Allah,
- #3301 [0.903] Narrated Anas b. Malik :  The Messenger of Allah (saws) saw a man that he was supported between his sons. He asked about him, and (the people) said: He has taken a vow to walk (on 

**Jihad (Kitab Al-Jihad)** (cohesion: 0.8576)
- #2365 [0.9225] Narrated A Companion of the Prophet: </p>      AbuBakr ibn AbdurRahman reported on the authority of a Companion of the Prophet (saws): I saw the Prophet (saws) commanding the peopl
- #2427 [0.9197] Narrated 'Abd Allah b. 'Amr b. al-'As: The Messenger of Allah (saws) met me and said: Have I not been informed that you told: I shall stand at prayer all the night, and I shall fas
- #2457 [0.915] Narrated Aisha, Ummul Mu'minin: </p>      Some food was presented to me and Hafsah. We were fasting, but broke our fast. Then the Messenger of Allah (saws) entered upon us. We said

**Foods (Kitab Al-At'imah)** (cohesion: 0.8572)
- #3696 [0.9174] Ibn ‘Abbas said : The deputation of ‘Abd al-Qais asked (the prophet):From which(vessels)should we drink ? He (the prophet) replied: Do not drink from the pumpkins, vessels smeared 
- #3734 [0.9075] Jabir said: We were with Prophet (may peace be upon him) and he asked for something to drink. A man from the company  asked: Should we not give you nabidh (drink made from dates) t
- #3695 [0.907] A man of the deputation of 'Abd al-Qais who came to the Prophet (saws) said - the narrator 'Awf thinks that his name was Qais bin al-Nu'man: The Prophet (saws) said: Do not drink f

**Types of Blood-Wit (Kitab Al-Diyat)** (cohesion: 0.8536)
- #4445 [0.9142] Abu Hurairah and Zaid b. Khalid al-Juhani said: Two men brought a dispute before the Messenger of Allah (saws). One of them said: Pronounce judgement between us in accordance with 
- #4410 [0.9127] Narrated Jabir ibn Abdullah: </p>      A thief was brought to the Prophet (saws).  He said: Kill him.  The people said: He has committed theft, Messenger of Allah!  Then he said: C
- #4437 [0.9089] Narrated Sahl ibn Sa'd: </p>      A man came to the Prophet (saws) and confessed before him that he had committed fornication with a woman whom he named. The Messenger of Allah (sa

**Signet-Rings (Kitab Al-Khatam)** (cohesion: 0.8529)
- #4163 [0.9058] Narrated AbuHurayrah: </p>      The Prophet (saws) said: He who has hair should honour it. </p>
- #4190 [0.9038] Narrated Wa'il  ibn Hujr: </p>      I came to the Prophet (saws) and I had long hair. When the Messenger of Allah (saws) saw me, he said: Evil, evil! He said: I then returned and c
- #4182 [0.8874] Narrated Anas ibn Malik: </p>      A man came to the Messenger of Allah (saws) and he had the mark of yellowness (of saffron). The Prophet (peace be upon him rarely mentioned a thi

**Divorce (Kitab Al-Talaq)** (cohesion: 0.8518)
- #2117 [0.9164] Narrated Uqbah ibn Amir: </p>      The Prophet (saws) said to a man: Would you like me to marry you to so-and-so?   </p>     He said: Yes.  He also said to the woman: Would you lik
- #2092 [0.9097] Abu Hurairah reported the Prophet(saws) as saying “ A woman who has been previously married should not be married until her permission is asked nor should a virgin be married witho
- #2106 [0.9011] AbulAjfa' as-Sulami said: Umar (Allah be pleased with him) delivered a speech to us and said: Do not go to extremes in giving women their dower, for if it represented honour in thi

**Purification (Kitab Al-Taharah)** (cohesion: 0.8506)
- #126 [0.9254] Narrated Ar-Rubayyi' daughter of Mu'awwidh ibn Afra': </p>      The Messenger of Allah (saws) used to come to us. He once said: Pour ablution water on me. She then described how th
- #68 [0.919] Narrated Abdullah ibn Abbas: </p>      One of the wives of the Prophet (saws) took a bath from a large bowl. The Prophet (saws) wanted to perform ablution or take from the water le
- #150 [0.9186] Al-Mughirah b. Shu’bah said: The Messenger of Allah (saws) performed ablution and wiped his forelock and turban. Another version says : The Messenger of Allah (saws) wiped his sock

**Hot Baths (Kitab Al-Hammam)** (cohesion: 0.8498)
- #4001 [0.9021] Narrated Umm Salamah, Ummul Mu'minin: </p>      The Messenger of Allah (saws) used to recite: "In the name of Allah, the Cherisher and Sustainer of the worlds; most Gracious, most 
- #3997 [0.9003] Narrated Abu Qilabah:  A man whom the Prophet (saws) made the following verse read informed me, or he was informed by a man whom a man made the following verse read through a man w
- #3979 [0.8863] Narrated AbuSa'id al-Khudri: </p>      The Prophet (saws) read the verse mentioned above, "min du'f." </p>

**Medicine (Kitab Al-Tibb)** (cohesion: 0.8491)
- #3764 [0.9232] Narrated Wahshi ibn Harb: </p>      The Companions of the Prophet (saws) said: Messenger of Allah (saws) we eat but we are not satisfied. He said: Perhaps you eat separately. They 
- #3800 [0.917] Narrated Abdullah ibn Abbas: </p>      The people of pre-Islamic times used to eat some things and leave others alone, considering them unclean. Then Allah sent His Prophet (saws) 
- #3799 [0.9137] Narrated Abdullah ibn Umar: </p>      Numaylah  said: I was with Ibn Umar. He was asked about eating hedgehog. He recited: "Say: I find not in the message received by me by inspira

**The Promised Deliverer (Kitab Al-Mahdi)** (cohesion: 0.8488)
- #4261 [0.9194] Narrated AbuDharr: </p>      The Messenger of Allah (saws) said to me: O AbuDharr.  I replied: At thy service and at thy pleasure, Messenger of Allah.  He then mentioned the tradit
- #4258 [0.9031] Narrated Abdullah ibn Mas'ud ; Khuraym ibn Fatik: </p>      The tradition mentioned above (No. 4243) has also been transmitted by Ibn Mas'ud through a different chain of narrators.
- #4277 [0.8969] Narrated Sa'id ibn Zayd: </p>      We were with the Prophet (saws). He mentioned civil strife (fitnah) and expressed its gravity. We or the people said: Messenger of Allah, if this

**Model Behavior of the Prophet (Kitab Al-Sunnah)** (cohesion: 0.8485)
- #4501 [0.9107] Narrated Wa'il (b. Hujr): A man brought an Abyssinian to the Prophet (saws) and said: This man has killed my nephew. He asked: How did you kill him? He replied: I struck his head w
- #4547 [0.9048] Narrated Abdullah ibn Amr: </p>      (Musaddad's version has): The Messenger of Allah (saws) made a speech on the day of the conquest of Mecca, and said: Allah is Most Great, three
- #4510 [0.9043] Narrated Ibn Shihab: </p>      Jabir ibn Abdullah used to say that a Jewess from the inhabitants of Khaybar poisoned a roasted sheep and presented it to the Messenger of Allah (saw

**Drinks (Kitab Al-Ashribah)** (cohesion: 0.8481)
- #3660 [0.9015] Narrated Zayd ibn Thabit: </p>      I heard the Messenger of Allah (saws) say: May Allah brighten a man who hears a tradition from us, gets it by heart and passes it on to others. 
- #3644 [0.8994] Narrated AbuNamlah al-Ansari: </p>      When he was sitting with the Messenger of Allah (saws) and a Jew was also with him, a funeral passed by him. He (the Jew) asked (Him): Muham
- #3646 [0.8952] Narrated Abdullah ibn Amr ibn al-'As: </p>      I used to write everything which I heard from the Messenger of Allah (saws). I intended (by it) to memorise it. The Quraysh prohibit

**Prayer (Kitab Al-Salat): Detailed Injunctions about Witr** (cohesion: 0.8479)
- #1481 [0.9142] Narrated Fudalah ibn Ubayd,: </p>      The Messenger of Allah (saws) heard a person supplicating during prayer. He did not mention the greatness of Allah, nor did he invoke blessin
- #1425 [0.9109] Narrated Al-Hasan ibn Ali: </p>      The Messenger of Allah (saws) taught me some words that I say during the witr. (The version of Ibn Jawwas has: I say them in the supplication o
- #1443 [0.8992] Narrated Abdullah ibn Abbas: </p>      The Messenger of Allah (saws) recited the supplication (Qunut) daily for a month at the noon, afternoon, sunset, night and morning prayers. W

**Fasting (Kitab Al-Siyam)** (cohesion: 0.8475)
- #2254 [0.9124] Ibn ‘Abbas said “Hilal bin Umayyah accused his wife in the presence of Prophet (saws) of having committed adultery with Sharik bin Sahma’”. The Prophet (saws) said “Produce evidenc
- #2290 [0.9124] ‘Ubaid Allah said “Marwan sent someone (Qabisah) to Fatimah and asked her (about  the case). She said that she was the wife of Abu Hafs. The Prophet (saws) appointed ‘Ali as govern
- #2214 [0.9123] Narrated Khuwaylah, daughter of Malik ibn Tha'labah: </p>      My husband, Aws ibn as-Samit, pronounced the words: You are like my mother. So I came to the Messenger of Allah (saws

**The Office of the Judge (Kitab Al-Aqdiyah)** (cohesion: 0.8445)
- #3510 [0.905] Narrated Aisha, Ummul Mu'minin: </p>      A man bought a slave, and he remained with him as long as Allah wished him to remain. He then found defect in him. He brought his dispute 
- #3470 [0.899] Narrated Jabir bin ‘Abdullah : The Messenger of Allah (saws) as saying: If you were to sell dried dates to your brother and they were smitten by blight, it will not be allowable fo
- #3501 [0.8981] Narrated Anas ibn Malik: </p>      During the time of the Messenger of Allah (saws) a man used to buy (goods), and he was weak in his intellect. His people came to the Prophet of A

**Divination and Omens (Kitab Al-Kahanah Wa Al-Tatayyur)** (cohesion: 0.8443)
- #3883 [0.9005] Narrated Abdullah ibn Mas'ud: </p>      Zaynab, the wife of Abdullah ibn Mas'ud, told that Abdullah said: I heard the Messenger of Allah (saws) saying: spells, charms and love-poti
- #3875 [0.8983] Narrated Sa'd: </p>      I suffered from an illness. The Messenger of Allah (saws) came to pay a visit to me. He put his hands between my nipples and I felt its coolness at my hear
- #3891 [0.8956] ‘Uthman b. Abl al-As said that he came to the Messenger of Allah (may peace be upon him). ‘Uthman said : I had a pain which was about to destroy me. So the Prophet (may peace be up

**Knowledge (Kitab Al-Ilm)** (cohesion: 0.8441)
- #3598 [0.8934] The tradition mentioned above has also been transmitted by Ibn 'Umar from the Prophet (saws) through different chain of narrators to the same effect. In this version he also said: 
- #3584 [0.8871] Umm Salamah said: Two men came to the Messenger of Allah (saws) who were disputing over their inheritance. They had no evidence except their claim. The Prophet (saws) then said in 
- #3582 [0.8814] Narrated Ali ibn AbuTalib: </p>      The Messenger of Allah (saws) sent me to the Yemen as judge, and I asked: Messenger of Allah, are you sending me when I am young and have no kn

**Prayer (Kitab Al-Salat)** (cohesion: 0.8437)
- #1034 [0.9215] Narrated Abdullah ibn Buhaynah: </p>      The Messenger of Allah (saws) led us in prayer praying two rak'ahs. When he stood up and did not sit (at the end of two rak'ahs) the peopl
- #1020 [0.9125] Narrated Abdullah ibn Mas'ud: </p>      The Messenger of Allah (saws) offered prayer. The version of the narrator Ibrahim goes: I do not know whether he increased or decreased (the
- #738 [0.9097] Narrated AbuHurayrah: </p>      When the Messenger of Allah (saws) uttered the takbir (Allah is most great) for prayer (in the beginning), he raised his hands opposite to his shoul

**The Book of Lost and Found Items** (cohesion: 0.8433)
- #1678 [0.9127] Narrated Umar ibn al-Khattab: </p>      The Messenger of Allah (saws) commanded us one day to give sadaqah. At that time I had some property. I said: Today I shall surpass AbuBakr 
- #1630 [0.9125] Narrated Ziyad ibn al-Harith as-Suda'i: </p>      I came to the Messenger of Allah (saws) and swore allegiance to him, and after telling a long story he said: Then a man came to hi
- #1583 [0.9094] Narrated Ubayy ibn Ka'b: </p>      The Messenger of Allah (saws) commissioned me as a collector of zakat. I visited a man. When he had collected his property of camels, I found tha

**Wages (Kitab Al-Ijarah)** (cohesion: 0.8431)
- #3404 [0.9045] Narrated Jabir b. 'Abd Allah : The Messenger of Allah (saws) forbade muhaqalah, muzabanah, mukhabarah, and mu'awanah. One of the two narrators from Hammad said the word mu'awamah, 
- #3398 [0.9018] Narrated Usaid b. Zuhair:  Rafi' b. Khadij came to us and said: The Messenger of Allah (saws) forbids you from a work which is beneficial to you ; and obedience to Allah and His Pr
- #3328 [0.9016] Narrated Abdullah ibn Abbas: </p>      A man seized his debtor who owed ten dinars to him. He said to him: I swear by Allah, I shall not leave you until you pay off (my debt) to me

**The Book of Manumission of Slaves** (cohesion: 0.842)
- #3921 [0.8938] Narrated Sa'd ibn Malik: </p>      The Prophet (saws) said: There is no hamah, no infection and no evil omen; if there is in anything an evil omen, it is a house, a horse, and a  w
- #3919 [0.8815] Narrated Urwah ibn Amir al-Qurashi: </p>      When taking omens was mentioned in the presence of the Prophet (saws), he said: The best type is the good omen, and it does not turn b
- #3922 [0.8805] It was narrated from 'Abdullah bin 'Umar that the Messenger of Allah (saws) said: "An omen is in a dwelling, a woman or a horse." </p>  Abu Dawud said: This tradition was read out 

**Funerals (Kitab Al-Jana'iz)** (cohesion: 0.8417)
- #2975 [0.904] Narrated Umar ibn al-Khattab: </p>      AbulBakhtari said: I heard from a man a tradition which I liked. I said to him: Write it down for me. So he brought it clearly written to me
- #2999 [0.8947] Narrated Yazid ibn Abdullah: </p>      We were at Mirbad. A man with dishevelled hair and holding a piece of red skin in his hand came.   </p>     We said: You appear to be a bedou
- #2980 [0.8925] Narrated Jubair b. Mu'tim: On the day of Khaibar the Messenger of Allah (saws) divided the portion to his relatives among the Banu Hashim and Banu 'Abd al-Muttalib, and omitted Ban

**Oaths and Vows (Kitab Al-Aiman Wa Al-Nudhur)** (cohesion: 0.8401)
- #3129 [0.9169] Narrated Ibn 'Umar:  The Messenger of Allah (saws) as saying: The dead is punished because of his family's weeping for him. When this was mentioned to 'Aishah, she said: Ibn 'Umar 
- #3148 [0.9131] Narrated Jabir b. 'Abd Allah : The Prophet (saws) made a speech one day and mentioned a man from among his Companions who died and was shrouded in a shroud of bad quality, and was 
- #3123 [0.913] Narrated Abdullah ibn Amr ibn al-'As: </p>      We buried a deceased person in the company of the Messenger of Allah (saws). When we had finished, the Messenger of Allah (saws) ret

**Sacrifice (Kitab Al-Dahaya)** (cohesion: 0.8397)
- #2737 [0.9007] Narrated Abdullah ibn Abbas: </p>      The Messenger of Allah (saws) said on the day of Badr: He who does such-and-such, will have such-and such. The young men came forward and the
- #2501 [0.8973] Narrated Sahl ibn al-Hanzaliyyah: </p>      On the day of Hunayn we travelled with the Messenger of Allah (saws) and we journeyed for a long time until the evening came. I attended
- #2717 [0.8972] Abu Qatadah said “We went out with the Apostle of Allaah(saws) in the year of Hunain. And when the armies met, the Muslims suffered a reverse. I saw one of the polytheists prevaili

**Combing the Hair (Kitab Al-Tarajjul)** (cohesion: 0.8362)
- #4052 [0.913] Narrated Aisha, Ummul Mu'minin: </p>      The Messenger of Allah (saws) once prayed wearing a garment having marks. He looked at its marks. When he saluted, he said: Take this garm
- #4020 [0.9082] Narrated AbuSa'id al-Khudri: </p>      When the Messenger of Allah (saws) put on a new garment he mentioned it by name, turban or shirt, and would then say: O Allah, praise be to T
- #4116 [0.9054] Narrated Dihyah ibn Khalifah al-Kalbi: </p>      The Messenger of Allah (saws) was brought some pieces of fine Egyptian linen and he gave me one and said: Divide it into two; cut o

**Marriage (Kitab Al-Nikah)** (cohesion: 0.8357)
- #1770 [0.9066] Narrated Abdullah ibn Abbas: </p>      Sa'id ibn Jubayr said: I said to Abdullah ibn Abbas: AbulAbbas, I am surprised to see the difference of opinion amongst the companions of the
- #1789 [0.9] Jabir bin Abdullah said The Apostle of Allaah(saws) and his companions raised their voices in talbiyah for Hajj. No one of them had brought the sacrificial animals with them except
- #1783 [0.8989] A’ishah said “We went out with the Messenger of Allah(saws) and we thought it nothing but a Hajj. When we came, we circumambulated the House (the Ka’bah). The Messenger of Allah(sa

**Prescribed Punishments (Kitab Al-Hudud)** (cohesion: 0.8355)
- #4342 [0.8871] Narrated Abdullah ibn Amr ibn al-'As: </p>      The Prophet (saws) said: How will you do when that time will come? Or he said: A time will soon come when the people are sifted and 
- #4321 [0.8799] Al-nawwas b. Sim’an al-Kilabi said: The Messenger of Allah (saws) mentioned the Dajjal (Antichrist)  saying: If he comes forth while I am among you I shall be the one who will disp
- #4329 [0.8784] Ibn ‘Umar said : The prophet (saws) passed by Ibn Sa’Id along with some of his companions. ‘Umar b. al-Kattab was among them. He was playing with boys near the fortress of Banu Mag

**General Behavior (Kitab Al-Adab)** (cohesion: 0.83)
- #4694 [0.9029] ‘Ali said: We attended a funeral at Baql’ al-Gharqad which was also attended by the Messenger of Allah (May peace be upon him). The Messenger of Allah (May peace be upon him) came 
- #4753 [0.8951] Narrated Al-Bara' ibn Azib: </p>      We went out with the Messenger of Allah (saws) accompanying the bier of a man of the Ansar. When we reached his grave, it was not yet dug. So 
- #4767 [0.8887] ‘Ali said: When I mention a tradition to you from the Messenger of Allah (May peace be upon him), it is dearer to me that I fall from the heaven than I lie on him. But when I talk 

### adab (50 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Mawlas (Clients of Manumission) | 2 | 0.9245 |
| Injustice | 8 | 0.904 |
| Looking after girls | 8 | 0.8998 |
| Mornings and evenings | 6 | 0.89 |
| Consultation | 4 | 0.8886 |
| Abandonment | 18 | 0.8799 |
| Ties of Kinship | 27 | 0.8778 |
| Compassion | 13 | 0.8766 |
| Supervision | 9 | 0.8749 |
| Praise | 11 | 0.8697 |
| Advising | 4 | 0.864 |
| Mercy | 13 | 0.8636 |
| Social Behaviour | 12 | 0.8601 |
| Guests and Spending | 15 | 0.8592 |
| Names | 31 | 0.8575 |
| Supplication | 135 | 0.8518 |
| Gatherings | 17 | 0.8518 |
| Gestures | 13 | 0.8509 |
| Visiting the Ill | 47 | 0.8504 |
| Cheerfulness Towards People | 18 | 0.8501 |
| Anger | 7 | 0.8495 |
| Disparaging | 23 | 0.8494 |
| Omens | 12 | 0.8487 |
| Visitation | 10 | 0.8449 |
| Parents | 46 | 0.8442 |
| Poetry | 19 | 0.8403 |
| Children's Death | 13 | 0.8389 |
| Generosity and Orphans | 14 | 0.8352 |
| Letters | 19 | 0.8332 |
| Cursing | 24 | 0.8309 |
| Sneezing and Yawning | 33 | 0.8286 |
| The People of the Book | 16 | 0.8274 |
| Looking after children | 17 | 0.8267 |
| Kunyas | 14 | 0.8264 |
| Neighbours | 28 | 0.8257 |
| Being a master | 56 | 0.8251 |
| Asking Permission | 50 | 0.8231 |
| Consequences | 19 | 0.8229 |
| Midday Naps | 6 | 0.8226 |
| Sitting and lying down | 24 | 0.8225 |
| Words | 13 | 0.822 |
| Behaviour with people | 22 | 0.8217 |
| Betting and similar pastimes | 23 | 0.8203 |
| General Behavior | 66 | 0.8172 |
| Children | 10 | 0.8154 |
| Extravagance in Building | 20 | 0.8091 |
| Sayings | 57 | 0.8048 |
| Greetings | 87 | 0.8048 |
| The Elderly | 9 | 0.7935 |
| Good Conduct | 17 | 0.7918 |

#### Representative hadiths per book

**Mawlas (Clients of Manumission)** (cohesion: 0.9245)
- #75 [0.9245] Rifa'a ibn Rafi' reported that the Prophet, may Allah bless him and grant him peace, said to 'Umar, "Gather your people [the Muhajirun] for me." He did so. When they reached the do
- #74 [0.9245] 'Abdu'r-Rahman ibn Habib said, "'Abdullah ibn 'Umar asked me, 'Which clan are you from?' I replied, 'From Taym of Tamim.' He asked, 'One of themselves or one of their mawlas?' 'One

**Injustice** (cohesion: 0.904)
- #487 [0.949] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "Beware of injustice. Injustice will appear as darkness on the Day of Rising. Beware of coarse
- #488 [0.9486] Jabir reported that the Prophet, may Allah bless him and grant him peace, said, "Beware of injustice. Injustice will appear as darkness on the Day of Rising. Fear avarice. It destr
- #483 [0.9441] Jabir ibn 'Abdullah reported that the Prophet, may Allah bless him and grant him peace, said, "Fear injustice. Injustice will appear as darkness on the Day of Rising. Fear avarice.

**Looking after girls** (cohesion: 0.8998)
- #78 [0.9447] Jabir ibn 'Abdullah reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Anyone who has three daughters and provides for them, clothes them and sho
- #77 [0.9236] Ibn 'Abbas reported that he heard the Messenger of Allah, may Allah bless him and grant him peace, say, "There is no Muslim who has two daughters and takes good care of them but th
- #76 [0.9179] 'Uqba ibn 'Amir reported that he heard the Messenger of Allah, may Allah bless him and grant him peace, say, "If someone has three daughters and is patient with them and clothes th

**Mornings and evenings** (cohesion: 0.89)
- #1202 [0.9385] Abu Hurayra reported that Abu Bakr said, "Messenger of Allah, teach me something that I can say morning and evening." The Prophet said, "O Allah, Knower of the Unseen and the Visib
- #1204 [0.9173] Abu Rashid al-Hubrani said, "I came to 'Abdullah ibn 'Umar and asked him to relate to us what he had heard from the Messenger of Allah, may Allah bless him and grant him peace. He 
- #1200 [0.9164] Ibn 'Umar said, "The Messenger of Allah, may Allah bless him and grant him peace, did not omit saying the following words in the morning and evening: 'O Allah, I ask you for well-b

**Consultation** (cohesion: 0.8886)
- #259 [0.9072] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "Anyone who attributes words to me which I did not say should take his seat in the Fire. Anyon
- #256 [0.8963] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, asked Abu'l-Haytham: "Do you have a servant?" "No," he replied. He said, "Come to us when we get som
- #258 [0.8755] Al-Hasan said, "People never seek advice without being guided to the best possibility available to them." Then he recited, "and manage their affairs by mutual consultation." (42:38

**Abandonment** (cohesion: 0.8799)
- #398 [0.9259] Anas ibn Malik reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Do not hate one another nor envy one another nor shun one another. Slaves of Al
- #406 [0.9209] Abu Ayyub al-Ansari reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "It is not lawful for a Muslim to refuse to speak to his (Muslim) brother f
- #399 [0.9149] Abu Ayyub, the Companion of the Messenger of Allah, may Allah bless him and grant him peace, said, "It is not lawful for anyone to cut himself off from his Muslim brother for more 

**Ties of Kinship** (cohesion: 0.8778)
- #65 [0.9238] Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Ties of kinship (rahim) is derived from the All-Merciful (ar-Rahman). They say. 'M
- #55 [0.9209] 'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Kinship (rahim) is derived from Allah. If anyone maintains ties of kinship Allah maintains ties w
- #52 [0.9208] Abu Hurayra said, "A man came to the Prophet, may Allah bless him and grant him peace, and said, 'Messenger of Allah! I have relatives with whom I maintain ties while they cut me o

**Compassion** (cohesion: 0.8766)
- #472 [0.9216] 'Abdullah ibn Mughaffal reported that the Prophet, may Allah bless him and grant him peace, said, "Allah is compassionate and loves compassion. He gives for compassion what He goes
- #466 [0.9157] Anas reported that the Prophet, may Allah bless him and grant him peace, said, "If there is roughness in anything it is bound to disgrace it. Allah is compassionate and loves compa
- #464 [0.9132] Abu'd-Darda' reported that the Prophet, may Allah bless him and grant him peace, said, "Whoever has been given his portion of compassion has been given his portion of good. Whoever

**Supervision** (cohesion: 0.8749)
- #216 [0.9204] Ibn 'Umar reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Anyone who seeks refuge in Allah will find refuge with Him. Anyone who asks from All
- #215 [0.8978] Jabir ibn 'Abdullah al-Ansari reported that the Prophet, may Allah bless him and grant him peace, said, "Whoever has a favour done for him should repay it. If he cannot find anythi
- #214 [0.8892] Ibn 'Umar reported that he heard the Messenger of Allah, may Allah bless him and grant him peace, say, "All of you are shepherds and each of you is responsible for his flock. A wom

**Praise** (cohesion: 0.8697)
- #340 [0.9169] 'Ata' ibn Abi Rabah reported that a man was praising another man in the presence of Ibn 'Umar. Ibn 'Umar began to throw dust towards his mouth. He said, "The Messenger of Allah, ma
- #333 [0.9157] Abu Bakr reported that a man was mentioned in the presence of the Prophet, may Allah bless him and grant him peace, and someone praised him. The Prophet, may Allah bless him and gr
- #334 [0.9049] Abu Musa reported that the Prophet, may Allah bless him and grant him peace, heard a man praise another man and he was using exaggeration in his praise of him. The Prophet, may All

**Advising** (cohesion: 0.864)
- #417 [0.8892] Ibn 'Abbas reported that the Prophet, may Allah bless him and grant him peace, said, "We do not give a bad example. The one who takes back his gift is like the dog who returns to h
- #418 [0.8852] Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "The believer is guileless and generous while the corrupt is a swindler and miserly
- #416 [0.8825] Ibn 'Umar saw a shepherd with some sheep in a bad place and saw a place which was better than it. He told him, "Woe to you, shepherd! Move them! I heard the Messenger of Allah, may

**Mercy** (cohesion: 0.8636)
- #377 [0.9197] Abu Hurayra said, "A man came to the Prophet, may Allah bless him and grant him peace, with a child which he began to embrace. The Prophet, may Allah bless him and grant him peace,
- #380 [0.9065] 'Abdullah ibn al-'As reported that the Prophet, may Allah bless him and grant him peace, said, "Show mercy and you will be shown mercy. Forgive and Allah will forgive you. Woe to t
- #382 [0.8933] 'Abdullah reported that the Prophet, may Allah bless him and grant him peace, stopped in a place and then someone took a bird's eggs and the bird began to beat its wings around the

**Social Behaviour** (cohesion: 0.8601)
- #386 [0.9029] 'Abdullah reported that the Prophet, may Allah bless him and grant him peace, said, "You must be truthful. Truthfulness leads to dutifulness and dutifulness leads to the Garden. A 
- #394 [0.8997] Ibn 'Abbas reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Do not dispute with your brother. Do not make fun of him. Do not make a promise to 
- #390 [0.8957] 'Abdullah said, "The Prophet, may Allah bless him and grant him peace, swore an oath like one of the oaths that people swear and a man of the Ansar said, 'By Allah, it is not an oa

**Guests and Spending** (cohesion: 0.8592)
- #743 [0.9006] Abu Shurayh al-Kabi al-Adawi (ra) has reported that the Messenger of Allah (saws) said, "He who believes in Allah and the last day should speak a good, decent conversation otherwis
- #740 [0.8992] Abu Hurayrah (ra) said that a man came to the Messenger of Allah (saws). He sent message to his homes that they should send him if they had anything (to entertain his guest). They 
- #741 [0.893] Abu Shurayh at Adawi (ra) said that his ears heard eyes observed that The Messenger of Allah (saws) was saying," he who believes in Allah and the last day should honour his neighbo

**Names** (cohesion: 0.8575)
- #814 [0.8918] Abu Wahb, a Companion, reported that the Prophet, may Allah bless him and grant him peace, said, "Name yourselves with the names of the Prophets. The names which Allah Almighty lov
- #836 [0.8891] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "Name yourselves with my name, but do not use my kunya; I am Abu'l-Qasim."
- #837 [0.8881] Anas ibn Malik said, "The Prophet, may Allah bless him and grant him peace, was in the market when a man said, 'Abu'l-Qasim!' The Prophet, may Allah bless him and grant him peace, 

**Supplication** (cohesion: 0.8518)
- #698 [0.9147] Ibn 'Abbas said, "The Prophet, may Allah bless him and grant him peace, used to make this supplication: 'O Allah, I ask You for pardon and good health in this world and the Next. O
- #665 [0.9128] Ibn 'Abbas said, "I heard the Prophet, may Allah bless him and grant him peace, making supplication with these words: 'O Allah, help me and do not help anyone against me. Devise fo
- #710 [0.9085] Abu Sa'id al-Khudri reported that the Prophet, may Allah bless him and grant him peace, said, "No Muslim makes supplication - unless he is someone who has cut off his relatives - b

**Gatherings** (cohesion: 0.8518)
- #1140 [0.8927] Ibn 'Umar reported that the Prophet, may Allah bless him and grant him peace, said, "None of you should make a man rise from his seat and then sit in it. Rather make room and sprea
- #1148 [0.892] Al-Harith ibn 'Amr as-Sahmi related, "I came to the Prophet, may Allah bless him and grant him peace, when he was at Mina or at 'Arafa. People crowded around him and some Bedouins 
- #1151 [0.8884] Abu Musa al-Ash'ari said, "The Messenger of Allah, may Allah bless him and grant him peace, went out one day to one of the walled gardens of Madina, and I went out after him. When 

**Gestures** (cohesion: 0.8509)
- #954 [0.8923] 'Abdullah ibn as-Samit said, "I questioned my close friend Abu Dharr who said, 'I brought some water for wudu' to the Prophet, may Allah bless him and grant him peace. He shook his
- #955 [0.8908] 'Ali reported that the Messenger of Allah, may Allah bless him and grant him peace, knocked at the door of 'Ali and Fatima, the daughter of the Prophet, may Allah bless him and gra
- #958 [0.883] It is related that 'Abdullah ibn 'Umar reported that 'Umar went with the Messenger of Allah, may Allah bless him and grant him peace, with a group to visit Ibn Sayyad. They found h

**Visiting the Ill** (cohesion: 0.8504)
- #526 [0.9172] Ibn 'Abbas reported that the Prophet, may Allah bless him and grant him peace, went to visit a bedouin who was ill. When the Prophet, may Allah bless him and grant him peace, visit
- #514 [0.9024] Ibn 'Abbas reported that the Messenger of Allah, may Allah bless him and grant him peace, went to visit a bedouin when he was ill and said, "Do not worry. It is a purification if A
- #525 [0.897] 'A'isha (ra) said, "When the Messenger of Allah, may Allah bless him and grant him peace, came to Madina, Abu Bakr (ra) and Bilal (ra) came down with a fever. I visited them and as

**Cheerfulness Towards People** (cohesion: 0.8501)
- #239 [0.9043] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "A believer is the mirror of his brother. A believer is the brother of another believer. He pr
- #248 [0.8987] Mu'awiya said, "I heard some words from the Prophet, may Allah bless him and grant him peace, by which Allah helped me." Jubayr ibn Nufayr said, "I heard him say that he heard the 
- #254 [0.8896] Abu Hurayra said, "The Prophet, may Allah bless him and grant him peace, went out to a group of his Companions who were laughing and talking. He said, 'By the One in whose hand my 

**Anger** (cohesion: 0.8495)
- #1317 [0.8827] Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "The person who is strong is not strong because he can knock people down. The perso
- #1319 [0.8707] Sulayman ibn Surad said, "Two men abused one another in the presence of the Prophet, may Allah bless him and grant him peace, and one of them began to get angry and his face got re
- #1320 [0.8703] Ibn 'Abbas said, "The Messenger of Allah, may Allah bless him and grant him peace, said, ' Teach and make it easy. Teach and make it easy.' three times. He went on, 'When you are a

**Disparaging** (cohesion: 0.8494)
- #440 [0.9098] 'Abdullah ibn 'Umar reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "When someone says to another, 'Unbeliever!' then one of them is an unbelie
- #432 [0.9056] Abu Dharr is reported as saying that he heard the Prophet, may Allah bless him and grant him peace, say, "If a man accuses another man of deviance or accuses him of disbelief, that
- #433 [0.9054] Abu Dharr states that he heard the Prophet, may Allah bless him and grant him peace, say, "A person who knowingly claims a father other than his own has disbelieved. A person who c

**Omens** (cohesion: 0.8487)
- #916 [0.8863] 'Abdullah ibn 'Umar reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Bad luck can be found in houses, women and horses."
- #909 [0.8852] 'Abdullah ibn Mas'ud reported that the Prophet, may Allah bless him and grant him peace, said, "Paying attention to the bad omen (tayyara) is association (shirk). It has nothing to
- #910 [0.8825] Abu Hurayra heard the Prophet, may Allah bless him and grant him peace, say, "Bad omens. The best of that is the good omen. They asked, "What is the good omen?" "A good word which 

**Visitation** (cohesion: 0.8449)
- #350 [0.9108] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "A man visited a brother of his in a village, so Allah put an angel in wait for him on the roa
- #349 [0.9] 'Abdullah ibn 'Umar said, "'Umar found a silk robe and brought it to the Prophet, may Allah bless him and grant him peace, and said, 'Buy this and wear it on Jumu'ah and when deleg
- #345 [0.8668] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "When a man visits his brothers, Allah tells him, 'You have been good and your evening will 

**Parents** (cohesion: 0.8442)
- #6 [0.9141] Abu Hurayra reported: "A man came to the Prophet of Allah, may Allah bless him and grant him peace, and asked, 'What do you command me to do?' He replied, 'Be dutiful towards your 
- #35 [0.8994] Abu Usayd said, "We were with the Messenger of Allah, may Allah bless him and grant him peace, when a man asked, 'Messenger of Allah, is there any act of dutifulness which I can do
- #27 [0.8875] 'Abdullah ibn 'Amr said that the Prophet, may Allah bless him and grant him peace, said, "Reviling one's parents is one of the great wrong actions." They asked, "How could he revil

**Poetry** (cohesion: 0.8403)
- #872 [0.9217] Ibn 'Abbas said that a man - or a bedouin - came to the Prophet, may Allah bless him and grant him peace, and spoke some eloquent words. The Prophet, may Allah bless him and grant 
- #865 [0.9083] 'Abdullah ibn 'Amr reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Poetry is in the same position as speech. The good of it is like good words
- #858 [0.9024] Ubayy ibn Ka'b mentioned that the Messenger of Allah, may Allah bless him and grant him peace, said, "There is some wisdom in poetry."

**Children's Death** (cohesion: 0.8389)
- #148 [0.912] Abu Hurayra reported, "A woman came to the Messenger of Allah, may Allah bless him and grant him peace, and said, 'Messenger of Allah! We cannot come to sit with you, so set aside 
- #146 [0.9071] Jabir ibn 'Abdullah said, "I heard the Messenger of Allah, may Allah bless him and grant him peace, say, 'If anyone has three of his children die young and resigns them to Allah, h
- #150 [0.8937] Al-Hasan reported that Sa'sa'a ibn Mu'awiya told him that he met Abu Dharr finding him alone without any relatives and asked, "Don't you have any children, Abu Dharr?" He said, "I 

**Generosity and Orphans** (cohesion: 0.8352)
- #137 [0.9148] Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "The best house among the Muslims is the house in which orphans are well treated. T
- #133 [0.8953] Umm Sa'id bint Murra al-Fihri related from her father that the Prophet, may Allah bless him and grant him peace, said, "I and the guardian of an orphan will be in the Garden like t
- #138 [0.8832] Dawud said, "Be like a merciful father towards the orphan. Know that you will reap as you sow. How ugly poverty is after wealth! More than that: how ugly is misguidance after guida

**Letters** (cohesion: 0.8332)
- #1124 [0.8964] Nafi' said, "Ibn 'Umar needed something from Mu'awiya and he wanted to write to him. People said, 'Begin with his name.' They kept on at him until he wrote, 'In the Name of Allah, 
- #1122 [0.8747] It is reported that Zayd ibn Thabit wrote this letter: "In the Name of Allah, the All-Merciful, Most Merciful. To the slave of Allah, Mu'awiya, the Amir al-Mu'minin, from Zayd ibn 
- #1119 [0.874] 'Abdullah ibn 'Umar wrote to 'Abdu'l-Malik ibn Marwan in order to pledge him his allegiance. He wrote to him, "In the Name of Allah, the All-Merciful, Most Merciful. To 'Abdu'l-Mal

**Cursing** (cohesion: 0.8309)
- #317 [0.8899] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "The true person must not be a curser."
- #320 [0.8747] Samura reported that the Prophet, may Allah bless him and grant him peace, said, "Do not curse one another with the curse of Allah, not the anger of Allah nor with the Fire."
- #330 [0.8702] Ad-Dahhak said, "It was about us (the Banu Salima) that these words were revealed, 'Do not find fault with one another' (49:11)" He went on to say, "The Messenger of Allah, may All

**Sneezing and Yawning** (cohesion: 0.8286)
- #927 [0.9445] Abu Salih reported that the Prophet, may Allah bless him and grant him peace, said, "When one of you sneezes, he should say, 'Praise be to Allah.' When he says, 'Praise be to Allah
- #921 [0.9393] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "When one of you sneezes, he should say, 'Praise be to Allah,' and his brother or companion sh
- #932 [0.9234] Abu Hurayra said, "Two men sat in the presence of the Prophet may Allah bless him and grant him peace, and one of them was from a noble family than the other. The nobler of the two

**The People of the Book** (cohesion: 0.8274)
- #1106 [0.9078] 'Abdullah ibn 'Umar said that the Messenger of Allah, may Allah bless him and grant him peace, said, "When one of the Jews greets you and says, 'Poison be upon you (as-samu 'alayku
- #1110 [0.8839] Jabir said, "Some of the Jews greeted the Prophet, may Allah bless him and grant him peace, by saying, 'Poison be upon you (as-Samu 'alaykum)' and the Prophet replied, 'And on you.
- #1102 [0.8775] Abu Basra al-Ghifari reported that the Prophet, may Allah bless him and grant him peace, said, "I will ride to the Jews tomorrow. Do not give them the greeting first. If they greet

**Looking after children** (cohesion: 0.8267)
- #98 [0.9078] 'A'isha said, "Some bedouins came to the Prophet, may Allah bless him and grant him peace. One of their men said to him, 'Messenger of Allah, do you kiss children? By Allah, we do 
- #90 [0.8943] 'A'isha said, "A bedouin came to the Prophet, may Allah bless him and grant him peace, and asked, "Do you kiss your children? We do not kiss them.' The Prophet, may Allah bless him
- #93 [0.8898] An-Nu'man ibn Bashir said that his father had carried him to the Messenger of Allah, may Allah bless him and grant him peace. He said, 'Messenger of Allah, I testify to you that I 

**Kunyas** (cohesion: 0.8264)
- #850 [0.8964] 'A'isha said, "I went to the Prophet, may Allah bless him and grant him peace, and said, 'Messenger of Allah, you give your wives kunyas, so give me a kunya.' He said, 'Take the ku
- #851 [0.878] 'A'isha said, "Prophet of Allah, will you not give me a kunya?" He said, "Use the kunya of your son," i.e. 'Abdullah ibn az-Zubayr. She was given the kunya Umm 'Abdullah.
- #844 [0.8766] Abu Hurayra said, "The Messenger of Allah, may Allah bless him and grant him peace, forbade for someone to have both his name and his kunya. He said, 'I am Abu'l-Qasim. Allah gives

**Neighbours** (cohesion: 0.8257)
- #124 [0.8973] Abu Hurayra said, "A man said, 'Messenger of Allah, I have a neighbour who does me harm.' He said, 'Go and take your things out into the road.' He took his things out into the road
- #117 [0.8941] Abu Hurayra said, "Part of the supplication of the Prophet, may Allah bless him and grant him peace, was, "Oh Allah, I seek refuge with you from an evil neighbour in the Eternal Wo
- #102 [0.8916] Abu Shurayh al-Khuza'i reported that the Prophet, may Allah bless him and grant him peace, said, "Anyone who believes in Allah and the Last Day should be good to his neighbours. An

**Being a master** (cohesion: 0.8251)
- #192 [0.9136] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "The slave has his food and clothing. Do not burden a slave with work which he is incapable of
- #163 [0.91] Abu Umama said, "The Prophet, may Allah bless him and grant him peace, came with two slaves and gave one of them to 'Ali and said, 'Do not beat him. I have forbidden beating the pe
- #190 [0.9052] Sallam ibn 'Amr reported from one of the Companions of the Prophet, may Allah bless him and grant him peace, said, "Your slaves are your brothers, so treat him well. Ask for their 

**Asking Permission** (cohesion: 0.8231)
- #1078 [0.8947] 'Abdullah ibn Busr, the Companion of the Prophet, may Allah bless him and grant him peace, said that when the Prophet, may Allah bless him and grant him peace, came to a door when 
- #1076 [0.8887] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "A man's messenger to another man is his permission to enter."
- #1084 [0.8859] Rib'i ibn Hirash reported that a man of the Banu 'Amir came to the Prophet, may Allah bless him and grant him peace, and said, "Can I come in?" The Prophet, may Allah bless him and

**Consequences** (cohesion: 0.8229)
- #897 [0.8889] Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "My friends on the Day of Rising will be those with taqwa, even if one lineage is c
- #902 [0.875] Abu Hurayra said, "I heard the Prophet, may Allah bless him and grant him peace, say, 'While a shepherd was tending to his sheep, a wolf came and snatched one of the sheep. The she
- #893 [0.8735] Ibn 'Abbas told Shahr (ibn Hawshab), "While the Prophet, may Allah bless him and grant him peace, was sitting in the courtyard of his house in Makka, 'Uthman ibn Maz'un passed by a

**Midday Naps** (cohesion: 0.8226)
- #1239 [0.9023] As-Sa'ib ibn Yazid said, "'Umar, may Allah be pleased with him, used to pass by us in the middle of the day - or near to it - and say, 'Get up and take a midday nap. Any time spent
- #1238 [0.8719] 'Umar said, "Sometimes some of the men of Quraysh sat at the door of Ibn Mas'ud. When the shadows shifted from west to east, he said, 'Get up, Any time spent here after this is for
- #1243 [0.8196] Maymun (ibn Mahran) said, "I asked Nafi', 'Did Ibn 'Umar ever invite people to a banquet?' He said, 'A camel of his once broke something and so we sacrificed it. Then Ibn 'Umar sai

**Sitting and lying down** (cohesion: 0.8225)
- #1185 [0.8836] 'Abdullah ibn Zayd ibn 'Asim al-Mazini said, "I saw him." Malik ibn Isma'il asked Ibn 'Uyayna (who had transmitted this to him), "The Prophet, may Allah bless him and grant him pea
- #1197 [0.8655] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, used to say when he left his house, "In the Name of Allah. Reliance is on Allah. There is no power n
- #1178 [0.864] Qayla related, "I saw the Prophet, may Allah bless him and grant him peace, sitting squatting. When I saw the Prophet, may Allah bless him and grant him peace, humble in his form o

**Words** (cohesion: 0.822)
- #882 [0.8794] 'A'isha, the wife of the Prophet, may Allah bless him and grant him peace, said, "People asked the Prophet, may Allah bless him and grant him peace, about soothsayers. He told them
- #875 [0.8726] Ibn 'Umar said, "Two men came from the east as orators in the time of the Messenger of Allah, may Allah bless him and grant him peace. They stood up, spoke and then sat down. Thabi
- #878 [0.8547] 'A'isha said, "The Prophet, may Allah bless him and grant him peace, was sleepless one night and said, 'Would that a man of righteous action among my Companions would come and guar

**Behaviour with people** (cohesion: 0.8217)
- #1166 [0.8839] Sa'id al-Maqburi said, "I passed by Ibn 'Umar who had a man with him with whom he was conversing. I went to them, and he struck me on the chest and said, 'When you find two men con
- #1170 [0.8812] Ibn 'Umar reported something similar from the Prophet, may Allah bless him and grant him peace. He stated, "We said, 'If there are four?' He said, 'Then it will not harm him.'"
- #1163 [0.8753] Anas ibn Malik said, "I came to the Prophet, may Allah bless him and grant him peace, while he was on a seat with a bad woven on it. He had a pillow under his head made of skin stu

**Betting and similar pastimes** (cohesion: 0.8203)
- #1275 [0.8876] Kulthum ibn Jabir said, "Ibn az-Zubayr addressed us and said, 'People of Makka, I have heard that there are men of Quraysh who play a game called backgammon. It is done with the le
- #1271 [0.8784] Burayda reported that the Prophet, may Allah bless him and grant him peace, said, "Someone who plays backgammon is like a person who puts his hand in the meat and blood of a pig."
- #1272 [0.8779] Abu Musa reported that the Prophet, may Allah bless him and grant him peace, said, "Anyone who plays backgammon has rebelled against Allah and His Messenger."

**General Behavior** (cohesion: 0.8172)
- #548 [0.8954] 'Abdullah ibn 'Amr said, "We were sitting with the Messenger of Allah, may Allah bless him and grant him peace, when a bedouin man wearing a robe with a border approached him until
- #552 [0.8853] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said that Allah Almighty said, "Might is My wrapper and pride is My cloak. I will punish anyone who 
- #584 [0.8804] Ashajj 'Abdu'l-Qays said, "The Prophet, may Allah bless him and grant him peace, said to me, 'You have two qualities which Allah loves.' I asked, 'What are they, may Allah bless hi

**Children** (cohesion: 0.8154)
- #363 [0.8686] 'Amr ibn Shu'ayb reported from his grandfather that the Messenger of Allah, may Allah bless him and grant him peace, said, "Anyone who does not show mercy to our children nor ackno
- #362 [0.8666] Abu Hurayra said, "When the Messenger of Allah, may Allah bless him and grant him peace, was brought new dates, he said, 'O Allah! Bless us in our city and in our mudd and sa', ble
- #364 [0.8623] Ya'la ibn Murra said, "We went out with the Prophet, may Allah bless him and grant him peace, and we were invited to eat. Husayn was playing in the road and the Prophet, may Allah 

**Extravagance in Building** (cohesion: 0.8091)
- #456 [0.88] 'Abdullah ibn 'Amr said, "The Prophet, may Allah bless him and grant him peace, went by while I was repairing a hut I owned. He said, 'What is this?' I replied, 'I am mending my hu
- #459 [0.8624] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "The Final Hour will not come until people build houses which are like coloured garments."  Ib
- #442 [0.8599] Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Allah is pleased with you about three things and He is angry with you about three 

**Sayings** (cohesion: 0.8048)
- #755 [0.8833] 'A'isha said, "A man asked for permission to come in to see the Prophet, may Allah bless him and grant him peace, and the Prophet remarked, 'He is a bad brother of his tribe.' When
- #760 [0.8752] 'Abdullah ibn Burayda reported from his father that the Messenger of Allah, may Allah bless him and grant him peace, said, "Do not call a hypocrite 'master'. He is not your master 
- #794 [0.8731] Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "When one of you wishes for something, he should look to what he desires. He does n

**Greetings** (cohesion: 0.8048)
- #986 [0.915] Abu Hurayra reported that a man passed by the Messenger of Allah, may Allah bless him and grant him peace, while hew as in an assembly and said, "Peace be upon you." "Ten good deed
- #1007 [0.9117] Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "When one of you comes to a gathering, he should give the greeting. If he leaves, h
- #992 [0.9064] 'Abdu'r-Rahman ibn Shibl said that he heard the Prophet, may Allah bless him and grant him peace, said, "The person riding should greet the person on foot. The person on foot shoul

**The Elderly** (cohesion: 0.7935)
- #354 [0.8648] 'Abdullah ibn 'Amr ibn al-'As reported that it reached him that the Prophet, may Allah bless him and grant him peace, said, "Anyone who does not show mercy to our children nor ackn
- #353 [0.8519] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "Anyone who does not show mercy to our children nor acknowledge the right of our old people is
- #360 [0.8408] Ibn 'Umar said, "The Messenger of Allah, may Allah bless him and grant him peace, said, 'Tell me which tree is like the Muslim? It gives fruits at all times by the permission of it

**Good Conduct** (cohesion: 0.7918)
- #229 [0.8673] Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "A man came across a thorn in the road and said, 'I will remove this thorn so that it does not
- #231 [0.8639] 'Abdullah ibn al-Khatami reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Every act of kindness is sadaqa."
- #225 [0.8638] Abu Musa reported that the Prophet, may Allah bless him and grant him peace, said, "Every Muslim must give sadaqa." They said, "And if he does not find anything (to give)?" He repl

### ahmad (7 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Musnad of Abu Muhammad Talhah bin 'Ubaidullah | 22 | 0.8822 |
| The Musnad of az-Zubair bin al-'Awwam | 31 | 0.8754 |
| The Hadeeth of Saqeefah | 8 | 0.8745 |
| Musnad Abu Bakr as-Siddiq (ra) | 77 | 0.874 |
| Musnad 'Ali Ibn Abi Talib | 778 | 0.8551 |
| Musnad Uthman ibn Affan | 152 | 0.8504 |
| Musnad `Umar b. al-Khattab (ra) | 291 | 0.8486 |

#### Representative hadiths per book

**Musnad of Abu Muhammad Talhah bin 'Ubaidullah** (cohesion: 0.8822)
- #1383 [0.9209] It was narrated from Mu`adh bin `Abdur-Rahman bin `Uthman at-Taimi that his father ‘ Abdur-Rahman bin `Uthman said: “We were with Talhah bin ‘Ubaidullah (رضي الله عنه) and we were 
- #1392 [0.9152] It was narrated from Mu`adh bin `Abdur-Rahman bin ‘Uthman at-Taimi that his father said: We were with Talhah bin `Ubaidullah and we were in ihram. A bird was given to him as a gift
- #1403 [0.9076] It was narrated from Talhah bin `Ubaidullah that Two men came to the Messenger of Allah (ﷺ) and they both became Muslim, but one of them strove harder in worship than his companion

**The Musnad of az-Zubair bin al-'Awwam** (cohesion: 0.8754)
- #1423 [0.9175] It was narrated that `Abdullah bin az-Zubair (رضي الله عنه) said: On the day of al-Ahzab, `Umar bin Abi Salamah and I were put with the women. I looked out and saw az-Zubair on his
- #1416 [0.9062] It was narrated that az-Zubair (رضي الله عنه) said: We came from Liyyah with the Messenger of Allah (ﷺ) and when we reached Sidrah, the Messenger of Allah (ﷺ) stood at one side of 
- #1437 [0.906] It was narrated that ‘Ali or az-Zubair said: The Messenger of Allah (ﷺ) used to address us and remind us of the annals of Allah, until we could see that on his face (because of ala

**The Hadeeth of Saqeefah** (cohesion: 0.8745)
- #396 [0.9174] It was narrated that Ibn `Umar (رضي الله عنه) said: The Messenger of Allah        (ﷺ)said: “Whoever buys foodstuff should not sell it until he takes possession of all of it.”
- #395 [0.9041] It was narrated that Ibn `Umar (رضي الله عنه) said:  We used to buy and sell foodstuff at the time of the Messenger of Allah (ﷺ), and he would send someone to tell us to transfer t
- #397 [0.9012] It was narrated from Ibn `Umar (رضي الله عنه) that the Messenger of Allah         (ﷺ) said: “If a person frees his share of a slave, and has enough Money to pay the full price of t

**Musnad Abu Bakr as-Siddiq (ra)** (cohesion: 0.874)
- #2 [0.9338] It was narrated that ‘Ali said: If I heard a hadeeth from the Messenger of Allah (ﷺ) Allah benefitted me as He willed thereby. If someone else told me something from him I would as
- #5 [0.9288] It was narrated that Awsat said: Abu Bakr addressed us and said: The Messenger of Allah (ﷺ) stood last year where I am standing. Abu Bakr wept, then he said: Ask Allah to keep you 
- #29 [0.9213] It was narrated that Qais said: Abu Bakr stood up and praised and glorified Allah, then he said:O people, you recite this verse: `O you who believe! Take care of your ownselves...`

**Musnad 'Ali Ibn Abi Talib** (cohesion: 0.8551)
- #1371 [0.9144] It was narrated that ‘Ali (رضي الله عنه) said: The Messenger of Allah (ﷺ) gathered - or the Messenger of Allah (ﷺ) called - Banu ‘Abdul-Muttalib, among whom were some people all of
- #987 [0.9115] It was narrated that ‘Ali (رضي الله عنه) said: If you are told a hadeeth from the Messenger of Allah (ﷺ), then think of the Messenger of Allah (ﷺ) in the best, most pious and most 
- #1080, 1081 [0.9071] It was narrated that `Ali bin Abi Talib (رضي الله عنه) said: If I tell you a hadeeth from the Messenger of Allah (ﷺ), then think of him in the best manner, the most guided manner a

**Musnad Uthman ibn Affan** (cohesion: 0.8504)
- #463 [0.9107] It was narrated that `Abdullah bin az-Zubair said: `Uthman bin `Affan (رضي الله عنه) said, speaking from his minbar:  I am going to tell you a hadeeth that I heard from the Messeng
- #439 [0.9094] It was narrated that Salim bin Abul-Ja`d said, `Uthman (رضي الله عنه) called some of the Companions of the Messenger of Allah (ﷺ), among whom was ‘Ammar bin Yasir, and said: I am g
- #400 [0.9077] It was narrated from Hisham bin `Urwah: My father told me that Humran told him: `Uthman (رضي الله عنه) did wudoo’ in al-Balat (a paved area in Madinah) then he said, i shall tell y

**Musnad `Umar b. al-Khattab (ra)** (cohesion: 0.8486)
- #121 [0.9098] It was narrated from 'Uqbah bin ‘Amir that he went out with the Messenger of Allah ﷺ on the campaign to Tabook, and one day the Messenger of Allah ﷺ sat talking to his companions a
- #265 [0.9075] It was narrated that ‘Umar bin al-Khattab said: When Abu Bakr and I were with him, the Messenger of Allah (ﷺ) passed by `Abdullah bin Mas`ood, when he was reciting [in prayer]. He 
- #376 [0.9039] I: was narrated that ‘Umar bin al-Khattab (رضي الله عنه) said: The Messenger of Allah (ﷺ) said: “Whoever shades the head of a warrior, Allah will shade him on the Day of Resurrecti

### bukhari (89 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Conditions | 6 | 0.9606 |
| Representation, Authorization, Business by Proxy | 3 | 0.9404 |
| Witr Prayer | 24 | 0.9167 |
| Virtues of the Night of Qadr | 11 | 0.9087 |
| Fasting | 6 | 0.9069 |
| Invoking Allah for Rain (Istisqaa) | 13 | 0.9056 |
| Forgetfulness in Prayer | 14 | 0.8932 |
| Hiring | 3 | 0.8887 |
| Oppressions | 24 | 0.8847 |
| Shuf'a | 16 | 0.8822 |
| Retiring to a Mosque for Remembrance of Allah (I'tikaf) | 21 | 0.8815 |
| Good Manners and Form (Al-Adab) | 30 | 0.8803 |
| The Two Festivals (Eids) | 34 | 0.8782 |
| Rubbing hands and feet with dust (Tayammum) | 15 | 0.8776 |
| Fear Prayer | 15 | 0.877 |
| Witnesses | 8 | 0.8753 |
| Mortgaging | 15 | 0.8749 |
| `Umrah (Minor pilgrimage) | 15 | 0.874 |
| Bathing (Ghusl) | 45 | 0.8729 |
| Menstrual Periods | 37 | 0.8725 |
| Invocations | 37 | 0.8706 |
| Accepting Information Given by a Truthful Person | 61 | 0.8697 |
| Hajj (Pilgrimage) | 30 | 0.8685 |
| Dress | 69 | 0.8685 |
| Revelation | 7 | 0.8676 |
| Friday Prayer | 37 | 0.8668 |
| Agriculture | 9 | 0.8666 |
| Virtues of Madinah | 112 | 0.8665 |
| Drinks | 22 | 0.8661 |
| Apostates | 15 | 0.8657 |
| Afflictions and the End of the World | 21 | 0.8649 |
| Shortening the Prayers (At-Taqseer) | 9 | 0.8646 |
| Eclipses | 39 | 0.8643 |
| Peacemaking | 41 | 0.8633 |
| Kafalah | 25 | 0.8606 |
| Khusoomaat | 28 | 0.8596 |
| Virtues of Prayer at Masjid Makkah and Madinah | 27 | 0.8586 |
| Distribution of Water | 18 | 0.8575 |
| Prostration During Recital of Qur'an | 63 | 0.8573 |
| Penalty of Hunting while on Pilgrimage | 24 | 0.8562 |
| Partnership | 15 | 0.8562 |
| (Statements made under) Coercion | 47 | 0.8556 |
| Prophets | 44 | 0.8555 |
| Obligatory Charity Tax (Zakat) | 112 | 0.8547 |
| Patients | 95 | 0.8547 |
| Laws of Inheritance (Al-Faraa'id) | 106 | 0.8545 |
| Wills and Testaments (Wasaayaa) | 68 | 0.8542 |
| Sacrifice on Occasion of Birth (`Aqiqa) | 87 | 0.8537 |
| Tricks | 81 | 0.8535 |
| Ablutions (Wudu') | 113 | 0.8531 |
| Beginning of Creation | 24 | 0.8501 |
| Gifts | 22 | 0.8494 |
| Jizyah and Mawaada'ah | 20 | 0.8494 |
| Times of the Prayers | 266 | 0.8491 |
| Lost Things Picked up by Someone (Luqatah) | 31 | 0.8485 |
| Oneness, Uniqueness of Allah (Tawheed) | 84 | 0.8478 |
| Merits of the Helpers in Madinah (Ansaar) | 30 | 0.8476 |
| Judgments (Ahkaam) | 13 | 0.8475 |
| Asking Permission | 65 | 0.8473 |
| Belief | 51 | 0.8468 |
| Funerals (Al-Janaa'iz) | 148 | 0.8455 |
| Knowledge | 76 | 0.8445 |
| Blood Money (Ad-Diyat) | 84 | 0.8442 |
| Pilgrims Prevented from Completing the Pilgrimage | 46 | 0.844 |
| Fighting for the Cause of Allah (Jihaad) | 50 | 0.844 |
| Call to Prayers (Adhaan) | 65 | 0.844 |
| Wedlock, Marriage (Nikaah) | 120 | 0.8435 |
| Hunting, Slaughtering | 183 | 0.8428 |
| Wishes | 28 | 0.8422 |
| Companions of the Prophet | 63 | 0.842 |
| Medicine | 9 | 0.841 |
| Oaths and Vows | 250 | 0.8403 |
| Interpretation of Dreams | 55 | 0.8402 |
| Al-Adha Festival Sacrifice (Adaahi) | 95 | 0.8392 |
| Sales and Trade | 184 | 0.8389 |
| To make the Heart Tender (Ar-Riqaq) | 93 | 0.8389 |
| Prayers (Salat) | 167 | 0.8379 |
| Prophetic Commentary on the Qur'an (Tafseer of the Prophet (pbuh)) | 154 | 0.8371 |
| Holding Fast to the Qur'an and Sunnah | 83 | 0.8363 |
| Makaatib | 43 | 0.8361 |
| Virtues and Merits of the Prophet (pbuh) and his Companions | 294 | 0.8345 |
| Expiation for Unfulfilled Oaths | 75 | 0.8339 |
| Supporting the Family | 488 | 0.8333 |
| Food, Meals | 499 | 0.8318 |
| Limits and Punishments set by Allah (Hudood) | 181 | 0.8317 |
| Virtues of the Qur'an | 151 | 0.8313 |
| Divine Will (Al-Qadar) | 185 | 0.8299 |
| Military Expeditions led by the Prophet (pbuh) (Al-Maghaazi) | 131 | 0.8266 |
| Divorce | 172 | 0.8245 |

#### Representative hadiths per book

**Conditions** (cohesion: 0.9606)
- #2563 [0.9826] Narrated Aisha:  Barirah came (to `Aisha) and said, "I have made a contract of emancipation with my masters for nine  Uqiyas (of gold) to be paid in yearly installments. Therefo
- #2560 [0.963] Narrated 'Aishah (ra) that Barira came to seek her help writing of emancipation and she had to pay five Uqiya (of gold) by five yearly installments. 'Aishah said to her, "Do you th
- #2561 [0.9627] Narrated `Urwa:  That `Aisha told him that Barirah came to seek her help in her writing of emancipation (for a certain  sum) and that time she had not paid anything of it. `Aish

**Representation, Authorization, Business by Proxy** (cohesion: 0.9404)
- #2287 [0.9717] Narrated Abu Huraira:  The Prophet said, "Procrastination (delay) in paying debts by a wealthy man is injustice. So, if your  debt is transferred from your debtor to a rich debtor,
- #2288 [0.9702] Narrated Abu Huraira:  The Prophet said, "Procrastination (delay) in paying debts by a wealthy person is injustice. So, if your  debt is transferred from your debtor to a rich debt
- #2289 [0.8793] Narrated Salama bin Al-Akwa:        Once, while we were sitting in the company of Prophet, a dead man was       brought. The Prophet was requested to lead the funeral prayer for th

**Witr Prayer** (cohesion: 0.9167)
- #1052 [0.9603] Narrated `Abdullah bin `Abbas:  The sun eclipsed in the lifetime of the Prophet (p.b.u.h) . Allah's Apostle offered the eclipse prayer  and stood for a long period equal to the per
- #1058 [0.9591] Narrated `Aisha:  In the lifetime of the Prophet the sun eclipsed and the Prophet (p.b.u.h) stood up to offer the prayer  with the people and recited a long recitation, then he per
- #1044 [0.958] Narrated `Aisha:  In the lifetime of Allah's Apostle (p.b.u.h) the sun eclipsed, so he led the people in prayer, and stood  up and performed a long Qiyam, then bowed for a long whi

**Virtues of the Night of Qadr** (cohesion: 0.9087)
- #2020 [0.9494] Narrated `Aisha:  Allah's Apostle used to practice I`tikaf in the last ten nights of Ramadan and used to say, "Look for  the Night of Qadr in the last ten nights of the month of Ra
- #2022 [0.9473] Narrated Ibn `Abbas:  Allah's Apostle said, "The Night of Qadr is in the last ten nights of the month (Ramadan), either on  the first nine or in the last (remaining) seven nights (
- #2017 [0.9459] Narrated `Aisha:  Allah's Apostle said, "Search for the Night of Qadr in the odd nights of the last ten days of Ramadan."

**Fasting** (cohesion: 0.9069)
- #2009 [0.9248] Narrated Abu Huraira:  Allah's Apostle said, "Whoever prayed at night the whole month of Ramadan out of sincere Faith and hoping for a reward from Allah, then all his previous sins
- #2013 [0.9226] Narrated Abu Salama bin `Abdur Rahman:  that he asked `Aisha "How was the prayer of Allah's Apostle in Ramadan?" She replied, "He did not  pray more than eleven rak`at in Ramadan o
- #2008 [0.9221] Narrated Abu Huraira:  I heard Allah's Apostle saying regarding Ramadan, "Whoever prayed at night in it (the month of  Ramadan) out of sincere Faith and hoping for a reward from Al

**Invoking Allah for Rain (Istisqaa)** (cohesion: 0.9056)
- #1079 [0.9447] Narrated Ibn `Umar.:  Whenever the Prophet recited the Sura which contained the prostration of recitation he used to  prostrate and then, we, too, would prostrate and some of us di
- #1076 [0.9414] Narrated Ibn `Umar:  When the Prophet recited Surat As-Sajda and we were with him, he would prostrate and we also  would prostrate with him and some of us (because of the heavy rus
- #1075 [0.939] Narrated Ibn `Umar:  When the Prophet recited a Sura that contained the prostration he would prostrate and we would do  the same and some of us (because of the heavy rush) could no

**Forgetfulness in Prayer** (cohesion: 0.8932)
- #1224 [0.9442] Narrated `Abdullah bin Buhaina:  Allah's Apostle once led us in a prayer and offered two rak`at and got up (for the third rak`a) without  sitting (after the second rak`a). The peop
- #1228 [0.9379] Narrated Abu Huraira.:  Once Allah's Apostle offered two rak`at and finished his prayer. So Dhul-Yadain asked him, "Has the  prayer been reduced or have you forgotten?" Allah's Apo
- #1227 [0.9353] Narrated Abu Huraira:  The Prophet led us in the `Asr or the Zuhr prayer and finished it with Taslim. Dhul-Yadain said to  him, "O Allah's Apostle! Has the prayer been reduced?" Th

**Hiring** (cohesion: 0.8887)
- #2258 [0.8978] Narrated `Amr bin Ash-Sharid:  While I was standing with Sa`d bin Abi Waqqas, Al-Miswar bin Makhrama came and put his hand on  my shoulder. Meanwhile Abu Rafi`, the freed slave of 
- #2259 [0.8886] Narrated Aisha:  I said, "O Allah's Apostle! I have two neighbors and would like to know to which of them I should  give presents." He replied, "To the one whose door is nearer to 
- #2257 [0.8797] Narrated Jabir bin `Abdullah:  Allah's Apostle gave a verdict regarding Shuf'a in every undivided joint thing (property). But if the  limits are defined (or demarcated) or the ways

**Oppressions** (cohesion: 0.8847)
- #2390 [0.9429] Narrated Abu Huraira:  A man demanded his debts from Allah's Apostle in such a rude manner that the companions of the  Prophet intended to harm him, but the Prophet said, "Leave hi
- #2392 [0.9269] Narrated Abu Huraira:  A man came to the Prophet and demanded a camel (the Prophet owed him). Allah's Apostle told his  companions to give him (a camel). They said, "We do not find
- #2405, 2406 [0.9217] Narrated Jabir:  When `Abdullah (my father) died, he left behind children and debts. I asked the lenders to put down  some of his debt, but they refused, so I went to the Prophet t

**Shuf'a** (cohesion: 0.8822)
- #2239 [0.9344] Narrated Ibn `Abbas:  Allah's Apostle came to Medina and the people used to pay in advance the price of fruits to be  delivered within one or two years. (The sub-narrator is in dou
- #2253 [0.9299] Narrated Ibn `Abbas:  The Prophet came to Medina and the people used to pay in advance the prices of fruits to be delivered  within two to three years. The Prophet said (to them), 
- #2240 [0.9275] Narrated Ibn `Abbas:  The Prophet came to Medina and the people used to pay in advance the price of dates to be delivered  within two or three years. He said (to them), "Whoever pa

**Retiring to a Mosque for Remembrance of Allah (I'tikaf)** (cohesion: 0.8815)
- #2027 [0.9313] Narrated Abu Sa`id Al-Khudri:  Allah's Apostle used to practice I`tikaf in the middle ten days of Ramadan and once he stayed in  I`tikaf till the night of the twenty-first and it w
- #2033 [0.9291] Narrated `Amra:  Aisha said, "the Prophet used to practice I`tikaf in the last ten days of Ramadan and I used to pitch a  tent for him, and after offering the morning prayer, he us
- #2040 [0.925] Narrated Abu Sa`id:  We practiced I`tikaf with Allah's Apostle in the middle ten days (of Ramadan). In the morning of the  twentieth (of Ramadan) we shifted our baggage, but Allah'

**Good Manners and Form (Al-Adab)** (cohesion: 0.8803)
- #5560 [0.9435] Narrated Al-Bara':  I heard the Prophet delivering a sermon, and he said (on the Day of `Id-Allah. a), "The first thing we  will do on this day of ours is that we will offer the `I
- #5549 [0.9409] Narrated Anas bin Malik:  The Prophet said on the day of Nahr, "Whoever has slaughtered his sacrifice before the prayer, should  repeat it (slaughter another sacrifice)." A man got
- #5561 [0.9369] Narrated Anas:  The Prophet said, "Whoever slaughtered the sacrifice before the `Id prayer, should repeat it (slaughter  another one)." A man said "This is the day on which meat is

**The Two Festivals (Eids)** (cohesion: 0.8782)
- #1019 [0.9316] Narrated Anas bin Malik:  A man came to Allah's Apostle and said, "O Allah's Apostle! Livestock are destroyed and the roads  are cut off; so please invoke Allah." So Allah's Apostl
- #1013 [0.9313] Narrated Sharik bin `Abdullah bin Abi Namir:  I heard Anas bin Malik saying, "On a Friday a person entered the main Mosque through the gate  facing the pulpit while Allah's Apostle
- #1014 [0.9311] Narrated Sharik:  Anas bin Malik said, "A person entered the Mosque on a Friday through the gate facing the Daril-  Qada' and Allah's Apostle was standing delivering the Khutba (se

**Rubbing hands and feet with dust (Tayammum)** (cohesion: 0.8776)
- #338 [0.9442] Narrated `Abdur Rahman bin Abza [??]:  A man came to `Umar bin Al-Khattab and said, "I became Junub but no water was available."  `Ammar bin Yasir said to `Umar, "Do you remember t
- #347 [0.9333] Narrated Al-A`mash:  Shaqiq said, "While I was sitting with `Abdullah and Abu Musa Al-Ash`ari, the latter asked the  former, 'If a person becomes Junub and does not find water for 
- #346 [0.9134] Narrated Shaqiq bin Salama:  I was with `Abdullah and Abu Musa; the latter asked the former, "O Abu `Abdur-Rahman! What is  your opinion if somebody becomes Junub and no water is a

**Fear Prayer** (cohesion: 0.877)
- #992 [0.9231] Narrated Ibn `Abbas:  Once I passed the night in the house of Maimuna (his aunt). I slept across the bed while Allah's  Apostle and his wife slept length-wise. The Prophet slept ti
- #995 [0.9199] Narrated Anas bin Seereen:  I asked Ibn `Umar, "What is your opinion about the two rak`at before the Fajr (compulsory) prayer, as  to prolonging the recitation in them?" He said, "
- #990 [0.9112] Narrated Ibn `Umar:        Once a person asked Allah's Apostle (saws) about the night prayer. Allah's       Apostle (saws) replied, "The night prayer is offered as two Rak`at follo

**Witnesses** (cohesion: 0.8753)
- #2509 [0.9109] Narrated `Aisha:  The Prophet bought some foodstuff on credit for a limited period and mortgaged his armor for it.
- #2511 [0.9003] Narrated Abu Huraira:  The Prophet said, "One can ride the mortgaged animal because of what one spends on it, and one can  drink the milk of a milch animal as long as it is mortgag
- #2510 [0.887] Narrated Jabir bin `Abdullah:  Allah's Apostle said, "Who would kill Ka`b bin Al-Ashraf as he has harmed Allah and His Apostle ?"  Muhammad bin Maslama (got up and) said, "I will k

**Mortgaging** (cohesion: 0.8749)
- #2427 [0.9361] Narrated Zaid bin Khalid Al-Juhani:  A bedouin went to the Prophet and asked him about picking up a lost thing. The Prophet said, "Make  public announcement about it for one year. 
- #2436 [0.9323] Narrated Zaid bin Khalid Al-Juhani:  A man asked Allah's Apostle about the Luqata. He said, "Make public announcement of it for one  year, then remember the description of its cont
- #2429 [0.9317] Narrated Zaid bin Khalid:  A man came and asked Allah's Apostle about picking a lost thing. The Prophet said, "Remember the  description of its container and the string it is tied 

**`Umrah (Minor pilgrimage)** (cohesion: 0.874)
- #1817 [0.9229] Narrated `Abdur-Rahman bin Abu Layla:  (Reporting the speech of Ka`b bin Umra) Allah's Apostle saw him (i.e. Ka`b) while the lice were  falling on his face. He asked (him), "Have y
- #1814 [0.9166] Narrated `Abdur-Rahman bin Abu Layla:  Ka`b bin 'Ujra said that Allah's Apostle said to him (Ka`b), "Perhaps your lice have troubled you?"  Ka`b replied, "Yes! O Allah's Apostle." 
- #1815 [0.9131] Narrated Ka`b bin `Umra:  Allah's Apostle stood beside me at Al-Hudaibiya and the lice were falling from my head in great  number. He asked me, "Have your lice troubled you?" I rep

**Bathing (Ghusl)** (cohesion: 0.8729)
- #276 [0.9359] Narrated Maimuna:  I placed water for the bath of the Prophet and screened him with a garment. He poured water over his  hands and washed them. After that he poured water with his 
- #266 [0.9299] Narrated Maimuna bint Al-Harith:  I placed water for the bath of Allah's Apostle and put a screen. He poured water over his hands, and  washed them once or twice. (The sub-narrator
- #272, 273 [0.9257] Narrated Hisham bin `Urwa:  (on the authority of his father) `Aisha said, "Whenever Allah's Apostle took the bath of Janaba, he  cleaned his hands and performed ablution like that 

**Menstrual Periods** (cohesion: 0.8725)
- #322 [0.9228] Narrated Zainab bint Abi Salama:  Um-Salama said, "I got my menses while I was lying with the Prophet under a woolen sheet. So I  slipped away, took the clothes for menses and put 
- #306 [0.9196] Narrated `Aisha:  Fatima bint Abi Hubaish said to Allah's Apostle, "O Allah's Apostle! I do not become clean (from  bleeding). Shall I give up my prayers?" Allah's Apostle replied:
- #309 [0.9167] Narrated `Aisha:  Once one of the wives of the Prophet did I`tikaf along with him and she was getting bleeding in  between her periods. She used to see the blood (from her private 

**Invocations** (cohesion: 0.8706)
- #5660 [0.9364] Narrated `Abdullah bin Mas`ud:  I visited Allah's Apostle while he was suffering from a high fever. I touched him with my hand and  said, "O Allah's Apostle! You have a high fever.
- #5667 [0.9345] Narrated Ibn Mas`ud:  I visited the Prophet while he was having a high fever. I touched him an said, "You have a very high  fever" He said, "Yes, as much fever as two me of you may
- #5661 [0.9278] Narrated `Abdullah:  I visited the Prophet during his illness and touched him while he was having a fever. I said to him,  "You have a high fever; is it because you will get a doub

**Accepting Information Given by a Truthful Person** (cohesion: 0.8697)
- #7030, 7031 [0.9256] Narrated Ibn `Umar:  I was a young unmarried man during the lifetime of the Prophet. I used to sleep in the mosque.  Anyone who had a dream, would narrate it to the Prophet. I said
- #7028, 7029 [0.925] Narrated Ibn `Umar:  Men from the companions of Allah's Apostle used to see dreams during the lifetime of Allah's Apostle  and they used to narrate those dreams to Allah's Apostle.
- #7046 [0.9208] Narrated Ibn `Abbas:  A man came to Allah's Apostle and said, "I saw in a dream, a cloud having shade. Butter and honey  were dropping from it and I saw the people gathering it in 

**Hajj (Pilgrimage)** (cohesion: 0.8685)
- #1782 [0.9217] Narrated Ata:  I heard Ibn `Abbas saying, "Allah's Apostle asked an Ansari woman (Ibn `Abbas named her but `Ata'  forgot her name), 'What prevented you from performing Hajj with us
- #1788 [0.9169] Narrated `Aisha:  We set out assuming the Ihram for Hajj in the months of Hajj towards the sacred precincts of Hajj. We  dismounted at Sarif and the Prophet said to his companions,
- #1787 [0.9133] Narrated Al-Aswad:  That `Aisha said, "O Allah's Apostle! The people are returning after performing the two Nusuks (i.e.  Hajj and `Umra) but I am returning with one only?" He said

**Dress** (cohesion: 0.8685)
- #5496 [0.9308] Narrated Abu Tha`laba Al-Khushani:  I came to the Prophet and said, "O Allah's Apostle! We are living in the land of the people of the  Scripture, and we take our meals in their ut
- #5498 [0.9254] Narrated Rafi` bin Khadij:  We were with the Prophet in Dhul-Hulaifa and there the people were struck with severe hunger. Then  we got camels and sheep as war booty (and slaughtere
- #5478 [0.9245] Narrated Abu Tha`laba Al-Khushani:  I said, "O Allah's Prophet! We are living in a land ruled by the people of the Scripture; Can we take  our meals in their utensils? In that land

**Revelation** (cohesion: 0.8676)
- #4 [0.9029] Narrated Jabir bin 'Abdullah Al-Ansari (while talking about the period of pause in revelation) reporting the speech of the Prophet: "While I was walking, all of a sudden I heard a 
- #3 [0.8985] Narrated 'Aisha (the mother of the faithful believers): The commencement of the Divine Inspiration to Allah's Apostle was in the form of good dreams which came true like bright day
- #2 [0.8814] Narrated 'Aisha:        (the mother of the faithful believers) Al-Harith bin Hisham asked Allah's Apostle "O Allah's Apostle! How is the Divine Inspiration revealed to you?" All

**Friday Prayer** (cohesion: 0.8668)
- #976 [0.9123] Narrated Al-Bara':  The Prophet went towards Al-Baqi (the graveyard at Medina) on the day of Id-ul-Adha and offered a  two-rak`at prayer (of `Id-ul-Adha) and then faced us and said
- #975 [0.9099] Narrated Ibn `Abbas:  I (in my boyhood) went out with the Prophet on the day of `Id ul Fitr or Id-ul-Adha. The Prophet  prayed and then delivered the Khutba and then went towards t
- #983 [0.9098] Narrated Al-Bara' bin `Azib:  On the day of Nahr Allah's Apostle delivered the Khutba after the `Id prayer and said, "Anyone who  prayed like us and slaughtered the sacrifice like 

**Agriculture** (cohesion: 0.8666)
- #2298 [0.8998] Narrated Abu Huraira:  Whenever a dead man in debt was brought to Allah's Apostle he would ask, "Has he left anything to  repay his debt?" If he was informed that he had left somet
- #2295 [0.8976] Narrated Salama bin Al-Akwa`:  A dead person was brought to the Prophet so that he might lead the funeral prayer for him. He asked,  "Is he in debt?" When the people replied in the
- #2292 [0.8888] Narrated Sa`id bin Jubair:  Ibn `Abbas said, "In the verse: To every one We have appointed ' (Muwaliya Muwaliya means one's)  heirs (4.33).' (And regarding the verse) 'And those wi

**Virtues of Madinah** (cohesion: 0.8665)
- #1975 [0.9426] Narrated `Abdullah bin `Amr bin Al-`As:  Allah's Apostle said to me, "O `Abdullah! Have I not been informed that you fast during the day and  offer prayers all the night." `Abdulla
- #1963 [0.9311] 'Narrated Abu Sa`id:  That he had heard the Prophet saying, "Do not fast continuously (practice Al-Wisal), and if you intend  to lengthen your fast, then carry it on only till the 
- #1976 [0.9267] Narrated `Abdullah bin `Amr:  Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the  night throughout my life (so Allah's Apostle ca

**Drinks** (cohesion: 0.8661)
- #5355 [0.9156] Narrated Abu Huraira:  "The Prophet said, 'The best alms is that which is given when one is rich, and a giving hand is better  than a taking one, and you should start first to supp
- #5370 [0.914] Narrated `Aisha:  Hind (bint `Utba) said, "O Allah's Apostle! Abu Sufyan is a miser. Is there any harm if I take of his  property what will cover me and my children's needs?" The P
- #5369 [0.9115] Narrated Um Salama:  I said, "O Allah's Apostle! Shall I get a reward (in the Hereafter) if I spend on the children of Abu  Salama and do not leave them like this and like this (i.

**Apostates** (cohesion: 0.8657)
- #6710 [0.9251] Narrated Abu Huraira:  A man came to Allah's Apostle and said, "I am ruined!" The Prophet said to him, "What is the  matter?" He said, "I have done a sexual relation with my wife (
- #6711 [0.9184] Narrated Abu Huraira:  A man came to the Prophets and said, "I am ruined!" The Prophet said, "What is the matter with you?"  He said, "I have done a sexual relation with my wife (w
- #6709 [0.908] Narrated Abu Huraira:  A man came to the Prophet and said, "I am ruined!" The Prophet said, "What is the matter with you?"  He said, "I had sexual relation with my wife (while I wa

**Afflictions and the End of the World** (cohesion: 0.8649)
- #6926 [0.9114] Narrated Anas bin Malik:  A Jew passed by Allah's Apostle and said, "As-Samu 'Alaika." Allah's Apostle said in reply, "We  'Alaika." Allah's Apostle then said to his companions, "D
- #6930 [0.9105] Narrated `Ali:  Whenever I tell you a narration from Allah's Apostle, by Allah, I would rather fall down from the sky  than ascribe a false statement to him, but if I tell you some
- #6933 [0.8987] Narrated Abu Sa`id:  While the Prophet was distributing (something, `Abdullah bin Dhil Khawaisira at-Tamimi came and  said, "Be just, O Allah's Apostle!" The Prophet said, "Woe to 

**Shortening the Prayers (At-Taqseer)** (cohesion: 0.8646)
- #1194 [0.9084] Narrated Ibn `Umar:  The Prophet used to go to the Mosque of Quba (sometimes) walking and sometimes riding. Added  Nafi` (in another narration), "He then would offer two rak`at (in
- #1193 [0.8984] Narrated `Abdullah bin Dinar:  Ibn `Umar said, "The Prophet used to go to the Mosque of Quba every Saturday (sometimes) walking  and (sometimes) riding." `Abdullah (Ibn `Umar) used
- #1189 [0.8828] Narrated Abu Huraira:   The Prophet said, "Do not set out on a journey      except for three Mosques i.e. Al-Masjid-AI-Haram, the Mosque of       Allah's Apostle , and the Mosque o

**Eclipses** (cohesion: 0.8643)
- #1096 [0.9075] Narrated `Abdullah bin Dinar:  On traveling, `Abdullah bin `Umar used to offer the prayer on his Mount by signs whatever direction  it took. `Abdullah said that the Prophet used to
- #1105 [0.9045] Narrated Salim bin `Abdullah:  Ibn `Umar said, "Allah's Apostle used to pray the Nawafil on the back of his Mount (carriage) by  signs facing any direction." Ibn `Umar used to do t
- #1111 [0.9023] Narrated Anas bin Malik:  Whenever the Prophet started the journey before noon, he used to delay the Zuhr prayer till the time  for the `Asr prayer and then he would dismount and p

**Peacemaking** (cohesion: 0.8633)
- #2553 [0.9087] Narrated Ibn `Umar:  The Prophet said, "If one manumits his share of a common slave (Abd), and he has money sufficient  to free the remaining portion of the price of the slave (jus
- #2526 [0.9067] Narrated Abu Huraira:  That the Prophet said, "Whoever frees his portion of a (common) slave."
- #2523 [0.9054] Narrated Ibn `Umar:  Allah's Apostle said, "Whoever manumits his share of a slave, then it is essential for him to get that  slave manumitted' completely as long as he has the mone

**Kafalah** (cohesion: 0.8606)
- #2271 [0.905] Narrated Abu Musa:  The Prophet said, "The example of Muslims, Jews and Christians is like the example of a man who  employed laborers to work for him from morning till night for s
- #2279 [0.9048] Narrated Ibn `Abbas:  When the Prophet was cupped, he paid the man who cupped him his wages. If it had been undesirable  he would not have paid him.
- #2268 [0.9006] Narrated Ibn `Umar:  The Prophet said, "Your example and the example of the people of the two Scriptures (i.e. Jews and  Christians) is like the example of a man who employed some 

**Khusoomaat** (cohesion: 0.8596)
- #2339 [0.9187] Narrated Rafi` bin Khadij:  My uncle Zuhair said, "Allah's Apostle forbade us to do a thing which was a source of help to us." I  said, "Whatever Allah's Apostle said was right." H
- #2343, 2344 [0.917] Narrated Nafi`:  Ibn `Umar used to rent his farms in the time of Abu Bakr, `Umar, `Uthman, and in the early days of  Muawiya. Then he was told the narration of Rafi` 'bin Khadij th
- #2348 [0.9158] Narrated Abu Huraira:  Once the Prophet was narrating (a story), while a bedouin was sitting with him. "One of the  inhabitants of Paradise will ask Allah to allow him to cultivate

**Virtues of Prayer at Masjid Makkah and Madinah** (cohesion: 0.8586)
- #1201 [0.9012] Narrated Sahl bin Sa`d:  The Prophet went out to affect a reconciliation between the tribes of Bani `Amr bin `Auf and the time  of the prayer became due; Bilal went to Abu Bakr and
- #1218 [0.8955] Narrated Sahl bin Sa`d:  The news about the differences amongst the people of Bani `Amr bin `Auf at Quba reached Allah's  Apostle and so he went to them along with some of his comp
- #1216 [0.8949] Narrated `Abdullah:  I used to greet the Prophet while he was in prayer and he would return my greeting, but when we  returned (from Ethiopia) I greeted the Prophet (while he was p

**Distribution of Water** (cohesion: 0.8575)
- #2306 [0.9253] Narrated Abu Huraira:  A man came to the Prophet demanding his debts and behaved rudely. The companions of the Prophet  intended to harm him, but Allah's Apostle said (to them), "L
- #2305 [0.9] Narrated Abu Huraira:  The Prophet owed somebody a camel of a certain age. When he came to demand it back, the Prophet  said (to some people), "Give him (his due)." When the people
- #2309 [0.8949] Narrated Jabir bin `Abdullah:  I was accompanying the Prophet on a journey and was riding a slow camel that was lagging behind  the others. The Prophet passed by me and asked, "Who

**Prostration During Recital of Qur'an** (cohesion: 0.8573)
- #1146 [0.9046] Narrated Al-Aswad:  I asked `Aisha "How is the night prayer of the Prophet?" She replied, "He used to sleep early at night,  and get up in its last part to pray, and then return to
- #1137 [0.901] Narrated `Abdullah bin `Umar:  A man said, "O Allah's Apostle! How is the prayer of the night?" He said, "Two rak`at followed by  two rak`at and so on, and when you apprehend the a
- #1172, 1173 [0.8985] Narrated Ibn `Umar:  I offered with the Prophet two rak`at before the Zuhr and two rak`at after the Zuhr prayer; two rak`at  after Maghrib, `Isha' and the Jumua prayers. Those of t

**Penalty of Hunting while on Pilgrimage** (cohesion: 0.8562)
- #1869 [0.9025] Narrated Abu Huraira:  The Prophet said, "I have made Medina a sanctuary between its two (Harrat) mountains." The Prophet  went to the tribe of Bani Haritha and said (to them), "I 
- #1867 [0.8967] Narrated Anas:  The Prophet said, "Medina is a sanctuary from that place to that. Its trees should not be cut and no  heresy should be innovated nor any sin should be committed in 
- #1874 [0.8964] Narrated Abu Huraira:  I heard Allah's Apostle saying, "The people will leave Medina in spite of the best state it will have,  and none except the wild birds and the beasts of prey

**Partnership** (cohesion: 0.8562)
- #2412 [0.8973] Narrated Abu Sa`id Al-Khudri:  While Allah's Apostle was sitting, a Jew came and said, "O Abul Qasim! One of your companions has  slapped me on my face." The Prophet asked who that
- #2418 [0.8846] Narrated `Abdullah bin Ka`b bin Malik:  Ka`b demanded his debt back from Ibn Abi Hadrad in the Mosque and their voices grew louder till  Allah's Apostle heard them while he was in 
- #2416, 2417 [0.8827] Narrated `Abdullah bin Mas`ud:  Allah's Apostle said, "Whoever takes a false oath so as to take the property of a Muslim (illegally)  will meet Allah while He will be angry with hi

**(Statements made under) Coercion** (cohesion: 0.8556)
- #6730 [0.9072] Narrated `Urwa:  `Aisha said, "When Allah's Apostle died, his wives intended to send `Uthman to Abu Bakr asking him  for their share of the inheritance." Then `Aisha said to them, 
- #6728 [0.8976] Narrated Malik bin Aus:  'I went and entered upon `Umar, his doorman, Yarfa came saying `Uthman, `Abdur-Rahman, Az-  Zubair and Sa`d are asking your permission (to see you). May I 
- #6763 [0.8878] Narrated Abu Huraira:  The Prophet said, " If somebody dies (among the Muslims) leaving some property, the property will  go to his heirs; and if he leaves a debt or dependants, we

**Prophets** (cohesion: 0.8555)
- #2742 [0.9198] Narrated Sa`d bin Abu Waqqas:  The Prophet came visiting me while I was (sick) in Mecca, ('Amir the sub-narrator said, and he  disliked to die in the land, whence he had already mi
- #2770 [0.9193] Narrated Ibn `Abbas:  A man said to Allah's Apostle , "My mother died, will it benefit her if I give in charity on her behalf?"  The Prophet replied in the affirmative. The man sai
- #2764 [0.9136] Narrated Ibn `Umar:  In the lifetime of Allah's Apostle , `Umar gave in charity some of his property, a garden of date-palms  called Thamgh. `Umar said, "O Allah's Apostle! I have 

**Obligatory Charity Tax (Zakat)** (cohesion: 0.8547)
- #1419 [0.9031] Narrated Abu Huraira:  A man came to the Prophet and asked, "O Allah's Apostle! Which charity is the most superior in  reward?" He replied, "The charity which you practice while yo
- #1424 [0.9011] Narrated Haritha bin Wahab Al-Khuza`i:  I heard the Prophet (p.b.u.h) saying, "(O people!) Give in charity (for Allah's cause) because a time  will come when a person will carry hi
- #1445 [0.8974] Narrated Abu Burda:  from his father from his grandfather that the Prophet said, "Every Muslim has to give in charity." The  people asked, "O Allah's Prophet! If someone has nothin

**Patients** (cohesion: 0.8547)
- #5423 [0.9082] Narrated `Abis:  I asked `Aisha "Did the Prophet forbid eating the meat of sacrifices offered on `Id-ul-Adha for more  than three days" She said, "The Prophet did not do this excep
- #5450 [0.9034] Narrated Anas:  My mother, Um Sulaim, took a Mudd of barley grain, ground it and made porridge from it, and  pressed (over it), a butter skin she had with her. Then she sent me to 
- #5393 [0.9009] Narrated Nafi`:  Ibn `Umar never used to take his meal unless a poor man was called to eat with him. One day I  brought a poor man to eat with him, the man ate too much, whereupon 

**Laws of Inheritance (Al-Faraa'id)** (cohesion: 0.8545)
- #6399 [0.9033] Narrated Abu Musa Al-Ash`ari:  The Prophet used to invoke Allah, saying, "Allahumma ighfirli khati'ati wa jahli wa israfi fi `Amri, wa  ma anta a-'lamu bihi minni. Allahumma ighfir
- #6393 [0.9031] Narrated Abu Huraira:  When the Prophet said, "Sami' al-lahu liman hamidah (Allah heard him who sent his praises to Him)"  in the last rak`a of the `Isha' prayer, he used to invoke
- #6375 [0.9026] Narrated `Aisha:  The Prophet used to say, "O Allah! I seek refuge with You from laziness from geriatric old age, from  being in debt, and from committing sins. O Allah! I seek ref

**Wills and Testaments (Wasaayaa)** (cohesion: 0.8542)
- #2606 [0.9026] Narrated Abu Huraira:  Allah's Apostle owed a man some debt (and that man demanded it very harshly). The companions of  the Prophet wanted to harm him, but the Prophet said to them
- #2597 [0.8978] Narrated Abu Humaid Al-Sa`idi:  The Prophet appointed a man from the tribe of Al-Azd, called Ibn 'Utbiyya for collecting the Zakat.  When he returned he said, "This (i.e. the Zakat
- #2623 [0.8949] Narrated `Umar bin Al-Khattab:  I gave a horse in Allah's Cause. The person to whom it was given, did not look after it. I intended to  buy it from him, thinking that he would sell

**Sacrifice on Occasion of Birth (`Aqiqa)** (cohesion: 0.8537)
- #5055 [0.9121] Narrated `Abdullah (bin Mas`ud):  Allah's Apostle said (to me), "Recite the Qur'an to me." I said, "Shall I recite (it) to you while it has  been revealed to you?" He said, "I like
- #5041 [0.9107] Narrated `Umar bin Khattab:  I heard Hisham bin Hakim bin Hizam reciting Surat-al-Furqan during the lifetime of Allah's Apostle,  and I listened to his recitation and noticed that 
- #4992 [0.9093] Narrated `Umar bin Al-Khattab:  I heard Hisham bin Hakim reciting Surat Al-Furqan during the lifetime of Allah's Apostle and I  listened to his recitation and noticed that he recit

**Tricks** (cohesion: 0.8535)
- #6827, 6828 [0.9315] Narrated Abu Huraira and Zaid bin Khalid:  While we were with the Prophet , a man stood up and said (to the Prophet ), "I beseech you by Allah,  that you should judge us according 
- #6859, 6860 [0.93] Narrated Abu Huraira and Zaid bin Khalid Al-Juhani:  A man came to the Prophet and said, "I beseech you to judge us according to Allah's Laws." Then his opponent who was wiser than
- #6842, 6843 [0.9213] Narrated Abu Huraira and Zaid bin Khalid:  Two men had a dispute in the presence of Allah's Apostle. One of them said, "Judge us according to  Allah's Laws." The other who was more

**Ablutions (Wudu')** (cohesion: 0.8531)
- #199 [0.9314] Narrated `Amr bin Yahya:  (on the authority of his father) My uncle used to perform ablution extravagantly and once he asked  `Abdullah bin Zaid to tell him how he had seen the 
- #192 [0.9227] Narrated `Amr bin Yahya:  My father said, "I saw `Amr bin Abi Hasan asking `Abdullah bin Zaid about the ablution of the  Prophet. `Abdullah bin Zaid asked for an earthenware pot co
- #186 [0.9143] Narrated `Amr:  My father saw `Amr bin Abi Hasan asking `Abdullah bin Zaid about the ablution of the Prophet.  `Abdullah bin Zaid asked for earthenware pot containing water and in 

**Beginning of Creation** (cohesion: 0.8501)
- #2729 [0.9062] Narrated `Urwa:  Aisha said, "Barirah came to me and said, 'My people (masters) have written the contract for my  emancipation for nine Awaq ) of gold) to be paid in yearly inst
- #2735 [0.9002] Narrated `Amra:  Aisha said that Barirah came to seek her help in the writing of her emancipation. `Aisha said to her,  "If you wish, I will pay your masters (your price) and th
- #2723 [0.8859] Narrated Abu Huraira:  The Prophet said, "No town-dweller should sell for a bedouin. Do not practice Najsh (i.e. Do not offer  a high price for a thing which you do not want to buy

**Gifts** (cohesion: 0.8494)
- #2491 [0.8876] Narrated Nafi`:  Ibn `Umar said, "Allah's Apostle said, 'If one manumits his share of a jointly possessed slave, and can  afford the price of the other shares according to the adeq
- #2500 [0.887] Narrated `Uqba bin 'Amir:  that Allah's Apostle gave him some sheep to distribute among his companions in order to sacrifice  them and a kid was left. He told the Prophet about it 
- #2484 [0.8804] Narrated Salama:  Once (on a journey) our provisions diminished and the people were reduced to poverty. They went to the Prophet  and asked his permission to slaughter their cam

**Jizyah and Mawaada'ah** (cohesion: 0.8494)
- #2698 [0.8995] Narrated Al-Bara bin `Azib:  When Allah's Apostle concluded a peace treaty with the people of Hudaibiya, `Ali bin Abu Talib  wrote the document and he mentioned in it, "Muhammad, A
- #2705 [0.8992] Narrated Aisha:  Once Allah's Apostle heard the loud voices of some opponents quarreling at the door. One of them  was appealing to the other to deduct his debt and asking him to b
- #2691 [0.8819] Narrated Anas:  It was said to the Prophet "Would that you see `Abdullah bin Ubai." So, the Prophet went to him,  riding a donkey, and the Muslims accompanied him, walking on salty

**Times of the Prayers** (cohesion: 0.8491)
- #757 [0.9178] Narrated Abu Huraira:  Allah's Apostle entered the mosque and a person followed him. The man prayed and went to the  Prophet and greeted him. The Prophet returned the greeting and 
- #828 [0.9105] Narrated Muhammad bin `Amr bin `Ata':  I was sitting with some of the companions of Allah's Apostle and we were discussing about the way of  praying of the Prophet. Abu Humaid As-S
- #793 [0.9098] Narrated Abu Huraira:  Once the Prophet entered the mosque, a man came in, offered the prayer and greeted the Prophet. The  Prophet returned his greeting and said to him, "Go back 

**Lost Things Picked up by Someone (Luqatah)** (cohesion: 0.8485)
- #2352 [0.8911] Narrated Az-Zuhri:  Anas bin Malik said, that once a domestic sheep was milked for Allah's Apostle while he was in the  house of Anas bin Malik. The milk was mixed with water drawn
- #2361 [0.8886] Narrated `Urwa:  When a man from the Ansar quarreled with Az-Zubair, the Prophet said, "O Zubair! Irrigate (your  land) first and then let the water flow (to the land of the others
- #2358 [0.8823] Narrated Abu Huraira:  Allah's Apostle said, "There are three persons whom Allah will not look at on the Day of  Resurrection, nor will he purify them and theirs shall be a severe 

**Oneness, Uniqueness of Allah (Tawheed)** (cohesion: 0.8478)
- #7211 [0.8951] Narrated Jabir bin `Abdullah:  A bedouin gave the Pledge of allegiance to Allah's Apostle for Islam. Then the bedouin got fever at  Medina, came to Allah's Apostle and said, "O All
- #7219 [0.8914] Narrated Anas bin Malik:  That he heard `Umar's second speech he delivered when he sat on the pulpit on the day following the  death of the Prophet `Umar recited the Tashahhud whil
- #7170 [0.8902] Narrated Abu Qatada:  Allah's Apostle said on the Day of (the battle of) Hunain, "Whoever has killed an infidel and has a  proof or a witness for it, then the salb (arms and belong

**Merits of the Helpers in Madinah (Ansaar)** (cohesion: 0.8476)
- #3182 [0.9015] Narrated Abu Wail:  We were in Siffin and Sahl bin Hunaif got up and said, "O people! Blame yourselves! We were with  the Prophet on the day of Hudaibiya, and if we had been called
- #3170 [0.8853] Narrated `Asim:  I asked Anas about the Qunut (i.e. invocation in the prayer). Anas said, "It should be recited before  bowing." I said, "So-and-so claims that you say that it shou
- #3179 [0.8813] Narrated `Ali:  We did not, write anything from the Prophet except the Qur'an and what is written in this paper,  (wherein) the Prophet said, "Medina is a sanctuary from (the mount

**Judgments (Ahkaam)** (cohesion: 0.8475)
- #6952 [0.8818] Narrated Anas:  Allah's Apostle said, "Help your brother whether he is an oppressor or an oppressed," A man said, "O  Allah's Apostle! I will help him if he is oppressed, but if he
- #6943 [0.8811] Narrated Khabbab bin Al-Art:  We complained to Allah's Apostle (about our state) while he was leaning against his sheet cloak in the  shade of the Ka`ba. We said, "Will you ask All
- #6951 [0.8734] Narrated `Abdullah bin `Umar:  Allah's Apostle said, "A Muslim is a brother of another Muslim. So he should neither oppress him nor  hand him over to an oppressor. And whoever fulf

**Asking Permission** (cohesion: 0.8473)
- #5613 [0.9077] Narrated Jabir bin `Abdullah:  Allah's Apostle and one of his companions entered upon an Ansari man and the Prophet said to him,  "If you have water kept overnight in a water skin,
- #5595 [0.9067] Narrated Ibrahim:  I asked Al-Aswad, "Did you ask `Aisha, Mother of the Believers, about the containers in which it is  disliked to prepare (non-alcoholic) drinks?" He said, "Yes, 
- #5621 [0.9037] Narrated Jabir bin `Abdullah:  The Prophet and one of his companions entered upon an Ansari man. The Prophet and his companion  greeted (the man) and he replied, "O Allah's Apostle

**Belief** (cohesion: 0.8468)
- #27 [0.8896] Narrated Sa'd:        Allah's Apostle distributed (Zakat) amongst (a group of) people while       I was sitting there but Allah's Apostle left a man whom I thought the       best o
- #24 [0.8861] Narrated 'Abdullah (bin 'Umar):        Once Allah's Apostle passed by an Ansari (man) who was admonishing      his brother regarding Haya'. On that Allah's Apostle said, "Leave him
- #26 [0.8833] Narrated Abu Huraira:        Allah's Apostle was asked, "What is the best deed?" He replied, "To       believe in Allah and His Apostle (Muhammad). The questioner then       asked,

**Funerals (Al-Janaa'iz)** (cohesion: 0.8455)
- #1247 [0.9082] Narrated Ibn `Abbas.:  A person died and Allah's Apostle used to visit him. He died at night and (the people) buried him at  night. In the morning they informed the Prophet (about 
- #1269 [0.9076] Narrated Ibn `Umar:  When `Abdullah bin Ubai (the chief of hypocrites) died, his son came to the Prophet and said, "O  Allah's Apostle! Please give me your shirt to shroud him in i
- #1286, 1287, 1288 [0.9039] Narrated `Abdullah bin 'Ubaidullah bin Abi Mulaika:  One of the daughters of `Uthman died at Mecca. We went to attend her funeral procession. Ibn `Umar  and Ibn `Abbas were also pr

**Knowledge** (cohesion: 0.8445)
- #128 [0.8872] Narrated Anas bin Malik:  "Once Mu`adh was along with Allah's Apostle as a companion rider. Allah's Apostle said, "O Mu`adh  bin Jabal." Mu`adh replied, "Labbaik and Sa`daik. O All
- #103 [0.8833] Narrated Ibn Abu Mulaika:  Whenever `Aisha (the wife of the Prophet) heard anything which she did not understand, she used to  ask again till she understood it completely. Aisha sa
- #105 [0.8815] Narrated Abu Bakra:  The Prophet said. No doubt your blood, property, the sub-narrator Muhammad thought that Abu  Bakra had also mentioned and your honor (chastity), are sacred to 

**Blood Money (Ad-Diyat)** (cohesion: 0.8442)
- #6676, 6677 [0.8986] Narrated `Abdullah:  Allah's Apostle said, "If somebody is ordered (by the ruler or the judge) to take an oath, and he takes a  false oath in order to grab the property of a Muslim
- #6680 [0.8906] Narrated Abu Musa Al-Ash`ari:  I went along with some men from the Ash-ariyin to Allah's Apostle and it happened that I met him  while he was in an angry mood. We asked him to prov
- #6632 [0.8901] Narrated `Abdullah bin Hisham:  We were with the Prophet and he was holding the hand of `Umar bin Al-Khattab. `Umar said to Him,  "O Allah's Apostle! You are dearer to me than ever

**Pilgrims Prevented from Completing the Pilgrimage** (cohesion: 0.844)
- #1822 [0.9054] Narrated `Abdullah bin Abu Qatada:  That his father said "We proceeded with the Prophet in the year of Al-Hudaibiya and his companions  assumed Ihram but I did not. We were informe
- #1821 [0.8953] Narrated `Abdullah bin Abu Qatada:  My father set out (for Mecca) in the year of Al-Hudaibiya, and his companions assumed Ihram, but he  did not. At that time the Prophet was infor
- #1853 [0.8946] Narrated Ibn `Abbas:  A woman from the tribe of Khath'am came in the year (of ,Hajjat-al-Wada` of the Prophet ) and said,  "O Allah's Apostle! My father has come under Allah's obli

**Fighting for the Cause of Allah (Jihaad)** (cohesion: 0.844)
- #2676, 2677 [0.8966] Narrated Abu Wail from `Abdullah:  The Prophet said, "Whoever takes a false oath in order to grab another man's (or his brother's)  property, then Allah will be angry with him when
- #2654 [0.8923] Narrated Abu Bakra:  The Prophet said thrice, "Should I inform you out the greatest of the great sins?" They said, "Yes, O  Allah's Apostle!" He said, "To join others in worship wi
- #2650 [0.8892] Narrated An-Nu`man bin Bashir:  My mother asked my father to present me a gift from his property; and he gave it to me after some  hesitation. My mother said that she would not be 

**Call to Prayers (Adhaan)** (cohesion: 0.844)
- #878 [0.916] Narrated Ibn `Umar:  While `Umar bin Al-Khattab was standing and delivering the sermon on a Friday, one of the  companions of the Prophet, who was one of the foremost Muhajirs (emi
- #883 [0.9042] Narrated Salman-Al-Farsi:  The Prophet (p.b.u.h) said, "Whoever takes a bath on Friday, purifies himself as much as he can, then  uses his (hair) oil or perfumes himself with the s
- #882 [0.9023] Narrated Abu Huraira:  While `Umar (bin Al-Khattab) was delivering the Khutba on a Friday, a man entered (the mosque).  `Umar asked him, "What has detained you from the prayer?" Th

**Wedlock, Marriage (Nikaah)** (cohesion: 0.8435)
- #3696 [0.9043] Narrated 'Ubaidullah bin `Adi bin Al-Khiyar:  Al-Miswar bin Makhrama and `Abdur-Rahman bin Al-Aswad bin 'Abu Yaghuth said (to me), "What  forbids you to talk to `Uthman about his b
- #3685 [0.9031] Narrated Ibn `Abbas:  When (the dead body of) `Umar was put on his deathbed, the people gathered around him and invoked  (Allah) and prayed for him before the body was taken away, 
- #3677 [0.9004] Narrated Ibn `Abbas:  While I was standing amongst the people who were invoking Allah for `Umar bin Al-Khattab who  was lying (dead) on his bed, a man behind me rested his elbows o

**Hunting, Slaughtering** (cohesion: 0.8428)
- #5126 [0.9197] Narrated Sahl bin Sa`d:  A woman came to Allah's Apostle and said, "O Allah's Apostle! I have come to you to present myself  to you (for marriage)." Allah's Apostle glanced at her.
- #5087 [0.9173] Narrated Sahl bin Sa`d As-Sa`idi:  A woman came to Allah's Apostle and said, "O Allah's Apostle! I have come to give you myself in  marriage (without Mahr)." Allah's Apostle looked
- #5149 [0.9146] Narrated Sahl bin Sa`d As-Sa`idi:  While I was (sitting) among the people in the company of Allah's Apostle a woman stood up and said,  "O Allah's Apostle! She has given herself in

**Wishes** (cohesion: 0.8422)
- #6977 [0.889] Narrated 'Amr bin Ash-Sharid:        Al-Miswar bin Makhrama came and put his hand on my shoulder and I       accompanied him to Sa'd. Abu Rafi' said to Al-Miswar, "Won't you order 
- #6979 [0.8856] Narrated Abu Humaid As-Sa`idi:  Allah's Apostle appointed a man called Ibn Al-Lutabiyya to collect the Zakat from Bani Sulaim's  tribe. When he returned, the Prophet called him to 
- #6978 [0.8841] Narrated 'Amr bin Ash-Sharid:   Abu Rafi' said that Sa'd offered him       four hundred Mithqal of gold for a house. Abu Rafi ' said, "If I had       not heard Allah's Apostle sayi

**Companions of the Prophet** (cohesion: 0.842)
- #3150 [0.9095] Narrated `Abdullah:  On the day (of the battle) of Hunain, Allah's Apostle favored some people in the distribution of the  booty (to the exclusion of others); he gave Al-Aqra' bin 
- #3147 [0.8946] Narrated Anas bin Malik:  When Allah favored His Apostle with the properties of Hawazin tribe as Fai (booty), he started giving  to some Quarries men even up to one-hundred camels 
- #3142 [0.8942] Narrated Abu Qatada:  We set out in the company of Allah's Apostle on the day (of the battle) of Hunain. When we faced the  enemy, the Muslims retreated and I saw a pagan throwing 

**Medicine** (cohesion: 0.841)
- #5472 [0.9065] Narrated Salman bin 'Amir Ad-Dabbi:  I heard Allah's Apostle saying, "'Aqiqa is to be offered for a (newly born) boy, so slaughter (an  animal) for him, and relieve him of his suff
- #5469 [0.8873] Narrated Asma' bint Abu Bakr:  I conceived `Abdullah bin AzZubair at Mecca and went out (of Mecca) while I was about to give  birth. I came to Medina and encamped at Quba', and gav
- #5470 [0.8772] Narrated Anas bin Malik:        Abu Talha had a child who was sick. Once, while Abu Talha was out, the      child died. When Abu Talha returned home, he asked, "How does my son    

**Oaths and Vows** (cohesion: 0.8403)
- #6054 [0.9088] Narrated `Aisha:  A man asked permission to enter upon Allah's Apostle. The Prophet said, "Admit him. What an evil  brother of his people or a son of his people." But when the man 
- #6131 [0.8963] Narrated Aisha:  A man asked permission to see the Prophet. He said, "Let Him come in; What an evil man of the tribe  he is! (Or, What an evil brother of the tribe he is).  But whe
- #5976 [0.895] Narrated Abu Bakra:  Allah's Apostle said thrice, "Shall I not inform you of the biggest of the great sins?" We said, "Yes, O  Allah's Apostle" He said, "To join partners in worshi

**Interpretation of Dreams** (cohesion: 0.8402)
- #6898 [0.8968] Narrated Sahl bin Abi Hathma:  (a man from the Ansar) that a number of people from his tribe went to Khaibar and dispersed, and  then they found one of them murdered. They said to 
- #6877 [0.8874] Narrated Anas bin Malik:  A girl wearing ornaments, went out at Medina. Somebody struck her with a stone. She was brought to  the Prophet while she was still alive. Allah's Apostle
- #6861 [0.8863] Narrated `Abdullah:  A man said, "O Allah's Apostle! Which sin is the greatest in Allah's Sight?" The Prophet said, "To set  up a rival unto Allah though He Alone created you . " T

**Al-Adha Festival Sacrifice (Adaahi)** (cohesion: 0.8392)
- #5252 [0.9133] Narrated Anas bin Seereen:  Ibn `Umar said: "I divorced my wife while she was menstruating. `Umar mentioned that to the  Prophet . The Prophet said, (to my father), "Let your son t
- #5349 [0.9116] Narrated Sa`id bin Jubair:  I said to Ibn `Umar, "If a man accuses his wife of illegal sexual intercourse (what is the judgment)?"  He said, "Allah's Prophet separated the couple o
- #5273 [0.9082] Narrated Ibn `Abbas:  The wife of Thabit bin Qais came to the Prophet and said, "O Allah's Apostle! I do not blame Thabit  for defects in his character or his religion, but I, bein

**Sales and Trade** (cohesion: 0.8389)
- #2123, 2124 [0.9004] Narrated Nafi`:  Ibn `Umar told us that the people used to buy food from the caravans in the lifetime of the Prophet.  The Prophet used to forbid them to sell it at the very place 
- #2136 [0.9] Narrated Ibn `Umar:  The Prophet said, "The buyer of foodstuff should not sell it before it has been measured for him."  Isma`il narrated instead, "He should not sell it before rec
- #2132 [0.8983] Narrated Tawus:  Ibn `Abbas said, "Allah's Apostle forbade the selling of foodstuff before its measuring and  transferring into one's possession." I asked Ibn `Abbas, "How is that?

**To make the Heart Tender (Ar-Riqaq)** (cohesion: 0.8389)
- #5737 [0.9035] Narrated Ibn `Abbas:  Some of the companions of the Prophet passed by some people staying at a place where there was  water, and one of those people had been stung by a scorpion. A
- #5714 [0.8971] Narrated `Aisha:  (the wife of the Prophet)  When the health of Allah's Apostle deteriorated and his condition became serious, he asked the  permission of all his wives to allow hi
- #5736 [0.8964] Narrated Abu Sa`id Al-Khudri:  Some of the companions of the Prophet came across a tribe amongst the tribes of the Arabs, and that  tribe did not entertain them. While they were in

**Prayers (Salat)** (cohesion: 0.8379)
- #397 [0.8989] Narrated Mujahid:  Someone came to Ibn `Umar and said, "Here is Allah's Apostle entering the Ka`ba." Ibn `Umar said,  "I went there but the Prophet had come out of the Ka`ba and I 
- #370 [0.8982] Narrated Muhammad bin Al-Munkadir:  I went to Jabir bin `Abdullah and he was praying wrapped in a garment and his Rida was Lying beside  him. When he finished the prayers, I said "
- #378 [0.8915] Narrated Anas bin Malik:  Once Allah's Apostle fell off a horse and his leg or shoulder got injured. He swore that he would not  go to his wives for one month and he stayed in a Ma

**Prophetic Commentary on the Qur'an (Tafseer of the Prophet (pbuh))** (cohesion: 0.8371)
- #3337 [0.8992] Narrated Ibn `Umar:  Once Allah's Apostle stood amongst the people, glorified and praised Allah as He deserved and then  mentioned the Dajjal saying, "l warn you against him (i.e. 
- #3361 [0.8926] Narrated Abu Huraira:  One day some meat was given to the Prophet and he said, "On the Day of Resurrection Allah will  gather all the first and the last (people) in one plain, and 
- #3349 [0.8916] Narrated Ibn `Abbas:  The Prophet said, "You will be gathered (on the Day of Judgment), bare-footed, naked and not  circumcised." He then recited:--'As We began the first creation,

**Holding Fast to the Qur'an and Sunnah** (cohesion: 0.8363)
- #7132 [0.8893] Narrated Abu Sa`id:  One day Allah's Apostle narrated to us a long narration about Ad-Dajjal and among the things he  narrated to us, was: "Ad-Dajjal will come, and he will be forb
- #7078 [0.8851] Narrated Abu Bakra:  Allah's Apostle addressed the people saying, "Don't you know what is the day today?" They replied,  "Allah and His Apostle know better." We thought that he mig
- #7077 [0.8745] Narrated Ibn `Umar:  I heard the Prophet saying, "Do not revert to disbelief after me by striking (cutting) the necks of one  another."

**Makaatib** (cohesion: 0.8361)
- #2444 [0.881] Narrated Anas:  Allah's Apostle said, "Help your brother, whether he is an oppressor or he is an oppressed one. People  asked, "O Allah's Apostle! It is all right to help him if he
- #2458 [0.8743] Narrated Um Salama:  (the wife of the Prophet) Allah's Apostle heard some people quarreling at the door of his dwelling. He  came out and said, "I am only a human being, and oppone
- #2441 [0.8718] Narrated Safwan bin Muhriz Al-Mazini:  While I was walking with Ibn `Umar holding his hand, a man came in front of us and asked, "What  have you heard from Allah's Apostle about An

**Virtues and Merits of the Prophet (pbuh) and his Companions** (cohesion: 0.8345)
- #2910 [0.9091] Narrated Jabir bin `Abdullah:  That he proceeded in the company of Allah's Apostle towards Najd to participate in a Ghazwa. (Holybattle)  When Allah's Apostle returned, he too retu
- #3076 [0.8939] Narrated Qais:  Jarir bin `Abdullah said to me, "Allah's Apostle said to me, 'Won't you relieve me from Dhul-  Khalasa?' Dhul-Khalasa was a house where the tribe of Khatham used to
- #2821 [0.8911] Narrated Muhammad bin Jubair:  Jubair bin Mut`im told me that while he was in the company of Allah's Apostle with the people  returning from Hunain, some people (bedouins) caught h

**Expiation for Unfulfilled Oaths** (cohesion: 0.8339)
- #6271 [0.9032] Narrated Anas bin Malik:  When Allah's Apostle married Zainab bint Jahsh, he invited the people who took their meals and then  remained sitting and talking. The Prophet pretended t
- #6239 [0.8807] Narrated Anas:  When the Prophet married Zainab, the people came and were offered a meal, and then they sat down  (after finishing their meals) and started chatting. The Prophet sh
- #6255 [0.8721] Narrated `Abdullah bin Ka`b:  I heard Ka`b bin Malik narrating (when he did not join the battle of Tabuk): Allah's Apostle forbade  all the Muslims to speak to us. I would come to 

**Supporting the Family** (cohesion: 0.8333)
- #4202 [0.9025] Narrated Sahl bin Sa`d As Saidi:  Allah's Apostle (and his army) encountered the pagans and the two armies.,, fought and then Allah's  Apostle returned to his army camps and the ot
- #4077 [0.9025] Narrated `Aisha:  Regarding the Holy Verse: "Those who responded (To the call) of Allah And the Apostle  (Muhammad), After being wounded, For those of them Who did good deeds And r
- #4139 [0.9008] Narrated Jabir bin `Abdullah:  We took part in the Ghazwa of Najd along with Allah's Apostle and when the time for the afternoon  rest approached while he was in a valley with plen

**Food, Meals** (cohesion: 0.8318)
- #4538 [0.9007] Narrated Ubaid bin Umair:  Once `Umar (bin Al-Khattab) said to the companions of the Prophet "What do you think about this  Verse:--"Does any of you wish that he should have a gard
- #4901 [0.8973] Narrated Zaid bin Arqam:  I was with my uncle and I heard `Abdullah bin Ubai bin Salul, saying, "Don't spend on those who are  with Allah's Apostle that they may disperse and go aw
- #4895 [0.8951] Narrated Ibn `Abbas:  I witnessed the `Id-al-Fitr prayer with Allah's Apostle , Abu Bakr, `Umar and `Uthman; and all of  them offered it before delivering the sermon... and then de

**Limits and Punishments set by Allah (Hudood)** (cohesion: 0.8317)
- #6571 [0.9002] Narrated `Abdullah:  The Prophet said, "I know the person who will be the last to come out of the (Hell) Fire, and the last to  enter Paradise. He will be a man who will come out o
- #6541 [0.8935] Narrated Ibn `Abbas:  The Prophet said, "The people were displayed in front of me and I saw one prophet passing by with a  large group of his followers, and another prophet passing
- #6542 [0.8923] Narrated Abu Huraira:  I heard Allah's Apostle saying, "From my followers there will enter Paradise a crowd, seventy  thousand in number, whose faces will glitter as the moon does 

**Virtues of the Qur'an** (cohesion: 0.8313)
- #3591 [0.8841] Narrated Abu Huraira:  I enjoyed the company of Allah's Apostle for three years, and during the other years of my life, never  was I so anxious to understand the (Prophet's) tradit
- #3595 [0.884] Narrated `Adi bin Hatim:  While I was in the city of the Prophet, a man came and complained to him (the Prophet, ) of  destitution and poverty. Then another man came and complained
- #3596 [0.8834] Narrated `Uqba bin `Amr:  The Prophet once came out and offered the funeral prayer for the martyrs of Uhud, and proceeded to  the pulpit and said, "I shall be your predecessor and 

**Divine Will (Al-Qadar)** (cohesion: 0.8299)
- #5829 [0.8801] Narrated Abu `Uthman:  While we were at Adharbijan, `Umar wrote to us: 'Allah's Apostle forbade wearing silk except this  much. Then the Prophet approximated his two fingers (index
- #5799 [0.88] Narrated Al-Mughira:  One night I was with the Prophet on a journey. He asked (me), "Have you got water with you?" I  replied, "Yes" So he got down from his she-camel and went away
- #5901 [0.8786] Narrated Al-Bara':  I did not see anybody in a red cloak looking more handsome than the Prophet.<br> Narrated Malik: The  hair of the Prophet used to hang near his shoulders. Abu I

**Military Expeditions led by the Prophet (pbuh) (Al-Maghaazi)** (cohesion: 0.8266)
- #3231 [0.8815] Narrated `Aisha:  That she asked the Prophet , 'Have you encountered a day harder than the day of the battle) of Uhud?"  The Prophet replied, "Your tribes have troubled me a lot, a
- #3239 [0.8768] Narrated Ibn `Abbas:  The Prophet said, "On the night of my Ascent to the Heaven, I saw Moses who was a tall brown curlyhaired  man as if he was one of the men of Shan'awa tribe, a
- #3294 [0.8756] Narrated Sa`d bin Abi Waqqas:  Once `Umar asked the leave to see Allah's Apostle in whose company there were some Quraishi  women who were talking to him and asking him for more fi

**Divorce** (cohesion: 0.8245)
- #3866 [0.8843] Narrated `Abdullah bin `Umar:  I never heard `Umar saying about something that he thought it would be so-and-so, but he was quite  right. Once, while `Umar was sitting, a handsome 
- #3916 [0.8833] Narrated Abu `Uthman:  I heard that Ibn `Umar used to become angry if someone mentioned that he had migrated before his  father (`Umar), and he used to say, " `Umar and I came to A
- #3861 [0.8833] Narrated Ibn `Abbas:  When Abu Dhar received the news of the Advent of the Prophet he said to his brother, "Ride to this  valley (of Mecca) and try to find out the truth of the per

### bulugh (5 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Oaths and Vows | 23 | 0.8695 |
| Funerals | 66 | 0.8672 |
| Judgments | 36 | 0.8613 |
| Hajj | 74 | 0.8533 |
| The Book of Purification | 179 | 0.8346 |

#### Representative hadiths per book

**Oaths and Vows** (cohesion: 0.8695)
- #1378 [0.919] Narrated Ibn 'Umar (RA): "Allah's Messenger (SAW) said, "Whoever swears an oath, and then says: "If Allah Wills", he is not held accountable if he breaks it."  [Ahmad and al-Arba'a
- #1376 [0.9127] Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "Your oath will be about that matter which your adversary has required you to swear about so that he will believe you."  I
- #1386 [0.9045] Abu Dawud has from the narration of Ibn Abbas (RA) (who reported Allah's Messenger (SAW) as saying): "If anyone takes a vow but does not name it, its atonement is the same as that 

**Funerals** (cohesion: 0.8672)
- #574 [0.942] Ibn 'Umar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “When you place your deceased in the grave, say, ‘In the Name of Allah, and in accordance with the tradition o
- #596 [0.9228] A’ishah (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Do not speak badly of the dead, they have already seen the result of (the deeds) that they sent on before them.
- #567 [0.9199] Abu Hurairah (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “If you offer the funeral prayer for a deceased person, supplicate Allah sincerely for him." Related by Abu

**Judgments** (cohesion: 0.8613)
- #1421 [0.9144] Narrated Ibn 'Abbas (RA): Allah's Messenger (SAW) ruled on the basis of an oath and a single witness.  [Muslim, Abu Dawud and an-Nasa'i reported it, the latter said that it has a J
- #1404 [0.9003] Narrated Umm Salamah (RA): Allah's Messenger (SAW) said, "Indeed, you bring your disputers to me, and perhaps some of you are more eloquent in their plea than others, so that I giv
- #1416 [0.8999] Narrated 'Abdullah bin 'Amr (RA): Allah's Messenger (SAW) said, "It is not permissible to accept the testimony of a man or a woman who does not  fulfill their trusts, or of one who

**Hajj** (cohesion: 0.8533)
- #781 [0.9118] A’ishah (RAA) narrated, 'The Messenger of Allah (P.B.U.H.) went to visit. Duba’ah bint Az-Zubair bin 'Abdul Muttalib. She said to him, ‘O Messenger of Allah I have made the intenti
- #766 [0.8985] 'Abdullah Ibn ‘Amro bin al-’As (RAA) narrated that the Messenger of Allah (P.B.U.H.) stood in Mina during the Farewell Hajj, while the people asked him questions and he answered th
- #714 [0.8984] Ibn ’Abbas (RAA) narrated, The Messenger of Allah (P.B.U.H.) came across some riders at ar-Rauha’ (a place near Madinah). He asked them, “Who are you?" They replied, ‘Who are you?’

**The Book of Purification** (cohesion: 0.8346)
- #6 [0.9055] Narrated Abu Huraira (rad): Narrated Abu Huraira (rad): Allah’s Messenger (saw) said: “None of you should take a bath in stagnant water when he is sexually impure”. [Muslim reporte
- #73 [0.9051] Narrated Busra bint Safwan (rad): Allah’s Messenger (saw) said, “He who touches his penis should perform ablution”. [Reported by Al-Khamsa, and At-Tirmidhi and Ibn Hibban graded it
- #112 [0.9045] Narrated ‘Aisha (rad): Allah’s Messenger (saw) used to take a bath from four things; after sexual intercourse, on Fridays, after extracting blood from his body and after washing a 

### forty (3 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Forty Hadith of an-Nawawi | 42 | 0.8946 |
| Forty Hadith Qudsi | 40 | 0.8909 |
| Forty Hadith of Shah Waliullah Dehlawi | 40 | 0.6937 |

#### Representative hadiths per book

**Forty Hadith of an-Nawawi** (cohesion: 0.8946)
- #31 [0.9336] On the authority of Abu al-’Abbas Sahl bin Sa’ad as-Sa’idee (may Allah be pleased with him) who said:  A man came to the Prophet (peace and blessings of Allah be upon him) and said
- #15 [0.9255] On the authority of Abu Hurayrah (may Allah be pleased with him), that the Messenger of Allah (peace and blessings of Allah be upon him) said:  Let him who believes in Allah and th
- #29 [0.9217] On the authority of Muadh bin Jabal (may Allah be pleased with him) who said:  I said, “O Messenger of Allah, tell me of an act which will take me into Paradise and will keep me aw

**Forty Hadith Qudsi** (cohesion: 0.8909)
- #29 [0.9267] On the authority of Abu Hurayrah (may Allah be pleased with him), who said that the Messenger of Allah (PBUH) said: Allah (mighty and sublime be He) says: My faithful servant's rew
- #25 [0.924] On the authority of Abu Hurayrah (may Allah be pleased with him), who said that the Messenger of Allah (PBUH) said: Allah (mighty and sublime be He) said: Whosoever shows enmity to
- #6 [0.9114] On the authority of Abu Hurayrah (may Allah be pleased with him), who said: I heard the Messenger of Allah (PBUH) say: The first of people against whom judgment will be pronounced 

**Forty Hadith of Shah Waliullah Dehlawi** (cohesion: 0.6937)
- #18 [0.7966] The felicitous person takes lessons from (the actions of) others.
- #5 [0.7886] The person guiding (someone) to do a good deed, is like the one performing the good deed.
- #22 [0.7641] A man who knows his worth will not be ruined.

### hisn (1 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Fortress of the Muslim (Hisn al-Muslim) | 268 | 0.8835 |

#### Representative hadiths per book

**Fortress of the Muslim (Hisn al-Muslim)** (cohesion: 0.8835)
- #15 [0.9277] <span class="transliteration">Subḥānaka Allāhumma wa biḥamdika,  'ash-hadu 'an lā 'ilāha 'illā 'Anta, 'astaghfiruka wa 'atūbu 'ilayk.</span>  <span class="translation">Glory is to 
- #49 [0.927] <span class="transliteration">Allāhumma’ghfir lī, war’ḥamnī,  wahdinī, wajburnī,  wa `āfinī, warzuqnī, warfa`nī. </span>  <span class="translation">O Allah forgive me, have mercy o
- #79 [0.9269] <span class="transliteration">Allāhumma anta Rabbī lā ilāha illā ant,  khalaqtanī wa anā `abduk,  wa anā `alā `ahdika wa wa`dika mastaṭa`t,  a`ūdhu bika min sharri mā ṣana`t,  abū'

### ibnmajah (37 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| The Chapters on Gifts | 15 | 0.9059 |
| Interpretation of Dreams | 34 | 0.9026 |
| Chapters on Shares of Inheritance | 34 | 0.8949 |
| The Chapters on Wills | 24 | 0.8913 |
| The Chapters on Charity | 46 | 0.8897 |
| Fasting | 145 | 0.8895 |
| The Chapters on Lost Property | 10 | 0.8894 |
| The Chapters on Manumission (of Slaves) | 21 | 0.8885 |
| The Chapters on Pre-emption | 11 | 0.8883 |
| Chapters on Sacrifices | 42 | 0.8871 |
| Chapters on Drinks | 65 | 0.8849 |
| Chapters on Food | 120 | 0.8817 |
| Supplication | 66 | 0.8811 |
| Chapters on Hunting | 51 | 0.8777 |
| The Chapters on Expiation | 47 | 0.8754 |
| Chapters on Slaughtering | 38 | 0.8733 |
| Chapters Regarding Funerals | 205 | 0.8729 |
| Establishing the Prayer and the Sunnah Regarding Them | 630 | 0.8728 |
| Zuhd | 242 | 0.8722 |
| Tribulations | 175 | 0.8713 |
| The Chapters on Legal Punishments | 82 | 0.8698 |
| The Chapters on Blood Money | 80 | 0.8694 |
| Chapters on Medicine | 114 | 0.868 |
| The Chapters on Rulings | 67 | 0.8672 |
| Chapters on <i>Hajj</i> Rituals | 238 | 0.8669 |
| Chapters on Dress | 107 | 0.8654 |
| The Chapters on Pawning | 57 | 0.8643 |
| The Book of the Adhan and the Sunnah Regarding It | 29 | 0.8615 |
| The Chapters on Jihad | 129 | 0.8607 |
| The Chapters Regarding Zakat | 62 | 0.8571 |
| The Chapters on Divorce | 74 | 0.8519 |
| The Book of Purification and its Sunnah | 400 | 0.8508 |
| The Book of the Prayer | 39 | 0.849 |
| The Chapters on Marriage | 171 | 0.8464 |
| The Book On The Mosques And The Congregations | 68 | 0.8452 |
| The Chapters on Business Transactions | 171 | 0.8449 |
| Etiquette | 170 | 0.8368 |

#### Representative hadiths per book

**The Chapters on Gifts** (cohesion: 0.9059)
- #2387 [0.9341] It was narrated from Abu Hurairah that the Messenger of Allah (SAW) said: “A man has more right to his gift so long as he has not gotten something in return for it.”
- #2378 [0.9315] It was narrated from Amr bin Shu'aib, from his father, from, his Grandfather, that the Prophet (SAW) of Allah (SWT) said: “None of you should take back his gift, except a father (t
- #2379 [0.9313] It was narrated from Abu Hurairah that the Messenger of Allah (SAW) said: “There is no lifelong grant. Whoever is given something as a lifelong grant, it is his.' ”

**Interpretation of Dreams** (cohesion: 0.9026)
- #3909 [0.9418] It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “(Good) dreams come from Allah and (bad) dreams come from Satan, so if anyone of you sees something that he
- #3905 [0.939] It was narrated from Ibn ‘Abbas that the Messenger of Allah (saw) said: “Whoever sees me in a dream has (really) sees me, for Satan cannot imitate me.”
- #3908 [0.9365] It was narrated from Jabir bin ‘Abdullah that the Messenger of Allah (saw) said: “If anyone of you sees a dream that he dislikes, let him spit dryly to his left three times and see

**Chapters on Shares of Inheritance** (cohesion: 0.8949)
- #2740 [0.935] It was narrated that Ibn ‘Abbas said: “The Messenger of Allah (saw) said: ‘Distribute wealth among those who are entitled to shares of inheritance, according to the Book of Allah, 
- #2745 [0.9277] It was narrated from ‘Amr bin Shu’aib, from his father, from his grandfather that the Messenger of Allah (saw) said: “Whoever commits adultery with a slave woman or a free woman, h
- #2736 [0.9272] It was narrated from ‘Abdullah bin ‘Amr that the Messenger of Allah (saw) stood up, on the day of the conquest of Makkah, and said: “A woman inherits from the blood money and wealt

**The Chapters on Wills** (cohesion: 0.8913)
- #2710 [0.9344] It was narrated from Ibn Umar that the Messenger of Allah (SAW) said: “(Allah says) O son of Adam! I have given you two things which you do not deserve (except by mercy of Allah (S
- #2716 [0.9248] It was narrated from Abu Hurairah that a man asked the Messenger of Allah (SAW): “My father died and left behind wealth, but he did not make a will. Will it expiate for him if I gi
- #2709 [0.9233] It was narrated from Abu Hurairah that the Messenger of Allah (SAW) said: “Allah (SWT) has been charitable with you over the disposal of one third of your wealth at the time of you

**The Chapters on Charity** (cohesion: 0.8897)
- #2406 [0.9387] It was narrated from Ibn 'Abbas: That during the time of the Messenger of Allah (SAW), a man pursued a debtor who owed him ten Dinar, and he said: “I do not have anything to give y
- #2425 [0.9364] It was narrated that Ibn 'Abbas said: “A man came to ask the Prophet of Allah (SAW) for some debt or some right, and he spoke harshly to him, and the Companions of the Messenger of
- #2409 [0.93] It was narrated from 'Abdullah bin Ja'far that the Messenger of Allah (SAW) said: “Allah will be the borrower until he pays off his debt, so long as it (the loan) is not for someth

**Fasting** (cohesion: 0.8895)
- #1733 [0.9451] It was narrated that ‘Aishah said: “The Messenger of Allah (saw) used to fast ‘Ashura’, and he ordered (others) to fast it too.”
- #1747 [0.9387] It was narrated that ‘Abdullah bin Zubair said: “The Messenger of Allah (saw) broke his fast with Sa’d bin Mu’adh and said: ‘Aftara ‘indakumus-saimun, wa akala ta’amakumul-abrar, w
- #1691 [0.938] It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “When anyone of you is fasting, let him not utter evil or ignorant speech. If anyone speaks to him in an i

**The Chapters on Lost Property** (cohesion: 0.8894)
- #2505 [0.9277] It was narrated from 'Iyad bin Himar that the Messenger of Allah (SAW) said: “Whoever finds lost property, let him ask one or two men of good character to witness it, then he shoul
- #2507 [0.9262] It was narrated from Zaid bin Khalid Al-Juhani that the Messenger of Allah (SAW) was asked about lost property. : He said: “Announce it for a year, then if someone describes it wit
- #2510 [0.8979] It was narrated from Ibn`Abbas that the Messenger of Allah (SAW) said: “One fifth is due on buried treasure.”

**The Chapters on Manumission (of Slaves)** (cohesion: 0.8885)
- #2529 [0.9482] It was narrated from Ibn`Umar that the Messenger of Allah (SAW) said: “Whoever frees a slave who has some wealth, the slave's wealth belongs to him, unless the master stipulates th
- #2527 [0.9257] It was narrated from Abu Hurairah that the Messenger of Allah (SAW) said: “Whoever frees his share of a slave or part of his share, must pay from his wealth if he has any wealth if
- #2515 [0.9212] It was narrated from Ibn`Abbas that the Messenger of Allah (SAW) said: “Any man whose slave won an bears him a child, she will be free after he dies.”

**The Chapters on Pre-emption** (cohesion: 0.8883)
- #2494 [0.9221] It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him even if he is absent, if they
- #2495 [0.9101] It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”
- #2496 [0.9047] It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has neighbors?' He said: 'The neighb

**Chapters on Sacrifices** (cohesion: 0.8871)
- #3138 [0.9468] It was narrated from ‘Uqbah bin ‘Amir Al-Juhani that the Messenger of Allah (saw) gave him some sheep, and he distributed them among his Companions to be sacrificed. There remained
- #3122 [0.9304] It was narrated from ‘Aishah and Abu Hurairah that when the Messenger of Allah (saw) wanted to offer a sacrifice, he brought two large, fat, horned, black-and-white, castrated rams
- #3147 [0.9234] It was narrated that ‘Ata’ bin Yasar said: “I asked Abu Ayyub Al- Ansari: ‘How were sacrifices offered among you at the time of the Messenger of Allah (saw)?’ He said: ‘At the time

**Chapters on Drinks** (cohesion: 0.8849)
- #3373 [0.9347] It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “Whoever drinks wine in this world, he will not drink it in the Hereafter, unless he repents.”
- #3374 [0.9339] Abu Hurairah narrated that the Messenger of Allah (saw) said: “Whoever drinks wine in this world, he will not drink it in the Hereafter.”
- #3421 [0.9319] It was narrated that Ibn ‘Abbas said: “The Messenger of Allah (saw) forbade drinking (directly) from the mouth of a water skin.”

**Chapters on Food** (cohesion: 0.8817)
- #3275 [0.9402] ‘Abdullah bin Busr narrated that the Messenger of Allah (saw) was brought a bowl (of food). The Messenger of Allah (saw) said: “Eat from the sides and leave the top, so that it may
- #3274 [0.9374] It was narrated that ‘Ikrash bin Dhu’aib said: “The Prophet (saw) was brought a bowl filled with Tharid and fatty meat, and we started to eat from it. My hand was wandering all ove
- #3264 [0.9362] It was narrated that ‘Aishah said: “The Messenger of Allah (saw) was eating food with six of his Companions when a Bedouin came and ate it all in two bites. The Messenger of Allah 

**Supplication** (cohesion: 0.8811)
- #3833 [0.9365] It was narrated that Abu Hurairah said: "The Messenger of Allah (saas) used to say: 'Allahummanfa'ni bima 'allamtani, wa 'allimni ma yanfa'uni, wa zidni 'ilman, wal-hamdu lillahi '
- #3838 [0.924] It was narrated from 'Aishah that the : Prophet (saas) would supplicate with these words: "Allahumma inni a'udhu bika min fitnatin-nari wa 'adhabin-nar, wa min fitnatil-qabri wa 'a
- #3872 [0.9186] It was narrated from 'Abdullah bin Buraidah that : his father said: "The Messenger of Allah (saas) said: Allahumma Anta Rabbi la ilaha illa Anta, khalaqtani wa ana 'abduka wa ana '

**Chapters on Hunting** (cohesion: 0.8777)
- #3207 [0.9287] It was narrated that Abu Tha’labah Al-Khushani said: “I came to the Messenger of Allah (saw) and said: ‘O Messenger of Allah, we live in a land of the People of the Book and we eat
- #3214 [0.9245] It was narrated that ‘Adi bin Hatim said: “I asked the Messenger of Allah (saw) about hunting with Mi’rad. He said: ‘Whatever it struck with its sharp edge, then eat it, but what i
- #3208 [0.9224] It was narrated that ‘Adi bin Hatim said: “I asked the Messenger of Allah (saw): ‘We are people who hunt with these dogs.’ He said: ‘If you send out your trained dogs and mention t

**The Chapters on Expiation** (cohesion: 0.8754)
- #2105 [0.937] It was narrated from Ibn 'Umar that the Messenger of Allah (SAW) said: "Whoever swears an oath and says In sha' Allah, if he wishes he may go ahead and if he wishes he may not, wit
- #2117 [0.927] It was narrated from Ibn 'Abbas that the Messenger of Allah (SAW) said: 'When anyone of you swears an oath, let him not say: 'What Allah wills and what you will.' Rather let him sa
- #2101 [0.9269] It was narrated that Ibn 'Umar said: "The Messenger of Allah (SAW) heard a man taking an oath by his father and said: 'Do not make oaths by your forefathers. Whoever makes an oath 

**Chapters on Slaughtering** (cohesion: 0.8733)
- #3179 [0.9108] It was narrated from Abu Sa’eed Al-Khudri that the Messenger of Allah (saw) passed by a boy who was skinning a sheep. The Messenger of Allah (saw) said to him: “Step aside and I wi
- #3172 [0.91] It was narrated that ‘Abdullah bin ‘Umar said: “The Messenger of Allah (saw) commanded that the blade should be sharpened, and hidden from the animals, and he said: ‘When one of yo
- #3180 [0.9054] It was narrated from Abu Hurairah that the Messenger of Allah (saw) came to a man from among the Ansar who had picked up a knife to slaughter an animal for the Messenger of Allah (

**Chapters Regarding Funerals** (cohesion: 0.8729)
- #1462 [0.9327] It was narrated from ‘Ali that the Messenger of Allah (SAW) said: “Whoever washes a deceased person, shrouds him, embalms him, carries him and offers the funeral prayer for him, an
- #1578 [0.9313] It was narrated that ‘Ali said: “The Messenger of Allah (SAW) went out and saw some women sitting, and he said: ‘What are you sitting here for?’ They said: ‘We are waiting for the 
- #1499 [0.9274] It was narrated that Wathilah bin Asqa’ said: “The Messenger of Allah (SAW) offered the funeral prayer for a man among the Muslims and I heard him say: ‘O Allah, so-and-so the son 

**Establishing the Prayer and the Sunnah Regarding Them** (cohesion: 0.8728)
- #1237 [0.9357] It was narrated that ‘Aishah said: “The Messenger of Allah (saw) fell ill and some of his Companions came to visit him. The Messenger of Allah (saw) performed prayer while sitting 
- #1191 [0.9308] It was narrated that Sa’d bin Hisham said: “I asked ‘Aishah: ‘O Mother of the Believers! Tell me about the Witr of the Messenger of Allah (saw).’ She said: ‘We used to keep his too
- #1153 [0.9284] It was narrated that ‘Abdullah bin Malik bin Buhainah said: “The Prophet (saw) passed by a man who was praying when the Iqamah for Subh prayer had been called, and he said somethin

**Zuhd** (cohesion: 0.8722)
- #4133 [0.9226] It was narrated from ‘Amr bin Ghailan Ath-Thaqafi that the Messenger of Allah (saw) said: “O Allah, whoever believes in my and knows that what I have brought is the truth from You,
- #4217 [0.9167] It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “O Abu Hurairah, be cautious, and you will be the most devoted of people to Allah. Be content, and you wil
- #4174 [0.9142] It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “Allah, the Glorified, says: ‘Pride is My cloak and greatness My robe, and whoever competes with Me with r

**Tribulations** (cohesion: 0.8713)
- #3979 [0.9261] It was narrated from Hudhaifah bin Yaman that the Messenger of Allah (saw) said: “There will be callers at the gates of Hell; whoever responds to them they throw them into it.” I s
- #3957 [0.9188] It was narrated from ‘Abdullah bin ‘Amr that the Messenger of Allah (saw) said: “How will you be at a time that will soon come, when the good people will pass away and only the wor
- #3928 [0.915] It was narrated from Jabir that the Messenger of Allah (saw) said: “I have been commanded to fight the people until they say: La ilaha illallah. If they say: La ilaha illallah, the

**The Chapters on Legal Punishments** (cohesion: 0.8698)
- #2549 [0.9201] It was narrated that Abu Hurairah, Zaid bin Khalid and Shibl said: “We were with the Messenger of Allah (SAW) and a man came to him and said: 'I adjure you by Allah (SWT)  to judge
- #2605 [0.915] It was narrated from Abu Hurairah that Sa'd bin Ubadah Al-Ansari said: “O Messenger of Allah (SAW) if a man finds another man with his wife, should he kill him?” The Messenger of A
- #2534 [0.9105] It was narrated from 'Abdullah, who is Ibn Mas`ud, that the Messenger of Allah (SAW) said: “It is not lawful to shed the blood of a Muslim who bears witness that none has the right

**The Chapters on Blood Money** (cohesion: 0.8694)
- #2624 [0.9295] It was narrated from Abu Hurairah that the Messenger of Allah (SAW) said: “If a person's relative is killed, he has the choice of two things: He may either have the killer killed, 
- #2626 [0.9212] It was narrated from 'Amr bin Shu'aib, from this father, from his grandfather that the Messenger of Allah (SAW) said: “Whoever kills deliberately, he will be handed over to the hei
- #2623 [0.9182] It was narrated from Abu Sharaih Al-Khuzai that the Messenger of Allah (SAW) said: “Whoever suffers from killing or wounding, has the choice of three things, and if he wants the fo

**Chapters on Medicine** (cohesion: 0.868)
- #3520 [0.9351] It was narrated that ‘Aishah said: “When the Messenger of Allah (saw) came to a sick person, he would make supplication for him, and would say: Adhhibil-bas, Rabban-nas, washfi Ant
- #3470 [0.9295] It was narrated from Abu Hurairah that the Prophet (saw) visited a sick person, due to an illness that he was suffering from and Abu Hurairah was with him. The Messenger of Allah (
- #3527 [0.919] It was narrated from ‘Umair that he heard Junadah bin Abu Umayyah say: “I heard ‘Ubadah bin Samit say: ‘Jibra’il (as) came to the Prophet (saw) when he was suffering from fever and

**The Chapters on Rulings** (cohesion: 0.8672)
- #2318 [0.931] It was narrated from Abu Hurairah that the Messenger of Allah (SAW) said: “I am only human, and some of you may be more eloquent in presenting your case than others. If I pass a ju
- #2317 [0.9255] It was narrated from Umm Salamah that the Messenger of Allah (SAW) said: “You refer your disputes to me and I am only human. Perhaps some of you may be more eloquent in presenting 
- #2321 [0.9219] It was narrated from Ibn 'Abbas that the Messenger of Allah (SAW) said: “If the people were given what they claimed, some would have claimed the lives and property of men. But the 

**Chapters on <i>Hajj</i> Rituals** (cohesion: 0.8669)
- #2903 [0.9264] It was narrated from Ibn ‘Abbas that the Messenger of Allah (saw) heard a man saying: “Labbaik ‘an Shubrumah (Here I am (O Allah) on behalf of Shubrumah.” The Messenger of Allah (s
- #2896 [0.9214] It was narrated that Ibn ‘Umar said: “A man stood up and said to the Prophet (saw): ‘O Messenger of Allah! What makes Hajj obligatory?’ He said: ‘Provision and a mount.’ He said: ‘
- #2981 [0.9176] It was narrated that ‘Aishah said: “We went out with the Messenger of Allah (saw) when there were five nights left of Dhul-Qa’dah, intending only to perform Hajj. When we came clos

**Chapters on Dress** (cohesion: 0.8654)
- #3597 [0.9304] It was narrated that ‘Abdullah bin ‘Umar said: “The Messenger of Allah (saw) came out to us, and in one of his hands was a garment of silk and in the other was some gold. He said: 
- #3577 [0.9236] It was narrated that Ibn ‘Abbas said: “The Messenger of Allah (saw) used to wear a shirt that was short in the sleeves and length.”
- #3635 [0.9204] It was narrated that ‘Aishah said: “The Messenger of Allah (saw) had hair that came between his earlobes and his shoulders.”

**The Chapters on Pawning** (cohesion: 0.8643)
- #2452 [0.9355] It was narrated from Abu Hurairah that the Messenger of Allah (SAW) said: “Whoever has land, let him cultivate it (himself) or let him give it to his brother (for free, to cultivat
- #2457 [0.9225] It was narrated from Ibn 'Abbas that the Messenger of Allah (SAW) said: “If one of you were to lend his brother his land, it would be better for him than taking such and such rent 
- #2465 [0.9213] It was narrated that Rafi` bin khadij said: We used to give land in return for food at the time of the Messenger of Allah (SAW), and some of my paternal uncles came to them and sai

**The Book of the Adhan and the Sunnah Regarding It** (cohesion: 0.8615)
- #717 [0.9058] It was narrated that Ziyad bin Harith As-Suda'i said: "I was with the Messenger of Allah on a journey, and he commanded me to call the Adhan. Bilal wanted to call the Iqamah, but t
- #718 [0.9038] It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'When the Mu'adh-dhin calls the Adhan, say as he says.'"
- #708 [0.8995] Ibn Juraij narrated: "Abdul-'Aziz bin 'Abdul-Malik bin Abu Mahdhurah narrated from 'Abdullah bin muhairiz who was an orphan under the care of Abu Mahdhurah bin mi'yar that when he 

**The Chapters on Jihad** (cohesion: 0.8607)
- #2766 [0.9166] It was narrated that ‘Abdullah bin Zubair said: “Uthman bin ‘Affan addressed the people and said: ‘O people! I heard a Hadith from the Messenger of Allah (saw) and nothing kept me 
- #2826 [0.9165] It was narrated that Ibn ‘Umar said: “When the Messenger of Allah (saw) would dispatch troops, he would say to the leader: ‘I commend to Allah’s keeping your religious commitment, 
- #2857 [0.9151] It was narrated that Safwan bin ‘Assil said: “The Messenger of Allah (saw) sent us in a military detachment and said: ‘Go in the Name of Allah, and in the cause of Allah. Fight tho

**The Chapters Regarding Zakat** (cohesion: 0.8571)
- #1840 [0.9028] Abdullah bin Mas'ud narrated that: the Messenger of Allah said: “Whoever begs when he has enough to suffice him, his begging will come on the Day of Resurrection like lacerations o
- #1784 [0.8976] 'Abdullah bin Masud (RAH) narrated that: the Messenger of Allah said: “There is no one who does not pay Zakat on his wealth but a bald headed snake will be made to appear to him on
- #1797 [0.8971] Abu Hurairah narrated that  : the Messenger of Allah(saw) said: “When you give Zakat, do not forget its reward, and say 'Allahummaj-'alha maghnaman wa la taj-'alha maghrama (O Alla

**The Chapters on Divorce** (cohesion: 0.8519)
- #2081 [0.9134] It was narrated that Ibn 'Abbas said: "A man came to the Prophet (SAW) and said: 'O Messenger of Allah, my master married me to his slave woman, and now he wants to separate me and
- #2080 [0.8961] It was narrated from 'Aishah that the Prophet (SAW) said: "The divorce of a slave woman is twice, and her (waiting) period is two menstrual cycles." Abu 'Asim said: "I mentioned th
- #2032 [0.8951] It was narrated from Hisham bin 'Urwah that his father said: "I entered upon Marwan and said to him: 'A women from your family has been divorced. I passed by her and she was moving

**The Book of Purification and its Sunnah** (cohesion: 0.8508)
- #268 [0.9154] It was narrated that 'Aishah said: "The Messenger of Allah used to perform ablution with a Mudd (of water) and bath with a Sa'."
- #503 [0.9126] It was narrated from 'Aishah: "The Messenger of Allah would perform ablution, then he would kiss, then he would perform prayer without performing ablution again. And sometimes he d
- #506 [0.9123] It was narrated that Sahl bin Hunaif said: "I used to suffer from a great deal of prostatic fluid, and I took many baths because of that. I asked the messenger of Allah about that,

**The Book of the Prayer** (cohesion: 0.849)
- #697 [0.8894] It was narrated from Abu Hurairah that : When the Messenger of Allah was coming back from the battle of Khaibar, night came and he felt sleepy, so he made camp and said to Bilal: "
- #693 [0.8865] It was narrated that Abu Sa'eed said: "The Messenger of Allah led us for the Maghrib prayer. Then he did not come out until half the night had passed. Then he came out and led them
- #691 [0.8788] It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Were it not that it would be too difficult for my Ummah, I would have delayed the 'Isha' prayer until one thi

**The Chapters on Marriage** (cohesion: 0.8464)
- #1866 [0.9096] It was narrated that: Mughirah bin Shubah said: “I came to the Prophet and told him of a woman to whom I had to propose marriage. He said: 'Go and look at her, for that is more lik
- #1846 [0.9088] It was narrated from Aishah that: the Messenger of Allah said: “Marriage is part of my sunnah, and whoever does not follow my sunnah has nothing to do with me. Get married, for I w
- #1882 [0.908] It was narrated from Abu Hurairah that: the Messenger of Allah said: “No woman should arrange the marriage of another woman, and no woman should arrange her own marriage. The adult

**The Book On The Mosques And The Congregations** (cohesion: 0.8452)
- #799 [0.9072] It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'When one of you enters the mosque, he is in a state of prayer, so long as the prayer keeps him there, and the
- #802 [0.9023] It was narrated from Abu Sa'eed that: The Messenger of Allah said: "If you see a man frequenting the mosques, then bear witness to his faith. Allah says: 'The mosques of Allah shal
- #774 [0.9015] It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'When one of you performs ablution and does it well, then he comes to the mosque with no other motive but pray

**The Chapters on Business Transactions** (cohesion: 0.8449)
- #2184 [0.9234] It was narrated that Jabir bin' Abdullah said: "The Messenger of Allah (SAW) bought a load of fodder from a Bedouin man. When the transaction was concluded, the Messenger of Allah 
- #2252 [0.9003] It was narrated from 'Amr bin Shu'aib from his father that his grandfather told that the Messenger of Allah (SAW) said: "When anyone of you buys a slave woman let him say: 'Allahum
- #2224 [0.8998] It was narrated that Abu Hurairah said: "The Messenger of Allah (SAW) passed by a man who was selling food. He put his hand in it and saw that there was something wrong with it. Th

**Etiquette** (cohesion: 0.8368)
- #3794 [0.8955] It was narrated from Abu Hurairah and Abu Saeed bore witness that the Messenger of Allah(SAW) said: "If a person says: 'La ilaha illallahu wa Allahu Akbar (None has the right to be
- #3813 [0.8928] It was narrated that Abu Darda' said: "The Messenger of Allah (SAW) said to me: 'You should recite Subhan-Allah, wal-Hamdu-Lillah, wa la ilahah illallah, wa Allahu Akbar (Glory is 
- #3798 [0.8887] It was narrated from Abu Hurairah that : the Messenger of Allah(SAW) said: "Whoever says one hundered times each day: La ilaha illahu wahdahu la sharikalahu, wa lahul-mulku wa lahu

### mishkat (22 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Oaths and Vows | 24 | 0.8917 |
| Inheritance and Wills | 37 | 0.8844 |
| Retaliation | 39 | 0.8815 |
| The Excellent Qualities of the Qur'an | 112 | 0.8775 |
| Knowledge | 75 | 0.8727 |
| Fasting | 148 | 0.8726 |
| Faith | 188 | 0.8721 |
| Supplications | 272 | 0.87 |
| Prescribed Punishments | 100 | 0.8676 |
| Purification | 258 | 0.8663 |
| Jihad | 121 | 0.8655 |
| Zakat | 180 | 0.864 |
| Funerals | 243 | 0.8623 |
| Prayer | 921 | 0.8622 |
| The Offices of Commander and Qadi | 94 | 0.8603 |
| Clothing | 135 | 0.8579 |
| Foods | 93 | 0.8572 |
| The Rites of Pilgrimage | 274 | 0.8542 |
| Marriage | 293 | 0.8531 |
| Game and Animals Which May Be Slaughtered | 273 | 0.85 |
| Medicine and Spells | 198 | 0.847 |
| Visions | 88 | 0.8426 |

#### Representative hadiths per book

**Oaths and Vows** (cohesion: 0.8917)
- #3396 [0.9439] Ibn ‘Umar reported God’s Messenger as saying, “If anyone emancipates a slave who owns property he gets the slave’s property, unless the master stipulates otherwise.”   Abu Dawud an
- #3388 [0.9286] Ibn ‘Umar reported God’s Messenger as saying, “If anyone emancipates his share in a slave and has enough money to pay the full price for him, a fair price for the slave should be f
- #3389 [0.9268] Abu Huraira reported the Prophet as saying, “If anyone emancipates a share in a slave, he is to be completely emancipated if he has money; but if he has none, the slave will be req

**Inheritance and Wills** (cohesion: 0.8844)
- #3078, 3079 [0.9172] Anas reported God’s Messenger as saying, “If anyone deprives an heir of his inheritance, God will deprive him of his inheritance in paradise on the day of resurrection.”   Ibn Maja
- #3052 [0.9154] Al-Miqdam reported God’s Messenger as saying, “I am nearer to every believer than himself, so if anyone leaves a debt or a helpless family I shall be responsible, but if anyone lea
- #3057 [0.9151] ‘Ali said: You recite this verse, “After a legacy you bequeathe or a debt (Al-Qur’an 4:12),’’ but God’s Messenger decided that a debt should be discharged before a legacy and that 

**Retaliation** (cohesion: 0.8815)
- #3411 [0.9292] Abu Musa reported God’s Messenger as saying, “I swear by God that if God will, I shall not swear an oath and then consider something else to be better than it without making atonem
- #3435 [0.9215] ‘A'isha reported God’s Messenger as saying, “No vow must be taken to do an act of disobedience, and the atonement for it is the same as for an oath.”   Abu Dawud, Tirmidhi and Nasa
- #3413 [0.921] Abu Huraira reported God’s Messenger as saying, "If anyone swears an oath and considers something else to be better than it he should make atonement for his oath and do that.”   Mu

**The Excellent Qualities of the Qur'an** (cohesion: 0.8775)
- #2134 [0.9304] ‘Abdallāh b. ‘Amr reported God’s messenger as saying, “The one who was devoted to the Qur’ān will be told to recite, ascend and recite carefully as he recited carefully when he was
- #2202 [0.9292] ‘Uqba b. ‘Āmir reported God’s messenger as saying, “He who recites the Qur’ān loudly is like him who gives <i>sadaqa</i> openly, and he who recites the Qur’ān quietly is like him w
- #2127, 2128 [0.9287] He reported God’s messenger as saying, “Is any of you incapable of reciting a third of the Qur’ān in a night?” On being asked how they could recite a third of the Qur’ān he replied

**Knowledge** (cohesion: 0.8727)
- #225, 226 [0.9163] Ka'b b. Malik reported God’s messenger as saying, “If anyone seeks knowledge to use it in vying with the learned, or disputing with the foolish, or to attract men’s attention to hi
- #230, 231 [0.9147] Ibn Mas'ud said that he heard God’s messenger saying, “God brighten a man who hears something from us and conveys it to others as he heard it, for many a one to whom it is brought 
- #216 [0.9122] Abu Huraira reported God's messenger as saying, “A word which contains wisdom is the stray beast* of the wise man, so wherever he finds it he is most entitled to it.” Tirmidhi and 

**Fasting** (cohesion: 0.8726)
- #1986 [0.9301] Abu Huraira said that God’s messenger forbade uninterrupted fasting, and when a man said, “You fast uninterruptedly, messenger of God,” he replied, “Which of you is like me? During
- #1970 [0.929] Abu Huraira reported God’s messenger as saying, “Fast when you see it and break your fast when you see it, and if the weather is cloudy treat Sha‘ban as having thirty days.”   (Buk
- #2003 [0.9288] Abu Huraira reported God’s messenger as saying, “If anyone forgets when he is fasting and eats or drinks he should complete his fast, for it is only God who has fed him and given h

**Faith** (cohesion: 0.8721)
- #146 [0.9133] ‘A’isha said: God’s messenger did a certain thing and gave permission for it to be done, but some people abstained from it. When God’s messenger heard of that, he delivered a sermo
- #173 [0.913] Ibn ‘Umar reported God’s messenger as saying, “God will not cause all my people (or he said, Muhammad’s people) to err. God’s hand is over the community, and he who is separate fro
- #194 [0.9101] Jabir told how ‘Umar b. al-Khattab brought God’s messenger a copy of the Torah saying, “Messenger of God, this is a copy of the Torah.” When he received no reply he began to read t

**Supplications** (cohesion: 0.87)
- #2461 [0.9266] ‘Abdallah b. ‘Umar said that one of the supplications of God’s messenger was, “O God, I seek refuge in Thee from the decline of Thy favour, change in Thy granting wellbeing, sudden
- #2462 [0.917] ‘A’isha said that God’s messenger used to say, “O God, I seek refuge in Thee from the evil of what I have done and from the evil of what I have not done.”   Muslim transmitted it.
- #2403 [0.9162] ‘Ali reported that God’s messenger used to say when he lay down, "O God, I seek refuge in Thy noble Person and in Thy perfect words from the evil of what Thou seizest by its forelo

**Prescribed Punishments** (cohesion: 0.8676)
- #3484 [0.9114] Abu Huraira reported God’s Messenger as saying, “If anyone helps in killing a believer to the extent of half a word,* he will meet God with ‘Despairing of God’s mercy’ written on h
- #3449 [0.9093] Al-Miqdad b. al-Aswad told that he said, “Tell me, Messenger of God, supposing I meet an infidel and we fight together and he strikes one of my hands with his sword and cuts it off
- #3478 [0.9081] Ta’us, on the authority of Ibn ‘Abbas, reported God’s Messenger as saying, “If anyone is killed in error when people are throwing stones, or by beating with whips, or striking with

**Purification** (cohesion: 0.8663)
- #458 [0.9318] Ibn ‘Abbas said that a wife of the Prophet washed in a bowl, and when God’s messenger wanted to perform ablution from it she said, “I was defiled, messenger of God.” He replied, “W
- #368 [0.9268] ‘A'isha told of God’s messenger passing water and ‘Umar standing behind him with a jug of water. He said, “What is this, ‘Umar?” He replied, “Water for you to perform ablution with
- #297 [0.9226] ‘Abdallah as-Sunabihi reported God’s messenger as saying, “When a believer performs ablution, then rinses his mouth, the sins go out from his mouth; when he snuffs up water, the si

**Jihad** (cohesion: 0.8655)
- #3679 [0.9181] ‘Abdallah b. ‘Amr reported God’s Messenger as saying, “If anyone swears allegiance to an <i>imam</i>, giving him his hand in ratification and sincere agreement in his heart, he mus
- #3741 [0.9169] 'Abdallah b. Abu Aufa reported God’s Messenger as saying, “God is with the <i>qadi</i> as long as he is not tyrannical, but when he is He departs from him and the devil attaches hi
- #3761 [0.9124] Umm Salama reported God’s Messenger as saying, “I am only a human being and you bring your disputes to me, some perhaps being more eloquent in their plea than others, so that I giv

**Zakat** (cohesion: 0.864)
- #1795 [0.9241] Abu Huraira reported God’s messenger as saying,  “No <i>sadaqa</i> is due from a Muslim on his slave or his horse.”  In a version he said, “There is no <i>sadaqa</i> on his slave e
- #1888 [0.9231] Abu Huraira reported God’s messenger as saying,  “If anyone gives as <i>sadaqa</i> the equivalent of a date from something lawfully earned, for God accepts only what is lawful, God
- #1939 [0.9214] Sulaiman b. ‘Amir reported God’s messenger as saying,  “<i>Sadaqa</i> given to a poor man is just <i>sadaqa</i>, but when given to a relative it serves a double purpose, being both

**Funerals** (cohesion: 0.8623)
- #1646 [0.9157] Abu Huraira reported God’s messenger as saying, “Walk quickly at a funeral, for if the dead person was good it is a good condition to which you are sending him on, but if he was ot
- #1647 [0.9138] Abu Sa'id reported God’s messenger as saying, “When a corpse is placed on a bier and men carry it on their shoulders, if it was a good man it says, ‘Take me quickly’; but if it was
- #1664 [0.9112] ‘A’isha reported God’s messenger as saying, “Do not revile the dead, for they have come to what they have sent before them.”   Bukhari transmitted it.

**Prayer** (cohesion: 0.8622)
- #1255 [0.9224] He reported God’s Messenger as saying, “The <i>witr</i>* is a <i>rak'a</i> at the end of the night.”   * Literally ‘single’, or ‘odd’, used of an odd number of <i>rak'as</i> prayed
- #583 [0.9172] Ibn ‘Abbas reported God’s Messenger as saying, “Gabriel twice led me in prayer at the House (i.e. the Ka’ba). He prayed the noon prayer with me when the sun had passed the meridian
- #710, 711 [0.9171] Abu Huraira reported God’s Messenger as saying, “When one of you gets up for prayer he must not spit in front, of him, because he is holding intimate converse with God as long as h

**The Offices of Commander and Qadi** (cohesion: 0.8603)
- #3633 [0.914] ‘Umar reported God’s Messenger as saying, “When you find a man has been unfaithful about spoil in God’s path, burn his goods and beat him.”   Tirmidhi and Abu Dawud transmitted it,
- #3617, 3618, 3619 [0.9115] Jabir reported the Prophet as saying, “Beat anyone who drinks wine, and if he does it a fourth time kill him.” He said that after that a man who had drunk wine four times was broug
- #3657, 3658, 3659 [0.9044] Ibn ‘Abbas reported God’s Messenger as saying, “If one who is addicted to wine dies he will meet God most high in the same condition as an idolater.”   Ahmad transmitted it, Ibn Ma

**Clothing** (cohesion: 0.8579)
- #4283 [0.927] Ibn ‘Abbas reported God’s messenger as saying, “When one of you eats food he should say, ‘O God, bless us in it and give us good nourishment from it', and when he is given a drink 
- #4201 [0.9178] Abu Ayyub said: We were with the Prophet when food was presented to him, and I never saw food which had greater blessing when we began to eat, or less when we finished. We asked Go
- #4213 [0.9144] ‘Abdallah b. al-Harith b. Jaz’ said: God’s messenger was brought some bread and meat when he was in the mosque, and he ate and we ate along with him. He then stood up and prayed an

**Foods** (cohesion: 0.8572)
- #4083 [0.9181] ‘Adi b. Hatim reported the Prophet as saying, “Eat whatever is caught for you by a dog or a hawk which you have trained and set off when you have mentioned God’s name.” He asked wh
- #4065 [0.9133] He said he told God’s messenger that he set off trained dogs, and he replied, “Eat what they catch for you.” He asked if that applied even if they killed the game, and he replied t
- #4126 [0.9074] Ibn ‘Umar told that God's messenger prohibited eating the animal which feeds on filth or drinking its milk.   Trimidhi transmitted it. In Abu Dawud’s version he said that he forbad

**The Rites of Pilgrimage** (cohesion: 0.8542)
- #2910 [0.9097] Abu Huraira reported the Prophet as saying, “If anyone accepts other people’s belongings meaning to pay back, God will pay back for him; but if anyone accepts them meaning to squan
- #3036 [0.909] ‘Amr b. Shu'aib, on his father’s authority, said his grandfather told that God’s Messenger was asked about hanging fruit and said, “If a needy person takes some and does not take a
- #3011 [0.908] He reported God’s Messenger as saying, “If anyone has property [[given him for the use of himself and his descendants it belongs to the one to whom it is given and does not return 

**Marriage** (cohesion: 0.8531)
- #3378 [0.9102] ‘Amr b. Shu'aib, on his father’s authority, said his grandfather,‘Abdallah b. ‘Amr, told of a woman who said, “Messenger of God, my womb was a vessel to this son of mine, my breast
- #3308 [0.9087] Abu Huraira told that Sa'd b. ‘Ubada asked, “If I were to find a man with my wife, should I not touch him before bringing four witnesses?” Then when God’s Messenger replied that th
- #3317 [0.9068] Ibn ‘Abbas told of a man coming to the Prophet and saying, “I have a wife who rejects no one who wishes intercourse with her,” but when he told him to divorce her he replied that h

**Game and Animals Which May Be Slaughtered** (cohesion: 0.85)
- #3796 [0.9072] He reported God’s Messenger as saying, “One of the best types of subsistence is that of a man who grasps his horse’s rein in (God’s path and races on its back, making for the place
- #3846 [0.9037] Mu'adh reported God’s Messenger as saying, “Fighting is of two kinds. The one who seeks God’s favour, obeys the leader, gives property he values, helps his associate and avoids doi
- #4033 [0.9036] Abu Huraira reported God’s Messenger as saying, “A prophet who went out on an expedition told his people that no man should follow him who had married a woman with whom he wished t

**Medicine and Spells** (cohesion: 0.847)
- #4322 [0.9066] ‘Ali told that God’s messenger was presented with a striped robe containing silk and sent it to him, but when ‘Ali wore it he saw he was looking angry. He then said, “I did not sen
- #4342 [0.9015] Abu Sa'id al-Khudri told that when God's messenger put on a new garment he mentioned it by name, turban, shirt, or cloak, and would then say, “O God, praise be to Thee ! As Thou ha
- #4346 [0.9003] Ibn ‘Umar reported God’s messenger as saying, “He who wears grand clothes in this world will be made by God to wear humble clothes on the day of resurrection.”  Ahmad, Abu Dawud an

**Visions** (cohesion: 0.8426)
- #4514 [0.9068] Abu Huraira reported God’s messenger as saying: “God has not sent down a disease without sending down remedy for it.”   Bukhari transmitted it.
- #4542 [0.8979] Abu Kabsha al-Anmari told that God’s messenger used to have himself cupped on the top of his head and between his shoulders and that he used to say: “If anyone pours out any of thi
- #4548 [0.8942] Abu Huraira reported God’s messenger as saying, “If anyone has himself cupped on the 17th, 19th, and 21st, it will be a remedy for every disease.”   Abu Dawud transmitted it.

### muslim (43 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| The Book of Vows | 11 | 0.9005 |
| The Book of Musaqah | 31 | 0.9002 |
| The Book of Emancipating Slaves | 19 | 0.8876 |
| The Book of Tribulations and Portents of the Last Hour | 11 | 0.886 |
| The Book on Government | 30 | 0.8838 |
| The Book of the Merits of the Companions | 20 | 0.8796 |
| The Book of <i>Jihad</i> and Expeditions | 27 | 0.8795 |
| The Book of Clothes and Adornment | 41 | 0.874 |
| The Book Pertaining to the Remembrance of Allah, Supplication, Repentance and Seeking Forgiveness | 62 | 0.8694 |
| The Book of Virtues | 28 | 0.8659 |
| The Book of <i>Zuhd</i> and Softening of Hearts | 41 | 0.8659 |
| The Book of Paradise, its Description, its Bounties and its Inhabitants | 23 | 0.8651 |
| The Book of Lost Property | 87 | 0.8647 |
| The Book of Drinks | 23 | 0.8637 |
| The Book of Greetings | 18 | 0.8636 |
| The Book of Wills | 285 | 0.8631 |
| The Book of Manners and Etiquette | 31 | 0.8617 |
| The Book of Legal Punishments | 84 | 0.8612 |
| The Book Concerning the Use of Correct Words | 88 | 0.8572 |
| The Book of Hunting, Slaughter, and what may be Eaten | 160 | 0.8567 |
| The Book of Suckling | 24 | 0.8543 |
| The Book of Poetry | 56 | 0.8539 |
| The Book of I'tikaf | 378 | 0.8531 |
| The Book of Menstruation | 157 | 0.853 |
| The Book of Dreams | 72 | 0.8523 |
| The Book of Knowledge | 92 | 0.8522 |
| The Book of Oaths, <i>Muharibin</i>, <i>Qasas</i> (Retaliation), and <i>Diyat</i> (Blood Money) | 169 | 0.8516 |
| The Book of Purification | 144 | 0.8514 |
| The Book of Pilgrimage | 93 | 0.8505 |
| The Book of Prayer - Funerals | 322 | 0.8504 |
| The Book of Sacrifices | 178 | 0.8486 |
| The Book of Faith | 439 | 0.847 |
| The Book of Oaths | 601 | 0.8469 |
| The Book of Zakat | 402 | 0.8461 |
| The Book of Gifts | 231 | 0.8445 |
| The Book of Virtue, Enjoining Good Manners, and Joining of the Ties of Kinship | 182 | 0.8423 |
| The Book of Heart-Melting Traditions | 257 | 0.8417 |
| Characteristics of The Hypocrites And Rulings Concerning Them | 60 | 0.8411 |
| The Book of the Rules of Inheritance | 138 | 0.8401 |
| The Book of Commentary on the Qur'an | 226 | 0.8399 |
| The Book of Repentance | 193 | 0.8372 |
| Characteristics of the Day of Judgment, Paradise, and Hell | 212 | 0.8365 |
| The Book of Destiny | 266 | 0.8254 |

#### Representative hadiths per book

**The Book of Vows** (cohesion: 0.9005)
- #1172 a [0.9631] 'A'isha (Allah be pleased with her) reported that the Messenger of Allah (may peace be upon him) used to observe i'tikaf in the last ten days of Ramadan.
- #1172 c [0.9565] 'A'isha (Allah be pleased with her) reported that the Messenger of Allah (may peace he upon him) used to observe i'tikif in the last ten days of Ramadan till Allah called him back 
- #1175 [0.9239] 'A'isha (Allah be pleased with her) reported that Allah's Messenger (may peace be upon him) used to exert himself in devotion during the last ten nights to a greater extent than at

**The Book of Musaqah** (cohesion: 0.9002)
- #901 c [0.9586] 'A'isha, the wife of the Apostle of Allah (may peace be upon him), reported There was an eclipse of the sun during the lifetime of the Messenger of Allah (may peace be upon him). S
- #901 f [0.9518] 'Ata' reported: I heard 'Ubaid b. 'Umair say: It has been narrated to me by one whom I regard as truthful, (the narrator says: I can well guess that he meant 'A'isha) that the sun 
- #907 a [0.9486] Ibn 'Abbas reported: There was an eclipse of the sun during the lifetime of the Messenger of Allah (may peace be upon him). The Messenger of Allah, (may peace be upon him) prayed a

**The Book of Emancipating Slaves** (cohesion: 0.8876)
- #899 b [0.9315] 'Ata' b. Rabah reported on the authority of 'A'isha, the wife of the Apostle of Allah (way peace be upon him), who said: Whenever the wind was stormy, the Apostle of Allah (may pea
- #898 [0.9267] Anas (b. Malik) reported: It rained upon us as we were with the Messenger of Allah (may peace be upon him). The Messenger of Allah (way peace be upon him) removed his cloth (from a
- #897 a [0.9199] Anas b. Malik reported that a person entered the mosque through the door situated on theside of Daral-Qada' during Friday (prayer) and the messenger of Allah (may peace be upon him

**The Book of Tribulations and Portents of the Last Hour** (cohesion: 0.886)
- #2256 b [0.934] Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: The truest word uttered by a poet is this verse of Labid: "Behold! apart from Allah everything is vain," a
- #2256 e [0.9291] Abu Huraira reported: I heard Allah's Messenger (may peace be upon him) as saying: The truest word which the poet stated is the word of Labid: "Behold! apart from Allah everything 
- #2256 c [0.9289] Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: The truest verse recited by a poet is: "Behold! apart from Allah everything is vain," and Ibn Abu Salt was

**The Book on Government** (cohesion: 0.8838)
- #1505 [0.943] Abu Huraira (Allah be pleased with him) reported: 'A'isha (Allah be pleated with her) thought of buying a slave-girl and emancipating her, but her owners refused to (sell her but o
- #1504 d [0.9318] 'A'isha (Allah be pleased with her) reported: Barira came to me and said: My family (owners) have made contract with me (for granting freedom) for nine 'uqiyas (of silver) payable 
- #1504 c [0.9265] 'A'isha, the wife of Allah's Apostle (may peace be upon him), reported: Barira came to me and said: 'A'isha, I have entered into contract for securing freedom with my family (who o

**The Book of the Merits of the Companions** (cohesion: 0.8796)
- #1722 b [0.9278] Zaid b. Khalid al-Juhani reported that a person asked Allah's Apostle (may peace be upon him) about picking up of stray articles, whereupon he said: Make announcement about it for 
- #1722 g, h [0.9267] Zaid b. Khalid al-Juhani reported that Allah's Messenger (may peace be upon him) was asked about picking up of stray things, whereupon he said: Make announcement of that for one ye
- #1722 e [0.9206] Zaid b. Khalid al-Juhani, the Companion ot Allah's Messenger (may peace be upon him), said that Allah's Messenger (may peace be upon him) was asked about the picking up of stray go

**The Book of <i>Jihad</i> and Expeditions** (cohesion: 0.8795)
- #1497 a [0.9284] Ibn Abbas (Allah be pleased with them) reported: Mention was made of li'an in the presence of Allah's Messenger (may peace be upon him). And Asim b. 'Adi passed a remark about it a
- #1498 c [0.9198] Abu Huraira (Allah be pleased with him) reported that Sa'd b. Ubada (Allah be pleased with him) said: Messenger of Allah, if I were to find with my wife a man, should I not touch h
- #1494 b [0.9159] Ibn 'Umar (Allah be pleased with them) reported: Allah's Messenger (may peace be upon him) asked a person from the Anger and his wife to invoke curse (upon one another in order to 

**The Book of Clothes and Adornment** (cohesion: 0.874)
- #1625 a [0.931] Jabir b. 'Abdullah (Allah be pleased with them) reported Allah's Messenger (may peace be upon him) as saying: "Any man who is given a gift for life, it belongs to him and his hei
- #1625 i [0.9238] Jabir (b. 'Abdullah) (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) having said: Keep your property to yourselves and do not squander it, for he who
- #1623 i [0.9191] Nu'man b. Bashir (Allah be pleased with them) reported: My father took me to Allah's Messenger (may peace be upon him) and said: Allah's Messenger, bear witness that I have given s

**The Book Pertaining to the Remembrance of Allah, Supplication, Repentance and Seeking Forgiveness** (cohesion: 0.8694)
- #1962 a [0.9307] Anas (b. Malik) reported Allah's Messenger (may peace be upon him) having said on the day of Nahr (Sacrifice): He who slaughtered (the animal as a sacrifice) before the ('Id) praye
- #1961 e [0.9263] Al-Bara' b. 'Azib reported Allah's Messenger (may peace be upon him) having said: The first (act) with which we started our day (the day of 'Id-ul Adha) was that we offered prayer.
- #1961 d [0.9255] Al-Bara' reported Allah's Messenger (may peace be upon him) having said: He who observes prayer like our prayer and turns his face towards our Qibla (in prayer) and who offers sacr

**The Book of Virtues** (cohesion: 0.8659)
- #1713 a [0.9093] Umm Salama reported Allah's Messenger (may peace be upon him) as saying: You bring to me, for (judgment) your disputes, some of you perhaps being more eloquent in their plea than o
- #1714 c [0.9032] A'isha reported that Hind came to Allah's Apostle (may peace be upon him) and said: Messenger of Allah, by Allah, there was no other household upon the surface of the earth than yo
- #1721 [0.8932] Hammim b. Munabbih said: Abu Huraira reported (so many) ahadith of Allah's Messenger (may peace be upon him), and one of them is this: A person bought from another person a piece o

**The Book of <i>Zuhd</i> and Softening of Hearts** (cohesion: 0.8659)
- #2268 d [0.9063] Jabir reported that there came to Allah's Apostle (may peace be upon him) a desert Arab and said: Allah's Messenger, I saw in the state of sleep as if my head had been cut off and 
- #2267 a [0.9055] Abu Qatada reported Allah's Messenger (may peace be upon him) as saying: He who saw me in dream in fact saw the truth (what is true).
- #2269 a [0.9045] It is reported either on the authority of Ibn `Abbas or on the authority of Abu Huraira that a person came to Allah's Messenger (may peace be upon him) and said: Allah's Messenger,

**The Book of Paradise, its Description, its Bounties and its Inhabitants** (cohesion: 0.8651)
- #2249 d [0.9175] Abu Huraira reported Allah's Messenger (may peace be upon him) so many ahadith and one of them is this that Allah's Messenger (may peace be upon him) said: None of you should say: 
- #2247 a [0.9116] Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: None of you should abuse Time for it is Allah Who is the Time, and none of you should call 'Inab (grape) a
- #2249 b [0.9011] Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: None of you should say: My bondman, for all of you are the bondmen of Allah, but say: My young man, and th

**The Book of Lost Property** (cohesion: 0.8647)
- #1480 q [0.9289] Fatima bint Qais (Allah be pleased with her) reported: My husband Abu 'Amr b. Hafs b. al-Mughira sent 'Ayyish b. Abu Rabi'a to me with a divorce, and he also sent through him five 
- #1471 p [0.92] Anas b. Sirin reported that he had heard Ibn 'Umar (Allah be pleased with them) as saying. I divorced my wife while she was in the state of menses. 'Umar (Allah be pleased with him
- #1471 n [0.9153] Ibn 'Umar (Allah be pleased with them) reported: I divorced my wife while she was in the state of menses. 'Umar (Allah he pleased wish him) came toAllah's Apostle (may peace be upo

**The Book of Drinks** (cohesion: 0.8637)
- #1619 d [0.9101] Hammam b. Munabbih reported: This is what Abu Huraira (Allah be pleased with him) narrated to us from Allah's Messenger (may peace he upon him). And he narrated many ahadith, and o
- #1616 c [0.903] Jabir b. 'Abdullah (Allah be pleased with them) reported: While I had been ill Allah's Messenger (may peace be upon him) visited me and Abu akr (Allah be pleased with him) was with
- #1616 a [0.8969] Jabir b. 'Abdullah (Allah be pleased with them) reported: I fell sick and there came to me on foot Allah's Messenger (may peace be upon him) and Abu Bakr for inquiring after my hea

**The Book of Greetings** (cohesion: 0.8636)
- #1640 c [0.9055] Abu Huraira reported Allah's Apostle (may peace be upon him) as saying: The vow does not bring anything near to the son of Adam which Allah has not ordained for him, but (at times)
- #1639 a [0.9015] 'Abdullah b. Umar reported: Allah's Messenger (may peace he upon him) singled out one day forbidding us to take vows and said: It would not avert anything; it is by which something
- #1639 b [0.8991] Ibn Umar reported Allah's Apostle (may peace be upon him) as saying: The vow neither hastens anything nor defers anything, but is the means whereby (something) is extracted from th

**The Book of Wills** (cohesion: 0.8631)
- #1103 a [0.9246] Abu Huraira (Allah be pleased with him) reported: The Messenger of Allah (may peace be upon him) forbade (his Companions) from observing fast uninterruptedly. One of the Muslims sa
- #1162 b [0.9198] Abu Qatada al-Ansari (Allah be pleased with him) reported that the Messenger of Allah (may peace be upon him) was asked about his fasting. The Messenger of Allah (may peace be upon
- #782 c [0.9159] 'A'isha (Allah be pleased with her) reported: The Messenger of Allah (may peace be upon him) did not observe fast in any month of the year more than in the month of Sha'ban, and us

**The Book of Manners and Etiquette** (cohesion: 0.8617)
- #1628 g [0.92] Humaid b. 'Abd al-Rahman al-Himyari reported from three of the sons of Sa'd all of whom reported from their father that Allah's Apostle (may peace be upon him) visited Sa'd as he w
- #1628 a [0.9029] Amir b. Sa'd reported on the authority of his father (Sa'd b. Abi Waqqas): Allah's Messenger (may peace be upon him) visited me in my illness which brought me near death in the yea
- #1629 [0.8991] Ibn 'Abbas (Allah be pleased with them) said: (I wish) if people would reduce from third to fourth (part for making a will of their property), for Allah's Messenger (may peace be u

**The Book of Legal Punishments** (cohesion: 0.8612)
- #1445 b [0.915] 'A'isha (Allah be pleased with her) reported: There came to me Aflah b. Abu Qulais, my uncle by reason of fosterage; the rest of the hadith is the same (but with this) addition:" I
- #1444 a [0.9104] 'A'isha (Allah be pleased with her) reported tha Allah's Messenger (may peace be upon him) was with her and she heard the voice of a person seeking permission to enter the house of
- #1449 c [0.9078] Umm Habiba, the wife of Allah's Apostle (may peace be upon him), reported that she said to Allah's Messenger (may peace be upon him): Messenger of Allah, marry my sister 'Azza, whe

**The Book Concerning the Use of Correct Words** (cohesion: 0.8572)
- #1666 a [0.9078] Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: When a slave fulfils obligation of Allah and obligation of his master, he has two rewards for him. I narra
- #1661 c [0.9009] Ma'rur b. Suwaid reported: I saw Abu Dharr wearing clothes, and his slave wearing similar ones. I asked him about it, and he narrated that he had abused a person during the lifetim
- #1655 [0.8928] Hammam b. Munabbih reported: This is what Abu Huraira reported to us from Allah's Messenger (may peace be upon him), and he narrated a hadith and (one) of them is that Allah's Mess

**The Book of Hunting, Slaughter, and what may be Eaten** (cohesion: 0.8567)
- #1522 a [0.9149] Jabir (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: The townsman should not sell for a man from the desert, leave the people alone, Alla
- #1526 b, 1527 b [0.9142] Ibn Umar (Allah be pleased with them) reported Allah's Messenger (may peace be upon him) as saying: He who buys foodgrain should not sell that before taking possession of it. He (t
- #1526 d [0.9104] Ibn 'Umar (Allah be pleased with them) reported Allah's Messenger (may peace be upon him) as saying,: He who bought foodgrain should not sell it until he had taken possession of it

**The Book of Suckling** (cohesion: 0.8543)
- #885 b [0.9161] Jabir b. 'Abdullah reported: I observed prayer with the Messenger of Allah (may peace be upon him) on the 'Id day. He commenced with prayer before the sermon without Adhan and Iqam
- #884 a [0.9143] Ibn 'Abbas reported: I participated in the Fitr prayer with the Apostle of Allah (may peace be upon him) and Abu Bakr, 'Umar and 'Uthman, and all of them observed this prayer befor
- #892 e [0.9119] `A'isha reported: The Messenger of Allah (may peace be upon him) came (to my apartment) while there were two girls with me singing the song of the Battle of Bu`ath. He lay down on 

**The Book of Poetry** (cohesion: 0.8539)
- #1680 a [0.9102] 'Alqama b. Wa'il reported on the authority of his-father: While I was sitting in the company of Allah's Apostle (may peace be upon him), a person came there dragging another one wi
- #1680 b [0.8996] 'Alaqama b. Wa'il reported on the authority of his father that a person was brought to the Messenger of Allah (may peace be upon him) who had killed another person, and the heir of
- #1676 c [0.8984] 'Abdullah (b. Mas'ud) reported: Allah's Messenger (may peace be upon him) stood up and said: By Him besides Whom there is no god but He, the blood of a Muslim who bears the testimo

**The Book of I'tikaf** (cohesion: 0.8531)
- #749 d [0.9154] 'Abdullah b. 'Umar reported: A person asked the Apostle of Allah (may peace be upon him) as I stood between him (the Holy Prophet) and the inquirer and he said: Messenger of Allah,
- #711 a [0.9132] 'Abdullah b. Malik b. Buhaina reported: The Messenger of Allah (may peace be upon him) happened to pass by a person who was busy in praying while the (Fard of the) dawn prayer had 
- #761 b [0.9052] 'A'isha reported: The Messenger of Allah (may peace be upon him) came out during the night and observed prayer in the mosque and some of the people prayed along with him. When it w

**The Book of Menstruation** (cohesion: 0.853)
- #345 [0.9183] Abu Sa'id al-Khudri reported: The Messenger of Allah (may peace be upon him) happened to pass by (the house) of a man amongst the Ansar, and he sent for him. He came out and water 
- #317 a [0.9165] Ibn 'Abbas reported it on the authority of Maimuna, his mother's sister, that she said: I placed water near the Messenger of Allah (may peace be upon him) to take a bath because of
- #321 a [0.9144] Salama b. Abd al-Rahman narrated it on the authority of A'isha that when the Messenger of Allah (may peace be upon him) took a bath, he started from the right hand and poured water

**The Book of Dreams** (cohesion: 0.8523)
- #1703 b [0.895] This hadith his been narrated on the authority of Abu Huraira through another chain of transmitters with a slight variation of words.
- #1691 c [0.8926] Abu Huraira reported that a person from amongst the Muslims came to Allah's Messenger (may peace be upon him) while he was in the mosque. He called him saying: Allah's Messenger. I
- #1688 b [0.8866] `A'isha, the wife of Allah's Apostle (may peace be upon him), reported that the Quraish were concerned about the woman who had committed theft during the lifetime of Allah's Apostl

**The Book of Knowledge** (cohesion: 0.8522)
- #1945 a [0.9145] 'Abdullah b. 'Abbas reported: I and Khalid b. Walid went to the apartment of Maimuna along with Allah's Messenger (may peace be upon him), and there was presented to him a roasted 
- #1930 a [0.9137] Abu Tha'laba al-Khushani reported: I came to Allah's Messenger (may peace be upon him) and said: Allah's Messenger, we are in the land of the People of the Book, (so) we eat in the
- #1948 [0.9072] Yazid b. al-Asamm reported: A newly wedded person of Medina invited us to a wedding feast, and he served us thirteen lizards. There were those who ate it and those who abandoned it

**The Book of Oaths, <i>Muharibin</i>, <i>Qasas</i> (Retaliation), and <i>Diyat</i> (Blood Money)** (cohesion: 0.8516)
- #1425 a [0.9063] Sahl b. Sa'd al-Sa'idi (Allah be pleased with him) reported: A woman came to Allah's Messenger. (may peace be upon him) and said: Messenger of Allah, I have come to you to entrust 
- #1428 h [0.9049] Anas (Allah be pleased with him) reported: When Allah's Apostle (may peace be upon him) contracted marriage with Zainab (Allah be pleased with bet), Umm Sulaim sent him hats in a v
- #1439 b [0.9041] Jabir b. 'Abdullah (Allah be pleased with them) reported that a person asked Allah's Apostle (may peace be upon him) saying: I have a slave-girl and I practise 'azl with her, where

**The Book of Purification** (cohesion: 0.8514)
- #235a [0.9206] 'Abdullah b. Zaid b. 'Asim al-Ansari, who was a Companion (of the Holy Prophet), reported: It was said to him (by people): Perform for us the ablution (as it was performed) by the 
- #246a [0.9134] Nu'aim b. 'Abdullah al-Mujmir reported: I saw Abu Huraira perform ablution. He washed his face and washed it well. He then washed his right hand including a portion of his arm. He 
- #236 [0.91] 'Abdullah b. Zaid b. 'Asim al-Mazini reported: He saw Allah's Messenger (may peace be upon him) perform the ablution. He rinsed his mouth then cleaned his nose, then washed his fac

**The Book of Pilgrimage** (cohesion: 0.8505)
- #845 a [0.916] 'Abdullah (b. 'Umar) reported from his father that while he was addressing the people on Friday (sermon), a person, one of the Companions of the Messenger of Allah (may peace be up
- #853 [0.8972] Abu Burda b. Abu Musa al-Ash'ari reported: 'Abdullah b. Umar said to me: Did you hear anything from your father narrating something from the messenger of Allah (may peace be upon h
- #875 a [0.8971] Jabir b. 'Abdullah reported that while Allah's Messenger (may peace be upon him) was delivering the sermon on Friday a person came there, and the Apostle of Allah (may peace be upo

**The Book of Prayer - Funerals** (cohesion: 0.8504)
- #397 a [0.912] Abu Huraira reported: The Messenger of Allah (may peace be upon him) entered the mosque and a person also entered therein and offered prayer, and then came and paid salutation to t
- #418 e [0.9116] 'A'isha reported: When the Messenger of Allah (may peace be upon him) came to my house, he said: Ask Abu Bakr to lead people in prayer. 'A'isha narrated: I said, Messenger of Allah
- #484 d [0.9107] 'A'isha reported: The Messenger of Allah (may peace be upon him) recited often these words: Hallowed be Allah and with His praise, I seek the forgiveness of Allah and return to Him

**The Book of Sacrifices** (cohesion: 0.8486)
- #1601 a [0.922] Abu Huraira (Allah be pleased with him) reported: Allah's Messenger (may peace be upon him) owed (something) to a person. He behaved in an uncivil manner with him. This vexed the C
- #1593 b [0.9101] Abu Huraira (Allah be pleased with him) reported that Allah's Messenger (may peace be upon him) deputed a person to collect revenue from Khaibar. He brought fine quality of dates, 
- #1560 d [0.9069] Hudhaifa (Allah be pleased with him) reported: A servant from amongst the servants of Allah was brought to Him whom Allah had endowed with riches. He (Allah) said to him: What (did

**The Book of Faith** (cohesion: 0.847)
- #198 c [0.9047] 'Amr b. Abu Sufyan transmitted a hadith like this from Abu Huraira who narrated it from the Messenger of Allah (may peace be upon him).
- #216 b [0.9031] Muhammad b. Ziyad reported: I heard Abu Huraira narrate this: I heard it from the Messenger of Allah (may peace be upon him) saying a hadith like one narrated by al-Rabi'.
- #83 [0.8988] Abu Huraira reported: The Messenger of Allah was asked about the best of deeds. He observed: Belief in Allah. He (the inquirer) said: What next? He (the Holy Prophet) replied: Jiha

**The Book of Oaths** (cohesion: 0.8469)
- #1221 c [0.9171] Abu Musa (Allah be pleased with him) reported: I came to the Messenger of Allah (may peace be upon him) and he was encamping at Batha. He (the Holy Prophet) said: With what purpose
- #1221 a [0.9161] Abu Musa (Allah be pleased with him) said: I came to the Messenger of Allah (may peace be upon him) as he was encamping at Batha. He said to me: Did you intend to perform Hajj? I s
- #1298 a [0.9139] Umm al-Husain (Allah be pleased with her) reported: I performed Hajj along with Allah's Messenger (may peace be upon him) on the occasion of the Farewell Pilgrimage and saw him whe

**The Book of Zakat** (cohesion: 0.8461)
- #573 b [0.9071] Abu Huraira reported: The Messenger of Allah (may peace be upon him) led us in one of the evening prayers. And this hadith was narrated like one transmitted by Sufyan.
- #573 c [0.9066] Abu Huraira reported: The Messenger of Allah (may peace be upon him) led us in the 'Asr prayer and gave salutation after two rak'ahs. Dhu'l-Yadain (the possessor of long arms) stoo
- #542 [0.9064] Abu Darda' reported: Allah's Messenger (may peace be upon him) stood up (to pray) and we heard him say:" I seek refuge in Allah from thee." Then said:" curse thee with Allah's curs

**The Book of Gifts** (cohesion: 0.8445)
- #1064 b [0.9095] Abu Said al-Khudri reported: 'Ali b. Abu Talib sent to the Messenger of Allah (may peace be upon him) from Yemen some gold alloyed with clay in a leather bag dyed in the leaves of 
- #1062 a [0.9022] Abdullah reported: On the day of Hunain, the Messenger of Allah (may peace be upon him) showed preference (to some) people in the distribution of the spoils. He bestowed on Aqra' b
- #1057 a [0.8995] Anas b. Malik reported: I was walking with the Messenger of Allah (may peace be upon him) and he had put on a mantle of Najran with a thick border. A bedouin met him and pulled the

**The Book of Virtue, Enjoining Good Manners, and Joining of the Ties of Kinship** (cohesion: 0.8423)
- #1747 [0.9143] It has been narrated by Abu Huraira that the Messenger of Allah (may peace be upon him) said: One of the Prophets made a holy war. He said to his followers: One who has married a w
- #1794 b [0.9067] It has been narrated by Abdullah (b. Mas'ud) who said: When the Messenger of Allah (may peace be upon him) was lying postrate in prayer and around him were some people from the Qur
- #1776 c [0.9034] It has been narrated through a still different chain of transmitters by the same narrator (i. e. Abu Ishaq) who said: I heard from Bara' who was asked by a man from the Qais tribe:

**The Book of Heart-Melting Traditions** (cohesion: 0.8417)
- #2011 a [0.9022] Jabir b 'Abdullah reported: We were with Allah's Messenger (may peace be upon him) and he asked for water. A person said: Allah's Messenger, may we not give you Nabidh to drink? He
- #2006 c [0.9016] Sahl b. Sa'd reported (this hadith through another chain of transmitters) and he said (these words):" In a big bowl of stone, and when Allah's Messenger (may peace be upon him) had
- #2029 c [0.8996] Anas b. Malik reported: Allah's Messenger (may peace be upon him) came to our house and he asked for a drink. We milked a goat for him and then mixed it (the milk) with the water o

**Characteristics of The Hypocrites And Rulings Concerning Them** (cohesion: 0.8411)
- #2133 d [0.9069] Jabir b. Abdullah reported Allah's Messenger (may peace be upon him) as saying: Give the name after my name, but do not give (the kunya of Abu'l-Qasim after my) kunya, for I am Abu
- #2133 a [0.8954] Jabir b. 'Abdullah reported that a child was born to a person amongst us and he gave him the name of Muhammad. Thereupon his people said: We will not allow You to give the name of 
- #2131 [0.892] Anas reported that person at Baqi' called another person as" Abu'l- Qasim," and Allah's Messenger (may peace be upon him) turned towards him. He (the person who had uttered these w

**The Book of the Rules of Inheritance** (cohesion: 0.8401)
- #943 [0.9008] Jabir b. 'Abdullah reported: Allah's Messenger (may peace be upon him) one day in the course of his sermon made mention of a person among his Companions who had died and had been w
- #954 a [0.893] Sha'bi reported that the Messenger of Allah (may peace be upon him) observed prayer over a grave after the dead was buried and he recited four takbirs over him. Shaibani said: I sa
- #931 [0.891] Hisham b. 'Urwa narrated on the authority of his father that the saying of Ibn 'Umar, viz." The dead would be punished because of the lamentation of his family over him" was mentio

**The Book of Commentary on the Qur'an** (cohesion: 0.8399)
- #2369 c [0.8981] Anas reported a hadith like this from Allah's Apostle (may peace be upon him) through another chain of transmitters.
- #2290, 2291 a [0.8927] Sahl (b. Sa'd) reported: I heard Allah's Apostle (may peace be upon him) as saying: I shall go to the Cistern before you and he who comes would drink and he who drinks would never 
- #2380 e [0.8921] Ibn 'Abbas has reported this hadith on the authority of Ubayy b. ka'b that Allah's Apostle (may peace be upon him) used to recite this.

**The Book of Repentance** (cohesion: 0.8372)
- #2088 e [0.8972] Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: There was a person (living before you) who took pride in his cloak. the rest of the hadith is the same.
- #2070 [0.8951] Jabir b. Abdullah reported that one day Allah's Apostle (may peace be upon him) put on a cloak made of brocade, which had been presented to him. He then quickly put it off and sent
- #2107 b, c [0.8907] A'isha reported: We had a curtain with us which had portraits of birds upon it. Whenever a visitor came, he found them in front of him. Thereupon Allah's Messenger (may peace be up

**Characteristics of the Day of Judgment, Paradise, and Hell** (cohesion: 0.8365)
- #2174 [0.8923] Anas reported that when Allah's Messenger (may peace be upon him) was in the company of one of his wives a person happened to pass by them. He called him and when he came, he said 
- #2191 d [0.8904] 'A'isha reported that when Allah's Messenger (may peace be upon him) came to visit any sick he supplicated for him and said: Lord of the people, remove the malady, cure him for Tho
- #2228 b [0.8892] 'Urwa reported from 'A'isha that she said that people asked Allah's Messenger (may peace be upon him) about the kahins. Allah's Messenger (may peace be upon him) said to them: It i

**The Book of Destiny** (cohesion: 0.8254)
- #1845 b, c [0.8963] This tradition has been narrated on the same authority through a different chain of transmitters. Another version of the tradition narrated on the authority of Shu'ba does not incl
- #1843 [0.8876] It has been narrated on the authority of 'Abdullah who said: The Messenger of Allah (may peace be upon him) said: After me there will be favouritism and many things that you will n
- #1893 a [0.8862] It has been narrated on the authority of Abu Mas'ud al-Ansari who said: A man came to the Messenger of Allah (may peace be upon him) and said: My riding beast has been killed, so g

### nasai (13 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| The Book of the Etiquette of Judges | 48 | 0.8841 |
| The Book of Agriculture | 188 | 0.8721 |
| The Book of Oaths and Vows | 150 | 0.8719 |
| The Book of Adornment | 23 | 0.8692 |
| The Book of Cutting off the Hand of the Thief | 99 | 0.8634 |
| The Book of Hunting and Slaughtering | 132 | 0.8628 |
| The Book of 'Umra | 153 | 0.8626 |
| The Book of Seeking Refuge with Allah | 53 | 0.8612 |
| The Book of Drinks | 46 | 0.8601 |
| The Book of ad-Dahaya (Sacrifices) | 62 | 0.859 |
| The Book of Oaths (qasamah), Retaliation and Blood Money | 35 | 0.8557 |
| The Book Of Faith and its Signs | 325 | 0.8488 |
| The Book of Financial Transactions | 54 | 0.8417 |

#### Representative hadiths per book

**The Book of the Etiquette of Judges** (cohesion: 0.8841)
- #364 [0.9443] It was narrated that 'Aishah said: "Fatimah bint Abi Hubaish suffered from Istihadah and she asked the Prophet (PBUH): 'O Messenger of Allah, I suffer from Istihadah and I do not b
- #365 [0.9438] It was narrated that 'Aishah said: "Fatimah bint Abi Hubaish said to the Messenger of Allah (PBUH): 'O Messenger of Allah (PBUH), I do not become pure. Should I stop praying?' The 
- #384 [0.9433] It was narrated that 'Aishah said: "The Messenger of Allah (PBUH) said: 'Give me the mat from the MAsjid.' She said: 'I am menstruating.' The Messenger of Allah (PBUH) said: 'Your 

**The Book of Agriculture** (cohesion: 0.8721)
- #1225 [0.935] It was narrated from Abu Hurairah that : The Messenger of Allah (SAW) finished praying two rak'ahs,and Dhul-Yadain said to him: "Has the prayer been shortened or did you forget, O 
- #1226 [0.928] It was narrated that Abu Hurairah said: "The Messenger of Allah (SAW) led us in praying 'Asr, and he said the salam after two rak'ahs. Dhul-Yadain stood up and said: 'Has the praye
- #1222 [0.928] It was narrated that Abdullah bin Buhainah said: "The Messenger of Allah (SAW) led us in praying two rak'ahs, then he stood up and did not sit, and the people stood up with him. Wh

**The Book of Oaths and Vows** (cohesion: 0.8719)
- #1059 [0.9427] It was narrated from Ibn 'Umar that: When the Messenger of Allah (SAW) started to pray, he raised his hands until they were in level with his shoulders, and when he said the takbir
- #1069 [0.9244] It was narrated from Hudhaifah that: He prayed with the Messenger of Allah (SAW) one night and he heard him say when he said the takbir: "Allahu Akbara dhal-jabaruti wal-malakuti w
- #1052 [0.9238] It was narrated from Muhammad bin Maslamah that: When the Messenger of Allah (SAW) stood to offer a voluntary prayer, he would say when he bowed: "Allahumma laka rak'atu wa bika am

**The Book of Adornment** (cohesion: 0.8692)
- #332 [0.8997] Abu Hurairah said: "A man asked the prophet (PBUH): 'O Messenger of Allah, we travel by sea and we take a little water with us, but if we use it for Wudu', we will go thirsty. Can 
- #335 [0.8985] It was narrated that Abu Hurairah said: "The Messenger of Allah (PBUH) said: 'If a dog licks the vessel of any one of you, let him throw (the contents) away and wash it seven times
- #334 [0.8984] It was narrated that Abu Hurairah said: "The Messenger of Allah (PBUH) would say: [1] 'Allahummaghsil khatayaya bi-ma'ith-thalj wal-barad (O Allah, wash away my sins with the water

**The Book of Cutting off the Hand of the Thief** (cohesion: 0.8634)
- #833 [0.913] It was narrated that Aisha said: "When the Messenger of Allah (saws) became seriously ill, Bilal came to tell him it was time to pray and he said: 'Tell Abu Bakr to lead the people
- #784 [0.9126] It was narrated from Sahl bin Sa'd that the Messenger of Allah (saws) heard that there was a dispute among Banu 'Amr bin 'Awf, so he went to them with some other people to reconcil
- #797 [0.9121] It was narrated from Aisha may Allah be pleased with her, that the Messenger of Allah (saws) told Abu Bakr to lead the people in prayer. She said: "The Prophet was in front of Abu 

**The Book of Hunting and Slaughtering** (cohesion: 0.8628)
- #502 [0.928] It was narrated that Abu Hurairah said: "The Messenger of Allah (PBUH) said: This is 'Jibril, peace be upon you, he came to teach you your religion. He prayed Subh when the dawn ap
- #517 [0.9177] It was narrated from Abu Hurairah that the Messenger of Allah (PBUH) said: "Whoever catches up with a Rak'ah of the Subh prayer before the sun rises, then he has caught up with Sub
- #625 [0.9127] It was narrated that Ibn 'Abbas said: "The Messenger of Allah (PBUH) set out at nightfall, then stopped to camp at the end of the night, and he did not wake up until the sun had ri

**The Book of 'Umra** (cohesion: 0.8626)
- #932 [0.9241] It was narrated from Abdul-Jabbar bin Wa'il that : His father said: "I prayed behind the Messenger of Allah (SAW) and when he said the takbir, he raised his hands to the bottom of 
- #884 [0.9209] It was narrated from Abu Hurairah that: The Messenger of Allah (SAW) entered the Masjid, then a man entered and prayed, then he came and greeted the Messenger of Allah (SAW) with S
- #878 [0.9161] It was narrated from Abdullah bin Umar : that when the Messenger of Allah (SAW) started to pray, he would raise his hands in level with his shoulders, and when he bowed and when he

**The Book of Seeking Refuge with Allah** (cohesion: 0.8612)
- #420 [0.9251] It was narrated that 'Aishah said: "When the Messenger of Allah (PBUH) performed Ghusl from Janabah, he would wash his hands, then perform Wudu' as for prayer, then he would perfor
- #423 [0.9156] It was narrated that 'Aishah said: "When the Messenger of Allah (PBUH0 performed Ghusl from Janabah, he would wash his hands, then perform Wudu' as for prayer, then run his fingers
- #419 [0.9115] It was narrated that Maimunah bint Al-Harith, the wife of the Prophet (PBUH), said: "When the Messenger of Allah (PBUH) performed Ghusl from Janabah, he would start by washing his 

**The Book of Drinks** (cohesion: 0.8601)
- #458 [0.901] It was narrated from Abu Suhail, from his fatehr, that he heard Talhah bin 'Ubaidullah say: "A man from the people of Najd came to the Messenger of Allah (PBUH) with unkempt hair. 
- #484 [0.8986] Salamah bin Kuhail narrated: "I heard Sa'eed bin Jubair say: 'I saw 'Abdullah bin 'Umar pray in Jam'; he made the Iqamah and prayed Maghrib, three Rak'ahs, then he prayed 'Isha', t
- #491 [0.8971] It was narrated that Ibn 'Umar said: "The Messenger of Allah (PBUH) used to pray while on his animal when he was coming back from Makkah to Madinah. Concerning this, the verse was 

**The Book of ad-Dahaya (Sacrifices)** (cohesion: 0.859)
- #633 [0.9197] It was narrated that Abu Mahdhurah said: "When the Messenger of Allah (S.A.W) left Hunain, I was the tenth of a group of ten of the people of Makkah who were trying to catch up wit
- #647 [0.9058] It was narrated that Abu Mahdhurah said: "I used to call the Adhan for the Messenger of Allah (S.A.W) and in the first Adhan of Fajr I used to Say: 'Hayya 'ala al-falah, as-salatu 
- #631 [0.9054] It was narrated that Abu Mahdhura said: "The Messenger of Allah (S.A.W) taught me the Adhan and said: 'Allahu Akbar, Allahu akbar, Allahu Akbar, Allahu Akbar; Ashhadu an la ilaha i

**The Book of Oaths (qasamah), Retaliation and Blood Money** (cohesion: 0.8557)
- #762 [0.8994] It was narrated that 'Aishah said: "The Messenger of Allah (saws) had a mat which he would spread in the day and make into a small booth at night to pray in it. The people found ou
- #746 [0.8874] It was narrated that Aisha(ra) said:"The messenger of Allah(saws) was asked during the campaign of Tabuk about the Sutra of one who is praying. He said: "Something as high as the b
- #743 [0.8862] It was narrated that Ibn Umar said: "The messenger of Allah (peace be upon him) used to pray atop his mount while travelling, facing whatever direction it was facing." (One of the 

**The Book Of Faith and its Signs** (cohesion: 0.8488)
- #244 [0.9272] It was narrated that Abu Salamah said: "I asked 'Aishah about how the Messenger of Allah (PBUH) performed Ghusl from Janabah. She said: 'The Messenger of Allah (PBUH) used to pour 
- #253 [0.9144] It was narrated that Ibn 'Abbas said: "My maternal aunt Maimunah told me: 'I brought the Messenger of Allah (PBUH) water for his Ghusl from Janabah, and he washed his hands two or 
- #102 [0.9115] It was narrated that Ibn 'Abbas said: "The Messenger of Allah (PBUH) performed Wudu', and he scooped up one handful (of water) and rinsed his mouth and nose. Then he scooped up ano

**The Book of Financial Transactions** (cohesion: 0.8417)
- #724 [0.9003] It was narrated from Ibn 'Umar that the Messenger of Allah (PBUH) saw some sputum on the Qiblah wall. He scrapped it off then he turned to the people and said: "When any one of you
- #693 [0.8907] It was narrated from 'Abdullah bin 'Amr that the Messenger of Allah (PBUH) said: "When Sulaiman bin Dawud finished building Bait Al-Maqdis, he asked Allah for three things: Judgeme
- #729 [0.8879] It was narrated that 'Abdul-Malik bin Sa'eed said: "I heard Abu Humaid and Abu Usaid say: 'The Messenger of Allah (PBUH) said: "When any one of you enters the Masjid, let him say: 

### riyadussalihin (19 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| The Book of I'tikaf | 3 | 0.9538 |
| The Book of Supplicating Allah to Exalt the Mention of Allah's Messenger | 11 | 0.9099 |
| The Book of Praise and Gratitude to Allah | 4 | 0.9072 |
| The Book of Knowledge | 17 | 0.9041 |
| The Book About the Etiquette of Eating | 51 | 0.895 |
| The Book of the Remembrance of Allah | 57 | 0.8892 |
| The Book of Hajj | 14 | 0.888 |
| The Book of Du'a (Supplications) | 46 | 0.8878 |
| The Book of Forgiveness | 28 | 0.8875 |
| The Book of Visiting the Sick | 62 | 0.8856 |
| The Book of Dress | 35 | 0.8846 |
| The Book of Etiquette of Traveling | 35 | 0.8815 |
| The Book of the Etiquette of Sleeping, Lying and Sitting etc | 31 | 0.8805 |
| The Book of Jihad | 91 | 0.8782 |
| The Book of Greetings | 50 | 0.8767 |
| The Book of Good Manners | 47 | 0.8735 |
| The Book of Virtues | 277 | 0.872 |
| The Book of the Prohibited actions | 297 | 0.8639 |
| The Book of Miscellaneous ahadith of Significant Values | 61 | 0.8576 |

#### Representative hadiths per book

**The Book of I'tikaf** (cohesion: 0.9538)
- #1270 [0.9601] Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) used to observe I'tikaf every year (during Ramadan) for ten days; in the year in which he passed away, he 
- #1269 [0.9508] 'Aishah (May Allah be pleased with her) reported: The Prophet (PBUH) used to engage himself in I'tikaf (seclusion for prayers) in the mosque during the last ten nights of Ramadan t
- #1268 [0.9506] Ibn `Umar (May Allah be pleased with them) reported: The Messenger of Allah (PBUH) used to observe I`tikaf in the last ten days of Ramadan.   <b>[Al-Bukhari and Muslim]</b>.

**The Book of Supplicating Allah to Exalt the Mention of Allah's Messenger** (cohesion: 0.9099)
- #1407 [0.9318] Abu Humaid As-Sa'idi (May Allah be pleased with him) reported: The Companions of the Messenger of Allah (PBUH) said: "O Messenger of Allah! How should we supplicate for you?" He (P
- #1406 [0.9269] Abu Mas'ud Al-Badri (May Allah be pleased with him) reported: We were sitting in the company of Sa'd bin 'Ubadah (May Allah be pleased with him), when the Messenger of Allah (PBUH)
- #1398 [0.925] Ibn Mas'ud (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said: "The people who will be nearest to me on the Day of Resurrection will be those who supplica

**The Book of Praise and Gratitude to Allah** (cohesion: 0.9072)
- #1396 [0.9375] Anas bin Malik (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "Allah is pleased with His slave who says: 'Al-hamdu lillah (praise be to Allah)' when 
- #1395 [0.9075] Abu Musa Al-Ash'ari (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "When a slave's child dies, Allah the Most High asks His angels, 'Have you taken o
- #1394 [0.8925] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "Any matter of importance which is not begun with Al-hamdu lillah (praise be to Allah) re

**The Book of Knowledge** (cohesion: 0.9041)
- #1389 [0.9293] Ibn Mas'ud (May Allah be pleased with him) reported: I heard the Messenger of Allah (PBUH) saying, "May Allah freshen the affairs of a person who hears something from us and commun
- #1387 [0.9237] Abu Umamah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "The superiority of the learned over the devout worshipper is like my superiority over the 
- #1381 [0.9207] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "Allah makes the way to Jannah easy for him who treads the path in search of knowledge."<

**The Book About the Etiquette of Eating** (cohesion: 0.895)
- #727 [0.9357] 'Umar bin Abu Salamah (May Allah be pleased with him) reported: Messenger of Allah (PBUH), said to me, "Mention Allah's Name (i.e., say Bismillah before starting eating), eat with 
- #742 [0.9262] Wahshi bin Harb (May Allah be pleased with him) reported: Some of the Companions of Messenger of Allah (PBUH) said: "We eat but are not satisfied." He (PBUH) said, "Perhaps you eat
- #752 [0.9225] Anas (May Allah be pleased with him) reported: Whenever the Messenger of Allah (PBUH) ate food, he would lick his three fingers and say, "If anyone of you drops a morsel of food, h

**The Book of the Remembrance of Allah** (cohesion: 0.8892)
- #1451 [0.9299] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "He who recites in the morning and in the evening the statement: 'Subhan-Allahi wa bihamd
- #1409 [0.929] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "The uttering of the words: "Subhan-Allah (Allah is free from imperfection), Al-hamdu lil
- #1419 [0.9249] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "He who recites after every prayer: Subhan-Allah (Allah is free from imperfection) thirty

**The Book of Hajj** (cohesion: 0.888)
- #1279 [0.9243] Ibn 'Abbas (May Allah be pleased with them) reported: A woman came to the Messenger of Allah (PBUH) and said, "Allah's obligation upon His slaves has become obligatory on my father
- #1282 [0.9154] Ibn 'Abbas (May Allah be pleased with them) reported: The Prophet (PBUH) came across a caravan at Ar-Rauha' and asked who the people in the caravan were. They replied that they wer
- #1274 [0.9107] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "Whoever performs Hajj (pilgrimage) and does not have sexual relations (with his wife), n

**The Book of Du'a (Supplications)** (cohesion: 0.8878)
- #1478 [0.9444] 'Abdullah bin 'Umar (May Allah be pleased with them) reported: The Messenger of Allah (PBUH) used to supplicate thus: "Allahumma inni a'udhu bika min zawali ni'matika, wa tahawwuli
- #1474 [0.9329] Anas (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) used to supplicate: "Allahumma inni a'udhu bika minal-ajzi wal- kasali, wal-jubni wal-harami, wal-bukhl
- #1468 [0.9323] 'Abdullah bin Mas'ud (May Allah be pleased with him) reported: The Prophet (PBUH) used to supplicate: "Allahumma inni as'alukal-huda, wat-tuqa, wal-'afafa, wal-ghina (O Allah! I be

**The Book of Forgiveness** (cohesion: 0.8875)
- #1894 [0.9245] Abu Sa'id Al-Khudri (May Allah be pleased with him) said: The Messenger of Allah (PBUH) said, "Allah, the Rubb of honour and glory, will say to the inhabitants of Jannah: 'O inhabi
- #1896 [0.913] Suhaib (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "When the inhabitants of Jannah enter Jannah, Allah, the Glorious and Exalted, will say to them
- #1890 [0.9074] Sahl bin Sa'd (May Allah be pleased with him) said: The Messenger of Allah (PBUH) said, "The dwellers of Jannah will see the upper abodes of Jannah as you see the stars in the sky.

**The Book of Visiting the Sick** (cohesion: 0.8856)
- #919 [0.9242] Umm Salamah (May Allah be pleased with her) reported: The Messenger of Allah (PBUH) visited Abu Salamah (May Allah be pleased with him) when his eyes were open soon after he died. 
- #894 [0.9166] Al-Bara' bin `Azib (May Allah be pleased with them) reported: Messenger of Allah (PBUH) has ordered us to visit the sick, to follow the funeral (of a dead believer), respond to the
- #939 [0.9155] Wathilah bin Al-Asqa' (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) led the funeral prayer of a Muslim man in our presence, and I heard him saying "Allahu

**The Book of Dress** (cohesion: 0.8846)
- #790 [0.9203] Ibn 'Umar (May Allah be pleased with him) reported: The Prophet (PBUH) said, "Whoever allows his lower garment to drag out of vanity will find that Allah will not look at him on th
- #791 [0.9151] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "On the Day of Resurrection, Allah will not look at him who trails his lower garment out 
- #806 [0.9101] 'Ali (May Allah be pleased with him) reported: I saw the Messenger of Allah (PBUH) holding a piece of gold in his left hand and a silk (cloth) in his right hand. Then he said, "The

**The Book of Etiquette of Traveling** (cohesion: 0.8815)
- #972 [0.9195] Ibn 'Umar (May Allah be pleased with them) reported: Whenever the Messenger of Allah (PBUH) mounted his camel for setting out on a journey, he would recite: "Allahu Akbar (Allah is
- #973 [0.9194] 'Abdullah bin Sarjis (May Allah be pleased with him) reported: Whenever the Messenger of Allah (PBUH) proceeded on a journey, he would seek refuge in Allah from the hardships of th
- #978 [0.9175] Abu Hurairah (May Allah be pleased with him) reported: A man said: "O Messenger of Allah (PBUH), I intend to set out on a journey, so counsel me." He (PBUH) said, "Fear Allah, and 

**The Book of the Etiquette of Sleeping, Lying and Sitting etc** (cohesion: 0.8805)
- #818 [0.9256] Abu Hurairah (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Whoever sits in a place where he does not remember Allah (SWT), he will suffer loss and incu
- #823 [0.9105] Ash-Sharid bin Suwaid (May Allah be pleased with him) reported: Messenger of Allah (PBUH) passed by me when I was sitting with my left hand behind my back and leaning on my palm. O
- #836 [0.904] Abu Hurairah (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "If anyone sits in a gathering where he does not remember Allah, he will bring grief upon him

**The Book of Jihad** (cohesion: 0.8782)
- #1322 [0.9161] Anas (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "He who supplicates sincerely for martyrdom, it will be granted to him even though he is not kill
- #1314 [0.9132] Jabir (May Allah be pleased with him) reported: A man asked the Messenger of Allah (PBUH): "Tell me where I will be if I am killed while fighting in the way of Allah?" He (PBUH) re
- #1287 [0.9104] Abu Dharr (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) was asked: "Which deed is the best?" He (PBUH) replied, "Faith in Allah and Jihad (fighting, strug

**The Book of Greetings** (cohesion: 0.8767)
- #869 [0.9204] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "When one of you arrives in a gathering, he should offer Salam to those who are already t
- #848 [0.9138] 'Abdullah bin Salam (May Allah be pleased with him) reported: I heard the Messenger of Allah (PBUH) saying, "O people, exchange greetings of peace (i.e., say: As-Salamu 'Alaikum to
- #879 [0.9132] Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "When one of you sneezes he should say: 'Al-hamdu lillah (praise be to Allah),' and his brother or h

**The Book of Good Manners** (cohesion: 0.8735)
- #680 [0.9062] Ibn 'Umar (May Allah be pleased with them) reported: Messenger of Allah (PBUH) passed by a man of the Ansar who was admonishing his brother regarding shyness. Messenger of Allah (P
- #694 [0.9046] Abu Dharr (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Do not disdain a good deed, (no matter how small it may seem) even if it is your meeting with y
- #716 [0.9034] Anas (May Allah be pleased with him) reported: A man came to the Prophet (PBUH) and said: "O Messenger of Allah! I intend to go on a journey, so supplicate for me." He (PBUH) said,

**The Book of Virtues** (cohesion: 0.872)
- #1177 [0.9141] 'Abdullah bin 'Amr (May Allah be pleased with them) reported: The Messenger of Allah (PBUH) said, "The Salat which is dearest to Allah is that of (Prophet) Dawud; and As-Saum (the 
- #1033 [0.9116] Abu Hurairah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said: "Were people to know the blessing of pronouncing Adhan and the standing in the first row,
- #1099 [0.9112] 'Abdullah bin Mughaffal (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) said, "There is a Salat (prayer) between every Adhan and Iqamah; there is a Salat be

**The Book of the Prohibited actions** (cohesion: 0.8639)
- #1717 [0.905] Abu Musa (May Allah be pleased with him) said: The Messenger of Allah (PBUH) said, "Verily, I swear by Allah, if Allah wills, I shall not swear to do something but that if I consid
- #1554 [0.9049] Samurah bin Jundub (May Allah be pleased with him) said: The Messenger of Allah (PBUH) said, "Do not curse one another, invoking Curse of Allah or Wrath of Allah or the fire of Hel
- #1734 [0.9024] Ibn Mas'ud (May Allah be pleased with him) said: The Messenger of Allah (PBUH) said, "A true believer does not taunt or curse or abuse or talk indecently."<br><br><b>[At-Tirmidhi]<

**The Book of Miscellaneous ahadith of Significant Values** (cohesion: 0.8576)
- #1818 [0.8942] Abu Hurairah (May Allah be pleased with him) said: The Messenger of Allah (PBUH) said, "Let me tell you something about Dajjal (the Antichrist) which no Prophet had told his people
- #1835 [0.8937] Abu Hurairah (May Allah be pleased with him) said: The Messenger of Allah (PBUH) said, "There are three (types of) people with whom Allah will neither speak on the Day of Resurrect
- #1851 [0.8921] Abu Hurairah (May Allah be pleased with him) said: The Messenger of Allah (PBUH) said, "O people! Allah is Pure and, therefore, accepts only that which is pure. Allah has commanded

### shamail (51 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| The Humbleness Of Sayyidina Rasoolullah | 2 | 0.9695 |
| The Helmet Of Rasoolullah | 2 | 0.9692 |
| Rasoolullah Performing Wudu At The Time Of Eating | 3 | 0.9656 |
| The Armor Of Rasoolullah | 2 | 0.9588 |
| Description Of The Things Rasoolullah Drank | 2 | 0.9543 |
| Kuhl Of Rasoolullah | 5 | 0.9484 |
| The Cup Of Rasoolullah | 2 | 0.9475 |
| The Names Of Sayyidina Rasoolullah | 2 | 0.9452 |
| The Walking Of Rasoolullah | 3 | 0.9403 |
| Rasoolullah Leaning On Something Other Than a Pillow | 2 | 0.9387 |
| The Speech Of rasoolullah | 3 | 0.9383 |
| Hajaamah (Cupping-Cautering) Of Sayyidina Rasoolullah | 2 | 0.9383 |
| Stating That Rasoolullah Wore The Ring On His Right Hand | 9 | 0.936 |
| The Death Of Sayyidina Rasoolullah | 6 | 0.9351 |
| The Khuff (Leather Socks) Of Rasoolullah | 2 | 0.935 |
| The Sword Of Rasoolullah | 4 | 0.9328 |
| The Mubarak Ring Of Rasoolullah | 8 | 0.9287 |
| The Fruits Eaten By Rasoolullah | 7 | 0.9282 |
| Sayyidina Rasoolullah Performing Nawaafil At Home | 8 | 0.9274 |
| The Words That Of Rasoolullah Said Before and After Eating | 7 | 0.9234 |
| The Turban Of Rasoolullah | 5 | 0.9216 |
| The Sitting Of Rasoolullah | 3 | 0.9208 |
| Worship And Devotion Of Rasoolullah | 6 | 0.9205 |
| The Living Of Sayyidina Rasoolullah | 6 | 0.9205 |
| The Mubarak Hair Of Rasoolullah | 8 | 0.9198 |
| The Pillow Of Rasoolullah | 5 | 0.9195 |
| The Lungi Of Rasoolullah | 4 | 0.9177 |
| The Bread Of Rasoolullah | 8 | 0.9177 |
| The Shoes Of Rasoolullah | 11 | 0.9159 |
| Hadith Describing The Manner Rasoolullah Drank | 10 | 0.9153 |
| Description Of The Eating Of Rasoolullah | 5 | 0.9148 |
| Rasoolullah Using a Dye | 5 | 0.9146 |
| Narrations Of The Bed Of Sayyidina Rasoolullah | 6 | 0.9138 |
| The Combing Of The Hair Of Rasoolullah | 5 | 0.9121 |
| Appearing Of The White Hair Of Rasoolullah | 8 | 0.9048 |
| The Seeing Of Rasoolullah In a Dream | 7 | 0.9025 |
| The Weeping Of Sayyidina Rasoolullah | 8 | 0.9017 |
| The Laughing Of Rasoolullah | 9 | 0.9004 |
| The Noble Features Of Rasoolullah | 14 | 0.8996 |
| Seal Of Nubuwwah (Prophethood) Of Rasoolullah | 8 | 0.8993 |
| The Recital Of Sayyidina Rasoolullah | 16 | 0.8991 |
| The Legacy Of Sayyidina Rasoolullah | 14 | 0.8962 |
| Salaatut Duha (Chaast Prayers) | 25 | 0.8901 |
| Noble Character And Habits Of Sayyidina Rasoolullah | 13 | 0.8896 |
| Modesty Of Sayyidina Rasoolullah | 15 | 0.8887 |
| Description Of The Saying Of Rasoolullah On Poetry | 9 | 0.8885 |
| Rasoolullah Using 'Itr | 6 | 0.8867 |
| The Dressing Of Rasoolullah | 18 | 0.8856 |
| Description Of The Joking Of Rasoolullah | 6 | 0.8855 |
| What Rasoolullah Would Eat with Bread | 34 | 0.8736 |
| The Noble Age Of Sayyidina Rasoolullah | 9 | 0.872 |

#### Representative hadiths per book

**The Humbleness Of Sayyidina Rasoolullah** (cohesion: 0.9695)
- #328 [0.9695] Ja'far ibn Muhammad reported that his father said: "'A'isha was asked: 'How was the mattress of Allah’s Messenger (Allah bless him and give him peace) in your home?' She said: 'It 
- #327 [0.9695] ‘A’isha said (may Allah be well pleased with her): "The mattress on which Allah’s Messenger (Allah bless him and give him peace) used to sleep consisted of tanned hides stuffed wit

**The Helmet Of Rasoolullah** (cohesion: 0.9692)
- #112 [0.9692] Anas ibn Malik reported: “Allah’s Messenger (Allah bless him and give him peace) entered Mecca in the Year of Victory with the helmet on his head. When he took it off, a man came t
- #111 [0.9692] Anas ibn Malik said: "The Prophet (Allah bless him and give him peace) entered Mecca wearing a helmet. He was told: 'This Ibn Khatal [son of corrupt speech] is clinging to the curt

**Rasoolullah Performing Wudu At The Time Of Eating** (cohesion: 0.9656)
- #185 [0.9779] Ibn 'Abbas said: "Allah’s Messenger (Allah bless him and give him peace) emerged from having a bowel movement and he was brought a meal, so he was asked: 'Will you not perform the 
- #184 [0.9765] Ibn Abbas said: "Allah’s Messenger (Allah bless him and give him peace) emerged from the toilet, whereupon the meal was presented to him and they said: 'Should we not bring you wat
- #186 [0.9424] Salman said: “I read in the Torah that the blessing of the meal is the minor ritual ablution after it, so I mentioned this to the Prophet (Allah bless him and give him peace), and 

**The Armor Of Rasoolullah** (cohesion: 0.9588)
- #110 [0.9588] As-Sa’ib ibn Yazid said: "Allah’s Messenger (Allah bless him and give him peace) wore on the Day of Uhud two coats of mail between which he rendered support.”
- #109 [0.9588] Az-Zubair ibn al-'Awwam said: "The Prophet (Allah bless him and give him peace) wore two coats of mail on the Day of  Uhud, so he tried to climb the boulder but was not able. He th

**Description Of The Things Rasoolullah Drank** (cohesion: 0.9543)
- #203 [0.9543] 'A’isha said (may Allah be well pleased with her): "The beverage dearest to Allah’s Messenger (Allah bless him and give him peace) was cold water sweetened with honey.”
- #204 [0.9543] Ibn 'Abbas said (may Allah be well pleased with him and his father): "Together with Allah’s Messenger (Allah bless him and give him peace), Khalid ibn al-Walid and I entered the pr

**Kuhl Of Rasoolullah** (cohesion: 0.9484)
- #52 [0.9566] Jabir (i.e. Ibn Abdillah) said: "Allah’s Messenger said (Allah bless him and give him peace): “You must apply antimony before going to sleep, for it clears the vision and makes the
- #53 [0.956] Ibn "Abbas said: "Allah’s Messenger said (Allah bless him and give him peace): 'The best of your eye salves is antimony, for it clears the vision and makes the eyelashes grow.'”
- #50 [0.9511] Ibn 'Abbas reported that the Prophet said (Allah bless him and give him peace): "Color the edges of the eyelids with antimony [ithmid], for it clears the vision and makes the eyela

**The Cup Of Rasoolullah** (cohesion: 0.9475)
- #195 [0.9475] Anas said: "I had given Allah’s Messenger (Allah bless him and give him peace) every kind of beverage to drink using this vessel: water, date juice, honey and milk.”
- #194 [0.9475] Thabit said: “Anas ibn Malik brought out to us a wooden drinking vessel, roughly clamped with iron, then he said: ‘O Ihabit, this is the drinking vessel of Allah’s Messenger (Allah

**The Names Of Sayyidina Rasoolullah** (cohesion: 0.9452)
- #365 [0.9452] Muhammad ibn Jubair ibn Mut'im reported that his father said: "Allah’s Messenger said (Allah bless him and give him peace): “Verily I have several names: I am Muhammad; I am Ahmad;
- #366, 367 [0.9452] Hudhaifa said: "I encountered the Prophet (Allah bless him and give him peace) in one of the streets of Medina, and he said: “I am Muhammad; I am Ahmad; I am the Prophet of Mercy a

**The Walking Of Rasoolullah** (cohesion: 0.9403)
- #124 [0.9558] Ali ibn Abi Talib said (may Allah ennoble his countenance): "When the Prophet (Allah bless him and give him peace) walked, he inclined forward as if he were descending a declivity.
- #123 [0.9498] Ibrahim ibn Muhammad, one of the offspring of 'Ali ibn Abi Talib, told me: “When "Ali described the Prophet (Allah bless him and give him peace), he said: ‘When he walked, he moved
- #122 [0.9152] Abu Huraira said: "I have not seen anything more beautiful than Allah’s Messenger (Allah bless him and give him peace). The sun seemed to shine in his face. Nor have I seen anyone 

**Rasoolullah Leaning On Something Other Than a Pillow** (cohesion: 0.9387)
- #135 [0.9387] Al-Fadl ibn Abbas said: "I went in to see Allah’s Messenger (Allah bless him and give him peace) during his illness in which he died, and on his head there was a yellow band. I gre
- #134 [0.9387] Anas said: “The Prophet (Allah bless him and give him peace) was feeling ill, so he came out leaning on Usama ibn Zaid wearing an outer garment of coarse cotton fabric, which he ha

**The Speech Of rasoolullah** (cohesion: 0.9383)
- #222 [0.9441] 'A’isha said (may Allah the Exalted be well pleased with her): "Allah’s Messenger (Allah bless him and give him peace) would not speak on and on the way you do. Rather, he would pa
- #224 [0.9392] Al-Hasan ibn 'Ali said (may Allah the Exalted be well pleased with him and his father): “I said to my maternal uncle, Hind ibn Abi Hala, who was skilled at describing people: ‘Desc
- #223 [0.9317] Anas ibn Malik said: "Allah’s Messenger (Allah bless him and give him peace) used to repeat each expression three times in order to make himself understood.”

**Hajaamah (Cupping-Cautering) Of Sayyidina Rasoolullah** (cohesion: 0.9383)
- #357 [0.9383] Abu Sa'id al-Khudri said: "He (Allah bless him and give him peace) was more bashful than the virgin in her boudoir, and when he disapproved of something, we knew it from the expres
- #358 [0.9383] 'A’isha said: “I never looked at the private parts of Allah’s Messenger (Allah bless him and give him peace).” (Or she said: “I never saw the private parts of Allah’s Messenger (Al

**Stating That Rasoolullah Wore The Ring On His Right Hand** (cohesion: 0.936)
- #97 [0.972] Abdullah ibn Ja'far said: “He (Allah bless him and give him peace) used to wear a signet ring on his right hand.”
- #98 [0.9678] Jabir ibn ‘Abdi’llah said: "The Prophet (Allah bless him and give him peace) used to wear a signet ring on his right hand.”
- #94, 95 [0.9654] 'Ali ibn Abi Talib said (may Allah be well pleased with him): “The Prophet (Allah bless him and give him peace) used to wear his signet ring on his right hand.”

**The Death Of Sayyidina Rasoolullah** (cohesion: 0.9351)
- #381 [0.9643] 'A’isha said: "The Prophet died (Allah bless him and give him peace) when he was sixty-three years of age.”
- #382 [0.9546] Ibn 'Abbas said:  "Allah’s Messenger died (Allah bless him and give him peace) when he was sixty-five years of age.”
- #379 [0.9439] Ibn Abbas said: “The Prophet (Allah bless him and give him peace) stayed in Mecca for thirteen years, during which he was inspired with Divine revelation, and in Medina for ten, an

**The Khuff (Leather Socks) Of Rasoolullah** (cohesion: 0.935)
- #72 [0.935] Ibn Buraida reported that his father said: "The Negus [the Emperor of Ethiopia] gave the Prophet (Allah bless him and give him peace) a pair of plain black shoes, so he put them on
- #73 [0.935] Al-Mughira ibn Shu'ba said: "Dihya [a notable Companion of his] gave the Prophet (Allah bless him and give him peace) a pair of plain black shoes, so he wore them,"— and Isra’il sa

**The Sword Of Rasoolullah** (cohesion: 0.9328)
- #105 [0.9581] Sa'id ibn Abi’l-Hasan al-Basri said: “The pommel of the sword of Allah’s Messenger (Allah bless him and give him peace) was made of silver."
- #104 [0.9487] Anas said: “Ihe pommel of the sword of Allah’s Messenger (Allah bless him and give him peace) was made of silver.”
- #106 [0.9285] Hud (i.e. Ibn 'Abdi’llah ibn Sa'd) reports that his grandfather said: "Allah’s Messenger (Allah bless him and give him peace) entered Mecca on the Day of Victory with gold and silv

**The Mubarak Ring Of Rasoolullah** (cohesion: 0.9287)
- #88 [0.9588] Anas ibn Malik said: “The signet ring of the Prophet (Allah bless him and give him peace) consisted of silver, including its stone.”
- #91 [0.9467] Anas ibn Malik said: "The Prophet (Allah bless him and give him peace) wrote to Chosroes, Caesar and the Negus, whereupon he was told: 'The non-Arabs will not accept a letter unles
- #90 [0.9462] Anas ibn Malik said: “The inscription engraved [in Arabic script] on the signet ring of Allah’s Messenger (Allah bless him and give him peace) was: Muhammadun forming one line, Ras

**The Fruits Eaten By Rasoolullah** (cohesion: 0.9282)
- #197 [0.959] 'A’isha said: (may Allah be well pleased with her): "The Prophet (Allah bless him and give him peace) used to eat watermelon with ripe dates.”
- #199 [0.9508] A’isha(may Allah be well pleased with her) said: “The Prophet (Allah bless him and give him peace) ate watermelon with ripe dates.”
- #196 [0.9351] 'Abdullah ibn Ja'far said: "The Prophet (Allah bless him and give him peace) used to eat cucumbers with ripe dates.”

**Sayyidina Rasoolullah Performing Nawaafil At Home** (cohesion: 0.9274)
- #287 [0.9414] Mu'adha said:  "I asked ‘A'isha (may Allah the Exalted be well pleased with her): “Did the Prophet (Allah bless him and give him peace) perform the mid-morning ritual prayer?” She 
- #292, 293 [0.9342] Abu Ayyub al-Ansari said (may Allah the Exalted be well pleased with him): “The Prophet (Allah bless him and give him peace) used to devote himself to four cycles [of ritual prayer
- #288 [0.9326] Anas ibn Maik said: “The Prophet (Allah bless him and give him peace) used to perform the mid-morning ritual prayer in six cycles.”

**The Words That Of Rasoolullah Said Before and After Eating** (cohesion: 0.9234)
- #188 [0.9371] 'A’isha said: “Allah’s Messenger said (Allah bless him and give him peace): ‘If one of you eats and forgets to mention Allah (Exalted is He) during his meal, let him say: B'ismilla
- #190 [0.9351] Abu Sa‘id al-Khudri said: “Allah’s Messenger (Allah bless him and give him peace) used to say, when he had finished his meal: ‘Praise be to Allah, who has fed us and quenched our t
- #189 [0.9273] 'Umar ibn Abi Salama said that he went in to see Allah’s Messenger (Allah bless him and give him peace), who had a meal before him, so he said to him: 'O my dear son, pronounce the

**The Turban Of Rasoolullah** (cohesion: 0.9216)
- #115 [0.9453] 'Amr ibn Huraith reported that his father said: "The Prophet (Allah bless him and give him peace) addressed the people while wearing a black turban.”
- #117 [0.9243] Ibn 'Abbas said: “The Prophet (Allah bless him and give him peace) addressed the people while wearing a turban that was dasma’ [marked with traces of oil from his hair].
- #114 [0.9234] 'Amr ibn Huraith reported that his father said: "I saw a black turban on the head of Allah’s Messenger (Allah bless him and give him peace).”

**The Sitting Of Rasoolullah** (cohesion: 0.9208)
- #128 [0.9397] Abu Sa'id al-Khudri said: “When Allah’s Messenger (Allah bless him and give him peace) sat in the mosque, he pressed his legs against his stomach with his hands.”
- #126 [0.912] 'Abdu’llah ibn Hassan reported on the authority of his grandmothers: Qaila bint Makhrama said that she saw Allah’s Messenger (Allah bless him and give him peace) in the mosque squa
- #127 [0.9107] 'Abbad ibn Tamim reported: His paternal uncle said that he saw the Prophet (Allah bless him and give him peace) lying on his back in the mosque, placing one of his legs over the ot

**Worship And Devotion Of Rasoolullah** (cohesion: 0.9205)
- #256 [0.9375] 'A’isha said: "When Allah’s Messenger (Allah bless him and give him peace) went to his mattress each night, he joined the palms of his hands, then breathed into them and recited in
- #259 [0.926] Abu Qatada said: “When the Prophet (Allah bless him and give him peace) alighted for rest at night, he would recline on his right side, and when he alighted for rest shortly before
- #253, 254 [0.9209] Al-Bara’ ibn 'Azib said: “When the Prophet (Allah bless him and give him peace) lay down to sleep, he placed the palm of his right hand under his right cheek and said: ‘O my Lord, 

**The Living Of Sayyidina Rasoolullah** (cohesion: 0.9205)
- #361 [0.9456] Ibn Abbas said: "The Prophet (Allah bless him and give him peace) had cupping performed between the two veins in the neck and between the shoulders. He also gave the cupper his fee
- #359 [0.9446] Anas ibn Malik said: "Allah’s Messenger (Allah bless him and give him peace) sought to have blood drawn from him by the operation of cupping. Abu Taiba cupped him, so he ordered tw
- #363 [0.9323] Anas ibn Malik said (may Allah be well pleased with him): "Allah’s Messenger (Allah bless him and give him peace) used to have cupping performed between the two veins of the neck a

**The Mubarak Hair Of Rasoolullah** (cohesion: 0.9198)
- #24 [0.9507] Anas ibn Malik said: "The hair of Allah’s Messenger (Allah bless him and give him peace) came down to the middle of his ears.”
- #29 [0.9484] Anas said: "The hair of Allah’s Messenger (Allah bless him and give him peace) was down to the middle parts of his ears.”
- #27 [0.9346] Qatada said: “I said to Anas: ‘How was the hair of Allah’s Messenger (Allah bless him and give him peace)?' He replied: 'It was neither crisply curled nor lank. His hair used to re

**The Pillow Of Rasoolullah** (cohesion: 0.9195)
- #133 [0.937] Jabir ibn Samura said: "I saw Allah’s Messenger (Allah bless him and give him peace) leaning on a cushion.”
- #129 [0.9327] Jabir ibn Samura said: "I saw Allah’s Messenger (Allah bless him and give him peace) leaning on a cushion on his left side.”
- #131 [0.9323] Abu Juhaifa said: "Allah’s Messenger said (Allah bless him and give him peace):‘As for me, I do not eat while leaning on a support!’”

**The Lungi Of Rasoolullah** (cohesion: 0.9177)
- #119 [0.9347] Al-Ash'ath ibn Sulaim said:  "I heard my maternal aunt relate, on the authority of her paternal uncle; 'While I was walking in Medina, someone behind me said: ‘Raise your loincloth
- #120 [0.9229] llyas ibn Salama al-Akwa reported that his father said: "'Uthman ibn 'Affan used to wear a loincloth reaching the middle parts of his shins, and he said: 'In this manner was the lo
- #121 [0.9092] Hudhaifa ibn al-Yuman said: "Allah’s Messenger (Allah bless him and give him peace) took hold of the calf of my legs or his leg, and he said: 'This is the position of the loincloth

**The Bread Of Rasoolullah** (cohesion: 0.9177)
- #148 [0.9476] 'A’isha said: "Allah’s Messenger (Allah bless him and give him peace) did not eat his fill of barley-bread for two days in a row until he died.”
- #142 [0.9366] 'A’isha said: "The family of Muhammad (Allah bless him and give him peace) did not satisfy their appetite with barley-bread for before even two consecutive days until Allah’s Messe
- #149 [0.936] Anas said: “Allah’s Messenger (Allah bless him and give him peace) did not eat food on a table, and he did not eat bread rolled thin and flat, until he died.”

**The Shoes Of Rasoolullah** (cohesion: 0.9159)
- #85 [0.9433] Abu Huraira said: “The sandals of Allah’s Messenger (Allah bless him and give him peace) had two thongs, as did those of Abu Bakr and 'Umar (may Allah the Exalted be well pleased w
- #78 [0.9428] Abu Huraira said: "The sandals of Allah’s Messenger (Allah bless him and give him peace) had two thongs."
- #83 [0.9388] Abu Huraira said: “The Prophet said (Allah bless him and give him peace): "When one of you puts on sandals, let him begin with the right, and when he takes them off, let him begin 

**Hadith Describing The Manner Rasoolullah Drank** (cohesion: 0.9153)
- #205 [0.9563] Ibn 'Abbas said (may Allah be well pleased with him and his father): “The Prophet (Allah bless him and give him peace) drank from [the water of] Zamzam while standing.”
- #210 [0.9391] Ibn 'Abbas said (may Allah be well pleased with him and his father): "When the Prophet drank (Allah bless him and give him peace), he used to take two breaths.”
- #207 [0.9317] Ibn 'Abbas said (may Allah be well pleased with him and his father): "I gave Allah’s Messenger (Allah bless him and give him peace) Zamzam water, and he drank it standing up.”

**Description Of The Eating Of Rasoolullah** (cohesion: 0.9148)
- #137 [0.9415] Anas said: “When the Prophet (Allah bless him and give him peace) ate a meal, he used to lick his three fingers [the thumb, the index finger and the middle finger].”
- #140 [0.9364] Ibn al-Ka'b ibn Malik reported that his father said: "Allah’s Messenger (Allah bless him and give him peace) used to eat with his three fingers and afterwards he would lick them.”
- #136 [0.9162] Reported on the authority of Ibn al-Ka'b ibn Malik, that his father said: "The Prophet (Allah bless him and give him peace) used to lick his fingers three times.”

**Rasoolullah Using a Dye** (cohesion: 0.9146)
- #46 [0.9305] Abu Huraira was asked: “Did Allah’s Messenger (Allah bless him and give him peace) dye [his hair]?” He said: “Yes!”
- #48 [0.9266] Humaid told us that Anas said: "I saw the hair of Allah’s Messenger (Allah bless him and give him peace)dyed.”
- #49 [0.9262] Hammad said: 'Abdullah ibn Muhammad ibn 'Uqail also informed us: "I saw the hair of Allah’s Messenger (Allah bless him and give him peace) dyed in the presence of Anas ibn Malik."

**Narrations Of The Bed Of Sayyidina Rasoolullah** (cohesion: 0.9138)
- #324 [0.9373] Ibn Abbas said: “Allah’s Messenger (Allah bless him and give him peace) took hold of a daughter of his who was dying, then embraced her and she died in his arms. Umm Aiman cried, s
- #322 [0.9242] 'Abdu’llah ibn Mas'ud said (may Allah be well pleased with him): “Allah’s Messenger (Allah bless him and give him peace) told me: ‘Recite the Qur’an to me,’ so I said: ‘O Messenger
- #325 [0.9219] 'A’isha said (may Allah be well pleased with her): “Allah’s Messenger (Allah bless him and give him peace) kissed 'Uthman ibn Maz'un when he was dead, and he was weeping." (or: “hi

**The Combing Of The Hair Of Rasoolullah** (cohesion: 0.9121)
- #35 [0.9152] 'Abdullah ibn Mughaffal said: "Allah’s Messenger (Allah bless him and give him peace) forbade combing except at intervals.”
- #36 [0.9132] Humaid ibn 'Abd ar-Rahman relates on the authority of a man from among the Companions of the Prophet (Allah bless him and give him peace): "The Prophet (Allah bless him and give hi
- #34 [0.9125] 'A’isha said: “Allah’s Messenger (Allah bless him and give him peace) used to love tayammun [beginning with his right hand, his right side and his right foot] in his ritual purific

**Appearing Of The White Hair Of Rasoolullah** (cohesion: 0.9048)
- #44 [0.9443] Jabir ibn Samura was asked: “Was there any grayness of the head of Allah’s Messenger (Allah bless him and give him peace)?" He replied: "There was no grayness on the head of Allah’
- #39 [0.9349] Jabir ibn Samura was asked about the grayness of Allah’s Messenger (Allah bless him and give him peace), so he said: "When he oiled his head, no grayness was visible, and when he d
- #41 [0.9165] Ibn Abbas said: Abu Bakr said: “O Messenger of Allah, you have grayed!” He said: 'I have been made gray-haired by Hud (Al-Qur'an; 11)), the calamity (Al-Qur'an; 56)), the winds sen

**The Seeing Of Rasoolullah In a Dream** (cohesion: 0.9025)
- #401 [0.9162] Abu Huraira said (may Allah be well pleased with him): “Fatima came to Abu Bakr and said: ‘Who will inherit from you?’ He said: ‘My wives and my offspring,’ so she said: ‘Why shoul
- #403 [0.9157] 'A’isha said (may Allah be well pleased with her): "Allah’s Messenger said (Allah bless him and give him peace): 'We are not inherited from. Whatever we leave behind is a charitabl
- #404 [0.9078] Abu Huraira (may Allah be well pleased with him) reported:  "The Prophet said (Allah bless him and give him peace): 'My legacy will not be distributed as gold coin, nor as silver c

**The Weeping Of Sayyidina Rasoolullah** (cohesion: 0.9017)
- #316 [0.9437] 'Abdu’llah ibn Abi Qais said: "I asked "A'isha (may Allah be well pleased with her) about the Qur’anic recitation of the Prophet (Allah bless him and give him peace): “Was he used 
- #315 [0.9253] Umm Salama said: "The Prophet (Allah bless him and give him peace) used to interrupt his Qur’anic recitation. He would say: “Praise be to Allah, the Lord of all the worlds [al-hamd
- #314 [0.9129] Qatada said: “I said to Anas ibn Malik: 'How was the Qur’anic recitation of Alla’s Messenger (Allah bless him and give him peace)?’ He said: ‘With the voice drawn out over the long

**The Laughing Of Rasoolullah** (cohesion: 0.9004)
- #227 [0.9434] Abdullah ibn al-Harith said (may Allah be well pleased with him): “The laughter of Allah’s Messenger (Allah bless him and give him peace) was nothing but a joyful smile.”
- #229 [0.9303] Jarir ibn ‘Abdi’llah said (may Allah be well pleased with him): “Allah’s Messenger (Allah bless him and give him peace) did not shun me from the time when I embraced Islam, and he 
- #226 [0.927] ‘Abdullah ibn al-Harith ibn Jaz said (may Allah be well pleased with him): "I have not seen anyone with a more cheerful countenance than Allah's Messenger (Allah bless him and give

**The Noble Features Of Rasoolullah** (cohesion: 0.8996)
- #3 [0.9441] Ibn Ishaq said: “I heard al-Bara’ ibn 'Azib say: "Allah’s Messenger(Allah bless him and give him peace)was neither curly nor lank-haired, of medium height, broad-shouldered, with l
- #8 [0.937] Al-Hasan ibn 'Ali (may Allah be well pleased with him and his father) said: “My maternal aunt Hind asked the son of Abu Hala, who was a describer of the finery of Allah’s Messenger
- #7 [0.9265] On the authority of 'Umar ibn 'Abdi’llah, the Mawla of Ghufra: 1 have been told by Ibrahim ibn Muhammad, one of the offspring of 'Ali ibn Abi Talib (may Allah be well pleased with 

**Seal Of Nubuwwah (Prophethood) Of Rasoolullah** (cohesion: 0.8993)
- #22 [0.917] Abu Nadra al-'Awaqi said: “I asked Sa'id al-Khudri about the Seal of Allah's Messenger (Allah bless him and give him peace), meaning the Seal of Prophethood, so he said: ‘It was a 
- #20 [0.9159] Abu Zaid 'Amr ibn Akhtab al-Ansari told me: “Allah’s Messenger (Allah bless him and give him peace) said to me: ‘O Abu Zaid, come close to me and stroke my back!’ I duly stroked hi
- #16 [0.9112] As-Sa’ib ibn Yazid said: ‘My maternal aunt took me to the Prophet (Allah bless him and give him peace), and she said; “O Messenger of Allah, my sister's son is in pain!” He therefo

**The Recital Of Sayyidina Rasoolullah** (cohesion: 0.8991)
- #301 [0.9448] 'A’isha said: "I did not see Allah’s Messenger (Allah bless him and give him peace) fast in any month more than his fasting for Allah’s sake in Sha'ban. He used to keep fast throug
- #305 [0.9418] 'A’isha said: “Allah’s Messenger (Allah bless him and give him peace) would not fast in any month more than he did in Sha'ban.”
- #302 [0.9301] 'Abdu’llah said: "Allah’s Messenger (Allah bless him and give him peace) used to fast three days at the beginning of every month, and he would seldom break fast on Friday, the Day 

**The Legacy Of Sayyidina Rasoolullah** (cohesion: 0.8962)
- #390 [0.9281] A’isha said: "When Allah’s Messenger died (Allah bless him and give him peace), they disagreed over where to bury him, so Abu Bakr said: “I heard Allah’s Messenger (Allah bless him
- #388 [0.9161] A’isha said: "I saw Allah’s Messenger (Allah bless him and give him peace) when he was at the point of death, and beside him there was a vessel containing water. He would dip his h
- #396 [0.9127] Abu Salama ibn 'Abd ar-Rahman ibn 'Awf said: "Allah’s Messenger (Allah bless him and give him peace) died on Monday and he was buried on Tuesday.”

**Salaatut Duha (Chaast Prayers)** (cohesion: 0.8901)
- #283 [0.9402] Ibn 'Umar said (may Allah be well pleased with him and his father): “Hafsa said: 'Allah’s Messenger (Allah bless him and give him peace) used to perform two cycles of ritual prayer
- #285 [0.939] Abdullah ibn Shaqiq said:  "I asked 'A’isha (may Allah be well pleased with her) about the ritual prayer of Allah’s Messenger (Allah bless him and give him peace), and she said: 'H
- #270 [0.939] 'A’isha said (may Allah be well pleased with her): “Allah’s Messenger (Allah bless him and give him peace) used to perform eleven cycles of ritual prayer during the night, making o

**Noble Character And Habits Of Sayyidina Rasoolullah** (cohesion: 0.8896)
- #336 [0.9344] Anas ibn Malik said (may Allah be well pleased with him): “Allah’s Messenger said (Allah bless him and give him peace): 'If a sheep’s trotter were given to me, I would receive it, 
- #331 [0.9188] Anas ibn Malik said (may Allah be well pleased with him): "Allah’s Messenger (Allah bless him and give him peace) used to visit the sick, attend funerals, ride a donkey, and accept
- #334 [0.9152] Anas ibn Malik (may Allah be well pleased with him) said: that there was no person dearer to them than Allah’s Messenger (Allah bless him and give him peace). He said: "Nevertheles

**Modesty Of Sayyidina Rasoolullah** (cohesion: 0.8887)
- #351 [0.9199] Jabir ibn 'Abdi’llah say: ‘Never did Allah’s Messenger (Allah bless him and give him peace) say “No” to anyone who requested something of him.!”
- #346 [0.9122] 'A’isha said: “Allah’s Messenger (Allah bless him and give him peace) was neither obscene, nor profligate, nor boisterous in the markets, and he would not repay a misdeed with a mi
- #354 [0.9109] 'Umar ibn al-Khattab said (may Allah be well pleased with him): "A man came to the Prophet (Allah bless him and give him peace) and asked him to give him a gift, so the Prophet sai

**Description Of The Saying Of Rasoolullah On Poetry** (cohesion: 0.8885)
- #240 [0.9101] 'A’isha (may Allah be well pleased with her) said that she was asked: "Was Allah’s Messenger (Allah bless him and give him peace) used to imitating any form of poetry?" She said: "
- #241 [0.9076] Abu Huraira said (may Allah be well pleased with him): “Allah’s Messenger said (Allah bless him and give him peace): ‘The most truthful saying spoken by a poet is the saying of Lab
- #249, 250 [0.9035] 'A’isha said: "Allah’s Messenger (Allah bless him and give him peace) used to set up a pulpit in the mosque for Hassan ibn Thabit. He would stand upright upon it, paying tribute to

**Rasoolullah Using 'Itr** (cohesion: 0.8867)
- #216 [0.9211] Thumama ibn 'Abdi’llah said: “Anas ibn Malik did not reject perfume. Anas also said: ‘The Prophet (Allah bless him and give him peace) did not reject perfume'.”
- #217 [0.9135] Ibn 'Umar said: "Allah’s Messenger said (Allah bless him and give him peace): Three things are not to be rejected: cushions, oil and perfume, and milk.’”
- #215 [0.887] Musa ibn Anas ibn Malik reports that his father said: “Allah’s Messenger (Allah bless him and give him peace) had a vial from which he used to perfume himself.”

**The Dressing Of Rasoolullah** (cohesion: 0.8856)
- #57 [0.9288] Umm Salama said: "The apparel dearest to Allah’s Messenger (Allah bless him and give him peace) was the shirt he used to wear.”
- #56 [0.9269] Umm Salama said: "The apparel dearest to Allah’s Messenger (Allah bless him and give him peace) was the shirt.”
- #63 [0.9237] Anas ibn Malik said: “The apparel dearest to Allah’s Messenger (Allah bless him and give him peace) was the hibara [striped garment of Yemenite fabric] that he used to wear.”

**Description Of The Joking Of Rasoolullah** (cohesion: 0.8855)
- #235 [0.9159] Anas ibn Malik said (may Allah be well pleased with him): "Allah’s Messenger (Allah bless him and give him peace) would associate so closely with us that he said to a young brother
- #238 [0.91] Anas ibn Malik said: “There was a man among the people of the desert — his name was Zahir — and he used to bring the Prophet (Allah bless him and give him peace) a present from the
- #237 [0.8997] Anas ibn Malik said: "A man asked Allah’s Messenger (Allah bless him and give him peace) to provide him with a mount, so he said: 'I will mount you on the offspring of a she-camel 

**What Rasoolullah Would Eat with Bread** (cohesion: 0.8736)
- #166 [0.9295] Abu Huraira said: ‘The Prophet (Allah bless him and give him peace) was brought some meat, so the foreleg was set before him, and he liked it, so he took a bite of it.”
- #161 [0.918] Anas ibn Malik said:  “A tailor invited Allah’s Messenger (Allah bless him and give him peace) to a meal he had made, so I went with Allah’s Messenger (Allah bless him and give him
- #180 [0.9153] Umm al-Mundhir said: “Allah’s Messenger (Allah bless him and give him peace) came to see me with 'Ali. We had some suspended clusters of grapes, so Allah’s Messenger (Allah bless h

**The Noble Age Of Sayyidina Rasoolullah** (cohesion: 0.872)
- #370 [0.9041] An-Nu'man ibn Bashir say: “Do you not have what you want in the way of food and drink? I have seen your Prophet (Allah bless him and give him peace), and the poor-quality dates [da
- #372 [0.8979] Abu Talha said: “We complained to Allah’s Messenger (Allah bless him and give him peace) of hunger, and we exposed our stomachs, each revealing a rock, so Allah’s Messenger (Allah 
- #376 [0.8973] Anas said: "Allah’s Messenger said (Allah bless him and give him peace): “I have been put in fear for Allah’s sake, while no one was afraid, and I have been troubled for Allah’s sa

### tirmidhi (32 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| The Book on Clothing | 52 | 0.8762 |
| Chapters on Supplication | 52 | 0.8746 |
| Chapters on Manners | 43 | 0.8733 |
| Chapters on the description of Paradise | 29 | 0.8714 |
| The Book on Blood Money | 125 | 0.8695 |
| Chapters on Seeking Permission | 39 | 0.8668 |
| Chapters on Knowledge | 33 | 0.8662 |
| Chapters on Virtues | 23 | 0.8659 |
| The Book on Food | 53 | 0.8624 |
| The Book on Drinks | 76 | 0.8565 |
| Chapters On Inheritance | 35 | 0.8564 |
| The Book on Virtues of Jihad | 26 | 0.8558 |
| Chapters On Dreams | 127 | 0.8556 |
| Chapters on The Virtues of the Qur'an | 48 | 0.854 |
| The Book on Hunting | 39 | 0.8533 |
| The Book on Jihad | 83 | 0.8528 |
| The Book on the Description of Hellfire | 31 | 0.8509 |
| The Book on Legal Punishments (Al-Hudud) | 66 | 0.8476 |
| Chapters On Wala' And Gifts | 14 | 0.8456 |
| Chapters on Tafsir | 17 | 0.8436 |
| Chapters On Wasaya (Wills and Testament) | 42 | 0.8404 |
| Chapters On Al-Fitan | 65 | 0.8377 |
| The Book on Military Expeditions | 36 | 0.8368 |
| Chapters on the description of the Day of Judgement, Ar-Riqaq, and Al-Wara' | 67 | 0.8334 |
| Chapters On Al-Qadar | 73 | 0.8321 |
| Chapters On Zuhd | 115 | 0.8316 |
| The Book on Sacrifices | 47 | 0.8305 |
| The Book on Faith | 148 | 0.8297 |
| Chapters on Medicine | 304 | 0.8294 |
| The Book on Vows and Oaths | 36 | 0.8278 |
| Chapters on Recitation | 135 | 0.8273 |
| Chapters On Witnesses | 158 | 0.8165 |

#### Representative hadiths per book

**The Book on Clothing** (cohesion: 0.8762)
- #1660 [0.9058] Narrated Abu Sa’id Al Khudri :  that the Messenger of Allah (saws) was asked: "Which of the people are most virtuous?" He said: "A man who take part in Jihad in Allah's cause." The
- #1665 [0.9035] Narrated Muhammad bin Al-Munkadir:  "Salman Al-Farisi passed by Shurahbil bin As-Simt while he was in garrison in which he and his companions were suffering from difficulties. He s
- #1646 [0.9027] Narrated Abu Musa:  "The Messenger of Allah (saws) was asked about a man who fights out of bravery, one who fights out of protection (for himself or others), and one who fought to 

**Chapters on Supplication** (cohesion: 0.8746)
- #2900 [0.9273] Narrated Abu Hurairah: that the Messenger of Allah (SAW) said: "Gather and I shall recite to you one third of the Qur'an." He said: "So whoever was to gather did so, then the Messe
- #2896 [0.9218] Narrated Abu Ayyub: that the Messenger of Allah (SAW) said: "Would one of you like to recite a third of the Qur'an during a night? Whoever recited: Allaahu Al-Wahid As-Samad then h
- #2876 [0.9205] Narrated Abu Hurairah: "The Messenger of Allah (SAW) sent an expedition force [comprised] of many, and he asked each what he could recite, so each one of them mentioned what he cou

**Chapters on Manners** (cohesion: 0.8733)
- #2674 [0.9113] Narrated Abu Hurairah: that the Messenger of Allah (SAW) said: "Whoever calls to guidance, then he receives the reward similar to the reward of whoever follows him, without that di
- #2669 [0.905] Narrated 'Abdullah bin 'Amr: that the Messenger of Allah (SAW) said: "Convey from me, even if it be an Ayah, and narrate from the Children of Isra'il, and there is no harm, And who
- #2671 [0.9029] Narrated Abu Mas'ud Al-Badri: that a man came to the Prophet (SAW) looking for a mount, he said: 'Mine has been ruined.' So the Messenger of Allah (SAW) said: 'Go to so-and-so.' So

**Chapters on the description of Paradise** (cohesion: 0.8714)
- #1172 [0.9016] Jabir narrated that The Prophet said: “Do not enter upon Al-Mughibar (the women whose husband are absent), for indeed the Shaitan flows through one of you as the blood flows.” We s
- #1154 [0.8977] Aishah narrated: “Barfah’s husband was a slave, so the Messenger of Allah let her chose, and she chose herself, and if he was a free man she would not have had a choice.”
- #1148 [0.8965] Aishah narrated: “My uncle through suckling came and asked permission (to enter) but I refused to admit him until I asked the Messenger of Allah. So the Messenger of Allah said: “L

**The Book on Blood Money** (cohesion: 0.8695)
- #1218 [0.9139] Narrated Anas bin Malik:  That the Messenger of Allah (saws) sold a saddle blanket and a drinking bowl. He (saws) said: "Who will buy saddle blanket and drinking bowl ?". So a man 
- #1276 [0.908] Narrated Abu Mas'ud Al-Ansari:  "The Messenger of Allah (saws) prohibited the price of a dog, the earnings of the fornicator (from harlotry), and the news of the fortune-teller." <
- #1221 [0.9067] Narrated Abu Hurairah:  "The Prophet (saws) prohibited meeting the goods being brought (to the market). If someone were to meet them and buy them, then the owner of the goods retai

**Chapters on Seeking Permission** (cohesion: 0.8668)
- #2615 [0.9049] Narrated Ibn 'Umar: that the Messenger of Allah (SAW) passed by a man and he was chastising his brother about modesty, so the Messenger of Allah (SAW) said: "Al-Haya' is part of fa
- #2608 [0.8949] Narrated Anas bin Malik: that the Messenger of Allah (SAW) said: "I have been ordered to fight the people until they bear witness to La Ilaha Illallah, and that Muhammad is His ser
- #2639 [0.8947] Narrated 'Abdullah bin 'Amr bin Al-'As: that the Messenger of Allah (SAW) said: "Indeed Allah will distinguish a man from my Ummah before all of creation on the Day of Judgement. N

**Chapters on Knowledge** (cohesion: 0.8662)
- #2604 [0.9085] An-Numan bin Bashir narrated that the Messenger Of Allah (s.a.w) said: "Indeed the person among the inhabitants of the Fire punished least [on the Day of Judgment] is a man who has
- #2574 [0.9066] Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Some of the Fire  (in the shape of a long neck) will come out of the Fire on the Day of judgment. It will have two 
- #2596 [0.9036] Abu Dharr narrated that the Messenger of Allah (s.a.w) said: " I know the last of the people of the Fire to depart from the Fire and the last of the people of Paradise to enter Par

**Chapters on Virtues** (cohesion: 0.8659)
- #2932 [0.9048] Narrated Umm Salamah: "The Messenger of Allah (SAW) recited this Ayah: 'Innahu 'Amalun Ghairu Salih'" (11:46)
- #2938 [0.8979] Narrated 'Aishah: that the Prophet (SAW) would recite: "Furuhun Wa Raihanun Wa Jannatu Na'im (56:89)"
- #2931 [0.8948] Narrated Umm Salamah: "The Prophet (SAW) would recite: 'Innahu 'Amila Ghaira Salih.'"

**The Book on Food** (cohesion: 0.8624)
- #1688 [0.908] Narrated Abu Ishaq:  From Al-Bara' bin 'Azib who said: "A man said to us: 'Did you flee from the Messenger of Allah (saws) O Abu 'Umarah ?'" He said: "No, By Allah! I did not flee 
- #1701 [0.9015] Narrated Ibn 'Abbas:  "The Messenger of Allah (saws) was a slave (of Allah), who would order as he has ben ordered to. He did not give an order to us instead of the people regardin
- #1689 [0.8953] Narrated Ibn 'Umar:  "Indeed we saw the day of Hunain, and indeed the two armies fled from the Messenger of Allah (saws), and there did not remain one hundred men with the Messenge

**The Book on Drinks** (cohesion: 0.8565)
- #1737 [0.9218] Narrated 'Ali bin Abi Talib:  "The Messenger of Allah (saws) prohibited me from rings of gold, and from wearing Al-Qassi, and from reciting in the bowing and prostration positions,
- #1765 [0.9062] Narrated Asma' bint Yazid bin As-Sakan Al-Ansariyyah: "The sleeves of (the shirt) of the Messenger of Allah (saws) were to the wrist." </p>  [Abu 'Eisa said:] This Hadith is Hasan 
- #1773 [0.9038] Narrated Qatadah:  From Anas: "The sandals of the Prophet (saws) had two straps." </p>  [Abu 'Eisa said:] This Hadith is Hasan Sahih. </p>  He said: There are narrations on this to

**Chapters On Inheritance** (cohesion: 0.8564)
- #460 [0.8924] Ali narrated: "Allah's Messenger would perform Al-Witr with three, reciting nine Surah from the Mufassal in them, reciting three Surah in each Rak'ah with Say: "Allah is One." At t
- #479 [0.8897] `Abdullah bin Abi Awfa narrated that : Allah's Messenger (saws) said: "Whoever has a need from Allah, or from one of the sons of Adam, then let him perform Wudu', performing it wel
- #482 [0.8873] Abu Rafi narrated that : Allah's Messenger said to Al-Abbas: "O uncle! Shall I not give to you, shall I not present to you, shall I not benefit you?" He said: "Of course, O Messeng

**The Book on Virtues of Jihad** (cohesion: 0.8558)
- #1532 [0.919] Narrated Abu Hurairah: That the Messenger of Allah (saws) said: "Whoever swears [about an oath] and says: 'If Allah wills (Insha Allah), then he will not have broken it."
- #1531 [0.9185] Narrated Ibn 'Umar: That the Messenger of Allah (saws) said: "Whoever swears about an oath and says: 'If Allah wills (Insha Allah), then there is no breaking of the oath against hi
- #1524 [0.9032] Narrated 'Aishah: That the Messenger of Allah (saws) said: "There is no vowing for disobedience, and its atonement is the atonement of an oath."

**Chapters On Dreams** (cohesion: 0.8556)
- #768 [0.9224] Abdullah bin Shaqiq narrated: "I asked Aishah about the Prophet's fasting.' She said: 'He would fast until we said: "He has fasted" and he would abstain from fasting until we said:
- #766 [0.905] Abu Hurairah narrated that: The Messenger of Allah said: "There are two joys for the fasting person: the joy when he breaks his fast, and the joy of when he meets his Lord."
- #711 [0.9039] Aishah narrated that : Hamzah bin Amr Al-Aslami asked the Messenger of Allah about fasting while traveling, and he fasted regularly. So the Messenger of Allah said: 'If you wish th

**Chapters on The Virtues of the Qur'an** (cohesion: 0.854)
- #2706 [0.9046] Narrated Abu Hurairah: that the Messenger of Allah (SAW) said: "When one of you arrives at the gathering, then give the Salam, and if he is given a place to sit, then let him sit. 
- #2689 [0.9016] Narrated 'Imran bin Husain: "A man came to the Prophet (SAW) and said: 'As-Salamu 'Alaykum (Peace be upon you).'" [He said:] "So the Prophet (SAW) said: 'Ten.' Then another came an
- #2731 [0.8988] Narrated Abu Umamah: that the Messenger of Allah (SAW) said: "From the complete of visiting the ill is that one of you place his hand on his forehead" - or he said - "on his hand, 

**The Book on Hunting** (cohesion: 0.8533)
- #1413 [0.9112] Narrated 'Amr bin Shu'aib: from his father, from his grandfather that the Messenger of Allah (saws) said: "The Muslim is not killed for disbeliever."  And with this chain, it has b
- #1420 [0.9015] Narrated 'Abdullah bin 'Amr: that the Messenger of Allah (saws) said: "If someone tries to get another's wealth without right, and he fights and is killed, then he is a martyr."
- #1407 [0.8972] Narrated Abu Hurairah: "A man was killed during the time of the Messenger of Allah (saws), so the killer was brought to the man's guardian. The killer said: 'O Messenger of Allah! 

**The Book on Jihad** (cohesion: 0.8528)
- #1589 [0.9187] Narrated 'Uqbah bin 'Amir:  "I said: 'O Messenger of Allah! We come across a people and they do not host us, and they do not give us our rights, and we do not take anything from th
- #1558 [0.9079] Narrated 'Aishah:  That the Messenger of Allah (saws) advanced towards Badr till he reached Harrah Al-Wabr where he was met by a man from the idolaters, about whom it was said he w
- #1567 [0.9074] Narrated 'Ali:  That the Messenger of Allah (saws) said that Jibra'il had indeed descended upon him to say to him: "Tell them - meaning your Companions - to choose regarding the ca

**The Book on the Description of Hellfire** (cohesion: 0.8509)
- #1192 [0.8974] Hisham bin Urwah narrated from his father, from Aishah that she said: "The people were such that a man would divorce his wife when he wanted to divorce her, and she remained his wi
- #1180 [0.8968] Fatimah bint Qais said: "My husband divorced me three times during the time of the Prophet. So the Messenger of Allah said: 'There is no housing for you nor maintenance.'" Al-Mughi
- #1175 [0.8871] Yunus bin Jubair said: "I asked Ibn Umar about a man who divorced his wife while she was menstruating. So he said: 'Don't you know Abdullah bin Umar?' Indeed he divorced his wife w

**The Book on Legal Punishments (Al-Hudud)** (cohesion: 0.8476)
- #1339 [0.9122] Umm Salamah narrated that the Messenger of Allah (saws) said: "Indeed you come to me with your disputes, and I am only a human being, perhaps one of you is more eloquent at present
- #1343 [0.9] Abu Hurairah narrated: "The Messenger of Allah (saws) passed judgement based on an oath along with one witness." Rabi'ah (one of the narrators) said: "A son of Ibn Sa'd bin 'Ubadah
- #1384 [0.8989] Narrated Rafi' bin Khadij: "The Messenger of Allah (saws) forbade us from a matter that was of benefit for us. When one of us had some land and we would let someone use it for a po

**Chapters On Wala' And Gifts** (cohesion: 0.8456)
- #541 [0.8802] Abu Hurairah narrated: "When Allah's Messenger would go out on the day of Eid by one route, he would return by another."
- #533 [0.8767] An-Numan bin Bashir narrated: "For the two Eid and the Friday prayer, the Prophet would recite: Glorify the Name of your Lord, the Most High, and Has there come to you the narratio
- #531 [0.8718] Ibn Umar narrated: "Allah's Messenger, Abu Bakr, and Umar would pray during the two Eid before the Khutbah, then they would give the Khutbah."

**Chapters on Tafsir** (cohesion: 0.8436)
- #2866 [0.9067] Narrated Abu Hurairah: that the Messenger of Allah (SAW) said: "The parable of the believer is like the plant; the wind does not stop causing it to sway, and the believer does not 
- #2860 [0.9032] Narrated Sa'eed bin Hilal: that Jabir bin 'Abdullah Al-Ansari said: "One day the Messenger of Allah (SAW) came out to us and said: "While I was sleeping I had a vision as if Jibra'
- #2862 [0.9005] Narrated Jabir bin 'Abdullah: that the Messenger of Allah (SAW) said: "The parable of myself and the Prophets [before myself] is that of a man who constructed a house. He completed

**Chapters On Wasaya (Wills and Testament)** (cohesion: 0.8404)
- #506 [0.9006] Ibn Umar narrated: "The Prophet would give a Khutbah on Friday, then sit, then stand and give (another) Khutbah." He said: "Similar to what they do today."
- #510 [0.8892] Jabir bin Abdullah narrated: "The Prophet was delivering a Khutbah on Friday when a man came. The Prophet said: 'Have you prayed?' He said no. So he said: 'Then stand and pray.'" A
- #522 [0.8859] Nafi narrated about Ibn Umar: "When he prayed the Friday prayer, he left and prayed two prostrations (Rak'ah) in his house. Then he said: 'Allah's Messenger would do this.'"

**Chapters On Al-Fitan** (cohesion: 0.8377)
- #657 [0.8994] Abu Rafi (may Allah be pleased with him) narrated that : the Messenger of Allah sent a man from Banu Makhzun to collect charity, so he said to Abu Rafi: "Accompany me so that perha
- #650 [0.8968] Abdullah bin Mas'ud narrated that : the Messenger of Allah said: "Whoever begs from the people while he has what he needs, he will come on the Day of Judgment and his begging with 
- #655 [0.8925] Abu Sa'eed Al-Khudri narrated: "During the time of the Messenger of Allah, a man suffered a loss on fruits that he had sold, resulting in more debt. The Messenger of Allah said: 'G

**The Book on Military Expeditions** (cohesion: 0.8368)
- #1521 [0.9137] Narrated Jabir bin 'Abdullah: "I attended the Eid Al-Adha' with the Prophet (saws) at the Musalla. When he finished his Khutbah, he descended from his Minbar and was given a male s
- #1508 [0.9124] Narrated Al-Bara' bin 'Azib : "The Messenger of Allah (saws) delivered a sermon to us on the Day of Nahr and he said: 'None of you should slaughter until he performs the Salat." He
- #1500 [0.897] Narrated 'Uqbah bin 'Amir: That the Messenger of Allah (saws) gave him sheep to distribute among his Companions as a sacrifice. "There remained a young male kid or a young billy go

**Chapters on the description of the Day of Judgement, Ar-Riqaq, and Al-Wara'** (cohesion: 0.8334)
- #1084 [0.8935] Abu Hurairah narrated that: The Messenger of Allah said: "When someone whose religion and character you are pleased with proposes to (someone under the care) of one of you, then ma
- #1085 [0.8922] Abu Hatim Al-Muzani narrated that: The Messenger of Allah said: "When someone whose religion and character you are pleased with comes to you then marry (her to) him. If you do not 
- #1114 [0.8843] Sahl bin Sa'd As-Sa'idi narrated that: A woman came to the Messenger of Allah and said: "I present myself to you (for marriage)." So she stood for a long time. Then a man said: "O 

**Chapters On Al-Qadar** (cohesion: 0.8321)
- #561 [0.8962] Aishah narrated: "The sun was eclipsed during the time of the Messenger of Allah, so the Messenger of Allah led the people in prayer. He recited a lengthy recitation, then he bowed
- #580 [0.8883] Aisha narrated: "When the Messenger of Allah would prostrate (for recitation of) the Qur'an, he would say: (Sajada wajhiya lilladhi khalaqahu wa shaqqa sam'ahu wa basarahu bihawlih
- #579 [0.8862] Al-Hasan bin Muhammad bin Ubaidullah bin Abi Yazid said: Ibn Juraij said to me: O Hasan! Ubaidullah bin Abi Yazid informed me that Ibn Abbas said: "A man came to the Prophet and sa

**Chapters On Zuhd** (cohesion: 0.8316)
- #983 [0.8988] Thabit narrated from Anas, that: The Prophet entered upon a young man while he was dying. So he said: "How do you feel?" He said: "By Allah! O Messenger of Allah! Indeed I hope in 
- #1046 [0.898] Ibn Umar narrated: "When he Prophet put the deceased in the grave" He said: And Abu Khalid (one of the narrators) said [one time]: "When he placed the deceased in the Lahd" - "He s
- #1034 [0.8939] Abu Ghalib narrated: "I prayed for the funeral of a man with Anas bin Malik, so he stood parallel to his head. Then they came with the body of a woman from the Quraish. They said: 

**The Book on Sacrifices** (cohesion: 0.8305)
- #1433 [0.9091] Narrated 'Ubaidullah bin 'Abdullah bin 'Uthbah: That he heard from Abu Hurairah, Zaid bin Khalid, and Shibl, that they were with the Prophet (saws) and two men came to him disputin
- #1428 [0.9061] Narrated Abu Hurairah: "Ma'iz Al-Aslamu came to the Messenger of Allah (saws) and said that he had committed adultery, so he (saws) turned away from him. Then he approached from hi
- #1441 [0.9044] Narrated Abu 'Abdur-Rahman As-Sulami: "Ali gave a Khutbah, and said: 'O people, establish the penalties upon your slaves, those married from them and those unmarried. A slave girl 

**The Book on Faith** (cohesion: 0.8297)
- #13 [0.8922] Hudhaifah narrated: "Allah's Messenger came to a waste area used by people, so he urinated on it while standing. I brought him the (water for) Wudu. Then I left to be away from him
- #65 [0.889] Ibn Abbas narrated: "One of the wives of the Prophet performed Ghusl with a bowl. Allah's Messenger wanted to perform Wudu with it, so she said: 'O Messenger of Allah! Indeed I am 
- #47 [0.8886] Abdullah bin Zaid narrated that: "The Prophet performed Wudu. So he washed his face three times, and washed his hands two times each, and wiped his head, and washed his feet [two t

**Chapters on Medicine** (cohesion: 0.8294)
- #289 [0.8944] Abdullah bin Mas'ud narrated: "Allah's Messenger taught us, that when we sit for every two Rak'ah we should say: (At-Tahyyatulillah, was-salawatu wattayybaat. As-salamu alaika ayyu
- #364 [0.8918] Ash-Sha'bi narrated: "Al-Mughirah bin Shu'bah led us in Salat, and he continued after the two Rak'ah, so the people said: 'Subhan Allah' and he said: 'Subhan Allah' to them. When h
- #303 [0.8915] Abu Hurairah narrated: "Allah's Messenger entered the Masjid, and a man entered and offered Salat. Then he came to give Salam to the Propet. He returned the Salam to him and said: 

**The Book on Vows and Oaths** (cohesion: 0.8278)
- #1470 [0.9084] Narrated 'Adi bin Hatim: "I asked the Messenger of Allah (saws) about the game caught by a trained dog. He said: 'If you mention the Name of Allah when you send your trained dog, t
- #1465 [0.9069] Narrated 'Adi bin Hatim: "I said: 'O Messenger of Allah! We send our trained dogs to catch game for us.' He said: 'Eat what it catches for you.' I said: 'O Messenger of Allah, and 
- #1474 [0.8967] Narrated Umm Habibah bint Al-'Irbad: From her father: "On the day of Khaibar, the Messenger of Allah (saws) prohibited eating the meat of every predator that has canine teeth, the 

**Chapters on Recitation** (cohesion: 0.8273)
- #2818 [0.8987] Narrated Al-Miswar bin Makhramah: "The Messenger of Allah (SAW) distributed some cloaks but he did not give anything to Makhramah. Makhramah said: 'O my son! Let us go to the Messe
- #2846 [0.8844] Narrated 'Aishah: "The Messenger of Allah (SAW) had a Minbar placed in the Masjid for Hassan to stand to boast (poetically) about the Messenger of Allah (SAW)" - or she said: "to d
- #2743 [0.8826] Narrated Iyas bin Salamah: from his father: "A man sneezed in the presence of the Messenger of Allah (SAW) while I was present, so the Messenger of Allah (SAW) said: 'Yarhamukallah

**Chapters On Witnesses** (cohesion: 0.8165)
- #941 [0.8926] Ibn Abbas narrated: "Duba'ah bint Az-Zubair came to the prophet and said: 'O Messenger of Allah! I want to perform Hajj so should I state a condition?' He said: 'Yes.' She asked: '
- #824 [0.8775] Salim bin Abdullah narrated that : he had heard a man from Ash-Sham asking Abdullah bin Umar about Tamattu after Umrah until Hajj, so Abdullah bin Umar said: "It is lawful." The ma
- #950 [0.877] Ibn Umar said: "When the Prophet would come home from a battle, or Hajj, or Umrah, when he was it a tract of land or raised area he would say 'Allahu Akbar (Allah is Most Great)' t

### virtues (1 books)

| Book | Hadiths | Cohesion |
|------|---------|---------|
| Special Virtues of the Qur'an's Chapters and Verses | 93 | 0.883 |

#### Representative hadiths per book

**Special Virtues of the Qur'an's Chapters and Verses** (cohesion: 0.883)
- #74 [0.9203] Jābir reported: “During the two rakʿahs of ṭawāf, the Messenger of Allah ﷺ recited the two suwar: Qul yā ayyuhal kāfirūn (Sūrat al-Kāfirūn), and Qul huwa Allāhu aḥad (Sūrat al-Ikhl
- #83 [0.9203] Jābir reported: “During the two rakʿahs of ṭawāf, the Messenger of Allah ﷺ recited the two suwar: Qul yā ayyuhal kāfirūn (Sūrat al-Kāfirūn), and Qul huwa Allāhu aḥad (Sūrat al-Ikhl
- #75 [0.9181] Ubayy reported: "In the first rakʿah of witr (prayer), the Messenger of Allah ﷺ used to recite: “Sabbiḥ isma rabbikal-aʿlā (Sūrat al-Aʿlā), in the second, Qul yā ayyuhal kāfirūn (S
