# The 40-year horizon

Session 33, Oct 2, 2026. Written by Claude for Duke. Plain words; labels in parentheses are for the code.

## What changed

The page still opens on 20 years, the results you read and released. A new **Years** switch beside the environment buttons shows the same model run for 40 years: the same 500 adults, the same rules, the same 500 paired runs, with and without Compassionism. "Run it yourself" follows the switch too. The 20-year figures did not change (checked by comparing the full output before and after).

One thing to keep in mind when reading the 40-year view, and the page says it: **the adults in the model do not age.** Someone who starts at 45 is still working at the same job 40 years later, at 85. So the 40-year view shows where the same rules lead if they keep running, not what happens over a lifetime. Adding ageing, retirement and new young adults is the first improvement I suggest (see `v5-7-suggestions.md`).

## Results: 500 paired runs, Compassionism against no programme

| | Reference, 20 years | Reference, 40 years | Adverse, 20 years | Adverse, 40 years | Stress, 20 years | Stress, 40 years |
|---|---|---|---|---|---|---|
| Adult-years below 30 days of basic living (BLEI) | 18.7% vs 46.7% | **14.8% vs 46.6%** | 33.1% vs 60.0% | 51.7% vs 75.1% | 54.9% vs 60.0% | 72.3% vs 75.1% |
| Adult-years below the cost of living | 22.0% vs 55.2% | **15.3% vs 47.4%** | 42.1% vs 78.2% | 62.2% vs 86.7% | 65.6% vs 78.2% | 79.3% vs 86.7% |
| Adults with too little wealth at the end | 35.7% vs 52.0% | **15.3% vs 44.2%** | 87.1% vs 82.6% | 97.9% vs 94.5% | 90.6% vs 82.6% | 98.8% vs 94.5% |
| Prices: rise a year from the programme | 34.9% | 30.4% | 45.6% | 65.4% | 23.8% | 36.4% |
| Cost per adult a year (today's dollars) | $29,619 | $32,277 | $27,678 | $27,014 | $10,495 | $10,687 |
| Adults who did not take part, real resources a year | −$789 | −$1,636 | +$2,080 | +$3,295 | +$1,031 | +$1,404 |

The first figure in each cell is with Compassionism, the second with no programme. For every change shown, the 95% interval is well away from zero.

## What it means, in everyday words

- **At Reference, a longer run makes Compassionism look better on every measure.** By year 40, 15% of adults have too little wealth, against 44% with no programme (at year 20 it was 36% against 52%). The gain is confirmed on all three measures. Prices still rise about 30% a year from the programme, but wages and the allowance keep up, and people have longer to build savings.
- **In the Adverse Environment and the Stress Test, a longer run makes things worse, with and without Compassionism.** These environments repeat recessions and an automation wave for 40 years with no recovery, so even with no programme almost everyone ends with too little wealth (95%). Compassionism still keeps fewer people below the cost of living and below 30 days of basic living, but slightly more end with too little wealth, because prices rise very fast (65% a year in Adverse) and savings in the model earn no interest. In Adverse, people work 18% fewer hours by then.
- **Adults who do not take part** lose about $1,600 a year at Reference over 40 years (about $800 over 20). In Adverse and Stress they gain a little in resources, but more of them live below the cost of living.
- **The "decisive unknown" matters even more over 40 years.** If every dollar the Source pays were backed by new output, prices would not rise, and at Reference only 7% would end with too little wealth.

## Limits (as the page states them)

- The adults do not age, retire or die, and no one new arrives.
- Savings earn no interest, so very fast price rises wipe them out; a real economy would not work that way (suggestion 1 in `v5-7-suggestions.md`).
- The Adverse and Stress environments were designed for 20 years; over 40 they describe a long decline with no recovery, and even the no-programme world ends with almost everyone short of savings.

## What Duke should check

Only this: is showing 40 years as a second view, with 20 years still first, what you meant by "expand the horizon to 40 years"? If you would rather open on 40 years, it is a one-line change.

Reproduce: `node harness.js testbed 500 release ref --years=40 --json=dev/runs/release-panel-40-ref.json` (and `adv`, `st`, one process each), then `python3 dev/tools/merge_panel.py 40`. Full tables: `dev/runs/step19-release40-500-{ref,adv,st}.txt`.
