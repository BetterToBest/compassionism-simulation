# S74 forward sweep tables (20 seeds, frozen round-2 main row)

Made by `node dev/tools/s74_sweep_table.js` from the sweep files in this folder (`node dev/tools/s74_sweep.js ENV 20`). Descriptive only: each cell is the mean over seeds 1-20 with the 10th to 90th percentile across seeds in brackets. E is the programme's effect (programme minus no programme, paired on seeds) in each setting; C is the setting's effect against no central bank, paired on seeds; X is the interaction on P1 (E in the setting minus E with no central bank). P1 spread of the basket price level's yearly change (points); P2 spread of yearly changes in real cash income ($, mean); P3 largest fall in real wealth ($, median); P4 years to recover from an income shock; P5 % pushed below the basket line in a recession year; basket poverty (`fgt0PY`, % of adult-years); wealth poverty (`pov`, % in the last year).

## History (2005-2025)

Engine: 1db387848de63846e80e1211eb6979be0abba295 (dirty); command `node dev/tools/s74_sweep.js hx 20 --only=off,main,fd0.034,fd0.062 --out=dev/runs/s74-fd`; 20 seeds; 4 settings.

### C2.2

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 3.80 [3.76, 3.83] | 1.43 [0.00, 4.76] | 0.34 [0.00, 0.87] | 1.15 [1.14, 1.15] | 0.00 [0.00, 0.00] | 22.19 / 0.74 |
| sale discount 0.034 | 3.80 [3.76, 3.83] | 1.43 [0.00, 4.76] | 0.34 [0.00, 0.86] | 1.15 [1.14, 1.15] | 0.00 [0.00, 0.00] | 22.08 / 0.74 |
| sale discount 0.062 | 3.80 [3.76, 3.83] | 1.43 [0.00, 4.76] | 0.34 [0.00, 0.84] | 1.15 [1.14, 1.15] | 0.00 [0.00, 0.00] | 21.95 / 0.73 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.09 [0.06, 0.12] | 13383 [12671, 13944] | -43605 [-48335, -38055] | -0.36 [-0.55, -0.15] | -7.61 [-9.24, -6.22] | -42.63 [-44.74, -39.87] | -25.15 [-27.46, -22.98] | 0.00 [0.00, 0.00] |
| main rule | 0.09 [0.07, 0.11] | 13276 [12488, 13824] | -46995 [-52248, -43047] | -0.33 [-0.48, -0.19] | -7.87 [-9.64, -6.32] | -43.09 [-45.22, -40.34] | -28.54 [-30.04, -26.58] | 0.00 [-0.02, 0.01] |
| sale discount 0.034 | 0.09 [0.07, 0.11] | 13276 [12487, 13825] | -47075 [-52248, -43150] | -0.33 [-0.47, -0.19] | -7.87 [-9.64, -6.32] | -43.09 [-45.22, -40.34] | -28.73 [-30.40, -26.96] | 0.00 [-0.01, 0.01] |
| sale discount 0.062 | 0.09 [0.07, 0.11] | 13277 [12487, 13826] | -47152 [-52248, -43240] | -0.33 [-0.46, -0.19] | -7.87 [-9.64, -6.32] | -43.09 [-45.22, -40.34] | -28.93 [-30.44, -27.00] | 0.00 [-0.01, 0.01] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | 0.48 [0.34, 0.58] | 0.02 [-0.01, 0.04] | 3.47 [2.18, 4.82] | 0.08 [0.00, 0.20] |
| sale discount 0.034 | 0.48 [0.34, 0.60] | 0.02 [-0.01, 0.04] | 3.66 [2.18, 5.02] | 0.08 [0.00, 0.20] |
| sale discount 0.062 | 0.48 [0.34, 0.60] | 0.02 [-0.01, 0.04] | 3.87 [2.58, 5.24] | 0.09 [0.00, 0.20] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.09 | 0.09 (main rule) | 0.09 (sale discount 0.062) | 3 of 3 |
| E P2 | 13276 | 13276 (main rule) | 13277 (sale discount 0.062) | 3 of 3 |
| E P3 | -46995 | -47152 (sale discount 0.062) | -46995 (main rule) | 3 of 3 |
| E P4 | -0.33 | -0.33 (main rule) | -0.33 (sale discount 0.062) | 3 of 3 |
| E P5 | -7.87 | -7.87 (sale discount 0.034) | -7.87 (main rule) | 3 of 3 |
| E basket pov. | -43.09 | -43.09 (sale discount 0.034) | -43.09 (main rule) | 3 of 3 |
| E wealth pov. | -28.54 | -28.93 (sale discount 0.062) | -28.54 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.062) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 2005 | 5.40 (5.40 to 5.40) | 5.40 (5.40 to 5.40) | - | 40.20 (38.20 to 43.28) | 20.30 (18.26 to 22.62) |
| 2006 | 5.40 (5.40 to 5.40) | 5.40 (5.40 to 5.40) | 4.67 (4.38 to 4.94) | 42.20 (38.94 to 45.62) | 7.40 (6.00 to 9.66) |
| 2007 | 4.40 (4.40 to 4.40) | 7.61 (7.18 to 8.03) | 5.14 (4.96 to 5.39) | 42.60 (39.10 to 47.52) | 2.80 (2.18 to 3.62) |
| 2008 | 6.73 (6.73 to 6.73) | 8.28 (8.00 to 8.65) | 0.33 (0.18 to 0.55) | 43.70 (39.36 to 49.00) | 7.80 (5.94 to 9.22) |
| 2009 | 0.00 (0.00 to 0.00) | 0.14 (0.00 to 0.47) | 2.70 (2.64 to 2.83) | 44.70 (41.54 to 50.44) | 3.50 (2.78 to 4.66) |
| 2010 | 1.86 (1.86 to 1.86) | 1.69 (1.60 to 1.89) | 1.54 (1.51 to 1.76) | 46.80 (42.66 to 51.26) | 6.00 (4.38 to 7.80) |
| 2011 | 0.46 (0.46 to 0.46) | 0.61 (0.57 to 0.94) | 3.00 (2.96 to 3.06) | 47.80 (43.68 to 52.42) | 3.60 (2.78 to 4.42) |
| 2012 | 2.94 (2.94 to 2.94) | 2.85 (2.79 to 2.94) | 1.81 (1.78 to 1.85) | 48.20 (45.56 to 52.84) | 3.70 (3.00 to 4.42) |
| 2013 | 1.29 (1.29 to 1.29) | 1.37 (1.32 to 1.43) | 1.51 (1.49 to 1.54) | 47.50 (41.58 to 50.12) | 2.60 (1.78 to 3.42) |
| 2014 | 1.08 (1.08 to 1.08) | 1.08 (1.04 to 1.11) | 0.68 (0.67 to 0.70) | 46.00 (42.20 to 50.66) | 2.20 (1.58 to 3.04) |
| 2015 | 0.09 (0.09 to 0.09) | 0.13 (0.12 to 0.17) | 0.65 (0.64 to 0.67) | 46.30 (41.28 to 48.22) | 1.80 (1.20 to 2.60) |
| 2016 | 0.52 (0.52 to 0.52) | 0.53 (0.51 to 0.56) | 2.06 (2.05 to 2.07) | 45.40 (41.76 to 48.18) | 1.80 (1.38 to 2.42) |
| 2017 | 2.52 (2.52 to 2.52) | 2.53 (2.51 to 2.55) | 2.13 (2.09 to 2.15) | 45.80 (42.16 to 48.00) | 1.60 (1.00 to 2.20) |
| 2018 | 2.85 (2.85 to 2.85) | 2.85 (2.79 to 2.88) | 2.00 (1.88 to 2.02) | 45.60 (42.84 to 49.28) | 1.40 (0.98 to 2.02) |
| 2019 | 3.11 (3.11 to 3.11) | 3.10 (2.94 to 3.15) | 2.34 (2.32 to 2.45) | 45.20 (43.20 to 49.28) | 1.30 (0.80 to 2.00) |
| 2020 | 3.82 (3.82 to 3.82) | 3.85 (3.82 to 4.02) | 1.32 (1.32 to 1.39) | 47.70 (44.62 to 50.22) | 1.20 (0.78 to 1.80) |
| 2021 | 0.31 (0.31 to 0.31) | 0.32 (0.31 to 0.41) | 7.18 (7.14 to 7.19) | 49.40 (46.52 to 51.62) | 1.20 (0.80 to 1.80) |
| 2022 | 11.14 (11.14 to 11.14) | 11.15 (11.09 to 11.16) | 6.41 (6.39 to 6.44) | 51.10 (48.34 to 54.02) | 1.20 (0.98 to 1.82) |
| 2023 | 10.03 (10.03 to 10.03) | 10.04 (10.02 to 10.09) | 3.31 (3.31 to 3.32) | 51.80 (49.16 to 54.64) | 1.00 (0.60 to 1.60) |
| 2024 | 5.55 (5.55 to 5.55) | 5.54 (5.53 to 5.56) | 2.88 (2.86 to 2.88) | 51.10 (48.72 to 52.74) | 1.00 (0.40 to 1.42) |
| 2025 | 5.02 (5.02 to 5.02) | 5.03 (5.01 to 5.03) | 2.66 (2.65 to 2.66) | 51.80 (48.36 to 54.22) | 1.00 (0.40 to 1.42) |

