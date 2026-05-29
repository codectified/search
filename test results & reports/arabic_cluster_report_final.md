# Final Arabic Matn Cluster Report

Model: OpenAI text-embedding-3-small (1536-dim)
k=75, MiniBatchKMeans, L2-normalized
Corpus: 131,728 hadiths
Vector quality: 89,332 editorial tags | 30,104 regex-extracted (v3) | 12,292 full-text
Avg cohesion: 0.638 | Avg cluster size: 1,756

| Cluster | Size | Cohesion | EdTag% | V3% | Top Collections |
|---|---|---|---|---|---|
| 54 | 3548 | 0.630 | 6% | 7% | mishkat(2004), riyadussalihin(528), bulugh(452) |
| 19 | 3192 | 0.652 | 72% | 17% | hakim(589), ibnabishayba(515), bukhari(389) |
| 6 | 3035 | 0.557 | 97% | 2% | ibnabishayba(1668), abdurrazzaq(637), daraqutni(175) |
| 57 | 2972 | 0.591 | 82% | 17% | ibnabishayba(1076), abdurrazzaq(574), hakim(211) |
| 74 | 2810 | 0.636 | 63% | 25% | bukhari(457), ibnabishayba(385), abdurrazzaq(305) |
| 62 | 2772 | 0.648 | 47% | 22% | mishkat(501), bukhari(284), hakim(284) |
| 12 | 2753 | 0.593 | 82% | 17% | ibnabishayba(924), abdurrazzaq(414), ibnhibban(238) |
| 23 | 2736 | 0.689 | 0% | 99% | muslim(789), nasai(675), abudawud(566) |
| 9 | 2649 | 0.654 | 87% | 11% | ibnabishayba(980), abdurrazzaq(542), daraqutni(173) |
| 40 | 2554 | 0.590 | 87% | 11% | ibnabishayba(984), abdurrazzaq(607), ibnhibban(135) |
| 34 | 2536 | 0.640 | 93% | 6% | ibnabishayba(1423), abdurrazzaq(697), hakim(62) |
| 5 | 2528 | 0.653 | 65% | 27% | ibnabishayba(579), hakim(303), ibnhibban(271) |
| 24 | 2447 | 0.636 | 67% | 28% | ibnabishayba(467), hakim(290), ibnhibban(265) |
| 39 | 2362 | 0.559 | 89% | 10% | ibnabishayba(944), abdurrazzaq(358), ibnhibban(196) |
| 58 | 2359 | 0.624 | 66% | 22% | ibnabishayba(580), abdurrazzaq(338), ibnhibban(184) |
| 22 | 2358 | 0.617 | 78% | 15% | ibnabishayba(712), abdurrazzaq(417), hakim(292) |
| 2 | 2311 | 0.562 | 72% | 22% | ibnabishayba(721), hakim(530), abdurrazzaq(244) |
| 63 | 2311 | 0.592 | 90% | 8% | ibnabishayba(1074), abdurrazzaq(469), hakim(130) |
| 69 | 2246 | 0.620 | 4% | 88% | tirmidhi(1088), abudawud(409), muslim(208) |
| 1 | 2183 | 0.662 | 79% | 13% | ibnabishayba(722), abdurrazzaq(320), hakim(194) |
| 27 | 2131 | 0.636 | 68% | 26% | ibnabishayba(538), ibnhibban(223), hakim(214) |
| 59 | 2128 | 0.605 | 84% | 14% | ibnabishayba(738), abdurrazzaq(612), ibnhibban(111) |
| 70 | 2116 | 0.652 | 43% | 25% | mishkat(380), ibnabishayba(370), abdurrazzaq(225) |
| 25 | 2064 | 0.609 | 86% | 13% | ibnabishayba(737), abdurrazzaq(517), daraqutni(148) |
| 8 | 2042 | 0.651 | 10% | 87% | nasai(460), muslim(407), abudawud(312) |
| 30 | 2039 | 0.596 | 77% | 20% | ibnabishayba(587), abdurrazzaq(432), hakim(171) |
| 14 | 2010 | 0.620 | 68% | 23% | ibnabishayba(451), hakim(261), ibnhibban(251) |
| 47 | 2009 | 0.639 | 80% | 16% | ibnabishayba(641), abdurrazzaq(419), ibnhibban(131) |
| 28 | 2001 | 0.663 | 41% | 34% | mishkat(255), nasai(198), ibnabishayba(163) |
| 42 | 1956 | 0.746 | 0% | 23% | ibnabishayba(767), nasai(361), abudawud(293) |
| 31 | 1943 | 0.628 | 64% | 28% | ibnabishayba(368), hakim(219), ibnhibban(211) |
| 15 | 1807 | 0.655 | 98% | 1% | ibnabishayba(967), hakim(377), abdurrazzaq(233) |
| 7 | 1798 | 0.613 | 87% | 11% | ibnabishayba(623), abdurrazzaq(502), hakim(163) |
| 50 | 1758 | 0.609 | 74% | 22% | ibnabishayba(507), abdurrazzaq(189), bukhari(157) |
| 35 | 1725 | 0.624 | 65% | 31% | ibnabishayba(381), bukhari(222), abdurrazzaq(175) |
| 60 | 1663 | 0.655 | 92% | 6% | ibnabishayba(475), hakim(308), ibnhibban(233) |
| 67 | 1649 | 0.681 | 85% | 10% | ibnabishayba(585), abdurrazzaq(482), daraqutni(92) |
| 16 | 1635 | 0.619 | 18% | 80% | muslim(355), abudawud(261), nasai(231) |
| 55 | 1635 | 0.597 | 80% | 16% | ibnabishayba(522), abdurrazzaq(301), hakim(127) |
| 26 | 1616 | 0.550 | 82% | 16% | ibnabishayba(594), abdurrazzaq(249), hakim(132) |
| 48 | 1610 | 0.642 | 76% | 18% | ibnabishayba(505), abdurrazzaq(331), bukhari(132) |
| 4 | 1592 | 0.587 | 93% | 6% | ibnabishayba(864), abdurrazzaq(233), ibnhibban(105) |
| 21 | 1591 | 0.616 | 83% | 14% | ibnabishayba(571), abdurrazzaq(260), daraqutni(133) |
| 52 | 1519 | 0.607 | 86% | 13% | ibnabishayba(601), abdurrazzaq(332), daraqutni(83) |
| 13 | 1508 | 0.654 | 77% | 19% | ibnabishayba(370), abdurrazzaq(297), ibnhibban(118) |
| 33 | 1491 | 0.608 | 94% | 5% | ibnabishayba(859), abdurrazzaq(321), ibnhibban(58) |
| 38 | 1489 | 0.684 | 95% | 4% | ibnabishayba(677), abdurrazzaq(334), ibnhibban(138) |
| 64 | 1470 | 0.629 | 72% | 26% | ibnabishayba(371), abdurrazzaq(175), ibnhibban(163) |
| 18 | 1466 | 0.769 | 0% | 23% | muslim(995), ibnmajah(160), abudawud(151) |
| 11 | 1444 | 0.635 | 79% | 17% | ibnabishayba(354), hakim(213), abdurrazzaq(182) |
| 68 | 1440 | 0.620 | 83% | 16% | ibnabishayba(481), abdurrazzaq(255), ibnhibban(120) |
| 53 | 1414 | 0.675 | 94% | 4% | ibnabishayba(643), abdurrazzaq(545), daraqutni(45) |
| 43 | 1382 | 0.644 | 82% | 17% | ibnabishayba(471), abdurrazzaq(331), hakim(107) |
| 45 | 1335 | 0.658 | 80% | 17% | ibnabishayba(463), abdurrazzaq(242), daraqutni(94) |
| 37 | 1328 | 0.673 | 3% | 7% | mishkat(615), riyadussalihin(316), bulugh(213) |
| 20 | 1281 | 0.634 | 87% | 11% | ibnabishayba(410), abdurrazzaq(318), ibnhibban(83) |
| 66 | 1270 | 0.670 | 69% | 29% | ibnabishayba(266), ibnhibban(160), abdurrazzaq(129) |
| 49 | 1248 | 0.656 | 62% | 30% | ibnabishayba(240), abdurrazzaq(129), bukhari(125) |
| 36 | 1244 | 0.636 | 87% | 10% | ibnabishayba(519), abdurrazzaq(280), ibnhibban(85) |
| 61 | 1169 | 0.654 | 78% | 17% | ibnabishayba(342), abdurrazzaq(155), ibnhibban(106) |
| 3 | 1165 | 0.693 | 0% | 96% | tirmidhi(883), abudawud(91), muslim(74) |
| 56 | 1145 | 0.646 | 91% | 8% | ibnabishayba(591), abdurrazzaq(278), ibnhibban(48) |
| 10 | 1039 | 0.590 | 56% | 21% | hakim(186), ibnabishayba(174), mishkat(96) |
| 65 | 1031 | 0.629 | 78% | 21% | ibnabishayba(317), abdurrazzaq(165), daraqutni(86) |
| 73 | 1023 | 0.578 | 87% | 11% | ibnabishayba(340), abdurrazzaq(242), daraqutni(108) |
| 71 | 971 | 0.638 | 67% | 28% | ibnabishayba(279), abdurrazzaq(117), muslim(98) |
| 41 | 929 | 0.618 | 94% | 4% | ibnabishayba(408), bukhari(180), ibnkhuzayma(101) |
| 17 | 809 | 0.848 | 0% | 99% | tirmidhi(804), nasai(2), shamail(2) |
| 44 | 809 | 0.649 | 86% | 10% | ibnabishayba(316), abdurrazzaq(204), ibnkhuzayma(56) |
| 29 | 807 | 0.645 | 74% | 20% | ibnabishayba(219), abdurrazzaq(174), bukhari(82) |
| 0 | 760 | 0.658 | 78% | 18% | ibnabishayba(207), abdurrazzaq(153), daraqutni(57) |
| 32 | 724 | 0.637 | 92% | 5% | ibnabishayba(301), abdurrazzaq(241), hakim(55) |
| 46 | 711 | 0.662 | 98% | 1% | ibnabishayba(530), abdurrazzaq(140), darimi(15) |
| 51 | 596 | 0.727 | 45% | 53% | ibnabishayba(126), nasai(106), abdurrazzaq(85) |
| 72 | 531 | 0.651 | 85% | 12% | ibnabishayba(181), abdurrazzaq(124), ibnhibban(40) |