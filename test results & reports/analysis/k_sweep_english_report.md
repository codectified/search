# k-Sweep Report — English OpenAI Vectors

Corpus: 48,703 hadiths | Model: OpenAI text-embedding-3-small | L2-normalized
Pre-filter strategy: top-2 clusters → kNN within that subset

## Summary Table

| k | Cohesion | Pairs>0.93 | Pairs>0.85 | Max sim | Median size | Top-2 coverage | P90 | P10 |
|---|---|---|---|---|---|---|---|---|
| 25 | 0.712 | 7 | 112 | 0.953 | 1887 | 5,969 (12.3%) | 2517 | 1403 |
| 40 | 0.724 | 8 | 158 | 0.957 | 1170 | 4,205 (8.6%) | 1680 | 728 |
| 50 | 0.726 | 8 | 231 | 0.960 | 964 | 3,167 (6.5%) | 1302 | 634 |
| 75 | 0.737 | 22 | 355 | 0.956 | 656 | 2,871 (5.9%) | 978 | 291 |
| 100 | 0.741 | 22 | 469 | 0.961 | 465 | 2,018 (4.1%) | 727 | 227 |
| 125 | 0.749 | 24 | 475 | 0.951 | 382 | 1,607 (3.3%) | 639 | 174 |

## Guidance

- **Cohesion**: higher = tighter clusters. Target ≥ 0.65 for good semantic grouping.
- **Pairs>0.93**: near-zero means clusters are well-separated. >10 = over-splitting.
- **Top-2 coverage**: how many docs the pre-filter lets through. Sweet spot: 1,000–3,000.
- **Median size**: should be ≥ 300 to give kNN enough candidates after filtering.
- **Note**: Arabic used k=150 on 131k (≈873/cluster). Same density on 48k = k≈55.