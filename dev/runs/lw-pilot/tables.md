# The cost-of-living line, weighted and current: pilot tables (S14, study L)

PILOT: seeds 1-100 (100 seeds), 500 adults, CPS earnings yardstick, octave raise off. Engine f66dc67; command per shard `node runner/jobs/lw.js --env=all --procs=2 --seeds=A-B --out=shard-NNNN.json` (compassionism-sim-results `pilot-l-f66dc67`). Written by `dev/tools/lw_pilot.py`. 95% paired bootstrap intervals in brackets; "ns": the interval includes zero. Preregistration: research-update `prereg/2026-11-lw-weighted-line.md`.

Lines: base $49,370 (current, unweighted mean); ext $51,201 (ext); bea $51,838 (bea). C2.2 needs level (BU, $ a month): base 1,788.43, ext 1,885.06, bea 1,918.43.


## Rule 1 summary: every cell (primary outcomes, difference in differences)

Columns: basic living (design-neutral, design reading), cost of living, wealth at the end ($25,000), cumulative inflation.

| Environment | Years | Row | Line | bNAPy | bOAPy | fgt0PY | wealth | inflation |
|---|---|---|---|---|---|---|---|---|
| Reference | 20 | main | ext | not changed | not changed | not changed | not changed | changed |
| Reference | 20 | main | bea | not changed | not changed | not changed | not changed | changed |
| Reference | 20 | c22 | ext | changed | small change | changed | changed | changed |
| Reference | 20 | c22 | bea | changed | changed | changed | changed | changed |
| Adverse | 20 | main | ext | not changed | not changed | not changed | changed | changed |
| Adverse | 20 | main | bea | not changed | not changed | not changed | changed | changed |
| Adverse | 20 | c22 | ext | changed | changed | changed | changed | changed |
| Adverse | 20 | c22 | bea | changed | changed | changed | changed | changed |
| Stress Test | 20 | main | ext | not changed | not changed | not changed | not changed | changed |
| Stress Test | 20 | main | bea | not changed | not changed | not changed | not changed | changed |
| Stress Test | 20 | c22 | ext | changed | changed | changed | changed | changed |
| Stress Test | 20 | c22 | bea | changed | changed | changed | changed | changed |
| Reference | 40 | main | ext | not changed | not changed | not changed | not changed | changed |
| Reference | 40 | main | bea | not changed | not changed | not changed | not changed | changed |
| Reference | 40 | c22 | ext | changed | changed | changed | changed | changed |
| Reference | 40 | c22 | bea | changed | changed | changed | changed | changed |
| Adverse | 40 | main | ext | changed | not changed | not changed | not changed | changed |
| Adverse | 40 | main | bea | changed | not changed | changed | not changed | changed |
| Adverse | 40 | c22 | ext | changed | changed | changed | changed | changed |
| Adverse | 40 | c22 | bea | changed | changed | changed | changed | changed |
| Stress Test | 40 | main | ext | not changed | not changed | not changed | not changed | changed |
| Stress Test | 40 | main | bea | not changed | not changed | not changed | not changed | changed |
| Stress Test | 40 | c22 | ext | changed | changed | changed | changed | changed |
| Stress Test | 40 | c22 | bea | changed | changed | changed | changed | changed |


## Reference, 20 years (headline cell)


### Levels

| Line | Row | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) |
|---|---|---|---|---|---|---|---|
| base | no programme | 17.6 (17.3 to 17.8) | 17.6 (17.3 to 17.8) | 27.2 (26.8 to 27.5) | 20.3 (20.0 to 20.7) | 0 (0 to 0) | 0.7 (0.7 to 0.7) |
| base | release row ($1,200, opt-in) | 6.9 (6.7 to 7.1) | 6.1 (6.0 to 6.3) | 10.1 (9.8 to 10.3) | 16.6 (16.2 to 17.0) | 32,583 (32,437 to 32,729) | 19,462 (18,808 to 20,134) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 0.2 (0.2 to 0.3) | 0.1 (0.0 to 0.1) | 1.8 (1.7 to 1.8) | 0.5 (0.5 to 0.6) | 61,278 (61,137 to 61,420) | 43,931 (42,612 to 45,310) |
| ext | no programme | 18.5 (18.2 to 18.7) | 18.5 (18.2 to 18.7) | 28.9 (28.5 to 29.2) | 21.5 (21.2 to 21.9) | 0 (0 to 0) | 0.8 (0.8 to 0.8) |
| ext | release row ($1,200, opt-in) | 7.8 (7.6 to 8.0) | 6.7 (6.6 to 6.9) | 11.5 (11.2 to 11.7) | 18.2 (17.8 to 18.6) | 32,497 (32,352 to 32,642) | 20,609 (19,911 to 21,328) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 0.1 (0.1 to 0.1) | 0.0 (0.0 to 0.0) | 1.8 (1.8 to 1.9) | 0.4 (0.3 to 0.4) | 64,885 (64,730 to 65,040) | 47,930 (46,472 to 49,456) |
| bea | no programme | 18.8 (18.5 to 19.0) | 18.8 (18.5 to 19.0) | 29.4 (29.1 to 29.8) | 21.9 (21.6 to 22.3) | 0 (0 to 0) | 0.8 (0.8 to 0.8) |
| bea | release row ($1,200, opt-in) | 8.2 (8.0 to 8.4) | 6.9 (6.8 to 7.1) | 12.0 (11.7 to 12.2) | 18.7 (18.3 to 19.1) | 32,471 (32,326 to 32,616) | 20,998 (20,283 to 21,733) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 1.8 (1.8 to 1.9) | 0.3 (0.3 to 0.4) | 66,133 (65,974 to 66,294) | 49,357 (47,856 to 50,932) |

### Levels: this study's own and secondary outcomes

| Line | Row | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| base | no programme | 23.8 (23.5 to 24.2) | 24.2 (23.8 to 24.6) | 31.8 (31.4 to 32.2) | 44.0 (43.1 to 44.9) | 4.23 (4.15 to 4.32) | 3.5 (3.3 to 3.7) |
| base | release row ($1,200, opt-in) | 20.3 (20.0 to 20.7) | 19.8 (19.3 to 20.2) | 11.9 (11.6 to 12.2) | 16.8 (16.3 to 17.4) | 0.76 (0.73 to 0.80) | 3.8 (3.7 to 4.0) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 8.3 (8.1 to 8.6) | 3.1 (2.8 to 3.3) | 2.8 (2.7 to 2.9) | 5.4 (5.1 to 5.7) | 0.05 (0.05 to 0.06) | 1.5 (1.4 to 1.6) |
| ext | no programme | 25.0 (24.6 to 25.3) | 25.6 (25.2 to 26.1) | 33.7 (33.2 to 34.1) | 46.4 (45.5 to 47.3) | 4.60 (4.51 to 4.69) | 3.4 (3.3 to 3.6) |
| ext | release row ($1,200, opt-in) | 22.2 (21.8 to 22.6) | 21.9 (21.4 to 22.3) | 13.6 (13.3 to 13.9) | 19.3 (18.7 to 20.0) | 0.87 (0.84 to 0.91) | 3.9 (3.7 to 4.1) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 8.3 (8.1 to 8.6) | 2.9 (2.7 to 3.2) | 2.8 (2.7 to 2.9) | 5.5 (5.2 to 5.8) | 0.05 (0.05 to 0.06) | 1.4 (1.3 to 1.5) |
| bea | no programme | 25.4 (25.1 to 25.8) | 26.1 (25.7 to 26.6) | 34.3 (33.9 to 34.8) | 47.2 (46.3 to 48.1) | 4.73 (4.64 to 4.82) | 3.4 (3.2 to 3.6) |
| bea | release row ($1,200, opt-in) | 22.9 (22.5 to 23.2) | 22.7 (22.2 to 23.2) | 14.2 (13.9 to 14.6) | 20.2 (19.6 to 20.9) | 0.91 (0.88 to 0.95) | 3.9 (3.7 to 4.1) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 8.3 (8.1 to 8.5) | 2.9 (2.6 to 3.1) | 2.9 (2.7 to 3.0) | 5.6 (5.3 to 5.9) | 0.05 (0.05 to 0.06) | 1.4 (1.3 to 1.4) |

### (a) No programme: the higher line minus the current line (positive = more people below the line)

| Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ext | 0.9 (0.8 to 1.0) | 0.9 (0.8 to 1.0) | 1.7 (1.6 to 1.7) | 1.2 (1.1 to 1.3) | 0.1 (0.1 to 0.1) | 1.2 (1.1 to 1.3) | 1.4 (1.3 to 1.6) | 1.9 (1.8 to 2.0) | 2.4 (2.3 to 2.5) | 0.36 (0.36 to 0.37) | -0.1 (-0.1 to -0.1) |
| bea | 1.2 (1.1 to 1.3) | 1.2 (1.1 to 1.3) | 2.3 (2.2 to 2.3) | 1.6 (1.4 to 1.7) | 0.2 (0.1 to 0.2) | 1.6 (1.5 to 1.7) | 1.9 (1.7 to 2.1) | 2.5 (2.5 to 2.6) | 3.2 (3.1 to 3.4) | 0.49 (0.49 to 0.50) | -0.1 (-0.1 to -0.1) |

### (b) Programme against no programme, at each line (shares: reductions, positive = fewer below)

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | base | 10.6 (10.4 to 10.9) | 11.4 (11.2 to 11.7) | 17.1 (16.8 to 17.4) | 3.8 (3.4 to 4.1) | 32,583 (32,437 to 32,729) | 19,461 (18,807 to 20,133) | 3.5 (3.2 to 3.8) | 4.5 (4.0 to 4.9) | 19.9 (19.5 to 20.2) | 27.2 (26.5 to 27.9) | 3.47 (3.40 to 3.54) | -0.3 (-0.4 to -0.2) |
| release row ($1,200, opt-in) | ext | 10.6 (10.3 to 10.9) | 11.7 (11.5 to 12.0) | 17.4 (17.1 to 17.7) | 3.3 (3.0 to 3.7) | 32,497 (32,352 to 32,642) | 20,608 (19,910 to 21,327) | 2.8 (2.5 to 3.1) | 3.8 (3.4 to 4.2) | 20.1 (19.7 to 20.4) | 27.1 (26.4 to 27.8) | 3.73 (3.65 to 3.80) | -0.5 (-0.6 to -0.4) |
| release row ($1,200, opt-in) | bea | 10.6 (10.3 to 10.9) | 11.8 (11.5 to 12.1) | 17.5 (17.1 to 17.8) | 3.2 (2.8 to 3.5) | 32,471 (32,326 to 32,616) | 20,997 (20,282 to 21,732) | 2.6 (2.3 to 2.8) | 3.4 (3.0 to 3.8) | 20.1 (19.7 to 20.5) | 27.0 (26.3 to 27.7) | 3.81 (3.74 to 3.89) | -0.5 (-0.6 to -0.4) |
| C2.2 design (automatic, all, needs level, needs-indexed) | base | 17.3 (17.1 to 17.6) | 17.5 (17.3 to 17.7) | 25.4 (25.0 to 25.7) | 19.8 (19.5 to 20.1) | 61,278 (61,137 to 61,420) | 43,930 (42,611 to 45,309) | 15.5 (15.2 to 15.8) | 21.1 (20.7 to 21.5) | 29.0 (28.6 to 29.4) | 38.6 (37.8 to 39.5) | 4.18 (4.10 to 4.26) | 2.0 (1.9 to 2.1) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 18.4 (18.1 to 18.6) | 18.4 (18.2 to 18.7) | 27.1 (26.7 to 27.4) | 21.2 (20.9 to 21.5) | 64,885 (64,730 to 65,040) | 47,929 (46,471 to 49,456) | 16.7 (16.3 to 17.0) | 22.7 (22.3 to 23.1) | 30.8 (30.4 to 31.3) | 40.9 (40.1 to 41.8) | 4.54 (4.46 to 4.63) | 2.0 (1.9 to 2.2) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 18.7 (18.5 to 19.0) | 18.7 (18.5 to 19.0) | 27.6 (27.3 to 28.0) | 21.6 (21.3 to 21.9) | 66,133 (65,974 to 66,294) | 49,356 (47,856 to 50,931) | 17.1 (16.8 to 17.4) | 23.3 (22.9 to 23.7) | 31.5 (31.0 to 31.9) | 41.7 (40.8 to 42.5) | 4.67 (4.59 to 4.76) | 2.0 (1.9 to 2.2) |

