# S59, part 2: the weighted top tail, business owners and the income wealth pays, pilot tables

Seeds 1-100, 500 adults, 20 years; engine `62a189b`. Effects are programme minus no programme on the same seeds, with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates (unadjusted). Shares, percentiles and rates are weighted by each adult's population weight (1 for every adult where the tail is off). A pilot is a mechanism check, not a result. Made by `dev/tools/s59_tail_table.py` from the per-seed files in compassionism-sim-results.

Check row (the tail with every weight 1 and no change of wealth) equals part 1's reading on every kept key: Reference yes, Adverse yes, Stress yes.

Readings: **off** all wealth is one number of dollars; **p1** part 1: by asset class (corrected group edges); **p1chi** part 1 with fixed-rate debt repricing (no debt relief); **flat** check: the tail with every weight 1 and no change of wealth (must equal p1); **r2** part 1 with business owners and capital income; **main** main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule); **tailonly** part 1 with the tail only; **a135** tail exponent one standard error lower (1.354: a heavier tail); **a163** tail exponent one standard error higher (1.626); **p99** cutoff at the 99th percentile (exponent 1.576); **gpd** generalised Pareto above the main cutoff; **gpd90** generalised Pareto from the 90th percentile; **m1** 1 tail household per type; **m6** 6 tail households per type; **ng0** no interest gradient at the very top; **ngall** interest gradient on the inflation pass-through too; **rg** higher real-estate gains for the top group; **bo0** no business-owner split (group averages); **ci0** no capital income; **chi1** fixed-rate debt reprices too (no debt relief); **ix05** real assets follow half of inflation; **ownW** owners keep the private premium, shared by positive wealth (no tail); **ownE** owners keep the private premium, shared by shares and business equity (no tail).

## 1. The start (end of Year 0, no programme, Reference) beside the survey

The SCF rows are the 2022 Survey of Consumer Finances for the engine's families (head aged 25-66 with wage income), counted by adult as the engine does (a couple's net worth split equally), in 2025 dollars. The tail is fitted to that survey, so agreement with it checks the build; the Fed's Distributional Financial Accounts (all households, a wider wealth concept) are the outside comparison.

| | top 0.1% share | top 1% share | top 10% share | bottom 50% share | Gini (debts kept) | mean | median | 99.9th percentile |
|---|---|---|---|---|---|---|---|---|
| all wealth is one number of dollars | 2.53 (2.45 to 2.60) | 20.77 (20.19 to 21.35) | 64.65 (63.95 to 65.32) | 3.60 (3.52 to 3.70) | 0.771 (0.768 to 0.775) | $512,300 ($503,300 to $521,900) | $127,600 ($125,400 to $129,700) | $12,807,600 ($12,329,400 to $13,264,700) |
| part 1: by asset class (corrected group edges) | 2.53 (2.45 to 2.61) | 20.77 (20.19 to 21.37) | 64.65 (63.96 to 65.33) | 3.60 (3.51 to 3.69) | 0.771 (0.768 to 0.775) | $512,300 ($503,400 to $521,100) | $127,600 ($125,400 to $129,800) | $12,807,600 ($12,342,800 to $13,244,700) |
| part 1 with business owners and capital income | 2.53 (2.45 to 2.61) | 20.79 (20.21 to 21.39) | 64.67 (63.98 to 65.34) | 3.60 (3.51 to 3.69) | 0.771 (0.768 to 0.775) | $513,100 ($504,400 to $522,300) | $127,700 ($125,700 to $129,800) | $12,844,700 ($12,398,300 to $13,315,600) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | 11.63 (10.96 to 12.33) | 30.11 (28.42 to 31.81) | 70.41 (69.21 to 71.65) | 3.00 (2.88 to 3.12) | 0.807 (0.800 to 0.814) | $641,200 ($609,900 to $675,800) | $127,600 ($125,400 to $129,800) | $24,085,300 ($19,911,100 to $28,615,100) |
| part 1 with the tail only | 11.61 (10.93 to 12.34) | 30.08 (28.52 to 31.76) | 70.39 (69.15 to 71.64) | 3.00 (2.88 to 3.11) | 0.807 (0.800 to 0.814) | $640,000 ($607,900 to $675,900) | $127,400 ($125,300 to $129,400) | $24,011,200 ($19,682,500 to $28,562,700) |
| tail exponent one standard error lower (1.354: a heavier tail) | 15.86 (14.84 to 16.86) | 35.05 (33.37 to 36.98) | 72.89 (71.69 to 74.12) | 2.74 (2.63 to 2.86) | 0.823 (0.816 to 0.830) | $712,700 ($669,100 to $759,600) | $127,600 ($125,500 to $129,700) | $30,696,000 ($25,067,800 to $37,058,300) |
| tail exponent one standard error higher (1.626) | 9.04 (8.57 to 9.53) | 26.75 (25.27 to 28.32) | 68.64 (67.47 to 69.80) | 3.18 (3.06 to 3.29) | 0.796 (0.790 to 0.803) | $597,300 ($572,600 to $624,800) | $127,600 ($125,500 to $129,700) | $19,973,200 ($16,641,700 to $23,173,500) |
| cutoff at the 99th percentile (exponent 1.576) | 10.85 (10.30 to 11.43) | 33.32 (31.77 to 35.10) | 70.95 (70.10 to 71.79) | 2.95 (2.86 to 3.04) | 0.811 (0.806 to 0.816) | $633,000 ($614,200 to $652,000) | $127,400 ($125,200 to $129,800) | $24,635,800 ($21,214,400 to $28,538,900) |
| generalised Pareto above the main cutoff | 10.34 (9.76 to 10.94) | 28.86 (27.26 to 30.55) | 69.89 (68.70 to 71.10) | 3.05 (2.93 to 3.16) | 0.804 (0.797 to 0.810) | $627,900 ($599,200 to $660,300) | $127,600 ($125,500 to $129,500) | $23,110,200 ($19,216,100 to $27,261,600) |
| generalised Pareto from the 90th percentile | 12.44 (11.44 to 13.53) | 23.55 (22.19 to 24.98) | 67.08 (65.05 to 69.12) | 3.25 (3.05 to 3.45) | 0.785 (0.776 to 0.795) | $652,000 ($589,900 to $716,300) | $127,500 ($125,500 to $129,600) | $28,758,200 ($25,530,900 to $32,107,700) |
| 1 tail household per type | 4.23 (3.45 to 5.15) | 24.80 (22.13 to 27.65) | 67.51 (65.99 to 69.11) | 3.30 (3.13 to 3.44) | 0.789 (0.780 to 0.798) | $615,400 ($558,600 to $682,700) | $127,500 ($125,400 to $129,600) | $25,722,600 ($16,112,400 to $40,681,500) |
| 6 tail households per type | 14.13 (13.74 to 14.52) | 31.65 (31.08 to 32.19) | 71.09 (70.58 to 71.56) | 2.94 (2.88 to 3.01) | 0.811 (0.808 to 0.814) | $625,200 ($615,000 to $635,300) | $127,400 ($125,000 to $129,700) | $17,733,000 ($16,770,600 to $18,683,100) |
| no business-owner split (group averages) | 11.62 (10.96 to 12.34) | 30.11 (28.45 to 31.74) | 70.41 (69.26 to 71.58) | 3.00 (2.87 to 3.11) | 0.807 (0.801 to 0.814) | $641,300 ($609,500 to $676,400) | $127,600 ($125,400 to $129,600) | $24,082,700 ($20,033,300 to $28,645,000) |
| **SCF 2022, the engine's families, by adult** | 11.84 | 31.46 | 69.27 | 3.17 | 0.801 | $599,300 | $135,600 | |
| SCF 2022, the engine's families, by family | 12.57 | 32.86 | 71.45 | 2.56 | 0.818 | $1,001,100 | $196,700 | |
| SCF 2022, all families | 14.67 | 35.10 | 73.36 | 2.20 | 0.830 | $1,165,500 | $212,000 | |
| SCF 2022 with the Forbes 400 added, all families | | 36.91 | | | | | | |
| Distributional Financial Accounts, 2022:Q1 | 13.6 | 30.4 | 67.2 | 2.6 | | | | |
| Distributional Financial Accounts, 2026:Q2 | 15.0 | 32.5 | 68.9 | 2.3 | | | | |

Primary outcome (i): the start's weighted top 1% share under the main reading is 30.11 (28.42 to 31.81), against the SCF's 31.46% for the same families by adult (gap -1.35 points) and the Fed accounts' 30.4% (2022:Q1) and 32.5% (2026:Q2). Tail adults per run: 18 of 500, standing for 2.57% of adults.

## 2. Primary outcome (ii): the programme's effect on the top 1% share of wealth at year 20 (points)

Top 1% share with no programme at year 20 (%): Reference p1 21.19, main 31.17; Adverse p1 21.91, main 31.97; Stress p1 21.91, main 31.97.

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | -12.37 (-12.92 to -11.83) | -13.65 (-14.19 to -13.12) | -12.26 (-12.87 to -11.66) | -14.17 (-14.75 to -13.60) | -7.08 (-7.42 to -6.73) | -13.78 (-14.37 to -13.21) |
| part 1: by asset class (corrected group edges) | -0.85 (-0.88 to -0.82) | -1.35 (-1.39 to -1.31) | -0.84 (-0.87 to -0.80) | -1.35 (-1.39 to -1.30) | -0.68 (-0.70 to -0.65) | -1.15 (-1.19 to -1.11) |
| part 1 with fixed-rate debt repricing (no debt relief) | +1.16 (+1.10 to +1.22) | +0.61 (+0.55 to +0.66) | +0.74 (+0.69 to +0.79) | +0.19 (+0.15 to +0.23) | +0.73 (+0.69 to +0.77) | +0.43 (+0.38 to +0.48) |
| part 1 with business owners and capital income | -0.98 (-1.04 to -0.92) | -1.49 (-1.56 to -1.42) | -0.96 (-1.02 to -0.91) | -1.47 (-1.53 to -1.40) | -0.76 (-0.81 to -0.71) | -1.28 (-1.34 to -1.21) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | -1.14 (-1.23 to -1.06) | -1.75 (-1.85 to -1.65) | -1.11 (-1.19 to -1.03) | -1.70 (-1.79 to -1.62) | -0.88 (-0.94 to -0.81) | -1.47 (-1.56 to -1.39) |
| part 1 with the tail only | -0.92 (-0.96 to -0.89) | -1.52 (-1.57 to -1.47) | -0.91 (-0.95 to -0.86) | -1.50 (-1.55 to -1.45) | -0.74 (-0.77 to -0.71) | -1.27 (-1.31 to -1.22) |
| tail exponent one standard error lower (1.354: a heavier tail) | -1.22 (-1.31 to -1.13) | -1.86 (-1.96 to -1.77) | -1.17 (-1.25 to -1.09) | -1.80 (-1.90 to -1.71) | -0.93 (-1.00 to -0.86) | -1.56 (-1.65 to -1.47) |
| tail exponent one standard error higher (1.626) | -1.08 (-1.17 to -1.00) | -1.65 (-1.74 to -1.56) | -1.05 (-1.13 to -0.98) | -1.61 (-1.69 to -1.53) | -0.83 (-0.89 to -0.77) | -1.40 (-1.48 to -1.32) |
| cutoff at the 99th percentile (exponent 1.576) | -1.32 (-1.40 to -1.23) | -1.99 (-2.09 to -1.90) | -1.27 (-1.34 to -1.19) | -1.93 (-2.01 to -1.85) | -1.00 (-1.06 to -0.94) | -1.68 (-1.75 to -1.60) |
| generalised Pareto above the main cutoff | -1.12 (-1.20 to -1.03) | -1.70 (-1.80 to -1.61) | -1.08 (-1.16 to -1.01) | -1.66 (-1.75 to -1.58) | -0.85 (-0.92 to -0.79) | -1.44 (-1.52 to -1.36) |
| generalised Pareto from the 90th percentile | -0.86 (-0.96 to -0.77) | -1.38 (-1.50 to -1.25) | -0.86 (-0.95 to -0.76) | -1.37 (-1.50 to -1.24) | -0.69 (-0.76 to -0.62) | -1.17 (-1.28 to -1.05) |
| 1 tail household per type | -1.00 (-1.13 to -0.89) | -1.49 (-1.63 to -1.36) | -0.97 (-1.07 to -0.86) | -1.45 (-1.57 to -1.33) | -0.76 (-0.85 to -0.68) | -1.26 (-1.38 to -1.15) |
| 6 tail households per type | -1.29 (-1.35 to -1.24) | -1.96 (-2.03 to -1.89) | -1.25 (-1.31 to -1.19) | -1.90 (-1.97 to -1.84) | -0.98 (-1.02 to -0.94) | -1.65 (-1.72 to -1.59) |
| no interest gradient at the very top | -1.11 (-1.20 to -1.03) | -1.71 (-1.81 to -1.62) | -1.08 (-1.16 to -1.01) | -1.67 (-1.76 to -1.59) | -0.85 (-0.92 to -0.79) | -1.44 (-1.53 to -1.36) |
| interest gradient on the inflation pass-through too | +9.34 (+8.30 to +10.42) | +12.78 (+11.41 to +14.19) | +15.87 (+14.29 to +17.47) | +20.56 (+18.67 to +22.50) | +2.97 (+2.56 to +3.39) | +22.50 (+20.51 to +24.53) |
| higher real-estate gains for the top group | -1.14 (-1.23 to -1.06) | -1.74 (-1.84 to -1.65) | -1.10 (-1.18 to -1.03) | -1.70 (-1.78 to -1.61) | -0.87 (-0.94 to -0.81) | -1.47 (-1.55 to -1.39) |
| no business-owner split (group averages) | -1.17 (-1.21 to -1.13) | -1.77 (-1.82 to -1.72) | -1.13 (-1.17 to -1.09) | -1.72 (-1.77 to -1.66) | -0.89 (-0.93 to -0.86) | -1.49 (-1.54 to -1.44) |
| no capital income | -0.89 (-0.98 to -0.80) | -1.49 (-1.59 to -1.39) | -0.87 (-0.96 to -0.80) | -1.47 (-1.56 to -1.38) | -0.72 (-0.78 to -0.65) | -1.24 (-1.32 to -1.15) |
| fixed-rate debt reprices too (no debt relief) | +1.23 (+1.13 to +1.33) | +0.59 (+0.50 to +0.68) | +0.74 (+0.66 to +0.82) | +0.12 (+0.04 to +0.20) | +0.76 (+0.70 to +0.83) | +0.39 (+0.31 to +0.47) |
| real assets follow half of inflation | -10.37 (-10.75 to -10.01) | -15.15 (-15.75 to -14.58) | -9.91 (-10.25 to -9.57) | -15.68 (-16.28 to -15.10) | -3.33 (-3.44 to -3.21) | -14.87 (-15.44 to -14.33) |
| owners keep the private premium, shared by positive wealth (no tail) | -0.73 (-0.79 to -0.67) | -0.80 (-0.87 to -0.73) | -0.74 (-0.79 to -0.68) | -0.93 (-0.99 to -0.87) | -0.63 (-0.67 to -0.59) | -0.80 (-0.86 to -0.74) |
| owners keep the private premium, shared by shares and business equity (no tail) | -0.61 (-0.68 to -0.55) | -0.64 (-0.71 to -0.57) | -0.63 (-0.69 to -0.58) | -0.80 (-0.86 to -0.74) | -0.55 (-0.60 to -0.51) | -0.66 (-0.72 to -0.60) |

