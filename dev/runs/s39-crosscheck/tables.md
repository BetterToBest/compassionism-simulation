## Engine side: study A rows rerun year by year (seeds 1-500, 500 adults, 20 years, CPS yardstick, raise off)

| Environment | Design | Unmatched money, share of cash income (mean of years) | year 1 | year 20 | Payout matched by output | General price level after 3 years | after 19 years | Full price level after 3 years | after 19 years | Yearly rate (full level) |
|---|---|---|---|---|---|---|---|---|---|---|
| Reference | C2.2 | 36.9% | 30.9% | 32.2% | 32.3% | 2.59 | 408 | 2.64 | 415 | 37.2% |
| Reference | release | 31.4% | 16.1% | 30.6% | 8.7% | 2.04 | 180 | 2.07 | 183 | 31.4% |
| Adverse | C2.2 | 43.8% | 30.9% | 46.5% | 30.5% | 2.64 | 982 | 2.85 | 1461 | 46.6% |
| Adverse | release | 37.9% | 16.1% | 44.5% | 8.1% | 2.06 | 425 | 2.22 | 627 | 40.2% |
| Stress | C2.2 | 45.8% | 31.1% | 51.8% | 25.4% | 2.69 | 1266 | 2.90 | 1883 | 48.5% |
| Stress | release | 16.6% | 6.1% | 19.4% | 2.6% | 1.40 | 18 | 1.49 | 27 | 18.7% |

Price levels: means over seeds (1 before any payout). The engine sets a year's price level from the new money of the years before it, so its level in year index k (the year path's entry k) is the level after k years of payout; the run's last entry is after 19 years. The yearly rate is the geometric mean over those 19 years, from the mean log.
The engine pass-through is 1 for the general level by construction (PG grows by exactly U/Y each year); the full level adds the essentials rule.

- Adverse, C2.2: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.08, after 19 years 1.06; general level 1.00, 1.00.
- Adverse, release: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.10, after 19 years 1.06; general level 1.00, 1.00.
- Reference, C2.2: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.02, after 19 years 1.00; general level 1.00, 1.00.
- Reference, release: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.02, after 19 years 1.00; general level 1.00, 1.00.
- Stress, C2.2: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.08, after 19 years 1.06; general level 1.00, 1.00.
- Stress, release: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.20, after 19 years 1.13; general level 1.00, 1.00.
