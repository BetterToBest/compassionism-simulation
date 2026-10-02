# Spending layer: new spending raises output and jobs where there is idle capacity

Session 31, Oct 2, 2026. Design note before code (ledger step s68). Written by Claude.

## What it is, in plain words

When people spend more at businesses, those businesses hire and produce more, and their workers spend in turn. Economists call the total effect per dollar the "multiplier". Published estimates agree on one thing: the effect is much bigger when the economy has idle workers and machines (a recession) than when it is running near full capacity. At full capacity most of the extra spending raises prices instead. The model today has no such effect: spending never creates jobs. This step adds it, from published estimates, and reports what comes out.

## Sourced figures

| Source | What it found |
|---|---|
| Congressional Budget Office, estimates of the 2009 Recovery Act's effects (output multipliers table, "transfer payments to individuals") | $0.80 to $2.20 of output per dollar of transfers, in a slack economy |
| Auerbach and Gorodnichenko (2012), "Measuring the Output Responses to Fiscal Policy", American Economic Journal: Economic Policy 4(2) | Spending multipliers of about 1.5 to 2 in recessions, about 0 to 0.5 in expansions |
| Ramey and Zubairy (2018), "Government Spending Multipliers in Good Times and in Bad", Journal of Political Economy 126(2) | Multipliers below 1 whether or not there is slack (the cautious counterpoint) |
| Parker, Souleles, Johnson and McClelland (2013), "Consumer Spending and the Economic Stimulus Payments of 2008", American Economic Review 103(6) | Households spent 12-30% of a payment on nondurables within three months, 50-90% including durables |

## Values used (Claude's decisions)

| | Recession years | Normal years |
|---|---|---|
| Main | 1.5 (the middle of CBO's range, and the low end of Auerbach-Gorodnichenko's recession figure) | 0.5 (the top of Auerbach-Gorodnichenko's expansion figure) |
| Low (cautious) | 0.8 (CBO's low end; consistent with Ramey-Zubairy) | 0 |
| High | 2.2 (CBO's high end) | 0.8 |

These are not tuned. They are the published ranges; the low and high rows are always shown.

## How it works in the model

1. **The spending push each year** is the program's net new spending at businesses: BU and converted dollars spent, plus extra spending out of income under the session-30 spending rule, minus whatever the program takes out of spending (any tax or contribution in force). It is counted once.
2. **Recession or normal year** comes from the model's existing recession path (the same one that drives the Adverse and Stress environments). A year counts as a recession year when its recession is active. Automation job losses also count as idle capacity for the workers they displace.
3. **Added output** = multiplier x push, but **never more than the idle capacity**: in a recession year, never more than the income the recession took away; in a normal year, the normal-year multiplier already reflects a nearly full economy.
4. **Where it goes.** The labour share of the added output (BEA national accounts, compensation of employees over gross domestic income, NIPA Table 1.10) becomes earnings. It goes first to adults who lost work or hours in the recession or to automation, in proportion to what they lost, so it is deterministic and uses no random draws. The rest raises business income as the model already handles it.
5. **Prices.** The added output counts as real output behind the money in circulation, so it slows the model's created-money price rise. Spending not matched by added output goes to prices exactly as today. Nothing is counted twice: the multiplier applies only to spending not already matched by output from the production side or creative work.
6. **Fairness rule.** This step changes how many jobs exist, not the reward for working, so the single wage elasticity is untouched.

## What to expect (not a target)

The ledger's expectation, kept as a hypothesis: the biggest help comes in the Adverse and Stress environments, where recessions leave idle capacity. At Reference it may mostly add to prices. Results are reported as they come out.

## Switches and checks

- Switch `MULT` (`'off'` = session 30, `'main'`, `'low'`, `'high'`). With `'off'` every output is bit-identical (full-output diff). No new random draws.
- Tests: added output is zero when the push is zero; it never exceeds idle capacity; with the normal multiplier at 0 nothing is added in normal years; the earnings added equal the labour share of the added output; adults who lost no work get none of the re-employment earnings.
- Restudy: seeds 1-500, paired, three environments, all three rows; basket and wealth poverty, work, prices, cost and groups.

## Built (session 31, Oct 2, 2026), and one change from the plan above

Built as switch `MULT` in `harness.js`, with 4 unit tests (`multUnitSuite`). With it off, output is identical.

**One change from the table above: the normal-years multipliers are not used.** The model has no idle workers or machines outside recessions: everyone who wants to work does. So in normal years the extra spending has no room to create jobs, and it goes to prices as before, whatever multiplier is assumed. The layer therefore works only in recession years. It restores up to all of the wages a recession took away: labour share (0.508 of national income in 2025, from the national accounts) × multiplier × last year's programme spending, capped at the recession's loss. Automation's wage losses are not filled, because they are a lasting change in what work pays, not a lack of spending (a stated limit).

## Results: 500 paired runs, against step 15 (`dev/runs/step16-17-v5-500-*.txt`)

| | Reference | Adverse | Stress |
|---|---|---|---|
| Below the cost of living | 22.0% (no change: no recessions) | **43.6% → 42.1%** | **66.6% → 65.6%** |
| Too little wealth at year 20 | 35.7% (no change) | **88.1% → 87.1%** | **91.2% → 90.6%** |
| Price level at year 20 | 297 (no change) | 2,082 → 1,851 | 92 → 86 |
| Low multiplier (0.8) / high (2.2) | no change | almost the same as 1.5 | a little smaller / almost the same |

In everyday words: **in hard times the programme's spending keeps people in work through recessions**, which lowers poverty by about 1 to 1.5 points and slows price rises a little. The size of the multiplier hardly matters, because the programme spends far more than a recession takes away, so even the low published multiplier is enough to fill most of the gap. At Reference there are no recessions, so the layer changes nothing.
