# Outside-style audit of the engine before the design freeze

Oct 31, 2026 (research-update step S13, first pass). Before the full study batch is frozen (step S47), the engine was audited the way an outsider would: a reviewer that had not seen the code read ODD.md and MODEL_SPEC.md first, wrote down about 36 checkable expectations, then checked the engine (`index.html`, the block between the `RELEASE ENGINE` markers) against them, running the code where a finding mattered. Claude then checked every finding again against the code and the published data. This note says what was found, what was fixed (behind a switch, so no released figure moves), what the frozen batch should do about it, and what is wording.

Every released figure is unchanged: the corrections are a new switch, off by default (guard test identical; engine lineage proof recorded).

## The short answers

- **No error in the accounting, the random-draw guarantee or the estimands.** Exactly eight draws per adult-year in both runs and all three environments; the construction stream, recession stream, price step, conversion, project pool, ESP payroll, surplus split, spending rule, wealth floor and every reported measure match the specification (list at the end).
- **Two small bugs, now fixable by a switch.** (E3) The BLEI test that gives a wage bonus reads this year's dollars against a fixed $68.33 a day, so under the programme's inflation almost everyone passes it; every reported BLEI figure is in year-0 prices. (E4) The income-graded spending rule reads income before conversion pay is added, so some participants whose cash income covers their costs are still made to spend less. A third, (E7), the financial-stability score behind octave advancement is in this year's dollars against a constant set in year-0 dollars. Together they move the release row's effect by a few tenths of a point on basket poverty and 0.6 to 0.8 points on basic living; the direction of every headline result is unchanged (table below).
- **One unstated assumption with a large effect (E5).** In Adverse and Stress the cost of living rises 2% a year, but wages do not follow it: they follow only the programme's own price rise. Letting wages follow outside inflation too cuts the no-programme run's basket poverty in Adverse from 66% to 52% and shrinks the programme's "too little wealth" penalty there by about a third. The changelog put the fall in real wages down to automation and recessions only. This is now a labelled reading (switch `AUD.wOut`); S47 should run it.
- **One assumption the headline depends on that was never varied (E6), and it matters most.** Wages keep up in full, within the year, with the programme's own price rise (about 51% a year in Reference). At 95% indexation the fall in basket poverty shrinks from 30 to 22 points; at 75% the programme raises basket poverty in every economy. Without the programme's inflation (the every-dollar-backed reading) the condition hardly matters. S47 must sweep it.
- **The specification documents describe an older model (E1).** MODEL_SPEC.md describes v5.3 and ODD.md v5.2; the published panel is v5.4 with today's safety net. S47 must write the frozen batch's model into MODEL_SPEC.md; S7 brings both documents to the release.
- **The study page's "What would have to be true" panel (a named audit item) overstated two things and left out three conditions.** It said BLEI poverty falls; in Stress it rises. It said two constants have no source, which reads as if all others had one. Corrected this session (section 4).

## 1. Corrections behind a switch (`AUD`, row option `au`)

`AUD` is null as released. A study row gets the three corrections with `au: true`, or chosen parts with an object, for example `au: {gate: true}`. Parts:

| Part | What it changes | Finding |
|---|---|---|
| `gate` | The BLEI test for the wage bonus, and the PTF adoption term that reads the same BLEI, divided by the year's price level (the same deflator every reported BLEI figure uses). | E3 |
| `sg` | Income-graded spending applied once the year's cash income is known: wages, Social Security, cash grants, unemployment insurance, the safety net or the testbed's transfers less its contribution, and conversion income (projects, business payouts, the ESP premium). | E4 |
| `fbs` | The financial-stability score that drives octave advancement (framework conversion) divided by the year's price level. | E7 |
| `wOut` | A reading, not a correction, and not in `au: true`: wages also follow the environment's outside inflation (2% a year in Adverse and Stress), added to wage growth the way the programme's price rise is. | E5 |

No part makes a random draw. With `au: {}` (no part on) the output equals the released row exactly.

