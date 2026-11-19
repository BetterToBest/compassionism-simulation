# The BU's two-year swing: a private business's lower BU price paid a year late

Nov 18, 2026. Written by Claude. A plain-words report of the research-update plan's step on this swing; the full decision is in `dev/DECISIONS.md` (Nov 18, "the two-year cycle in the BU's relief").

## What was seen

In the main row (full backing, flat prices; Reference environment, seed 1, 500 adults), the Basic Units (BU) each adult spends on the cost of living swing from year to year: $22,838 in years 0 and 1, then $10,969, $21,452, $13,819, $19,472, $16,202, and so on. The swing shrinks each year but takes more than ten years to die out. Meanwhile the BU paid each month keep their value and the cost of living hardly moves. The swing is in every programme row, and it was behind the swing in the cash share that the supply study found.

## What causes it

The BU an adult receives in a year (about $24,900) are less than the essentials bill (about $30,000), so every BU is spent unless a price cut lowers the bill first. Two price cuts do that, and both are paid from the businesses' conversion premium (an essential-service business converts the BU it accepts into dollars at three times face value; the extra is the premium):

1. the cut that community-owned businesses (PTFs) give from their share of the premium;
2. the lower BU price that privately owned businesses give from theirs.

A trace of one run, turning each cut off in a copy of the engine (never the engine itself), shows that the private businesses' price causes the swing. With the community cut off, the swing stays; with the private price off, it goes.

The private price was paid from **last year's** premium. A large cut this year means fewer BU spent this year, so less premium, so a smaller cut next year, and so on: the BU spent alternate above and below the level where the cut equals the premium it earns. Average incomes swing with them ($72,358, $92,808, $81,544, $98,970 in years 1-4), because the conversion and the workers' share of the premium follow the BU spent.

## Design or defect

A defect. Duke's design (Oct 1) sets the private price at the sale:

> A privately owned ESP cuts its prices for customers paying in BU so that it stays revenue neutral. At a 3x conversion rate, a $9 / $12 / $15 menu becomes $3 / $4 / $5 in BU.

The model's own decision for that step said the same ("one BU buys as many essentials as the conversion rate in dollars"), but the code paid the premium a year late. The lag is not in the design, and it is what makes the swing.

## The fix (built, off until a rerun)

A new option of the surplus split, `vAt: 'sale'`, sets the private price at the sale. One BU spent at a private business buys 1 + vK dollars of essentials, where vK is the premium the business will earn on that BU (after the conversion tax and the share kept for business payroll) less the workers' share of it. In the main row vK is about 0.90 at first and 0.81 once community capacity is reached (0.79 and 0.71 in the Stress Test): a BU spent there buys about $1.90 of essentials rather than Duke's $3, because the conversion tax, payroll and the workers' match come out of the premium too. That is the same price, on average, as the lagged rule settled to; only its timing changes. The cut is paid as an advance, and next year's premium repays it exactly. One small part cannot be known at the sale: payroll BU that a business could not pay out and converts the next year. That part is shared a year late, as before ($305 per adult in year 1, $73 in year 2, $4 in year 3, then nothing in the main row).

With the option on, the swing is gone in all three environments: the BU spent per adult in Reference run $16,815, $16,590, $17,392, $17,592, $17,981, and stay within $16,236-18,195 after that, and incomes rise smoothly.

The option is off by default, so every published figure is unchanged and the registered v5.9 model can still be reproduced (the guard test is identical in every output).

## What it reaches

Every programme row uses the private rule, so every published programme figure since v5.0 (Oct 2, 2026) is reached. This includes the v5.9 main rows and readings, the central-bank and history studies, and the supply study. A first look on two seeds (not a result) shows small changes, all in the programme's favour: the cut in basket poverty grows by about 0.6-0.7 points (Reference: 32.3 to 33.0 points), the deepest-poverty measure (FGT2) by about 0.1, and median real wealth by $200-1,200. The preregistered rerun (research-update `prereg/2026-11-s90-private-price-at-sale.md`) will measure the change on 500 paired seeds in all three environments. Its results will be published whichever way they come out. Until then the swing is a stated limit of every programme row.

## What the community businesses' cut does

