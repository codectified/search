# mxbai Quantization Ladder

Six variants of `mxbai-embed-large` / `mxbai-embed-xsmall`, stepped from full F16
through GGUF 4-bit down to ONNX INT4. All variants query the `small-model-eval`
index; BM25 on `english-mxbai` is the lexical baseline.

**Filters & boosts** (identical to production semantic search)

| Setting | Status |
|---|---|
| `isChainRef` exclusion | **ON** — chain-reference hadiths excluded from results |
| Dedup by `dupGroup` | **ON** — highest collection-boosted member wins per group |
| Collection boosts | **ON** — bukhari 5×, muslim 4.8×, nawawi40 3.3×, malik/ahmad/riyadussalihin 2.5×, nasai 3.5×, abudawud 3×, tirmidhi 2.5×, ibnmajah/darimi/mishkat 2× |
| Embed times | Post-warmup — all models loaded into memory before measurement |

> **Note on Ollama latency:** With only 2 Ollama models (F16 + Q4_K_M), both fit in
> Ollama's loaded-model cache simultaneously — no eviction between queries. These numbers
> reflect true single-model steady-state latency. In the full small-model comparison where
> 5 Ollama models compete, each evicts the others between queries, adding ~440 ms reload
> overhead per switch. The quant ladder numbers here are more representative of production.

## Contents

