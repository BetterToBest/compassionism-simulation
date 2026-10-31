# Who receives the Basic Units, and do they cover basic needs? (C2.2 coverage and adequacy)

Oct 31, 2026 · S6 · Claude · engine switch `C22` (study row option `c22`), off by default · preregistration: research-update `prereg/2026-11-c22-coverage-adequacy.md`

## Why this step

NEEC, the normative evaluation that scores economic systems against fixed criteria, has a criterion called C2.2, "Labor Non-Necessity". It passes a system that gives "unconditional provision covering 100% of basic needs (housing, food, healthcare, utilities) for all residents". NEEC's adjudication (its decision 83.8, ledger D65) reads Compassionism at 0.5 on C2.2, not 1.0, for two reasons:

1. **Coverage.** The draft Act pays "every citizen and legal resident 18 years or older", not all residents.
2. **Adequacy.** The design's own accounting has essentials paid partly in ordinary money, and the published model leaves adults below their cost of living.

This step asks what the design says, what the model does, and what changing the design would do. Changing the design (who receives the BU, and how much) is Duke's decision. Choosing how to model each option is Claude's.

## What the design says (Claude's reading of the design)

- **The draft Act, section 102** (Integrated Implementation Roadmap, Appendix A): "Every citizen and legal resident 18 years or older shall receive 1,200 basic units monthly. Distribution shall be automatic through Treasury Direct Deposit or physical cards. ... No means testing or work requirements apply."
- **The Optimal Transfer Design paper** calls the BU "distributed universally as opt-in basic income" and writes the distribution as going "to all participants".
- **Children.** Duke chose a child allowance of a quarter of the adult BU for each child, and said the Act's text should be updated to include it (v5.3, `dev/reports/v5-14-households.md`). The Act on the Hub still says 18 or older.
- **What the BU buys** (section 103 and the glossary): housing, food, transport, healthcare, education and PTF services. That covers C2.2's four needs: utilities are part of housing in the model's cost-of-living data (MIT).

So the texts disagree on one point: the Act says distribution is automatic, while the transfer paper says opt-in. On the other two points they agree: the BU goes only to citizens and legal residents, and its level is $1,200 a month.

## What the model does today (release v5.6)

- **Only participants receive the BU.** At the start, 78% of adults take part in Reference and Adverse, and 40% in the Stress Test. Each adult's cost of taking part is inferred so that exactly those adults join at the start (`dev/reports/04-joining.md`). After that, adults join or leave each year as the BU's value to them changes. Non-participants receive nothing, but they face the price rises the programme causes.
- **Nobody is excluded by legal status.** The simulated adults stand for all US adults, and every one of them can join.
- **Children:** a quarter of the adult BU for each child, paid to the household.
- **Level:** $1,200 a month. It rises with prices only in a year when prices rise more than 5%.

## The gaps, in numbers that need no simulation

- **Adequacy for one adult.** C2.2's four needs (food, housing with utilities, medical care) are 43.47% of MIT's 2026 cost of living for a single adult: $21,461 a year, or **$1,788 a month**. The BU of $1,200 pays for **67%** of them, for an adult with no other income, at reference prices. The calculation is `c22NeedsBU()` in the engine: `CFG.LIVING_WAGE_ANNUAL` × (food + housing + medical shares) / 12.
- **Status.** Unauthorized immigrants were 4.1% of the US population and 5.6% of its workforce in 2023 (Pew Research Center, "U.S. Unauthorized Immigrant Population Reached a Record 14 Million in 2023", Aug 21, 2025, opened). Their share of adults lies between these two figures, because the group includes few children. Pew counts temporary visa holders (students, guest workers) as lawful. The Act's "legal resident" may or may not include them.
- **Opt-in.** In the model, 22% of adults (60% in the Stress Test) start outside the programme and receive no BU.

## What the switch models (all off by default; switch off is bit-identical)