The community businesses' cut stays as it is. Duke's text for them ("The converted dollars go one-third each to lower prices, reinvestment in capacity and profit-sharing with the ESP's workers") says how their premium is split, not when. Paying the price third once the year's premium is known is therefore a modelling assumption where the design is silent, not something the design requires. With the private price at the sale, it shows no swing. Paying it at the sale as well is a possible later reading.

## Status

*Superseded Nov 19, 2026 by part 2 below: the checks passed and the fix is the corrected model.* The fix was a candidate. It would become the corrected model only if the preregistered rerun passes its checks and shows the swing gone in every environment. An outside reading by a model from another maker (research-update `audits/2026-11-18-s90-reading.md`) found the diagnosis, the defect call and the algebra sound.

## The rerun, part 1 (Nov 19, 2026)

**The swing is gone.** The preregistered measure is the mean change in BU spent from one year to the next, years 2 to 12. It was computed for each of seeds 1 to 20 and then averaged, on the full-coverage main row with 500 adults over 20 years.

| Environment | Paid a year late | Set at the sale | At the sale over late |
|---|---|---|---|
| Reference | 18.33% | 2.27% | 0.124 |
| Adverse | 16.58% | 3.33% | 0.201 |
| Stress | 14.24% | 3.19% | 0.224 |

The rule set before the run was that the fix works if the measure at the sale is below half the late one in every environment. That holds in all three. Averaging the seeds into one series first gives the same answer (ratios 0.096, 0.168 and 0.185). The files are in compassionism-sim-results, `s90-swing-b8ccd8d`; the tools are `dev/tools/s90_swing.js` and `dev/tools/s90_trace.js --from`.

**The books balance.** The engine's accounting checks were run on both designs with the price set at the sale, for seeds 1 to 5 in each environment. None failed, and the premium identity was checked 105 times per row (`dev/tools/s90_acct.js`).

**The full rerun has started.** It covers the main rows: no programme, and both designs under both rules, for seeds 1 to 500 in all three environments at 20 and 40 years. It runs on GitHub Actions with the results repository's job `runner/jobs/s90.js` and lands in `s90-sale-<environment>-<years>-b8ccd8d`. On a two-seed trial, the no-programme and late-price rows matched the published main rows on all 5,862 values, as the first preregistered check requires. The tables come from `dev/tools/s90_tables.py`, which runs the folder checks first and stops if any fails. The effects on poverty and wealth are in part 2, below.

## The rerun, part 2 (Nov 19, 2026): what setting the price at the sale changes

**Every check passed before any effect was read.** All six folders are complete: 500 seeds in each row, the engine commit `b8ccd8d`, a clean engine, and every checksum verifies. The no-programme row and both late-price rows equal the published main rows seed by seed, on all 1,465,500 values in each environment and horizon. The accounting checks passed (part 1). So, under the rules set before the run, the price at the sale is now the corrected model. Its figures replace the main rows' figures at the next release, with an entry in the Hub's corrections log; the version number of that release is Duke's to set. The late-price figures stay published as the record of v5.9, which is the model registered on OSF.

**The poverty and wealth effects grow slightly, in the programme's favour, in every case.** Below, the effect against no programme as published (price paid a year late) and with the price set at the sale, for the full-coverage design in Reference at 20 years. Each is a mean over 500 paired seeds with its 95% interval.

| Outcome | Paid a year late | Set at the sale | Change |
|---|---|---|---|
| Below 30 days of basic living (points) | −18.72 (−18.84 to −18.61) | −18.80 (−18.92 to −18.69) | −0.08 (−0.08 to −0.07) |
| Basket poverty (points) | −32.39 (−32.54 to −32.24) | −32.95 (−33.10 to −32.79) | −0.55 (−0.56 to −0.54) |
| Too little wealth, yearly average (points) | −18.60 (−18.72 to −18.49) | −18.90 (−19.01 to −18.78) | −0.30 (−0.30 to −0.29) |
| Median real wealth (weighted, year-0 dollars) | +$208,444 (207,067 to 209,870) | +$209,026 (207,655 to 210,439) | +$582 (456 to 703) |
| Programme inflation (points a year) | 0.15 (0.15 to 0.15) | 0.15 (0.15 to 0.15) | less than 0.001 |