- [Latency Summary](#latency-summary)
- [Per-Query Results](#per-query-results)
  - [good character and manners](#query-good-character-and-manners)
  - [angels recording deeds](#query-angels-recording-deeds)
  - [prayer at night](#query-prayer-at-night)
  - [forgiving someone who wronged you](#query-forgiving-someone-who-wronged-you)
  - [comparing yourself to others](#query-comparing-yourself-to-others)
  - [aisha](#query-aisha)
  - [fasting expiation sins](#query-fasting-expiation-sins)
  - [neighbor rights](#query-neighbor-rights)

---

## Latency Summary

All times are post-warmup averages across 8 queries. Models run in model-major order —
all 8 queries for one model before switching — so Ollama never evicts a model mid-batch.
With only 2 Ollama models (F16 + Q4_K_M), both can stay resident simultaneously.
Speedup is relative to the F16 embed time (embed cost dominates for CPU inference).

| Step | Model | Dims | Backend | Avg Embed | Avg Search | Avg Total | Speedup vs F16 |
|---|---|---|---|---|---|---|---|
| — | BM25 Lexical | — | ES query_string | — | 20ms | 20ms | — |
| 1 | mxbai-large F16 | 1024-dim | Ollama | 46ms | 85ms | 131ms | baseline |
| 2 | mxbai-large Q4_K_M | 1024-dim | Ollama | 48ms | 86ms | 134ms | 1.0× |
| 3 | mxbai-large INT8 ONNX | 1024-dim | ONNX Runtime | 24ms | 82ms | 106ms | 1.9× |
| 4 | mxbai-xsmall FP32 | 384-dim | SentenceTransformers | 12ms | 78ms | 90ms | 3.8× |
| 5 | mxbai-xsmall INT8 ONNX | 384-dim | ONNX Runtime | 3ms | 80ms | 83ms | 15.2× |
| 6 | mxbai-xsmall INT4 ONNX | 384-dim | ONNX Runtime | 6ms | 80ms | 86ms | 7.6× |

---

## Per-Query Results

## Query: good character and manners

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 90ms |
| mxbai-large F16 | 37ms | 105ms |
| mxbai-large Q4_K_M | 46ms | 106ms |
| mxbai-large INT8 ONNX | 23ms | 80ms |
| mxbai-xsmall FP32 | 11ms | 78ms |
| mxbai-xsmall INT8 ONNX | 5ms | 81ms |
| mxbai-xsmall INT4 ONNX | 6ms | 79ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="14%"><strong>BM25 Lexical</strong><br><small>no encoding · query_string</small></th>
<th width="14%"><strong>mxbai-large F16</strong><br><small>1024-dim · 335M · Ollama (F16)</small></th>
<th width="14%"><strong>mxbai-large Q4_K_M</strong><br><small>1024-dim · 335M · Ollama GGUF</small></th>
<th width="14%"><strong>mxbai-large INT8 ONNX</strong><br><small>1024-dim · 335M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall FP32</strong><br><small>384-dim · 33M · SentenceTransformers</small></th>
<th width="14%"><strong>mxbai-xsmall INT8 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall INT4 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 18.0449 <small>· Sahih</small><br><br>We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafahhish, and he use</td>
<td valign="top"><strong>forty 22</strong>&nbsp; 0.8371<br><br>A man who knows his worth will not be ruined.</td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.8320<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8546 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7668 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7562 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7687 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>adab 290</strong>&nbsp; 15.1631 <small>· Da'if</small><br><br>Abu'd-Darda' stood up in the night to pray. He was weeping and said, 'O Allah! You made my physical form good, so make my character good!' until morni</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8333<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>forty 22</strong>&nbsp; 0.8304<br><br>A man who knows his worth will not be ruined.</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8521<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7666 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7509 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7547 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 14.9349 <small>· Hasan</small><br><br>"Nothing is placed on the Scale that is heavier than good character. Indeed the person with good character will have attained the rank of the person o</td>
<td valign="top"><strong>shamail 350</strong>&nbsp; 0.8324 <small>· Da'if Isnād</small><br><br>Al-Hasan ibn 'Ali said: “Al-Husain said: ‘I asked my father how the Prophet (Allah bless him and give him peace) comported himself among his table com</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8302<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8508<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.7414<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>shamail 349</strong>&nbsp; 0.7434 <small>· Sahih</small><br><br>'Aisha said (may Allah be well pleased with her): "A man sought permission to come in to see Allah’s Messenger (Allah bless him and give him peace) wh</td>
<td valign="top"><strong>shamail 349</strong>&nbsp; 0.7393 <small>· Sahih</small><br><br>'Aisha said (may Allah be well pleased with her): "A man sought permission to come in to see Allah’s Messenger (Allah bless him and give him peace) wh</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bukhari 6029</strong>&nbsp; 14.7588 <small>· Sahih</small><br><br>Abdullah bin 'Amr mentioned Allah's Apostle saying that he was neither a Fahish nor a Mutafahish. Abdullah bin 'Amr added, Allah's Apostle said, 'The </td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.8322<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8282 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8499 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7381<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.7406<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7355<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 14.6536 <small>· Sahih</small><br><br>The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those who have the best manners and c</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8275 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8251 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>adab 271</strong>&nbsp; 0.8464 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr said, "The Prophet, may Allah bless him and grant him peace, was neither coarse nor loud. He used to say, "The best of you is the o</td>
<td valign="top"><strong>shamail 349</strong>&nbsp; 0.7376 <small>· Sahih</small><br><br>'Aisha said (may Allah be well pleased with her): "A man sought permission to come in to see Allah’s Messenger (Allah bless him and give him peace) wh</td>
<td valign="top"><strong>bukhari 28</strong>&nbsp; 0.7295<br><br>Narrated 'Abdullah bin 'Amr: A person asked Allah's Apostle . "What (sort of) deeds in or (what qualities of) Islam are good?" He replied, "To feed (t</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7350 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>bukhari 3759, 3760</strong>&nbsp; 14.2273 <small>· Sahih</small><br><br>Allah's Apostle neither talked in an insulting manner nor did he ever speak evil intentionally. He used to say, "The most beloved to me amongst you is</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8242 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>forty 5</strong>&nbsp; 0.8236<br><br>The person guiding (someone) to do a good deed, is like the one performing the good deed.</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.8442 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>bukhari 28</strong>&nbsp; 0.7361<br><br>Narrated 'Abdullah bin 'Amr: A person asked Allah's Apostle . "What (sort of) deeds in or (what qualities of) Islam are good?" He replied, "To feed (t</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7284<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
<td valign="top"><strong>bukhari 28</strong>&nbsp; 0.7338<br><br>Narrated 'Abdullah bin 'Amr: A person asked Allah's Apostle . "What (sort of) deeds in or (what qualities of) Islam are good?" He replied, "To feed (t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>mishkat 5770</strong>&nbsp; 13.8450 <small>· Uncategorized</small><br><br>God has sent me to perfect good qualities of character and to complete good deeds." It is transmitted in Sharh as-sunna .</td>
<td valign="top"><strong>shamail 8</strong>&nbsp; 0.8231 <small>· Da'if Isnād</small><br><br>Al-Hasan ibn 'Ali (may Allah be well pleased with him and his father) said: “My maternal aunt Hind asked the son of Abu Hala, who was a describer of t</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.8210<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.8440<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7350<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7240 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>bukhari 6236</strong>&nbsp; 0.7313<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet, "What Islamic traits are the best?" The Prophet said, "Feed the people, and greet those whom you</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>adab 270</strong>&nbsp; 13.2727 <small>· Uncategorized</small><br><br>Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.8223<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8201<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.8435<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7319 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7232<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>abudawud 5143</strong>&nbsp; 0.7308 <small>· Sahih</small><br><br>Ibn ‘Umar reported the Messenger of Allah (May peace be upon him) as saying: One of the finest acts of kindness is for a man to treat his father’s fri</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 13.2451 <small>· Sahih</small><br><br>"It is a smiling face, doing one's best in good, and refraining from harm."</td>
<td valign="top"><strong>shamail 224</strong>&nbsp; 0.8214 <small>· Da'if Isnād</small><br><br>Al-Hasan ibn 'Ali said (may Allah the Exalted be well pleased with him and his father): “I said to my maternal uncle, Hind ibn Abi Hala, who was skill</td>
<td valign="top"><strong>hisn 231</strong>&nbsp; 0.8177<br><br>If any of you praises his companion then let him say: Aḥsibu fulānan wallāhu ḥasībuh wa lā uzakkī `alallāhi aḥada. If any of you praises his companion</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.8399<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>bukhari 6236</strong>&nbsp; 0.7301<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet, "What Islamic traits are the best?" The Prophet said, "Feed the people, and greet those whom you</td>
<td valign="top"><strong>abudawud 5143</strong>&nbsp; 0.7168 <small>· Sahih</small><br><br>Ibn ‘Umar reported the Messenger of Allah (May peace be upon him) as saying: One of the finest acts of kindness is for a man to treat his father’s fri</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.7302<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>adab 273</strong>&nbsp; 12.7513 <small>· Sahih</small><br><br>I was sent to perfect good character."</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.8207 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8161<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>bukhari 6029</strong>&nbsp; 0.8396<br><br>Narrated Masruq: Abdullah bin 'Amr mentioned Allah's Apostle saying that he was neither a Fahish nor a Mutafahish. Abdullah bin 'Amr added, Allah's Ap</td>
<td valign="top"><strong>riyadussalihin 341</strong>&nbsp; 0.7283<br><br>'Abdullah bin 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said, "The finest act of goodness is that a person should treat kind</td>
<td valign="top"><strong>bukhari 6236</strong>&nbsp; 0.7157<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet, "What Islamic traits are the best?" The Prophet said, "Feed the people, and greet those whom you</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7300<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
</tr>
</tbody></table>

---

## Query: angels recording deeds

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 9ms |
| mxbai-large F16 | 38ms | 83ms |
| mxbai-large Q4_K_M | 46ms | 83ms |
| mxbai-large INT8 ONNX | 22ms | 80ms |
| mxbai-xsmall FP32 | 22ms | 77ms |
| mxbai-xsmall INT8 ONNX | 4ms | 79ms |
| mxbai-xsmall INT4 ONNX | 6ms | 80ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="14%"><strong>BM25 Lexical</strong><br><small>no encoding · query_string</small></th>
<th width="14%"><strong>mxbai-large F16</strong><br><small>1024-dim · 335M · Ollama (F16)</small></th>
<th width="14%"><strong>mxbai-large Q4_K_M</strong><br><small>1024-dim · 335M · Ollama GGUF</small></th>
<th width="14%"><strong>mxbai-large INT8 ONNX</strong><br><small>1024-dim · 335M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall FP32</strong><br><small>384-dim · 33M · SentenceTransformers</small></th>
<th width="14%"><strong>mxbai-xsmall INT8 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall INT4 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 17.2169 <small>· Sahih</small><br><br>The Great and the Glorious Lord said (to angels): Whenever My servant intends to commit an evil, do not record it against him, but if he actually comm</td>
<td valign="top"><strong>muslim 2689</strong>&nbsp; 0.8306<br><br>Abu Huraira reported Allah's Apostle (may peace be upon him) as saying Allah has mobile (squads) of angels, who have no other work (to attend to but) </td>
<td valign="top"><strong>bukhari 7429</strong>&nbsp; 0.8279<br><br>Narrated Abu Huraira: Allah's Apostle said, "(A group of) angels stay with you at night and (another group of) angels by daytime, and both groups gath</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8528 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7944<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.7956<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7993<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>mishkat 2112</strong>&nbsp; 16.6777 <small>· Uncategorized</small><br><br>One who is skilled in the Qur’ān is associated with the noble, upright recording angels; and he who falters when reciting the Qur’ān and finds it diff</td>
<td valign="top"><strong>bukhari 7429</strong>&nbsp; 0.8243<br><br>Narrated Abu Huraira: Allah's Apostle said, "(A group of) angels stay with you at night and (another group of) angels by daytime, and both groups gath</td>
<td valign="top"><strong>mishkat 463</strong>&nbsp; 0.8258<br><br>‘Ali reported God’s messenger as saying, “The angels do not enter a house in which there is a picture, a dog, or one who is defiled.” Abu Dawud and Na</td>
<td valign="top"><strong>bukhari 6491</strong>&nbsp; 0.8506<br><br>Narrated Ibn `Abbas: The Prophet narrating about his Lord I'm and said, "Allah ordered (the appointed angels over you) that the good and the bad deeds</td>
<td valign="top"><strong>mishkat 44</strong>&nbsp; 0.7839 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh ", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “When one of you makes a good profession of Islam, every good deed he does will be recorded for him te</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7953<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>mishkat 44</strong>&nbsp; 0.7824 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh ", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “When one of you makes a good profession of Islam, every good deed he does will be recorded for him te</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>abudawud 1454</strong>&nbsp; 16.6777 <small>· Sahih</small><br><br>One who is skilled in the Qur'an is associated with the noble, upright recording angels, and he who falters when he recites the Qur'an and finds it di</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8206<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8251<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>ibnmajah 76</strong>&nbsp; 0.8461 <small>· Sahih</small><br><br>'Abdullah bin Mas'ud said: "The Messenger of Allah (SAW), the true and truly inspired one, told us that: 'The creation of one of you is put together i</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7756<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>mishkat 44</strong>&nbsp; 0.7874 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh ", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “When one of you makes a good profession of Islam, every good deed he does will be recorded for him te</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7775<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>mishkat 1560</strong>&nbsp; 16.0469 <small>· Uncategorized</small><br><br>When a Muslim is afflicted with some trouble in his body the angel is told to record for him his good deeds which he was accustomed to do. Then if God</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8195 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8233 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.8447<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>mishkat 2096</strong>&nbsp; 0.7580<br><br>Anas reported God's messenger as saying that when lailat al-qadr comes Gabriel descends with a company of angels who invoke blessings on everyone who </td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7862<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>abudawud 1454</strong>&nbsp; 0.7654 <small>· Sahih</small><br><br>'Aishah reported the Prophet (saws) as saying: One who is skilled in the Qur'an is associated with the noble, upright recording angels, and he who fal</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 15.4689 <small>· Uncategorized</small><br><br>God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it, God enters it for him in His record as a comple</td>
<td valign="top"><strong>mishkat 463</strong>&nbsp; 0.8189<br><br>‘Ali reported God’s messenger as saying, “The angels do not enter a house in which there is a picture, a dog, or one who is defiled.” Abu Dawud and Na</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.8233<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8437<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7564<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7610<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>muslim 128 b</strong>&nbsp; 0.7602<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) observed: Allah, the Great and Glorious, said: When</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>abudawud 5263</strong>&nbsp; 15.3019 <small>· Sahih</small><br><br>The Prophet (saws) said: If anyone kills a gecko with the first blow, such and such number of good deeds will be recorded for him, if he kills it with</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.8189<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>mishkat 2594</strong>&nbsp; 0.8219<br><br>‘A’isha reported God’s messenger as saying, “There is no day when God sets free more servants from hell than the day of ‘Arafa. He draws near, then pr</td>
<td valign="top"><strong>bukhari 7429</strong>&nbsp; 0.8430<br><br>Narrated Abu Huraira: Allah's Apostle said, "(A group of) angels stay with you at night and (another group of) angels by daytime, and both groups gath</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.7503<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>mishkat 2096</strong>&nbsp; 0.7602<br><br>Anas reported God's messenger as saying that when lailat al-qadr comes Gabriel descends with a company of angels who invoke blessings on everyone who </td>
<td valign="top"><strong>mishkat 635</strong>&nbsp; 0.7588<br><br>Concerning God’s words, “The recitation of the dawn is witnessed,” (Al-Qur’an, 17:78). Abu Huraira quoted the Prophet as saying, "The angels of the ni</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>muslim 2644</strong>&nbsp; 14.9987 <small>· Sahih</small><br><br>When the drop of (semen) remains in the womb for forty or forty five nights, the angel comes and says: My Lord, will he be good or evil? And both thes</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.8180<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>ibnmajah 76</strong>&nbsp; 0.8214 <small>· Sahih</small><br><br>'Abdullah bin Mas'ud said: "The Messenger of Allah (SAW), the true and truly inspired one, told us that: 'The creation of one of you is put together i</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8423<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>bukhari 3223</strong>&nbsp; 0.7483<br><br>Narrated Abu Huraira: The Prophet said, "Angels keep on descending from and ascending to the Heaven in turn, some at night and some by daytime, and al</td>
<td valign="top"><strong>muslim 128 b</strong>&nbsp; 0.7542<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) observed: Allah, the Great and Glorious, said: When</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7575<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>riyadussalihin 1864</strong>&nbsp; 14.4177 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) said, "He who kills a chameleon at the first blow, such and such number of good deeds will be awarded to him; whoever ki</td>
<td valign="top"><strong>ibnmajah 76</strong>&nbsp; 0.8177 <small>· Sahih</small><br><br>'Abdullah bin Mas'ud said: "The Messenger of Allah (SAW), the true and truly inspired one, told us that: 'The creation of one of you is put together i</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.8203<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>riyadussalihin 547</strong>&nbsp; 0.8419<br><br>Abu Hurairah (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Everyday two angels descend and one of them says, 'O Allah! Co</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.7479<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.7507<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7572<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 14.3222 <small>· Sahih</small><br><br>When it occurs to my bondsman that he should do a good deed but he actually does not do it, record one good to him, but if he puts it into practice, I</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.8175<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.8201<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.8415<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>mishkat 635</strong>&nbsp; 0.7465<br><br>Concerning God’s words, “The recitation of the dawn is witnessed,” (Al-Qur’an, 17:78). Abu Huraira quoted the Prophet as saying, "The angels of the ni</td>
<td valign="top"><strong>bukhari 3223</strong>&nbsp; 0.7489<br><br>Narrated Abu Huraira: The Prophet said, "Angels keep on descending from and ascending to the Heaven in turn, some at night and some by daytime, and al</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.7555<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>ibnmajah 1426</strong>&nbsp; 14.0222 <small>· Sahih</small><br><br>“The first thing for which a person will be brought to account on the Day of Resurrection will be his prayer. If it is complete, then the voluntary (p</td>
<td valign="top"><strong>muslim 632 a</strong>&nbsp; 0.8170<br><br>Abu Huraira reported: The Messenger of Allah (may peace be upon him) said: Angels take turns among you by night and by day, and they all assemble at t</td>
<td valign="top"><strong>muslim 632 a</strong>&nbsp; 0.8199<br><br>Abu Huraira reported: The Messenger of Allah (may peace be upon him) said: Angels take turns among you by night and by day, and they all assemble at t</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.8405<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>bukhari 3332</strong>&nbsp; 0.7462<br><br>Narrated `Abdullah: Allah's Apostle, the true and truly inspired said, "(as regards your creation), every one of you is collected in the womb of his m</td>
<td valign="top"><strong>bukhari 3332</strong>&nbsp; 0.7485<br><br>Narrated `Abdullah: Allah's Apostle, the true and truly inspired said, "(as regards your creation), every one of you is collected in the womb of his m</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.7554<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
</tr>
</tbody></table>

---

## Query: prayer at night

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 13ms |
| mxbai-large F16 | 43ms | 81ms |
| mxbai-large Q4_K_M | 48ms | 83ms |
| mxbai-large INT8 ONNX | 21ms | 82ms |
| mxbai-xsmall FP32 | 9ms | 78ms |
| mxbai-xsmall INT8 ONNX | 2ms | 79ms |
| mxbai-xsmall INT4 ONNX | 6ms | 79ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="14%"><strong>BM25 Lexical</strong><br><small>no encoding · query_string</small></th>
<th width="14%"><strong>mxbai-large F16</strong><br><small>1024-dim · 335M · Ollama (F16)</small></th>
<th width="14%"><strong>mxbai-large Q4_K_M</strong><br><small>1024-dim · 335M · Ollama GGUF</small></th>
<th width="14%"><strong>mxbai-large INT8 ONNX</strong><br><small>1024-dim · 335M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall FP32</strong><br><small>384-dim · 33M · SentenceTransformers</small></th>
<th width="14%"><strong>mxbai-xsmall INT8 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall INT4 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>riyadussalihin 1071</strong>&nbsp; 9.9731 <small>· Uncategorized</small><br><br>I heard the Messenger of Allah (PBUH) saying: "One who performs 'Isha' prayer in congregation, is as if he has performed Salat for half of the night. </td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8847<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8834<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8939<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8607<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8592<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8670<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 9.9572 <small>· Sahih</small><br><br>Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of the night.</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8796 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8808<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8930<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8505 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8536 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8554 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>ibnmajah 1327</strong>&nbsp; 9.9569 <small>· Sahih</small><br><br>“We fasted Ramadan with the Messenger of Allah (saw) and he did not lead us in praying Qiyam (prayers at night) during any part of it, until there wer</td>
<td valign="top"><strong>muslim 740</strong>&nbsp; 0.8763<br><br>'A'isha observed that the Messenger of Allah (may peace be upon him) used to observe prayer in the night and the last of his (night) prayer was Witr.</td>
<td valign="top"><strong>muslim 740</strong>&nbsp; 0.8779<br><br>'A'isha observed that the Messenger of Allah (may peace be upon him) used to observe prayer in the night and the last of his (night) prayer was Witr.</td>
<td valign="top"><strong>muslim 740</strong>&nbsp; 0.8890<br><br>'A'isha observed that the Messenger of Allah (may peace be upon him) used to observe prayer in the night and the last of his (night) prayer was Witr.</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8492<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8425 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8538 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>ibnmajah 286</strong>&nbsp; 9.9426 <small>· Sahih</small><br><br>"Whenever the Messenger of Allah got up for prayer at night to pray Tahajjud (night optional prayer), he would clean his mouth with the tooth stick."</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8754<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>bukhari 997</strong>&nbsp; 0.8766<br><br>Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8881<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8483 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8425<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8538<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>bulugh 380</strong>&nbsp; 9.9318 <small>· Uncategorized</small><br><br>Allah's Messenger (SAW) offered Witr prayer (on different nights) at various hours, extending (from the 'Isha' prayer) up to the last hour of the nigh</td>
<td valign="top"><strong>bukhari 997</strong>&nbsp; 0.8739<br><br>Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he</td>
<td valign="top"><strong>muslim 514</strong>&nbsp; 0.8746<br><br>'A'isha reported: The Apostle of Allah (may peace be upon him) said prayer at night and I was by his side in a state of meanses and I had a sheet pull</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8871 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8437<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8413<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8502<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>tirmidhi 806</strong>&nbsp; 9.9219 <small>· Sahih</small><br><br>"We fasted with the Prophet, so he did not pray (the night prayer) with us until seven (nights) of the month remained. Then he (pbuh) led us in prayer</td>
<td valign="top"><strong>muslim 514</strong>&nbsp; 0.8733<br><br>'A'isha reported: The Apostle of Allah (may peace be upon him) said prayer at night and I was by his side in a state of meanses and I had a sheet pull</td>
<td valign="top"><strong>bukhari 990</strong>&nbsp; 0.8738<br><br>Narrated Ibn `Umar: Once a person asked Allah's Apostle (saws) about the night prayer. Allah's Apostle (saws) replied, "The night prayer is offered as</td>
<td valign="top"><strong>muslim 755 a</strong>&nbsp; 0.8866<br><br>Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he sho</td>
<td valign="top"><strong>abudawud 1307</strong>&nbsp; 0.8435 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Do not give up prayer at night, for the Messenger of Allah (saws) would not leave it. Whenever he fell ill or lethargi</td>
<td valign="top"><strong>ibnmajah 1252</strong>&nbsp; 0.8296 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “Safwan bin Mu’attal asked the Messenger of Allah (saw): ‘O Messenger of Allah, I want to ask you about someth</td>
<td valign="top"><strong>abudawud 1314</strong>&nbsp; 0.8394 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Prophet (saws) said: Any person who offers prayer at night regularly but (on a certain night) he is dominated by s</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 9.9218 <small>· Sahih</small><br><br>Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to follow him in the </td>
<td valign="top"><strong>bukhari 990</strong>&nbsp; 0.8725<br><br>Narrated Ibn `Umar: Once a person asked Allah's Apostle (saws) about the night prayer. Allah's Apostle (saws) replied, "The night prayer is offered as</td>
<td valign="top"><strong>muslim 755 a</strong>&nbsp; 0.8722<br><br>Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he sho</td>
<td valign="top"><strong>muslim 514</strong>&nbsp; 0.8865<br><br>'A'isha reported: The Apostle of Allah (may peace be upon him) said prayer at night and I was by his side in a state of meanses and I had a sheet pull</td>
<td valign="top"><strong>abudawud 1314</strong>&nbsp; 0.8380 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Prophet (saws) said: Any person who offers prayer at night regularly but (on a certain night) he is dominated by s</td>
<td valign="top"><strong>abudawud 1307</strong>&nbsp; 0.8275 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Do not give up prayer at night, for the Messenger of Allah (saws) would not leave it. Whenever he fell ill or lethargi</td>
<td valign="top"><strong>abudawud 1307</strong>&nbsp; 0.8391 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Do not give up prayer at night, for the Messenger of Allah (saws) would not leave it. Whenever he fell ill or lethargi</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>tirmidhi 221</strong>&nbsp; 9.9061 <small>· Sahih</small><br><br>"Whoever attends Isha (prayer) in congregation, then he has (the reward as if he had) stood half of the night. And whoever prays Isha and Fajr in cong</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8722<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>bulugh 390</strong>&nbsp; 0.8702<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "If anyone is afraid that he may not get up in the latter part of the night, he should offer Witr i</td>
<td valign="top"><strong>bukhari 990</strong>&nbsp; 0.8864<br><br>Narrated Ibn `Umar: Once a person asked Allah's Apostle (saws) about the night prayer. Allah's Apostle (saws) replied, "The night prayer is offered as</td>
<td valign="top"><strong>abudawud 1304</strong>&nbsp; 0.8287 <small>· Hasan</small><br><br>Narrated Abdullah Ibn Abbas: In Surat al-Muzzammil (73), the verse: "Keep vigil at night but a little, a half thereof" (2-3) has been abrogated by the</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8252<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8374 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 564</strong>&nbsp; 9.9051 <small>· Sahih</small><br><br>"One night Allah's Apostle led us in the `Isha' prayer and that is the one called Al-`Atma [??] by the people. After the completion of the prayer, he </td>
<td valign="top"><strong>muslim 749 b</strong>&nbsp; 0.8709<br><br>Salim reported on the authority of his father that a person asked the Apostle of Allah (may peace be upon him) about the night prayer. He said: It con</td>
<td valign="top"><strong>bukhari 212</strong>&nbsp; 0.8699<br><br>Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep) till his slumber is over because in pr</td>
<td valign="top"><strong>muslim 749 b</strong>&nbsp; 0.8856<br><br>Salim reported on the authority of his father that a person asked the Apostle of Allah (may peace be upon him) about the night prayer. He said: It con</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8267<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>abudawud 419</strong>&nbsp; 0.8248 <small>· Sahih</small><br><br>Narrated An-Nu'man ibn Bashir: I am the one who is best informed of the time of this prayer, i.e. the night prayer. The Messenger of Allah (saws) used</td>
<td valign="top"><strong>mishkat 1254</strong>&nbsp; 0.8369<br><br>Ibn ‘Umar reported God’s Messenger as saying, “Prayer during the night should consist of pairs of rak'as , but if one of you fears the morning is near</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>nasai 5202</strong>&nbsp; 9.8950 <small>· Sahih</small><br><br>"The Messenger of Allah [SAW] delayed 'Isha' prayer one night, until half the night had passed, then he came out and led us in prayer. And it is as if</td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.8700<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>muslim 749 b</strong>&nbsp; 0.8691<br><br>Salim reported on the authority of his father that a person asked the Apostle of Allah (may peace be upon him) about the night prayer. He said: It con</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8845 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8266 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8215 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
<td valign="top"><strong>malik 267</strong>&nbsp; 0.8353<br><br>Yahya related to me from Malik from Nafi and Abdullah ibn Umar that a man asked the Messenger of Allah, may Allah bless him and grant him peace, about</td>
</tr>
</tbody></table>

---

## Query: forgiving someone who wronged you

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 12ms |
| mxbai-large F16 | 51ms | 81ms |
| mxbai-large Q4_K_M | 53ms | 83ms |
| mxbai-large INT8 ONNX | 30ms | 83ms |
| mxbai-xsmall FP32 | 10ms | 77ms |
| mxbai-xsmall INT8 ONNX | 2ms | 78ms |
| mxbai-xsmall INT4 ONNX | 11ms | 80ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="14%"><strong>BM25 Lexical</strong><br><small>no encoding · query_string</small></th>
<th width="14%"><strong>mxbai-large F16</strong><br><small>1024-dim · 335M · Ollama (F16)</small></th>
<th width="14%"><strong>mxbai-large Q4_K_M</strong><br><small>1024-dim · 335M · Ollama GGUF</small></th>
<th width="14%"><strong>mxbai-large INT8 ONNX</strong><br><small>1024-dim · 335M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall FP32</strong><br><small>384-dim · 33M · SentenceTransformers</small></th>
<th width="14%"><strong>mxbai-xsmall INT8 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall INT4 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ahmad 930</strong>&nbsp; 16.8779 <small>· Hasan</small><br><br>`Abdur-Razzaq said. Someone who saw `Ali when he rode told me: When he put his foot in the stirrup, he said: Bismillah (in the Name of Allah). When he</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8291<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8227<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8625<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7959 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7881 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7920 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>adab 667</strong>&nbsp; 15.8980 <small>· Da'if</small><br><br>The firmest supplication is to say, 'O Allah, you are my Lord and I am Your slave. I have wronged myself and I admit my wrong action. Only You forgive</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.8228 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.8215 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>bukhari 2449</strong>&nbsp; 0.8518<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his reputation or anything else, he should beg him to for</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7799 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7760 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7702 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>adab 706</strong>&nbsp; 15.5979 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>hisn 57</strong>&nbsp; 0.8222<br><br>Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfir lī maghfiratam’min `indika warḥamnī innaka 'anta ‘l-Ghafūr</td>
<td valign="top"><strong>forty 28</strong>&nbsp; 0.8189<br><br>One who repents from sin is like someone without sin.</td>
<td valign="top"><strong>nasai 4723</strong>&nbsp; 0.8506 <small>· Sahih</small><br><br>It was narrated from 'Alqamah binWa'il Al-Hadrami that his farther said: A man who had killed someone was brought to the Messenger of Allah, and he wa</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7757<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7753 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7646 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>ahmad 56</strong>&nbsp; 14.7569 <small>· Sahih</small><br><br>I heard ‘Ali say: If I heard a hadeeth from the Messenger of Allah (ﷺ), Allah benefitted me as He willed thereby. If someone else told me something fr</td>
<td valign="top"><strong>muslim 1695 b</strong>&nbsp; 0.8213<br><br>'Abdullah b. Buraida reported on the authority of his father that Ma'iz b. Malik al-Aslami came to Allah's Messenger (may peace be upon him) and said:</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8177<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8496<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7586 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7577<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7627<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>ahmad 47, 48</strong>&nbsp; 14.1649 <small>· Sahih</small><br><br>If Heard something from the Messenger of Allah (ﷺ), Allah would benefit me thereby as He willed. Abu Bakr told me - and Abu Bakr spoke the truth - he </td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8162<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>forty 27</strong>&nbsp; 0.8157<br><br>Hearts are predisposed to love someone who does them good and detest someone who does them harm.</td>
<td valign="top"><strong>mishkat 3277</strong>&nbsp; 0.8474<br><br>Ibn ‘Abbas said: One makes atonement for something he has made unlawful for himself.* You have had a good example in God’s Messenger. * i.e. something</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7504 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7494 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7582 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>ahmad 8</strong>&nbsp; 14.1250 <small>· Sahih</small><br><br>Teach me a dua that I may say in my prayer. He said: `Say: O Allah, I have wronged myself greatly and no one forgives sins but you, grant me forgivene</td>
<td valign="top"><strong>tirmidhi 2495</strong>&nbsp; 0.8152 <small>· Hasan</small><br><br>Abu Dharr narrated that the Messenger of Allah (s.a.w) said: "Allah,Most High said: 'O My Slaves! All of you are astray except whom I guide, so ask Me</td>
<td valign="top"><strong>bukhari 7387, 7388</strong>&nbsp; 0.8122<br><br>Narrated `Abdullah bin `Amr: Abu Bakr As-Siddiq said to the Prophet "O Allah's Apostle! Teach me an invocation with which I may invoke Allah in my pra</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.8466 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>riyadussalihin 210</strong>&nbsp; 0.7472<br><br>Abu Hurairah (May Allah bepleased with him) reported: The Prophet (PBUH) said, "He who has done a wrong affecting his brother's honour or anything els</td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.7459<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7492 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>adab 673</strong>&nbsp; 14.0837 <small>· Sahih</small><br><br>One of the supplications of the Prophet, may Allah bless him and grant him peace, was 'O Allah, forgive me for my past and future wrong actions, what </td>
<td valign="top"><strong>bulugh 825</strong>&nbsp; 0.8149<br><br>Narrated [Abu Hurairah (RA)]: Allah's Messenger (SAW) said, "Whoever accepts back what he sold to a Muslim, Allah will forgive his fault." [Reported b</td>
<td valign="top"><strong>bukhari 3480</strong>&nbsp; 0.8121<br><br>Narrated Abu Huraira: Allah's Apostle said, "A man used to give loans to the people and used to say to his servant, 'If the debtor is poor, forgive hi</td>
<td valign="top"><strong>bulugh 319</strong>&nbsp; 0.8464<br><br>Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I h</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7405 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>riyadussalihin 210</strong>&nbsp; 0.7448<br><br>Abu Hurairah (May Allah bepleased with him) reported: The Prophet (PBUH) said, "He who has done a wrong affecting his brother's honour or anything els</td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.7488<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>adab 688</strong>&nbsp; 14.0330 <small>· Sahih</small><br><br>Abu Musa reported that the Prophet, may Allah bless him and grant him peace, used to make this supplication, "O Allah, forgive my errors, my ignorance</td>
<td valign="top"><strong>nasai 4723</strong>&nbsp; 0.8143 <small>· Sahih</small><br><br>It was narrated from 'Alqamah binWa'il Al-Hadrami that his farther said: A man who had killed someone was brought to the Messenger of Allah, and he wa</td>
<td valign="top"><strong>adab 617</strong>&nbsp; 0.8116 <small>· Sahih</small><br><br>Shaddad ibn Aws reported that the Prophet, may Allah bless him and grant him peace, said, "The best way of asking forgiveness is 'O Allah, You are my </td>
<td valign="top"><strong>adab 673</strong>&nbsp; 0.8464 <small>· Sahih</small><br><br>Abu Hurayra said, "One of the supplications of the Prophet, may Allah bless him and grant him peace, was 'O Allah, forgive me for my past and future w</td>
<td valign="top"><strong>forty 34</strong>&nbsp; 0.7382<br><br>On the authority of Anas (may Allah be pleased with him), who said: I heard the Messenger of Allah (PBUH) say: Allah the Almighty said: O son of Adam,</td>
<td valign="top"><strong>bulugh 1556</strong>&nbsp; 0.7406<br><br>Shaddad bin Aus (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “The best manner of asking for forgiveness is to say: “O Allah! You are my</td>
<td valign="top"><strong>adab 293</strong>&nbsp; 0.7478 <small>· Sahih</small><br><br>Abu Mas'ud al-Ansari reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Before your time a man was called to accoun</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>ahmad 28</strong>&nbsp; 14.0007 <small>· Sahih</small><br><br>Teach me a du'a` that I may say in my prayer. He said: `Say: O Allah. I have wronged myself greatly and no one forgives sins except You, so grant me f</td>
<td valign="top"><strong>mishkat 3277</strong>&nbsp; 0.8139<br><br>Ibn ‘Abbas said: One makes atonement for something he has made unlawful for himself.* You have had a good example in God’s Messenger. * i.e. something</td>
<td valign="top"><strong>bulugh 825</strong>&nbsp; 0.8111<br><br>Narrated [Abu Hurairah (RA)]: Allah's Messenger (SAW) said, "Whoever accepts back what he sold to a Muslim, Allah will forgive his fault." [Reported b</td>
<td valign="top"><strong>bukhari 3480</strong>&nbsp; 0.8454<br><br>Narrated Abu Huraira: Allah's Apostle said, "A man used to give loans to the people and used to say to his servant, 'If the debtor is poor, forgive hi</td>
<td valign="top"><strong>bulugh 1556</strong>&nbsp; 0.7378<br><br>Shaddad bin Aus (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “The best manner of asking for forgiveness is to say: “O Allah! You are my</td>
<td valign="top"><strong>ahmad 1363</strong>&nbsp; 0.7359 <small>· A Hasan Hadeeth]</small><br><br>It was narrated that ‘Ali (رضي الله عنه) said: The Messenger of Allah (رضي الله عنه) said: `Shall I not teach you some words which, if you say them yo</td>
<td valign="top"><strong>ahmad 1363</strong>&nbsp; 0.7453 <small>· A Hasan Hadeeth]</small><br><br>It was narrated that ‘Ali (رضي الله عنه) said: The Messenger of Allah (رضي الله عنه) said: `Shall I not teach you some words which, if you say them yo</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bulugh 319</strong>&nbsp; 14.0007 <small>· Uncategorized</small><br><br>He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I have greatly wronged myself, and no</td>
<td valign="top"><strong>malik 1520</strong>&nbsp; 0.8129<br><br>Malik related to me from Zurayq ibn Hakim al-Ayli that a man called Misbah asked his son for help and he thought him unnecessarily slow. When the son </td>
<td valign="top"><strong>mishkat 3277</strong>&nbsp; 0.8108<br><br>Ibn ‘Abbas said: One makes atonement for something he has made unlawful for himself.* You have had a good example in God’s Messenger. * i.e. something</td>
<td valign="top"><strong>bulugh 1517</strong>&nbsp; 0.8442<br><br>Anas (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “The atonement of backbiting a man is to ask Allah to forgive him.” Related by Al-Har</td>
<td valign="top"><strong>forty 39</strong>&nbsp; 0.7357<br><br>On the authority of Ibn Abbas (may Allah be pleased with him), that the Messenger of Allah (peace and blessings of Allah be upon him) said: Verily All</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.7350<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.7404 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
</tr>
</tbody></table>

---

## Query: comparing yourself to others

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 11ms |
| mxbai-large F16 | 54ms | 82ms |
| mxbai-large Q4_K_M | 47ms | 81ms |
| mxbai-large INT8 ONNX | 39ms | 83ms |
| mxbai-xsmall FP32 | 11ms | 79ms |
| mxbai-xsmall INT8 ONNX | 6ms | 79ms |
| mxbai-xsmall INT4 ONNX | 6ms | 81ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="14%"><strong>BM25 Lexical</strong><br><small>no encoding · query_string</small></th>
<th width="14%"><strong>mxbai-large F16</strong><br><small>1024-dim · 335M · Ollama (F16)</small></th>
<th width="14%"><strong>mxbai-large Q4_K_M</strong><br><small>1024-dim · 335M · Ollama GGUF</small></th>
<th width="14%"><strong>mxbai-large INT8 ONNX</strong><br><small>1024-dim · 335M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall FP32</strong><br><small>384-dim · 33M · SentenceTransformers</small></th>
<th width="14%"><strong>mxbai-xsmall INT8 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall INT4 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>muslim 1776 d</strong>&nbsp; 13.1936 <small>· Sahih</small><br><br>This hadith has been narrated on the authority of Bara' with another chain of transmitters, but this hadith is short as compared with other ahadith wh</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8145<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8091<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8453<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7205<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7254 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7225<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>abudawud 4627</strong>&nbsp; 11.8770 <small>· Sahih</small><br><br>We used to say in the times of the Prophet (saws): We do not compare anyone with Abu Bakr. ’Umar came next and then ‘Uthman. We then would leave (rest</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8031<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7977<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.8377<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7198<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7241<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7149<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>muslim 2431</strong>&nbsp; 11.3899 <small>· Sahih</small><br><br>There are many persons amongst men who are quite perfect but there are none perfect amongst women except Mary, daughter of 'Imran, Asiya wife of Phara</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7971<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7929<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8313<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7192 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7225<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7128 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bukhari 3334</strong>&nbsp; 11.2561 <small>· Sahih</small><br><br>The Prophet said, "Allah will say to that person of the (Hell) Fire who will receive the least punishment, 'If you had everything on the earth, would </td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7928<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7885<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.8308<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7148<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7218<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>bulugh 1527</strong>&nbsp; 0.7119<br><br>’Iyad bin Himar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Allah, the Most High has revealed to me that you (people) should be humbl</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>abudawud 356</strong>&nbsp; 10.7595 <small>· Hasan</small><br><br>I have embraced Islam. The Prophet (saws) said to him: Remove from yourself the hair that grew during of unbelief, saying "shave them". He further say</td>
<td valign="top"><strong>adab 159</strong>&nbsp; 0.7910<br><br>Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. T</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7849<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>adab 159</strong>&nbsp; 0.8282<br><br>Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. T</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7112<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7145<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
<td valign="top"><strong>bulugh 928</strong>&nbsp; 0.7112<br><br>A narration by Muslim has: He said, "Call someone other than me as a witness to this." He then said, "Would you like them to be equal in their kind tr</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>mishkat 6025</strong>&nbsp; 10.4603 <small>· Uncategorized</small><br><br>In the time of the Prophet, we did not compare anyone with Abu Bakr. `Umar came next and then Uthman. We would then leave the Prophet's companions wit</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7869<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>adab 159</strong>&nbsp; 0.7839<br><br>Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. T</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.8275 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>riyadussalihin 571</strong>&nbsp; 0.7054<br><br>Ibn 'Umar (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said: "Envy is justified in regard to two types of persons only: a man w</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7088<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7101<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>mishkat 48</strong>&nbsp; 10.3950 <small>· Uncategorized</small><br><br>He also said that he asked the Prophet what was the most excellent aspect of faith, and received the reply, “That you should love for God’s sake, hate</td>
<td valign="top"><strong>muslim 2536</strong>&nbsp; 0.7830<br><br>'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to</td>
<td valign="top"><strong>abudawud 4092</strong>&nbsp; 0.7838 <small>· Sahih in chain</small><br><br>Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been gi</td>
<td valign="top"><strong>muslim 2536</strong>&nbsp; 0.8273<br><br>'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to</td>
<td valign="top"><strong>riyadussalihin 997</strong>&nbsp; 0.7047<br><br>Ibn 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said: "Envy is justified in regard to two types of persons only: a man whom Al</td>
<td valign="top"><strong>riyadussalihin 997</strong>&nbsp; 0.7087<br><br>Ibn 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said: "Envy is justified in regard to two types of persons only: a man whom Al</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7092<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>muslim 2939 b</strong>&nbsp; 10.0806 <small>· Sahih</small><br><br>What did you ask? Mughira replied: I said that the people alleged that he would have a mountain load of bread and mutton and rivers of water. Thereupo</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7829 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>muslim 2536</strong>&nbsp; 0.7812<br><br>'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.8208<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>muslim 816</strong>&nbsp; 0.7037<br><br>'Abdullah b. Mas'ud reported Allah's Messenger (may peace be upon him) as saying: There should be no envy but only in case of two persons: one having </td>
<td valign="top"><strong>riyadussalihin 571</strong>&nbsp; 0.7071<br><br>Ibn 'Umar (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said: "Envy is justified in regard to two types of persons only: a man w</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7062<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 4816</strong>&nbsp; 9.8959 <small>· Sahih</small><br><br>(regarding) the Verse: 'And you have not been screening against yourself lest your ears, and your eyes and your skins should testify against you..' (4</td>
<td valign="top"><strong>abudawud 4092</strong>&nbsp; 0.7815 <small>· Sahih in chain</small><br><br>Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been gi</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7812 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>muslim 2963 c</strong>&nbsp; 0.8200<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those wh</td>
<td valign="top"><strong>bulugh 1527</strong>&nbsp; 0.7013<br><br>’Iyad bin Himar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Allah, the Most High has revealed to me that you (people) should be humbl</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7069<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
<td valign="top"><strong>riyadussalihin 997</strong>&nbsp; 0.7050<br><br>Ibn 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said: "Envy is justified in regard to two types of persons only: a man whom Al</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>mishkat 2757</strong>&nbsp; 9.3983 <small>· Uncategorized</small><br><br>Yahya b. Sa'id said that God’s messenger was sitting when a grave was being dug in Medina. A man looked down into the grave and said, "What a bad-rest</td>
<td valign="top"><strong>adab 898</strong>&nbsp; 0.7814 <small>· Sahih</small><br><br>Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes </td>
<td valign="top"><strong>adab 898</strong>&nbsp; 0.7778 <small>· Sahih</small><br><br>Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes </td>
<td valign="top"><strong>adab 898</strong>&nbsp; 0.8200 <small>· Sahih</small><br><br>Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes </td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.6986<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>riyadussalihin 371</strong>&nbsp; 0.7054<br><br>Abu Hurairah (May Allah be pleased with him) reported: I heard Messenger of Allah (PBUH) saying, "People are like gold and silver; those who were best</td>
<td valign="top"><strong>adab 426</strong>&nbsp; 0.7049 <small>· Sahih</small><br><br>The Prophet, may Allah bless him and grant him peace, said, "Allah Almighty revealed to me that you should be humble and that you should not wrong one</td>
</tr>
</tbody></table>

---

## Query: aisha

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 9ms |
| mxbai-large F16 | 42ms | 81ms |
| mxbai-large Q4_K_M | 52ms | 85ms |
| mxbai-large INT8 ONNX | 17ms | 83ms |
| mxbai-xsmall FP32 | 8ms | 80ms |
| mxbai-xsmall INT8 ONNX | 2ms | 83ms |
| mxbai-xsmall INT4 ONNX | 5ms | 82ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="14%"><strong>BM25 Lexical</strong><br><small>no encoding · query_string</small></th>
<th width="14%"><strong>mxbai-large F16</strong><br><small>1024-dim · 335M · Ollama (F16)</small></th>
<th width="14%"><strong>mxbai-large Q4_K_M</strong><br><small>1024-dim · 335M · Ollama GGUF</small></th>
<th width="14%"><strong>mxbai-large INT8 ONNX</strong><br><small>1024-dim · 335M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall FP32</strong><br><small>384-dim · 33M · SentenceTransformers</small></th>
<th width="14%"><strong>mxbai-xsmall INT8 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall INT4 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 1972</strong>&nbsp; 5.3097 <small>· Sahih</small><br><br>that when Saudah bint Zam'ah grew old, she gave her day to 'Aishah, and the Messenger of Allah went to 'Aishah on Saudah's day.</td>
<td valign="top"><strong>bukhari 3894</strong>&nbsp; 0.8492<br><br>Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then </td>
<td valign="top"><strong>abudawud 4164</strong>&nbsp; 0.8521 <small>· Da'if</small><br><br>Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing wi</td>
<td valign="top"><strong>bukhari 4401</strong>&nbsp; 0.8730<br><br>Narrated `Aisha: (the wife of the Prophet) Safiya bin Huyai, the wife of the Prophet menstruated during Hajjat-ul- Wada` The Prophet said, "Is she goi</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8283<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8362<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8199<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>bukhari 5212</strong>&nbsp; 5.3071 <small>· Sahih</small><br><br>Sauda bint Zam`a gave up her turn to me (`Aisha), and so the Prophet used to give me (`Aisha) both my day and the day of Sauda.</td>
<td valign="top"><strong>bukhari 277</strong>&nbsp; 0.8462<br><br>Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head</td>
<td valign="top"><strong>bukhari 277</strong>&nbsp; 0.8516<br><br>Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head</td>
<td valign="top"><strong>bukhari 2688</strong>&nbsp; 0.8684<br><br>Narrated Aisha: Whenever Allah's Apostle intended to go on a journey, he used to draw lots among his wives and would take with him the one on whom the</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8267<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8250<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8177 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>muslim 2046 b</strong>&nbsp; 5.3001 <small>· Sahih</small><br><br>'A'isha a family which has no dates (in their house) its members will be hungry; (or) 'A'isha the family which has no dates its members may be hungry.</td>
<td valign="top"><strong>abudawud 4164</strong>&nbsp; 0.8448 <small>· Da'if</small><br><br>Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing wi</td>
<td valign="top"><strong>bukhari 3894</strong>&nbsp; 0.8495<br><br>Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then </td>
<td valign="top"><strong>bukhari 2593</strong>&nbsp; 0.8684<br><br>Narrated Aisha: Whenever Allah's Apostle wanted to go on a journey, he would draw lots as to which of his wives would accompany him. He would take her</td>
<td valign="top"><strong>bukhari 5419</strong>&nbsp; 0.8244<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other women is like the superiority of Tharid to other kinds of food . "</td>
<td valign="top"><strong>bukhari 3411</strong>&nbsp; 0.8232<br><br>Narrated Abu Musa: Allah's Apostle said, "Many amongst men reached (the level of) perfection but none amongst the women reached this level except Asia</td>
<td valign="top"><strong>bukhari 5419</strong>&nbsp; 0.8169<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other women is like the superiority of Tharid to other kinds of food . "</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bulugh 1059</strong>&nbsp; 5.2994 <small>· Uncategorized</small><br><br>Sauda (RA) daughter of Zam'ah gave away her day to 'Aishah (RA). So the Prophet (SAW) allotted a share to 'Aishah (RA) of her day and Sauda's. [Agreed</td>
<td valign="top"><strong>bukhari 1151</strong>&nbsp; 0.8426<br><br>Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I sai</td>
<td valign="top"><strong>abudawud 1497</strong>&nbsp; 0.8494 <small>· Da'if</small><br><br>Narrated Aisha, Ummul Mu'minin: Ata' said: The quilt of Aisha was stolen. She began to curse the person who had stolen it. The Prophet (saws) began to</td>
<td valign="top"><strong>bukhari 2029</strong>&nbsp; 0.8676<br><br>Narrated `Aisha: (the wife of the Prophet) Allah's Apostle used to let his head in (the house) while he was in the mosque and I would comb and oil his</td>
<td valign="top"><strong>bukhari 3411</strong>&nbsp; 0.8140<br><br>Narrated Abu Musa: Allah's Apostle said, "Many amongst men reached (the level of) perfection but none amongst the women reached this level except Asia</td>
<td valign="top"><strong>bukhari 5419</strong>&nbsp; 0.8216<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other women is like the superiority of Tharid to other kinds of food . "</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8166<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>nasai 3213</strong>&nbsp; 5.2966 <small>· Sahih</small><br><br>It was narrated from 'Aishah that the Messenger of Allah forbade celibacy.</td>
<td valign="top"><strong>bukhari 902</strong>&nbsp; 0.8424<br><br>Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of f</td>
<td valign="top"><strong>bukhari 1151</strong>&nbsp; 0.8494<br><br>Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I sai</td>
<td valign="top"><strong>bukhari 1289</strong>&nbsp; 0.8675<br><br>Narrated `Aisha: (the wife of the Prophet) Once Allah's Apostle passed by (the grave of) a Jewess whose relatives were weeping over her. He said, "The</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8130<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
<td valign="top"><strong>bukhari 6249</strong>&nbsp; 0.8157<br><br>Narrated `Aisha: Allah's Apostle said, "O `Aisha! This is Gabriel sending his greetings to you." I said, "Peace, and Allah's Mercy be on him (Gabriel)</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8130<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>muslim 2445</strong>&nbsp; 5.2936 <small>· Sahih</small><br><br>'A'isha reported that when Allah's Messenger (may peace be upon him) set ont on a journey, he used to cast lots amongst his wives. Once this lot came </td>
<td valign="top"><strong>bukhari 4573</strong>&nbsp; 0.8419<br><br>Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of </td>
<td valign="top"><strong>bukhari 4573</strong>&nbsp; 0.8485<br><br>Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of </td>
<td valign="top"><strong>bukhari 1539</strong>&nbsp; 0.8672<br><br>Narrated `Aisha: (the wife of the Prophet (p.b.u.h) I used to scent Allah's Apostle when he wanted to assume Ihram and also on finishing Ihram before </td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8112 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8151 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
<td valign="top"><strong>bukhari 3411</strong>&nbsp; 0.8091<br><br>Narrated Abu Musa: Allah's Apostle said, "Many amongst men reached (the level of) perfection but none amongst the women reached this level except Asia</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>bukhari 5325, 5326</strong>&nbsp; 5.2910 <small>· Sahih</small><br><br>Urwa said to Aisha, "Do you know so-and-so, the daughter of Al-Hakam? Her husband divorced her irrevocably and she left (her husband's house)." `Aisha</td>
<td valign="top"><strong>bukhari 43</strong>&nbsp; 0.8417<br><br>Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her</td>
<td valign="top"><strong>bukhari 902</strong>&nbsp; 0.8474<br><br>Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of f</td>
<td valign="top"><strong>bukhari 2026</strong>&nbsp; 0.8670<br><br>Narrated `Aisha: (the wife of the Prophet) The Prophet used to practice I`tikaf in the last ten days of Ramadan till he died and then his wives used t</td>
<td valign="top"><strong>bukhari 3768</strong>&nbsp; 0.8094<br><br>Narrated Abu Salama: `Aisha said, "Once Allah's Apostle said (to me), 'O Aish (`Aisha)! This is Gabriel greeting you.' I said, 'Peace and Allah's Merc</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8103<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
<td valign="top"><strong>bukhari 4691</strong>&nbsp; 0.8034<br><br>Narrated Um Ruman: Who was `Aisha's mother: While I was with `Aisha, `Aisha got fever, whereupon the Prophet said, "Probably her fever is caused by th</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>abudawud 1280</strong>&nbsp; 5.2892 <small>· Da'if</small><br><br>Dhakwan, the client of Aisha, reported on the authority of Aisha: The Messenger of Allah (saws) used to pray after the afternoon prayer but prohibited</td>
<td valign="top"><strong>abudawud 288</strong>&nbsp; 0.8400 <small>· Sahih</small><br><br>'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, </td>
<td valign="top"><strong>bukhari 4750</strong>&nbsp; 0.8463<br><br>Narrated Aisha: (The wife of the Prophet) Whenever Allah's Apostle intended to go on a journey, he used to draw lots among his wives and would take wi</td>
<td valign="top"><strong>bukhari 3894</strong>&nbsp; 0.8662<br><br>Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then </td>
<td valign="top"><strong>bukhari 3771</strong>&nbsp; 0.8082<br><br>Narrated Al-Qasim bin Muhammad: Once `Aisha became sick and Ibn `Abbas went to see her and said, "O mother of the believers! You are leaving for truth</td>
<td valign="top"><strong>bukhari 4691</strong>&nbsp; 0.8096<br><br>Narrated Um Ruman: Who was `Aisha's mother: While I was with `Aisha, `Aisha got fever, whereupon the Prophet said, "Probably her fever is caused by th</td>
<td valign="top"><strong>bukhari 5158</strong>&nbsp; 0.7976<br><br>Narrated 'Urwa: The Prophet wrote the (marriage contract) with `Aisha while she was six years old and consummated his marriage with her while she was </td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>ibnmajah 1469</strong>&nbsp; 5.2892 <small>· Sahih</small><br><br>“They used to claim that he was shrouded in Hibarah.” ‘Aishah said: “They brought a Hibarah Burd, but they did not shroud him in it.”</td>
<td valign="top"><strong>abudawud 3708</strong>&nbsp; 0.8388 <small>· Da'if in chain</small><br><br>Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays, and asked her about mixing dri</td>
<td valign="top"><strong>abudawud 288</strong>&nbsp; 0.8457 <small>· Sahih</small><br><br>'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, </td>
<td valign="top"><strong>bukhari 4442</strong>&nbsp; 0.8661<br><br>Narrated Aisha: (the wife of the Prophet) "When the ailment of Allah's Apostle became aggravated, he requested his wives to permit him to be (treated)</td>
<td valign="top"><strong>bukhari 3388</strong>&nbsp; 0.8052<br><br>Narrated Masruq: I asked Um Ruman, `Aisha's mother about the accusation forged against `Aisha. She said, "While I was sitting with `Aisha, an Ansari w</td>
<td valign="top"><strong>bukhari 251</strong>&nbsp; 0.8078<br><br>Narrated Abu Salama: `Aisha's brother and I went to `Aisha and he asked her about the bath of the Prophet. She brought a pot containing about a Sa` of</td>
<td valign="top"><strong>bukhari 4428</strong>&nbsp; 0.7966<br><br>Narrated `Aisha: The Prophet in his ailment in which he died, used to say, "O `Aisha! I still feel the pain caused by the food I ate at Khaibar, and a</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bukhari 6201</strong>&nbsp; 5.2867 <small>· Sahih</small><br><br>(the wife the Prophet) Allah's Apostle said, "O Aisha! This is Gabriel sending his greetings to you." I said, "Peace, and Allah's Mercy be on him." `A</td>
<td valign="top"><strong>bukhari 5160</strong>&nbsp; 0.8383<br><br>Narrated Aisha: When the Prophet married me, my mother came to me and made me enter the house (of the Prophet) and nothing surprised me but the coming</td>
<td valign="top"><strong>bukhari 43</strong>&nbsp; 0.8455<br><br>Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her</td>
<td valign="top"><strong>bukhari 5995</strong>&nbsp; 0.8656<br><br>Narrated `Aisha: (the wife of the Prophet) A lady along with her two daughters came to me asking me (for some alms), but she found nothing with me exc</td>
<td valign="top"><strong>bukhari 3770</strong>&nbsp; 0.8047<br><br>Narrated Anas bin Malik: Allah's Apostle said, "The superiority of `Aisha over other women is like the superiority of Tharid to other meals."</td>
<td valign="top"><strong>bukhari 6201</strong>&nbsp; 0.8076<br><br>Narrated `Aisha: (the wife the Prophet) Allah's Apostle said, "O Aisha! This is Gabriel sending his greetings to you." I said, "Peace, and Allah's Mer</td>
<td valign="top"><strong>bukhari 3770</strong>&nbsp; 0.7950<br><br>Narrated Anas bin Malik: Allah's Apostle said, "The superiority of `Aisha over other women is like the superiority of Tharid to other meals."</td>
</tr>
</tbody></table>

---

## Query: fasting expiation sins

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 10ms |
| mxbai-large F16 | 53ms | 86ms |
| mxbai-large Q4_K_M | 43ms | 82ms |
| mxbai-large INT8 ONNX | 27ms | 82ms |
| mxbai-xsmall FP32 | 13ms | 79ms |
| mxbai-xsmall INT8 ONNX | 2ms | 82ms |
| mxbai-xsmall INT4 ONNX | 6ms | 80ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="14%"><strong>BM25 Lexical</strong><br><small>no encoding · query_string</small></th>
<th width="14%"><strong>mxbai-large F16</strong><br><small>1024-dim · 335M · Ollama (F16)</small></th>
<th width="14%"><strong>mxbai-large Q4_K_M</strong><br><small>1024-dim · 335M · Ollama GGUF</small></th>
<th width="14%"><strong>mxbai-large INT8 ONNX</strong><br><small>1024-dim · 335M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall FP32</strong><br><small>384-dim · 33M · SentenceTransformers</small></th>
<th width="14%"><strong>mxbai-xsmall INT8 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall INT4 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 19.7723 <small>· Sahih</small><br><br>“Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previous year.”</td>
<td valign="top"><strong>mishkat 1965</strong>&nbsp; 0.8632<br><br>Salman al-Farisi told of God’s messenger saying in a sermon which he delivered to them on the last day of Sha'ban, “A great month, a blessed month, a </td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8598<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8890<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8351<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8310<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8379 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 19.3202 <small>· Sahih</small><br><br>“Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of the year before and the year after.”</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8581<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8581<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>mishkat 1959</strong>&nbsp; 0.8846<br><br>He reported God’s messenger as saying, "Every [good] deed a son of Adam does will be multiplied, a good deed receiving a tenfold to seven hundredfold </td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8257 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8236 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8206 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 19.2294 <small>· Uncategorized</small><br><br>The five daily (prescribed) Salat, and Friday (prayer) to the next Friday (prayer), and the fasting of Ramadan to the next Ramadan, is expiation of th</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8580<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.8575<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8845<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8102 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8092 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8205<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>riyadussalihin 1250</strong>&nbsp; 19.1035 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) was asked about the observance of Saum (fasting) on the day of 'Arafah. He said, "It is an expiation for the sins of the</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.8551<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>bukhari 1904</strong>&nbsp; 0.8551<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah said, 'All the deeds of Adam's sons (people) are for them, except fasting which is for Me, and I wi</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8831<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bulugh 441</strong>&nbsp; 0.7972<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said: "The best of my followers are those who, having done evil, ask for forgiveness (from Allah); and wh</td>
<td valign="top"><strong>ibnmajah 428</strong>&nbsp; 0.7998 <small>· Hasan</small><br><br>It was narrated from Abu Hurairah that: The Prophet said: "Sins are expiated by well-performed ablution despite difficulties, increasing the number of</td>
<td valign="top"><strong>bulugh 441</strong>&nbsp; 0.8094<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said: "The best of my followers are those who, having done evil, ask for forgiveness (from Allah); and wh</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>riyadussalihin 1252</strong>&nbsp; 18.9781 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) was asked about observing As-Saum (the fast) on the tenth day of Muharram, and he replied, "It is an expiation for the s</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8516<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>abudawud 2380</strong>&nbsp; 0.8527 <small>· Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: if one has a sudden attack of vomiting while one is fasting, no atonement is required of him, but if he</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.8830<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.7953<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.7972<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8072 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 18.0183 <small>· Sahih</small><br><br>The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward for it; and the smell wh</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8515<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8527<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8824<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.7944 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7962<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8056<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>muslim 1162 b</strong>&nbsp; 15.3458 <small>· Sahih</small><br><br>Abu Qatada al-Ansari (Allah be pleased with him) reported that the Messenger of Allah (may peace be upon him) was asked about his fasting. The Messeng</td>
<td valign="top"><strong>bukhari 1904</strong>&nbsp; 0.8511<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah said, 'All the deeds of Adam's sons (people) are for them, except fasting which is for Me, and I wi</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8502<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>abudawud 1372</strong>&nbsp; 0.8815 <small>· Sahih</small><br><br>Narrated Abu Hurairah: The Prophet (saws) as saying: If anyone fasts during Ramadan because of faith and in order to seek his reward from Allah, his p</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7891<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.7929<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.8039<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>bulugh 680</strong>&nbsp; 14.3741 <small>· Uncategorized</small><br><br>Abu Qatadah Al-Ansari (RAA) narrated, ‘The Messenger of Allah (P.B.U.H.) was asked about fasting on the day of Arafah (the 9th of the month of Dhul Hi</td>
<td valign="top"><strong>abudawud 2380</strong>&nbsp; 0.8487 <small>· Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: if one has a sudden attack of vomiting while one is fasting, no atonement is required of him, but if he</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.8495<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8782<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>ibnmajah 428</strong>&nbsp; 0.7885 <small>· Hasan</small><br><br>It was narrated from Abu Hurairah that: The Prophet said: "Sins are expiated by well-performed ablution despite difficulties, increasing the number of</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.7905 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.7954<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>tirmidhi 3549</strong>&nbsp; 14.0407 <small>· Uncategorized</small><br><br>“Ishaq bin Mansur narrated to us, from Isra’il” with this (Another chain) Bilal narrated that the Messenger of Allah (saws) said: “Hold fast to Qiyam </td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8476<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>abudawud 1372</strong>&nbsp; 0.8493 <small>· Sahih</small><br><br>Narrated Abu Hurairah: The Prophet (saws) as saying: If anyone fasts during Ramadan because of faith and in order to seek his reward from Allah, his p</td>
<td valign="top"><strong>bukhari 1904</strong>&nbsp; 0.8780<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah said, 'All the deeds of Adam's sons (people) are for them, except fasting which is for Me, and I wi</td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.7846<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.7871<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
<td valign="top"><strong>abudawud 2316</strong>&nbsp; 0.7950 <small>· Hasan</small><br><br>Ibn ‘Abbas explain the Qur’anic verse “For those who can do it(with hardship) is a ransom, the feeding of one, that is indigent” said “If one of them </td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bukhari 415</strong>&nbsp; 13.7088 <small>· Sahih</small><br><br>The Prophet said, "Spitting in the mosque is a sin and its expiation is to bury it."</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.8456<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8491<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bukhari 7492</strong>&nbsp; 0.8773<br><br>Narrated Abu Huraira: The Prophet said, "Allah said: The Fast is for Me and I will give the reward for it, as he (the one who observes the fast) leave</td>
<td valign="top"><strong>abudawud 2316</strong>&nbsp; 0.7802 <small>· Hasan</small><br><br>Ibn ‘Abbas explain the Qur’anic verse “For those who can do it(with hardship) is a ransom, the feeding of one, that is indigent” said “If one of them </td>
<td valign="top"><strong>bulugh 441</strong>&nbsp; 0.7860<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said: "The best of my followers are those who, having done evil, ask for forgiveness (from Allah); and wh</td>
<td valign="top"><strong>ibnmajah 1731</strong>&nbsp; 0.7948 <small>· Da’if</small><br><br>It was narrated that Qatadah bin Nu’man said: “I heard the Messenger of Allah (saw) say: ‘Whoever fasts the Day of ‘Arafah, his sins of the previous a</td>
</tr>
</tbody></table>

---

## Query: neighbor rights

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 9ms |
| mxbai-large F16 | 47ms | 81ms |
| mxbai-large Q4_K_M | 47ms | 83ms |
| mxbai-large INT8 ONNX | 16ms | 83ms |
| mxbai-xsmall FP32 | 10ms | 79ms |
| mxbai-xsmall INT8 ONNX | 2ms | 81ms |
| mxbai-xsmall INT4 ONNX | 5ms | 81ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="14%"><strong>BM25 Lexical</strong><br><small>no encoding · query_string</small></th>
<th width="14%"><strong>mxbai-large F16</strong><br><small>1024-dim · 335M · Ollama (F16)</small></th>
<th width="14%"><strong>mxbai-large Q4_K_M</strong><br><small>1024-dim · 335M · Ollama GGUF</small></th>
<th width="14%"><strong>mxbai-large INT8 ONNX</strong><br><small>1024-dim · 335M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall FP32</strong><br><small>384-dim · 33M · SentenceTransformers</small></th>
<th width="14%"><strong>mxbai-xsmall INT8 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
<th width="14%"><strong>mxbai-xsmall INT4 ONNX</strong><br><small>384-dim · 33M · ONNX Runtime</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 14.2937 <small>· Da'if</small><br><br>“The neighbor has more right to preemption of his neighbor, so let him wait for him even if he is absent, if they share a path.”</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8379 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8334 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8715 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8567<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8545<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8483<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 13.8410 <small>· Sahih</small><br><br>“I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has neighbors?' He said: 'The neighbor has more rig</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8378 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8324 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8672 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8378<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8401<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8253<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 13.8410 <small>· Sahih</small><br><br>"O Messenger of Allah, not one else has any share in my land, but there are neighbors." He said: "The neighbor has more right to property that is near</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8326<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8259<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8657 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8102 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8046 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8013 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>nasai 4705</strong>&nbsp; 13.7818 <small>· Sahih</small><br><br>"The Messenger of Allah decreed the principle of pre-emption, and the (rights of) neighbors."</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8289 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8217 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8577<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8008 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.7942 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.7992 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 13.6682 <small>· Hasan</small><br><br>that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>abudawud 3517</strong>&nbsp; 0.8224 <small>· Sahih</small><br><br>Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or land of the neighbour.</td>
<td valign="top"><strong>abudawud 3517</strong>&nbsp; 0.8197 <small>· Sahih</small><br><br>Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or land of the neighbour.</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8558 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7942 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7865<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7879 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 13.5564 <small>· Uncategorized</small><br><br>"The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8212<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8139<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8552<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7901 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7849 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7874 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 13.5564 <small>· Sahih</small><br><br>“The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>abudawud 3513</strong>&nbsp; 0.8180 <small>· Sahih</small><br><br>Narrated Jabir: The Messenger of Allah (saws) as saying: There is the right of option regarding everything which is shared, whether a dwelling or a ga</td>
<td valign="top"><strong>abudawud 3513</strong>&nbsp; 0.8130 <small>· Sahih</small><br><br>Narrated Jabir: The Messenger of Allah (saws) as saying: There is the right of option regarding everything which is shared, whether a dwelling or a ga</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8502 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7831 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7821 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7801 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>bukhari 6981</strong>&nbsp; 13.2157 <small>· Sahih</small><br><br>Abu Rafi` sold a house to Sa`d bin Malik for four-hundred Mithqal of gold, and said, "If I had not heard the Prophet saying, 'The neighbor has more ri</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8174 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8123 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>adab 109</strong>&nbsp; 0.8475 <small>· Hasan</small><br><br>Al-Hasan was asked about the neighbour and said, "The term 'neighbour' includes the forty houses in front a person, the forty houses behind him, the f</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7828 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7803 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7787<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 6978</strong>&nbsp; 13.0867 <small>· Sahih</small><br><br>Abu Rafi' said that Sa'd offered him four hundred Mithqal of gold for a house. Abu Rafi ' said, "If I had not heard Allah's Apostle saying, 'A neighbo</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8159 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>adab 109</strong>&nbsp; 0.8114 <small>· Hasan</small><br><br>Al-Hasan was asked about the neighbour and said, "The term 'neighbour' includes the forty houses in front a person, the forty houses behind him, the f</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.8453 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7792<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7767 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7624 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 12.8224 <small>· Hasan</small><br><br>that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, when their paths</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8156<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>bukhari 6976</strong>&nbsp; 0.8105<br><br>Narrated Jabir bin `Abdullah: The Prophet has decreed that preemption is valid in all cases where the real estate concerned has not been divided, but </td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8405<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7718 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7698 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>abudawud 3518</strong>&nbsp; 0.7496 <small>· Sahih</small><br><br>Narrated Jabir ibn Abdullah: The Prophet (saws) said: The neighbour is most entitled to the right of pre-emption, and he should wait for its exercise </td>
</tr>
</tbody></table>

---

*Generated by `tests/quant_ladder_report.py` · pool=50 · N=10*