## 3. The programme's effect on the top 0.1% share of wealth at year 20 (points)

With no programme (%): Reference p1 2.61, main 12.24; Adverse p1 2.70, main 12.60; Stress p1 2.70, main 12.60.

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | -1.44 (-1.53 to -1.36) | -1.61 (-1.69 to -1.53) | -1.39 (-1.49 to -1.29) | -1.65 (-1.75 to -1.57) | -0.88 (-0.93 to -0.83) | -1.60 (-1.70 to -1.51) |
| part 1: by asset class (corrected group edges) | -0.10 (-0.10 to -0.09) | -0.16 (-0.17 to -0.15) | -0.10 (-0.10 to -0.09) | -0.16 (-0.17 to -0.15) | -0.08 (-0.08 to -0.08) | -0.13 (-0.14 to -0.13) |
| part 1 with fixed-rate debt repricing (no debt relief) | +0.17 (+0.16 to +0.18) | +0.10 (+0.09 to +0.11) | +0.11 (+0.10 to +0.12) | +0.04 (+0.03 to +0.05) | +0.11 (+0.10 to +0.11) | +0.07 (+0.06 to +0.08) |
| part 1 with business owners and capital income | -0.11 (-0.13 to -0.10) | -0.18 (-0.19 to -0.17) | -0.11 (-0.12 to -0.10) | -0.18 (-0.19 to -0.16) | -0.09 (-0.10 to -0.08) | -0.15 (-0.16 to -0.14) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | -0.47 (-0.52 to -0.42) | -0.73 (-0.79 to -0.66) | -0.46 (-0.50 to -0.41) | -0.71 (-0.77 to -0.65) | -0.37 (-0.40 to -0.33) | -0.61 (-0.67 to -0.56) |
| part 1 with the tail only | -0.34 (-0.37 to -0.31) | -0.60 (-0.65 to -0.55) | -0.34 (-0.37 to -0.31) | -0.60 (-0.65 to -0.55) | -0.28 (-0.31 to -0.26) | -0.49 (-0.54 to -0.45) |
| tail exponent one standard error lower (1.354: a heavier tail) | -0.59 (-0.65 to -0.53) | -0.92 (-1.00 to -0.83) | -0.57 (-0.63 to -0.51) | -0.89 (-0.98 to -0.81) | -0.46 (-0.51 to -0.41) | -0.77 (-0.84 to -0.69) |
| tail exponent one standard error higher (1.626) | -0.38 (-0.42 to -0.35) | -0.60 (-0.64 to -0.55) | -0.37 (-0.41 to -0.34) | -0.58 (-0.63 to -0.54) | -0.30 (-0.33 to -0.27) | -0.50 (-0.55 to -0.46) |
| cutoff at the 99th percentile (exponent 1.576) | -0.43 (-0.47 to -0.40) | -0.67 (-0.71 to -0.62) | -0.42 (-0.45 to -0.39) | -0.65 (-0.69 to -0.61) | -0.33 (-0.36 to -0.31) | -0.56 (-0.60 to -0.52) |
| generalised Pareto above the main cutoff | -0.42 (-0.46 to -0.38) | -0.66 (-0.71 to -0.60) | -0.41 (-0.45 to -0.37) | -0.64 (-0.70 to -0.59) | -0.33 (-0.36 to -0.30) | -0.55 (-0.60 to -0.50) |
| generalised Pareto from the 90th percentile | -0.45 (-0.52 to -0.38) | -0.76 (-0.85 to -0.66) | -0.45 (-0.52 to -0.38) | -0.76 (-0.86 to -0.66) | -0.37 (-0.43 to -0.32) | -0.63 (-0.72 to -0.55) |
| 1 tail household per type | -0.15 (-0.18 to -0.12) | -0.23 (-0.27 to -0.20) | -0.15 (-0.18 to -0.12) | -0.23 (-0.27 to -0.19) | -0.12 (-0.14 to -0.10) | -0.20 (-0.23 to -0.17) |
| 6 tail households per type | -0.60 (-0.63 to -0.57) | -0.91 (-0.95 to -0.87) | -0.57 (-0.61 to -0.54) | -0.88 (-0.92 to -0.84) | -0.46 (-0.48 to -0.43) | -0.76 (-0.80 to -0.73) |
| no interest gradient at the very top | -0.43 (-0.47 to -0.38) | -0.69 (-0.75 to -0.63) | -0.42 (-0.46 to -0.38) | -0.68 (-0.73 to -0.62) | -0.34 (-0.37 to -0.30) | -0.58 (-0.63 to -0.52) |
| interest gradient on the inflation pass-through too | +12.39 (+11.32 to +13.54) | +17.03 (+15.62 to +18.53) | +20.56 (+18.95 to +22.27) | +26.78 (+24.89 to +28.75) | +4.38 (+3.94 to +4.85) | +29.06 (+27.09 to +31.16) |
| higher real-estate gains for the top group | -0.47 (-0.51 to -0.42) | -0.73 (-0.79 to -0.66) | -0.45 (-0.50 to -0.41) | -0.71 (-0.77 to -0.65) | -0.36 (-0.40 to -0.33) | -0.61 (-0.67 to -0.56) |
| no business-owner split (group averages) | -0.48 (-0.52 to -0.44) | -0.74 (-0.80 to -0.68) | -0.46 (-0.50 to -0.42) | -0.72 (-0.78 to -0.66) | -0.37 (-0.40 to -0.34) | -0.62 (-0.67 to -0.57) |
| no capital income | -0.33 (-0.37 to -0.29) | -0.59 (-0.64 to -0.53) | -0.33 (-0.37 to -0.29) | -0.59 (-0.64 to -0.53) | -0.27 (-0.31 to -0.24) | -0.48 (-0.53 to -0.44) |
| fixed-rate debt reprices too (no debt relief) | +0.61 (+0.54 to +0.67) | +0.33 (+0.28 to +0.37) | +0.38 (+0.34 to +0.43) | +0.11 (+0.08 to +0.14) | +0.38 (+0.34 to +0.43) | +0.23 (+0.19 to +0.27) |
| real assets follow half of inflation | -4.53 (-4.87 to -4.20) | -6.49 (-6.95 to -6.04) | -4.37 (-4.70 to -4.04) | -6.74 (-7.23 to -6.26) | -1.50 (-1.61 to -1.38) | -6.42 (-6.89 to -5.96) |
| owners keep the private premium, shared by positive wealth (no tail) | -0.08 (-0.10 to -0.07) | -0.09 (-0.10 to -0.08) | -0.08 (-0.10 to -0.07) | -0.11 (-0.12 to -0.10) | -0.07 (-0.08 to -0.06) | -0.09 (-0.10 to -0.08) |
| owners keep the private premium, shared by shares and business equity (no tail) | -0.07 (-0.08 to -0.05) | -0.07 (-0.08 to -0.05) | -0.07 (-0.08 to -0.06) | -0.09 (-0.10 to -0.08) | -0.06 (-0.07 to -0.05) | -0.07 (-0.08 to -0.06) |

## 4. The programme's effect on the top 10% share of wealth at year 20 (points)

With no programme (%): Reference p1 63.78, main 70.14; Adverse p1 65.40, main 71.55; Stress p1 65.40, main 71.55.

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | -26.97 (-27.63 to -26.31) | -33.26 (-34.00 to -32.55) | -25.36 (-26.07 to -24.66) | -34.27 (-35.05 to -33.53) | -13.02 (-13.40 to -12.62) | -32.59 (-33.35 to -31.85) |
| part 1: by asset class (corrected group edges) | -3.44 (-3.51 to -3.37) | -4.83 (-4.91 to -4.75) | -3.35 (-3.43 to -3.27) | -4.73 (-4.82 to -4.65) | -2.56 (-2.62 to -2.49) | -4.25 (-4.33 to -4.16) |
| part 1 with fixed-rate debt repricing (no debt relief) | +0.97 (+0.91 to +1.03) | -0.54 (-0.61 to -0.47) | +0.09 (+0.02 to +0.15) | -1.38 (-1.46 to -1.31) | +0.50 (+0.46 to +0.54) | -0.80 (-0.87 to -0.73) |
| part 1 with business owners and capital income | -3.65 (-3.72 to -3.58) | -5.03 (-5.10 to -4.96) | -3.52 (-3.60 to -3.45) | -4.89 (-4.97 to -4.81) | -2.68 (-2.73 to -2.62) | -4.41 (-4.49 to -4.33) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | -3.28 (-3.41 to -3.15) | -4.56 (-4.72 to -4.41) | -3.14 (-3.26 to -3.01) | -4.39 (-4.55 to -4.23) | -2.38 (-2.48 to -2.28) | -3.95 (-4.09 to -3.80) |
| part 1 with the tail only | -3.03 (-3.15 to -2.91) | -4.32 (-4.47 to -4.17) | -2.93 (-3.05 to -2.80) | -4.20 (-4.35 to -4.05) | -2.23 (-2.32 to -2.14) | -3.75 (-3.89 to -3.60) |
| tail exponent one standard error lower (1.354: a heavier tail) | -3.09 (-3.22 to -2.95) | -4.32 (-4.48 to -4.14) | -2.94 (-3.07 to -2.81) | -4.14 (-4.30 to -3.97) | -2.23 (-2.33 to -2.13) | -3.71 (-3.86 to -3.55) |
| tail exponent one standard error higher (1.626) | -3.41 (-3.54 to -3.29) | -4.73 (-4.88 to -4.59) | -3.27 (-3.39 to -3.15) | -4.57 (-4.71 to -4.42) | -2.48 (-2.57 to -2.39) | -4.11 (-4.25 to -3.97) |
| cutoff at the 99th percentile (exponent 1.576) | -3.28 (-3.36 to -3.19) | -4.57 (-4.67 to -4.46) | -3.13 (-3.22 to -3.04) | -4.39 (-4.50 to -4.29) | -2.37 (-2.44 to -2.30) | -3.94 (-4.04 to -3.84) |
| generalised Pareto above the main cutoff | -3.32 (-3.45 to -3.19) | -4.61 (-4.77 to -4.46) | -3.17 (-3.30 to -3.05) | -4.44 (-4.59 to -4.29) | -2.41 (-2.51 to -2.31) | -3.99 (-4.14 to -3.85) |
| generalised Pareto from the 90th percentile | -3.16 (-3.34 to -2.97) | -4.39 (-4.62 to -4.17) | -3.01 (-3.18 to -2.83) | -4.23 (-4.44 to -4.01) | -2.31 (-2.44 to -2.18) | -3.79 (-3.99 to -3.58) |
| 1 tail household per type | -3.44 (-3.60 to -3.29) | -4.75 (-4.94 to -4.56) | -3.30 (-3.46 to -3.15) | -4.60 (-4.78 to -4.41) | -2.51 (-2.63 to -2.40) | -4.14 (-4.32 to -3.97) |
| 6 tail households per type | -3.31 (-3.39 to -3.23) | -4.61 (-4.70 to -4.53) | -3.16 (-3.25 to -3.08) | -4.44 (-4.54 to -4.34) | -2.39 (-2.46 to -2.33) | -3.99 (-4.09 to -3.89) |
| no interest gradient at the very top | -3.27 (-3.39 to -3.14) | -4.55 (-4.71 to -4.39) | -3.12 (-3.25 to -3.00) | -4.38 (-4.53 to -4.22) | -2.37 (-2.47 to -2.28) | -3.93 (-4.08 to -3.79) |
| interest gradient on the inflation pass-through too | +1.75 (+1.26 to +2.26) | +2.60 (+1.93 to +3.28) | +4.73 (+3.97 to +5.46) | +6.22 (+5.28 to +7.13) | -0.63 (-0.80 to -0.45) | +7.35 (+6.36 to +8.32) |
| higher real-estate gains for the top group | -3.27 (-3.40 to -3.15) | -4.56 (-4.71 to -4.40) | -3.13 (-3.26 to -3.01) | -4.38 (-4.54 to -4.23) | -2.38 (-2.47 to -2.28) | -3.94 (-4.09 to -3.79) |
| no business-owner split (group averages) | -3.23 (-3.34 to -3.11) | -4.50 (-4.65 to -4.36) | -3.09 (-3.21 to -2.97) | -4.34 (-4.49 to -4.19) | -2.34 (-2.43 to -2.25) | -3.90 (-4.04 to -3.76) |
| no capital income | -3.09 (-3.22 to -2.96) | -4.39 (-4.55 to -4.22) | -2.98 (-3.11 to -2.85) | -4.26 (-4.42 to -4.09) | -2.28 (-2.38 to -2.18) | -3.80 (-3.95 to -3.65) |
| fixed-rate debt reprices too (no debt relief) | +0.81 (+0.74 to +0.88) | -0.54 (-0.64 to -0.45) | +0.04 (-0.04 to +0.11) | -1.25 (-1.36 to -1.15) | +0.42 (+0.37 to +0.47) | -0.74 (-0.83 to -0.65) |
| real assets follow half of inflation | -18.13 (-18.39 to -17.86) | -27.29 (-27.59 to -27.00) | -16.86 (-17.15 to -16.56) | -27.94 (-28.25 to -27.61) | -5.68 (-5.84 to -5.53) | -26.24 (-26.57 to -25.92) |
| owners keep the private premium, shared by positive wealth (no tail) | -3.00 (-3.07 to -2.93) | -3.32 (-3.39 to -3.24) | -2.92 (-2.99 to -2.85) | -3.53 (-3.61 to -3.45) | -2.32 (-2.38 to -2.27) | -3.19 (-3.27 to -3.11) |
| owners keep the private premium, shared by shares and business equity (no tail) | -2.78 (-2.85 to -2.71) | -3.02 (-3.10 to -2.95) | -2.72 (-2.78 to -2.65) | -3.28 (-3.36 to -3.20) | -2.18 (-2.23 to -2.12) | -2.94 (-3.01 to -2.86) |

## 5. The programme's effect on the bottom 50% share of wealth at year 20 (points)