### (c) Does the effect depend on the line? (row - none) at the higher line minus (row - none) at the current line, rule 1 label

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Cost: effect as % of the base effect | Inflation: as % of the base effect |
|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -0.0 (-0.1 to 0.0), *not changed* | 0.3 (0.2 to 0.3), *not changed* | 0.3 (0.2 to 0.3), *not changed* | -0.4 (-0.6 to -0.2), *not changed* | -87 (-90 to -84) | 1,147 (1,100 to 1,196), *changed* | 99.7 (99.7 to 99.7) | 105.9 (105.8 to 106.0) |
| release row ($1,200, opt-in) | bea | -0.1 (-0.2 to 0.0), *not changed* | 0.4 (0.3 to 0.4), *not changed* | 0.3 (0.3 to 0.4), *not changed* | -0.6 (-0.8 to -0.4), *not changed* | -112 (-116 to -108) | 1,536 (1,472 to 1,601), *changed* | 99.7 (99.6 to 99.7) | 107.9 (107.8 to 108.0) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.1 (1.0 to 1.1), *changed* | 0.9 (0.9 to 1.0), *small change* | 1.7 (1.6 to 1.7), *changed* | 1.4 (1.2 to 1.5), *changed* | 3,607 (3,593 to 3,621) | 3,999 (3,856 to 4,149), *changed* | 105.9 (105.9 to 105.9) | 109.1 (109.0 to 109.2) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.4 (1.3 to 1.5), *changed* | 1.2 (1.2 to 1.3), *changed* | 2.2 (2.2 to 2.3), *changed* | 1.8 (1.6 to 1.9), *changed* | 4,855 (4,837 to 4,874) | 5,426 (5,235 to 5,626), *changed* | 107.9 (107.9 to 107.9) | 112.4 (112.2 to 112.5) |

### (c) for this study's own and secondary outcomes (reductions; rule 1 label)

| Row | Line | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -0.7 (-0.8 to -0.6), *not changed* | -0.7 (-0.9 to -0.4), *not changed* | 0.2 (0.1 to 0.3), *not changed* | -0.0 (-0.3 to 0.2), *not changed* | 0.25 (0.25 to 0.26), *not changed* | -0.1 (-0.2 to -0.1), *not changed* |
| release row ($1,200, opt-in) | bea | -0.9 (-1.1 to -0.8), *small change* | -1.0 (-1.3 to -0.7), *changed* | 0.2 (0.1 to 0.3), *not changed* | -0.2 (-0.4 to 0.1), *not changed* | 0.34 (0.33 to 0.35), *not changed* | -0.2 (-0.2 to -0.2), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.2 (1.1 to 1.3), *changed* | 1.6 (1.4 to 1.8), *changed* | 1.8 (1.8 to 1.9), *changed* | 2.3 (2.2 to 2.4), *changed* | 0.36 (0.36 to 0.37), *not changed* | 0.0 (0.0 to 0.1), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.6 (1.5 to 1.7), *changed* | 2.2 (1.9 to 2.4), *changed* | 2.5 (2.4 to 2.5), *changed* | 3.0 (2.9 to 3.2), *changed* | 0.49 (0.49 to 0.50), *not changed* | 0.0 (0.0 to 0.1), *not changed* |

### Coverage, participation and distribution (levels)

| Line | Row | Adult-years receiving the BU (%) | Adult-years the BU covers the C2.2 needs (%) | Mean share of the C2.2 needs covered (%) | Participation in the last year (%) | Non-participants below the cost of living (% of their years) | Non-participants with too little wealth (%) | Hours (mean) | Gini, disposable income | Gini, wealth |
|---|---|---|---|---|---|---|---|---|---|---|
| base | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.334 (0.331 to 0.337) | 0.663 (0.658 to 0.667) |
| base | release row ($1,200, opt-in) | 83.4 (83.0 to 83.8) | 0.0 (0.0 to 0.0) | 65.2 (64.9 to 65.6) | 83.7 (83.3 to 84.1) | 17.3 (16.6 to 17.9) | 25.1 (24.2 to 25.9) | -0.1 (-0.1 to -0.1) | 0.347 (0.344 to 0.349) | 0.474 (0.471 to 0.477) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.0 (99.0 to 99.0) | 100.0 (100.0 to 100.0) | 1.7 (1.6 to 1.8) | 0.5 (0.4 to 0.6) | 0.0 (0.0 to 0.0) | 0.290 (0.288 to 0.292) | 0.339 (0.337 to 0.341) |
| ext | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.334 (0.331 to 0.337) | 0.669 (0.665 to 0.674) |
| ext | release row ($1,200, opt-in) | 83.4 (83.0 to 83.8) | 0.0 (0.0 to 0.0) | 62.2 (61.9 to 62.6) | 83.7 (83.3 to 84.1) | 18.9 (18.2 to 19.5) | 26.9 (26.0 to 27.8) | -0.1 (-0.1 to -0.1) | 0.348 (0.345 to 0.351) | 0.485 (0.482 to 0.488) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.0 to 99.1) | 100.0 (100.0 to 100.0) | 1.7 (1.6 to 1.9) | 0.3 (0.2 to 0.4) | 0.0 (0.0 to 0.0) | 0.287 (0.284 to 0.289) | 0.334 (0.332 to 0.337) |
| bea | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.334 (0.331 to 0.337) | 0.672 (0.667 to 0.676) |
| bea | release row ($1,200, opt-in) | 83.4 (83.0 to 83.8) | 0.0 (0.0 to 0.0) | 61.3 (60.9 to 61.6) | 83.7 (83.3 to 84.1) | 19.4 (18.7 to 20.1) | 27.4 (26.5 to 28.3) | -0.1 (-0.1 to -0.1) | 0.349 (0.346 to 0.351) | 0.489 (0.485 to 0.492) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.1 to 99.1) | 100.0 (100.0 to 100.0) | 1.7 (1.6 to 1.9) | 0.3 (0.2 to 0.4) | 0.0 (0.0 to 0.0) | 0.285 (0.283 to 0.288) | 0.333 (0.330 to 0.335) |

## Adverse, 20 years


### Levels

| Line | Row | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) |
|---|---|---|---|---|---|---|---|
| base | no programme | 21.2 (20.9 to 21.5) | 21.2 (20.9 to 21.5) | 38.5 (38.0 to 39.0) | 29.4 (29.0 to 29.8) | 0 (0 to 0) | 45.8 (45.8 to 45.8) |
| base | release row ($1,200, opt-in) | 10.9 (10.6 to 11.1) | 9.2 (8.9 to 9.4) | 15.8 (15.5 to 16.1) | 39.6 (39.0 to 40.2) | 31,156 (31,020 to 31,294) | 69,019 (66,182 to 71,925) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 0.3 (0.2 to 0.3) | 0.1 (0.1 to 0.1) | 2.5 (2.4 to 2.6) | 6.1 (5.7 to 6.4) | 58,504 (58,364 to 58,648) | 157,411 (151,380 to 163,817) |
| ext | no programme | 22.2 (21.9 to 22.5) | 22.2 (21.9 to 22.5) | 40.4 (39.9 to 40.9) | 30.8 (30.4 to 31.2) | 0 (0 to 0) | 45.8 (45.8 to 45.8) |
| ext | release row ($1,200, opt-in) | 12.4 (12.1 to 12.6) | 10.0 (9.8 to 10.2) | 17.9 (17.5 to 18.2) | 42.2 (41.5 to 42.8) | 31,089 (30,953 to 31,227) | 73,512 (70,458 to 76,652) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 0.1 (0.1 to 0.1) | 0.0 (0.0 to 0.0) | 2.5 (2.4 to 2.6) | 4.6 (4.4 to 4.9) | 61,916 (61,765 to 62,074) | 171,104 (164,526 to 178,096) |
| bea | no programme | 22.5 (22.2 to 22.8) | 22.5 (22.2 to 22.8) | 41.1 (40.6 to 41.6) | 31.3 (30.9 to 31.7) | 0 (0 to 0) | 45.8 (45.8 to 45.8) |
| bea | release row ($1,200, opt-in) | 12.9 (12.6 to 13.1) | 10.3 (10.1 to 10.5) | 18.6 (18.3 to 18.9) | 43.0 (42.4 to 43.6) | 31,069 (30,933 to 31,207) | 75,056 (71,925 to 78,277) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 2.5 (2.4 to 2.6) | 4.2 (3.9 to 4.5) | 63,096 (62,940 to 63,258) | 175,995 (169,240 to 183,201) |

### Levels: this study's own and secondary outcomes

| Line | Row | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| base | no programme | 28.4 (28.0 to 28.8) | 34.0 (33.6 to 34.5) | 43.9 (43.3 to 44.4) | 58.1 (57.1 to 59.0) | 6.96 (6.83 to 7.10) | 6.6 (6.4 to 6.8) |
| base | release row ($1,200, opt-in) | 29.9 (29.4 to 30.3) | 43.0 (42.3 to 43.7) | 18.2 (17.8 to 18.5) | 24.4 (23.7 to 25.1) | 1.29 (1.24 to 1.34) | 7.0 (6.8 to 7.2) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 12.9 (12.5 to 13.2) | 12.3 (11.8 to 12.8) | 3.9 (3.7 to 4.0) | 7.5 (7.2 to 7.9) | 0.07 (0.06 to 0.07) | 2.2 (2.1 to 2.3) |
| ext | no programme | 29.7 (29.3 to 30.1) | 35.6 (35.1 to 36.1) | 45.9 (45.3 to 46.4) | 60.3 (59.4 to 61.3) | 7.49 (7.34 to 7.63) | 6.5 (6.3 to 6.7) |
| ext | release row ($1,200, opt-in) | 32.2 (31.8 to 32.7) | 46.4 (45.7 to 47.1) | 20.6 (20.2 to 21.0) | 27.8 (27.1 to 28.6) | 1.47 (1.42 to 1.52) | 7.2 (6.9 to 7.4) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 12.8 (12.4 to 13.1) | 11.5 (11.0 to 12.0) | 3.9 (3.8 to 4.0) | 7.7 (7.3 to 8.0) | 0.06 (0.06 to 0.07) | 2.0 (1.9 to 2.1) |
| bea | no programme | 30.2 (29.8 to 30.5) | 36.1 (35.7 to 36.6) | 46.6 (46.0 to 47.1) | 61.1 (60.1 to 62.0) | 7.67 (7.53 to 7.82) | 6.5 (6.3 to 6.7) |
| bea | release row ($1,200, opt-in) | 33.1 (32.6 to 33.5) | 47.6 (46.8 to 48.3) | 21.5 (21.1 to 21.9) | 29.1 (28.3 to 29.9) | 1.54 (1.49 to 1.59) | 7.2 (7.0 to 7.4) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 12.7 (12.4 to 13.1) | 11.3 (10.8 to 11.8) | 3.9 (3.8 to 4.1) | 7.7 (7.3 to 8.1) | 0.07 (0.06 to 0.07) | 1.9 (1.8 to 2.0) |

### (a) No programme: the higher line minus the current line (positive = more people below the line)

| Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ext | 1.0 (1.0 to 1.0) | 1.0 (1.0 to 1.0) | 1.9 (1.8 to 2.0) | 1.4 (1.2 to 1.5) | -0.0 (-0.0 to 0.0) ns | 1.3 (1.2 to 1.3) | 1.5 (1.4 to 1.7) | 2.0 (1.9 to 2.1) | 2.3 (2.1 to 2.4) | 0.52 (0.52 to 0.53) | -0.1 (-0.1 to -0.1) |
| bea | 1.3 (1.3 to 1.4) | 1.3 (1.3 to 1.4) | 2.6 (2.5 to 2.6) | 1.9 (1.7 to 2.1) | -0.0 (-0.0 to 0.0) ns | 1.7 (1.7 to 1.8) | 2.1 (1.9 to 2.3) | 2.7 (2.6 to 2.8) | 3.0 (2.9 to 3.1) | 0.71 (0.70 to 0.72) | -0.1 (-0.1 to -0.1) |

