# What the programme costs the government, and what paying for it does (S72)

Nov 14, 2026. Pilot: seeds 1-100; frontier: seeds 1-20; 500 adults, 20 years, three environments, the candidate main row of round 2 in both runs (`r2MainRow`), engine `df9cfbe` (clean worktree; the frontier without the weighted tail ran on `c5db934`, the same engine). A pilot is a mechanism check, not a result; the frozen 500-seed batch decides. Preregistered before the build and before any run (research-update `prereg/2026-11-s72-government-budget.md`), with two dated amendments: one before the pilot, one after the frontier ran (a check added, nothing changed). It answers findings 1 and 2 of the Nov 13 audit (research-update `audits/2026-11-13-simulation-audit.md`). Tables: `dev/runs/s72-government/tables.md` and `summary.md`; per-seed results: compassionism-sim-results `s72-government-df9cfbe`.

## In short
1. **The engine now keeps a government account.** For every row it records what the government finances, what the contribution raises, the interest on any borrowing, the deficit and how it is met (new money, borrowing, or nothing), the stock of programme debt, today's federal debt and how much of it the programme's inflation erodes, today's safety net, and the government's loss as a lender when household debt is inflated away. A books check holds every year on every reading. Off, nothing moves (guard test).
2. **Two new answers to "who pays the part the contribution cannot raise":** the government borrows it (at the 10-year inflation-protected Treasury rate, 0.97% real, plus a premium that rises with the debt, from Laubach 2003; or at the rate a simple central-bank rule would set), or the contribution's cap is raised to 99%.
3. **The C2.2 design cannot be paid for by a contribution on wages.** That is the design and financing behind ledger decision D21. On wages, at any share and cap tried, its inflation stays at 32-49% a year when the rest is new money. Borrowing the rest instead keeps inflation near zero, but programme debt passes the size of the whole economy (100% of GDP per adult) in year 4 or 5 and keeps compounding. Even with no premium at all, the debt reaches 7 to 9 times GDP by year 20. A higher cap makes things worse: at 99% people work so much less that the contribution raises less (about $27,700 per adult a year, against $37,800 at 90%), and inflation rises to 50-67%.
4. **The only C2.2 row on the grid that comes close is a contribution on all money income** (wages, conversion proceeds, Social Security, the programme's cash and capital income), set to raise the whole payout, capped at 90%:
   - The rate averages 69-78% of all money income.
   - With the rest as new money, inflation is 6.4-7.8% a year: over 5% in every environment.
   - With the rest borrowed, inflation is 0.1-0.2% a year and programme debt is 12-23% of GDP per adult at year 20, falling over the last five years.
   - Paid for this way, C2.2's effect on poverty is small. Basket poverty changes by −7.0, −1.9 and +1.2 points (Reference, Adverse, Stress) with the rest as new money, and by −11.6, −2.3 and +0.3 with it borrowed. Under the Source it falls by 30-38 points. Wealth poverty falls by 9-13 points (new money) or 4-8 (borrowed), against 21-23 under the Source. Most of C2.2's measured gain comes from money that is not raised from anyone in the model.
5. **The release design can be paid for by a contribution**, but only by a large one, and paying for it that way leaves people worse off on the cost of living:
   - On wages plus conversion proceeds (cap 70% or more) or on all money income (cap 70% or more), raising the whole payout keeps inflation at 0.7-3.2% a year in all three environments.
   - On wages alone it does not: 12.0% a year in Adverse.
   - Paid wholly by a contribution on wages (cap 90%, the rate averaging 62-79% in Reference and Adverse), basket poverty rises against no programme: by 5.3, 14.8 and 1.0 points with the rest as new money, and by 9.8, 11.1 and 0.8 points borrowed.
   - Its borrowing is modest: programme debt is 2.5-19.5% of GDP per adult at year 20, and falling.
6. **The Source rows (the main financing of both designs) owe almost nothing to the government account.** Their contribution covers only the transfers it is meant to cover (a deficit of $45-95 per adult a year). The Source's own payout is new money, as before. The account shows two other effects of their inflation (36-52% a year in the candidate main row, as in S68):
   - The fixed-coupon part of today's federal debt is almost wholly inflated away within the run. That is about $79,000 per adult; the erosion is $2,600-3,950 more per adult a year than without the programme with no repricing (an upper bound), or $1,300-2,400 if a sixth of it reprices each year. Holders of Treasuries bear this loss: households, pension funds, the Federal Reserve and foreign holders.
   - The government loses about $30,500 per adult over the run as a lender on household debt (student loans and the federal share of mortgages, S71's ledger).
7. **Today's safety net costs less under C2.2** ($300-800 per adult a year less, against no programme). Under the release design it costs about the same.
8. **A policy-rate rule instead of a fixed rate** changes the release design's borrowing by 1-2%, and C2.2's by 13-15% (inflation that the rule did not expect erodes the debt). C2.2's debt explodes either way.
9. **Found by the build: the weighted top tail and the contribution's books.** The candidate main row includes S59's weighted top tail of wealth. Its 18 adults stand for very few people but count as ordinary adults in every decision. Two effects:
   - Counted that way, they distort a contribution's base. A new part, the books at each adult's weight (`gv.wb`), corrects the contribution's base and receipts. Under the Source it moves the contribution's rate by at most 0.04 points and no outcome by more than 0.01 points. Without the tail it changes nothing.
   - The tail also distorts any rule that charges capital income. Under "all money income" the tail's adults pay a large charge on their capital income and, through the income effect, raise their hours by over 100%. Their extra wages enter the price module unweighted and lower measured inflation (C2.2, all money income, cap 90%: 3.1-4.0% with the tail, 6.4-7.8% without).
   - The frontier was therefore run again without the tail (Amendment 2). For the wider bases the run without the tail is the one to read. On wages alone the two runs agree within 0.2 points.

## What was built (engine; every part off by default, guard test identical)
- **Row option `gv`** (switch `GOV`; MODEL_SPEC 14.14; TESTBED_SPEC 7). The account (keys `GV_KEYS`), with an identity checked every year (`ACCT` id `gov`): payout + interest − contribution = new money + borrowing + unpaid − surplus.
- **Today's debt** from opened sources (`sources/s72_government.py`): debt held by the public at Sept 30, 2025, $30,277.8 billion (Treasury's Monthly Statement of the Public Debt), over 266,978,268 adults (Census, July 2024), which gives $113,410 per adult. GDP in fiscal 2025 was $30,322.8 billion (FRED), $113,579 per adult. The fixed-coupon share (notes, bonds, non-marketable) is 69.7%.
- **`fx.fin 'debt'`**: borrowed at `rr` 0.97% real plus `dk` × (programme debt over GDP), `dk` = 0.04 (Laubach's 4 basis points per point of debt to GDP), so the debt keeps its real value. `gv.r 'rule'`: Taylor's rule as the Federal Reserve writes it (weights 0.5 and 0.5, target 2%), reacting to last year's inflation and the environment's recessions. Interest is paid from the account: next year's contribution aims to raise it too, up to the cap, and what it cannot raise is borrowed. Interest goes to bondholders outside the model's households, a cautious assumption.
- **`fx.fin 'cap'`**: the cap raised to 99%; what it still cannot raise is new money.
- **The frontier's settings**:
  - `gv.sh`: the share of the payout the rate is set to raise.
  - `gv.base`: wages; wages plus conversion proceeds; or all money income, charged on last year's amounts. Charges on income other than wages act only through the income effect (one income effect per unconditional dollar, guardrail 7).
  - `gv.wb`: the contribution's books at each adult's weight.
- **A numerical guard**: the borrowing rate is held at 100% a year at most (`gvGuard`). It is reached only where the debt has already exploded and keeps the numbers finite. It is not a reading.
- **Tests**: 9 unit tests (`s72UnitSuite`), 350 in all, all pass. Guard test identical. Validate, domtest (153) and lineage all pass; the six release panels are identical. On-together tests with `gv` added to the candidate main row and `R2_ALT`: 137 rows × 3 environments × 5 seeds, all pass, run order identical (`dev/runs/s68-pairs/`).

## The pilot (100 seeds; D21's row is "C2.2, flat contribution on wages, cap 90%, share 100%")
Programme inflation (% a year), Reference / Adverse / Stress; basket poverty and weighted wealth poverty at year 20 are differences from no programme, in points:

| Row | Inflation | Mean rate | Basket poverty | Wealth poverty (weighted, yr 20) | Programme debt yr 20, % of GDP (median) |
|---|---|---|---|---|---|
| Release, Source | 36.5 / 43.4 / 18.9 | 3.0 / 3.8 / 1.5 | −18.4 / −22.1 / −7.9 | −14.8 / −14.3 / −7.8 | 0 |
| Release, contribution, rest as new money | 2.5 / 11.4 / 0.9 | 62 / 79 / 19 | +5.3 / +14.8 / +1.0 | −3.2 / −4.2 / −1.1 | 0 |
| Release, contribution, rest borrowed | 0.1 / 0.0 / 0.0 | 71 / 63 / 18 | +9.8 / +11.1 / +0.8 | +0.8 / +1.2 / −0.5 | 19.5 / 8.4 / 2.5 |
| C2.2, Source | 41.9 / 49.0 / 52.4 | 3.1 / 4.0 / 2.6 | −29.6 / −38.1 / −37.2 | −21.7 / −22.6 / −20.8 | 0 |
| C2.2, contribution, rest as new money (D21 with S68's fix) | 32.0 / 45.0 / 41.4 | 85 | −20.0 / −24.4 / −16.6 | −16.3 / −16.2 / −14.2 | 0 |
| C2.2, contribution, rest borrowed | 0.1 / 0.2 / 0.2 | 85 | −25.5 / −34.2 / −31.6 | −19.5 / −23.0 / −19.9 | 110,000 / 139,000 / 49,000 (passes 100% in year 5 / 4 / 5) |
| the same, no debt premium | 0.1 / 0.2 / 0.2 | 85 | as above | as above | 771 / 912 / 715 |
| C2.2, contribution, cap 99% | 50.1 / 66.7 / 64.6 | 93 | −8.8 / −9.4 / +1.8 | −12.2 / −12.4 / −9.9 | 0 |

Under borrowing, household outcomes do not depend on the rate: the contribution is already at its cap and interest is paid to holders outside the model, so the rate readings only change the debt. The debt readings (100 seeds, C2.2; year-20 debt against the fixed-rate reading): the policy-rate rule, −13% to −15%; with its weights moved (inflation 0.25-1.0, the gap 0-1.0), −5% to −16%; with its neutral rate at 0 or 2%, −28% to +3%; a real rate of 0 or 1.96%, −19% to +27%; interest borrowed instead of raised, 0% (the contribution is at its cap); the premium at Laubach's 2.1 basis points, −91% to −93% (3,500-12,300% of GDP); a 95% cap, inflation 36-50% a year with the rest as new money. None of them keeps the debt from exploding. Hours fall by 14-17% under borrowing and by 21-25% with the rest as new money, against no programme.

## The frontier (20 seeds; without the weighted tail, the run to read for the wider bases)
**Rule (A), the lowest share of the payout on the grid with inflation under 5% a year (upper 95% bound) in all three environments, the rest as new money:**

| Design | Wages | Wages plus conversion | All money income |
|---|---|---|---|
| Release | none at any cap (Adverse 12.0-20.7% at share 100%) | 100% at cap 0.7 or 0.9 (inflation 0.9-3.2%) | 100% at cap 0.7 or 0.9 (0.7-2.4%) |
| C2.2 | none (31.8-48.4% at 100%) | none (7.6-11.3% at best, cap 0.9) | none (6.4-7.8% at best, cap 0.9) |

With the tail on (the candidate main row as run), C2.2 on all money income at cap 0.9 passes at 3.1-4.0% and the release design passes at cap 0.5 as well. Both differences are the tail's distortion described above. Every other cell agrees.

**Rule (E):** for the release design, adding conversion proceeds or all money income to the base turns "no share passes" into "100% passes". For C2.2 no base passes.

Every cell's contribution rate, poverty, hours and the borrowing reading's debt are in the tables. As the share falls below 100%, inflation rises steeply: C2.2 on all money income at cap 0.9 gives 16.9-20.5% at share 75% and 62-73% at share 0 (the whole payout as new money).

## Decision rules (fixed before the pilot), applied
- **(A)** As in the table: no share on the grid works for C2.2 on any base. For the release design, 100% works on wages plus conversion or on all money income with a cap of 70% or more.
- **(B)** Claude's recommendation for S63's choice between new money and borrowing, for any financed row:
  - The release design under the flat contribution meets the test (debt under 30% of GDP per adult in every environment, falling over years 16-20), so borrowing is its main reading.
  - D21's row (C2.2 on wages) fails it in every reading, so new money stays its main reading with borrowing printed beside it.
  - C2.2 on all money income at cap 0.9, share 100%, meets the test in the run without the tail (12-23%, falling). With the tail, Adverse reaches 30.5%.
- **(C)** The rule and the fixed rate differ by more than 10% for C2.2, so both readings go to S70's screen. For the release design they differ by 1-2%.
- **(D)** The Source rows: `gv` moves their contribution by at most 0.04 points (the weighted books) and no outcome by more than 0.01 points.
- **(E)** As above.

## Limits
- Contribution rates of 50-99% of a base are far outside the changes the one labour elasticity (Chetty's 0.33) was measured on. Avoidance, informal work and moving income out of the base are not modelled.
- Laubach's estimate comes from US debt between 30% and 60% of GDP. Programme debt of many times GDP is far outside it, and whether anyone would lend at all is not modelled. The no-premium reading is shown for that reason, and it explodes too.
- The model has no GDP: debt ratios use fiscal 2025's GDP per adult, held fixed in real terms.
- Interest reaches no modelled household's income.
- The repricing reading's six years is a design parameter (the average maturity of marketable debt was not opened). The no-repricing figure is an upper bound.
- The policy-rate rule reads only the environment's recessions. There is no central-bank layer (S74).
- Hours depend on population size in the frozen engine (S68 part 2); every flat-contribution figure carries that.
- With the weighted tail on, every decision and the price module stay unweighted (S59's rule). Rules that charge capital income are distorted by it; the weighted books correct only the contribution's own sums.
- CBO's projections could not be opened from the session (its site refused). No figure depends on them.

## For later steps
- **S63** (main row and D23): the candidate main row carries `gv: {}`. No financed C2.2 row is carried on wages: on that base its inflation is 32-46% a year, or its debt explodes. If a financed C2.2 row is carried, Claude's recommendation is C2.2 on all money income, share 100%, cap 0.9, with the rest borrowed (inflation 0.1-0.2%, debt 12-23% of GDP per adult at year 20). Print it beside the Source rows with its rate (69-78% of all money income) and its much smaller effects on poverty, and the same row with the rest as new money (6.4-7.8% inflation) beside it. D23 (whether the Hub may lead with a financed row) is decided again with this in hand; it remains Duke's decision. Any row with a base wider than wages is read without the weighted tail or with that distortion stated.
- **S70**: join the screen: the share (0-1), the base (three), the cap (0.5-0.9; 0.95 and 0.99 under 'cap'), how a deficit is met ('money', 'debt'), the real rate (0-1.96%), the debt premium (0-0.04), the rule's weights and neutral rate, interest paid or borrowed.
- **S69**: the packet is rebuilt with `gv: {}` in the candidate main row (as planned, after S73).
- **S74**: the policy-rate rule here is a placeholder for the central bank's; S74 replaces the gap with its own and may read the account's debt.