With no programme (%): Reference p1 4.56, main 3.73; Adverse p1 3.60, main 2.94; Stress p1 3.60, main 2.94.

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | +11.93 (+11.76 to +12.11) | +20.87 (+20.71 to +21.04) | +8.17 (+7.99 to +8.35) | +20.64 (+20.49 to +20.80) | +1.67 (+1.53 to +1.80) | +18.09 (+17.93 to +18.25) |
| part 1: by asset class (corrected group edges) | +3.07 (+3.00 to +3.15) | +4.32 (+4.24 to +4.42) | +2.92 (+2.85 to +2.99) | +4.14 (+4.05 to +4.22) | +1.93 (+1.87 to +1.98) | +3.77 (+3.69 to +3.85) |
| part 1 with fixed-rate debt repricing (no debt relief) | +0.92 (+0.87 to +0.97) | +2.19 (+2.13 to +2.25) | +1.26 (+1.21 to +1.31) | +2.43 (+2.36 to +2.49) | +0.55 (+0.51 to +0.58) | +2.03 (+1.97 to +2.09) |
| part 1 with business owners and capital income | +3.07 (+3.00 to +3.14) | +4.31 (+4.22 to +4.39) | +2.91 (+2.84 to +2.97) | +4.11 (+4.03 to +4.19) | +1.91 (+1.86 to +1.97) | +3.75 (+3.67 to +3.83) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | +2.61 (+2.49 to +2.72) | +3.68 (+3.52 to +3.83) | +2.45 (+2.33 to +2.56) | +3.47 (+3.33 to +3.62) | +1.61 (+1.53 to +1.68) | +3.16 (+3.03 to +3.30) |
| part 1 with the tail only | +2.60 (+2.49 to +2.71) | +3.68 (+3.52 to +3.83) | +2.45 (+2.34 to +2.55) | +3.49 (+3.33 to +3.63) | +1.61 (+1.54 to +1.69) | +3.17 (+3.03 to +3.30) |
| tail exponent one standard error lower (1.354: a heavier tail) | +2.40 (+2.28 to +2.51) | +3.39 (+3.23 to +3.54) | +2.24 (+2.13 to +2.35) | +3.19 (+3.04 to +3.34) | +1.47 (+1.40 to +1.55) | +2.90 (+2.76 to +3.04) |
| tail exponent one standard error higher (1.626) | +2.76 (+2.65 to +2.87) | +3.88 (+3.74 to +4.02) | +2.59 (+2.49 to +2.70) | +3.68 (+3.54 to +3.81) | +1.71 (+1.63 to +1.78) | +3.35 (+3.22 to +3.48) |
| cutoff at the 99th percentile (exponent 1.576) | +2.57 (+2.49 to +2.65) | +3.63 (+3.52 to +3.73) | +2.41 (+2.33 to +2.49) | +3.42 (+3.32 to +3.52) | +1.59 (+1.53 to +1.64) | +3.12 (+3.02 to +3.21) |
| generalised Pareto above the main cutoff | +2.65 (+2.54 to +2.77) | +3.74 (+3.58 to +3.89) | +2.49 (+2.38 to +2.60) | +3.53 (+3.38 to +3.68) | +1.64 (+1.56 to +1.71) | +3.22 (+3.08 to +3.35) |
| generalised Pareto from the 90th percentile | +2.73 (+2.55 to +2.89) | +3.85 (+3.62 to +4.08) | +2.57 (+2.39 to +2.73) | +3.65 (+3.42 to +3.88) | +1.69 (+1.58 to +1.80) | +3.33 (+3.11 to +3.53) |
| 1 tail household per type | +2.83 (+2.69 to +2.97) | +3.98 (+3.80 to +4.17) | +2.67 (+2.53 to +2.80) | +3.79 (+3.60 to +3.97) | +1.76 (+1.66 to +1.85) | +3.45 (+3.28 to +3.62) |
| 6 tail households per type | +2.59 (+2.53 to +2.65) | +3.65 (+3.58 to +3.73) | +2.42 (+2.36 to +2.48) | +3.44 (+3.37 to +3.52) | +1.59 (+1.55 to +1.63) | +3.14 (+3.07 to +3.21) |
| no interest gradient at the very top | +2.61 (+2.49 to +2.72) | +3.67 (+3.52 to +3.83) | +2.44 (+2.33 to +2.55) | +3.47 (+3.32 to +3.62) | +1.61 (+1.53 to +1.68) | +3.16 (+3.03 to +3.29) |
| interest gradient on the inflation pass-through too | +1.65 (+1.54 to +1.74) | +2.14 (+2.00 to +2.27) | +1.10 (+0.99 to +1.20) | +1.39 (+1.25 to +1.53) | +1.35 (+1.29 to +1.41) | +1.03 (+0.88 to +1.16) |
| higher real-estate gains for the top group | +2.60 (+2.49 to +2.72) | +3.67 (+3.52 to +3.82) | +2.44 (+2.33 to +2.55) | +3.47 (+3.32 to +3.61) | +1.61 (+1.53 to +1.68) | +3.16 (+3.02 to +3.29) |
| no business-owner split (group averages) | +2.59 (+2.48 to +2.70) | +3.65 (+3.50 to +3.80) | +2.43 (+2.32 to +2.53) | +3.45 (+3.30 to +3.59) | +1.60 (+1.53 to +1.67) | +3.14 (+3.00 to +3.27) |
| no capital income | +2.62 (+2.50 to +2.73) | +3.70 (+3.55 to +3.85) | +2.46 (+2.35 to +2.57) | +3.51 (+3.36 to +3.65) | +1.62 (+1.54 to +1.70) | +3.19 (+3.05 to +3.33) |
| fixed-rate debt reprices too (no debt relief) | +0.76 (+0.71 to +0.82) | +1.82 (+1.73 to +1.92) | +1.03 (+0.96 to +1.09) | +1.99 (+1.89 to +2.09) | +0.44 (+0.40 to +0.48) | +1.66 (+1.57 to +1.74) |
| real assets follow half of inflation | +7.73 (+7.53 to +7.91) | +14.50 (+14.23 to +14.76) | +6.04 (+5.85 to +6.22) | +14.34 (+14.04 to +14.62) | +1.74 (+1.66 to +1.82) | +12.81 (+12.53 to +13.08) |
| owners keep the private premium, shared by positive wealth (no tail) | +2.49 (+2.43 to +2.56) | +2.98 (+2.91 to +3.05) | +2.33 (+2.27 to +2.39) | +3.00 (+2.94 to +3.07) | +1.59 (+1.55 to +1.64) | +2.72 (+2.65 to +2.79) |
| owners keep the private premium, shared by shares and business equity (no tail) | +2.42 (+2.36 to +2.48) | +2.88 (+2.81 to +2.95) | +2.25 (+2.20 to +2.31) | +2.92 (+2.86 to +2.99) | +1.55 (+1.51 to +1.59) | +2.63 (+2.57 to +2.70) |

## 6. The programme's effect on the wealth Gini, debts kept, at year 20

With no programme: Reference p1 0.757, main 0.798; Adverse p1 0.774, main 0.813; Stress p1 0.774, main 0.813. With debts counted as zero the effects are in summary.json (`wtGzE`).

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | -0.249 (-0.253 to -0.245) | -0.378 (-0.382 to -0.373) | -0.202 (-0.206 to -0.198) | -0.375 (-0.380 to -0.371) | -0.082 (-0.084 to -0.079) | -0.339 (-0.343 to -0.335) |
| part 1: by asset class (corrected group edges) | -0.048 (-0.049 to -0.047) | -0.069 (-0.070 to -0.068) | -0.045 (-0.046 to -0.044) | -0.065 (-0.067 to -0.064) | -0.031 (-0.032 to -0.030) | -0.059 (-0.060 to -0.058) |
| part 1 with fixed-rate debt repricing (no debt relief) | -0.005 (-0.006 to -0.005) | -0.026 (-0.027 to -0.026) | -0.012 (-0.013 to -0.011) | -0.031 (-0.032 to -0.031) | -0.003 (-0.004 to -0.003) | -0.025 (-0.025 to -0.024) |
| part 1 with business owners and capital income | -0.049 (-0.050 to -0.048) | -0.070 (-0.071 to -0.069) | -0.046 (-0.047 to -0.045) | -0.066 (-0.067 to -0.065) | -0.032 (-0.032 to -0.031) | -0.060 (-0.061 to -0.059) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | -0.043 (-0.044 to -0.041) | -0.061 (-0.063 to -0.059) | -0.039 (-0.041 to -0.038) | -0.057 (-0.059 to -0.055) | -0.027 (-0.028 to -0.026) | -0.052 (-0.053 to -0.049) |
| part 1 with the tail only | -0.041 (-0.043 to -0.040) | -0.060 (-0.062 to -0.058) | -0.038 (-0.040 to -0.037) | -0.056 (-0.058 to -0.054) | -0.027 (-0.028 to -0.025) | -0.051 (-0.053 to -0.049) |
| tail exponent one standard error lower (1.354: a heavier tail) | -0.040 (-0.041 to -0.038) | -0.057 (-0.059 to -0.054) | -0.037 (-0.038 to -0.035) | -0.053 (-0.055 to -0.051) | -0.025 (-0.026 to -0.024) | -0.048 (-0.050 to -0.046) |
| tail exponent one standard error higher (1.626) | -0.045 (-0.046 to -0.043) | -0.064 (-0.066 to -0.062) | -0.042 (-0.043 to -0.040) | -0.060 (-0.062 to -0.058) | -0.029 (-0.030 to -0.028) | -0.054 (-0.056 to -0.052) |
| cutoff at the 99th percentile (exponent 1.576) | -0.042 (-0.043 to -0.041) | -0.060 (-0.062 to -0.059) | -0.039 (-0.040 to -0.038) | -0.057 (-0.058 to -0.055) | -0.027 (-0.028 to -0.026) | -0.051 (-0.052 to -0.050) |
| generalised Pareto above the main cutoff | -0.043 (-0.045 to -0.042) | -0.062 (-0.064 to -0.059) | -0.040 (-0.042 to -0.038) | -0.058 (-0.060 to -0.056) | -0.028 (-0.029 to -0.026) | -0.052 (-0.054 to -0.050) |
| generalised Pareto from the 90th percentile | -0.043 (-0.046 to -0.041) | -0.062 (-0.065 to -0.058) | -0.040 (-0.042 to -0.037) | -0.058 (-0.061 to -0.054) | -0.028 (-0.029 to -0.026) | -0.052 (-0.055 to -0.049) |
| 1 tail household per type | -0.046 (-0.048 to -0.044) | -0.065 (-0.068 to -0.062) | -0.042 (-0.044 to -0.040) | -0.061 (-0.064 to -0.058) | -0.029 (-0.031 to -0.028) | -0.055 (-0.058 to -0.053) |
| 6 tail households per type | -0.043 (-0.044 to -0.042) | -0.061 (-0.062 to -0.060) | -0.039 (-0.040 to -0.039) | -0.057 (-0.058 to -0.056) | -0.027 (-0.028 to -0.027) | -0.051 (-0.053 to -0.050) |
| no interest gradient at the very top | -0.043 (-0.044 to -0.041) | -0.061 (-0.063 to -0.059) | -0.039 (-0.041 to -0.038) | -0.057 (-0.059 to -0.055) | -0.027 (-0.028 to -0.026) | -0.051 (-0.053 to -0.049) |
| interest gradient on the inflation pass-through too | -0.006 (-0.009 to -0.002) | -0.006 (-0.011 to -0.002) | +0.017 (+0.012 to +0.022) | +0.022 (+0.016 to +0.028) | -0.015 (-0.016 to -0.014) | +0.032 (+0.025 to +0.038) |
| higher real-estate gains for the top group | -0.043 (-0.044 to -0.041) | -0.061 (-0.063 to -0.059) | -0.039 (-0.041 to -0.038) | -0.057 (-0.059 to -0.055) | -0.027 (-0.028 to -0.026) | -0.051 (-0.053 to -0.049) |
| no business-owner split (group averages) | -0.042 (-0.044 to -0.041) | -0.060 (-0.063 to -0.058) | -0.039 (-0.041 to -0.037) | -0.057 (-0.059 to -0.054) | -0.027 (-0.028 to -0.026) | -0.051 (-0.053 to -0.049) |
| no capital income | -0.042 (-0.044 to -0.040) | -0.060 (-0.063 to -0.058) | -0.039 (-0.041 to -0.037) | -0.057 (-0.059 to -0.054) | -0.027 (-0.028 to -0.026) | -0.051 (-0.053 to -0.049) |
| fixed-rate debt reprices too (no debt relief) | -0.004 (-0.005 to -0.004) | -0.022 (-0.024 to -0.021) | -0.010 (-0.011 to -0.009) | -0.026 (-0.028 to -0.025) | -0.002 (-0.003 to -0.002) | -0.020 (-0.022 to -0.019) |
| real assets follow half of inflation | -0.165 (-0.168 to -0.162) | -0.283 (-0.286 to -0.279) | -0.140 (-0.143 to -0.137) | -0.282 (-0.286 to -0.278) | -0.045 (-0.046 to -0.043) | -0.257 (-0.260 to -0.253) |
| owners keep the private premium, shared by positive wealth (no tail) | -0.040 (-0.041 to -0.039) | -0.047 (-0.048 to -0.046) | -0.037 (-0.038 to -0.036) | -0.047 (-0.048 to -0.046) | -0.027 (-0.027 to -0.026) | -0.043 (-0.043 to -0.042) |
| owners keep the private premium, shared by shares and business equity (no tail) | -0.038 (-0.039 to -0.037) | -0.045 (-0.046 to -0.044) | -0.035 (-0.036 to -0.034) | -0.045 (-0.046 to -0.044) | -0.026 (-0.026 to -0.025) | -0.040 (-0.041 to -0.040) |

## 7. The programme's effect on the top 1% of adults' share of private-business equity at year 20 (points)