Across both designs, three environments and both horizons (24 cells for the four poverty and wealth outcomes), every change is in the programme's favour and every interval excludes zero, also after the Holm adjustment across the five outcomes in each cell:

| Outcome | Full-coverage design | Opt-in design |
|---|---|---|
| Below 30 days of basic living | 0.04 to 0.08 points lower | 0.07 to 0.22 points lower |
| Basket poverty | 0.28 to 0.59 points lower | 0.04 to 0.26 points lower |
| Too little wealth, yearly average | 0.15 to 0.38 points lower | 0.06 to 0.25 points lower |
| Median real wealth | $481 to $1,525 higher | $110 to $605 higher |
| Programme inflation | under 0.0001 points a year | under 0.001 points a year |

The changes are about half as large at 40 years as at 20. That fits a swing that dies down: most of the difference comes in the early years, and a 40-year average spreads it over twice as many years.

**Smaller readings.** Poverty severity (the squared poverty gap) falls by a further 0.01 to 0.08 points. The weighted readings at the last year barely move (basket poverty within 0.06 points either way; too little wealth 0.00 to 0.10 points lower), because the late price cost adults more in some years than in others, and a single year's snapshot catches only one phase of that. With the price at the sale, private businesses take slightly fewer BU in the full-coverage design ($13 to $109 less spent per adult-year, and $17 to $119 more left unspent), real wage earnings are $3 to $64 lower per adult-year across both designs, and programme cost is $107 to $494 higher per adult-year (opt-in design: $41 to $206). The median real disposable income in the last year moves by −$16 to +$338. No secondary reading changes sign.

**The findings page (the preregistration's third question).** No statement on the page changes sign. Of the 60 main-row effects the v5.9 section prints (five outcomes, two designs, three environments, two horizons), 45 change in their last printed digit, none falls outside the printed range across the preregistered readings, and programme inflation does not change as printed anywhere. The four headline cards (full-coverage design, Reference, 20 years) would read:

| Card | Printed now | At the sale |
|---|---|---|
| Below 30 days of basic living | 0.9% (−18.7 points) | 0.8% (−18.8 points) |
| Below the cost of living | 3.7% (−32.4 points) | 3.2% (−32.9 points) |
| Too little wealth, yearly average | 6.0% (−18.6 points) | 5.7% (−18.9 points) |
| Median real wealth at year 20 | $432,297 (+$208,444) | $432,879 (+$209,026) |

The page's prose statements hold as written: both designs lower all three poverty measures and raise median real wealth in every environment and at both horizons; programme inflation shows no material change at the main row; the opt-in design's effects still shrink by about two thirds in Stress (basket poverty: 7.8 against 21.2 points in Reference). An inspection beyond the preregistered outcomes, on the 180 distribution and work effects behind the "Who gains" and "Unfavourable results" lists (seed means only), found no sign change. Two figures on the page were not rerun and stay as published: the share of the wealth gain that is the erosion of opening balances, and the readings and financed rows. The page now carries a dated note saying so; its figures change only at the release.

**What this means.** The defect was real and is fixed, and it worked slightly against the programme: paying the private price a year late made what a BU bought swing from one year to the next. Correcting it strengthens every published poverty and wealth effect of the main rows by less than six-tenths of a point and changes no conclusion.

**Other studies.** Every other published study with programme rows paid the private price a year late: the readings, financed rows and 10,000-adult rows of v5.9; the central-bank study; the history study; the study of limits on supply; the three visual-suite runs; and the v5.0 to v5.6 panels. Each report now carries a dated note giving the main rows' change above. None of them is being rerun now; a rerun of any one would be its own preregistered amendment.

**Files.** Tables: compassionism-sim-results `s90-tables-b8ccd8d` (every cell with its interval, the checks, the findings-page reading, `run.txt`, `SHA256SUMS`). Commands: `python3 dev/tools/s90_tables.py RESULTS OUT --swing RESULTS/s90-swing-b8ccd8d/swing.json --acct RESULTS/s90-swing-b8ccd8d/acct.json`, then `python3 dev/tools/s90_page_check.py OUT/s90-summary.json RESULTS OUT/page-check.md`. Preregistration: research-update `prereg/2026-11-s90-private-price-at-sale.md`.
