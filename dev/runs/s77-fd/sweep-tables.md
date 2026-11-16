# S74 forward sweep tables (20 seeds, frozen round-2 main row)

Made by `node dev/tools/s74_sweep_table.js` from the sweep files in this folder (`node dev/tools/s74_sweep.js ENV 20`). Descriptive only: each cell is the mean over seeds 1-20 with the 10th to 90th percentile across seeds in brackets. E is the programme's effect (programme minus no programme, paired on seeds) in each setting; C is the setting's effect against no central bank, paired on seeds; X is the interaction on P1 (E in the setting minus E with no central bank). P1 spread of the basket price level's yearly change (points); P2 spread of yearly changes in real cash income ($, mean); P3 largest fall in real wealth ($, median); P4 years to recover from an income shock; P5 % pushed below the basket line in a recession year; basket poverty (`fgt0PY`, % of adult-years); wealth poverty (`pov`, % in the last year).

## History (2005-2025)

Engine: e5649efec5160cb34abdb101d2cddc52cd992d28; command `node dev/tools/s74_sweep.js hx 20 --only=off,main,fd0.034,fd0.062 --out=/home/user/runs/s77-fd`; 20 seeds; 4 settings.

### C2.2

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 3.80 [3.76, 3.82] | 0.71 [0.00, 4.76] | 0.22 [0.00, 0.43] | 1.15 [1.14, 1.15] | 0.00 [0.00, 0.00] | 22.78 / 1.01 |
| sale discount 0.034 | 3.80 [3.76, 3.82] | 0.71 [0.00, 4.76] | 0.22 [0.00, 0.42] | 1.15 [1.14, 1.15] | 0.00 [0.00, 0.00] | 22.67 / 1.00 |
| sale discount 0.062 | 3.80 [3.76, 3.82] | 0.71 [0.00, 4.76] | 0.22 [0.00, 0.41] | 1.15 [1.14, 1.15] | 0.00 [0.00, 0.00] | 22.54 / 1.00 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.08 [0.06, 0.11] | 13164 [12311, 13914] | -32779 [-35827, -30059] | -0.36 [-0.53, -0.15] | -7.30 [-8.86, -5.99] | -42.16 [-44.46, -39.40] | -25.00 [-27.60, -23.38] | 0.00 [0.00, 0.00] |
| main rule | 0.08 [0.06, 0.10] | 13063 [12127, 13812] | -31783 [-35484, -28550] | -0.34 [-0.46, -0.20] | -7.57 [-9.43, -6.16] | -42.62 [-44.84, -39.89] | -28.42 [-29.80, -27.20] | 0.00 [-0.02, 0.01] |
| sale discount 0.034 | 0.08 [0.06, 0.10] | 13064 [12126, 13813] | -31863 [-35474, -28547] | -0.34 [-0.46, -0.20] | -7.57 [-9.43, -6.16] | -42.62 [-44.84, -39.90] | -28.61 [-29.84, -27.38] | 0.00 [-0.01, 0.01] |
| sale discount 0.062 | 0.08 [0.06, 0.10] | 13065 [12125, 13814] | -31951 [-35497, -28545] | -0.34 [-0.45, -0.20] | -7.57 [-9.43, -6.16] | -42.62 [-44.84, -39.90] | -28.72 [-30.42, -27.40] | 0.00 [-0.01, 0.01] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | 0.48 [0.32, 0.57] | 0.02 [-0.02, 0.07] | 3.65 [2.58, 4.82] | 0.23 [0.00, 0.60] |
| sale discount 0.034 | 0.48 [0.32, 0.57] | 0.02 [-0.02, 0.07] | 3.84 [2.58, 5.02] | 0.23 [0.00, 0.60] |
| sale discount 0.062 | 0.48 [0.32, 0.57] | 0.02 [-0.02, 0.07] | 3.95 [2.78, 5.20] | 0.23 [0.00, 0.60] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.08 | 0.08 (main rule) | 0.08 (sale discount 0.062) | 3 of 3 |
| E P2 | 13063 | 13063 (main rule) | 13065 (sale discount 0.062) | 3 of 3 |
| E P3 | -31783 | -31951 (sale discount 0.062) | -31783 (main rule) | 3 of 3 |
| E P4 | -0.34 | -0.34 (main rule) | -0.34 (sale discount 0.062) | 3 of 3 |
| E P5 | -7.57 | -7.57 (main rule) | -7.57 (main rule) | 3 of 3 |
| E basket pov. | -42.62 | -42.62 (sale discount 0.062) | -42.62 (main rule) | 3 of 3 |
| E wealth pov. | -28.42 | -28.72 (sale discount 0.062) | -28.42 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.062) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 2005 | 5.40 (5.40 to 5.40) | 5.40 (5.40 to 5.40) | - | 40.20 (38.20 to 43.28) | 21.40 (18.54 to 23.82) |
| 2006 | 5.40 (5.40 to 5.40) | 5.40 (5.40 to 5.40) | 4.67 (4.35 to 4.93) | 42.20 (38.94 to 45.62) | 8.10 (7.00 to 10.28) |
| 2007 | 4.40 (4.40 to 4.40) | 7.62 (7.13 to 8.01) | 5.10 (4.96 to 5.31) | 42.60 (39.10 to 47.52) | 3.20 (2.58 to 3.80) |
| 2008 | 6.73 (6.73 to 6.73) | 8.21 (8.00 to 8.53) | 0.35 (0.21 to 0.56) | 43.70 (39.36 to 49.00) | 8.80 (7.18 to 10.66) |
| 2009 | 0.00 (0.00 to 0.00) | 0.18 (0.00 to 0.50) | 2.67 (2.59 to 2.80) | 44.70 (41.54 to 50.44) | 4.20 (3.38 to 4.88) |
| 2010 | 1.86 (1.86 to 1.86) | 1.65 (1.53 to 1.85) | 1.58 (1.54 to 1.78) | 46.80 (42.66 to 51.26) | 6.80 (5.40 to 8.62) |
| 2011 | 0.46 (0.46 to 0.46) | 0.66 (0.61 to 0.97) | 2.99 (2.93 to 3.05) | 47.80 (43.72 to 52.42) | 3.90 (3.18 to 5.02) |
| 2012 | 2.94 (2.94 to 2.94) | 2.83 (2.73 to 2.93) | 1.83 (1.80 to 1.88) | 48.20 (45.56 to 52.84) | 4.50 (3.58 to 5.64) |
| 2013 | 1.29 (1.29 to 1.29) | 1.39 (1.35 to 1.47) | 1.51 (1.49 to 1.54) | 47.50 (41.58 to 50.12) | 2.70 (1.78 to 4.00) |
| 2014 | 1.08 (1.08 to 1.08) | 1.07 (1.04 to 1.11) | 0.70 (0.68 to 0.71) | 46.20 (42.20 to 50.66) | 2.70 (1.96 to 3.62) |
| 2015 | 0.09 (0.09 to 0.09) | 0.15 (0.13 to 0.17) | 0.64 (0.63 to 0.67) | 46.30 (41.28 to 48.22) | 2.00 (1.58 to 2.82) |
| 2016 | 0.52 (0.52 to 0.52) | 0.52 (0.50 to 0.56) | 2.06 (2.04 to 2.08) | 45.50 (41.76 to 48.16) | 2.30 (1.78 to 2.64) |
| 2017 | 2.52 (2.52 to 2.52) | 2.53 (2.51 to 2.57) | 2.13 (2.09 to 2.15) | 45.80 (42.16 to 48.00) | 1.90 (1.40 to 2.62) |
| 2018 | 2.85 (2.85 to 2.85) | 2.86 (2.79 to 2.88) | 2.00 (1.89 to 2.03) | 45.80 (42.86 to 49.28) | 1.60 (1.20 to 2.62) |
| 2019 | 3.11 (3.11 to 3.11) | 3.10 (2.94 to 3.16) | 2.34 (2.31 to 2.45) | 45.20 (43.20 to 49.28) | 1.50 (1.18 to 2.46) |
| 2020 | 3.82 (3.82 to 3.82) | 3.85 (3.81 to 4.02) | 1.32 (1.32 to 1.38) | 47.70 (44.62 to 50.42) | 1.40 (0.98 to 2.04) |
| 2021 | 0.31 (0.31 to 0.31) | 0.32 (0.31 to 0.40) | 7.18 (7.15 to 7.19) | 49.50 (46.52 to 51.62) | 1.40 (1.20 to 2.40) |
| 2022 | 11.14 (11.14 to 11.14) | 11.15 (11.10 to 11.16) | 6.41 (6.39 to 6.44) | 51.10 (48.36 to 54.02) | 1.60 (1.00 to 2.42) |
| 2023 | 10.03 (10.03 to 10.03) | 10.04 (10.01 to 10.09) | 3.31 (3.30 to 3.32) | 51.80 (49.18 to 54.64) | 1.20 (0.80 to 2.02) |
| 2024 | 5.55 (5.55 to 5.55) | 5.54 (5.53 to 5.55) | 2.88 (2.87 to 2.88) | 51.20 (49.08 to 52.94) | 1.20 (0.60 to 1.84) |
| 2025 | 5.02 (5.02 to 5.02) | 5.03 (5.01 to 5.04) | 2.66 (2.65 to 2.66) | 51.90 (48.36 to 54.22) | 1.10 (0.60 to 1.60) |

