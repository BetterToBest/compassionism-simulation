# Who the "no programme" people are: adults outside the labour force, and how households below their budget borrow (S61)

Built Nov 9, 2026. Preregistration: research-update `prereg/2026-11-s61-baseline-scope.md` (the criterion for choosing a spending rule was fixed there before anything was built; Amendment 1 lists the small choices made while building). Choices: `dev/DECISIONS.md`, S61. Tables: `dev/runs/s61-scope/tables.md`. This is a **pilot** at 100 seeds: round 2 runs nothing at 500 seeds before its freeze (S63).

## Why this matters

Every result compares Compassionism with "no programme" on the same simulated people. S34 found two ways in which those people differ from Americans that matter for the next round of results:

1. **Everyone works.** In the model every adult aged 25-64 is in the labour force. In the US, 19.4% of adults that age did not work at all in 2025, and 17.3% gave a reason outside the labour market: illness or disability (5.8%), retirement (4.1%), caring for home or family (6.3%), school (1.1%) (Census Bureau, CPS ASEC 2026). These adults are among the poorest: about a third of those out for disability or school are below the official poverty line, against 4.6% of adults in the labour force.
2. **Households below their budget slide into debt.** A household whose income is below its living-wage budget spends less than the budget but more than its income, every year, with no limit until the debt floor (−$10,000), where the rest is written off. So families in debt rise over 20 years far beyond the survey's figure.

The outside reviews (research-update `audits/2026-11-s39-s55-review-triage.md`, D1-D2) asked for exactly these two fixes: spending above income only from savings or an explicit, limited borrowing channel (borrowing not set to zero), and adults outside the labour force with their own income, benefits and poverty measure.

## What was built (both off by default; with them off every published figure is unchanged)