### release design

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 3.73 [3.70, 3.76] | 4.52 [0.00, 9.52] | 1.05 [0.00, 2.27] | 1.14 [1.13, 1.14] | 0.00 [0.00, 0.00] | 22.19 / 8.02 |
| sale discount 0.034 | 3.73 [3.70, 3.76] | 4.52 [0.00, 9.52] | 1.05 [0.00, 2.29] | 1.14 [1.13, 1.14] | 0.00 [0.00, 0.00] | 22.08 / 7.96 |
| sale discount 0.062 | 3.73 [3.70, 3.76] | 4.52 [0.00, 9.52] | 1.05 [0.00, 2.31] | 1.14 [1.13, 1.14] | 0.00 [0.00, 0.00] | 21.95 / 7.91 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.12 [0.09, 0.14] | 2790 [2340, 3247] | -21668 [-25345, -16337] | 0.49 [0.32, 0.64] | -3.50 [-4.56, -2.18] | -25.45 [-28.00, -22.19] | -14.78 [-17.68, -12.82] | 0.00 [0.00, 0.00] |
| main rule | 0.12 [0.09, 0.15] | 2744 [2342, 3216] | -19441 [-23909, -15835] | 0.45 [0.31, 0.59] | -3.66 [-4.96, -2.15] | -25.67 [-28.37, -22.40] | -16.74 [-18.84, -13.74] | 0.00 [-0.01, 0.02] |
| sale discount 0.034 | 0.12 [0.09, 0.15] | 2746 [2341, 3216] | -19442 [-23951, -15834] | 0.45 [0.34, 0.61] | -3.66 [-4.96, -2.15] | -25.67 [-28.37, -22.40] | -16.85 [-18.84, -13.78] | 0.00 [-0.01, 0.02] |
| sale discount 0.062 | 0.12 [0.09, 0.15] | 2746 [2341, 3216] | -19462 [-24046, -15831] | 0.46 [0.32, 0.61] | -3.66 [-4.96, -2.15] | -25.67 [-28.37, -22.40] | -16.97 [-18.86, -13.90] | 0.00 [-0.01, 0.02] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | 0.48 [0.34, 0.58] | 0.25 [0.14, 0.34] | 3.47 [2.18, 4.82] | 1.51 [0.78, 2.60] |
| sale discount 0.034 | 0.48 [0.34, 0.60] | 0.25 [0.14, 0.34] | 3.66 [2.18, 5.02] | 1.59 [0.78, 2.62] |
| sale discount 0.062 | 0.48 [0.34, 0.60] | 0.25 [0.14, 0.33] | 3.87 [2.58, 5.24] | 1.68 [0.98, 2.62] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.12 | 0.12 (main rule) | 0.12 (sale discount 0.062) | 3 of 3 |
| E P2 | 2744 | 2744 (main rule) | 2746 (sale discount 0.062) | 3 of 3 |
| E P3 | -19441 | -19462 (sale discount 0.062) | -19441 (main rule) | 3 of 3 |
| E P4 | 0.45 | 0.45 (main rule) | 0.46 (sale discount 0.062) | 3 of 3 |
| E P5 | -3.66 | -3.66 (sale discount 0.034) | -3.66 (main rule) | 3 of 3 |
| E basket pov. | -25.67 | -25.67 (sale discount 0.062) | -25.67 (main rule) | 3 of 3 |
| E wealth pov. | -16.74 | -16.97 (sale discount 0.062) | -16.74 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.062) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 2005 | 5.40 (5.40 to 5.40) | 5.40 (5.40 to 5.40) | - | 40.20 (38.20 to 43.28) | 29.40 (26.74 to 31.08) |
| 2006 | 5.40 (5.40 to 5.40) | 5.40 (5.40 to 5.40) | 3.81 (3.59 to 3.97) | 42.20 (38.94 to 45.62) | 17.50 (16.20 to 19.70) |
| 2007 | 4.40 (4.40 to 4.40) | 6.33 (6.00 to 6.56) | 5.26 (5.04 to 5.52) | 42.60 (39.10 to 47.52) | 16.30 (15.00 to 18.82) |
| 2008 | 6.73 (6.73 to 6.73) | 8.45 (8.12 to 8.84) | 0.23 (0.10 to 0.40) | 43.70 (39.36 to 49.00) | 18.60 (17.00 to 22.46) |
| 2009 | 0.00 (0.00 to 0.00) | 0.01 (0.00 to 0.25) | 2.73 (2.55 to 2.84) | 44.70 (41.54 to 50.44) | 17.50 (15.54 to 19.62) |
| 2010 | 1.86 (1.86 to 1.86) | 1.73 (1.47 to 1.89) | 1.45 (1.27 to 1.64) | 46.80 (42.66 to 51.26) | 21.50 (18.68 to 22.62) |
| 2011 | 0.46 (0.46 to 0.46) | 0.47 (0.20 to 0.76) | 2.90 (2.80 to 3.10) | 47.80 (43.68 to 52.42) | 19.80 (18.38 to 22.26) |
| 2012 | 2.94 (2.94 to 2.94) | 2.69 (2.55 to 2.99) | 1.79 (1.64 to 1.94) | 48.20 (45.56 to 52.84) | 22.70 (20.58 to 26.08) |
| 2013 | 1.29 (1.29 to 1.29) | 1.34 (1.11 to 1.56) | 1.33 (1.25 to 1.45) | 47.50 (41.58 to 50.12) | 22.50 (19.80 to 24.40) |
| 2014 | 1.08 (1.08 to 1.08) | 0.80 (0.68 to 0.98) | 0.64 (0.56 to 0.82) | 46.00 (42.20 to 50.66) | 22.50 (20.28 to 24.48) |
| 2015 | 0.09 (0.09 to 0.09) | 0.07 (0.00 to 0.34) | 0.64 (0.43 to 0.78) | 46.30 (41.28 to 48.22) | 21.30 (18.58 to 23.22) |
| 2016 | 0.52 (0.52 to 0.52) | 0.51 (0.21 to 0.73) | 2.17 (2.05 to 2.25) | 45.40 (41.76 to 48.18) | 21.80 (18.76 to 23.22) |
| 2017 | 2.52 (2.52 to 2.52) | 2.70 (2.52 to 2.82) | 2.11 (2.02 to 2.35) | 45.80 (42.16 to 48.00) | 21.80 (18.96 to 23.72) |
| 2018 | 2.85 (2.85 to 2.85) | 2.83 (2.68 to 3.18) | 1.97 (1.85 to 2.06) | 45.60 (42.84 to 49.28) | 23.20 (20.92 to 25.30) |
| 2019 | 3.11 (3.11 to 3.11) | 3.06 (2.89 to 3.20) | 2.26 (2.16 to 2.43) | 45.20 (43.20 to 49.28) | 23.70 (21.92 to 26.66) |
| 2020 | 3.82 (3.82 to 3.82) | 3.72 (3.59 to 3.99) | 1.24 (1.17 to 1.35) | 47.70 (44.62 to 50.22) | 24.30 (23.24 to 27.60) |
| 2021 | 0.31 (0.31 to 0.31) | 0.19 (0.08 to 0.35) | 7.13 (6.99 to 7.27) | 49.40 (46.52 to 51.62) | 22.20 (19.04 to 23.86) |
| 2022 | 11.14 (11.14 to 11.14) | 11.08 (10.86 to 11.28) | 6.75 (6.56 to 6.89) | 51.10 (48.34 to 54.02) | 18.70 (15.74 to 19.68) |
| 2023 | 10.03 (10.03 to 10.03) | 10.56 (10.27 to 10.77) | 3.49 (3.42 to 3.62) | 51.80 (49.16 to 54.64) | 16.70 (14.72 to 18.22) |
| 2024 | 5.55 (5.55 to 5.55) | 5.81 (5.70 to 6.00) | 2.86 (2.82 to 2.93) | 51.10 (48.72 to 52.74) | 19.50 (17.00 to 21.46) |
| 2025 | 5.02 (5.02 to 5.02) | 5.01 (4.94 to 5.12) | 2.51 (2.45 to 2.62) | 51.80 (48.36 to 54.22) | 20.30 (17.40 to 22.08) |

