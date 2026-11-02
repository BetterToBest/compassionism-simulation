# Security beyond wealth: what the model now measures, and how

Nov 2, 2026 · research-update plan step S53 · written before any run · Claude

Duke, the plan asks for five kinds of security the simulation did not measure: big income drops with no buffer, how long a household could cover the basics without wages, the hours of work the basics cost, forced moves, and how much of a household's budget is exposed to market prices for essentials. It also asks for the year-by-year poverty figures that the public-costs step (S19) will turn into costs, so that step needs no new run. This note says how each is measured and which are true by construction. Please say if any of them misses what you mean by security.

Nothing here changes what any simulated adult does. The measures only read the model, and only when a study turns them on (study option `sec`); off, every figure is identical to the last release (guard test: 25 rows x 20 seeds x 483 outputs, identical in all three environments).

## Words used below
- **Resources**: money income plus the market value of the help a household gets in kind (BU spent on the basics, PTF and PTH price cuts), in today's dollars. This is the engine's own resources measure.
- **Liquid savings**: 20% of a household's positive savings. The model's savings include homes and other holdings from the Survey of Consumer Finances; the BLEI already treats 20% as liquid, so these measures do the same. A second reading uses all savings.
- **Income without wages**: what a household would still receive if it stopped working this year: cash transfers, unemployment insurance, Social Security. BU, PTF and PTH are already in the household's own cost of living. Conversion proceeds are left out, because they follow work and BU use; this is the cautious reading (it understates the programme's protection), and a second reading counts them.
- **Need**: the household's own cost of living less its income without wages.
- Three groups: all adults; the adults who take part; the adults who choose not to (the same people in every design and in the no-programme run, so the no-harm test compares like with like).

## The five measures

| Measure | How it is counted | By construction or emergent |
|---|---|---|
| **Big income drops with no buffer** | A year in which resources fall 25% or more from the year before, and liquid savings at the start of the year are less than the fall. Per 100 adult-years. Readings: a 50% fall; money income alone (no in-kind help). | Emergent: falls come from recessions, job loss, ageing and prices. The BU softens falls in resources because it does not stop when wages do; that is the mechanism, not an assumption. |
| **Months the basics are covered without wages** | Liquid savings over a month of need. The share of adult-years below 1 month and below 3 months, and the median (a household whose income without wages covers its need counts as 120 months). Reading: all savings. | Mixed: lower need is by construction (BU and price cuts lower own cost); savings are emergent (inflation, earnings, spending). |
| **Hours of work to cover the basics** | Need over the adult's own hourly wage (its usual wage over a 2,080-hour year), per week. The median over working-age adults with a wage, and the share needing more than 40 hours. Reading: conversion proceeds counted. | By construction, given prices and wages: a lower own cost means fewer hours. The price level and wages that enter it are emergent. Taxes on the extra hours are not counted (it understates hours for everyone, programme and none alike). |
| **Forced moves** | (a) PTH tenancies ended, per 100 PTH member-years. (b) Displacement by price: adults outside PTH who could pay last year's cost of living from income and savings and cannot this year (the engine's housing-distress test, which feeds its estimate of unhoused people), per 100 adult-years. | (a) By construction: the model has no rule that ends a PTH tenancy against the member's will. With the PTH books on, members leave at a drawn moving rate (6.2% a year); with them off, no one leaves. So a forced PTH move is zero by construction and the measure counts ordinary moves. (b) Emergent, but a proxy: the model has no moving decision, so it counts households pushed past the point where they can no longer pay. |
| **Exposure to market prices for essentials** | The essentials (what BU can buy: food, housing with utilities, medical care, and transport where the BU covers it) that a household pays for in money at its own prices, as a share of its whole cost of living at market prices, and as a share of the essentials at market prices. Ratios of totals over all adult-years. | By construction: with no programme every essential is paid in money (the second share is exactly 100%, unit test) and the first is the essentials' share of the budget; BU and the price cuts lower both. PTF members' purchases count at PTF's price, which still moves with costs (as the supply-shock study found). |

## The year-by-year series for the public-costs step (S19)
For each year of the run, all adults: the share below their own cost of living; the average poverty gap (as a share of the line, and in today's dollars per adult); the same gap with each adult's gap capped at $10,000 a year (the income range of the prison study the public-costs calculation already uses, Deshpande and Mueller-Smith 2022); deep poverty (half or more of the cost of living unmet); housing distress; the engine's estimate of extreme poverty (the unhoused); the number of adults; and the share below their own cost of living among the adults who chose not to take part. Weighted by adults, the yearly shares add up exactly to the run's person-year figures (unit test). The public-costs step multiplies these by the costs already sourced in `dev/reports/v5-4-public-costs.md`.

## Limits, said plainly
- The model has no moving decision, no rent arrears process and no eviction court. Forced moves are a proxy.
- Liquid savings are a fixed share of savings, not a separate account.
- The hours measure uses the adult's usual wage; in a recession year the wage on offer may be lower.
- Households that pool their income share one cost of living; their income without wages is each adult's own.
