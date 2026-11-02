# What it takes to back the new money: pilot results (PILOT)

Nov 2, 2026 · research-update plan step S51 (ledger D11) · Claude

**This is a pilot.** 50 seeds on GitHub Actions. The figures below decide only what the design freeze (S47) carries into the full study; they are not figures of the model. The full study (seeds 1-500) runs after the freeze. Preregistration: `prereg/2026-11-backing-addendum.md` in BetterToBest/research-update (study M), committed before any run. Engine: commit `6428b96`. Per-seed values: BetterToBest/compassionism-sim-results, folder `s51-backing-6428b96/` (run.txt, SHA256SUMS; workflow run 41373143374). Every table: `dev/reports/s51-backing-tables.md`, made by `python3 dev/tools/s51_backing.py ../compassionism-sim-results/s51-backing-6428b96 --out dev/reports/s51-backing-tables.md`. Claude's reading of the design, written before the run: `dev/reports/s51-backing-reading.md`.

Every figure is the programme minus no programme, on the same 50 seeds, in percentage points, with a 95% interval in brackets. "Wages keep up 90%" means wages rise by 90% of the programme's price rise.

## In short

1. **The C2.2 design needs no backing for basket poverty to fall.** At every wage indexation tested (100% down to 75%) and in all three environments, basket poverty falls with nothing backed. Its basic unit is raised every year to the price of basic needs, so inflation does not wear it down.
2. **The release row needs backing only when wages lag prices badly.** Basket poverty falls with nothing backed when wages keep up 95% or 90%. When they keep up only 75%, it falls only if about half the payout is backed: 46% in Reference, 31% in Adverse, 54% in Stress.
3. **Wealth poverty is where backing bites.** For the release row, wealth poverty at year 20 (too little wealth) is below no programme only if 32% (Reference), 63% (Adverse) or 75% (Stress) of the payout is backed, even with wages keeping up in full. With wages at 90% the shares are 66%, 75% and 81%.
4. **Under the main reading, the mechanism backs about 1% of the release row's payout.** The main reading: only added output absorbs new money, and added output is capped at 8% of earned income. That is far short of what wealth poverty needs. **No main-reading setting reaches break-even for the release row, in any environment (0 of 36).** Basket poverty falls in all of them; wealth poverty rises in all of them. This is the outcome the reading note warned of.
5. **With no ceiling, it still does not reach.** Under the main reading with no ceiling, the most productive setting backs 19.5% of the payout, by having the projects produce 2.3 times the economy's earned income in year 19. Programme inflation falls from about 51% to about 41% a year, and wealth poverty still rises (by 52 points at 90% wages in Reference). Only the other reading ("proceeds retire the money") with no ceiling reaches break-even: 6 of the release row's 216 settings, in Reference and Adverse, none in Stress. Each of those has the projects producing 1.2 to 3.3 times earned income by year 19.
6. **Why wealth poverty rises: savings lose their value to inflation.** In these rows, household savings earn interest that does not keep up with prices. At about 51% inflation a year, savings melt. A check run on the session machine (not preregistered, 10 seeds) turned on the engine's existing option for savings that keep up with prices. The release row's rise in wealth poverty then became a fall: 12 points up became 21 down at full wages, and 60 up became 12 down at 90% wages. Basket poverty did not move.
7. **A gap in the release row's protection of the basic unit.** In the release row, the basic unit (BU) is raised to match prices only in a year when inflation exceeds 5% (the Inflation Surge Protocol). Inflation of 2-5% a year wears it down unprotected, fewer people find it worth joining, and the poverty gain shrinks. This is why, oddly, backing 95% of the payout does worse than backing 90% or 100%. The same check confirmed it: with the BU following prices every year, the dip disappears.

## What was run

The study asked three questions (Q11-Q13 of the preregistration).