## Adverse

Engine: 1db387848de63846e80e1211eb6979be0abba295 (dirty); command `node dev/tools/s74_sweep.js adv 20 --only=off,main,fd0.034,fd0.062 --out=dev/runs/s74-fd`; 20 seeds; 4 settings.

### C2.2

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.20 [24.18, 26.54] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.29 / 0.79 |
| sale discount 0.034 | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.20 [24.21, 26.50] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.23 / 0.78 |
| sale discount 0.062 | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.19 [24.25, 26.54] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.16 / 0.78 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.54 [0.46, 0.60] | 13624 [12681, 14128] | -250.82 [-919.00, -0.00] | -0.14 [-0.38, 0.08] | -11.31 [-13.70, -7.97] | -42.08 [-43.88, -38.77] | -25.98 [-28.04, -23.94] | 0.00 [0.00, 0.00] |
| main rule | 0.54 [0.46, 0.60] | 13554 [12577, 14085] | -53048 [-67579, -18815] | -0.20 [-0.42, -0.02] | -11.06 [-13.64, -7.69] | -41.88 [-43.79, -38.76] | -26.56 [-28.60, -23.98] | 0.00 [-0.00, 0.01] |
| sale discount 0.034 | 0.54 [0.46, 0.59] | 13554 [12578, 14086] | -53149 [-67982, -18766] | -0.20 [-0.41, -0.02] | -11.06 [-13.64, -7.69] | -41.88 [-43.79, -38.76] | -26.71 [-28.60, -24.00] | 0.00 [-0.00, 0.01] |
| sale discount 0.062 | 0.54 [0.46, 0.59] | 13554 [12578, 14086] | -53304 [-68331, -19057] | -0.19 [-0.41, -0.01] | -11.05 [-13.62, -7.69] | -41.88 [-43.79, -38.76] | -26.82 [-28.80, -24.00] | 0.00 [-0.00, 0.01] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | -0.20 [-0.36, -0.07] | -0.00 [-0.03, 0.01] | 0.58 [-0.44, 1.62] | -0.00 [0.00, 0.00] |
| sale discount 0.034 | -0.20 [-0.36, -0.07] | -0.00 [-0.03, 0.01] | 0.73 [-0.08, 1.80] | -0.00 [0.00, 0.00] |
| sale discount 0.062 | -0.20 [-0.36, -0.07] | -0.00 [-0.03, 0.01] | 0.85 [-0.08, 1.80] | 0.01 [0.00, 0.02] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.54 | 0.54 (sale discount 0.062) | 0.54 (sale discount 0.034) | 3 of 3 |
| E P2 | 13554 | 13554 (main rule) | 13554 (sale discount 0.062) | 3 of 3 |
| E P3 | -53048 | -53304 (sale discount 0.062) | -53048 (main rule) | 3 of 3 |
| E P4 | -0.20 | -0.20 (main rule) | -0.19 (sale discount 0.062) | 3 of 3 |
| E P5 | -11.06 | -11.06 (main rule) | -11.05 (sale discount 0.062) | 3 of 3 |
| E basket pov. | -41.88 | -41.88 (sale discount 0.062) | -41.88 (main rule) | 3 of 3 |
| E wealth pov. | -26.56 | -26.82 (sale discount 0.062) | -26.56 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (sale discount 0.062) | 0.00 (sale discount 0.034) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | - | 40.20 (38.20 to 43.28) | 20.30 (18.26 to 22.62) |
| 1 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | 4.13 (3.84 to 4.41) | 42.00 (38.58 to 45.18) | 7.30 (5.98 to 9.82) |
| 2 | 2.97 (2.67 to 2.97) | 6.06 (5.24 to 6.43) | 3.02 (2.83 to 3.31) | 41.70 (38.52 to 46.74) | 2.80 (2.14 to 3.62) |
| 3 | 2.97 (0.00 to 2.97) | 4.38 (0.00 to 4.76) | 2.32 (2.17 to 2.43) | 42.60 (38.98 to 50.72) | 7.60 (5.76 to 8.48) |
| 4 | 2.97 (0.00 to 2.97) | 3.39 (0.00 to 3.61) | 1.84 (1.78 to 1.94) | 42.60 (38.44 to 46.52) | 3.20 (2.76 to 4.66) |
| 5 | 2.97 (0.00 to 2.97) | 2.70 (0.00 to 2.83) | 2.11 (1.97 to 2.26) | 43.90 (38.60 to 47.38) | 5.00 (3.80 to 7.00) |
| 6 | 2.97 (0.00 to 2.97) | 3.13 (0.00 to 3.37) | 1.97 (1.88 to 2.24) | 44.70 (40.00 to 47.38) | 3.20 (2.38 to 4.20) |
| 7 | 2.97 (0.00 to 2.97) | 2.89 (0.00 to 3.15) | 2.02 (1.94 to 2.09) | 43.90 (39.96 to 48.26) | 3.40 (2.78 to 4.22) |
| 8 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 3.09) | 1.99 (1.93 to 2.16) | 43.40 (38.96 to 46.16) | 2.60 (1.80 to 3.20) |
| 9 | 2.97 (2.97 to 2.97) | 2.96 (2.81 to 3.22) | 2.03 (1.91 to 2.18) | 43.70 (39.88 to 49.84) | 2.20 (1.60 to 3.02) |
| 10 | 2.97 (0.00 to 2.97) | 3.00 (0.00 to 3.25) | 2.02 (2.00 to 2.20) | 45.50 (40.34 to 51.06) | 1.90 (1.38 to 2.80) |
| 11 | 2.97 (0.00 to 2.97) | 2.99 (0.00 to 3.19) | 2.01 (2.00 to 2.13) | 46.40 (42.84 to 51.68) | 2.00 (1.20 to 2.60) |
| 12 | 2.97 (0.00 to 2.97) | 2.98 (0.00 to 2.99) | 2.00 (1.98 to 2.05) | 46.80 (43.52 to 50.50) | 1.50 (1.20 to 2.20) |
| 13 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.05) | 47.20 (43.88 to 53.62) | 1.40 (0.98 to 2.04) |
| 14 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 3.02) | 2.01 (1.97 to 2.03) | 47.10 (44.40 to 53.68) | 1.20 (0.80 to 2.02) |
| 15 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.03) | 48.80 (43.96 to 52.08) | 1.20 (0.78 to 1.80) |
| 16 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 3.01) | 2.00 (1.99 to 2.01) | 48.80 (43.96 to 53.58) | 1.00 (0.80 to 1.82) |
| 17 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.02) | 48.10 (46.14 to 53.02) | 1.00 (0.60 to 1.42) |
| 18 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.98) | 2.00 (2.00 to 2.01) | 48.50 (46.16 to 52.40) | 0.80 (0.78 to 1.60) |
| 19 | 2.97 (2.97 to 2.97) | 2.97 (2.96 to 2.98) | 2.00 (2.00 to 2.01) | 48.40 (46.76 to 51.28) | 0.90 (0.40 to 1.26) |

