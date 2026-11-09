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

## BeforeIT, full scale (1:1) (65 runs)

| Scenario | Quarter | Price level vs no payout (CPI, %) | 95% interval | Pass-through λ | 95% interval | Deflator (%) | Food (%) | Housing (%) | Medical (%) | Real GDP (%) | Unemployment | Debt / year's output |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c22-ref-ea | 12 | +1.46 | -0.26 to +3.20 | 0.015 | -0.003 to 0.033 | +1.46 | +1.46 | +1.46 | +1.46 | +15.52 | 0.000 | 1.60 |
| c22-ref-ea | 80 | -0.38 | -7.07 to +6.80 | -0.001 | -0.012 to 0.010 | -0.38 | -0.38 | -0.38 | -0.38 | +3.16 | 0.000 | 9.80 |
| c22-ref-dom | 12 | +1.80 | -1.32 to +5.03 | 0.019 | -0.014 to 0.052 | +1.80 | +1.80 | +1.80 | +1.80 | +13.65 | 0.000 | 1.61 |
| c22-ref-dom | 80 | +2.21 | -8.35 to +14.00 | 0.003 | -0.014 to 0.021 | +2.21 | +2.21 | +2.21 | +2.21 | +3.67 | 0.000 | 9.62 |
| c22-adv-ea | 12 | -0.80 | -3.24 to +1.70 | -0.008 | -0.034 to 0.017 | -0.80 | -0.80 | -0.80 | -0.80 | +15.17 | 0.000 | 1.67 |
| c22-adv-ea | 80 | +1.59 | -8.91 to +13.31 | 0.002 | -0.013 to 0.017 | +1.59 | +1.59 | +1.59 | +1.59 | +5.18 | 0.000 | 11.58 |
| c22-st-ea | 12 | -0.49 | -3.53 to +2.64 | -0.005 | -0.036 to 0.026 | -0.49 | -0.49 | -0.49 | -0.49 | +15.31 | 0.000 | 1.66 |
| c22-st-ea | 80 | -5.18 | -16.06 to +7.11 | -0.007 | -0.023 to 0.009 | -5.18 | -5.18 | -5.18 | -5.18 | +5.64 | 0.000 | 12.45 |
| rls-ref-ea | 12 | -1.39 | -5.12 to +2.49 | -0.020 | -0.074 to 0.034 | -1.39 | -1.39 | -1.39 | -1.39 | +14.73 | 0.000 | 1.29 |
| rls-ref-ea | 80 | +2.06 | -13.09 to +19.86 | 0.004 | -0.026 to 0.033 | +2.06 | +2.06 | +2.06 | +2.06 | +3.57 | 0.000 | 7.15 |
| c22-ref-gross-ea | 12 | -0.69 | -6.33 to +5.29 | -0.005 | -0.050 to 0.039 | -0.69 | -0.69 | -0.69 | -0.69 | +15.81 | 0.000 | 2.56 |
| c22-ref-gross-ea | 80 | +2.76 | -7.13 to +13.71 | 0.003 | -0.009 to 0.015 | +2.76 | +2.76 | +2.76 | +2.76 | +4.61 | 0.000 | 17.76 |
| c22-ref-tax-ea | 12 | +0.40 | -2.81 to +3.71 | 0.004 | -0.030 to 0.038 | +0.40 | +0.40 | +0.40 | +0.40 | +0.81 | 0.051 | 0.90 |
| c22-ref-tax-ea | 80 | +0.38 | -12.56 to +15.22 | 0.001 | -0.021 to 0.023 | +0.38 | +0.38 | +0.38 | +0.38 | -3.77 | 0.016 | 1.21 |
| dose01-ea | 12 | -0.25 | -1.85 to +1.38 | -0.083 | -0.625 to 0.460 | -0.25 | -0.25 | -0.25 | -0.25 | +0.74 | 0.037 | 0.91 |
| dose01-ea | 80 | +3.52 | -4.73 to +12.48 | 0.174 | -0.243 to 0.591 | +3.52 | +3.52 | +3.52 | +3.52 | -1.02 | 0.000 | 1.25 |
| dose03-ea | 12 | +2.72 | +0.11 to +5.39 | 0.302 | 0.013 to 0.592 | +2.72 | +2.72 | +2.72 | +2.72 | +3.37 | 0.019 | 0.89 |
| dose03-ea | 80 | +7.37 | -0.22 to +15.54 | 0.120 | -0.004 to 0.244 | +7.37 | +7.37 | +7.37 | +7.37 | +2.47 | 0.000 | 1.50 |
| dose10-ea | 12 | -0.59 | -2.92 to +1.80 | -0.021 | -0.104 to 0.062 | -0.59 | -0.59 | -0.59 | -0.59 | +9.32 | 0.000 | 0.93 |
| dose10-ea | 80 | +3.22 | -4.13 to +11.13 | 0.017 | -0.022 to 0.055 | +3.22 | +3.22 | +3.22 | +3.22 | +4.21 | 0.000 | 2.21 |
| dose30-ea | 12 | +0.76 | -3.76 to +5.49 | 0.010 | -0.049 to 0.068 | +0.76 | +0.76 | +0.76 | +0.76 | +14.64 | 0.000 | 1.33 |
| dose30-ea | 80 | +0.74 | -7.15 to +9.31 | 0.001 | -0.014 to 0.017 | +0.74 | +0.74 | +0.74 | +0.74 | +3.85 | 0.000 | 6.87 |
- No payout (base-ea), quarter 12: CPI 1.039, unemployment 0.047, debt / year's output 0.91 (means over seeds).
- No payout (base-ea), quarter 80: CPI 1.313, unemployment 0.000, debt / year's output 1.14 (means over seeds).
- No payout (base-dom), quarter 12: CPI 1.026, unemployment 0.036, debt / year's output 0.91 (means over seeds).
- No payout (base-dom), quarter 80: CPI 1.295, unemployment 0.000, debt / year's output 1.23 (means over seeds).

