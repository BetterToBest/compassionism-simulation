# The frozen engine's corrections, measured (S47): tables

Written by `node dev/tools/s47_fx_measure.js --table dev/runs/s47-fx/s47-fx-{ref,adv,st}.json.gz` from the runs of Nov 5, 2026 (seeds 1-50, CPS earnings yardstick, 500 adults, 20 years). The plain-words reading is `dev/reports/s47-fx.md`. In the first table of each design, the columns pthb, hb, ab and sp are each part alone added to the audit-corrected engine (au), minus au.

### Reference (seeds 1-50, 50 paired; 445 s on one process)

Levels on the published engine, and the change each setting makes against the audit-corrected engine (au); the last column is the frozen engine against the published one. Mean change, with its 95% interval, over the paired seeds.

**No programme**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 27.33 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.39 ± 0.03 | -0.39 ± 0.03 | -0.39 ± 0.03 |
| wealth poverty, year 20 (%) | 20.38 | 0.01 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.26 ± 0.07 | -0.26 ± 0.07 | -0.26 ± 0.07 |
| BLEI below precarious, year 20 (%) | 19.13 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.28 ± 0.07 | -0.28 ± 0.07 | -0.28 ± 0.07 |
| design-neutral BLEI below precarious (%) | 19.13 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.28 ± 0.07 | -0.28 ± 0.07 | -0.28 ± 0.07 |
| basket poverty severity (FGT2 x100) | 4.27 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.07 ± 0.00 | -0.07 ± 0.00 | -0.07 ± 0.00 |
| programme inflation (yearly rate, %) | 0.04 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.04 ± 0.00 | -0.04 ± 0.00 | -0.04 ± 0.00 |
| price level, year 20 | 1.0068 | -0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0068 ± 0.0002 | -0.0068 ± 0.0002 | -0.0068 ± 0.0002 |
| median real wealth, year 20 ($) | 403289 | 0.86 ± 0.37 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 5829 ± 226 | 5829 ± 226 | 5830 ± 226 |
| programme cost per adult-year ($) | 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
| employment (%) | 99.81 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
| Gini, disposable income | 0.3354 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0001 ± 0.0000 | -0.0001 ± 0.0000 | -0.0001 ± 0.0000 |
| SNAP work-rule months lost (per adult) | 0.48 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.00 ± 0.00 | -0.01 ± 0.00 | -0.01 ± 0.00 |

**Release design**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 9.99 | 0.25 ± 0.03 | -0.00 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.17 ± 0.02 | -0.18 ± 0.03 | 0.07 ± 0.04 |
| wealth poverty, year 20 (%) | 16.43 | 0.55 ± 0.10 | -0.02 ± 0.06 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.37 ± 0.11 | -0.36 ± 0.11 | 0.20 ± 0.12 |
| BLEI below precarious, year 20 (%) | 6.23 | 0.65 ± 0.11 | -0.07 ± 0.05 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.08 ± 0.03 | -0.14 ± 0.06 | 0.50 ± 0.13 |
| design-neutral BLEI below precarious (%) | 6.35 | 1.01 ± 0.12 | -0.02 ± 0.04 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.15 ± 0.05 | -0.14 ± 0.06 | 0.87 ± 0.12 |
| basket poverty severity (FGT2 x100) | 0.78 | 0.02 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.02 ± 0.00 | -0.01 ± 0.00 | 0.00 ± 0.00 |
| programme inflation (yearly rate, %) | 32.01 | 0.00 ± 0.01 | -0.01 ± 0.01 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.39 ± 0.01 | -0.40 ± 0.01 | -0.39 ± 0.01 |
| price level, year 20 | 198.8061 | 0.0370 ± 0.1902 | -0.2069 ± 0.2244 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -10.9460 ± 0.8046 | -11.1441 ± 0.8433 | -11.1070 ± 0.8353 |
| median real wealth, year 20 ($) | 91809 | -161 ± 118 | 3.17 ± 143 | 0.00 ± 0.00 | 0.00 ± 0.00 | 1792 ± 79.23 | 1806 ± 167 | 1646 ± 194 |
| programme cost per adult-year ($) | 32733 | -16.03 ± 3.66 | -2.25 ± 2.89 | 0.00 ± 0.00 | 0.00 ± 0.00 | 72.05 ± 2.11 | 69.75 ± 3.67 | 53.72 ± 4.81 |
| employment (%) | 99.77 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 |
| Gini, disposable income | 0.3481 | 0.0014 ± 0.0002 | 0.0000 ± 0.0001 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0003 ± 0.0001 | -0.0003 ± 0.0001 | 0.0011 ± 0.0002 |
| SNAP work-rule months lost (per adult) | 0.54 | 0.02 ± 0.01 | -0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.01 ± 0.00 | -0.01 ± 0.00 | 0.00 ± 0.01 |