### release design

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 2.59 [2.35, 2.84] | 16.00 [10.00, 25.00] | 26.60 [25.93, 29.75] | -0.39 [-0.63, -0.23] | 0.00 [0.00, 0.00] | 22.29 / 9.91 |
| sale discount 0.034 | 2.59 [2.35, 2.84] | 16.00 [10.00, 25.00] | 26.60 [25.76, 29.76] | -0.39 [-0.63, -0.23] | 0.00 [0.00, 0.00] | 22.23 / 9.87 |
| sale discount 0.062 | 2.59 [2.35, 2.84] | 16.00 [10.00, 25.00] | 26.62 [25.93, 29.77] | -0.39 [-0.63, -0.23] | 0.00 [0.00, 0.00] | 22.16 / 9.83 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.42 [0.37, 0.48] | 2302 [1967, 2777] | -250.82 [-919.00, -0.00] | 0.32 [0.14, 0.56] | -5.57 [-7.87, -3.51] | -20.55 [-22.55, -17.77] | -10.59 [-12.68, -8.98] | 0.00 [0.00, 0.00] |
| main rule | 0.43 [0.37, 0.48] | 2268 [1917, 2731] | -9305 [-16172, -982.21] | 0.29 [0.13, 0.49] | -5.45 [-7.80, -3.31] | -20.48 [-22.48, -17.52] | -11.11 [-13.22, -9.18] | 0.00 [-0.00, 0.01] |
| sale discount 0.034 | 0.43 [0.37, 0.48] | 2268 [1920, 2732] | -9382 [-15685, -1001] | 0.29 [0.11, 0.49] | -5.44 [-7.80, -3.31] | -20.49 [-22.48, -17.53] | -11.18 [-13.62, -9.14] | 0.00 [-0.00, 0.01] |
| sale discount 0.062 | 0.43 [0.37, 0.48] | 2268 [1919, 2733] | -9508 [-16139, -1017] | 0.29 [0.10, 0.52] | -5.43 [-7.65, -3.31] | -20.49 [-22.48, -17.53] | -11.25 [-13.66, -9.18] | 0.00 [-0.00, 0.01] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | -0.20 [-0.36, -0.07] | -0.13 [-0.27, -0.04] | 0.58 [-0.44, 1.62] | 0.06 [-0.66, 0.80] |
| sale discount 0.034 | -0.20 [-0.36, -0.07] | -0.14 [-0.27, -0.04] | 0.73 [-0.08, 1.80] | 0.14 [-0.62, 0.80] |
| sale discount 0.062 | -0.20 [-0.36, -0.07] | -0.13 [-0.27, -0.04] | 0.85 [-0.08, 1.80] | 0.19 [-0.60, 0.80] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.43 | 0.43 (main rule) | 0.43 (sale discount 0.062) | 3 of 3 |
| E P2 | 2268 | 2268 (main rule) | 2268 (sale discount 0.062) | 3 of 3 |
| E P3 | -9305 | -9508 (sale discount 0.062) | -9305 (main rule) | 3 of 3 |
| E P4 | 0.29 | 0.29 (main rule) | 0.29 (sale discount 0.062) | 3 of 3 |
| E P5 | -5.45 | -5.45 (main rule) | -5.43 (sale discount 0.062) | 3 of 3 |
| E basket pov. | -20.48 | -20.49 (sale discount 0.062) | -20.48 (main rule) | 3 of 3 |
| E wealth pov. | -11.11 | -11.25 (sale discount 0.062) | -11.11 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.062) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | - | 40.20 (38.20 to 43.28) | 29.40 (26.74 to 31.08) |
| 1 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | 3.28 (3.06 to 3.43) | 42.00 (38.58 to 45.18) | 17.60 (16.18 to 19.38) |
| 2 | 2.97 (2.67 to 2.97) | 4.78 (4.00 to 5.04) | 3.12 (2.92 to 3.41) | 41.70 (38.52 to 46.74) | 16.40 (15.36 to 19.66) |
| 3 | 2.97 (0.00 to 2.97) | 4.60 (0.18 to 5.01) | 2.13 (1.97 to 2.32) | 42.60 (38.98 to 50.72) | 21.10 (18.10 to 23.92) |
| 4 | 2.97 (0.00 to 2.97) | 3.12 (0.00 to 3.38) | 1.75 (1.64 to 1.87) | 42.60 (38.44 to 46.52) | 19.40 (16.72 to 22.06) |
| 5 | 2.97 (0.00 to 2.97) | 2.56 (0.00 to 2.78) | 2.01 (1.90 to 2.17) | 43.90 (38.60 to 47.38) | 22.70 (19.14 to 24.22) |
| 6 | 2.97 (0.00 to 2.97) | 2.92 (0.00 to 3.20) | 1.92 (1.77 to 2.15) | 44.70 (40.00 to 47.38) | 21.20 (18.18 to 22.92) |
| 7 | 2.97 (0.00 to 2.97) | 2.81 (0.00 to 3.07) | 2.06 (1.91 to 2.16) | 43.90 (39.96 to 48.26) | 23.50 (21.54 to 24.84) |
| 8 | 2.97 (0.00 to 2.97) | 3.00 (0.00 to 3.20) | 1.84 (1.75 to 2.05) | 43.40 (38.96 to 46.16) | 23.40 (20.30 to 25.24) |
| 9 | 2.97 (2.97 to 2.97) | 2.70 (2.43 to 2.93) | 1.96 (1.87 to 2.13) | 43.70 (39.88 to 49.84) | 23.90 (21.94 to 26.74) |
| 10 | 2.97 (0.00 to 2.97) | 2.88 (0.00 to 3.17) | 1.94 (1.76 to 2.10) | 45.50 (40.34 to 51.06) | 25.20 (23.00 to 26.84) |
| 11 | 2.97 (0.00 to 2.97) | 2.79 (0.00 to 3.12) | 1.99 (1.90 to 2.14) | 46.40 (42.84 to 51.68) | 25.80 (23.92 to 28.44) |
| 12 | 2.97 (0.00 to 2.97) | 2.88 (0.00 to 3.06) | 1.99 (1.77 to 2.12) | 46.80 (43.52 to 50.50) | 25.90 (24.56 to 28.20) |
| 13 | 2.97 (0.00 to 2.97) | 2.86 (0.00 to 3.09) | 1.98 (1.81 to 2.19) | 47.20 (43.88 to 53.62) | 26.70 (24.18 to 29.64) |
| 14 | 2.97 (0.00 to 2.97) | 2.77 (0.00 to 3.11) | 1.93 (1.79 to 2.09) | 47.10 (44.40 to 53.68) | 28.10 (25.56 to 30.46) |
| 15 | 2.97 (0.00 to 2.97) | 2.75 (0.00 to 3.06) | 1.90 (1.75 to 2.07) | 48.80 (43.96 to 52.08) | 28.40 (26.78 to 31.08) |
| 16 | 2.97 (0.00 to 2.97) | 2.82 (0.00 to 3.07) | 1.92 (1.78 to 2.16) | 48.80 (43.96 to 53.58) | 28.90 (27.20 to 32.06) |
| 17 | 2.97 (0.00 to 2.97) | 2.80 (0.00 to 3.16) | 1.92 (1.80 to 2.12) | 48.10 (46.14 to 53.02) | 30.70 (26.78 to 33.26) |
| 18 | 2.97 (0.00 to 2.97) | 2.83 (0.00 to 3.14) | 1.89 (1.77 to 2.12) | 48.50 (46.16 to 52.40) | 29.90 (28.38 to 32.96) |
| 19 | 2.97 (2.97 to 2.97) | 2.81 (2.61 to 3.15) | 1.94 (1.83 to 2.07) | 48.40 (46.76 to 51.28) | 31.20 (28.58 to 33.24) |

