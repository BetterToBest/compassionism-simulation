# Release 2's other BLEI-paper measures and the measures study (S79, job X3)

*Nov 17, 2026. Plain-words report. Preregistration: research-update `prereg/2026-11-x3-measures-addendum.md` (committed before the run). Check note before the run: [s79-r2-measures-check.md](s79-r2-measures-check.md).*

## What was done, and why

The visual suite page's release 2 view showed only the BLEI series (the three tier shares and the median BLEI with its parts). Its cards for the BLEI paper's other five measures (the Extractive Drain Coefficient, EDC; the Effective Purchasing Power Multiplier, EPPM; the Financial Bandwidth Score, FBS; the Compound Stability Index, CSI; the Indirect Participant Benefit Index, IPBI) and the measures study (who gains, how people move between tiers, wealth net of drain) said they existed for release 1 only.

Job X3 re-ran release 2's main rows (no programme, the C2.2 design, the release design; 500 adults; seeds 1-500, paired across rows; Reference, Adverse and Stress; 20 and 40 years) with the measures study on and two reporting switches that release 2's rows did not carry: the measured EDC and the FBS50 tally with each adult's own advancement rate (the rule release 2 ran). Both switches record; neither changes what happens.

- Where: GitHub Actions (free), compassionism-sim-results run-study run 126, Nov 17, 2026; engine commit `6d095a1`; results folder `x3-6d095a1/` with `run.txt` and `SHA256SUMS` (all files verify).
- **The run is release 2.** In every one of the six shards, every engine output of every row and seed (2,931 row-keys, 1,465,500 values a shard) equals release 2's stored results (part M, engine `104691f`); the only extra keys are the two switches' own. Seed 1's adults add up to the engine's yearly shares. The accounting check found no failures in any shard.
- **A second tie to the published release.** Each row's share of adult-years below the cost of living from X3 equals release 2's published basket-poverty figure, in all 18 cells (3 rows, 3 environments, 2 horizons); `dev/tools/suite_r2.py --check` checks this on every change.

The page now reads `data/releases/r2/study-20.json` and `study-40.json` (written by `suite_r2.py --study` from the shards, a re-arrangement only). Release 1's and release 2's rows are still never drawn on one chart; v5.6's files are untouched.

## What the measures show (all preregistered outputs; nulls and the Adverse and Stress environments included)

Every figure below is the mean over 500 paired runs with the 10th to 90th percentile across runs, or, for changes, the paired difference against no programme on the same seeds with its 95% interval. The intervals cover the model's randomness only, not the choice of design parameters (full backing, today's price rule; see release 2's own report). No synergy is measured here.

**EDC (drain to rent and interest).** Without the programme, 26.2% of income goes to rent and interest in the Reference environment at 20 years (Adverse and Stress: 30.1%). Both designs lower it in every environment and horizon: C2.2 by 16.9 to 23.1 points; the release design by 10.9 to 11.1 points in Reference and Adverse, and by 5.3 (20 years) to 5.5 (40 years) points in Stress. Every interval excludes zero.