## BeforeIT, 1:1000 (1300 runs)

| Scenario | Quarter | Price level vs no payout (CPI, %) | 95% interval | Pass-through λ | 95% interval | Deflator (%) | Food (%) | Housing (%) | Medical (%) | Real GDP (%) | Unemployment | Debt / year's output |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c22-ref-ea | 12 | -0.17 | -0.73 to +0.37 | -0.002 | -0.008 to 0.004 | -0.17 | -0.17 | -0.17 | -0.17 | +13.83 | 0.000 | 1.60 |
| c22-ref-ea | 80 | +0.20 | -1.80 to +2.27 | 0.000 | -0.003 to 0.004 | +0.20 | +0.20 | +0.20 | +0.20 | +2.49 | 0.000 | 9.06 |
| c22-ref-dom | 12 | +0.14 | -0.39 to +0.67 | 0.002 | -0.004 to 0.007 | +0.14 | +0.14 | +0.14 | +0.14 | +13.28 | 0.000 | 1.60 |
| c22-ref-dom | 80 | -0.09 | -2.08 to +1.94 | -0.000 | -0.003 to 0.003 | -0.09 | -0.09 | -0.09 | -0.09 | +3.29 | 0.000 | 9.09 |
| c22-adv-ea | 12 | -0.39 | -0.87 to +0.09 | -0.004 | -0.009 to 0.001 | -0.39 | -0.39 | -0.39 | -0.39 | +13.97 | 0.000 | 1.63 |
| c22-adv-ea | 80 | -0.94 | -2.69 to +0.88 | -0.001 | -0.004 to 0.001 | -0.94 | -0.94 | -0.94 | -0.94 | +2.99 | 0.000 | 11.63 |
| c22-st-ea | 12 | -0.36 | -0.88 to +0.15 | -0.004 | -0.009 to 0.002 | -0.36 | -0.36 | -0.36 | -0.36 | +14.15 | 0.000 | 1.67 |
| c22-st-ea | 80 | -1.46 | -3.37 to +0.57 | -0.002 | -0.005 to 0.001 | -1.46 | -1.46 | -1.46 | -1.46 | +3.21 | 0.000 | 12.64 |
| rls-ref-ea | 12 | -0.33 | -0.85 to +0.18 | -0.005 | -0.012 to 0.003 | -0.33 | -0.33 | -0.33 | -0.33 | +13.83 | 0.000 | 1.26 |
| rls-ref-ea | 80 | -0.25 | -2.15 to +1.66 | -0.000 | -0.004 to 0.003 | -0.25 | -0.25 | -0.25 | -0.25 | +2.50 | 0.000 | 7.28 |
| c22-ref-gross-ea | 12 | +0.04 | -0.47 to +0.56 | 0.000 | -0.004 to 0.004 | +0.04 | +0.04 | +0.04 | +0.04 | +14.76 | 0.000 | 2.55 |
| c22-ref-gross-ea | 80 | -0.28 | -2.40 to +1.87 | -0.000 | -0.003 to 0.002 | -0.28 | -0.28 | -0.28 | -0.28 | +3.11 | 0.000 | 17.86 |
| c22-ref-tax-ea | 12 | -0.20 | -0.76 to +0.39 | -0.002 | -0.008 to 0.004 | -0.20 | -0.20 | -0.20 | -0.20 | +1.49 | 0.029 | 0.88 |
| c22-ref-tax-ea | 80 | -0.25 | -2.20 to +1.75 | -0.000 | -0.004 to 0.003 | -0.25 | -0.25 | -0.25 | -0.25 | -1.09 | 0.003 | 1.13 |
| dose01-ea | 12 | -0.10 | -0.59 to +0.38 | -0.035 | -0.198 to 0.127 | -0.10 | -0.10 | -0.10 | -0.10 | +1.28 | 0.031 | 0.88 |
| dose01-ea | 80 | -0.08 | -2.11 to +2.01 | -0.004 | -0.107 to 0.100 | -0.08 | -0.08 | -0.08 | -0.08 | +0.46 | 0.000 | 1.24 |
| dose03-ea | 12 | -0.24 | -0.74 to +0.24 | -0.027 | -0.084 to 0.028 | -0.24 | -0.24 | -0.24 | -0.24 | +2.96 | 0.018 | 0.89 |
| dose03-ea | 80 | -0.16 | -2.21 to +1.81 | -0.003 | -0.038 to 0.030 | -0.16 | -0.16 | -0.16 | -0.16 | +2.02 | 0.000 | 1.41 |
| dose10-ea | 12 | -0.01 | -0.55 to +0.54 | -0.000 | -0.019 to 0.019 | -0.01 | -0.01 | -0.01 | -0.01 | +10.74 | 0.000 | 0.89 |
| dose10-ea | 80 | -0.07 | -1.97 to +1.95 | -0.000 | -0.010 to 0.010 | -0.07 | -0.07 | -0.07 | -0.07 | +2.67 | 0.000 | 2.39 |
| dose30-ea | 12 | -0.44 | -0.99 to +0.11 | -0.006 | -0.013 to 0.001 | -0.44 | -0.44 | -0.44 | -0.44 | +13.38 | 0.000 | 1.33 |
| dose30-ea | 80 | -1.08 | -3.04 to +0.93 | -0.002 | -0.006 to 0.002 | -1.08 | -1.08 | -1.08 | -1.08 | +2.41 | 0.000 | 6.84 |
- No payout (base-ea), quarter 12: CPI 1.044, unemployment 0.040, debt / year's output 0.89 (means over seeds).
- No payout (base-ea), quarter 80: CPI 1.330, unemployment 0.000, debt / year's output 1.17 (means over seeds).
- No payout (base-dom), quarter 12: CPI 1.041, unemployment 0.036, debt / year's output 0.88 (means over seeds).
- No payout (base-dom), quarter 80: CPI 1.326, unemployment 0.002, debt / year's output 1.14 (means over seeds).

