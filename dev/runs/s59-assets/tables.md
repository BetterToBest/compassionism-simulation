# S59: wealth held by asset class, pilot tables

Seeds 1-100, 500 adults, 20 years; engine 1d2cf29. Effects are programme minus no programme on the same seeds, with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates (unadjusted). A pilot is a mechanism check, not a result. Made by `dev/tools/s59_table.py` from the per-seed files in compassionism-sim-results.

Check row (every asset nominal, no pass-through) equals "off" on every kept key: Reference yes, Adverse yes, Stress yes.

## 1. Primary outcome: the programme's effect on wealth poverty (points; adults under $25,000 of real wealth, year 20)

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| today: all wealth is one number of dollars | +21.51 (+20.96 to +22.05) | +0.66 (+0.19 to +1.11) | +45.03 (+44.43 to +45.60) | +30.16 (+29.43 to +30.85) | +24.81 (+24.12 to +25.50) | +41.65 (+40.93 to +42.33) |
| by asset class, main reading | -12.66 (-12.96 to -12.36) | -18.18 (-18.51 to -17.86) | -13.15 (-13.47 to -12.85) | -20.24 (-20.61 to -19.89) | -7.09 (-7.36 to -6.82) | -18.71 (-19.08 to -18.36) |
| nominal assets earn nothing | -11.44 (-11.75 to -11.15) | -16.95 (-17.29 to -16.62) | -11.78 (-12.10 to -11.47) | -17.99 (-18.36 to -17.64) | -6.39 (-6.67 to -6.12) | -16.53 (-16.93 to -16.16) |
| nominal assets keep up with prices in full | -13.81 (-14.13 to -13.48) | -18.73 (-19.04 to -18.42) | -15.38 (-15.71 to -15.07) | -22.08 (-22.41 to -21.76) | -8.02 (-8.30 to -7.75) | -21.57 (-21.92 to -21.22) |
| real assets follow half of inflation | -2.11 (-2.42 to -1.80) | -14.14 (-14.49 to -13.81) | +9.05 (+8.59 to +9.52) | -8.19 (-8.58 to -7.80) | +3.63 (+3.21 to +4.02) | -0.03 (-0.58 to +0.49) |
| no real price gain | -14.28 (-14.61 to -13.96) | -20.18 (-20.51 to -19.86) | -14.81 (-15.15 to -14.46) | -22.52 (-22.92 to -22.15) | -8.36 (-8.66 to -8.07) | -20.85 (-21.24 to -20.46) |
| real price gains of 1983-2022 | -11.69 (-11.98 to -11.40) | -16.85 (-17.16 to -16.56) | -12.05 (-12.38 to -11.73) | -18.75 (-19.12 to -18.41) | -6.38 (-6.63 to -6.12) | -17.36 (-17.72 to -17.01) |
| real price gains of 1890-2022 | -13.32 (-13.64 to -13.01) | -19.01 (-19.34 to -18.68) | -13.81 (-14.15 to -13.50) | -21.15 (-21.53 to -20.80) | -7.58 (-7.86 to -7.30) | -19.56 (-19.94 to -19.19) |
| new saving split by the group's asset shares | -13.60 (-13.94 to -13.28) | -18.54 (-18.83 to -18.24) | -15.19 (-15.53 to -14.86) | -21.94 (-22.27 to -21.61) | -7.85 (-8.14 to -7.58) | -21.41 (-21.76 to -21.06) |
| fixed-rate debt reprices too (no debt relief) | -6.68 (-6.98 to -6.38) | -13.32 (-13.68 to -12.97) | -7.80 (-8.14 to -7.48) | -15.71 (-16.09 to -15.34) | -2.78 (-3.05 to -2.53) | -13.39 (-13.74 to -13.03) |

Wealth poverty with no programme (%): Reference off 21.9, main 19.7; Adverse off 31.9, main 24.1; Stress off 31.9, main 24.1.

## 2. Secondary outcomes: the programme's effect, today's reading beside the asset-class readings

**Reference, release**

| Outcome | no programme (off / main) | effect, off | effect, main | effect, fixed debt reprices |
|---|---|---|---|---|
| median real wealth ($) | $212,300 / $265,800 | -$182,800 (-$186,000 to -$179,500) | +$43,600 ($40,800 to $46,500) | -$43,800 (-$46,100 to -$41,400) |
| real wealth at the 10th percentile ($) | -$10,000 / -$10,000 | +$12,200 ($11,900 to $12,400) | +$51,900 ($50,800 to $53,100) | +$20,900 ($19,700 to $22,200) |
| real wealth at the 90th percentile ($) | $1,338,100 / $1,959,000 | -$1,254,500 (-$1,276,500 to -$1,231,500) | -$166,900 (-$181,600 to -$151,600) | -$326,700 (-$340,800 to -$312,100) |
| wealth Gini, debts kept | 0.730 / 0.758 | -0.249 (-0.253 to -0.245) | -0.050 (-0.051 to -0.050) | -0.006 (-0.007 to -0.005) |
| wealth Gini, debts as zero | 0.725 / 0.756 | -0.245 (-0.249 to -0.241) | -0.047 (-0.048 to -0.047) | -0.003 (-0.004 to -0.002) |
| top 1% share of wealth (%) | 18.21 / 21.23 | -12.37 (-12.90 to -11.82) | -0.96 (-1.00 to -0.93) | +1.16 (+1.09 to +1.22) |
| top 10% share of wealth (%) | 58.91 / 63.79 | -26.97 (-27.63 to -26.30) | -3.73 (-3.79 to -3.66) | +0.92 (+0.87 to +0.98) |
| bottom 50% share of wealth (%) | 5.18 / 4.58 | +11.93 (+11.75 to +12.11) | +3.16 (+3.09 to +3.24) | +0.93 (+0.89 to +0.98) |
| families in debt (%) | 21.97 / 20.00 | -12.41 (-12.74 to -12.09) | -15.13 (-15.42 to -14.86) | -10.85 (-11.15 to -10.54) |
| basket poverty (% of adult-years) | 26.81 / 26.76 | -16.68 (-16.99 to -16.37) | -16.73 (-17.04 to -16.44) | -16.67 (-16.98 to -16.37) |
| adults below the cost of living (% of adult-years) | 31.41 / 31.36 | -19.41 (-19.79 to -19.05) | -19.46 (-19.83 to -19.10) | -19.39 (-19.77 to -19.03) |
| programme inflation (points a year) | 0.00 / 0.00 | +31.52 (+31.29 to +31.74) | +31.51 (+31.28 to +31.73) | +31.47 (+31.23 to +31.68) |

