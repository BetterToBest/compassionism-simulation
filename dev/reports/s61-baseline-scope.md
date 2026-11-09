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

## Results

(Filled from the pilot below.)

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
