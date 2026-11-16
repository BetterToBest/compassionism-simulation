# S74 pilot tables (100 seeds, frozen round-2 main row)

Made by `node dev/tools/s74_table.js` from the pilot files in this folder (`node dev/tools/s74_pilot.js ENV 100`). Programme effect: programme minus no programme, paired on seeds. Interaction: the programme's effect with the central bank on minus with it off (History: off is no central bank). Intervals are 95% paired t; Holm-adjusted intervals (H) are across the five primary outcomes within each environment, design and family. For every primary outcome lower is steadier.

## History (2005-2025)

Engine: 3beb5ff7b009e177e296156cdcb33c819a15b2af; command `node dev/tools/s74_pilot.js hx 100 --out=/tmp/claude-0/-home-user-research-update/8aadb0ca-2bae-541c-b34b-c58ccfa7773f/scratchpad/s74fix`; 100 seeds.

### C2.2

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 1.76 | 1.84 | 0.08 [0.08, 0.09] | [0.08, 0.09] | less steady | 0.08 [0.08, 0.09] | -0.00 [-0.00, 0.00] | [-0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 20195 | 33264 | 13068 [12877, 13259] | [12816, 13321] | less steady | 13168 [12977, 13359] | -99.82 [-114.81, -84.84] | [-119.66, -79.99] |
| P3 largest fall in real wealth ($, median) | 58359 | 26608 | -31751 [-32345, -31158] (boot -32334, -31176) | [-32512, -30990] | steadier | -32193 [-32732, -31655] | 442.14 [-72.32, 956.60] | [-147.98, 1032] |
| P4 years to recover from an income shock (mean) | 3.40 | 3.08 | -0.33 [-0.36, -0.29] | [-0.36, -0.29] | steadier | -0.35 [-0.38, -0.31] | 0.02 [0.01, 0.04] | [0.00, 0.04] |
| P5 % pushed below the basket line in a recession year | 9.33 | 1.77 | -7.56 [-7.77, -7.36] (boot -7.77, -7.36) | [-7.82, -7.31] | steadier | -7.33 [-7.53, -7.14] | -0.23 [-0.28, -0.19] | [-0.29, -0.17] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -41.87 [-42.26, -41.48] | -41.48 [-41.87, -41.09] | 0.41 [0.38, 0.44] | 0.02 [0.01, 0.02] |
| pov | -28.17 [-28.54, -27.81] | -24.80 [-25.15, -24.45] | 3.56 [3.36, 3.76] | 0.18 [0.14, 0.22] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1o | -0.00 [-0.00, -0.00] | -0.00 [-0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.49 [0.48, 0.50] | 0.49 [0.48, 0.50] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP2q1 | 12506 [12105, 12908] | 12564 [12161, 12967] | 104.33 [86.33, 122.33] | 46.59 [30.69, 62.50] |
| stP2q3 | 13071 [12696, 13445] | 13115 [12744, 13486] | 167.02 [138.39, 195.66] | 122.43 [94.96, 149.90] |
| stP2q5 | 13523 [12992, 14054] | 13824 [13290, 14358] | 5423 [4619, 6227] | 5123 [4330, 5915] |
| stP3q1 | -3933 [-4137, -3729] | -3261 [-3477, -3046] | 784.65 [678.72, 890.59] | 112.96 [70.26, 155.66] |
| stP3q3 | -29944 [-31064, -28823] | -30100 [-31172, -29028] | 4914 [4107, 5721] | 5071 [4774, 5368] |
| stP3q5 | -23692 [-25601, -21782] | -23077 [-25948, -20205] | 254808 [237789, 271828] | 254194 [238250, 270137] |
| stP3t1 | -193096 [-238174, -148019] | -17991 [-23391, -12591] | 14797332 [10137055, 19457609] | 14622227 [9999144, 19245309] |
| stP5r | -6.96 [-7.17, -6.75] | 0.00 [0.00, 0.00] | 8.90 [8.70, 9.10] | 1.94 [1.86, 2.02] |
| rkRec3 | 9.03 [8.68, 9.39] | 10.44 [10.06, 10.82] | 2.46 [2.29, 2.63] | 1.05 [0.97, 1.14] |
| rkDdB | 4.85 [-2.10, 11.81] | -18.12 [-23.95, -12.29] | 15.15 [13.72, 16.58] | 38.12 [35.10, 41.15] |
| rkDdB30 | -6.14 [-6.62, -5.66] | -6.21 [-6.67, -5.75] | 1.70 [1.55, 1.84] | 1.77 [1.58, 1.96] |
| rkDdW | -7.77 [-7.92, -7.63] | -7.93 [-8.07, -7.79] | 1.16 [1.04, 1.27] | 1.32 [1.24, 1.39] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 3.55 | 3.79 |
| cbIst | 3.53 | 3.79 |
| cbFloor | 4.76 | 1.24 |
| cbQ | 0.62 | 0.07 |
| cbQmax | 4.36 | 0.49 |
| cbM | 0.70 | 0.70 |
| cbRfY | 2.00 | 1.98 |
| cbRfSh | 72.06 | 64.72 |
| cbU | 1.10 | 1.15 |
| cbA | 59316 | 58697 |
| cbN | 20527 | 39226 |
| cbF | -2026 | -318.49 |
| cbR | 3724 | 4102 |
| fsQ | 819.44 | 20.44 |
| fsN | 22.49 | 0.97 |
| fsRec | 30.08 | 38.50 |
| fsOut | 5.11 | 1.54 |
| fsBuyG | 15292 | 353.51 |
| fsGap | -0.00 | 0.00 |
| fsS0 | 0.01 | 0.03 |
| fsS1 | 8.72 | 40.29 |
| fsS2 | 47.96 | 51.76 |
| fsS3 | 39.20 | 7.92 |
| fsS4 | 4.11 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.74 | 3.06 |
| fsB1 | 1.61 | 4.42 |
| fsB2 | 3.63 | 8.39 |
| fsB3 | 9.43 | 14.15 |
| fsB4 | 18.53 | 18.72 |
| fsB5 | 40.41 | 33.20 |
| fsB6 | 24.65 | 18.07 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.49 points against 1.76 for outside inflation: the programme's own inflation is the smaller source here.

**History checks** (no-programme run, actual rate path; checked, not tuned).

| check | model | data | verdict |
|---|---|---|---|
| top 1% share of net worth, change (points) | 5.22 | 4.60 | matches |
| bottom 50% share, change (points) | -1.08 | -0.13 | same direction, different size |
| basket poverty, change 2005-2025 (points) vs official poverty | 10.37 | -2.40 | does not match |
| basket poverty vs anchored SPM (2005-2012) | 8.11 | 1.45 | same direction, different size |
| wealth poverty, change (points) vs official poverty | 2.18 | -2.40 | does not match |

**Who gains and who pays: no programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus no central bank; and cb minus the actual rate path, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | C vs actual path (95%) | asset prices | deposits | floating debt | refinancing (actual path) | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|---|
| poorest fifth | 1156 [1049, 1263] | 2210 [2075, 2345] | 80 | 2341 | -812 | 6 (5) | -2599 | 1123 | -2051 |
| second fifth | -4253 [-4622, -3884] | -396.72 [-727.22, -66.21] | -705 | 3109 | -2374 | 775 (630) | -3907 | 990 | -13117 |
| middle fifth | -14213 [-15009, -13417] | -7166 [-7816, -6517] | -919 | 5248 | -2933 | 2618 (2962) | -4385 | 2053 | -20516 |
| fourth fifth | 3015 [1782, 4248] | 7965 [6847, 9084] | 5730 | 11611 | -2385 | 5296 (7082) | -5177 | 5691 | -14567 |
| richest fifth | 383594 [352948, 414240] | 407967 [376063, 439870] | 295262 | 81088 | -1635 | 10019 (13436) | -5728 | 41610 | -1131 |
| top 1% | 9433709 [7163034, 11704384] | 9873681 [7508280, 12239082] | 8056693 | 1282849 | -3466 | 65767 (88199) | -10450 | 603345 | 0 |

**Who gains and who pays: programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus no central bank; and cb minus the actual rate path, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | C vs actual path (95%) | asset prices | deposits | floating debt | refinancing (actual path) | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|---|
| poorest fifth | 6139 [6011, 6268] | 11547 [11347, 11748] | 22 | 13739 | -93 | 2 (2) | -2901 | 85 | -401 |
| second fifth | 6605 [6374, 6835] | 12968 [12648, 13288] | -819 | 16800 | -220 | 460 (611) | -4057 | 94 | -760 |
| middle fifth | 10261 [9980, 10541] | 16856 [16510, 17203] | -513 | 21167 | -384 | 2422 (2863) | -4595 | 137 | -385 |
| fourth fifth | 24309 [23838, 24780] | 31846 [31276, 32417] | 6347 | 30737 | -339 | 6123 (6846) | -5457 | 242 | -192 |
| richest fifth | 353500 [323313, 383687] | 388839 [357192, 420486] | 291178 | 114636 | -561 | 11615 (12993) | -6120 | 1192 | 0 |
| top 1% | 8800772 [6645843, 10955701] | 9328707 [7063145, 11594268] | 7987946 | 1525018 | -3510 | 76328 (85321) | -10672 | 16265 | 0 |

**Wealth shares at the end** (the central bank's effect, cb minus no central bank or the actual rate path, points of net worth, paired, 95%; weighted tail).

| run | against | top 1% share | top 10% share | bottom 50% share |
|---|---|---|---|---|
| no programme | no central bank | 0.45 [0.44, 0.47] | 0.88 [0.85, 0.92] | -0.48 [-0.51, -0.45] |
| no programme | actual rate path | 0.36 [0.35, 0.37] | 0.72 [0.70, 0.75] | -0.32 [-0.34, -0.30] |
| programme | no central bank | 0.30 [0.28, 0.31] | 0.46 [0.45, 0.47] | -0.15 [-0.16, -0.15] |
| programme | actual rate path | 0.18 [0.17, 0.19] | 0.28 [0.27, 0.29] | -0.04 [-0.05, -0.04] |

**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme's effect, central bank on; E0 with it off.

| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |
|---|---|---|---|---|
| stP2s | 29.27 | 27.70 | -1.57 [-1.83, -1.30] | -1.11 [-1.39, -0.83] |
| stP2sq1 | 31.74 | 29.44 | -2.30 [-2.91, -1.69] | -1.79 [-2.39, -1.19] |
| stP2sq2 | 31.24 | 28.97 | -2.27 [-2.80, -1.74] | -1.70 [-2.27, -1.13] |
| stP2sq3 | 30.84 | 28.38 | -2.46 [-3.00, -1.92] | -1.97 [-2.51, -1.43] |
| stP2sq4 | 29.73 | 27.56 | -2.17 [-2.68, -1.66] | -1.85 [-2.35, -1.34] |
| stP2sq5 | 24.20 | 24.38 | 0.18 [-0.14, 0.51] | 1.28 [0.88, 1.68] |

**Each household's own inflation, 2006-2025** (% a year; its basket by household type, food, housing and medical care at their CPI-U components, the rest at CPI-U; no-programme run, actual rate path). CPI-U 2.537; all households 2.766 (10th-90th percentile 2.748 to 2.784); by fifth 2.771, 2.767, 2.764, 2.765, 2.764; top 1% 2.775. BLS's R-CPI-I check: dev/runs/s74-rcpi/rcpi.md (Amendment 3).

**Decision rule 3: does the central bank's response offset the programme's gain?** (programme run, central bank on minus no central bank, points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)

| outcome | C (95%) | C (Holm) | reading |
|---|---|---|---|
| basket poverty | 0.02 [0.01, 0.02] | [0.01, 0.02] | offsets part of the programme's gain |
| wealth poverty, last year | 0.18 [0.14, 0.22] | [0.12, 0.24] | offsets part of the programme's gain |
| wealth poverty, yearly average | -0.00 [-0.02, 0.01] | [-0.02, 0.01] | no measurable difference |

### release design

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 1.76 | 1.89 | 0.13 [0.12, 0.13] | [0.12, 0.13] | less steady | 0.12 [0.12, 0.13] | 0.00 [0.00, 0.00] | [0.00, 0.01] |
| P2 spread of yearly changes in real cash income ($, mean) | 20195 | 22800 | 2605 [2527, 2683] | [2502, 2708] | less steady | 2645 [2567, 2723] | -40.06 [-50.45, -29.67] | [-53.38, -26.74] |
| P3 largest fall in real wealth ($, median) | 58359 | 38915 | -19445 [-20078, -18811] (boot -20070, -18841) | [-20257, -18632] | steadier | -19803 [-20360, -19247] | 358.86 [-221.40, 939.13] | [-221.40, 939.13] |
| P4 years to recover from an income shock (mean) | 3.40 | 3.79 | 0.39 [0.36, 0.41] | [0.36, 0.41] | less steady | 0.46 [0.43, 0.49] | -0.08 [-0.09, -0.06] | [-0.10, -0.05] |
| P5 % pushed below the basket line in a recession year | 9.33 | 6.01 | -3.32 [-3.53, -3.11] (boot -3.53, -3.12) | [-3.56, -3.08] | steadier | -3.19 [-3.39, -2.98] | -0.13 [-0.18, -0.09] | [-0.19, -0.08] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -23.70 [-24.07, -23.32] | -23.54 [-23.92, -23.16] | 0.41 [0.38, 0.44] | 0.26 [0.23, 0.28] |
| pov | -16.46 [-16.86, -16.06] | -14.18 [-14.53, -13.83] | 3.56 [3.36, 3.76] | 1.28 [1.14, 1.42] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP1o | -0.00 [-0.00, 0.00] | -0.00 [-0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.39 [0.38, 0.39] | 0.39 [0.38, 0.39] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP2q1 | 1984 [1836, 2131] | 1996 [1851, 2141] | 104.33 [86.33, 122.33] | 92.38 [71.78, 112.97] |
| stP2q3 | 2535 [2384, 2686] | 2537 [2386, 2688] | 167.02 [138.39, 195.66] | 164.72 [132.80, 196.64] |
| stP2q5 | 3251 [2980, 3523] | 3411 [3138, 3683] | 5423 [4619, 6227] | 5264 [4466, 6061] |
| stP3q1 | -560.18 [-769.97, -350.39] | -140.35 [-367.28, 86.57] | 784.65 [678.72, 890.59] | 364.83 [280.04, 449.62] |
| stP3q3 | -20276 [-21339, -19212] | -20241 [-21168, -19315] | 4914 [4107, 5721] | 4880 [4384, 5376] |
| stP3q5 | -12801 [-14454, -11148] | -13457 [-15543, -11371] | 254808 [237789, 271828] | 255465 [238761, 272169] |
| stP3t1 | -46420 [-117106, 24266] | -465.11 [-3804, 2873] | 14797332 [10137055, 19457609] | 14751377 [10113694, 19389061] |
| stP5r | -3.01 [-3.21, -2.80] | 0.00 [0.00, 0.00] | 8.90 [8.70, 9.10] | 5.89 [5.72, 6.06] |
| rkRec3 | 3.97 [3.70, 4.25] | 4.43 [4.14, 4.72] | 2.46 [2.29, 2.63] | 2.01 [1.89, 2.12] |
| rkDdB | 23.78 [19.51, 28.05] | 10.97 [6.59, 15.36] | 15.15 [13.72, 16.58] | 27.96 [25.50, 30.41] |
| rkDdB30 | 1.78 [1.41, 2.14] | 1.58 [1.21, 1.95] | 1.70 [1.55, 1.84] | 1.89 [1.73, 2.06] |
| rkDdW | -4.76 [-4.92, -4.59] | -4.86 [-5.00, -4.73] | 1.16 [1.04, 1.27] | 1.27 [1.17, 1.36] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 3.55 | 3.73 |
| cbIst | 3.53 | 3.72 |
| cbFloor | 4.76 | 5.57 |
| cbQ | 0.62 | 0.31 |
| cbQmax | 4.36 | 1.87 |
| cbM | 0.70 | 0.70 |
| cbRfY | 2.00 | 1.55 |
| cbRfSh | 72.06 | 51.08 |
| cbU | 1.10 | 1.13 |
| cbA | 59316 | 56569 |
| cbN | 20527 | 29051 |
| cbF | -2026 | -985.51 |
| cbR | 3724 | 3607 |
| fsQ | 819.44 | 210.82 |
| fsN | 22.49 | 7.48 |
| fsRec | 30.08 | 28.89 |
| fsOut | 5.11 | 4.34 |
| fsBuyG | 15292 | 3078 |
| fsGap | -0.00 | 0.00 |
| fsS0 | 0.01 | 0.04 |
| fsS1 | 8.72 | 17.49 |
| fsS2 | 47.96 | 57.03 |
| fsS3 | 39.20 | 25.24 |
| fsS4 | 4.11 | 0.19 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.74 | 2.33 |
| fsB1 | 1.61 | 3.31 |
| fsB2 | 3.63 | 6.83 |
| fsB3 | 9.43 | 13.02 |
| fsB4 | 18.53 | 19.00 |
| fsB5 | 40.41 | 35.09 |
| fsB6 | 24.65 | 20.42 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.39 points against 1.76 for outside inflation: the programme's own inflation is the smaller source here.

**History checks** (no-programme run, actual rate path; checked, not tuned).

| check | model | data | verdict |
|---|---|---|---|
| top 1% share of net worth, change (points) | 5.22 | 4.60 | matches |
| bottom 50% share, change (points) | -1.08 | -0.13 | same direction, different size |
| basket poverty, change 2005-2025 (points) vs official poverty | 10.37 | -2.40 | does not match |
| basket poverty vs anchored SPM (2005-2012) | 8.11 | 1.45 | same direction, different size |
| wealth poverty, change (points) vs official poverty | 2.18 | -2.40 | does not match |

**Who gains and who pays: no programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus no central bank; and cb minus the actual rate path, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | C vs actual path (95%) | asset prices | deposits | floating debt | refinancing (actual path) | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|---|
| poorest fifth | 1156 [1049, 1263] | 2210 [2075, 2345] | 80 | 2341 | -812 | 6 (5) | -2599 | 1123 | -2051 |
| second fifth | -4253 [-4622, -3884] | -396.72 [-727.22, -66.21] | -705 | 3109 | -2374 | 775 (630) | -3907 | 990 | -13117 |
| middle fifth | -14213 [-15009, -13417] | -7166 [-7816, -6517] | -919 | 5248 | -2933 | 2618 (2962) | -4385 | 2053 | -20516 |
| fourth fifth | 3015 [1782, 4248] | 7965 [6847, 9084] | 5730 | 11611 | -2385 | 5296 (7082) | -5177 | 5691 | -14567 |
| richest fifth | 383594 [352948, 414240] | 407967 [376063, 439870] | 295262 | 81088 | -1635 | 10019 (13436) | -5728 | 41610 | -1131 |
| top 1% | 9433709 [7163034, 11704384] | 9873681 [7508280, 12239082] | 8056693 | 1282849 | -3466 | 65767 (88199) | -10450 | 603345 | 0 |

**Who gains and who pays: programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus no central bank; and cb minus the actual rate path, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | C vs actual path (95%) | asset prices | deposits | floating debt | refinancing (actual path) | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|---|
| poorest fifth | 1867 [1739, 1994] | 4239 [4052, 4426] | -66 | 5606 | -497 | 0 (4) | -2863 | 461 | -1283 |
| second fifth | -1530 [-1857, -1203] | 2630 [2276, 2985] | -1354 | 7844 | -1076 | 22 (619) | -4055 | 548 | -4722 |
| middle fifth | -1379 [-1879, -879.80] | 3285 [2817, 3753] | -1964 | 11568 | -1292 | 1699 (2897) | -4577 | 902 | -4681 |
| fourth fifth | 14061 [13389, 14733] | 18668 [17947, 19388] | 3902 | 20238 | -1055 | 5656 (6917) | -5405 | 1785 | -2616 |
| richest fifth | 349426 [319181, 379671] | 379825 [348186, 411464] | 285030 | 100912 | -1013 | 10761 (13131) | -6146 | 9725 | -42 |
| top 1% | 8867378 [6702840, 11031916] | 9370494 [7099927, 11641062] | 7934942 | 1464967 | -3745 | 69583 (86200) | -10528 | 136753 | 0 |

**Wealth shares at the end** (the central bank's effect, cb minus no central bank or the actual rate path, points of net worth, paired, 95%; weighted tail).

| run | against | top 1% share | top 10% share | bottom 50% share |
|---|---|---|---|---|
| no programme | no central bank | 0.45 [0.44, 0.47] | 0.88 [0.85, 0.92] | -0.48 [-0.51, -0.45] |
| no programme | actual rate path | 0.36 [0.35, 0.37] | 0.72 [0.70, 0.75] | -0.32 [-0.34, -0.30] |
| programme | no central bank | 0.39 [0.38, 0.41] | 0.65 [0.63, 0.67] | -0.30 [-0.31, -0.28] |
| programme | actual rate path | 0.31 [0.30, 0.32] | 0.54 [0.52, 0.55] | -0.21 [-0.22, -0.19] |

**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme's effect, central bank on; E0 with it off.

| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |
|---|---|---|---|---|
| stP2s | 29.27 | 29.36 | 0.09 [-0.08, 0.25] | 0.33 [0.15, 0.50] |
| stP2sq1 | 31.74 | 32.71 | 0.97 [0.54, 1.40] | 1.15 [0.72, 1.58] |
| stP2sq2 | 31.24 | 31.44 | 0.20 [-0.16, 0.55] | 0.52 [0.13, 0.90] |
| stP2sq3 | 30.84 | 30.62 | -0.22 [-0.57, 0.12] | -0.04 [-0.41, 0.33] |
| stP2sq4 | 29.73 | 29.30 | -0.43 [-0.75, -0.12] | -0.34 [-0.66, -0.02] |
| stP2sq5 | 24.20 | 24.08 | -0.12 [-0.29, 0.05] | 0.15 [-0.11, 0.41] |

**Each household's own inflation, 2006-2025** (% a year; its basket by household type, food, housing and medical care at their CPI-U components, the rest at CPI-U; no-programme run, actual rate path). CPI-U 2.537; all households 2.766 (10th-90th percentile 2.748 to 2.784); by fifth 2.771, 2.767, 2.764, 2.765, 2.764; top 1% 2.775. BLS's R-CPI-I check: dev/runs/s74-rcpi/rcpi.md (Amendment 3).

**Decision rule 3: does the central bank's response offset the programme's gain?** (programme run, central bank on minus no central bank, points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)

| outcome | C (95%) | C (Holm) | reading |
|---|---|---|---|
| basket poverty | 0.26 [0.23, 0.28] | [0.23, 0.28] | offsets part of the programme's gain |
| wealth poverty, last year | 1.28 [1.14, 1.42] | [1.14, 1.42] | offsets part of the programme's gain |
| wealth poverty, yearly average | 0.48 [0.44, 0.52] | [0.43, 0.53] | offsets part of the programme's gain |

## Adverse

Engine: 3beb5ff7b009e177e296156cdcb33c819a15b2af; command `node dev/tools/s74_pilot.js adv 100 --out=/tmp/claude-0/-home-user-research-update/8aadb0ca-2bae-541c-b34b-c58ccfa7773f/scratchpad/s74fix`; 100 seeds.

### C2.2

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.52 | 0.52 [0.51, 0.53] | [0.51, 0.53] | less steady | 0.52 [0.51, 0.53] | 0.00 [0.00, 0.00] | [0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 18382 | 31687 | 13305 [13109, 13501] | [13046, 13564] | less steady | 13376 [13180, 13571] | -70.81 [-86.34, -55.29] | [-90.72, -50.91] |
| P3 largest fall in real wealth ($, median) | 43056 | 20888 | -22169 [-25045, -19292] (boot -24960, -19435) | [-25468, -18869] | steadier | -238.39 [-326.12, -150.67] | -21930 [-24787, -19074] | [-25711, -18149] |
| P4 years to recover from an income shock (mean) | 3.23 | 3.06 | -0.18 [-0.21, -0.14] | [-0.21, -0.14] | steadier | -0.12 [-0.16, -0.08] | -0.06 [-0.07, -0.04] | [-0.08, -0.03] |
| P5 % pushed below the basket line in a recession year | 10.39 | 0.75 | -9.64 [-10.52, -8.77] (boot -10.52, -8.73) | [-10.72, -8.57] | steadier | -9.85 [-10.74, -8.96] | 0.21 [0.15, 0.26] | [0.14, 0.28] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -40.55 [-40.98, -40.12] | -40.70 [-41.15, -40.26] | -0.16 [-0.20, -0.13] | -0.01 [-0.01, -0.01] |
| pov | -25.90 [-26.31, -25.49] | -25.34 [-25.73, -24.95] | 0.60 [0.40, 0.79] | 0.04 [0.00, 0.07] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.51 [0.50, 0.52] | 0.51 [0.50, 0.52] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP2q1 | 12760 [12341, 13180] | 12752 [12333, 13171] | -25.71 [-40.09, -11.34] | -17.51 [-29.06, -5.95] |
| stP2q3 | 13290 [12909, 13672] | 13278 [12895, 13662] | -36.37 [-53.18, -19.57] | -24.57 [-44.62, -4.53] |
| stP2q5 | 13898 [13355, 14441] | 14273 [13726, 14819] | 2987 [2349, 3625] | 2612 [2002, 3222] |
| stP3q1 | -3529 [-3877, -3182] | -769.60 [-948.35, -590.85] | 2760 [2440, 3080] | 0.00 [0.00, 0.00] |
| stP3q3 | -20332 [-22572, -18092] | -6155 [-6697, -5613] | 35281 [30454, 40108] | 21104 [18179, 24030] |
| stP3q5 | -25860 [-30100, -21620] | 0.00 [0.00, 0.00] | 178935 [155196, 202673] | 153075 [132590, 173559] |
| stP3t1 | -63617 [-105371, -21864] | 0.00 [0.00, 0.00] | 7136642 [4495582, 9777702] | 7073024 [4440766, 9705283] |
| stP5r | -4.91 [-5.60, -4.22] | 0.00 [0.00, 0.00] | 5.48 [4.77, 6.19] | 0.57 [0.42, 0.72] |
| rkRec3 | 10.68 [10.23, 11.14] | 11.24 [10.77, 11.71] | 0.55 [0.41, 0.68] | -0.01 [-0.08, 0.06] |
| rkDdB | -13.41 [-18.06, -8.77] | -4.21 [-4.56, -3.86] | 156.83 [136.32, 177.34] | 147.62 [127.79, 167.46] |
| rkDdB30 | -6.40 [-7.08, -5.72] | -6.92 [-7.78, -6.06] | 37.78 [33.37, 42.19] | 38.31 [33.90, 42.71] |
| rkDdW | -5.44 [-6.16, -4.73] | -0.04 [-0.06, -0.02] | 10.61 [9.23, 12.00] | 5.21 [4.50, 5.93] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 2.55 | 2.78 |
| cbIst | 2.23 | 2.50 |
| cbFloor | 14.20 | 13.60 |
| cbQ | 6.36 | 5.71 |
| cbQmax | 21.79 | 21.85 |
| cbM | -0.64 | -0.63 |
| cbRfY | 0.86 | 1.09 |
| cbRfSh | 60.98 | 64.71 |
| cbU | -0.35 | -0.30 |
| cbA | 51170 | 51865 |
| cbN | 6099 | 10164 |
| cbF | -3880 | -623.75 |
| cbR | 5941 | 5488 |
| fsQ | 947.21 | 24.52 |
| fsN | 22.56 | 1.03 |
| fsRec | 15.58 | 14.76 |
| fsOut | 5.93 | 2.14 |
| fsBuyG | 5118 | 139.77 |
| fsGap | 0.00 | 0.00 |
| fsS0 | 0.01 | 0.05 |
| fsS1 | 9.00 | 43.13 |
| fsS2 | 52.11 | 50.08 |
| fsS3 | 35.92 | 6.74 |
| fsS4 | 2.97 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.57 | 3.02 |
| fsB1 | 1.57 | 4.39 |
| fsB2 | 3.57 | 8.31 |
| fsB3 | 9.47 | 14.08 |
| fsB4 | 18.67 | 18.68 |
| fsB5 | 40.44 | 33.23 |
| fsB6 | 24.70 | 18.29 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.51 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

**Who gains and who pays: no programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 786.06 [522.82, 1049] | 1124 | 699 | -1513 | 11 | 749 | 351 | -1214 |
| second fifth | 3298 [2075, 4521] | 4007 | 863 | -4389 | 2280 | 1005 | 324 | -5666 |
| middle fifth | 11888 [7702, 16074] | 12642 | 1501 | -5455 | 5936 | 1211 | 681 | -6448 |
| fourth fifth | 34463 [25552, 43374] | 28369 | 3468 | -4396 | 7511 | 1440 | 1931 | -3854 |
| richest fifth | 270313 [188989, 351638] | 211789 | 24194 | -3667 | 14102 | 1769 | 14076 | -206 |
| top 1% | 3984867 [2389739, 5579995] | 3082704 | 366695 | -14428 | 92945 | 1409 | 182859 | 0 |

**Who gains and who pays: programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 4232 [3842, 4623] | 1364 | 3193 | -190 | 14 | 671 | 31 | -229 |
| second fifth | 11394 [9604, 13184] | 5926 | 3865 | -433 | 2604 | 842 | 34 | -292 |
| middle fifth | 23424 [18952, 27896] | 14575 | 4990 | -735 | 5545 | 996 | 51 | -110 |
| fourth fifth | 41836 [33169, 50503] | 29104 | 7641 | -649 | 6738 | 1312 | 93 | -55 |
| richest fifth | 256843 [176967, 336719] | 210375 | 31399 | -1120 | 12657 | 1584 | 484 | 0 |
| top 1% | 3743938 [2163583, 5324293] | 3083114 | 415420 | -8216 | 83323 | 1324 | 6214 | 0 |

**Wealth shares at the end** (the central bank's effect, cb minus off, points of net worth, paired, 95%; weighted tail).

| run | against | top 1% share | top 10% share | bottom 50% share |
|---|---|---|---|---|
| no programme | off | -0.19 [-0.34, -0.04] | -0.17 [-0.36, 0.03] | -0.10 [-0.14, -0.05] |
| programme | off | -0.10 [-0.25, 0.04] | -0.11 [-0.30, 0.08] | -0.02 [-0.08, 0.05] |

**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme's effect, central bank on; E0 with it off.

| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |
|---|---|---|---|---|
| stP2s | 27.33 | 27.06 | -0.27 [-0.57, 0.03] | -0.18 [-0.50, 0.14] |
| stP2sq1 | 30.14 | 29.06 | -1.08 [-1.75, -0.41] | -1.04 [-1.72, -0.36] |
| stP2sq2 | 29.70 | 28.49 | -1.22 [-1.88, -0.56] | -0.97 [-1.64, -0.30] |
| stP2sq3 | 29.33 | 27.87 | -1.45 [-2.06, -0.85] | -1.36 [-1.98, -0.73] |
| stP2sq4 | 28.28 | 26.97 | -1.32 [-1.89, -0.74] | -1.29 [-1.85, -0.73] |
| stP2sq5 | 20.50 | 22.58 | 2.08 [1.61, 2.55] | 1.95 [1.48, 2.43] |

**Decision rule 3: does the central bank's response offset the programme's gain?** (programme run, central bank on minus off, points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)

| outcome | C (95%) | C (Holm) | reading |
|---|---|---|---|
| basket poverty | -0.01 [-0.01, -0.01] | [-0.01, -0.00] | adds to the programme's gain |
| wealth poverty, last year | 0.04 [0.00, 0.07] | [0.00, 0.07] | offsets part of the programme's gain |
| wealth poverty, yearly average | -0.07 [-0.10, -0.05] | [-0.11, -0.04] | adds to the programme's gain |

### release design

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.41 | 0.41 [0.41, 0.42] | [0.40, 0.42] | less steady | 0.41 [0.40, 0.42] | 0.00 [0.00, 0.00] | [0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 18382 | 20523 | 2141 [2072, 2209] | [2052, 2229] | less steady | 2175 [2107, 2243] | -34.23 [-44.31, -24.16] | [-46.60, -21.87] |
| P3 largest fall in real wealth ($, median) | 43056 | 33886 | -9170 [-10555, -7786] (boot -10522, -7847) | [-10555, -7786] | steadier | -238.39 [-326.12, -150.67] | -8932 [-10298, -7565] | [-10741, -7123] |
| P4 years to recover from an income shock (mean) | 3.23 | 3.54 | 0.31 [0.27, 0.34] | [0.26, 0.35] | less steady | 0.36 [0.33, 0.40] | -0.06 [-0.07, -0.04] | [-0.08, -0.04] |
| P5 % pushed below the basket line in a recession year | 10.39 | 5.82 | -4.57 [-5.11, -4.04] (boot -5.12, -4.04) | [-5.19, -3.96] | steadier | -4.71 [-5.25, -4.17] | 0.13 [0.07, 0.20] | [0.07, 0.20] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -18.79 [-19.12, -18.45] | -18.85 [-19.19, -18.51] | -0.16 [-0.20, -0.13] | -0.10 [-0.13, -0.08] |
| pov | -12.41 [-12.75, -12.07] | -11.77 [-12.11, -11.44] | 0.60 [0.40, 0.79] | -0.04 [-0.16, 0.08] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1p | 0.41 [0.40, 0.41] | 0.40 [0.40, 0.41] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP2q1 | 1630 [1493, 1766] | 1632 [1496, 1769] | -25.71 [-40.09, -11.34] | -28.34 [-44.12, -12.56] |
| stP2q3 | 2036 [1906, 2166] | 2044 [1915, 2173] | -36.37 [-53.18, -19.57] | -44.13 [-64.07, -24.20] |
| stP2q5 | 2781 [2562, 3000] | 2936 [2717, 3155] | 2987 [2349, 3625] | 2832 [2210, 3454] |
| stP3q1 | 896.79 [639.30, 1154] | 1649 [1402, 1895] | 2760 [2440, 3080] | 2008 [1728, 2288] |
| stP3q3 | -10108 [-11332, -8884] | -6152 [-6694, -5611] | 35281 [30454, 40108] | 31326 [27073, 35578] |
| stP3q5 | -9326 [-11788, -6864] | 0.00 [0.00, 0.00] | 178935 [155196, 202673] | 169608 [146966, 192251] |
| stP3t1 | -53262 [-108054, 1529] | 0.00 [0.00, 0.00] | 7136642 [4495582, 9777702] | 7083379 [4454596, 9712163] |
| stP5r | -1.45 [-1.87, -1.04] | 0.00 [0.00, 0.00] | 5.48 [4.77, 6.19] | 4.03 [3.49, 4.57] |
| rkRec3 | -0.10 [-0.51, 0.30] | 0.29 [-0.11, 0.69] | 0.55 [0.41, 0.68] | 0.16 [0.04, 0.27] |
| rkDdB | 23.98 [19.66, 28.31] | 6.50 [5.72, 7.28] | 156.83 [136.32, 177.34] | 174.31 [151.31, 197.31] |
| rkDdB30 | 5.02 [4.52, 5.53] | 6.82 [6.08, 7.56] | 37.78 [33.37, 42.19] | 35.98 [31.76, 40.20] |
| rkDdW | -2.27 [-2.61, -1.93] | -0.04 [-0.06, -0.02] | 10.61 [9.23, 12.00] | 8.38 [7.27, 9.50] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 2.55 | 2.65 |
| cbIst | 2.23 | 2.35 |
| cbFloor | 14.20 | 14.10 |
| cbQ | 6.36 | 6.12 |
| cbQmax | 21.79 | 23.76 |
| cbM | -0.64 | -0.70 |
| cbRfY | 0.86 | 1.05 |
| cbRfSh | 60.98 | 64.27 |
| cbU | -0.35 | -0.33 |
| cbA | 51170 | 53355 |
| cbN | 6099 | 7647 |
| cbF | -3880 | -1955 |
| cbR | 5941 | 5656 |
| fsQ | 947.21 | 311.60 |
| fsN | 22.56 | 9.12 |
| fsRec | 15.58 | 15.68 |
| fsOut | 5.93 | 7.42 |
| fsBuyG | 5118 | 1297 |
| fsGap | 0.00 | 0.00 |
| fsS0 | 0.01 | 0.04 |
| fsS1 | 9.00 | 16.82 |
| fsS2 | 52.11 | 58.83 |
| fsS3 | 35.92 | 23.95 |
| fsS4 | 2.97 | 0.36 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.57 | 2.14 |
| fsB1 | 1.57 | 3.12 |
| fsB2 | 3.57 | 6.53 |
| fsB3 | 9.47 | 12.73 |
| fsB4 | 18.67 | 18.97 |
| fsB5 | 40.44 | 35.49 |
| fsB6 | 24.70 | 21.02 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.41 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

**Who gains and who pays: no programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 786.06 [522.82, 1049] | 1124 | 699 | -1513 | 11 | 749 | 351 | -1214 |
| second fifth | 3298 [2075, 4521] | 4007 | 863 | -4389 | 2280 | 1005 | 324 | -5666 |
| middle fifth | 11888 [7702, 16074] | 12642 | 1501 | -5455 | 5936 | 1211 | 681 | -6448 |
| fourth fifth | 34463 [25552, 43374] | 28369 | 3468 | -4396 | 7511 | 1440 | 1931 | -3854 |
| richest fifth | 270313 [188989, 351638] | 211789 | 24194 | -3667 | 14102 | 1769 | 14076 | -206 |
| top 1% | 3984867 [2389739, 5579995] | 3082704 | 366695 | -14428 | 92945 | 1409 | 182859 | 0 |

**Who gains and who pays: programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 1866 [1556, 2177] | 1253 | 1325 | -937 | 18 | 720 | 174 | -767 |
| second fifth | 7405 [5737, 9073] | 5361 | 1774 | -2148 | 2577 | 917 | 212 | -2226 |
| middle fifth | 19129 [14556, 23701] | 14509 | 2695 | -2532 | 5716 | 1206 | 353 | -1722 |
| fourth fifth | 39467 [30554, 48380] | 29875 | 5087 | -2041 | 6992 | 1403 | 729 | -823 |
| richest fifth | 265783 [185139, 346427] | 217868 | 27614 | -2127 | 13102 | 1765 | 4097 | -7 |
| top 1% | 3933508 [2353695, 5513320] | 3217275 | 391528 | -10775 | 85853 | 1475 | 52415 | 0 |

**Wealth shares at the end** (the central bank's effect, cb minus off, points of net worth, paired, 95%; weighted tail).

| run | against | top 1% share | top 10% share | bottom 50% share |
|---|---|---|---|---|
| no programme | off | -0.19 [-0.34, -0.04] | -0.17 [-0.36, 0.03] | -0.10 [-0.14, -0.05] |
| programme | off | -0.18 [-0.33, -0.04] | -0.23 [-0.42, -0.04] | 0.01 [-0.03, 0.06] |

**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme's effect, central bank on; E0 with it off.

| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |
|---|---|---|---|---|
| stP2s | 27.33 | 28.09 | 0.76 [0.57, 0.95] | 0.89 [0.71, 1.08] |
| stP2sq1 | 30.14 | 31.82 | 1.68 [1.25, 2.12] | 1.76 [1.31, 2.20] |
| stP2sq2 | 29.70 | 30.86 | 1.15 [0.72, 1.58] | 1.29 [0.85, 1.74] |
| stP2sq3 | 29.33 | 29.73 | 0.40 [-0.03, 0.84] | 0.41 [-0.03, 0.85] |
| stP2sq4 | 28.28 | 28.30 | 0.01 [-0.33, 0.35] | 0.08 [-0.27, 0.42] |
| stP2sq5 | 20.50 | 21.16 | 0.66 [0.37, 0.94] | 0.69 [0.39, 0.99] |

**Decision rule 3: does the central bank's response offset the programme's gain?** (programme run, central bank on minus off, points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)

| outcome | C (95%) | C (Holm) | reading |
|---|---|---|---|
| basket poverty | -0.10 [-0.13, -0.08] | [-0.13, -0.07] | adds to the programme's gain |
| wealth poverty, last year | -0.04 [-0.16, 0.08] | [-0.16, 0.08] | no measurable difference |
| wealth poverty, yearly average | -0.16 [-0.22, -0.11] | [-0.22, -0.10] | adds to the programme's gain |

## Stress

Engine: 3beb5ff7b009e177e296156cdcb33c819a15b2af; command `node dev/tools/s74_pilot.js st 100 --out=/tmp/claude-0/-home-user-research-update/8aadb0ca-2bae-541c-b34b-c58ccfa7773f/scratchpad/s74fix`; 100 seeds.

### C2.2

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.52 | 0.52 [0.51, 0.53] | [0.50, 0.53] | less steady | 0.51 [0.50, 0.52] | 0.00 [0.00, 0.00] | [0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 18382 | 27467 | 9085 [8936, 9234] | [8888, 9282] | less steady | 9137 [8988, 9286] | -52.24 [-63.78, -40.70] | [-67.04, -37.44] |
| P3 largest fall in real wealth ($, median) | 43056 | 22939 | -20117 [-22750, -17485] (boot -22695, -17611) | [-23137, -17098] | steadier | -238.39 [-326.12, -150.67] | -19879 [-22491, -17267] | [-23337, -16422] |
| P4 years to recover from an income shock (mean) | 3.23 | 3.34 | 0.10 [0.07, 0.14] | [0.07, 0.14] | less steady | 0.16 [0.12, 0.20] | -0.06 [-0.07, -0.04] | [-0.08, -0.03] |
| P5 % pushed below the basket line in a recession year | 10.39 | 1.01 | -9.38 [-10.24, -8.52] (boot -10.23, -8.48) | [-10.43, -8.32] | steadier | -9.58 [-10.45, -8.71] | 0.20 [0.14, 0.26] | [0.13, 0.27] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -40.03 [-40.46, -39.60] | -40.19 [-40.63, -39.74] | -0.16 [-0.20, -0.13] | -0.01 [-0.01, -0.00] |
| pov | -25.36 [-25.77, -24.95] | -24.76 [-25.16, -24.37] | 0.60 [0.40, 0.79] | -0.00 [-0.03, 0.03] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1p | 0.51 [0.50, 0.52] | 0.50 [0.49, 0.51] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP2q1 | 9014 [8726, 9302] | 9007 [8719, 9294] | -25.71 [-40.09, -11.34] | -18.07 [-30.58, -5.56] |
| stP2q3 | 9041 [8753, 9329] | 9026 [8737, 9315] | -36.37 [-53.18, -19.57] | -22.07 [-41.84, -2.31] |
| stP2q5 | 9246 [8849, 9643] | 9536 [9139, 9934] | 2987 [2349, 3625] | 2696 [2075, 3318] |
| stP3q1 | -3521 [-3866, -3175] | -769.60 [-948.35, -590.85] | 2760 [2440, 3080] | 8.94 [-3.64, 21.53] |
| stP3q3 | -18419 [-20444, -16394] | -6155 [-6697, -5613] | 35281 [30454, 40108] | 23017 [19836, 26199] |
| stP3q5 | -22735 [-26711, -18758] | 0.00 [0.00, 0.00] | 178935 [155196, 202673] | 156200 [135279, 177121] |
| stP3t1 | -64055 [-106341, -21769] | 0.00 [0.00, 0.00] | 7136642 [4495582, 9777702] | 7072587 [4442297, 9702877] |
| stP5r | -4.70 [-5.36, -4.04] | 0.00 [0.00, 0.00] | 5.48 [4.77, 6.19] | 0.78 [0.60, 0.96] |
| rkRec3 | 3.56 [3.11, 4.01] | 4.00 [3.54, 4.46] | 0.55 [0.41, 0.68] | 0.10 [0.04, 0.17] |
| rkDdB | -45.96 [-52.09, -39.82] | -4.21 [-4.56, -3.86] | 156.83 [136.32, 177.34] | 115.08 [99.46, 130.70] |
| rkDdB30 | -10.63 [-11.49, -9.77] | -18.04 [-18.78, -17.29] | 37.78 [33.37, 42.19] | 45.19 [40.01, 50.38] |
| rkDdW | -4.96 [-5.61, -4.31] | -0.04 [-0.06, -0.02] | 10.61 [9.23, 12.00] | 5.70 [4.92, 6.48] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 2.55 | 2.78 |
| cbIst | 2.23 | 2.50 |
| cbFloor | 14.20 | 13.65 |
| cbQ | 6.36 | 5.70 |
| cbQmax | 21.79 | 21.89 |
| cbM | -0.64 | -0.63 |
| cbRfY | 0.86 | 1.08 |
| cbRfSh | 60.98 | 64.76 |
| cbU | -0.35 | -0.30 |
| cbA | 51170 | 51874 |
| cbN | 6099 | 9683 |
| cbF | -3880 | -665.38 |
| cbR | 5941 | 5464 |
| fsQ | 947.21 | 29.16 |
| fsN | 22.56 | 1.19 |
| fsRec | 15.58 | 14.92 |
| fsOut | 5.93 | 2.92 |
| fsBuyG | 5118 | 157.39 |
| fsGap | 0.00 | -0.00 |
| fsS0 | 0.01 | 0.05 |
| fsS1 | 9.00 | 38.37 |
| fsS2 | 52.11 | 51.94 |
| fsS3 | 35.92 | 9.63 |
| fsS4 | 2.97 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.57 | 2.94 |
| fsB1 | 1.57 | 4.24 |
| fsB2 | 3.57 | 8.13 |
| fsB3 | 9.47 | 13.97 |
| fsB4 | 18.67 | 18.71 |
| fsB5 | 40.44 | 33.42 |
| fsB6 | 24.70 | 18.59 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.51 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

**Who gains and who pays: no programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 786.06 [522.82, 1049] | 1124 | 699 | -1513 | 11 | 749 | 351 | -1214 |
| second fifth | 3298 [2075, 4521] | 4007 | 863 | -4389 | 2280 | 1005 | 324 | -5666 |
| middle fifth | 11888 [7702, 16074] | 12642 | 1501 | -5455 | 5936 | 1211 | 681 | -6448 |
| fourth fifth | 34463 [25552, 43374] | 28369 | 3468 | -4396 | 7511 | 1440 | 1931 | -3854 |
| richest fifth | 270313 [188989, 351638] | 211789 | 24194 | -3667 | 14102 | 1769 | 14076 | -206 |
| top 1% | 3984867 [2389739, 5579995] | 3082704 | 366695 | -14428 | 92945 | 1409 | 182859 | 0 |

**Who gains and who pays: programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 3865 [3487, 4243] | 1364 | 2808 | -210 | 15 | 678 | 33 | -238 |
| second fifth | 10917 [9102, 12732] | 5917 | 3417 | -478 | 2596 | 813 | 36 | -319 |
| middle fifth | 22893 [18382, 27403] | 14570 | 4512 | -794 | 5519 | 977 | 56 | -131 |
| fourth fifth | 41276 [32569, 49983] | 29109 | 7138 | -695 | 6708 | 1287 | 104 | -82 |
| richest fifth | 256331 [176419, 336243] | 210426 | 30810 | -1159 | 12603 | 1556 | 546 | 0 |
| top 1% | 3744200 [2163466, 5324934] | 3083543 | 414474 | -8382 | 82898 | 1310 | 7019 | 0 |

**Wealth shares at the end** (the central bank's effect, cb minus off, points of net worth, paired, 95%; weighted tail).

| run | against | top 1% share | top 10% share | bottom 50% share |
|---|---|---|---|---|
| no programme | off | -0.19 [-0.34, -0.04] | -0.17 [-0.36, 0.03] | -0.10 [-0.14, -0.05] |
| programme | off | -0.12 [-0.27, 0.02] | -0.15 [-0.33, 0.04] | 0.00 [-0.06, 0.06] |

**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme's effect, central bank on; E0 with it off.

| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |
|---|---|---|---|---|
| stP2s | 27.33 | 27.69 | 0.36 [0.05, 0.67] | 0.46 [0.14, 0.79] |
| stP2sq1 | 30.14 | 30.13 | -0.01 [-0.68, 0.67] | 0.11 [-0.58, 0.80] |
| stP2sq2 | 29.70 | 29.26 | -0.44 [-1.08, 0.19] | -0.15 [-0.80, 0.49] |
| stP2sq3 | 29.33 | 28.73 | -0.59 [-1.15, -0.03] | -0.48 [-1.07, 0.11] |
| stP2sq4 | 28.28 | 27.61 | -0.67 [-1.19, -0.15] | -0.65 [-1.17, -0.13] |
| stP2sq5 | 20.50 | 22.34 | 1.83 [1.40, 2.26] | 1.71 [1.27, 2.15] |

**Decision rule 3: does the central bank's response offset the programme's gain?** (programme run, central bank on minus off, points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)

| outcome | C (95%) | C (Holm) | reading |
|---|---|---|---|
| basket poverty | -0.01 [-0.01, -0.00] | [-0.01, -0.00] | adds to the programme's gain |
| wealth poverty, last year | -0.00 [-0.03, 0.03] | [-0.03, 0.03] | no measurable difference |
| wealth poverty, yearly average | -0.09 [-0.12, -0.06] | [-0.13, -0.06] | adds to the programme's gain |

### release design

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.24 | 0.24 [0.23, 0.25] | [0.23, 0.25] | less steady | 0.23 [0.23, 0.24] | 0.01 [0.00, 0.01] | [0.00, 0.01] |
| P2 spread of yearly changes in real cash income ($, mean) | 18382 | 18818 | 436.12 [399.58, 472.67] | [389.26, 482.99] | less steady | 451.25 [415.42, 487.08] | -15.12 [-21.21, -9.04] | [-22.59, -7.65] |
| P3 largest fall in real wealth ($, median) | 43056 | 39442 | -3614 [-4328, -2901] (boot -4341, -2940) | [-4328, -2901] | steadier | -238.39 [-326.12, -150.67] | -3376 [-4084, -2668] | [-4313, -2439] |
| P4 years to recover from an income shock (mean) | 3.23 | 3.47 | 0.24 [0.21, 0.27] | [0.20, 0.27] | less steady | 0.25 [0.22, 0.29] | -0.02 [-0.03, -0.00] | [-0.03, 0.00] |
| P5 % pushed below the basket line in a recession year | 10.39 | 7.26 | -3.13 [-3.51, -2.76] (boot -3.51, -2.75) | [-3.60, -2.67] | steadier | -3.20 [-3.58, -2.82] | 0.07 [0.00, 0.13] | [0.00, 0.13] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -7.58 [-7.80, -7.35] | -7.59 [-7.82, -7.37] | -0.16 [-0.20, -0.13] | -0.15 [-0.18, -0.12] |
| pov | -4.90 [-5.16, -4.64] | -4.74 [-4.98, -4.49] | 0.60 [0.40, 0.79] | 0.43 [0.25, 0.61] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1p | 0.23 [0.23, 0.24] | 0.23 [0.22, 0.23] | 0.00 [0.00, 0.00] | 0.01 [0.00, 0.01] |
| stP2q1 | 362.21 [298.37, 426.05] | 365.50 [301.67, 429.33] | -25.71 [-40.09, -11.34] | -29.00 [-44.34, -13.67] |
| stP2q3 | 398.20 [322.71, 473.69] | 405.86 [329.81, 481.90] | -36.37 [-53.18, -19.57] | -44.03 [-62.50, -25.56] |
| stP2q5 | 584.36 [484.78, 683.94] | 639.18 [544.90, 733.46] | 2987 [2349, 3625] | 2932 [2303, 3561] |
| stP3q1 | 577.83 [421.00, 734.65] | 821.33 [640.87, 1002] | 2760 [2440, 3080] | 2516 [2207, 2825] |
| stP3q3 | -4952 [-5740, -4164] | -4302 [-4666, -3938] | 35281 [30454, 40108] | 34632 [29934, 39330] |
| stP3q5 | -1853 [-3163, -542.73] | 0.00 [0.00, 0.00] | 178935 [155196, 202673] | 177082 [153542, 200622] |
| stP3t1 | 21927 [-58742, 102597] | 0.00 [0.00, 0.00] | 7136642 [4495582, 9777702] | 7158569 [4512751, 9804388] |
| stP5r | -0.78 [-1.06, -0.50] | 0.00 [0.00, 0.00] | 5.48 [4.77, 6.19] | 4.70 [4.11, 5.30] |
| rkRec3 | 0.22 [-0.08, 0.52] | 0.32 [0.06, 0.58] | 0.55 [0.41, 0.68] | 0.45 [0.31, 0.59] |
| rkDdB | 1.33 [-0.43, 3.09] | 0.83 [0.53, 1.13] | 156.83 [136.32, 177.34] | 157.32 [136.72, 177.93] |
| rkDdB30 | 1.13 [0.87, 1.40] | -0.09 [-0.48, 0.29] | 37.78 [33.37, 42.19] | 39.01 [34.45, 43.57] |
| rkDdW | -0.91 [-1.08, -0.74] | -0.04 [-0.06, -0.02] | 10.61 [9.23, 12.00] | 9.74 [8.47, 11.02] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 2.55 | 2.57 |
| cbIst | 2.23 | 2.26 |
| cbFloor | 14.20 | 14.20 |
| cbQ | 6.36 | 6.50 |
| cbQmax | 21.79 | 25.01 |
| cbM | -0.64 | -0.69 |
| cbRfY | 0.86 | 0.93 |
| cbRfSh | 60.98 | 62.56 |
| cbU | -0.35 | -0.34 |
| cbA | 51170 | 52743 |
| cbN | 6099 | 6697 |
| cbF | -3880 | -3083 |
| cbR | 5941 | 5694 |
| fsQ | 947.21 | 660.20 |
| fsN | 22.56 | 16.85 |
| fsRec | 15.58 | 15.44 |
| fsOut | 5.93 | 6.24 |
| fsBuyG | 5118 | 3222 |
| fsGap | 0.00 | 0.00 |
| fsS0 | 0.01 | 0.02 |
| fsS1 | 9.00 | 11.17 |
| fsS2 | 52.11 | 54.43 |
| fsS3 | 35.92 | 32.41 |
| fsS4 | 2.97 | 1.97 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.57 | 1.79 |
| fsB1 | 1.57 | 2.11 |
| fsB2 | 3.57 | 4.67 |
| fsB3 | 9.47 | 10.84 |
| fsB4 | 18.67 | 18.87 |
| fsB5 | 40.44 | 38.51 |
| fsB6 | 24.70 | 23.20 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.23 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

**Who gains and who pays: no programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 786.06 [522.82, 1049] | 1124 | 699 | -1513 | 11 | 749 | 351 | -1214 |
| second fifth | 3298 [2075, 4521] | 4007 | 863 | -4389 | 2280 | 1005 | 324 | -5666 |
| middle fifth | 11888 [7702, 16074] | 12642 | 1501 | -5455 | 5936 | 1211 | 681 | -6448 |
| fourth fifth | 34463 [25552, 43374] | 28369 | 3468 | -4396 | 7511 | 1440 | 1931 | -3854 |
| richest fifth | 270313 [188989, 351638] | 211789 | 24194 | -3667 | 14102 | 1769 | 14076 | -206 |
| top 1% | 3984867 [2389739, 5579995] | 3082704 | 366695 | -14428 | 92945 | 1409 | 182859 | 0 |

**Who gains and who pays: programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 1129 [840.70, 1416] | 1179 | 890 | -1327 | 13 | 762 | 291 | -1091 |
| second fifth | 4910 [3477, 6344] | 4592 | 1162 | -3491 | 2379 | 1006 | 309 | -4299 |
| middle fifth | 15051 [10639, 19464] | 13610 | 1917 | -4224 | 5740 | 1249 | 586 | -4243 |
| fourth fifth | 36860 [27894, 45826] | 29276 | 4075 | -3384 | 7106 | 1498 | 1453 | -2364 |
| richest fifth | 270463 [188581, 352346] | 217168 | 25686 | -3005 | 13360 | 1813 | 9457 | -89 |
| top 1% | 3994508 [2396689, 5592326] | 3176073 | 380232 | -12816 | 89836 | 1551 | 121287 | 0 |

**Wealth shares at the end** (the central bank's effect, cb minus off, points of net worth, paired, 95%; weighted tail).

| run | against | top 1% share | top 10% share | bottom 50% share |
|---|---|---|---|---|
| no programme | off | -0.19 [-0.34, -0.04] | -0.17 [-0.36, 0.03] | -0.10 [-0.14, -0.05] |
| programme | off | -0.19 [-0.34, -0.04] | -0.20 [-0.39, -0.01] | -0.05 [-0.09, -0.00] |

**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme's effect, central bank on; E0 with it off.

| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |
|---|---|---|---|---|
| stP2s | 27.33 | 27.26 | -0.07 [-0.18, 0.04] | 0.02 [-0.09, 0.13] |
| stP2sq1 | 30.14 | 30.39 | 0.25 [-0.03, 0.53] | 0.30 [0.01, 0.59] |
| stP2sq2 | 29.70 | 29.67 | -0.04 [-0.36, 0.29] | 0.10 [-0.23, 0.42] |
| stP2sq3 | 29.33 | 28.95 | -0.38 [-0.65, -0.11] | -0.36 [-0.64, -0.08] |
| stP2sq4 | 28.28 | 27.75 | -0.53 [-0.75, -0.32] | -0.46 [-0.69, -0.24] |
| stP2sq5 | 20.50 | 20.31 | -0.19 [-0.36, -0.03] | -0.11 [-0.28, 0.06] |

**Decision rule 3: does the central bank's response offset the programme's gain?** (programme run, central bank on minus off, points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)

| outcome | C (95%) | C (Holm) | reading |
|---|---|---|---|
| basket poverty | -0.15 [-0.18, -0.12] | [-0.18, -0.11] | adds to the programme's gain |
| wealth poverty, last year | 0.43 [0.25, 0.61] | [0.23, 0.64] | offsets part of the programme's gain |
| wealth poverty, yearly average | -0.05 [-0.14, 0.03] | [-0.14, 0.03] | no measurable difference |

## Reference

Engine: 3beb5ff7b009e177e296156cdcb33c819a15b2af; command `node dev/tools/s74_pilot.js ref 100 --out=/tmp/claude-0/-home-user-research-update/8aadb0ca-2bae-541c-b34b-c58ccfa7773f/scratchpad/s74fix`; 100 seeds.

### C2.2

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.52 | 0.52 [0.51, 0.53] | [0.51, 0.53] | less steady | 0.52 [0.51, 0.53] | -0.00 [-0.00, -0.00] | [-0.00, -0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 20088 | 34043 | 13955 [13754, 14155] | [13689, 14220] | less steady | 13950 [13749, 14151] | 5.04 [-1.63, 11.71] | [-2.61, 12.69] |
| P3 largest fall in real wealth ($, median) | 208.95 | 0.00 | -208.95 [-276.37, -141.52] (boot -276.62, -143.53) | [-286.29, -131.60] | steadier | -23.95 [-46.53, -1.36] | -185.00 [-241.13, -128.87] | [-256.97, -113.03] |
| P4 years to recover from an income shock (mean) | 3.75 | 3.26 | -0.49 [-0.53, -0.46] | [-0.54, -0.45] | steadier | -0.46 [-0.50, -0.42] | -0.03 [-0.04, -0.02] | [-0.05, -0.02] |
| P5 % pushed below the basket line in a recession year | 0.00 | 0.00 | 0.00 [0.00, 0.00] (boot 0.00, 0.00) | [0.00, 0.00] | no measurable difference | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | [0.00, 0.00] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -32.43 [-32.79, -32.08] | -32.37 [-32.72, -32.01] | 0.07 [0.06, 0.08] | 0.00 [0.00, 0.00] |
| pov | -23.59 [-23.93, -23.26] | -22.30 [-22.63, -21.97] | 1.36 [1.24, 1.49] | 0.07 [0.04, 0.10] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.52 [0.51, 0.53] | 0.52 [0.51, 0.53] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP2q1 | 13602 [13166, 14037] | 13604 [13169, 14039] | -1.33 [-1.65, -1.01] | -3.15 [-8.81, 2.52] |
| stP2q3 | 13837 [13439, 14235] | 13830 [13431, 14228] | -3.50 [-4.28, -2.72] | 4.08 [-9.88, 18.04] |
| stP2q5 | 14623 [14063, 15183] | 14609 [14047, 15172] | 0.26 [0.14, 0.39] | 13.97 [-12.59, 40.54] |
| stP3q1 | -1256 [-1338, -1174] | -254.91 [-364.86, -144.95] | 1001 [921.40, 1080] | 0.00 [0.00, 0.00] |
| stP3q3 | -5619 [-6333, -4905] | -5290 [-5962, -4618] | 328.38 [225.68, 431.08] | 0.00 [0.00, 0.00] |
| stP3q5 | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP3t1 | 39623 [21034, 58212] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 39623 [21034, 58212] |
| stP5r | 0.20 [0.14, 0.26] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.20 [0.14, 0.26] |
| rkRec3 | 2.21 [1.77, 2.65] | 2.04 [1.59, 2.49] | -0.12 [-0.24, -0.00] | 0.05 [0.01, 0.08] |
| rkDdB | -2.11 [-2.43, -1.80] | -1.98 [-2.28, -1.67] | 0.14 [0.10, 0.18] | 0.00 [0.00, 0.00] |
| rkDdB30 | -4.06 [-4.86, -3.26] | -5.19 [-6.01, -4.37] | 0.47 [0.40, 0.54] | 1.60 [1.35, 1.84] |
| rkDdW | -0.03 [-0.05, -0.02] | -0.00 [-0.01, 0.00] | 0.03 [0.02, 0.04] | 0.00 [0.00, 0.00] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 0.00 | 0.29 |
| cbIst | -0.03 | 0.20 |
| cbFloor | 100.00 | 53.85 |
| cbQ | 0.34 | 1.68 |
| cbQmax | 0.34 | 5.23 |
| cbM | 0.00 | -0.05 |
| cbRfY | 0.00 | 0.00 |
| cbRfSh | 0.00 | 0.00 |
| cbU | 0.00 | 0.04 |
| cbA | 0.00 | 452.58 |
| cbN | 0.00 | 2636 |
| cbF | -2713 | -485.87 |
| cbR | 0.00 | 0.00 |
| fsQ | 579.85 | 19.01 |
| fsN | 18.59 | 0.91 |
| fsRec | 0.00 | 0.00 |
| fsOut | 3.86 | 1.53 |
| fsBuyG | 3642 | 117.63 |
| fsGap | 0.00 | 0.00 |
| fsS0 | 0.01 | 0.04 |
| fsS1 | 7.72 | 41.16 |
| fsS2 | 51.27 | 51.80 |
| fsS3 | 38.60 | 7.00 |
| fsS4 | 2.40 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 2.10 | 3.01 |
| fsB1 | 1.71 | 4.16 |
| fsB2 | 3.91 | 8.00 |
| fsB3 | 10.21 | 13.83 |
| fsB4 | 19.06 | 18.77 |
| fsB5 | 39.67 | 33.81 |
| fsB6 | 23.34 | 18.42 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.52 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

**Who gains and who pays: no programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | -502.11 [-522.59, -481.64] | 0 | 0 | -1112 | 0 | 0 | 310 | -994 |
| second fifth | -2246 [-2369, -2123] | 0 | 0 | -2980 | 0 | 0 | 249 | -4421 |
| middle fifth | -5932 [-6199, -5664] | 0 | 0 | -3733 | 0 | 0 | 551 | -4833 |
| fourth fifth | -3817 [-4090, -3545] | 0 | 0 | -3059 | 0 | 0 | 1517 | -2793 |
| richest fifth | 7713 [7387, 8040] | 0 | 0 | -2697 | 0 | 0 | 10555 | -125 |
| top 1% | 127041 [101460, 152622] | 0 | 0 | -11183 | 0 | 0 | 151458 | 0 |

**Who gains and who pays: programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | 642.69 [594.13, 691.24] | 14 | 815 | -145 | 0 | -90 | 26 | -192 |
| second fifth | 571.49 [483.78, 659.20] | 61 | 961 | -330 | 0 | -112 | 28 | -247 |
| middle fifth | 784.87 [660.81, 908.93] | 154 | 1256 | -579 | 0 | -260 | 43 | -97 |
| fourth fifth | 1748 [1543, 1954] | 286 | 1968 | -513 | 0 | -205 | 79 | -44 |
| richest fifth | 8844 [6310, 11377] | 1752 | 8249 | -869 | 0 | -219 | 409 | 0 |
| top 1% | 135367 [33409, 237326] | 37856 | 112423 | -5787 | 0 | -12 | 5428 | 0 |

**Wealth shares at the end** (the central bank's effect, cb minus off, points of net worth, paired, 95%; weighted tail).

| run | against | top 1% share | top 10% share | bottom 50% share |
|---|---|---|---|---|
| no programme | off | 0.07 [0.07, 0.08] | 0.20 [0.19, 0.21] | -0.20 [-0.21, -0.19] |
| programme | off | -0.01 [-0.02, -0.01] | -0.01 [-0.02, -0.00] | -0.01 [-0.01, -0.00] |

**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme's effect, central bank on; E0 with it off.

| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |
|---|---|---|---|---|
| stP2s | 25.90 | 26.57 | 0.67 [0.38, 0.97] | 0.83 [0.53, 1.13] |
| stP2sq1 | 27.91 | 28.23 | 0.32 [-0.27, 0.90] | 0.59 [-0.01, 1.18] |
| stP2sq2 | 28.00 | 27.99 | -0.00 [-0.69, 0.68] | 0.34 [-0.36, 1.04] |
| stP2sq3 | 27.50 | 27.19 | -0.30 [-0.98, 0.38] | -0.17 [-0.84, 0.51] |
| stP2sq4 | 26.97 | 26.70 | -0.28 [-0.85, 0.30] | -0.24 [-0.81, 0.33] |
| stP2sq5 | 19.77 | 22.24 | 2.47 [1.97, 2.97] | 2.49 [1.98, 3.00] |

**Decision rule 3: does the central bank's response offset the programme's gain?** (programme run, central bank on minus off, points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)

| outcome | C (95%) | C (Holm) | reading |
|---|---|---|---|
| basket poverty | 0.00 [0.00, 0.00] | [0.00, 0.00] | offsets part of the programme's gain |
| wealth poverty, last year | 0.07 [0.04, 0.10] | [0.04, 0.10] | offsets part of the programme's gain |
| wealth poverty, yearly average | 0.07 [0.06, 0.08] | [0.06, 0.08] | offsets part of the programme's gain |

### release design

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.38 | 0.38 [0.38, 0.39] | [0.37, 0.39] | less steady | 0.38 [0.38, 0.39] | -0.00 [-0.00, -0.00] | [-0.00, -0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 20088 | 22392 | 2304 [2230, 2378] | [2209, 2399] | less steady | 2294 [2220, 2368] | 9.78 [4.69, 14.86] | [3.94, 15.61] |
| P3 largest fall in real wealth ($, median) | 208.95 | 0.00 | -208.95 [-276.37, -141.52] (boot -276.62, -143.53) | [-286.29, -131.60] | steadier | -23.95 [-46.53, -1.36] | -185.00 [-241.13, -128.87] | [-259.29, -110.70] |
| P4 years to recover from an income shock (mean) | 3.75 | 3.92 | 0.17 [0.14, 0.20] | [0.14, 0.21] | less steady | 0.20 [0.17, 0.23] | -0.03 [-0.04, -0.02] | [-0.05, -0.02] |
| P5 % pushed below the basket line in a recession year | 0.00 | 0.00 | 0.00 [0.00, 0.00] (boot 0.00, 0.00) | [0.00, 0.00] | no measurable difference | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | [0.00, 0.00] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -20.92 [-21.21, -20.63] | -20.90 [-21.19, -20.61] | 0.07 [0.06, 0.08] | 0.05 [0.04, 0.05] |
| pov | -15.09 [-15.43, -14.74] | -14.18 [-14.51, -13.85] | 1.36 [1.24, 1.49] | 0.45 [0.39, 0.52] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1p | 0.38 [0.38, 0.39] | 0.38 [0.38, 0.39] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP2q1 | 1806 [1652, 1960] | 1811 [1657, 1964] | -1.33 [-1.65, -1.01] | -5.85 [-10.23, -1.48] |
| stP2q3 | 2109 [1977, 2241] | 2107 [1975, 2239] | -3.50 [-4.28, -2.72] | -1.76 [-8.65, 5.13] |
| stP2q5 | 3165 [2906, 3424] | 3111 [2852, 3370] | 0.26 [0.14, 0.39] | 53.84 [35.80, 71.88] |
| stP3q1 | -854.17 [-958.62, -749.72] | -86.57 [-205.40, 32.26] | 1001 [921.40, 1080] | 233.13 [173.27, 292.98] |
| stP3q3 | -5619 [-6333, -4905] | -5290 [-5962, -4618] | 328.38 [225.68, 431.08] | 0.00 [0.00, 0.00] |
| stP3q5 | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP3t1 | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP5r | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| rkRec3 | -0.40 [-0.73, -0.06] | -0.49 [-0.83, -0.15] | -0.12 [-0.24, -0.00] | -0.03 [-0.10, 0.03] |
| rkDdB | -0.63 [-0.98, -0.28] | -1.50 [-1.82, -1.19] | 0.14 [0.10, 0.18] | 1.01 [0.79, 1.23] |
| rkDdB30 | 0.96 [0.26, 1.66] | 0.30 [-0.41, 1.01] | 0.47 [0.40, 0.54] | 1.13 [1.01, 1.25] |
| rkDdW | -0.03 [-0.05, -0.02] | -0.00 [-0.01, 0.00] | 0.03 [0.02, 0.04] | 0.00 [0.00, 0.00] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 0.00 | 0.23 |
| cbIst | -0.03 | 0.15 |
| cbFloor | 100.00 | 53.55 |
| cbQ | 0.34 | 1.43 |
| cbQmax | 0.34 | 4.38 |
| cbM | 0.00 | -0.03 |
| cbRfY | 0.00 | 0.00 |
| cbRfSh | 0.00 | 0.00 |
| cbU | 0.00 | 0.03 |
| cbA | 0.00 | 207.04 |
| cbN | 0.00 | 1746 |
| cbF | -2713 | -1228 |
| cbR | 0.00 | 0.00 |
| fsQ | 579.85 | 128.42 |
| fsN | 18.59 | 5.20 |
| fsRec | 0.00 | 0.00 |
| fsOut | 3.86 | 3.39 |
| fsBuyG | 3642 | 719.78 |
| fsGap | 0.00 | -0.00 |
| fsS0 | 0.01 | 0.04 |
| fsS1 | 7.72 | 18.63 |
| fsS2 | 51.27 | 59.08 |
| fsS3 | 38.60 | 22.25 |
| fsS4 | 2.40 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 2.10 | 2.51 |
| fsB1 | 1.71 | 3.19 |
| fsB2 | 3.91 | 6.66 |
| fsB3 | 10.21 | 12.95 |
| fsB4 | 19.06 | 19.10 |
| fsB5 | 39.67 | 35.45 |
| fsB6 | 23.34 | 20.13 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.38 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

**Who gains and who pays: no programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | -502.11 [-522.59, -481.64] | 0 | 0 | -1112 | 0 | 0 | 310 | -994 |
| second fifth | -2246 [-2369, -2123] | 0 | 0 | -2980 | 0 | 0 | 249 | -4421 |
| middle fifth | -5932 [-6199, -5664] | 0 | 0 | -3733 | 0 | 0 | 551 | -4833 |
| fourth fifth | -3817 [-4090, -3545] | 0 | 0 | -3059 | 0 | 0 | 1517 | -2793 |
| richest fifth | 7713 [7387, 8040] | 0 | 0 | -2697 | 0 | 0 | 10555 | -125 |
| top 1% | 127041 [101460, 152622] | 0 | 0 | -11183 | 0 | 0 | 151458 | 0 |

**Who gains and who pays: programme run** (by fifth of starting real wealth and the top 1%; Year-0 dollars per adult). C: the central bank's effect on the change in real wealth over the run (cb minus off, paired, 95%). Channels: first-round tallies in the central-bank arm (asset prices, deposits, floating debt, refinancing, job-loss income, forced-sale buyers' and sellers' later gains), means over seeds.

| group | C on real wealth (95%) | asset prices | deposits | floating debt | refinancing | job-loss income | buyers' gain | sellers' gain |
|---|---|---|---|---|---|---|---|---|
| poorest fifth | -242.49 [-278.18, -206.81] | 9 | 360 | -551 | 0 | -75 | 111 | -543 |
| second fifth | -1072 [-1176, -967.83] | 31 | 449 | -1182 | 0 | -78 | 121 | -1304 |
| middle fifth | -1507 [-1661, -1354] | 79 | 667 | -1554 | 0 | -143 | 210 | -953 |
| fourth fifth | -171.88 [-380.82, 37.06] | 145 | 1212 | -1328 | 0 | -179 | 430 | -458 |
| richest fifth | 7005 [4948, 9063] | 770 | 6099 | -1534 | 0 | -113 | 2411 | -4 |
| top 1% | 106354 [26320, 186387] | 8337 | 87525 | -7963 | 0 | -22 | 33325 | 0 |

**Wealth shares at the end** (the central bank's effect, cb minus off, points of net worth, paired, 95%; weighted tail).

| run | against | top 1% share | top 10% share | bottom 50% share |
|---|---|---|---|---|
| no programme | off | 0.07 [0.07, 0.08] | 0.20 [0.19, 0.21] | -0.20 [-0.21, -0.19] |
| programme | off | 0.02 [0.01, 0.02] | 0.06 [0.05, 0.07] | -0.08 [-0.08, -0.07] |

**P2 as a share of income** (per adult, the spread of the yearly change in real cash income over its mean, %; weighted median; all adults, then by fifth). E: the programme's effect, central bank on; E0 with it off.

| key | no programme, cb on | programme, cb on | E (95%) | E0 (95%) |
|---|---|---|---|---|
| stP2s | 25.90 | 24.95 | -0.95 [-1.11, -0.78] | -0.85 [-1.02, -0.68] |
| stP2sq1 | 27.91 | 27.64 | -0.27 [-0.65, 0.10] | -0.00 [-0.42, 0.41] |
| stP2sq2 | 28.00 | 26.99 | -1.01 [-1.40, -0.62] | -0.80 [-1.21, -0.39] |
| stP2sq3 | 27.50 | 26.06 | -1.43 [-1.85, -1.01] | -1.39 [-1.82, -0.96] |
| stP2sq4 | 26.97 | 25.79 | -1.18 [-1.52, -0.85] | -1.18 [-1.51, -0.86] |
| stP2sq5 | 19.77 | 19.22 | -0.56 [-0.81, -0.31] | -0.57 [-0.82, -0.32] |

**Decision rule 3: does the central bank's response offset the programme's gain?** (programme run, central bank on minus off, points; 95% and Holm-adjusted across the three; the reading uses the Holm interval)

| outcome | C (95%) | C (Holm) | reading |
|---|---|---|---|
| basket poverty | 0.05 [0.04, 0.05] | [0.04, 0.05] | offsets part of the programme's gain |
| wealth poverty, last year | 0.45 [0.39, 0.52] | [0.38, 0.53] | offsets part of the programme's gain |
| wealth poverty, yearly average | 0.24 [0.22, 0.27] | [0.21, 0.27] | offsets part of the programme's gain |

## Decision rule: does the programme's share of essentials damp what the central bank and outside shocks do to the cost of basic living?

- C2.2: P1 interaction below zero (Holm) in History false, Adverse false, Stress false; basket poverty not worse true. **Claim not supported.**
- release design: P1 interaction below zero (Holm) in History false, Adverse false, Stress false; basket poverty not worse true. **Claim not supported.**