**Reference, C2.2**

| Outcome | no programme (off / main) | effect, off | effect, main | effect, fixed debt reprices |
|---|---|---|---|---|
| median real wealth ($) | $212,300 / $265,800 | -$171,500 (-$174,700 to -$168,300) | +$65,700 ($62,800 to $68,800) | -$22,500 (-$25,000 to -$20,100) |
| real wealth at the 10th percentile ($) | -$10,000 / -$10,000 | +$26,800 ($26,600 to $27,100) | +$80,500 ($79,500 to $81,600) | +$50,800 ($50,000 to $51,700) |
| real wealth at the 90th percentile ($) | $1,338,100 / $1,959,000 | -$1,248,700 (-$1,270,400 to -$1,225,600) | -$153,800 (-$168,300 to -$138,900) | -$314,100 (-$328,100 to -$299,800) |
| wealth Gini, debts kept | 0.730 / 0.758 | -0.378 (-0.383 to -0.374) | -0.071 (-0.072 to -0.070) | -0.027 (-0.028 to -0.026) |
| wealth Gini, debts as zero | 0.725 / 0.756 | -0.374 (-0.378 to -0.370) | -0.068 (-0.069 to -0.067) | -0.024 (-0.025 to -0.023) |
| top 1% share of wealth (%) | 18.21 / 21.23 | -13.65 (-14.19 to -13.11) | -1.46 (-1.51 to -1.42) | +0.60 (+0.54 to +0.65) |
| top 10% share of wealth (%) | 58.91 / 63.79 | -33.26 (-33.98 to -32.52) | -5.11 (-5.18 to -5.04) | -0.59 (-0.65 to -0.53) |
| bottom 50% share of wealth (%) | 5.18 / 4.58 | +20.87 (+20.71 to +21.03) | +4.41 (+4.32 to +4.50) | +2.21 (+2.15 to +2.27) |
| families in debt (%) | 21.97 / 20.00 | -21.15 (-21.48 to -20.83) | -19.60 (-19.90 to -19.30) | -16.92 (-17.21 to -16.63) |
| basket poverty (% of adult-years) | 26.81 / 26.76 | -24.64 (-24.96 to -24.32) | -24.60 (-24.92 to -24.27) | -24.58 (-24.90 to -24.26) |
| adults below the cost of living (% of adult-years) | 31.41 / 31.36 | -28.24 (-28.66 to -27.86) | -28.19 (-28.59 to -27.80) | -28.17 (-28.58 to -27.78) |
| programme inflation (points a year) | 0.00 / 0.00 | +37.44 (+37.22 to +37.65) | +37.42 (+37.21 to +37.64) | +37.40 (+37.18 to +37.61) |

**Adverse, release**

| Outcome | no programme (off / main) | effect, off | effect, main | effect, fixed debt reprices |
|---|---|---|---|---|
| median real wealth ($) | $116,000 / $232,500 | -$104,500 (-$107,000 to -$102,100) | +$45,000 ($41,900 to $47,900) | -$16,800 (-$19,400 to -$14,200) |
| real wealth at the 10th percentile ($) | -$6,900 / -$6,900 | +$6,800 ($6,800 to $6,800) | +$27,900 ($26,900 to $28,900) | +$7,100 ($6,900 to $7,300) |
| real wealth at the 90th percentile ($) | $889,600 / $1,874,000 | -$849,400 (-$864,300 to -$833,100) | -$135,500 (-$148,800 to -$121,900) | -$247,800 (-$259,300 to -$235,900) |
| wealth Gini, debts kept | 0.765 / 0.775 | -0.202 (-0.206 to -0.198) | -0.047 (-0.048 to -0.046) | -0.013 (-0.013 to -0.012) |
| wealth Gini, debts as zero | 0.758 / 0.772 | -0.195 (-0.199 to -0.191) | -0.044 (-0.045 to -0.043) | -0.010 (-0.010 to -0.009) |
| top 1% share of wealth (%) | 19.29 / 21.92 | -12.26 (-12.86 to -11.65) | -0.93 (-0.97 to -0.89) | +0.73 (+0.68 to +0.78) |
| top 10% share of wealth (%) | 61.91 / 65.34 | -25.36 (-26.08 to -24.65) | -3.57 (-3.64 to -3.50) | +0.04 (-0.02 to +0.11) |
| bottom 50% share of wealth (%) | 2.98 / 3.65 | +8.17 (+7.99 to +8.35) | +2.99 (+2.92 to +3.06) | +1.28 (+1.23 to +1.33) |
| families in debt (%) | 30.48 / 24.07 | -8.70 (-9.10 to -8.29) | -15.99 (-16.35 to -15.62) | -11.83 (-12.19 to -11.46) |
| basket poverty (% of adult-years) | 38.32 / 38.23 | -22.56 (-22.96 to -22.15) | -22.56 (-22.97 to -22.15) | -22.59 (-22.99 to -22.19) |
| adults below the cost of living (% of adult-years) | 43.66 / 43.59 | -25.54 (-25.99 to -25.08) | -25.55 (-26.01 to -25.07) | -25.57 (-26.02 to -25.11) |
| programme inflation (points a year) | 0.00 / 0.00 | +37.59 (+37.30 to +37.87) | +37.62 (+37.33 to +37.90) | +37.54 (+37.25 to +37.82) |

**Adverse, C2.2**

