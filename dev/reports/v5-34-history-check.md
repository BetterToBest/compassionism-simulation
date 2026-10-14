# The history check: the model through 2008-2012 and 2020 (ledger step s146)

Session 9, Oct 14, 2026; 500-seed figures added in session 10 (same day). **The figures below are from 500 seeds** (seeds 1-500, engine commit 5bf5bcc, clean tree), run on the study pod as one piece of the s165 study; the file is `dev/runs/history/history-check.json` (also in BetterToBest/compassionism-sim-results, folder `s165-5bf5bcc`). They replace the 20-seed smoke figures of session 9; the verdicts are copied exactly as the file gives them. The comparisons and their pass bands were fixed in `dev/plans/s146-history-check.md` (sections 4 and 8) and committed before the tool first ran.

**Read this first: changes, not levels.** The model's starting population is built from 2022 data (in 2025 dollars). So this check asks "how would a population like today's respond to a shock like 2008, or like 2020?", not "does the model reproduce 2007". Every figure below is a change: for the model, the shock run minus the same run without any recession (paired by seed); for the data, the change from the year before the shock. No constant was adjusted to fit the history (standing guardrail 5), and there is no target result.

## 1. The comparisons, with verdicts (500 seeds)

The model measure is the share of adults below the cost-of-living basket (basket poverty), with today's safety net unless the row says otherwise. Data: the official poverty rate, Columbia's historical supplemental rate (before and after taxes and transfers, to 2012), Census's supplemental rate (2009 on). The model's 2010 rise has a 90% range across seeds of +2.8 to +7.2 points, and its 2012 rise +4.4 to +9.4 (`history.log`).

| # | Comparison (fixed in advance) | Model (500 seeds) | Data | Verdict (500 seeds, from the file) |
|---|---|---|---|---|
| 1 | Poverty higher in 2009 and 2010 than in 2007 | +2.89 and +4.90 points | +1.8 and +2.6 (official) | matches |
| 2 | Rise at the peak between half and double the official rise (1.3 to 5.2) | +6.86 (peak in 2012), about 2.6 times the official rise | +2.6 (peak in 2010) | same direction, different size (bigger) |
| 3 | Peak within a year of 2010 | 2012 | 2010 | does not match |
| 4 | Share of the rise gone two years after the peak (no verdict) | outside the window (the peak is the last year) | 3.85% | reported |
| 5 | How much of the rise the safety net absorbs, 2007 to 2012 (within 20 points) | 0.48% (rise +6.90 without, +6.86 with) | 72.96% (before transfers +5.77, after +1.56) | same direction, different size; **in substance a miss** (see below) |
| 6 | 2020: poverty higher than in 2019, official-style (without SNAP and tax credits) | +1.53 | +1.0 (official) | matches |
| 7 | 2020, supplemental measure (no verdict) | +1.53 | −2.6 (Census) | reported |

**Comparison 5, plainly.** The file's verdict is "same direction, different size", and it is kept as the file gives it: the rule fixed before the run says zero or less is "does not match", and at 500 seeds the model's safety net absorbs a small positive share (0.48%), so the rule gives the milder label. In substance this is a miss: the model's safety net absorbs about half of one percent of the rise, the data's about 73%, a gap of more than 70 points against a band of 20. The 20-seed smoke run had said "does not match" (it absorbed −0.6%). Neither the rule nor the band was changed to make the label read better or worse.

**Changes from the 20-seed smoke figures:** comparison 1 +3.1/+5.3 became +2.89/+4.90; comparison 2 +7.2 became +6.86; comparison 5 about 0% became 0.48% (its label moved from "does not match" to "same direction, different size", as above); comparisons 6 and 7 +1.3 became +1.53. No other verdict changed.

## 2. What it says (plain words; checked against the 500-seed figures)

