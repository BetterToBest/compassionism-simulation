# The top of the wealth distribution, business owners and the income wealth pays (S59, part 2)

Nov 13, 2026. Pilot: seeds 1-100, 500 adults, 20 years, three environments, engine `62a189b`. A pilot is a mechanism check, not a result; the frozen 500-seed batch decides. Preregistered before the build and before any run (research-update `prereg/2026-11-s59-tail-returns.md`, with dated amendments). Tables: `dev/runs/s59-tail/tables.md`. Per-seed files: compassionism-sim-results `s59-tail-62a189b`. Part 1 of this step is `dev/reports/s59-asset-classes.md`.

## In short
1. **The model had no very wealthy households.** Its starting wealth tables stop at the 99.5th percentile, so its richest households held $14-22 million and the top 1% of adults held 20.8% of all wealth. In the 2022 Survey of Consumer Finances (SCF), for the same families, the top 1% of adults hold 31.5%.
2. **With a fitted top tail the start matches the survey closely.** The top 1% of adults hold 30.1% (28.4 to 31.8 over seeds), the top 0.1% hold 11.6% (survey 11.8%), the top 10% hold 70.4% (survey 69.3%). The Fed's Distributional Financial Accounts, an outside source with a wider wealth concept, give 29.3-30.4% for the top 1% in 2022 and 32.5% in mid-2026. The tail is fitted to the survey, so agreement with the survey shows the build works; it is not independent confirmation.
3. **Whether the programme lowers or raises concentration is not established.** Under the main reading the programme lowers the top 1% share at year 20 by 1.1 points (release design) and 1.8 points (C2.2 design) in Reference, and by 0.9 to 1.7 points in Adverse and Stress. Every tail assumption tested keeps that sign. But the fall comes from fixed-rate mortgages being inflated away with nobody bearing the loss (the model has no lender). With that debt relief removed, the programme raises the top 1% share by 1.2 points (release) and 0.6 (C2.2) in Reference, and by 0.1 to 0.8 elsewhere.
4. **The tail does not change the programme's other results.** Wealth poverty, basket poverty, median real wealth and inflation move by less than their own intervals when the tail is switched on. The programme's effect on wealth poverty under the main reading is −12.5 points (release) and −18.1 (C2.2) in Reference, against −12.6 and −18.2 in part 1's reading.
5. **Wealth pays income, mostly at the top.** With SCF rates, capital income is about $9,800 per adult at the start (the survey: about $8,950), 16% of money income by year 20 without the programme. The programme lowers real capital income per adult by $700 to $1,100 at year 20, because nominal assets lose value.
6. **If private owners kept the conversion premium** (an earlier reading of the design; the release reading passes it to customers as lower prices), the programme would still lower the top 1% share of wealth, by less (−0.6 to −0.8 in Reference instead of −1.0 to −1.5), but the top 1% share of income would rise by 1 to 5 points instead of falling, and the programme's cut in basket poverty would be about 4 points smaller.
7. **A correction to part 1.** The survey file was re-issued in 2025 dollars on Oct 5, 2026, and part 1's script adjusted for prices a second time: its wealth-group edges were 9.4% too high. Corrected and rerun: no finding changes (largest move 0.11 points).

## What was built
All of it is off unless a study row asks for it; with everything off every figure of the engine is unchanged (guard test; 8 new unit tests).

**The top tail (switch `WEALTH_TAIL`, row option `wt`).**
- *Where it starts.* A rule fixed before it was applied: take the lowest cutoff from which the estimated Pareto exponent stops drifting (it stays within one standard error at every higher cutoff) and at which a more flexible form (the generalised Pareto) does not fit better. For the engine's families that is the 97.5th percentile of net worth, $6.16 million in 2022 dollars, with exponent 1.490 (standard error 0.136). Below that point the plain Pareto is rejected; above it the flexible form adds nothing.
- *How it is carried.* No adult is added. In each of the four household types the three households with the highest wealth rank become tail households. The tail runs from the cutoff up to the net worth at which only one family of that type is left in the country; it is cut into three layers, each rarer than the one below by the same ratio; each tail household takes one layer and draws its exact place in it from a random stream of its own, identical in the programme run and the no-programme run. Each adult carries a weight: a tail adult stands for the small share of people in its layer, everyone else for slightly more than one person.
- *Weights enter measures only.* No rule of the model reads a weight. Prices, the Source's payout, taxes and every decision are computed exactly as before.
- *New weighted measures:* wealth poverty, basket poverty, the wealth Gini, the top 0.1%, 1% and 10% shares, the bottom half's share.