## Stress

Engine: 1db387848de63846e80e1211eb6979be0abba295 (dirty); command `node dev/tools/s74_sweep.js st 20 --only=off,main,fd0.034,fd0.062 --out=dev/runs/s74-fd`; 20 seeds; 4 settings.

### C2.2

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.26 [24.33, 26.72] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.29 / 0.92 |
| sale discount 0.034 | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.26 [24.36, 26.66] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.23 / 0.91 |
| sale discount 0.062 | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.26 [24.38, 26.69] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.16 / 0.91 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.53 [0.46, 0.59] | 9265 [8608, 10234] | -250.82 [-919.00, -0.00] | 0.17 [-0.01, 0.31] | -10.98 [-13.28, -8.30] | -41.50 [-43.45, -38.23] | -25.71 [-27.84, -23.72] | 0.00 [0.00, 0.00] |
| main rule | 0.53 [0.46, 0.59] | 9211 [8575, 10098] | -51676 [-66143, -18815] | 0.12 [-0.04, 0.26] | -10.73 [-13.13, -8.01] | -41.31 [-43.39, -38.22] | -26.26 [-28.40, -23.58] | 0.00 [-0.00, 0.01] |
| sale discount 0.034 | 0.53 [0.46, 0.59] | 9212 [8576, 10098] | -51771 [-66536, -18766] | 0.12 [-0.03, 0.26] | -10.73 [-13.13, -8.01] | -41.31 [-43.38, -38.22] | -26.40 [-28.22, -23.76] | 0.00 [-0.00, 0.01] |
| sale discount 0.062 | 0.53 [0.46, 0.59] | 9212 [8577, 10099] | -51922 [-67126, -19057] | 0.12 [-0.03, 0.28] | -10.73 [-13.11, -8.01] | -41.32 [-43.38, -38.22] | -26.52 [-28.42, -23.76] | 0.00 [-0.00, 0.01] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | -0.20 [-0.36, -0.07] | -0.01 [-0.04, 0.00] | 0.58 [-0.44, 1.62] | 0.03 [0.00, 0.20] |
| sale discount 0.034 | -0.20 [-0.36, -0.07] | -0.01 [-0.04, 0.00] | 0.73 [-0.08, 1.80] | 0.04 [0.00, 0.20] |
| sale discount 0.062 | -0.20 [-0.36, -0.07] | -0.01 [-0.04, 0.00] | 0.85 [-0.08, 1.80] | 0.04 [0.00, 0.20] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.53 | 0.53 (main rule) | 0.53 (sale discount 0.034) | 3 of 3 |
| E P2 | 9211 | 9211 (main rule) | 9212 (sale discount 0.062) | 3 of 3 |
| E P3 | -51676 | -51922 (sale discount 0.062) | -51676 (main rule) | 3 of 3 |
| E P4 | 0.12 | 0.12 (main rule) | 0.12 (sale discount 0.062) | 3 of 3 |
| E P5 | -10.73 | -10.73 (main rule) | -10.73 (sale discount 0.062) | 3 of 3 |
| E basket pov. | -41.31 | -41.32 (sale discount 0.062) | -41.31 (sale discount 0.034) | 3 of 3 |
| E wealth pov. | -26.26 | -26.52 (sale discount 0.062) | -26.26 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.034) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | - | 40.20 (38.20 to 43.28) | 21.20 (18.56 to 23.80) |
| 1 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | 4.14 (3.81 to 4.38) | 42.00 (38.58 to 45.18) | 8.60 (7.12 to 10.32) |
| 2 | 2.97 (2.67 to 2.97) | 6.01 (5.17 to 6.34) | 3.02 (2.84 to 3.22) | 41.70 (38.52 to 46.74) | 3.10 (2.56 to 3.80) |
| 3 | 2.97 (0.00 to 2.97) | 4.35 (0.00 to 4.70) | 2.34 (2.19 to 2.45) | 42.60 (38.98 to 50.72) | 8.00 (6.78 to 9.04) |
| 4 | 2.97 (0.00 to 2.97) | 3.42 (0.00 to 3.64) | 1.83 (1.76 to 1.93) | 42.60 (38.44 to 46.52) | 3.60 (2.80 to 4.40) |
| 5 | 2.97 (0.00 to 2.97) | 2.70 (0.00 to 2.82) | 2.13 (2.01 to 2.28) | 43.90 (38.60 to 47.38) | 5.60 (4.40 to 6.82) |
| 6 | 2.97 (0.00 to 2.97) | 3.15 (0.00 to 3.39) | 1.96 (1.88 to 2.23) | 44.70 (40.00 to 47.38) | 2.90 (2.36 to 3.82) |
| 7 | 2.97 (0.00 to 2.97) | 2.88 (0.00 to 3.14) | 2.04 (1.95 to 2.12) | 43.90 (39.96 to 48.26) | 3.80 (2.98 to 4.64) |
| 8 | 2.97 (0.00 to 2.97) | 3.00 (0.00 to 3.13) | 1.98 (1.92 to 2.15) | 43.40 (38.96 to 46.16) | 2.70 (1.98 to 3.62) |
| 9 | 2.97 (2.97 to 2.97) | 2.94 (2.75 to 3.20) | 2.03 (1.92 to 2.17) | 43.70 (39.88 to 49.84) | 3.10 (2.20 to 3.82) |
| 10 | 2.97 (0.00 to 2.97) | 3.01 (0.00 to 3.23) | 2.00 (1.98 to 2.19) | 45.50 (40.34 to 51.06) | 2.80 (2.18 to 3.42) |
| 11 | 2.97 (0.00 to 2.97) | 2.96 (0.00 to 3.19) | 2.01 (1.99 to 2.14) | 46.40 (42.84 to 51.68) | 2.60 (1.78 to 4.04) |
| 12 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 3.00) | 2.00 (1.97 to 2.05) | 46.80 (43.52 to 50.50) | 2.40 (1.60 to 3.22) |
| 13 | 2.97 (0.00 to 2.97) | 2.95 (0.00 to 3.01) | 2.01 (2.00 to 2.04) | 47.20 (43.88 to 53.62) | 2.20 (1.38 to 2.42) |
| 14 | 2.97 (0.00 to 2.97) | 2.98 (0.00 to 3.02) | 2.01 (1.98 to 2.03) | 47.10 (44.40 to 53.68) | 1.80 (1.56 to 2.62) |
| 15 | 2.97 (0.00 to 2.97) | 2.95 (0.00 to 3.00) | 2.01 (1.99 to 2.02) | 48.80 (43.96 to 52.08) | 1.80 (1.18 to 2.80) |
| 16 | 2.97 (0.00 to 2.97) | 2.96 (0.00 to 3.01) | 2.00 (1.98 to 2.02) | 48.80 (43.96 to 53.58) | 1.70 (1.38 to 2.40) |
| 17 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.03) | 48.10 (46.14 to 53.02) | 1.60 (1.18 to 2.60) |
| 18 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.01) | 48.50 (46.16 to 52.40) | 1.60 (1.18 to 2.42) |
| 19 | 2.97 (2.97 to 2.97) | 2.97 (2.96 to 2.98) | 2.00 (1.99 to 2.01) | 48.40 (46.76 to 51.28) | 1.60 (0.98 to 2.42) |

