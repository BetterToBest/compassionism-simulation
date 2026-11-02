# Study O (S52): the outside supply shock, every preregistered table

PILOT: seeds 1-50, labelled pilot throughout; not figures of the model. Engine 98b6100. Analysis: `dev/tools/s52_shock.py` (prereg/2026-11-supply-shock-addendum.md).

Share of the shock reaching a group: the rise in its own money costs over the rise in the same basket at market prices, against the same run without the shock (same seed). 1 = the whole rise; 0 = none of it. 95% intervals: paired bootstrap over seeds.

## Reference, release row (released wages)

### Q14 (primary): share of the main shock reaching each group, during the shock (years 5-8), main reading (markup 25%, no local sourcing)

| Group | No programme | Programme | Programme, after the shock (years 9-19) |
|---|---|---|---|
| all adults | 100.0% (100.0 to 100.0) | 52.4% (52.1 to 52.6) | 51.9% (51.7 to 52.2) |
| PTF members | no adults | 55.9% (55.4 to 56.5) | 52.3% (51.2 to 53.5) |
| PTH members (not PTF) | no adults | 48.0% (47.1 to 48.9) | 47.1% (46.4 to 47.8) |
| other CCO participants | no adults | 44.3% (44.1 to 44.6) | 45.5% (45.2 to 45.8) |
| in none of the three | 100.0% (100.0 to 100.0) | 99.9% (99.9 to 99.9) | 99.8% (99.7 to 99.8) |
| chose not to take part | 100.0% (100.0 to 100.0) | 71.3% (70.6 to 72.0) | 69.8% (69.0 to 70.5) |

### Q15: PTF members (F) by markup share and local sourcing, during the main shock (local supply half as exposed; no pooling)

| Markup share | no local sourcing | 25% local | 50% local | all local |
|---|---|---|---|---|
| 0% | 60.1% (59.6 to 60.7) | 58.0% (57.5 to 58.6) | 55.9% (55.4 to 56.5) | 51.8% (51.2 to 52.3) |
| 25% | 55.9% (55.4 to 56.5) | 54.4% (53.8 to 54.9) | 52.8% (52.3 to 53.4) | 49.7% (49.2 to 50.2) |
| 50% | 51.8% (51.2 to 52.3) | 50.7% (50.2 to 51.3) | 49.7% (49.2 to 50.2) | 47.6% (47.1 to 48.2) |

Sensitivities (markup 25%): local supply fully protected (kap 0), and a three-year price reserve (pool 3).

| Row | PTF members | all adults |
|---|---|---|
| m25.s25.k0.p1 | 52.8% (52.3 to 53.4) | 51.7% (51.5 to 51.9) |
| m25.s50.k0.p1 | 49.7% (49.2 to 50.2) | 51.0% (50.8 to 51.3) |
| m25.s100.k0.p1 | 43.5% (42.9 to 44.0) | 49.7% (49.5 to 50.0) |
| m25.s0.k50.p3 | 54.1% (53.5 to 54.6) | 52.0% (51.7 to 52.2) |
| m25.s50.k50.p3 | 51.4% (50.9 to 52.0) | 51.4% (51.2 to 51.6) |

### Protection by part of the design (Analysis; decision rules 1, 3)

- PTF (markup removal, main reading): PTF members' share without markup removal less with it: 4.2% (4.2 to 4.2) (rule 1: protects if the interval is above zero).
- BU: adults in none of the three less other CCO participants: 55.6% (55.4 to 55.8).
- PTH: other CCO participants less PTH members (not PTF): -3.7% (-4.7 to -2.7) (rule 3: protects if the interval is above zero; the groups differ in who they are).

### Q16: basket poverty and volatility, main shock, main reading: shocked less unshocked (points), and for the programme against no programme

| Measure | No programme | Programme | Programme less no programme |
|---|---|---|---|
| basket poverty during the shock, all | +1.70 (+1.58 to +1.82) | +0.89 (+0.80 to +0.98) | -0.81 (-0.97 to -0.65) |
| basket poverty after the shock, all | +1.70 (+1.62 to +1.78) | +0.93 (+0.86 to +1.00) | -0.77 (-0.89 to -0.66) |
| basket poverty during, chose not to take part (no harm, rule 4) | +1.74 (+1.55 to +1.94) | +1.21 (+1.04 to +1.39) | -0.53 (-0.81 to -0.22) |
| basket poverty after, chose not to take part | +1.74 (+1.60 to +1.90) | +1.33 (+1.20 to +1.47) | -0.41 (-0.64 to -0.21) |
| basket poverty during, PTF members | +0.00 (+0.00 to +0.00) | +0.80 (+0.63 to +0.99) | +0.80 (+0.63 to +0.99) |
| basket poverty over the run | +1.28 (+1.22 to +1.33) | +0.69 (+0.64 to +0.74) | -0.59 (-0.67 to -0.51) |
| too little wealth at year 20 | +0.82 (+0.69 to +0.96) | +3.02 (+2.77 to +3.28) | +2.20 (+1.91 to +2.50) |
| volatility of costs, all (points of yearly change) | +0.36 (+0.35 to +0.36) | +0.25 (+0.25 to +0.26) | -0.11 (-0.11 to -0.10) |
| volatility, chose not to take part | +0.36 (+0.35 to +0.36) | +0.31 (+0.31 to +0.32) | -0.05 (-0.06 to -0.04) |
| too little wealth at year 20, participants | +0.84 (+0.69 to +0.98) | +3.04 (+2.77 to +3.33) | +2.20 (+1.90 to +2.53) |
| too little wealth at year 20, non-participants | +0.77 (+0.55 to +1.00) | +2.97 (+2.51 to +3.41) | +2.20 (+1.70 to +2.66) |
| median real wealth at year 20 ($) | -10676.22 (-11062.54 to -10328.93) | -2160.06 (-2240.78 to -2087.49) | +8516.16 (+8169.42 to +8886.55) |
| participation in year 19 (%) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) |
| BU cost a person-year ($) | +0.00 (+0.00 to +0.00) | +34.22 (+33.52 to +34.91) | +34.22 (+33.52 to +34.91) |
| programme inflation a year (points) | +0.14 (+0.14 to +0.14) | +1.26 (+1.25 to +1.28) | +1.12 (+1.11 to +1.13) |
| price level at year 20 (% of the unshocked level) | +2.73 (+2.73 to +2.74) | +17.21 (+17.07 to +17.34) | +14.48 (+14.34 to +14.61) |