**C2.2 design**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 1.82 | 0.33 ± 0.04 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.07 ± 0.01 | 0.07 ± 0.01 | 0.40 ± 0.04 |
| wealth poverty, year 20 (%) | 0.52 | 2.08 ± 0.15 | 0.00 ± 0.01 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.12 ± 0.04 | 0.10 ± 0.04 | 2.18 ± 0.16 |
| BLEI below precarious, year 20 (%) | 0.00 | 0.14 ± 0.04 | -0.00 ± 0.01 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.04 ± 0.03 | 0.04 ± 0.03 | 0.18 ± 0.05 |
| design-neutral BLEI below precarious (%) | 0.00 | 0.20 ± 0.06 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.02 ± 0.02 | 0.02 ± 0.02 | 0.23 ± 0.06 |
| basket poverty severity (FGT2 x100) | 0.06 | 0.01 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.01 ± 0.00 |
| programme inflation (yearly rate, %) | 37.69 | 0.01 ± 0.01 | 0.01 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.26 ± 0.01 | -0.26 ± 0.01 | -0.25 ± 0.01 |
| price level, year 20 | 441.6048 | 0.6222 ± 0.3215 | 0.3022 ± 0.2183 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -15.8047 ± 1.0331 | -15.5430 ± 1.0773 | -14.9207 ± 1.1811 |
| median real wealth, year 20 ($) | 133428 | 83.42 ± 122 | 43.53 ± 44.37 | 0.00 ± 0.00 | 0.00 ± 0.00 | -325 ± 142 | -274 ± 144 | -191 ± 128 |
| programme cost per adult-year ($) | 61391 | -7.72 ± 11.15 | -8.30 ± 4.50 | 0.00 ± 0.00 | 0.00 ± 0.00 | -862 ± 18.53 | -870 ± 17.40 | -878 ± 18.05 |
| employment (%) | 99.72 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
| Gini, disposable income | 0.2907 | 0.0008 ± 0.0002 | -0.0001 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0013 ± 0.0001 | 0.0013 ± 0.0001 | 0.0020 ± 0.0002 |
| SNAP work-rule months lost (per adult) | 0.45 | 0.05 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.01 ± 0.01 | -0.01 ± 0.01 | 0.05 ± 0.01 |

**Programme effects (design minus no programme, paired): how the corrections move them**

| Design | Measure | published | au | frozen | frozen - published |
|---|---|---|---|---|---|
| release | basket poverty (% of person-years) | -17.33 | -17.09 | -16.87 | 0.46 ± 0.05 |
| release | wealth poverty, year 20 (%) | -3.95 | -3.41 | -3.50 | 0.45 ± 0.14 |
| release | BLEI below precarious, year 20 (%) | -12.90 | -12.26 | -12.12 | 0.78 ± 0.13 |
| release | programme inflation (yearly rate, %) | 31.98 | 31.98 | 31.62 | -0.36 ± 0.01 |
| release | median real wealth, year 20 ($) | -311479 | -311641 | -315664 | -4184 ± 303 |
| c22 | basket poverty (% of person-years) | -25.51 | -25.18 | -24.71 | 0.79 ± 0.06 |
| c22 | wealth poverty, year 20 (%) | -19.86 | -17.79 | -17.42 | 2.44 ± 0.18 |
| c22 | BLEI below precarious, year 20 (%) | -19.13 | -18.99 | -18.67 | 0.46 ± 0.09 |
| c22 | programme inflation (yearly rate, %) | 37.66 | 37.67 | 37.45 | -0.21 ± 0.01 |
| c22 | median real wealth, year 20 ($) | -269861 | -269779 | -275882 | -6020 ± 249 |