| Outcome | no programme (off / main) | effect, off | effect, main | effect, fixed debt reprices |
|---|---|---|---|---|
| median real wealth ($) | $116,000 / $232,500 | -$95,600 (-$98,000 to -$93,200) | +$63,800 ($60,600 to $66,900) | +$2,700 (-$100 to $5,500) |
| real wealth at the 10th percentile ($) | -$6,900 / -$6,900 | +$13,800 ($13,600 to $13,900) | +$56,500 ($55,700 to $57,400) | +$29,800 ($29,100 to $30,600) |
| real wealth at the 90th percentile ($) | $889,600 / $1,874,000 | -$841,700 (-$856,500 to -$825,300) | -$120,200 (-$133,800 to -$106,700) | -$232,400 (-$244,100 to -$219,700) |
| wealth Gini, debts kept | 0.765 / 0.775 | -0.376 (-0.380 to -0.372) | -0.067 (-0.068 to -0.066) | -0.032 (-0.033 to -0.031) |
| wealth Gini, debts as zero | 0.758 / 0.772 | -0.369 (-0.373 to -0.365) | -0.064 (-0.066 to -0.063) | -0.029 (-0.030 to -0.028) |
| top 1% share of wealth (%) | 19.29 / 21.92 | -14.17 (-14.75 to -13.58) | -1.43 (-1.48 to -1.39) | +0.18 (+0.13 to +0.22) |
| top 10% share of wealth (%) | 61.91 / 65.34 | -34.27 (-35.02 to -33.51) | -4.95 (-5.04 to -4.87) | -1.43 (-1.50 to -1.36) |
| bottom 50% share of wealth (%) | 2.98 / 3.65 | +20.64 (+20.49 to +20.80) | +4.21 (+4.12 to +4.29) | +2.45 (+2.38 to +2.51) |
| families in debt (%) | 30.48 / 24.07 | -27.84 (-28.20 to -27.49) | -23.02 (-23.40 to -22.64) | -20.54 (-20.91 to -20.19) |
| basket poverty (% of adult-years) | 38.32 / 38.23 | -35.26 (-35.73 to -34.79) | -35.19 (-35.66 to -34.72) | -35.21 (-35.68 to -34.75) |
| adults below the cost of living (% of adult-years) | 43.66 / 43.59 | -39.24 (-39.77 to -38.72) | -39.18 (-39.71 to -38.66) | -39.19 (-39.72 to -38.68) |
| programme inflation (points a year) | 0.00 / 0.00 | +43.98 (+43.69 to +44.27) | +43.98 (+43.69 to +44.27) | +43.95 (+43.65 to +44.23) |

**Stress, release**

| Outcome | no programme (off / main) | effect, off | effect, main | effect, fixed debt reprices |
|---|---|---|---|---|
| median real wealth ($) | $116,000 / $232,500 | -$97,300 (-$99,500 to -$95,000) | +$38,900 ($36,500 to $41,300) | -$20,600 (-$22,700 to -$18,500) |
| real wealth at the 10th percentile ($) | -$6,900 / -$6,900 | +$6,500 ($6,500 to $6,500) | +$6,500 ($6,500 to $6,500) | +$6,500 ($6,500 to $6,500) |
| real wealth at the 90th percentile ($) | $889,600 / $1,874,000 | -$792,000 (-$806,300 to -$776,700) | -$97,600 (-$108,100 to -$86,600) | -$201,800 (-$211,500 to -$191,300) |
| wealth Gini, debts kept | 0.765 / 0.775 | -0.082 (-0.084 to -0.080) | -0.033 (-0.033 to -0.032) | -0.003 (-0.004 to -0.003) |
| wealth Gini, debts as zero | 0.758 / 0.772 | -0.079 (-0.081 to -0.077) | -0.030 (-0.031 to -0.029) | -0.001 (-0.001 to -0.000) |
| top 1% share of wealth (%) | 19.29 / 21.92 | -7.08 (-7.42 to -6.75) | -0.76 (-0.79 to -0.73) | +0.73 (+0.68 to +0.76) |
| top 10% share of wealth (%) | 61.91 / 65.34 | -13.02 (-13.42 to -12.64) | -2.76 (-2.82 to -2.70) | +0.47 (+0.43 to +0.52) |
| bottom 50% share of wealth (%) | 2.98 / 3.65 | +1.67 (+1.53 to +1.80) | +1.99 (+1.93 to +2.04) | +0.55 (+0.52 to +0.59) |
| families in debt (%) | 30.48 / 24.07 | +3.71 (+3.33 to +4.10) | -8.23 (-8.53 to -7.93) | -4.16 (-4.44 to -3.90) |
| basket poverty (% of adult-years) | 38.32 / 38.23 | -8.72 (-9.01 to -8.42) | -8.72 (-9.02 to -8.43) | -8.76 (-9.05 to -8.46) |
| adults below the cost of living (% of adult-years) | 43.66 / 43.59 | -9.87 (-10.23 to -9.52) | -9.88 (-10.23 to -9.52) | -9.91 (-10.27 to -9.56) |
| programme inflation (points a year) | 0.00 / 0.00 | +16.47 (+16.20 to +16.72) | +16.49 (+16.23 to +16.74) | +16.46 (+16.20 to +16.71) |

**Stress, C2.2**

| Outcome | no programme (off / main) | effect, off | effect, main | effect, fixed debt reprices |
|---|---|---|---|---|
| median real wealth ($) | $116,000 / $232,500 | -$100,300 (-$102,700 to -$97,900) | +$55,000 ($51,900 to $58,100) | -$6,300 (-$9,200 to -$3,500) |
| real wealth at the 10th percentile ($) | -$6,900 / -$6,900 | +$10,800 ($10,700 to $11,000) | +$49,900 ($49,100 to $50,700) | +$23,900 ($23,200 to $24,600) |
| real wealth at the 90th percentile ($) | $889,600 / $1,874,000 | -$849,900 (-$864,800 to -$833,500) | -$131,600 (-$145,000 to -$117,700) | -$243,600 (-$255,900 to -$230,600) |
| wealth Gini, debts kept | 0.765 / 0.775 | -0.340 (-0.344 to -0.336) | -0.061 (-0.062 to -0.060) | -0.025 (-0.026 to -0.024) |
| wealth Gini, debts as zero | 0.758 / 0.772 | -0.333 (-0.337 to -0.328) | -0.058 (-0.059 to -0.057) | -0.022 (-0.023 to -0.021) |
| top 1% share of wealth (%) | 19.29 / 21.92 | -13.78 (-14.37 to -13.19) | -1.24 (-1.28 to -1.19) | +0.42 (+0.37 to +0.47) |
| top 10% share of wealth (%) | 61.91 / 65.34 | -32.59 (-33.34 to -31.82) | -4.47 (-4.55 to -4.39) | -0.85 (-0.92 to -0.78) |
| bottom 50% share of wealth (%) | 2.98 / 3.65 | +18.09 (+17.93 to +18.24) | +3.85 (+3.77 to +3.93) | +2.05 (+1.99 to +2.11) |
| families in debt (%) | 30.48 / 24.07 | -25.46 (-25.83 to -25.10) | -22.31 (-22.69 to -21.95) | -19.08 (-19.46 to -18.71) |
| basket poverty (% of adult-years) | 38.32 / 38.23 | -34.52 (-35.00 to -34.07) | -34.45 (-34.94 to -34.00) | -34.47 (-34.95 to -34.02) |
| adults below the cost of living (% of adult-years) | 43.66 / 43.59 | -38.18 (-38.69 to -37.68) | -38.12 (-38.63 to -37.63) | -38.12 (-38.64 to -37.63) |
| programme inflation (points a year) | 0.00 / 0.00 | +45.89 (+45.56 to +46.22) | +45.90 (+45.56 to +46.23) | +45.84 (+45.50 to +46.17) |