### Other shock paths (programme rows: main reading and 50% local sourcing)

| Path | No programme, all adults | Programme, all | PTF members, main reading | PTF members, 50% local | basket poverty during, programme less no programme (points) |
|---|---|---|---|---|---|
| main shock (rise 32.8%, 88% kept) | 100.0% (100.0 to 100.0) | 52.4% (52.1 to 52.6) | 55.9% (55.4 to 56.5) | 52.8% (52.3 to 53.4) | -0.81 (-0.97 to -0.65) |
| rise 24.6% | 100.0% (100.0 to 100.0) | 52.4% (52.1 to 52.6) | 55.9% (55.4 to 56.5) | 52.8% (52.3 to 53.4) | -0.59 (-0.73 to -0.44) |
| rise 37.3% | 100.0% (100.0 to 100.0) | 52.4% (52.1 to 52.6) | 55.9% (55.4 to 56.5) | 52.8% (52.3 to 53.4) | -0.90 (-1.06 to -0.73) |
| rise 65.5% (beyond history) | 100.0% (100.0 to 100.0) | 52.4% (52.1 to 52.6) | 55.9% (55.4 to 56.5) | 52.8% (52.3 to 53.3) | -1.34 (-1.54 to -1.16) |
| 51% kept | 100.0% (100.0 to 100.0) | 52.0% (51.8 to 52.2) | 55.6% (55.1 to 56.2) | 52.8% (52.3 to 53.3) | -0.68 (-0.82 to -0.54) |
| all kept | 100.0% (100.0 to 100.0) | 52.5% (52.2 to 52.7) | 56.0% (55.5 to 56.6) | 52.8% (52.3 to 53.4) | -0.83 (-0.99 to -0.67) |

## Reference, C2.2 design (CPS yardstick)

### Q14 (primary): share of the main shock reaching each group, during the shock (years 5-8), main reading (markup 25%, no local sourcing)

| Group | No programme | Programme | Programme, after the shock (years 9-19) |
|---|---|---|---|
| all adults | 100.0% (100.0 to 100.0) | 20.7% (20.5 to 20.8) | 30.1% (30.0 to 30.1) |
| PTF members | no adults | 29.2% (28.7 to 29.8) | 29.1% (29.0 to 29.2) |
| PTH members (not PTF) | no adults | 17.4% (17.0 to 17.9) | 29.9% (29.8 to 30.1) |
| other CCO participants | no adults | 18.6% (18.4 to 18.8) | 30.6% (30.5 to 30.7) |
| in none of the three | 100.0% (100.0 to 100.0) | no adults | no adults |
| chose not to take part | 100.0% (100.0 to 100.0) | 20.6% (20.2 to 21.0) | 30.0% (29.8 to 30.2) |

### Q15: PTF members (F) by markup share and local sourcing, during the main shock (local supply half as exposed; no pooling)

| Markup share | no local sourcing | 25% local | 50% local | all local |
|---|---|---|---|---|
| 0% | 31.6% (31.0 to 32.2) | 30.4% (29.8 to 31.0) | 29.2% (28.7 to 29.8) | 26.9% (26.4 to 27.5) |
| 25% | 29.2% (28.7 to 29.8) | 28.4% (27.8 to 28.9) | 27.5% (27.0 to 28.1) | 25.7% (25.3 to 26.3) |
| 50% | 26.9% (26.4 to 27.5) | 26.3% (25.8 to 26.9) | 25.7% (25.3 to 26.3) | 24.6% (24.1 to 25.1) |

Sensitivities (markup 25%): local supply fully protected (kap 0), and a three-year price reserve (pool 3).

| Row | PTF members | all adults |
|---|---|---|
| m25.s25.k0.p1 | 27.5% (27.0 to 28.1) | 20.3% (20.1 to 20.4) |
| m25.s50.k0.p1 | 25.7% (25.3 to 26.3) | 19.9% (19.7 to 20.0) |
| m25.s100.k0.p1 | 22.2% (21.8 to 22.7) | 19.1% (18.9 to 19.2) |
| m25.s0.k50.p3 | 28.1% (27.6 to 28.7) | 20.4% (20.2 to 20.5) |
| m25.s50.k50.p3 | 26.6% (26.1 to 27.2) | 20.0% (19.9 to 20.2) |

### Protection by part of the design (Analysis; decision rules 1, 3)

- PTF (markup removal, main reading): PTF members' share without markup removal less with it: 2.3% (2.3 to 2.4) (rule 1: protects if the interval is above zero).
- BU: no adult is outside all three in this design (automatic distribution), so the BU's share cannot be read from the groups.
- PTH: other CCO participants less PTH members (not PTF): 1.2% (0.7 to 1.7) (rule 3: protects if the interval is above zero; the groups differ in who they are).

### Q16: basket poverty and volatility, main shock, main reading: shocked less unshocked (points), and for the programme against no programme