### (b) Programme against no programme, at each line (shares: reductions, positive = fewer below)

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | base | 10.3 (10.0 to 10.6) | 12.0 (11.7 to 12.3) | 22.7 (22.3 to 23.1) | -10.2 (-10.7 to -9.8) | 31,156 (31,020 to 31,294) | 68,973 (66,137 to 71,879) | -1.4 (-1.7 to -1.2) | -8.9 (-9.5 to -8.4) | 25.7 (25.3 to 26.2) | 33.7 (32.9 to 34.5) | 5.67 (5.56 to 5.79) | -0.4 (-0.5 to -0.2) |
| release row ($1,200, opt-in) | ext | 9.8 (9.5 to 10.1) | 12.2 (11.9 to 12.5) | 22.5 (22.1 to 22.9) | -11.4 (-11.8 to -11.0) | 31,089 (30,953 to 31,227) | 73,466 (70,412 to 76,606) | -2.5 (-2.8 to -2.2) | -10.8 (-11.3 to -10.3) | 25.3 (24.8 to 25.7) | 32.5 (31.7 to 33.3) | 6.02 (5.90 to 6.14) | -0.6 (-0.7 to -0.5) |
| release row ($1,200, opt-in) | bea | 9.7 (9.4 to 10.0) | 12.2 (12.0 to 12.5) | 22.5 (22.1 to 22.9) | -11.7 (-12.1 to -11.3) | 31,069 (30,933 to 31,207) | 75,010 (71,879 to 78,231) | -2.9 (-3.2 to -2.6) | -11.4 (-12.0 to -10.9) | 25.1 (24.6 to 25.6) | 32.0 (31.2 to 32.8) | 6.14 (6.01 to 6.26) | -0.7 (-0.8 to -0.6) |
| C2.2 design (automatic, all, needs level, needs-indexed) | base | 20.9 (20.6 to 21.2) | 21.1 (20.8 to 21.4) | 36.0 (35.5 to 36.5) | 23.3 (22.9 to 23.7) | 58,504 (58,364 to 58,648) | 157,365 (151,334 to 163,771) | 15.5 (15.2 to 15.9) | 21.8 (21.3 to 22.3) | 40.0 (39.5 to 40.6) | 50.6 (49.6 to 51.5) | 6.90 (6.76 to 7.03) | 4.4 (4.3 to 4.6) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 22.1 (21.8 to 22.4) | 22.2 (21.9 to 22.5) | 37.9 (37.5 to 38.4) | 26.1 (25.7 to 26.5) | 61,916 (61,765 to 62,074) | 171,058 (164,480 to 178,050) | 16.9 (16.6 to 17.3) | 24.1 (23.6 to 24.6) | 42.0 (41.4 to 42.5) | 52.7 (51.8 to 53.6) | 7.42 (7.28 to 7.56) | 4.6 (4.4 to 4.7) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 22.5 (22.2 to 22.8) | 22.5 (22.2 to 22.8) | 38.6 (38.1 to 39.1) | 27.1 (26.7 to 27.5) | 63,096 (62,940 to 63,258) | 175,949 (169,194 to 183,155) | 17.4 (17.1 to 17.8) | 24.8 (24.3 to 25.3) | 42.6 (42.1 to 43.2) | 53.4 (52.5 to 54.3) | 7.61 (7.46 to 7.75) | 4.6 (4.4 to 4.8) |

### (c) Does the effect depend on the line? (row - none) at the higher line minus (row - none) at the current line, rule 1 label

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Cost: effect as % of the base effect | Inflation: as % of the base effect |
|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -0.5 (-0.6 to -0.4), *not changed* | 0.2 (0.1 to 0.2), *not changed* | -0.2 (-0.3 to -0.1), *not changed* | -1.2 (-1.4 to -0.9), *changed* | -66 (-69 to -64) | 4,493 (4,265 to 4,731), *changed* | 99.8 (99.8 to 99.8) | 106.5 (106.4 to 106.6) |
| release row ($1,200, opt-in) | bea | -0.7 (-0.8 to -0.6), *not changed* | 0.2 (0.2 to 0.3), *not changed* | -0.3 (-0.4 to -0.1), *not changed* | -1.5 (-1.8 to -1.2), *changed* | -87 (-91 to -83) | 6,038 (5,730 to 6,360), *changed* | 99.7 (99.7 to 99.7) | 108.8 (108.6 to 108.9) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.2 (1.1 to 1.2), *changed* | 1.1 (1.0 to 1.1), *changed* | 1.9 (1.9 to 2.0), *changed* | 2.8 (2.6 to 3.0), *changed* | 3,412 (3,399 to 3,426) | 13,693 (13,127 to 14,297), *changed* | 105.8 (105.8 to 105.8) | 108.7 (108.6 to 108.8) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.6 (1.5 to 1.6), *changed* | 1.4 (1.4 to 1.5), *changed* | 2.6 (2.5 to 2.6), *changed* | 3.8 (3.5 to 4.0), *changed* | 4,592 (4,574 to 4,610) | 18,584 (17,806 to 19,414), *changed* | 107.8 (107.8 to 107.9) | 111.8 (111.7 to 112.0) |

### (c) for this study's own and secondary outcomes (reductions; rule 1 label)

| Row | Line | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -1.1 (-1.2 to -1.0), *changed* | -1.9 (-2.1 to -1.6), *changed* | -0.5 (-0.6 to -0.3), *not changed* | -1.2 (-1.4 to -1.0), *changed* | 0.34 (0.34 to 0.35), *not changed* | -0.3 (-0.3 to -0.2), *not changed* |
| release row ($1,200, opt-in) | bea | -1.5 (-1.6 to -1.4), *changed* | -2.5 (-2.8 to -2.2), *changed* | -0.6 (-0.8 to -0.5), *not changed* | -1.7 (-1.9 to -1.4), *changed* | 0.46 (0.45 to 0.47), *not changed* | -0.3 (-0.4 to -0.3), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.4 (1.4 to 1.5), *changed* | 2.3 (2.1 to 2.5), *changed* | 2.0 (1.9 to 2.0), *changed* | 2.1 (2.0 to 2.2), *changed* | 0.52 (0.52 to 0.53), *not changed* | 0.1 (0.1 to 0.1), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.9 (1.8 to 2.0), *changed* | 3.0 (2.8 to 3.3), *changed* | 2.6 (2.6 to 2.7), *changed* | 2.8 (2.7 to 3.0), *changed* | 0.71 (0.70 to 0.72), *not changed* | 0.1 (0.1 to 0.2), *not changed* |

### Coverage, participation and distribution (levels)

| Line | Row | Adult-years receiving the BU (%) | Adult-years the BU covers the C2.2 needs (%) | Mean share of the C2.2 needs covered (%) | Participation in the last year (%) | Non-participants below the cost of living (% of their years) | Non-participants with too little wealth (%) | Hours (mean) | Gini, disposable income | Gini, wealth |
|---|---|---|---|---|---|---|---|---|---|---|
| base | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.340 (0.337 to 0.343) | 0.710 (0.705 to 0.715) |
| base | release row ($1,200, opt-in) | 83.4 (83.0 to 83.8) | 0.0 (0.0 to 0.0) | 65.0 (64.7 to 65.4) | 83.7 (83.3 to 84.1) | 25.5 (24.7 to 26.2) | 50.9 (49.8 to 51.9) | -0.1 (-0.1 to -0.1) | 0.364 (0.361 to 0.367) | 0.554 (0.551 to 0.557) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.0 (99.0 to 99.0) | 100.0 (100.0 to 100.0) | 2.4 (2.2 to 2.5) | 5.5 (5.0 to 6.0) | -0.0 (-0.0 to -0.0) | 0.302 (0.300 to 0.304) | 0.359 (0.356 to 0.361) |
| ext | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.340 (0.337 to 0.343) | 0.717 (0.712 to 0.722) |
| ext | release row ($1,200, opt-in) | 83.4 (83.0 to 83.8) | 0.0 (0.0 to 0.0) | 62.1 (61.7 to 62.4) | 83.7 (83.3 to 84.1) | 27.6 (26.7 to 28.4) | 53.2 (52.2 to 54.2) | -0.1 (-0.1 to -0.1) | 0.366 (0.363 to 0.369) | 0.569 (0.566 to 0.573) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.0 to 99.1) | 100.0 (100.0 to 100.0) | 2.3 (2.2 to 2.5) | 4.2 (3.8 to 4.7) | -0.0 (-0.0 to -0.0) | 0.297 (0.295 to 0.300) | 0.351 (0.349 to 0.354) |
| bea | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.340 (0.337 to 0.343) | 0.719 (0.714 to 0.724) |
| bea | release row ($1,200, opt-in) | 83.4 (83.0 to 83.8) | 0.0 (0.0 to 0.0) | 61.1 (60.8 to 61.4) | 83.7 (83.3 to 84.1) | 28.3 (27.5 to 29.1) | 54.0 (53.1 to 55.1) | -0.1 (-0.1 to -0.1) | 0.367 (0.364 to 0.369) | 0.574 (0.571 to 0.578) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.1 to 99.1) | 100.0 (100.0 to 100.0) | 2.3 (2.2 to 2.5) | 3.8 (3.4 to 4.3) | -0.0 (-0.0 to 0.0) | 0.296 (0.294 to 0.298) | 0.349 (0.347 to 0.351) |

## Stress Test, 20 years


### Levels

| Line | Row | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) |
|---|---|---|---|---|---|---|---|
| base | no programme | 21.2 (20.9 to 21.5) | 21.2 (20.9 to 21.5) | 38.5 (38.0 to 39.0) | 29.4 (29.0 to 29.8) | 0 (0 to 0) | 45.8 (45.8 to 45.8) |
| base | release row ($1,200, opt-in) | 20.6 (20.3 to 20.9) | 19.7 (19.4 to 20.0) | 29.9 (29.5 to 30.3) | 40.3 (39.7 to 40.9) | 12,231 (12,079 to 12,383) | 2,709 (2,586 to 2,839) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 0.2 (0.2 to 0.3) | 0.2 (0.2 to 0.2) | 3.4 (3.3 to 3.5) | 18.3 (17.7 to 18.9) | 50,951 (50,838 to 51,063) | 207,392 (198,196 to 217,213) |
| ext | no programme | 22.2 (21.9 to 22.5) | 22.2 (21.9 to 22.5) | 40.4 (39.9 to 40.9) | 30.8 (30.4 to 31.2) | 0 (0 to 0) | 45.8 (45.8 to 45.8) |
| ext | release row ($1,200, opt-in) | 21.8 (21.5 to 22.1) | 20.7 (20.4 to 21.1) | 31.8 (31.3 to 32.2) | 42.0 (41.4 to 42.6) | 12,264 (12,112 to 12,415) | 2,725 (2,600 to 2,856) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 0.1 (0.1 to 0.1) | 0.1 (0.0 to 0.1) | 3.4 (3.3 to 3.5) | 17.3 (16.7 to 17.9) | 53,772 (53,650 to 53,894) | 234,707 (224,154 to 246,000) |
| bea | no programme | 22.5 (22.2 to 22.8) | 22.5 (22.2 to 22.8) | 41.1 (40.6 to 41.6) | 31.3 (30.9 to 31.7) | 0 (0 to 0) | 45.8 (45.8 to 45.8) |
| bea | release row ($1,200, opt-in) | 22.2 (21.9 to 22.5) | 21.1 (20.8 to 21.4) | 32.4 (31.9 to 32.8) | 42.6 (42.0 to 43.1) | 12,275 (12,123 to 12,427) | 2,729 (2,605 to 2,861) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.1) | 3.4 (3.3 to 3.5) | 16.9 (16.3 to 17.5) | 54,747 (54,621 to 54,872) | 244,710 (233,670 to 256,595) |