### release design

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 2.51 [2.25, 2.72] | 16.25 [10.00, 25.00] | 28.23 [25.26, 32.66] | -0.41 [-0.65, -0.25] | 0.00 [0.00, 0.00] | 22.29 / 17.49 |
| sale discount 0.034 | 2.51 [2.25, 2.72] | 16.25 [10.00, 25.00] | 28.24 [25.25, 32.61] | -0.41 [-0.65, -0.25] | 0.00 [0.00, 0.00] | 22.23 / 17.43 |
| sale discount 0.062 | 2.51 [2.25, 2.72] | 16.25 [10.00, 25.00] | 28.26 [25.25, 32.61] | -0.41 [-0.65, -0.25] | 0.00 [0.00, 0.00] | 22.16 / 17.36 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.24 [0.21, 0.29] | 343.80 [152.36, 538.47] | -238.86 [-741.04, -0.00] | 0.24 [0.06, 0.45] | -3.59 [-6.10, -2.03] | -7.98 [-9.21, -6.55] | -3.40 [-4.82, -1.80] | 0.00 [0.00, 0.00] |
| main rule | 0.25 [0.20, 0.30] | 324.81 [110.05, 490.67] | -3090 [-5018, 53.92] | 0.22 [0.02, 0.39] | -3.54 [-6.09, -2.00] | -7.92 [-9.06, -6.43] | -3.69 [-5.22, -2.56] | 0.01 [-0.01, 0.02] |
| sale discount 0.034 | 0.25 [0.20, 0.30] | 325.18 [109.79, 489.98] | -2994 [-5992, 50.98] | 0.22 [0.02, 0.42] | -3.53 [-6.09, -2.00] | -7.92 [-9.06, -6.43] | -3.78 [-5.22, -2.56] | 0.01 [-0.01, 0.02] |
| sale discount 0.062 | 0.25 [0.20, 0.30] | 325.51 [109.90, 489.75] | -2933 [-6370, 48.35] | 0.23 [0.04, 0.46] | -3.53 [-6.10, -2.00] | -7.92 [-9.06, -6.45] | -3.73 [-5.06, -2.38] | 0.01 [-0.01, 0.02] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | -0.20 [-0.36, -0.07] | -0.14 [-0.24, -0.01] | 0.58 [-0.44, 1.62] | 0.29 [-1.00, 1.02] |
| sale discount 0.034 | -0.20 [-0.36, -0.07] | -0.14 [-0.26, -0.01] | 0.73 [-0.08, 1.80] | 0.35 [-1.00, 1.02] |
| sale discount 0.062 | -0.20 [-0.36, -0.07] | -0.14 [-0.26, -0.01] | 0.85 [-0.08, 1.80] | 0.52 [-0.64, 1.20] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.25 | 0.25 (main rule) | 0.25 (sale discount 0.062) | 3 of 3 |
| E P2 | 324.81 | 324.81 (main rule) | 325.51 (sale discount 0.062) | 3 of 3 |
| E P3 | -3090 | -3090 (main rule) | -2933 (sale discount 0.062) | 3 of 3 |
| E P4 | 0.22 | 0.22 (main rule) | 0.23 (sale discount 0.062) | 3 of 3 |
| E P5 | -3.54 | -3.54 (main rule) | -3.53 (sale discount 0.062) | 3 of 3 |
| E basket pov. | -7.92 | -7.92 (sale discount 0.062) | -7.92 (main rule) | 3 of 3 |
| E wealth pov. | -3.69 | -3.78 (sale discount 0.034) | -3.69 (main rule) | 3 of 3 |
| X P1 | 0.01 | 0.01 (main rule) | 0.01 (sale discount 0.062) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | - | 40.20 (38.20 to 43.28) | 37.30 (34.12 to 39.00) |
| 1 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | 2.49 (2.35 to 2.64) | 42.00 (38.58 to 45.18) | 32.00 (28.60 to 35.06) |
| 2 | 2.97 (2.67 to 2.97) | 3.67 (3.09 to 3.85) | 2.63 (2.50 to 2.73) | 41.70 (38.52 to 46.74) | 33.30 (30.34 to 36.82) |
| 3 | 2.97 (0.00 to 2.97) | 3.91 (0.00 to 4.01) | 1.98 (1.87 to 2.09) | 42.60 (38.98 to 50.72) | 34.50 (29.96 to 37.40) |
| 4 | 2.97 (0.00 to 2.97) | 2.90 (0.00 to 3.10) | 1.92 (1.82 to 2.01) | 42.60 (38.44 to 46.52) | 33.60 (30.86 to 36.94) |
| 5 | 2.97 (0.00 to 2.97) | 2.81 (0.00 to 2.97) | 1.96 (1.84 to 2.09) | 43.90 (38.60 to 47.38) | 35.10 (32.64 to 37.04) |
| 6 | 2.97 (0.00 to 2.97) | 2.82 (0.00 to 3.09) | 2.00 (1.85 to 2.13) | 44.70 (40.00 to 47.38) | 35.50 (32.04 to 38.06) |
| 7 | 2.97 (0.00 to 2.97) | 2.91 (0.00 to 3.17) | 2.02 (1.89 to 2.21) | 43.90 (39.96 to 48.26) | 35.70 (33.30 to 38.80) |
| 8 | 2.97 (0.00 to 2.97) | 2.98 (0.00 to 3.17) | 1.94 (1.81 to 2.06) | 43.40 (38.96 to 46.16) | 35.30 (32.72 to 37.46) |
| 9 | 2.97 (2.97 to 2.97) | 2.86 (2.67 to 3.06) | 1.94 (1.86 to 2.12) | 43.70 (39.88 to 49.84) | 35.10 (33.56 to 40.62) |
| 10 | 2.97 (0.00 to 2.97) | 2.87 (0.00 to 3.11) | 1.92 (1.76 to 2.08) | 45.50 (40.34 to 51.06) | 37.30 (34.50 to 40.88) |
| 11 | 2.97 (0.00 to 2.97) | 2.80 (0.00 to 3.02) | 1.97 (1.82 to 2.11) | 46.40 (42.84 to 51.68) | 38.20 (34.18 to 41.88) |
| 12 | 2.97 (0.00 to 2.97) | 2.82 (0.00 to 3.01) | 1.92 (1.83 to 2.07) | 46.80 (43.52 to 50.50) | 39.20 (35.56 to 42.40) |
| 13 | 2.97 (0.00 to 2.97) | 2.76 (0.00 to 3.03) | 1.94 (1.73 to 2.30) | 47.20 (43.88 to 53.62) | 39.60 (36.74 to 43.64) |
| 14 | 2.97 (0.00 to 2.97) | 2.73 (0.00 to 3.01) | 1.94 (1.68 to 2.13) | 47.10 (44.40 to 53.68) | 40.10 (36.78 to 44.10) |
| 15 | 2.97 (0.00 to 2.97) | 2.73 (0.00 to 3.06) | 1.93 (1.58 to 2.06) | 48.80 (43.96 to 52.08) | 41.10 (38.68 to 44.04) |
| 16 | 2.97 (0.00 to 2.97) | 2.83 (0.00 to 3.05) | 2.03 (1.83 to 2.17) | 48.80 (43.96 to 53.58) | 41.00 (38.10 to 44.44) |
| 17 | 2.97 (0.00 to 2.97) | 2.86 (0.00 to 3.19) | 2.00 (1.65 to 2.22) | 48.10 (46.14 to 53.02) | 41.20 (39.56 to 44.46) |
| 18 | 2.97 (0.00 to 2.97) | 2.84 (0.00 to 3.30) | 1.92 (1.69 to 2.21) | 48.50 (46.16 to 52.40) | 42.20 (38.54 to 44.52) |
| 19 | 2.97 (2.97 to 2.97) | 2.82 (2.45 to 3.29) | 1.97 (1.83 to 2.17) | 48.40 (46.76 to 51.28) | 41.50 (40.36 to 44.02) |