**EPPM (how far each adult's resources go against the same adult with no programme).** At the last year, adults under C2.2 have 2.0 to 3.0 times their twin's resources; under the release design 1.1 to 1.5 times (participants 1.3 to 1.6, non-participants 1.04 to 1.15). The poorest fifth gains most (2.6 to 11.3 times). 97% to 99.6% of adults are better off than their twin. Under C2.2 everyone takes part, so the non-participant cells are empty ("–"), not zero.

**FBS (financial bandwidth).** The share of participant-years whose monthly surplus reaches the level at which the chance of advancing a tier is even: 73% to 79% under C2.2 and 46% to 67% under the release design, lowest in Stress. The even-odds level itself (about $830-$890 a month) is the model's rule, not an outcome; it differs between environments only through prices. The median monthly surplus at the last year is $0 to $2,026 without the programme, $3,929 to $9,289 under C2.2, and $0 to $5,393 under the release design. Under the release design in Adverse and Stress the median adult has almost no surplus: $729 and $48 at 20 years, $9 and $0 at 40 years, with 41% to 60% of adults having none at all.

**CSI (two years or more of basic living, counting Acre Equity).** At the last year: 51% to 65% of adults without the programme, 76% to 96% under C2.2, 56% to 83% under the release design. Under Stress the release design adds little (55.8% against 51.4% at 20 years).

**IPBI (only partly modelled: public costs avoided).** Prisons and hospital and psychiatric stays avoided: about $670 to $1,320 per adult a year in every cell but one (high reading up to about $11,600); about $300 under the release design in Stress. Unhoused person-years avoided: 0.5 to 2.6 per 1,000 adults a year. These come from the means over the runs, as release 1's panel computes them, so they carry no interval. The paper's market, productivity and property-value channels are not in the model.

**Poverty lines and cost.** Extreme poverty falls by 0.06 to 0.26 points from 0.25-0.31%; the share below the cost of living (basket poverty) falls by 6.7 to 46.1 points; the poverty gap by 5.0 to 21.5 points; every interval excludes zero. The gross programme cost per adult-year (year-0 dollars, as the engine's `cost` reports it, not net of anything) is $68,000 to $84,000 under C2.2 and $7,800 to $39,400 under the release design (lowest in Stress, where fewer take part and the allowance is smaller).

**Movement (the measures study).** Without the programme 21% to 30% of adults are in Crisis at some point and 61% to 82% of those who start there never leave. Under C2.2 no adult is in Crisis in any year, so "re-enter" and "never leave" have no one to count and are shown as missing. Under the release design 3.5% to 21% are ever in Crisis; in Stress at 40 years 21.1%, against 29.5% without it.

**A null result: the wealth Gini.** The wealth Gini is about 0.984 to 0.987 in every row, environment and horizon, with or without the programme, and net of drain the same. The model's wealth distribution is dominated by a few large holdings, and neither design changes that measurably. The page shows it as it is.

**Where the release design is weak.** In Stress (40% take part, a smaller allowance, smaller community programmes) the release design's gains are a third or less of C2.2's on the drain and the poverty lines, and far smaller on bandwidth. At 20 years: EDC −5.3 points against −18.3, basket poverty −7.7 against −40.1, 52% of participant-years at even odds against 74%, and half of adults with no monthly surplus at the last year.

## Full tables


#### 20 years: measures (mean over 500 runs, 10th to 90th percentile)

| Environment | Row | EDC measured % | FBS participant-years above even odds % | FBS50 median $/month | Cost $/adult/yr | Extreme poverty % | Below cost of living % | Poverty gap % |
|---|---|---|---|---|---|---|---|---|
| Reference | No programme | 26.2 (25.1 to 27.3) | 0.0 (0.0 to 0.0) | 0 (0 to 0) | 0 (0 to 0) | 0.26 (0.24 to 0.28) | 36.1 (33.9 to 38.5) | 15.8 (14.6 to 16.9) |
| Reference | C2.2 | 9.0 (8.5 to 9.5) | 79.2 (76.8 to 81.8) | 827 (790 to 867) | 80493 (79157 to 81910) | 0.06 (0.05 to 0.06) | 3.7 (3.1 to 4.3) | 0.7 (0.5 to 0.8) |
| Reference | Release design | 15.1 (14.3 to 16.1) | 67.2 (64.1 to 70.2) | 827 (784 to 869) | 38093 (36773 to 39346) | 0.12 (0.10 to 0.13) | 15.2 (13.6 to 16.8) | 4.3 (3.7 to 4.8) |
| Adverse | No programme | 30.1 (28.8 to 31.4) | 0.0 (0.0 to 0.0) | 0 (0 to 0) | 0 (0 to 0) | 0.28 (0.26 to 0.30) | 44.6 (42.1 to 47.3) | 19.8 (18.4 to 21.1) |
| Adverse | C2.2 | 9.7 (9.2 to 10.3) | 78.1 (75.5 to 80.9) | 827 (790 to 867) | 79396 (78138 to 80857) | 0.06 (0.05 to 0.06) | 4.0 (3.4 to 4.7) | 0.7 (0.6 to 0.8) |
| Adverse | Release design | 19.2 (18.1 to 20.3) | 63.6 (60.5 to 66.7) | 827 (784 to 869) | 26994 (25828 to 28069) | 0.15 (0.14 to 0.16) | 25.7 (23.6 to 27.9) | 8.1 (7.3 to 8.9) |
| Stress | No programme | 30.1 (28.8 to 31.4) | 0.0 (0.0 to 0.0) | 0 (0 to 0) | 0 (0 to 0) | 0.28 (0.26 to 0.30) | 44.6 (42.1 to 47.3) | 19.8 (18.4 to 21.1) |
| Stress | C2.2 | 11.8 (11.3 to 12.3) | 73.5 (70.2 to 76.7) | 882 (842 to 924) | 68178 (67046 to 69356) | 0.07 (0.07 to 0.08) | 4.5 (3.9 to 5.2) | 0.8 (0.6 to 0.9) |
| Stress | Release design | 24.8 (23.7 to 26.0) | 52.1 (47.4 to 57.2) | 886 (830 to 949) | 9660 (8804 to 10513) | 0.22 (0.21 to 0.24) | 37.0 (34.5 to 39.5) | 14.6 (13.5 to 15.6) |

#### 20 years: paired change against no programme (mean [95% interval])

| Environment | Design | EDC (person-years) pts | EDC (aggregate) pts | Cost $/adult/yr | Extreme poverty pts | Below cost of living pts | Poverty gap pts | IPBI: prisons and hospital stays avoided $/adult/yr (high) | Unhoused person-years avoided per 1,000 | Homelessness costs avoided $ low-high |
|---|---|---|---|---|---|---|---|---|---|---|
| Reference | C2.2 | −17.2 [−17.3, −17.2] | −8.4 [−8.4, −8.4] | 80493 [80401, 80586] | −0.20 [−0.20, −0.20] | −32.4 [−32.5, −32.2] | −15.1 [−15.2, −15.1] | 925 (8169) | 1.98 | 21-199 |
| Reference | Release design | −11.0 [−11.1, −11.0] | −5.6 [−5.7, −5.6] | 38093 [38005, 38181] | −0.14 [−0.14, −0.14] | −20.9 [−21.1, −20.8] | −11.5 [−11.6, −11.5] | 702 (6225) | 1.41 | 15-141 |
| Adverse | C2.2 | −20.4 [−20.5, −20.3] | −11.0 [−11.1, −11.0] | 79396 [79305, 79487] | −0.22 [−0.22, −0.22] | −40.6 [−40.8, −40.5] | −19.1 [−19.2, −19.0] | 1166 (10296) | 2.19 | 23-221 |
| Adverse | Release design | −10.9 [−11.0, −10.8] | −6.4 [−6.5, −6.4] | 26994 [26917, 27070] | −0.13 [−0.13, −0.13] | −18.9 [−19.1, −18.8] | −11.7 [−11.8, −11.6] | 710 (6314) | 1.30 | 14-131 |
| Stress | C2.2 | −18.3 [−18.4, −18.2] | −9.3 [−9.4, −9.3] | 68178 [68100, 68256] | −0.21 [−0.21, −0.21] | −40.1 [−40.3, −40.0] | −19.0 [−19.1, −19.0] | 1163 (10272) | 2.07 | 22-209 |
| Stress | Release design | −5.3 [−5.3, −5.2] | −3.1 [−3.1, −3.0] | 9660 [9602, 9717] | −0.06 [−0.06, −0.05] | −7.7 [−7.8, −7.6] | −5.2 [−5.3, −5.2] | 316 (2816) | 0.56 | 6-56 |

#### 20 years: the measures study at the last year (mean, 10th to 90th percentile)

| Environment | Row | EPPM all | EPPM participants | EPPM non-participants | EPPM poorest fifth | Better off than twin % | Median monthly surplus $ | No surplus % | Two years+ basic living, with Acre Equity % | Wealth Gini | Wealth Gini net of drain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Reference | No programme | – | – | – | – | – | 1011 (686 to 1364) | 41.4 (38.6 to 44.0) | 53.5 (51.0 to 55.8) | 0.986 (0.983 to 0.990) | 0.986 (0.983 to 0.990) |
| Reference | C2.2 | 2.10 (2.04 to 2.16) | 2.10 (2.04 to 2.16) | – (– to –) | 9.23 (7.53 to 11.11) | 99.2 (98.8 to 99.6) | 7474 (7058 to 7905) | 1.5 (0.8 to 2.2) | 83.9 (82.0 to 85.6) | 0.984 (0.979 to 0.989) | 0.984 (0.980 to 0.989) |
| Reference | Release design | 1.51 (1.48 to 1.54) | 1.61 (1.57 to 1.64) | 1.09 (1.07 to 1.10) | 4.99 (4.11 to 5.95) | 98.7 (98.0 to 99.4) | 3738 (3349 to 4122) | 21.1 (18.8 to 23.4) | 69.9 (67.4 to 72.2) | 0.985 (0.982 to 0.990) | 0.985 (0.982 to 0.990) |
| Adverse | No programme | – | – | – | – | – | 0 (0 to 0) | 57.3 (54.0 to 60.8) | 51.4 (49.0 to 53.6) | 0.987 (0.983 to 0.990) | 0.987 (0.984 to 0.990) |
| Adverse | C2.2 | 2.57 (2.44 to 2.74) | 2.57 (2.44 to 2.74) | – (– to –) | 10.41 (8.64 to 12.40) | 99.4 (99.0 to 99.8) | 5394 (5079 to 5717) | 1.8 (1.0 to 2.6) | 81.2 (79.2 to 83.2) | 0.984 (0.980 to 0.989) | 0.984 (0.980 to 0.989) |
| Adverse | Release design | 1.38 (1.33 to 1.46) | 1.58 (1.52 to 1.68) | 1.10 (1.07 to 1.16) | 4.08 (3.38 to 4.88) | 98.4 (97.6 to 99.2) | 729 (472 to 996) | 41.4 (38.6 to 44.2) | 63.2 (61.0 to 65.6) | 0.986 (0.982 to 0.990) | 0.986 (0.982 to 0.990) |
| Stress | No programme | – | – | – | – | – | 0 (0 to 0) | 57.3 (54.0 to 60.8) | 51.4 (49.0 to 53.6) | 0.987 (0.983 to 0.990) | 0.987 (0.984 to 0.990) |
| Stress | C2.2 | 2.30 (2.19 to 2.45) | 2.30 (2.19 to 2.45) | – (– to –) | 8.99 (7.47 to 10.62) | 99.2 (98.8 to 99.6) | 4446 (4135 to 4755) | 3.9 (2.8 to 5.2) | 75.7 (73.6 to 77.8) | 0.984 (0.980 to 0.989) | 0.985 (0.981 to 0.989) |
| Stress | Release design | 1.14 (1.11 to 1.20) | 1.37 (1.32 to 1.44) | 1.04 (1.03 to 1.09) | 3.14 (2.59 to 3.75) | 97.4 (95.8 to 99.0) | 48 (0 to 187) | 51.0 (47.8 to 54.0) | 55.8 (53.4 to 58.0) | 0.986 (0.983 to 0.990) | 0.986 (0.983 to 0.990) |

#### 20 years: movement (per run at the last year; mean, 10th to 90th percentile)

| Environment | Row | Start in Crisis % | Ever in Crisis % | Years in Crisis | Re-enter within 2 years % | Never leave Crisis % |
|---|---|---|---|---|---|---|
| Reference | No programme | 9.2 (7.8 to 10.8) | 21.3 (19.6 to 23.2) | 2.82 (2.56 to 3.09) | 9.9 (3.0 to 17.1) | 73.8 (65.1 to 82.5) |
| Reference | C2.2 | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.00 (0.00 to 0.00) | – (– to –) | – (– to –) |
| Reference | Release design | 1.9 (1.2 to 2.8) | 3.5 (2.4 to 4.8) | 0.39 (0.25 to 0.54) | 8.3 (0.0 to 20.0) | 44.8 (22.2 to 69.4) |
| Adverse | No programme | 9.2 (7.8 to 10.8) | 24.1 (22.0 to 26.2) | 3.23 (2.93 to 3.55) | 13.4 (5.4 to 22.7) | 81.7 (73.5 to 89.2) |
| Adverse | C2.2 | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.00 (0.00 to 0.00) | – (– to –) | – (– to –) |
| Adverse | Release design | 1.9 (1.2 to 2.8) | 6.9 (5.4 to 8.4) | 0.75 (0.56 to 0.95) | 14.5 (0.0 to 33.3) | 54.6 (28.6 to 80.0) |
| Stress | No programme | 9.2 (7.8 to 10.8) | 24.1 (22.0 to 26.2) | 3.23 (2.93 to 3.55) | 13.4 (5.4 to 22.7) | 81.7 (73.5 to 89.2) |
| Stress | C2.2 | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.00 (0.00 to 0.00) | – (– to –) | – (– to –) |
| Stress | Release design | 5.4 (4.2 to 6.8) | 15.2 (13.2 to 17.2) | 1.91 (1.64 to 2.21) | 13.1 (0.0 to 25.0) | 74.3 (62.1 to 86.1) |

#### 40 years: measures (mean over 500 runs, 10th to 90th percentile)

| Environment | Row | EDC measured % | FBS participant-years above even odds % | FBS50 median $/month | Cost $/adult/yr | Extreme poverty % | Below cost of living % | Poverty gap % |
|---|---|---|---|---|---|---|---|---|
| Reference | No programme | 24.9 (24.0 to 25.8) | 0.0 (0.0 to 0.0) | 0 (0 to 0) | 0 (0 to 0) | 0.25 (0.23 to 0.27) | 32.8 (31.0 to 34.9) | 14.5 (13.5 to 15.5) |
| Reference | C2.2 | 8.0 (7.6 to 8.4) | 78.5 (75.7 to 81.3) | 827 (790 to 867) | 84175 (82815 to 85598) | 0.05 (0.05 to 0.05) | 2.1 (1.7 to 2.5) | 0.4 (0.3 to 0.4) |
| Reference | Release design | 14.0 (13.2 to 14.8) | 64.5 (61.0 to 67.8) | 827 (784 to 869) | 39420 (38042 to 40764) | 0.10 (0.09 to 0.11) | 12.9 (11.6 to 14.2) | 3.6 (3.1 to 4.0) |
| Adverse | No programme | 32.5 (31.3 to 33.7) | 0.0 (0.0 to 0.0) | 0 (0 to 0) | 0 (0 to 0) | 0.31 (0.28 to 0.34) | 48.5 (46.1 to 50.9) | 21.9 (20.7 to 23.2) |
| Adverse | C2.2 | 9.4 (8.9 to 9.9) | 77.0 (73.9 to 79.9) | 827 (790 to 867) | 83322 (81987 to 84820) | 0.05 (0.05 to 0.05) | 2.4 (1.9 to 2.8) | 0.4 (0.3 to 0.5) |
| Adverse | Release design | 21.4 (20.3 to 22.5) | 59.0 (55.3 to 62.8) | 827 (784 to 869) | 20689 (19751 to 21600) | 0.17 (0.16 to 0.19) | 31.8 (29.7 to 34.0) | 10.9 (10.0 to 11.7) |
| Stress | No programme | 32.5 (31.3 to 33.7) | 0.0 (0.0 to 0.0) | 0 (0 to 0) | 0 (0 to 0) | 0.31 (0.28 to 0.34) | 48.5 (46.1 to 50.9) | 21.9 (20.7 to 23.2) |
| Stress | C2.2 | 11.7 (11.3 to 12.2) | 72.6 (69.1 to 75.9) | 882 (842 to 924) | 70946 (69819 to 72115) | 0.06 (0.06 to 0.07) | 3.1 (2.6 to 3.6) | 0.5 (0.4 to 0.6) |
| Stress | Release design | 27.0 (25.8 to 28.2) | 46.4 (41.0 to 52.6) | 886 (830 to 949) | 7771 (7040 to 8466) | 0.25 (0.23 to 0.27) | 41.7 (39.5 to 44.0) | 16.9 (15.8 to 18.0) |

#### 40 years: paired change against no programme (mean [95% interval])

| Environment | Design | EDC (person-years) pts | EDC (aggregate) pts | Cost $/adult/yr | Extreme poverty pts | Below cost of living pts | Poverty gap pts | IPBI: prisons and hospital stays avoided $/adult/yr (high) | Unhoused person-years avoided per 1,000 | Homelessness costs avoided $ low-high |
|---|---|---|---|---|---|---|---|---|---|---|
| Reference | C2.2 | −16.9 [−17.0, −16.9] | −7.8 [−7.8, −7.7] | 84175 [84081, 84269] | −0.20 [−0.20, −0.20] | −30.7 [−30.9, −30.6] | −14.2 [−14.2, −14.1] | 866 (7642) | 2.00 | 21-202 |
| Reference | Release design | −10.9 [−11.0, −10.9] | −5.3 [−5.4, −5.3] | 39420 [39328, 39512] | −0.15 [−0.15, −0.15] | −20.0 [−20.1, −19.9] | −11.0 [−11.0, −10.9] | 666 (5911) | 1.49 | 16-150 |
| Adverse | C2.2 | −23.1 [−23.2, −23.0] | −13.2 [−13.3, −13.1] | 83322 [83227, 83416] | −0.26 [−0.26, −0.25] | −46.1 [−46.3, −45.9] | −21.5 [−21.6, −21.4] | 1316 (11616) | 2.56 | 27-258 |
| Adverse | Release design | −11.1 [−11.2, −11.0] | −7.1 [−7.2, −7.1] | 20689 [20626, 20753] | −0.14 [−0.14, −0.14] | −16.7 [−16.8, −16.6] | −11.1 [−11.1, −11.0] | 668 (5953) | 1.37 | 14-137 |
| Stress | C2.2 | −20.8 [−20.8, −20.7] | −11.3 [−11.4, −11.3] | 70946 [70864, 71028] | −0.24 [−0.25, −0.24] | −45.4 [−45.5, −45.2] | −21.5 [−21.6, −21.4] | 1311 (11581) | 2.44 | 26-245 |
| Stress | Release design | −5.5 [−5.5, −5.4] | −3.5 [−3.5, −3.5] | 7771 [7723, 7819] | −0.06 [−0.06, −0.06] | −6.7 [−6.8, −6.7] | −5.0 [−5.1, −5.0] | 302 (2699) | 0.59 | 6-59 |

#### 40 years: the measures study at the last year (mean, 10th to 90th percentile)

| Environment | Row | EPPM all | EPPM participants | EPPM non-participants | EPPM poorest fifth | Better off than twin % | Median monthly surplus $ | No surplus % | Two years+ basic living, with Acre Equity % | Wealth Gini | Wealth Gini net of drain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Reference | No programme | – | – | – | – | – | 2026 (1658 to 2435) | 35.9 (33.4 to 38.4) | 64.7 (62.2 to 67.0) | 0.987 (0.984 to 0.991) | 0.987 (0.984 to 0.991) |
| Reference | C2.2 | 2.03 (1.98 to 2.08) | 2.03 (1.98 to 2.08) | – (– to –) | 9.42 (7.52 to 11.65) | 99.3 (98.8 to 99.6) | 9289 (8824 to 9769) | 0.8 (0.4 to 1.4) | 95.9 (94.8 to 97.0) | 0.984 (0.980 to 0.989) | 0.984 (0.980 to 0.989) |
| Reference | Release design | 1.53 (1.50 to 1.55) | 1.61 (1.57 to 1.64) | 1.15 (1.14 to 1.16) | 5.04 (4.13 to 6.13) | 98.9 (98.2 to 99.4) | 5393 (4935 to 5878) | 18.2 (16.2 to 20.4) | 83.4 (81.4 to 85.2) | 0.986 (0.982 to 0.990) | 0.986 (0.982 to 0.990) |
| Adverse | No programme | – | – | – | – | – | 0 (0 to 0) | 65.0 (61.6 to 68.8) | 55.9 (53.4 to 58.4) | 0.987 (0.984 to 0.991) | 0.987 (0.985 to 0.991) |
| Adverse | C2.2 | 2.98 (2.83 to 3.16) | 2.98 (2.83 to 3.16) | – (– to –) | 11.34 (9.49 to 13.33) | 99.6 (99.2 to 100.0) | 4995 (4682 to 5288) | 1.1 (0.6 to 1.6) | 92.0 (90.4 to 93.4) | 0.985 (0.981 to 0.989) | 0.985 (0.981 to 0.989) |
| Adverse | Release design | 1.30 (1.27 to 1.36) | 1.54 (1.48 to 1.62) | 1.15 (1.13 to 1.20) | 3.29 (2.79 to 3.87) | 98.7 (98.0 to 99.4) | 9 (0 to 7) | 52.9 (50.0 to 56.2) | 67.2 (64.8 to 69.4) | 0.987 (0.984 to 0.991) | 0.987 (0.984 to 0.991) |
| Stress | No programme | – | – | – | – | – | 0 (0 to 0) | 65.0 (61.6 to 68.8) | 55.9 (53.4 to 58.4) | 0.987 (0.984 to 0.991) | 0.987 (0.985 to 0.991) |
| Stress | C2.2 | 2.61 (2.48 to 2.76) | 2.61 (2.48 to 2.76) | – (– to –) | 9.64 (8.06 to 11.31) | 99.3 (98.8 to 99.8) | 3929 (3644 to 4203) | 3.7 (2.8 to 4.8) | 87.5 (85.8 to 89.2) | 0.985 (0.982 to 0.990) | 0.985 (0.982 to 0.990) |
| Stress | Release design | 1.11 (1.09 to 1.14) | 1.32 (1.27 to 1.37) | 1.06 (1.05 to 1.09) | 2.59 (2.19 to 3.10) | 97.7 (96.4 to 99.0) | 0 (0 to 0) | 60.4 (57.2 to 64.0) | 60.3 (57.8 to 62.6) | 0.987 (0.984 to 0.991) | 0.987 (0.984 to 0.991) |

#### 40 years: movement (per run at the last year; mean, 10th to 90th percentile)

| Environment | Row | Start in Crisis % | Ever in Crisis % | Years in Crisis | Re-enter within 2 years % | Never leave Crisis % |
|---|---|---|---|---|---|---|
| Reference | No programme | 9.2 (7.8 to 10.8) | 23.7 (21.6 to 25.6) | 5.60 (5.03 to 6.13) | 10.7 (6.5 to 15.6) | 61.1 (52.8 to 71.1) |
| Reference | C2.2 | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.00 (0.00 to 0.00) | – (– to –) | – (– to –) |
| Reference | Release design | 1.9 (1.2 to 2.8) | 3.8 (2.6 to 5.0) | 0.71 (0.45 to 0.99) | 9.5 (0.0 to 20.7) | 32.0 (11.1 to 57.1) |
| Adverse | No programme | 9.2 (7.8 to 10.8) | 29.5 (27.4 to 31.6) | 7.84 (7.22 to 8.49) | 15.1 (8.3 to 22.1) | 78.4 (70.2 to 86.6) |
| Adverse | C2.2 | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.00 (0.00 to 0.00) | – (– to –) | – (– to –) |
| Adverse | Release design | 1.9 (1.2 to 2.8) | 12.0 (10.2 to 14.0) | 2.39 (1.95 to 2.84) | 15.8 (3.2 to 27.3) | 51.2 (27.3 to 75.0) |
| Stress | No programme | 9.2 (7.8 to 10.8) | 29.5 (27.4 to 31.6) | 7.84 (7.22 to 8.49) | 15.1 (8.3 to 22.1) | 78.4 (70.2 to 86.6) |
| Stress | C2.2 | 0.0 (0.0 to 0.0) | 0.0 (0.0 to 0.0) | 0.00 (0.00 to 0.00) | – (– to –) | – (– to –) |
| Stress | Release design | 5.4 (4.2 to 6.8) | 21.1 (18.8 to 23.2) | 5.00 (4.35 to 5.58) | 15.0 (7.0 to 23.5) | 70.8 (58.6 to 83.3) |


"–" means the cell has no one to count (for example non-participants under C2.2, where everyone takes part) or the measure does not apply to the row (EPPM for no programme); it is not zero. Stress's no-programme row equals Adverse's: Stress is the Adverse environment with weaker programme settings.

## Limits

EPPM, FBS and CSI are measured in the model's own terms, not with the paper's formulas; each card says how. IPBI covers only public costs. The FBS's even-odds level is a model rule with a provisional range, not an observed rate. The model has not been reviewed by an independent economist.

## How to reproduce

`node runner/jobs/series-r2.js --env=all --years=20,40 --n=500 --study --seeds=1-6` in compassionism-sim-results (runner commit `e88585d`) with a clean checkout of engine `6d095a1`; then `python3 dev/tools/suite_r2.py --study RESULTS/x3-6d095a1` and `python3 dev/tools/suite_r2.py --check` here. The tables above are printed from `data/releases/r2/study-*.json`.