### What the corrections change (50 paired seeds, the published v5.4 pair with today's safety net)

Each cell: no programme / programme / difference, in percentage points of adult-years (too little wealth: of adults at year 20). "fix" is `au: true`; "fixW" adds `wOut`. Probe: research-update session S13, the panel pair built as `node harness.js testbed 500 release ref,adv,st --v54 --snab --slope` builds it; 50 seeds, so read the differences between settings, not the levels.

**Reference**

| Setting | Below the cost of living | Below 30 days (BLEI) | Below 30 days, same rules | Too little wealth | Programme inflation a year | Cost per adult-year |
|---|---|---|---|---|---|---|
| as released | 49.5 / 19.5 / -29.97 | 26.5 / 11.6 / -14.88 | 26.5 / 13.9 / -12.57 | 32.8 / 44.1 / +11.30 | 51.0% | $29,896 |
| gate | 49.5 / 19.7 / -29.77 | 26.5 / 11.7 / -14.75 | 26.5 / 14.1 / -12.39 | 32.8 / 44.3 / +11.52 | 51.0% | $29,914 |
| sg | 49.5 / 19.5 / -29.95 | 26.5 / 12.1 / -14.40 | 26.5 / 14.9 / -11.56 | 32.8 / 44.6 / +11.87 | 51.0% | $29,893 |
| fbs | 49.5 / 19.6 / -29.84 | 26.5 / 11.7 / -14.78 | 26.5 / 14.0 / -12.46 | 32.8 / 44.1 / +11.29 | 50.9% | $29,837 |
| fix | 49.5 / 19.9 / -29.61 | 26.5 / 12.3 / -14.18 | 26.5 / 15.3 / -11.22 | 32.8 / 44.8 / +12.08 | 51.0% | $29,853 |
| wOut | identical to as released (Reference has no outside inflation) | | | | | |

**Adverse**

| Setting | Below the cost of living | Below 30 days (BLEI) | Below 30 days, same rules | Too little wealth | Programme inflation a year | Cost per adult-year |
|---|---|---|---|---|---|---|
| as released | 66.3 / 31.0 / -35.23 | 31.3 / 17.4 / -13.97 | 31.3 / 23.3 / -8.05 | 45.0 / 81.3 / +36.30 | 61.1% | $28,487 |
| fix | 66.3 / 31.4 / -34.92 | 31.4 / 18.3 / -13.05 | 31.4 / 25.6 / -5.75 | 45.0 / 81.9 / +36.83 | 61.1% | $28,449 |
| wOut | 51.7 / 23.3 / -28.45 | 27.6 / 13.7 / -13.96 | 27.6 / 17.0 / -10.62 | 36.3 / 61.7 / +25.43 | 53.8% | $29,226 |
| fix + wOut | 51.8 / 23.7 / -28.11 | 27.6 / 14.4 / -13.23 | 27.6 / 18.7 / -8.90 | 36.3 / 62.5 / +26.17 | 53.8% | $29,187 |

**Stress**

| Setting | Below the cost of living | Below 30 days (BLEI) | Below 30 days, same rules | Too little wealth | Programme inflation a year | Cost per adult-year |
|---|---|---|---|---|---|---|
| as released | 66.3 / 52.9 / -13.42 | 31.3 / 35.2 / +3.90 | 31.3 / 37.1 / +5.80 | 45.0 / 76.5 / +31.47 | 27.7% | $11,776 |
| fix | 66.3 / 53.0 / -13.24 | 31.4 / 36.0 / +4.69 | 31.4 / 38.0 / +6.68 | 45.0 / 78.3 / +33.27 | 27.7% | $11,793 |
| wOut | 51.7 / 42.1 / -9.67 | 27.6 / 28.3 / +0.71 | 27.6 / 29.9 / +2.28 | 36.3 / 57.1 / +20.83 | 23.6% | $11,982 |
| fix + wOut | 51.8 / 42.3 / -9.42 | 27.6 / 28.9 / +1.26 | 27.6 / 30.6 / +2.93 | 36.3 / 58.3 / +21.96 | 23.6% | $11,995 |