### Levels: this study's own and secondary outcomes

| Line | Row | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| base | no programme | 28.4 (28.0 to 28.8) | 34.0 (33.6 to 34.5) | 43.9 (43.3 to 44.4) | 58.1 (57.1 to 59.0) | 6.96 (6.83 to 7.10) | 6.6 (6.4 to 6.8) |
| base | release row ($1,200, opt-in) | 31.6 (31.2 to 32.1) | 44.3 (43.7 to 44.8) | 34.1 (33.6 to 34.6) | 45.2 (44.3 to 46.1) | 4.14 (4.04 to 4.23) | 7.0 (6.8 to 7.3) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 17.4 (17.0 to 17.8) | 23.6 (23.0 to 24.3) | 5.1 (4.9 to 5.2) | 9.5 (9.1 to 9.9) | 0.08 (0.08 to 0.09) | 3.1 (2.9 to 3.2) |
| ext | no programme | 29.7 (29.3 to 30.1) | 35.6 (35.1 to 36.1) | 45.9 (45.3 to 46.4) | 60.3 (59.4 to 61.3) | 7.49 (7.34 to 7.63) | 6.5 (6.3 to 6.7) |
| ext | release row ($1,200, opt-in) | 33.2 (32.8 to 33.6) | 46.2 (45.6 to 46.8) | 36.1 (35.6 to 36.6) | 47.7 (46.8 to 48.6) | 4.51 (4.41 to 4.61) | 7.0 (6.7 to 7.2) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 17.7 (17.3 to 18.1) | 23.8 (23.2 to 24.5) | 5.1 (4.9 to 5.3) | 9.8 (9.3 to 10.2) | 0.08 (0.08 to 0.09) | 2.8 (2.7 to 2.9) |
| bea | no programme | 30.2 (29.8 to 30.5) | 36.1 (35.7 to 36.6) | 46.6 (46.0 to 47.1) | 61.1 (60.1 to 62.0) | 7.67 (7.53 to 7.82) | 6.5 (6.3 to 6.7) |
| bea | release row ($1,200, opt-in) | 33.8 (33.3 to 34.2) | 47.0 (46.4 to 47.6) | 36.8 (36.3 to 37.3) | 48.5 (47.6 to 49.4) | 4.64 (4.54 to 4.74) | 6.9 (6.7 to 7.2) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 17.8 (17.4 to 18.2) | 23.9 (23.3 to 24.6) | 5.2 (5.0 to 5.3) | 9.8 (9.4 to 10.2) | 0.09 (0.08 to 0.09) | 2.7 (2.6 to 2.9) |

### (a) No programme: the higher line minus the current line (positive = more people below the line)

| Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ext | 1.0 (1.0 to 1.0) | 1.0 (1.0 to 1.0) | 1.9 (1.8 to 2.0) | 1.4 (1.2 to 1.5) | -0.0 (-0.0 to 0.0) ns | 1.3 (1.2 to 1.3) | 1.5 (1.4 to 1.7) | 2.0 (1.9 to 2.1) | 2.3 (2.1 to 2.4) | 0.52 (0.52 to 0.53) | -0.1 (-0.1 to -0.1) |
| bea | 1.3 (1.3 to 1.4) | 1.3 (1.3 to 1.4) | 2.6 (2.5 to 2.6) | 1.9 (1.7 to 2.1) | -0.0 (-0.0 to 0.0) ns | 1.7 (1.7 to 1.8) | 2.1 (1.9 to 2.3) | 2.7 (2.6 to 2.8) | 3.0 (2.9 to 3.1) | 0.71 (0.70 to 0.72) | -0.1 (-0.1 to -0.1) |

### (b) Programme against no programme, at each line (shares: reductions, positive = fewer below)

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | base | 0.6 (0.3 to 0.8) | 1.5 (1.3 to 1.7) | 8.6 (8.3 to 8.9) | -10.9 (-11.4 to -10.5) | 12,231 (12,079 to 12,383) | 2,663 (2,540 to 2,793) | -3.2 (-3.5 to -2.9) | -10.2 (-10.6 to -9.8) | 9.8 (9.4 to 10.1) | 12.9 (12.2 to 13.5) | 2.82 (2.75 to 2.90) | -0.4 (-0.5 to -0.3) |
| release row ($1,200, opt-in) | ext | 0.4 (0.1 to 0.6) | 1.4 (1.2 to 1.7) | 8.7 (8.4 to 9.0) | -11.2 (-11.7 to -10.8) | 12,264 (12,112 to 12,415) | 2,679 (2,554 to 2,810) | -3.5 (-3.8 to -3.2) | -10.6 (-11.1 to -10.2) | 9.7 (9.4 to 10.1) | 12.6 (12.0 to 13.2) | 2.98 (2.90 to 3.05) | -0.4 (-0.5 to -0.4) |
| release row ($1,200, opt-in) | bea | 0.3 (0.1 to 0.5) | 1.4 (1.2 to 1.7) | 8.7 (8.4 to 9.0) | -11.3 (-11.7 to -10.9) | 12,275 (12,123 to 12,427) | 2,684 (2,559 to 2,815) | -3.6 (-3.9 to -3.3) | -10.9 (-11.3 to -10.4) | 9.8 (9.4 to 10.1) | 12.6 (12.0 to 13.2) | 3.03 (2.95 to 3.11) | -0.4 (-0.5 to -0.4) |
| C2.2 design (automatic, all, needs level, needs-indexed) | base | 20.9 (20.7 to 21.2) | 21.0 (20.7 to 21.3) | 35.1 (34.7 to 35.6) | 11.1 (10.6 to 11.5) | 50,951 (50,838 to 51,063) | 207,346 (198,150 to 217,167) | 11.0 (10.7 to 11.3) | 10.4 (9.9 to 10.9) | 38.8 (38.3 to 39.3) | 48.6 (47.7 to 49.5) | 6.88 (6.74 to 7.01) | 3.5 (3.4 to 3.7) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 22.1 (21.8 to 22.4) | 22.1 (21.8 to 22.4) | 37.0 (36.6 to 37.5) | 13.5 (13.0 to 14.0) | 53,772 (53,650 to 53,894) | 234,662 (224,108 to 245,954) | 12.0 (11.7 to 12.3) | 11.8 (11.3 to 12.3) | 40.7 (40.2 to 41.3) | 50.6 (49.7 to 51.5) | 7.40 (7.26 to 7.54) | 3.7 (3.6 to 3.9) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 22.5 (22.2 to 22.8) | 22.5 (22.2 to 22.8) | 37.7 (37.2 to 38.2) | 14.4 (13.9 to 14.9) | 54,747 (54,621 to 54,872) | 244,664 (233,624 to 256,549) | 12.3 (12.0 to 12.7) | 12.2 (11.7 to 12.7) | 41.4 (40.9 to 41.9) | 51.3 (50.4 to 52.1) | 7.59 (7.45 to 7.73) | 3.8 (3.6 to 3.9) |

### (c) Does the effect depend on the line? (row - none) at the higher line minus (row - none) at the current line, rule 1 label

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Cost: effect as % of the base effect | Inflation: as % of the base effect |
|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -0.2 (-0.3 to -0.2), *not changed* | -0.1 (-0.1 to -0.0), *not changed* | 0.0 (-0.0 to 0.1), *not changed* | -0.3 (-0.5 to -0.1), *not changed* | 33 (32 to 34) | 15.6 (14.5 to 16.8), *changed* | 100.3 (100.3 to 100.3) | 100.6 (100.6 to 100.6) |
| release row ($1,200, opt-in) | bea | -0.3 (-0.3 to -0.2), *not changed* | -0.1 (-0.2 to -0.0), *not changed* | 0.1 (-0.0 to 0.1), *not changed* | -0.4 (-0.6 to -0.1), *not changed* | 44 (43 to 46) | 20.4 (19.0 to 21.9), *changed* | 100.4 (100.3 to 100.4) | 100.8 (100.7 to 100.8) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.2 (1.1 to 1.2), *changed* | 1.1 (1.1 to 1.2), *changed* | 1.9 (1.9 to 2.0), *changed* | 2.4 (2.2 to 2.6), *changed* | 2,821 (2,811 to 2,832) | 27,315 (25,930 to 28,830), *changed* | 105.5 (105.5 to 105.5) | 113.2 (113.0 to 113.3) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.6 (1.5 to 1.6), *changed* | 1.5 (1.5 to 1.6), *changed* | 2.6 (2.5 to 2.6), *changed* | 3.3 (3.1 to 3.5), *changed* | 3,796 (3,781 to 3,810) | 37,318 (35,432 to 39,385), *changed* | 107.4 (107.4 to 107.5) | 118.0 (117.8 to 118.2) |

### (c) for this study's own and secondary outcomes (reductions; rule 1 label)

| Row | Line | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -0.3 (-0.3 to -0.2), *not changed* | -0.4 (-0.6 to -0.2), *not changed* | -0.0 (-0.1 to 0.0), *not changed* | -0.3 (-0.4 to -0.1), *not changed* | 0.15 (0.15 to 0.16), *not changed* | -0.0 (-0.0 to -0.0), *not changed* |
| release row ($1,200, opt-in) | bea | -0.4 (-0.5 to -0.3), *not changed* | -0.7 (-0.9 to -0.4), *not changed* | -0.0 (-0.1 to 0.1), *not changed* | -0.3 (-0.5 to -0.1), *not changed* | 0.20 (0.20 to 0.21), *not changed* | -0.0 (-0.0 to -0.0), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.0 (0.9 to 1.1), *small change* | 1.3 (1.1 to 1.6), *changed* | 1.9 (1.9 to 2.0), *changed* | 2.0 (1.9 to 2.1), *changed* | 0.52 (0.52 to 0.53), *not changed* | 0.2 (0.2 to 0.2), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.3 (1.2 to 1.4), *changed* | 1.8 (1.5 to 2.0), *changed* | 2.6 (2.5 to 2.7), *changed* | 2.7 (2.5 to 2.8), *changed* | 0.71 (0.70 to 0.72), *not changed* | 0.2 (0.2 to 0.3), *not changed* |

### Coverage, participation and distribution (levels)

| Line | Row | Adult-years receiving the BU (%) | Adult-years the BU covers the C2.2 needs (%) | Mean share of the C2.2 needs covered (%) | Participation in the last year (%) | Non-participants below the cost of living (% of their years) | Non-participants with too little wealth (%) | Hours (mean) | Gini, disposable income | Gini, wealth |
|---|---|---|---|---|---|---|---|---|---|---|
| base | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.340 (0.337 to 0.343) | 0.710 (0.705 to 0.715) |
| base | release row ($1,200, opt-in) | 43.4 (42.8 to 44.0) | 0.0 (0.0 to 0.0) | 25.6 (25.2 to 26.0) | 43.6 (43.0 to 44.1) | 35.1 (34.6 to 35.6) | 46.3 (45.6 to 47.1) | -0.0 (-0.0 to -0.0) | 0.353 (0.350 to 0.356) | 0.647 (0.643 to 0.651) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.0 (99.0 to 99.0) | 100.0 (100.0 to 100.0) | 3.3 (3.2 to 3.5) | 18.4 (17.7 to 19.1) | -0.0 (-0.0 to -0.0) | 0.320 (0.318 to 0.322) | 0.394 (0.392 to 0.397) |
| ext | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.340 (0.337 to 0.343) | 0.717 (0.712 to 0.722) |
| ext | release row ($1,200, opt-in) | 43.4 (42.8 to 44.0) | 0.0 (0.0 to 0.0) | 24.4 (24.1 to 24.8) | 43.6 (43.0 to 44.1) | 37.0 (36.5 to 37.6) | 48.1 (47.4 to 48.8) | -0.0 (-0.0 to -0.0) | 0.353 (0.350 to 0.356) | 0.658 (0.654 to 0.661) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.0 to 99.1) | 100.0 (100.0 to 100.0) | 3.3 (3.2 to 3.5) | 17.4 (16.7 to 18.0) | -0.0 (-0.0 to -0.0) | 0.317 (0.314 to 0.319) | 0.389 (0.386 to 0.391) |
| bea | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.340 (0.337 to 0.343) | 0.719 (0.714 to 0.724) |
| bea | release row ($1,200, opt-in) | 43.4 (42.8 to 44.0) | 0.0 (0.0 to 0.0) | 24.1 (23.7 to 24.4) | 43.6 (43.0 to 44.1) | 37.7 (37.1 to 38.2) | 48.6 (47.9 to 49.3) | -0.0 (-0.0 to -0.0) | 0.353 (0.350 to 0.356) | 0.661 (0.658 to 0.665) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.1 to 99.1) | 100.0 (100.0 to 100.0) | 3.4 (3.2 to 3.5) | 17.0 (16.3 to 17.6) | -0.0 (-0.0 to -0.0) | 0.316 (0.313 to 0.318) | 0.387 (0.384 to 0.389) |

