# v5.6: the results with today's safety net in both runs

Oct 14, 2026 (session 10; ledger step s167). **This is a draft release for Duke to merge or withhold.** Merging it is the release. If it is withheld, the pages stay on v5.5 and nothing else changes.

**Duke: before deciding, please read `dev/reports/v5-33-snap-work-rule.md`** (what SNAP's work rule is and how it is modelled) and `dev/reports/v5-35-safety-net-poverty.md` (why today's safety net slightly raises basket poverty in some runs). The open questions are yours: whether v5.6's main rows include today's safety net (issue i23) and SNAP's work rule (issue i24-2). This report gives the figures for that decision. It does not decide it.

## 1. What changes in v5.6

v5.5 (Oct 13) changed no figure: it shows v5.4's results. In v5.4 and v5.5 the "no program" run had no taxes or transfers at all. In v5.6 **both runs, with and without Compassionism, also have today's safety net**: SNAP (food stamps), the earned income tax credit (EITC) and the refundable Child Tax Credit, paid on last year's income, at today's take-up rates. "No program" therefore means today's US policy, and each change is what Compassionism adds to it. Three things are in v5.6's runs, each behind a switch that leaves v5.5's figures identical when it is off:

1. **Today's safety net** (`--sn`), in both runs of every row.
2. **SNAP's work rule** for adults aged 18 to 64 with no child under 14 (`--snab`; Public Law 119-21, in force since Nov 1, 2025).
3. **A fix to how the safety net's marginal rate is read** (`--slope`): SNAP's income limit is no longer read as a tax on all earnings (`v5-35-safety-net-poverty.md`, section 4).

Everything else is v5.4's engine. The figures are 500 paired runs (seeds 1 to 500) in each of the Reference, Adverse and Stress Test environments, over 20 and 40 years, from one study on one machine: engine commit 5bf5bcc, clean tree, every file checked (`dev/tools/s165_verify.py`). Command: `node harness.js testbed 500 release ENV --v54 --snab --slope` (and `--years=40`), in pieces merged with `dev/tools/merge_parts.py`; results in BetterToBest/compassionism-sim-results, folder `s165-5bf5bcc`.

## 2. The headline figures, v5.5 beside v5.6

Each cell: the no-program run → with Compassionism (the change, in points). Shares of adults (or of children) in a typical year, except "too little wealth", which is at the last year. A lower number is better. "Gain moved" is v5.6's change minus v5.5's: a minus sign means Compassionism's measured gain grew; a plus sign means it shrank.

**Reference, 20 years**

| Measure | v5.5 | v5.6 | Gain moved |
|---|---|---|---|
| Below 30 days of basic living | 26.5 → 11.6 (−14.9) | 26.5 → 11.7 (−14.8) | +0.07 |
| Below the cost of living | 49.2 → 19.6 (−29.6) | 49.3 → 19.5 (−29.7) | −0.13 |
| Too little wealth (worse with the program) | 32.6 → 43.6 (+11.0) | 32.7 → 44.4 (+11.7) | +0.66 |
| Children below the cost of living | 76.3 → 33.3 (−43.1) | 76.4 → 32.2 (−44.2) | −1.13 |
| Depth of poverty (severity measure) | 7.57 → 1.56 (−6.01) | 7.17 → 1.34 (−5.83) | +0.17 |

**Adverse, 20 years**

| Measure | v5.5 | v5.6 | Gain moved |
|---|---|---|---|
| Below 30 days of basic living | 31.5 → 17.3 (−14.2) | 31.6 → 17.5 (−14.1) | +0.13 |
| Below the cost of living | 66.0 → 31.3 (−34.7) | 66.0 → 31.1 (−34.9) | −0.25 |
| Too little wealth (worse with the program) | 45.1 → 80.0 (+34.9) | 45.1 → 80.9 (+35.8) | +0.91 |
| Children below the cost of living | 89.0 → 48.6 (−40.4) | 89.0 → 46.9 (−42.1) | −1.68 |
| Depth of poverty | 13.05 → 2.84 (−10.21) | 11.96 → 2.38 (−9.58) | +0.62 |

**Stress Test, 20 years**

| Measure | v5.5 | v5.6 | Gain moved |
|---|---|---|---|
| Below 30 days of basic living (worse with the program) | 31.5 → 35.0 (+3.4) | 31.6 → 35.3 (+3.8) | +0.34 |
| Below the cost of living | 66.0 → 52.3 (−13.7) | 66.0 → 52.8 (−13.2) | +0.46 |
| Too little wealth (worse with the program) | 45.1 → 75.4 (+30.4) | 45.1 → 76.3 (+31.2) | +0.77 |
| Children below the cost of living | 89.0 → 73.6 (−15.4) | 89.0 → 74.4 (−14.6) | +0.77 |
| Depth of poverty | 13.05 → 8.14 (−4.91) | 11.96 → 7.31 (−4.65) | +0.25 |

**40 years** (gain moved, v5.6 minus v5.5; the full tables are in the findings explorer, release v5.6)

