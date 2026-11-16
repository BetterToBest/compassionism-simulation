# S74 pilot tables (100 seeds, frozen round-2 main row)

Made by `node dev/tools/s74_table.js` from the pilot files in this folder (`node dev/tools/s74_pilot.js ENV 100`). Programme effect: programme minus no programme, paired on seeds. Interaction: the programme's effect with the central bank on minus with it off (History: off is no central bank). Intervals are 95% paired t; Holm-adjusted intervals (H) are across the five primary outcomes within each environment, design and family. For every primary outcome lower is steadier.

## History (2005-2025)

Engine: 5f11ceb0a5fea4d62f7c8bc024e4896b17fda723; command `node dev/tools/s74_pilot.js hx 100`; 100 seeds.

### C2.2

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 1.76 | 1.85 | 0.09 [0.08, 0.09] | [0.08, 0.09] | less steady | 0.09 [0.09, 0.09] | -0.00 [-0.00, 0.00] | [-0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 20201 | 33354 | 13153 [12946, 13361] | [12887, 13420] | less steady | 13257 [13049, 13465] | -103.41 [-117.68, -89.15] | [-122.29, -84.53] |
| P3 largest fall in real wealth ($, median) | 56647 | 10024 | -46623 [-47235, -46011] (boot -47238, -46035) | [-47433, -45813] | steadier | -42902 [-43517, -42288] | -3721 [-4254, -3187] | [-4405, -3037] |
| P4 years to recover from an income shock (mean) | 3.37 | 3.08 | -0.29 [-0.32, -0.26] | [-0.32, -0.26] | steadier | -0.32 [-0.35, -0.29] | 0.03 [0.01, 0.04] | [0.01, 0.05] |
| P5 % pushed below the basket line in a recession year | 9.30 | 1.44 | -7.86 [-8.07, -7.66] (boot -8.07, -7.66) | [-8.11, -7.61] | steadier | -7.64 [-7.84, -7.44] | -0.22 [-0.27, -0.18] | [-0.28, -0.17] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -42.38 [-42.77, -41.99] | -41.99 [-42.38, -41.59] | 0.40 [0.37, 0.43] | 0.01 [0.01, 0.02] |
| pov | -28.32 [-28.68, -27.95] | -24.99 [-25.35, -24.63] | 3.38 [3.18, 3.57] | 0.05 [0.03, 0.06] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1o | -0.00 [-0.00, 0.00] | -0.00 [-0.00, -0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1p | 0.50 [0.49, 0.50] | 0.50 [0.49, 0.50] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP2q1 | 13418 [12976, 13860] | 13467 [13025, 13910] | 104.01 [86.13, 121.89] | 54.58 [36.98, 72.17] |
| stP2q3 | 12908 [12511, 13306] | 12971 [12575, 13367] | 172.14 [143.04, 201.24] | 109.25 [83.24, 135.27] |
| stP2q5 | 13381 [12846, 13917] | 13688 [13150, 14227] | 5362 [4564, 6160] | 5055 [4270, 5839] |
| stP3q1 | -4316 [-4538, -4094] | -3569 [-3802, -3335] | 776.74 [661.07, 892.40] | 29.52 [3.51, 55.53] |
| stP3q3 | -47755 [-49097, -46413] | -40215 [-41564, -38867] | 6216 [5380, 7053] | -1324 [-1690, -957.48] |
| stP3q5 | -65370 [-71446, -59294] | -55109 [-58934, -51283] | 258903 [241974, 275832] | 248642 [234084, 263200] |
| stP3t1 | -276807 [-352814, -200800] | -52824 [-75460, -30188] | 14888784 [10218539, 19559030] | 14664801 [10054738, 19274863] |
| stP5r | -7.30 [-7.51, -7.09] | 0.00 [0.00, 0.00] | 8.88 [8.68, 9.08] | 1.58 [1.51, 1.65] |
| rkRec3 | 8.85 [8.52, 9.18] | 10.22 [9.88, 10.57] | 2.44 [2.27, 2.60] | 1.07 [0.99, 1.14] |
| rkDdB | -60.64 [-68.47, -52.81] | -73.92 [-80.02, -67.81] | 18.87 [17.26, 20.49] | 32.15 [28.81, 35.50] |
| rkDdB30 | -18.33 [-18.96, -17.69] | -18.20 [-18.78, -17.63] | 1.72 [1.57, 1.87] | 1.59 [1.33, 1.86] |
| rkDdW | -11.52 [-11.67, -11.38] | -10.57 [-10.72, -10.42] | 1.38 [1.26, 1.50] | 0.43 [0.37, 0.50] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 3.55 | 3.79 |
| cbIst | 3.53 | 3.79 |
| cbFloor | 4.76 | 1.76 |
| cbQ | 0.62 | 0.10 |
| cbQmax | 4.36 | 0.68 |
| cbM | 0.70 | 0.70 |
| cbRfY | 2.00 | 1.95 |
| cbRfSh | 72.07 | 65.45 |
| cbU | 1.10 | 1.15 |
| cbA | 59289 | 58753 |
| cbN | 39684 | 125894 |
| cbF | -1716 | -129.12 |
| cbR | 3724 | 4097 |
| fsQ | 795.72 | 14.79 |
| fsN | 21.91 | 0.71 |
| fsRec | 30.46 | 36.43 |
| fsOut | 4.95 | 1.52 |
| fsBuyG | 14515 | 262.37 |
| fsGap | 0.00 | 0.00 |
| fsS0 | 0.01 | 0.10 |
| fsS1 | 8.84 | 42.72 |
| fsS2 | 48.19 | 49.74 |
| fsS3 | 38.95 | 7.44 |
| fsS4 | 4.01 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.24 | 3.88 |
| fsB1 | 1.26 | 7.10 |
| fsB2 | 2.87 | 11.98 |
| fsB3 | 7.32 | 15.99 |
| fsB4 | 13.81 | 16.53 |
| fsB5 | 36.08 | 26.47 |
| fsB6 | 37.43 | 18.06 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.50 points against 1.76 for outside inflation: the programme's own inflation is the smaller source here.

**History checks** (no-programme run, actual rate path; checked, not tuned).

| check | model | data | verdict |
|---|---|---|---|
| top 1% share of net worth, change (points) | 7.58 | 4.60 | matches |
| bottom 50% share, change (points) | -1.15 | -0.13 | same direction, different size |
| basket poverty, change 2005-2025 (points) vs official poverty | 10.32 | -2.40 | does not match |
| basket poverty vs anchored SPM (2005-2012) | 8.08 | 1.45 | same direction, different size |
| wealth poverty, change (points) vs official poverty | 1.75 | -2.40 | does not match |

### release design

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 1.76 | 1.88 | 0.12 [0.12, 0.13] | [0.12, 0.13] | less steady | 0.12 [0.12, 0.13] | 0.00 [0.00, 0.00] | [0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 20201 | 22907 | 2706 [2624, 2789] | [2597, 2815] | less steady | 2755 [2671, 2838] | -48.38 [-58.33, -38.43] | [-61.55, -35.21] |
| P3 largest fall in real wealth ($, median) | 56647 | 37006 | -19641 [-20374, -18909] (boot -20348, -18930) | [-20581, -18702] | steadier | -21456 [-22218, -20694] | 1815 [1178, 2452] | [1033, 2597] |
| P4 years to recover from an income shock (mean) | 3.37 | 3.82 | 0.45 [0.42, 0.47] | [0.42, 0.47] | less steady | 0.49 [0.46, 0.52] | -0.05 [-0.06, -0.03] | [-0.07, -0.03] |
| P5 % pushed below the basket line in a recession year | 9.30 | 5.66 | -3.65 [-3.85, -3.44] (boot -3.85, -3.45) | [-3.88, -3.41] | steadier | -3.52 [-3.71, -3.32] | -0.13 [-0.17, -0.08] | [-0.18, -0.07] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -25.22 [-25.60, -24.84] | -25.04 [-25.42, -24.67] | 0.40 [0.37, 0.43] | 0.23 [0.21, 0.25] |
| pov | -16.70 [-17.11, -16.28] | -14.80 [-15.19, -14.42] | 3.38 [3.18, 3.57] | 1.48 [1.34, 1.63] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP1o | -0.00 [-0.00, 0.00] | -0.00 [-0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.39 [0.38, 0.40] | 0.39 [0.38, 0.40] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP2q1 | 2766 [2590, 2941] | 2781 [2607, 2955] | 104.01 [86.13, 121.89] | 89.06 [68.43, 109.69] |
| stP2q3 | 2479 [2303, 2654] | 2501 [2324, 2677] | 172.14 [143.04, 201.24] | 150.36 [119.43, 181.28] |
| stP2q5 | 3176 [2899, 3452] | 3346 [3071, 3621] | 5362 [4564, 6160] | 5192 [4401, 5982] |
| stP3q1 | 1566 [1274, 1857] | 1372 [1070, 1674] | 776.74 [661.07, 892.40] | 970.10 [833.96, 1106] |
| stP3q3 | -21226 [-22566, -19886] | -22430 [-23715, -21144] | 6216 [5380, 7053] | 7421 [6844, 7997] |
| stP3q5 | -25434 [-30845, -20023] | -20936 [-24036, -17837] | 258903 [241974, 275832] | 254405 [238249, 270562] |
| stP3t1 | -72056 [-147594, 3482] | 2027 [-9463, 13517] | 14888784 [10218539, 19559030] | 14814701 [10183712, 19445690] |
| stP5r | -3.29 [-3.50, -3.09] | 0.00 [0.00, 0.00] | 8.88 [8.68, 9.08] | 5.59 [5.42, 5.75] |
| rkRec3 | 3.42 [3.13, 3.70] | 4.18 [3.87, 4.48] | 2.44 [2.27, 2.60] | 1.68 [1.57, 1.78] |
| rkDdB | 36.29 [31.15, 41.42] | 17.29 [12.54, 22.04] | 18.87 [17.26, 20.49] | 37.87 [35.17, 40.58] |
| rkDdB30 | 0.45 [-0.02, 0.93] | 0.09 [-0.38, 0.56] | 1.72 [1.57, 1.87] | 2.08 [1.88, 2.28] |
| rkDdW | -4.87 [-5.06, -4.69] | -5.30 [-5.48, -5.11] | 1.38 [1.26, 1.50] | 1.81 [1.70, 1.91] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 3.55 | 3.73 |
| cbIst | 3.53 | 3.72 |
| cbFloor | 4.76 | 5.05 |
| cbQ | 0.62 | 0.26 |
| cbQmax | 4.36 | 1.59 |
| cbM | 0.70 | 0.69 |
| cbRfY | 2.00 | 1.57 |
| cbRfSh | 72.07 | 51.87 |
| cbU | 1.10 | 1.14 |
| cbA | 59289 | 57021 |
| cbN | 39684 | 60914 |
| cbF | -1716 | -895.87 |
| cbR | 3724 | 3599 |
| fsQ | 795.72 | 220.79 |
| fsN | 21.91 | 7.74 |
| fsRec | 30.46 | 28.40 |
| fsOut | 4.95 | 4.84 |
| fsBuyG | 14515 | 3098 |
| fsGap | 0.00 | 0.00 |
| fsS0 | 0.01 | 0.10 |
| fsS1 | 8.84 | 18.47 |
| fsS2 | 48.19 | 57.90 |
| fsS3 | 38.95 | 23.38 |
| fsS4 | 4.01 | 0.16 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.24 | 2.43 |
| fsB1 | 1.26 | 4.56 |
| fsB2 | 2.87 | 8.34 |
| fsB3 | 7.32 | 12.60 |
| fsB4 | 13.81 | 15.28 |
| fsB5 | 36.08 | 29.19 |
| fsB6 | 37.43 | 27.60 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.39 points against 1.76 for outside inflation: the programme's own inflation is the smaller source here.

**History checks** (no-programme run, actual rate path; checked, not tuned).

| check | model | data | verdict |
|---|---|---|---|
| top 1% share of net worth, change (points) | 7.58 | 4.60 | matches |
| bottom 50% share, change (points) | -1.15 | -0.13 | same direction, different size |
| basket poverty, change 2005-2025 (points) vs official poverty | 10.32 | -2.40 | does not match |
| basket poverty vs anchored SPM (2005-2012) | 8.08 | 1.45 | same direction, different size |
| wealth poverty, change (points) vs official poverty | 1.75 | -2.40 | does not match |

## Adverse

Engine: 5f11ceb0a5fea4d62f7c8bc024e4896b17fda723; command `node dev/tools/s74_pilot.js adv 100`; 100 seeds.

### C2.2

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.52 | 0.52 [0.51, 0.53] | [0.51, 0.54] | less steady | 0.52 [0.51, 0.53] | 0.00 [0.00, 0.00] | [0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 18383 | 31881 | 13498 [13288, 13707] | [13220, 13775] | less steady | 13565 [13354, 13775] | -67.24 [-82.82, -51.65] | [-87.22, -47.25] |
| P3 largest fall in real wealth ($, median) | 40752 | 0.00 | -40752 [-46028, -35476] (boot -45857, -35643) | [-46804, -34700] | steadier | -295.54 [-391.64, -199.45] | -40457 [-45710, -35203] | [-47411, -33503] |
| P4 years to recover from an income shock (mean) | 3.24 | 3.05 | -0.19 [-0.22, -0.15] | [-0.22, -0.15] | steadier | -0.12 [-0.16, -0.08] | -0.06 [-0.08, -0.05] | [-0.09, -0.04] |
| P5 % pushed below the basket line in a recession year | 10.38 | 0.61 | -9.77 [-10.65, -8.88] (boot -10.65, -8.84) | [-10.85, -8.68] | steadier | -9.96 [-10.86, -9.07] | 0.20 [0.14, 0.25] | [0.13, 0.26] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -41.05 [-41.49, -40.61] | -41.21 [-41.66, -40.76] | -0.16 [-0.20, -0.13] | -0.01 [-0.01, -0.00] |
| pov | -26.21 [-26.61, -25.81] | -25.58 [-25.97, -25.19] | 0.64 [0.45, 0.83] | 0.01 [-0.00, 0.03] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.51 [0.50, 0.52] | 0.51 [0.50, 0.52] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP2q1 | 13771 [13319, 14223] | 13762 [13309, 14214] | -26.80 [-41.35, -12.25] | -17.49 [-29.96, -5.02] |
| stP2q3 | 13260 [12853, 13668] | 13245 [12836, 13654] | -36.77 [-53.59, -19.95] | -20.99 [-40.87, -1.10] |
| stP2q5 | 13842 [13294, 14389] | 14208 [13653, 14762] | 2844 [2224, 3464] | 2479 [1884, 3074] |
| stP3q1 | -3670 [-4021, -3320] | -924.73 [-1128, -721.46] | 2746 [2433, 3059] | 0.00 [0.00, 0.00] |
| stP3q3 | -39566 [-44261, -34870] | -6314 [-6860, -5767] | 33252 [28633, 37870] | 0.00 [0.00, 0.00] |
| stP3q5 | -70521 [-80166, -60876] | 0.00 [0.00, 0.00] | 158611 [137544, 179677] | 88089 [75405, 100774] |
| stP3t1 | -135801 [-178716, -92885] | 0.00 [0.00, 0.00] | 5915506 [3747570, 8083443] | 5779706 [3624679, 7934732] |
| stP5r | -5.00 [-5.70, -4.30] | 0.00 [0.00, 0.00] | 5.48 [4.77, 6.19] | 0.48 [0.34, 0.62] |
| rkRec3 | 10.66 [10.21, 11.11] | 11.13 [10.66, 11.60] | 0.54 [0.41, 0.67] | 0.07 [0.00, 0.13] |
| rkDdB | -135.59 [-152.87, -118.32] | -4.37 [-4.74, -4.01] | 148.60 [129.19, 168.01] | 17.38 [13.70, 21.07] |
| rkDdB30 | -27.36 [-29.83, -24.89] | -8.35 [-9.20, -7.49] | 37.18 [32.80, 41.55] | 18.16 [16.00, 20.33] |
| rkDdW | -10.09 [-11.40, -8.78] | -0.05 [-0.07, -0.03] | 10.04 [8.73, 11.34] | 0.00 [0.00, 0.00] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 2.55 | 2.78 |
| cbIst | 2.23 | 2.50 |
| cbFloor | 14.20 | 13.60 |
| cbQ | 6.36 | 5.71 |
| cbQmax | 21.79 | 21.80 |
| cbM | -0.64 | -0.63 |
| cbRfY | 0.86 | 1.09 |
| cbRfSh | 60.94 | 64.80 |
| cbU | -0.35 | -0.30 |
| cbA | 51193 | 51882 |
| cbN | 10404 | 28965 |
| cbF | -3186 | -296.18 |
| cbR | 5941 | 5512 |
| fsQ | 922.28 | 17.45 |
| fsN | 21.98 | 0.75 |
| fsRec | 15.48 | 13.93 |
| fsOut | 5.76 | 1.79 |
| fsBuyG | 4896 | 106.87 |
| fsGap | -0.00 | -0.00 |
| fsS0 | 0.01 | 0.10 |
| fsS1 | 9.13 | 44.81 |
| fsS2 | 52.37 | 48.58 |
| fsS3 | 35.63 | 6.51 |
| fsS4 | 2.87 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.12 | 3.85 |
| fsB1 | 1.19 | 7.15 |
| fsB2 | 2.80 | 12.00 |
| fsB3 | 7.30 | 15.99 |
| fsB4 | 13.90 | 16.35 |
| fsB5 | 36.25 | 26.19 |
| fsB6 | 37.44 | 18.46 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.51 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

### release design

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.42 | 0.42 [0.41, 0.43] | [0.41, 0.43] | less steady | 0.42 [0.41, 0.43] | 0.00 [0.00, 0.00] | [0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 18383 | 20666 | 2282 [2207, 2358] | [2185, 2379] | less steady | 2316 [2242, 2390] | -33.78 [-44.24, -23.31] | [-46.62, -20.93] |
| P3 largest fall in real wealth ($, median) | 40752 | 33681 | -7072 [-8378, -5765] (boot -8414, -5814) | [-8378, -5765] | steadier | -295.54 [-391.64, -199.45] | -6776 [-8062, -5491] | [-8478, -5075] |
| P4 years to recover from an income shock (mean) | 3.24 | 3.50 | 0.26 [0.22, 0.29] | [0.22, 0.30] | less steady | 0.32 [0.28, 0.36] | -0.06 [-0.07, -0.04] | [-0.08, -0.04] |
| P5 % pushed below the basket line in a recession year | 10.38 | 5.57 | -4.81 [-5.36, -4.25] (boot -5.37, -4.25) | [-5.49, -4.13] | steadier | -4.93 [-5.49, -4.38] | 0.13 [0.07, 0.19] | [0.07, 0.19] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -20.03 [-20.38, -19.68] | -20.09 [-20.44, -19.74] | -0.16 [-0.20, -0.13] | -0.10 [-0.13, -0.08] |
| pov | -10.86 [-11.22, -10.50] | -10.29 [-10.63, -9.96] | 0.64 [0.45, 0.83] | 0.08 [-0.04, 0.20] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.41 [0.40, 0.42] | 0.41 [0.40, 0.42] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP2q1 | 2401 [2236, 2565] | 2401 [2237, 2564] | -26.80 [-41.35, -12.25] | -26.86 [-41.99, -11.72] |
| stP2q3 | 2044 [1876, 2212] | 2053 [1888, 2218] | -36.77 [-53.59, -19.95] | -45.82 [-66.43, -25.21] |
| stP2q5 | 2791 [2562, 3020] | 2943 [2715, 3171] | 2844 [2224, 3464] | 2691 [2086, 3297] |
| stP3q1 | 4710 [4286, 5134] | 5813 [5445, 6181] | 2746 [2433, 3059] | 1643 [1284, 2001] |
| stP3q3 | -6524 [-7680, -5368] | -6281 [-6820, -5742] | 33252 [28633, 37870] | 33009 [28513, 37505] |
| stP3q5 | -9797 [-12671, -6924] | 0.00 [0.00, 0.00] | 158611 [137544, 179677] | 148813 [128929, 168698] |
| stP3t1 | -54479 [-105447, -3511] | 0.00 [0.00, 0.00] | 5915506 [3747570, 8083443] | 5861027 [3699001, 8023053] |
| stP5r | -1.49 [-1.88, -1.10] | 0.00 [0.00, 0.00] | 5.48 [4.77, 6.19] | 3.99 [3.46, 4.52] |
| rkRec3 | -0.30 [-0.68, 0.08] | 0.06 [-0.33, 0.46] | 0.54 [0.41, 0.67] | 0.18 [0.06, 0.29] |
| rkDdB | 39.92 [34.19, 45.65] | 11.40 [10.28, 12.52] | 148.60 [129.19, 168.01] | 177.12 [153.83, 200.41] |
| rkDdB30 | 5.67 [4.88, 6.45] | 10.17 [9.35, 10.98] | 37.18 [32.80, 41.55] | 32.68 [28.82, 36.54] |
| rkDdW | -1.78 [-2.10, -1.45] | -0.05 [-0.07, -0.03] | 10.04 [8.73, 11.34] | 8.31 [7.22, 9.41] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 2.55 | 2.66 |
| cbIst | 2.23 | 2.36 |
| cbFloor | 14.20 | 14.10 |
| cbQ | 6.36 | 6.07 |
| cbQmax | 21.79 | 23.65 |
| cbM | -0.64 | -0.69 |
| cbRfY | 0.86 | 1.05 |
| cbRfSh | 60.94 | 64.46 |
| cbU | -0.35 | -0.33 |
| cbA | 51193 | 53291 |
| cbN | 10404 | 14036 |
| cbF | -3186 | -1795 |
| cbR | 5941 | 5626 |
| fsQ | 922.28 | 320.78 |
| fsN | 21.98 | 9.53 |
| fsRec | 15.48 | 15.64 |
| fsOut | 5.76 | 7.78 |
| fsBuyG | 4896 | 1282 |
| fsGap | -0.00 | 0.00 |
| fsS0 | 0.01 | 0.12 |
| fsS1 | 9.13 | 19.19 |
| fsS2 | 52.37 | 58.80 |
| fsS3 | 35.63 | 21.58 |
| fsS4 | 2.87 | 0.31 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.12 | 2.13 |
| fsB1 | 1.19 | 3.92 |
| fsB2 | 2.80 | 7.34 |
| fsB3 | 7.30 | 11.57 |
| fsB4 | 13.90 | 14.85 |
| fsB5 | 36.25 | 30.19 |
| fsB6 | 37.44 | 30.00 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.41 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

## Stress

Engine: 5f11ceb0a5fea4d62f7c8bc024e4896b17fda723; command `node dev/tools/s74_pilot.js st 100`; 100 seeds.

### C2.2

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.52 | 0.52 [0.51, 0.53] | [0.50, 0.53] | less steady | 0.52 [0.51, 0.53] | 0.00 [0.00, 0.00] | [0.00, 0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 18383 | 27511 | 9127 [8976, 9279] | [8927, 9328] | less steady | 9178 [9027, 9329] | -50.78 [-62.57, -39.00] | [-65.89, -35.67] |
| P3 largest fall in real wealth ($, median) | 40752 | 903.13 | -39849 [-45001, -34697] (boot -44842, -34939) | [-45759, -33940] | steadier | -295.54 [-391.64, -199.45] | -39554 [-44683, -34424] | [-46343, -32764] |
| P4 years to recover from an income shock (mean) | 3.24 | 3.36 | 0.11 [0.08, 0.15] | [0.08, 0.15] | less steady | 0.17 [0.13, 0.22] | -0.06 [-0.08, -0.04] | [-0.08, -0.04] |
| P5 % pushed below the basket line in a recession year | 10.38 | 0.85 | -9.53 [-10.40, -8.66] (boot -10.40, -8.62) | [-10.60, -8.46] | steadier | -9.72 [-10.61, -8.84] | 0.19 [0.14, 0.25] | [0.13, 0.26] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -40.42 [-40.85, -39.99] | -40.57 [-41.02, -40.13] | -0.16 [-0.20, -0.13] | -0.01 [-0.01, -0.00] |
| pov | -25.95 [-26.34, -25.55] | -25.32 [-25.70, -24.93] | 0.64 [0.45, 0.83] | 0.01 [-0.00, 0.03] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1p | 0.51 [0.50, 0.52] | 0.51 [0.50, 0.52] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP2q1 | 9345 [9057, 9634] | 9340 [9052, 9629] | -26.80 [-41.35, -12.25] | -22.09 [-34.19, -10.00] |
| stP2q3 | 8966 [8678, 9255] | 8951 [8661, 9241] | -36.77 [-53.59, -19.95] | -21.01 [-40.65, -1.37] |
| stP2q5 | 9174 [8775, 9572] | 9452 [9054, 9850] | 2844 [2224, 3464] | 2566 [1960, 3171] |
| stP3q1 | -3670 [-4021, -3320] | -924.73 [-1128, -721.46] | 2746 [2433, 3059] | 0.00 [0.00, 0.00] |
| stP3q3 | -39002 [-43613, -34391] | -6314 [-6860, -5767] | 33252 [28633, 37870] | 563.97 [298.15, 829.78] |
| stP3q5 | -58444 [-66660, -50227] | 0.00 [0.00, 0.00] | 158611 [137544, 179677] | 100167 [86105, 114229] |
| stP3t1 | -123650 [-167157, -80143] | 0.00 [0.00, 0.00] | 5915506 [3747570, 8083443] | 5791856 [3638815, 7944898] |
| stP5r | -4.82 [-5.49, -4.15] | 0.00 [0.00, 0.00] | 5.48 [4.77, 6.19] | 0.66 [0.50, 0.82] |
| rkRec3 | 3.40 [2.94, 3.86] | 3.86 [3.39, 4.33] | 0.54 [0.41, 0.67] | 0.08 [0.01, 0.15] |
| rkDdB | -138.25 [-155.89, -120.61] | -4.37 [-4.74, -4.01] | 148.60 [129.19, 168.01] | 14.73 [11.98, 17.48] |
| rkDdB30 | -31.00 [-32.73, -29.27] | -18.97 [-19.70, -18.24] | 37.18 [32.80, 41.55] | 25.15 [22.14, 28.15] |
| rkDdW | -9.84 [-11.12, -8.57] | -0.05 [-0.07, -0.03] | 10.04 [8.73, 11.34] | 0.25 [0.18, 0.31] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 2.55 | 2.78 |
| cbIst | 2.23 | 2.50 |
| cbFloor | 14.20 | 13.65 |
| cbQ | 6.36 | 5.70 |
| cbQmax | 21.79 | 21.83 |
| cbM | -0.64 | -0.63 |
| cbRfY | 0.86 | 1.07 |
| cbRfSh | 60.94 | 64.86 |
| cbU | -0.35 | -0.30 |
| cbA | 51193 | 51881 |
| cbN | 10404 | 25472 |
| cbF | -3186 | -291.70 |
| cbR | 5941 | 5464 |
| fsQ | 922.28 | 23.02 |
| fsN | 21.98 | 0.90 |
| fsRec | 15.48 | 15.02 |
| fsOut | 5.76 | 2.47 |
| fsBuyG | 4896 | 130.56 |
| fsGap | -0.00 | 0.00 |
| fsS0 | 0.01 | 0.04 |
| fsS1 | 9.13 | 40.59 |
| fsS2 | 52.37 | 50.07 |
| fsS3 | 35.63 | 9.30 |
| fsS4 | 2.87 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.12 | 3.68 |
| fsB1 | 1.19 | 6.81 |
| fsB2 | 2.80 | 11.64 |
| fsB3 | 7.30 | 15.66 |
| fsB4 | 13.90 | 16.30 |
| fsB5 | 36.25 | 26.51 |
| fsB6 | 37.44 | 19.40 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.51 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

### release design

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.24 | 0.24 [0.23, 0.25] | [0.23, 0.25] | less steady | 0.24 [0.23, 0.24] | 0.01 [0.00, 0.01] | [0.00, 0.01] |
| P2 spread of yearly changes in real cash income ($, mean) | 18383 | 18735 | 351.98 [315.24, 388.73] | [304.87, 399.10] | less steady | 364.54 [328.59, 400.48] | -12.55 [-18.47, -6.63] | [-19.34, -5.76] |
| P3 largest fall in real wealth ($, median) | 40752 | 38182 | -2570 [-3222, -1918] (boot -3224, -1968) | [-3222, -1918] | steadier | -274.76 [-361.62, -187.90] | -2295 [-2938, -1653] | [-3146, -1445] |
| P4 years to recover from an income shock (mean) | 3.24 | 3.44 | 0.19 [0.16, 0.22] | [0.16, 0.23] | less steady | 0.23 [0.20, 0.27] | -0.04 [-0.05, -0.02] | [-0.06, -0.02] |
| P5 % pushed below the basket line in a recession year | 10.38 | 7.24 | -3.13 [-3.52, -2.75] (boot -3.52, -2.74) | [-3.61, -2.66] | steadier | -3.18 [-3.56, -2.79] | 0.04 [-0.01, 0.10] | [-0.01, 0.10] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -7.80 [-8.03, -7.57] | -7.83 [-8.06, -7.60] | -0.16 [-0.20, -0.13] | -0.14 [-0.17, -0.11] |
| pov | -3.22 [-3.51, -2.94] | -3.05 [-3.33, -2.76] | 0.64 [0.45, 0.83] | 0.47 [0.30, 0.64] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.24 [0.23, 0.24] | 0.23 [0.22, 0.24] | 0.00 [0.00, 0.00] | 0.01 [0.00, 0.01] |
| stP2q1 | 518.11 [429.83, 606.39] | 521.08 [432.89, 609.27] | -26.80 [-41.35, -12.25] | -29.77 [-45.20, -14.34] |
| stP2q3 | 207.04 [114.07, 300.01] | 212.79 [120.58, 305.01] | -36.77 [-53.59, -19.95] | -42.52 [-60.87, -24.18] |
| stP2q5 | 467.89 [361.33, 574.46] | 515.78 [413.18, 618.38] | 2844 [2224, 3464] | 2796 [2184, 3409] |
| stP3q1 | 1645 [1414, 1875] | 2235 [2002, 2468] | 2746 [2433, 3059] | 2155 [1840, 2470] |
| stP3q3 | -3161 [-3917, -2404] | -4492 [-4886, -4098] | 33252 [28633, 37870] | 34583 [29905, 39262] |
| stP3q5 | -1472 [-3356, 411.97] | 0.00 [0.00, 0.00] | 158611 [137544, 179677] | 157139 [136301, 177977] |
| stP3t1 | 36753 [-44440, 117946] | 0.00 [0.00, 0.00] | 5915506 [3747570, 8083443] | 5952259 [3773931, 8130588] |
| stP5r | -0.83 [-1.13, -0.54] | 0.00 [0.00, 0.00] | 5.48 [4.77, 6.19] | 4.65 [4.05, 5.25] |
| rkRec3 | 0.84 [0.52, 1.16] | 0.89 [0.60, 1.18] | 0.54 [0.41, 0.67] | 0.49 [0.35, 0.64] |
| rkDdB | 7.10 [4.98, 9.22] | 1.18 [0.84, 1.51] | 148.60 [129.19, 168.01] | 154.52 [134.27, 174.78] |
| rkDdB30 | 1.11 [0.82, 1.40] | -0.12 [-0.56, 0.31] | 37.18 [32.80, 41.55] | 38.41 [33.93, 42.89] |
| rkDdW | -0.64 [-0.80, -0.47] | -0.05 [-0.07, -0.03] | 10.04 [8.73, 11.34] | 9.45 [8.21, 10.69] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 2.55 | 2.57 |
| cbIst | 2.23 | 2.26 |
| cbFloor | 14.20 | 14.20 |
| cbQ | 6.36 | 6.49 |
| cbQmax | 21.79 | 24.96 |
| cbM | -0.64 | -0.69 |
| cbRfY | 0.86 | 0.93 |
| cbRfSh | 60.94 | 62.39 |
| cbU | -0.35 | -0.34 |
| cbA | 51193 | 52697 |
| cbN | 10404 | 11281 |
| cbF | -3186 | -2805 |
| cbR | 5941 | 5691 |
| fsQ | 922.28 | 664.14 |
| fsN | 21.98 | 17.36 |
| fsRec | 15.48 | 15.44 |
| fsOut | 5.76 | 6.31 |
| fsBuyG | 4896 | 3295 |
| fsGap | -0.00 | -0.00 |
| fsS0 | 0.01 | 0.05 |
| fsS1 | 9.13 | 12.02 |
| fsS2 | 52.37 | 54.57 |
| fsS3 | 35.63 | 31.62 |
| fsS4 | 2.87 | 1.74 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.12 | 1.42 |
| fsB1 | 1.19 | 1.82 |
| fsB2 | 2.80 | 3.92 |
| fsB3 | 7.30 | 8.48 |
| fsB4 | 13.90 | 14.21 |
| fsB5 | 36.25 | 34.66 |
| fsB6 | 37.44 | 35.49 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.24 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

## Reference

Engine: 5f11ceb0a5fea4d62f7c8bc024e4896b17fda723; command `node dev/tools/s74_pilot.js ref 100`; 100 seeds.

### C2.2

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.52 | 0.52 [0.51, 0.53] | [0.51, 0.54] | less steady | 0.53 [0.52, 0.54] | -0.00 [-0.00, -0.00] | [-0.00, -0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 20127 | 34247 | 14120 [13910, 14330] | [13842, 14398] | less steady | 14118 [13908, 14327] | 2.69 [-2.88, 8.26] | [-3.70, 9.08] |
| P3 largest fall in real wealth ($, median) | 212.04 | 0.00 | -212.04 [-280.06, -144.02] (boot -278.22, -144.98) | [-290.06, -134.02] | steadier | -25.48 [-49.51, -1.45] | -186.56 [-243.04, -130.09] | [-258.97, -114.15] |
| P4 years to recover from an income shock (mean) | 3.75 | 3.27 | -0.48 [-0.52, -0.44] | [-0.52, -0.44] | steadier | -0.45 [-0.49, -0.41] | -0.03 [-0.04, -0.02] | [-0.04, -0.02] |
| P5 % pushed below the basket line in a recession year | 0.00 | 0.00 | 0.00 [0.00, 0.00] (boot 0.00, 0.00) | [0.00, 0.00] | no measurable difference | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | [0.00, 0.00] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -32.89 [-33.25, -32.54] | -32.83 [-33.18, -32.47] | 0.07 [0.06, 0.08] | 0.00 [0.00, 0.00] |
| pov | -23.72 [-24.05, -23.38] | -22.32 [-22.65, -22.00] | 1.40 [1.28, 1.52] | 0.01 [0.00, 0.02] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [-0.00, 0.00] |
| stP1p | 0.52 [0.51, 0.53] | 0.53 [0.52, 0.54] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP2q1 | 14673 [14190, 15156] | 14675 [14192, 15157] | -1.75 [-2.10, -1.39] | -3.55 [-9.08, 1.98] |
| stP2q3 | 13748 [13309, 14188] | 13749 [13311, 14188] | -3.19 [-3.95, -2.43] | -3.94 [-11.53, 3.65] |
| stP2q5 | 14528 [13974, 15082] | 14522 [13966, 15077] | -3.27 [-3.74, -2.80] | 2.79 [-20.55, 26.12] |
| stP3q1 | -1325 [-1405, -1245] | -310.32 [-427.76, -192.88] | 1015 [927.72, 1101] | 0.00 [0.00, 0.00] |
| stP3q3 | -5475 [-6205, -4745] | -5182 [-5862, -4502] | 292.83 [179.97, 405.68] | 0.00 [0.00, 0.00] |
| stP3q5 | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP3t1 | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP5r | 0.18 [0.13, 0.23] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.18 [0.13, 0.23] |
| rkRec3 | 1.94 [1.51, 2.37] | 1.73 [1.29, 2.16] | -0.14 [-0.26, -0.03] | 0.07 [0.04, 0.10] |
| rkDdB | -1.89 [-2.20, -1.57] | -1.76 [-2.06, -1.45] | 0.13 [0.08, 0.18] | 0.00 [0.00, 0.00] |
| rkDdB30 | -6.72 [-7.52, -5.91] | -6.65 [-7.46, -5.83] | 0.39 [0.32, 0.46] | 0.32 [0.27, 0.38] |
| rkDdW | -0.03 [-0.05, -0.02] | -0.00 [-0.01, 0.00] | 0.03 [0.02, 0.04] | 0.00 [0.00, 0.00] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 0.00 | 0.29 |
| cbIst | -0.03 | 0.20 |
| cbFloor | 100.00 | 53.75 |
| cbQ | 0.34 | 1.65 |
| cbQmax | 0.34 | 5.15 |
| cbM | 0.00 | -0.05 |
| cbRfY | 0.00 | 0.00 |
| cbRfSh | 0.00 | 0.00 |
| cbU | 0.00 | 0.04 |
| cbA | 0.00 | 497.24 |
| cbN | 0.00 | 6928 |
| cbF | -2187 | -217.30 |
| cbR | 0.00 | 0.00 |
| fsQ | 564.52 | 13.91 |
| fsN | 18.22 | 0.68 |
| fsRec | 0.00 | 0.00 |
| fsOut | 3.68 | 1.16 |
| fsBuyG | 3498 | 90.80 |
| fsGap | 0.00 | 0.00 |
| fsS0 | 0.01 | 0.11 |
| fsS1 | 7.86 | 43.65 |
| fsS2 | 51.47 | 49.94 |
| fsS3 | 38.35 | 6.30 |
| fsS4 | 2.31 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.51 | 3.79 |
| fsB1 | 1.33 | 6.77 |
| fsB2 | 3.14 | 11.48 |
| fsB3 | 8.11 | 15.58 |
| fsB4 | 14.90 | 16.53 |
| fsB5 | 36.40 | 27.19 |
| fsB6 | 34.61 | 18.65 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.52 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

### release design

**Primary outcomes.** Levels are the no-programme run with the central bank on; E the programme's effect with it on (H: Holm-adjusted); X the interaction.

| outcome | no programme, cb on | programme, cb on | E (95%) | E (H) | verdict | E with cb off | X (95%) | X (H) |
|---|---|---|---|---|---|---|---|---|
| P1 spread of the basket price level's yearly change (points) | 0.00 | 0.39 | 0.39 [0.38, 0.40] | [0.38, 0.40] | less steady | 0.39 [0.38, 0.40] | -0.00 [-0.00, -0.00] | [-0.00, -0.00] |
| P2 spread of yearly changes in real cash income ($, mean) | 20127 | 22610 | 2484 [2406, 2561] | [2384, 2583] | less steady | 2473 [2395, 2551] | 10.47 [3.06, 17.88] | [1.97, 18.97] |
| P3 largest fall in real wealth ($, median) | 212.04 | 0.00 | -212.04 [-280.06, -144.02] (boot -278.22, -144.98) | [-290.06, -134.02] | steadier | -25.48 [-49.51, -1.45] | -186.56 [-243.04, -130.09] | [-261.31, -111.81] |
| P4 years to recover from an income shock (mean) | 3.75 | 3.89 | 0.14 [0.11, 0.17] | [0.10, 0.18] | less steady | 0.17 [0.14, 0.20] | -0.03 [-0.04, -0.02] | [-0.04, -0.01] |
| P5 % pushed below the basket line in a recession year | 0.00 | 0.00 | 0.00 [0.00, 0.00] (boot 0.00, 0.00) | [0.00, 0.00] | no measurable difference | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | [0.00, 0.00] |

**Secondary outcomes** (E, E with cb off; C: the central bank's effect, cb minus off, in the no-programme run and in the programme run).

| key | E | E, cb off | C, no programme | C, programme |
|---|---|---|---|---|
| fgt0PY | -22.16 [-22.47, -21.85] | -22.13 [-22.44, -21.83] | 0.07 [0.06, 0.08] | 0.05 [0.04, 0.05] |
| pov | -15.99 [-16.36, -15.62] | -15.02 [-15.35, -14.68] | 1.40 [1.28, 1.52] | 0.43 [0.35, 0.50] |
| endoAnn | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP1o | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | -0.00 [-0.00, 0.00] |
| stP1p | 0.39 [0.38, 0.40] | 0.39 [0.38, 0.40] | 0.00 [0.00, 0.00] | -0.00 [-0.00, -0.00] |
| stP2q1 | 2735 [2551, 2920] | 2739 [2556, 2923] | -1.75 [-2.10, -1.39] | -5.74 [-10.44, -1.03] |
| stP2q3 | 2146 [1956, 2336] | 2144 [1954, 2333] | -3.19 [-3.95, -2.43] | -1.00 [-7.26, 5.26] |
| stP2q5 | 3157 [2908, 3406] | 3101 [2851, 3351] | -3.27 [-3.74, -2.80] | 52.93 [20.47, 85.39] |
| stP3q1 | -705.50 [-830.58, -580.42] | 61.13 [-94.71, 216.98] | 1015 [927.72, 1101] | 247.95 [183.78, 312.12] |
| stP3q3 | -5475 [-6205, -4745] | -5182 [-5862, -4502] | 292.83 [179.97, 405.68] | 0.00 [0.00, 0.00] |
| stP3q5 | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP3t1 | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| stP5r | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| rkRec3 | -0.54 [-0.90, -0.19] | -0.67 [-1.03, -0.30] | -0.14 [-0.26, -0.03] | -0.02 [-0.08, 0.04] |
| rkDdB | -1.39 [-1.72, -1.06] | -1.70 [-2.00, -1.40] | 0.13 [0.08, 0.18] | 0.43 [0.25, 0.62] |
| rkDdB30 | 0.07 [-0.64, 0.77] | -0.61 [-1.33, 0.11] | 0.39 [0.32, 0.46] | 1.07 [0.94, 1.20] |
| rkDdW | -0.03 [-0.05, -0.02] | -0.00 [-0.01, 0.00] | 0.03 [0.02, 0.04] | 0.00 [0.00, 0.00] |

**The rule and forced sales** (means over seeds, central-bank arm).

| key | no programme | programme |
|---|---|---|
| cbI | 0.00 | 0.23 |
| cbIst | -0.03 | 0.15 |
| cbFloor | 100.00 | 53.05 |
| cbQ | 0.34 | 1.46 |
| cbQmax | 0.34 | 4.61 |
| cbM | 0.00 | -0.03 |
| cbRfY | 0.00 | 0.00 |
| cbRfSh | 0.00 | 0.00 |
| cbU | 0.00 | 0.03 |
| cbA | 0.00 | 262.26 |
| cbN | 0.00 | 3308 |
| cbF | -2187 | -1078 |
| cbR | 0.00 | 0.00 |
| fsQ | 564.52 | 135.15 |
| fsN | 18.22 | 5.59 |
| fsRec | 0.00 | 0.00 |
| fsOut | 3.68 | 3.37 |
| fsBuyG | 3498 | 719.18 |
| fsGap | 0.00 | -0.00 |
| fsS0 | 0.01 | 0.13 |
| fsS1 | 7.86 | 21.08 |
| fsS2 | 51.47 | 59.07 |
| fsS3 | 38.35 | 19.72 |
| fsS4 | 2.31 | 0.00 |
| fsS5 | 0.00 | 0.00 |
| fsS6 | 0.00 | 0.00 |
| fsB0 | 1.51 | 2.62 |
| fsB1 | 1.33 | 4.49 |
| fsB2 | 3.14 | 8.28 |
| fsB3 | 8.11 | 12.78 |
| fsB4 | 14.90 | 15.84 |
| fsB5 | 36.40 | 29.99 |
| fsB6 | 34.61 | 26.00 |

**Plain statement (programme run, central bank on):** the spread of the programme's own yearly price change is 0.39 points against 0.00 for outside inflation: the programme's own inflation is **the larger source of instability** here.

## Decision rule: does the programme's share of essentials damp what the central bank and outside shocks do to the cost of basic living?

- C2.2: P1 interaction below zero (Holm) in History false, Adverse false, Stress false; basket poverty not worse true. **Claim not supported.**
- release design: P1 interaction below zero (Holm) in History false, Adverse false, Stress false; basket poverty not worse true. **Claim not supported.**