## Reference, 40 years


### Levels

| Line | Row | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) |
|---|---|---|---|---|---|---|---|
| base | no programme | 18.1 (17.9 to 18.4) | 18.1 (17.9 to 18.4) | 23.5 (23.1 to 23.8) | 18.8 (18.4 to 19.1) | 0 (0 to 0) | 0.2 (0.1 to 0.2) |
| base | release row ($1,200, opt-in) | 5.9 (5.7 to 6.1) | 5.5 (5.4 to 5.7) | 8.0 (7.8 to 8.2) | 10.9 (10.6 to 11.2) | 33,052 (32,904 to 33,202) | 3,040,252 (2,838,816 to 3,254,424) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 0.1 (0.1 to 0.1) | 0.0 (0.0 to 0.0) | 1.0 (1.0 to 1.1) | 0.0 (0.0 to 0.1) | 64,530 (64,372 to 64,692) | 8,954,309 (8,422,105 to 9,522,873) |
| ext | no programme | 19.2 (18.9 to 19.4) | 19.2 (18.9 to 19.4) | 25.0 (24.7 to 25.3) | 19.9 (19.5 to 20.2) | 0 (0 to 0) | 0.2 (0.2 to 0.2) |
| ext | release row ($1,200, opt-in) | 6.8 (6.6 to 7.0) | 6.2 (6.1 to 6.4) | 9.2 (9.0 to 9.4) | 12.3 (12.0 to 12.7) | 32,912 (32,764 to 33,061) | 3,460,473 (3,227,075 to 3,708,046) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 1.1 (1.0 to 1.1) | 0.0 (0.0 to 0.1) | 68,401 (68,229 to 68,577) | 10,515,602 (9,885,600 to 11,189,585) |
| bea | no programme | 19.5 (19.2 to 19.8) | 19.5 (19.2 to 19.8) | 25.5 (25.2 to 25.8) | 20.3 (19.9 to 20.6) | 0 (0 to 0) | 0.2 (0.2 to 0.3) |
| bea | release row ($1,200, opt-in) | 7.2 (7.0 to 7.4) | 6.4 (6.3 to 6.6) | 9.7 (9.5 to 9.9) | 12.9 (12.5 to 13.2) | 32,866 (32,720 to 33,015) | 3,614,640 (3,369,880 to 3,874,442) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 1.1 (1.0 to 1.1) | 0.0 (0.0 to 0.0) | 69,740 (69,563 to 69,922) | 11,103,303 (10,436,395 to 11,817,256) |

### Levels: this study's own and secondary outcomes

| Line | Row | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| base | no programme | 23.7 (23.3 to 24.1) | 22.7 (22.3 to 23.1) | 27.7 (27.3 to 28.1) | 39.0 (38.2 to 39.8) | 3.66 (3.59 to 3.74) | 3.0 (2.9 to 3.2) |
| base | release row ($1,200, opt-in) | 18.5 (18.1 to 18.8) | 13.9 (13.5 to 14.3) | 9.6 (9.4 to 9.8) | 13.8 (13.3 to 14.2) | 0.59 (0.56 to 0.62) | 3.1 (3.0 to 3.3) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 5.1 (4.9 to 5.3) | 1.3 (1.1 to 1.4) | 1.7 (1.7 to 1.8) | 3.6 (3.4 to 3.9) | 0.03 (0.03 to 0.03) | 0.9 (0.8 to 0.9) |
| ext | no programme | 25.0 (24.6 to 25.4) | 24.0 (23.6 to 24.5) | 29.4 (29.0 to 29.8) | 41.2 (40.4 to 42.0) | 3.98 (3.90 to 4.06) | 3.0 (2.8 to 3.1) |
| ext | release row ($1,200, opt-in) | 20.5 (20.1 to 20.8) | 15.8 (15.4 to 16.3) | 11.0 (10.8 to 11.3) | 15.8 (15.3 to 16.4) | 0.68 (0.65 to 0.71) | 3.2 (3.1 to 3.4) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 5.1 (4.9 to 5.3) | 1.2 (1.1 to 1.4) | 1.8 (1.7 to 1.9) | 3.7 (3.5 to 4.0) | 0.03 (0.03 to 0.03) | 0.8 (0.7 to 0.9) |
| bea | no programme | 25.5 (25.1 to 25.8) | 24.5 (24.1 to 25.0) | 30.0 (29.6 to 30.4) | 42.0 (41.2 to 42.8) | 4.10 (4.01 to 4.18) | 2.9 (2.8 to 3.1) |
| bea | release row ($1,200, opt-in) | 21.2 (20.8 to 21.5) | 16.5 (16.1 to 17.0) | 11.6 (11.3 to 11.9) | 16.6 (16.1 to 17.2) | 0.71 (0.68 to 0.75) | 3.2 (3.1 to 3.4) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 5.1 (4.9 to 5.3) | 1.2 (1.0 to 1.4) | 1.8 (1.7 to 1.9) | 3.7 (3.5 to 4.0) | 0.03 (0.03 to 0.03) | 0.8 (0.7 to 0.8) |

### (a) No programme: the higher line minus the current line (positive = more people below the line)

| Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ext | 1.0 (1.0 to 1.1) | 1.0 (1.0 to 1.1) | 1.5 (1.5 to 1.6) | 1.1 (1.0 to 1.2) | 0.1 (0.1 to 0.1) | 1.3 (1.2 to 1.4) | 1.3 (1.2 to 1.5) | 1.7 (1.7 to 1.8) | 2.2 (2.1 to 2.3) | 0.32 (0.31 to 0.32) | -0.1 (-0.1 to -0.0) |
| bea | 1.4 (1.3 to 1.4) | 1.4 (1.3 to 1.4) | 2.0 (2.0 to 2.1) | 1.5 (1.4 to 1.6) | 0.1 (0.1 to 0.1) | 1.7 (1.7 to 1.8) | 1.9 (1.7 to 2.0) | 2.3 (2.2 to 2.4) | 3.0 (2.9 to 3.2) | 0.43 (0.43 to 0.44) | -0.1 (-0.1 to -0.1) |

### (b) Programme against no programme, at each line (shares: reductions, positive = fewer below)

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | base | 12.2 (12.0 to 12.5) | 12.6 (12.4 to 12.9) | 15.4 (15.2 to 15.7) | 7.9 (7.6 to 8.2) | 33,052 (32,904 to 33,202) | 3,040,252 (2,838,816 to 3,254,424) | 5.2 (4.9 to 5.6) | 8.8 (8.4 to 9.2) | 18.1 (17.8 to 18.5) | 25.2 (24.6 to 25.9) | 3.07 (3.01 to 3.14) | -0.1 (-0.2 to -0.0) |
| release row ($1,200, opt-in) | ext | 12.3 (12.1 to 12.6) | 12.9 (12.7 to 13.2) | 15.8 (15.5 to 16.0) | 7.5 (7.2 to 7.9) | 32,912 (32,764 to 33,061) | 3,460,473 (3,227,075 to 3,708,046) | 4.5 (4.2 to 4.8) | 8.2 (7.8 to 8.6) | 18.4 (18.0 to 18.7) | 25.4 (24.7 to 26.0) | 3.30 (3.23 to 3.37) | -0.3 (-0.3 to -0.2) |
| release row ($1,200, opt-in) | bea | 12.3 (12.1 to 12.6) | 13.0 (12.8 to 13.3) | 15.8 (15.5 to 16.1) | 7.4 (7.0 to 7.7) | 32,866 (32,720 to 33,015) | 3,614,640 (3,369,880 to 3,874,441) | 4.3 (4.0 to 4.6) | 8.0 (7.6 to 8.4) | 18.4 (18.1 to 18.8) | 25.4 (24.7 to 26.0) | 3.38 (3.31 to 3.45) | -0.3 (-0.4 to -0.2) |
| C2.2 design (automatic, all, needs level, needs-indexed) | base | 18.0 (17.8 to 18.3) | 18.1 (17.8 to 18.4) | 22.4 (22.1 to 22.7) | 18.7 (18.4 to 19.0) | 64,530 (64,372 to 64,692) | 8,954,308 (8,422,105 to 9,522,873) | 18.6 (18.2 to 18.9) | 21.4 (21.0 to 21.8) | 26.0 (25.6 to 26.4) | 35.4 (34.6 to 36.2) | 3.63 (3.56 to 3.71) | 2.1 (2.0 to 2.3) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 19.1 (18.8 to 19.4) | 19.1 (18.9 to 19.4) | 23.9 (23.6 to 24.2) | 19.8 (19.5 to 20.2) | 68,401 (68,229 to 68,577) | 10,515,601 (9,885,600 to 11,189,585) | 19.9 (19.6 to 20.2) | 22.8 (22.4 to 23.2) | 27.7 (27.3 to 28.0) | 37.5 (36.7 to 38.3) | 3.95 (3.87 to 4.03) | 2.2 (2.0 to 2.3) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 19.5 (19.2 to 19.8) | 19.5 (19.2 to 19.8) | 24.4 (24.1 to 24.8) | 20.2 (19.9 to 20.6) | 69,740 (69,563 to 69,922) | 11,103,303 (10,436,395 to 11,817,256) | 20.4 (20.1 to 20.7) | 23.3 (22.9 to 23.8) | 28.2 (27.8 to 28.6) | 38.3 (37.5 to 39.1) | 4.07 (3.99 to 4.15) | 2.2 (2.0 to 2.3) |

### (c) Does the effect depend on the line? (row - none) at the higher line minus (row - none) at the current line, rule 1 label

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Cost: effect as % of the base effect | Inflation: as % of the base effect |
|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | 0.1 (0.0 to 0.2), *not changed* | 0.3 (0.3 to 0.4), *not changed* | 0.3 (0.2 to 0.4), *not changed* | -0.3 (-0.5 to -0.1), *not changed* | -140 (-144 to -137) | 420,221 (388,800 to 454,304), *changed* | 99.6 (99.6 to 99.6) | 113.8 (113.6 to 114.0) |
| release row ($1,200, opt-in) | bea | 0.1 (0.0 to 0.2), *not changed* | 0.4 (0.4 to 0.5), *not changed* | 0.4 (0.3 to 0.5), *not changed* | -0.5 (-0.7 to -0.3), *not changed* | -186 (-191 to -181) | 574,388 (531,158 to 621,267), *changed* | 99.4 (99.4 to 99.5) | 118.9 (118.6 to 119.2) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.1 (1.0 to 1.2), *changed* | 1.0 (1.0 to 1.1), *changed* | 1.5 (1.5 to 1.5), *changed* | 1.1 (1.0 to 1.2), *changed* | 3,870 (3,855 to 3,886) | 1,561,293 (1,463,296 to 1,665,901), *changed* | 106.0 (106.0 to 106.0) | 117.4 (117.3 to 117.6) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.5 (1.4 to 1.5), *changed* | 1.4 (1.3 to 1.5), *changed* | 2.0 (2.0 to 2.1), *changed* | 1.5 (1.4 to 1.7), *changed* | 5,209 (5,189 to 5,230) | 2,148,994 (2,014,711 to 2,292,815), *changed* | 108.1 (108.1 to 108.1) | 124.0 (123.7 to 124.3) |

### (c) for this study's own and secondary outcomes (reductions; rule 1 label)