### Adverse (seeds 1-50, 50 paired; 450 s on one process)

Levels on the published engine, and the change each setting makes against the audit-corrected engine (au); the last column is the frozen engine against the published one. Mean change, with its 95% interval, over the paired seeds.

**No programme**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 38.65 | 0.01 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.31 ± 0.02 | -0.31 ± 0.02 | -0.30 ± 0.02 |
| wealth poverty, year 20 (%) | 29.45 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.28 ± 0.10 | -0.28 ± 0.10 | -0.28 ± 0.10 |
| BLEI below precarious, year 20 (%) | 26.98 | 0.01 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.22 ± 0.07 | -0.22 ± 0.07 | -0.20 ± 0.06 |
| design-neutral BLEI below precarious (%) | 26.98 | 0.01 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.22 ± 0.07 | -0.22 ± 0.07 | -0.20 ± 0.06 |
| basket poverty severity (FGT2 x100) | 7.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.07 ± 0.00 | -0.07 ± 0.00 | -0.07 ± 0.00 |
| programme inflation (yearly rate, %) | 0.00 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.00 ± 0.00 | -0.00 ± 0.00 |
| price level, year 20 | 1.4578 | -0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0010 ± 0.0005 | -0.0010 ± 0.0005 | -0.0010 ± 0.0005 |
| median real wealth, year 20 ($) | 204854 | 7.27 ± 1.47 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 1885 ± 167 | 1885 ± 167 | 1893 ± 168 |
| programme cost per adult-year ($) | 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
| employment (%) | 99.63 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
| Gini, disposable income | 0.3417 | 0.0001 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0001 ± 0.0000 | -0.0001 ± 0.0000 | 0.0000 ± 0.0000 |
| SNAP work-rule months lost (per adult) | 1.04 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.01 ± 0.00 | -0.01 ± 0.00 | -0.01 ± 0.00 |

**Release design**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 15.69 | 0.23 ± 0.04 | -0.01 ± 0.03 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.31 ± 0.02 | -0.32 ± 0.03 | -0.09 ± 0.05 |
| wealth poverty, year 20 (%) | 39.63 | 0.98 ± 0.16 | -0.08 ± 0.09 | 0.00 ± 0.00 | 0.00 ± 0.00 | -1.03 ± 0.18 | -1.05 ± 0.18 | -0.07 ± 0.23 |
| BLEI below precarious, year 20 (%) | 13.57 | 1.17 ± 0.16 | -0.15 ± 0.08 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.36 ± 0.07 | -0.48 ± 0.12 | 0.68 ± 0.18 |
| design-neutral BLEI below precarious (%) | 15.60 | 2.50 ± 0.27 | -0.08 ± 0.08 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.38 ± 0.11 | -0.43 ± 0.13 | 2.07 ± 0.24 |
| basket poverty severity (FGT2 x100) | 1.31 | 0.02 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.03 ± 0.00 | -0.03 ± 0.00 | -0.01 ± 0.00 |
| programme inflation (yearly rate, %) | 38.26 | 0.02 ± 0.01 | -0.01 ± 0.01 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.59 ± 0.02 | -0.60 ± 0.02 | -0.58 ± 0.02 |
| price level, year 20 | 702.2019 | 1.4909 ± 0.9683 | -0.7983 ± 0.9964 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -55.6293 ± 4.5430 | -56.2334 ± 4.7929 | -54.7426 ± 4.8387 |
| median real wealth, year 20 ($) | 36116 | -430 ± 126 | 20.38 ± 55.87 | 0.00 ± 0.00 | 0.00 ± 0.00 | 1334 ± 54.10 | 1328 ± 74.62 | 898 ± 146 |
| programme cost per adult-year ($) | 31294 | -18.89 ± 4.10 | -2.18 ± 2.75 | 0.00 ± 0.00 | 0.00 ± 0.00 | 90.71 ± 2.13 | 88.17 ± 3.91 | 69.28 ± 5.48 |
| employment (%) | 99.52 | -0.01 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.01 ± 0.00 | -0.00 ± 0.01 |
| Gini, disposable income | 0.3658 | 0.0021 ± 0.0003 | 0.0001 ± 0.0001 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0008 ± 0.0001 | -0.0007 ± 0.0001 | 0.0014 ± 0.0004 |
| SNAP work-rule months lost (per adult) | 1.19 | 0.03 ± 0.01 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.03 ± 0.01 | -0.04 ± 0.01 | -0.01 ± 0.01 |

