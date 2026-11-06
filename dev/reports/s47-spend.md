# The spending share, re-derived for the frozen model (S47, Nov 6, 2026)

Outside audit item E17 (`dev/reports/s13-engine-audit.md`) asked for this before the design freeze (research-update `prereg/run-manifest.md` section 6 item 4). The share was derived on an earlier engine and never re-derived for the model the batch will run.

## What the share is
Each year, adults spend part of the cash they have left after paying their cost of living. The engine's share for this, 0.593 (`SPEND_SOURCED`), was set on Oct 1 from a primary source. It is the share at which the no-programme run saves 5.4% of income, the US personal saving rate in 2025 (BEA NIPA Table 2.1, line 35). It was never tuned to any programme result. The audit asked whether it still gives 5.4% on today's no-programme run, which now has households, today's safety net, unemployment insurance, income-graded spending and the audit's corrections.

## What was done
`dev/tools/s47_spend.js` repeats the derivation by its stated method, bisecting on the share in the Reference environment over seeds 1-100. It does this on the run the share was derived on, and on the frozen model's no-programme row: the batch's common settings, the CPS earnings yardstick, and the audit's corrections and the second implementation's fixes. Results: `dev/runs/s47-spend/rederive.json`.

| Run | Saving rate at 0.593 | Share that gives 5.4% |
|---|---|---|
| The published run, counted as it was on Oct 1 | 5.40% | 0.593 (reproduced) |
| The published run, counted on its own years only | 5.87% | |
| Frozen no-programme run: the method's formula (saving over wages) on the row's own years | | 0.862 |
| Frozen no-programme run: saving over disposable income on the row's own years | 19.48% | **0.877** |
| Frozen no-programme run: the method's ledger as it was counted (see below) | 14.63% | 0.779 |

## Two counting faults in the original derivation
The derivation read the engine's yearly ledger, which adds up every run it sees. Each seed was run cold, so the ledger also counted two runs that are not the no-programme row:
1. the seed's supply-path run, a price-only run that ran first (in the published run, half of the adult-years counted);
2. a one-year pass the testbed makes to set the contribution rate (year 0 counted twice, about 5% of the adult-years).

Both are counting faults in the tool, not in the method. The new tool fills the supply path's cache before it counts. It also reads each adult's flows at year end from the engine's accounting check (reporting only), so only the row's own 20 years are counted. In the published run, which has no transfers, the method's formula and saving over disposable income then agree exactly (5.87%), which checks the new counting.

## Which reading the frozen model uses
**0.877: saving over disposable income.** The target, 5.4%, is BEA's saving as a share of disposable personal income. The method's formula divided by wages because wages were the run's only income when the share was set. The frozen run also has Social Security, unemployment insurance, the safety net's cash (net of tax), interest, and income-graded spending, so over wages the formula no longer measures the target. Counted on the row's own years, the method's formula over wages gives 0.862. The two readings differ by 0.015.

This is a re-derivation of a constant by its own method, on the model being frozen. It is not tuning: no programme figure was looked at to choose it. The published engine keeps 0.593 (`SPEND_SOURCED`; the released figures and the guard test are unchanged). The frozen model's share lives in `harness.js` (`SPEND_FROZEN`, set by `frozenRow`).

## What it changes (50 paired seeds, all three environments; `dev/tools/s47_spend_effect.js`, tables `dev/reports/s47-spend-tables.md`)
- **Almost nothing in poverty against the cost of living or in prices.** Basket poverty moves by at most 0.1 point, with and without a programme. Programme inflation does not move.
- **Savings fall.** Median real wealth at year 20 with no programme drops from $409,000 to $212,000 in Reference. The lower figure is closer to the Survey of Consumer Finances, though still above it.
- **Wealth poverty with no programme rises 1.8 points** (Reference).
- **The programme's effect on wealth poverty changes most.** The programme's inflation erodes savings, and with more of each surplus spent there is less saving for the programme's own income to add to. For the C2.2 design the year-20 effect goes from −17.4 points at 0.593 to +0.5 at 0.877 in Reference, from −17.4 to +30.1 in Adverse, and from −7.8 to +41.7 in Stress. For the release design it goes from −3.5 to +21.4 points in Reference. Every one of these changes is far outside its interval.
- The design-neutral BLEI effect moves by under 1 point (C2.2's cut grows slightly; the release design's shrinks slightly).

So at the re-derived share, the C2.2 design still cuts poverty against the cost of living by about 25-35 points. But it no longer cuts wealth poverty, and in Adverse and Stress it raises it. This is a measured result of the frozen model, not a target. It goes into the record as it is.

## What the batch does with it
- Every frozen row uses 0.877.
- Study R also runs the frozen engine at 0.593 for none and both designs (research-update manifest Amendment 3), so the release panel shows how much of the frozen model's wealth result comes from the share.
- No other constant moves.

## Limits
- The share is derived in Reference on the CPS yardstick, as the headline is, and used in every environment and on both yardsticks, as 0.593 was.
- The saving rate is a ratio of sums over 100 seeds. Its seed-to-seed spread is not used.
- Interest enters disposable income only where savings that keep up with prices are on (none of the no-programme rows here).