| Measure | No programme | Programme | Programme less no programme |
|---|---|---|---|
| basket poverty during the shock, all | +1.06 (+0.97 to +1.16) | +0.12 (+0.09 to +0.14) | -0.94 (-1.05 to -0.84) |
| basket poverty after the shock, all | +0.99 (+0.94 to +1.05) | +0.08 (+0.07 to +0.10) | -0.91 (-0.97 to -0.85) |
| basket poverty during, chose not to take part (no harm, rule 4) | +1.04 (+0.90 to +1.19) | +0.09 (+0.03 to +0.15) | -0.96 (-1.12 to -0.80) |
| basket poverty after, chose not to take part | +1.00 (+0.90 to +1.09) | +0.08 (+0.05 to +0.11) | -0.92 (-1.01 to -0.81) |
| basket poverty during, PTF members | +0.00 (+0.00 to +0.00) | +0.15 (+0.08 to +0.23) | +0.15 (+0.08 to +0.23) |
| basket poverty over the run | +0.76 (+0.72 to +0.80) | +0.07 (+0.06 to +0.08) | -0.69 (-0.73 to -0.65) |
| too little wealth at year 20 | +0.57 (+0.44 to +0.70) | +0.28 (+0.20 to +0.35) | -0.30 (-0.44 to -0.15) |
| volatility of costs, all (points of yearly change) | +0.21 (+0.21 to +0.22) | +0.14 (+0.14 to +0.15) | -0.07 (-0.07 to -0.06) |
| volatility, chose not to take part | +0.21 (+0.21 to +0.22) | +0.15 (+0.14 to +0.15) | -0.07 (-0.07 to -0.06) |
| too little wealth at year 20, participants | +0.54 (+0.42 to +0.67) | +0.30 (+0.21 to +0.40) | -0.24 (-0.38 to -0.10) |
| too little wealth at year 20, non-participants | +0.67 (+0.43 to +0.91) | +0.20 (+0.10 to +0.31) | -0.47 (-0.75 to -0.18) |
| median real wealth at year 20 ($) | -17237.26 (-17620.42 to -16828.38) | -9635.46 (-9836.56 to -9432.07) | +7601.80 (+7222.62 to +7985.56) |
| participation in year 19 (%) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) |
| BU cost a person-year ($) | +0.00 (+0.00 to +0.00) | +147.67 (+146.15 to +149.27) | +147.67 (+146.15 to +149.27) |
| programme inflation a year (points) | +0.14 (+0.14 to +0.14) | +1.29 (+1.27 to +1.30) | +1.14 (+1.13 to +1.15) |
| price level at year 20 (% of the unshocked level) | +2.77 (+2.76 to +2.77) | +19.40 (+19.23 to +19.57) | +16.63 (+16.46 to +16.80) |

### Other shock paths (programme rows: main reading and 50% local sourcing)

| Path | No programme, all adults | Programme, all | PTF members, main reading | PTF members, 50% local | basket poverty during, programme less no programme (points) |
|---|---|---|---|---|---|
| main shock (rise 32.8%, 88% kept) | 100.0% (100.0 to 100.0) | 20.7% (20.5 to 20.8) | 29.2% (28.7 to 29.8) | 27.5% (27.0 to 28.1) | -0.94 (-1.05 to -0.84) |
| rise 24.6% | 100.0% (100.0 to 100.0) | 20.7% (20.5 to 20.8) | 29.2% (28.6 to 29.8) | 27.4% (26.9 to 28.0) | -0.73 (-0.82 to -0.63) |
| rise 37.3% | 100.0% (100.0 to 100.0) | 20.7% (20.5 to 20.8) | 29.3% (28.7 to 29.9) | 27.5% (27.0 to 28.1) | -1.06 (-1.17 to -0.95) |
| rise 65.5% (beyond history) | 100.0% (100.0 to 100.0) | 20.8% (20.6 to 20.9) | 29.5% (28.9 to 30.1) | 27.7% (27.2 to 28.2) | -1.76 (-1.92 to -1.60) |
| 51% kept | 100.0% (100.0 to 100.0) | 21.8% (21.7 to 22.0) | 29.3% (28.8 to 29.9) | 27.8% (27.3 to 28.3) | -0.82 (-0.92 to -0.73) |
| all kept | 100.0% (100.0 to 100.0) | 20.4% (20.2 to 20.5) | 29.2% (28.7 to 29.8) | 27.4% (26.9 to 28.0) | -0.99 (-1.10 to -0.88) |

## Adverse, release row (released wages)

### Q14 (primary): share of the main shock reaching each group, during the shock (years 5-8), main reading (markup 25%, no local sourcing)

| Group | No programme | Programme | Programme, after the shock (years 9-19) |
|---|---|---|---|
| all adults | 100.0% (100.0 to 100.0) | 53.2% (53.0 to 53.5) | 54.4% (54.1 to 54.7) |
| PTF members | no adults | 56.5% (56.0 to 57.1) | 54.9% (54.1 to 55.7) |
| PTH members (not PTF) | no adults | 49.3% (48.5 to 50.2) | 49.5% (48.8 to 50.1) |
| other CCO participants | no adults | 45.4% (45.1 to 45.6) | 48.3% (48.1 to 48.6) |
| in none of the three | 100.0% (100.0 to 100.0) | 99.9% (99.9 to 99.9) | 99.8% (99.7 to 99.8) |
| chose not to take part | 100.0% (100.0 to 100.0) | 71.9% (71.2 to 72.6) | 71.5% (70.8 to 72.2) |

### Q15: PTF members (F) by markup share and local sourcing, during the main shock (local supply half as exposed; no pooling)

| Markup share | no local sourcing | 25% local | 50% local | all local |
|---|---|---|---|---|
| 0% | 60.7% (60.2 to 61.2) | 58.6% (58.1 to 59.1) | 56.5% (56.0 to 57.1) | 52.4% (51.9 to 52.9) |
| 25% | 56.5% (56.0 to 57.1) | 55.0% (54.4 to 55.5) | 53.4% (52.9 to 53.9) | 50.3% (49.8 to 50.9) |
| 50% | 52.4% (51.9 to 52.9) | 51.4% (50.8 to 51.9) | 50.3% (49.8 to 50.9) | 48.3% (47.7 to 48.8) |

