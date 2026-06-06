# Small Model Comparison

## Contents

**hadithText**
- [good character and manners](#hadithtext-good-character-and-manners)
- [angels recording deeds](#hadithtext-angels-recording-deeds)
- [prayer at night](#hadithtext-prayer-at-night)
- [forgiving someone who wronged you](#hadithtext-forgiving-someone-who-wronged-you)
- [comparing yourself to others](#hadithtext-comparing-yourself-to-others)
- [aisha](#hadithtext-aisha)
- [fasting expiation sins](#hadithtext-fasting-expiation-sins)
- [neighbor rights](#hadithtext-neighbor-rights)

**englishMatn**
- [good character and manners](#englishmatn-good-character-and-manners)
- [angels recording deeds](#englishmatn-angels-recording-deeds)
- [prayer at night](#englishmatn-prayer-at-night)
- [forgiving someone who wronged you](#englishmatn-forgiving-someone-who-wronged-you)
- [comparing yourself to others](#englishmatn-comparing-yourself-to-others)
- [aisha](#englishmatn-aisha)
- [fasting expiation sins](#englishmatn-fasting-expiation-sins)
- [neighbor rights](#englishmatn-neighbor-rights)

**HF Serverless API**
- [good character and manners](#hf-serverless-api-good-character-and-manners)
- [angels recording deeds](#hf-serverless-api-angels-recording-deeds)
- [prayer at night](#hf-serverless-api-prayer-at-night)
- [forgiving someone who wronged you](#hf-serverless-api-forgiving-someone-who-wronged-you)
- [comparing yourself to others](#hf-serverless-api-comparing-yourself-to-others)
- [aisha](#hf-serverless-api-aisha)
- [fasting expiation sins](#hf-serverless-api-fasting-expiation-sins)
- [neighbor rights](#hf-serverless-api-neighbor-rights)

---

## Latency Summary

All times are post-warmup averages across 8 queries. Models run in model-major order so
each Ollama model stays resident in Ollama's single-model cache for its entire batch —
no inter-query eviction, matching single-model production latency.

| Model | Dims | Backend | Avg Embed | Avg Search | Avg Total |
|---|---|---|---|---|---|
| BM25 Lexical | — | ES query_string | — | 12ms | 12ms |
| mxbai-embed-large | 1024-dim | Ollama | 43ms | 86ms | 129ms |
| nomic-embed-text | 768-dim | Ollama | 33ms | 84ms | 117ms |
| snowflake-arctic-embed:m | 768-dim | Ollama | 49ms | 87ms | 136ms |
| all-MiniLM-L6-v2 | 384-dim | Ollama | 34ms | 86ms | 120ms |
| embeddinggemma-300m | 768-dim | SentenceTransformers | 67ms | 81ms | 148ms |
| embeddinggemma-300m-qat-q8 | 768-dim | SentenceTransformers | 68ms | 84ms | 152ms |
| embeddinggemma-300m-qat-q4 | 768-dim | SentenceTransformers | 76ms | 81ms | 157ms |
| mxbai-embed-xsmall-v1 | 384-dim | SentenceTransformers | 12ms | 80ms | 92ms |
| mxbai-embed-large (Q4_K_M) | 1024-dim | Ollama | 45ms | 86ms | 131ms |
| mxbai-embed-large (INT8 ONNX) | 1024-dim | ONNX Runtime | 30ms | 82ms | 112ms |
| mxbai-embed-xsmall (INT8 ONNX) | 384-dim | ONNX Runtime | 2ms | 81ms | 83ms |
| mxbai-embed-xsmall (INT4 ONNX) | 384-dim | ONNX Runtime | 5ms | 81ms | 86ms |
| mxbai-embed-large (HF API) | 1024-dim | HF Serverless | 219ms | 98ms | 317ms |
| snowflake-arctic-embed:m (HF API) | 768-dim | HF Serverless | 725ms | 96ms | 821ms |
| all-MiniLM-L6-v2 (HF API) | 384-dim | HF Serverless | 182ms | 96ms | 278ms |

---

# Small Model Comparison — hadithText

Input: raw `hadithText` (isnad + matn). Identical to production semantic search.

**Filters & boosts**

| Setting | Status |
|---|---|
| `isChainRef` exclusion | **ON** — chain-reference hadiths excluded from results |
| Dedup by `dupGroup` | **ON** — highest collection-boosted member wins per group |
| Collection boosts | **ON** — bukhari 5×, muslim 4.8×, nawawi40 3.3×, malik/ahmad/riyadussalihin 2.5×, nasai 3.5×, abudawud 3×, tirmidhi 2.5×, ibnmajah/darimi/mishkat 2× |
| Embed times | Post-warmup — models loaded into memory before measurement |

| # | Model | Vec field | Dims | Size | Backend |
|---|---|---|---|---|---|
| 1 | mxbai-embed-large | `vec_mxbai` | 1024-dim | 335M | Ollama |
| 2 | nomic-embed-text | `vec_nomic` | 768-dim | 137M | Ollama |
| 3 | snowflake-arctic-embed:m | `vec_snowflake` | 768-dim | 110M | Ollama |
| 4 | all-MiniLM-L6-v2 | `vec_miniLM` | 384-dim | 22M | Ollama |
| 5 | embeddinggemma-300m | `vec_gemma` | 768-dim | 300M | sentence_transformers |
| 6 | embeddinggemma-300m-qat-q8 | `vec_gemma_q8` | 768-dim | 300M | sentence_transformers |
| 7 | embeddinggemma-300m-qat-q4 | `vec_gemma_q4` | 768-dim | 300M | sentence_transformers |
| 8 | mxbai-embed-xsmall-v1 | `vec_mxbai_xs` | 384-dim | 33M | sentence_transformers |
| 9 | mxbai-embed-large (Q4_K_M) | `vec_mxbai_q4km` | 1024-dim | 335M | Ollama |
| 10 | mxbai-embed-large (INT8 ONNX) | `vec_mxbai_q` | 1024-dim | 335M | ONNX Runtime |
| 11 | mxbai-embed-xsmall (INT8 ONNX) | `vec_mxbai_xs_q8` | 384-dim | 33M | ONNX Runtime |
| 12 | mxbai-embed-xsmall (INT4 ONNX) | `vec_mxbai_xs_q4` | 384-dim | 33M | ONNX Runtime |

---

## hadithText: good character and manners

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 15ms |
| mxbai-embed-large | 32ms | 103ms |
| nomic-embed-text | 26ms | 101ms |
| snowflake-arctic-embed:m | 49ms | 111ms |
| all-MiniLM-L6-v2 | 32ms | 108ms |
| embeddinggemma-300m | 64ms | 81ms |
| embeddinggemma-300m-qat-q8 | 76ms | 90ms |
| embeddinggemma-300m-qat-q4 | 71ms | 80ms |
| mxbai-embed-xsmall-v1 | 12ms | 79ms |
| mxbai-embed-large (Q4_K_M) | 30ms | 105ms |
| mxbai-embed-large (INT8 ONNX) | 23ms | 85ms |
| mxbai-embed-xsmall (INT8 ONNX) | 2ms | 81ms |
| mxbai-embed-xsmall (INT4 ONNX) | 7ms | 83ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M)</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX)</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX)</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX)</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 18.0449 <small>· Sahih</small><br><br>We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafahhish, and he use</td>
<td valign="top"><strong>forty 22</strong>&nbsp; 0.8371<br><br>A man who knows his worth will not be ruined.</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.8408<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8836<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7577 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8250<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8220<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8266<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7668 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.8320<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8546 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7562 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7687 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>adab 290</strong>&nbsp; 15.1631 <small>· Da'if</small><br><br>Abu'd-Darda' stood up in the night to pray. He was weeping and said, 'O Allah! You made my physical form good, so make my character good!' until morni</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8333<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8255 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>tirmidhi 2780b</strong>&nbsp; 0.8412<br><br>Another chain with a similar narration</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7322<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>ibnmajah 4218</strong>&nbsp; 0.7894 <small>· Da’if</small><br><br>It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “There is no wisdom like reflection, and no honor like good manners.”</td>
<td valign="top"><strong>ibnmajah 4218</strong>&nbsp; 0.7858 <small>· Da’if</small><br><br>It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “There is no wisdom like reflection, and no honor like good manners.”</td>
<td valign="top"><strong>ibnmajah 4218</strong>&nbsp; 0.7972 <small>· Da’if</small><br><br>It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “There is no wisdom like reflection, and no honor like good manners.”</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7666 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>forty 22</strong>&nbsp; 0.8304<br><br>A man who knows his worth will not be ruined.</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8521<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7509 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7547 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 14.9349 <small>· Hasan</small><br><br>"Nothing is placed on the Scale that is heavier than good character. Indeed the person with good character will have attained the rank of the person o</td>
<td valign="top"><strong>shamail 350</strong>&nbsp; 0.8324 <small>· Da'if Isnād</small><br><br>Al-Hasan ibn 'Ali said: “Al-Husain said: ‘I asked my father how the Prophet (Allah bless him and give him peace) comported himself among his table com</td>
<td valign="top"><strong>tirmidhi 1962</strong>&nbsp; 0.8191 <small>· Da'if</small><br><br>Abu Sa'eed Al-Khudri narrated that the Messenger of Allah said: "Two traits are not combined in a believer: Stinginess and bad manners."</td>
<td valign="top"><strong>forty 33</strong>&nbsp; 0.8346<br><br>Actions are through intentions.</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7206 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.7794 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.7699 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7920 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.7414<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8302<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8508<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>shamail 349</strong>&nbsp; 0.7434 <small>· Sahih</small><br><br>'Aisha said (may Allah be well pleased with her): "A man sought permission to come in to see Allah’s Messenger (Allah bless him and give him peace) wh</td>
<td valign="top"><strong>shamail 349</strong>&nbsp; 0.7393 <small>· Sahih</small><br><br>'Aisha said (may Allah be well pleased with her): "A man sought permission to come in to see Allah’s Messenger (Allah bless him and give him peace) wh</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bukhari 6029</strong>&nbsp; 14.7588 <small>· Sahih</small><br><br>Abdullah bin 'Amr mentioned Allah's Apostle saying that he was neither a Fahish nor a Mutafahish. Abdullah bin 'Amr added, Allah's Apostle said, 'The </td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.8322<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>bukhari 3762</strong>&nbsp; 0.8177<br><br>Narrated `Abdur-Rahman bin Yazid: We asked Hudhaifa to tell us of a person resembling (to some extent) the Prophet in good appearance and straight for</td>
<td valign="top"><strong>forty 35</strong>&nbsp; 0.8323<br><br>The best of affairs is that which is balanced.</td>
<td valign="top"><strong>adab 272</strong>&nbsp; 0.7198 <small>· Sahih</small><br><br>'Amr ibn Shu'ayb reported from his grandfather that the Prophet, may Allah bless him and grant him peace, said, "Shall I tell you about who is most be</td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.7684<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7664 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.7894 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7381<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8282 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8499 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.7406<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7355<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 14.6536 <small>· Sahih</small><br><br>The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those who have the best manners and c</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8275 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8138<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>forty 21</strong>&nbsp; 0.8314<br><br>A man will be with whom he loves.</td>
<td valign="top"><strong>adab 271</strong>&nbsp; 0.7157 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr said, "The Prophet, may Allah bless him and grant him peace, was neither coarse nor loud. He used to say, "The best of you is the o</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.7647 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.7636<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.7794<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>shamail 349</strong>&nbsp; 0.7376 <small>· Sahih</small><br><br>'Aisha said (may Allah be well pleased with her): "A man sought permission to come in to see Allah’s Messenger (Allah bless him and give him peace) wh</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8251 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>adab 271</strong>&nbsp; 0.8464 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr said, "The Prophet, may Allah bless him and grant him peace, was neither coarse nor loud. He used to say, "The best of you is the o</td>
<td valign="top"><strong>bukhari 28</strong>&nbsp; 0.7295<br><br>Narrated 'Abdullah bin 'Amr: A person asked Allah's Apostle . "What (sort of) deeds in or (what qualities of) Islam are good?" He replied, "To feed (t</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7350 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>bukhari 3759, 3760</strong>&nbsp; 14.2273 <small>· Sahih</small><br><br>Allah's Apostle neither talked in an insulting manner nor did he ever speak evil intentionally. He used to say, "The most beloved to me amongst you is</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8242 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8117 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>forty 13</strong>&nbsp; 0.8285<br><br>A little that suffices is better than an abundance that distracts.</td>
<td valign="top"><strong>riyadussalihin 341</strong>&nbsp; 0.7148<br><br>'Abdullah bin 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said, "The finest act of goodness is that a person should treat kind</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.7643 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.7528 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.7682<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>bukhari 28</strong>&nbsp; 0.7361<br><br>Narrated 'Abdullah bin 'Amr: A person asked Allah's Apostle . "What (sort of) deeds in or (what qualities of) Islam are good?" He replied, "To feed (t</td>
<td valign="top"><strong>forty 5</strong>&nbsp; 0.8236<br><br>The person guiding (someone) to do a good deed, is like the one performing the good deed.</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.8442 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7284<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
<td valign="top"><strong>bukhari 28</strong>&nbsp; 0.7338<br><br>Narrated 'Abdullah bin 'Amr: A person asked Allah's Apostle . "What (sort of) deeds in or (what qualities of) Islam are good?" He replied, "To feed (t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>mishkat 5770</strong>&nbsp; 13.8450 <small>· Uncategorized</small><br><br>God has sent me to perfect good qualities of character and to complete good deeds." It is transmitted in Sharh as-sunna .</td>
<td valign="top"><strong>shamail 8</strong>&nbsp; 0.8231 <small>· Da'if Isnād</small><br><br>Al-Hasan ibn 'Ali (may Allah be well pleased with him and his father) said: “My maternal aunt Hind asked the son of Abu Hala, who was a describer of t</td>
<td valign="top"><strong>mishkat 5770</strong>&nbsp; 0.8111<br><br>Jabir reported the Prophet as saying, "God has sent me to perfect good qualities of character and to complete good deeds." It is transmitted in Sharh </td>
<td valign="top"><strong>tirmidhi 226</strong>&nbsp; 0.8253<br><br>Narrator not mentioned: A Similar narration</td>
<td valign="top"><strong>muslim 48 b</strong>&nbsp; 0.7115<br><br>Abd Shuraib al-Adawi reported: My eare listened and my eye saw when Allah's Messenger (may peace be upon him) spoke and said: He who believes In Allah</td>
<td valign="top"><strong>ibnmajah 4188</strong>&nbsp; 0.7630 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Abbas that the Prophet (saw) said to Ashajj ‘Ansari: “You have two characteristics that Allah likes: Forbearance and modesty</td>
<td valign="top"><strong>ibnmajah 4188</strong>&nbsp; 0.7525 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Abbas that the Prophet (saw) said to Ashajj ‘Ansari: “You have two characteristics that Allah likes: Forbearance and modesty</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.7681 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7350<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.8210<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.8440<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7240 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>bukhari 6236</strong>&nbsp; 0.7313<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet, "What Islamic traits are the best?" The Prophet said, "Feed the people, and greet those whom you</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>adab 270</strong>&nbsp; 13.2727 <small>· Uncategorized</small><br><br>Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.8223<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>abudawud 2815</strong>&nbsp; 0.8108 <small>· Sahih</small><br><br>Narrated Shaddad b. Aws: There are two characteristics that I heard the Messenger of Allah (saws) say: Allah has decreed that everything should be don</td>
<td valign="top"><strong>tirmidhi 2783b</strong>&nbsp; 0.8245<br><br>(Another chain) with a similar narration</td>
<td valign="top"><strong>adab 244</strong>&nbsp; 0.7094 <small>· Sahih</small><br><br>'Abdullah ibn az-Zubayr said on the minbar, "Make allowances for people and command what is right and turn away from the ignorant." (7:199) He said, "</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.7616<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.7522 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>tirmidhi 2494</strong>&nbsp; 0.7676 <small>· Da'if</small><br><br>Abu Bakr bin Al-Munkadir narrated from Jabir that the Messenger of Allah (s.a.w) said: "There are three (characteristics) for which whomever has them,</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7319 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8201<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>forty 30</strong>&nbsp; 0.8435<br><br>If the nobleman of a people comes to you, honour him.</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7232<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>abudawud 5143</strong>&nbsp; 0.7308 <small>· Sahih</small><br><br>Ibn ‘Umar reported the Messenger of Allah (May peace be upon him) as saying: One of the finest acts of kindness is for a man to treat his father’s fri</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 13.2451 <small>· Sahih</small><br><br>"It is a smiling face, doing one's best in good, and refraining from harm."</td>
<td valign="top"><strong>shamail 224</strong>&nbsp; 0.8214 <small>· Da'if Isnād</small><br><br>Al-Hasan ibn 'Ali said (may Allah the Exalted be well pleased with him and his father): “I said to my maternal uncle, Hind ibn Abi Hala, who was skill</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.8043<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>adab 585</strong>&nbsp; 0.8243<br><br>(As hadith above)</td>
<td valign="top"><strong>adab 464</strong>&nbsp; 0.7086 <small>· Sahih</small><br><br>Abu'd-Darda' reported that the Prophet, may Allah bless him and grant him peace, said, "Whoever has been given his portion of compassion has been give</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.7559 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>tirmidhi 2494</strong>&nbsp; 0.7497 <small>· Da'if</small><br><br>Abu Bakr bin Al-Munkadir narrated from Jabir that the Messenger of Allah (s.a.w) said: "There are three (characteristics) for which whomever has them,</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.7666 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>bukhari 6236</strong>&nbsp; 0.7301<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet, "What Islamic traits are the best?" The Prophet said, "Feed the people, and greet those whom you</td>
<td valign="top"><strong>hisn 231</strong>&nbsp; 0.8177<br><br>If any of you praises his companion then let him say: Aḥsibu fulānan wallāhu ḥasībuh wa lā uzakkī `alallāhi aḥada. If any of you praises his companion</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.8399<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>abudawud 5143</strong>&nbsp; 0.7168 <small>· Sahih</small><br><br>Ibn ‘Umar reported the Messenger of Allah (May peace be upon him) as saying: One of the finest acts of kindness is for a man to treat his father’s fri</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.7302<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>adab 273</strong>&nbsp; 12.7513 <small>· Sahih</small><br><br>I was sent to perfect good character."</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.8207 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
<td valign="top"><strong>forty 5</strong>&nbsp; 0.8028<br><br>The person guiding (someone) to do a good deed, is like the one performing the good deed.</td>
<td valign="top"><strong>adab 586</strong>&nbsp; 0.8243<br><br>(As hadith above)</td>
<td valign="top"><strong>muslim 2552 b</strong>&nbsp; 0.7064<br><br>'Abdullah b. Umar reported Allah's Apostle (may peace be upon him) as saying: The finest act of goodness is that a person should treat kindly the love</td>
<td valign="top"><strong>forty 22</strong>&nbsp; 0.7528<br><br>A man who knows his worth will not be ruined.</td>
<td valign="top"><strong>forty 22</strong>&nbsp; 0.7493<br><br>A man who knows his worth will not be ruined.</td>
<td valign="top"><strong>tirmidhi 1952</strong>&nbsp; 0.7647 <small>· Da'if</small><br><br>Ayyub bin Musa narrated from his father, from his grandfather, that the Messenger of Allah said : "There is no gift that a father gives his son more v</td>
<td valign="top"><strong>riyadussalihin 341</strong>&nbsp; 0.7283<br><br>'Abdullah bin 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said, "The finest act of goodness is that a person should treat kind</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8161<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>bukhari 6029</strong>&nbsp; 0.8396<br><br>Narrated Masruq: Abdullah bin 'Amr mentioned Allah's Apostle saying that he was neither a Fahish nor a Mutafahish. Abdullah bin 'Amr added, Allah's Ap</td>
<td valign="top"><strong>bukhari 6236</strong>&nbsp; 0.7157<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet, "What Islamic traits are the best?" The Prophet said, "Feed the people, and greet those whom you</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7300<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
</tr>
</tbody></table>

---

## hadithText: angels recording deeds

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 12ms |
| mxbai-embed-large | 42ms | 82ms |
| nomic-embed-text | 19ms | 81ms |
| snowflake-arctic-embed:m | 40ms | 81ms |
| all-MiniLM-L6-v2 | 34ms | 85ms |
| embeddinggemma-300m | 58ms | 82ms |
| embeddinggemma-300m-qat-q8 | 59ms | 82ms |
| embeddinggemma-300m-qat-q4 | 63ms | 83ms |
| mxbai-embed-xsmall-v1 | 14ms | 79ms |
| mxbai-embed-large (Q4_K_M) | 46ms | 84ms |
| mxbai-embed-large (INT8 ONNX) | 25ms | 83ms |
| mxbai-embed-xsmall (INT8 ONNX) | 2ms | 80ms |
| mxbai-embed-xsmall (INT4 ONNX) | 7ms | 81ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M)</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX)</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX)</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX)</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 17.2169 <small>· Sahih</small><br><br>The Great and the Glorious Lord said (to angels): Whenever My servant intends to commit an evil, do not record it against him, but if he actually comm</td>
<td valign="top"><strong>muslim 2689</strong>&nbsp; 0.8306<br><br>Abu Huraira reported Allah's Apostle (may peace be upon him) as saying Allah has mobile (squads) of angels, who have no other work (to attend to but) </td>
<td valign="top"><strong>mishkat 2112</strong>&nbsp; 0.8232<br><br>‘Ā’isha reported God’s messenger as saying, “One who is skilled in the Qur’ān is associated with the noble, upright recording angels; and he who falte</td>
<td valign="top"><strong>forty 2</strong>&nbsp; 0.7942<br><br>War is deception.</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7628<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7890<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7847<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7883<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7944<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>bukhari 7429</strong>&nbsp; 0.8279<br><br>Narrated Abu Huraira: Allah's Apostle said, "(A group of) angels stay with you at night and (another group of) angels by daytime, and both groups gath</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8528 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.7956<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7993<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>mishkat 2112</strong>&nbsp; 16.6777 <small>· Uncategorized</small><br><br>One who is skilled in the Qur’ān is associated with the noble, upright recording angels; and he who falters when reciting the Qur’ān and finds it diff</td>
<td valign="top"><strong>bukhari 7429</strong>&nbsp; 0.8243<br><br>Narrated Abu Huraira: Allah's Apostle said, "(A group of) angels stay with you at night and (another group of) angels by daytime, and both groups gath</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8226<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>forty 10</strong>&nbsp; 0.7872<br><br>The word of the believer is like seizing of the hand.</td>
<td valign="top"><strong>muslim 1560 a</strong>&nbsp; 0.7481<br><br>Hudhaifa reported Allah's Messenger (may peace be upon him) as saying The angels took away the soul of a person who had lived among people who were be</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7429<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7415<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7476<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.7868<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>mishkat 463</strong>&nbsp; 0.8258<br><br>‘Ali reported God’s messenger as saying, “The angels do not enter a house in which there is a picture, a dog, or one who is defiled.” Abu Dawud and Na</td>
<td valign="top"><strong>bukhari 6491</strong>&nbsp; 0.8506<br><br>Narrated Ibn `Abbas: The Prophet narrating about his Lord I'm and said, "Allah ordered (the appointed angels over you) that the good and the bad deeds</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7953<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>mishkat 44</strong>&nbsp; 0.7824 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh ", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “When one of you makes a good profession of Islam, every good deed he does will be recorded for him te</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>abudawud 1454</strong>&nbsp; 16.6777 <small>· Sahih</small><br><br>One who is skilled in the Qur'an is associated with the noble, upright recording angels, and he who falters when he recites the Qur'an and finds it di</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8206<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.8182<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>bulugh 164</strong>&nbsp; 0.7849<br><br>ash-Shafi'i views the second ruling from</td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7425<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7382<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7365<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7446<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>mishkat 44</strong>&nbsp; 0.7839 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh ", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “When one of you makes a good profession of Islam, every good deed he does will be recorded for him te</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8251<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>ibnmajah 76</strong>&nbsp; 0.8461 <small>· Sahih</small><br><br>'Abdullah bin Mas'ud said: "The Messenger of Allah (SAW), the true and truly inspired one, told us that: 'The creation of one of you is put together i</td>
<td valign="top"><strong>mishkat 44</strong>&nbsp; 0.7874 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh ", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “When one of you makes a good profession of Islam, every good deed he does will be recorded for him te</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7775<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>mishkat 1560</strong>&nbsp; 16.0469 <small>· Uncategorized</small><br><br>When a Muslim is afflicted with some trouble in his body the angel is told to record for him his good deeds which he was accustomed to do. Then if God</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8195 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>ibnmajah 1426</strong>&nbsp; 0.8168 <small>· Sahih</small><br><br>It was narrated from Tamim Dari that the Prophet (saw) said: “The first thing for which a person will be brought to account on the Day of Resurrection</td>
<td valign="top"><strong>bulugh 465</strong>&nbsp; 0.7837<br><br>Ibn Majah reported from 'Abdullah bin Salam</td>
<td valign="top"><strong>bukhari 6408</strong>&nbsp; 0.7420<br><br>Narrated Abu Huraira: Allah 's Apostle said, "Allah has some angels who look for those who celebrate the Praises of Allah on the roads and paths. And </td>
<td valign="top"><strong>muslim 632 a</strong>&nbsp; 0.7279<br><br>Abu Huraira reported: The Messenger of Allah (may peace be upon him) said: Angels take turns among you by night and by day, and they all assemble at t</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.7324<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.7384<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7756<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8233 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.8447<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7862<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>abudawud 1454</strong>&nbsp; 0.7654 <small>· Sahih</small><br><br>'Aishah reported the Prophet (saws) as saying: One who is skilled in the Qur'an is associated with the noble, upright recording angels, and he who fal</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 15.4689 <small>· Uncategorized</small><br><br>God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it, God enters it for him in His record as a comple</td>
<td valign="top"><strong>mishkat 463</strong>&nbsp; 0.8189<br><br>‘Ali reported God’s messenger as saying, “The angels do not enter a house in which there is a picture, a dog, or one who is defiled.” Abu Dawud and Na</td>
<td valign="top"><strong>abudawud 1454</strong>&nbsp; 0.8154 <small>· Sahih</small><br><br>'Aishah reported the Prophet (saws) as saying: One who is skilled in the Qur'an is associated with the noble, upright recording angels, and he who fal</td>
<td valign="top"><strong>forty 17</strong>&nbsp; 0.7832<br><br>Richness lies in the richness of the soul.</td>
<td valign="top"><strong>muslim 2112</strong>&nbsp; 0.7387<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels do not enter the house in which there are portrayals or pictures.</td>
<td valign="top"><strong>forty 33</strong>&nbsp; 0.7257<br><br>Actions are through intentions.</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.7289<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.7290<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>mishkat 2096</strong>&nbsp; 0.7580<br><br>Anas reported God's messenger as saying that when lailat al-qadr comes Gabriel descends with a company of angels who invoke blessings on everyone who </td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.8233<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8437<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7610<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>muslim 128 b</strong>&nbsp; 0.7602<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) observed: Allah, the Great and Glorious, said: When</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>abudawud 5263</strong>&nbsp; 15.3019 <small>· Sahih</small><br><br>The Prophet (saws) said: If anyone kills a gecko with the first blow, such and such number of good deeds will be recorded for him, if he kills it with</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.8189<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>muslim 1560 a</strong>&nbsp; 0.8143<br><br>Hudhaifa reported Allah's Messenger (may peace be upon him) as saying The angels took away the soul of a person who had lived among people who were be</td>
<td valign="top"><strong>bukhari 7126</strong>&nbsp; 0.7829<br><br>Narrated Abu Bakra: [as above]</td>
<td valign="top"><strong>muslim 632 a</strong>&nbsp; 0.7334<br><br>Abu Huraira reported: The Messenger of Allah (may peace be upon him) said: Angels take turns among you by night and by day, and they all assemble at t</td>
<td valign="top"><strong>mishkat 626</strong>&nbsp; 0.7255<br><br>Abu Huraira reported God’s Messenger as saying: Angels take turns among you by night and by day, and they all assemble at the dawn and the afternoon p</td>
<td valign="top"><strong>muslim 632 a</strong>&nbsp; 0.7263<br><br>Abu Huraira reported: The Messenger of Allah (may peace be upon him) said: Angels take turns among you by night and by day, and they all assemble at t</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.7284<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7564<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>mishkat 2594</strong>&nbsp; 0.8219<br><br>‘A’isha reported God’s messenger as saying, “There is no day when God sets free more servants from hell than the day of ‘Arafa. He draws near, then pr</td>
<td valign="top"><strong>bukhari 7429</strong>&nbsp; 0.8430<br><br>Narrated Abu Huraira: Allah's Apostle said, "(A group of) angels stay with you at night and (another group of) angels by daytime, and both groups gath</td>
<td valign="top"><strong>mishkat 2096</strong>&nbsp; 0.7602<br><br>Anas reported God's messenger as saying that when lailat al-qadr comes Gabriel descends with a company of angels who invoke blessings on everyone who </td>
<td valign="top"><strong>mishkat 635</strong>&nbsp; 0.7588<br><br>Concerning God’s words, “The recitation of the dawn is witnessed,” (Al-Qur’an, 17:78). Abu Huraira quoted the Prophet as saying, "The angels of the ni</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>muslim 2644</strong>&nbsp; 14.9987 <small>· Sahih</small><br><br>When the drop of (semen) remains in the womb for forty or forty five nights, the angel comes and says: My Lord, will he be good or evil? And both thes</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.8180<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>mishkat 2172</strong>&nbsp; 0.8137<br><br>Makhūl said, “If anyone recites Āl ‘Imrān on a Friday, the angels will invoke blessings on him till night comes.” Transmitted by Dārimī.</td>
<td valign="top"><strong>tirmidhi 434</strong>&nbsp; 0.7825<br><br>Ibn Umar : has a similar narration</td>
<td valign="top"><strong>muslim 128 b</strong>&nbsp; 0.7326<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) observed: Allah, the Great and Glorious, said: When</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.7255<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.7262<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>muslim 632 a</strong>&nbsp; 0.7261<br><br>Abu Huraira reported: The Messenger of Allah (may peace be upon him) said: Angels take turns among you by night and by day, and they all assemble at t</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.7503<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>ibnmajah 76</strong>&nbsp; 0.8214 <small>· Sahih</small><br><br>'Abdullah bin Mas'ud said: "The Messenger of Allah (SAW), the true and truly inspired one, told us that: 'The creation of one of you is put together i</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8423<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>muslim 128 b</strong>&nbsp; 0.7542<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) observed: Allah, the Great and Glorious, said: When</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7575<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>riyadussalihin 1864</strong>&nbsp; 14.4177 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) said, "He who kills a chameleon at the first blow, such and such number of good deeds will be awarded to him; whoever ki</td>
<td valign="top"><strong>ibnmajah 76</strong>&nbsp; 0.8177 <small>· Sahih</small><br><br>'Abdullah bin Mas'ud said: "The Messenger of Allah (SAW), the true and truly inspired one, told us that: 'The creation of one of you is put together i</td>
<td valign="top"><strong>ibnmajah 851</strong>&nbsp; 0.8122 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “When the reciter says Amin, then say Amin, for the angels say Amin, and if </td>
<td valign="top"><strong>tirmidhi 2780b</strong>&nbsp; 0.7823<br><br>Another chain with a similar narration</td>
<td valign="top"><strong>nasai 705</strong>&nbsp; 0.7290 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet (PBUH) said: "When a man goes out of his house to his Masjid, one foot records a good deed and the </td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7252<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>mishkat 3115</strong>&nbsp; 0.7258<br><br>Ibn ‘Umar reported God’s Messenger as saying, "Avoid being naked, for with you are those who never leave you (the recording angels) except when you ar</td>
<td valign="top"><strong>bukhari 1442</strong>&nbsp; 0.7260<br><br>Narrated Abu Huraira: The Prophet said, "Every day two angels come down from Heaven and one of them says, 'O Allah! Compensate every person who spends</td>
<td valign="top"><strong>bukhari 3223</strong>&nbsp; 0.7483<br><br>Narrated Abu Huraira: The Prophet said, "Angels keep on descending from and ascending to the Heaven in turn, some at night and some by daytime, and al</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.8203<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>riyadussalihin 547</strong>&nbsp; 0.8419<br><br>Abu Hurairah (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Everyday two angels descend and one of them says, 'O Allah! Co</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.7507<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7572<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 14.3222 <small>· Sahih</small><br><br>When it occurs to my bondsman that he should do a good deed but he actually does not do it, record one good to him, but if he puts it into practice, I</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.8175<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>mishkat 877</strong>&nbsp; 0.8110<br><br>Rifa'a b. Raf’i said: We were praying behind the Prophet, and when he raised his head at the end of the rak'a he said, “God listens to him who praises</td>
<td valign="top"><strong>forty 32</strong>&nbsp; 0.7805<br><br>Whoever is killed attempting to save his property is a martyr.</td>
<td valign="top"><strong>abudawud 3098</strong>&nbsp; 0.7290 <small>· Sahih Mauquf</small><br><br>Narrated 'Ali: If a man visits a patient in the evening, seventy thousand angels come along with him seeking forgiveness from Allah for him till the m</td>
<td valign="top"><strong>mishkat 3115</strong>&nbsp; 0.7237<br><br>Ibn ‘Umar reported God’s Messenger as saying, "Avoid being naked, for with you are those who never leave you (the recording angels) except when you ar</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7226<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>bukhari 6408</strong>&nbsp; 0.7231<br><br>Narrated Abu Huraira: Allah 's Apostle said, "Allah has some angels who look for those who celebrate the Praises of Allah on the roads and paths. And </td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.7479<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.8201<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.8415<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>bukhari 3223</strong>&nbsp; 0.7489<br><br>Narrated Abu Huraira: The Prophet said, "Angels keep on descending from and ascending to the Heaven in turn, some at night and some by daytime, and al</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.7555<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>ibnmajah 1426</strong>&nbsp; 14.0222 <small>· Sahih</small><br><br>“The first thing for which a person will be brought to account on the Day of Resurrection will be his prayer. If it is complete, then the voluntary (p</td>
<td valign="top"><strong>muslim 632 a</strong>&nbsp; 0.8170<br><br>Abu Huraira reported: The Messenger of Allah (may peace be upon him) said: Angels take turns among you by night and by day, and they all assemble at t</td>
<td valign="top"><strong>tirmidhi 3378</strong>&nbsp; 0.8095 <small>· Sahih</small><br><br>Al-Agharr Abu Muslim narrated that: He bears witness, from Abu Hurairah and Abu Sa’eed Al-Khudri, that they bear witness, from the Messenger of Allah,</td>
<td valign="top"><strong>riyadussalihin 1643</strong>&nbsp; 0.7796<br><br>A similar narration was narrated on the authority of 'Aishah.</td>
<td valign="top"><strong>ibnmajah 3791</strong>&nbsp; 0.7283 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah and Abu Sa'eed bore witness that the Prophet(SAW) said: "No people sit in a gathering remembering Allah, But the ang</td>
<td valign="top"><strong>mishkat 1860</strong>&nbsp; 0.7230<br><br>He reported him as saying that two angels come down every morning and one says, "O God, give him who spends something in place of it;” the other says,</td>
<td valign="top"><strong>muslim 2112</strong>&nbsp; 0.7206<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels do not enter the house in which there are portrayals or pictures.</td>
<td valign="top"><strong>muslim 2689</strong>&nbsp; 0.7227<br><br>Abu Huraira reported Allah's Apostle (may peace be upon him) as saying Allah has mobile (squads) of angels, who have no other work (to attend to but) </td>
<td valign="top"><strong>mishkat 635</strong>&nbsp; 0.7465<br><br>Concerning God’s words, “The recitation of the dawn is witnessed,” (Al-Qur’an, 17:78). Abu Huraira quoted the Prophet as saying, "The angels of the ni</td>
<td valign="top"><strong>muslim 632 a</strong>&nbsp; 0.8199<br><br>Abu Huraira reported: The Messenger of Allah (may peace be upon him) said: Angels take turns among you by night and by day, and they all assemble at t</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.8405<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>bukhari 3332</strong>&nbsp; 0.7485<br><br>Narrated `Abdullah: Allah's Apostle, the true and truly inspired said, "(as regards your creation), every one of you is collected in the womb of his m</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.7554<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
</tr>
</tbody></table>

---

## hadithText: prayer at night

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 15ms |
| mxbai-embed-large | 47ms | 82ms |
| nomic-embed-text | 26ms | 80ms |
| snowflake-arctic-embed:m | 35ms | 81ms |
| all-MiniLM-L6-v2 | 32ms | 83ms |
| embeddinggemma-300m | 76ms | 79ms |
| embeddinggemma-300m-qat-q8 | 74ms | 84ms |
| embeddinggemma-300m-qat-q4 | 75ms | 79ms |
| mxbai-embed-xsmall-v1 | 11ms | 80ms |
| mxbai-embed-large (Q4_K_M) | 42ms | 83ms |
| mxbai-embed-large (INT8 ONNX) | 42ms | 80ms |
| mxbai-embed-xsmall (INT8 ONNX) | 2ms | 81ms |
| mxbai-embed-xsmall (INT4 ONNX) | 6ms | 79ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M)</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX)</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX)</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX)</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>riyadussalihin 1071</strong>&nbsp; 9.9731 <small>· Uncategorized</small><br><br>I heard the Messenger of Allah (PBUH) saying: "One who performs 'Isha' prayer in congregation, is as if he has performed Salat for half of the night. </td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8847<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8884<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>bulugh 270</strong>&nbsp; 0.8434<br><br>And in another narration of Muslim: "he used to say that in the night prayer..."</td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8666<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
<td valign="top"><strong>ibnmajah 1360</strong>&nbsp; 0.7983 <small>· Sahih</small><br><br>It was narrated from ‘Aishah that the Prophet (saw) used to pray nine Rak’ah at night.</td>
<td valign="top"><strong>ibnmajah 1359</strong>&nbsp; 0.8040 <small>· Sahih</small><br><br>It was narrated that ‘Aishah said: “The Prophet (saw) used to pray thirteen Rak’ah at night.”</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8020<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8607<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8834<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8939<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8592<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8670<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 9.9572 <small>· Sahih</small><br><br>Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of the night.</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8796 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>mishkat 1296</strong>&nbsp; 0.8845<br><br>Abu Huraira said that God’s Messenger used to commend prayer at night in Ramadan, but did not command it as a duty. He would say, “If anyone prays dur</td>
<td valign="top"><strong>bulugh 222</strong>&nbsp; 0.8392<br><br>Muslim added: "during Salat (prayer)".</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8446 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>ibnmajah 1359</strong>&nbsp; 0.7975 <small>· Sahih</small><br><br>It was narrated that ‘Aishah said: “The Prophet (saw) used to pray thirteen Rak’ah at night.”</td>
<td valign="top"><strong>ibnmajah 898</strong>&nbsp; 0.8024 <small>· Da’if</small><br><br>It was narrated that Ibn ‘Abbas said: “When praying at night (Qiyamul-Lail), the Messenger of Allah (saw) used to say between the two prostrations: ‘R</td>
<td valign="top"><strong>ibnmajah 1360</strong>&nbsp; 0.7980 <small>· Sahih</small><br><br>It was narrated from ‘Aishah that the Prophet (saw) used to pray nine Rak’ah at night.</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8505 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8808<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8930<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8536 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8554 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>ibnmajah 1327</strong>&nbsp; 9.9569 <small>· Sahih</small><br><br>“We fasted Ramadan with the Messenger of Allah (saw) and he did not lead us in praying Qiyam (prayers at night) during any part of it, until there wer</td>
<td valign="top"><strong>muslim 740</strong>&nbsp; 0.8763<br><br>'A'isha observed that the Messenger of Allah (may peace be upon him) used to observe prayer in the night and the last of his (night) prayer was Witr.</td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8832<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>bulugh 353</strong>&nbsp; 0.8380<br><br>Muslim has: 'He never prayed after the break of dawn except two light Rak'at.'</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8418<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>nasai 1671</strong>&nbsp; 0.7940 <small>· Sahih</small><br><br>It was narrated from Ibn Umar that: The Prophet (SAW) said: "prayers at night are (offered) two by two, then if you fear that dawn will come, pray wit</td>
<td valign="top"><strong>ibnmajah 1360</strong>&nbsp; 0.8004 <small>· Sahih</small><br><br>It was narrated from ‘Aishah that the Prophet (saw) used to pray nine Rak’ah at night.</td>
<td valign="top"><strong>ibnmajah 898</strong>&nbsp; 0.7959 <small>· Da’if</small><br><br>It was narrated that Ibn ‘Abbas said: “When praying at night (Qiyamul-Lail), the Messenger of Allah (saw) used to say between the two prostrations: ‘R</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8492<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
<td valign="top"><strong>muslim 740</strong>&nbsp; 0.8779<br><br>'A'isha observed that the Messenger of Allah (may peace be upon him) used to observe prayer in the night and the last of his (night) prayer was Witr.</td>
<td valign="top"><strong>muslim 740</strong>&nbsp; 0.8890<br><br>'A'isha observed that the Messenger of Allah (may peace be upon him) used to observe prayer in the night and the last of his (night) prayer was Witr.</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8425 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8538 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>ibnmajah 286</strong>&nbsp; 9.9426 <small>· Sahih</small><br><br>"Whenever the Messenger of Allah got up for prayer at night to pray Tahajjud (night optional prayer), he would clean his mouth with the tooth stick."</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8754<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>nasai 1673</strong>&nbsp; 0.8831 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said that: A man asked the Messenger of Allah (SAW) about prayers at night. The Messenger of Allah (SAW) said: </td>
<td valign="top"><strong>forty 36</strong>&nbsp; 0.8346<br><br>O Allah, bless my nation in its early rising on Thursdays!</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8325 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
<td valign="top"><strong>ibnmajah 1186</strong>&nbsp; 0.7922 <small>· Hasan</small><br><br>It was narrated that ‘Ali said: “At every part of the night the Messenger of Allah (saw) prayed Witr, at the beginning and in the middle, and finally </td>
<td valign="top"><strong>nasai 1671</strong>&nbsp; 0.7923 <small>· Sahih</small><br><br>It was narrated from Ibn Umar that: The Prophet (SAW) said: "prayers at night are (offered) two by two, then if you fear that dawn will come, pray wit</td>
<td valign="top"><strong>ibnmajah 1359</strong>&nbsp; 0.7956 <small>· Sahih</small><br><br>It was narrated that ‘Aishah said: “The Prophet (saw) used to pray thirteen Rak’ah at night.”</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8483 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>bukhari 997</strong>&nbsp; 0.8766<br><br>Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8881<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8425<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8538<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>bulugh 380</strong>&nbsp; 9.9318 <small>· Uncategorized</small><br><br>Allah's Messenger (SAW) offered Witr prayer (on different nights) at various hours, extending (from the 'Isha' prayer) up to the last hour of the nigh</td>
<td valign="top"><strong>bukhari 997</strong>&nbsp; 0.8739<br><br>Narrated `A'isha: The Prophet used to offer his night prayer while I was sleeping across in his bed. Whenever he intended to offer the witr prayer, he</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8819 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>tirmidhi 448</strong>&nbsp; 0.8317 <small>· Sahih</small><br><br>Aishah narrated: "The Prophet (S) stood (in prayer) with an Ayah from the Qur'an at night"</td>
<td valign="top"><strong>nasai 1672</strong>&nbsp; 0.8274 <small>· Sahih</small><br><br>It was narrated that Ibn Umar said: "A man from among the Muslims asked the Messenger of Allah (SAW): 'How are prayers at night to be done?' He said: </td>
<td valign="top"><strong>tirmidhi 443</strong>&nbsp; 0.7916 <small>· Sahih</small><br><br>Aishah narrated: "The Prophet (S) would pray nine Rak'ah in the night."</td>
<td valign="top"><strong>nasai 1668</strong>&nbsp; 0.7919 <small>· Sahih</small><br><br>It was narrated from Salim, from his father, that : The Prophet (SAW) said: "Prayers at night are two by two, then if you fear that dawn will come, pr</td>
<td valign="top"><strong>nasai 1668</strong>&nbsp; 0.7928 <small>· Sahih</small><br><br>It was narrated from Salim, from his father, that : The Prophet (SAW) said: "Prayers at night are two by two, then if you fear that dawn will come, pr</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8437<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>muslim 514</strong>&nbsp; 0.8746<br><br>'A'isha reported: The Apostle of Allah (may peace be upon him) said prayer at night and I was by his side in a state of meanses and I had a sheet pull</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8871 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8413<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8502<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>tirmidhi 806</strong>&nbsp; 9.9219 <small>· Sahih</small><br><br>"We fasted with the Prophet, so he did not pray (the night prayer) with us until seven (nights) of the month remained. Then he (pbuh) led us in prayer</td>
<td valign="top"><strong>muslim 514</strong>&nbsp; 0.8733<br><br>'A'isha reported: The Apostle of Allah (may peace be upon him) said prayer at night and I was by his side in a state of meanses and I had a sheet pull</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8812<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>forty 2</strong>&nbsp; 0.8244<br><br>War is deception.</td>
<td valign="top"><strong>abudawud 1321</strong>&nbsp; 0.8269 <small>· Sahih</small><br><br>Anas b. Malik said (explaining the meaning of the Qur'anic verse "Who forsake their beds to cry unto their Lord in fear and hope, and spend of what We</td>
<td valign="top"><strong>nasai 1692</strong>&nbsp; 0.7913 <small>· Sahih</small><br><br>It was narrated from 'Abdullah bin 'Umar that: The Messenger of Allah (SAW) said: "Prayer at night is two by two, then when you want to finish, pray o</td>
<td valign="top"><strong>tirmidhi 448</strong>&nbsp; 0.7918 <small>· Sahih</small><br><br>Aishah narrated: "The Prophet (S) stood (in prayer) with an Ayah from the Qur'an at night"</td>
<td valign="top"><strong>adab 696</strong>&nbsp; 0.7913 <small>· Sahih</small><br><br>'Abdullah ibn 'Abbas said, "When the Prophet, may Allah bless him and grant him peace, prayed the night prayer, and finished his prayer, glorifying Al</td>
<td valign="top"><strong>abudawud 1307</strong>&nbsp; 0.8435 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Do not give up prayer at night, for the Messenger of Allah (saws) would not leave it. Whenever he fell ill or lethargi</td>
<td valign="top"><strong>bukhari 990</strong>&nbsp; 0.8738<br><br>Narrated Ibn `Umar: Once a person asked Allah's Apostle (saws) about the night prayer. Allah's Apostle (saws) replied, "The night prayer is offered as</td>
<td valign="top"><strong>muslim 755 a</strong>&nbsp; 0.8866<br><br>Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he sho</td>
<td valign="top"><strong>ibnmajah 1252</strong>&nbsp; 0.8296 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “Safwan bin Mu’attal asked the Messenger of Allah (saw): ‘O Messenger of Allah, I want to ask you about someth</td>
<td valign="top"><strong>abudawud 1314</strong>&nbsp; 0.8394 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Prophet (saws) said: Any person who offers prayer at night regularly but (on a certain night) he is dominated by s</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 9.9218 <small>· Sahih</small><br><br>Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to follow him in the </td>
<td valign="top"><strong>bukhari 990</strong>&nbsp; 0.8725<br><br>Narrated Ibn `Umar: Once a person asked Allah's Apostle (saws) about the night prayer. Allah's Apostle (saws) replied, "The night prayer is offered as</td>
<td valign="top"><strong>nasai 1670</strong>&nbsp; 0.8767 <small>· Sahih</small><br><br>Ibn Umar told them that : A man asked the Messenger of Allah (SAW)about prayers at night, and he said: "Two by two, then if one of you fears that dawn</td>
<td valign="top"><strong>bulugh 188</strong>&nbsp; 0.8224<br><br>Abu Dawud added the words: "for each prayer".</td>
<td valign="top"><strong>nasai 1682</strong>&nbsp; 0.8266 <small>· Sahih</small><br><br>It was narrated that Ibn 'Umar said: "Whoever prays during the night, let him make the last of his prayers at night witr, because the Messenger of All</td>
<td valign="top"><strong>ibnmajah 898</strong>&nbsp; 0.7913 <small>· Da’if</small><br><br>It was narrated that Ibn ‘Abbas said: “When praying at night (Qiyamul-Lail), the Messenger of Allah (saw) used to say between the two prostrations: ‘R</td>
<td valign="top"><strong>ibnmajah 1321</strong>&nbsp; 0.7917 <small>· Da’if</small><br><br>It was narrated that Ibn ‘Abbas said: “The Prophet (saw) used to pray the night prayer two Rak’ah by two Rak’ah.”</td>
<td valign="top"><strong>nasai 1682</strong>&nbsp; 0.7908 <small>· Sahih</small><br><br>It was narrated that Ibn 'Umar said: "Whoever prays during the night, let him make the last of his prayers at night witr, because the Messenger of All</td>
<td valign="top"><strong>abudawud 1314</strong>&nbsp; 0.8380 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Prophet (saws) said: Any person who offers prayer at night regularly but (on a certain night) he is dominated by s</td>
<td valign="top"><strong>muslim 755 a</strong>&nbsp; 0.8722<br><br>Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he sho</td>
<td valign="top"><strong>muslim 514</strong>&nbsp; 0.8865<br><br>'A'isha reported: The Apostle of Allah (may peace be upon him) said prayer at night and I was by his side in a state of meanses and I had a sheet pull</td>
<td valign="top"><strong>abudawud 1307</strong>&nbsp; 0.8275 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Do not give up prayer at night, for the Messenger of Allah (saws) would not leave it. Whenever he fell ill or lethargi</td>
<td valign="top"><strong>abudawud 1307</strong>&nbsp; 0.8391 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Do not give up prayer at night, for the Messenger of Allah (saws) would not leave it. Whenever he fell ill or lethargi</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>tirmidhi 221</strong>&nbsp; 9.9061 <small>· Sahih</small><br><br>"Whoever attends Isha (prayer) in congregation, then he has (the reward as if he had) stood half of the night. And whoever prays Isha and Fajr in cong</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8722<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>nasai 1694</strong>&nbsp; 0.8757 <small>· Sahih</small><br><br>It was narrated from Abdullah bin 'Umar that: A man asked the Messenger of Allah (SAW) about prayer at night and the Messenger of Allah (SAW) said: "P</td>
<td valign="top"><strong>bulugh 331</strong>&nbsp; 0.8213<br><br>And in the narration of Muslim: "'Asr prayer".</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8214<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
<td valign="top"><strong>nasai 1672</strong>&nbsp; 0.7897 <small>· Sahih</small><br><br>It was narrated that Ibn Umar said: "A man from among the Muslims asked the Messenger of Allah (SAW): 'How are prayers at night to be done?' He said: </td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.7910<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>ibnmajah 1322</strong>&nbsp; 0.7905 <small>· Hasan</small><br><br>Ibn ‘Umar narrated that the Messenger of Allah (saw) said: “Prayers at night and during the day are to be offered two by two.”</td>
<td valign="top"><strong>abudawud 1304</strong>&nbsp; 0.8287 <small>· Hasan</small><br><br>Narrated Abdullah Ibn Abbas: In Surat al-Muzzammil (73), the verse: "Keep vigil at night but a little, a half thereof" (2-3) has been abrogated by the</td>
<td valign="top"><strong>bulugh 390</strong>&nbsp; 0.8702<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "If anyone is afraid that he may not get up in the latter part of the night, he should offer Witr i</td>
<td valign="top"><strong>bukhari 990</strong>&nbsp; 0.8864<br><br>Narrated Ibn `Umar: Once a person asked Allah's Apostle (saws) about the night prayer. Allah's Apostle (saws) replied, "The night prayer is offered as</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8252<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8374 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 564</strong>&nbsp; 9.9051 <small>· Sahih</small><br><br>"One night Allah's Apostle led us in the `Isha' prayer and that is the one called Al-`Atma [??] by the people. After the completion of the prayer, he </td>
<td valign="top"><strong>muslim 749 b</strong>&nbsp; 0.8709<br><br>Salim reported on the authority of his father that a person asked the Apostle of Allah (may peace be upon him) about the night prayer. He said: It con</td>
<td valign="top"><strong>nasai 1672</strong>&nbsp; 0.8751 <small>· Sahih</small><br><br>It was narrated that Ibn Umar said: "A man from among the Muslims asked the Messenger of Allah (SAW): 'How are prayers at night to be done?' He said: </td>
<td valign="top"><strong>bulugh 252</strong>&nbsp; 0.8205<br><br>Muslim added: "and Christians."</td>
<td valign="top"><strong>nasai 1793</strong>&nbsp; 0.8207 <small>· Sahih</small><br><br>It was narrated that Humaid bin Abdur-Rahman said: "Whoever misses his Wird at night, let him recite it during prayer before Zuhr, and that will be eq</td>
<td valign="top"><strong>nasai 1668</strong>&nbsp; 0.7895 <small>· Sahih</small><br><br>It was narrated from Salim, from his father, that : The Prophet (SAW) said: "Prayers at night are two by two, then if you fear that dawn will come, pr</td>
<td valign="top"><strong>nasai 1672</strong>&nbsp; 0.7903 <small>· Sahih</small><br><br>It was narrated that Ibn Umar said: "A man from among the Muslims asked the Messenger of Allah (SAW): 'How are prayers at night to be done?' He said: </td>
<td valign="top"><strong>ibnmajah 1372</strong>&nbsp; 0.7905 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet (saw) said: “When anyone of you gets up to pray at night, and his tongue stumbles over the words of</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8267<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>bukhari 212</strong>&nbsp; 0.8699<br><br>Narrated `Aisha: Allah's Apostle said, "If anyone of you feels drowsy while praying he should go to bed (sleep) till his slumber is over because in pr</td>
<td valign="top"><strong>muslim 749 b</strong>&nbsp; 0.8856<br><br>Salim reported on the authority of his father that a person asked the Apostle of Allah (may peace be upon him) about the night prayer. He said: It con</td>
<td valign="top"><strong>abudawud 419</strong>&nbsp; 0.8248 <small>· Sahih</small><br><br>Narrated An-Nu'man ibn Bashir: I am the one who is best informed of the time of this prayer, i.e. the night prayer. The Messenger of Allah (saws) used</td>
<td valign="top"><strong>mishkat 1254</strong>&nbsp; 0.8369<br><br>Ibn ‘Umar reported God’s Messenger as saying, “Prayer during the night should consist of pairs of rak'as , but if one of you fears the morning is near</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>nasai 5202</strong>&nbsp; 9.8950 <small>· Sahih</small><br><br>"The Messenger of Allah [SAW] delayed 'Isha' prayer one night, until half the night had passed, then he came out and led us in prayer. And it is as if</td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.8700<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>bulugh 380</strong>&nbsp; 0.8740<br><br>Narrated ['Aishah (RA)]: Allah's Messenger (SAW) offered Witr prayer (on different nights) at various hours, extending (from the 'Isha' prayer) up to </td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8168<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>nasai 1673</strong>&nbsp; 0.8172 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said that: A man asked the Messenger of Allah (SAW) about prayers at night. The Messenger of Allah (SAW) said: </td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.7890<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>nasai 1673</strong>&nbsp; 0.7901 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said that: A man asked the Messenger of Allah (SAW) about prayers at night. The Messenger of Allah (SAW) said: </td>
<td valign="top"><strong>ibnmajah 1319</strong>&nbsp; 0.7905 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The night prayer is (to be offered) two by two.”</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8266 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
<td valign="top"><strong>muslim 749 b</strong>&nbsp; 0.8691<br><br>Salim reported on the authority of his father that a person asked the Apostle of Allah (may peace be upon him) about the night prayer. He said: It con</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8845 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8215 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
<td valign="top"><strong>malik 267</strong>&nbsp; 0.8353<br><br>Yahya related to me from Malik from Nafi and Abdullah ibn Umar that a man asked the Messenger of Allah, may Allah bless him and grant him peace, about</td>
</tr>
</tbody></table>

---

## hadithText: forgiving someone who wronged you

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 13ms |
| mxbai-embed-large | 51ms | 83ms |
| nomic-embed-text | 42ms | 81ms |
| snowflake-arctic-embed:m | 120ms | 91ms |
| all-MiniLM-L6-v2 | 41ms | 82ms |
| embeddinggemma-300m | 80ms | 81ms |
| embeddinggemma-300m-qat-q8 | 62ms | 83ms |
| embeddinggemma-300m-qat-q4 | 74ms | 80ms |
| mxbai-embed-xsmall-v1 | 12ms | 79ms |
| mxbai-embed-large (Q4_K_M) | 56ms | 85ms |
| mxbai-embed-large (INT8 ONNX) | 31ms | 82ms |
| mxbai-embed-xsmall (INT8 ONNX) | 2ms | 80ms |
| mxbai-embed-xsmall (INT4 ONNX) | 7ms | 82ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M)</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX)</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX)</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX)</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ahmad 930</strong>&nbsp; 16.8779 <small>· Hasan</small><br><br>`Abdur-Razzaq said. Someone who saw `Ali when he rode told me: When he put his foot in the stirrup, he said: Bismillah (in the Name of Allah). When he</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8291<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8670<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>forty 28</strong>&nbsp; 0.8396<br><br>One who repents from sin is like someone without sin.</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7683 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>bukhari 1848</strong>&nbsp; 0.7551<br><br>A man bit the hand of another man but in that process the latter broke one incisor tooth of the former, and the Prophet forgave the latter.</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.7519 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.7528 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7959 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8227<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8625<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7881 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7920 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>adab 667</strong>&nbsp; 15.8980 <small>· Da'if</small><br><br>The firmest supplication is to say, 'O Allah, you are my Lord and I am Your slave. I have wronged myself and I admit my wrong action. Only You forgive</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.8228 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>mishkat 942</strong>&nbsp; 0.8560<br><br>Abu Bakr as-Siddiq said that he asked God’s Messenger to teach him a supplication to use in his prayer, and he told him to say, “O God, I have greatly</td>
<td valign="top"><strong>forty 14</strong>&nbsp; 0.8387<br><br>Someone who takes back his gift is like someone who eats his vomit.</td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.7459<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.7548 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>forty 20</strong>&nbsp; 0.7506<br><br>The king’s pardon preserves the kingdom.</td>
<td valign="top"><strong>adab 380</strong>&nbsp; 0.7510 <small>· Sahih</small><br><br>'Abdullah ibn al-'As reported that the Prophet, may Allah bless him and grant him peace, said, "Show mercy and you will be shown mercy. Forgive and Al</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7799 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.8215 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>bukhari 2449</strong>&nbsp; 0.8518<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his reputation or anything else, he should beg him to for</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7760 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7702 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>adab 706</strong>&nbsp; 15.5979 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>hisn 57</strong>&nbsp; 0.8222<br><br>Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfir lī maghfiratam’min `indika warḥamnī innaka 'anta ‘l-Ghafūr</td>
<td valign="top"><strong>adab 667</strong>&nbsp; 0.8506 <small>· Da'if</small><br><br>Abu Hurayra reported that the Prophet, may Allah bless him and grant him peace, said, "The firmest supplication is to say, 'O Allah, you are my Lord a</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8369<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7424<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>forty 20</strong>&nbsp; 0.7526<br><br>The king’s pardon preserves the kingdom.</td>
<td valign="top"><strong>bukhari 1848</strong>&nbsp; 0.7482<br><br>A man bit the hand of another man but in that process the latter broke one incisor tooth of the former, and the Prophet forgave the latter.</td>
<td valign="top"><strong>bukhari 1848</strong>&nbsp; 0.7462<br><br>A man bit the hand of another man but in that process the latter broke one incisor tooth of the former, and the Prophet forgave the latter.</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7757<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>forty 28</strong>&nbsp; 0.8189<br><br>One who repents from sin is like someone without sin.</td>
<td valign="top"><strong>nasai 4723</strong>&nbsp; 0.8506 <small>· Sahih</small><br><br>It was narrated from 'Alqamah binWa'il Al-Hadrami that his farther said: A man who had killed someone was brought to the Messenger of Allah, and he wa</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7753 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7646 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>ahmad 56</strong>&nbsp; 14.7569 <small>· Sahih</small><br><br>I heard ‘Ali say: If I heard a hadeeth from the Messenger of Allah (ﷺ), Allah benefitted me as He willed thereby. If someone else told me something fr</td>
<td valign="top"><strong>muslim 1695 b</strong>&nbsp; 0.8213<br><br>'Abdullah b. Buraida reported on the authority of his father that Ma'iz b. Malik al-Aslami came to Allah's Messenger (may peace be upon him) and said:</td>
<td valign="top"><strong>bukhari 4644</strong>&nbsp; 0.8493<br><br>`Abdullah bin Az-Zubair said: Allah ordered His Prophet to forgive the people their misbehavior (towards him).</td>
<td valign="top"><strong>forty 12</strong>&nbsp; 0.8262<br><br>He is not one of us who cheats us.</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7411 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
<td valign="top"><strong>adab 380</strong>&nbsp; 0.7519 <small>· Sahih</small><br><br>'Abdullah ibn al-'As reported that the Prophet, may Allah bless him and grant him peace, said, "Show mercy and you will be shown mercy. Forgive and Al</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7383<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>hisn 57</strong>&nbsp; 0.7436<br><br>Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfir lī maghfiratam’min `indika warḥamnī innaka 'anta ‘l-Ghafūr</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7586 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8177<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8496<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7577<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7627<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>ahmad 47, 48</strong>&nbsp; 14.1649 <small>· Sahih</small><br><br>If Heard something from the Messenger of Allah (ﷺ), Allah would benefit me thereby as He willed. Abu Bakr told me - and Abu Bakr spoke the truth - he </td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8162<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>adab 37</strong>&nbsp; 0.8457 <small>· Sahih</small><br><br>Ibn Sirin said, "We were with Abu Hurayra one night and he said, 'O Allah, forgive Abu Hurayra and his mother and whoever asks for forgiveness for bot</td>
<td valign="top"><strong>forty 34</strong>&nbsp; 0.8261<br><br>The leader of a people is their servant.</td>
<td valign="top"><strong>forty 34</strong>&nbsp; 0.7397<br><br>On the authority of Anas (may Allah be pleased with him), who said: I heard the Messenger of Allah (PBUH) say: Allah the Almighty said: O son of Adam,</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7456<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>adab 380</strong>&nbsp; 0.7380 <small>· Sahih</small><br><br>'Abdullah ibn al-'As reported that the Prophet, may Allah bless him and grant him peace, said, "Show mercy and you will be shown mercy. Forgive and Al</td>
<td valign="top"><strong>forty 28</strong>&nbsp; 0.7422<br><br>One who repents from sin is like someone without sin.</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7504 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
<td valign="top"><strong>forty 27</strong>&nbsp; 0.8157<br><br>Hearts are predisposed to love someone who does them good and detest someone who does them harm.</td>
<td valign="top"><strong>mishkat 3277</strong>&nbsp; 0.8474<br><br>Ibn ‘Abbas said: One makes atonement for something he has made unlawful for himself.* You have had a good example in God’s Messenger. * i.e. something</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7494 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7582 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>ahmad 8</strong>&nbsp; 14.1250 <small>· Sahih</small><br><br>Teach me a dua that I may say in my prayer. He said: `Say: O Allah, I have wronged myself greatly and no one forgives sins but you, grant me forgivene</td>
<td valign="top"><strong>tirmidhi 2495</strong>&nbsp; 0.8152 <small>· Hasan</small><br><br>Abu Dharr narrated that the Messenger of Allah (s.a.w) said: "Allah,Most High said: 'O My Slaves! All of you are astray except whom I guide, so ask Me</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.8446 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>forty 25</strong>&nbsp; 0.8244<br><br>He does not thank Allah who does not thank people.</td>
<td valign="top"><strong>adab 293</strong>&nbsp; 0.7395 <small>· Sahih</small><br><br>Abu Mas'ud al-Ansari reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Before your time a man was called to accoun</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.7455<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7349 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7409<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>riyadussalihin 210</strong>&nbsp; 0.7472<br><br>Abu Hurairah (May Allah bepleased with him) reported: The Prophet (PBUH) said, "He who has done a wrong affecting his brother's honour or anything els</td>
<td valign="top"><strong>bukhari 7387, 7388</strong>&nbsp; 0.8122<br><br>Narrated `Abdullah bin `Amr: Abu Bakr As-Siddiq said to the Prophet "O Allah's Apostle! Teach me an invocation with which I may invoke Allah in my pra</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.8466 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.7459<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7492 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>adab 673</strong>&nbsp; 14.0837 <small>· Sahih</small><br><br>One of the supplications of the Prophet, may Allah bless him and grant him peace, was 'O Allah, forgive me for my past and future wrong actions, what </td>
<td valign="top"><strong>bulugh 825</strong>&nbsp; 0.8149<br><br>Narrated [Abu Hurairah (RA)]: Allah's Messenger (SAW) said, "Whoever accepts back what he sold to a Muslim, Allah will forgive his fault." [Reported b</td>
<td valign="top"><strong>ahmad 8</strong>&nbsp; 0.8441 <small>· Sahih (Darussalam) [Bukhari 834 and Muslim 2705]</small><br><br>It was narrated from Abu Bakr as Siddeeq that he said to the Messenger of Allah (ﷺ) : Teach me a dua that I may say in my prayer. He said: `Say: O All</td>
<td valign="top"><strong>forty 32</strong>&nbsp; 0.8239<br><br>Whoever is killed attempting to save his property is a martyr.</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7361 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>nasai 2041</strong>&nbsp; 0.7393 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "When An-Najashi died, the Prophet said: 'Pray for forgiveness for him."'</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.7346<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>forty 20</strong>&nbsp; 0.7387<br><br>The king’s pardon preserves the kingdom.</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7405 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>bukhari 3480</strong>&nbsp; 0.8121<br><br>Narrated Abu Huraira: Allah's Apostle said, "A man used to give loans to the people and used to say to his servant, 'If the debtor is poor, forgive hi</td>
<td valign="top"><strong>bulugh 319</strong>&nbsp; 0.8464<br><br>Narrated Abu Bakr as-Siddiq (RA): He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I h</td>
<td valign="top"><strong>riyadussalihin 210</strong>&nbsp; 0.7448<br><br>Abu Hurairah (May Allah bepleased with him) reported: The Prophet (PBUH) said, "He who has done a wrong affecting his brother's honour or anything els</td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.7488<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>adab 688</strong>&nbsp; 14.0330 <small>· Sahih</small><br><br>Abu Musa reported that the Prophet, may Allah bless him and grant him peace, used to make this supplication, "O Allah, forgive my errors, my ignorance</td>
<td valign="top"><strong>nasai 4723</strong>&nbsp; 0.8143 <small>· Sahih</small><br><br>It was narrated from 'Alqamah binWa'il Al-Hadrami that his farther said: A man who had killed someone was brought to the Messenger of Allah, and he wa</td>
<td valign="top"><strong>muslim 1562 a</strong>&nbsp; 0.8429<br><br>Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: There was a person who gave loans to the people </td>
<td valign="top"><strong>forty 26</strong>&nbsp; 0.8235<br><br>Your love of something can blind and deafen (you).</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.7354<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7385 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>bukhari 6534</strong>&nbsp; 0.7339<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever has wronged his brother, should ask for his pardon (before his death), as (in the Hereafter) ther</td>
<td valign="top"><strong>nasai 2041</strong>&nbsp; 0.7371 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "When An-Najashi died, the Prophet said: 'Pray for forgiveness for him."'</td>
<td valign="top"><strong>forty 34</strong>&nbsp; 0.7382<br><br>On the authority of Anas (may Allah be pleased with him), who said: I heard the Messenger of Allah (PBUH) say: Allah the Almighty said: O son of Adam,</td>
<td valign="top"><strong>adab 617</strong>&nbsp; 0.8116 <small>· Sahih</small><br><br>Shaddad ibn Aws reported that the Prophet, may Allah bless him and grant him peace, said, "The best way of asking forgiveness is 'O Allah, You are my </td>
<td valign="top"><strong>adab 673</strong>&nbsp; 0.8464 <small>· Sahih</small><br><br>Abu Hurayra said, "One of the supplications of the Prophet, may Allah bless him and grant him peace, was 'O Allah, forgive me for my past and future w</td>
<td valign="top"><strong>bulugh 1556</strong>&nbsp; 0.7406<br><br>Shaddad bin Aus (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “The best manner of asking for forgiveness is to say: “O Allah! You are my</td>
<td valign="top"><strong>adab 293</strong>&nbsp; 0.7478 <small>· Sahih</small><br><br>Abu Mas'ud al-Ansari reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Before your time a man was called to accoun</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>ahmad 28</strong>&nbsp; 14.0007 <small>· Sahih</small><br><br>Teach me a du'a` that I may say in my prayer. He said: `Say: O Allah. I have wronged myself greatly and no one forgives sins except You, so grant me f</td>
<td valign="top"><strong>mishkat 3277</strong>&nbsp; 0.8139<br><br>Ibn ‘Abbas said: One makes atonement for something he has made unlawful for himself.* You have had a good example in God’s Messenger. * i.e. something</td>
<td valign="top"><strong>ahmad 28</strong>&nbsp; 0.8417 <small>· Sahih (Darussalam) [Bukhari 834 and Muslim 2705]</small><br><br>It was narrated from Abu Bakr as-Siddeeq that he said to the Messenger of Allah (ﷺ): Teach me a du'a` that I may say in my prayer. He said: `Say: O Al</td>
<td valign="top"><strong>forty 21</strong>&nbsp; 0.8223<br><br>A man will be with whom he loves.</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.7304 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>ibnmajah 2040</strong>&nbsp; 0.7362 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that: the Messenger of Allah (SAW) said: "Allah has forgiven my nation for what they think of to themselves, so long</td>
<td valign="top"><strong>ibnmajah 2040</strong>&nbsp; 0.7328 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that: the Messenger of Allah (SAW) said: "Allah has forgiven my nation for what they think of to themselves, so long</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7369 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>bulugh 1556</strong>&nbsp; 0.7378<br><br>Shaddad bin Aus (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “The best manner of asking for forgiveness is to say: “O Allah! You are my</td>
<td valign="top"><strong>bulugh 825</strong>&nbsp; 0.8111<br><br>Narrated [Abu Hurairah (RA)]: Allah's Messenger (SAW) said, "Whoever accepts back what he sold to a Muslim, Allah will forgive his fault." [Reported b</td>
<td valign="top"><strong>bukhari 3480</strong>&nbsp; 0.8454<br><br>Narrated Abu Huraira: Allah's Apostle said, "A man used to give loans to the people and used to say to his servant, 'If the debtor is poor, forgive hi</td>
<td valign="top"><strong>ahmad 1363</strong>&nbsp; 0.7359 <small>· A Hasan Hadeeth]</small><br><br>It was narrated that ‘Ali (رضي الله عنه) said: The Messenger of Allah (رضي الله عنه) said: `Shall I not teach you some words which, if you say them yo</td>
<td valign="top"><strong>ahmad 1363</strong>&nbsp; 0.7453 <small>· A Hasan Hadeeth]</small><br><br>It was narrated that ‘Ali (رضي الله عنه) said: The Messenger of Allah (رضي الله عنه) said: `Shall I not teach you some words which, if you say them yo</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bulugh 319</strong>&nbsp; 14.0007 <small>· Uncategorized</small><br><br>He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I have greatly wronged myself, and no</td>
<td valign="top"><strong>malik 1520</strong>&nbsp; 0.8129<br><br>Malik related to me from Zurayq ibn Hakim al-Ayli that a man called Misbah asked his son for help and he thought him unnecessarily slow. When the son </td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.8403<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
<td valign="top"><strong>forty 27</strong>&nbsp; 0.8222<br><br>Hearts are predisposed to love someone who does them good and detest someone who does them harm.</td>
<td valign="top"><strong>bulugh 825</strong>&nbsp; 0.7287<br><br>Narrated [Abu Hurairah (RA)]: Allah's Messenger (SAW) said, "Whoever accepts back what he sold to a Muslim, Allah will forgive his fault." [Reported b</td>
<td valign="top"><strong>mishkat 2330</strong>&nbsp; 0.7346<br><br>'A’isha reported God’s messenger as saying, "When a servant acknowledges his sin and repents, God forgives him.” (Bukhari and Muslim.)</td>
<td valign="top"><strong>bukhari 2449</strong>&nbsp; 0.7305<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever has oppressed another person concerning his reputation or anything else, he should beg him to for</td>
<td valign="top"><strong>bukhari 6534</strong>&nbsp; 0.7342<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever has wronged his brother, should ask for his pardon (before his death), as (in the Hereafter) ther</td>
<td valign="top"><strong>forty 39</strong>&nbsp; 0.7357<br><br>On the authority of Ibn Abbas (may Allah be pleased with him), that the Messenger of Allah (peace and blessings of Allah be upon him) said: Verily All</td>
<td valign="top"><strong>mishkat 3277</strong>&nbsp; 0.8108<br><br>Ibn ‘Abbas said: One makes atonement for something he has made unlawful for himself.* You have had a good example in God’s Messenger. * i.e. something</td>
<td valign="top"><strong>bulugh 1517</strong>&nbsp; 0.8442<br><br>Anas (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “The atonement of backbiting a man is to ask Allah to forgive him.” Related by Al-Har</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.7350<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.7404 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
</tr>
</tbody></table>

---

## hadithText: comparing yourself to others

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 10ms |
| mxbai-embed-large | 43ms | 81ms |
| nomic-embed-text | 40ms | 82ms |
| snowflake-arctic-embed:m | 38ms | 84ms |
| all-MiniLM-L6-v2 | 32ms | 82ms |
| embeddinggemma-300m | 67ms | 83ms |
| embeddinggemma-300m-qat-q8 | 74ms | 83ms |
| embeddinggemma-300m-qat-q4 | 61ms | 80ms |
| mxbai-embed-xsmall-v1 | 10ms | 78ms |
| mxbai-embed-large (Q4_K_M) | 43ms | 82ms |
| mxbai-embed-large (INT8 ONNX) | 28ms | 80ms |
| mxbai-embed-xsmall (INT8 ONNX) | 2ms | 82ms |
| mxbai-embed-xsmall (INT4 ONNX) | 6ms | 81ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M)</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX)</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX)</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX)</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>muslim 1776 d</strong>&nbsp; 13.1936 <small>· Sahih</small><br><br>This hadith has been narrated on the authority of Bara' with another chain of transmitters, but this hadith is short as compared with other ahadith wh</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8145<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8351<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8379<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7151<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7346<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7365<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7421<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7205<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8091<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8453<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7254 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7225<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>abudawud 4627</strong>&nbsp; 11.8770 <small>· Sahih</small><br><br>We used to say in the times of the Prophet (saws): We do not compare anyone with Abu Bakr. ’Umar came next and then ‘Uthman. We then would leave (rest</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8031<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>bukhari 6061</strong>&nbsp; 0.8167<br><br>Narrated Abu Bakra: A man was mentioned before the Prophet and another man praised him greatly The Prophet said, "May Allah's Mercy be on you ! You ha</td>
<td valign="top"><strong>forty 16</strong>&nbsp; 0.8265<br><br>People are like the teeth of a comb.</td>
<td valign="top"><strong>muslim 816</strong>&nbsp; 0.7032<br><br>'Abdullah b. Mas'ud reported Allah's Messenger (may peace be upon him) as saying: There should be no envy but only in case of two persons: one having </td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.7288<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.7252<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>forty 16</strong>&nbsp; 0.7403<br><br>People are like the teeth of a comb.</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7198<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7977<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.8377<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7241<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7149<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>muslim 2431</strong>&nbsp; 11.3899 <small>· Sahih</small><br><br>There are many persons amongst men who are quite perfect but there are none perfect amongst women except Mary, daughter of 'Imran, Asiya wife of Phara</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7971<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.8105<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>tirmidhi 2780b</strong>&nbsp; 0.8228<br><br>Another chain with a similar narration</td>
<td valign="top"><strong>adab 426</strong>&nbsp; 0.6897 <small>· Sahih</small><br><br>The Prophet, may Allah bless him and grant him peace, said, "Allah Almighty revealed to me that you should be humble and that you should not wrong one</td>
<td valign="top"><strong>forty 16</strong>&nbsp; 0.7238<br><br>People are like the teeth of a comb.</td>
<td valign="top"><strong>forty 16</strong>&nbsp; 0.7202<br><br>People are like the teeth of a comb.</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.7345<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7192 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7929<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8313<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7225<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7128 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bukhari 3334</strong>&nbsp; 11.2561 <small>· Sahih</small><br><br>The Prophet said, "Allah will say to that person of the (Hell) Fire who will receive the least punishment, 'If you had everything on the earth, would </td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7928<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>bulugh 1471</strong>&nbsp; 0.8105<br><br>Ibn ’Umar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “He who imitates any people (in their actions) is considered to be one of them.”</td>
<td valign="top"><strong>forty 37</strong>&nbsp; 0.8198<br><br>Poverty can almost turn into disbelief.</td>
<td valign="top"><strong>tirmidhi 3607</strong>&nbsp; 0.6892 <small>· Da'if</small><br><br>Narrated Al-'Abbas bin 'Abdul-Muttalib: "I said: 'O Messenger of Allah! Indeed the Quraish have sat and spoken between themselves about the best of th</td>
<td valign="top"><strong>forty 13</strong>&nbsp; 0.7097<br><br>A little that suffices is better than an abundance that distracts.</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7170 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7199 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7148<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7885<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.8308<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7218<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>bulugh 1527</strong>&nbsp; 0.7119<br><br>’Iyad bin Himar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Allah, the Most High has revealed to me that you (people) should be humbl</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>abudawud 356</strong>&nbsp; 10.7595 <small>· Hasan</small><br><br>I have embraced Islam. The Prophet (saws) said to him: Remove from yourself the hair that grew during of unbelief, saying "shave them". He further say</td>
<td valign="top"><strong>adab 159</strong>&nbsp; 0.7910<br><br>Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. T</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.8086 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>forty 17</strong>&nbsp; 0.8136<br><br>Richness lies in the richness of the soul.</td>
<td valign="top"><strong>bulugh 928</strong>&nbsp; 0.6887<br><br>A narration by Muslim has: He said, "Call someone other than me as a witness to this." He then said, "Would you like them to be equal in their kind tr</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7089 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>forty 13</strong>&nbsp; 0.7143<br><br>A little that suffices is better than an abundance that distracts.</td>
<td valign="top"><strong>forty 14</strong>&nbsp; 0.7134<br><br>Someone who takes back his gift is like someone who eats his vomit.</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7112<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7849<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>adab 159</strong>&nbsp; 0.8282<br><br>Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. T</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7145<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
<td valign="top"><strong>bulugh 928</strong>&nbsp; 0.7112<br><br>A narration by Muslim has: He said, "Call someone other than me as a witness to this." He then said, "Would you like them to be equal in their kind tr</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>mishkat 6025</strong>&nbsp; 10.4603 <small>· Uncategorized</small><br><br>In the time of the Prophet, we did not compare anyone with Abu Bakr. `Umar came next and then Uthman. We would then leave the Prophet's companions wit</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7869<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>bukhari 6162</strong>&nbsp; 0.8078<br><br>Narrated Abu Bakra: A man praised another man in front of the Prophet. The Prophet said thrice, "Wailaka (Woe on you) ! You have cut the neck of your </td>
<td valign="top"><strong>tirmidhi 2783b</strong>&nbsp; 0.8135<br><br>(Another chain) with a similar narration</td>
<td valign="top"><strong>adab 898</strong>&nbsp; 0.6847 <small>· Sahih</small><br><br>Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes </td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7061<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7065<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>forty 13</strong>&nbsp; 0.7121<br><br>A little that suffices is better than an abundance that distracts.</td>
<td valign="top"><strong>riyadussalihin 571</strong>&nbsp; 0.7054<br><br>Ibn 'Umar (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said: "Envy is justified in regard to two types of persons only: a man w</td>
<td valign="top"><strong>adab 159</strong>&nbsp; 0.7839<br><br>Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. T</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.8275 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7088<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7101<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>mishkat 48</strong>&nbsp; 10.3950 <small>· Uncategorized</small><br><br>He also said that he asked the Prophet what was the most excellent aspect of faith, and received the reply, “That you should love for God’s sake, hate</td>
<td valign="top"><strong>muslim 2536</strong>&nbsp; 0.7830<br><br>'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to</td>
<td valign="top"><strong>nasai 3947</strong>&nbsp; 0.8073 <small>· sahih</small><br><br>It was narrated from Abu Musa that the Prophet said: "The superiority of 'Aishah to other women is like the superiority of Tharid to other kinds of fo</td>
<td valign="top"><strong>forty 2</strong>&nbsp; 0.8132<br><br>War is deception.</td>
<td valign="top"><strong>muslim 2762 b</strong>&nbsp; 0.6763<br><br>Asma' reported that Allah's Apostle (may peace be upon him) said: There is none more self-respecting than Allah, the Exalted and Glorious.</td>
<td valign="top"><strong>nasai 384b</strong>&nbsp; 0.7035<br><br>(Another chain) with similarity.</td>
<td valign="top"><strong>muslim 2963 c</strong>&nbsp; 0.7050<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those wh</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7055<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>riyadussalihin 997</strong>&nbsp; 0.7047<br><br>Ibn 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said: "Envy is justified in regard to two types of persons only: a man whom Al</td>
<td valign="top"><strong>abudawud 4092</strong>&nbsp; 0.7838 <small>· Sahih in chain</small><br><br>Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been gi</td>
<td valign="top"><strong>muslim 2536</strong>&nbsp; 0.8273<br><br>'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to</td>
<td valign="top"><strong>riyadussalihin 997</strong>&nbsp; 0.7087<br><br>Ibn 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said: "Envy is justified in regard to two types of persons only: a man whom Al</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7092<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>muslim 2939 b</strong>&nbsp; 10.0806 <small>· Sahih</small><br><br>What did you ask? Mughira replied: I said that the people alleged that he would have a mountain load of bread and mutton and rivers of water. Thereupo</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7829 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>adab 1146</strong>&nbsp; 0.8044 <small>· Da'if</small><br><br>Ibn 'Abbas said, "The most precious of people in my opinion is my sitting companion. This is so much the case that he can step over the shoulders of p</td>
<td valign="top"><strong>forty 21</strong>&nbsp; 0.8128<br><br>A man will be with whom he loves.</td>
<td valign="top"><strong>bukhari 3336</strong>&nbsp; 0.6750<br><br>Narrated Aishah (ra): I heard the Prophet (saws), "Souls are like recruited troops: Those who are like qualities are inclined to each other, but those</td>
<td valign="top"><strong>tirmidhi 1515</strong>&nbsp; 0.7012 <small>· Hasan</small><br><br>Another chain with similar.</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.7045<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>forty 28</strong>&nbsp; 0.7010<br><br>One who repents from sin is like someone without sin.</td>
<td valign="top"><strong>muslim 816</strong>&nbsp; 0.7037<br><br>'Abdullah b. Mas'ud reported Allah's Messenger (may peace be upon him) as saying: There should be no envy but only in case of two persons: one having </td>
<td valign="top"><strong>muslim 2536</strong>&nbsp; 0.7812<br><br>'A'isha reported that a person asked Allah's Apostle (may peace be upon him) as to who amongst the people were the best. He said: Of the generation to</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.8208<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>riyadussalihin 571</strong>&nbsp; 0.7071<br><br>Ibn 'Umar (May Allah be pleased with him) reported: Messenger of Allah (PBUH) said: "Envy is justified in regard to two types of persons only: a man w</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7062<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 4816</strong>&nbsp; 9.8959 <small>· Sahih</small><br><br>(regarding) the Verse: 'And you have not been screening against yourself lest your ears, and your eyes and your skins should testify against you..' (4</td>
<td valign="top"><strong>abudawud 4092</strong>&nbsp; 0.7815 <small>· Sahih in chain</small><br><br>Narrated AbuHurayrah: A man who was beautiful came to the Prophet (saws). He said: Messenger of Allah, I am a man who likes beauty, and I have been gi</td>
<td valign="top"><strong>abudawud 4627</strong>&nbsp; 0.8041 <small>· Sahih</small><br><br>Ibn ‘Umar said: We used to say in the times of the Prophet (saws): We do not compare anyone with Abu Bakr. ’Umar came next and then ‘Uthman. We then w</td>
<td valign="top"><strong>tirmidhi 226</strong>&nbsp; 0.8126<br><br>Narrator not mentioned: A Similar narration</td>
<td valign="top"><strong>adab 783</strong>&nbsp; 0.6745 <small>· Sahih</small><br><br>Ibn 'Abbas said, "A man said, to the Prophet, 'Whatever Allah wills and you will.' He said, 'You have put an equal with Allah. It is what Allah alone </td>
<td valign="top"><strong>forty 17</strong>&nbsp; 0.7001<br><br>Richness lies in the richness of the soul.</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7036<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.7003<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>bulugh 1527</strong>&nbsp; 0.7013<br><br>’Iyad bin Himar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Allah, the Most High has revealed to me that you (people) should be humbl</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7812 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>muslim 2963 c</strong>&nbsp; 0.8200<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those wh</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7069<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
<td valign="top"><strong>riyadussalihin 997</strong>&nbsp; 0.7050<br><br>Ibn 'Umar (May Allah be pleased with them) reported: The Prophet (PBUH) said: "Envy is justified in regard to two types of persons only: a man whom Al</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>mishkat 2757</strong>&nbsp; 9.3983 <small>· Uncategorized</small><br><br>Yahya b. Sa'id said that God’s messenger was sitting when a grave was being dug in Medina. A man looked down into the grave and said, "What a bad-rest</td>
<td valign="top"><strong>adab 898</strong>&nbsp; 0.7814 <small>· Sahih</small><br><br>Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes </td>
<td valign="top"><strong>nasai 3948</strong>&nbsp; 0.8039 <small>· hasan</small><br><br>It was narrated from 'Aishah that the Prophet said: "The superiority of 'Aishah to other women is like the superiority of Tharid to other kinds of foo</td>
<td valign="top"><strong>forty 22</strong>&nbsp; 0.8125<br><br>A man who knows his worth will not be ruined.</td>
<td valign="top"><strong>muslim 3000 b</strong>&nbsp; 0.6717<br><br>Abd al-Rahman b. Abu Bakra reported on the authority of his father that a person was mentioned in the presence of Allah's Apostle (may peace be upon h</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.6998<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>forty 1</strong>&nbsp; 0.6996<br><br>The report is not like witnessing.</td>
<td valign="top"><strong>adab 328</strong>&nbsp; 0.6992 <small>· Da'if</small><br><br>Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faults."</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.6986<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>adab 898</strong>&nbsp; 0.7778 <small>· Sahih</small><br><br>Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes </td>
<td valign="top"><strong>adab 898</strong>&nbsp; 0.8200 <small>· Sahih</small><br><br>Ibn 'Abbas said, "I do not know anyone who acts by this ayat: 'Mankind! We created you from a male and a female, and made you into peoples and tribes </td>
<td valign="top"><strong>riyadussalihin 371</strong>&nbsp; 0.7054<br><br>Abu Hurairah (May Allah be pleased with him) reported: I heard Messenger of Allah (PBUH) saying, "People are like gold and silver; those who were best</td>
<td valign="top"><strong>adab 426</strong>&nbsp; 0.7049 <small>· Sahih</small><br><br>The Prophet, may Allah bless him and grant him peace, said, "Allah Almighty revealed to me that you should be humble and that you should not wrong one</td>
</tr>
</tbody></table>

---

## hadithText: aisha

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 9ms |
| mxbai-embed-large | 43ms | 83ms |
| nomic-embed-text | 39ms | 87ms |
| snowflake-arctic-embed:m | 34ms | 82ms |
| all-MiniLM-L6-v2 | 33ms | 83ms |
| embeddinggemma-300m | 60ms | 78ms |
| embeddinggemma-300m-qat-q8 | 64ms | 82ms |
| embeddinggemma-300m-qat-q4 | 100ms | 82ms |
| mxbai-embed-xsmall-v1 | 12ms | 83ms |
| mxbai-embed-large (Q4_K_M) | 42ms | 83ms |
| mxbai-embed-large (INT8 ONNX) | 22ms | 85ms |
| mxbai-embed-xsmall (INT8 ONNX) | 2ms | 82ms |
| mxbai-embed-xsmall (INT4 ONNX) | 2ms | 81ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M)</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX)</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX)</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX)</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 1972</strong>&nbsp; 5.3097 <small>· Sahih</small><br><br>that when Saudah bint Zam'ah grew old, she gave her day to 'Aishah, and the Messenger of Allah went to 'Aishah on Saudah's day.</td>
<td valign="top"><strong>bukhari 3894</strong>&nbsp; 0.8492<br><br>Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then </td>
<td valign="top"><strong>muslim 334 b</strong>&nbsp; 0.7809<br><br>'A'isha, the wife of the Messenger of Allah (may peace be upon him) reported: Umm Habiba b. Jahsh who was the sister-in-law of the Messenger of Allah </td>
<td valign="top"><strong>adab 995</strong>&nbsp; 0.9192 <small>· Sahih</small><br><br>See 993.</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.7880 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
<td valign="top"><strong>tirmidhi 2846b</strong>&nbsp; 0.7614<br><br>(Another chain) from 'Aishah with the same narration.</td>
<td valign="top"><strong>tirmidhi 2846b</strong>&nbsp; 0.7684<br><br>(Another chain) from 'Aishah with the same narration.</td>
<td valign="top"><strong>mishkat 3129</strong>&nbsp; 0.7538<br><br>‘A’isha said that the Prophet married her when she was seven, she was brought to live with him when she was nine bringing her toys with her, and he di</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8283<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
<td valign="top"><strong>abudawud 4164</strong>&nbsp; 0.8521 <small>· Da'if</small><br><br>Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing wi</td>
<td valign="top"><strong>bukhari 4401</strong>&nbsp; 0.8730<br><br>Narrated `Aisha: (the wife of the Prophet) Safiya bin Huyai, the wife of the Prophet menstruated during Hajjat-ul- Wada` The Prophet said, "Is she goi</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8362<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8199<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>bukhari 5212</strong>&nbsp; 5.3071 <small>· Sahih</small><br><br>Sauda bint Zam`a gave up her turn to me (`Aisha), and so the Prophet used to give me (`Aisha) both my day and the day of Sauda.</td>
<td valign="top"><strong>bukhari 277</strong>&nbsp; 0.8462<br><br>Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head</td>
<td valign="top"><strong>muslim 1422 d</strong>&nbsp; 0.7806<br><br>Narrated 'A'isha : 'A'isha (Allah be pleased with her) reported that Allah's Apostle (may peace be upon him) married her when she was six years old, a</td>
<td valign="top"><strong>adab 1000</strong>&nbsp; 0.9192 <small>· Sahih</small><br><br>See 993.</td>
<td valign="top"><strong>ibnmajah 3668</strong>&nbsp; 0.7705 <small>· Sahih</small><br><br>It was narrated that Sa'sa'ah the paternal uncle of Ahnaf, said: "A woman entered upon Aisha with her two daughters, and she gave her three dates. (Th</td>
<td valign="top"><strong>adab 585</strong>&nbsp; 0.7490<br><br>(As hadith above)</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7499 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>muslim 1422 b</strong>&nbsp; 0.7459<br><br>'A'isha (Allah be pleased with her) reported: Allah's Apostle (may peace be upon him) married me when I was six years old, and I was admitted to his h</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8267<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>bukhari 277</strong>&nbsp; 0.8516<br><br>Narrated Aisha: Whenever any one of us was Junub, she poured water over her head thrice with both her hands and then rubbed the right side of her head</td>
<td valign="top"><strong>bukhari 2688</strong>&nbsp; 0.8684<br><br>Narrated Aisha: Whenever Allah's Apostle intended to go on a journey, he used to draw lots among his wives and would take with him the one on whom the</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8250<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8177 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>muslim 2046 b</strong>&nbsp; 5.3001 <small>· Sahih</small><br><br>'A'isha a family which has no dates (in their house) its members will be hungry; (or) 'A'isha the family which has no dates its members may be hungry.</td>
<td valign="top"><strong>abudawud 4164</strong>&nbsp; 0.8448 <small>· Da'if</small><br><br>Narrated Aisha, Ummul Mu'minin: Karimah, daughter of Hammam, told that a woman came to Aisha (Allah be pleased with her) and asked her about dyeing wi</td>
<td valign="top"><strong>muslim 332 b</strong>&nbsp; 0.7782<br><br>'A'isha reported: A woman asked the Apostle of Allah (may peace be upon him) how he should wash herself after the menstrual period. He (the Holy Proph</td>
<td valign="top"><strong>adab 1111</strong>&nbsp; 0.9184<br><br>See 1103.</td>
<td valign="top"><strong>nasai 761</strong>&nbsp; 0.7675 <small>· Sahih</small><br><br>It was narrated that Aisha said: "In my house there was a cloth on which there were images, which I covered a closet which is in the house, and the Me</td>
<td valign="top"><strong>adab 586</strong>&nbsp; 0.7490<br><br>(As hadith above)</td>
<td valign="top"><strong>riyadussalihin 1643</strong>&nbsp; 0.7435<br><br>A similar narration was narrated on the authority of 'Aishah.</td>
<td valign="top"><strong>muslim 1422 d</strong>&nbsp; 0.7450<br><br>Narrated 'A'isha : 'A'isha (Allah be pleased with her) reported that Allah's Apostle (may peace be upon him) married her when she was six years old, a</td>
<td valign="top"><strong>bukhari 5419</strong>&nbsp; 0.8244<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other women is like the superiority of Tharid to other kinds of food . "</td>
<td valign="top"><strong>bukhari 3894</strong>&nbsp; 0.8495<br><br>Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then </td>
<td valign="top"><strong>bukhari 2593</strong>&nbsp; 0.8684<br><br>Narrated Aisha: Whenever Allah's Apostle wanted to go on a journey, he would draw lots as to which of his wives would accompany him. He would take her</td>
<td valign="top"><strong>bukhari 3411</strong>&nbsp; 0.8232<br><br>Narrated Abu Musa: Allah's Apostle said, "Many amongst men reached (the level of) perfection but none amongst the women reached this level except Asia</td>
<td valign="top"><strong>bukhari 5419</strong>&nbsp; 0.8169<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other women is like the superiority of Tharid to other kinds of food . "</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bulugh 1059</strong>&nbsp; 5.2994 <small>· Uncategorized</small><br><br>Sauda (RA) daughter of Zam'ah gave away her day to 'Aishah (RA). So the Prophet (SAW) allotted a share to 'Aishah (RA) of her day and Sauda's. [Agreed</td>
<td valign="top"><strong>bukhari 1151</strong>&nbsp; 0.8426<br><br>Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I sai</td>
<td valign="top"><strong>adab 851</strong>&nbsp; 0.7763 <small>· Sahih</small><br><br>'A'isha said, "Prophet of Allah, will you not give me a kunya?" He said, "Use the kunya of your son," i.e. 'Abdullah ibn az-Zubayr. She was given the </td>
<td valign="top"><strong>adab 998</strong>&nbsp; 0.9154 <small>· Sahih</small><br><br>See 996.</td>
<td valign="top"><strong>nasai 2911</strong>&nbsp; 0.7618 <small>· Sahih</small><br><br>Aisha said: "I said: 'O Messenger of Allah! Can I not enter the House?' He said: 'Enter the Hijr for it is part of the House.'"</td>
<td valign="top"><strong>forty 17</strong>&nbsp; 0.7412<br><br>Richness lies in the richness of the soul.</td>
<td valign="top"><strong>shamail 389</strong>&nbsp; 0.7374 <small>· Hasan</small><br><br>'A’isha said: "No more will I envy anyone for an easy death now that I have seen how the Messenger of Allah (Allah bless him and give him peace) suffe</td>
<td valign="top"><strong>bukhari 1389</strong>&nbsp; 0.7362<br><br>Narrated `Aisha: During his sickness, Allah's Apostle was asking repeatedly, "Where am I today? Where will I be tomorrow?" And I was waiting for the d</td>
<td valign="top"><strong>bukhari 3411</strong>&nbsp; 0.8140<br><br>Narrated Abu Musa: Allah's Apostle said, "Many amongst men reached (the level of) perfection but none amongst the women reached this level except Asia</td>
<td valign="top"><strong>abudawud 1497</strong>&nbsp; 0.8494 <small>· Da'if</small><br><br>Narrated Aisha, Ummul Mu'minin: Ata' said: The quilt of Aisha was stolen. She began to curse the person who had stolen it. The Prophet (saws) began to</td>
<td valign="top"><strong>bukhari 2029</strong>&nbsp; 0.8676<br><br>Narrated `Aisha: (the wife of the Prophet) Allah's Apostle used to let his head in (the house) while he was in the mosque and I would comb and oil his</td>
<td valign="top"><strong>bukhari 5419</strong>&nbsp; 0.8216<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other women is like the superiority of Tharid to other kinds of food . "</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8166<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>nasai 3213</strong>&nbsp; 5.2966 <small>· Sahih</small><br><br>It was narrated from 'Aishah that the Messenger of Allah forbade celibacy.</td>
<td valign="top"><strong>bukhari 902</strong>&nbsp; 0.8424<br><br>Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of f</td>
<td valign="top"><strong>adab 947</strong>&nbsp; 0.7761 <small>· Sahih</small><br><br>'A'isha, the Umm al-Mu'minin, said, "I have not seen anyone who more resembled the Prophet, may Allah bless him and grant him peace, in words or speec</td>
<td valign="top"><strong>adab 999</strong>&nbsp; 0.9154 <small>· Sahih</small><br><br>See 996.</td>
<td valign="top"><strong>tirmidhi 1996</strong>&nbsp; 0.7565 <small>· Sahih</small><br><br>Aisha narrated: "A man sought permission to enter upon the Messenger of Allah while I was with him, so he said: 'What an evil son of his tribe, or bro</td>
<td valign="top"><strong>forty 2</strong>&nbsp; 0.7404<br><br>War is deception.</td>
<td valign="top"><strong>bukhari 5923</strong>&nbsp; 0.7369<br><br>Narrated `Aisha: I used to perfume Allah's Apostle with the best scent available till I saw the shine of the scent on his head and shine beard.</td>
<td valign="top"><strong>forty 17</strong>&nbsp; 0.7351<br><br>Richness lies in the richness of the soul.</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8130<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
<td valign="top"><strong>bukhari 1151</strong>&nbsp; 0.8494<br><br>Narrated 'Aisha: A woman from the tribe of Bani Asad was sitting with me and Allah's Apostle (p.b.u.h) came to my house and said, "Who is this?" I sai</td>
<td valign="top"><strong>bukhari 1289</strong>&nbsp; 0.8675<br><br>Narrated `Aisha: (the wife of the Prophet) Once Allah's Apostle passed by (the grave of) a Jewess whose relatives were weeping over her. He said, "The</td>
<td valign="top"><strong>bukhari 6249</strong>&nbsp; 0.8157<br><br>Narrated `Aisha: Allah's Apostle said, "O `Aisha! This is Gabriel sending his greetings to you." I said, "Peace, and Allah's Mercy be on him (Gabriel)</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8130<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>muslim 2445</strong>&nbsp; 5.2936 <small>· Sahih</small><br><br>'A'isha reported that when Allah's Messenger (may peace be upon him) set ont on a journey, he used to cast lots amongst his wives. Once this lot came </td>
<td valign="top"><strong>bukhari 4573</strong>&nbsp; 0.8419<br><br>Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of </td>
<td valign="top"><strong>adab 280</strong>&nbsp; 0.7742 <small>· Sahih</small><br><br>'Abdullah ibn az-Zubayr said, "I have never seen two women more generous than 'A'isha and Asma'. Their generosity was different. 'A'isha used to gathe</td>
<td valign="top"><strong>adab 796</strong>&nbsp; 0.9143 <small>· Sahih</small><br><br>See 772.</td>
<td valign="top"><strong>tirmidhi 3884</strong>&nbsp; 0.7503 <small>· Da'if</small><br><br>Narrated Musa bin Talhah: "I have not seen anyone clearer (in speech) than 'Aishah."</td>
<td valign="top"><strong>bukhari 1444</strong>&nbsp; 0.7396<br><br>See previous hadith.</td>
<td valign="top"><strong>bulugh 1006</strong>&nbsp; 0.7364<br><br>Muslim has from 'Aishah (RA): "Her husband was a slave."</td>
<td valign="top"><strong>nasai 3379</strong>&nbsp; 0.7351 <small>· hasan</small><br><br>It was narrated that 'Aishah said: "The Messenger of Allah married me when I was six, and consummated the marriage with me when I was nine."</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8112 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
<td valign="top"><strong>bukhari 4573</strong>&nbsp; 0.8485<br><br>Narrated Aisha: There was an orphan (girl) under the care of a man. He married her and she owned a date palm (garden). He married her just because of </td>
<td valign="top"><strong>bukhari 1539</strong>&nbsp; 0.8672<br><br>Narrated `Aisha: (the wife of the Prophet (p.b.u.h) I used to scent Allah's Apostle when he wanted to assume Ihram and also on finishing Ihram before </td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8151 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
<td valign="top"><strong>bukhari 3411</strong>&nbsp; 0.8091<br><br>Narrated Abu Musa: Allah's Apostle said, "Many amongst men reached (the level of) perfection but none amongst the women reached this level except Asia</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>bukhari 5325, 5326</strong>&nbsp; 5.2910 <small>· Sahih</small><br><br>Urwa said to Aisha, "Do you know so-and-so, the daughter of Al-Hakam? Her husband divorced her irrevocably and she left (her husband's house)." `Aisha</td>
<td valign="top"><strong>bukhari 43</strong>&nbsp; 0.8417<br><br>Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her</td>
<td valign="top"><strong>muslim 1211 ac</strong>&nbsp; 0.7736<br><br>Abd al-Rahman b. al Qasim narrated on the authority of 'A'isha (Allah be pleased with her) that she made a mention to Allah's Messenger (may peace be </td>
<td valign="top"><strong>adab 1127</strong>&nbsp; 0.9122 <small>· Hasan</small><br><br>See 1122.</td>
<td valign="top"><strong>tirmidhi 3889</strong>&nbsp; 0.7483 <small>· Sahih</small><br><br>Narrated 'Ammar bin Yasir: "She is his wife in the world and in the Hereafter." - meaning: 'Aishah [may Allah be pleased with her].</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7359 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>muslim 1092 d</strong>&nbsp; 0.7357<br><br>A hadith like this has been transmitted on the authority of 'A'isha (Allah be pleased with her).</td>
<td valign="top"><strong>adab 585</strong>&nbsp; 0.7343<br><br>(As hadith above)</td>
<td valign="top"><strong>bukhari 3768</strong>&nbsp; 0.8094<br><br>Narrated Abu Salama: `Aisha said, "Once Allah's Apostle said (to me), 'O Aish (`Aisha)! This is Gabriel greeting you.' I said, 'Peace and Allah's Merc</td>
<td valign="top"><strong>bukhari 902</strong>&nbsp; 0.8474<br><br>Narrated Aisha: (the wife of the Prophet) The people used to come from their abodes and from Al-`Awali (i.e. outskirts of Medina up to a distance of f</td>
<td valign="top"><strong>bukhari 2026</strong>&nbsp; 0.8670<br><br>Narrated `Aisha: (the wife of the Prophet) The Prophet used to practice I`tikaf in the last ten days of Ramadan till he died and then his wives used t</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8103<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
<td valign="top"><strong>bukhari 4691</strong>&nbsp; 0.8034<br><br>Narrated Um Ruman: Who was `Aisha's mother: While I was with `Aisha, `Aisha got fever, whereupon the Prophet said, "Probably her fever is caused by th</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>abudawud 1280</strong>&nbsp; 5.2892 <small>· Da'if</small><br><br>Dhakwan, the client of Aisha, reported on the authority of Aisha: The Messenger of Allah (saws) used to pray after the afternoon prayer but prohibited</td>
<td valign="top"><strong>abudawud 288</strong>&nbsp; 0.8400 <small>· Sahih</small><br><br>'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, </td>
<td valign="top"><strong>muslim 785 b</strong>&nbsp; 0.7734<br><br>'A'isha said: The Messenger of Allah (may peace be upon him) came to me when a woman was sitting with me. He said: Who is she? I said: She is a woman </td>
<td valign="top"><strong>adab 1249</strong>&nbsp; 0.9115 <small>· Da'if</small><br><br>See 1245.</td>
<td valign="top"><strong>bulugh 1124</strong>&nbsp; 0.7474<br><br>The aforesaid Hadith is also a part of 'Aishah's Hadith in the course of a story.</td>
<td valign="top"><strong>riyadussalihin 1643</strong>&nbsp; 0.7348<br><br>A similar narration was narrated on the authority of 'Aishah.</td>
<td valign="top"><strong>muslim 1422 b</strong>&nbsp; 0.7334<br><br>'A'isha (Allah be pleased with her) reported: Allah's Apostle (may peace be upon him) married me when I was six years old, and I was admitted to his h</td>
<td valign="top"><strong>adab 586</strong>&nbsp; 0.7343<br><br>(As hadith above)</td>
<td valign="top"><strong>bukhari 3771</strong>&nbsp; 0.8082<br><br>Narrated Al-Qasim bin Muhammad: Once `Aisha became sick and Ibn `Abbas went to see her and said, "O mother of the believers! You are leaving for truth</td>
<td valign="top"><strong>bukhari 4750</strong>&nbsp; 0.8463<br><br>Narrated Aisha: (The wife of the Prophet) Whenever Allah's Apostle intended to go on a journey, he used to draw lots among his wives and would take wi</td>
<td valign="top"><strong>bukhari 3894</strong>&nbsp; 0.8662<br><br>Narrated Aisha: The Prophet engaged me when I was a girl of six (years). We went to Medina and stayed at the home of Bani-al-Harith bin Khazraj. Then </td>
<td valign="top"><strong>bukhari 4691</strong>&nbsp; 0.8096<br><br>Narrated Um Ruman: Who was `Aisha's mother: While I was with `Aisha, `Aisha got fever, whereupon the Prophet said, "Probably her fever is caused by th</td>
<td valign="top"><strong>bukhari 5158</strong>&nbsp; 0.7976<br><br>Narrated 'Urwa: The Prophet wrote the (marriage contract) with `Aisha while she was six years old and consummated his marriage with her while she was </td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>ibnmajah 1469</strong>&nbsp; 5.2892 <small>· Sahih</small><br><br>“They used to claim that he was shrouded in Hibarah.” ‘Aishah said: “They brought a Hibarah Burd, but they did not shroud him in it.”</td>
<td valign="top"><strong>abudawud 3708</strong>&nbsp; 0.8388 <small>· Da'if in chain</small><br><br>Narrated Aisha, Ummul Mu'minin: Safiyyah, daughter of Atiyyah, said: I entered upon Aisha with some women of AbdulQays, and asked her about mixing dri</td>
<td valign="top"><strong>bulugh 1103</strong>&nbsp; 0.7730<br><br>Narrated al-Miswar bin Makhramah (RA): Some nights after her husband's death, Subai'ah al-Aslamiyah (RA) gave birth to a child. Then she went to the P</td>
<td valign="top"><strong>adab 585</strong>&nbsp; 0.9081<br><br>(As hadith above)</td>
<td valign="top"><strong>tirmidhi 580</strong>&nbsp; 0.7454 <small>· Da'if</small><br><br>Aisha narrated: "When the Messenger of Allah would prostrate (for recitation of) the Qur'an, he would say: (Sajada wajhiya lilladhi khalaqahu wa shaqq</td>
<td valign="top"><strong>mishkat 3129</strong>&nbsp; 0.7278<br><br>‘A’isha said that the Prophet married her when she was seven, she was brought to live with him when she was nine bringing her toys with her, and he di</td>
<td valign="top"><strong>bukhari 5918</strong>&nbsp; 0.7333<br><br>Narrated `Aisha: As if I am now looking at the shine of the hair parting of the Prophet while he was in the state of lhram.</td>
<td valign="top"><strong>tirmidhi 1179</strong>&nbsp; 0.7330 <small>· Sahih</small><br><br>Aishah said: "The Messenger of Allah gave us the choice, so we chose him. So was that a divorce?"</td>
<td valign="top"><strong>bukhari 3388</strong>&nbsp; 0.8052<br><br>Narrated Masruq: I asked Um Ruman, `Aisha's mother about the accusation forged against `Aisha. She said, "While I was sitting with `Aisha, an Ansari w</td>
<td valign="top"><strong>abudawud 288</strong>&nbsp; 0.8457 <small>· Sahih</small><br><br>'Aishah, wife of Prophet (saws), said: Umm Habibah, daughter of Jahsh, sister-in-law of Messenger of Allah (saws) and wife of 'Abd al-Rahman b. 'Awf, </td>
<td valign="top"><strong>bukhari 4442</strong>&nbsp; 0.8661<br><br>Narrated Aisha: (the wife of the Prophet) "When the ailment of Allah's Apostle became aggravated, he requested his wives to permit him to be (treated)</td>
<td valign="top"><strong>bukhari 251</strong>&nbsp; 0.8078<br><br>Narrated Abu Salama: `Aisha's brother and I went to `Aisha and he asked her about the bath of the Prophet. She brought a pot containing about a Sa` of</td>
<td valign="top"><strong>bukhari 4428</strong>&nbsp; 0.7966<br><br>Narrated `Aisha: The Prophet in his ailment in which he died, used to say, "O `Aisha! I still feel the pain caused by the food I ate at Khaibar, and a</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bukhari 6201</strong>&nbsp; 5.2867 <small>· Sahih</small><br><br>(the wife the Prophet) Allah's Apostle said, "O Aisha! This is Gabriel sending his greetings to you." I said, "Peace, and Allah's Mercy be on him." `A</td>
<td valign="top"><strong>bukhari 5160</strong>&nbsp; 0.8383<br><br>Narrated Aisha: When the Prophet married me, my mother came to me and made me enter the house (of the Prophet) and nothing surprised me but the coming</td>
<td valign="top"><strong>muslim 334 f</strong>&nbsp; 0.7729<br><br>'A'isha, the wife of the Apostle (may peace be upon him), said: Umm Habiba b. Jahsh who was the spouse of Abd al- Rahman b. Auf made a complaint to th</td>
<td valign="top"><strong>adab 586</strong>&nbsp; 0.9081<br><br>(As hadith above)</td>
<td valign="top"><strong>riyadussalihin 1643</strong>&nbsp; 0.7451<br><br>A similar narration was narrated on the authority of 'Aishah.</td>
<td valign="top"><strong>shamail 389</strong>&nbsp; 0.7277 <small>· Hasan</small><br><br>'A’isha said: "No more will I envy anyone for an easy death now that I have seen how the Messenger of Allah (Allah bless him and give him peace) suffe</td>
<td valign="top"><strong>adab 585</strong>&nbsp; 0.7328<br><br>(As hadith above)</td>
<td valign="top"><strong>abudawud 2121</strong>&nbsp; 0.7323 <small>· Sahih</small><br><br>Narrated 'Aishah: The Messenger of Allah (saws) married me when I was seven years old. The narrator Sulaiman said: or Six years. He had intercourse wi</td>
<td valign="top"><strong>bukhari 3770</strong>&nbsp; 0.8047<br><br>Narrated Anas bin Malik: Allah's Apostle said, "The superiority of `Aisha over other women is like the superiority of Tharid to other meals."</td>
<td valign="top"><strong>bukhari 43</strong>&nbsp; 0.8455<br><br>Narrated 'Aisha: Once the Prophet came while a woman was sitting with me. He said, "Who is she?" I replied, "She is so and so," and told him about her</td>
<td valign="top"><strong>bukhari 5995</strong>&nbsp; 0.8656<br><br>Narrated `Aisha: (the wife of the Prophet) A lady along with her two daughters came to me asking me (for some alms), but she found nothing with me exc</td>
<td valign="top"><strong>bukhari 6201</strong>&nbsp; 0.8076<br><br>Narrated `Aisha: (the wife the Prophet) Allah's Apostle said, "O Aisha! This is Gabriel sending his greetings to you." I said, "Peace, and Allah's Mer</td>
<td valign="top"><strong>bukhari 3770</strong>&nbsp; 0.7950<br><br>Narrated Anas bin Malik: Allah's Apostle said, "The superiority of `Aisha over other women is like the superiority of Tharid to other meals."</td>
</tr>
</tbody></table>

---

## hadithText: fasting expiation sins

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 10ms |
| mxbai-embed-large | 43ms | 84ms |
| nomic-embed-text | 35ms | 82ms |
| snowflake-arctic-embed:m | 36ms | 82ms |
| all-MiniLM-L6-v2 | 31ms | 84ms |
| embeddinggemma-300m | 59ms | 82ms |
| embeddinggemma-300m-qat-q8 | 63ms | 82ms |
| embeddinggemma-300m-qat-q4 | 94ms | 82ms |
| mxbai-embed-xsmall-v1 | 12ms | 80ms |
| mxbai-embed-large (Q4_K_M) | 44ms | 84ms |
| mxbai-embed-large (INT8 ONNX) | 50ms | 82ms |
| mxbai-embed-xsmall (INT8 ONNX) | 2ms | 82ms |
| mxbai-embed-xsmall (INT4 ONNX) | 6ms | 81ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M)</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX)</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX)</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX)</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 19.7723 <small>· Sahih</small><br><br>“Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previous year.”</td>
<td valign="top"><strong>mishkat 1965</strong>&nbsp; 0.8632<br><br>Salman al-Farisi told of God’s messenger saying in a sermon which he delivered to them on the last day of Sha'ban, “A great month, a blessed month, a </td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8885<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>forty 28</strong>&nbsp; 0.8478<br><br>One who repents from sin is like someone without sin.</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8327<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.7998 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.7902<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.7860 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8351<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8598<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8890<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8310<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8379 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 19.3202 <small>· Sahih</small><br><br>“Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of the year before and the year after.”</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8581<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>riyadussalihin 1250</strong>&nbsp; 0.8806<br><br>Abu Qatadah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) was asked about the observance of Saum (fasting) on the day of 'Ar</td>
<td valign="top"><strong>forty 10</strong>&nbsp; 0.8202<br><br>The word of the believer is like seizing of the hand.</td>
<td valign="top"><strong>bulugh 441</strong>&nbsp; 0.8065<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said: "The best of my followers are those who, having done evil, ask for forgiveness (from Allah); and wh</td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.7971 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.7846 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>ibnmajah 1086</strong>&nbsp; 0.7858 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “From one Friday to the next is an expiation for whatever was committed in b</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8257 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8581<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>mishkat 1959</strong>&nbsp; 0.8846<br><br>He reported God’s messenger as saying, "Every [good] deed a son of Adam does will be multiplied, a good deed receiving a tenfold to seven hundredfold </td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8236 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8206 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 19.2294 <small>· Uncategorized</small><br><br>The five daily (prescribed) Salat, and Friday (prayer) to the next Friday (prayer), and the fasting of Ramadan to the next Ramadan, is expiation of th</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8580<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>bukhari 1904</strong>&nbsp; 0.8792<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah said, 'All the deeds of Adam's sons (people) are for them, except fasting which is for Me, and I wi</td>
<td valign="top"><strong>nasai 2209</strong>&nbsp; 0.8189<br><br>A similar report was narrated from Abu Salamah and he said: "Whoever fasts it and spends its nights in prayer out of faith and in the hope of reward."</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.7911 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.7933 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7844<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.7803<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8102 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.8575<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8845<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8092 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8205<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>riyadussalihin 1250</strong>&nbsp; 19.1035 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) was asked about the observance of Saum (fasting) on the day of 'Arafah. He said, "It is an expiation for the sins of the</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.8551<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8777 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>bulugh 252</strong>&nbsp; 0.8181<br><br>Muslim added: "and Christians."</td>
<td valign="top"><strong>ibnmajah 428</strong>&nbsp; 0.7759 <small>· Hasan</small><br><br>It was narrated from Abu Hurairah that: The Prophet said: "Sins are expiated by well-performed ablution despite difficulties, increasing the number of</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.7891<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.7794 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.7785 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
<td valign="top"><strong>bulugh 441</strong>&nbsp; 0.7972<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said: "The best of my followers are those who, having done evil, ask for forgiveness (from Allah); and wh</td>
<td valign="top"><strong>bukhari 1904</strong>&nbsp; 0.8551<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah said, 'All the deeds of Adam's sons (people) are for them, except fasting which is for Me, and I wi</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8831<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>ibnmajah 428</strong>&nbsp; 0.7998 <small>· Hasan</small><br><br>It was narrated from Abu Hurairah that: The Prophet said: "Sins are expiated by well-performed ablution despite difficulties, increasing the number of</td>
<td valign="top"><strong>bulugh 441</strong>&nbsp; 0.8094<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said: "The best of my followers are those who, having done evil, ask for forgiveness (from Allah); and wh</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>riyadussalihin 1252</strong>&nbsp; 18.9781 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) was asked about observing As-Saum (the fast) on the tenth day of Muharram, and he replied, "It is an expiation for the s</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8516<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.8748<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>shamail 304</strong>&nbsp; 0.8154 <small>· Sahih Isnād</small><br><br>'A’isha said: "The Prophet (Allah bless him and give him peace) was devoutly committed to fasting every Monday and Thursday.”</td>
<td valign="top"><strong>muslim 1102 a</strong>&nbsp; 0.7716<br><br>Ibn 'Umar (Allah be pleased with both of them) said that the Apostle of Allah (may peace be upon him) forbade uninterrupted fasting. They (some of the</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7888<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.7789 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.7736 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.7953<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>abudawud 2380</strong>&nbsp; 0.8527 <small>· Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: if one has a sudden attack of vomiting while one is fasting, no atonement is required of him, but if he</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.8830<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.7972<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8072 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 18.0183 <small>· Sahih</small><br><br>The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward for it; and the smell wh</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8515<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8734<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>tirmidhi 84</strong>&nbsp; 0.8153 <small>· Hasan</small><br><br>Busrah narrated that : the Prophet said a similar Hadith</td>
<td valign="top"><strong>tirmidhi 764</strong>&nbsp; 0.7710 <small>· Sahih</small><br><br>Abu Hurairah narrated that: The Messenger of Allah said: "Indeed your Lord said: 'Every good deed is rewarded with ten of the same up to seven hundred</td>
<td valign="top"><strong>nasai 2204</strong>&nbsp; 0.7878 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.7727<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7711<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.7944 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8527<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8824<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7962<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8056<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>muslim 1162 b</strong>&nbsp; 15.3458 <small>· Sahih</small><br><br>Abu Qatada al-Ansari (Allah be pleased with him) reported that the Messenger of Allah (may peace be upon him) was asked about his fasting. The Messeng</td>
<td valign="top"><strong>bukhari 1904</strong>&nbsp; 0.8511<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah said, 'All the deeds of Adam's sons (people) are for them, except fasting which is for Me, and I wi</td>
<td valign="top"><strong>nasai 2205</strong>&nbsp; 0.8721 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>bulugh 68</strong>&nbsp; 0.8145<br><br>Al-Bukhari’s version adds: “Then perform ablution for every prayer”.</td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.7701<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
<td valign="top"><strong>nasai 2205</strong>&nbsp; 0.7875 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>nasai 2204</strong>&nbsp; 0.7710 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.7679<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7891<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8502<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>abudawud 1372</strong>&nbsp; 0.8815 <small>· Sahih</small><br><br>Narrated Abu Hurairah: The Prophet (saws) as saying: If anyone fasts during Ramadan because of faith and in order to seek his reward from Allah, his p</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.7929<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.8039<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>bulugh 680</strong>&nbsp; 14.3741 <small>· Uncategorized</small><br><br>Abu Qatadah Al-Ansari (RAA) narrated, ‘The Messenger of Allah (P.B.U.H.) was asked about fasting on the day of Arafah (the 9th of the month of Dhul Hi</td>
<td valign="top"><strong>abudawud 2380</strong>&nbsp; 0.8487 <small>· Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: if one has a sudden attack of vomiting while one is fasting, no atonement is required of him, but if he</td>
<td valign="top"><strong>nasai 2204</strong>&nbsp; 0.8721 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8133<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.7686<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
<td valign="top"><strong>ibnmajah 1086</strong>&nbsp; 0.7862 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “From one Friday to the next is an expiation for whatever was committed in b</td>
<td valign="top"><strong>bukhari 1901</strong>&nbsp; 0.7707<br><br>Narrated Abu Huraira: The Prophet said, "Whoever established prayers on the night of Qadr out of sincere faith and hoping for a reward from Allah, the</td>
<td valign="top"><strong>abudawud 1372</strong>&nbsp; 0.7676 <small>· Sahih</small><br><br>Narrated Abu Hurairah: The Prophet (saws) as saying: If anyone fasts during Ramadan because of faith and in order to seek his reward from Allah, his p</td>
<td valign="top"><strong>ibnmajah 428</strong>&nbsp; 0.7885 <small>· Hasan</small><br><br>It was narrated from Abu Hurairah that: The Prophet said: "Sins are expiated by well-performed ablution despite difficulties, increasing the number of</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.8495<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8782<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.7905 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.7954<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>tirmidhi 3549</strong>&nbsp; 14.0407 <small>· Uncategorized</small><br><br>“Ishaq bin Mansur narrated to us, from Isra’il” with this (Another chain) Bilal narrated that the Messenger of Allah (saws) said: “Hold fast to Qiyam </td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8476<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.8683<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>nasai 2341</strong>&nbsp; 0.8131<br><br>Something similar was narrated from 'Aishah and Hafsah: "There is no fast except for one who intends to fast before dawn." (Daif)</td>
<td valign="top"><strong>nasai 2303</strong>&nbsp; 0.7665 <small>· Sahih</small><br><br>It was narrated from Hamzah bin 'Amr that he said to the Messenger of Allah: "I feel able to fast while traveling; is there any sin on me?" He said: "</td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.7828<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>nasai 2205</strong>&nbsp; 0.7699 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.7674<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.7846<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
<td valign="top"><strong>abudawud 1372</strong>&nbsp; 0.8493 <small>· Sahih</small><br><br>Narrated Abu Hurairah: The Prophet (saws) as saying: If anyone fasts during Ramadan because of faith and in order to seek his reward from Allah, his p</td>
<td valign="top"><strong>bukhari 1904</strong>&nbsp; 0.8780<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah said, 'All the deeds of Adam's sons (people) are for them, except fasting which is for Me, and I wi</td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.7871<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
<td valign="top"><strong>abudawud 2316</strong>&nbsp; 0.7950 <small>· Hasan</small><br><br>Ibn ‘Abbas explain the Qur’anic verse “For those who can do it(with hardship) is a ransom, the feeding of one, that is indigent” said “If one of them </td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bukhari 415</strong>&nbsp; 13.7088 <small>· Sahih</small><br><br>The Prophet said, "Spitting in the mosque is a sin and its expiation is to bury it."</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.8456<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
<td valign="top"><strong>ibnmajah 1638</strong>&nbsp; 0.8659 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “Every good deed of the son of Adam will be multiplied manifold. A good deed</td>
<td valign="top"><strong>forty 17</strong>&nbsp; 0.8130<br><br>Richness lies in the richness of the soul.</td>
<td valign="top"><strong>nasai 2403</strong>&nbsp; 0.7633 <small>· Sahih</small><br><br>'Abdullah bin Amr said: "The Messenger of Allah said to me: 'Fast one day of the month and you will have the reward of what is left.' I said: 'I am ab</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.7775 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>ibnmajah 1086</strong>&nbsp; 0.7682 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “From one Friday to the next is an expiation for whatever was committed in b</td>
<td valign="top"><strong>bukhari 1901</strong>&nbsp; 0.7644<br><br>Narrated Abu Huraira: The Prophet said, "Whoever established prayers on the night of Qadr out of sincere faith and hoping for a reward from Allah, the</td>
<td valign="top"><strong>abudawud 2316</strong>&nbsp; 0.7802 <small>· Hasan</small><br><br>Ibn ‘Abbas explain the Qur’anic verse “For those who can do it(with hardship) is a ransom, the feeding of one, that is indigent” said “If one of them </td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8491<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bukhari 7492</strong>&nbsp; 0.8773<br><br>Narrated Abu Huraira: The Prophet said, "Allah said: The Fast is for Me and I will give the reward for it, as he (the one who observes the fast) leave</td>
<td valign="top"><strong>bulugh 441</strong>&nbsp; 0.7860<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said: "The best of my followers are those who, having done evil, ask for forgiveness (from Allah); and wh</td>
<td valign="top"><strong>ibnmajah 1731</strong>&nbsp; 0.7948 <small>· Da’if</small><br><br>It was narrated that Qatadah bin Nu’man said: “I heard the Messenger of Allah (saw) say: ‘Whoever fasts the Day of ‘Arafah, his sins of the previous a</td>
</tr>
</tbody></table>

---

## hadithText: neighbor rights

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 8ms |
| mxbai-embed-large | 43ms | 86ms |
| nomic-embed-text | 35ms | 82ms |
| snowflake-arctic-embed:m | 38ms | 81ms |
| all-MiniLM-L6-v2 | 36ms | 82ms |
| embeddinggemma-300m | 70ms | 81ms |
| embeddinggemma-300m-qat-q8 | 69ms | 83ms |
| embeddinggemma-300m-qat-q4 | 71ms | 82ms |
| mxbai-embed-xsmall-v1 | 9ms | 81ms |
| mxbai-embed-large (Q4_K_M) | 54ms | 83ms |
| mxbai-embed-large (INT8 ONNX) | 19ms | 80ms |
| mxbai-embed-xsmall (INT8 ONNX) | 2ms | 83ms |
| mxbai-embed-xsmall (INT4 ONNX) | 2ms | 83ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M)</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX)</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX)</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX)</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 14.2937 <small>· Da'if</small><br><br>“The neighbor has more right to preemption of his neighbor, so let him wait for him even if he is absent, if they share a path.”</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8379 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8859 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>forty 33</strong>&nbsp; 0.8244<br><br>Actions are through intentions.</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8529<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7756 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.7804 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.7852 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8567<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8334 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8715 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8545<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8483<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 13.8410 <small>· Sahih</small><br><br>“I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has neighbors?' He said: 'The neighbor has more rig</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8378 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8767 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>forty 21</strong>&nbsp; 0.8243<br><br>A man will be with whom he loves.</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8329<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.7728 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7730 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7710 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8378<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8324 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8672 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8401<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8253<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 13.8410 <small>· Sahih</small><br><br>"O Messenger of Allah, not one else has any share in my land, but there are neighbors." He said: "The neighbor has more right to property that is near</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8326<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8746<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>bulugh 252</strong>&nbsp; 0.8221<br><br>Muslim added: "and Christians."</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7936 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7669<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7625<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7667<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8102 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8259<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8657 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8046 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8013 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>nasai 4705</strong>&nbsp; 13.7818 <small>· Sahih</small><br><br>"The Messenger of Allah decreed the principle of pre-emption, and the (rights of) neighbors."</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8289 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8644 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>forty 2</strong>&nbsp; 0.8174<br><br>War is deception.</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7808 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7493 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7530 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.7616<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8008 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8217 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8577<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.7942 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.7992 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 13.6682 <small>· Hasan</small><br><br>that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>abudawud 3517</strong>&nbsp; 0.8224 <small>· Sahih</small><br><br>Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or land of the neighbour.</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.8575 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8163<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7759 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.7486<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.7517<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7611 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7942 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>abudawud 3517</strong>&nbsp; 0.8197 <small>· Sahih</small><br><br>Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or land of the neighbour.</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8558 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7865<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7879 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 13.5564 <small>· Uncategorized</small><br><br>"The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8212<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8519<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 164</strong>&nbsp; 0.8159<br><br>ash-Shafi'i views the second ruling from</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7725<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7433 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7482 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7564 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7901 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8139<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8552<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7849 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7874 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 13.5564 <small>· Sahih</small><br><br>“The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>abudawud 3513</strong>&nbsp; 0.8180 <small>· Sahih</small><br><br>Narrated Jabir: The Messenger of Allah (saws) as saying: There is the right of option regarding everything which is shared, whether a dwelling or a ga</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8462 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>tirmidhi 226</strong>&nbsp; 0.8151<br><br>Narrator not mentioned: A Similar narration</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7642 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7432 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7433 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7505 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7831 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>abudawud 3513</strong>&nbsp; 0.8130 <small>· Sahih</small><br><br>Narrated Jabir: The Messenger of Allah (saws) as saying: There is the right of option regarding everything which is shared, whether a dwelling or a ga</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8502 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7821 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7801 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>bukhari 6981</strong>&nbsp; 13.2157 <small>· Sahih</small><br><br>Abu Rafi` sold a house to Sa`d bin Malik for four-hundred Mithqal of gold, and said, "If I had not heard the Prophet saying, 'The neighbor has more ri</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8174 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8430 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>forty 37</strong>&nbsp; 0.8125<br><br>Poverty can almost turn into disbelief.</td>
<td valign="top"><strong>bulugh 902</strong>&nbsp; 0.7541<br><br>Narrated Anas bin Malik (RA): Allah's Messenger (SAW) said, "The neighbor of the house has the most right to buy it." [Reported by an-Nasa'i. Ibn Hibb</td>
<td valign="top"><strong>nasai 4705</strong>&nbsp; 0.7421 <small>· Sahih</small><br><br>It was narrated that Jabir said: "The Messenger of Allah decreed the principle of pre-emption, and the (rights of) neighbors."</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7395 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7470 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7828 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8123 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>adab 109</strong>&nbsp; 0.8475 <small>· Hasan</small><br><br>Al-Hasan was asked about the neighbour and said, "The term 'neighbour' includes the forty houses in front a person, the forty houses behind him, the f</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7803 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7787<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 6978</strong>&nbsp; 13.0867 <small>· Sahih</small><br><br>Abu Rafi' said that Sa'd offered him four hundred Mithqal of gold for a house. Abu Rafi ' said, "If I had not heard Allah's Apostle saying, 'A neighbo</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8159 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8414<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>forty 12</strong>&nbsp; 0.8124<br><br>He is not one of us who cheats us.</td>
<td valign="top"><strong>adab 121</strong>&nbsp; 0.7266 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A person whose neighbours are not safe from his evil</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7394 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4705</strong>&nbsp; 0.7355 <small>· Sahih</small><br><br>It was narrated that Jabir said: "The Messenger of Allah decreed the principle of pre-emption, and the (rights of) neighbors."</td>
<td valign="top"><strong>nasai 4705</strong>&nbsp; 0.7364 <small>· Sahih</small><br><br>It was narrated that Jabir said: "The Messenger of Allah decreed the principle of pre-emption, and the (rights of) neighbors."</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7792<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>adab 109</strong>&nbsp; 0.8114 <small>· Hasan</small><br><br>Al-Hasan was asked about the neighbour and said, "The term 'neighbour' includes the forty houses in front a person, the forty houses behind him, the f</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.8453 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7767 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7624 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 12.8224 <small>· Hasan</small><br><br>that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, when their paths</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8156<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>nasai 4705</strong>&nbsp; 0.8350 <small>· Sahih</small><br><br>It was narrated that Jabir said: "The Messenger of Allah decreed the principle of pre-emption, and the (rights of) neighbors."</td>
<td valign="top"><strong>bukhari 7126</strong>&nbsp; 0.8123<br><br>Narrated Abu Bakra: [as above]</td>
<td valign="top"><strong>adab 117</strong>&nbsp; 0.7215 <small>· Hasan</small><br><br>Abu Hurayra said, "Part of the supplication of the Prophet, may Allah bless him and grant him peace, was, "Oh Allah, I seek refuge with you from an ev</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7228 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7271 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>abudawud 3517</strong>&nbsp; 0.7329 <small>· Sahih</small><br><br>Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or land of the neighbour.</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7718 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>bukhari 6976</strong>&nbsp; 0.8105<br><br>Narrated Jabir bin `Abdullah: The Prophet has decreed that preemption is valid in all cases where the real estate concerned has not been divided, but </td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8405<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7698 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>abudawud 3518</strong>&nbsp; 0.7496 <small>· Sahih</small><br><br>Narrated Jabir ibn Abdullah: The Prophet (saws) said: The neighbour is most entitled to the right of pre-emption, and he should wait for its exercise </td>
</tr>
</tbody></table>

---

*Generated by `tests/small_model_comparison.py` · pool=50 · N=10*

# Small Model Comparison — englishMatn

Input: `englishMatn` (matn only, isnad stripped). Same production filters/boosts as hadithText.
Compare with hadithText section to see the effect of noisy isnad chains on retrieval.

**Filters & boosts**

| Setting | Status |
|---|---|
| `isChainRef` exclusion | **ON** — chain-reference hadiths excluded from results |
| Dedup by `dupGroup` | **ON** — highest collection-boosted member wins per group |
| Collection boosts | **ON** — bukhari 5×, muslim 4.8×, nawawi40 3.3×, malik/ahmad/riyadussalihin 2.5×, nasai 3.5×, abudawud 3×, tirmidhi 2.5×, ibnmajah/darimi/mishkat 2× |
| Embed times | Post-warmup — models loaded into memory before measurement |

| # | Model | Vec field | Dims | Size | Backend |
|---|---|---|---|---|---|
| 1 | mxbai-embed-large [matn] | `vec_mxbai_matn` | 1024-dim | 335M | Ollama |
| 2 | nomic-embed-text [matn] | `vec_nomic_matn` | 768-dim | 137M | Ollama |
| 3 | snowflake-arctic-embed:m [matn] | `vec_snowflake_matn` | 768-dim | 110M | Ollama |
| 4 | all-MiniLM-L6-v2 [matn] | `vec_miniLM_matn` | 384-dim | 22M | Ollama |
| 5 | embeddinggemma-300m [matn] | `vec_gemma_matn` | 768-dim | 300M | sentence_transformers |
| 6 | embeddinggemma-300m-qat-q8 [matn] | `vec_gemma_q8_matn` | 768-dim | 300M | sentence_transformers |
| 7 | embeddinggemma-300m-qat-q4 [matn] | `vec_gemma_q4_matn` | 768-dim | 300M | sentence_transformers |
| 8 | mxbai-embed-xsmall-v1 [matn] | `vec_mxbai_xs_matn` | 384-dim | 33M | sentence_transformers |
| 9 | mxbai-embed-large (Q4_K_M) [matn] | `vec_mxbai_q4km_matn` | 1024-dim | 335M | Ollama |
| 10 | mxbai-embed-large (INT8 ONNX) [matn] | `vec_mxbai_q_matn` | 1024-dim | 335M | ONNX Runtime |
| 11 | mxbai-embed-xsmall (INT8 ONNX) [matn] | `vec_mxbai_xs_q8_matn` | 384-dim | 33M | ONNX Runtime |
| 12 | mxbai-embed-xsmall (INT4 ONNX) [matn] | `vec_mxbai_xs_q4_matn` | 384-dim | 33M | ONNX Runtime |

---

## englishMatn: good character and manners

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 15ms |
| mxbai-embed-large [matn] | 38ms | 105ms |
| nomic-embed-text [matn] | 21ms | 86ms |
| snowflake-arctic-embed:m [matn] | 25ms | 84ms |
| all-MiniLM-L6-v2 [matn] | 29ms | 105ms |
| embeddinggemma-300m [matn] | 98ms | 82ms |
| embeddinggemma-300m-qat-q8 [matn] | 64ms | 82ms |
| embeddinggemma-300m-qat-q4 [matn] | 64ms | 81ms |
| mxbai-embed-xsmall-v1 [matn] | 16ms | 83ms |
| mxbai-embed-large (Q4_K_M) [matn] | 42ms | 110ms |
| mxbai-embed-large (INT8 ONNX) [matn] | 26ms | 83ms |
| mxbai-embed-xsmall (INT8 ONNX) [matn] | 2ms | 85ms |
| mxbai-embed-xsmall (INT4 ONNX) [matn] | 6ms | 82ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large [matn]</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text [matn]</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m [matn]</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2 [matn]</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m [matn]</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8 [matn]</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4 [matn]</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1 [matn]</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M) [matn]</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX) [matn]</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX) [matn]</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX) [matn]</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 18.0449 <small>· Sahih</small><br><br>We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafahhish, and he use</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8723<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.8553<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8888 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7718 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8291<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>ibnmajah 4218</strong>&nbsp; 0.8296 <small>· Da’if</small><br><br>It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “There is no wisdom like reflection, and no honor like good manners.”</td>
<td valign="top"><strong>ibnmajah 4218</strong>&nbsp; 0.8366 <small>· Da’if</small><br><br>It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “There is no wisdom like reflection, and no honor like good manners.”</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7808 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8800<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.8924 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7792 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.7741 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>adab 290</strong>&nbsp; 15.1631 <small>· Da'if</small><br><br>Abu'd-Darda' stood up in the night to pray. He was weeping and said, 'O Allah! You made my physical form good, so make my character good!' until morni</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.8656 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8399 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8837<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.7477<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>ibnmajah 4218</strong>&nbsp; 0.8262 <small>· Da’if</small><br><br>It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “There is no wisdom like reflection, and no honor like good manners.”</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8266<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8265<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.7515<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.8699 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8848<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.7537<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
<td valign="top"><strong>malik 1749</strong>&nbsp; 0.7467<br><br>Yahya related to me from Malik that he had heard that Abdullah ibn Abbas said, "Equanimity, gentleness, and good behaviour are one twenty-fifth of pro</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 14.9349 <small>· Hasan</small><br><br>"Nothing is placed on the Scale that is heavier than good character. Indeed the person with good character will have attained the rank of the person o</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8575 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.8349 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8761<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>adab 1046</strong>&nbsp; 0.7418 <small>· Hasan</small><br><br>Al-Hasan said, "Be women who greet men."</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8252<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8216<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8247<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7413 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8613 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8738 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>adab 1046</strong>&nbsp; 0.7495 <small>· Hasan</small><br><br>Al-Hasan said, "Be women who greet men."</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.7461 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bukhari 6029</strong>&nbsp; 14.7588 <small>· Sahih</small><br><br>Abdullah bin 'Amr mentioned Allah's Apostle saying that he was neither a Fahish nor a Mutafahish. Abdullah bin 'Amr added, Allah's Apostle said, 'The </td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.8518 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>tirmidhi 1962</strong>&nbsp; 0.8341 <small>· Da'if</small><br><br>Abu Sa'eed Al-Khudri narrated that the Messenger of Allah said: "Two traits are not combined in a believer: Stinginess and bad manners."</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.8723 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.7367 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8234 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.8141 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.8216 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>adab 1046</strong>&nbsp; 0.7384 <small>· Hasan</small><br><br>Al-Hasan said, "Be women who greet men."</td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.8526 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>tirmidhi 1952</strong>&nbsp; 0.8694 <small>· Da'if</small><br><br>Ayyub bin Musa narrated from his father, from his grandfather, that the Messenger of Allah said : "There is no gift that a father gives his son more v</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.7417 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7458 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 14.6536 <small>· Sahih</small><br><br>The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those who have the best manners and c</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8493 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>bukhari 6029</strong>&nbsp; 0.8260<br><br>Narrated Masruq: Abdullah bin 'Amr mentioned Allah's Apostle saying that he was neither a Fahish nor a Mutafahish. Abdullah bin 'Amr added, Allah's Ap</td>
<td valign="top"><strong>abudawud 4816</strong>&nbsp; 0.8644 <small>· Hasan Sahih</small><br><br>Abu Hurairah reported the Prophet (saws) as saying on the same occasion: And guiding the people on their way.</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7310<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.8221 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8095 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8209 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.7362 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.8509 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>ibnmajah 3671</strong>&nbsp; 0.8674 <small>· Da'if</small><br><br>Anas bin Malik narrated that the Messenger of Allah(SAW) said: "Be kind to your children, and perfect their manners."</td>
<td valign="top"><strong>abudawud 4682</strong>&nbsp; 0.7322 <small>· Hasan Sahih</small><br><br>Narrated AbuHurayrah: The Prophet (saws) said: The most perfect believer in respect of faith is he who is best of them in manners.</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.7415<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>bukhari 3759, 3760</strong>&nbsp; 14.2273 <small>· Sahih</small><br><br>Allah's Apostle neither talked in an insulting manner nor did he ever speak evil intentionally. He used to say, "The most beloved to me amongst you is</td>
<td valign="top"><strong>tirmidhi 1952</strong>&nbsp; 0.8447 <small>· Da'if</small><br><br>Ayyub bin Musa narrated from his father, from his grandfather, that the Messenger of Allah said : "There is no gift that a father gives his son more v</td>
<td valign="top"><strong>bukhari 3762</strong>&nbsp; 0.8193<br><br>Narrated `Abdur-Rahman bin Yazid: We asked Hudhaifa to tell us of a person resembling (to some extent) the Prophet in good appearance and straight for</td>
<td valign="top"><strong>adab 1046</strong>&nbsp; 0.8610 <small>· Hasan</small><br><br>Al-Hasan said, "Be women who greet men."</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7264<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.8013 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>tirmidhi 1952</strong>&nbsp; 0.7897 <small>· Da'if</small><br><br>Ayyub bin Musa narrated from his father, from his grandfather, that the Messenger of Allah said : "There is no gift that a father gives his son more v</td>
<td valign="top"><strong>tirmidhi 1952</strong>&nbsp; 0.8070 <small>· Da'if</small><br><br>Ayyub bin Musa narrated from his father, from his grandfather, that the Messenger of Allah said : "There is no gift that a father gives his son more v</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7362<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>adab 1040</strong>&nbsp; 0.8483 <small>· Sahih</small><br><br>Al-Hasan said, "Greeting is an act of obedience while the answer is a duty."</td>
<td valign="top"><strong>ibnmajah 4219</strong>&nbsp; 0.8649 <small>· Hasan</small><br><br>It was narrated from Samurah bin Jundab that the Messenger of Allah (saw) said: “Being honorable is wealth and noble character is piety.’</td>
<td valign="top"><strong>muslim 39</strong>&nbsp; 0.7310<br><br>It is narrated on the authority of 'Abdullah b. 'Amr that a man asked the Messenger of Allah (may peace and blessings be upon him) which of the merits</td>
<td valign="top"><strong>muslim 39</strong>&nbsp; 0.7404<br><br>It is narrated on the authority of 'Abdullah b. 'Amr that a man asked the Messenger of Allah (may peace and blessings be upon him) which of the merits</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>mishkat 5770</strong>&nbsp; 13.8450 <small>· Uncategorized</small><br><br>God has sent me to perfect good qualities of character and to complete good deeds." It is transmitted in Sharh as-sunna .</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8427 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>tirmidhi 2004</strong>&nbsp; 0.8191 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah was asked about that for which people are admitted into Paradise the most, so he said: "Taqwa of All</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8563<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>bukhari 28</strong>&nbsp; 0.7264<br><br>Narrated 'Abdullah bin 'Amr: A person asked Allah's Apostle . "What (sort of) deeds in or (what qualities of) Islam are good?" He replied, "To feed (t</td>
<td valign="top"><strong>tirmidhi 1952</strong>&nbsp; 0.7950 <small>· Da'if</small><br><br>Ayyub bin Musa narrated from his father, from his grandfather, that the Messenger of Allah said : "There is no gift that a father gives his son more v</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.7829 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>tirmidhi 2494</strong>&nbsp; 0.7977 <small>· Da'if</small><br><br>Abu Bakr bin Al-Munkadir narrated from Jabir that the Messenger of Allah (s.a.w) said: "There are three (characteristics) for which whomever has them,</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.7355<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
<td valign="top"><strong>tirmidhi 1952</strong>&nbsp; 0.8461 <small>· Da'if</small><br><br>Ayyub bin Musa narrated from his father, from his grandfather, that the Messenger of Allah said : "There is no gift that a father gives his son more v</td>
<td valign="top"><strong>adab 1040</strong>&nbsp; 0.8625 <small>· Sahih</small><br><br>Al-Hasan said, "Greeting is an act of obedience while the answer is a duty."</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7289<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
<td valign="top"><strong>bukhari 6035</strong>&nbsp; 0.7372<br><br>Narrated Masruq: We were sitting with `Abdullah bin `Amr who was narrating to us (Hadith): He said, "Allah's Apostle was neither a Fahish nor a Mutafa</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>adab 270</strong>&nbsp; 13.2727 <small>· Uncategorized</small><br><br>Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>adab 1040</strong>&nbsp; 0.8420 <small>· Sahih</small><br><br>Al-Hasan said, "Greeting is an act of obedience while the answer is a duty."</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.8179 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>adab 1307</strong>&nbsp; 0.8557<br><br>Abu Hurayra said, "There is no good in excess words."</td>
<td valign="top"><strong>bukhari 3559</strong>&nbsp; 0.7258<br><br>Narrated `Abdullah bin `Amr: The Prophet never used bad language neither a "Fahish nor a Mutafahish. He used to say "The best amongst you are those wh</td>
<td valign="top"><strong>ibnmajah 4188</strong>&nbsp; 0.7930 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Abbas that the Prophet (saw) said to Ashajj ‘Ansari: “You have two characteristics that Allah likes: Forbearance and modesty</td>
<td valign="top"><strong>ibnmajah 4188</strong>&nbsp; 0.7824 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Abbas that the Prophet (saw) said to Ashajj ‘Ansari: “You have two characteristics that Allah likes: Forbearance and modesty</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.7972 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>ahmad 673, 674</strong>&nbsp; 0.7340 <small>· Hasan because of corroborating evidence; this is a Da'if isnad], Hasan because of corroborating evidence; it is a repeat of the     report above]</small><br><br>I was narrated that ‘Ali (رضي الله عنه) said: “The Muslim has the right to six acts of kindness from his fellow Muslim: he should greet him with salam</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8452 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8563<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>muslim 48 b</strong>&nbsp; 0.7241<br><br>Abd Shuraib al-Adawi reported: My eare listened and my eye saw when Allah's Messenger (may peace be upon him) spoke and said: He who believes In Allah</td>
<td valign="top"><strong>ahmad 673, 674</strong>&nbsp; 0.7355 <small>· Hasan because of corroborating evidence; this is a Da'if isnad], Hasan because of corroborating evidence; it is a repeat of the     report above]</small><br><br>I was narrated that ‘Ali (رضي الله عنه) said: “The Muslim has the right to six acts of kindness from his fellow Muslim: he should greet him with salam</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 13.2451 <small>· Sahih</small><br><br>"It is a smiling face, doing one's best in good, and refraining from harm."</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8415<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>mishkat 219</strong>&nbsp; 0.8174<br><br>Abu Huraira reported God’s messenger as saying, “Two qualities are not found together in a hypocrite: good behaviour and knowledge of religion.” Tirmi</td>
<td valign="top"><strong>muslim 572 g</strong>&nbsp; 0.8548<br><br>This hadith has been narrated by Mansur and he said:" He should aim at correctness."</td>
<td valign="top"><strong>muslim 48 b</strong>&nbsp; 0.7250<br><br>Abd Shuraib al-Adawi reported: My eare listened and my eye saw when Allah's Messenger (may peace be upon him) spoke and said: He who believes In Allah</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.7893 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.7822 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>adab 273</strong>&nbsp; 0.7968 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "I was sent to perfect good character."</td>
<td valign="top"><strong>bukhari 12</strong>&nbsp; 0.7338<br><br>Narrated 'Abdullah bin 'Amr: A man asked the Prophet , "What sort of deeds or (what qualities of) Islam are good?" The Prophet replied, 'To feed (the </td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8410<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>tirmidhi 2005</strong>&nbsp; 0.8546 <small>· Sahih</small><br><br>Abu Wahb narrated that : 'Abdullah bin Al-Mubarak explained good character, and then he said: "It is a smiling face, doing one's best in good, and ref</td>
<td valign="top"><strong>shamail 349</strong>&nbsp; 0.7233 <small>· Sahih</small><br><br>'Aisha said (may Allah be well pleased with her): "A man sought permission to come in to see Allah’s Messenger (Allah bless him and give him peace) wh</td>
<td valign="top"><strong>ibnmajah 4218</strong>&nbsp; 0.7342 <small>· Da’if</small><br><br>It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “There is no wisdom like reflection, and no honor like good manners.”</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>adab 273</strong>&nbsp; 12.7513 <small>· Sahih</small><br><br>I was sent to perfect good character."</td>
<td valign="top"><strong>forty 22</strong>&nbsp; 0.8378<br><br>A man who knows his worth will not be ruined.</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.8164<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
<td valign="top"><strong>tirmidhi 64</strong>&nbsp; 0.8526 <small>· Hasan</small><br><br>A1-Hakim bin Amr AI-Ghifari narrated that: "The Prophet forbade that a man should perform Wudu with the leftover (water) from a woman's purifcation." </td>
<td valign="top"><strong>muslim 39</strong>&nbsp; 0.7245<br><br>It is narrated on the authority of 'Abdullah b. 'Amr that a man asked the Messenger of Allah (may peace and blessings be upon him) which of the merits</td>
<td valign="top"><strong>tirmidhi 2494</strong>&nbsp; 0.7878 <small>· Da'if</small><br><br>Abu Bakr bin Al-Munkadir narrated from Jabir that the Messenger of Allah (s.a.w) said: "There are three (characteristics) for which whomever has them,</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.7818 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>tirmidhi 2003</strong>&nbsp; 0.7869 <small>· Hasan</small><br><br>Abu Ad-Dardh narrated that the Messenger of Allah said: "Nothing is placed on the Scale that is heavier than good character. Indeed the person with go</td>
<td valign="top"><strong>bukhari 28</strong>&nbsp; 0.7319<br><br>Narrated 'Abdullah bin 'Amr: A person asked Allah's Apostle . "What (sort of) deeds in or (what qualities of) Islam are good?" He replied, "To feed (t</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.8370 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>adab 284</strong>&nbsp; 0.8528 <small>· Sahih</small><br><br>Abu Hurayra reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "A man who is known for his good character has the sa</td>
<td valign="top"><strong>ibnmajah 4218</strong>&nbsp; 0.7230 <small>· Da’if</small><br><br>It was narrated from Abu Dharr that the Messenger of Allah (saw) said: “There is no wisdom like reflection, and no honor like good manners.”</td>
<td valign="top"><strong>adab 288</strong>&nbsp; 0.7337<br><br>'Abdullah ibn 'Amr said, "There are four qualities such that if you were to be given them, you will not be harmed even if the world were to be taken a</td>
</tr>
</tbody></table>