- **Direction: right.** A recession like 2008 and a shock like 2020 raise poverty in the model, as they did (comparisons 1 and 6 match).
- **Size: too big, and too late.** The model's rise at its peak, +6.86 points, is about 2.6 times the official rise of +2.6, outside the band of half to double. It keeps growing to 2012, when real median household income was at its lowest; the official rate stopped rising in 2010, when unemployment peaked, so the peak-year comparison (model 2012, data 2010) does not match. The model follows the income path it is given, so its timing follows income, not unemployment. The size partly reflects the line: the model's cost-of-living basket sits far higher than the official poverty line, where many more households sit close to it, so the same income loss moves more people across it.
- **The safety net absorbs almost none of the rise in the model (0.48%), against about three quarters in the data (73%).** This is the check's clearest miss. Three reasons, all in the model's design: (a) SNAP and the tax credits are paid on last year's income, so they arrive a year late; (b) the model's basket line is high, and benefits of a few thousand dollars rarely lift someone over it (they shrink the gap instead: see `v5-35-safety-net-poverty.md`); (c) the data's "before transfers" removes far more than the model's three programmes: Social Security, unemployment insurance, housing aid and the tax system. In the model, unemployment insurance is in both arms, and Social Security, housing aid and taxes do not respond to the shock.
- **2020:** the model, with the shock alone, rises +1.53 points against +1.0 official. The supplemental rate fell in 2020 because of stimulus payments and the weekly unemployment top-up, which the engine does not have (the plan's optional section 5 was not built; it is an invitation to whoever forks the repository).
- **What this means for the main results:** the model's response to a recession is in the right direction but too large and too slow, and its safety net cushions a downturn far less than the real one did. Comparisons of Compassionism against "today's safety net" in a recession should be read with that in mind: the model's baseline safety net is weaker in a downturn than the real one.

## 3. The scripted shock (rule (a), fixed before any run)

In each year after the base year, the income multiplier is that year's real median household income over the base year's: 0.966, 0.960, 0.937, 0.923, 0.923 for 2008-2012; 0.980, 0.976 for 2020-2021. The recession flag is on in every year below 1, so the engine's own recession job-loss rates apply; the engine then reduces the income cut by the extra job loss, so the year's whole loss is the median income's fall. In 2008, 2009, 2020 and 2021 the extra job loss alone is larger than the median income's fall, so the income cut is zero and only job loss acts (this is why 2020 and 2008 show the same model figures). The same path is used for every seed and both arms; no random draw is added. Outside inflation is the Reference Environment's own (none).

The engine change is one switch, `REC_SCRIPT` in `index.html` (null by default: every earlier figure is bit-identical, `guard_test.js` and `snap_rule_check.js`).

**One correction made after the 20-seed smoke test, stated openly:** the tool first labelled comparison 5 "same direction, different size" for an absorption of −0.6%. Absorbing none of the rise is not the data's direction, so the code now gives "does not match" for zero or less. No band, rule or comparison changed. At 500 seeds the absorption is +0.48%, above zero, so that rule does not apply and the file's label is "same direction, different size" (section 1 says why this is still a miss in substance).

## 4. Limits

- The start population is 2022-based: compare changes only.
- The data are outside data, not verified against Census, BLS or the Federal Reserve by this repository (`sources/history/README.md`). Seven supplemental-rate cells are disputed between the two data packs; one lies in the windows (65 and over, 2020, 0.1 point) and is not used here.
- The model's poverty line is the cost-of-living basket, not the official or supplemental threshold, so it compares changes in different lines.
- Columbia's before-transfers history exists only to 2012. The model's transfers are SNAP, the EITC and the refundable CTC; unemployment insurance is in both arms; Social Security, housing aid and taxes do not respond to the shock.
- The 2020 survey had pandemic non-response (Census puts the official rate about 0.5 point higher with it corrected).
- Each run is short (6 or 3 years), so long-run effects of the shock (for example on savings) are not seen.

## 5. How to reproduce

`node dev/tools/history_check.js --seeds=500` (about 3 minutes on one core; `--engine=DIR` runs another checkout's engine; output `dev/runs/history/history-check.json`). On the pod it runs as one piece of the s165 job (`dev/tools/s165_jobs.sh`, job `hist`).