## Reference

Engine: 1db387848de63846e80e1211eb6979be0abba295 (dirty); command `node dev/tools/s74_sweep.js ref 20 --only=off,main,fd0.034,fd0.062 --out=dev/runs/s74-fd`; 20 seeds; 4 settings.

### C2.2

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 0.30 [0.27, 0.34] | 56.00 [49.50, 60.50] | 5.39 [3.95, 7.21] | 0.04 [0.03, 0.04] | 0.00 [0.00, 0.00] | 18.32 / 0.69 |
| sale discount 0.034 | 0.30 [0.27, 0.34] | 55.75 [49.50, 60.50] | 5.35 [4.01, 7.17] | 0.04 [0.03, 0.04] | 0.00 [0.00, 0.00] | 18.26 / 0.69 |
| sale discount 0.062 | 0.30 [0.27, 0.34] | 56.25 [49.50, 65.00] | 5.36 [4.01, 7.21] | 0.04 [0.03, 0.04] | 0.00 [0.00, 0.00] | 18.23 / 0.68 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.54 [0.48, 0.61] | 14159 [13135, 14969] | -65.11 [-57.63, 0.00] | -0.42 [-0.59, -0.28] | 0.00 [0.00, 0.00] | -33.24 [-35.75, -31.23] | -22.56 [-24.26, -20.76] | 0.00 [0.00, 0.00] |
| main rule | 0.54 [0.48, 0.60] | 14162 [13134, 14986] | -204.60 [-483.11, 0.00] | -0.44 [-0.59, -0.26] | 0.00 [0.00, 0.00] | -33.30 [-35.81, -31.23] | -24.11 [-25.72, -22.60] | -0.00 [-0.00, 0.00] |
| sale discount 0.034 | 0.54 [0.48, 0.60] | 14162 [13135, 14987] | -204.70 [-482.91, 0.00] | -0.44 [-0.59, -0.26] | 0.00 [0.00, 0.00] | -33.31 [-35.81, -31.24] | -24.18 [-25.72, -22.60] | -0.00 [-0.00, 0.00] |
| sale discount 0.062 | 0.54 [0.48, 0.60] | 14163 [13135, 14987] | -205.50 [-481.53, 0.00] | -0.44 [-0.59, -0.24] | 0.00 [0.00, 0.00] | -33.31 [-35.81, -31.25] | -24.27 [-25.74, -22.60] | -0.00 [-0.00, 0.00] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | 0.07 [0.03, 0.11] | 0.00 [-0.00, 0.02] | 1.59 [0.98, 2.20] | 0.04 [0.00, 0.20] |
| sale discount 0.034 | 0.07 [0.03, 0.12] | 0.00 [-0.00, 0.02] | 1.66 [1.16, 2.20] | 0.04 [0.00, 0.20] |
| sale discount 0.062 | 0.08 [0.03, 0.12] | 0.00 [-0.00, 0.02] | 1.75 [1.20, 2.42] | 0.04 [0.00, 0.20] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.54 | 0.54 (sale discount 0.062) | 0.54 (main rule) | 3 of 3 |
| E P2 | 14162 | 14162 (main rule) | 14163 (sale discount 0.062) | 3 of 3 |
| E P3 | -204.60 | -205.50 (sale discount 0.062) | -204.60 (main rule) | 3 of 3 |
| E P4 | -0.44 | -0.44 (sale discount 0.034) | -0.44 (sale discount 0.062) | 3 of 3 |
| E P5 | 0.00 | 0.00 (main rule) | 0.00 (main rule) | 3 of 3 |
| E basket pov. | -33.30 | -33.31 (sale discount 0.062) | -33.30 (main rule) | 3 of 3 |
| E wealth pov. | -24.11 | -24.27 (sale discount 0.062) | -24.11 (main rule) | 3 of 3 |
| X P1 | -0.00 | -0.00 (sale discount 0.062) | -0.00 (main rule) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | - | 40.20 (38.20 to 43.28) | 20.30 (18.26 to 22.62) |
| 1 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | 2.09 (1.81 to 2.36) | 40.40 (38.20 to 44.06) | 6.90 (5.80 to 9.60) |
| 2 | 0.00 (0.00 to 0.00) | 3.11 (2.68 to 3.51) | 0.92 (0.75 to 1.16) | 39.80 (37.00 to 45.02) | 2.60 (1.78 to 3.22) |
| 3 | 0.00 (0.00 to 0.00) | 1.35 (1.10 to 1.72) | 0.29 (0.11 to 0.46) | 40.10 (34.32 to 44.08) | 7.10 (5.56 to 8.44) |
| 4 | 0.00 (0.00 to 0.00) | 0.41 (0.13 to 0.66) | -0.19 (-0.33 to -0.04) | 39.10 (34.58 to 42.18) | 3.10 (2.76 to 4.62) |
| 5 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | 0.17 (-0.09 to 0.25) | 38.00 (35.42 to 43.06) | 4.90 (3.78 to 6.42) |
| 6 | 0.00 (0.00 to 0.00) | 0.23 (0.00 to 0.34) | -0.07 (-0.25 to 0.09) | 37.30 (33.72 to 42.24) | 3.20 (1.98 to 4.00) |
| 7 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.11) | -0.07 (-0.21 to 0.07) | 37.30 (34.24 to 40.28) | 3.30 (2.20 to 4.02) |
| 8 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.07) | -0.04 (-0.12 to 0.17) | 36.30 (33.18 to 39.86) | 2.10 (1.80 to 3.20) |
| 9 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.22) | 0.07 (-0.17 to 0.18) | 35.50 (31.76 to 40.62) | 2.10 (1.40 to 2.82) |
| 10 | 0.00 (0.00 to 0.00) | 0.08 (0.00 to 0.24) | -0.00 (-0.10 to 0.24) | 35.70 (33.10 to 40.66) | 1.70 (1.38 to 2.22) |
| 11 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.33) | -0.02 (-0.20 to 0.12) | 35.50 (31.74 to 39.28) | 1.60 (1.00 to 2.20) |
| 12 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.15) | -0.04 (-0.23 to 0.12) | 35.80 (32.88 to 38.72) | 1.40 (1.00 to 2.00) |
| 13 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.15) | 0.02 (-0.24 to 0.20) | 34.50 (32.20 to 37.28) | 1.20 (0.80 to 1.64) |
| 14 | 0.00 (0.00 to 0.00) | 0.01 (0.00 to 0.27) | -0.06 (-0.26 to 0.08) | 35.30 (32.94 to 37.82) | 1.10 (0.80 to 1.62) |
| 15 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.09) | 0.07 (-0.15 to 0.22) | 34.80 (32.74 to 36.40) | 1.00 (0.78 to 1.42) |
| 16 | 0.00 (0.00 to 0.00) | 0.07 (0.00 to 0.30) | -0.09 (-0.25 to 0.13) | 33.80 (32.36 to 36.48) | 1.00 (0.78 to 1.44) |
| 17 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.17) | -0.01 (-0.22 to 0.17) | 33.50 (31.98 to 35.82) | 0.80 (0.60 to 1.22) |
| 18 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.22) | -0.04 (-0.29 to 0.19) | 33.30 (31.78 to 36.20) | 0.80 (0.38 to 1.42) |
| 19 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.25) | -0.03 (-0.15 to 0.04) | 33.20 (31.20 to 35.42) | 0.60 (0.40 to 1.04) |