Sensitivities (markup 25%): local supply fully protected (kap 0), and a three-year price reserve (pool 3).

| Row | PTF members | all adults |
|---|---|---|
| m25.s25.k0.p1 | 53.4% (52.9 to 53.9) | 52.6% (52.3 to 52.8) |
| m25.s50.k0.p1 | 50.3% (49.8 to 50.9) | 51.9% (51.7 to 52.1) |
| m25.s100.k0.p1 | 44.1% (43.6 to 44.7) | 50.6% (50.4 to 50.9) |
| m25.s0.k50.p3 | 54.8% (54.3 to 55.4) | 52.9% (52.7 to 53.1) |
| m25.s50.k50.p3 | 52.2% (51.6 to 52.7) | 52.3% (52.1 to 52.5) |

### Protection by part of the design (Analysis; decision rules 1, 3)

- PTF (markup removal, main reading): PTF members' share without markup removal less with it: 4.2% (4.1 to 4.2) (rule 1: protects if the interval is above zero).
- BU: adults in none of the three less other CCO participants: 54.6% (54.3 to 54.8).
- PTH: other CCO participants less PTH members (not PTF): -3.9% (-4.9 to -3.0) (rule 3: protects if the interval is above zero; the groups differ in who they are).

### Q16: basket poverty and volatility, main shock, main reading: shocked less unshocked (points), and for the programme against no programme

| Measure | No programme | Programme | Programme less no programme |
|---|---|---|---|
| basket poverty during the shock, all | +1.62 (+1.51 to +1.74) | +1.06 (+0.96 to +1.16) | -0.56 (-0.69 to -0.43) |
| basket poverty after the shock, all | +1.60 (+1.53 to +1.67) | +1.18 (+1.10 to +1.27) | -0.42 (-0.54 to -0.31) |
| basket poverty during, chose not to take part (no harm, rule 4) | +1.66 (+1.46 to +1.86) | +1.33 (+1.13 to +1.52) | -0.33 (-0.58 to -0.10) |
| basket poverty after, chose not to take part | +1.67 (+1.55 to +1.80) | +1.28 (+1.14 to +1.41) | -0.39 (-0.57 to -0.23) |
| basket poverty during, PTF members | +0.00 (+0.00 to +0.00) | +1.21 (+0.98 to +1.43) | +1.21 (+0.98 to +1.43) |
| basket poverty over the run | +1.21 (+1.16 to +1.25) | +0.86 (+0.80 to +0.92) | -0.34 (-0.41 to -0.27) |
| too little wealth at year 20 | +0.95 (+0.80 to +1.11) | +1.67 (+1.48 to +1.86) | +0.72 (+0.46 to +0.97) |
| volatility of costs, all (points of yearly change) | +0.40 (+0.39 to +0.40) | +0.52 (+0.51 to +0.52) | +0.12 (+0.11 to +0.13) |
| volatility, chose not to take part | +0.40 (+0.39 to +0.40) | +0.58 (+0.57 to +0.59) | +0.18 (+0.17 to +0.19) |
| too little wealth at year 20, participants | +1.00 (+0.82 to +1.18) | +1.79 (+1.57 to +2.00) | +0.79 (+0.49 to +1.09) |
| too little wealth at year 20, non-participants | +0.78 (+0.58 to +1.01) | +1.27 (+1.03 to +1.51) | +0.49 (+0.14 to +0.84) |
| median real wealth at year 20 ($) | -6615.51 (-6912.24 to -6341.12) | -850.47 (-909.07 to -792.29) | +5765.05 (+5487.88 to +6049.40) |
| participation in year 19 (%) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) |
| BU cost a person-year ($) | +0.00 (+0.00 to +0.00) | +32.00 (+31.46 to +32.57) | +32.00 (+31.46 to +32.57) |
| programme inflation a year (points) | +0.14 (+0.14 to +0.14) | +1.48 (+1.46 to +1.49) | +1.34 (+1.32 to +1.35) |
| price level at year 20 (% of the unshocked level) | +2.73 (+2.73 to +2.73) | +19.04 (+18.86 to +19.21) | +16.31 (+16.13 to +16.48) |

### Other shock paths (programme rows: main reading and 50% local sourcing)

| Path | No programme, all adults | Programme, all | PTF members, main reading | PTF members, 50% local | basket poverty during, programme less no programme (points) |
|---|---|---|---|---|---|
| main shock (rise 32.8%, 88% kept) | 100.0% (100.0 to 100.0) | 53.2% (53.0 to 53.5) | 56.5% (56.0 to 57.1) | 53.4% (52.9 to 53.9) | -0.56 (-0.69 to -0.43) |
| rise 24.6% | 100.0% (100.0 to 100.0) | 53.2% (53.0 to 53.5) | 56.5% (56.0 to 57.1) | 53.4% (52.9 to 53.9) | -0.44 (-0.56 to -0.32) |
| rise 37.3% | 100.0% (100.0 to 100.0) | 53.2% (53.0 to 53.5) | 56.5% (56.0 to 57.1) | 53.4% (52.9 to 54.0) | -0.66 (-0.79 to -0.53) |
| rise 65.5% (beyond history) | 100.0% (100.0 to 100.0) | 53.2% (53.0 to 53.5) | 56.5% (56.0 to 57.1) | 53.4% (52.9 to 54.0) | -1.11 (-1.28 to -0.94) |
| 51% kept | 100.0% (100.0 to 100.0) | 53.0% (52.7 to 53.2) | 56.3% (55.8 to 56.8) | 53.5% (53.0 to 54.0) | -0.53 (-0.65 to -0.40) |
| all kept | 100.0% (100.0 to 100.0) | 53.3% (53.1 to 53.5) | 56.6% (56.1 to 57.1) | 53.4% (52.9 to 53.9) | -0.60 (-0.72 to -0.47) |