---

## englishMatn: angels recording deeds

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 12ms |
| mxbai-embed-large [matn] | 35ms | 83ms |
| nomic-embed-text [matn] | 25ms | 79ms |
| snowflake-arctic-embed:m [matn] | 34ms | 83ms |
| all-MiniLM-L6-v2 [matn] | 24ms | 82ms |
| embeddinggemma-300m [matn] | 78ms | 84ms |
| embeddinggemma-300m-qat-q8 [matn] | 64ms | 82ms |
| embeddinggemma-300m-qat-q4 [matn] | 73ms | 82ms |
| mxbai-embed-xsmall-v1 [matn] | 14ms | 77ms |
| mxbai-embed-large (Q4_K_M) [matn] | 44ms | 85ms |
| mxbai-embed-large (INT8 ONNX) [matn] | 32ms | 82ms |
| mxbai-embed-xsmall (INT8 ONNX) [matn] | 2ms | 80ms |
| mxbai-embed-xsmall (INT4 ONNX) [matn] | 6ms | 80ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large [matn]</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text [matn]</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m [matn]</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2 [matn]</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m [matn]</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8 [matn]</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4 [matn]</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1 [matn]</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M) [matn]</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX) [matn]</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX) [matn]</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX) [matn]</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 17.2169 <small>· Sahih</small><br><br>The Great and the Glorious Lord said (to angels): Whenever My servant intends to commit an evil, do not record it against him, but if he actually comm</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8437<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8338<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 2112</strong>&nbsp; 0.8273<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels do not enter the house in which there are portrayals or pictures.</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7900<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8032<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8023<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8104<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7929<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8487<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8604<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7984<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8118<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>mishkat 2112</strong>&nbsp; 16.6777 <small>· Uncategorized</small><br><br>One who is skilled in the Qur’ān is associated with the noble, upright recording angels; and he who falters when reciting the Qur’ān and finds it diff</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.8419<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>mishkat 2112</strong>&nbsp; 0.8297<br><br>‘Ā’isha reported God’s messenger as saying, “One who is skilled in the Qur’ān is associated with the noble, upright recording angels; and he who falte</td>
<td valign="top"><strong>muslim 487 a</strong>&nbsp; 0.8217<br><br>'A'isha reported that the Messenger of Allah (may peace he upon him) used to pronounce while bowing and prostrating himself: All Glorious, All Holy, L</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7586<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>muslim 2106 a</strong>&nbsp; 0.7530<br><br>Abu Talha reported Allah's Apostle (may peace be upon him) having said: Angels do not enter a house in which there is a dog or a picture.</td>
<td valign="top"><strong>muslim 2106 a</strong>&nbsp; 0.7513<br><br>Abu Talha reported Allah's Apostle (may peace be upon him) having said: Angels do not enter a house in which there is a dog or a picture.</td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7474<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7918<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8453<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>muslim 2644</strong>&nbsp; 0.8593<br><br>Hudhaifa b. Usaid reported directly from Allah's Messenger (may peace be upon him) that he said: When the drop of (semen) remains in the womb for fort</td>
<td valign="top"><strong>muslim 128 a</strong>&nbsp; 0.7906<br><br>It is narrated on the authority of Abu Huraira that the Messenger of Allah (may peace be upon him) said: The Great and the Glorious Lord said (to ange</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7989<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>abudawud 1454</strong>&nbsp; 16.6777 <small>· Sahih</small><br><br>One who is skilled in the Qur'an is associated with the noble, upright recording angels, and he who falters when he recites the Qur'an and finds it di</td>
<td valign="top"><strong>muslim 2644</strong>&nbsp; 0.8367<br><br>Hudhaifa b. Usaid reported directly from Allah's Messenger (may peace be upon him) that he said: When the drop of (semen) remains in the womb for fort</td>
<td valign="top"><strong>mishkat 635</strong>&nbsp; 0.8271<br><br>Concerning God’s words, “The recitation of the dawn is witnessed,” (Al-Qur’an, 17:78). Abu Huraira quoted the Prophet as saying, "The angels of the ni</td>
<td valign="top"><strong>muslim 2106 a</strong>&nbsp; 0.8193<br><br>Abu Talha reported Allah's Apostle (may peace be upon him) having said: Angels do not enter a house in which there is a dog or a picture.</td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7562<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
<td valign="top"><strong>muslim 2112</strong>&nbsp; 0.7483<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels do not enter the house in which there are portrayals or pictures.</td>
<td valign="top"><strong>muslim 2112</strong>&nbsp; 0.7490<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels do not enter the house in which there are portrayals or pictures.</td>
<td valign="top"><strong>mishkat 1559</strong>&nbsp; 0.7469<br><br>‘Abdallah b. ‘Amr reported God’s messenger as saying, “When a servant of God is accustomed to worship Him in a good manner, then becomes ill, the ange</td>
<td valign="top"><strong>mishkat 44</strong>&nbsp; 0.7724 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh ", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “When one of you makes a good profession of Islam, every good deed he does will be recorded for him te</td>
<td valign="top"><strong>muslim 2644</strong>&nbsp; 0.8367<br><br>Hudhaifa b. Usaid reported directly from Allah's Messenger (may peace be upon him) that he said: When the drop of (semen) remains in the womb for fort</td>
<td valign="top"><strong>ibnmajah 76</strong>&nbsp; 0.8535 <small>· Sahih</small><br><br>'Abdullah bin Mas'ud said: "The Messenger of Allah (SAW), the true and truly inspired one, told us that: 'The creation of one of you is put together i</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.7774<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.7692<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>mishkat 1560</strong>&nbsp; 16.0469 <small>· Uncategorized</small><br><br>When a Muslim is afflicted with some trouble in his body the angel is told to record for him his good deeds which he was accustomed to do. Then if God</td>
<td valign="top"><strong>mishkat 4594</strong>&nbsp; 0.8304<br><br>She told that she heard God’s messenger say: “The angels descend in al-’anan , i e. the clouds, and mention a matter which has been decreed in heaven,</td>
<td valign="top"><strong>abudawud 1454</strong>&nbsp; 0.8236 <small>· Sahih</small><br><br>'Aishah reported the Prophet (saws) as saying: One who is skilled in the Qur'an is associated with the noble, upright recording angels, and he who fal</td>
<td valign="top"><strong>ibnmajah 3764</strong>&nbsp; 0.8133 <small>· Hasan</small><br><br>It was narrated from 'Aishah that the Prophet(SAW) looked at a man who was chasing a bird and said: "A devil chasing a devil."</td>
<td valign="top"><strong>bukhari 6408</strong>&nbsp; 0.7521<br><br>Narrated Abu Huraira: Allah 's Apostle said, "Allah has some angels who look for those who celebrate the Praises of Allah on the roads and paths. And </td>
<td valign="top"><strong>nasai 4281</strong>&nbsp; 0.7428 <small>· Hasan</small><br><br>It was narrated from 'Ali bin Abi Talib that the Prophet said: "The angels do not enter a house in which there is a picture, a dog or a person who is </td>
<td valign="top"><strong>nasai 4281</strong>&nbsp; 0.7434 <small>· Hasan</small><br><br>It was narrated from 'Ali bin Abi Talib that the Prophet said: "The angels do not enter a house in which there is a picture, a dog or a person who is </td>
<td valign="top"><strong>muslim 2106 a</strong>&nbsp; 0.7463<br><br>Abu Talha reported Allah's Apostle (may peace be upon him) having said: Angels do not enter a house in which there is a dog or a picture.</td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 0.7723<br><br>Ibn ‘Abbas reported God’s messenger as saying, “God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it,</td>
<td valign="top"><strong>ibnmajah 851</strong>&nbsp; 0.8363 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “When the reciter says Amin, then say Amin, for the angels say Amin, and if </td>
<td valign="top"><strong>bukhari 6491</strong>&nbsp; 0.8520<br><br>Narrated Ibn `Abbas: The Prophet narrating about his Lord I'm and said, "Allah ordered (the appointed angels over you) that the good and the bad deeds</td>
<td valign="top"><strong>mishkat 44</strong>&nbsp; 0.7743 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh ", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “When one of you makes a good profession of Islam, every good deed he does will be recorded for him te</td>
<td valign="top"><strong>ibnmajah 3649</strong>&nbsp; 0.7687 <small>· Sahih</small><br><br>It was narrated from Abu Talhah that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>mishkat 2374</strong>&nbsp; 15.4689 <small>· Uncategorized</small><br><br>God records the good deeds and the evil deeds. If anyone intends to do a good deed but does not do it, God enters it for him in His record as a comple</td>
<td valign="top"><strong>ibnmajah 851</strong>&nbsp; 0.8288 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “When the reciter says Amin, then say Amin, for the angels say Amin, and if </td>
<td valign="top"><strong>mishkat 2172</strong>&nbsp; 0.8177<br><br>Makhūl said, “If anyone recites Āl ‘Imrān on a Friday, the angels will invoke blessings on him till night comes.” Transmitted by Dārimī.</td>
<td valign="top"><strong>ibnmajah 3818</strong>&nbsp; 0.8101 <small>· Hasan</small><br><br>'Abdullah bin Busr said that : the Prophet (saas) said: "Glad tidings to those who find a lot of seeking forgiveness in the record of their deeds."</td>
<td valign="top"><strong>bukhari 3210</strong>&nbsp; 0.7509<br><br>Narrated `Aisha: I heard Allah's Apostle saying, "The angels descend, the clouds and mention this or that matter decreed in the Heaven. The devils lis</td>
<td valign="top"><strong>ibnmajah 3649</strong>&nbsp; 0.7426 <small>· Sahih</small><br><br>It was narrated from Abu Talhah that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>ahmad 1172</strong>&nbsp; 0.7431 <small>· Sahih because of corroborating evidences]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) that the Messenger of Allah (ﷺ) said: “The angels do not enter a house in which there is an image or a person</td>
<td valign="top"><strong>muslim 2112</strong>&nbsp; 0.7429<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Angels do not enter the house in which there are portrayals or pictures.</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7660<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>bukhari 7429</strong>&nbsp; 0.8314<br><br>Narrated Abu Huraira: Allah's Apostle said, "(A group of) angels stay with you at night and (another group of) angels by daytime, and both groups gath</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8519 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7731<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>ibnmajah 3650</strong>&nbsp; 0.7687 <small>· Hasan</small><br><br>It was narrated from ‘Ali bin Abu Talib that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>abudawud 5263</strong>&nbsp; 15.3019 <small>· Sahih</small><br><br>The Prophet (saws) said: If anyone kills a gecko with the first blow, such and such number of good deeds will be recorded for him, if he kills it with</td>
<td valign="top"><strong>bukhari 7429</strong>&nbsp; 0.8283<br><br>Narrated Abu Huraira: Allah's Apostle said, "(A group of) angels stay with you at night and (another group of) angels by daytime, and both groups gath</td>
<td valign="top"><strong>ibnmajah 1426</strong>&nbsp; 0.8170 <small>· Sahih</small><br><br>It was narrated from Tamim Dari that the Prophet (saw) said: “The first thing for which a person will be brought to account on the Day of Resurrection</td>
<td valign="top"><strong>abudawud 4453</strong>&nbsp; 0.8081 <small>· Sahih li ghairih</small><br><br>A similar tradition has also been transmitted by Ibrahim and al-Sha’bi from the Prophet (saws) through a different chain of narrators. But this versio</td>
<td valign="top"><strong>nasai 261</strong>&nbsp; 0.7495 <small>· Hasan</small><br><br>It was narrated from 'Ali that the Prophet (PBUH) said: "The angels do not enter a house where there is an image, a dog or a Junub person."</td>
<td valign="top"><strong>ibnmajah 3650</strong>&nbsp; 0.7426 <small>· Hasan</small><br><br>It was narrated from ‘Ali bin Abu Talib that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>nasai 261</strong>&nbsp; 0.7398 <small>· Hasan</small><br><br>It was narrated from 'Ali that the Prophet (PBUH) said: "The angels do not enter a house where there is an image, a dog or a Junub person."</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7422<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>mishkat 4594</strong>&nbsp; 0.7604<br><br>She told that she heard God’s messenger say: “The angels descend in al-’anan , i e. the clouds, and mention a matter which has been decreed in heaven,</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8310 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>bukhari 4701</strong>&nbsp; 0.8461<br><br>Narrated Abu Huraira: The Prophet said, "When Allah has ordained some affair in the Heaven, the angels beat with their wings in obedience to His state</td>
<td valign="top"><strong>ahmad 815</strong>&nbsp; 0.7633 <small>· Sahih because of corroborating evidence, this is a Da'if isnad]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) from the Prophet (ﷺ), that He said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>ahmad 815</strong>&nbsp; 0.7687 <small>· Sahih because of corroborating evidence, this is a Da'if isnad]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) from the Prophet (ﷺ), that He said: “The angels do not enter a house in which there is a dog or an image.”</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>muslim 2644</strong>&nbsp; 14.9987 <small>· Sahih</small><br><br>When the drop of (semen) remains in the womb for forty or forty five nights, the angel comes and says: My Lord, will he be good or evil? And both thes</td>
<td valign="top"><strong>ibnmajah 3801</strong>&nbsp; 0.8277 <small>· Da'if</small><br><br>It was narrated from 'Abdullah bin 'Umar that : the Messenger of Allah (SAW) told them: "One of the slaves of Allah said: 'Ya Rabb! Lakal-hamdu kama y</td>
<td valign="top"><strong>muslim 798 a</strong>&nbsp; 0.8160<br><br>`A'isha reported Allah's Messenger (may peace be upon him) (as saying): One who is proficient in the Qur'an is associated with the noble, upright, rec</td>
<td valign="top"><strong>abudawud 4719</strong>&nbsp; 0.8020 <small>· Sahih</small><br><br>Anas b. Malik reported the Messenger of Allah (May peace be upon him) as saying : The devil flows in a man like his blood.</td>
<td valign="top"><strong>muslim 85 e</strong>&nbsp; 0.7461<br><br>It is reported on the authority of 'Abdullah that the Apostle of Allah observed: The best of' the deeds or deed is the (observance of) prayer at its p</td>
<td valign="top"><strong>ahmad 815</strong>&nbsp; 0.7426 <small>· Sahih because of corroborating evidence, this is a Da'if isnad]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) from the Prophet (ﷺ), that He said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>ibnmajah 3649</strong>&nbsp; 0.7395 <small>· Sahih</small><br><br>It was narrated from Abu Talhah that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>ibnmajah 3365</strong>&nbsp; 0.7421 <small>· Sahih</small><br><br>It was narrated from Jabir that a group of people came to the Prophet (saw) and he noticed the smell of leeks coming from them. He said: “Did I not fo</td>
<td valign="top"><strong>ahmad 815</strong>&nbsp; 0.7598 <small>· Sahih because of corroborating evidence, this is a Da'if isnad]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) from the Prophet (ﷺ), that He said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.8277<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>mishkat 4594</strong>&nbsp; 0.8445<br><br>She told that she heard God’s messenger say: “The angels descend in al-’anan , i e. the clouds, and mention a matter which has been decreed in heaven,</td>
<td valign="top"><strong>adab 500</strong>&nbsp; 0.7617<br><br>It is narrated by Abdullah bin Amr that Prophet (saws) said, "When a person falls ill then the reward of those deeds is also recorded for him which he</td>
<td valign="top"><strong>ahmad 1172</strong>&nbsp; 0.7660 <small>· Sahih because of corroborating evidences]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) that the Messenger of Allah (ﷺ) said: “The angels do not enter a house in which there is an image or a person</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>riyadussalihin 1864</strong>&nbsp; 14.4177 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) said, "He who kills a chameleon at the first blow, such and such number of good deeds will be awarded to him; whoever ki</td>
<td valign="top"><strong>bukhari 7486</strong>&nbsp; 0.8260<br><br>Narrated Abu Huraira: Allah's Apostle said, "There are angels coming to you in succession at night, and others during the day, and they all gather at </td>
<td valign="top"><strong>ibnmajah 851</strong>&nbsp; 0.8140 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “When the reciter says Amin, then say Amin, for the angels say Amin, and if </td>
<td valign="top"><strong>muslim 1623 h</strong>&nbsp; 0.7972<br><br>Nu'man b. Bashir (Allah be pleased with them) reported that Allah's Messenger (may peace be upon him) said to his father: Call me not as witness to an</td>
<td valign="top"><strong>nasai 485</strong>&nbsp; 0.7455 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (PBUH) said: "Angels come to you in succession by night and day, and they meet at Fajr p</td>
<td valign="top"><strong>muslim 487 a</strong>&nbsp; 0.7426<br><br>'A'isha reported that the Messenger of Allah (may peace he upon him) used to pronounce while bowing and prostrating himself: All Glorious, All Holy, L</td>
<td valign="top"><strong>ibnmajah 3650</strong>&nbsp; 0.7395 <small>· Hasan</small><br><br>It was narrated from ‘Ali bin Abu Talib that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>ahmad 1172</strong>&nbsp; 0.7414 <small>· Sahih because of corroborating evidences]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) that the Messenger of Allah (ﷺ) said: “The angels do not enter a house in which there is an image or a person</td>
<td valign="top"><strong>ibnmajah 3649</strong>&nbsp; 0.7590 <small>· Sahih</small><br><br>It was narrated from Abu Talhah that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>bukhari 3218</strong>&nbsp; 0.8258<br><br>Narrated Ibn `Abbas: Allah's Apostle asked Gabriel, "Why don't you visit us more often than you do?" Then the following Holy Verse was revealed (in th</td>
<td valign="top"><strong>mishkat 924</strong>&nbsp; 0.8436<br><br>He also reported God’s Messenger as saying, “God has angels who travel about in the earth and convey to me greetings from my people.” Nassa’i and Dari</td>
<td valign="top"><strong>ahmad 1172</strong>&nbsp; 0.7598 <small>· Sahih because of corroborating evidences]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) that the Messenger of Allah (ﷺ) said: “The angels do not enter a house in which there is an image or a person</td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7653<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 14.3222 <small>· Sahih</small><br><br>When it occurs to my bondsman that he should do a good deed but he actually does not do it, record one good to him, but if he puts it into practice, I</td>
<td valign="top"><strong>ibnmajah 76</strong>&nbsp; 0.8242 <small>· Sahih</small><br><br>'Abdullah bin Mas'ud said: "The Messenger of Allah (SAW), the true and truly inspired one, told us that: 'The creation of one of you is put together i</td>
<td valign="top"><strong>mishkat 877</strong>&nbsp; 0.8129<br><br>Rifa'a b. Raf’i said: We were praying behind the Prophet, and when he raised his head at the end of the rak'a he said, “God listens to him who praises</td>
<td valign="top"><strong>abudawud 706</strong>&nbsp; 0.7962 <small>· Da'if</small><br><br>This tradition as also been reported by Sa’id through the same chain of narrators and to the same effect. He added: He cut off our prayer, may Allah c</td>
<td valign="top"><strong>bukhari 3225</strong>&nbsp; 0.7422<br><br>Narrated Abu Talha: I heard Allah's Apostle saying; "Angels (of Mercy) do not enter a house wherein there is a dog or a picture of a living creature (</td>
<td valign="top"><strong>mishkat 3115</strong>&nbsp; 0.7409<br><br>Ibn ‘Umar reported God’s Messenger as saying, "Avoid being naked, for with you are those who never leave you (the recording angels) except when you ar</td>
<td valign="top"><strong>ahmad 815</strong>&nbsp; 0.7395 <small>· Sahih because of corroborating evidence, this is a Da'if isnad]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) from the Prophet (ﷺ), that He said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>ibnmajah 3649</strong>&nbsp; 0.7411 <small>· Sahih</small><br><br>It was narrated from Abu Talhah that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>ibnmajah 3650</strong>&nbsp; 0.7590 <small>· Hasan</small><br><br>It was narrated from ‘Ali bin Abu Talib that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.8257<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>tirmidhi 981</strong>&nbsp; 0.8433 <small>· Da'if</small><br><br>Anas bin Malik narrated that: The Messenger of Allah said: "There is nothing that the two Guardian Angels raise to Allah that they have preserved in a</td>
<td valign="top"><strong>bukhari 3332</strong>&nbsp; 0.7593<br><br>Narrated `Abdullah: Allah's Apostle, the true and truly inspired said, "(as regards your creation), every one of you is collected in the womb of his m</td>
<td valign="top"><strong>ibnmajah 1455</strong>&nbsp; 0.7641 <small>· Da’if</small><br><br>It was narrated from Shaddad bin Aws that the Messenger of Allah (SAW) said: “When you come to your dead ones, close their eyes, for the sight follows</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>ibnmajah 1426</strong>&nbsp; 14.0222 <small>· Sahih</small><br><br>“The first thing for which a person will be brought to account on the Day of Resurrection will be his prayer. If it is complete, then the voluntary (p</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.8236<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>mishkat 463</strong>&nbsp; 0.8117<br><br>‘Ali reported God’s messenger as saying, “The angels do not enter a house in which there is a picture, a dog, or one who is defiled.” Abu Dawud and Na</td>
<td valign="top"><strong>ahmad 632</strong>&nbsp; 0.7960 <small>· Sahih, because of corroborating evidences]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) from the Prophet (ﷺ): “The angels do not enter a house in which there is a junub person or an image or a dog.</td>
<td valign="top"><strong>nasai 705</strong>&nbsp; 0.7418 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet (PBUH) said: "When a man goes out of his house to his Masjid, one foot records a good deed and the </td>
<td valign="top"><strong>muslim 129</strong>&nbsp; 0.7407<br><br>Abu Huraira reported that Muhammad, the Messenger of Allah (may peace be upon him), said: When it occurs to my bondsman that he should do a good deed </td>
<td valign="top"><strong>ahmad 632</strong>&nbsp; 0.7391 <small>· Sahih, because of corroborating evidences]</small><br><br>It was narrated from ‘Ali (رضي الله عنه) from the Prophet (ﷺ): “The angels do not enter a house in which there is a junub person or an image or a dog.</td>
<td valign="top"><strong>ibnmajah 3650</strong>&nbsp; 0.7411 <small>· Hasan</small><br><br>It was narrated from ‘Ali bin Abu Talib that the Prophet (saw) said: “The angels do not enter a house in which there is a dog or an image.”</td>
<td valign="top"><strong>bukhari 3332</strong>&nbsp; 0.7579<br><br>Narrated `Abdullah: Allah's Apostle, the true and truly inspired said, "(as regards your creation), every one of you is collected in the womb of his m</td>
<td valign="top"><strong>bukhari 555</strong>&nbsp; 0.8257<br><br>Narrated Abu Huraira: Allah's Apostle said, "Angels come to you in succession by night and day and all of them get together at the time of the Fajr an</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.8433<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
<td valign="top"><strong>muslim 85 e</strong>&nbsp; 0.7589<br><br>It is reported on the authority of 'Abdullah that the Apostle of Allah observed: The best of' the deeds or deed is the (observance of) prayer at its p</td>
<td valign="top"><strong>bukhari 7501</strong>&nbsp; 0.7641<br><br>Narrated Abu Huraira: Allah's Apostle said, "Allah says, 'If My slave intends to do a bad deed then (O Angels) do not write it unless he does it; if h</td>
</tr>
</tbody></table>