## 3. The programme's effect on mean real wealth in three parts (Year-0 dollars per adult)

E: the opening nominal position held untouched (nominal assets and floating debt with their interest, less fixed-rate debt). V: the opening real assets held untouched. S: saving since the start and what it earned. The share is E's part of the whole effect.

**Reference**

| Reading | Design | Group | E: opening nominal position | V: opening real assets | S: saving | Whole | E share |
|---|---|---|---|---|---|---|---|
| by asset class, main reading | release | all adults | +$5,700 ($4,700 to $6,700) | +$0 (-$0 to $0) | -$24,000 (-$24,700 to -$23,200) | -$18,300 | -31% |
|  |  | fifth 1 of starting wealth | +$36,100 ($35,000 to $37,100) | +$0 (-$0 to $0) | -$15,800 (-$16,600 to -$15,000) | +$20,300 | 178% |
|  |  | fifth 2 of starting wealth | +$44,600 ($44,000 to $45,100) | +$0 (-$0 to $0) | -$3,700 (-$5,300 to -$2,000) | +$40,900 | 109% |
|  |  | fifth 3 of starting wealth | +$74,000 ($73,100 to $74,900) | -$0 (-$0 to $0) | -$9,600 (-$11,600 to -$7,600) | +$64,500 | 115% |
|  |  | fifth 4 of starting wealth | +$54,800 ($53,800 to $55,800) | -$0 (-$0 to $0) | -$26,800 (-$29,100 to -$24,500) | +$28,100 | 195% |
|  |  | fifth 5 of starting wealth | -$181,000 (-$186,000 to -$175,600) | -$0 (-$0 to $0) | -$64,000 (-$66,200 to -$61,700) | -$245,000 | 74% |
| by asset class, main reading | C2.2 | all adults | +$3,500 ($2,500 to $4,600) | +$0 (-$0 to $0) | -$400 (-$1,200 to $400) | +$3,100 | 112% |
|  |  | fifth 1 of starting wealth | +$36,100 ($35,000 to $37,100) | +$0 (-$0 to $0) | +$8,500 ($7,700 to $9,400) | +$44,600 | 81% |
|  |  | fifth 2 of starting wealth | +$44,500 ($43,900 to $45,000) | -$0 (-$0 to $0) | +$22,500 ($20,800 to $24,300) | +$67,000 | 66% |
|  |  | fifth 3 of starting wealth | +$73,700 ($72,800 to $74,600) | -$0 (-$0 to $0) | +$14,800 ($12,600 to $16,800) | +$88,400 | 83% |
|  |  | fifth 4 of starting wealth | +$53,500 ($52,500 to $54,600) | +$0 (-$0 to $0) | -$3,300 (-$5,900 to -$900) | +$50,200 | 107% |
|  |  | fifth 5 of starting wealth | -$190,100 (-$195,400 to -$184,600) | -$0 (-$0 to $0) | -$44,400 (-$46,600 to -$42,100) | -$234,600 | 81% |
| nominal assets earn nothing | release | all adults | -$1,500 (-$2,600 to -$300) | +$0 (-$0 to $0) | -$48,300 (-$49,300 to -$47,300) | -$49,700 | 3% |
| nominal assets earn nothing | C2.2 | all adults | -$1,500 (-$2,600 to -$300) | +$0 (-$0 to $0) | -$32,500 (-$33,600 to -$31,500) | -$34,000 | 4% |
| nominal assets keep up with prices in full | release | all adults | +$105,100 ($104,600 to $105,700) | -$0 (-$0 to $0) | +$65,600 ($65,200 to $66,000) | +$170,800 | 62% |
| nominal assets keep up with prices in full | C2.2 | all adults | +$105,400 ($104,900 to $106,000) | +$0 (-$0 to $0) | +$131,700 ($131,300 to $132,100) | +$237,100 | 44% |
| real assets follow half of inflation | release | all adults | +$5,700 ($4,700 to $6,700) | -$744,500 (-$758,600 to -$730,600) | -$20,700 (-$21,500 to -$20,000) | -$759,600 | -1% |
| real assets follow half of inflation | C2.2 | all adults | +$3,500 ($2,500 to $4,600) | -$766,500 (-$781,000 to -$751,900) | +$0 (-$800 to $800) | -$763,000 | -0% |
| no real price gain | release | all adults | +$5,700 ($4,700 to $6,700) | +$0 (-$0 to $0) | -$26,000 (-$26,800 to -$25,300) | -$20,300 | -28% |
| no real price gain | C2.2 | all adults | +$3,500 ($2,500 to $4,600) | -$0 (-$0 to $0) | -$2,700 (-$3,400 to -$1,900) | +$900 | 410% |
| real price gains of 1983-2022 | release | all adults | +$5,700 ($4,700 to $6,700) | +$0 (-$0 to $0) | -$22,500 (-$23,300 to -$21,800) | -$16,800 | -34% |
| real price gains of 1983-2022 | C2.2 | all adults | +$3,500 ($2,500 to $4,600) | -$0 (-$0 to -$0) | +$1,200 ($400 to $2,000) | +$4,700 | 74% |
| real price gains of 1890-2022 | release | all adults | +$5,700 ($4,700 to $6,700) | -$0 (-$0 to -$0) | -$24,800 (-$25,600 to -$24,100) | -$19,100 | -30% |
| real price gains of 1890-2022 | C2.2 | all adults | +$3,500 ($2,500 to $4,600) | +$0 (-$0 to $0) | -$1,300 (-$2,100 to -$600) | +$2,200 | 159% |
| new saving split by the group's asset shares | release | all adults | +$5,700 ($4,700 to $6,700) | -$0 (-$0 to $0) | +$60,300 ($59,900 to $60,700) | +$66,000 | 9% |
| new saving split by the group's asset shares | C2.2 | all adults | +$3,500 ($2,500 to $4,600) | +$0 (-$0 to $0) | +$125,800 ($125,400 to $126,200) | +$129,300 | 3% |
| fixed-rate debt reprices too (no debt relief) | release | all adults | -$99,400 (-$100,700 to -$98,100) | +$0 (-$0 to $0) | -$20,500 (-$21,300 to -$19,800) | -$119,900 | 83% |
|  |  | fifth 1 of starting wealth | -$5,000 (-$5,100 to -$4,900) | +$0 (-$0 to $0) | -$2,500 (-$3,300 to -$1,600) | -$7,500 | 67% |
|  |  | fifth 2 of starting wealth | -$10,100 (-$10,200 to -$10,000) | +$0 (-$0 to $0) | -$1,000 (-$2,600 to $700) | -$11,100 | 91% |
|  |  | fifth 3 of starting wealth | -$25,700 (-$26,000 to -$25,500) | -$0 (-$0 to $0) | -$8,900 (-$11,000 to -$7,000) | -$34,700 | 74% |
|  |  | fifth 4 of starting wealth | -$65,700 (-$66,700 to -$64,800) | -$0 (-$0 to $0) | -$26,600 (-$28,900 to -$24,300) | -$92,300 | 71% |
|  |  | fifth 5 of starting wealth | -$390,400 (-$396,900 to -$383,800) | -$0 (-$0 to $0) | -$63,800 (-$66,000 to -$61,500) | -$454,200 | 86% |
| fixed-rate debt reprices too (no debt relief) | C2.2 | all adults | -$101,900 (-$103,200 to -$100,600) | -$0 (-$0 to $0) | +$1,000 ($200 to $1,800) | -$100,900 | 101% |
|  |  | fifth 1 of starting wealth | -$5,100 (-$5,300 to -$5,000) | -$0 (-$0 to $0) | +$15,200 ($14,300 to $16,000) | +$10,100 | -51% |
|  |  | fifth 2 of starting wealth | -$10,400 (-$10,500 to -$10,200) | -$0 (-$0 to $0) | +$22,800 ($21,100 to $24,600) | +$12,500 | -83% |
|  |  | fifth 3 of starting wealth | -$26,400 (-$26,600 to -$26,100) | -$0 (-$0 to $0) | +$14,800 ($12,600 to $16,800) | -$11,600 | 227% |
|  |  | fifth 4 of starting wealth | -$67,400 (-$68,400 to -$66,500) | -$0 (-$0 to -$0) | -$3,400 (-$5,900 to -$900) | -$70,800 | 95% |
|  |  | fifth 5 of starting wealth | -$400,300 (-$406,900 to -$393,500) | -$0 (-$0 to -$0) | -$44,400 (-$46,600 to -$42,100) | -$444,700 | 90% |