## Identity check (added in part 2)

- Identity check, full scale (1:1) (65 runs): largest gap between a quarter's CPI growth and expected inflation 8.9e-16; largest gap between any of the deflator, food, housing and medical indices and the CPI 3.3e-15 (relative).
- Identity check, 1:1000 (1300 runs): largest gap between a quarter's CPI growth and expected inflation 1.1e-15; largest gap between any of the deflator, food, housing and medical indices and the CPI 3.2e-15 (relative).

## Rule 5: secondary contrasts (added in part 2), seed-paired differences in log points shown as %

| Contrast | Scale | Quarter | CPI difference (%) | 95% interval | Real GDP difference (%) | 95% interval |
|---|---|---|---|---|---|---|
| Q4 gross minus net (c22-ref-gross-ea vs c22-ref-ea) | full scale (1:1) | 12 | -2.12 | -7.37 to +3.43 | +0.25 | -0.05 to +0.55 |
| Q4 gross minus net (c22-ref-gross-ea vs c22-ref-ea) | full scale (1:1) | 80 | +3.15 | -8.80 to +16.67 | +1.41 | -1.02 to +3.90 |
| Q4 gross minus net (c22-ref-gross-ea vs c22-ref-ea) | 1:1000 | 12 | +0.22 | -0.36 to +0.78 | +0.81 | +0.60 to +1.01 |
| Q4 gross minus net (c22-ref-gross-ea vs c22-ref-ea) | 1:1000 | 80 | -0.47 | -2.54 to +1.59 | +0.60 | +0.35 to +0.84 |
| Q5 tax-financed minus new money (c22-ref-tax-ea vs c22-ref-ea) | full scale (1:1) | 12 | -1.05 | -3.91 to +1.91 | -12.74 | -15.05 to -10.36 |
| Q5 tax-financed minus new money (c22-ref-tax-ea vs c22-ref-ea) | full scale (1:1) | 80 | +0.76 | -9.67 to +12.39 | -6.72 | -12.92 to -0.08 |
| Q5 tax-financed minus new money (c22-ref-tax-ea vs c22-ref-ea) | 1:1000 | 12 | -0.02 | -0.56 to +0.49 | -10.84 | -11.39 to -10.30 |
| Q5 tax-financed minus new money (c22-ref-tax-ea vs c22-ref-ea) | 1:1000 | 80 | -0.44 | -2.36 to +1.55 | -3.49 | -4.28 to -2.73 |
| Q6 domestic minus euro-area closure (each against its own no-payout run) | full scale (1:1) | 12 | +0.34 | -3.81 to +4.68 | -1.62 | -3.37 to +0.16 |
| Q6 domestic minus euro-area closure (each against its own no-payout run) | full scale (1:1) | 80 | +2.60 | -7.61 to +13.94 | +0.49 | -2.39 to +3.46 |
| Q6 domestic minus euro-area closure (each against its own no-payout run) | 1:1000 | 12 | +0.32 | -0.47 to +1.07 | -0.48 | -1.01 to +0.06 |
| Q6 domestic minus euro-area closure (each against its own no-payout run) | 1:1000 | 80 | -0.28 | -2.96 to +2.51 | +0.78 | -0.06 to +1.64 |
| Primary row against no payout (c22-ref-ea vs base-ea) | full scale (1:1) | 12 | +1.46 | -0.26 to +3.20 | +15.52 | +14.54 to +16.52 |
| Primary row against no payout (c22-ref-ea vs base-ea) | full scale (1:1) | 80 | -0.38 | -7.07 to +6.80 | +3.16 | +0.49 to +5.89 |
| Primary row against no payout (c22-ref-ea vs base-ea) | 1:1000 | 12 | -0.17 | -0.72 to +0.39 | +13.83 | +13.41 to +14.26 |
| Primary row against no payout (c22-ref-ea vs base-ea) | 1:1000 | 80 | +0.20 | -1.85 to +2.24 | +2.49 | +1.91 to +3.08 |