| Row | Line | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -0.7 (-0.8 to -0.6), *not changed* | -0.6 (-0.9 to -0.4), *not changed* | 0.3 (0.2 to 0.4), *not changed* | 0.2 (-0.0 to 0.3), *not changed* | 0.23 (0.23 to 0.23), *not changed* | -0.2 (-0.2 to -0.1), *not changed* |
| release row ($1,200, opt-in) | bea | -0.9 (-1.1 to -0.8), *small change* | -0.8 (-1.1 to -0.5), *small change* | 0.3 (0.2 to 0.4), *not changed* | 0.1 (-0.1 to 0.4), *not changed* | 0.31 (0.30 to 0.32), *not changed* | -0.2 (-0.2 to -0.2), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.3 (1.3 to 1.4), *changed* | 1.4 (1.2 to 1.6), *changed* | 1.7 (1.6 to 1.7), *changed* | 2.1 (2.0 to 2.2), *changed* | 0.32 (0.31 to 0.32), *not changed* | 0.0 (0.0 to 0.0), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.8 (1.7 to 1.9), *changed* | 1.9 (1.7 to 2.1), *changed* | 2.3 (2.2 to 2.3), *changed* | 2.9 (2.7 to 3.0), *changed* | 0.43 (0.43 to 0.44), *not changed* | 0.0 (0.0 to 0.0), *not changed* |

### Coverage, participation and distribution (levels)

| Line | Row | Adult-years receiving the BU (%) | Adult-years the BU covers the C2.2 needs (%) | Mean share of the C2.2 needs covered (%) | Participation in the last year (%) | Non-participants below the cost of living (% of their years) | Non-participants with too little wealth (%) | Hours (mean) | Gini, disposable income | Gini, wealth |
|---|---|---|---|---|---|---|---|---|---|---|
| base | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.332 (0.329 to 0.335) | 0.602 (0.597 to 0.606) |
| base | release row ($1,200, opt-in) | 83.6 (83.1 to 84.0) | 0.0 (0.0 to 0.0) | 65.6 (65.2 to 65.9) | 83.7 (83.3 to 84.1) | 14.4 (13.9 to 15.0) | 17.8 (17.1 to 18.4) | -0.0 (-0.0 to -0.0) | 0.349 (0.346 to 0.351) | 0.448 (0.445 to 0.451) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.0 (99.0 to 99.0) | 100.0 (100.0 to 100.0) | 1.0 (0.9 to 1.1) | 0.0 (0.0 to 0.1) | 0.0 (0.0 to 0.0) | 0.289 (0.286 to 0.291) | 0.327 (0.324 to 0.329) |
| ext | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.333 (0.330 to 0.335) | 0.609 (0.605 to 0.614) |
| ext | release row ($1,200, opt-in) | 83.6 (83.1 to 84.0) | 0.0 (0.0 to 0.0) | 62.6 (62.2 to 62.9) | 83.7 (83.3 to 84.1) | 15.8 (15.2 to 16.4) | 19.3 (18.6 to 20.0) | -0.1 (-0.1 to -0.0) | 0.351 (0.348 to 0.353) | 0.458 (0.455 to 0.461) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.0 to 99.1) | 100.0 (100.0 to 100.0) | 1.0 (0.9 to 1.1) | 0.0 (0.0 to 0.1) | 0.0 (0.0 to 0.0) | 0.285 (0.283 to 0.287) | 0.323 (0.320 to 0.325) |
| bea | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.333 (0.330 to 0.336) | 0.612 (0.608 to 0.616) |
| bea | release row ($1,200, opt-in) | 83.6 (83.1 to 84.0) | 0.0 (0.0 to 0.0) | 61.6 (61.3 to 61.9) | 83.7 (83.3 to 84.1) | 16.3 (15.7 to 16.9) | 19.9 (19.2 to 20.6) | -0.1 (-0.1 to -0.1) | 0.351 (0.348 to 0.354) | 0.462 (0.459 to 0.465) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.1 to 99.1) | 100.0 (100.0 to 100.0) | 1.0 (0.9 to 1.1) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.284 (0.282 to 0.286) | 0.322 (0.319 to 0.324) |

## Adverse, 40 years


### Levels

| Line | Row | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) |
|---|---|---|---|---|---|---|---|
| base | no programme | 26.8 (26.5 to 27.1) | 26.8 (26.5 to 27.1) | 45.1 (44.6 to 45.6) | 39.1 (38.6 to 39.5) | 0 (0 to 0) | 116.5 (116.5 to 116.5) |
| base | release row ($1,200, opt-in) | 16.7 (16.3 to 17.0) | 13.6 (13.3 to 13.8) | 20.9 (20.5 to 21.2) | 65.2 (64.5 to 65.8) | 30,512 (30,378 to 30,646) | 475,532,481 (426,820,921 to 528,585,646) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 0.1 (0.1 to 0.1) | 0.1 (0.0 to 0.1) | 2.4 (2.3 to 2.5) | 20.5 (19.6 to 21.4) | 59,010 (58,853 to 59,171) | 1,182,054,278 (1,070,657,671 to 1,303,474,008) |
| ext | no programme | 28.1 (27.8 to 28.4) | 28.1 (27.8 to 28.4) | 47.1 (46.6 to 47.6) | 40.7 (40.3 to 41.2) | 0 (0 to 0) | 116.5 (116.5 to 116.5) |
| ext | release row ($1,200, opt-in) | 19.1 (18.7 to 19.4) | 14.7 (14.4 to 15.0) | 23.6 (23.2 to 24.0) | 67.3 (66.7 to 68.0) | 30,408 (30,275 to 30,541) | 567,460,390 (508,343,955 to 631,646,911) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 2.3 (2.3 to 2.4) | 16.7 (15.8 to 17.5) | 62,556 (62,387 to 62,732) | 1,329,990,477 (1,205,229,653 to 1,466,155,939) |
| bea | no programme | 28.6 (28.2 to 28.9) | 28.6 (28.2 to 28.9) | 47.8 (47.3 to 48.3) | 41.4 (40.9 to 41.8) | 0 (0 to 0) | 116.5 (116.5 to 116.5) |
| bea | release row ($1,200, opt-in) | 19.8 (19.5 to 20.2) | 15.1 (14.8 to 15.3) | 24.5 (24.1 to 24.9) | 68.0 (67.4 to 68.7) | 30,379 (30,247 to 30,512) | 599,192,196 (536,558,583 to 667,109,271) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 2.3 (2.3 to 2.4) | 15.4 (14.6 to 16.2) | 63,783 (63,608 to 63,965) | 1,383,833,243 (1,254,079,242 to 1,524,961,304) |

### Levels: this study's own and secondary outcomes

| Line | Row | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| base | no programme | 33.9 (33.5 to 34.3) | 44.3 (43.8 to 44.8) | 50.6 (50.1 to 51.1) | 65.1 (64.3 to 65.9) | 9.15 (9.00 to 9.30) | 10.1 (9.8 to 10.4) |
| base | release row ($1,200, opt-in) | 42.8 (42.3 to 43.4) | 66.3 (65.6 to 67.0) | 23.4 (23.0 to 23.9) | 30.3 (29.5 to 31.1) | 1.74 (1.68 to 1.79) | 11.1 (10.8 to 11.4) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 15.9 (15.4 to 16.4) | 26.7 (25.8 to 27.6) | 3.9 (3.8 to 4.1) | 8.0 (7.6 to 8.4) | 0.05 (0.05 to 0.05) | 2.2 (2.1 to 2.4) |
| ext | no programme | 35.5 (35.0 to 35.9) | 46.1 (45.6 to 46.6) | 52.6 (52.1 to 53.1) | 67.2 (66.4 to 68.0) | 9.78 (9.63 to 9.94) | 10.0 (9.7 to 10.3) |
| ext | release row ($1,200, opt-in) | 45.7 (45.1 to 46.2) | 69.3 (68.7 to 70.0) | 26.6 (26.2 to 27.1) | 34.8 (33.9 to 35.6) | 1.98 (1.92 to 2.04) | 11.4 (11.1 to 11.7) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 15.3 (14.8 to 15.8) | 25.1 (24.2 to 26.0) | 3.9 (3.8 to 4.1) | 8.0 (7.6 to 8.4) | 0.05 (0.05 to 0.05) | 1.9 (1.8 to 2.1) |
| bea | no programme | 36.0 (35.6 to 36.4) | 46.8 (46.3 to 47.3) | 53.3 (52.7 to 53.8) | 67.9 (67.1 to 68.7) | 10.01 (9.85 to 10.17) | 9.9 (9.7 to 10.2) |
| bea | release row ($1,200, opt-in) | 46.6 (46.1 to 47.1) | 70.3 (69.6 to 70.9) | 27.7 (27.3 to 28.2) | 36.3 (35.5 to 37.1) | 2.07 (2.01 to 2.13) | 11.5 (11.2 to 11.8) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 15.1 (14.6 to 15.6) | 24.4 (23.5 to 25.3) | 3.9 (3.8 to 4.1) | 8.1 (7.7 to 8.5) | 0.05 (0.05 to 0.05) | 1.9 (1.7 to 2.0) |

### (a) No programme: the higher line minus the current line (positive = more people below the line)

| Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ext | 1.3 (1.3 to 1.4) | 1.3 (1.3 to 1.4) | 2.0 (1.9 to 2.0) | 1.7 (1.5 to 1.8) | 0.0 (0.0 to 0.0) ns | 1.5 (1.5 to 1.6) | 1.8 (1.6 to 2.0) | 2.0 (1.9 to 2.0) | 2.1 (2.0 to 2.2) | 0.64 (0.63 to 0.65) | -0.1 (-0.1 to -0.1) |
| bea | 1.8 (1.7 to 1.8) | 1.8 (1.7 to 1.8) | 2.6 (2.6 to 2.7) | 2.3 (2.2 to 2.5) | 0.0 (0.0 to 0.0) | 2.0 (2.0 to 2.1) | 2.5 (2.3 to 2.7) | 2.7 (2.6 to 2.7) | 2.8 (2.7 to 2.9) | 0.86 (0.86 to 0.87) | -0.2 (-0.2 to -0.1) |

### (b) Programme against no programme, at each line (shares: reductions, positive = fewer below)

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | base | 10.1 (9.8 to 10.4) | 13.2 (12.9 to 13.5) | 24.3 (23.9 to 24.6) | -26.1 (-26.6 to -25.6) | 30,512 (30,378 to 30,646) | 475,532,364 (426,820,804 to 528,585,529) | -8.9 (-9.2 to -8.6) | -22.0 (-22.5 to -21.4) | 27.2 (26.8 to 27.6) | 34.8 (34.1 to 35.5) | 7.41 (7.28 to 7.54) | -1.0 (-1.1 to -0.8) |
| release row ($1,200, opt-in) | ext | 9.0 (8.8 to 9.3) | 13.4 (13.1 to 13.7) | 23.5 (23.2 to 23.9) | -26.6 (-27.1 to -26.1) | 30,408 (30,275 to 30,541) | 567,460,274 (508,343,838 to 631,646,794) | -10.2 (-10.6 to -9.9) | -23.2 (-23.7 to -22.7) | 26.0 (25.6 to 26.3) | 32.4 (31.8 to 33.1) | 7.81 (7.68 to 7.94) | -1.4 (-1.6 to -1.3) |
| release row ($1,200, opt-in) | bea | 8.7 (8.4 to 9.0) | 13.5 (13.2 to 13.8) | 23.3 (22.9 to 23.6) | -26.6 (-27.2 to -26.1) | 30,379 (30,247 to 30,512) | 599,192,079 (536,558,466 to 667,109,155) | -10.6 (-11.0 to -10.3) | -23.5 (-24.0 to -23.0) | 25.5 (25.2 to 25.9) | 31.6 (31.0 to 32.2) | 7.94 (7.81 to 8.08) | -1.6 (-1.7 to -1.4) |
| C2.2 design (automatic, all, needs level, needs-indexed) | base | 26.7 (26.3 to 27.0) | 26.7 (26.4 to 27.1) | 42.7 (42.2 to 43.2) | 18.5 (17.8 to 19.2) | 59,010 (58,853 to 59,171) | 1,182,054,161 (1,070,657,555 to 1,303,473,891) | 18.0 (17.7 to 18.4) | 17.6 (16.9 to 18.2) | 46.7 (46.2 to 47.2) | 57.1 (56.3 to 58.0) | 9.10 (8.95 to 9.25) | 7.9 (7.6 to 8.1) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 28.1 (27.7 to 28.4) | 28.1 (27.8 to 28.4) | 44.7 (44.3 to 45.2) | 24.1 (23.4 to 24.7) | 62,556 (62,387 to 62,732) | 1,329,990,361 (1,205,229,537 to 1,466,155,823) | 20.2 (19.8 to 20.5) | 21.0 (20.3 to 21.7) | 48.7 (48.2 to 49.2) | 59.2 (58.3 to 60.0) | 9.74 (9.58 to 9.89) | 8.1 (7.8 to 8.3) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 28.5 (28.2 to 28.9) | 28.6 (28.2 to 28.9) | 45.4 (44.9 to 45.9) | 26.0 (25.3 to 26.6) | 63,783 (63,608 to 63,965) | 1,383,833,127 (1,254,079,126 to 1,524,961,188) | 20.9 (20.5 to 21.2) | 22.4 (21.7 to 23.1) | 49.4 (48.9 to 49.9) | 59.8 (59.0 to 60.6) | 9.96 (9.81 to 10.12) | 8.1 (7.9 to 8.3) |