**Adverse**

| Reading | Design | Group | E: opening nominal position | V: opening real assets | S: saving | Whole | E share |
|---|---|---|---|---|---|---|---|
| by asset class, main reading | release | all adults | -$10,800 (-$11,700 to -$9,900) | -$0 (-$0 to -$0) | -$2,700 (-$3,600 to -$1,700) | -$13,400 | 80% |
|  |  | fifth 1 of starting wealth | +$24,100 ($23,300 to $24,800) | -$0 (-$0 to -$0) | -$7,200 (-$7,900 to -$6,500) | +$16,900 | 143% |
|  |  | fifth 2 of starting wealth | +$29,200 ($28,800 to $29,600) | -$0 (-$0 to -$0) | +$13,000 ($11,600 to $14,500) | +$42,200 | 69% |
|  |  | fifth 3 of starting wealth | +$47,200 ($46,500 to $47,800) | -$0 (-$0 to -$0) | +$15,500 ($13,300 to $17,600) | +$62,600 | 75% |
|  |  | fifth 4 of starting wealth | +$28,000 ($27,200 to $28,800) | -$0 (-$0 to -$0) | -$500 (-$2,900 to $1,800) | +$27,500 | 102% |
|  |  | fifth 5 of starting wealth | -$182,300 (-$186,800 to -$177,800) | -$0 (-$0 to -$0) | -$34,100 (-$36,200 to -$31,900) | -$216,500 | 84% |
| by asset class, main reading | C2.2 | all adults | -$12,100 (-$13,000 to -$11,200) | -$0 (-$0 to -$0) | +$19,500 ($18,500 to $20,500) | +$7,400 | -164% |
|  |  | fifth 1 of starting wealth | +$24,100 ($23,300 to $24,800) | -$0 (-$0 to -$0) | +$13,500 ($12,900 to $14,200) | +$37,600 | 64% |
|  |  | fifth 2 of starting wealth | +$29,100 ($28,700 to $29,500) | -$0 (-$0 to -$0) | +$38,400 ($36,900 to $40,000) | +$67,500 | 43% |
|  |  | fifth 3 of starting wealth | +$46,900 ($46,300 to $47,500) | -$0 (-$0 to -$0) | +$39,100 ($36,700 to $41,400) | +$86,000 | 55% |
|  |  | fifth 4 of starting wealth | +$27,200 ($26,400 to $28,000) | -$0 (-$0 to -$0) | +$21,900 ($19,300 to $24,400) | +$49,100 | 55% |
|  |  | fifth 5 of starting wealth | -$187,700 (-$192,200 to -$183,100) | -$0 (-$0 to -$0) | -$15,600 (-$17,700 to -$13,400) | -$203,300 | 92% |
| nominal assets earn nothing | release | all adults | -$1,000 (-$1,800 to -$200) | -$0 (-$0 to -$0) | -$14,200 (-$15,300 to -$13,200) | -$15,200 | 7% |
| nominal assets earn nothing | C2.2 | all adults | -$1,000 (-$1,800 to -$200) | -$0 (-$0 to -$0) | +$1,700 ($500 to $2,800) | +$700 | -148% |
| nominal assets keep up with prices in full | release | all adults | +$72,400 ($72,000 to $72,800) | -$0 (-$0 to -$0) | +$69,600 ($69,000 to $70,200) | +$142,000 | 51% |
| nominal assets keep up with prices in full | C2.2 | all adults | +$72,500 ($72,100 to $72,900) | -$0 (-$0 to -$0) | +$133,600 ($133,000 to $134,200) | +$206,100 | 35% |
| real assets follow half of inflation | release | all adults | -$10,800 (-$11,600 to -$9,900) | -$634,500 (-$646,500 to -$622,700) | +$800 (-$300 to $1,800) | -$644,500 | 2% |
| real assets follow half of inflation | C2.2 | all adults | -$12,100 (-$13,000 to -$11,200) | -$647,600 (-$659,800 to -$635,300) | +$17,600 ($16,700 to $18,600) | -$642,100 | 2% |
| no real price gain | release | all adults | -$10,800 (-$11,700 to -$9,900) | -$0 (-$0 to -$0) | -$5,100 (-$6,000 to -$4,100) | -$15,800 | 68% |
| no real price gain | C2.2 | all adults | -$12,100 (-$13,000 to -$11,200) | -$0 (-$0 to -$0) | +$16,700 ($15,700 to $17,600) | +$4,600 | -264% |
| real price gains of 1983-2022 | release | all adults | -$10,800 (-$11,700 to -$9,900) | +$0 ($0 to $0) | -$1,000 (-$2,000 to -$0) | -$11,800 | 92% |
| real price gains of 1983-2022 | C2.2 | all adults | -$12,100 (-$13,000 to -$11,200) | +$0 ($0 to $0) | +$21,400 ($20,400 to $22,400) | +$9,300 | -130% |
| real price gains of 1890-2022 | release | all adults | -$10,800 (-$11,700 to -$9,900) | -$0 (-$0 to -$0) | -$3,600 (-$4,600 to -$2,700) | -$14,400 | 75% |
| real price gains of 1890-2022 | C2.2 | all adults | -$12,100 (-$13,000 to -$11,200) | -$0 (-$0 to -$0) | +$18,300 ($17,400 to $19,300) | +$6,300 | -193% |
| new saving split by the group's asset shares | release | all adults | -$10,800 (-$11,700 to -$9,900) | -$0 (-$0 to -$0) | +$65,900 ($65,300 to $66,500) | +$55,100 | -20% |
| new saving split by the group's asset shares | C2.2 | all adults | -$12,100 (-$13,000 to -$11,200) | -$0 (-$0 to -$0) | +$128,600 ($128,000 to $129,200) | +$116,500 | -10% |
| fixed-rate debt reprices too (no debt relief) | release | all adults | -$83,100 (-$84,200 to -$82,100) | -$0 (-$0 to -$0) | -$1,300 (-$2,300 to -$400) | -$84,500 | 98% |
|  |  | fifth 1 of starting wealth | -$4,200 (-$4,300 to -$4,100) | -$0 (-$0 to -$0) | +$2,000 ($1,300 to $2,600) | -$2,200 | 187% |
|  |  | fifth 2 of starting wealth | -$8,400 (-$8,500 to -$8,400) | -$0 (-$0 to -$0) | +$11,700 ($10,400 to $13,100) | +$3,300 | -258% |
|  |  | fifth 3 of starting wealth | -$21,500 (-$21,700 to -$21,300) | -$0 (-$0 to -$0) | +$14,200 ($12,000 to $16,200) | -$7,400 | 292% |
|  |  | fifth 4 of starting wealth | -$55,000 (-$55,800 to -$54,200) | -$0 (-$0 to -$0) | -$500 (-$2,900 to $1,800) | -$55,500 | 99% |
|  |  | fifth 5 of starting wealth | -$326,500 (-$332,000 to -$321,100) | -$0 (-$0 to -$0) | -$33,900 (-$36,000 to -$31,700) | -$360,400 | 91% |
| fixed-rate debt reprices too (no debt relief) | C2.2 | all adults | -$84,600 (-$85,600 to -$83,500) | -$0 (-$0 to -$0) | +$18,200 ($17,200 to $19,100) | -$66,400 | 127% |
|  |  | fifth 1 of starting wealth | -$4,300 (-$4,400 to -$4,200) | -$0 (-$0 to -$0) | +$14,400 ($13,700 to $15,000) | +$10,100 | -42% |
|  |  | fifth 2 of starting wealth | -$8,600 (-$8,700 to -$8,500) | -$0 (-$0 to -$0) | +$33,400 ($32,000 to $34,900) | +$24,800 | -35% |
|  |  | fifth 3 of starting wealth | -$21,900 (-$22,100 to -$21,700) | -$0 (-$0 to -$0) | +$36,900 ($34,600 to $39,100) | +$15,000 | -146% |
|  |  | fifth 4 of starting wealth | -$55,900 (-$56,700 to -$55,200) | -$0 (-$0 to -$0) | +$21,700 ($19,100 to $24,200) | -$34,300 | 163% |
|  |  | fifth 5 of starting wealth | -$332,200 (-$337,700 to -$326,500) | -$0 (-$0 to -$0) | -$15,600 (-$17,700 to -$13,400) | -$347,800 | 96% |