---

## englishMatn: prayer at night

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 15ms |
| mxbai-embed-large [matn] | 68ms | 84ms |
| nomic-embed-text [matn] | 37ms | 80ms |
| snowflake-arctic-embed:m [matn] | 34ms | 82ms |
| all-MiniLM-L6-v2 [matn] | 42ms | 82ms |
| embeddinggemma-300m [matn] | 72ms | 80ms |
| embeddinggemma-300m-qat-q8 [matn] | 105ms | 80ms |
| embeddinggemma-300m-qat-q4 [matn] | 56ms | 80ms |
| mxbai-embed-xsmall-v1 [matn] | 10ms | 77ms |
| mxbai-embed-large (Q4_K_M) [matn] | 41ms | 83ms |
| mxbai-embed-large (INT8 ONNX) [matn] | 22ms | 80ms |
| mxbai-embed-xsmall (INT8 ONNX) [matn] | 2ms | 81ms |
| mxbai-embed-xsmall (INT4 ONNX) [matn] | 6ms | 80ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large [matn]</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text [matn]</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m [matn]</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2 [matn]</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m [matn]</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8 [matn]</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4 [matn]</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1 [matn]</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M) [matn]</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX) [matn]</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX) [matn]</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX) [matn]</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>riyadussalihin 1071</strong>&nbsp; 9.9731 <small>· Uncategorized</small><br><br>I heard the Messenger of Allah (PBUH) saying: "One who performs 'Isha' prayer in congregation, is as if he has performed Salat for half of the night. </td>
<td valign="top"><strong>ibnmajah 1319</strong>&nbsp; 0.9234 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The night prayer is (to be offered) two by two.”</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.9114 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>muslim 751 b</strong>&nbsp; 0.8999<br><br>Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: Make Witr the end of your night prayer.</td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8582<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.8613 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.8618 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.8609 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>abudawud 1314</strong>&nbsp; 0.8563 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Prophet (saws) said: Any person who offers prayer at night regularly but (on a certain night) he is dominated by s</td>
<td valign="top"><strong>ibnmajah 1319</strong>&nbsp; 0.9241 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The night prayer is (to be offered) two by two.”</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.9389 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8578 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8611<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 9.9572 <small>· Sahih</small><br><br>Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of the night.</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.9187 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>nasai 1673</strong>&nbsp; 0.9010 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said that: A man asked the Messenger of Allah (SAW) about prayers at night. The Messenger of Allah (SAW) said: </td>
<td valign="top"><strong>bulugh 270</strong>&nbsp; 0.8987<br><br>And in another narration of Muslim: "he used to say that in the night prayer..."</td>
<td valign="top"><strong>abudawud 1314</strong>&nbsp; 0.8578 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Prophet (saws) said: Any person who offers prayer at night regularly but (on a certain night) he is dominated by s</td>
<td valign="top"><strong>ibnmajah 1322</strong>&nbsp; 0.8315 <small>· Hasan</small><br><br>Ibn ‘Umar narrated that the Messenger of Allah (saw) said: “Prayers at night and during the day are to be offered two by two.”</td>
<td valign="top"><strong>ibnmajah 1322</strong>&nbsp; 0.8298 <small>· Hasan</small><br><br>Ibn ‘Umar narrated that the Messenger of Allah (saw) said: “Prayers at night and during the day are to be offered two by two.”</td>
<td valign="top"><strong>ibnmajah 1322</strong>&nbsp; 0.8392 <small>· Hasan</small><br><br>Ibn ‘Umar narrated that the Messenger of Allah (saw) said: “Prayers at night and during the day are to be offered two by two.”</td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8519<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.9183 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>muslim 751 b</strong>&nbsp; 0.9361<br><br>Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: Make Witr the end of your night prayer.</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8540<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8575<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>ibnmajah 1327</strong>&nbsp; 9.9569 <small>· Sahih</small><br><br>“We fasted Ramadan with the Messenger of Allah (saw) and he did not lead us in praying Qiyam (prayers at night) during any part of it, until there wer</td>
<td valign="top"><strong>muslim 751 b</strong>&nbsp; 0.9088<br><br>Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: Make Witr the end of your night prayer.</td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.8990<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.8972 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8525<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>ibnmajah 1522</strong>&nbsp; 0.8260 <small>· Da’if</small><br><br>It was narrated from Jabir bin ‘Abdullah that the Prophet (SAW) said: “Offer the funeral prayer for your dead by night or by day.”</td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.8242<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>ibnmajah 1319</strong>&nbsp; 0.8270 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The night prayer is (to be offered) two by two.”</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8493 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
<td valign="top"><strong>muslim 751 b</strong>&nbsp; 0.9114<br><br>Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: Make Witr the end of your night prayer.</td>
<td valign="top"><strong>ibnmajah 1319</strong>&nbsp; 0.9132 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The night prayer is (to be offered) two by two.”</td>
<td valign="top"><strong>abudawud 1314</strong>&nbsp; 0.8445 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Prophet (saws) said: Any person who offers prayer at night regularly but (on a certain night) he is dominated by s</td>
<td valign="top"><strong>abudawud 1314</strong>&nbsp; 0.8556 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Prophet (saws) said: Any person who offers prayer at night regularly but (on a certain night) he is dominated by s</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>ibnmajah 286</strong>&nbsp; 9.9426 <small>· Sahih</small><br><br>"Whenever the Messenger of Allah got up for prayer at night to pray Tahajjud (night optional prayer), he would clean his mouth with the tooth stick."</td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8934<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8956<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>muslim 750</strong>&nbsp; 0.8725<br><br>Ibn 'Umar reported the Apostle of Allah (may peace be upon him) as say- ing: Hasten to pray Witr before morning.</td>
<td valign="top"><strong>bukhari 1152</strong>&nbsp; 0.8455<br><br>Narrated `Abdullah bin `Amr bin Al-`As: Allah's Apostle said to me, "O `Abdullah! Do not be like so and so who used to pray at night and then stopped </td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.8212<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8185<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.8199<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8459<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.8967<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>ibnmajah 1322</strong>&nbsp; 0.9128 <small>· Hasan</small><br><br>Ibn ‘Umar narrated that the Messenger of Allah (saw) said: “Prayers at night and during the day are to be offered two by two.”</td>
<td valign="top"><strong>bulugh 369</strong>&nbsp; 0.8445<br><br>Narrated Abu Hurairah (RA): Allah's Messenger (SAW) said, "The most excellent prayer after that which is obligatory is the (voluntary) late night pray</td>
<td valign="top"><strong>abudawud 555</strong>&nbsp; 0.8550 <small>· Sahih</small><br><br>‘Uthman b. ‘Affan reported the Messenger of Allah (may peace be him) as saying; if anyone says the night prayer in congregation, he is like one who ke</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>bulugh 380</strong>&nbsp; 9.9318 <small>· Uncategorized</small><br><br>Allah's Messenger (SAW) offered Witr prayer (on different nights) at various hours, extending (from the 'Isha' prayer) up to the last hour of the nigh</td>
<td valign="top"><strong>muslim 755 a</strong>&nbsp; 0.8883<br><br>Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he sho</td>
<td valign="top"><strong>nasai 1694</strong>&nbsp; 0.8938 <small>· Sahih</small><br><br>It was narrated from Abdullah bin 'Umar that: A man asked the Messenger of Allah (SAW) about prayer at night and the Messenger of Allah (SAW) said: "P</td>
<td valign="top"><strong>muslim 694 f</strong>&nbsp; 0.8706<br><br>This hadith has been narrated by Shu'ba with the same chain of transmitters but no mention has been made of Mina, but they (the narrators) only said: </td>
<td valign="top"><strong>abudawud 1307</strong>&nbsp; 0.8447 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Do not give up prayer at night, for the Messenger of Allah (saws) would not leave it. Whenever he fell ill or lethargi</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8171<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>muslim 751 b</strong>&nbsp; 0.8185<br><br>Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: Make Witr the end of your night prayer.</td>
<td valign="top"><strong>ibnmajah 1522</strong>&nbsp; 0.8193 <small>· Da’if</small><br><br>It was narrated from Jabir bin ‘Abdullah that the Prophet (SAW) said: “Offer the funeral prayer for your dead by night or by day.”</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8450<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
<td valign="top"><strong>ibnmajah 1344</strong>&nbsp; 0.8938 <small>· Sahih</small><br><br>It was narrated that Abu Darda’ conveyed that the Prophet (saw) said: “Whoever goes to bed intending to wake up and pray during the night, but is over</td>
<td valign="top"><strong>bukhari 996</strong>&nbsp; 0.9101<br><br>Narrated `Aisha: Allah's Apostle offered witr prayer at different nights at various hours extending (from the `Isha' prayer) up to the last hour of th</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8379<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8452<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>tirmidhi 806</strong>&nbsp; 9.9219 <small>· Sahih</small><br><br>"We fasted with the Prophet, so he did not pray (the night prayer) with us until seven (nights) of the month remained. Then he (pbuh) led us in prayer</td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.8879<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>muslim 759 a</strong>&nbsp; 0.8922<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed prayer at night during Ramadan, because of faith and seeking</td>
<td valign="top"><strong>ibnmajah 1319</strong>&nbsp; 0.8651 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The night prayer is (to be offered) two by two.”</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.8428 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>ibnmajah 1319</strong>&nbsp; 0.8146 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The night prayer is (to be offered) two by two.”</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8165<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8185<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>nasai 1672</strong>&nbsp; 0.8380 <small>· Sahih</small><br><br>It was narrated that Ibn Umar said: "A man from among the Muslims asked the Messenger of Allah (SAW): 'How are prayers at night to be done?' He said: </td>
<td valign="top"><strong>muslim 755 a</strong>&nbsp; 0.8913<br><br>Jabir reported Allah's Messenger (may peace be upon him) as saying: If anyone is afraid that he may not get up in the latter part of the night, he sho</td>
<td valign="top"><strong>mishkat 1258</strong>&nbsp; 0.9084<br><br>Ibn ‘Umar reported the Prophet as saying, "Make the last of your prayer at night a witr .” Muslim transmitted it.</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8371 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
<td valign="top"><strong>nasai 1672</strong>&nbsp; 0.8430 <small>· Sahih</small><br><br>It was narrated that Ibn Umar said: "A man from among the Muslims asked the Messenger of Allah (SAW): 'How are prayers at night to be done?' He said: </td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 9.9218 <small>· Sahih</small><br><br>Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to follow him in the </td>
<td valign="top"><strong>nasai 1623</strong>&nbsp; 0.8877 <small>· Sahih</small><br><br>It was narrated that Hudhaifah said: "We were commanded to use the siwak when we got up to pray at night."</td>
<td valign="top"><strong>muslim 751 b</strong>&nbsp; 0.8910<br><br>Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: Make Witr the end of your night prayer.</td>
<td valign="top"><strong>abudawud 706</strong>&nbsp; 0.8611 <small>· Da'if</small><br><br>This tradition as also been reported by Sa’id through the same chain of narrators and to the same effect. He added: He cut off our prayer, may Allah c</td>
<td valign="top"><strong>bukhari 729</strong>&nbsp; 0.8419<br><br>Narrated `Aisha: Allah's Apostle used to pray in his room at night. As the wall of the room was LOW, the people saw him and some of them stood up to f</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8142<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>bulugh 270</strong>&nbsp; 0.8162<br><br>And in another narration of Muslim: "he used to say that in the night prayer..."</td>
<td valign="top"><strong>bulugh 270</strong>&nbsp; 0.8157<br><br>And in another narration of Muslim: "he used to say that in the night prayer..."</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8375 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
<td valign="top"><strong>ibnmajah 1187</strong>&nbsp; 0.8912 <small>· Sahih</small><br><br>It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fears that he will not wake up at the end of the night, let him </td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.9068<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8344 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8423 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>tirmidhi 221</strong>&nbsp; 9.9061 <small>· Sahih</small><br><br>"Whoever attends Isha (prayer) in congregation, then he has (the reward as if he had) stood half of the night. And whoever prays Isha and Fajr in cong</td>
<td valign="top"><strong>ibnmajah 1187</strong>&nbsp; 0.8875 <small>· Sahih</small><br><br>It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fears that he will not wake up at the end of the night, let him </td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8909 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>nasai 617</strong>&nbsp; 0.8582 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that when they missed the prayer because they slept until the sun rose, the Messenger of Allah (PBUH) said: "Let any </td>
<td valign="top"><strong>nasai 1672</strong>&nbsp; 0.8401 <small>· Sahih</small><br><br>It was narrated that Ibn Umar said: "A man from among the Muslims asked the Messenger of Allah (SAW): 'How are prayers at night to be done?' He said: </td>
<td valign="top"><strong>muslim 751 b</strong>&nbsp; 0.8136<br><br>Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: Make Witr the end of your night prayer.</td>
<td valign="top"><strong>ibnmajah 1359</strong>&nbsp; 0.8162 <small>· Sahih</small><br><br>It was narrated that ‘Aishah said: “The Prophet (saw) used to pray thirteen Rak’ah at night.”</td>
<td valign="top"><strong>muslim 751 b</strong>&nbsp; 0.8151<br><br>Ibn 'Umar reported Allah's Messenger (may peace be upon him) as saying: Make Witr the end of your night prayer.</td>
<td valign="top"><strong>abudawud 1307</strong>&nbsp; 0.8354 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Do not give up prayer at night, for the Messenger of Allah (saws) would not leave it. Whenever he fell ill or lethargi</td>
<td valign="top"><strong>bukhari 998</strong>&nbsp; 0.8897<br><br>Narrated `Abdullah bin `Umar: The Prophet said, "Make witr as your last prayer at night."</td>
<td valign="top"><strong>ahmad 651</strong>&nbsp; 0.9038 <small>· A Qawi Hadeeth and Da'if (Darussalam) because of the weakness of Al-Harith Al-A’war]</small><br><br>It was narrated that ‘Ali (رضي الله عنه) said: At different times of the night the Messenger of Allah (ﷺ) prayed Witr at the beginning, in the middle </td>
<td valign="top"><strong>nasai 1672</strong>&nbsp; 0.8342 <small>· Sahih</small><br><br>It was narrated that Ibn Umar said: "A man from among the Muslims asked the Messenger of Allah (SAW): 'How are prayers at night to be done?' He said: </td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.8411 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 564</strong>&nbsp; 9.9051 <small>· Sahih</small><br><br>"One night Allah's Apostle led us in the `Isha' prayer and that is the one called Al-`Atma [??] by the people. After the completion of the prayer, he </td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8867<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>abudawud 419</strong>&nbsp; 0.8890 <small>· Sahih</small><br><br>Narrated An-Nu'man ibn Bashir: I am the one who is best informed of the time of this prayer, i.e. the night prayer. The Messenger of Allah (saws) used</td>
<td valign="top"><strong>muslim 2085 b</strong>&nbsp; 0.8579<br><br>This hadith has been narrated on the authority of Ibn 'Umar through other chains of transmitters also with the addition of these words:" On the Day of</td>
<td valign="top"><strong>nasai 1674</strong>&nbsp; 0.8395 <small>· Sahih</small><br><br>It was narrated that Abdullah bin Umar said: "A man stood up and said: 'O Messenger of Allah (SAW), how are the prayers at night to be done?' The Mess</td>
<td valign="top"><strong>nasai 1683</strong>&nbsp; 0.8122 <small>· Sahih</small><br><br>Abu Nadrah Al-'Awaqi narrated that he heard Abu Sa'eed Al-Khudri say: "The Messenger of Allah (SAW) was asked about witr and he said: 'Pray witr befor</td>
<td valign="top"><strong>ibnmajah 1522</strong>&nbsp; 0.8161 <small>· Da’if</small><br><br>It was narrated from Jabir bin ‘Abdullah that the Prophet (SAW) said: “Offer the funeral prayer for your dead by night or by day.”</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8147<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>abudawud 1438</strong>&nbsp; 0.8343 <small>· Sahih</small><br><br>Ibn 'Umar reported the Prophet (saws) as suing: Make the last of your prayer at night a witr.</td>
<td valign="top"><strong>bukhari 589</strong>&nbsp; 0.8890<br><br>Narrated Ibn `Umar: I pray as I saw my companions praying. I do not forbid praying at any time during the day or night except at sunset and sunrise.</td>
<td valign="top"><strong>ibnmajah 1187</strong>&nbsp; 0.9024 <small>· Sahih</small><br><br>It was narrated from Jabir that the Messenger of Allah (saw) said: “Whoever among you fears that he will not wake up at the end of the night, let him </td>
<td valign="top"><strong>ibnmajah 1252</strong>&nbsp; 0.8335 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “Safwan bin Mu’attal asked the Messenger of Allah (saw): ‘O Messenger of Allah, I want to ask you about someth</td>
<td valign="top"><strong>mishkat 1254</strong>&nbsp; 0.8392<br><br>Ibn ‘Umar reported God’s Messenger as saying, “Prayer during the night should consist of pairs of rak'as , but if one of you fears the morning is near</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>nasai 5202</strong>&nbsp; 9.8950 <small>· Sahih</small><br><br>"The Messenger of Allah [SAW] delayed 'Isha' prayer one night, until half the night had passed, then he came out and led us in prayer. And it is as if</td>
<td valign="top"><strong>muslim 749 a</strong>&nbsp; 0.8863<br><br>Ibn 'Umar reported that a person asked the Messenger of Allah (may peace be upon him) about the night prayer. The Messenger of Allah (may peace be upo</td>
<td valign="top"><strong>mishkat 597</strong>&nbsp; 0.8882<br><br>‘A'isha said that they used to pray the night prayer at any time after the ending of the twilight until a third of the night had passed. (Bukhari and </td>
<td valign="top"><strong>nasai 548</strong>&nbsp; 0.8578 <small>· Sahih</small><br><br>It was narrated from Rafi' bin Khadij that the Prophet (PBUH) said: "Pray Fajr when the dawn shines."</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8309 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
<td valign="top"><strong>bukhari 2011</strong>&nbsp; 0.8119<br><br>Narrated `Aisha: (the wife of the Prophet) Allah's Apostle used to pray (at night) in Ramadan.</td>
<td valign="top"><strong>ibnmajah 1319</strong>&nbsp; 0.8158 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The night prayer is (to be offered) two by two.”</td>
<td valign="top"><strong>nasai 1682</strong>&nbsp; 0.8135 <small>· Sahih</small><br><br>It was narrated that Ibn 'Umar said: "Whoever prays during the night, let him make the last of his prayers at night witr, because the Messenger of All</td>
<td valign="top"><strong>riyadussalihin 1161</strong>&nbsp; 0.8308<br><br>'Ali (May Allah be pleased with him) reported: The Prophet (PBUH) visited me and Fatimah (May Allah be pleased with her) one night and said, "Do you n</td>
<td valign="top"><strong>mishkat 1260</strong>&nbsp; 0.8884<br><br>Jabir reported God’s Messenger as saying, "If anyone is afraid that he may not get up in the latter part of the night, he should observe a witr in the</td>
<td valign="top"><strong>muslim 514</strong>&nbsp; 0.9012<br><br>'A'isha reported: The Apostle of Allah (may peace be upon him) said prayer at night and I was by his side in a state of meanses and I had a sheet pull</td>
<td valign="top"><strong>riyadussalihin 1161</strong>&nbsp; 0.8264<br><br>'Ali (May Allah be pleased with him) reported: The Prophet (PBUH) visited me and Fatimah (May Allah be pleased with her) one night and said, "Do you n</td>
<td valign="top"><strong>abudawud 1326</strong>&nbsp; 0.8390 <small>· Sahih</small><br><br>Narrated 'Abdullah bin 'Umar: A man asked the Messenger of Allah (saws) about the prayer at night. The Messenger of Allah (saws) said: Prayer during t</td>
</tr>
</tbody></table>