**Borrowing for ordinary spending** (row option `dr`, S35's debt reading, extended). When the spending rule would have a household spend more than its cash income, the excess is paid from its savings at the start of the year and from a borrowing limit, and from nothing else; once both are used up, the household spends its income and the rest of its budget is cut.
- The **borrowing limit** is $2,500 in today's money, moved with prices: the median unsecured consumer debt (credit cards, other instalment loans, other debt) of families aged 25-64 in the bottom 40% of income who hold any, in the Federal Reserve's 2025 Survey of Consumer Finances. It is a design parameter (how much of a family's unsecured debt is room for ordinary spending), swept over $0 (S35's reading), $5,000, $8,700 and $10,000.
- The **liquid share** of savings that can pay for ordinary spending is 1 (the model has one wealth stock), with a reading at 0.046 (the survey's median of liquid assets over net worth).
- The **floor reading** applies the income-graded rule only to spending above the household's official poverty line: below the line, spending is the line; between the line and the budget, the graded rule applies to the part above the line. The borrowing limit applies on top.

**Adults outside the labour force** (row option `lf`). At the start, each adult is placed outside the labour force for the whole run with the CPS probability for the adult's household type and reason, and given its own yearly income drawn from the CPS distribution for that reason: Social Security (including disability insurance), SSI, other disability income, pensions, survivor and veterans' payments, public assistance, unemployment and workers' compensation, educational assistance, child support, help from outside the household. The income moves with prices, as Social Security's cost-of-living adjustment does. SNAP and tax credits come from the engine's safety net, as for everyone. These adults earn no wages, lose no job, do no paid programme work and are left out of the wage index: the engine's rules for a retired adult, reused.

## Claude's reading of the design (please check)

The Hub's Optimal Transfer Design paper distributes the Basic Unit "universally" (`dev/reports/c22-coverage-adequacy.md`, which read the papers for S6); nothing in the papers treats adults outside the labour force differently. So in the model they receive the Basic Unit and every price effect like anyone else. Where the papers are silent is whether they gain programme income through work. The engine treats them as it treats retirees: they may take part in conversion projects, giving up no wage. A reading with no conversion at all (`conv: 'none'`) is reported beside it. **Modelling assumption:** status is fixed for the run (nobody enters or leaves the labour force); bargaining power and the outside option, which could move people in or out, come in S60.

## Results (pilot: seeds 1-100, 500 adults, 20 years; engine `1d9ab84`; every figure in `dev/runs/s61-scope/tables.md`)

Every row is the frozen yardstick (the frozen engine, US earnings, today's safety net) plus the named reading. Figures are means over the 100 seeds.

### 1. Borrowing for ordinary spending: the limit changes how deep households fall, not how many fall into debt

| Families in debt (net worth below zero), Reference | Year 0 | Year 20 | Single parents, median net worth, Year 20 |
|---|---|---|---|
| US (SCF 2025, head 25-64 with wages) | 9.3% | (one year only) | $49,000 |
| Frozen yardstick (no limit; write-off at −$10,000) | 13.4% | 22.0% | −$1,400 |
| **Cap, limit $2,500 (recommended)** | 13.4% | 21.6% | $5,000 |
| Cap, limit $5,000 / $8,700 / $10,000 | 13.4% | 21.8% / 21.9% / 21.9% | $2,800 / −$300 / −$1,400 |
| Cap, limit $0 (S35's reading) | 9.9% | 12.3% | $7,100 |
| Cap, only 4.6% of savings available | 10.6% | 18.3% | $24,900 |
| Floor (graded only above the poverty line) + cap | 12.5% | 20.8% | $8,100 |

- Any positive limit lets a household below its budget cross zero, so the share in debt hardly moves (22.0% → 21.6-21.9%). What the limit changes is how far households fall and whether the floor writes their debt off: with the cap, a single parent's median net worth at Year 20 is +$5,000 instead of −$1,400, and spending that the released rule financed by a write-off is cut instead (the limit binds in about 58% of the year-decisions where spending is graded, with a mean cut of about $10,900 in today's dollars).
- Only a limit of zero (no borrowing at all, which the reviews called unrealistic) brings the figure near the survey's: 12.3%. The remaining gap at any positive limit is **open**: households below their budget in the model keep spending above their income every year, which the survey's 9.3% says real households do far less. A sourced reason for that (family help inside the household, deeper cuts, the timing of spending) is not in the model. The 9.3% is a check, not a target, and no constant was changed to approach it.
- Adverse and Stress tell the same story (Year 20: 30.5% frozen, 30.4% cap, 28.9% floor, 18.2% limit $0).
- None of the readings moves basket poverty or the cost-of-living measure (they compare income with the full budget, so a cut in spending is hardship, not relief); wealth poverty moves by at most 2.4 points (the liquid-share reading: 21.9% → 20.5% in Reference, 31.9% → 29.5% in Adverse and Stress; the floor reading: 21.9% → 21.4% in Reference, 31.9% → 31.0% in Adverse and Stress; the limit alone by less than 0.1).

**Recommendation to S63 (criterion C1-C3, fixed before the run):** the **cap reading with the $2,500 limit** for the main row. It is admissible (spending above income only from savings and the explicit limit; unit test), every constant is sourced or a labelled design parameter, and it has one fewer design choice than the floor reading. The floor reading, the limit sweep and the liquid-share reading go beside it.

### 2. Adults outside the labour force

| Reference, Year 0 | US | Frozen yardstick | With adults outside the labour force (`lf`) |
|---|---|---|---|
| Adults 25-64 with any earnings | 80.9% | 100.0% (gap) | 82.7% |
| Official poverty, adults | 8.5% | 3.3% (gap) | 11.5% |
| Official poverty, children | 13.4% | 6.1% (gap) | 14.5% |
| Official poverty, adults and children | 10.0% | 4.1% (gap) | 12.4% |
| Median household money income | $105,000 | $93,000 | $75,600 (gap) |
| Median family net worth | $185,600 | $162,300 | $159,300 |
| Families in debt (Year 20: 22.0% and 27.9%) | 9.3% | 13.4% (gap) | 14.3% (gap) |

- The switch does what it says: 17.3% of adults are outside the labour force (the CPS share), the share with earnings moves from 100% to 82.7% (the survey: 80.9%), and official poverty closes from well below the survey to somewhat above it.
- It overshoots poverty for the adults it adds. By reason, the model's official poverty at Year 0 against the CPS: disability 52% (35%), early retirement 28% (19%), care 44% (24%), school 63% (35%); adults in the labour force 4.7% (4.6%). The likely reason is scope (class "scope"): in the model a household is one or two adults and their children, so a student or a disabled adult living with parents or other relatives is a one-adult household with only its own income; in the survey their family's income counts. Household money income falls for the same reason (more one-adult households with low income). Not tuned; reported.
- They fall into debt more: 27.9% of families at Year 20 (27.7% with the cap).

### 3. Does the programme's effect depend on the reading? (criterion C4; pilot, not a result)

The C2.2 design against its own no-programme row, Reference, points (95% paired bootstrap interval):

| Reading | Basket poverty | Wealth poverty | Cost-of-living measure |
|---|---|---|---|
| Frozen yardstick | −24.6 [−25.0, −24.3] | +0.7 [+0.2, +1.1] | −28.2 [−28.7, −27.8] |
| Cap ($2,500) | −24.6 [−25.0, −24.3] | +0.7 [+0.3, +1.1] | −28.3 [−28.7, −27.8] |
| Floor + cap | −24.6 [−25.0, −24.3] | +1.1 [+0.7, +1.6] | −28.2 [−28.7, −27.8] |
| Adults outside the labour force | −31.4 [−31.8, −31.0] | +9.8 [+9.4, +10.3] | −34.9 [−35.4, −34.5] |
| Adults outside the labour force + cap | −31.4 [−31.8, −31.0] | +9.9 [+9.4, +10.4] | −35.0 [−35.4, −34.5] |

- No reading changes the sign of an effect or whether its interval excludes zero, in any environment, so C4 does not require S63 to carry two main rows.
- But adding adults outside the labour force changes the size of the programme's effects a great deal. The basket-poverty gain is larger (−31.4 against −24.6 points: more people start below the cost of living and the Basic Unit reaches them), and so is the wealth-poverty **harm**: +9.8 points against +0.7 in Reference (Adverse +35.4 against +30.2; Stress +45.0 against +41.7). A likely mechanism, not yet traced: adults with no wages cannot rebuild savings that the programme's inflation erodes. **For S63:** carry `lf` on and off beside each other whatever the main row, and trace the wealth-poverty harm before any headline uses it.
- With no conversion income for these adults (`conv: 'none'`), the no-programme figures are identical (as they must be); the programme effect under that reading is for S63's rows.

## What S63 must carry from this step
1. Main-row candidates: the cap reading at $2,500 (recommended) and `lf` (recommended under decision rule 3: its tests pass and it moves the share with earnings to the CPS figure). Which readings join the main row is S63's ledger decision.
2. Beside them: the limit sweep ($0, $5,000, $8,700, $10,000), the liquid share 0.046, the floor reading, `lf` off, `conv: 'none'`.
3. A per-adult reporting key for basket poverty by labour-force reason (Q4; prereg Amendment 1 item 5).
4. The open gap on families in debt, and the wealth-poverty harm under `lf`, traced before any headline uses it.

## Limits

- Status is fixed for 20 years; real people move in and out of the labour force. No sourced transition rates were used in this step.
- Adults outside the labour force start with the same wealth distribution as workers (the survey's household draw), which overstates their wealth.
- "Single without children" includes adults who live with parents or roommates; the model gives each a one-adult budget, so a single adult with no own income looks poorer than one who shares a home.
- The model has one wealth stock: home equity and retirement accounts count as savings that can pay for ordinary spending (the liquid-share reading shows how much this matters).
- Help from family inside the household and informal borrowing are not modelled beyond the borrowing limit.

## Sources opened

- U.S. Census Bureau, Current Population Survey, 2026 Annual Social and Economic Supplement, public-use CSV (downloaded Nov 9, 2026; `sources/lf_scope.py`, output `sources/lf_scope.json`).
- Federal Reserve, 2025 Survey of Consumer Finances, summary extract (downloaded Nov 9, 2026; `sources/s61_borrowing.py`, output `sources/s61_borrowing.json`).
- U.S. Census Bureau, poverty thresholds for 2025 (already in the engine, `CFG.HH_FPL`).

## Design parameters (labelled, with the ranges to sweep in S63)

| Parameter | Main value | Range | What it is |
|---|---|---|---|
| Borrowing limit for ordinary spending | $2,500 | $0, $5,000, $8,700, $10,000 | how much of a family's unsecured debt is room for ordinary spending |
| Liquid share of savings | 1 | 0.046 | how much of net worth can pay for ordinary spending |
| Floor | none (cap reading) | the official poverty line (floor reading) | the part of spending the graded rule does not cut |
| Conversion for adults outside the labour force | as retirees | none | whether they gain programme income through projects |
| Status | fixed for the run | (no sweep this step) | movement in and out of the labour force |

## Reproduce

From a clean checkout of the commit named in each output's `_meta.manifest`: `node dev/tools/s61_scope.js ENV 100 20` and `node dev/tools/s61_scope.js ENV 100 20 --prog --rows=F0,DC,DF,L,LC` for ENV in ref, adv, st; then `python3 dev/tools/s61_table.py`. Outside data: `python3 sources/lf_scope.py DATA_DIR` and `python3 sources/s61_borrowing.py DATA_DIR`. Unit tests: `node harness.js unit` (lfUnitSuite).