**C2.2 design**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 2.50 | 0.44 ± 0.05 | -0.00 ± 0.01 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.15 ± 0.02 | 0.15 ± 0.02 | 0.59 ± 0.05 |
| wealth poverty, year 20 (%) | 5.95 | 5.20 ± 0.30 | 0.00 ± 0.05 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.68 ± 0.14 | 0.64 ± 0.13 | 5.83 ± 0.33 |
| BLEI below precarious, year 20 (%) | 0.04 | 0.33 ± 0.07 | 0.00 ± 0.01 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.18 ± 0.05 | 0.18 ± 0.05 | 0.51 ± 0.08 |
| design-neutral BLEI below precarious (%) | 0.00 | 0.56 ± 0.09 | -0.00 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.11 ± 0.04 | 0.11 ± 0.04 | 0.68 ± 0.10 |
| basket poverty severity (FGT2 x100) | 0.07 | 0.02 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.01 ± 0.00 | 0.02 ± 0.00 |
| programme inflation (yearly rate, %) | 44.28 | 0.03 ± 0.01 | 0.01 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.35 ± 0.01 | -0.35 ± 0.01 | -0.31 ± 0.01 |
| price level, year 20 | 1573.5166 | 6.6738 ± 1.5307 | 1.1691 ± 1.0520 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -72.4816 ± 5.2809 | -71.3381 ± 5.4757 | -64.6643 ± 5.6767 |
| median real wealth, year 20 ($) | 67730 | -467 ± 167 | 31.14 ± 55.30 | 0.00 ± 0.00 | 0.00 ± 0.00 | -539 ± 107 | -520 ± 119 | -987 ± 174 |
| programme cost per adult-year ($) | 58597 | 28.09 ± 11.84 | -8.65 ± 4.78 | 0.00 ± 0.00 | 0.00 ± 0.00 | -1000 ± 21.42 | -1009 ± 20.48 | -981 ± 21.48 |
| employment (%) | 99.39 | -0.01 ± 0.01 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.02 ± 0.01 | 0.02 ± 0.01 | 0.01 ± 0.01 |
| Gini, disposable income | 0.3022 | 0.0011 ± 0.0003 | -0.0001 ± 0.0001 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0027 ± 0.0001 | 0.0027 ± 0.0001 | 0.0038 ± 0.0003 |
| SNAP work-rule months lost (per adult) | 0.91 | 0.09 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.00 ± 0.01 | -0.00 ± 0.01 | 0.09 ± 0.02 |

**Programme effects (design minus no programme, paired): how the corrections move them**

| Design | Measure | published | au | frozen | frozen - published |
|---|---|---|---|---|---|
| release | basket poverty (% of person-years) | -22.96 | -22.74 | -22.74 | 0.22 ± 0.05 |
| release | wealth poverty, year 20 (%) | 10.18 | 11.16 | 10.39 | 0.22 ± 0.25 |
| release | BLEI below precarious, year 20 (%) | -13.41 | -12.26 | -12.52 | 0.89 ± 0.20 |
| release | programme inflation (yearly rate, %) | 38.26 | 38.27 | 37.68 | -0.58 ± 0.02 |
| release | median real wealth, year 20 ($) | -168738 | -169175 | -169732 | -994 ± 220 |
| c22 | basket poverty (% of person-years) | -36.14 | -35.71 | -35.25 | 0.89 ± 0.05 |
| c22 | wealth poverty, year 20 (%) | -23.50 | -18.31 | -17.39 | 6.12 ± 0.37 |
| c22 | BLEI below precarious, year 20 (%) | -26.94 | -26.62 | -26.23 | 0.71 ± 0.10 |
| c22 | programme inflation (yearly rate, %) | 44.27 | 44.31 | 43.96 | -0.31 ± 0.01 |
| c22 | median real wealth, year 20 ($) | -137125 | -137599 | -140004 | -2880 ± 260 |