**Stress**

| Reading | Design | Group | E: opening nominal position | V: opening real assets | S: saving | Whole | E share |
|---|---|---|---|---|---|---|---|
| by asset class, main reading | release | all adults | +$700 (-$0 to $1,400) | -$0 (-$0 to -$0) | -$9,400 (-$10,100 to -$8,800) | -$8,700 | -8% |
|  |  | fifth 1 of starting wealth | +$23,300 ($22,600 to $24,000) | -$0 (-$0 to -$0) | -$12,400 (-$13,000 to -$11,900) | +$10,900 | 214% |
|  |  | fifth 2 of starting wealth | +$28,700 ($28,400 to $29,100) | -$0 (-$0 to -$0) | -$3,100 (-$4,200 to -$2,000) | +$25,600 | 112% |
|  |  | fifth 3 of starting wealth | +$47,400 ($46,800 to $48,000) | -$0 (-$0 to -$0) | +$1,300 (-$200 to $2,900) | +$48,700 | 97% |
|  |  | fifth 4 of starting wealth | +$33,700 ($33,000 to $34,400) | -$0 (-$0 to -$0) | -$6,200 (-$7,800 to -$4,600) | +$27,500 | 123% |
|  |  | fifth 5 of starting wealth | -$129,700 (-$133,200 to -$125,900) | -$0 (-$0 to -$0) | -$26,700 (-$28,200 to -$25,200) | -$156,400 | 83% |
| by asset class, main reading | C2.2 | all adults | -$12,400 (-$13,300 to -$11,500) | -$0 (-$0 to -$0) | +$10,700 ($9,700 to $11,700) | -$1,700 | 736% |
|  |  | fifth 1 of starting wealth | +$24,000 ($23,300 to $24,800) | -$0 (-$0 to -$0) | +$6,400 ($5,700 to $7,100) | +$30,400 | 79% |
|  |  | fifth 2 of starting wealth | +$29,100 ($28,700 to $29,400) | -$0 (-$0 to -$0) | +$30,300 ($28,700 to $31,900) | +$59,400 | 49% |
|  |  | fifth 3 of starting wealth | +$46,800 ($46,200 to $47,400) | -$0 (-$0 to -$0) | +$30,500 ($28,100 to $32,800) | +$77,300 | 61% |
|  |  | fifth 4 of starting wealth | +$27,000 ($26,200 to $27,800) | -$0 (-$0 to -$0) | +$12,600 ($9,900 to $15,100) | +$39,600 | 68% |
|  |  | fifth 5 of starting wealth | -$188,900 (-$193,400 to -$184,200) | -$0 (-$0 to -$0) | -$26,200 (-$28,400 to -$23,900) | -$215,100 | 88% |
| nominal assets earn nothing | release | all adults | -$900 (-$1,700 to -$200) | -$0 (-$0 to -$0) | -$20,100 (-$20,900 to -$19,400) | -$21,100 | 4% |
| nominal assets earn nothing | C2.2 | all adults | -$1,000 (-$1,800 to -$200) | -$0 (-$0 to -$0) | -$3,800 (-$5,000 to -$2,700) | -$4,800 | 21% |
| nominal assets keep up with prices in full | release | all adults | +$68,500 ($68,100 to $68,900) | -$0 (-$0 to -$0) | +$24,500 ($24,000 to $25,000) | +$92,900 | 74% |
| nominal assets keep up with prices in full | C2.2 | all adults | +$72,500 ($72,100 to $72,900) | -$0 (-$0 to -$0) | +$113,700 ($113,100 to $114,300) | +$186,200 | 39% |
| real assets follow half of inflation | release | all adults | +$700 ($0 to $1,500) | -$505,800 (-$515,500 to -$495,600) | -$2,100 (-$2,800 to -$1,300) | -$507,100 | -0% |
| real assets follow half of inflation | C2.2 | all adults | -$12,400 (-$13,300 to -$11,500) | -$650,500 (-$662,800 to -$638,100) | +$9,200 ($8,200 to $10,200) | -$653,700 | 2% |
| no real price gain | release | all adults | +$700 (-$0 to $1,500) | -$0 (-$0 to -$0) | -$11,000 (-$11,600 to -$10,400) | -$10,300 | -7% |
| no real price gain | C2.2 | all adults | -$12,400 (-$13,300 to -$11,500) | -$0 (-$0 to -$0) | +$7,900 ($6,900 to $8,900) | -$4,400 | 279% |
| real price gains of 1983-2022 | release | all adults | +$700 (-$0 to $1,400) | +$0 ($0 to $0) | -$8,400 (-$9,000 to -$7,700) | -$7,700 | -9% |
| real price gains of 1983-2022 | C2.2 | all adults | -$12,400 (-$13,300 to -$11,500) | +$0 ($0 to $0) | +$12,600 ($11,600 to $13,700) | +$300 | -4905% |
| real price gains of 1890-2022 | release | all adults | +$700 (-$0 to $1,400) | -$0 (-$0 to -$0) | -$10,100 (-$10,700 to -$9,400) | -$9,400 | -7% |
| real price gains of 1890-2022 | C2.2 | all adults | -$12,400 (-$13,300 to -$11,500) | -$0 (-$0 to -$0) | +$9,600 ($8,600 to $10,600) | -$2,800 | 443% |
| new saving split by the group's asset shares | release | all adults | +$700 (-$0 to $1,400) | -$0 (-$0 to -$0) | +$24,100 ($23,600 to $24,600) | +$24,800 | 3% |
| new saving split by the group's asset shares | C2.2 | all adults | -$12,400 (-$13,300 to -$11,500) | -$0 (-$0 to -$0) | +$108,300 ($107,700 to $108,900) | +$95,900 | -13% |
| fixed-rate debt reprices too (no debt relief) | release | all adults | -$67,700 (-$68,600 to -$66,800) | -$0 (-$0 to -$0) | -$5,400 (-$6,100 to -$4,800) | -$73,200 | 93% |
|  |  | fifth 1 of starting wealth | -$3,400 (-$3,500 to -$3,300) | -$0 (-$0 to -$0) | +$800 ($200 to $1,300) | -$2,700 | 128% |
|  |  | fifth 2 of starting wealth | -$6,900 (-$7,000 to -$6,800) | -$0 (-$0 to -$0) | +$2,400 ($1,400 to $3,500) | -$4,500 | 154% |
|  |  | fifth 3 of starting wealth | -$17,500 (-$17,700 to -$17,300) | -$0 (-$0 to -$0) | +$2,200 ($700 to $3,700) | -$15,400 | 114% |
|  |  | fifth 4 of starting wealth | -$44,800 (-$45,500 to -$44,100) | -$0 (-$0 to -$0) | -$6,000 (-$7,600 to -$4,500) | -$50,800 | 88% |
|  |  | fifth 5 of starting wealth | -$266,000 (-$270,400 to -$261,200) | -$0 (-$0 to -$0) | -$26,500 (-$27,900 to -$25,000) | -$292,500 | 91% |
| fixed-rate debt reprices too (no debt relief) | C2.2 | all adults | -$84,900 (-$85,900 to -$83,800) | -$0 (-$0 to -$0) | +$9,700 ($8,700 to $10,700) | -$75,100 | 113% |
|  |  | fifth 1 of starting wealth | -$4,300 (-$4,400 to -$4,200) | -$0 (-$0 to -$0) | +$8,600 ($7,900 to $9,300) | +$4,300 | -99% |
|  |  | fifth 2 of starting wealth | -$8,600 (-$8,700 to -$8,500) | -$0 (-$0 to -$0) | +$25,500 ($24,000 to $26,900) | +$16,800 | -51% |
|  |  | fifth 3 of starting wealth | -$22,000 (-$22,200 to -$21,800) | -$0 (-$0 to -$0) | +$28,400 ($26,100 to $30,600) | +$6,400 | -342% |
|  |  | fifth 4 of starting wealth | -$56,100 (-$56,900 to -$55,400) | -$0 (-$0 to -$0) | +$12,300 ($9,700 to $14,800) | -$43,800 | 128% |
|  |  | fifth 5 of starting wealth | -$333,400 (-$338,900 to -$327,700) | -$0 (-$0 to -$0) | -$26,200 (-$28,300 to -$23,800) | -$359,500 | 93% |