| Option | Row option | What it does |
|---|---|---|
| The Act's status rule | `c22: {u: 0.041}` (swept 0.056) | A share u of households is not eligible: their adults never receive the BU, cannot join, and are skipped by emergency enrolment. Everything else about them is unchanged. Drawn once per household on its own random stream. |
| Automatic distribution | `c22: {auto: true}` | Every eligible adult receives the BU from year 0, and nobody leaves (taking part costs nothing). |
| BU at the C2.2 needs level | `p.bu = c22NeedsBU()` ($1,788.43) | The BU set to a single adult's four needs at reference prices. |
| BU indexed to the needs | `c22: {idx: 'needs'}` | The BU rises every year with the price of the four needs, instead of only in years with more than 5% inflation. |

**Reported** (reporting only, no random draw): the share of adult-years in which the BU an adult receives covers the four needs at market prices (`c22PY`); the mean share covered, capped at 100% (`c22R`); the share of adult-years receiving any BU (`buPY`); and, for adults who are not eligible, their share of years below the cost of living, their share with too little wealth at the end, and their mean real resources (`elF0`, `elW`, `elRes`). With the status rule also set on the no-programme row, the same adults are found there, because the draw does not depend on the row. A unit test checks that this changes nothing in that row.

## Modelling choices (Claude's; recorded in `dev/DECISIONS.md`, S6)

- **Coverage is measured at market prices.** The PTF and PTH price cuts go only to members who pay in, so they are not unconditional provision. Counting them would raise the coverage figures.
- **Status is drawn by household.** All adults in a household share one status. Mixed-status families exist (Pew: 4.6 million US-born children lived with an unauthorized parent in 2023), so this is a limit.
- **"Automatic" means the BU's receipt does not wait on a choice.** In the model, joining also brings octaves and conversion. With `auto` every eligible adult is in, as in the existing "taking part costs nothing" row, but from year 0 instead of year 1.

## Limits

- One US-average cost-of-living line. Local costs vary a great deal (S14 builds a population-weighted line).
- MIT's medical budget assumes employer coverage. An adult without it pays more, so the four needs are understated for such adults.
- Under ageing (off in these rows), adults who enter later are all eligible.
- Temporary visa holders are not modelled separately from the status share.

## What the pilot shows (PILOT: 100 seeds, 500 adults; not headline figures)

The figures come from compassionism-sim-results `pilot-k-395dd5b` (engine 395dd5b), analysed by `dev/tools/c22_pilot.py`. All tables, with 95% intervals for every cell, are in `dev/runs/c22-pilot/tables.md` and `estimates.csv`. There are twelve cells: three environments, 20 and 40 years, and two wage yardsticks. Below, "headline" means Reference, 20 years, CPS earnings. Every interval quoted excludes zero unless it says otherwise.

An earlier run (`pilot-k-3e79adb`) stays published. A rounding error understated one measure in the five needs-level rows (preregistration amendment 1; engine pull request 54). Every other measure is identical, seed by seed, between the two runs.

### 1. Coverage: who receives the BU

| Design | Adult-years receiving the BU | Adult-years in which the BU covers housing, food and medical care | Mean share of those needs covered |
|---|---|---|---|
| As released (opt-in, everyone eligible, $1,200) | 83% (Stress Test: 43%) | **0%** | 65% (Stress Test: 26%) |
| The Act as written (automatic; citizens and legal residents) | 96% | **0%** | 75% (Stress Test: 56%) |
| Automatic, all residents, BU at the needs level and indexed to them (the "C2.2 design") | **100%** | **95%** | 99% |
| The same, with a child allowance of half the adult BU | 100% | 97% | 100% |

- **Coverage closes (rule 1)** only when distribution is automatic and nobody is excluded by status.
- **Adequacy does not close in any row (rule 2).** Even the C2.2 design leaves 5% of adult-years uncovered (3% with the larger child allowance). These are all single parents: one seed's check found every single adult covered, every two-adult household covered, and single parents at 77% to 85% of their needs. A child allowance of a quarter of the adult BU is less than a child's share of housing, food and medical care.

### 2. The adults the Act's status rule leaves out are made worse off by the programme (rule 3)
Under every status row, in all 12 cells, the adults left out end with too little wealth far more often than the same adults with no programme: **8 to 53 points more**. Their real resources are $500 to $5,200 a year lower. Their share of years below the cost of living is about the same (headline: −0.0 points, interval −0.4 to 0.4) or higher, by up to 8 points (in Adverse and Stress, and under the released yardstick). The reason is that they bear the programme's price rises and receive none of the BU.