### release design

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 3.73 [3.69, 3.76] | 5.24 [0.00, 9.52] | 1.23 [0.00, 2.81] | 1.13 [1.13, 1.14] | 0.00 [0.00, 0.00] | 22.78 / 7.48 |
| sale discount 0.034 | 3.73 [3.69, 3.76] | 5.24 [0.00, 9.52] | 1.22 [0.00, 2.83] | 1.13 [1.13, 1.14] | 0.00 [0.00, 0.00] | 22.67 / 7.44 |
| sale discount 0.062 | 3.73 [3.69, 3.76] | 5.24 [0.00, 9.52] | 1.22 [0.00, 2.86] | 1.13 [1.13, 1.14] | 0.00 [0.00, 0.00] | 22.54 / 7.39 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.12 [0.10, 0.14] | 2655 [2251, 3112] | -20747 [-23426, -17632] | 0.50 [0.28, 0.68] | -3.24 [-4.54, -2.04] | -23.97 [-26.61, -21.00] | -14.62 [-16.06, -12.76] | 0.00 [0.00, 0.00] |
| main rule | 0.12 [0.10, 0.14] | 2621 [2201, 3099] | -19360 [-22435, -16286] | 0.43 [0.24, 0.62] | -3.38 [-4.92, -2.23] | -24.14 [-27.04, -21.22] | -16.79 [-18.46, -15.56] | 0.00 [-0.01, 0.02] |
| sale discount 0.034 | 0.12 [0.10, 0.15] | 2622 [2203, 3099] | -19364 [-22431, -16595] | 0.43 [0.26, 0.62] | -3.38 [-4.92, -2.23] | -24.14 [-27.04, -21.22] | -16.92 [-18.86, -15.56] | 0.00 [-0.01, 0.02] |
| sale discount 0.062 | 0.12 [0.10, 0.15] | 2623 [2204, 3099] | -19402 [-22424, -16382] | 0.43 [0.25, 0.61] | -3.38 [-4.92, -2.23] | -24.14 [-27.04, -21.22] | -16.99 [-18.86, -15.74] | 0.00 [-0.01, 0.02] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | 0.48 [0.32, 0.57] | 0.31 [0.19, 0.40] | 3.65 [2.58, 4.82] | 1.48 [0.80, 2.62] |
| sale discount 0.034 | 0.48 [0.32, 0.57] | 0.31 [0.20, 0.40] | 3.84 [2.58, 5.02] | 1.54 [0.80, 2.62] |
| sale discount 0.062 | 0.48 [0.32, 0.57] | 0.31 [0.20, 0.40] | 3.95 [2.78, 5.20] | 1.58 [0.80, 2.80] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.12 | 0.12 (main rule) | 0.12 (sale discount 0.062) | 3 of 3 |
| E P2 | 2621 | 2621 (main rule) | 2623 (sale discount 0.062) | 3 of 3 |
| E P3 | -19360 | -19402 (sale discount 0.062) | -19360 (main rule) | 3 of 3 |
| E P4 | 0.43 | 0.43 (main rule) | 0.43 (sale discount 0.034) | 3 of 3 |
| E P5 | -3.38 | -3.38 (main rule) | -3.38 (sale discount 0.034) | 3 of 3 |
| E basket pov. | -24.14 | -24.14 (sale discount 0.062) | -24.14 (sale discount 0.034) | 3 of 3 |
| E wealth pov. | -16.79 | -16.99 (sale discount 0.062) | -16.79 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.062) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 2005 | 5.40 (5.40 to 5.40) | 5.40 (5.40 to 5.40) | - | 40.20 (38.20 to 43.28) | 29.60 (27.58 to 32.22) |
| 2006 | 5.40 (5.40 to 5.40) | 5.40 (5.40 to 5.40) | 3.79 (3.57 to 3.90) | 42.20 (38.94 to 45.62) | 18.20 (16.40 to 20.84) |
| 2007 | 4.40 (4.40 to 4.40) | 6.30 (5.97 to 6.46) | 5.27 (5.07 to 5.44) | 42.60 (39.10 to 47.52) | 17.50 (16.74 to 20.02) |
| 2008 | 6.73 (6.73 to 6.73) | 8.47 (8.17 to 8.73) | 0.19 (0.07 to 0.36) | 43.70 (39.36 to 49.00) | 19.80 (17.80 to 23.86) |
| 2009 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.19) | 2.71 (2.58 to 2.88) | 44.70 (41.54 to 50.44) | 18.90 (17.10 to 21.44) |
| 2010 | 1.86 (1.86 to 1.86) | 1.71 (1.51 to 1.96) | 1.42 (1.27 to 1.60) | 46.80 (42.66 to 51.26) | 22.40 (19.98 to 25.12) |
| 2011 | 0.46 (0.46 to 0.46) | 0.43 (0.20 to 0.70) | 2.88 (2.79 to 3.04) | 47.80 (43.72 to 52.42) | 21.10 (19.20 to 24.26) |
| 2012 | 2.94 (2.94 to 2.94) | 2.67 (2.53 to 2.91) | 1.79 (1.67 to 1.93) | 48.20 (45.56 to 52.84) | 24.00 (21.74 to 27.44) |
| 2013 | 1.29 (1.29 to 1.29) | 1.33 (1.15 to 1.55) | 1.33 (1.24 to 1.42) | 47.50 (41.58 to 50.12) | 24.80 (21.60 to 25.98) |
| 2014 | 1.08 (1.08 to 1.08) | 0.81 (0.66 to 0.93) | 0.61 (0.55 to 0.80) | 46.20 (42.20 to 50.66) | 24.70 (21.52 to 26.08) |
| 2015 | 0.09 (0.09 to 0.09) | 0.03 (0.00 to 0.31) | 0.62 (0.44 to 0.82) | 46.30 (41.28 to 48.22) | 22.70 (20.72 to 25.24) |
| 2016 | 0.52 (0.52 to 0.52) | 0.50 (0.22 to 0.78) | 2.21 (2.08 to 2.32) | 45.50 (41.76 to 48.16) | 23.00 (20.96 to 24.92) |
| 2017 | 2.52 (2.52 to 2.52) | 2.76 (2.56 to 2.93) | 2.11 (2.02 to 2.29) | 45.80 (42.16 to 48.00) | 23.80 (21.00 to 26.44) |
| 2018 | 2.85 (2.85 to 2.85) | 2.82 (2.69 to 3.09) | 1.94 (1.85 to 2.04) | 45.80 (42.86 to 49.28) | 23.90 (21.60 to 27.44) |
| 2019 | 3.11 (3.11 to 3.11) | 3.02 (2.89 to 3.17) | 2.26 (2.18 to 2.45) | 45.20 (43.20 to 49.28) | 25.40 (23.40 to 29.06) |
| 2020 | 3.82 (3.82 to 3.82) | 3.73 (3.61 to 4.02) | 1.24 (1.12 to 1.35) | 47.70 (44.62 to 50.42) | 26.10 (23.60 to 28.26) |
| 2021 | 0.31 (0.31 to 0.31) | 0.18 (0.02 to 0.36) | 7.15 (7.00 to 7.28) | 49.50 (46.52 to 51.62) | 23.10 (19.58 to 26.04) |
| 2022 | 11.14 (11.14 to 11.14) | 11.11 (10.88 to 11.30) | 6.75 (6.54 to 6.90) | 51.10 (48.36 to 54.02) | 20.50 (17.84 to 21.62) |
| 2023 | 10.03 (10.03 to 10.03) | 10.56 (10.23 to 10.78) | 3.50 (3.42 to 3.68) | 51.80 (49.18 to 54.64) | 18.60 (16.30 to 20.92) |
| 2024 | 5.55 (5.55 to 5.55) | 5.83 (5.70 to 6.09) | 2.87 (2.80 to 2.96) | 51.20 (49.08 to 52.94) | 21.90 (19.62 to 23.06) |
| 2025 | 5.02 (5.02 to 5.02) | 5.02 (4.91 to 5.16) | 2.51 (2.42 to 2.61) | 51.90 (48.36 to 54.22) | 22.90 (18.78 to 24.44) |