**Business owners (`bo`).** Each household draws once whether it holds private-business equity, with the survey's share for its wealth group (5% of the poorest group, 45% of the group from the 90th to the 99th percentile, 87% of the top 1%). Owners and non-owners take their own survey balance sheets. Part 1 gave every household the group average.

**The income wealth pays (`ci`).** Each year an adult receives interest on nominal assets, dividends on shares, and rents and business income on other real estate and private business, at the survey's rates for the household's wealth group. It is cash income: it counts in disposable income and basket poverty, and what is not spent is saved. Income from a sole proprietorship or farm is not added, because it is self-employment income and already inside the earnings the model draws from the Current Population Survey; it is reported apart from wages (about $1,200 per adult in Reference).

**Returns that rise with wealth.** The survey's rates already rise at the top (interest: 1.09% of nominal assets for the top 1%, 0.1-0.4% below). In addition, with the tail on, the interest rate of the top 0.1% and 0.01% is raised by the ratios in Smith, Zidar and Zwick (2023): 0.91%, 1.52% and 3.79% from the 99th percentile up. A reading applies Campbell, Robbins and Wylde's (2025) higher real-estate returns for top earners to the top wealth group.

**The owners rule.** Claude's reading of the design, from the Hub and the record of Duke's answers of Oct 1-2, 2026: a private business that accepts Basic Units earns a conversion premium; in the release row it passes that premium to its customers as lower prices, after matching the profit share for its workers, and nothing goes to owners. Under the earlier reading (owners keep it) the model shared it among all adults by positive wealth, because it had no shares. It can now be shared by shares plus private-business equity held (option `own: 'eq'`).