The same holds, less starkly, for adults who choose not to take part in the opt-in design. In the headline cell, 25% of non-participants end with too little wealth, and 17% of their years are below the cost of living.

### 3. Each option against the release row (rule 4; better = fewer adults below the cost of living AND fewer with too little wealth)

| Option | Label in the 12 cells | Fewer adult-years below the cost of living (points) | Fewer adults with too little wealth (points) | Extra cost ($ per adult-year) |
|---|---|---|---|---|
| Status rule 4.1% (5.6%) | worse in 12 | −0.3 to −1.3 (−0.4 to −1.8) | −0.5 to +0.6 | −390 to −1,140 |
| Automatic, all residents | better 5, mixed 1, worse 6 | 2.2 to 16.0 | −8.8 to +2.1 | 3,760 to 12,780 |
| The Act as written | better 5, mixed 2, worse 5 | 1.5 to 14.9 | −8.5 to +1.7 | 2,770 to 11,890 |
| BU $1,500 | better in 12 | 2.6 to 12.7 | 1.3 to 9.4 | 6,620 to 8,970 |
| BU at the needs level, indexed as released | better in 12 | 3.9 to 21.6 | 6.7 to 27.4 | 10,750 to 19,350 |
| BU at the needs level, needs-indexed | better in 12 | 4.4 to 23.5 | 7.3 to 33.6 | 10,900 to 21,970 |
| **The C2.2 design** | **better in 12** | **7.0 to 51.1** | **2.9 to 44.7** | **23,660 to 38,720** |
| The C2.2 design with the status rule | better in 12 | 6.0 to 48.4 | 3.1 to 42.6 | 21,840 to 36,940 |
| The C2.2 design, child allowance half | better in 12 | 7.4 to 55.9 | 8.0 to 59.1 | 30,020 to 44,110 |

Automatic distribution on its own is not a clear gain. More people receive the BU and fewer are below the cost of living. But prices rise faster, and in the Adverse and Stress Test environments more adults end with too little wealth. Raising the BU's level is a gain in every cell, on both measures. This pilot does not break down why; the full report (S48) will.

**Headline cell, against no programme:**

| | Fewer adult-years below the cost of living | Fewer adults with too little wealth | Programme cost per adult-year | Children: fewer child-years below the cost of living |
|---|---|---|---|---|
| As released | 17.1 points | 3.8 | $32,583 | 27.2 |
| The Act as written | 18.8 | 5.3 | $36,286 | 26.8 |
| The C2.2 design | 25.4 | 19.8 | $61,278 | 38.6 |
| The C2.2 design, child allowance half | 26.0 | 20.2 | $68,213 | 41.5 |

**Cost and prices.** The C2.2 design costs about $28,700 more per adult-year than the release row in the headline cell, close to doubling the programme's cost. The model's price level rises far faster with every programme row: by year 20 it is about 200 times its starting level with the release row, and about 440 times with the C2.2 design (headline cell; `plv_19`). The released model already has prices rising 23-51% a year under the Source's financing (`dev/reports/04-joining.md`). The shares below a line, and the costs in year-0 dollars, already take the price level into account.

## What this means for C2.2 (Claude's reading; the design choice is Duke's)
1. **As written, the design does not meet C2.2.** Its BU covers about two-thirds of a single adult's basic needs, and it is limited by status (and, in one paper, by opting in). NEEC's 0.5 reading is supported by the model.
2. **Covering everyone is not enough on its own.** Automatic distribution to all residents reaches everyone, but the BU still covers the needs in no adult-year at $1,200.
3. **A BU set at the needs level, indexed to them, and paid automatically to all residents comes close:** 95% of adult-years. It is better than the release row in every cell, at roughly twice the cost.
4. **Single parents remain the gap.** Closing it needs a child allowance at a child's share of the needs. That row is not in this study and would be a new preregistered row.
5. **Leaving people out of a programme that raises prices harms them.** This holds for the status rule and for opting out. It bears on C2.2's "for all residents" and on NEEC's harm criteria.

Which option the design adopts goes to Duke as a ledger decision. The full 500-seed rows join the S48 batch after the S47 design freeze.
