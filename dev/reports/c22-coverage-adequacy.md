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

## What comes next

The preregistered pilot (100 seeds, all three environments) gives the figures beside each design option. Those figures are added here and go to Duke as a ledger decision. The full rows join the S48 batch after the S47 design freeze.