## Adverse

Engine: e5649efec5160cb34abdb101d2cddc52cd992d28; command `node dev/tools/s74_sweep.js adv 20 --only=off,main,fd0.034,fd0.062 --out=/home/user/runs/s77-fd`; 20 seeds; 4 settings.

### C2.2

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.34 [24.42, 27.26] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.83 / 1.07 |
| sale discount 0.034 | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.34 [24.42, 27.33] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.77 / 1.06 |
| sale discount 0.062 | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.34 [24.42, 27.32] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.70 / 1.06 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.53 [0.46, 0.60] | 13355 [12413, 14045] | -208.89 [-866.75, -0.00] | -0.11 [-0.33, 0.15] | -11.19 [-13.42, -7.80] | -41.60 [-43.64, -38.26] | -25.79 [-28.00, -23.68] | 0.00 [0.00, 0.00] |
| main rule | 0.53 [0.46, 0.59] | 13285 [12318, 13907] | -28273 [-41162, -16643] | -0.16 [-0.31, 0.03] | -10.93 [-13.38, -7.51] | -41.41 [-43.54, -38.26] | -26.26 [-28.46, -23.88] | 0.00 [-0.00, 0.01] |
| sale discount 0.034 | 0.53 [0.46, 0.59] | 13285 [12319, 13908] | -28426 [-41317, -16630] | -0.16 [-0.31, 0.04] | -10.95 [-13.38, -7.51] | -41.41 [-43.54, -38.26] | -26.40 [-28.82, -24.24] | 0.00 [-0.00, 0.01] |
| sale discount 0.062 | 0.53 [0.46, 0.59] | 13287 [12321, 13912] | -28577 [-41265, -16652] | -0.16 [-0.33, 0.04] | -10.95 [-13.38, -7.51] | -41.41 [-43.54, -38.26] | -26.60 [-28.84, -24.28] | 0.00 [-0.00, 0.01] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | -0.20 [-0.35, -0.08] | -0.01 [-0.04, 0.01] | 0.51 [-0.24, 1.42] | 0.04 [-0.20, 0.40] |
| sale discount 0.034 | -0.20 [-0.35, -0.06] | -0.01 [-0.04, 0.01] | 0.66 [-0.24, 1.44] | 0.05 [-0.20, 0.40] |
| sale discount 0.062 | -0.20 [-0.35, -0.06] | -0.01 [-0.04, 0.01] | 0.86 [-0.24, 2.06] | 0.05 [-0.20, 0.40] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.53 | 0.53 (main rule) | 0.53 (sale discount 0.034) | 3 of 3 |
| E P2 | 13285 | 13285 (main rule) | 13287 (sale discount 0.062) | 3 of 3 |
| E P3 | -28273 | -28577 (sale discount 0.062) | -28273 (main rule) | 3 of 3 |
| E P4 | -0.16 | -0.16 (main rule) | -0.16 (sale discount 0.062) | 3 of 3 |
| E P5 | -10.93 | -10.95 (sale discount 0.034) | -10.93 (main rule) | 3 of 3 |
| E basket pov. | -41.41 | -41.41 (sale discount 0.062) | -41.41 (main rule) | 3 of 3 |
| E wealth pov. | -26.26 | -26.60 (sale discount 0.062) | -26.26 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.034) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | - | 40.20 (38.20 to 43.28) | 21.40 (18.54 to 23.82) |
| 1 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | 4.14 (3.82 to 4.40) | 42.00 (38.58 to 45.18) | 8.20 (6.96 to 10.84) |
| 2 | 2.97 (2.67 to 2.97) | 6.04 (5.24 to 6.35) | 3.01 (2.82 to 3.22) | 41.70 (38.52 to 46.74) | 3.20 (2.56 to 3.80) |
| 3 | 2.97 (0.00 to 2.97) | 4.35 (0.00 to 4.62) | 2.34 (2.19 to 2.45) | 42.60 (38.98 to 50.72) | 8.00 (6.98 to 10.24) |
| 4 | 2.97 (0.00 to 2.97) | 3.44 (0.00 to 3.65) | 1.81 (1.74 to 1.91) | 42.60 (38.44 to 46.52) | 4.10 (3.18 to 4.88) |
| 5 | 2.97 (0.00 to 2.97) | 2.64 (0.00 to 2.78) | 2.15 (2.00 to 2.30) | 43.90 (38.60 to 47.74) | 6.20 (4.98 to 7.44) |
| 6 | 2.97 (0.00 to 2.97) | 3.18 (0.00 to 3.42) | 1.95 (1.87 to 2.22) | 44.70 (40.00 to 47.38) | 3.70 (2.60 to 5.02) |
| 7 | 2.97 (0.00 to 2.97) | 2.85 (0.00 to 3.14) | 2.04 (1.95 to 2.11) | 43.90 (39.96 to 48.28) | 4.20 (3.00 to 5.22) |
| 8 | 2.97 (0.00 to 2.97) | 2.98 (0.00 to 3.13) | 1.98 (1.94 to 2.16) | 43.40 (38.96 to 46.16) | 2.50 (1.98 to 3.80) |
| 9 | 2.97 (2.97 to 2.97) | 2.94 (2.80 to 3.20) | 2.04 (1.94 to 2.20) | 43.70 (39.88 to 49.84) | 2.50 (1.96 to 3.60) |
| 10 | 2.97 (0.00 to 2.97) | 3.01 (0.00 to 3.28) | 2.02 (2.00 to 2.20) | 45.50 (40.34 to 51.06) | 2.20 (1.40 to 2.82) |
| 11 | 2.97 (0.00 to 2.97) | 3.00 (0.00 to 3.20) | 2.01 (1.99 to 2.11) | 46.40 (42.84 to 51.68) | 2.20 (1.60 to 2.64) |
| 12 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.98 to 2.05) | 46.80 (43.52 to 50.50) | 1.80 (1.58 to 2.62) |
| 13 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.05) | 47.40 (43.88 to 53.62) | 1.80 (1.20 to 2.80) |
| 14 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 3.03) | 2.00 (1.97 to 2.02) | 47.10 (44.40 to 53.68) | 1.50 (1.18 to 2.46) |
| 15 | 2.97 (0.00 to 2.97) | 2.96 (0.00 to 2.99) | 2.00 (1.99 to 2.03) | 49.00 (44.00 to 52.12) | 1.50 (0.98 to 2.04) |
| 16 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 3.02) | 2.00 (1.99 to 2.01) | 48.80 (43.96 to 53.58) | 1.40 (1.18 to 2.26) |
| 17 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.01) | 48.10 (46.14 to 53.02) | 1.30 (1.00 to 2.00) |
| 18 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.01) | 48.60 (46.52 to 52.40) | 1.20 (0.98 to 2.02) |
| 19 | 2.97 (2.97 to 2.97) | 2.97 (2.96 to 2.99) | 2.00 (2.00 to 2.01) | 48.80 (46.98 to 51.28) | 1.20 (0.60 to 1.66) |