---

## englishMatn: forgiving someone who wronged you

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 13ms |
| mxbai-embed-large [matn] | 54ms | 83ms |
| nomic-embed-text [matn] | 45ms | 80ms |
| snowflake-arctic-embed:m [matn] | 46ms | 83ms |
| all-MiniLM-L6-v2 [matn] | 46ms | 80ms |
| embeddinggemma-300m [matn] | 71ms | 86ms |
| embeddinggemma-300m-qat-q8 [matn] | 63ms | 81ms |
| embeddinggemma-300m-qat-q4 [matn] | 72ms | 82ms |
| mxbai-embed-xsmall-v1 [matn] | 10ms | 78ms |
| mxbai-embed-large (Q4_K_M) [matn] | 64ms | 85ms |
| mxbai-embed-large (INT8 ONNX) [matn] | 48ms | 82ms |
| mxbai-embed-xsmall (INT8 ONNX) [matn] | 2ms | 80ms |
| mxbai-embed-xsmall (INT4 ONNX) [matn] | 7ms | 80ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large [matn]</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text [matn]</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m [matn]</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2 [matn]</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m [matn]</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8 [matn]</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4 [matn]</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1 [matn]</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M) [matn]</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX) [matn]</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX) [matn]</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX) [matn]</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ahmad 930</strong>&nbsp; 16.8779 <small>· Hasan</small><br><br>`Abdur-Razzaq said. Someone who saw `Ali when he rode told me: When he put his foot in the stirrup, he said: Bismillah (in the Name of Allah). When he</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8657 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8672<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8671 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.8100 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8443 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8545 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8408 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.8115 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8649 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8847 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8183 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8240 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>adab 667</strong>&nbsp; 15.8980 <small>· Da'if</small><br><br>The firmest supplication is to say, 'O Allah, you are my Lord and I am Your slave. I have wronged myself and I admit my wrong action. Only You forgive</td>
<td valign="top"><strong>ibnmajah 3818</strong>&nbsp; 0.8381 <small>· Hasan</small><br><br>'Abdullah bin Busr said that : the Prophet (saas) said: "Glad tidings to those who find a lot of seeking forgiveness in the record of their deeds."</td>
<td valign="top"><strong>bukhari 4644</strong>&nbsp; 0.8638<br><br>`Abdullah bin Az-Zubair said: Allah ordered His Prophet to forgive the people their misbehavior (towards him).</td>
<td valign="top"><strong>bulugh 1092</strong>&nbsp; 0.8573<br><br>al-Bazzar reported it through another chain, from Ibn 'Abbas (RA) and he added: "Make atonement and do not repeat it."</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8086 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7849 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7837 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>bulugh 1092</strong>&nbsp; 0.7759<br><br>al-Bazzar reported it through another chain, from Ibn 'Abbas (RA) and he added: "Make atonement and do not repeat it."</td>
<td valign="top"><strong>adab 465</strong>&nbsp; 0.8103 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Forgive right-acting people their slips."</td>
<td valign="top"><strong>ibnmajah 3818</strong>&nbsp; 0.8430 <small>· Hasan</small><br><br>'Abdullah bin Busr said that : the Prophet (saas) said: "Glad tidings to those who find a lot of seeking forgiveness in the record of their deeds."</td>
<td valign="top"><strong>tirmidhi 3552</strong>&nbsp; 0.8662 <small>· Da’if</small><br><br>Aishah narrated, saying: The Messenger of Allah (saws) said: “Whoever supplicates against the one who wronged him has triumphed.”</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.8024 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7990 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>adab 706</strong>&nbsp; 15.5979 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>muslim 1650 b</strong>&nbsp; 0.8373<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who took an oath and then found another thing better than (this) should e</td>
<td valign="top"><strong>mishkat 942</strong>&nbsp; 0.8569<br><br>Abu Bakr as-Siddiq said that he asked God’s Messenger to teach him a supplication to use in his prayer, and he told him to say, “O God, I have greatly</td>
<td valign="top"><strong>ibnmajah 3818</strong>&nbsp; 0.8563 <small>· Hasan</small><br><br>'Abdullah bin Busr said that : the Prophet (saas) said: "Glad tidings to those who find a lot of seeking forgiveness in the record of their deeds."</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7816<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>bulugh 1092</strong>&nbsp; 0.7793<br><br>al-Bazzar reported it through another chain, from Ibn 'Abbas (RA) and he added: "Make atonement and do not repeat it."</td>
<td valign="top"><strong>bulugh 1092</strong>&nbsp; 0.7782<br><br>al-Bazzar reported it through another chain, from Ibn 'Abbas (RA) and he added: "Make atonement and do not repeat it."</td>
<td valign="top"><strong>ibnmajah 2043</strong>&nbsp; 0.7733 <small>· Sahih</small><br><br>It was narrated from Abu Dharr Al-Ghifari that the Messenger of Allah (SAW) said: Allah has forgiven for me my nation their mistakes and forgetfulness</td>
<td valign="top"><strong>hisn 57</strong>&nbsp; 0.7835<br><br>Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfir lī maghfiratam’min `indika warḥamnī innaka 'anta ‘l-Ghafūr</td>
<td valign="top"><strong>muslim 1650 c</strong>&nbsp; 0.8398<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who took an oath and (later on) found another thing better than that, he </td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8643<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7842<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7717<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>ahmad 56</strong>&nbsp; 14.7569 <small>· Sahih</small><br><br>I heard ‘Ali say: If I heard a hadeeth from the Messenger of Allah (ﷺ), Allah benefitted me as He willed thereby. If someone else told me something fr</td>
<td valign="top"><strong>muslim 1650 c</strong>&nbsp; 0.8368<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who took an oath and (later on) found another thing better than that, he </td>
<td valign="top"><strong>hisn 57</strong>&nbsp; 0.8555<br><br>Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfir lī maghfiratam’min `indika warḥamnī innaka 'anta ‘l-Ghafūr</td>
<td valign="top"><strong>adab 463</strong>&nbsp; 0.8559 <small>· Sahih</small><br><br>Jarir ibn 'Abdullah reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Whoever is denied compassion is denied good.</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7733 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
<td valign="top"><strong>abudawud 1528</strong>&nbsp; 0.7785 <small>· Sahih</small><br><br>The aforesaid tradition has also been transmitted by Abu Musa al-Ash'ari through a different chain of narrators. This version adds: Be lenient to your</td>
<td valign="top"><strong>muslim 2612 c</strong>&nbsp; 0.7722<br><br>Abu Huraira reported Allah's Apostle (may peace be upon him) as saying: When any one of you fights with his brother, he should spare his face.</td>
<td valign="top"><strong>abudawud 1528</strong>&nbsp; 0.7729 <small>· Sahih</small><br><br>The aforesaid tradition has also been transmitted by Abu Musa al-Ash'ari through a different chain of narrators. This version adds: Be lenient to your</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7825 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
<td valign="top"><strong>muslim 1650 b</strong>&nbsp; 0.8389<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who took an oath and then found another thing better than (this) should e</td>
<td valign="top"><strong>bukhari 4644</strong>&nbsp; 0.8597<br><br>`Abdullah bin Az-Zubair said: Allah ordered His Prophet to forgive the people their misbehavior (towards him).</td>
<td valign="top"><strong>mishkat 3569</strong>&nbsp; 0.7712<br><br>‘A’isha reported the Prophet as saying, “Forgive the people of good qualities their slips, but not faults to which prescribed penalties apply.” Abu Da</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7703 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>ahmad 47, 48</strong>&nbsp; 14.1649 <small>· Sahih</small><br><br>If Heard something from the Messenger of Allah (ﷺ), Allah would benefit me thereby as He willed. Abu Bakr told me - and Abu Bakr spoke the truth - he </td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8303<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>muslim 1562 a</strong>&nbsp; 0.8528<br><br>Abu Huraira (Allah be pleased with him) reported Allah's Messenger (may peace be upon him) as saying: There was a person who gave loans to the people </td>
<td valign="top"><strong>muslim 679 c</strong>&nbsp; 0.8519<br><br>A hadith like this has been transmitted by Khufaf b. Ima' except this that he did not mention (these words):" cursing of unbelievers got a sanctions.</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7683 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>tirmidhi 3552</strong>&nbsp; 0.7742 <small>· Da’if</small><br><br>Aishah narrated, saying: The Messenger of Allah (saws) said: “Whoever supplicates against the one who wronged him has triumphed.”</td>
<td valign="top"><strong>abudawud 1528</strong>&nbsp; 0.7713 <small>· Sahih</small><br><br>The aforesaid tradition has also been transmitted by Abu Musa al-Ash'ari through a different chain of narrators. This version adds: Be lenient to your</td>
<td valign="top"><strong>muslim 2751 b</strong>&nbsp; 0.7715<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Allah, the Exalted and Glorious, said: My mercy excels My wrath.</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.7824<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>muslim 976 a</strong>&nbsp; 0.8378<br><br>Abu Huraira reported Allah's Messenger, (may peace be upon him) as saying: I sought permission to beg forgiveness for my mother, but He did not grant </td>
<td valign="top"><strong>mishkat 2901</strong>&nbsp; 0.8589<br><br>Abu Huraira said that the Prophet told of a man who used to make loans and say to his servant, “When you come to one who is in straitened circumstance</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7687 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.7653<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>ahmad 8</strong>&nbsp; 14.1250 <small>· Sahih</small><br><br>Teach me a dua that I may say in my prayer. He said: `Say: O Allah, I have wronged myself greatly and no one forgives sins but you, grant me forgivene</td>
<td valign="top"><strong>bulugh 1556</strong>&nbsp; 0.8291<br><br>Shaddad bin Aus (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “The best manner of asking for forgiveness is to say: “O Allah! You are my</td>
<td valign="top"><strong>bukhari 3375</strong>&nbsp; 0.8506<br><br>Narrated Abu Huraira: The Prophet said, "May Allah forgive Lot: He wanted to have a powerful support."</td>
<td valign="top"><strong>ibnmajah 4214</strong>&nbsp; 0.8493 <small>· Hasan</small><br><br>It was narrated from Anas bin Malik that the Messenger of Allah (saw) said: “Allah has revealed to me that you should be humble towards one another an</td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.7526<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7664 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>tirmidhi 3552</strong>&nbsp; 0.7669 <small>· Da’if</small><br><br>Aishah narrated, saying: The Messenger of Allah (saws) said: “Whoever supplicates against the one who wronged him has triumphed.”</td>
<td valign="top"><strong>tirmidhi 3552</strong>&nbsp; 0.7695 <small>· Da’if</small><br><br>Aishah narrated, saying: The Messenger of Allah (saws) said: “Whoever supplicates against the one who wronged him has triumphed.”</td>
<td valign="top"><strong>mishkat 3569</strong>&nbsp; 0.7754<br><br>‘A’isha reported the Prophet as saying, “Forgive the people of good qualities their slips, but not faults to which prescribed penalties apply.” Abu Da</td>
<td valign="top"><strong>muslim 1650 d</strong>&nbsp; 0.8350<br><br>This hadith is narrated on the authority of Suhail with the same chain of transmitters (with these words):" He should expiate for (breaking) the vow a</td>
<td valign="top"><strong>riyadussalihin 1878</strong>&nbsp; 0.8584<br><br>Anas (May Allah be pleased with him) said: I heard the Messenger of Allah (PBUH) saying, "Allah, the Exalted, has said: 'O son of Adam! I shall go on </td>
<td valign="top"><strong>mishkat 3568</strong>&nbsp; 0.7687<br><br>‘Amr b. Shu'aib, on his father’s authority, told that his grandfather, ‘Abdallah b. ‘Amr b. al-‘As, reported God’s Messenger as saying, “Forgive the i</td>
<td valign="top"><strong>ahmad 1363</strong>&nbsp; 0.7631 <small>· A Hasan Hadeeth]</small><br><br>It was narrated that ‘Ali (رضي الله عنه) said: The Messenger of Allah (رضي الله عنه) said: `Shall I not teach you some words which, if you say them yo</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>adab 673</strong>&nbsp; 14.0837 <small>· Sahih</small><br><br>One of the supplications of the Prophet, may Allah bless him and grant him peace, was 'O Allah, forgive me for my past and future wrong actions, what </td>
<td valign="top"><strong>riyadussalihin 1878</strong>&nbsp; 0.8282<br><br>Anas (May Allah be pleased with him) said: I heard the Messenger of Allah (PBUH) saying, "Allah, the Exalted, has said: 'O son of Adam! I shall go on </td>
<td valign="top"><strong>muslim 2705 a</strong>&nbsp; 0.8493<br><br>Abu Bakr reported that he said to Allah's Messenger (may peace be upon him): Teach me a supplication which I should recite in my prayer. Thereupon he </td>
<td valign="top"><strong>abudawud 4507</strong>&nbsp; 0.8485 <small>· Da'if</small><br><br>Narrated Jabir ibn Abdullah: The Prophet (saws) said: I will not forgive anyone who kills after accepting blood-wit</td>
<td valign="top"><strong>bukhari 7387, 7388</strong>&nbsp; 0.7478<br><br>Narrated `Abdullah bin `Amr: Abu Bakr As-Siddiq said to the Prophet "O Allah's Apostle! Teach me an invocation with which I may invoke Allah in my pra</td>
<td valign="top"><strong>muslim 2612 c</strong>&nbsp; 0.7658<br><br>Abu Huraira reported Allah's Apostle (may peace be upon him) as saying: When any one of you fights with his brother, he should spare his face.</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7660 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
<td valign="top"><strong>muslim 2599</strong>&nbsp; 0.7695<br><br>Abu Huraira reported it was said to Allah's Messenger (may peace be upon him): Invoke curse upon the polytheists, whereupon he said: I have not been s</td>
<td valign="top"><strong>mishkat 3568</strong>&nbsp; 0.7693<br><br>‘Amr b. Shu'aib, on his father’s authority, told that his grandfather, ‘Abdallah b. ‘Amr b. al-‘As, reported God’s Messenger as saying, “Forgive the i</td>
<td valign="top"><strong>adab 36</strong>&nbsp; 0.8302 <small>· Hasan</small><br><br>Abu Hurayra said, "The dead person can be raised a degree after his death. He said, 'My Lord, how is this?' He was told, 'Your child can ask for forgi</td>
<td valign="top"><strong>muslim 1650 b</strong>&nbsp; 0.8572<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who took an oath and then found another thing better than (this) should e</td>
<td valign="top"><strong>hisn 57</strong>&nbsp; 0.7677<br><br>Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfir lī maghfiratam’min `indika warḥamnī innaka 'anta ‘l-Ghafūr</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7607 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>adab 688</strong>&nbsp; 14.0330 <small>· Sahih</small><br><br>Abu Musa reported that the Prophet, may Allah bless him and grant him peace, used to make this supplication, "O Allah, forgive my errors, my ignorance</td>
<td valign="top"><strong>muslim 1650 d</strong>&nbsp; 0.8280<br><br>This hadith is narrated on the authority of Suhail with the same chain of transmitters (with these words):" He should expiate for (breaking) the vow a</td>
<td valign="top"><strong>ahmad 8</strong>&nbsp; 0.8491 <small>· Sahih (Darussalam) [Bukhari 834 and Muslim 2705]</small><br><br>It was narrated from Abu Bakr as Siddeeq that he said to the Messenger of Allah (ﷺ) : Teach me a dua that I may say in my prayer. He said: `Say: O All</td>
<td valign="top"><strong>tirmidhi 668</strong>&nbsp; 0.8427 <small>· Sahih</small><br><br>Ibn Umar narrated that : Umar gave a horse to be used in the cause of Allah. Then he saw it being sold, so he wanted to buy it, but the Prophet said: </td>
<td valign="top"><strong>adab 293</strong>&nbsp; 0.7463 <small>· Sahih</small><br><br>Abu Mas'ud al-Ansari reported that the Messenger of Allah, may Allah bless him and grant him peace, said, "Before your time a man was called to accoun</td>
<td valign="top"><strong>ibnmajah 2045</strong>&nbsp; 0.7649 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said : "Allah has forgiven my nation for mistakes and forgetfulness, and what they are forced t</td>
<td valign="top"><strong>muslim 2751 b</strong>&nbsp; 0.7641<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Allah, the Exalted and Glorious, said: My mercy excels My wrath.</td>
<td valign="top"><strong>adab 95</strong>&nbsp; 0.7579 <small>· Sahih</small><br><br>Abu Sa'id said that the Prophet (may Allah bless him and grant him peace) said: 'Someone who does not show mercy will not be shown mercy.'</td>
<td valign="top"><strong>adab 706</strong>&nbsp; 0.7590 <small>· Sahih</small><br><br>'Abdullah ibn 'Amr was heard to say, "Abu Bakr, may Allah be pleased with him, said to the Prophet, may Allah bless him and grant him peace, 'Teach me</td>
<td valign="top"><strong>bulugh 1556</strong>&nbsp; 0.8291<br><br>Shaddad bin Aus (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “The best manner of asking for forgiveness is to say: “O Allah! You are my</td>
<td valign="top"><strong>hisn 57</strong>&nbsp; 0.8570<br><br>Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfir lī maghfiratam’min `indika warḥamnī innaka 'anta ‘l-Ghafūr</td>
<td valign="top"><strong>abudawud 4376</strong>&nbsp; 0.7664 <small>· Sahih</small><br><br>Narrated Abdullah ibn Amr ibn al-'As: The Prophet (saws) said: Forgive the infliction of prescribed penalties among yourselves, for any prescribed pen</td>
<td valign="top"><strong>hisn 57</strong>&nbsp; 0.7601<br><br>Allāhumma ‘innī ẓalamtu nafsī ẓulman kathīran, wa lā yaghfiru-dhdhunūba illā 'anta, faghfir lī maghfiratam’min `indika warḥamnī innaka 'anta ‘l-Ghafūr</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>ahmad 28</strong>&nbsp; 14.0007 <small>· Sahih</small><br><br>Teach me a du'a` that I may say in my prayer. He said: `Say: O Allah. I have wronged myself greatly and no one forgives sins except You, so grant me f</td>
<td valign="top"><strong>muslim 976 a</strong>&nbsp; 0.8253<br><br>Abu Huraira reported Allah's Messenger, (may peace be upon him) as saying: I sought permission to beg forgiveness for my mother, but He did not grant </td>
<td valign="top"><strong>tirmidhi 1320</strong>&nbsp; 0.8489 <small>· Hasan</small><br><br>Narrated Jabir: That the Messenger of Allah (saws) said: "Allah forgave a man who was before you: He was tolerant when selling, tolerant when purchasi</td>
<td valign="top"><strong>adab 318</strong>&nbsp; 0.8423 <small>· Sahih</small><br><br>Hudhayfa said, "People do not curse one another without that curse coming true."</td>
<td valign="top"><strong>muslim 2621</strong>&nbsp; 0.7448<br><br>Jundub reported that Allah's Messenger (may peace be upon him) stated that a person said: Allah would not forgive such and such (person). Thereupon Al</td>
<td valign="top"><strong>bukhari 4644</strong>&nbsp; 0.7633<br><br>`Abdullah bin Az-Zubair said: Allah ordered His Prophet to forgive the people their misbehavior (towards him).</td>
<td valign="top"><strong>bukhari 4644</strong>&nbsp; 0.7620<br><br>`Abdullah bin Az-Zubair said: Allah ordered His Prophet to forgive the people their misbehavior (towards him).</td>
<td valign="top"><strong>muslim 2455</strong>&nbsp; 0.7575<br><br>Anas reported that Allah's Apostle (may peace be upon him) did not enter the house of any woman except that of his wives and that of Umm Sulaim. He us</td>
<td valign="top"><strong>ahmad 1363</strong>&nbsp; 0.7557 <small>· A Hasan Hadeeth]</small><br><br>It was narrated that ‘Ali (رضي الله عنه) said: The Messenger of Allah (رضي الله عنه) said: `Shall I not teach you some words which, if you say them yo</td>
<td valign="top"><strong>adab 617</strong>&nbsp; 0.8269 <small>· Sahih</small><br><br>Shaddad ibn Aws reported that the Prophet, may Allah bless him and grant him peace, said, "The best way of asking forgiveness is 'O Allah, You are my </td>
<td valign="top"><strong>tirmidhi 3540</strong>&nbsp; 0.8564 <small>· Hasan</small><br><br>Anas bin Malik narrated that the Messenger of Allah (saws) said: “Allah, Blessed is He and Most High, said: ‘O son of Adam! Verily as long as you call</td>
<td valign="top"><strong>hisn 158</strong>&nbsp; 0.7658<br><br>Allāhumma inna [name the person] fī dhimmatik, wa ḥabli jiwārik, faqihi min fitnati ‘l-qabri wa `adhābin-nār, wa anta ahlu ‘l-wafā'i wa ‘l-ḥaqq. Faghf</td>
<td valign="top"><strong>mishkat 3569</strong>&nbsp; 0.7594<br><br>‘A’isha reported the Prophet as saying, “Forgive the people of good qualities their slips, but not faults to which prescribed penalties apply.” Abu Da</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bulugh 319</strong>&nbsp; 14.0007 <small>· Uncategorized</small><br><br>He said to Allah's Messenger (SAW), "Teach me a supplication to use in my prayer." He (SAW) said, "Say: O Allah, I have greatly wronged myself, and no</td>
<td valign="top"><strong>ahmad 28</strong>&nbsp; 0.8253 <small>· Sahih (Darussalam) [Bukhari 834 and Muslim 2705]</small><br><br>It was narrated from Abu Bakr as-Siddeeq that he said to the Messenger of Allah (ﷺ): Teach me a du'a` that I may say in my prayer. He said: `Say: O Al</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8482<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>tirmidhi 2019</strong>&nbsp; 0.8419 <small>· Hasan</small><br><br>Ibn 'Umar narrated that the Messenger of Allah said: "The believer is not one who curses others."</td>
<td valign="top"><strong>ibnmajah 3817</strong>&nbsp; 0.7438 <small>· Hasan</small><br><br>It was narrated that Hudhaifah said: "I was harsh in the way I spoke to my family, but not to others. I mentioned that to the Prophet (saas) and he sa</td>
<td valign="top"><strong>muslim 2751 b</strong>&nbsp; 0.7631<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Allah, the Exalted and Glorious, said: My mercy excels My wrath.</td>
<td valign="top"><strong>adab 558</strong>&nbsp; 0.7566 <small>· Sahih</small><br><br>'A'isha reported that the Prophet, may Allah bless him and grant him peace, said, "Go ahead, take revenge."</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.7551 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>hisn 158</strong>&nbsp; 0.7550<br><br>Allāhumma inna [name the person] fī dhimmatik, wa ḥabli jiwārik, faqihi min fitnati ‘l-qabri wa `adhābin-nār, wa anta ahlu ‘l-wafā'i wa ‘l-ḥaqq. Faghf</td>
<td valign="top"><strong>bukhari 2078</strong>&nbsp; 0.8262<br><br>Narrated Abu Huraira: The Prophet said, "There was a merchant who used to lend the people, and whenever his debtor was in straitened circumstances, he</td>
<td valign="top"><strong>abudawud 4375</strong>&nbsp; 0.8560 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: The Messenger of Allah (saws) Said: Forgive the people of good qualities their slips, but not faults to which prescrib</td>
<td valign="top"><strong>ahmad 1363</strong>&nbsp; 0.7594 <small>· A Hasan Hadeeth]</small><br><br>It was narrated that ‘Ali (رضي الله عنه) said: The Messenger of Allah (رضي الله عنه) said: `Shall I not teach you some words which, if you say them yo</td>
<td valign="top"><strong>mishkat 63</strong>&nbsp; 0.7591 <small>· [{"graded_by": "Zubair `Aliza'i", "grade": "Muttafaqun 'alayh", "priority": 40}]</small><br><br>Abu Huraira reported God’s messenger as saying, “God forgives my people the evil promptings which arise within them so long as they do not act upon th</td>
</tr>
</tbody></table>