### (c) Does the effect depend on the line? (row - none) at the higher line minus (row - none) at the current line, rule 1 label

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Cost: effect as % of the base effect | Inflation: as % of the base effect |
|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -1.1 (-1.2 to -1.0), *changed* | 0.2 (0.1 to 0.2), *not changed* | -0.8 (-0.8 to -0.7), *not changed* | -0.5 (-0.7 to -0.2), *not changed* | -104 (-108 to -100) | 91,927,909 (81,511,696 to 103,279,744), *changed* | 99.7 (99.6 to 99.7) | 119.3 (119.0 to 119.7) |
| release row ($1,200, opt-in) | bea | -1.4 (-1.5 to -1.3), *changed* | 0.3 (0.2 to 0.3), *not changed* | -1.0 (-1.1 to -0.9), *changed* | -0.5 (-0.8 to -0.3), *not changed* | -133 (-138 to -128) | 123,659,715 (109,643,169 to 138,916,096), *changed* | 99.6 (99.5 to 99.6) | 126.0 (125.5 to 126.5) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.4 (1.4 to 1.4), *changed* | 1.4 (1.3 to 1.4), *changed* | 2.0 (2.0 to 2.1), *changed* | 5.5 (5.3 to 5.8), *changed* | 3,546 (3,532 to 3,561) | 147,936,199 (134,184,423 to 162,937,565), *changed* | 106.0 (106.0 to 106.0) | 112.5 (112.2 to 112.9) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.9 (1.8 to 1.9), *changed* | 1.8 (1.8 to 1.9), *changed* | 2.7 (2.7 to 2.8), *changed* | 7.5 (7.2 to 7.7), *changed* | 4,773 (4,753 to 4,793) | 201,778,965 (182,878,109 to 222,251,136), *changed* | 108.1 (108.1 to 108.1) | 117.1 (116.6 to 117.5) |

### (c) for this study's own and secondary outcomes (reductions; rule 1 label)

| Row | Line | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -1.3 (-1.4 to -1.3), *changed* | -1.2 (-1.5 to -0.9), *changed* | -1.2 (-1.3 to -1.1), *changed* | -2.4 (-2.6 to -2.2), *changed* | 0.40 (0.39 to 0.40), *not changed* | -0.5 (-0.5 to -0.4), *not changed* |
| release row ($1,200, opt-in) | bea | -1.7 (-1.8 to -1.7), *changed* | -1.5 (-1.8 to -1.2), *changed* | -1.6 (-1.7 to -1.5), *changed* | -3.2 (-3.5 to -3.0), *changed* | 0.53 (0.53 to 0.54), *not changed* | -0.6 (-0.6 to -0.6), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 2.1 (2.1 to 2.2), *changed* | 3.4 (3.2 to 3.7), *changed* | 2.0 (2.0 to 2.1), *changed* | 2.0 (1.9 to 2.1), *changed* | 0.64 (0.63 to 0.65), *not changed* | 0.2 (0.2 to 0.2), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 2.9 (2.8 to 3.0), *changed* | 4.8 (4.6 to 5.1), *changed* | 2.7 (2.6 to 2.8), *changed* | 2.7 (2.6 to 2.8), *changed* | 0.87 (0.86 to 0.88), *not changed* | 0.2 (0.2 to 0.3), *not changed* |

### Coverage, participation and distribution (levels)

| Line | Row | Adult-years receiving the BU (%) | Adult-years the BU covers the C2.2 needs (%) | Mean share of the C2.2 needs covered (%) | Participation in the last year (%) | Non-participants below the cost of living (% of their years) | Non-participants with too little wealth (%) | Hours (mean) | Gini, disposable income | Gini, wealth |
|---|---|---|---|---|---|---|---|---|---|---|
| base | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.337 (0.334 to 0.340) | 0.724 (0.720 to 0.729) |
| base | release row ($1,200, opt-in) | 83.6 (83.1 to 84.0) | 0.0 (0.0 to 0.0) | 65.3 (64.9 to 65.6) | 83.7 (83.3 to 84.1) | 32.0 (31.1 to 32.8) | 74.0 (73.1 to 74.9) | -0.1 (-0.1 to -0.1) | 0.377 (0.375 to 0.380) | 0.647 (0.644 to 0.651) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.0 (99.0 to 99.0) | 100.0 (100.0 to 100.0) | 2.2 (2.0 to 2.4) | 19.9 (18.9 to 21.0) | -0.0 (-0.0 to -0.0) | 0.307 (0.304 to 0.309) | 0.365 (0.363 to 0.368) |
| ext | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.338 (0.335 to 0.340) | 0.733 (0.729 to 0.738) |
| ext | release row ($1,200, opt-in) | 83.6 (83.1 to 84.0) | 0.0 (0.0 to 0.0) | 62.3 (62.0 to 62.7) | 83.7 (83.3 to 84.1) | 34.6 (33.7 to 35.4) | 75.7 (74.9 to 76.6) | -0.1 (-0.1 to -0.1) | 0.380 (0.377 to 0.382) | 0.666 (0.663 to 0.670) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.0 to 99.1) | 100.0 (100.0 to 100.0) | 2.2 (2.0 to 2.3) | 16.2 (15.3 to 17.1) | -0.0 (-0.0 to -0.0) | 0.301 (0.299 to 0.304) | 0.354 (0.352 to 0.357) |
| bea | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.338 (0.335 to 0.340) | 0.736 (0.732 to 0.741) |
| bea | release row ($1,200, opt-in) | 83.6 (83.1 to 84.0) | 0.0 (0.0 to 0.0) | 61.4 (61.1 to 61.7) | 83.7 (83.3 to 84.1) | 35.5 (34.6 to 36.3) | 76.3 (75.4 to 77.1) | -0.1 (-0.1 to -0.1) | 0.380 (0.378 to 0.383) | 0.673 (0.669 to 0.676) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.1 to 99.1) | 100.0 (100.0 to 100.0) | 2.1 (2.0 to 2.3) | 15.2 (14.3 to 16.1) | -0.0 (-0.0 to -0.0) | 0.300 (0.298 to 0.302) | 0.351 (0.348 to 0.353) |

## Stress Test, 40 years


### Levels

| Line | Row | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) |
|---|---|---|---|---|---|---|---|
| base | no programme | 26.8 (26.5 to 27.1) | 26.8 (26.5 to 27.1) | 45.1 (44.6 to 45.6) | 39.1 (38.6 to 39.5) | 0 (0 to 0) | 116.5 (116.5 to 116.5) |
| base | release row ($1,200, opt-in) | 31.2 (30.8 to 31.6) | 29.7 (29.3 to 30.0) | 37.5 (37.1 to 37.9) | 64.0 (63.4 to 64.7) | 12,319 (12,171 to 12,467) | 251,525 (225,177 to 279,806) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 0.1 (0.1 to 0.1) | 0.3 (0.3 to 0.3) | 4.6 (4.4 to 4.7) | 48.1 (47.1 to 49.1) | 50,535 (50,416 to 50,653) | 5,123,649,243 (4,537,031,701 to 5,787,646,314) |
| ext | no programme | 28.1 (27.8 to 28.4) | 28.1 (27.8 to 28.4) | 47.1 (46.6 to 47.6) | 40.7 (40.3 to 41.2) | 0 (0 to 0) | 116.5 (116.5 to 116.5) |
| ext | release row ($1,200, opt-in) | 32.8 (32.4 to 33.1) | 31.1 (30.7 to 31.4) | 39.5 (39.1 to 39.9) | 65.6 (65.0 to 66.3) | 12,354 (12,206 to 12,502) | 253,769 (227,090 to 282,383) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.1 (0.1 to 0.1) | 4.5 (4.4 to 4.7) | 46.4 (45.5 to 47.4) | 53,362 (53,233 to 53,490) | 6,483,690,668 (5,732,639,240 to 7,329,128,531) |
| bea | no programme | 28.6 (28.2 to 28.9) | 28.6 (28.2 to 28.9) | 47.8 (47.3 to 48.3) | 41.4 (40.9 to 41.8) | 0 (0 to 0) | 116.5 (116.5 to 116.5) |
| bea | release row ($1,200, opt-in) | 33.3 (32.9 to 33.6) | 31.5 (31.1 to 31.9) | 40.2 (39.7 to 40.6) | 66.1 (65.5 to 66.8) | 12,366 (12,217 to 12,513) | 254,456 (227,679 to 283,179) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 0.0 (0.0 to 0.0) | 0.1 (0.1 to 0.1) | 4.5 (4.4 to 4.6) | 45.6 (44.7 to 46.6) | 54,338 (54,205 to 54,470) | 7,016,496,623 (6,203,319,664 to 7,932,358,114) |

### Levels: this study's own and secondary outcomes

| Line | Row | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| base | no programme | 33.9 (33.5 to 34.3) | 44.3 (43.8 to 44.8) | 50.6 (50.1 to 51.1) | 65.1 (64.3 to 65.9) | 9.15 (9.00 to 9.30) | 10.1 (9.8 to 10.4) |
| base | release row ($1,200, opt-in) | 44.2 (43.8 to 44.7) | 66.9 (66.2 to 67.5) | 41.9 (41.4 to 42.4) | 53.6 (52.8 to 54.5) | 5.63 (5.52 to 5.74) | 10.7 (10.4 to 11.0) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 27.4 (26.8 to 28.0) | 50.7 (49.7 to 51.6) | 6.4 (6.2 to 6.7) | 11.4 (11.0 to 11.9) | 0.10 (0.09 to 0.10) | 4.9 (4.7 to 5.1) |
| ext | no programme | 35.5 (35.0 to 35.9) | 46.1 (45.6 to 46.6) | 52.6 (52.1 to 53.1) | 67.2 (66.4 to 68.0) | 9.78 (9.63 to 9.94) | 10.0 (9.7 to 10.3) |
| ext | release row ($1,200, opt-in) | 46.1 (45.6 to 46.5) | 68.7 (68.0 to 69.5) | 44.1 (43.6 to 44.5) | 56.2 (55.3 to 57.0) | 6.10 (5.98 to 6.21) | 10.6 (10.3 to 10.9) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 27.7 (27.1 to 28.2) | 50.7 (49.7 to 51.7) | 6.5 (6.3 to 6.7) | 11.7 (11.2 to 12.1) | 0.10 (0.09 to 0.10) | 4.4 (4.2 to 4.5) |
| bea | no programme | 36.0 (35.6 to 36.4) | 46.8 (46.3 to 47.3) | 53.3 (52.7 to 53.8) | 67.9 (67.1 to 68.7) | 10.01 (9.85 to 10.17) | 9.9 (9.7 to 10.2) |
| bea | release row ($1,200, opt-in) | 46.7 (46.2 to 47.2) | 69.4 (68.7 to 70.1) | 44.8 (44.3 to 45.3) | 57.0 (56.1 to 57.8) | 6.26 (6.15 to 6.37) | 10.5 (10.3 to 10.8) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 27.7 (27.2 to 28.3) | 50.6 (49.6 to 51.6) | 6.5 (6.3 to 6.7) | 11.7 (11.3 to 12.2) | 0.10 (0.09 to 0.10) | 4.2 (4.0 to 4.4) |