### release design

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 2.59 [2.35, 2.84] | 16.00 [10.00, 25.00] | 26.71 [25.78, 29.50] | -0.39 [-0.63, -0.23] | 0.00 [0.00, 0.00] | 22.83 / 9.18 |
| sale discount 0.034 | 2.59 [2.35, 2.84] | 16.00 [10.00, 25.00] | 26.72 [25.82, 29.50] | -0.39 [-0.63, -0.23] | 0.00 [0.00, 0.00] | 22.77 / 9.15 |
| sale discount 0.062 | 2.59 [2.35, 2.84] | 16.00 [10.00, 25.00] | 26.72 [25.87, 29.48] | -0.39 [-0.63, -0.23] | 0.00 [0.00, 0.00] | 22.70 / 9.12 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.42 [0.37, 0.47] | 2167 [1799, 2592] | -208.89 [-866.75, -0.00] | 0.37 [0.16, 0.62] | -5.33 [-8.02, -3.06] | -19.38 [-21.41, -16.70] | -12.35 [-13.84, -10.80] | 0.00 [0.00, 0.00] |
| main rule | 0.42 [0.37, 0.47] | 2133 [1741, 2567] | -12161 [-20568, -5354] | 0.32 [0.17, 0.54] | -5.17 [-7.89, -2.83] | -19.30 [-21.37, -16.58] | -12.69 [-14.40, -11.40] | 0.00 [-0.00, 0.01] |
| sale discount 0.034 | 0.42 [0.37, 0.47] | 2133 [1742, 2568] | -12137 [-20609, -5301] | 0.33 [0.17, 0.55] | -5.18 [-7.89, -2.83] | -19.30 [-21.38, -16.58] | -12.79 [-14.42, -11.58] | 0.00 [-0.00, 0.01] |
| sale discount 0.062 | 0.42 [0.37, 0.47] | 2134 [1742, 2569] | -12276 [-20631, -5264] | 0.33 [0.16, 0.55] | -5.19 [-7.89, -2.83] | -19.31 [-21.38, -16.58] | -12.91 [-14.60, -11.56] | 0.00 [-0.00, 0.01] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | -0.20 [-0.35, -0.08] | -0.12 [-0.25, -0.03] | 0.51 [-0.24, 1.42] | 0.17 [-1.00, 0.82] |
| sale discount 0.034 | -0.20 [-0.35, -0.06] | -0.12 [-0.25, -0.03] | 0.66 [-0.24, 1.44] | 0.22 [-1.00, 1.02] |
| sale discount 0.062 | -0.20 [-0.35, -0.06] | -0.12 [-0.25, -0.03] | 0.86 [-0.24, 2.06] | 0.30 [-1.00, 1.22] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.42 | 0.42 (main rule) | 0.42 (sale discount 0.062) | 3 of 3 |
| E P2 | 2133 | 2133 (main rule) | 2134 (sale discount 0.062) | 3 of 3 |
| E P3 | -12161 | -12276 (sale discount 0.062) | -12137 (sale discount 0.034) | 3 of 3 |
| E P4 | 0.32 | 0.32 (main rule) | 0.33 (sale discount 0.062) | 3 of 3 |
| E P5 | -5.17 | -5.19 (sale discount 0.062) | -5.17 (main rule) | 3 of 3 |
| E basket pov. | -19.30 | -19.31 (sale discount 0.062) | -19.30 (main rule) | 3 of 3 |
| E wealth pov. | -12.69 | -12.91 (sale discount 0.062) | -12.69 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.062) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | - | 40.20 (38.20 to 43.28) | 29.60 (27.58 to 32.22) |
| 1 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | 3.26 (3.04 to 3.37) | 42.00 (38.58 to 45.18) | 17.90 (16.00 to 21.02) |
| 2 | 2.97 (2.67 to 2.97) | 4.80 (3.99 to 4.99) | 3.13 (2.94 to 3.38) | 41.70 (38.52 to 46.74) | 18.00 (16.40 to 21.04) |
| 3 | 2.97 (0.00 to 2.97) | 4.57 (0.03 to 4.91) | 2.11 (1.95 to 2.31) | 42.60 (38.98 to 50.72) | 21.70 (19.96 to 24.54) |
| 4 | 2.97 (0.00 to 2.97) | 3.08 (0.00 to 3.30) | 1.76 (1.64 to 1.86) | 42.60 (38.44 to 46.52) | 21.10 (18.20 to 23.22) |
| 5 | 2.97 (0.00 to 2.97) | 2.55 (0.00 to 2.74) | 2.01 (1.89 to 2.16) | 43.90 (38.60 to 47.74) | 23.50 (20.36 to 25.42) |
| 6 | 2.97 (0.00 to 2.97) | 2.91 (0.00 to 3.22) | 1.90 (1.76 to 2.14) | 44.70 (40.00 to 47.38) | 22.60 (20.44 to 24.24) |
| 7 | 2.97 (0.00 to 2.97) | 2.76 (0.00 to 3.05) | 2.06 (1.93 to 2.18) | 43.90 (39.96 to 48.28) | 25.00 (21.96 to 27.04) |
| 8 | 2.97 (0.00 to 2.97) | 3.01 (0.00 to 3.21) | 1.87 (1.76 to 2.01) | 43.40 (38.96 to 46.16) | 24.80 (21.40 to 26.24) |
| 9 | 2.97 (2.97 to 2.97) | 2.74 (2.43 to 2.92) | 1.94 (1.85 to 2.11) | 43.70 (39.88 to 49.84) | 25.70 (23.26 to 28.40) |
| 10 | 2.97 (0.00 to 2.97) | 2.86 (0.00 to 3.13) | 1.93 (1.75 to 2.13) | 45.50 (40.34 to 51.06) | 26.80 (24.78 to 28.22) |
| 11 | 2.97 (0.00 to 2.97) | 2.78 (0.00 to 3.12) | 2.00 (1.91 to 2.11) | 46.40 (42.84 to 51.68) | 27.30 (23.58 to 29.40) |
| 12 | 2.97 (0.00 to 2.97) | 2.89 (0.00 to 3.06) | 1.99 (1.84 to 2.15) | 46.80 (43.52 to 50.50) | 27.20 (25.38 to 29.72) |
| 13 | 2.97 (0.00 to 2.97) | 2.89 (0.00 to 3.04) | 1.97 (1.76 to 2.19) | 47.40 (43.88 to 53.62) | 28.30 (26.00 to 30.82) |
| 14 | 2.97 (0.00 to 2.97) | 2.79 (0.00 to 3.15) | 1.93 (1.85 to 2.10) | 47.10 (44.40 to 53.68) | 29.50 (27.00 to 31.62) |
| 15 | 2.97 (0.00 to 2.97) | 2.77 (0.00 to 3.07) | 1.91 (1.75 to 2.06) | 49.00 (44.00 to 52.12) | 30.20 (28.00 to 32.26) |
| 16 | 2.97 (0.00 to 2.97) | 2.79 (0.00 to 3.07) | 1.94 (1.77 to 2.16) | 48.80 (43.96 to 53.58) | 30.60 (28.04 to 33.16) |
| 17 | 2.97 (0.00 to 2.97) | 2.80 (0.00 to 3.09) | 2.00 (1.81 to 2.16) | 48.10 (46.14 to 53.02) | 31.40 (28.58 to 34.42) |
| 18 | 2.97 (0.00 to 2.97) | 2.86 (0.00 to 3.21) | 1.87 (1.73 to 2.10) | 48.60 (46.52 to 52.40) | 31.70 (29.90 to 34.24) |
| 19 | 2.97 (2.97 to 2.97) | 2.76 (2.54 to 3.12) | 1.97 (1.85 to 2.16) | 48.80 (46.98 to 51.28) | 32.00 (29.74 to 34.00) |