---

## englishMatn: comparing yourself to others

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 10ms |
| mxbai-embed-large [matn] | 45ms | 85ms |
| nomic-embed-text [matn] | 37ms | 82ms |
| snowflake-arctic-embed:m [matn] | 31ms | 83ms |
| all-MiniLM-L6-v2 [matn] | 33ms | 81ms |
| embeddinggemma-300m [matn] | 62ms | 80ms |
| embeddinggemma-300m-qat-q8 [matn] | 66ms | 80ms |
| embeddinggemma-300m-qat-q4 [matn] | 76ms | 80ms |
| mxbai-embed-xsmall-v1 [matn] | 10ms | 81ms |
| mxbai-embed-large (Q4_K_M) [matn] | 50ms | 83ms |
| mxbai-embed-large (INT8 ONNX) [matn] | 27ms | 83ms |
| mxbai-embed-xsmall (INT8 ONNX) [matn] | 2ms | 81ms |
| mxbai-embed-xsmall (INT4 ONNX) [matn] | 6ms | 81ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large [matn]</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text [matn]</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m [matn]</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2 [matn]</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m [matn]</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8 [matn]</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4 [matn]</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1 [matn]</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M) [matn]</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX) [matn]</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX) [matn]</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX) [matn]</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>muslim 1776 d</strong>&nbsp; 13.1936 <small>· Sahih</small><br><br>This hadith has been narrated on the authority of Bara' with another chain of transmitters, but this hadith is short as compared with other ahadith wh</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.8618<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.8435<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>ibnmajah 4179</strong>&nbsp; 0.8386 <small>· Sahih</small><br><br>It was narrated from ‘Iyad bin Himar that the Prophet (saw) addressed them and said: “Allah has revealed to me that you should be humble towards one a</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7368<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>nasai 4725</strong>&nbsp; 0.7677 <small>· Sahih</small><br><br>A similar report was narrated from 'Alqamah bin Wa'il from his father, from the Prophet. Yahya (one of the narrators) said: "He is better than him." [</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7631<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>nasai 4725</strong>&nbsp; 0.7621 <small>· Sahih</small><br><br>A similar report was narrated from 'Alqamah bin Wa'il from his father, from the Prophet. Yahya (one of the narrators) said: "He is better than him." [</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7452<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.8627<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.8920<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7452<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.7442<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>abudawud 4627</strong>&nbsp; 11.8770 <small>· Sahih</small><br><br>We used to say in the times of the Prophet (saws): We do not compare anyone with Abu Bakr. ’Umar came next and then ‘Uthman. We then would leave (rest</td>
<td valign="top"><strong>ibnmajah 4032</strong>&nbsp; 0.8138 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The believer who mixes with people and bears their annoyance with patience wil</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8433<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>forty 9</strong>&nbsp; 0.8374<br><br>Modesty is entirely good.</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7340<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7527<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>nasai 4725</strong>&nbsp; 0.7575 <small>· Sahih</small><br><br>A similar report was narrated from 'Alqamah bin Wa'il from his father, from the Prophet. Yahya (one of the narrators) said: "He is better than him." [</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7588<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7326<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
<td valign="top"><strong>ibnmajah 4179</strong>&nbsp; 0.8200 <small>· Sahih</small><br><br>It was narrated from ‘Iyad bin Himar that the Prophet (saw) addressed them and said: “Allah has revealed to me that you should be humble towards one a</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8622<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7370<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7331<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>muslim 2431</strong>&nbsp; 11.3899 <small>· Sahih</small><br><br>There are many persons amongst men who are quite perfect but there are none perfect amongst women except Mary, daughter of 'Imran, Asiya wife of Phara</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8135<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>tirmidhi 1345</strong>&nbsp; 0.8316 <small>· Sahih</small><br><br>Ja'far bin Muhammad narrated from his father: "The Prophet (saws) passed judgement based on an oath along with one witness." He said: "And 'Ali judged</td>
<td valign="top"><strong>ibnmajah 4214</strong>&nbsp; 0.8361 <small>· Hasan</small><br><br>It was narrated from Anas bin Malik that the Messenger of Allah (saw) said: “Allah has revealed to me that you should be humble towards one another an</td>
<td valign="top"><strong>muslim 2963 c</strong>&nbsp; 0.7261<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those wh</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7346<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7368<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>forty 3</strong>&nbsp; 0.7413<br><br>A Muslim is a mirror of the Muslim.</td>
<td valign="top"><strong>muslim 2963 c</strong>&nbsp; 0.7321<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those wh</td>
<td valign="top"><strong>nasai 4725</strong>&nbsp; 0.8136 <small>· Sahih</small><br><br>A similar report was narrated from 'Alqamah bin Wa'il from his father, from the Prophet. Yahya (one of the narrators) said: "He is better than him." [</td>
<td valign="top"><strong>bulugh 1438</strong>&nbsp; 0.8524<br><br>Abu Hurairah (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Look at those who are lower than you (financially) but do not look at those </td>
<td valign="top"><strong>muslim 2963 c</strong>&nbsp; 0.7332<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those wh</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7298<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bukhari 3334</strong>&nbsp; 11.2561 <small>· Sahih</small><br><br>The Prophet said, "Allah will say to that person of the (Hell) Fire who will receive the least punishment, 'If you had everything on the earth, would </td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8132<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.8211 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>adab 270</strong>&nbsp; 0.8344<br><br>Abu Ad-Darda' reported that the Prophet (saws) said, "Nothing is heavier on the scale than good character."</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7232<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
<td valign="top"><strong>adab 328</strong>&nbsp; 0.7318 <small>· Da'if</small><br><br>Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faults."</td>
<td valign="top"><strong>tirmidhi 2373</strong>&nbsp; 0.7335 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Richness is not having many possessions, but richness is being content with oneself."</td>
<td valign="top"><strong>forty 16</strong>&nbsp; 0.7407<br><br>People are like the teeth of a comb.</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7314<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
<td valign="top"><strong>ibnmajah 4032</strong>&nbsp; 0.8134 <small>· Sahih</small><br><br>It was narrated from Ibn ‘Umar that the Messenger of Allah (saw) said: “The believer who mixes with people and bears their annoyance with patience wil</td>
<td valign="top"><strong>muslim 2963 c</strong>&nbsp; 0.8480<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those wh</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7286<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>muslim 2963 a</strong>&nbsp; 0.7274<br><br>Abu Huraira reported that Allah's Messenger (may peace be upon him) said: When one of you looks at one who stands at a higher level than you in regard</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>abudawud 356</strong>&nbsp; 10.7595 <small>· Hasan</small><br><br>I have embraced Islam. The Prophet (saws) said to him: Remove from yourself the hair that grew during of unbelief, saying "shave them". He further say</td>
<td valign="top"><strong>ibnmajah 4179</strong>&nbsp; 0.8130 <small>· Sahih</small><br><br>It was narrated from ‘Iyad bin Himar that the Prophet (saw) addressed them and said: “Allah has revealed to me that you should be humble towards one a</td>
<td valign="top"><strong>nasai 3947</strong>&nbsp; 0.8171 <small>· sahih</small><br><br>It was narrated from Abu Musa that the Prophet said: "The superiority of 'Aishah to other women is like the superiority of Tharid to other kinds of fo</td>
<td valign="top"><strong>abudawud 4620</strong>&nbsp; 0.8340<br><br>Explaining the Quranic verse; “And between them and their desire is placed a barrier.” Al-Hasan said: Between them and their faith.</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7209<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.7299<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>abudawud 4013</strong>&nbsp; 0.7319 <small>· Hasan Sahih</small><br><br>The tradition mentioned above has also been transmitted by Ya'la from the Prophet (saws) through a different chain of narrators. Abu Dawud said: The f</td>
<td valign="top"><strong>adab 328</strong>&nbsp; 0.7343 <small>· Da'if</small><br><br>Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faults."</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7302<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8098<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>ibnmajah 4142</strong>&nbsp; 0.8431 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (saw) said: “Look at those who are beneath you and do not look at those who are above you, for it is</td>
<td valign="top"><strong>bukhari 7141</strong>&nbsp; 0.7270<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anyone, except in two cases: (1) A man whom Allah has given wealth and he spends it </td>
<td valign="top"><strong>muslim 2963 c</strong>&nbsp; 0.7239<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: Look at those who stand at a lower level than you but don't look at those wh</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>mishkat 6025</strong>&nbsp; 10.4603 <small>· Uncategorized</small><br><br>In the time of the Prophet, we did not compare anyone with Abu Bakr. `Umar came next and then Uthman. We would then leave the Prophet's companions wit</td>
<td valign="top"><strong>nasai 4725</strong>&nbsp; 0.8065 <small>· Sahih</small><br><br>A similar report was narrated from 'Alqamah bin Wa'il from his father, from the Prophet. Yahya (one of the narrators) said: "He is better than him." [</td>
<td valign="top"><strong>nasai 3948</strong>&nbsp; 0.8171 <small>· hasan</small><br><br>It was narrated from 'Aishah that the Prophet said: "The superiority of 'Aishah to other women is like the superiority of Tharid to other kinds of foo</td>
<td valign="top"><strong>nasai 4725</strong>&nbsp; 0.8327 <small>· Sahih</small><br><br>A similar report was narrated from 'Alqamah bin Wa'il from his father, from the Prophet. Yahya (one of the narrators) said: "He is better than him." [</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7181<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>tirmidhi 2373</strong>&nbsp; 0.7266 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Richness is not having many possessions, but richness is being content with oneself."</td>
<td valign="top"><strong>abudawud 1528</strong>&nbsp; 0.7281 <small>· Sahih</small><br><br>The aforesaid tradition has also been transmitted by Abu Musa al-Ash'ari through a different chain of narrators. This version adds: Be lenient to your</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.7330<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7209<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>bukhari 6490</strong>&nbsp; 0.8098<br><br>Narrated Abu Huraira: Allah's Apostle said, "If anyone of you looked at a person who was made superior to him in property and (in good) appearance, th</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.8370 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>bukhari 7316</strong>&nbsp; 0.7269<br><br>Narrated `Abdullah: Allah's Apostle said, "Do not wish to be like anybody except in two cases: The case of a man whom Allah has given wealth and he sp</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7213<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>mishkat 48</strong>&nbsp; 10.3950 <small>· Uncategorized</small><br><br>He also said that he asked the Prophet what was the most excellent aspect of faith, and received the reply, “That you should love for God’s sake, hate</td>
<td valign="top"><strong>ibnmajah 4214</strong>&nbsp; 0.8051 <small>· Hasan</small><br><br>It was narrated from Anas bin Malik that the Messenger of Allah (saw) said: “Allah has revealed to me that you should be humble towards one another an</td>
<td valign="top"><strong>abudawud 4627</strong>&nbsp; 0.8164 <small>· Sahih</small><br><br>Ibn ‘Umar said: We used to say in the times of the Prophet (saws): We do not compare anyone with Abu Bakr. ’Umar came next and then ‘Uthman. We then w</td>
<td valign="top"><strong>abudawud 1528</strong>&nbsp; 0.8317 <small>· Sahih</small><br><br>The aforesaid tradition has also been transmitted by Abu Musa al-Ash'ari through a different chain of narrators. This version adds: Be lenient to your</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7097<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
<td valign="top"><strong>abudawud 1528</strong>&nbsp; 0.7255 <small>· Sahih</small><br><br>The aforesaid tradition has also been transmitted by Abu Musa al-Ash'ari through a different chain of narrators. This version adds: Be lenient to your</td>
<td valign="top"><strong>adab 328</strong>&nbsp; 0.7255 <small>· Da'if</small><br><br>Ibn 'Abbas said, "When you want to mention your companion's faults, remember your own faults."</td>
<td valign="top"><strong>abudawud 625</strong>&nbsp; 0.7323 <small>· Sahih</small><br><br>Abu Hurairah said; The Messenger of Allah (may peace be upon him) was asked shout the validity of prayer in a single garment. The prophet (may peace b</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7187<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
<td valign="top"><strong>ibnmajah 4214</strong>&nbsp; 0.8088 <small>· Hasan</small><br><br>It was narrated from Anas bin Malik that the Messenger of Allah (saw) said: “Allah has revealed to me that you should be humble towards one another an</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.8336<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
<td valign="top"><strong>bukhari 73</strong>&nbsp; 0.7233<br><br>Narrated `Abdullah bin Mas`ud: The Prophet said, "Do not wish to be like anyone except in two cases. (The first is) A person, whom Allah has given wea</td>
<td valign="top"><strong>tirmidhi 2007</strong>&nbsp; 0.7192 <small>· Hasan</small><br><br>Hudhaifah narrated that the Messenger of Allah said: “Do not be a people without a will of your own, saying: 'If people treat us well, we will treat t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>muslim 2939 b</strong>&nbsp; 10.0806 <small>· Sahih</small><br><br>What did you ask? Mughira replied: I said that the people alleged that he would have a mountain load of bread and mutton and rivers of water. Thereupo</td>
<td valign="top"><strong>tirmidhi 1345</strong>&nbsp; 0.8048 <small>· Sahih</small><br><br>Ja'far bin Muhammad narrated from his father: "The Prophet (saws) passed judgement based on an oath along with one witness." He said: "And 'Ali judged</td>
<td valign="top"><strong>ibnmajah 4179</strong>&nbsp; 0.8158 <small>· Sahih</small><br><br>It was narrated from ‘Iyad bin Himar that the Prophet (saw) addressed them and said: “Allah has revealed to me that you should be humble towards one a</td>
<td valign="top"><strong>forty 16</strong>&nbsp; 0.8270<br><br>People are like the teeth of a comb.</td>
<td valign="top"><strong>muslim 816</strong>&nbsp; 0.7011<br><br>'Abdullah b. Mas'ud reported Allah's Messenger (may peace be upon him) as saying: There should be no envy but only in case of two persons: one having </td>
<td valign="top"><strong>forty 16</strong>&nbsp; 0.7240<br><br>People are like the teeth of a comb.</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.7249<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>abudawud 1528</strong>&nbsp; 0.7303 <small>· Sahih</small><br><br>The aforesaid tradition has also been transmitted by Abu Musa al-Ash'ari through a different chain of narrators. This version adds: Be lenient to your</td>
<td valign="top"><strong>ibnmajah 4142</strong>&nbsp; 0.7120 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (saw) said: “Look at those who are beneath you and do not look at those who are above you, for it is</td>
<td valign="top"><strong>ibnmajah 2171</strong>&nbsp; 0.8072 <small>· Sahih</small><br><br>It was narrated from Ibn 'Umar that the Messenger of Allah (SAW) said: "Let one of you not undersell another."[1]</td>
<td valign="top"><strong>forty 18</strong>&nbsp; 0.8332<br><br>The felicitous person takes lessons from (the actions of) others.</td>
<td valign="top"><strong>ibnmajah 4142</strong>&nbsp; 0.7157 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (saw) said: “Look at those who are beneath you and do not look at those who are above you, for it is</td>
<td valign="top"><strong>riyadussalihin 466</strong>&nbsp; 0.7182<br><br>Abu Hurairah (May allah be pleased with him) reported: Messenger of Allah (PBUH) said, "Look at those who are inferior to you and do not look at those</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 4816</strong>&nbsp; 9.8959 <small>· Sahih</small><br><br>(regarding) the Verse: 'And you have not been screening against yourself lest your ears, and your eyes and your skins should testify against you..' (4</td>
<td valign="top"><strong>ibnmajah 2171</strong>&nbsp; 0.7991 <small>· Sahih</small><br><br>It was narrated from Ibn 'Umar that the Messenger of Allah (SAW) said: "Let one of you not undersell another."[1]</td>
<td valign="top"><strong>bukhari 6061</strong>&nbsp; 0.8154<br><br>Narrated Abu Bakra: A man was mentioned before the Prophet and another man praised him greatly The Prophet said, "May Allah's Mercy be on you ! You ha</td>
<td valign="top"><strong>muslim 674 e</strong>&nbsp; 0.8263<br><br>This hadith has been narrated with the same chain of transmitters, but al-Hadra' made this addition:" They both were equal in recitation."</td>
<td valign="top"><strong>muslim 3000 b</strong>&nbsp; 0.6994<br><br>Abd al-Rahman b. Abu Bakra reported on the authority of his father that a person was mentioned in the presence of Allah's Apostle (may peace be upon h</td>
<td valign="top"><strong>abudawud 4013</strong>&nbsp; 0.7228 <small>· Hasan Sahih</small><br><br>The tradition mentioned above has also been transmitted by Ya'la from the Prophet (saws) through a different chain of narrators. Abu Dawud said: The f</td>
<td valign="top"><strong>ibnmajah 3990</strong>&nbsp; 0.7201 <small>· Sahih</small><br><br>It was narrated from ‘Abdullah bin ‘Umar that the Messenger of Allah (saw) said: “People are like a hundred camels; you can hardly find one worth ridi</td>
<td valign="top"><strong>ibnmajah 3990</strong>&nbsp; 0.7277 <small>· Sahih</small><br><br>It was narrated from ‘Abdullah bin ‘Umar that the Messenger of Allah (saw) said: “People are like a hundred camels; you can hardly find one worth ridi</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7118 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>tirmidhi 1345</strong>&nbsp; 0.7989 <small>· Sahih</small><br><br>Ja'far bin Muhammad narrated from his father: "The Prophet (saws) passed judgement based on an oath along with one witness." He said: "And 'Ali judged</td>
<td valign="top"><strong>tirmidhi 1345</strong>&nbsp; 0.8326 <small>· Sahih</small><br><br>Ja'far bin Muhammad narrated from his father: "The Prophet (saws) passed judgement based on an oath along with one witness." He said: "And 'Ali judged</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7153 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>bulugh 928</strong>&nbsp; 0.7155<br><br>A narration by Muslim has: He said, "Call someone other than me as a witness to this." He then said, "Would you like them to be equal in their kind tr</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>mishkat 2757</strong>&nbsp; 9.3983 <small>· Uncategorized</small><br><br>Yahya b. Sa'id said that God’s messenger was sitting when a grave was being dug in Medina. A man looked down into the grave and said, "What a bad-rest</td>
<td valign="top"><strong>bulugh 1438</strong>&nbsp; 0.7983<br><br>Abu Hurairah (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “Look at those who are lower than you (financially) but do not look at those </td>
<td valign="top"><strong>bulugh 1471</strong>&nbsp; 0.8146<br><br>Ibn ’Umar (RAA) narrated that the Messenger of Allah (P.B.U.H.) said, “He who imitates any people (in their actions) is considered to be one of them.”</td>
<td valign="top"><strong>ibnmajah 3211</strong>&nbsp; 0.8253 <small>· Sahih</small><br><br>It was narrated from Abu Tha’labah that the Prophet (saw) said: “Eat what your bow brings you.”</td>
<td valign="top"><strong>abudawud 4895</strong>&nbsp; 0.6987 <small>· Sahih</small><br><br>Narrated Iyad ibn Himar (al-Mujashi'i): The Prophet (saws) said: Allah has revealed to me that you must be humble, so that no one oppresses another an</td>
<td valign="top"><strong>muslim 2404 e</strong>&nbsp; 0.7215<br><br>Sa'd reported Allah's Apostle (may peace be upon him) as saying to 'Ali: Aren't you satisfied with being unto me what Aaron was unto Moses?</td>
<td valign="top"><strong>forty 16</strong>&nbsp; 0.7200<br><br>People are like the teeth of a comb.</td>
<td valign="top"><strong>abudawud 4013</strong>&nbsp; 0.7258 <small>· Hasan Sahih</small><br><br>The tradition mentioned above has also been transmitted by Ya'la from the Prophet (saws) through a different chain of narrators. Abu Dawud said: The f</td>
<td valign="top"><strong>tirmidhi 2007</strong>&nbsp; 0.7104 <small>· Hasan</small><br><br>Hudhaifah narrated that the Messenger of Allah said: “Do not be a people without a will of your own, saying: 'If people treat us well, we will treat t</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7987 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
<td valign="top"><strong>adab 159</strong>&nbsp; 0.8307<br><br>Abu'd-Darda' used to say to people. "We know you better than the veterinarian knows his animals. We recognise the best of you from the worst of you. T</td>
<td valign="top"><strong>bulugh 928</strong>&nbsp; 0.7147<br><br>A narration by Muslim has: He said, "Call someone other than me as a witness to this." He then said, "Would you like them to be equal in their kind tr</td>
<td valign="top"><strong>tirmidhi 2513</strong>&nbsp; 0.7140 <small>· Sahih</small><br><br>Abu Hurairah narrated that the Messenger of Allah (s.a.w) said: "Look to one who is lower than you, and do not look to one who is above you. For indee</td>
</tr>
</tbody></table>

---

## englishMatn: aisha

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 9ms |
| mxbai-embed-large [matn] | 41ms | 89ms |
| nomic-embed-text [matn] | 41ms | 84ms |
| snowflake-arctic-embed:m [matn] | 46ms | 81ms |
| all-MiniLM-L6-v2 [matn] | 34ms | 83ms |
| embeddinggemma-300m [matn] | 68ms | 82ms |
| embeddinggemma-300m-qat-q8 [matn] | 58ms | 82ms |
| embeddinggemma-300m-qat-q4 [matn] | 60ms | 81ms |
| mxbai-embed-xsmall-v1 [matn] | 9ms | 82ms |
| mxbai-embed-large (Q4_K_M) [matn] | 51ms | 85ms |
| mxbai-embed-large (INT8 ONNX) [matn] | 17ms | 83ms |
| mxbai-embed-xsmall (INT8 ONNX) [matn] | 2ms | 83ms |
| mxbai-embed-xsmall (INT4 ONNX) [matn] | 3ms | 83ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large [matn]</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text [matn]</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m [matn]</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2 [matn]</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m [matn]</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8 [matn]</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4 [matn]</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1 [matn]</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M) [matn]</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX) [matn]</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX) [matn]</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX) [matn]</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 1972</strong>&nbsp; 5.3097 <small>· Sahih</small><br><br>that when Saudah bint Zam'ah grew old, she gave her day to 'Aishah, and the Messenger of Allah went to 'Aishah on Saudah's day.</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8560 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
<td valign="top"><strong>muslim 512 c</strong>&nbsp; 0.7828<br><br>'Urwa b. Zubair reported: 'A'isha asked: What disrupts the prayer? We said: The woman and the ass. Upon this she remarked: Is the woman an ugly animal</td>
<td valign="top"><strong>adab 995</strong>&nbsp; 0.9191 <small>· Sahih</small><br><br>See 993.</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8134<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>tirmidhi 2846b</strong>&nbsp; 0.7615<br><br>(Another chain) from 'Aishah with the same narration.</td>
<td valign="top"><strong>tirmidhi 2846b</strong>&nbsp; 0.7683<br><br>(Another chain) from 'Aishah with the same narration.</td>
<td valign="top"><strong>muslim 2639 e</strong>&nbsp; 0.7655<br><br>Anas b. Malik reported Allah's Apostle (may peace be upon him) this hadith through another chain of transmitters but he did not make mention of the wo</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8354<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8630 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
<td valign="top"><strong>bukhari 5818</strong>&nbsp; 0.8673<br><br>Narrated Abu Burda: Aisha brought out to us a Kisa and an Izar and said, "The Prophet died while wearing these two." (Kisa, a square black piece of wo</td>
<td valign="top"><strong>bukhari 6068</strong>&nbsp; 0.8388<br><br>Narrated Al-Laith: `Aisha said "The Prophet entered upon me one day and said, 'O `Aisha! I do not think that so-and-so and so-and-so know anything of </td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8258<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>bukhari 5212</strong>&nbsp; 5.3071 <small>· Sahih</small><br><br>Sauda bint Zam`a gave up her turn to me (`Aisha), and so the Prophet used to give me (`Aisha) both my day and the day of Sauda.</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8441<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>muslim 240a</strong>&nbsp; 0.7785<br><br>Salim, the freed slave of Shaddad, said: I came to 'A'isha, the wife of the Holy Prophet (may peace be upon him), on the day when Sa'db. Abi Waqqas di</td>
<td valign="top"><strong>adab 1000</strong>&nbsp; 0.9191 <small>· Sahih</small><br><br>See 993.</td>
<td valign="top"><strong>bukhari 4751</strong>&nbsp; 0.7871<br><br>Narrated Um Ruman: Aisha's mother, When `Aisha was accused, she fell down Unconscious.</td>
<td valign="top"><strong>adab 585</strong>&nbsp; 0.7498<br><br>(As hadith above)</td>
<td valign="top"><strong>muslim 240d</strong>&nbsp; 0.7550<br><br>Salim, the freed slave of Shaddad b. al-Had said: I was in the presence of 'A'isha, and then narrated on her authority a hadith like this from the Hol</td>
<td valign="top"><strong>muslim 725 b</strong>&nbsp; 0.7558<br><br>'A'isha reported that the Apostle of Allah (may peace be upon him) said about the two (supererogatory) rak'ahs of the dawn: They are dearer to me than</td>
<td valign="top"><strong>bukhari 6068</strong>&nbsp; 0.8325<br><br>Narrated Al-Laith: `Aisha said "The Prophet entered upon me one day and said, 'O `Aisha! I do not think that so-and-so and so-and-so know anything of </td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8537<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>bukhari 4691</strong>&nbsp; 0.8647<br><br>Narrated Um Ruman: Who was `Aisha's mother: While I was with `Aisha, `Aisha got fever, whereupon the Prophet said, "Probably her fever is caused by th</td>
<td valign="top"><strong>bukhari 5363</strong>&nbsp; 0.8287<br><br>Narrated Al-Aswad bin Yazid: I asked `Aisha "What did the Prophet use to do at home?" She said, "He used to work for his family, and when he heard the</td>
<td valign="top"><strong>bukhari 4751</strong>&nbsp; 0.8212<br><br>Narrated Um Ruman: Aisha's mother, When `Aisha was accused, she fell down Unconscious.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>muslim 2046 b</strong>&nbsp; 5.3001 <small>· Sahih</small><br><br>'A'isha a family which has no dates (in their house) its members will be hungry; (or) 'A'isha the family which has no dates its members may be hungry.</td>
<td valign="top"><strong>abudawud 269</strong>&nbsp; 0.8408 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Khallas al-Hujari reported: Aisha said: I and the Messenger of Allah (saws) used to pass night in one (piece of) cloth</td>
<td valign="top"><strong>muslim 240d</strong>&nbsp; 0.7783<br><br>Salim, the freed slave of Shaddad b. al-Had said: I was in the presence of 'A'isha, and then narrated on her authority a hadith like this from the Hol</td>
<td valign="top"><strong>adab 1111</strong>&nbsp; 0.9184<br><br>See 1103.</td>
<td valign="top"><strong>bukhari 2562</strong>&nbsp; 0.7818<br><br>Narrated `Abdullah bin `Umar: Aisha wanted to buy a slave-girl in order to manumit her. The girl's masters stipulated that her Wala' would be for them</td>
<td valign="top"><strong>adab 586</strong>&nbsp; 0.7498<br><br>(As hadith above)</td>
<td valign="top"><strong>muslim 1092 d</strong>&nbsp; 0.7522<br><br>A hadith like this has been transmitted on the authority of 'A'isha (Allah be pleased with her).</td>
<td valign="top"><strong>muslim 1425 b</strong>&nbsp; 0.7473<br><br>This hadith has been narrated on the authority of Sahl b. Sa'd with a minor alteration of words, but the hadith transmitted through Za'idah (the words</td>
<td valign="top"><strong>bukhari 3768</strong>&nbsp; 0.8293<br><br>Narrated Abu Salama: `Aisha said, "Once Allah's Apostle said (to me), 'O Aish (`Aisha)! This is Gabriel greeting you.' I said, 'Peace and Allah's Merc</td>
<td valign="top"><strong>abudawud 269</strong>&nbsp; 0.8471 <small>· Sahih</small><br><br>Narrated Aisha, Ummul Mu'minin: Khallas al-Hujari reported: Aisha said: I and the Messenger of Allah (saws) used to pass night in one (piece of) cloth</td>
<td valign="top"><strong>bukhari 382</strong>&nbsp; 0.8627<br><br>Narrated Abu Salama: `Aisha the wife of the Prophet said, "I used to sleep in front o Allah's Apostle and my legs were opposite his Qibla and in prost</td>
<td valign="top"><strong>bukhari 251</strong>&nbsp; 0.8284<br><br>Narrated Abu Salama: `Aisha's brother and I went to `Aisha and he asked her about the bath of the Prophet. She brought a pot containing about a Sa` of</td>
<td valign="top"><strong>bukhari 4691</strong>&nbsp; 0.8208<br><br>Narrated Um Ruman: Who was `Aisha's mother: While I was with `Aisha, `Aisha got fever, whereupon the Prophet said, "Probably her fever is caused by th</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>bulugh 1059</strong>&nbsp; 5.2994 <small>· Uncategorized</small><br><br>Sauda (RA) daughter of Zam'ah gave away her day to 'Aishah (RA). So the Prophet (SAW) allotted a share to 'Aishah (RA) of her day and Sauda's. [Agreed</td>
<td valign="top"><strong>nasai 773</strong>&nbsp; 0.8388 <small>· Hasan</small><br><br>Khilas bin 'Amr said: "I heard Aisha (ra) say: 'The Messenger of Allah (saws), Abii Al-Qbim, and I were beneath a single blanket, and I was menstruati</td>
<td valign="top"><strong>malik 1659</strong>&nbsp; 0.7783<br><br>Malik related to me from Hisham ibn Urwa from his father that A'isha the wife of the Prophet, may Allah bless him and grant him peace, dressed Abdulla</td>
<td valign="top"><strong>adab 998</strong>&nbsp; 0.9155 <small>· Sahih</small><br><br>See 996.</td>
<td valign="top"><strong>ibnmajah 3668</strong>&nbsp; 0.7760 <small>· Sahih</small><br><br>It was narrated that Sa'sa'ah the paternal uncle of Ahnaf, said: "A woman entered upon Aisha with her two daughters, and she gave her three dates. (Th</td>
<td valign="top"><strong>muslim 1436 b</strong>&nbsp; 0.7481<br><br>This hadith has been narrated through the same chain of transmitters (with a slight variation):" He said: Until she comes back."</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7496 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>muslim 1422 d</strong>&nbsp; 0.7462<br><br>Narrated 'A'isha : 'A'isha (Allah be pleased with her) reported that Allah's Apostle (may peace be upon him) married her when she was six years old, a</td>
<td valign="top"><strong>bukhari 4691</strong>&nbsp; 0.8247<br><br>Narrated Um Ruman: Who was `Aisha's mother: While I was with `Aisha, `Aisha got fever, whereupon the Prophet said, "Probably her fever is caused by th</td>
<td valign="top"><strong>bukhari 3108</strong>&nbsp; 0.8466<br><br>Narrated Abu Burda: `Aisha brought out to us a patched wool Len garment, and she said, "(It chanced that) the soul of Allah's Apostle was taken away w</td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8624<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>bukhari 3217</strong>&nbsp; 0.8230<br><br>Narrated Abu Salama: `Aisha said that the Prophet said to her "O `Aisha' This is Gabriel and he sends his (greetings) salutations to you." `Aisha said</td>
<td valign="top"><strong>bukhari 6068</strong>&nbsp; 0.8207<br><br>Narrated Al-Laith: `Aisha said "The Prophet entered upon me one day and said, 'O `Aisha! I do not think that so-and-so and so-and-so know anything of </td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>nasai 3213</strong>&nbsp; 5.2966 <small>· Sahih</small><br><br>It was narrated from 'Aishah that the Messenger of Allah forbade celibacy.</td>
<td valign="top"><strong>bukhari 5818</strong>&nbsp; 0.8382<br><br>Narrated Abu Burda: Aisha brought out to us a Kisa and an Izar and said, "The Prophet died while wearing these two." (Kisa, a square black piece of wo</td>
<td valign="top"><strong>muslim 2446 a</strong>&nbsp; 0.7780<br><br>Anas b. Malik reported Allah's Messenger (may peace be upon him) as saying: The excellence of 'A'isha over women is like the excellence of Tharid over</td>
<td valign="top"><strong>adab 999</strong>&nbsp; 0.9155 <small>· Sahih</small><br><br>See 996.</td>
<td valign="top"><strong>bukhari 6757</strong>&nbsp; 0.7751<br><br>Narrated Ibn `Umar: That Aisha, the mother of the Believers, intended to buy a slave girl in order to manumit her. The slave girl's master said, "We a</td>
<td valign="top"><strong>forty 17</strong>&nbsp; 0.7415<br><br>Richness lies in the richness of the soul.</td>
<td valign="top"><strong>riyadussalihin 1643</strong>&nbsp; 0.7435<br><br>A similar narration was narrated on the authority of 'Aishah.</td>
<td valign="top"><strong>bulugh 1076</strong>&nbsp; 0.7455<br><br>In a narration of Ibn 'Adi, through another chain of narrators, which is Da'if (weak); it has: "Divorce, emancipation and marriage."</td>
<td valign="top"><strong>bukhari 251</strong>&nbsp; 0.8208<br><br>Narrated Abu Salama: `Aisha's brother and I went to `Aisha and he asked her about the bath of the Prophet. She brought a pot containing about a Sa` of</td>
<td valign="top"><strong>bukhari 6757</strong>&nbsp; 0.8446<br><br>Narrated Ibn `Umar: That Aisha, the mother of the Believers, intended to buy a slave girl in order to manumit her. The slave girl's master said, "We a</td>
<td valign="top"><strong>bukhari 5417</strong>&nbsp; 0.8621<br><br>Narrated `Aisha: (the wife of the Prophet) that whenever one of her relatives died, the women assembled and then dispersed (returned to their houses) </td>
<td valign="top"><strong>bukhari 3768</strong>&nbsp; 0.8224<br><br>Narrated Abu Salama: `Aisha said, "Once Allah's Apostle said (to me), 'O Aish (`Aisha)! This is Gabriel greeting you.' I said, 'Peace and Allah's Merc</td>
<td valign="top"><strong>bukhari 3411</strong>&nbsp; 0.8196<br><br>Narrated Abu Musa: Allah's Apostle said, "Many amongst men reached (the level of) perfection but none amongst the women reached this level except Asia</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>muslim 2445</strong>&nbsp; 5.2936 <small>· Sahih</small><br><br>'A'isha reported that when Allah's Messenger (may peace be upon him) set ont on a journey, he used to cast lots amongst his wives. Once this lot came </td>
<td valign="top"><strong>bukhari 3108</strong>&nbsp; 0.8363<br><br>Narrated Abu Burda: `Aisha brought out to us a patched wool Len garment, and she said, "(It chanced that) the soul of Allah's Apostle was taken away w</td>
<td valign="top"><strong>muslim 611 c</strong>&nbsp; 0.7772<br><br>'A'isha, the wife of the Apostle (may peace be upon him), said that the Messenger of Allah (may peace be upon him) said the afternoon prayer (at the t</td>
<td valign="top"><strong>adab 796</strong>&nbsp; 0.9142 <small>· Sahih</small><br><br>See 772.</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.7681 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
<td valign="top"><strong>forty 2</strong>&nbsp; 0.7408<br><br>War is deception.</td>
<td valign="top"><strong>nasai 5679</strong>&nbsp; 0.7386 <small>· Da'if</small><br><br>It was narrated from Simak, from Qirsafah, one of their womenfolk, that: 'Aishah said: "Drink but do not become intoxicated."</td>
<td valign="top"><strong>nasai 3257</strong>&nbsp; 0.7446 <small>· sahih</small><br><br>It was narrated that Abu 'Ubaidah said: "Aishah said: 'The Messenger of Allah married me when I was nine and I lived with him for nine years.'"</td>
<td valign="top"><strong>bukhari 4751</strong>&nbsp; 0.8188<br><br>Narrated Um Ruman: Aisha's mother, When `Aisha was accused, she fell down Unconscious.</td>
<td valign="top"><strong>bukhari 5818</strong>&nbsp; 0.8440<br><br>Narrated Abu Burda: Aisha brought out to us a Kisa and an Izar and said, "The Prophet died while wearing these two." (Kisa, a square black piece of wo</td>
<td valign="top"><strong>bukhari 3768</strong>&nbsp; 0.8595<br><br>Narrated Abu Salama: `Aisha said, "Once Allah's Apostle said (to me), 'O Aish (`Aisha)! This is Gabriel greeting you.' I said, 'Peace and Allah's Merc</td>
<td valign="top"><strong>bukhari 4691</strong>&nbsp; 0.8224<br><br>Narrated Um Ruman: Who was `Aisha's mother: While I was with `Aisha, `Aisha got fever, whereupon the Prophet said, "Probably her fever is caused by th</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8156<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>bukhari 5325, 5326</strong>&nbsp; 5.2910 <small>· Sahih</small><br><br>Urwa said to Aisha, "Do you know so-and-so, the daughter of Al-Hakam? Her husband divorced her irrevocably and she left (her husband's house)." `Aisha</td>
<td valign="top"><strong>tirmidhi 3889</strong>&nbsp; 0.8357 <small>· Sahih</small><br><br>Narrated 'Ammar bin Yasir: "She is his wife in the world and in the Hereafter." - meaning: 'Aishah [may Allah be pleased with her].</td>
<td valign="top"><strong>muslim 1422 d</strong>&nbsp; 0.7767<br><br>Narrated 'A'isha : 'A'isha (Allah be pleased with her) reported that Allah's Apostle (may peace be upon him) married her when she was six years old, a</td>
<td valign="top"><strong>adab 1127</strong>&nbsp; 0.9123 <small>· Hasan</small><br><br>See 1122.</td>
<td valign="top"><strong>bukhari 2169</strong>&nbsp; 0.7672<br><br>Narrated `Abdullah bin `Umar: Aisha, (mother of the faithful believers) wanted to buy a slave girl and manumit her, but her masters said that they wou</td>
<td valign="top"><strong>abudawud 4816</strong>&nbsp; 0.7391 <small>· Hasan Sahih</small><br><br>Abu Hurairah reported the Prophet (saws) as saying on the same occasion: And guiding the people on their way.</td>
<td valign="top"><strong>bukhari 4751</strong>&nbsp; 0.7380<br><br>Narrated Um Ruman: Aisha's mother, When `Aisha was accused, she fell down Unconscious.</td>
<td valign="top"><strong>tirmidhi 3889</strong>&nbsp; 0.7446 <small>· Sahih</small><br><br>Narrated 'Ammar bin Yasir: "She is his wife in the world and in the Hereafter." - meaning: 'Aishah [may Allah be pleased with her].</td>
<td valign="top"><strong>bukhari 3411</strong>&nbsp; 0.8180<br><br>Narrated Abu Musa: Allah's Apostle said, "Many amongst men reached (the level of) perfection but none amongst the women reached this level except Asia</td>
<td valign="top"><strong>bukhari 2562</strong>&nbsp; 0.8439<br><br>Narrated `Abdullah bin `Umar: Aisha wanted to buy a slave-girl in order to manumit her. The girl's masters stipulated that her Wala' would be for them</td>
<td valign="top"><strong>bukhari 6757</strong>&nbsp; 0.8589<br><br>Narrated Ibn `Umar: That Aisha, the mother of the Believers, intended to buy a slave girl in order to manumit her. The slave girl's master said, "We a</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8212<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8143<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>abudawud 1280</strong>&nbsp; 5.2892 <small>· Da'if</small><br><br>Dhakwan, the client of Aisha, reported on the authority of Aisha: The Messenger of Allah (saws) used to pray after the afternoon prayer but prohibited</td>
<td valign="top"><strong>bukhari 6757</strong>&nbsp; 0.8354<br><br>Narrated Ibn `Umar: That Aisha, the mother of the Believers, intended to buy a slave girl in order to manumit her. The slave girl's master said, "We a</td>
<td valign="top"><strong>muslim 2594 b</strong>&nbsp; 0.7761<br><br>This hadith has been reported by Miqdam b. Shuraih b. Hani with the same chain of transmitters but with this addition:" 'A'isha mounted upon a wild ca</td>
<td valign="top"><strong>adab 1249</strong>&nbsp; 0.9117 <small>· Da'if</small><br><br>See 1245.</td>
<td valign="top"><strong>bukhari 5327, 5328</strong>&nbsp; 0.7659<br><br>Narrated 'Urwa: Aisha disapproved of what Fatima used to say.'</td>
<td valign="top"><strong>muslim 2639 e</strong>&nbsp; 0.7390<br><br>Anas b. Malik reported Allah's Apostle (may peace be upon him) this hadith through another chain of transmitters but he did not make mention of the wo</td>
<td valign="top"><strong>bulugh 1006</strong>&nbsp; 0.7369<br><br>Muslim has from 'Aishah (RA): "Her husband was a slave."</td>
<td valign="top"><strong>muslim 2680 a</strong>&nbsp; 0.7434<br><br>Anas (b. Malik) reported Allah's Messenger (may peace be upon him) as saying. None of you should make a request for death because of the trouble in wh</td>
<td valign="top"><strong>bukhari 3433</strong>&nbsp; 0.8176<br><br>Narrated Abu Musa Al-Ash`ari: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid (i.e. meat and bread dish</td>
<td valign="top"><strong>nasai 773</strong>&nbsp; 0.8437 <small>· Hasan</small><br><br>Khilas bin 'Amr said: "I heard Aisha (ra) say: 'The Messenger of Allah (saws), Abii Al-Qbim, and I were beneath a single blanket, and I was menstruati</td>
<td valign="top"><strong>bukhari 6717</strong>&nbsp; 0.8580<br><br>Narrated `Aisha: that she intended to buy Barira (a slave girl) and her masters stipulated that they would have her Wala'. When `Aisha mentioned that </td>
<td valign="top"><strong>bukhari 2046</strong>&nbsp; 0.8193<br><br>Narrated `Urwa: Aisha during her menses used to comb and oil the hair of the Prophet while he used to be in I`tikaf in the mosque. He would stretch ou</td>
<td valign="top"><strong>bukhari 251</strong>&nbsp; 0.8138<br><br>Narrated Abu Salama: `Aisha's brother and I went to `Aisha and he asked her about the bath of the Prophet. She brought a pot containing about a Sa` of</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>ibnmajah 1469</strong>&nbsp; 5.2892 <small>· Sahih</small><br><br>“They used to claim that he was shrouded in Hibarah.” ‘Aishah said: “They brought a Hibarah Burd, but they did not shroud him in it.”</td>
<td valign="top"><strong>bukhari 2562</strong>&nbsp; 0.8352<br><br>Narrated `Abdullah bin `Umar: Aisha wanted to buy a slave-girl in order to manumit her. The girl's masters stipulated that her Wala' would be for them</td>
<td valign="top"><strong>muslim 1277 d</strong>&nbsp; 0.7758<br><br>'Urwa b. Zubair reported: I asked 'A'isha (Allah be pleased with her) ; the rest of the hadith is the same. And in this hadith (these words are also f</td>
<td valign="top"><strong>bukhari 5257</strong>&nbsp; 0.9103<br><br>Narrated Sahl bin Sa`d: similarly as above (182).</td>
<td valign="top"><strong>bukhari 6758</strong>&nbsp; 0.7630<br><br>Narrated Al-Aswad: Aisha said, "I bought Barira and her masters stipulated that the Wala would be for them." Aisha mentioned that to the Prophet and h</td>
<td valign="top"><strong>muslim 240d</strong>&nbsp; 0.7377<br><br>Salim, the freed slave of Shaddad b. al-Had said: I was in the presence of 'A'isha, and then narrated on her authority a hadith like this from the Hol</td>
<td valign="top"><strong>muslim 1452 c</strong>&nbsp; 0.7365<br><br>Ahadith like this is transmitted by 'A'isha through another chain of narrators.</td>
<td valign="top"><strong>mishkat 3129</strong>&nbsp; 0.7409<br><br>‘A’isha said that the Prophet married her when she was seven, she was brought to live with him when she was nine bringing her toys with her, and he di</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8166<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
<td valign="top"><strong>tirmidhi 3889</strong>&nbsp; 0.8423 <small>· Sahih</small><br><br>Narrated 'Ammar bin Yasir: "She is his wife in the world and in the Hereafter." - meaning: 'Aishah [may Allah be pleased with her].</td>
<td valign="top"><strong>bukhari 2562</strong>&nbsp; 0.8574<br><br>Narrated `Abdullah bin `Umar: Aisha wanted to buy a slave-girl in order to manumit her. The girl's masters stipulated that her Wala' would be for them</td>
<td valign="top"><strong>bukhari 4751</strong>&nbsp; 0.8154<br><br>Narrated Um Ruman: Aisha's mother, When `Aisha was accused, she fell down Unconscious.</td>
<td valign="top"><strong>shamail 173</strong>&nbsp; 0.8133 <small>· Sahih Isnād</small><br><br>Abu Musa al-Ash'ari said that the Prophet said (Allah bless him and give him peace): “The superiority of 'Aisha over all other women is like the super</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bukhari 6201</strong>&nbsp; 5.2867 <small>· Sahih</small><br><br>(the wife the Prophet) Allah's Apostle said, "O Aisha! This is Gabriel sending his greetings to you." I said, "Peace, and Allah's Mercy be on him." `A</td>
<td valign="top"><strong>ibnmajah 626</strong>&nbsp; 0.8316 <small>· Sahih</small><br><br>It was narrated from 'Urwah bin Zubair and 'Amrah bint 'Abdur-Rahman that : 'Aishah the wife of the Prophet said: "Umm Habibah Jahsh experienced prolo</td>
<td valign="top"><strong>muslim 334 b</strong>&nbsp; 0.7756<br><br>'A'isha, the wife of the Messenger of Allah (may peace be upon him) reported: Umm Habiba b. Jahsh who was the sister-in-law of the Messenger of Allah </td>
<td valign="top"><strong>nasai 4588</strong>&nbsp; 0.9096 <small>· Hasan</small><br><br>Something similar was narrated form Saeed bin Jubair. Abu 'Abdur-Rehman (An-Nasai) said: This is what I have found on this topic.</td>
<td valign="top"><strong>bukhari 1928</strong>&nbsp; 0.7625<br><br>Narrated Hisham's father: Aisha said, "Allah's Apostle used to kiss some of his wives while he was fasting," and then she smiled.</td>
<td valign="top"><strong>adab 810</strong>&nbsp; 0.7363 <small>· Sahih</small><br><br>Same with another isnad.</td>
<td valign="top"><strong>muslim 15 b</strong>&nbsp; 0.7342<br><br>A similar hadith is narrated on Jabir's authority in which the following words are added: I will do nothing more.</td>
<td valign="top"><strong>muslim 1436 b</strong>&nbsp; 0.7406<br><br>This hadith has been narrated through the same chain of transmitters (with a slight variation):" He said: Until she comes back."</td>
<td valign="top"><strong>bukhari 5419</strong>&nbsp; 0.8140<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other women is like the superiority of Tharid to other kinds of food . "</td>
<td valign="top"><strong>abudawud 2292</strong>&nbsp; 0.8413 <small>· Hasan</small><br><br>Urwah said: Aisha (Allah be pleased with her) severely objected to the tradition of Fatimah daughter of Qays. She said: Fatimah lived in a desolate ho</td>
<td valign="top"><strong>tirmidhi 3884</strong>&nbsp; 0.8572 <small>· Da'if</small><br><br>Narrated Musa bin Talhah: "I have not seen anyone clearer (in speech) than 'Aishah."</td>
<td valign="top"><strong>bukhari 5428</strong>&nbsp; 0.8142<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other ladies is like the superiority of Tharid to other kinds of food."</td>
<td valign="top"><strong>bukhari 5419</strong>&nbsp; 0.8130<br><br>Narrated Anas: The Prophet said, "The superiority of `Aisha to other women is like the superiority of Tharid to other kinds of food . "</td>
</tr>
</tbody></table>

---

## englishMatn: fasting expiation sins

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 10ms |
| mxbai-embed-large [matn] | 54ms | 85ms |
| nomic-embed-text [matn] | 42ms | 84ms |
| snowflake-arctic-embed:m [matn] | 36ms | 83ms |
| all-MiniLM-L6-v2 [matn] | 42ms | 83ms |
| embeddinggemma-300m [matn] | 83ms | 81ms |
| embeddinggemma-300m-qat-q8 [matn] | 73ms | 82ms |
| embeddinggemma-300m-qat-q4 [matn] | 79ms | 81ms |
| mxbai-embed-xsmall-v1 [matn] | 14ms | 81ms |
| mxbai-embed-large (Q4_K_M) [matn] | 58ms | 84ms |
| mxbai-embed-large (INT8 ONNX) [matn] | 27ms | 82ms |
| mxbai-embed-xsmall (INT8 ONNX) [matn] | 2ms | 82ms |
| mxbai-embed-xsmall (INT4 ONNX) [matn] | 6ms | 88ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large [matn]</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text [matn]</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m [matn]</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2 [matn]</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m [matn]</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8 [matn]</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4 [matn]</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1 [matn]</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M) [matn]</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX) [matn]</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX) [matn]</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX) [matn]</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 19.7723 <small>· Sahih</small><br><br>“Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previous year.”</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8768<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.9053 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8615 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8556<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8215 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8145 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>ibnmajah 1086</strong>&nbsp; 0.8237 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “From one Friday to the next is an expiation for whatever was committed in b</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8625<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8806<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.9067 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8511<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8528 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 19.3202 <small>· Sahih</small><br><br>“Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of the year before and the year after.”</td>
<td valign="top"><strong>muslim 233b</strong>&nbsp; 0.8651<br><br>Abu Huraira reported that the Messenger of Allah (may peace be upon him) said: The five (daily) prayers and one Friday prayer to (the next) Friday pra</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.9043 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8590 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8153<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8213 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>ibnmajah 1086</strong>&nbsp; 0.8089 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “From one Friday to the next is an expiation for whatever was committed in b</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8136 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8394 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>muslim 233b</strong>&nbsp; 0.8721<br><br>Abu Huraira reported that the Messenger of Allah (may peace be upon him) said: The five (daily) prayers and one Friday prayer to (the next) Friday pra</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.9035 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8447 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8421 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 19.2294 <small>· Uncategorized</small><br><br>The five daily (prescribed) Salat, and Friday (prayer) to the next Friday (prayer), and the fasting of Ramadan to the next Ramadan, is expiation of th</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8624 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>riyadussalihin 1250</strong>&nbsp; 0.8959<br><br>Abu Qatadah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) was asked about the observance of Saum (fasting) on the day of 'Ar</td>
<td valign="top"><strong>ibnmajah 1706</strong>&nbsp; 0.8575 <small>· Sahih</small><br><br>It was narrated from ‘Abdullah bin ‘Amr that the Messenger of Allah (saw) said: “There is no fasting for one who fasts continually.”</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8005 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>ibnmajah 1086</strong>&nbsp; 0.8153 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: “From one Friday to the next is an expiation for whatever was committed in b</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8074 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8091 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8351 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
<td valign="top"><strong>mishkat 1959</strong>&nbsp; 0.8671<br><br>He reported God’s messenger as saying, "Every [good] deed a son of Adam does will be multiplied, a good deed receiving a tenfold to seven hundredfold </td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.9025<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>ibnmajah 1730</strong>&nbsp; 0.8390 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting on the Day of ‘Arafah, I hope from Allah, expiates for the sins of t</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8379<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>riyadussalihin 1250</strong>&nbsp; 19.1035 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) was asked about the observance of Saum (fasting) on the day of 'Arafah. He said, "It is an expiation for the sins of the</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8619<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>nasai 2205</strong>&nbsp; 0.8957 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>nasai 2181</strong>&nbsp; 0.8560 <small>· Sahih</small><br><br>It was narrated that Aishah said: "The Prophet used to fast Shaban." '</td>
<td valign="top"><strong>riyadussalihin 1219</strong>&nbsp; 0.7999<br><br>Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "He who observes fasting during the month of Ramadan with Faith while </td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.8102 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.7990 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.7964 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
<td valign="top"><strong>ibnmajah 1731</strong>&nbsp; 0.8140 <small>· Da’if</small><br><br>It was narrated that Qatadah bin Nu’man said: “I heard the Messenger of Allah (saw) say: ‘Whoever fasts the Day of ‘Arafah, his sins of the previous a</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8670<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.9024 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8194 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>ibnmajah 1731</strong>&nbsp; 0.8299 <small>· Da’if</small><br><br>It was narrated that Qatadah bin Nu’man said: “I heard the Messenger of Allah (saw) say: ‘Whoever fasts the Day of ‘Arafah, his sins of the previous a</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>riyadussalihin 1252</strong>&nbsp; 18.9781 <small>· Uncategorized</small><br><br>The Messenger of Allah (PBUH) was asked about observing As-Saum (the fast) on the tenth day of Muharram, and he replied, "It is an expiation for the s</td>
<td valign="top"><strong>mishkat 1959</strong>&nbsp; 0.8613<br><br>He reported God’s messenger as saying, "Every [good] deed a son of Adam does will be multiplied, a good deed receiving a tenfold to seven hundredfold </td>
<td valign="top"><strong>nasai 2204</strong>&nbsp; 0.8957 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>nasai 2339</strong>&nbsp; 0.8550 <small>· Sahih</small><br><br>It was narrated that Hafsah said: "There is no fast for the one who does not intend to fast before dawn.</td>
<td valign="top"><strong>bulugh 441</strong>&nbsp; 0.7984<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said: "The best of my followers are those who, having done evil, ask for forgiveness (from Allah); and wh</td>
<td valign="top"><strong>nasai 2204</strong>&nbsp; 0.8064 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7950<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>nasai 2204</strong>&nbsp; 0.7890 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8119<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8646 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8939<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8152<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8240<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 18.0183 <small>· Sahih</small><br><br>The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward for it; and the smell wh</td>
<td valign="top"><strong>tirmidhi 683</strong>&nbsp; 0.8602 <small>· Hasan</small><br><br>Abu Hurairah narrated that : the Messenger of Allah said: "Whoever fasts Ramadan and stands (in the night prayer) for it out of faith and seeking a re</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.8923<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>ibnmajah 1738</strong>&nbsp; 0.8548 <small>· Sahih</small><br><br>It was narrated from Abu Qatadah that the Messenger of Allah (saw) said: “Fasting the day of ‘Ashura’, I hope, will expiate for the sins of the previo</td>
<td valign="top"><strong>bukhari 7538</strong>&nbsp; 0.7910<br><br>Narrated Abu Huraira: The Prophet said that your Lord said, "Every (sinful) deed can be expiated; and the fast is for Me, so I will give the reward fo</td>
<td valign="top"><strong>nasai 2205</strong>&nbsp; 0.8045 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.7920<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>nasai 2205</strong>&nbsp; 0.7884 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8109 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>ibnmajah 4210</strong>&nbsp; 0.8642 <small>· Da’if</small><br><br>It was narrated from Anas that the Messenger of Allah (saw) said: “Envy consumes good deeds just as fire consumes wood, and charity extinguishes bad d</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8938<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8101 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8236 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>muslim 1162 b</strong>&nbsp; 15.3458 <small>· Sahih</small><br><br>Abu Qatada al-Ansari (Allah be pleased with him) reported that the Messenger of Allah (may peace be upon him) was asked about his fasting. The Messeng</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8597<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>riyadussalihin 1252</strong>&nbsp; 0.8907<br><br>Abu Qatadah (May Allah be pleased with him) reported: The Messenger of Allah (PBUH) was asked about observing As-Saum (the fast) on the tenth day of M</td>
<td valign="top"><strong>muslim 233b</strong>&nbsp; 0.8538<br><br>Abu Huraira reported that the Messenger of Allah (may peace be upon him) said: The five (daily) prayers and one Friday prayer to (the next) Friday pra</td>
<td valign="top"><strong>bukhari 1894</strong>&nbsp; 0.7881<br><br>Narrated Abu Huraira: Allah's Apostle said, "Fasting is a shield (or a screen or a shelter). So, the person observing fasting should avoid sexual rela</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.8012<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.7915<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.7883<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8089<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>tirmidhi 683</strong>&nbsp; 0.8631 <small>· Hasan</small><br><br>Abu Hurairah narrated that : the Messenger of Allah said: "Whoever fasts Ramadan and stands (in the night prayer) for it out of faith and seeking a re</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8928 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>ibnmajah 1731</strong>&nbsp; 0.8099 <small>· Da’if</small><br><br>It was narrated that Qatadah bin Nu’man said: “I heard the Messenger of Allah (saw) say: ‘Whoever fasts the Day of ‘Arafah, his sins of the previous a</td>
<td valign="top"><strong>riyadussalihin 1219</strong>&nbsp; 0.8221<br><br>Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "He who observes fasting during the month of Ramadan with Faith while </td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>bulugh 680</strong>&nbsp; 14.3741 <small>· Uncategorized</small><br><br>Abu Qatadah Al-Ansari (RAA) narrated, ‘The Messenger of Allah (P.B.U.H.) was asked about fasting on the day of Arafah (the 9th of the month of Dhul Hi</td>
<td valign="top"><strong>ibnmajah 1641</strong>&nbsp; 0.8586 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (saw) said: ‘Whoever fasts Ramadan out of faith and the hope of reward will be forgiven </td>
<td valign="top"><strong>tirmidhi 683</strong>&nbsp; 0.8903 <small>· Hasan</small><br><br>Abu Hurairah narrated that : the Messenger of Allah said: "Whoever fasts Ramadan and stands (in the night prayer) for it out of faith and seeking a re</td>
<td valign="top"><strong>abudawud 3271</strong>&nbsp; 0.8520 <small>· Sahih</small><br><br>A similar tradition has also been transmitted by 'Abd al-Rahman b. Abi Bakr through a different chain of narrators. This version adds on the authority</td>
<td valign="top"><strong>ibnmajah 428</strong>&nbsp; 0.7881 <small>· Hasan</small><br><br>It was narrated from Abu Hurairah that: The Prophet said: "Sins are expiated by well-performed ablution despite difficulties, increasing the number of</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.8003<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>nasai 2204</strong>&nbsp; 0.7906 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>riyadussalihin 1149</strong>&nbsp; 0.7882<br><br>Abu Hurairah (May Allah be pleased with him)reported: The Prophet (PBUH) said, "The five daily (prescribed) Salat, and Friday (prayer) to the next Fri</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8025 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>muslim 1145 a</strong>&nbsp; 0.8612<br><br>Salama b. Akwa' (Allah be pleased with him) reported that when this verse was revealed: "And as for those who can fast (but do not) expiation is the f</td>
<td valign="top"><strong>mishkat 1958</strong>&nbsp; 0.8925<br><br>Abu Huraira reported God's messenger as saying, "He who fasts during Ramadan with faith and seeking his reward from God will have his past sins forgiv</td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.8095 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8183 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>tirmidhi 3549</strong>&nbsp; 14.0407 <small>· Uncategorized</small><br><br>“Ishaq bin Mansur narrated to us, from Isra’il” with this (Another chain) Bilal narrated that the Messenger of Allah (saws) said: “Hold fast to Qiyam </td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.8584<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.8901<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>abudawud 4347</strong>&nbsp; 0.8502 <small>· Sahih</small><br><br>A man from among the companions of the prophet (saws) reported him as saying: The people will not perish until their sins and faults become abundant, </td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.7847<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
<td valign="top"><strong>nasai 2199</strong>&nbsp; 0.7993 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah said: "Whoever spends the nights of Ramadan in prayer (Qiyam) out of faith and in the ho</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.7885<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>bukhari 38</strong>&nbsp; 0.7876<br><br>Narrated Abu Huraira: Allah's Apostle said, "Whoever observes fasts during the month of Ramadan out of sincere faith, and hoping to attain Allah's rew</td>
<td valign="top"><strong>riyadussalihin 1219</strong>&nbsp; 0.8003<br><br>Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "He who observes fasting during the month of Ramadan with Faith while </td>
<td valign="top"><strong>nasai 2203</strong>&nbsp; 0.8608 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts in Ramadan out of faith and in the hope of reward, he will be forgiven his pre</td>
<td valign="top"><strong>tirmidhi 683</strong>&nbsp; 0.8921 <small>· Hasan</small><br><br>Abu Hurairah narrated that : the Messenger of Allah said: "Whoever fasts Ramadan and stands (in the night prayer) for it out of faith and seeking a re</td>
<td valign="top"><strong>riyadussalihin 1219</strong>&nbsp; 0.8083<br><br>Abu Hurairah (May Allah be pleased with him) reported: The Prophet (PBUH) said, "He who observes fasting during the month of Ramadan with Faith while </td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.8101 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>bukhari 415</strong>&nbsp; 13.7088 <small>· Sahih</small><br><br>The Prophet said, "Spitting in the mosque is a sin and its expiation is to bury it."</td>
<td valign="top"><strong>ibnmajah 4210</strong>&nbsp; 0.8575 <small>· Da’if</small><br><br>It was narrated from Anas that the Messenger of Allah (saw) said: “Envy consumes good deeds just as fire consumes wood, and charity extinguishes bad d</td>
<td valign="top"><strong>nasai 2202</strong>&nbsp; 0.8841 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet said: "Whoever fasts during Ramadan" and according to the Hadith of Qutaibah, the Prophet said: "Wh</td>
<td valign="top"><strong>muslim 679 c</strong>&nbsp; 0.8494<br><br>A hadith like this has been transmitted by Khufaf b. Ima' except this that he did not mention (these words):" cursing of unbelievers got a sanctions.</td>
<td valign="top"><strong>tirmidhi 764</strong>&nbsp; 0.7841 <small>· Sahih</small><br><br>Abu Hurairah narrated that: The Messenger of Allah said: "Indeed your Lord said: 'Every good deed is rewarded with ten of the same up to seven hundred</td>
<td valign="top"><strong>nasai 2191</strong>&nbsp; 0.7993 <small>· Sahih</small><br><br>It was narrated from Saeed bin Al-Musayyab that the Messenger of Allah said: "Whoever spends the nights of Ramadan in prayer (Qiyam) out of faith and </td>
<td valign="top"><strong>nasai 2205</strong>&nbsp; 0.7880 <small>· Sahih</small><br><br>It was narrated that Abu Hurairah said: "The Messenger of Allah said: 'Whoever fasts Ramadan out of faith and in the hope of reward, he will be forgiv</td>
<td valign="top"><strong>muslim 1886 a</strong>&nbsp; 0.7861<br><br>It has been reported on the authority of 'Amr b. al-'As that the Messenger of Allah (may peace be upon him) said: All the sins of a Shahid (martyr) ar</td>
<td valign="top"><strong>ibnmajah 1326</strong>&nbsp; 0.7999 <small>· Hasan</small><br><br>It was narrated that Abu Hurairah said: “The Messenger of Allah (saw) said: ‘Whoever fasts Ramadan and spends its nights in prayer, out of faith and i</td>
<td valign="top"><strong>muslim 760 a</strong>&nbsp; 0.8603<br><br>Abu Huraira reported Allah's Messenger (may peace be upon him) as saying: He who observed the fasts of Ramadan with faith and seeking reward (from All</td>
<td valign="top"><strong>bukhari 2014</strong>&nbsp; 0.8896<br><br>Narrated Abu Huraira: The Prophet said, "Whoever fasted the month of Ramadan out of sincere Faith (i.e. belief) and hoping for a reward from Allah, th</td>
<td valign="top"><strong>ibnmajah 428</strong>&nbsp; 0.8018 <small>· Hasan</small><br><br>It was narrated from Abu Hurairah that: The Prophet said: "Sins are expiated by well-performed ablution despite difficulties, increasing the number of</td>
<td valign="top"><strong>bukhari 1976</strong>&nbsp; 0.8098<br><br>Narrated `Abdullah bin `Amr: Allah's Apostle was informed that I had taken an oath to fast daily and to pray (every night) all the night throughout my</td>
</tr>
</tbody></table>