### Stress (seeds 1-50, 50 paired; 395 s on one process)

Levels on the published engine, and the change each setting makes against the audit-corrected engine (au); the last column is the frozen engine against the published one. Mean change, with its 95% interval, over the paired seeds.

**No programme**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 38.65 | 0.01 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.31 ± 0.02 | -0.31 ± 0.02 | -0.30 ± 0.02 |
| wealth poverty, year 20 (%) | 29.45 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.28 ± 0.10 | -0.28 ± 0.10 | -0.28 ± 0.10 |
| BLEI below precarious, year 20 (%) | 26.98 | 0.01 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.22 ± 0.07 | -0.22 ± 0.07 | -0.20 ± 0.06 |
| design-neutral BLEI below precarious (%) | 26.98 | 0.01 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.22 ± 0.07 | -0.22 ± 0.07 | -0.20 ± 0.06 |
| basket poverty severity (FGT2 x100) | 7.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.07 ± 0.00 | -0.07 ± 0.00 | -0.07 ± 0.00 |
| programme inflation (yearly rate, %) | 0.00 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.00 ± 0.00 | -0.00 ± 0.00 |
| price level, year 20 | 1.4578 | -0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0010 ± 0.0005 | -0.0010 ± 0.0005 | -0.0010 ± 0.0005 |
| median real wealth, year 20 ($) | 204854 | 7.27 ± 1.47 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 1885 ± 167 | 1885 ± 167 | 1893 ± 168 |
| programme cost per adult-year ($) | 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
| employment (%) | 99.63 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
| Gini, disposable income | 0.3417 | 0.0001 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0001 ± 0.0000 | -0.0001 ± 0.0000 | 0.0000 ± 0.0000 |
| SNAP work-rule months lost (per adult) | 1.04 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.01 ± 0.00 | -0.01 ± 0.00 | -0.01 ± 0.00 |

**Release design**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 29.91 | 0.09 ± 0.02 | 0.01 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.47 ± 0.03 | -0.48 ± 0.03 | -0.39 ± 0.04 |
| wealth poverty, year 20 (%) | 40.40 | 0.74 ± 0.16 | -0.05 ± 0.06 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.79 ± 0.14 | -0.78 ± 0.14 | -0.04 ± 0.19 |
| BLEI below precarious, year 20 (%) | 29.68 | 0.53 ± 0.13 | -0.02 ± 0.10 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.54 ± 0.10 | -0.59 ± 0.14 | -0.06 ± 0.19 |
| design-neutral BLEI below precarious (%) | 31.01 | 0.66 ± 0.15 | 0.02 ± 0.04 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.62 ± 0.11 | -0.63 ± 0.11 | 0.03 ± 0.19 |
| basket poverty severity (FGT2 x100) | 4.16 | 0.04 ± 0.00 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.08 ± 0.00 | -0.08 ± 0.00 | -0.03 ± 0.01 |
| programme inflation (yearly rate, %) | 16.87 | -0.01 ± 0.00 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.24 ± 0.01 | -0.24 ± 0.01 | -0.25 ± 0.01 |
| price level, year 20 | 28.8027 | -0.0277 ± 0.0241 | -0.0031 ± 0.0051 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -1.1231 ± 0.0943 | -1.1263 ± 0.0950 | -1.1539 ± 0.0965 |
| median real wealth, year 20 ($) | 45725 | -879 ± 298 | 116 ± 120 | 0.00 ± 0.00 | 0.00 ± 0.00 | 1821 ± 127 | 1919 ± 146 | 1040 ± 331 |
| programme cost per adult-year ($) | 12360 | 9.23 ± 2.89 | -2.65 ± 1.38 | 0.00 ± 0.00 | 0.00 ± 0.00 | 7.28 ± 0.65 | 4.71 ± 1.50 | 13.93 ± 3.19 |
| employment (%) | 99.60 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
| Gini, disposable income | 0.3547 | 0.0018 ± 0.0001 | -0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -0.0001 ± 0.0001 | -0.0000 ± 0.0001 | 0.0018 ± 0.0001 |
| SNAP work-rule months lost (per adult) | 1.10 | 0.01 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.02 ± 0.00 | -0.02 ± 0.00 | -0.01 ± 0.01 |