With no programme (%): Reference p1 47.20, main 58.89; Adverse p1 47.20, main 59.13; Stress p1 47.20, main 59.13; at the start: Reference p1 46.60, main 57.12; Adverse p1 46.60, main 57.12; Stress p1 46.60, main 57.12.

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| part 1: by asset class (corrected group edges) | +0.21 (+0.05 to +0.43) | +0.21 (+0.05 to +0.43) | +0.21 (+0.04 to +0.42) | +0.21 (+0.04 to +0.42) | +0.10 (-0.00 to +0.25) | +0.21 (+0.04 to +0.42) |
| part 1 with fixed-rate debt repricing (no debt relief) | +0.46 (+0.20 to +0.76) | +0.46 (+0.20 to +0.76) | +0.46 (+0.20 to +0.76) | +0.46 (+0.20 to +0.76) | +0.20 (+0.04 to +0.41) | +0.46 (+0.20 to +0.76) |
| part 1 with business owners and capital income | +0.84 (+0.34 to +1.45) | +0.72 (+0.26 to +1.31) | +0.82 (+0.34 to +1.40) | +0.82 (+0.34 to +1.40) | +0.47 (+0.13 to +0.91) | +0.82 (+0.34 to +1.40) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | +0.36 (+0.06 to +0.78) | +0.32 (+0.02 to +0.73) | +0.10 (-0.00 to +0.26) | +0.07 (-0.00 to +0.20) | +0.06 (-0.00 to +0.17) | +0.05 (-0.00 to +0.17) |
| part 1 with the tail only | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | +0.00 (-0.00 to +0.00) | +0.00 (+0.00 to +0.00) | +0.00 (-0.00 to +0.00) | +0.00 (-0.00 to +0.00) |
| tail exponent one standard error lower (1.354: a heavier tail) | +0.36 (+0.04 to +0.77) | +0.41 (+0.08 to +0.82) | +0.37 (+0.07 to +0.78) | +0.37 (+0.07 to +0.78) | +0.29 (+0.01 to +0.69) | +0.37 (+0.07 to +0.78) |
| tail exponent one standard error higher (1.626) | +0.58 (+0.16 to +1.11) | +0.58 (+0.16 to +1.11) | +0.27 (+0.02 to +0.61) | +0.27 (+0.02 to +0.61) | +0.27 (+0.02 to +0.61) | +0.27 (+0.02 to +0.61) |
| cutoff at the 99th percentile (exponent 1.576) | +0.35 (+0.07 to +0.71) | +0.35 (+0.07 to +0.71) | +0.35 (+0.07 to +0.71) | +0.35 (+0.07 to +0.71) | +0.33 (+0.05 to +0.69) | +0.35 (+0.07 to +0.71) |
| generalised Pareto above the main cutoff | +0.34 (+0.02 to +0.78) | +0.38 (+0.06 to +0.83) | +0.06 (-0.00 to +0.18) | +0.06 (-0.00 to +0.18) | +0.06 (-0.00 to +0.18) | +0.06 (-0.00 to +0.18) |
| generalised Pareto from the 90th percentile | +0.01 (-0.04 to +0.07) | +0.01 (-0.04 to +0.07) | +0.02 (+0.00 to +0.07) | +0.02 (-0.00 to +0.07) | +0.02 (+0.00 to +0.07) | +0.02 (+0.00 to +0.07) |
| 1 tail household per type | +0.51 (+0.09 to +1.06) | +0.51 (+0.09 to +1.06) | +0.34 (+0.05 to +0.74) | +0.34 (+0.05 to +0.74) | +0.34 (+0.05 to +0.74) | +0.34 (+0.05 to +0.74) |
| 6 tail households per type | +0.14 (-0.02 to +0.34) | +0.14 (-0.02 to +0.34) | +0.14 (-0.02 to +0.35) | +0.14 (-0.02 to +0.35) | +0.11 (-0.03 to +0.29) | +0.14 (-0.01 to +0.35) |
| no interest gradient at the very top | +0.36 (+0.06 to +0.78) | +0.32 (+0.02 to +0.73) | +0.10 (-0.00 to +0.26) | +0.07 (-0.00 to +0.20) | +0.06 (-0.00 to +0.17) | +0.05 (-0.00 to +0.17) |
| interest gradient on the inflation pass-through too | +0.36 (+0.06 to +0.78) | +0.32 (+0.02 to +0.73) | +0.10 (-0.00 to +0.26) | +0.07 (-0.00 to +0.20) | +0.06 (-0.00 to +0.17) | +0.05 (-0.00 to +0.17) |
| higher real-estate gains for the top group | +0.45 (+0.10 to +0.91) | +0.40 (+0.07 to +0.87) | +0.10 (-0.00 to +0.26) | +0.07 (-0.00 to +0.20) | +0.06 (-0.00 to +0.17) | +0.06 (-0.00 to +0.17) |
| no business-owner split (group averages) | +0.05 (+0.00 to +0.14) | +0.05 (+0.00 to +0.14) | +0.05 (+0.00 to +0.14) | +0.05 (+0.00 to +0.14) | +0.00 (-0.00 to +0.00) | +0.05 (-0.00 to +0.14) |
| no capital income | +0.30 (-0.00 to +0.71) | +0.30 (-0.00 to +0.71) | +0.30 (-0.00 to +0.71) | +0.30 (-0.00 to +0.71) | +0.30 (+0.00 to +0.71) | +0.30 (-0.00 to +0.71) |
| fixed-rate debt reprices too (no debt relief) | +0.48 (+0.11 to +0.95) | +0.48 (+0.12 to +0.94) | +0.23 (+0.02 to +0.51) | +0.23 (+0.02 to +0.51) | +0.06 (-0.00 to +0.17) | +0.23 (+0.02 to +0.51) |
| real assets follow half of inflation | -0.12 (-0.43 to +0.18) | -0.30 (-0.76 to +0.13) | -0.13 (-0.62 to +0.35) | -0.43 (-0.95 to +0.10) | -0.12 (-0.43 to +0.15) | -0.33 (-0.83 to +0.17) |
| owners keep the private premium, shared by positive wealth (no tail) | +0.84 (+0.34 to +1.45) | +0.84 (+0.34 to +1.45) | +0.82 (+0.34 to +1.40) | +0.82 (+0.34 to +1.40) | +0.39 (+0.08 to +0.79) | +0.82 (+0.34 to +1.40) |
| owners keep the private premium, shared by shares and business equity (no tail) | +0.84 (+0.34 to +1.45) | +0.84 (+0.34 to +1.45) | +0.82 (+0.34 to +1.40) | +0.82 (+0.34 to +1.40) | +0.47 (+0.13 to +0.91) | +0.82 (+0.34 to +1.40) |

## 8. The programme's effect on wealth poverty at year 20 (points; adults under $25,000 of real wealth, weighted)

With no programme (%): Reference off 21.9, p1 19.7, main 19.7; Adverse off 31.9, p1 24.2, main 24.1; Stress off 31.9, p1 24.2, main 24.1.

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | +21.51 (+20.97 to +22.05) | +0.66 (+0.19 to +1.10) | +45.03 (+44.44 to +45.60) | +30.16 (+29.45 to +30.81) | +24.81 (+24.15 to +25.46) | +41.65 (+40.95 to +42.32) |
| part 1: by asset class (corrected group edges) | -12.63 (-12.93 to -12.35) | -18.18 (-18.49 to -17.89) | -13.22 (-13.53 to -12.92) | -20.34 (-20.71 to -20.00) | -7.13 (-7.40 to -6.85) | -18.82 (-19.18 to -18.48) |
| part 1 with fixed-rate debt repricing (no debt relief) | -6.68 (-6.98 to -6.40) | -13.33 (-13.68 to -12.99) | -7.82 (-8.14 to -7.49) | -15.72 (-16.10 to -15.36) | -2.80 (-3.05 to -2.54) | -13.40 (-13.75 to -13.06) |
| part 1 with business owners and capital income | -12.50 (-12.80 to -12.21) | -18.05 (-18.35 to -17.76) | -12.91 (-13.24 to -12.60) | -20.05 (-20.41 to -19.71) | -6.94 (-7.21 to -6.66) | -18.54 (-18.90 to -18.18) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | -12.53 (-12.84 to -12.25) | -18.13 (-18.45 to -17.83) | -12.96 (-13.27 to -12.68) | -20.15 (-20.50 to -19.80) | -7.01 (-7.28 to -6.73) | -18.63 (-18.97 to -18.28) |
| part 1 with the tail only | -12.70 (-13.00 to -12.42) | -18.31 (-18.61 to -18.02) | -13.26 (-13.59 to -12.96) | -20.43 (-20.78 to -20.10) | -7.22 (-7.51 to -6.93) | -18.94 (-19.29 to -18.59) |
| tail exponent one standard error lower (1.354: a heavier tail) | -12.53 (-12.84 to -12.25) | -18.13 (-18.45 to -17.83) | -12.96 (-13.27 to -12.68) | -20.15 (-20.50 to -19.80) | -7.01 (-7.28 to -6.73) | -18.63 (-18.97 to -18.28) |
| tail exponent one standard error higher (1.626) | -12.53 (-12.84 to -12.25) | -18.13 (-18.45 to -17.83) | -12.96 (-13.27 to -12.68) | -20.15 (-20.50 to -19.80) | -7.01 (-7.28 to -6.73) | -18.63 (-18.97 to -18.28) |
| cutoff at the 99th percentile (exponent 1.576) | -12.53 (-12.83 to -12.25) | -18.18 (-18.48 to -17.88) | -13.04 (-13.36 to -12.73) | -20.20 (-20.57 to -19.86) | -7.00 (-7.28 to -6.72) | -18.68 (-19.04 to -18.32) |
| generalised Pareto above the main cutoff | -12.53 (-12.84 to -12.25) | -18.13 (-18.45 to -17.83) | -12.96 (-13.27 to -12.68) | -20.15 (-20.50 to -19.80) | -7.01 (-7.28 to -6.73) | -18.63 (-18.97 to -18.28) |
| generalised Pareto from the 90th percentile | -12.36 (-12.66 to -12.08) | -17.82 (-18.12 to -17.54) | -12.66 (-12.93 to -12.39) | -19.82 (-20.16 to -19.49) | -6.90 (-7.14 to -6.63) | -18.32 (-18.66 to -18.00) |
| 1 tail household per type | -12.43 (-12.74 to -12.14) | -18.00 (-18.30 to -17.72) | -12.86 (-13.17 to -12.56) | -20.04 (-20.39 to -19.71) | -6.99 (-7.25 to -6.72) | -18.50 (-18.85 to -18.16) |
| 6 tail households per type | -12.63 (-12.90 to -12.34) | -18.32 (-18.63 to -18.01) | -13.05 (-13.37 to -12.71) | -20.24 (-20.61 to -19.89) | -7.06 (-7.34 to -6.79) | -18.74 (-19.11 to -18.38) |
| no interest gradient at the very top | -12.53 (-12.84 to -12.25) | -18.13 (-18.45 to -17.83) | -12.96 (-13.27 to -12.68) | -20.15 (-20.50 to -19.80) | -7.01 (-7.28 to -6.73) | -18.63 (-18.97 to -18.28) |
| interest gradient on the inflation pass-through too | -12.53 (-12.84 to -12.25) | -18.13 (-18.45 to -17.83) | -12.96 (-13.27 to -12.68) | -20.15 (-20.50 to -19.80) | -7.01 (-7.28 to -6.73) | -18.63 (-18.97 to -18.28) |
| higher real-estate gains for the top group | -12.53 (-12.84 to -12.25) | -18.13 (-18.45 to -17.83) | -12.96 (-13.27 to -12.68) | -20.15 (-20.50 to -19.80) | -7.01 (-7.28 to -6.73) | -18.63 (-18.97 to -18.28) |
| no business-owner split (group averages) | -12.54 (-12.83 to -12.26) | -18.11 (-18.42 to -17.83) | -13.10 (-13.43 to -12.79) | -20.21 (-20.58 to -19.86) | -7.06 (-7.35 to -6.79) | -18.73 (-19.08 to -18.37) |
| no capital income | -12.68 (-12.98 to -12.39) | -18.32 (-18.63 to -18.02) | -13.16 (-13.48 to -12.85) | -20.38 (-20.73 to -20.03) | -7.17 (-7.45 to -6.88) | -18.86 (-19.21 to -18.51) |
| fixed-rate debt reprices too (no debt relief) | -6.65 (-6.94 to -6.39) | -13.33 (-13.67 to -13.02) | -7.78 (-8.12 to -7.44) | -15.59 (-15.94 to -15.24) | -2.77 (-3.01 to -2.52) | -13.26 (-13.60 to -12.93) |
| real assets follow half of inflation | -2.07 (-2.38 to -1.76) | -14.04 (-14.38 to -13.72) | +9.19 (+8.74 to +9.64) | -7.93 (-8.34 to -7.52) | +3.65 (+3.27 to +4.03) | +0.25 (-0.28 to +0.77) |
| owners keep the private premium, shared by positive wealth (no tail) | -9.72 (-10.03 to -9.43) | -13.67 (-13.97 to -13.37) | -9.56 (-9.85 to -9.27) | -14.27 (-14.61 to -13.95) | -5.40 (-5.65 to -5.15) | -12.56 (-12.89 to -12.23) |
| owners keep the private premium, shared by shares and business equity (no tail) | -9.65 (-9.95 to -9.35) | -13.59 (-13.90 to -13.29) | -9.45 (-9.74 to -9.15) | -14.10 (-14.43 to -13.78) | -5.34 (-5.58 to -5.08) | -12.35 (-12.69 to -12.02) |