---

## englishMatn: neighbor rights

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 8ms |
| mxbai-embed-large [matn] | 39ms | 82ms |
| nomic-embed-text [matn] | 40ms | 83ms |
| snowflake-arctic-embed:m [matn] | 35ms | 83ms |
| all-MiniLM-L6-v2 [matn] | 31ms | 82ms |
| embeddinggemma-300m [matn] | 72ms | 82ms |
| embeddinggemma-300m-qat-q8 [matn] | 73ms | 80ms |
| embeddinggemma-300m-qat-q4 [matn] | 71ms | 81ms |
| mxbai-embed-xsmall-v1 [matn] | 29ms | 85ms |
| mxbai-embed-large (Q4_K_M) [matn] | 46ms | 84ms |
| mxbai-embed-large (INT8 ONNX) [matn] | 20ms | 81ms |
| mxbai-embed-xsmall (INT8 ONNX) [matn] | 2ms | 82ms |
| mxbai-embed-xsmall (INT4 ONNX) [matn] | 5ms | 84ms |

<table width="100%"><thead><tr>
<th width="2%">#</th>
<th width="7%"><strong>BM25 Lexical</strong><br><small>— · no encoding · query_string</small></th>
<th width="7%"><strong>mxbai-embed-large [matn]</strong><br><small>1024-dim · 335M · F16</small></th>
<th width="7%"><strong>nomic-embed-text [matn]</strong><br><small>768-dim · 137M · Ollama</small></th>
<th width="7%"><strong>snowflake-arctic-embed:m [matn]</strong><br><small>768-dim · 110M · Ollama</small></th>
<th width="7%"><strong>all-MiniLM-L6-v2 [matn]</strong><br><small>384-dim · 22M · Ollama</small></th>
<th width="7%"><strong>embeddinggemma-300m [matn]</strong><br><small>768-dim · 300M · base</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q8 [matn]</strong><br><small>768-dim · 300M · QAT-Q8</small></th>
<th width="7%"><strong>embeddinggemma-300m-qat-q4 [matn]</strong><br><small>768-dim · 300M · QAT-Q4</small></th>
<th width="7%"><strong>mxbai-embed-xsmall-v1 [matn]</strong><br><small>384-dim · 33M · ST</small></th>
<th width="7%"><strong>mxbai-embed-large (Q4_K_M) [matn]</strong><br><small>1024-dim · 335M · Q4_K_M</small></th>
<th width="7%"><strong>mxbai-embed-large (INT8 ONNX) [matn]</strong><br><small>1024-dim · 335M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT8 ONNX) [matn]</strong><br><small>384-dim · 33M · INT8</small></th>
<th width="7%"><strong>mxbai-embed-xsmall (INT4 ONNX) [matn]</strong><br><small>384-dim · 33M · INT4</small></th>
</tr></thead><tbody>
<tr>
<td align="center" valign="top"><strong>1</strong></td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 14.2937 <small>· Da'if</small><br><br>“The neighbor has more right to preemption of his neighbor, so let him wait for him even if he is absent, if they share a path.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.9243 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.9165 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8986 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8462<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8528 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8517 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8579 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8554 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.9273 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.9286 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8620 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8574 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
</tr>
<tr>
<td align="center" valign="top"><strong>2</strong></td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 13.8410 <small>· Sahih</small><br><br>“I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has neighbors?' He said: 'The neighbor has more rig</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.8731 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8928<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8665<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8334<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8156<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8175<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8082<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8490<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.8747 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.8856 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8490<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8427<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
</tr>
<tr>
<td align="center" valign="top"><strong>3</strong></td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 13.8410 <small>· Sahih</small><br><br>"O Messenger of Allah, not one else has any share in my land, but there are neighbors." He said: "The neighbor has more right to property that is near</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8598<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8906 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>abudawud 4620</strong>&nbsp; 0.8348<br><br>Explaining the Quranic verse; “And between them and their desire is placed a barrier.” Al-Hasan said: Between them and their faith.</td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 0.8135 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Prophet (SAW) said: “The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7972<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7962 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8064<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8387<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8570<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8805 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8399<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
<td valign="top"><strong>bulugh 903</strong>&nbsp; 0.8266<br><br>Narrated Jabir (RA): Allah's Messenger (SAW) said, "The neighbor is most entitled to the right of option to buy his neighbor's property, and its exerc</td>
</tr>
<tr>
<td align="center" valign="top"><strong>4</strong></td>
<td valign="top"><strong>nasai 4705</strong>&nbsp; 13.7818 <small>· Sahih</small><br><br>"The Messenger of Allah decreed the principle of pre-emption, and the (rights of) neighbors."</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8564<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.8725 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>bulugh 1076</strong>&nbsp; 0.8330<br><br>In a narration of Ibn 'Adi, through another chain of narrators, which is Da'if (weak); it has: "Divorce, emancipation and marriage."</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8009<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7904 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.7941<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7927 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8142<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8537<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8701 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.8109 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8099<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
</tr>
<tr>
<td align="center" valign="top"><strong>5</strong></td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 13.6682 <small>· Hasan</small><br><br>that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8498 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8694 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.8320 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>mishkat 2967</strong>&nbsp; 0.7791<br><br>Jabir reported God’s Messenger as saying, “The neighbour is most entitled to the right of option and its exercise should be waited for even if he is a</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7854 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7848 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7911 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7902 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8476 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8699<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 0.8036<br><br>It was narrated that Abu Rafi said: "The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.7958 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
</tr>
<tr>
<td align="center" valign="top"><strong>6</strong></td>
<td valign="top"><strong>nasai 4702</strong>&nbsp; 13.5564 <small>· Uncategorized</small><br><br>"The Messenger of Allah said" "The neighbor has more right to property that is near."'</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8482 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.8675 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2498</strong>&nbsp; 0.8281 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Messenger of Allah (SAW) said: “The partner has more right to what is near him, so long as he is still a partn</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7729 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>ibnmajah 2498</strong>&nbsp; 0.7763 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Messenger of Allah (SAW) said: “The partner has more right to what is near him, so long as he is still a partn</td>
<td valign="top"><strong>ibnmajah 2498</strong>&nbsp; 0.7744 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Messenger of Allah (SAW) said: “The partner has more right to what is near him, so long as he is still a partn</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7829 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.7874 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.8445 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.8666 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>ibnmajah 2496</strong>&nbsp; 0.7873 <small>· Sahih</small><br><br>It was narrated that Sharid bin Suwaid said: “I said: 'O Messenger of Allah, (what do you think of) land owned by only one person but this land has ne</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7842 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
</tr>
<tr>
<td align="center" valign="top"><strong>7</strong></td>
<td valign="top"><strong>ibnmajah 2495</strong>&nbsp; 13.5564 <small>· Sahih</small><br><br>“The neighbor has more right to property that is near.”</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8381<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8575<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>abudawud 3609</strong>&nbsp; 0.8280 <small>· Sahih Maqtu'</small><br><br>The tradition mentioned above has also been transmitted by 'Amr bin Dinar through a different chain of narrators and to the same effect. Salamah has i</td>
<td valign="top"><strong>abudawud 3517</strong>&nbsp; 0.7691 <small>· Sahih</small><br><br>Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or land of the neighbour.</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7742 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7724 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7768 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>mishkat 2967</strong>&nbsp; 0.7857<br><br>Jabir reported God’s Messenger as saying, “The neighbour is most entitled to the right of option and its exercise should be waited for even if he is a</td>
<td valign="top"><strong>ibnmajah 2493</strong>&nbsp; 0.8357 <small>· Sahih</small><br><br>It was narrated from Ibn Abbas that the Prophet (SAW) said: “Whoever has land and wants to sell it, let him offer it to his neighbor.”</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8626<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7858 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7799 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>8</strong></td>
<td valign="top"><strong>bukhari 6981</strong>&nbsp; 13.2157 <small>· Sahih</small><br><br>Abu Rafi` sold a house to Sa`d bin Malik for four-hundred Mithqal of gold, and said, "If I had not heard the Prophet saying, 'The neighbor has more ri</td>
<td valign="top"><strong>mishkat 2967</strong>&nbsp; 0.8375<br><br>Jabir reported God’s Messenger as saying, “The neighbour is most entitled to the right of option and its exercise should be waited for even if he is a</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8485<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>ibnmajah 3717</strong>&nbsp; 0.8271 <small>· Sahih</small><br><br>It was narrated from Abu Hurairah that the Prophet(SAW) said: "When one of you gets up from his spot, then comes back, he has more right to it."</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7665 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.7689<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7687 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>ibnmajah 2498</strong>&nbsp; 0.7762 <small>· Sahih</small><br><br>It was narrated from Abu Rafi' that the Messenger of Allah (SAW) said: “The partner has more right to what is near him, so long as he is still a partn</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7794 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>mishkat 2967</strong>&nbsp; 0.8347<br><br>Jabir reported God’s Messenger as saying, “The neighbour is most entitled to the right of option and its exercise should be waited for even if he is a</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.8612<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7834 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>ibnmajah 2493</strong>&nbsp; 0.7783 <small>· Sahih</small><br><br>It was narrated from Ibn Abbas that the Prophet (SAW) said: “Whoever has land and wants to sell it, let him offer it to his neighbor.”</td>
</tr>
<tr>
<td align="center" valign="top"><strong>9</strong></td>
<td valign="top"><strong>bukhari 6978</strong>&nbsp; 13.0867 <small>· Sahih</small><br><br>Abu Rafi' said that Sa'd offered him four hundred Mithqal of gold for a house. Abu Rafi ' said, "If I had not heard Allah's Apostle saying, 'A neighbo</td>
<td valign="top"><strong>ibnmajah 2493</strong>&nbsp; 0.8326 <small>· Sahih</small><br><br>It was narrated from Ibn Abbas that the Prophet (SAW) said: “Whoever has land and wants to sell it, let him offer it to his neighbor.”</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8472 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>ibnmajah 74</strong>&nbsp; 0.8266 <small>· Da'if</small><br><br>It was narrated that Abu Hurairah and Ibn 'Abbas said: "Faith increases and decreases."</td>
<td valign="top"><strong>ibnmajah 2494</strong>&nbsp; 0.7578 <small>· Da'if</small><br><br>It was narrated from Jabir that the Messenger of Allah (SAW) said: “The neighbor has more right to preemption of his neighbor, so let him wait for him</td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 0.7685 <small>· Hasan</small><br><br>Narrated Jabir: that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, </td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.7683<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.7748<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>nasai 4703</strong>&nbsp; 0.7763 <small>· Sahih</small><br><br>It was narrated from 'Amr Bin Ash-Sharid, from his father, that a man said: "O Messenger of Allah, not one else has any share in my land, but there ar</td>
<td valign="top"><strong>bulugh 901</strong>&nbsp; 0.8322<br><br>Narrated Abu Rafi' (RA): Allah's Messenger (SAW) said, "The neighbor has more right (to be given preference) to the property which is near to him." [a</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.8599 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>mishkat 2967</strong>&nbsp; 0.7786<br><br>Jabir reported God’s Messenger as saying, “The neighbour is most entitled to the right of option and its exercise should be waited for even if he is a</td>
<td valign="top"><strong>abudawud 3517</strong>&nbsp; 0.7756 <small>· Sahih</small><br><br>Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or land of the neighbour.</td>
</tr>
<tr>
<td align="center" valign="top"><strong>10</strong></td>
<td valign="top"><strong>tirmidhi 1369</strong>&nbsp; 12.8224 <small>· Hasan</small><br><br>that the Messenger of Allah (saws) said: "The neighbor has more right to his preemption. He is to be waited for even if he is absent, when their paths</td>
<td valign="top"><strong>abudawud 3518</strong>&nbsp; 0.8314 <small>· Sahih</small><br><br>Narrated Jabir ibn Abdullah: The Prophet (saws) said: The neighbour is most entitled to the right of pre-emption, and he should wait for its exercise </td>
<td valign="top"><strong>mishkat 2967</strong>&nbsp; 0.8458<br><br>Jabir reported God’s Messenger as saying, “The neighbour is most entitled to the right of option and its exercise should be waited for even if he is a</td>
<td valign="top"><strong>ibnmajah 75</strong>&nbsp; 0.8266 <small>· Da'if</small><br><br>It was narrated that Abu Darda' said: "Faith increases and decreases."</td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7547 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>ibnmajah 2422</strong>&nbsp; 0.7671 <small>· Hasan</small><br><br>It was narrated from Abu Hurairah that the Messenger of Allah (SAW) said to the one who was entitled to something: “Take your rights in a decent manne</td>
<td valign="top"><strong>nasai 4705</strong>&nbsp; 0.7603 <small>· Sahih</small><br><br>It was narrated that Jabir said: "The Messenger of Allah decreed the principle of pre-emption, and the (rights of) neighbors."</td>
<td valign="top"><strong>abudawud 3516</strong>&nbsp; 0.7683 <small>· Sahih</small><br><br>Narrated Abu Rafi': The Messenger of Allah (saws) as saying: A neighbor has the best claim to the house or land of the neighbor.</td>
<td valign="top"><strong>abudawud 3517</strong>&nbsp; 0.7728 <small>· Sahih</small><br><br>Narrated Samurah: The Prophet (saws) said: A neighbour has the best claim to the house or land of the neighbour.</td>
<td valign="top"><strong>ibnmajah 2337</strong>&nbsp; 0.8308 <small>· Sahih</small><br><br>It was narrated from Ibn 'Abbas that the Prophet (SAW) said: “No one of you should refuse to let his neighbor fix a piece of wood to his wall.”</td>
<td valign="top"><strong>abudawud 3518</strong>&nbsp; 0.8580 <small>· Sahih</small><br><br>Narrated Jabir ibn Abdullah: The Prophet (saws) said: The neighbour is most entitled to the right of pre-emption, and he should wait for its exercise </td>
<td valign="top"><strong>tirmidhi 1368</strong>&nbsp; 0.7697 <small>· Hasan</small><br><br>Narrated Samurah: that the Messenger of Allah (saws) said: "The neighbor of a home has more right to the home."</td>
<td valign="top"><strong>muslim 47 c</strong>&nbsp; 0.7699<br><br>Another hadith similar to one narrated (above) by Abu Husain is also reported by Abu Huraira with the exception of these words: He (the Prophet) said:</td>
</tr>
</tbody></table>

---

*Generated by `tests/small_model_comparison.py` · pool=50 · N=10*

# Small Model Comparison — HF Serverless API

HuggingFace Serverless Inference API — GPU-backed, latency includes network round-trip.
Latency summary only (no result tables). Vectors queried against `small-model-eval`.

**Filters & boosts**

| Setting | Status |
|---|---|
| `isChainRef` exclusion | **ON** — chain-reference hadiths excluded from results |
| Dedup by `dupGroup` | **ON** — highest collection-boosted member wins per group |
| Collection boosts | **ON** — bukhari 5×, muslim 4.8×, nawawi40 3.3×, malik/ahmad/riyadussalihin 2.5×, nasai 3.5×, abudawud 3×, tirmidhi 2.5×, ibnmajah/darimi/mishkat 2× |
| Embed times | Post-warmup — models loaded into memory before measurement |

---

## HF Serverless API: good character and manners

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 15ms |
| mxbai-embed-large (HF API) | 232ms | 102ms |
| snowflake-arctic-embed:m (HF API) | 4423ms | 99ms |
| all-MiniLM-L6-v2 (HF API) | 177ms | 97ms |

---

## HF Serverless API: angels recording deeds

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 12ms |
| mxbai-embed-large (HF API) | 197ms | 100ms |
| snowflake-arctic-embed:m (HF API) | 192ms | 97ms |
| all-MiniLM-L6-v2 (HF API) | 184ms | 93ms |

---

## HF Serverless API: prayer at night

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 15ms |
| mxbai-embed-large (HF API) | 228ms | 102ms |
| snowflake-arctic-embed:m (HF API) | 211ms | 91ms |
| all-MiniLM-L6-v2 (HF API) | 186ms | 98ms |

---

## HF Serverless API: forgiving someone who wronged you

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 13ms |
| mxbai-embed-large (HF API) | 224ms | 103ms |
| snowflake-arctic-embed:m (HF API) | 199ms | 95ms |
| all-MiniLM-L6-v2 (HF API) | 174ms | 96ms |

---

## HF Serverless API: comparing yourself to others

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 10ms |
| mxbai-embed-large (HF API) | 259ms | 103ms |
| snowflake-arctic-embed:m (HF API) | 199ms | 98ms |
| all-MiniLM-L6-v2 (HF API) | 196ms | 98ms |

---

## HF Serverless API: aisha

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 9ms |
| mxbai-embed-large (HF API) | 198ms | 92ms |
| snowflake-arctic-embed:m (HF API) | 179ms | 93ms |
| all-MiniLM-L6-v2 (HF API) | 189ms | 98ms |

---

## HF Serverless API: fasting expiation sins

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 10ms |
| mxbai-embed-large (HF API) | 204ms | 90ms |
| snowflake-arctic-embed:m (HF API) | 207ms | 99ms |
| all-MiniLM-L6-v2 (HF API) | 190ms | 94ms |

---

## HF Serverless API: neighbor rights

| Model | Embed | ES search |
|---|---|---|
| BM25 Lexical | — | 8ms |
| mxbai-embed-large (HF API) | 209ms | 95ms |
| snowflake-arctic-embed:m (HF API) | 193ms | 98ms |
| all-MiniLM-L6-v2 (HF API) | 162ms | 91ms |

---

*Generated by `tests/small_model_comparison.py` · pool=50 · N=10*