## Adverse, C2.2 design (CPS yardstick)

### Q14 (primary): share of the main shock reaching each group, during the shock (years 5-8), main reading (markup 25%, no local sourcing)

| Group | No programme | Programme | Programme, after the shock (years 9-19) |
|---|---|---|---|
| all adults | 100.0% (100.0 to 100.0) | 22.2% (22.1 to 22.4) | 31.4% (31.3 to 31.4) |
| PTF members | no adults | 31.0% (30.5 to 31.6) | 30.2% (30.1 to 30.3) |
| PTH members (not PTF) | no adults | 18.8% (18.3 to 19.2) | 31.2% (31.0 to 31.3) |
| other CCO participants | no adults | 20.2% (19.9 to 20.4) | 32.0% (31.9 to 32.1) |
| in none of the three | 100.0% (100.0 to 100.0) | no adults | no adults |
| chose not to take part | 100.0% (100.0 to 100.0) | 22.2% (21.7 to 22.6) | 31.3% (31.1 to 31.4) |

### Q15: PTF members (F) by markup share and local sourcing, during the main shock (local supply half as exposed; no pooling)

| Markup share | no local sourcing | 25% local | 50% local | all local |
|---|---|---|---|---|
| 0% | 33.4% (32.8 to 34.0) | 32.2% (31.6 to 32.8) | 31.0% (30.5 to 31.6) | 28.7% (28.2 to 29.3) |
| 25% | 31.0% (30.5 to 31.6) | 30.2% (29.6 to 30.8) | 29.3% (28.8 to 29.9) | 27.5% (27.1 to 28.1) |
| 50% | 28.7% (28.2 to 29.3) | 28.1% (27.6 to 28.7) | 27.5% (27.1 to 28.1) | 26.4% (25.9 to 26.9) |

Sensitivities (markup 25%): local supply fully protected (kap 0), and a three-year price reserve (pool 3).

| Row | PTF members | all adults |
|---|---|---|
| m25.s25.k0.p1 | 29.3% (28.8 to 29.9) | 21.8% (21.7 to 22.0) |
| m25.s50.k0.p1 | 27.5% (27.1 to 28.1) | 21.4% (21.3 to 21.6) |
| m25.s100.k0.p1 | 24.0% (23.6 to 24.5) | 20.6% (20.5 to 20.8) |
| m25.s0.k50.p3 | 30.0% (29.4 to 30.6) | 21.9% (21.8 to 22.1) |
| m25.s50.k50.p3 | 28.5% (28.0 to 29.0) | 21.6% (21.5 to 21.8) |

### Protection by part of the design (Analysis; decision rules 1, 3)

- PTF (markup removal, main reading): PTF members' share without markup removal less with it: 2.3% (2.3 to 2.4) (rule 1: protects if the interval is above zero).
- BU: no adult is outside all three in this design (automatic distribution), so the BU's share cannot be read from the groups.
- PTH: other CCO participants less PTH members (not PTF): 1.4% (0.8 to 1.9) (rule 3: protects if the interval is above zero; the groups differ in who they are).

### Q16: basket poverty and volatility, main shock, main reading: shocked less unshocked (points), and for the programme against no programme

| Measure | No programme | Programme | Programme less no programme |
|---|---|---|---|
| basket poverty during the shock, all | +1.07 (+0.99 to +1.16) | +0.16 (+0.14 to +0.19) | -0.91 (-1.00 to -0.82) |
| basket poverty after the shock, all | +1.21 (+1.16 to +1.26) | +0.21 (+0.18 to +0.24) | -1.00 (-1.05 to -0.94) |
| basket poverty during, chose not to take part (no harm, rule 4) | +1.06 (+0.92 to +1.20) | +0.16 (+0.10 to +0.23) | -0.90 (-1.05 to -0.74) |
| basket poverty after, chose not to take part | +1.26 (+1.15 to +1.36) | +0.16 (+0.12 to +0.21) | -1.09 (-1.21 to -0.97) |
| basket poverty during, PTF members | +0.00 (+0.00 to +0.00) | +0.22 (+0.15 to +0.31) | +0.22 (+0.15 to +0.31) |
| basket poverty over the run | +0.88 (+0.84 to +0.92) | +0.15 (+0.13 to +0.16) | -0.73 (-0.77 to -0.69) |
| too little wealth at year 20 | +0.88 (+0.72 to +1.07) | +3.10 (+2.84 to +3.38) | +2.22 (+1.88 to +2.52) |
| volatility of costs, all (points of yearly change) | +0.19 (+0.18 to +0.20) | +0.41 (+0.41 to +0.42) | +0.22 (+0.21 to +0.23) |
| volatility, chose not to take part | +0.19 (+0.18 to +0.20) | +0.41 (+0.41 to +0.42) | +0.22 (+0.21 to +0.24) |
| too little wealth at year 20, participants | +0.85 (+0.69 to +1.03) | +3.16 (+2.87 to +3.46) | +2.31 (+1.94 to +2.65) |
| too little wealth at year 20, non-participants | +0.98 (+0.68 to +1.30) | +2.87 (+2.43 to +3.35) | +1.89 (+1.40 to +2.38) |
| median real wealth at year 20 ($) | -10480.30 (-10788.23 to -10188.73) | -5786.19 (-5912.57 to -5659.74) | +4694.11 (+4398.02 to +5020.35) |
| participation in year 19 (%) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) |
| BU cost a person-year ($) | +0.00 (+0.00 to +0.00) | +157.77 (+156.57 to +158.89) | +157.77 (+156.57 to +158.89) |
| programme inflation a year (points) | +0.14 (+0.14 to +0.14) | +1.63 (+1.61 to +1.65) | +1.49 (+1.47 to +1.51) |
| price level at year 20 (% of the unshocked level) | +2.69 (+2.68 to +2.71) | +23.99 (+23.75 to +24.21) | +21.30 (+21.06 to +21.52) |