## 9. The programme's effect on median real wealth at year 20 (Year-0 dollars, weighted)

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | -$182,800 (-$186,000 to -$179,800) | -$171,500 (-$174,600 to -$168,500) | -$104,500 (-$107,100 to -$102,200) | -$95,600 (-$98,100 to -$93,400) | -$97,300 (-$99,500 to -$95,200) | -$100,300 (-$102,800 to -$98,000) |
| part 1: by asset class (corrected group edges) | +$38,500 ($35,700 to $41,200) | +$60,500 ($57,300 to $63,400) | +$40,200 ($37,200 to $43,200) | +$60,100 ($57,100 to $63,200) | +$34,600 ($32,100 to $37,100) | +$51,200 ($48,200 to $54,200) |
| part 1 with fixed-rate debt repricing (no debt relief) | -$44,200 (-$46,500 to -$41,800) | -$22,800 (-$25,400 to -$20,300) | -$17,300 (-$20,100 to -$14,600) | +$2,600 (-$300 to $5,500) | -$20,900 (-$23,000 to -$18,800) | -$6,600 (-$9,600 to -$3,700) |
| part 1 with business owners and capital income | +$36,200 ($33,200 to $39,000) | +$58,900 ($55,800 to $61,800) | +$37,900 ($34,900 to $40,900) | +$57,400 ($54,300 to $60,500) | +$33,100 ($30,700 to $35,600) | +$48,600 ($45,400 to $51,600) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | +$36,000 ($33,100 to $38,800) | +$58,600 ($55,600 to $61,400) | +$37,000 ($33,800 to $40,000) | +$57,400 ($54,200 to $60,400) | +$33,400 ($30,900 to $36,100) | +$48,100 ($44,900 to $51,100) |
| part 1 with the tail only | +$38,300 ($35,300 to $41,200) | +$60,700 ($57,800 to $63,400) | +$39,700 ($36,500 to $42,800) | +$60,300 ($57,100 to $63,400) | +$34,600 ($32,100 to $37,300) | +$51,000 ($47,900 to $54,100) |
| tail exponent one standard error lower (1.354: a heavier tail) | +$36,000 ($33,100 to $38,800) | +$58,600 ($55,600 to $61,400) | +$37,000 ($33,800 to $40,000) | +$57,400 ($54,200 to $60,400) | +$33,400 ($30,900 to $36,100) | +$48,100 ($44,900 to $51,100) |
| tail exponent one standard error higher (1.626) | +$36,000 ($33,100 to $38,800) | +$58,600 ($55,600 to $61,400) | +$37,000 ($33,800 to $40,000) | +$57,400 ($54,200 to $60,400) | +$33,400 ($30,900 to $36,100) | +$48,100 ($44,900 to $51,100) |
| cutoff at the 99th percentile (exponent 1.576) | +$37,100 ($34,000 to $40,100) | +$59,000 ($56,100 to $61,800) | +$38,900 ($35,900 to $41,800) | +$58,300 ($55,100 to $61,300) | +$33,900 ($31,500 to $36,400) | +$49,500 ($46,400 to $52,400) |
| generalised Pareto above the main cutoff | +$36,000 ($33,100 to $38,800) | +$58,600 ($55,600 to $61,400) | +$37,000 ($33,800 to $40,000) | +$57,400 ($54,200 to $60,400) | +$33,400 ($30,900 to $36,100) | +$48,100 ($44,900 to $51,100) |
| generalised Pareto from the 90th percentile | +$32,600 ($29,800 to $35,400) | +$54,800 ($52,000 to $57,800) | +$33,800 ($31,000 to $36,600) | +$53,200 ($50,400 to $56,000) | +$30,600 ($28,300 to $33,100) | +$44,400 ($41,700 to $47,200) |
| 1 tail household per type | +$36,000 ($32,800 to $38,900) | +$57,400 ($54,200 to $60,300) | +$36,200 ($33,100 to $39,200) | +$56,000 ($53,000 to $59,000) | +$32,600 ($30,200 to $35,000) | +$47,000 ($43,800 to $50,100) |
| 6 tail households per type | +$41,500 ($38,800 to $44,400) | +$63,200 ($60,500 to $65,900) | +$41,300 ($38,700 to $43,800) | +$61,000 ($58,200 to $63,700) | +$35,800 ($33,300 to $38,400) | +$51,800 ($48,900 to $54,400) |
| no interest gradient at the very top | +$36,000 ($33,100 to $38,800) | +$58,600 ($55,600 to $61,400) | +$37,000 ($33,800 to $40,000) | +$57,400 ($54,200 to $60,400) | +$33,400 ($30,900 to $36,100) | +$48,100 ($44,900 to $51,100) |
| interest gradient on the inflation pass-through too | +$36,000 ($33,100 to $38,800) | +$58,600 ($55,600 to $61,400) | +$37,000 ($33,800 to $40,000) | +$57,400 ($54,200 to $60,400) | +$33,400 ($30,900 to $36,100) | +$48,100 ($44,900 to $51,100) |
| higher real-estate gains for the top group | +$36,000 ($33,100 to $38,800) | +$58,600 ($55,600 to $61,400) | +$37,000 ($33,800 to $40,000) | +$57,400 ($54,200 to $60,400) | +$33,400 ($30,900 to $36,100) | +$48,100 ($44,900 to $51,100) |
| no business-owner split (group averages) | +$36,100 ($33,100 to $38,900) | +$58,200 ($55,400 to $61,100) | +$37,300 ($34,200 to $40,400) | +$57,400 ($54,300 to $60,600) | +$33,300 ($30,700 to $36,000) | +$48,200 ($45,100 to $51,300) |
| no capital income | +$37,800 ($34,800 to $40,600) | +$60,900 ($57,800 to $63,700) | +$39,800 ($36,700 to $42,900) | +$60,500 ($57,400 to $63,500) | +$35,300 ($32,800 to $37,900) | +$51,000 ($47,900 to $54,100) |
| fixed-rate debt reprices too (no debt relief) | -$46,000 (-$48,600 to -$43,600) | -$25,100 (-$27,800 to -$22,800) | -$19,700 (-$22,600 to -$17,000) | +$500 (-$2,700 to $3,500) | -$22,100 (-$24,200 to -$20,000) | -$8,500 (-$11,600 to -$5,400) |
| real assets follow half of inflation | -$189,300 (-$192,800 to -$186,100) | -$176,800 (-$180,200 to -$173,400) | -$151,600 (-$155,000 to -$148,400) | -$139,900 (-$143,200 to -$136,700) | -$113,700 (-$116,500 to -$110,900) | -$148,900 (-$152,300 to -$145,700) |
| owners keep the private premium, shared by positive wealth (no tail) | +$28,500 ($25,800 to $31,000) | +$29,200 ($26,000 to $32,000) | +$30,800 ($27,800 to $33,500) | +$37,100 ($34,000 to $40,000) | +$28,700 ($26,400 to $31,000) | +$31,900 ($28,800 to $34,900) |
| owners keep the private premium, shared by shares and business equity (no tail) | +$26,000 ($23,300 to $28,400) | +$25,700 ($22,600 to $28,600) | +$28,200 ($25,400 to $30,900) | +$34,400 ($31,300 to $37,400) | +$27,000 ($24,600 to $29,200) | +$28,900 ($25,900 to $31,800) |

## 10. The programme's effect on basket poverty (points of adult-years; unweighted, the engine's own measure)

Weighted, at year 20 (`wtF0E`), in summary.json. With no programme (% of adult-years): Reference off 26.8, p1 26.8, r2 25.6, main 25.2; Adverse off 38.3, p1 38.2, r2 36.1, main 35.6; Stress off 38.3, p1 38.2, r2 36.1, main 35.6.

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | -16.68 (-17.00 to -16.37) | -24.64 (-24.96 to -24.32) | -22.56 (-22.95 to -22.17) | -35.26 (-35.71 to -34.80) | -8.72 (-9.00 to -8.41) | -34.52 (-34.96 to -34.07) |
| part 1: by asset class (corrected group edges) | -16.73 (-17.06 to -16.43) | -24.60 (-24.92 to -24.27) | -22.56 (-22.96 to -22.17) | -35.19 (-35.64 to -34.73) | -8.72 (-9.00 to -8.43) | -34.45 (-34.89 to -34.01) |
| part 1 with fixed-rate debt repricing (no debt relief) | -16.67 (-16.99 to -16.36) | -24.58 (-24.90 to -24.25) | -22.59 (-22.99 to -22.20) | -35.21 (-35.66 to -34.76) | -8.76 (-9.04 to -8.46) | -34.47 (-34.91 to -34.03) |
| part 1 with business owners and capital income | -16.03 (-16.34 to -15.73) | -23.51 (-23.80 to -23.20) | -21.43 (-21.81 to -21.04) | -33.27 (-33.70 to -32.83) | -8.28 (-8.55 to -8.00) | -32.61 (-33.03 to -32.18) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | -15.85 (-16.17 to -15.55) | -23.17 (-23.47 to -22.87) | -21.22 (-21.61 to -20.84) | -32.85 (-33.27 to -32.42) | -8.19 (-8.45 to -7.91) | -32.23 (-32.65 to -31.80) |
| part 1 with the tail only | -16.72 (-17.05 to -16.42) | -24.58 (-24.91 to -24.26) | -22.56 (-22.96 to -22.16) | -35.18 (-35.63 to -34.72) | -8.72 (-9.00 to -8.42) | -34.45 (-34.89 to -34.00) |
| tail exponent one standard error lower (1.354: a heavier tail) | -15.85 (-16.17 to -15.55) | -23.17 (-23.47 to -22.87) | -21.22 (-21.61 to -20.84) | -32.85 (-33.27 to -32.42) | -8.19 (-8.45 to -7.91) | -32.23 (-32.65 to -31.80) |
| tail exponent one standard error higher (1.626) | -15.85 (-16.17 to -15.55) | -23.17 (-23.47 to -22.87) | -21.22 (-21.61 to -20.84) | -32.85 (-33.27 to -32.42) | -8.19 (-8.45 to -7.91) | -32.23 (-32.65 to -31.80) |
| cutoff at the 99th percentile (exponent 1.576) | -15.79 (-16.10 to -15.50) | -23.09 (-23.38 to -22.79) | -21.12 (-21.50 to -20.74) | -32.70 (-33.12 to -32.26) | -8.15 (-8.40 to -7.87) | -32.07 (-32.50 to -31.64) |
| generalised Pareto above the main cutoff | -15.85 (-16.17 to -15.55) | -23.17 (-23.47 to -22.87) | -21.22 (-21.61 to -20.84) | -32.85 (-33.27 to -32.42) | -8.19 (-8.45 to -7.91) | -32.23 (-32.65 to -31.80) |
| generalised Pareto from the 90th percentile | -16.11 (-16.42 to -15.82) | -23.55 (-23.85 to -23.25) | -21.65 (-22.04 to -21.27) | -33.51 (-33.94 to -33.07) | -8.37 (-8.63 to -8.09) | -32.88 (-33.31 to -32.45) |
| 1 tail household per type | -16.02 (-16.33 to -15.73) | -23.46 (-23.76 to -23.16) | -21.45 (-21.84 to -21.07) | -33.26 (-33.69 to -32.82) | -8.28 (-8.55 to -8.00) | -32.61 (-33.04 to -32.18) |
| 6 tail households per type | -15.54 (-15.85 to -15.25) | -22.66 (-22.95 to -22.35) | -20.81 (-21.19 to -20.43) | -32.12 (-32.54 to -31.69) | -8.03 (-8.28 to -7.76) | -31.53 (-31.95 to -31.11) |
| no interest gradient at the very top | -15.85 (-16.17 to -15.55) | -23.17 (-23.47 to -22.87) | -21.22 (-21.61 to -20.84) | -32.85 (-33.27 to -32.42) | -8.19 (-8.45 to -7.91) | -32.23 (-32.65 to -31.80) |
| interest gradient on the inflation pass-through too | -15.85 (-16.17 to -15.55) | -23.17 (-23.47 to -22.87) | -21.22 (-21.61 to -20.84) | -32.85 (-33.27 to -32.42) | -8.19 (-8.45 to -7.91) | -32.23 (-32.65 to -31.80) |
| higher real-estate gains for the top group | -15.85 (-16.17 to -15.55) | -23.17 (-23.47 to -22.87) | -21.22 (-21.61 to -20.84) | -32.85 (-33.27 to -32.42) | -8.19 (-8.45 to -7.91) | -32.23 (-32.65 to -31.80) |
| no business-owner split (group averages) | -15.83 (-16.13 to -15.54) | -23.12 (-23.42 to -22.82) | -21.22 (-21.59 to -20.85) | -32.78 (-33.20 to -32.35) | -8.18 (-8.43 to -7.90) | -32.17 (-32.58 to -31.75) |
| no capital income | -16.72 (-17.05 to -16.42) | -24.58 (-24.91 to -24.26) | -22.56 (-22.95 to -22.16) | -35.18 (-35.63 to -34.72) | -8.72 (-9.00 to -8.43) | -34.45 (-34.89 to -34.00) |
| fixed-rate debt reprices too (no debt relief) | -15.80 (-16.11 to -15.50) | -23.16 (-23.46 to -22.85) | -21.27 (-21.65 to -20.89) | -32.89 (-33.32 to -32.46) | -8.22 (-8.48 to -7.94) | -32.26 (-32.69 to -31.84) |
| real assets follow half of inflation | -15.55 (-15.86 to -15.26) | -23.12 (-23.42 to -22.82) | -20.74 (-21.12 to -20.36) | -32.92 (-33.34 to -32.48) | -7.64 (-7.90 to -7.36) | -32.23 (-32.65 to -31.80) |
| owners keep the private premium, shared by positive wealth (no tail) | -12.37 (-12.65 to -12.10) | -19.79 (-20.09 to -19.49) | -16.72 (-17.06 to -16.39) | -27.29 (-27.69 to -26.88) | -6.59 (-6.80 to -6.36) | -24.62 (-25.00 to -24.23) |
| owners keep the private premium, shared by shares and business equity (no tail) | -11.69 (-11.96 to -11.41) | -19.28 (-19.58 to -18.98) | -15.56 (-15.88 to -15.23) | -26.33 (-26.73 to -25.93) | -5.90 (-6.11 to -5.69) | -23.29 (-23.65 to -22.92) |

## 11. Programme inflation (points a year)

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | +31.52 (+31.29 to +31.74) | +37.44 (+37.22 to +37.65) | +37.59 (+37.30 to +37.87) | +43.98 (+43.70 to +44.26) | +16.47 (+16.21 to +16.72) | +45.89 (+45.56 to +46.21) |
| part 1: by asset class (corrected group edges) | +31.51 (+31.29 to +31.74) | +37.42 (+37.21 to +37.64) | +37.62 (+37.33 to +37.90) | +43.98 (+43.70 to +44.26) | +16.49 (+16.23 to +16.74) | +45.90 (+45.57 to +46.22) |
| part 1 with fixed-rate debt repricing (no debt relief) | +31.47 (+31.24 to +31.69) | +37.40 (+37.19 to +37.62) | +37.54 (+37.26 to +37.83) | +43.95 (+43.66 to +44.23) | +16.46 (+16.20 to +16.71) | +45.84 (+45.51 to +46.16) |
| part 1 with business owners and capital income | +31.49 (+31.27 to +31.72) | +37.41 (+37.20 to +37.62) | +37.60 (+37.32 to +37.89) | +43.96 (+43.68 to +44.24) | +16.49 (+16.23 to +16.74) | +45.87 (+45.54 to +46.19) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.31 to +37.88) | +43.95 (+43.67 to +44.24) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| part 1 with the tail only | +31.51 (+31.28 to +31.73) | +37.42 (+37.21 to +37.64) | +37.61 (+37.33 to +37.90) | +43.98 (+43.70 to +44.26) | +16.49 (+16.23 to +16.74) | +45.90 (+45.56 to +46.22) |
| tail exponent one standard error lower (1.354: a heavier tail) | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.31 to +37.88) | +43.95 (+43.67 to +44.24) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| tail exponent one standard error higher (1.626) | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.31 to +37.88) | +43.95 (+43.67 to +44.24) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| cutoff at the 99th percentile (exponent 1.576) | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.30 to +37.87) | +43.95 (+43.67 to +44.23) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| generalised Pareto above the main cutoff | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.31 to +37.88) | +43.95 (+43.67 to +44.24) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| generalised Pareto from the 90th percentile | +31.49 (+31.27 to +31.72) | +37.41 (+37.20 to +37.62) | +37.61 (+37.33 to +37.90) | +43.97 (+43.68 to +44.25) | +16.49 (+16.24 to +16.75) | +45.88 (+45.55 to +46.20) |
| 1 tail household per type | +31.49 (+31.26 to +31.72) | +37.41 (+37.19 to +37.62) | +37.60 (+37.32 to +37.89) | +43.96 (+43.68 to +44.24) | +16.49 (+16.24 to +16.74) | +45.87 (+45.54 to +46.19) |
| 6 tail households per type | +31.47 (+31.24 to +31.69) | +37.39 (+37.18 to +37.61) | +37.57 (+37.29 to +37.86) | +43.94 (+43.66 to +44.22) | +16.48 (+16.23 to +16.74) | +45.84 (+45.51 to +46.16) |
| no interest gradient at the very top | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.31 to +37.88) | +43.95 (+43.67 to +44.24) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| interest gradient on the inflation pass-through too | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.31 to +37.88) | +43.95 (+43.67 to +44.24) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| higher real-estate gains for the top group | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.31 to +37.88) | +43.95 (+43.67 to +44.24) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| no business-owner split (group averages) | +31.48 (+31.26 to +31.71) | +37.40 (+37.19 to +37.62) | +37.59 (+37.31 to +37.88) | +43.95 (+43.67 to +44.24) | +16.49 (+16.23 to +16.74) | +45.86 (+45.53 to +46.18) |
| no capital income | +31.51 (+31.28 to +31.73) | +37.42 (+37.21 to +37.64) | +37.61 (+37.33 to +37.90) | +43.98 (+43.70 to +44.26) | +16.48 (+16.23 to +16.74) | +45.90 (+45.56 to +46.22) |
| fixed-rate debt reprices too (no debt relief) | +31.44 (+31.21 to +31.66) | +37.37 (+37.16 to +37.59) | +37.52 (+37.23 to +37.80) | +43.92 (+43.64 to +44.20) | +16.46 (+16.21 to +16.71) | +45.80 (+45.47 to +46.12) |
| real assets follow half of inflation | +31.46 (+31.24 to +31.69) | +37.40 (+37.19 to +37.62) | +37.54 (+37.25 to +37.82) | +43.95 (+43.67 to +44.23) | +16.46 (+16.20 to +16.71) | +45.85 (+45.52 to +46.17) |
| owners keep the private premium, shared by positive wealth (no tail) | +31.23 (+31.02 to +31.44) | +46.01 (+45.76 to +46.25) | +36.74 (+36.48 to +37.00) | +53.71 (+53.40 to +54.03) | +15.84 (+15.60 to +16.07) | +54.44 (+54.11 to +54.77) |
| owners keep the private premium, shared by shares and business equity (no tail) | +31.22 (+31.02 to +31.43) | +45.97 (+45.72 to +46.21) | +36.73 (+36.47 to +36.99) | +53.65 (+53.33 to +53.96) | +15.83 (+15.60 to +16.07) | +54.36 (+54.04 to +54.69) |