| Measure | Reference | Adverse | Stress Test |
|---|---|---|---|
| Below 30 days of basic living | +0.10 | +0.20 | +0.49 |
| Below the cost of living | −0.16 | +0.03 | +0.54 |
| Too little wealth | +0.55 (the change goes from +0.78 to +1.33) | +0.41 | +0.36 |
| Children below the cost of living | −1.30 | −1.69 | +0.66 |
| Depth of poverty | +0.14 | +1.04 | +0.37 |

Every 95% interval of the main changes is about ±0.1 to ±0.25 points (shown on the pages), so moves under about 0.2 points are within the runs' own spread.

## 3. Did Compassionism's measured gain move?

**Very little, and not in one direction.**

- **The headline picture is unchanged.** In every environment and at both horizons, Compassionism still cuts the share below 30 days of basic living (except the Stress Test, where it still raises it), still cuts the share below the cost of living by 10 to 35 points, and still leaves more adults with too little wealth at the end. No result changed sign.
- **For adults, the gain moved by less than one point everywhere.** It grew slightly on the cost of living at Reference and Adverse (−0.13 and −0.25 points over 20 years) and shrank slightly on the 30-day measure (+0.07 to +0.34). Too little wealth got a little worse with the program (by 0.36 to 0.91 points).
- **For children, the gain grew by 1.1 to 1.7 points at Reference and Adverse** (why is not traced yet; the Child Tax Credit and SNAP reach families with children in both runs), and shrank by 0.7 to 0.8 points in the Stress Test.
- **The no-program run itself barely moves on the shares** (by 0.01 to 0.1 points), because the safety net's few thousand dollars a year rarely lift a household over the high cost-of-living line. **It moves the depth of poverty clearly** (the severity measure falls by 0.3 to 1.9 points with no program). So the program has a little less depth to remove, and its measured gain on depth is 0.1 to 1.0 points smaller.
- **The Stress Test is where the gain shrinks on every measure** (by 0.2 to 0.8 points). There, the safety net's phase-outs and the program's weaker setting combine; `v5-35-safety-net-poverty.md` (section 5) shows why: with Compassionism in the Stress Test, the safety net's work response puts some people just below the line.

## 4. Where the move comes from

v5.6 differs from v5.5 by the three switches of section 1 and nothing else (each switch off gives v5.5's figures exactly, shown by `guard_test.js` and `snap_rule_check.js`).

- **SNAP's work rule: almost nothing.** The study ran the main row and its no-program run with today's safety net, rule off and rule on, paired by seed (`dev/runs/snap-rule/snap-iso-ENV-YEARS.json`). The rule changes Compassionism's measured gain by at most 0.07 points (cost of living, Adverse, 40 years), and by under 0.03 points everywhere else. It moves the no-program run by under 0.01 points on the shares. The rule takes about $5 a year of SNAP per adult on average at Reference and $12 to $30 in Adverse and the Stress Test: few adults are covered and out of work for more than three months.
- **Today's safety net, with the marginal-rate fix: nearly all of the move.** Since the rule adds almost nothing, the gain moves in section 2 are, to within a few hundredths of a point, the safety net's (with the fix on).
- **The marginal-rate fix alone** was not run separately at 500 seeds (every safety-net run of the study has it on, by decision; `dev/DECISIONS.md`, session 9). At 20 seeds it lowered basket poverty with Compassionism by 0.05 to 0.12 points (`v5-35-safety-net-poverty.md`, section 4), so it is a small part of the move, in the direction of a slightly larger gain.

## 5. What stays from earlier releases (stated on the pages)

- **What each part of the design does** (the attribution runs) and **the no-program run against US data** are still v5.3's runs, as they were in v5.4 and v5.5. They have no safety net in either run; the pages now say so. Rerunning them with the safety net is follow-up work.
- The pages' own "run it yourself" simulator does not have the safety net (it is a study setting of the 500-run engine, not a control on the page). The guided figures and the findings explorer show the v5.6 study.

## 6. Limits

- The safety net is three programmes (SNAP, the EITC and the refundable Child Tax Credit). Medicaid, housing aid, unemployment insurance beyond the model's own, Social Security and state programmes are not in it.
- The history check (`v5-34-history-check.md`) found that the model's safety net absorbs almost none of a recession's rise in poverty (0.48%, against 73% in the data). In a downturn, "today's US policy" in the model is weaker than the real one. That matters most for the Adverse and Stress Test environments, which have recessions.
- All figures are what the model's assumptions imply, not a forecast. The model has not yet been reviewed by an independent economist.

## 7. How to reproduce

Panels: `node harness.js testbed 500 release ENV --v54 --snab --slope [--years=40]` for ENV ref, adv, st (or the resumable job `dev/tools/s165_jobs.sh`), then `python3 dev/tools/merge_panel.py`, `python3 dev/tools/merge_panel.py 40`, `python3 dev/tools/backing_chart.py`, `python3 dev/tools/release_data.py`. The rule's own effect: `node dev/tools/snap_rule_check.js --on --slope --env=ENV --seeds=500 --years=20|40`.