Q8, full scale minus 1:1000 (independent seeds; Welch interval; log points shown as %):

| Scenario | Quarter | CPI effect, full minus 1:1000 (%) | 95% interval | Real GDP effect, full minus 1:1000 (%) | 95% interval |
|---|---|---|---|---|---|
| c22-ref-ea | 12 | +1.63 | -0.12 to +3.41 | +1.49 | +0.62 to +2.36 |
| c22-ref-ea | 80 | -0.57 | -7.26 to +6.61 | +0.65 | -2.06 to +3.45 |
| c22-ref-dom | 12 | +1.66 | -1.55 to +4.97 | +0.33 | -1.29 to +1.97 |
| c22-ref-dom | 80 | +2.31 | -8.62 to +14.54 | +0.37 | -1.91 to +2.69 |
| c22-adv-ea | 12 | -0.41 | -2.96 to +2.20 | +1.05 | +0.13 to +1.97 |
| c22-adv-ea | 80 | +2.56 | -8.31 to +14.72 | +2.13 | +0.21 to +4.09 |
| c22-st-ea | 12 | -0.13 | -3.26 to +3.10 | +1.01 | -0.46 to +2.51 |
| c22-st-ea | 80 | -3.78 | -15.10 to +9.06 | +2.36 | +0.51 to +4.24 |
| rls-ref-ea | 12 | -1.06 | -4.87 to +2.90 | +0.79 | -0.05 to +1.64 |
| rls-ref-ea | 80 | +2.31 | -13.08 to +20.43 | +1.04 | -1.56 to +3.71 |
| c22-ref-gross-ea | 12 | -0.73 | -6.41 to +5.29 | +0.92 | +0.04 to +1.81 |
| c22-ref-gross-ea | 80 | +3.05 | -7.27 to +14.52 | +1.46 | -0.11 to +3.05 |
| c22-ref-tax-ea | 12 | +0.59 | -2.72 to +4.02 | -0.67 | -3.18 to +1.90 |
| c22-ref-tax-ea | 80 | +0.63 | -12.59 to +15.84 | -2.71 | -8.55 to +3.50 |
| dose01-ea | 12 | -0.14 | -1.76 to +1.50 | -0.52 | -4.12 to +3.20 |
| dose01-ea | 80 | +3.60 | -4.52 to +12.42 | -1.47 | -3.29 to +0.39 |
| dose03-ea | 12 | +2.96 | +0.26 to +5.74 | +0.39 | -2.35 to +3.21 |
| dose03-ea | 80 | +7.54 | -0.04 to +15.70 | +0.44 | -3.39 to +4.43 |
| dose10-ea | 12 | -0.57 | -3.02 to +1.94 | -1.28 | -3.85 to +1.36 |
| dose10-ea | 80 | +3.30 | -3.99 to +11.14 | +1.50 | +0.57 to +2.44 |
| dose30-ea | 12 | +1.21 | -3.40 to +6.03 | +1.12 | +0.04 to +2.21 |
| dose30-ea | 80 | +1.84 | -6.00 to +10.34 | +1.41 | -1.25 to +4.14 |
