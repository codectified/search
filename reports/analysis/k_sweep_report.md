# k-Sweep Report — Arabic Matn v3 Vectors

Corpus: 131,728 hadiths | Model: OpenAI text-embedding-3-small | L2-normalized

## Summary Table

| k | Cohesion | Pairs>0.93 | Pairs>0.85 | Pairs>0.75 | Max sim | Median size | P90 size | P10 size |
|---|---|---|---|---|---|---|---|---|
| 50 | 0.624 | 2 | 95 | 602 | 0.936 | 2531 | 3639 | 1607 |
| 75 | 0.638 | 2 | 107 | 861 | 0.932 | 1635 | 2736 | 809 |
| 100 | 0.639 | 7 | 176 | 1335 | 0.947 | 1158 | 2028 | 771 |
| 125 | 0.648 | 4 | 233 | 1746 | 0.966 | 1007 | 1552 | 556 |
| 150 | 0.652 | 12 | 233 | 2105 | 0.952 | 872 | 1326 | 418 |
| 175 | 0.661 | 9 | 277 | 2325 | 0.955 | 770 | 1177 | 296 |
| 200 | 0.665 | 9 | 310 | 2862 | 0.951 | 673 | 1025 | 250 |

## Guidance

- **Pairs>0.93**: near-zero means no meaningful over-splitting. >20 suggests k is too high.
- **Cohesion**: higher = tighter clusters. Should not drop below 0.60.
- **Median size**: should be large enough to be useful as a filter (>500 hadiths).
- **Max sim**: should be below 0.95 ideally — two centroids at 0.97 are the same topic.