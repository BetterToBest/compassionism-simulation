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

The fix is a candidate. It becomes the corrected model only if the preregistered rerun passes its checks and shows the swing gone in every environment. An outside reading by a model from another maker (research-update `audits/2026-11-18-s90-reading.md`) found the diagnosis, the defect call and the algebra sound.

## The rerun, part 1 (Nov 19, 2026)

**The swing is gone.** The preregistered measure is the mean change in BU spent from one year to the next, years 2 to 12. It was computed for each of seeds 1 to 20 and then averaged, on the full-coverage main row with 500 adults over 20 years.

| Environment | Paid a year late | Set at the sale | At the sale over late |
|---|---|---|---|
| Reference | 18.33% | 2.27% | 0.124 |
| Adverse | 16.58% | 3.33% | 0.201 |
| Stress | 14.24% | 3.19% | 0.224 |

The rule set before the run was that the fix works if the measure at the sale is below half the late one in every environment. That holds in all three. Averaging the seeds into one series first gives the same answer (ratios 0.096, 0.168 and 0.185). The files are in compassionism-sim-results, `s90-swing-b8ccd8d`; the tools are `dev/tools/s90_swing.js` and `dev/tools/s90_trace.js --from`.

**The books balance.** The engine's accounting checks were run on both designs with the price set at the sale, for seeds 1 to 5 in each environment. None failed, and the premium identity was checked 105 times per row (`dev/tools/s90_acct.js`).

**The full rerun has started.** It covers the main rows: no programme, and both designs under both rules, for seeds 1 to 500 in all three environments at 20 and 40 years. It runs on GitHub Actions with the results repository's job `runner/jobs/s90.js` and lands in `s90-sale-<environment>-<years>-b8ccd8d`. On a two-seed trial, the no-programme and late-price rows matched the published main rows on all 5,862 values, as the first preregistered check requires. The tables come from `dev/tools/s90_tables.py`, which runs the folder checks first and stops if any fails. The effects on poverty and wealth will be added here once the six folders are complete. Until then the fix stays a candidate, and the published figures stand.