**C2.2 design**

| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |
|---|---|---|---|---|---|---|---|---|
| basket poverty (% of person-years) | 3.36 | 0.25 ± 0.04 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.18 ± 0.02 | 0.18 ± 0.02 | 0.43 ± 0.04 |
| wealth poverty, year 20 (%) | 18.20 | 2.83 ± 0.27 | 0.00 ± 0.03 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.36 ± 0.11 | 0.32 ± 0.10 | 3.16 ± 0.27 |
| BLEI below precarious, year 20 (%) | 0.21 | 0.71 ± 0.11 | -0.02 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.41 ± 0.08 | 0.40 ± 0.09 | 1.10 ± 0.12 |
| design-neutral BLEI below precarious (%) | 0.01 | 1.25 ± 0.14 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.15 ± 0.06 | 0.15 ± 0.06 | 1.40 ± 0.15 |
| basket poverty severity (FGT2 x100) | 0.09 | 0.01 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.01 ± 0.00 | 0.01 ± 0.00 | 0.02 ± 0.00 |
| programme inflation (yearly rate, %) | 46.32 | 0.05 ± 0.01 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.52 ± 0.01 | -0.52 ± 0.01 | -0.47 ± 0.02 |
| price level, year 20 | 2067.9756 | 13.6686 ± 2.1845 | 0.9052 ± 1.0484 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | -137.6431 ± 11.6266 | -136.8985 ± 11.4853 | -123.2299 ± 11.0533 |
| median real wealth, year 20 ($) | 52114 | -648 ± 142 | 16.98 ± 15.74 | 0.00 ± 0.00 | 0.00 ± 0.00 | 58.17 ± 94.30 | 78.99 ± 92.43 | -569 ± 166 |
| programme cost per adult-year ($) | 51015 | 29.93 ± 9.09 | -3.63 ± 2.76 | 0.00 ± 0.00 | 0.00 ± 0.00 | -796 ± 16.58 | -799 ± 16.93 | -770 ± 16.73 |
| employment (%) | 99.37 | -0.01 ± 0.01 | -0.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 | 0.02 ± 0.01 | 0.02 ± 0.01 | 0.01 ± 0.01 |
| Gini, disposable income | 0.3207 | 0.0004 ± 0.0003 | -0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0022 ± 0.0001 | 0.0022 ± 0.0001 | 0.0026 ± 0.0003 |
| SNAP work-rule months lost (per adult) | 1.20 | 0.06 ± 0.02 | 0.00 ± 0.00 | 0.00 ± 0.00 | -0.00 ± 0.00 | -0.01 ± 0.01 | -0.02 ± 0.01 | 0.04 ± 0.02 |

**Programme effects (design minus no programme, paired): how the corrections move them**

| Design | Measure | published | au | frozen | frozen - published |
|---|---|---|---|---|---|
| release | basket poverty (% of person-years) | -8.74 | -8.66 | -8.82 | -0.09 ± 0.04 |
| release | wealth poverty, year 20 (%) | 10.95 | 11.69 | 11.19 | 0.24 ± 0.20 |
| release | BLEI below precarious, year 20 (%) | 2.70 | 3.22 | 2.85 | 0.14 ± 0.20 |
| release | programme inflation (yearly rate, %) | 16.87 | 16.86 | 16.62 | -0.24 ± 0.01 |
| release | median real wealth, year 20 ($) | -159130 | -160016 | -159983 | -853 ± 356 |
| c22 | basket poverty (% of person-years) | -35.28 | -35.04 | -34.55 | 0.73 ± 0.04 |
| c22 | wealth poverty, year 20 (%) | -11.25 | -8.42 | -7.81 | 3.44 ± 0.29 |
| c22 | BLEI below precarious, year 20 (%) | -26.77 | -26.07 | -25.46 | 1.31 ± 0.13 |
| c22 | programme inflation (yearly rate, %) | 46.32 | 46.37 | 45.86 | -0.46 ± 0.02 |
| c22 | median real wealth, year 20 ($) | -152740 | -153396 | -155202 | -2462 ± 228 |