## Stress

Engine: e5649efec5160cb34abdb101d2cddc52cd992d28; command `node dev/tools/s74_sweep.js st 20 --only=off,main,fd0.034,fd0.062 --out=/home/user/runs/s77-fd`; 20 seeds; 4 settings.

### C2.2

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.36 [24.17, 27.07] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.83 / 1.15 |
| sale discount 0.034 | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.36 [24.17, 27.10] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.77 / 1.14 |
| sale discount 0.062 | 2.72 [2.45, 2.95] | 15.75 [10.00, 25.00] | 24.36 [24.17, 27.14] | -0.37 [-0.61, -0.21] | 0.00 [0.00, 0.00] | 22.70 / 1.14 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.53 [0.45, 0.59] | 9190 [8506, 10147] | -208.89 [-866.75, -0.00] | 0.13 [-0.10, 0.36] | -10.74 [-13.00, -7.58] | -41.13 [-43.35, -37.82] | -25.35 [-27.46, -23.44] | 0.00 [0.00, 0.00] |
| main rule | 0.53 [0.46, 0.59] | 9136 [8435, 10012] | -25499 [-36718, -14810] | 0.09 [-0.10, 0.29] | -10.51 [-12.94, -7.44] | -40.94 [-43.25, -37.82] | -25.85 [-27.86, -23.48] | 0.00 [-0.00, 0.01] |
| sale discount 0.034 | 0.53 [0.46, 0.59] | 9136 [8435, 10012] | -25653 [-36855, -14791] | 0.10 [-0.10, 0.31] | -10.53 [-12.94, -7.44] | -40.94 [-43.25, -37.82] | -26.00 [-28.22, -23.84] | 0.00 [-0.00, 0.01] |
| sale discount 0.062 | 0.53 [0.46, 0.59] | 9136 [8435, 10013] | -25807 [-36804, -14816] | 0.10 [-0.10, 0.34] | -10.53 [-12.94, -7.44] | -40.94 [-43.26, -37.82] | -26.19 [-28.24, -23.88] | 0.00 [-0.00, 0.01] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | -0.20 [-0.35, -0.08] | -0.01 [-0.04, 0.00] | 0.51 [-0.24, 1.42] | 0.01 [-0.02, 0.20] |
| sale discount 0.034 | -0.20 [-0.35, -0.06] | -0.01 [-0.04, 0.01] | 0.66 [-0.24, 1.44] | 0.01 [-0.02, 0.20] |
| sale discount 0.062 | -0.20 [-0.35, -0.06] | -0.01 [-0.04, 0.01] | 0.86 [-0.24, 2.06] | 0.02 [-0.02, 0.20] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.53 | 0.53 (main rule) | 0.53 (sale discount 0.034) | 3 of 3 |
| E P2 | 9136 | 9136 (sale discount 0.034) | 9136 (main rule) | 3 of 3 |
| E P3 | -25499 | -25807 (sale discount 0.062) | -25499 (main rule) | 3 of 3 |
| E P4 | 0.09 | 0.09 (main rule) | 0.10 (sale discount 0.062) | 3 of 3 |
| E P5 | -10.51 | -10.53 (sale discount 0.034) | -10.51 (main rule) | 3 of 3 |
| E basket pov. | -40.94 | -40.94 (sale discount 0.062) | -40.94 (main rule) | 3 of 3 |
| E wealth pov. | -25.85 | -26.19 (sale discount 0.062) | -25.85 (main rule) | 3 of 3 |
| X P1 | 0.00 | 0.00 (main rule) | 0.00 (sale discount 0.034) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | - | 40.20 (38.20 to 43.28) | 21.70 (18.58 to 24.20) |
| 1 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | 4.12 (3.80 to 4.38) | 42.00 (38.58 to 45.18) | 9.00 (7.40 to 11.62) |
| 2 | 2.97 (2.67 to 2.97) | 6.02 (5.20 to 6.34) | 3.01 (2.83 to 3.20) | 41.70 (38.52 to 46.74) | 3.60 (2.76 to 4.02) |
| 3 | 2.97 (0.00 to 2.97) | 4.34 (0.00 to 4.63) | 2.35 (2.22 to 2.47) | 42.60 (38.98 to 50.72) | 8.40 (7.38 to 10.06) |
| 4 | 2.97 (0.00 to 2.97) | 3.45 (0.00 to 3.67) | 1.80 (1.75 to 1.92) | 42.60 (38.44 to 46.52) | 3.80 (2.98 to 4.42) |
| 5 | 2.97 (0.00 to 2.97) | 2.66 (0.00 to 2.80) | 2.17 (2.02 to 2.30) | 43.90 (38.60 to 47.74) | 6.10 (4.76 to 7.30) |
| 6 | 2.97 (0.00 to 2.97) | 3.20 (0.00 to 3.42) | 1.95 (1.86 to 2.22) | 44.70 (40.00 to 47.38) | 3.20 (2.20 to 4.40) |
| 7 | 2.97 (0.00 to 2.97) | 2.85 (0.00 to 3.13) | 2.05 (1.96 to 2.13) | 43.90 (39.96 to 48.28) | 4.20 (3.38 to 5.40) |
| 8 | 2.97 (0.00 to 2.97) | 3.00 (0.00 to 3.15) | 1.98 (1.91 to 2.15) | 43.40 (38.96 to 46.16) | 3.10 (2.56 to 4.04) |
| 9 | 2.97 (2.97 to 2.97) | 2.93 (2.74 to 3.19) | 2.04 (1.94 to 2.19) | 43.70 (39.88 to 49.84) | 3.60 (2.80 to 4.62) |
| 10 | 2.97 (0.00 to 2.97) | 3.00 (0.00 to 3.26) | 2.00 (1.98 to 2.18) | 45.50 (40.34 to 51.06) | 3.20 (2.60 to 3.82) |
| 11 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 3.19) | 2.01 (1.99 to 2.11) | 46.40 (42.84 to 51.68) | 3.10 (2.00 to 4.80) |
| 12 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 3.00) | 2.00 (1.97 to 2.05) | 46.80 (43.52 to 50.50) | 2.80 (1.78 to 3.62) |
| 13 | 2.97 (0.00 to 2.97) | 2.95 (0.00 to 3.01) | 2.02 (2.00 to 2.05) | 47.40 (43.88 to 53.62) | 2.50 (1.78 to 3.00) |
| 14 | 2.97 (0.00 to 2.97) | 2.99 (0.00 to 3.04) | 2.01 (1.98 to 2.03) | 47.10 (44.40 to 53.68) | 2.20 (1.78 to 3.20) |
| 15 | 2.97 (0.00 to 2.97) | 2.95 (0.00 to 3.01) | 2.00 (1.98 to 2.03) | 49.00 (44.00 to 52.12) | 2.10 (1.60 to 2.82) |
| 16 | 2.97 (0.00 to 2.97) | 2.96 (0.00 to 3.02) | 2.00 (1.98 to 2.02) | 48.80 (43.96 to 53.58) | 2.00 (1.60 to 3.02) |
| 17 | 2.97 (0.00 to 2.97) | 2.96 (0.00 to 2.99) | 2.00 (1.98 to 2.02) | 48.10 (46.14 to 53.02) | 2.10 (1.20 to 2.82) |
| 18 | 2.97 (0.00 to 2.97) | 2.97 (0.00 to 2.99) | 2.00 (1.99 to 2.01) | 48.60 (46.52 to 52.40) | 1.80 (1.38 to 2.82) |
| 19 | 2.97 (2.97 to 2.97) | 2.97 (2.96 to 2.99) | 2.00 (1.99 to 2.01) | 48.80 (46.98 to 51.28) | 1.90 (1.38 to 2.60) |