### Other shock paths (programme rows: main reading and 50% local sourcing)

| Path | No programme, all adults | Programme, all | PTF members, main reading | PTF members, 50% local | basket poverty during, programme less no programme (points) |
|---|---|---|---|---|---|
| main shock (rise 32.8%, 88% kept) | 100.0% (100.0 to 100.0) | 22.2% (22.1 to 22.4) | 31.0% (30.5 to 31.6) | 29.3% (28.8 to 29.9) | -0.91 (-1.00 to -0.82) |
| rise 24.6% | 100.0% (100.0 to 100.0) | 22.2% (22.0 to 22.4) | 31.0% (30.4 to 31.6) | 29.2% (28.7 to 29.8) | -0.69 (-0.76 to -0.62) |
| rise 37.3% | 100.0% (100.0 to 100.0) | 22.3% (22.1 to 22.4) | 31.1% (30.5 to 31.7) | 29.3% (28.8 to 29.9) | -1.02 (-1.14 to -0.92) |
| rise 65.5% (beyond history) | 100.0% (100.0 to 100.0) | 22.3% (22.2 to 22.5) | 31.4% (30.8 to 32.0) | 29.6% (29.1 to 30.2) | -1.62 (-1.77 to -1.49) |
| 51% kept | 100.0% (100.0 to 100.0) | 23.5% (23.4 to 23.7) | 31.3% (30.8 to 31.8) | 29.7% (29.2 to 30.3) | -0.78 (-0.85 to -0.70) |
| all kept | 100.0% (100.0 to 100.0) | 21.9% (21.7 to 22.1) | 31.0% (30.4 to 31.6) | 29.2% (28.7 to 29.8) | -0.96 (-1.06 to -0.86) |

## Stress, release row (released wages)

### Q14 (primary): share of the main shock reaching each group, during the shock (years 5-8), main reading (markup 25%, no local sourcing)

| Group | No programme | Programme | Programme, after the shock (years 9-19) |
|---|---|---|---|
| all adults | 100.0% (100.0 to 100.0) | 80.5% (80.2 to 80.7) | 79.7% (79.4 to 80.1) |
| PTF members | no adults | 79.1% (78.3 to 80.0) | 79.7% (79.0 to 80.5) |
| PTH members (not PTF) | no adults | 78.9% (77.9 to 79.8) | 75.1% (74.3 to 76.0) |
| other CCO participants | no adults | 58.3% (58.1 to 58.5) | 58.0% (57.8 to 58.1) |
| in none of the three | 100.0% (100.0 to 100.0) | 100.0% (100.0 to 100.0) | 99.9% (99.9 to 99.9) |
| chose not to take part | 100.0% (100.0 to 100.0) | 90.5% (90.2 to 90.8) | 89.6% (89.3 to 90.0) |

### Q15: PTF members (F) by markup share and local sourcing, during the main shock (local supply half as exposed; no pooling)

| Markup share | no local sourcing | 25% local | 50% local | all local |
|---|---|---|---|---|
| 0% | 83.9% (83.1 to 84.8) | 81.5% (80.7 to 82.4) | 79.1% (78.3 to 80.0) | 74.3% (73.5 to 75.2) |
| 25% | 79.1% (78.3 to 80.0) | 77.3% (76.5 to 78.2) | 75.5% (74.7 to 76.4) | 71.9% (71.1 to 72.8) |
| 50% | 74.3% (73.5 to 75.2) | 73.1% (72.3 to 74.0) | 71.9% (71.1 to 72.8) | 69.5% (68.7 to 70.4) |

Sensitivities (markup 25%): local supply fully protected (kap 0), and a three-year price reserve (pool 3).

| Row | PTF members | all adults |
|---|---|---|
| m25.s25.k0.p1 | 75.5% (74.7 to 76.4) | 80.0% (79.7 to 80.3) |
| m25.s50.k0.p1 | 71.9% (71.1 to 72.8) | 79.6% (79.3 to 79.9) |
| m25.s100.k0.p1 | 64.8% (63.9 to 65.6) | 78.8% (78.5 to 79.0) |
| m25.s0.k50.p3 | 76.5% (75.6 to 77.3) | 80.1% (79.9 to 80.4) |
| m25.s50.k50.p3 | 73.6% (72.7 to 74.4) | 79.8% (79.5 to 80.1) |

### Protection by part of the design (Analysis; decision rules 1, 3)

- PTF (markup removal, main reading): PTF members' share without markup removal less with it: 4.8% (4.8 to 4.9) (rule 1: protects if the interval is above zero).
- BU: adults in none of the three less other CCO participants: 41.7% (41.5 to 41.9).
- PTH: other CCO participants less PTH members (not PTF): -20.6% (-21.5 to -19.6) (rule 3: protects if the interval is above zero; the groups differ in who they are).

### Q16: basket poverty and volatility, main shock, main reading: shocked less unshocked (points), and for the programme against no programme