## 12. Check 2: does the tail move the economy? The programme's effect with the tail less the effect without it, same seeds

"Tail only" against part 1's reading, and the main reading against the same reading without the tail (r2). The preregistered rule: programme inflation, the cost of living and unweighted basket poverty must differ by less than their intervals. Each difference is followed in square brackets by the half-width of the interval of the effect itself under the reading without the tail. The unweighted poverty measures count the tail's adults as ordinary adults (about 18 of 500 where the population has 2.6%), so they also move through who is counted; the weighted year-20 measures are given beside them.

| Comparison | Outcome | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|---|
| tailonly less p1 | programme inflation (points a year) | -0.005 (-0.006 to -0.003) [0.226] | -0.003 (-0.003 to -0.003) [0.215] | -0.004 (-0.006 to -0.002) [0.286] | -0.003 (-0.003 to -0.003) [0.283] | -0.001 (-0.002 to -0.000) [0.254] | -0.004 (-0.005 to -0.004) [0.327] |
| tailonly less p1 | adults below the cost of living (points of adult-years, unweighted) | +0.01 (+0.01 to +0.02) [0.37] | +0.02 (+0.01 to +0.03) [0.41] | +0.01 (+0.00 to +0.01) [0.46] | +0.01 (+0.00 to +0.01) [0.52] | +0.00 (+0.00 to +0.01) [0.35] | +0.01 (+0.00 to +0.01) [0.51] |
| tailonly less p1 | basket poverty (points of adult-years, unweighted) | +0.01 (+0.00 to +0.01) [0.31] | +0.01 (+0.01 to +0.02) [0.32] | +0.00 (+0.00 to +0.01) [0.40] | +0.01 (+0.00 to +0.01) [0.45] | +0.00 (+0.00 to +0.01) [0.29] | +0.01 (+0.00 to +0.01) [0.44] |
| tailonly less p1 | basket poverty at year 20, weighted (points) | -0.14 (-0.18 to -0.09) [0.32] | -0.23 (-0.27 to -0.18) [0.35] | -0.04 (-0.10 to +0.02) [0.69] | -0.19 (-0.24 to -0.13) [0.76] | +0.02 (-0.02 to +0.06) [0.53] | -0.16 (-0.22 to -0.10) [0.72] |
| tailonly less p1 | wealth poverty at year 20, weighted (points) | -0.07 (-0.14 to +0.01) [0.29] | -0.13 (-0.19 to -0.06) [0.30] | -0.05 (-0.14 to +0.05) [0.31] | -0.09 (-0.18 to -0.00) [0.35] | -0.09 (-0.18 to +0.00) [0.28] | -0.12 (-0.20 to -0.03) [0.35] |
| tailonly less p1 | price level at year 20 (ratio to Year 0) | -0.12 (-0.17 to -0.09) [5.97] | -0.17 (-0.19 to -0.15) [12.47] | -0.35 (-0.50 to -0.20) [25.44] | -0.54 (-0.58 to -0.50) [57.16] | -0.00 (-0.01 to -0.00) [1.16] | -1.08 (-1.21 to -0.98) [82.95] |
| main less r2 | programme inflation (points a year) | -0.010 (-0.012 to -0.009) [0.225] | -0.008 (-0.008 to -0.007) [0.215] | -0.011 (-0.013 to -0.008) [0.286] | -0.009 (-0.010 to -0.008) [0.283] | -0.001 (-0.002 to -0.001) [0.254] | -0.013 (-0.014 to -0.012) [0.326] |
| main less r2 | adults below the cost of living (points of adult-years, unweighted) | +0.31 (+0.26 to +0.37) [0.36] | +0.60 (+0.53 to +0.66) [0.38] | +0.34 (+0.28 to +0.40) [0.45] | +0.71 (+0.64 to +0.79) [0.50] | +0.16 (+0.11 to +0.21) [0.34] | +0.64 (+0.57 to +0.71) [0.49] |
| main less r2 | basket poverty (points of adult-years, unweighted) | +0.18 (+0.15 to +0.21) [0.30] | +0.34 (+0.31 to +0.37) [0.30] | +0.20 (+0.17 to +0.24) [0.39] | +0.42 (+0.39 to +0.46) [0.44] | +0.09 (+0.06 to +0.12) [0.28] | +0.39 (+0.35 to +0.43) [0.43] |
| main less r2 | basket poverty at year 20, weighted (points) | -0.10 (-0.15 to -0.04) [0.31] | -0.17 (-0.22 to -0.12) [0.33] | -0.05 (-0.13 to +0.03) [0.61] | -0.12 (-0.18 to -0.05) [0.68] | +0.00 (-0.05 to +0.05) [0.51] | -0.09 (-0.15 to -0.03) [0.66] |
| main less r2 | wealth poverty at year 20, weighted (points) | -0.03 (-0.10 to +0.04) [0.30] | -0.09 (-0.15 to -0.02) [0.29] | -0.06 (-0.14 to +0.03) [0.32] | -0.09 (-0.18 to -0.01) [0.35] | -0.07 (-0.15 to +0.01) [0.27] | -0.09 (-0.18 to +0.00) [0.36] |
| main less r2 | price level at year 20 (ratio to Year 0) | -0.27 (-0.32 to -0.23) [5.94] | -0.46 (-0.49 to -0.42) [12.45] | -0.97 (-1.22 to -0.75) [25.35] | -1.76 (-1.90 to -1.62) [57.08] | -0.01 (-0.01 to -0.00) [1.16] | -3.25 (-3.54 to -2.98) [82.40] |

## 13. Business owners and the income wealth pays (no programme unless said; Year-0 dollars per adult)

| Environment | Reading | owners among adults, start (%) | in the bottom half of money income (%) | in the top tenth (%) | capital income per adult, start | year 20 | share of money income, year 20 (%) | sole-proprietorship income inside owners' earnings, per adult |
|---|---|---|---|---|---|---|---|---|
| Reference | r2 | 15.0 | 9.8 | 32.1 | $6,400 | $11,700 | 11.0 | $1,200 |
| Reference | main | 15.0 | 9.9 | 32.3 | $9,800 | $18,300 | 15.9 | $1,200 |
| Reference | bo0 | 0.0 | 0.0 | 0.0 | $10,000 | $18,800 | 16.3 | $0 |
| Reference | ci0 | 15.0 | 12.0 | 23.0 | $0 | $0 | 0.0 | $1,200 |
| Adverse | r2 | 15.0 | 9.8 | 32.1 | $6,400 | $11,500 | 16.3 | $700 |
| Adverse | main | 15.0 | 9.9 | 32.3 | $9,800 | $18,000 | 22.6 | $700 |
| Adverse | bo0 | 0.0 | 0.0 | 0.0 | $10,000 | $18,500 | 23.2 | $0 |
| Adverse | ci0 | 15.0 | 12.0 | 23.0 | $0 | $0 | 0.0 | $700 |
| Stress | r2 | 15.0 | 9.8 | 32.1 | $6,400 | $11,500 | 16.3 | $700 |
| Stress | main | 15.0 | 9.9 | 32.3 | $9,800 | $18,000 | 22.6 | $700 |
| Stress | bo0 | 0.0 | 0.0 | 0.0 | $10,000 | $18,500 | 23.2 | $0 |
| Stress | ci0 | 15.0 | 12.0 | 23.0 | $0 | $0 | 0.0 | $700 |

SCF 2022: 14.7% of the engine's families hold private-business equity; of all families 14.6%, 8.3% in the bottom half of income and 41.0% in the top tenth (the Bulletin's 20%, 14% and "nearly half" also count the self-employed without business equity). The engine's own unweighted income Gini (`giniD`) and wealth Ginis (`eGiniW`, `eGiniWN`) are not valid where the tail is on; the weighted keys are.

**The programme's effect on capital income per adult at year 20 (Year-0 dollars)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| part 1 with business owners and capital income | -$600 (-$600 to -$600) | -$600 (-$600 to -$500) | -$500 (-$500 to -$500) | -$500 (-$500 to -$400) | -$400 (-$400 to -$400) | -$500 (-$500 to -$500) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | -$1,100 (-$1,100 to -$1,000) | -$1,100 (-$1,200 to -$1,000) | -$900 (-$1,000 to -$800) | -$900 (-$1,000 to -$800) | -$700 (-$800 to -$700) | -$900 (-$1,000 to -$900) |
| fixed-rate debt reprices too (no debt relief) | -$1,100 (-$1,100 to -$1,000) | -$1,100 (-$1,100 to -$1,000) | -$900 (-$1,000 to -$800) | -$900 (-$1,000 to -$800) | -$700 (-$800 to -$700) | -$900 (-$1,000 to -$900) |
| real assets follow half of inflation | -$16,600 (-$18,300 to -$15,000) | -$17,100 (-$18,900 to -$15,400) | -$14,100 (-$15,600 to -$12,700) | -$14,400 (-$15,900 to -$12,900) | -$11,300 (-$12,400 to -$10,200) | -$14,500 (-$16,000 to -$13,000) |

**Shares of the last year's real gains on real assets received by the top 1% and top 10% of adults ranked by disposable income plus those gains (%)** (Campbell, Robbins and Wylde 2025 report 45.3% and 75.7% of capital gains for 2002-2021 on a comparable ranking; a comparison, not a target)

| Reading | Reference: none / release / C2.2 | Adverse: none / release / C2.2 | Stress: none / release / C2.2 |
|---|---|---|---|
| part 1: by asset class (corrected group edges) | 25.8 and 63.7 / 25.3 and 62.8 / 25.2 and 62.7 | 27.0 and 67.1 / 26.7 and 65.7 / 26.5 and 65.3 | 27.0 and 67.1 / 26.8 and 66.3 / 26.8 and 65.9 |
| part 1 with business owners and capital income | 27.3 and 66.9 / 27.2 and 65.8 / 27.2 and 65.7 | 27.7 and 69.6 / 27.6 and 68.4 / 27.6 and 68.0 | 27.7 and 69.6 / 27.6 and 69.0 / 27.7 and 68.6 |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | 37.6 and 73.8 / 37.4 and 72.9 / 37.3 and 72.8 | 38.0 and 75.8 / 37.8 and 74.9 / 37.7 and 74.7 | 38.0 and 75.8 / 37.9 and 75.3 / 37.8 and 75.1 |
| higher real-estate gains for the top group | 37.7 and 73.9 / 37.5 and 73.0 / 37.4 and 72.8 | 38.1 and 75.9 / 37.9 and 75.0 / 37.8 and 74.7 | 38.1 and 75.9 / 38.0 and 75.3 / 37.9 and 75.2 |
| tail exponent one standard error lower (1.354: a heavier tail) | 43.1 and 76.6 / 43.0 and 75.9 / 42.9 and 75.7 | 43.5 and 78.4 / 43.4 and 77.6 / 43.3 and 77.4 | 43.5 and 78.4 / 43.4 and 77.9 / 43.4 and 77.8 |
| tail exponent one standard error higher (1.626) | 33.5 and 71.7 / 33.4 and 70.8 / 33.3 and 70.6 | 34.0 and 73.9 / 33.8 and 72.9 / 33.6 and 72.6 | 34.0 and 73.9 / 33.9 and 73.3 / 33.8 and 73.1 |

## 14. The programme's effect on the top 1% share of disposable income at year 20 (points)

With no programme (%): Reference p1 4.39, r2 6.63, main 10.49; Adverse p1 4.54, r2 8.49, main 13.70; Stress p1 4.54, r2 8.49, main 13.70. Top 10% share with no programme (%): Reference p1 24.85, r2 29.01, main 32.61; Adverse p1 25.35, r2 31.83, main 36.67; Stress p1 25.35, r2 31.83, main 36.67.

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | +0.27 (+0.21 to +0.32) | -0.35 (-0.43 to -0.28) | +0.51 (+0.42 to +0.60) | -0.19 (-0.30 to -0.09) | +0.31 (+0.26 to +0.37) | -0.00 (-0.10 to +0.09) |
| part 1: by asset class (corrected group edges) | +0.26 (+0.20 to +0.32) | -0.35 (-0.42 to -0.27) | +0.52 (+0.42 to +0.61) | -0.18 (-0.29 to -0.08) | +0.31 (+0.25 to +0.37) | +0.00 (-0.09 to +0.09) |
| part 1 with business owners and capital income | -0.08 (-0.13 to -0.02) | -1.00 (-1.07 to -0.92) | -0.09 (-0.18 to +0.00) | -1.53 (-1.65 to -1.40) | +0.01 (-0.05 to +0.07) | -0.88 (-0.98 to -0.78) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | -0.46 (-0.53 to -0.40) | -1.87 (-2.02 to -1.72) | -0.55 (-0.67 to -0.43) | -2.75 (-3.01 to -2.52) | -0.24 (-0.32 to -0.16) | -1.72 (-1.89 to -1.56) |
| no capital income | +0.24 (+0.18 to +0.30) | -0.35 (-0.43 to -0.27) | +0.49 (+0.39 to +0.57) | -0.18 (-0.29 to -0.06) | +0.29 (+0.24 to +0.35) | -0.00 (-0.10 to +0.09) |
| fixed-rate debt reprices too (no debt relief) | -0.47 (-0.53 to -0.40) | -1.87 (-2.02 to -1.71) | -0.57 (-0.69 to -0.45) | -2.76 (-3.01 to -2.53) | -0.24 (-0.33 to -0.17) | -1.73 (-1.90 to -1.57) |
| real assets follow half of inflation | -5.73 (-6.60 to -4.92) | -6.44 (-7.33 to -5.62) | -7.26 (-8.33 to -6.29) | -8.03 (-9.09 to -7.04) | -6.05 (-6.86 to -5.30) | -7.85 (-8.92 to -6.87) |
| owners keep the private premium, shared by positive wealth (no tail) | +1.13 (+1.07 to +1.20) | +1.75 (+1.65 to +1.85) | +1.63 (+1.54 to +1.71) | +2.13 (+2.02 to +2.23) | +0.72 (+0.68 to +0.77) | +2.75 (+2.62 to +2.87) |
| owners keep the private premium, shared by shares and business equity (no tail) | +2.04 (+1.93 to +2.15) | +3.31 (+3.13 to +3.47) | +2.85 (+2.71 to +2.98) | +4.04 (+3.84 to +4.22) | +1.27 (+1.20 to +1.33) | +4.73 (+4.51 to +4.93) |