- **Arm A: how much backing is needed (Q11).** The model assumes a fixed share of the payout is backed by output (0% to 100%), crossed with wage indexation (100%, 95%, 90%, 75%). The break-even backed share is the smallest share at which poverty falls below no programme.
- **Arm B: how much the mechanism backs (Q12, Q13).** A share f of the payout funds projects that add output after a lag. The backed share is then a result of the run, not an input. Settings swept: f (25%, 50%, 100%); output a year per dollar, rho (0.05 to 0.32); ceiling (8% of earned income, 16%, none); how output backs money (main reading: only added output; other reading: proceeds retire the money); lag and wear (sensitivities).
- **Two designs:** the release row as released, and the C2.2 design (the study programme's headline design: BU at the cost of basic needs, raised every year, automatic distribution).
- **Three environments:** Reference, Adverse and Stress. 500 adults, 20 years, seeds 1-50, paired.

## Q11: how much backing each design needs

Break-even backed share. "0%" means poverty falls with nothing backed. Intervals are narrow (within 2 points) in every cell; see the tables file.

**Basket poverty (the primary measure: income below the cost of living)**

| Design | Environment | Wages keep up 100% | 95% | 90% | 75% |
|---|---|---|---|---|---|
| Release row | Reference | 0% | 0% | 0% | 46% |
| Release row | Adverse | 0% | 0% | 0% | 31% |
| Release row | Stress | 0% | 0% | 0% | 54% |
| C2.2 design | all three | 0% | 0% | 0% | 0% |

**Wealth poverty (too little wealth at year 20; a confirmation measure)**

| Design | Environment | Wages keep up 100% | 95% | 90% | 75% |
|---|---|---|---|---|---|
| Release row | Reference | 32% | 57% | 66% | 78% |
| Release row | Adverse | 63% | 71% | 75% | 82% |
| Release row | Stress | 75% | 78% | 81% | 87% |
| C2.2 design | Reference | 0% | 0% | 0% | 31% |
| C2.2 design | Adverse | 0% | 0% | 12% | 40% |
| C2.2 design | Stress | 0% | 12% | 29% | 52% |

The two "below 30 days of basic living" measures need less backing than wealth poverty in every cell. For the release row in Stress they need backing even at full wages: 44% for the design-neutral measure, 33% for the design's own. For C2.2 they need none anywhere.

**What decision rule 1 says.** The rule claims a gain only where basket and wealth poverty agree. The C2.2 design's gain holds on both with nothing backed when wages keep up in full, in all three environments. It also holds with nothing backed at 95% in Reference and Adverse, and at 90% in Reference. The release row's gain holds on both only if roughly a third (Reference) to three quarters (Stress) of its payout is backed, even with full wages. Both statements depend on how savings are treated (point 6 above and the section on savings below).

## Q12: how much the mechanism backs, and whether it is enough

Decision rule 2: a setting **reaches** break-even if, at 90% wages, both basket poverty and wealth poverty fall, each with its interval below zero. "Basket only" means basket poverty falls but wealth poverty does not.

**The main reading** (only added output absorbs new money, ceiling 8%, lag 2 years, wear 5%). All 12 settings of f and rho give nearly the same result, because the ceiling binds in almost all of them:

| Design | Environment | Share of payout backed | Programme inflation a year | Basket poverty, wages 90% | Wealth poverty, wages 90% | Verdict |
|---|---|---|---|---|---|---|
| Release row | Reference | 0.7% | 50.6% | −10.8 (−11.3 to −10.4) | +60.0 (+59.4 to +60.6) | basket only, 12 of 12 |
| Release row | Adverse | 0.4% | 60.8% | −12.9 (−13.3 to −12.4) | +54.0 (+53.4 to +54.6) | basket only, 12 of 12 |
| Release row | Stress | 1.1% | 27.4% | −1.9 (−2.4 to −1.4) | +47.4 (+46.8 to +48.1) | basket only, 12 of 12 |
| C2.2 design | Reference | 0.8% | 37.4% | −24.6 (−25.1 to −24.1) | −10.8 (−11.6 to −10.0) | reaches, 12 of 12 |
| C2.2 design | Adverse | 0.5% | 44.1% | −33.9 (−34.5 to −33.3) | +20.0 (+18.3 to +21.7) | basket only, 12 of 12 |
| C2.2 design | Stress | 0.5% | 46.1% | −30.9 (−31.4 to −30.3) | +43.6 (+42.2 to +44.9) | basket only, 12 of 12 |

(Rows shown: f 100%, rho 0.32. Inflation is with wages keeping up in full.) The C2.2 design reaches break-even in Reference because it needs no backing there, not because the mechanism supplies it.

**Headline for Q12 (decision rule 3).** Under the main reading, the mechanism does not back enough of the release row's payout for its poverty gain to hold on wealth poverty, in any environment. It backs about 1%; wealth poverty needs two thirds or more at 90% wages. Decision rule 4 applies: see "What this means for the design".

**Why so little is backed.** The release row pays out about 60% of a year's earned income in new money, every year (83% once wages lag at 90%). Over 20 years that is about twelve years' worth of income in new money. Under the main reading, new money is absorbed only by output that is added. So to back it all, project output would have to rise by about 60% of earned income every year. With a ceiling at 8% of earned income, project output can absorb, over the whole run, new money worth 8% of one year's income: under 1% of the 20 years' payout.

**Every setting, by reading and ceiling.** Settings that reach break-even, of 12 in each cell:

| Design | Environment | Main (added output, 8%) | Added output, 16% | Added output, no ceiling | Proceeds retire, 8% | Proceeds retire, 16% | Proceeds retire, no ceiling |
|---|---|---|---|---|---|---|---|
| Release row | Reference | 0 | 0 | 0 | 0 | 0 | 3 |
| Release row | Adverse | 0 | 0 | 0 | 0 | 0 | 3 |
| Release row | Stress | 0 | 0 | 0 | 0 | 0 | 0 |
| C2.2 design | Reference | 12 | (not run) | 12 | 12 | (not run) | 12 |
| C2.2 design | Adverse | 0 | (not run) | 1 | 0 | (not run) | 11 |
| C2.2 design | Stress | 0 | (not run) | 0 | 0 | (not run) | 9 |

Every setting is published in the tables file, including all that do not reach. The release row's three settings that reach in Reference back 76-86% of the payout. They need f of 50% or 100%, rho of 0.20 or 0.32, and project output of 1.2 to 2.4 times earned income in year 19. In Adverse the same three need 1.8 to 3.3 times. In Stress none reaches: the best backs 81.6% and still leaves wealth poverty 1 point higher than no programme (+1.0, +0.5 to +1.6).

## Q13: what the answers depend on

- **How output backs the money matters most.** At the same settings, "proceeds retire the money" backs 16 to 24 times more than "only added output" under a ceiling, and about 4 times more with none. Under it, each year's whole project output takes that much money back, again every year. Under the main reading, output that already exists absorbed earlier money and cannot absorb more.
- **The ceiling matters next.** With a ceiling, f and rho hardly matter, because the ceiling binds. With no ceiling, the backed share rises with f times rho.
- **Lag and wear matter little.** Release row, Reference, f 100%, rho 0.20, no ceiling, main reading: 12.2% backed as run. A 1-year lag gives 12.6%, a 3-year lag 11.8%, no wear 18.0%.

## Two findings the study was not built for

### Savings, inflation and wealth poverty

Wealth poverty counts adults whose wealth at year 20 is below the wealth poverty line, and that line rises with prices. In the preregistered rows, household savings earn a fixed interest that does not keep up with prices. Under 51% programme inflation a year the price level at year 20 is about 2,600 times its start, and money savings are wiped out. In the 10-seed check below, the median adult's wealth at year 20, in year-0 dollars, falls from about $158,000 (no programme) to about $28,000 (release row, full wages), and to about $130 when wages keep up 90%.

The engine already has an option for savings that keep up with prices (row option `sv`, savings earning prices plus 0.97% a year). A check turned it on for both the programme and the no-programme run. It used the release row with nothing backed, Reference, seeds 1-10, on the session machine. It was not preregistered; it explains a pattern and is not a result. Command: `node dev/tools/s51_diag.js 10` in the engine, commit `6428b96`.

| Release row, nothing backed, Reference, 10 seeds | Basket poverty | Wealth poverty | Median wealth at year 20 (year-0 $) |
|---|---|---|---|
| No programme | 50.7% | 33.1% | 157,800 |
| Programme, wages 100% | 20.2% | 45.7% | 27,840 |
| Programme, wages 100%, savings keep up (both runs) | 20.2% | 11.4% (no programme: 32.2%) | 380,600 |
| Programme, wages 90% | 40.3% | 93.4% | 127 |
| Programme, wages 90%, savings keep up (both runs) | 40.4% | 20.0% (no programme: 32.2%) | 267,100 |

So the "basket only" verdicts, and most of the wealth-poverty break-even shares above, measure how much high inflation destroys money savings. Neither treatment of savings is right on its own. People with savings would move some of them into things that keep their value, but people with little tend to hold cash and bank deposits. The full study should report both (see the list for S47). The preregistered measure stays the test; the other is a sensitivity, chosen after this pilot and labelled so.

### The surge protocol's 5% threshold (release row only)

The release row raises the BU to the full price level only in a year whose inflation exceeds 5%. When inflation stays at 2-5% a year, the BU keeps its dollar amount while prices rise. Over 20 years, 3% a year takes away about 45% of what it buys. Fewer adults find joining worth its cost, and the gain shrinks. In arm A this shows as a dip close to full backing. Release row, Reference, full wages: basket poverty falls by 34.4 points at 90% backed (5.3% inflation, so the BU is protected) and by 35.0 at 100% (no inflation, so nothing to protect against). At 95% backed (2.1% inflation, unprotected) it falls by only 26.2. Participation in year 19 falls from 75-84% to 58%. Adverse and Stress show the same dip (Adverse at 95-100% backed, Stress at 90-100%), because they add 2% a year of ordinary inflation.

The same check confirmed the cause. With the BU raised to the price level every year, basket poverty at 95% backed is 14.2% instead of 23.6%. Participation is 83% instead of 57%. The dip is gone.

The dip touches only two break-even shares in the tables: wealth poverty in Stress at 90% and 75% wages (81% and 87%), which are interpolated to the 90% point, inside the dip. Read those two with that in mind. The C2.2 design raises its BU every year to the price of basic needs, so it has no such gap.

## What this means for the design (for Duke)

Under the model's main reading, the release row's payout is too large and too fast for any plausible amount of new output to back. About 60% of a year's earned income is paid out in new money every year. This holds even with no ceiling on how much the projects can produce. What would change the answer are the design's own levers (decision rule 4). Each is a change to the design, so each is your call, not mine:

1. **A smaller or slower payout**, so that less new money needs backing each year.
2. **A conversion tax, or the Source taking back part of the projects' proceeds**, so that money leaves circulation as well as entering it. The "proceeds retire the money" rows show what this does. It needs an institution your writing does not yet describe.
3. **A cap on octave capacity**, which limits how fast conversions can grow.
4. **The C2.2 design's way of protecting the BU.** It is raised every year to the price of basic needs, not only above 5%. This removes the surge-protocol gap. It also makes the basket-poverty gain independent of backing. C2.2 is already the study programme's headline design (Amendment 4).

**On the case for no ceiling.** The no-ceiling rows are in the study, and the full study publishes them beside the main reading. Your view, Nov 2, is that this is where the cultural enrichment would be felt. The pilot says the ceiling is not what blocks the release row: with no ceiling, the main reading still backs at most a fifth of the payout. What blocks it is how new money is absorbed. Output that is added once absorbs the money once, while the payout comes again every year. Cultural value (art, care, learning) is real, but it does not count here unless it is sold. The basket poverty measure prices food, housing, transport and the like, and new money raises those prices whatever else it buys.

## What S47 must carry

1. **The full grid as preregistered,** for both designs, all three environments and seeds 1-500 (350 rows per environment). The pilot gives no reason to drop any row, and dropping unfavourable rows is not allowed. Cost: one seed takes about 315 seconds on one process for all three environments. That is about 44 processor-hours for 500 seeds.
2. **Savings that keep up with prices, as a labelled sensitivity** (preregistration amendment at S47, before the full run, with the reason: this pilot). Arm A for both designs at all four wage indexations, the no-programme rows included, with `sv` on both sides of each pair: 104 rows per environment. The preregistered wealth-poverty measure stays the test. Both are published side by side.
3. **The surge-protocol gap, shown and explained.** Add arm A's 90%, 95% and 100% rows for the release row, at all four wage indexations, with the BU raised every year (12 rows per environment, labelled sensitivity). The findings page then shows the dip and its cause together.
4. **Ledger decision for Duke** on the design levers above (decision rule 4). Default meanwhile: no design change. C2.2 stays the headline design; the release row is reported as released, with these results.
5. **Wording for the findings page.** Basket poverty falls under C2.2 with no backing. The release row's gain holds on wealth poverty only with backing the mechanism cannot supply under the main reading. Every claim is labelled with its savings treatment.

## Limits

- 50 seeds; the full study may move these figures a little. The intervals are narrow, so the verdicts are unlikely to change.
- The backing mechanism and its readings are Claude's modelling of a design that does not specify them (`dev/reports/s51-backing-reading.md`).
- The price rule is the quantity theory's: prices rise with new money relative to income. The model has no interest rates, exchange rate, or asset market through which inflation could play out differently.
- Neither treatment of savings is realistic on its own; the truth lies between.
- The outside supply-shock environment (S52) and security outcomes beyond wealth (S53) come next and are not in this study.