### release design

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 2.51 [2.25, 2.72] | 16.25 [10.00, 25.00] | 28.34 [25.43, 32.79] | -0.41 [-0.65, -0.25] | 0.00 [0.00, 0.00] | 22.83 / 16.83 |
| sale discount 0.034 | 2.51 [2.25, 2.72] | 16.25 [10.00, 25.00] | 28.37 [25.42, 32.82] | -0.41 [-0.65, -0.25] | 0.00 [0.00, 0.00] | 22.77 / 16.77 |
| sale discount 0.062 | 2.51 [2.25, 2.72] | 16.25 [10.00, 25.00] | 28.38 [25.33, 32.84] | -0.41 [-0.65, -0.25] | 0.00 [0.00, 0.00] | 22.70 / 16.72 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.24 [0.20, 0.28] | 437.14 [262.90, 649.90] | -208.89 [-866.75, -0.00] | 0.23 [0.05, 0.36] | -3.41 [-5.28, -1.58] | -7.80 [-8.96, -6.10] | -5.10 [-6.82, -3.18] | 0.00 [0.00, 0.00] |
| main rule | 0.24 [0.20, 0.29] | 414.92 [218.09, 596.19] | -4603 [-10179, 0.08] | 0.24 [0.09, 0.36] | -3.42 [-5.54, -1.88] | -7.75 [-8.96, -6.03] | -5.28 [-6.48, -4.16] | 0.01 [-0.01, 0.02] |
| sale discount 0.034 | 0.24 [0.20, 0.29] | 415.64 [219.14, 595.75] | -4462 [-10779, -173.08] | 0.25 [0.11, 0.37] | -3.43 [-5.40, -1.88] | -7.75 [-8.97, -6.03] | -5.33 [-6.52, -4.16] | 0.01 [-0.01, 0.02] |
| sale discount 0.062 | 0.24 [0.20, 0.29] | 415.91 [218.31, 597.19] | -4514 [-11065, -213.80] | 0.25 [0.11, 0.37] | -3.43 [-5.40, -1.88] | -7.75 [-8.97, -6.03] | -5.38 [-6.88, -4.16] | 0.01 [-0.01, 0.02] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | -0.20 [-0.35, -0.08] | -0.16 [-0.31, -0.02] | 0.51 [-0.24, 1.42] | 0.33 [-0.48, 1.42] |
| sale discount 0.034 | -0.20 [-0.35, -0.06] | -0.15 [-0.31, -0.02] | 0.66 [-0.24, 1.44] | 0.43 [-0.30, 1.42] |
| sale discount 0.062 | -0.20 [-0.35, -0.06] | -0.16 [-0.31, -0.02] | 0.86 [-0.24, 2.06] | 0.58 [-0.30, 1.42] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.24 | 0.24 (main rule) | 0.24 (sale discount 0.062) | 3 of 3 |
| E P2 | 414.92 | 414.92 (main rule) | 415.91 (sale discount 0.062) | 3 of 3 |
| E P3 | -4603 | -4603 (main rule) | -4462 (sale discount 0.034) | 3 of 3 |
| E P4 | 0.24 | 0.24 (main rule) | 0.25 (sale discount 0.062) | 3 of 3 |
| E P5 | -3.42 | -3.43 (sale discount 0.062) | -3.42 (main rule) | 3 of 3 |
| E basket pov. | -7.75 | -7.75 (sale discount 0.062) | -7.75 (main rule) | 3 of 3 |
| E wealth pov. | -5.28 | -5.38 (sale discount 0.062) | -5.28 (main rule) | 3 of 3 |
| X P1 | 0.01 | 0.01 (main rule) | 0.01 (sale discount 0.062) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | - | 40.20 (38.20 to 43.28) | 37.60 (34.86 to 38.62) |
| 1 | 2.97 (2.97 to 2.97) | 2.97 (2.97 to 2.97) | 2.49 (2.36 to 2.61) | 42.00 (38.58 to 45.18) | 31.90 (29.20 to 34.48) |
| 2 | 2.97 (2.67 to 2.97) | 3.65 (3.12 to 3.89) | 2.62 (2.49 to 2.70) | 41.70 (38.52 to 46.74) | 32.80 (30.80 to 37.22) |
| 3 | 2.97 (0.00 to 2.97) | 3.89 (0.00 to 3.99) | 1.96 (1.84 to 2.07) | 42.60 (38.98 to 50.72) | 34.70 (30.36 to 37.60) |
| 4 | 2.97 (0.00 to 2.97) | 2.89 (0.00 to 3.03) | 1.93 (1.86 to 2.05) | 42.60 (38.44 to 46.52) | 34.20 (30.54 to 37.34) |
| 5 | 2.97 (0.00 to 2.97) | 2.85 (0.00 to 2.99) | 1.94 (1.83 to 2.08) | 43.90 (38.60 to 47.74) | 35.30 (32.46 to 36.72) |
| 6 | 2.97 (0.00 to 2.97) | 2.84 (0.00 to 3.09) | 2.01 (1.87 to 2.16) | 44.70 (40.00 to 47.38) | 35.60 (31.36 to 39.12) |
| 7 | 2.97 (0.00 to 2.97) | 2.89 (0.00 to 3.21) | 2.02 (1.88 to 2.20) | 43.90 (39.96 to 48.28) | 35.80 (33.74 to 39.48) |
| 8 | 2.97 (0.00 to 2.97) | 2.98 (0.00 to 3.18) | 1.94 (1.83 to 2.06) | 43.40 (38.96 to 46.16) | 35.50 (33.20 to 38.28) |
| 9 | 2.97 (2.97 to 2.97) | 2.87 (2.68 to 3.05) | 1.95 (1.86 to 2.11) | 43.70 (39.88 to 49.84) | 35.60 (33.94 to 40.64) |
| 10 | 2.97 (0.00 to 2.97) | 2.87 (0.00 to 3.09) | 1.93 (1.76 to 2.08) | 45.50 (40.34 to 51.06) | 37.80 (34.20 to 40.80) |
| 11 | 2.97 (0.00 to 2.97) | 2.82 (0.00 to 3.04) | 1.97 (1.83 to 2.10) | 46.40 (42.84 to 51.68) | 38.00 (34.98 to 41.46) |
| 12 | 2.97 (0.00 to 2.97) | 2.82 (0.00 to 3.05) | 1.91 (1.81 to 2.11) | 46.80 (43.52 to 50.50) | 39.90 (36.14 to 42.24) |
| 13 | 2.97 (0.00 to 2.97) | 2.81 (0.00 to 3.06) | 1.95 (1.75 to 2.31) | 47.40 (43.88 to 53.62) | 39.60 (36.80 to 43.56) |
| 14 | 2.97 (0.00 to 2.97) | 2.69 (0.00 to 3.05) | 1.96 (1.72 to 2.16) | 47.10 (44.40 to 53.68) | 40.90 (37.38 to 43.94) |
| 15 | 2.97 (0.00 to 2.97) | 2.76 (0.00 to 3.05) | 1.91 (1.57 to 2.03) | 49.00 (44.00 to 52.12) | 40.90 (37.90 to 44.84) |
| 16 | 2.97 (0.00 to 2.97) | 2.78 (0.00 to 3.01) | 2.03 (1.81 to 2.20) | 48.80 (43.96 to 53.58) | 41.00 (39.30 to 45.40) |
| 17 | 2.97 (0.00 to 2.97) | 2.86 (0.00 to 3.18) | 1.98 (1.63 to 2.23) | 48.10 (46.14 to 53.02) | 41.40 (39.18 to 44.58) |
| 18 | 2.97 (0.00 to 2.97) | 2.85 (0.00 to 3.31) | 1.94 (1.69 to 2.22) | 48.60 (46.52 to 52.40) | 41.90 (38.76 to 44.52) |
| 19 | 2.97 (2.97 to 2.97) | 2.79 (2.50 to 3.30) | 1.98 (1.84 to 2.16) | 48.80 (46.98 to 51.28) | 41.90 (39.98 to 44.82) |

## Reference

Engine: e5649efec5160cb34abdb101d2cddc52cd992d28; command `node dev/tools/s74_sweep.js ref 20 --only=off,main,fd0.034,fd0.062 --out=/home/user/runs/s77-fd`; 20 seeds; 4 settings.