## 4. Levels of the three parts under the main reading (Year-0 dollars per adult, year 20), and the start

**Reference**

| Group | start: nominal position / real assets | no programme: E / V / S | release: E / V / S | C2.2: E / V / S |
|---|---|---|---|---|
| all adults | -$10,100 / $517,200 | -$10,100 / $817,300 / $91,000 | -$4,400 / $817,300 / $67,000 | -$6,500 / $817,300 / $90,600 |
| fifth 1 | -$39,300 / $26,900 | -$39,300 / $32,400 / $46,800 | -$3,200 / $32,400 / $31,000 | -$3,200 / $32,400 / $55,300 |
| fifth 2 | -$49,800 / $92,200 | -$49,800 / $112,700 / $48,300 | -$5,200 / $112,700 / $44,600 | -$5,300 / $112,700 / $70,800 |
| fifth 3 | -$82,800 / $211,700 | -$82,800 / $268,000 / $70,800 | -$8,800 / $268,000 / $61,200 | -$9,200 / $268,000 / $85,600 |
| fifth 4 | -$62,600 / $390,300 | -$62,600 / $523,800 / $104,200 | -$7,800 / $523,800 / $77,400 | -$9,100 / $523,800 / $100,800 |
| fifth 5 | $184,200 / $1,865,100 | $184,200 / $3,149,800 / $185,000 | $3,300 / $3,149,800 / $121,000 | -$5,900 / $3,149,800 / $140,600 |

