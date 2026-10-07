# Four calibrations: making the "no programme" run look more like the US

Oct 7, 2026 · v5.3, plan item B7 · Claude · 500 paired runs in each of the three environments · labelled readings; which ones join the main result was recorded before the v5.3 restudy

## What was asked

Every result compares Compassionism with "no programme" on the same simulated people. So the no-programme run is the yardstick, and the closer it looks to the US, the more the comparison means. The v5.2 check against US data found its largest gaps there. The plan asks for four calibrations, each first as a labelled reading:

1. **Starting wealth for households** from the Federal Reserve's Survey of Consumer Finances (SCF), by household type.
2. **Spending that depends on income.** In the model everyone paid the full living-wage basket every year, so 46% of adults were in debt by Year 7, against 12.6% in the survey.
3. **Earnings that follow age** (with ageing on), so families' incomes follow their life stages.
4. **The advancement rule in readable units**: the monthly surplus at which a participant has an even chance of moving up an octave (FBS50).

Each is off by default, adds no random numbers, and applies to the no-programme run too, since it describes the population, not the programme.

## What each does

1. **Wealth from the survey.** Each household starts with the SCF 2022 net worth for its type: couples with or without children, single parents, single adults, all with a head aged 25 to 66 and wages. Within each type, households with higher wages tend to hold more, as in the survey. Before this, a couple started with about $80,000; the survey's typical couple with children holds $272,609.
2. **Spending graded by income.** When someone's income in a year is below their costs, they spend less than the full basket. The amount comes from the Bureau of Labor Statistics Consumer Expenditure Survey, 2024: each 1% more income means about 0.56% more spending. The poverty measures still compare income with the full cost of living, so spending less never counts as being better off: it is hardship, and the measures still show it.
3. **Earnings by age.** Wages follow the shape of US median earnings by age (Bureau of Labor Statistics, 2026): a 25-year-old earns about 73% of the average, a 45-year-old about 108%. The average wage is unchanged.
4. **FBS50.** The advancement rule's coefficient is now also read as a monthly surplus: between $524 and $4,191 a month gives even odds. Spreading that range evenly, or doubling it, was tested.

## How close the yardstick now comes to US data (no programme, Year 7, Reference)

| Share in debt (median net worth) | Model before | With survey wealth | With graded spending | With both | US survey |
|---|---|---|---|---|---|
| All households | 41.1% ($44,638) | 34.6% ($124,537) | 27.6% ($69,366) | 26.1% ($159,088) | — |
| Couples with children | 51.6% ($882) | 38.0% ($161,768) | 31.8% ($65,468) | 25.1% ($236,590) | 4.9% ($272,609) |
| Couples without children | 7.5% ($187,021) | 9.7% ($432,640) | 2.7% ($190,336) | 7.4% ($436,613) | 4.4% ($357,505) |
| Single parents | 88.3% (−$10,000) | 77.2% (−$10,000) | 75.3% (−$9,988) | 61.1% (−$8,925) | 16.3% ($49,503) |
| Single adults | 45.9% ($15,652) | 39.2% ($56,609) | 31.0% ($39,247) | 30.9% ($80,637) | 12.6% ($74,422) |

Both calibrations move the yardstick a long way toward the survey, especially for couples. Big gaps remain for single parents and single adults: their living-wage budgets, with childcare for single parents, are far above what the model's wages pay. The model's wages are also lower and less spread out than the survey's; that is a separate reading.

## What the 500 runs show (Compassionism against no programme, Reference)

| Measure | Households before | With survey wealth | With graded spending | With both |
|---|---|---|---|---|
| Adult-years below the cost of living | 46.0% → 13.3% | 45.5% → 13.6% | 45.1% → 13.9% | 45.1% → 14.0% |
| Adults with too little wealth at the end | 42.6% → 20.0% | 36.5% → 20.4% | 36.2% → 16.6% | 30.6% → 16.2% |
| Children below the cost of living | 74.4% → 24.0% | 73.1% → 24.4% | 73.4% → 24.8% | 72.6% → 24.9% |
| People in households with too little wealth (last year) | 50.5% → 25.0% | 42.9% → 25.5% | 43.9% → 21.1% | 36.0% → 20.6% |

**Adverse and Stress Test (households, too little wealth at the end):** Adverse goes from slightly better than no programme (76.5% → 73.8%) to worse (48.9% → 59.7%) with both calibrations. The Stress Test goes from worse (76.5% → 89.1%) to much worse (48.9% → 83.3%).

**What this means.**
- **Income results hardly move.** People below the cost of living fall by about 31 to 33 points either way, and children by 47 to 50 points.
- **Wealth results move a lot, and against the programme.** With realistic starting wealth and spending, far fewer people end with too little wealth when there is no programme. In the programme, prices rise fast (33-34% a year in Reference, 42% in Adverse) and wear down those larger savings. So the programme's advantage on wealth shrinks in Reference, and reverses in Adverse.
- This is the same finding as before, now measured against a more realistic yardstick. Savings unprotected from the programme's inflation are the programme's weak point.

**Earnings by age** (with ageing, adults alone) changes the results by about a point. **FBS50**: spreading or doubling it moves results by under half a point, because nearly everyone who takes part reaches the top octave within 20 years whatever the rule.

## How it was checked

- **Off means off.** Every earlier result is reproduced exactly with each switched off.
- **Each does what it says.** Starting medians by household type come out within 9% of the survey's, with the survey's link to wages. Every graded year follows the formula exactly. The earnings curve averages exactly 1. With FBS50 kept as it is, nothing changes.
- **The books balance.** Every accounting check passes in every run, including the new spending flow.

## Decisions made (full reasons in `dev/DECISIONS.md`, Session 39)

- The four readings and their sources, as above.
- Before the v5.3 restudy I recorded which of them join the main result. **Survey wealth and graded spending join**, with households, because the alternative assumptions have no source and are the yardstick's largest gaps with US data. **Earnings by age** stays with the ageing reading. **FBS50** is reported. The rule was set before any restudy result, so the results cannot choose it.

## Claude's reading of the design (please check)

None of these is a design question: they describe the US population the programme would serve, not the programme. One choice is mine and is labelled on the page: graded spending assumes people spend their full basket exactly when their income equals its cost.

## What you need to do

Nothing yet: this is one step of v5.3.

The runs and their exact commands are in `dev/runs/calib-check-ref.json`, `-adv.json` and `-st.json` (`node dev/tools/calib_check.js ENV 500`).