### C2.2

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 0.30 [0.27, 0.34] | 56.25 [49.50, 65.00] | 5.53 [3.92, 7.35] | 0.04 [0.03, 0.04] | 0.00 [0.00, 0.00] | 18.68 / 0.94 |
| sale discount 0.034 | 0.30 [0.27, 0.34] | 56.00 [49.50, 65.00] | 5.51 [3.95, 7.30] | 0.04 [0.03, 0.04] | 0.00 [0.00, 0.00] | 18.62 / 0.93 |
| sale discount 0.062 | 0.30 [0.27, 0.34] | 55.75 [49.50, 65.00] | 5.52 [3.95, 7.36] | 0.04 [0.03, 0.04] | 0.00 [0.00, 0.00] | 18.59 / 0.93 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.54 [0.48, 0.60] | 13902 [12731, 14932] | -61.39 [-57.63, 0.00] | -0.40 [-0.55, -0.25] | 0.00 [0.00, 0.00] | -32.80 [-35.38, -30.84] | -22.40 [-24.44, -19.98] | 0.00 [0.00, 0.00] |
| main rule | 0.54 [0.47, 0.60] | 13904 [12713, 14947] | -210.05 [-575.27, 0.00] | -0.42 [-0.58, -0.27] | 0.00 [0.00, 0.00] | -32.87 [-35.47, -30.86] | -23.97 [-25.84, -22.14] | -0.00 [-0.00, -0.00] |
| sale discount 0.034 | 0.54 [0.47, 0.60] | 13903 [12710, 14948] | -209.85 [-575.01, 0.00] | -0.42 [-0.58, -0.28] | 0.00 [0.00, 0.00] | -32.88 [-35.46, -30.87] | -24.02 [-25.66, -22.14] | -0.00 [-0.00, 0.00] |
| sale discount 0.062 | 0.54 [0.47, 0.60] | 13905 [12729, 14949] | -209.72 [-574.28, 0.00] | -0.42 [-0.58, -0.27] | 0.00 [0.00, 0.00] | -32.88 [-35.47, -30.88] | -24.14 [-26.02, -22.14] | -0.00 [-0.00, 0.00] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | 0.07 [0.03, 0.11] | 0.00 [-0.00, 0.00] | 1.60 [0.96, 2.20] | 0.03 [0.00, 0.20] |
| sale discount 0.034 | 0.08 [0.03, 0.12] | 0.00 [0.00, 0.00] | 1.66 [1.14, 2.20] | 0.04 [0.00, 0.20] |
| sale discount 0.062 | 0.08 [0.03, 0.12] | -0.00 [-0.00, 0.00] | 1.79 [1.14, 2.22] | 0.05 [0.00, 0.20] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.54 | 0.54 (sale discount 0.062) | 0.54 (main rule) | 3 of 3 |
| E P2 | 13904 | 13903 (sale discount 0.034) | 13905 (sale discount 0.062) | 3 of 3 |
| E P3 | -210.05 | -210.05 (main rule) | -209.72 (sale discount 0.062) | 3 of 3 |
| E P4 | -0.42 | -0.42 (sale discount 0.034) | -0.42 (main rule) | 3 of 3 |
| E P5 | 0.00 | 0.00 (main rule) | 0.00 (main rule) | 3 of 3 |
| E basket pov. | -32.87 | -32.88 (sale discount 0.062) | -32.87 (main rule) | 3 of 3 |
| E wealth pov. | -23.97 | -24.14 (sale discount 0.062) | -23.97 (main rule) | 3 of 3 |
| X P1 | -0.00 | -0.00 (sale discount 0.062) | -0.00 (main rule) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | - | 40.20 (38.20 to 43.28) | 21.40 (18.54 to 23.82) |
| 1 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | 2.10 (1.78 to 2.35) | 40.40 (38.20 to 44.06) | 7.80 (6.60 to 9.94) |
| 2 | 0.00 (0.00 to 0.00) | 3.12 (2.64 to 3.50) | 0.90 (0.75 to 1.09) | 39.80 (37.00 to 45.02) | 3.10 (2.54 to 3.84) |
| 3 | 0.00 (0.00 to 0.00) | 1.32 (1.10 to 1.61) | 0.32 (0.13 to 0.49) | 40.10 (34.32 to 44.08) | 7.90 (6.60 to 9.62) |
| 4 | 0.00 (0.00 to 0.00) | 0.45 (0.17 to 0.70) | -0.21 (-0.37 to -0.08) | 39.10 (34.58 to 42.18) | 3.70 (3.00 to 4.64) |
| 5 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | 0.20 (-0.05 to 0.30) | 38.00 (35.42 to 43.06) | 5.80 (4.78 to 7.20) |
| 6 | 0.00 (0.00 to 0.00) | 0.27 (0.00 to 0.42) | -0.08 (-0.26 to 0.09) | 37.50 (33.72 to 42.24) | 3.50 (2.40 to 4.22) |
| 7 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.10) | -0.06 (-0.18 to 0.09) | 37.30 (34.24 to 40.28) | 4.00 (2.80 to 4.62) |
| 8 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.11) | -0.04 (-0.12 to 0.15) | 36.30 (33.18 to 39.86) | 2.40 (1.80 to 3.62) |
| 9 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.20) | 0.07 (-0.16 to 0.18) | 35.50 (31.76 to 40.62) | 2.40 (1.58 to 3.22) |
| 10 | 0.00 (0.00 to 0.00) | 0.08 (0.00 to 0.24) | -0.00 (-0.09 to 0.25) | 35.70 (33.10 to 40.66) | 2.00 (1.58 to 2.62) |
| 11 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.35) | -0.03 (-0.20 to 0.12) | 35.50 (31.74 to 39.28) | 2.00 (1.40 to 2.82) |
| 12 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.15) | -0.03 (-0.23 to 0.13) | 35.80 (32.88 to 38.72) | 1.60 (1.20 to 2.20) |
| 13 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.16) | 0.02 (-0.23 to 0.22) | 34.50 (32.20 to 37.28) | 1.40 (1.18 to 2.42) |
| 14 | 0.00 (0.00 to 0.00) | 0.01 (0.00 to 0.30) | -0.06 (-0.25 to 0.09) | 35.30 (32.94 to 37.82) | 1.20 (0.98 to 2.00) |
| 15 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.11) | 0.07 (-0.13 to 0.21) | 34.80 (32.74 to 36.42) | 1.30 (0.98 to 1.64) |
| 16 | 0.00 (0.00 to 0.00) | 0.08 (0.00 to 0.28) | -0.09 (-0.25 to 0.13) | 33.80 (32.36 to 36.48) | 1.20 (0.80 to 2.00) |
| 17 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.17) | -0.00 (-0.21 to 0.17) | 33.50 (31.98 to 35.82) | 1.00 (0.80 to 1.80) |
| 18 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.22) | -0.03 (-0.28 to 0.19) | 33.40 (31.78 to 36.20) | 0.80 (0.60 to 1.62) |
| 19 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.26) | -0.04 (-0.15 to 0.04) | 33.20 (31.40 to 35.60) | 0.90 (0.40 to 1.40) |

### release design

**The rule in each setting** (programme run; no-programme run after the slash where it differs in kind).

| setting | policy rate, mean (%) | years at the floor (%) | purchases, peak (% of GDP) | unemployment rise (points) | programme's own inflation (%) | forced sales (% of adult-years, no programme / programme) |
|---|---|---|---|---|---|---|
| no central bank | - | - | - | - | 0.00 [0.00, 0.00] | - |
| main rule | 0.23 [0.20, 0.26] | 52.50 [45.00, 60.00] | 4.78 [3.25, 6.09] | 0.03 [0.03, 0.03] | 0.00 [0.00, 0.00] | 18.68 / 5.09 |
| sale discount 0.034 | 0.23 [0.20, 0.26] | 52.50 [45.00, 60.00] | 4.77 [3.33, 6.08] | 0.03 [0.03, 0.03] | 0.00 [0.00, 0.00] | 18.62 / 5.07 |
| sale discount 0.062 | 0.23 [0.20, 0.26] | 53.50 [45.00, 60.00] | 4.75 [3.37, 6.01] | 0.03 [0.03, 0.03] | 0.00 [0.00, 0.00] | 18.59 / 5.05 |