### (a) No programme: the higher line minus the current line (positive = more people below the line)

| Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ext | 1.3 (1.3 to 1.4) | 1.3 (1.3 to 1.4) | 2.0 (1.9 to 2.0) | 1.7 (1.5 to 1.8) | 0.0 (0.0 to 0.0) ns | 1.5 (1.5 to 1.6) | 1.8 (1.6 to 2.0) | 2.0 (1.9 to 2.0) | 2.1 (2.0 to 2.2) | 0.64 (0.63 to 0.65) | -0.1 (-0.1 to -0.1) |
| bea | 1.8 (1.7 to 1.8) | 1.8 (1.7 to 1.8) | 2.6 (2.6 to 2.7) | 2.3 (2.2 to 2.5) | 0.0 (0.0 to 0.0) | 2.0 (2.0 to 2.1) | 2.5 (2.3 to 2.7) | 2.7 (2.6 to 2.7) | 2.8 (2.7 to 2.9) | 0.86 (0.86 to 0.87) | -0.2 (-0.2 to -0.1) |

### (b) Programme against no programme, at each line (shares: reductions, positive = fewer below)

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | base | -4.4 (-4.6 to -4.2) | -2.9 (-3.2 to -2.7) | 7.6 (7.4 to 7.9) | -25.0 (-25.5 to -24.4) | 12,319 (12,171 to 12,467) | 251,409 (225,060 to 279,689) | -10.3 (-10.6 to -10.0) | -22.6 (-23.1 to -22.0) | 8.7 (8.4 to 9.0) | 11.5 (10.9 to 12.0) | 3.51 (3.43 to 3.60) | -0.6 (-0.7 to -0.5) |
| release row ($1,200, opt-in) | ext | -4.6 (-4.9 to -4.4) | -2.9 (-3.2 to -2.7) | 7.6 (7.3 to 7.9) | -24.9 (-25.5 to -24.4) | 12,354 (12,206 to 12,502) | 253,652 (226,974 to 282,267) | -10.6 (-10.9 to -10.3) | -22.6 (-23.2 to -22.1) | 8.5 (8.2 to 8.8) | 11.0 (10.5 to 11.6) | 3.69 (3.60 to 3.78) | -0.6 (-0.7 to -0.5) |
| release row ($1,200, opt-in) | bea | -4.7 (-4.9 to -4.5) | -2.9 (-3.2 to -2.7) | 7.6 (7.3 to 7.9) | -24.8 (-25.3 to -24.2) | 12,366 (12,217 to 12,513) | 254,340 (227,563 to 283,063) | -10.7 (-11.0 to -10.4) | -22.6 (-23.2 to -22.1) | 8.5 (8.2 to 8.8) | 10.9 (10.4 to 11.5) | 3.75 (3.66 to 3.84) | -0.6 (-0.7 to -0.5) |
| C2.2 design (automatic, all, needs level, needs-indexed) | base | 26.7 (26.3 to 27.0) | 26.5 (26.2 to 26.8) | 40.6 (40.1 to 41.0) | -9.1 (-9.8 to -8.4) | 50,535 (50,416 to 50,653) | 5,123,649,127 (4,537,031,585 to 5,787,646,198) | 6.5 (6.2 to 6.9) | -6.4 (-7.1 to -5.6) | 44.2 (43.7 to 44.6) | 53.7 (52.9 to 54.5) | 9.05 (8.90 to 9.20) | 5.2 (5.0 to 5.4) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 28.1 (27.8 to 28.4) | 28.0 (27.7 to 28.3) | 42.6 (42.1 to 43.0) | -5.7 (-6.5 to -5.0) | 53,362 (53,233 to 53,490) | 6,483,690,552 (5,732,639,123 to 7,329,128,414) | 7.8 (7.4 to 8.2) | -4.6 (-5.4 to -3.9) | 46.1 (45.7 to 46.6) | 55.5 (54.8 to 56.3) | 9.69 (9.54 to 9.84) | 5.6 (5.5 to 5.8) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 28.5 (28.2 to 28.9) | 28.5 (28.2 to 28.8) | 43.3 (42.8 to 43.7) | -4.3 (-5.0 to -3.5) | 54,338 (54,205 to 54,470) | 7,016,496,507 (6,203,319,548 to 7,932,357,998) | 8.2 (7.8 to 8.6) | -3.8 (-4.6 to -3.1) | 46.8 (46.3 to 47.3) | 56.2 (55.4 to 56.9) | 9.92 (9.76 to 10.07) | 5.8 (5.6 to 6.0) |

### (c) Does the effect depend on the line? (row - none) at the higher line minus (row - none) at the current line, rule 1 label

| Row | Line | Below 30 days of basic living, design-neutral (% adult-years) | Below 30 days of basic living, the design's own reading (% adult-years) | Below the cost of living (% adult-years) | Too little wealth at the end, $25,000 line (% adults) | Programme cost ($ per adult-year) | Cumulative inflation (% to the last year) | Cost: effect as % of the base effect | Inflation: as % of the base effect |
|---|---|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -0.2 (-0.3 to -0.2), *not changed* | -0.0 (-0.1 to 0.0), *not changed* | -0.0 (-0.1 to 0.0), *not changed* | 0.1 (-0.1 to 0.3), *not changed* | 35 (33 to 36) | 2,244 (1,934 to 2,581), *changed* | 100.3 (100.3 to 100.3) | 100.9 (100.8 to 100.9) |
| release row ($1,200, opt-in) | bea | -0.3 (-0.4 to -0.2), *not changed* | -0.0 (-0.1 to 0.0), *not changed* | -0.0 (-0.1 to 0.0), *not changed* | 0.2 (0.0 to 0.5), *not changed* | 46 (45 to 48) | 2,931 (2,538 to 3,363), *changed* | 100.4 (100.4 to 100.4) | 101.2 (101.1 to 101.2) |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.4 (1.4 to 1.5), *changed* | 1.5 (1.5 to 1.5), *changed* | 2.0 (2.0 to 2.0), *changed* | 3.3 (3.2 to 3.5), *changed* | 2,827 (2,816 to 2,838) | 1,360,041,425 (1,195,397,936 to 1,547,699,574), *changed* | 105.6 (105.6 to 105.6) | 126.5 (126.0 to 127.1) |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.9 (1.8 to 1.9), *changed* | 2.0 (1.9 to 2.0), *changed* | 2.7 (2.6 to 2.8), *changed* | 4.8 (4.6 to 5.0), *changed* | 3,803 (3,788 to 3,818) | 1,892,847,380 (1,663,730,363 to 2,153,203,689), *changed* | 107.5 (107.5 to 107.5) | 136.9 (136.2 to 137.7) |

### (c) for this study's own and secondary outcomes (reductions; rule 1 label)

| Row | Line | Too little wealth, household reading (% adult-years) | Too little wealth at the end, household reading (% households) | Households below their cost of living (% household-years) | Children below the cost of living (% child-years) | Poverty severity (FGT2) | Below the official poverty line (% household-years) |
|---|---|---|---|---|---|---|---|
| release row ($1,200, opt-in) | ext | -0.3 (-0.4 to -0.3), *not changed* | -0.1 (-0.4 to 0.2), *not changed* | -0.2 (-0.2 to -0.1), *not changed* | -0.4 (-0.6 to -0.3), *not changed* | 0.17 (0.17 to 0.18), *not changed* | 0.0 (-0.0 to 0.0), *not changed* |
| release row ($1,200, opt-in) | bea | -0.4 (-0.5 to -0.4), *not changed* | -0.1 (-0.4 to 0.2), *not changed* | -0.2 (-0.3 to -0.1), *not changed* | -0.5 (-0.7 to -0.4), *not changed* | 0.24 (0.23 to 0.24), *not changed* | 0.0 (0.0 to 0.0), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | ext | 1.3 (1.2 to 1.3), *changed* | 1.7 (1.5 to 2.0), *changed* | 2.0 (1.9 to 2.0), *changed* | 1.8 (1.7 to 1.9), *changed* | 0.64 (0.63 to 0.65), *not changed* | 0.4 (0.4 to 0.5), *not changed* |
| C2.2 design (automatic, all, needs level, needs-indexed) | bea | 1.7 (1.6 to 1.8), *changed* | 2.5 (2.3 to 2.8), *changed* | 2.6 (2.6 to 2.7), *changed* | 2.5 (2.4 to 2.6), *changed* | 0.87 (0.86 to 0.88), *not changed* | 0.5 (0.5 to 0.6), *not changed* |

### Coverage, participation and distribution (levels)

| Line | Row | Adult-years receiving the BU (%) | Adult-years the BU covers the C2.2 needs (%) | Mean share of the C2.2 needs covered (%) | Participation in the last year (%) | Non-participants below the cost of living (% of their years) | Non-participants with too little wealth (%) | Hours (mean) | Gini, disposable income | Gini, wealth |
|---|---|---|---|---|---|---|---|---|---|---|
| base | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.337 (0.334 to 0.340) | 0.724 (0.720 to 0.729) |
| base | release row ($1,200, opt-in) | 43.5 (42.9 to 44.0) | 0.0 (0.0 to 0.0) | 25.8 (25.5 to 26.2) | 43.6 (43.0 to 44.1) | 43.4 (42.9 to 43.9) | 70.4 (69.7 to 71.1) | -0.1 (-0.1 to -0.1) | 0.354 (0.351 to 0.357) | 0.743 (0.739 to 0.746) |
| base | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.0 (99.0 to 99.0) | 100.0 (100.0 to 100.0) | 4.5 (4.4 to 4.7) | 48.5 (47.5 to 49.6) | -0.1 (-0.1 to -0.1) | 0.339 (0.336 to 0.341) | 0.436 (0.433 to 0.439) |
| ext | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.338 (0.335 to 0.340) | 0.733 (0.729 to 0.738) |
| ext | release row ($1,200, opt-in) | 43.5 (42.9 to 44.0) | 0.0 (0.0 to 0.0) | 24.7 (24.3 to 25.0) | 43.6 (43.0 to 44.1) | 45.4 (44.9 to 45.9) | 71.8 (71.1 to 72.5) | -0.1 (-0.1 to -0.1) | 0.354 (0.351 to 0.357) | 0.754 (0.750 to 0.758) |
| ext | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.0 to 99.1) | 100.0 (100.0 to 100.0) | 4.5 (4.3 to 4.7) | 46.9 (45.9 to 48.0) | -0.1 (-0.1 to -0.1) | 0.334 (0.332 to 0.337) | 0.425 (0.422 to 0.428) |
| bea | no programme | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | n/a | n/a | n/a | -0.0 (-0.0 to -0.0) | 0.338 (0.335 to 0.340) | 0.736 (0.732 to 0.741) |
| bea | release row ($1,200, opt-in) | 43.5 (42.9 to 44.0) | 0.0 (0.0 to 0.0) | 24.3 (24.0 to 24.6) | 43.6 (43.0 to 44.1) | 46.1 (45.5 to 46.6) | 72.3 (71.6 to 73.0) | -0.1 (-0.1 to -0.1) | 0.354 (0.351 to 0.357) | 0.758 (0.754 to 0.761) |
| bea | C2.2 design (automatic, all, needs level, needs-indexed) | 100.0 (100.0 to 100.0) | 95.0 (95.0 to 95.0) | 99.1 (99.1 to 99.1) | 100.0 (100.0 to 100.0) | 4.5 (4.3 to 4.7) | 46.1 (45.0 to 47.2) | -0.1 (-0.1 to -0.1) | 0.333 (0.331 to 0.335) | 0.421 (0.419 to 0.424) |