The gate correction also moves the no-programme run very slightly in Adverse and Stress (66.28 to 66.29): there too the wage bonus's BLEI test was read in nominal dollars, against 2% outside inflation. The `sg` part leaves the no-programme run unchanged, as it should (it has no conversion income).

**Recommendation to S47** (Claude's choice, recorded in `dev/DECISIONS.md`): the frozen batch's main rows carry `au: true`, since the three parts correct the model to its own specification, and the as-released row is kept beside them for continuity with v5.6. `wOut` runs as a sensitivity reading on the release pair in Adverse and Stress (study A rows, 500 adults, 20 and 40 years). Both are dated amendments to the study programme at the freeze.

## 2. Findings, one by one

Classes: **bug** (the code does not do what its specification says), **assumption** (the code does something the specification does not say, which matters), **drift** (the documents describe an older model), **wording**.

| # | Class | Finding | Checked | Action |
|---|---|---|---|---|
| E1 | drift | MODEL_SPEC.md describes v5.3, ODD.md v5.2; the panel is v5.4 plus today's safety net. Not described: automation works through job loss (the wage drag is off in v5.4); PTH appreciation capped at the price rise plus 2%; PTH and PTF members leave each year (6.2% and 3.2%); SNAP, the EITC and the refundable CTC with SNAP's work rule in both runs. TESTBED_SPEC.md lacks the switches added since S34 (`DEBT_READ`, `COMM`, `C22`, `LW`, the CPS earnings reading). | Yes (code and `_meta.command` of the embedded panel). | S47: write the frozen batch's model into MODEL_SPEC.md and list every switch in TESTBED_SPEC.md. S7: ODD.md to the release. |
| E2 | assumption | The release row charges every earner a flat contribution on wages (about 2.8% in Reference, 3.5% Adverse, 1.6% Stress; the published rows' `tau`), which pays for the PTF and PTH price cuts and the cash part of PTH appreciation. The no-programme run pays nothing. MODEL_SPEC.md says the release row has no testbed cash flows. | Yes (code; the published `tau`). | A modelling reading of who pays for the price cuts; it must be written into MODEL_SPEC.md (S47) and stated on the page (S25/S40). Not a design change. |
| E3 | bug | The BLEI gate on the wage bonus (and the PTF adoption term) compares this year's dollars with the fixed $68.33 a day. By years 15-19 every participant passes it; in year-0 prices about 81% would. | Yes. | `AUD.gate`. |
| E4 | bug | Income-graded spending reads income before conversion pay, business payouts and the testbed's transfers are added; 2-5% of participant-years are made to spend less although their cash income covers their cost. The rule's own reasoning (spending follows income, the CE survey's elasticity) applies to all cash income. | Yes (code; the 50-seed table). | `AUD.sg`. |
| E5 | assumption | Wages follow only the programme's price level; the cost of living, BU indexation and project pay also follow the environment's 2% outside inflation. About half the Adverse "too little wealth" penalty, and much of Adverse's no-programme poverty, comes from this. The changelog's sentence on falling real wages names only automation and recessions. | Yes (50-seed table). | Reading `AUD.wOut`; S47 runs it; S47/S7 state it in MODEL_SPEC.md 6.1 and correct the changelog's limits sentence at the next release. |
| E6 | assumption | The release assumes wages follow the programme's price rise in full, within the year (`PRICE.wIdx` = 1). Never varied in the sensitivity study. | See section E6 below. | S47: sweep `wIdx` (a study option, no engine change); the panel now names the condition. |
| E7 | bug (small) and calibration | Octave advancement uses nominal dollars against a constant set in year-0 dollars; even deflated, 89% of participants reach the top octave by year 9. Conversion pay is about half the programme's cost, so this ladder drives cost. | Yes (reviewer's probe; the `fbs` row of the table). | `AUD.fbs`. The saturation itself is an open calibration: S47 should run the existing FBS50 reading (row `fbs50`) beside the release row. |
| E8 | wording | "2.2 points a year from year 15" in the automation drag can never act: the 10-point cap binds from year 13 (and the drag is off in v5.4). | Yes (arithmetic). | Drop from MODEL_SPEC.md A1 and ODD.md 6 (S47). |
| E9 | wording | The wage median is exp(3.5) = 33.1 SIU = $39,945, not "35 SIU"; the taper's pivot (35 SIU) is the CPS median. | Yes. | MODEL_SPEC.md 3 (S47). |
| E10 | wording | The recession stream's draw count varies (gamma's rejection loop), not "1-3 a year"; no recession starts in the year one ends. Its own stream, so harmless. | Reading. | MODEL_SPEC.md 8 (S47). |
| E11 | wording | Essentials prices can fall below 1 when demand is under capacity (no-programme price level about 0.994). | Reviewer's probe. | Document (S47). |
| E12 | wording | SZH's induction into PTF is open only to participants. | Reading. | MODEL_SPEC.md 6.10 (S47). |
| E13 | wording | The hours measure includes project hours. | Reading. | MODEL_SPEC.md 9 (S47). |
| E14 | wording | Businesses convert 80% of the BU they accept at 3x; 20% is ESP payroll. ODD.md says "3x on all BU accepted". | Reading. | ODD.md 6 (S47). |
| E15 | wording | One of the eight yearly draws (the BU spending share) is drawn but unused on the release path; kept so the draw count and pairing hold. | Reading. | Say so in ODD.md (S47). |
| E16 | wording | "a = 0: none backed" is not exact: matched output (about 7.7% of the Source's payout in Reference) is still treated as backed. | Reviewer's probe. | MODEL_SPEC.md 6.12 and the panel's inflation row (done, section 4). |
| E17 | calibration (low confidence) | The 0.593 share of cash surplus spent was derived on the v5.1-era adults-only run, not re-derived for the v5.3/v5.4 no-programme run. | Not confirmed (a rough check only). | S47: re-run its derivation, by its stated method, on the current no-programme run; if it moves, a dated amendment (re-deriving a constant by its own method is not tuning). |
| E18 | wording | The non-finite wealth floor tests NaN only, not Infinity (never occurs). | Reading. | MODEL_SPEC.md B1 (S47). |

### E6: wages that keep up only in part

The release assumes that every wage rises each year by the full rise in the programme's own price level (`PRICE.wIdx` = 1), on top of ordinary wage growth. The programme's price level rises about 51% a year in Reference (61% Adverse, 28% Stress). So the model asks wages to keep up, within the year, with very high inflation. The sensitivity study never varied this. Run here on 20 paired seeds (the same pair as the table above, as released otherwise; `wIdx` is an existing study option):

| Wage indexation | Reference: below the cost of living (none / programme) | Reference: too little wealth | Reference: programme inflation a year | Adverse: below the cost of living | Stress: below the cost of living |
|---|---|---|---|---|---|
| 100% (as released) | 50.2 / 20.0 | 33.0 / 45.0 | 51% | 67.6 / 31.9 | 67.6 / 53.9 |
| 95% | 50.2 / 28.0 | 33.0 / 74.8 | 59% | 67.6 / 43.0 | 67.6 / 59.6 |
| 90% | 50.2 / 39.7 | 33.0 / 92.9 | 69% | 67.6 / 54.5 | 67.6 / 65.4 |
| 75% | 50.2 / 69.4 | 33.0 / 100.0 | 161% | 67.6 / 74.4 | 67.6 / 77.9 |

Below full indexation, wages fall behind the programme's prices, the price rise feeds on itself, and the gain shrinks fast: at 95% the fall in basket poverty in Reference is 22 points instead of 30; at 90% it is 11 and in Stress almost nothing; at 75% the programme raises basket poverty in every economy. The headline result "basket poverty falls" therefore holds only if wages keep up in full with the programme's own inflation, or if that inflation does not happen (in the every-dollar-backed reading it almost vanishes, and then indexation hardly matters). This is the single most important condition this audit found. It is now named in the study page's panel, and S47 must sweep it (100%, 95%, 90%, 75%) beside the backing readings, so that the batch reports the result across both.

## 3. What the frozen batch should add (S47)
1. `au: true` on the main rows, the as-released row beside them (E3, E4, E7).
2. `wOut` as a sensitivity reading in Adverse and Stress (E5).
3. A `wIdx` sweep (E6).
4. The FBS50 reading beside the release row (E7).
5. The 0.593 spending share re-derived on the current no-programme run (E17).
6. MODEL_SPEC.md written for the frozen model, including the contribution (E2), and TESTBED_SPEC.md listing every switch (E1).
7. From the Grok audit's triage (research-update `audits/grok-i5-triage.md`): the middle and every-dollar-backed readings of the release pair.

## 4. The "What would have to be true (Claude's reading)" panel on the study page

The panel (study page, from `dev/tools/study_data.py` into `data/studies/s137.json`) was a named item for this audit. Checked against the study file and the published panel:

- **BLEI poverty does not fall in Stress.** The study file has +3.3 points in Stress (the release panel: 35.3% against 31.6%). The row now says "falls in Reference and Adverse; in Stress it rises", and names the condition that the design's own BLEI (which credits participants with a month of BU and a larger share of wages) is the right yardstick; the same-rules fall is smaller.
- **"Too little wealth rises" left out its deciding condition:** savings earn nothing while prices rise. In the published reading where savings keep up with prices it falls instead, in every economy (by 20, 23 and 9 points). Added.
- **Cost:** about half the cost is conversion pay, which depends on the business conversion rate (3x, a placeholder) and on how fast people climb the octaves; the study varied neither. The row said cost was "mostly" participation times the BU amount. Corrected.
- **Programme inflation:** its size is set by the backing reading (none of the payout backed beyond matched output) and full pass-through into prices, neither varied in the study; in the every-dollar-backed reading it almost vanishes. Added.
- **Basket poverty:** the condition on wage indexation (E6) is added.
- **"Two constants with no source"** read as if every other constant were sourced. Many constants the released figures use are design choices or placeholders, labelled in ODD.md section 6; the lead now says so, and the table's title says the two are not used by the released figures. The evidence check (4 seeds, 8 years, Adverse) is now described as small, with the code reading that supports it.
- **The damping constant** was described as "applied to the overall inflation rate". The code multiplies only the environment's outside inflation (zero in Reference), never the programme's. This wording was chosen in an earlier session from Claude's reading of the code (recorded with Duke's clarity answers, d201 and d213); the reading was wrong, and the wording is corrected to "the outside inflation rate". Flagged for Duke's reading.

## 5. Checked and consistent with the specification
Construction stream and its draw order; automation risk by exact inverse CDF; quality and lambda; exactly 8.0000 main-stream draws per adult-year in both runs, all three environments; recession probability, length and multiplier; basket shares; the spending layer (recession years only); PTF capacity; open enrolment's revealed cost; the project pool, rates and willingness test; ESP payroll; the surplus split; business conversion with next-year premium; conversion rate and progressive tax; wage growth (base 1%, BLEI bonus taper, CIP, the 80% floor, octave raise off); PTF and PTH cuts and forgone profit; BU purchases and expiry; the labour response; the spending rule (0.593 of cash surplus); the wealth floor; the price step and the COLA ratchet; damping off on the release path; every estimand (basket poverty and depth, too little wealth, the official line at Year 7, Gini with n/(n-1), inflation, cost, the interval); the no-programme run's own inflation; the accounting check bit-identical.

## Limits of this audit
One reviewer, from the documents and the code; the single-payer health rows were not audited. Probe figures are 50 seeds (the reviewer's own, 2-4 seeds, are indicative only). The second audit pass, on the release itself, comes after S7.