| Measure | No programme | Programme | Programme less no programme |
|---|---|---|---|
| basket poverty during the shock, all | +1.62 (+1.51 to +1.74) | +1.39 (+1.28 to +1.51) | -0.23 (-0.38 to -0.07) |
| basket poverty after the shock, all | +1.60 (+1.53 to +1.67) | +1.43 (+1.34 to +1.51) | -0.18 (-0.28 to -0.07) |
| basket poverty during, chose not to take part (no harm, rule 4) | +1.61 (+1.48 to +1.74) | +1.52 (+1.39 to +1.66) | -0.08 (-0.26 to +0.11) |
| basket poverty after, chose not to take part | +1.59 (+1.50 to +1.67) | +1.48 (+1.38 to +1.59) | -0.11 (-0.22 to +0.00) |
| basket poverty during, PTF members | +0.00 (+0.00 to +0.00) | +1.19 (+0.92 to +1.48) | +1.19 (+0.92 to +1.48) |
| basket poverty over the run | +1.21 (+1.16 to +1.25) | +1.06 (+1.01 to +1.12) | -0.14 (-0.21 to -0.07) |
| too little wealth at year 20 | +0.95 (+0.80 to +1.11) | +1.78 (+1.57 to +2.00) | +0.82 (+0.58 to +1.07) |
| volatility of costs, all (points of yearly change) | +0.40 (+0.39 to +0.40) | +0.21 (+0.21 to +0.22) | -0.19 (-0.19 to -0.18) |
| volatility, chose not to take part | +0.40 (+0.39 to +0.40) | +0.23 (+0.22 to +0.23) | -0.17 (-0.18 to -0.17) |
| too little wealth at year 20, participants | +1.02 (+0.80 to +1.25) | +2.10 (+1.79 to +2.41) | +1.09 (+0.71 to +1.44) |
| too little wealth at year 20, non-participants | +0.91 (+0.74 to +1.10) | +1.56 (+1.36 to +1.79) | +0.65 (+0.38 to +0.92) |
| median real wealth at year 20 ($) | -6615.51 (-6912.24 to -6341.12) | -6.23 (-32.42 to +7.11) | +6609.29 (+6340.42 to +6897.53) |
| participation in year 19 (%) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) |
| BU cost a person-year ($) | +0.00 (+0.00 to +0.00) | +0.86 (+0.71 to +1.02) | +0.86 (+0.71 to +1.02) |
| programme inflation a year (points) | +0.14 (+0.14 to +0.14) | +0.70 (+0.69 to +0.71) | +0.55 (+0.55 to +0.56) |
| price level at year 20 (% of the unshocked level) | +2.73 (+2.73 to +2.73) | +11.00 (+10.88 to +11.10) | +8.26 (+8.15 to +8.37) |

### Other shock paths (programme rows: main reading and 50% local sourcing)

| Path | No programme, all adults | Programme, all | PTF members, main reading | PTF members, 50% local | basket poverty during, programme less no programme (points) |
|---|---|---|---|---|---|
| main shock (rise 32.8%, 88% kept) | 100.0% (100.0 to 100.0) | 80.5% (80.2 to 80.7) | 79.1% (78.3 to 80.0) | 75.5% (74.7 to 76.4) | -0.23 (-0.38 to -0.07) |
| rise 24.6% | 100.0% (100.0 to 100.0) | 80.4% (80.1 to 80.7) | 79.1% (78.2 to 80.0) | 75.5% (74.6 to 76.4) | -0.19 (-0.32 to -0.06) |
| rise 37.3% | 100.0% (100.0 to 100.0) | 80.5% (80.2 to 80.7) | 79.1% (78.3 to 80.0) | 75.5% (74.7 to 76.4) | -0.28 (-0.44 to -0.13) |
| rise 65.5% (beyond history) | 100.0% (100.0 to 100.0) | 80.5% (80.2 to 80.8) | 79.4% (78.5 to 80.2) | 75.7% (74.9 to 76.6) | -0.58 (-0.80 to -0.35) |
| 51% kept | 100.0% (100.0 to 100.0) | 79.9% (79.6 to 80.2) | 78.9% (78.0 to 79.8) | 75.5% (74.6 to 76.4) | -0.25 (-0.38 to -0.12) |
| all kept | 100.0% (100.0 to 100.0) | 80.6% (80.3 to 80.9) | 79.2% (78.3 to 80.1) | 75.5% (74.7 to 76.4) | -0.24 (-0.38 to -0.09) |

## Stress, C2.2 design (CPS yardstick)

### Q14 (primary): share of the main shock reaching each group, during the shock (years 5-8), main reading (markup 25%, no local sourcing)

| Group | No programme | Programme | Programme, after the shock (years 9-19) |
|---|---|---|---|
| all adults | 100.0% (100.0 to 100.0) | 22.1% (21.9 to 22.2) | 32.9% (32.9 to 33.0) |
| PTF members | no adults | 34.0% (33.2 to 34.8) | 35.7% (35.4 to 36.1) |
| PTH members (not PTF) | no adults | 19.0% (18.4 to 19.7) | 31.3% (31.0 to 31.5) |
| other CCO participants | no adults | 20.7% (20.5 to 20.9) | 32.5% (32.4 to 32.6) |
| in none of the three | 100.0% (100.0 to 100.0) | no adults | no adults |
| chose not to take part | 100.0% (100.0 to 100.0) | 22.1% (21.9 to 22.3) | 32.9% (32.8 to 33.0) |

### Q15: PTF members (F) by markup share and local sourcing, during the main shock (local supply half as exposed; no pooling)

| Markup share | no local sourcing | 25% local | 50% local | all local |
|---|---|---|---|---|
| 0% | 36.2% (35.4 to 37.1) | 35.1% (34.3 to 35.9) | 34.0% (33.2 to 34.8) | 31.8% (31.1 to 32.5) |
| 25% | 34.0% (33.2 to 34.8) | 33.2% (32.4 to 33.9) | 32.3% (31.6 to 33.1) | 30.7% (30.0 to 31.4) |
| 50% | 31.8% (31.1 to 32.5) | 31.2% (30.5 to 32.0) | 30.7% (30.0 to 31.4) | 29.6% (28.9 to 30.3) |