### release design

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 0.24 [0.21, 0.26] | 52.00 [50.00, 60.00] | 5.01 [2.97, 6.55] | 0.03 [0.03, 0.03] | 0.00 [0.00, 0.00] | 18.32 / 5.75 |
| sale discount 0.034 | 0.24 [0.21, 0.26] | 51.50 [45.00, 55.50] | 4.99 [3.04, 6.57] | 0.03 [0.03, 0.03] | 0.00 [0.00, 0.00] | 18.26 / 5.71 |
| sale discount 0.062 | 0.24 [0.21, 0.26] | 51.50 [45.00, 60.00] | 4.99 [3.10, 6.58] | 0.03 [0.03, 0.03] | 0.00 [0.00, 0.00] | 18.23 / 5.67 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.40 [0.35, 0.46] | 2478 [2069, 3044] | -65.11 [-57.63, 0.00] | 0.18 [0.04, 0.34] | 0.00 [0.00, 0.00] | -22.28 [-25.07, -19.88] | -14.98 [-17.00, -12.98] | 0.00 [0.00, 0.00] |
| main rule | 0.40 [0.35, 0.45] | 2486 [2055, 3051] | -204.60 [-483.11, 0.00] | 0.16 [0.01, 0.31] | 0.00 [0.00, 0.00] | -22.30 [-25.11, -19.84] | -16.11 [-18.06, -13.98] | -0.00 [-0.00, 0.00] |
| sale discount 0.034 | 0.40 [0.35, 0.45] | 2488 [2074, 3061] | -204.70 [-482.91, 0.00] | 0.16 [0.02, 0.30] | 0.00 [0.00, 0.00] | -22.30 [-25.11, -19.83] | -16.16 [-18.06, -14.16] | -0.00 [-0.00, 0.00] |
| sale discount 0.062 | 0.40 [0.35, 0.45] | 2486 [2073, 3061] | -205.50 [-481.53, 0.00] | 0.17 [0.03, 0.34] | 0.00 [0.00, 0.00] | -22.30 [-25.11, -19.83] | -16.21 [-18.06, -14.16] | -0.00 [-0.00, 0.00] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | 0.07 [0.03, 0.11] | 0.05 [0.02, 0.10] | 1.59 [0.98, 2.20] | 0.46 [0.00, 1.00] |
| sale discount 0.034 | 0.07 [0.03, 0.12] | 0.05 [0.02, 0.11] | 1.66 [1.16, 2.20] | 0.48 [0.00, 1.02] |
| sale discount 0.062 | 0.08 [0.03, 0.12] | 0.05 [0.02, 0.11] | 1.75 [1.20, 2.42] | 0.52 [0.00, 1.20] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.40 | 0.40 (sale discount 0.062) | 0.40 (main rule) | 3 of 3 |
| E P2 | 2486 | 2486 (sale discount 0.062) | 2488 (sale discount 0.034) | 3 of 3 |
| E P3 | -204.60 | -205.50 (sale discount 0.062) | -204.60 (main rule) | 3 of 3 |
| E P4 | 0.16 | 0.16 (sale discount 0.034) | 0.17 (sale discount 0.062) | 3 of 3 |
| E P5 | 0.00 | 0.00 (main rule) | 0.00 (main rule) | 3 of 3 |
| E basket pov. | -22.30 | -22.30 (sale discount 0.062) | -22.30 (main rule) | 3 of 3 |
| E wealth pov. | -16.11 | -16.21 (sale discount 0.062) | -16.11 (main rule) | 3 of 3 |
| X P1 | -0.00 | -0.00 (sale discount 0.062) | -0.00 (main rule) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | - | 40.20 (38.20 to 43.28) | 29.40 (26.74 to 31.08) |
| 1 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | 1.25 (1.04 to 1.41) | 40.40 (38.20 to 44.06) | 16.60 (15.36 to 19.22) |
| 2 | 0.00 (0.00 to 0.00) | 1.85 (1.53 to 2.08) | 1.08 (0.87 to 1.34) | 39.80 (37.00 to 45.02) | 14.80 (13.76 to 17.02) |
| 3 | 0.00 (0.00 to 0.00) | 1.60 (1.28 to 1.98) | 0.15 (0.08 to 0.42) | 40.10 (34.32 to 44.08) | 17.60 (15.36 to 20.24) |
| 4 | 0.00 (0.00 to 0.00) | 0.19 (0.09 to 0.59) | -0.18 (-0.36 to -0.11) | 39.10 (34.58 to 42.18) | 15.30 (13.18 to 17.44) |
| 5 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | 0.13 (-0.07 to 0.24) | 38.00 (35.42 to 43.06) | 16.50 (14.52 to 17.60) |
| 6 | 0.00 (0.00 to 0.00) | 0.17 (0.00 to 0.33) | -0.06 (-0.23 to 0.10) | 37.30 (33.72 to 42.24) | 14.30 (12.74 to 15.88) |
| 7 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.12) | 0.01 (-0.11 to 0.11) | 37.30 (34.24 to 40.28) | 14.90 (12.98 to 17.52) |
| 8 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.14) | -0.08 (-0.17 to 0.07) | 36.30 (33.18 to 39.86) | 14.50 (12.54 to 16.08) |
| 9 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.08) | 0.06 (-0.18 to 0.17) | 35.50 (31.76 to 40.62) | 14.10 (12.42 to 16.82) |
| 10 | 0.00 (0.00 to 0.00) | 0.05 (0.00 to 0.23) | 0.06 (-0.11 to 0.26) | 35.70 (33.10 to 40.66) | 13.80 (11.16 to 14.86) |
| 11 | 0.00 (0.00 to 0.00) | 0.06 (0.00 to 0.35) | 0.04 (-0.08 to 0.18) | 35.50 (31.74 to 39.28) | 12.90 (11.64 to 14.64) |
| 12 | 0.00 (0.00 to 0.00) | 0.03 (0.00 to 0.24) | 0.01 (-0.18 to 0.14) | 35.80 (32.88 to 38.72) | 12.80 (10.40 to 14.24) |
| 13 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.18) | 0.04 (-0.10 to 0.20) | 34.50 (32.20 to 37.28) | 12.60 (10.56 to 13.68) |
| 14 | 0.00 (0.00 to 0.00) | 0.02 (0.00 to 0.27) | -0.06 (-0.16 to 0.08) | 35.30 (32.94 to 37.82) | 12.30 (10.56 to 13.42) |
| 15 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.09) | 0.07 (-0.08 to 0.24) | 34.80 (32.74 to 36.40) | 11.80 (10.14 to 13.40) |
| 16 | 0.00 (0.00 to 0.00) | 0.07 (0.00 to 0.33) | -0.06 (-0.29 to 0.12) | 33.80 (32.36 to 36.48) | 11.30 (9.74 to 13.10) |
| 17 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.15) | -0.02 (-0.17 to 0.20) | 33.50 (31.98 to 35.82) | 11.20 (9.78 to 13.00) |
| 18 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.27) | 0.02 (-0.21 to 0.15) | 33.30 (31.78 to 36.20) | 10.70 (9.58 to 12.62) |
| 19 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.19) | -0.03 (-0.16 to 0.07) | 33.20 (31.20 to 35.42) | 11.10 (9.56 to 12.46) |