**The programme's effect E in each setting**, and the interaction X on P1.

| setting | E P1 | E P2 | E P3 | E P4 | E P5 | E basket pov. | E wealth pov. | X P1 |
|---|---|---|---|---|---|---|---|---|
| no central bank | 0.39 [0.34, 0.45] | 2292 [1834, 2847] | -61.39 [-57.63, 0.00] | 0.24 [0.07, 0.43] | 0.00 [0.00, 0.00] | -21.20 [-24.09, -18.81] | -14.49 [-16.62, -12.80] | 0.00 [0.00, 0.00] |
| main rule | 0.39 [0.34, 0.45] | 2305 [1825, 2852] | -210.05 [-575.27, 0.00] | 0.22 [0.09, 0.38] | 0.00 [0.00, 0.00] | -21.21 [-24.11, -18.75] | -15.68 [-17.42, -14.18] | -0.00 [-0.00, 0.00] |
| sale discount 0.034 | 0.39 [0.34, 0.45] | 2304 [1824, 2852] | -209.85 [-575.01, 0.00] | 0.22 [0.09, 0.37] | 0.00 [0.00, 0.00] | -21.21 [-24.11, -18.76] | -15.68 [-17.40, -14.18] | -0.00 [-0.00, 0.00] |
| sale discount 0.062 | 0.39 [0.34, 0.45] | 2305 [1824, 2852] | -209.72 [-574.28, 0.00] | 0.22 [0.09, 0.40] | 0.00 [0.00, 0.00] | -21.21 [-24.11, -18.77] | -15.78 [-17.40, -14.18] | -0.00 [-0.00, 0.00] |

**The setting's effect C on poverty** (against no central bank; points).

| setting | C basket poverty, no programme | C basket poverty, programme | C wealth poverty, no programme | C wealth poverty, programme |
|---|---|---|---|---|
| main rule | 0.07 [0.03, 0.11] | 0.05 [0.02, 0.11] | 1.60 [0.96, 2.20] | 0.41 [0.00, 0.82] |
| sale discount 0.034 | 0.08 [0.03, 0.12] | 0.06 [0.02, 0.11] | 1.66 [1.14, 2.20] | 0.47 [0.00, 1.02] |
| sale discount 0.062 | 0.08 [0.03, 0.12] | 0.06 [0.02, 0.11] | 1.79 [1.14, 2.22] | 0.50 [0.00, 1.20] |

**Ranges across the 3 central-bank settings** (the mean E in each setting: the main rule's, the lowest and highest, and how many settings share the main rule's sign).

| outcome | main rule | lowest (setting) | highest (setting) | same sign as main |
|---|---|---|---|---|
| E P1 | 0.39 | 0.39 (sale discount 0.062) | 0.39 (main rule) | 3 of 3 |
| E P2 | 2305 | 2304 (sale discount 0.034) | 2305 (main rule) | 3 of 3 |
| E P3 | -210.05 | -210.05 (main rule) | -209.72 (sale discount 0.062) | 3 of 3 |
| E P4 | 0.22 | 0.22 (sale discount 0.034) | 0.22 (main rule) | 3 of 3 |
| E P5 | 0.00 | 0.00 (main rule) | 0.00 (main rule) | 3 of 3 |
| E basket pov. | -21.21 | -21.21 (sale discount 0.034) | -21.21 (main rule) | 3 of 3 |
| E wealth pov. | -15.68 | -15.78 (sale discount 0.062) | -15.68 (main rule) | 3 of 3 |
| X P1 | -0.00 | -0.00 (sale discount 0.062) | -0.00 (main rule) | 3 of 3 |

**Fan: main rule** (median across seeds, 10th to 90th percentile in brackets).

| year | policy rate, no programme | policy rate, programme | basket price change, programme | basket poverty, no programme | basket poverty, programme |
|---|---|---|---|---|---|
| 0 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | - | 40.20 (38.20 to 43.28) | 29.60 (27.58 to 32.22) |
| 1 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | 1.24 (1.02 to 1.34) | 40.40 (38.20 to 44.06) | 17.00 (15.60 to 19.84) |
| 2 | 0.00 (0.00 to 0.00) | 1.82 (1.50 to 1.98) | 1.09 (0.91 to 1.27) | 39.80 (37.00 to 45.02) | 16.20 (14.60 to 17.72) |
| 3 | 0.00 (0.00 to 0.00) | 1.61 (1.33 to 1.87) | 0.12 (0.07 to 0.38) | 40.10 (34.32 to 44.08) | 18.50 (16.18 to 20.10) |
| 4 | 0.00 (0.00 to 0.00) | 0.14 (0.08 to 0.53) | -0.19 (-0.32 to -0.08) | 39.10 (34.58 to 42.18) | 16.20 (14.20 to 18.42) |
| 5 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.00) | 0.14 (-0.04 to 0.23) | 38.00 (35.42 to 43.06) | 17.70 (15.14 to 19.04) |
| 6 | 0.00 (0.00 to 0.00) | 0.18 (0.00 to 0.31) | -0.04 (-0.25 to 0.05) | 37.50 (33.72 to 42.24) | 15.40 (12.78 to 17.88) |
| 7 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.04) | 0.03 (-0.13 to 0.13) | 37.30 (34.24 to 40.28) | 16.30 (13.96 to 18.44) |
| 8 | 0.00 (0.00 to 0.00) | 0.01 (0.00 to 0.16) | -0.07 (-0.16 to 0.05) | 36.30 (33.18 to 39.86) | 15.50 (12.98 to 17.28) |
| 9 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.04) | 0.02 (-0.15 to 0.18) | 35.50 (31.76 to 40.62) | 15.70 (13.12 to 17.50) |
| 10 | 0.00 (0.00 to 0.00) | 0.01 (0.00 to 0.24) | 0.06 (-0.11 to 0.26) | 35.70 (33.10 to 40.66) | 14.50 (12.56 to 16.22) |
| 11 | 0.00 (0.00 to 0.00) | 0.06 (0.00 to 0.35) | 0.08 (-0.07 to 0.21) | 35.50 (31.74 to 39.28) | 13.90 (12.46 to 15.66) |
| 12 | 0.00 (0.00 to 0.00) | 0.09 (0.00 to 0.29) | -0.00 (-0.18 to 0.17) | 35.80 (32.88 to 38.72) | 14.30 (11.98 to 16.22) |
| 13 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.23) | 0.01 (-0.12 to 0.19) | 34.50 (32.20 to 37.28) | 13.70 (11.40 to 15.60) |
| 14 | 0.00 (0.00 to 0.00) | 0.01 (0.00 to 0.26) | -0.06 (-0.18 to 0.07) | 35.30 (32.94 to 37.82) | 13.90 (11.96 to 15.00) |
| 15 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.07) | 0.07 (-0.09 to 0.24) | 34.80 (32.74 to 36.42) | 12.90 (11.14 to 15.40) |
| 16 | 0.00 (0.00 to 0.00) | 0.07 (0.00 to 0.33) | -0.04 (-0.25 to 0.12) | 33.80 (32.36 to 36.48) | 12.50 (11.14 to 14.30) |
| 17 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.16) | -0.03 (-0.16 to 0.18) | 33.50 (31.98 to 35.82) | 12.40 (10.96 to 14.04) |
| 18 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.25) | 0.00 (-0.20 to 0.17) | 33.40 (31.78 to 36.20) | 12.10 (10.58 to 13.84) |
| 19 | 0.00 (0.00 to 0.00) | 0.00 (0.00 to 0.22) | -0.04 (-0.13 to 0.07) | 33.20 (31.40 to 35.60) | 11.70 (10.60 to 13.82) |