**Top 10% share of disposable income (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is one number of dollars | +1.00 (+0.90 to +1.10) | -1.71 (-1.83 to -1.59) | +1.82 (+1.69 to +1.96) | -1.24 (-1.41 to -1.09) | +1.11 (+1.04 to +1.19) | -0.43 (-0.57 to -0.29) |
| part 1: by asset class (corrected group edges) | +1.00 (+0.90 to +1.09) | -1.68 (-1.81 to -1.56) | +1.85 (+1.71 to +1.98) | -1.19 (-1.35 to -1.03) | +1.11 (+1.03 to +1.19) | -0.37 (-0.52 to -0.24) |
| part 1 with business owners and capital income | +0.54 (+0.44 to +0.63) | -2.57 (-2.70 to -2.44) | +0.99 (+0.85 to +1.13) | -2.93 (-3.12 to -2.74) | +0.67 (+0.59 to +0.76) | -1.50 (-1.65 to -1.36) |
| main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule) | +0.19 (+0.09 to +0.29) | -3.28 (-3.44 to -3.11) | +0.54 (+0.37 to +0.70) | -3.95 (-4.19 to -3.72) | +0.43 (+0.32 to +0.53) | -2.19 (-2.38 to -2.01) |
| no capital income | +0.98 (+0.87 to +1.08) | -1.68 (-1.83 to -1.54) | +1.83 (+1.68 to +1.98) | -1.18 (-1.37 to -1.00) | +1.11 (+1.02 to +1.21) | -0.37 (-0.53 to -0.22) |
| owners keep the private premium, shared by positive wealth (no tail) | +2.29 (+2.20 to +2.37) | +3.03 (+2.89 to +3.15) | +3.41 (+3.30 to +3.52) | +4.01 (+3.86 to +4.15) | +1.61 (+1.54 to +1.67) | +5.44 (+5.30 to +5.58) |
| owners keep the private premium, shared by shares and business equity (no tail) | +3.63 (+3.51 to +3.73) | +5.42 (+5.26 to +5.56) | +5.25 (+5.13 to +5.38) | +7.00 (+6.84 to +7.15) | +2.37 (+2.29 to +2.44) | +8.53 (+8.38 to +8.68) |

## 15. The programme's effect on mean real wealth in three parts (Year-0 dollars per adult, weighted)

E: the opening nominal position held untouched. V: the opening real assets held untouched. S: saving since the start and what it earned (capital income that is saved is here).

**Reference**

| Reading | Design | Group | E | V | S | Whole |
|---|---|---|---|---|---|---|
| p1 | release | all adults | +$1,300 ($200 to $2,400) | -$0 (-$0 to $0) | -$24,300 (-$25,100 to -$23,600) | -$23,000 |
| p1 | C2.2 | all adults | -$900 (-$2,000 to $200) | -$0 (-$0 to $0) | -$800 (-$1,600 to -$100) | -$1,700 |
| p1chi | release | all adults | -$98,900 (-$100,200 to -$97,700) | -$0 (-$0 to -$0) | -$20,900 (-$21,700 to -$20,200) | -$119,900 |
| p1chi | C2.2 | all adults | -$101,400 (-$102,800 to -$100,200) | -$0 (-$0 to $0) | +$600 (-$100 to $1,300) | -$100,900 |
| r2 | release | all adults | -$400 (-$1,900 to $1,100) | -$0 (-$0 to $0) | -$37,800 (-$38,600 to -$37,000) | -$38,200 |
| r2 | C2.2 | all adults | -$2,600 (-$4,100 to -$1,100) | +$0 (-$0 to $0) | -$15,200 (-$15,900 to -$14,300) | -$17,700 |
| main | release | all adults | -$14,400 (-$18,600 to -$10,500) | +$0 (-$0 to $0) | -$43,400 (-$45,300 to -$41,600) | -$57,700 |
|  |  | fifth 1 of starting wealth | +$35,900 ($34,700 to $37,000) | +$0 (-$0 to $0) | -$15,800 (-$16,600 to -$15,000) | +$20,100 |
|  |  | fifth 2 of starting wealth | +$43,700 ($43,000 to $44,200) | +$0 (-$0 to $0) | -$3,900 (-$5,600 to -$2,200) | +$39,800 |
|  |  | fifth 3 of starting wealth | +$68,100 ($67,100 to $69,000) | +$0 (-$0 to $0) | -$11,200 (-$13,200 to -$9,300) | +$56,900 |
|  |  | fifth 4 of starting wealth | +$46,300 ($45,200 to $47,400) | +$0 (-$0 to $0) | -$32,500 (-$34,800 to -$30,200) | +$13,800 |
|  |  | fifth 5 of starting wealth | -$265,200 (-$285,500 to -$246,000) | -$0 (-$0 to $0) | -$153,300 (-$162,200 to -$144,700) | -$418,500 |
| main | C2.2 | all adults | -$17,000 (-$21,400 to -$13,000) | +$0 (-$0 to $0) | -$20,800 (-$22,800 to -$18,900) | -$37,800 |
|  |  | fifth 1 of starting wealth | +$35,900 ($34,700 to $37,000) | +$0 (-$0 to $0) | +$8,300 ($7,500 to $9,200) | +$44,200 |
|  |  | fifth 2 of starting wealth | +$43,600 ($43,000 to $44,100) | +$0 (-$0 to $0) | +$22,000 ($20,300 to $23,900) | +$65,600 |
|  |  | fifth 3 of starting wealth | +$67,700 ($66,800 to $68,700) | +$0 (-$0 to $0) | +$12,900 ($10,900 to $14,900) | +$80,700 |
|  |  | fifth 4 of starting wealth | +$45,000 ($43,900 to $46,100) | +$0 (-$0 to $0) | -$9,600 (-$12,000 to -$7,100) | +$35,400 |
|  |  | fifth 5 of starting wealth | -$276,600 (-$297,600 to -$257,100) | -$0 (-$0 to $0) | -$137,700 (-$147,000 to -$128,800) | -$414,300 |
| chi1 | release | all adults | -$116,800 (-$121,300 to -$112,500) | -$0 (-$0 to $0) | -$40,000 (-$41,800 to -$38,200) | -$156,800 |
| chi1 | C2.2 | all adults | -$119,800 (-$124,500 to -$115,400) | -$0 (-$0 to $0) | -$19,400 (-$21,400 to -$17,500) | -$139,200 |
| ix05 | release | all adults | -$14,300 (-$18,500 to -$10,500) | -$936,700 (-$993,300 to -$883,300) | -$50,600 (-$53,500 to -$47,700) | -$1,001,700 |
| ix05 | C2.2 | all adults | -$17,000 (-$21,400 to -$13,000) | -$964,500 (-$1,023,200 to -$909,300) | -$30,800 (-$33,900 to -$27,900) | -$1,012,400 |

**Adverse**

| Reading | Design | Group | E | V | S | Whole |
|---|---|---|---|---|---|---|
| p1 | release | all adults | -$13,700 (-$14,700 to -$12,800) | -$0 (-$0 to -$0) | -$3,000 (-$4,000 to -$2,100) | -$16,800 |
| p1 | C2.2 | all adults | -$15,100 (-$16,000 to -$14,100) | -$0 (-$0 to -$0) | +$19,000 ($18,100 to $20,000) | +$4,000 |
| p1chi | release | all adults | -$82,700 (-$83,800 to -$81,800) | -$0 (-$0 to -$0) | -$1,700 (-$2,600 to -$800) | -$84,400 |
| p1chi | C2.2 | all adults | -$84,200 (-$85,300 to -$83,200) | -$0 (-$0 to -$0) | +$17,800 ($16,800 to $18,700) | -$66,400 |
| r2 | release | all adults | -$15,100 (-$16,400 to -$13,900) | -$0 (-$0 to -$0) | -$16,600 (-$17,600 to -$15,700) | -$31,700 |
| r2 | C2.2 | all adults | -$16,400 (-$17,700 to -$15,200) | -$0 (-$0 to -$0) | +$4,500 ($3,600 to $5,400) | -$11,900 |
| main | release | all adults | -$27,200 (-$30,700 to -$23,900) | -$0 (-$0 to -$0) | -$22,200 (-$24,100 to -$20,300) | -$49,300 |
|  |  | fifth 1 of starting wealth | +$24,000 ($23,200 to $24,700) | -$0 (-$0 to -$0) | -$7,300 (-$7,900 to -$6,600) | +$16,700 |
|  |  | fifth 2 of starting wealth | +$28,600 ($28,200 to $29,000) | -$0 (-$0 to -$0) | +$12,700 ($11,200 to $14,300) | +$41,300 |
|  |  | fifth 3 of starting wealth | +$43,100 ($42,400 to $43,800) | -$0 (-$0 to -$0) | +$13,400 ($11,100 to $15,400) | +$56,500 |
|  |  | fifth 4 of starting wealth | +$22,000 ($21,200 to $22,900) | -$0 (-$0 to -$0) | -$6,800 (-$9,000 to -$4,600) | +$15,300 |
|  |  | fifth 5 of starting wealth | -$253,100 (-$270,300 to -$236,800) | -$0 (-$0 to -$0) | -$122,700 (-$131,400 to -$114,300) | -$375,800 |
| main | C2.2 | all adults | -$28,700 (-$32,400 to -$25,400) | -$0 (-$0 to -$0) | -$1,100 (-$3,200 to $800) | -$29,900 |
|  |  | fifth 1 of starting wealth | +$23,900 ($23,200 to $24,700) | -$0 (-$0 to -$0) | +$13,300 ($12,600 to $14,000) | +$37,200 |
|  |  | fifth 2 of starting wealth | +$28,500 ($28,100 to $28,900) | -$0 (-$0 to -$0) | +$37,600 ($36,000 to $39,300) | +$66,100 |
|  |  | fifth 3 of starting wealth | +$42,800 ($42,200 to $43,500) | -$0 (-$0 to -$0) | +$36,600 ($34,300 to $38,800) | +$79,400 |
|  |  | fifth 4 of starting wealth | +$21,200 ($20,400 to $22,000) | -$0 (-$0 to -$0) | +$14,800 ($12,400 to $17,200) | +$36,000 |
|  |  | fifth 5 of starting wealth | -$259,700 (-$277,400 to -$243,200) | -$0 (-$0 to -$0) | -$107,700 (-$116,700 to -$99,100) | -$367,400 |
| chi1 | release | all adults | -$97,700 (-$101,500 to -$94,100) | -$0 (-$0 to -$0) | -$20,800 (-$22,700 to -$18,900) | -$118,500 |
| chi1 | C2.2 | all adults | -$99,400 (-$103,300 to -$95,700) | -$0 (-$0 to -$0) | -$2,400 (-$4,400 to -$500) | -$101,700 |
| ix05 | release | all adults | -$27,100 (-$30,700 to -$23,900) | -$798,400 (-$846,800 to -$752,700) | -$25,300 (-$27,900 to -$22,800) | -$850,800 |
| ix05 | C2.2 | all adults | -$28,700 (-$32,400 to -$25,400) | -$814,900 (-$864,700 to -$768,300) | -$9,100 (-$11,800 to -$6,600) | -$852,800 |

**Stress**

| Reading | Design | Group | E | V | S | Whole |
|---|---|---|---|---|---|---|
| p1 | release | all adults | -$2,200 (-$2,900 to -$1,400) | -$0 (-$0 to -$0) | -$9,700 (-$10,300 to -$9,000) | -$11,800 |
| p1 | C2.2 | all adults | -$15,300 (-$16,300 to -$14,400) | -$0 (-$0 to -$0) | +$10,300 ($9,300 to $11,200) | -$5,100 |
| p1chi | release | all adults | -$67,400 (-$68,300 to -$66,500) | -$0 (-$0 to -$0) | -$5,700 (-$6,300 to -$5,000) | -$73,100 |
| p1chi | C2.2 | all adults | -$84,500 (-$85,600 to -$83,500) | -$0 (-$0 to -$0) | +$9,300 ($8,400 to $10,300) | -$75,100 |
| r2 | release | all adults | -$3,300 (-$4,300 to -$2,300) | -$0 (-$0 to -$0) | -$18,900 (-$19,500 to -$18,300) | -$22,200 |
| r2 | C2.2 | all adults | -$16,700 (-$18,000 to -$15,500) | -$0 (-$0 to -$0) | -$4,500 (-$5,400 to -$3,500) | -$21,200 |
| main | release | all adults | -$13,000 (-$15,900 to -$10,200) | -$0 (-$0 to -$0) | -$22,900 (-$24,200 to -$21,600) | -$35,900 |
|  |  | fifth 1 of starting wealth | +$23,200 ($22,500 to $24,000) | -$0 (-$0 to -$0) | -$12,400 (-$13,000 to -$11,900) | +$10,800 |
|  |  | fifth 2 of starting wealth | +$28,100 ($27,700 to $28,500) | -$0 (-$0 to -$0) | -$2,900 (-$4,000 to -$1,800) | +$25,200 |
|  |  | fifth 3 of starting wealth | +$43,500 ($42,900 to $44,200) | -$0 (-$0 to -$0) | -$0 (-$1,600 to $1,600) | +$43,500 |
|  |  | fifth 4 of starting wealth | +$28,100 ($27,400 to $28,900) | -$0 (-$0 to -$0) | -$10,400 (-$11,900 to -$8,800) | +$17,700 |
|  |  | fifth 5 of starting wealth | -$187,500 (-$201,800 to -$174,300) | -$0 (-$0 to -$0) | -$88,800 (-$95,000 to -$82,900) | -$276,200 |
| main | C2.2 | all adults | -$29,100 (-$32,700 to -$25,700) | -$0 (-$0 to -$0) | -$10,200 (-$12,300 to -$8,300) | -$39,300 |
|  |  | fifth 1 of starting wealth | +$23,900 ($23,100 to $24,700) | -$0 (-$0 to -$0) | +$6,200 ($5,500 to $6,900) | +$30,100 |
|  |  | fifth 2 of starting wealth | +$28,500 ($28,100 to $28,900) | -$0 (-$0 to -$0) | +$29,500 ($27,800 to $31,300) | +$58,000 |
|  |  | fifth 3 of starting wealth | +$42,800 ($42,100 to $43,400) | -$0 (-$0 to -$0) | +$28,000 ($25,700 to $30,200) | +$70,800 |
|  |  | fifth 4 of starting wealth | +$21,000 ($20,200 to $21,900) | -$0 (-$0 to -$0) | +$5,400 ($3,000 to $7,800) | +$26,400 |
|  |  | fifth 5 of starting wealth | -$261,200 (-$278,900 to -$244,600) | -$0 (-$0 to -$0) | -$120,000 (-$129,300 to -$111,200) | -$381,200 |
| chi1 | release | all adults | -$79,600 (-$82,800 to -$76,600) | -$0 (-$0 to -$0) | -$19,000 (-$20,300 to -$17,700) | -$98,600 |
| chi1 | C2.2 | all adults | -$99,700 (-$103,700 to -$96,100) | -$0 (-$0 to -$0) | -$11,100 (-$13,200 to -$9,200) | -$110,800 |
| ix05 | release | all adults | -$12,900 (-$15,800 to -$10,200) | -$637,000 (-$675,400 to -$600,300) | -$23,000 (-$25,100 to -$21,000) | -$672,900 |
| ix05 | C2.2 | all adults | -$29,100 (-$32,700 to -$25,700) | -$818,500 (-$868,400 to -$771,600) | -$17,700 (-$20,300 to -$15,100) | -$865,300 |