## What the sources said, where it differs from the plan
- **Smith, Zidar and Zwick:** "fixed income at the top about 3.5 times the average" is the top 0.01% only. From the bottom up to the 99.9th percentile their rates are flat (0.77-0.91%).
- **Campbell, Robbins and Wylde:** the 45.3% and 75.7% of capital gains go to the top 1% and 10% of people **ranked by income including the gains**, not by wealth. On that ranking the model gives 37.6% and 73.8% under the main reading (25.8% and 63.7% without the tail and capital income). A comparison, not a target.
- **Business ownership:** 14.6% of families hold business equity (the survey's question, used here). The Bulletin's "20%, 14% in the bottom half of income, nearly half of the top tenth" also counts the self-employed with no business equity. On the survey's question: 8.3% and 41.0%. The model: 15.0% of adults, 9.9% in the bottom half of money income, 32.3% in the top tenth. The model's link between income and wealth is weaker than the survey's at the top: a gap, reported.
- **The Forbes 400** (2022: 400 entries, $4.0 trillion, lowest $2.7 billion) was used as a check only. The tail fitted to the survey alone puts 554 families above $2.7 billion, holding $4.1 trillion (295 to 1,043 families over one standard error of the exponent). Each list entry is counted as one family; 35 entries say "& family". Adding the list to the survey raises the survey's top 1% share by 1.8 points (Bricker, Hansen and Volz 2019 report about 1.5 for earlier years).

## Results

**The start, beside the survey** (Reference; means over 100 seeds; tables section 1)

| | Top 0.1% | Top 1% | Top 10% | Bottom 50% | Gini | Mean net worth per adult |
|---|---|---|---|---|---|---|
| Model, no tail | 2.5% | 20.8% | 64.7% | 3.6% | 0.771 | $512,300 |
| Model, main reading | 11.6% | 30.1% | 70.4% | 3.0% | 0.807 | $641,200 |
| Survey, same families, by adult | 11.8% | 31.5% | 69.3% | 3.2% | 0.801 | $599,300 |
| Fed's accounts, all households, 2022 | 13.1-13.6% | 29.3-30.4% | 65.7-67.2% | 2.6-2.7% | | |

Gaps: the model's mean net worth is 7% above the survey's, because a Pareto tail holds more at the very top than the survey records (the survey leaves the Forbes families out by design). The median is $127,600 against the survey's $135,600, as before the tail.

**What moves the start** (top 1% share): the exponent one standard error either way, 35.1% and 26.8%; the cutoff at the 99th percentile, 33.3%; the flexible form above the main cutoff, 28.9%, and from the 90th percentile, 23.6%; six tail households per type, 31.7% (30.1% with three); one per type, 24.8% with a wide interval (22.1 to 27.7), as the unit test predicted. The exponent is the assumption that matters most.

**The programme's effect on concentration at year 20** (points; programme minus no programme, same seeds; 95% intervals in the tables, sections 2-7)

| | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| Top 1% share, main reading | −1.14 | −1.75 | −1.11 | −1.70 | −0.88 | −1.47 |
| Top 1% share, no debt relief | +1.23 | +0.59 | +0.74 | +0.12 | +0.76 | +0.39 |
| Top 1% share, real assets follow half of inflation | −10.4 | −15.2 | −9.9 | −15.7 | −3.3 | −14.9 |
| Top 0.1% share, main | −0.47 | −0.73 | −0.46 | −0.71 | −0.37 | −0.61 |
| Top 10% share, main | −3.28 | −4.56 | −3.14 | −4.39 | −2.38 | −3.95 |
| Bottom 50% share, main | +2.61 | +3.68 | +2.45 | +3.47 | +1.61 | +3.16 |
| Bottom 50% share, no debt relief | +0.76 | +1.82 | +1.03 | +1.99 | +0.44 | +1.66 |
| Wealth Gini, main | −0.043 | −0.061 | −0.039 | −0.057 | −0.027 | −0.052 |
| Wealth Gini, no debt relief | −0.004 | −0.022 | −0.010 | −0.026 | −0.002 | −0.020 |
| Top 1% share of business equity, main | +0.36 | +0.32 | +0.10 | +0.07 | +0.06 | +0.05 |

Reading it:
- Across every tail reading (the exponent, the cutoff, the form, the number of tail households) the effect on the top 1% share stays between −0.7 and −2.0 points. The tail's shape does not decide the sign.
- Debt relief does. The bottom half gains share in every reading (its gains do not all come from debt relief), and the Gini falls in every reading; but the top 1% share rises once fixed-rate debt reprices. By the preregistered rule the direction of the programme's effect on the top 1% share is reported as not established.
- If homes, shares and businesses kept up with only half of the programme's inflation, top shares would fall by 10-15 points: wealth at the top would be inflated away, as in the all-cash reading. That is a statement about the assumption, not a prediction.
- One reading must be read as a stress test: if the top 0.01%'s higher interest rate also multiplied the pass-through of 30-45% inflation, the top 1% share would rise by 3 to 23 points. The paper measured the gap at about 2% inflation; nothing supports carrying the ratio to these rates, and the main reading does not.
- The top 1% of adults hold 57% of private-business equity at the start (47% before owners and the tail were modelled) and 59% at year 20 without the programme; the programme adds 0.1 to 0.4 points.

**Does the tail move anything else?** (check 2; tables section 12) With the tail alone switched on, programme inflation changes by 0.001 to 0.005 points a year, and the programme's effects on the cost of living and basket poverty by 0.00 to 0.02 points, far inside those effects' own intervals (0.2 to 0.5 points). The preregistered check passes. A caution for anyone reading these rows: the model's older, unweighted measures count the tail's 18 adults as ordinary adults, so the unweighted Gini and top shares are not valid with the tail on, and unweighted poverty rates shift a little through who is counted (up to 0.7 points on the cost-of-living measure under C2.2). The weighted measures are the ones to use.

**Wealth poverty with everything on** (the programme's effect, points; weighted)

| | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| All wealth is cash | +21.5 | +0.7 | +45.0 | +30.2 | +24.8 | +41.7 |
| Part 1, corrected edges | −12.6 | −18.2 | −13.2 | −20.3 | −7.1 | −18.8 |
| Main reading (owners, capital income, tail) | −12.5 | −18.1 | −13.0 | −20.2 | −7.0 | −18.6 |
| Main, no debt relief | −6.7 | −13.3 | −7.8 | −15.6 | −2.8 | −13.3 |
| Main, real assets follow half of inflation | −2.1 | −14.0 | +9.2 | −7.9 | +3.7 | +0.3 |

Part 1's findings stand: a reduction under the main reading in every environment; about half of it gone for the release design without debt relief; the sign not established for the release design if real assets lag inflation. Median real wealth: +$36,000 (release) and +$58,600 (C2.2) in Reference under main, but −$46,000 and −$25,100 without debt relief.

**Income.** With capital income and the tail the top 1% of adults receive 8.1% of disposable income at the start (4.5% without either). At year 20 the programme lowers that share by 0.5 points (release) and 1.9 (C2.2) in Reference. Basket poverty is a little lower in both runs once wealth pays income (25.2% of adult-years without the programme against 26.8%), and the programme's cut is about one point smaller (−15.9 and −23.2 in Reference against −16.7 and −24.6).

**The owners readings** (no tail; tables section 16). If owners kept the private premium, shared by equity held: the programme's effect on the top 1% share of wealth would be −0.61 (release) and −0.64 (C2.2) in Reference instead of −0.98 and −1.49; the top 1% share of income would rise by 2.0 and 3.3 points instead of falling; wealth poverty would fall 2.9 and 4.5 points less; basket poverty 4.3 and 4.2 points less; and under C2.2 programme inflation would be 46% a year instead of 37%, because the premium reaches households as new dollars instead of lower prices. Shared by all positive wealth the pattern is the same, a little weaker. The release reading (lower prices) is the more equal one on every measure here.

## Checks against the preregistered rules
- Check 1 (unit tests, guard test): pass. Check 2 (the tail does not move the economy): pass.
- Recommended to the design freeze (S63): the tail (three per type, Pareto, cutoff by the rule), business owners and capital income as main-row candidates, with these readings beside every concentration result: no debt relief, half indexing, the exponent one standard error either way, and six tail households per type. Every concentration figure is read from the weighted measures.
- The direction of the programme's effect on the top 1% share is not established (it turns on the missing creditor side, not on the tail).
- No synergy is claimed: these rows are not a factorial design.

## Limits
1. **No lender.** A mortgage inflated away is a gain with no one who loses it. The concentration results turn on it. Building the creditor side is the next thing this part of the model needs.
2. **Weights in measures only.** The model economy holds about three times as many very wealthy households as the population. The check shows this moves prices and poverty negligibly at 500 adults; it must be rechecked at 10,000 adults and with any rule that reads wealth (the owners readings could not be run with the tail for this reason).
3. **One exponent for four household types**, though single parents have only 20 survey records above the cutoff; and a tail fitted to one survey year.
4. **The survey leaves out the Forbes families**; the fitted tail reaches them by extrapolation (554 families above the list's threshold against 400 listed), and the list's own valuations are not audited.
5. **Capital income** is untaxed here, does not change hours worked, uses one year's survey rates (2021, a year of low interest), and leaves out returns kept inside retirement accounts. Without the programme it grows from 11% to 16% of money income over 20 years, because assets gain value and wages in the model do not grow: a drift of the baseline, not a forecast.
6. **Income and wealth are less tightly linked at the top than in the survey** (owners in the top tenth of income: 32% against 41%).
7. **Returns** are price gains from 1953-2022 and survey income rates; private businesses take the share market's rate, with no series of their own.
8. **Political influence** is not modelled; the model has no mechanism for it.
9. Tested with wealth by asset class only, without ageing, the capacity price rule or adults outside the labour force; those combinations belong to the pairwise tests (S68).