Sensitivities (markup 25%): local supply fully protected (kap 0), and a three-year price reserve (pool 3).

| Row | PTF members | all adults |
|---|---|---|
| m25.s25.k0.p1 | 32.3% (31.6 to 33.1) | 21.9% (21.7 to 22.0) |
| m25.s50.k0.p1 | 30.7% (30.0 to 31.4) | 21.7% (21.5 to 21.8) |
| m25.s100.k0.p1 | 27.4% (26.7 to 28.0) | 21.3% (21.1 to 21.4) |
| m25.s0.k50.p3 | 33.0% (32.3 to 33.8) | 21.9% (21.8 to 22.1) |
| m25.s50.k50.p3 | 31.6% (30.9 to 32.3) | 21.8% (21.6 to 21.9) |

### Protection by part of the design (Analysis; decision rules 1, 3)

- PTF (markup removal, main reading): PTF members' share without markup removal less with it: 2.2% (2.2 to 2.3) (rule 1: protects if the interval is above zero).
- BU: no adult is outside all three in this design (automatic distribution), so the BU's share cannot be read from the groups.
- PTH: other CCO participants less PTH members (not PTF): 1.7% (0.9 to 2.3) (rule 3: protects if the interval is above zero; the groups differ in who they are).

### Q16: basket poverty and volatility, main shock, main reading: shocked less unshocked (points), and for the programme against no programme

| Measure | No programme | Programme | Programme less no programme |
|---|---|---|---|
| basket poverty during the shock, all | +1.07 (+0.99 to +1.16) | +0.23 (+0.20 to +0.27) | -0.84 (-0.93 to -0.74) |
| basket poverty after the shock, all | +1.21 (+1.16 to +1.26) | +0.35 (+0.32 to +0.39) | -0.86 (-0.91 to -0.80) |
| basket poverty during, chose not to take part (no harm, rule 4) | +1.06 (+0.96 to +1.16) | +0.26 (+0.22 to +0.31) | -0.79 (-0.90 to -0.69) |
| basket poverty after, chose not to take part | +1.22 (+1.16 to +1.28) | +0.36 (+0.31 to +0.40) | -0.86 (-0.94 to -0.78) |
| basket poverty during, PTF members | +0.00 (+0.00 to +0.00) | +0.33 (+0.20 to +0.50) | +0.33 (+0.20 to +0.50) |
| basket poverty over the run | +0.88 (+0.84 to +0.92) | +0.24 (+0.22 to +0.26) | -0.64 (-0.68 to -0.60) |
| too little wealth at year 20 | +0.88 (+0.72 to +1.07) | +3.88 (+3.62 to +4.16) | +2.99 (+2.67 to +3.34) |
| volatility of costs, all (points of yearly change) | +0.19 (+0.18 to +0.20) | +0.51 (+0.50 to +0.52) | +0.32 (+0.30 to +0.33) |
| volatility, chose not to take part | +0.19 (+0.18 to +0.20) | +0.51 (+0.50 to +0.51) | +0.32 (+0.30 to +0.33) |
| too little wealth at year 20, participants | +0.92 (+0.70 to +1.17) | +3.87 (+3.48 to +4.33) | +2.95 (+2.52 to +3.44) |
| too little wealth at year 20, non-participants | +0.86 (+0.65 to +1.07) | +3.87 (+3.55 to +4.22) | +3.02 (+2.61 to +3.43) |
| median real wealth at year 20 ($) | -10480.30 (-10788.23 to -10188.73) | -4583.85 (-4728.90 to -4443.22) | +5896.46 (+5610.55 to +6211.08) |
| participation in year 19 (%) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) |
| BU cost a person-year ($) | +0.00 (+0.00 to +0.00) | +156.94 (+155.42 to +158.47) | +156.94 (+155.42 to +158.47) |
| programme inflation a year (points) | +0.14 (+0.14 to +0.14) | +1.73 (+1.71 to +1.75) | +1.59 (+1.57 to +1.61) |
| price level at year 20 (% of the unshocked level) | +2.69 (+2.68 to +2.71) | +25.25 (+25.02 to +25.48) | +22.56 (+22.33 to +22.79) |

### Other shock paths (programme rows: main reading and 50% local sourcing)

| Path | No programme, all adults | Programme, all | PTF members, main reading | PTF members, 50% local | basket poverty during, programme less no programme (points) |
|---|---|---|---|---|---|
| main shock (rise 32.8%, 88% kept) | 100.0% (100.0 to 100.0) | 22.1% (21.9 to 22.2) | 34.0% (33.2 to 34.8) | 32.3% (31.6 to 33.1) | -0.84 (-0.93 to -0.74) |
| rise 24.6% | 100.0% (100.0 to 100.0) | 22.0% (21.9 to 22.2) | 33.9% (33.1 to 34.7) | 32.2% (31.5 to 33.0) | -0.64 (-0.71 to -0.57) |
| rise 37.3% | 100.0% (100.0 to 100.0) | 22.1% (21.9 to 22.2) | 34.0% (33.3 to 34.9) | 32.4% (31.7 to 33.1) | -0.95 (-1.06 to -0.84) |
| rise 65.5% (beyond history) | 100.0% (100.0 to 100.0) | 22.2% (22.0 to 22.3) | 34.4% (33.7 to 35.2) | 32.7% (32.0 to 33.5) | -1.51 (-1.65 to -1.37) |
| 51% kept | 100.0% (100.0 to 100.0) | 23.4% (23.3 to 23.6) | 34.0% (33.4 to 34.8) | 32.6% (31.9 to 33.3) | -0.71 (-0.79 to -0.63) |
| all kept | 100.0% (100.0 to 100.0) | 21.7% (21.6 to 21.9) | 34.0% (33.2 to 34.8) | 32.3% (31.5 to 33.1) | -0.90 (-1.00 to -0.79) |