## 16. The owners readings (no tail): owners keep the private premium, against the release reading (lower prices for customers)

Each cell: the programme's effect under the reading, and in brackets the reading less r2 on the same seeds.

**top 1% share of wealth (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| r2: lower prices (release reading) | -0.98 (-1.04 to -0.92) | -1.49 (-1.56 to -1.42) | -0.96 (-1.02 to -0.91) | -1.47 (-1.53 to -1.40) | -0.76 (-0.81 to -0.71) | -1.28 (-1.34 to -1.21) |
| owners keep the private premium, shared by positive wealth (no tail) | -0.73 (-0.79 to -0.67) [+0.25 (+0.24 to +0.26)] | -0.80 (-0.87 to -0.73) [+0.69 (+0.67 to +0.71)] | -0.74 (-0.79 to -0.68) [+0.23 (+0.22 to +0.23)] | -0.93 (-0.99 to -0.87) [+0.54 (+0.52 to +0.56)] | -0.63 (-0.67 to -0.59) [+0.13 (+0.12 to +0.14)] | -0.80 (-0.86 to -0.74) [+0.48 (+0.46 to +0.50)] |
| owners keep the private premium, shared by shares and business equity (no tail) | -0.61 (-0.68 to -0.55) [+0.37 (+0.35 to +0.38)] | -0.64 (-0.71 to -0.57) [+0.85 (+0.82 to +0.88)] | -0.63 (-0.69 to -0.58) [+0.33 (+0.32 to +0.34)] | -0.80 (-0.86 to -0.74) [+0.67 (+0.65 to +0.70)] | -0.55 (-0.60 to -0.51) [+0.20 (+0.20 to +0.21)] | -0.66 (-0.72 to -0.60) [+0.61 (+0.59 to +0.63)] |

**top 10% share of wealth (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| r2: lower prices (release reading) | -3.65 (-3.72 to -3.58) | -5.03 (-5.10 to -4.96) | -3.52 (-3.60 to -3.45) | -4.89 (-4.97 to -4.81) | -2.68 (-2.73 to -2.62) | -4.41 (-4.49 to -4.33) |
| owners keep the private premium, shared by positive wealth (no tail) | -3.00 (-3.07 to -2.93) [+0.65 (+0.64 to +0.66)] | -3.32 (-3.39 to -3.24) [+1.71 (+1.69 to +1.73)] | -2.92 (-2.99 to -2.85) [+0.60 (+0.59 to +0.61)] | -3.53 (-3.61 to -3.45) [+1.36 (+1.34 to +1.38)] | -2.32 (-2.38 to -2.27) [+0.36 (+0.35 to +0.37)] | -3.19 (-3.27 to -3.11) [+1.22 (+1.20 to +1.23)] |
| owners keep the private premium, shared by shares and business equity (no tail) | -2.78 (-2.85 to -2.71) [+0.87 (+0.85 to +0.88)] | -3.02 (-3.10 to -2.95) [+2.01 (+1.98 to +2.03)] | -2.72 (-2.78 to -2.65) [+0.81 (+0.79 to +0.82)] | -3.28 (-3.36 to -3.20) [+1.61 (+1.58 to +1.63)] | -2.18 (-2.23 to -2.12) [+0.50 (+0.49 to +0.51)] | -2.94 (-3.01 to -2.86) [+1.47 (+1.45 to +1.49)] |

**wealth Gini, debts kept**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| r2: lower prices (release reading) | -0.049 (-0.050 to -0.048) | -0.070 (-0.071 to -0.069) | -0.046 (-0.047 to -0.045) | -0.066 (-0.067 to -0.065) | -0.032 (-0.032 to -0.031) | -0.060 (-0.061 to -0.059) |
| owners keep the private premium, shared by positive wealth (no tail) | -0.040 (-0.041 to -0.039) [+0.009 (+0.009 to +0.010)] | -0.047 (-0.048 to -0.046) [+0.023 (+0.022 to +0.023)] | -0.037 (-0.038 to -0.036) [+0.009 (+0.009 to +0.009)] | -0.047 (-0.048 to -0.046) [+0.019 (+0.018 to +0.019)] | -0.027 (-0.027 to -0.026) [+0.005 (+0.005 to +0.005)] | -0.043 (-0.043 to -0.042) [+0.017 (+0.017 to +0.017)] |
| owners keep the private premium, shared by shares and business equity (no tail) | -0.038 (-0.039 to -0.037) [+0.011 (+0.011 to +0.011)] | -0.045 (-0.046 to -0.044) [+0.025 (+0.025 to +0.025)] | -0.035 (-0.036 to -0.034) [+0.011 (+0.010 to +0.011)] | -0.045 (-0.046 to -0.044) [+0.021 (+0.020 to +0.021)] | -0.026 (-0.026 to -0.025) [+0.006 (+0.006 to +0.006)] | -0.040 (-0.041 to -0.040) [+0.019 (+0.019 to +0.020)] |

**top 1% share of business equity (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| r2: lower prices (release reading) | +0.84 (+0.34 to +1.45) | +0.72 (+0.26 to +1.31) | +0.82 (+0.34 to +1.40) | +0.82 (+0.34 to +1.40) | +0.47 (+0.13 to +0.91) | +0.82 (+0.34 to +1.40) |
| owners keep the private premium, shared by positive wealth (no tail) | +0.84 (+0.34 to +1.45) [+0.00 (+0.00 to +0.00)] | +0.84 (+0.34 to +1.45) [+0.12 (+0.00 to +0.36)] | +0.82 (+0.34 to +1.40) [+0.00 (+0.00 to +0.00)] | +0.82 (+0.34 to +1.40) [+0.00 (+0.00 to +0.00)] | +0.39 (+0.08 to +0.79) [-0.08 (-0.24 to +0.00)] | +0.82 (+0.34 to +1.40) [+0.00 (+0.00 to +0.00)] |
| owners keep the private premium, shared by shares and business equity (no tail) | +0.84 (+0.34 to +1.45) [+0.00 (+0.00 to +0.00)] | +0.84 (+0.34 to +1.45) [+0.12 (+0.00 to +0.36)] | +0.82 (+0.34 to +1.40) [+0.00 (+0.00 to +0.00)] | +0.82 (+0.34 to +1.40) [+0.00 (+0.00 to +0.00)] | +0.47 (+0.13 to +0.91) [+0.00 (+0.00 to +0.00)] | +0.82 (+0.34 to +1.40) [+0.00 (+0.00 to +0.00)] |

**wealth poverty (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| r2: lower prices (release reading) | -12.50 (-12.80 to -12.21) | -18.05 (-18.35 to -17.76) | -12.91 (-13.24 to -12.60) | -20.05 (-20.41 to -19.71) | -6.94 (-7.21 to -6.66) | -18.54 (-18.90 to -18.18) |
| owners keep the private premium, shared by positive wealth (no tail) | -9.72 (-10.03 to -9.43) [+2.78 (+2.62 to +2.96)] | -13.67 (-13.97 to -13.37) [+4.38 (+4.21 to +4.56)] | -9.56 (-9.85 to -9.27) [+3.35 (+3.15 to +3.56)] | -14.27 (-14.61 to -13.95) [+5.78 (+5.56 to +6.02)] | -5.40 (-5.65 to -5.15) [+1.54 (+1.40 to +1.69)] | -12.56 (-12.89 to -12.23) [+5.98 (+5.77 to +6.19)] |
| owners keep the private premium, shared by shares and business equity (no tail) | -9.65 (-9.95 to -9.35) [+2.85 (+2.70 to +3.02)] | -13.59 (-13.90 to -13.29) [+4.46 (+4.27 to +4.64)] | -9.45 (-9.74 to -9.15) [+3.46 (+3.28 to +3.66)] | -14.10 (-14.43 to -13.78) [+5.96 (+5.73 to +6.19)] | -5.34 (-5.58 to -5.08) [+1.60 (+1.47 to +1.74)] | -12.35 (-12.69 to -12.02) [+6.18 (+5.96 to +6.41)] |

**top 1% share of disposable income (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| r2: lower prices (release reading) | -0.08 (-0.13 to -0.02) | -1.00 (-1.07 to -0.92) | -0.09 (-0.18 to +0.00) | -1.53 (-1.65 to -1.40) | +0.01 (-0.05 to +0.07) | -0.88 (-0.98 to -0.78) |
| owners keep the private premium, shared by positive wealth (no tail) | +1.13 (+1.07 to +1.20) [+1.21 (+1.12 to +1.30)] | +1.75 (+1.65 to +1.85) [+2.75 (+2.60 to +2.89)] | +1.63 (+1.54 to +1.71) [+1.72 (+1.60 to +1.83)] | +2.13 (+2.02 to +2.23) [+3.65 (+3.47 to +3.83)] | +0.72 (+0.68 to +0.77) [+0.71 (+0.66 to +0.77)] | +2.75 (+2.62 to +2.87) [+3.63 (+3.45 to +3.80)] |
| owners keep the private premium, shared by shares and business equity (no tail) | +2.04 (+1.93 to +2.15) [+2.12 (+1.99 to +2.25)] | +3.31 (+3.13 to +3.47) [+4.30 (+4.09 to +4.52)] | +2.85 (+2.71 to +2.98) [+2.94 (+2.77 to +3.09)] | +4.04 (+3.84 to +4.22) [+5.57 (+5.30 to +5.82)] | +1.27 (+1.20 to +1.33) [+1.25 (+1.17 to +1.34)] | +4.73 (+4.51 to +4.93) [+5.61 (+5.35 to +5.86)] |

**basket poverty (points of adult-years)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| r2: lower prices (release reading) | -16.03 (-16.34 to -15.73) | -23.51 (-23.80 to -23.20) | -21.43 (-21.81 to -21.04) | -33.27 (-33.70 to -32.83) | -8.28 (-8.55 to -8.00) | -32.61 (-33.03 to -32.18) |
| owners keep the private premium, shared by positive wealth (no tail) | -12.37 (-12.65 to -12.10) [+3.66 (+3.50 to +3.82)] | -19.79 (-20.09 to -19.49) [+3.72 (+3.58 to +3.86)] | -16.72 (-17.06 to -16.39) [+4.71 (+4.52 to +4.89)] | -27.29 (-27.69 to -26.88) [+5.99 (+5.80 to +6.17)] | -6.59 (-6.80 to -6.36) [+1.69 (+1.57 to +1.83)] | -24.62 (-25.00 to -24.23) [+7.99 (+7.80 to +8.19)] |
| owners keep the private premium, shared by shares and business equity (no tail) | -11.69 (-11.96 to -11.41) [+4.34 (+4.18 to +4.51)] | -19.28 (-19.58 to -18.98) [+4.24 (+4.07 to +4.40)] | -15.56 (-15.88 to -15.23) [+5.87 (+5.69 to +6.07)] | -26.33 (-26.73 to -25.93) [+6.94 (+6.73 to +7.14)] | -5.90 (-6.11 to -5.69) [+2.38 (+2.25 to +2.52)] | -23.29 (-23.65 to -22.92) [+9.32 (+9.11 to +9.54)] |

## 17. Part 1's rows again with the corrected wealth-group edges, beside the Nov 10 pilot (the programme's effect on wealth poverty, points)

| Row | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| all wealth is cash, Nov 10 | +21.51 (+20.96 to +22.05) | +0.66 (+0.19 to +1.11) | +45.03 (+44.43 to +45.60) | +30.16 (+29.43 to +30.85) | +24.81 (+24.12 to +25.50) | +41.65 (+40.93 to +42.33) |
| all wealth is cash, this pilot | +21.51 (+20.97 to +22.05) | +0.66 (+0.19 to +1.10) | +45.03 (+44.44 to +45.60) | +30.16 (+29.45 to +30.81) | +24.81 (+24.15 to +25.46) | +41.65 (+40.95 to +42.32) |
| main reading, Nov 10 (edges 9.4% too high) | -12.66 (-12.96 to -12.36) | -18.18 (-18.51 to -17.86) | -13.15 (-13.47 to -12.85) | -20.24 (-20.61 to -19.89) | -7.09 (-7.36 to -6.82) | -18.71 (-19.08 to -18.36) |
| main reading, corrected edges | -12.63 (-12.93 to -12.35) | -18.18 (-18.49 to -17.89) | -13.22 (-13.53 to -12.92) | -20.34 (-20.71 to -20.00) | -7.13 (-7.40 to -6.85) | -18.82 (-19.18 to -18.48) |
| fixed-rate debt reprices, Nov 10 | -6.68 (-6.98 to -6.38) | -13.32 (-13.68 to -12.97) | -7.80 (-8.14 to -7.48) | -15.71 (-16.09 to -15.34) | -2.78 (-3.05 to -2.53) | -13.39 (-13.74 to -13.03) |
| fixed-rate debt reprices, corrected edges | -6.68 (-6.98 to -6.40) | -13.33 (-13.68 to -12.99) | -7.82 (-8.14 to -7.49) | -15.72 (-16.10 to -15.36) | -2.80 (-3.05 to -2.54) | -13.40 (-13.75 to -13.06) |