**Adverse**

| Group | start: nominal position / real assets | no programme: E / V / S | release: E / V / S | C2.2: E / V / S |
|---|---|---|---|---|
| all adults | -$10,100 / $517,200 | $3,500 / $817,300 / $37,000 | -$7,300 / $817,300 / $34,300 | -$8,600 / $817,300 / $56,500 |
| fifth 1 | -$39,300 / $26,900 | -$27,300 / $32,400 / $17,900 | -$3,300 / $32,400 / $10,700 | -$3,300 / $32,400 / $31,500 |
| fifth 2 | -$49,800 / $92,200 | -$34,500 / $112,700 / $3,200 | -$5,300 / $112,700 / $16,200 | -$5,400 / $112,700 / $41,600 |
| fifth 3 | -$82,800 / $211,700 | -$56,500 / $268,000 / $13,700 | -$9,300 / $268,000 / $29,200 | -$9,600 / $268,000 / $52,800 |
| fifth 4 | -$62,600 / $390,300 | -$37,600 / $523,800 / $41,200 | -$9,600 / $523,800 / $40,700 | -$10,400 / $523,800 / $63,100 |
| fifth 5 | $184,200 / $1,865,100 | $173,200 / $3,149,800 / $109,000 | -$9,100 / $3,149,800 / $74,900 | -$14,500 / $3,149,800 / $93,400 |

**Stress**

| Group | start: nominal position / real assets | no programme: E / V / S | release: E / V / S | C2.2: E / V / S |
|---|---|---|---|---|
| all adults | -$10,100 / $517,200 | $3,500 / $817,300 / $37,000 | $4,200 / $817,300 / $27,600 | -$8,900 / $817,300 / $47,700 |
| fifth 1 | -$39,300 / $26,900 | -$27,300 / $32,400 / $17,900 | -$4,000 / $32,400 / $5,500 | -$3,300 / $32,400 / $24,300 |
| fifth 2 | -$49,800 / $92,200 | -$34,500 / $112,700 / $3,200 | -$5,800 / $112,700 / $100 | -$5,400 / $112,700 / $33,500 |
| fifth 3 | -$82,800 / $211,700 | -$56,500 / $268,000 / $13,700 | -$9,100 / $268,000 / $15,000 | -$9,700 / $268,000 / $44,200 |
| fifth 4 | -$62,600 / $390,300 | -$37,600 / $523,800 / $41,200 | -$3,900 / $523,800 / $35,000 | -$10,600 / $523,800 / $53,700 |
| fifth 5 | $184,200 / $1,865,100 | $173,200 / $3,149,800 / $109,000 | $43,500 / $3,149,800 / $82,300 | -$15,700 / $3,149,800 / $82,800 |

## 5. The no-programme run: the start and year 20, today's reading and the main reading

| Environment | Measure | start | year 20, off | year 20, main | year 20, no real price gain |
|---|---|---|---|---|---|
| Reference | median real wealth | $127,600 | $212,300 | $265,800 | $212,300 |
| Reference | top 1% share (%) | 20.8 | 18.2 | 21.2 | 18.2 |
| Reference | top 10% share (%) | 64.6 | 58.9 | 63.8 | 58.9 |
| Reference | bottom 50% share (%) | 3.6 | 5.2 | 4.6 | 5.2 |
| Reference | families in debt (%) | 13.4 | 22.0 | 20.0 | 22.0 |
| Adverse | median real wealth | $127,600 | $116,000 | $232,500 | $179,700 |
| Adverse | top 1% share (%) | 20.8 | 19.3 | 21.9 | 19.0 |
| Adverse | top 10% share (%) | 64.6 | 61.9 | 65.3 | 60.8 |
| Adverse | bottom 50% share (%) | 3.6 | 3.0 | 3.7 | 4.0 |
| Adverse | families in debt (%) | 13.4 | 30.5 | 24.1 | 26.5 |
| Stress | median real wealth | $127,600 | $116,000 | $232,500 | $179,700 |
| Stress | top 1% share (%) | 20.8 | 19.3 | 21.9 | 19.0 |
| Stress | top 10% share (%) | 64.6 | 61.9 | 65.3 | 60.8 |
| Stress | bottom 50% share (%) | 3.6 | 3.0 | 3.7 | 4.0 |
| Stress | families in debt (%) | 13.4 | 30.5 | 24.1 | 26.5 |

## 6. The top 1% of adults' share of private business equity (%, main reading)

| Environment | start | year 20, no programme | year 20, release | year 20, C2.2 |
|---|---|---|---|---|
| Reference | 47.5 | 48.1 | 48.2 | 48.2 |
| Adverse | 47.5 | 48.1 | 48.2 | 48.2 |
| Stress | 47.5 | 48.1 | 48.2 | 48.2 |

Year-20 holdings under the main reading (Year-0 dollars per adult: real assets / nominal assets / floating debt / fixed-rate debt): Reference: no programme $817,300 / $198,200 / $11,600 / $105,700, release $817,300 / $67,600 / $4,400 / $600, C2.2 $817,300 / $84,800 / $500 / $300; Adverse: no programme $817,300 / $133,300 / $20,300 / $72,600, release $817,300 / $34,800 / $7,600 / $200, C2.2 $817,300 / $48,800 / $900 / $100; Stress: no programme $817,300 / $133,300 / $20,300 / $72,600, release $817,300 / $53,600 / $17,800 / $4,100, C2.2 $817,300 / $40,100 / $1,300 / $100.
