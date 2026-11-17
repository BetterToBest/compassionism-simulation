# The v5.9 model on the findings page: the text for the v5.9 release

Nov 15, 2026. The words the v5.9 release puts on the findings page for v5.9, beside v5.6. Every sentence comes from the v5.9 reports (`dev/reports/s64-round2-overview.md` and the seven question reports) and follows the preregistered rules of research-update `prereg/2026-11-s63-round2-freeze.md`: the range across the preregistered readings comes before the main row's figure (rule 1); every wealth figure names the price rule it rests on and has its erosion share beside it (rule 6); every inflation figure has the backing statement beside it (rule 4); the financed rows are never led with. Figures are Reference at 20 years unless a sentence says otherwise; the tables give every environment and horizon. Charts: `dev/runs/s64-round2/charts/` (made by `python3 dev/tools/s64_charts.py`; `index.html` previews them with their captions).

The v5.9 release may shorten any paragraph; it may not drop a qualifier that a rule attaches to a figure, or any of the unfavourable results.

## The answer in ten seconds (v5.9)

**Headline cards.** With Compassionism (the full-coverage design, built to meet NEEC's criterion C2.2), against no programme, Reference, 20 years, main row:
- *Below 30 days of basic living:* 0.9% of adult-years, against 19.6% (−18.7 points).
- *Below the cost of living (the basket of essentials):* 3.7% of adult-years, against 36.1% (−32.4 points).
- *Too little wealth (under $25,000), yearly average:* 6.0% of adults, against 24.6% (−18.6 points).
- *Median real wealth at year 20:* $432,300, against $223,900 (+$208,400). Rests on full backing (corrected Nov 17, 2026: it said today's price rule, which full backing barely tests); 1.0% of the gain is the erosion of opening balances (in the programme's favour).

Card footnote (required): "Main row: every dollar the programme pays is matched by new output, as the design states (a design parameter, not a model estimate). The model's own mechanism for new output reaches about 1% of that. See *How much new output backs the payout*."

**One-sentence answer.** Across all 62 preregistered readings, both designs lower all three poverty measures and raise median real wealth, in every environment and at both horizons; the full-coverage design does about 1.4 to 7.1 times as much as the opt-in design. These results hold when every dollar paid is matched by new output, which is the design's statement and not something the model shows; with the model's own backing mechanism, prices rise 15 to 53 points a year.

## How sure we are: the range across readings

Chart: `spec-c22-fgt0PY-20.svg` first (basket poverty), then basic living, wealth poverty and median wealth; programme inflation last. Each has the financed rows beside it.

- Across the 62 preregistered readings, the full-coverage design lowers basket poverty by 25.9 to 33.3 points; at the main row, 32.4 points (seed interval 32.2 to 32.5). The opt-in design lowers it by 16.2 to 22.3 points; at the main row, 20.9 (20.8 to 21.1).
- The full-coverage design lowers adult-years below 30 days of basic living by 16.5 to 19.7 points (main row 18.7) and wealth poverty by 15.7 to 19.7 points (main row 18.6); the opt-in design by 10.7 to 13.0 (12.3) and 9.0 to 12.7 (10.9).
- Across the 62 readings, the full-coverage design raises median real wealth by $187,600 to $659,600; at the main row, $208,400 ($207,100 to $209,900); the opt-in design by $84,600 to $282,100 (main row $99,400). These figures rest on full backing (corrected Nov 17, 2026: this sentence also said they rest on today's price rule, but at full backing almost no unmatched money reaches prices, so the price rule is barely tested there; below full backing they rest on it). Less than 3% of any wealth figure is the erosion of the balances adults held at the start, and it works in the programme's favour: slightly higher prices lower what net debtors owe in real terms (if all wealth were cash, it would work against it, by at most 5.3%). The widest part of the range comes from how much of their spare cash adults spend.
- Every one of these curves is robust: at every reading the effect keeps its sign and its interval excludes zero (48 of 48 poverty and wealth curves, three environments, two horizons). In Stress the opt-in design keeps every sign but loses about two thirds of each effect (basket poverty −7.7 points), because Stress lowers take-up to 40% and the PTF share; the full-coverage design's effects grow there (basket poverty −40.1).

Caption for every curve chart: "Each dot is one preregistered reading, sorted by its effect, with its 95% seed interval. The seed interval covers the model's randomness only, not the choice of reading; the spread of the dots shows that."

## Prices, and how much new output backs the payout

Chart: `backing-c22-20.svg` (and the opt-in design's beside it).

At the main row, programme inflation is 0.0 to 0.2 points a year above no programme, which is no material change, at every reading. **The main row assumes that every dollar the programme pays is matched by new output**, as the design states (a design parameter). The model's own mechanism for new output reaches 0.2 to 1.9% of the payout (14 to 20% if its ceiling is removed). Inflation stays under 5% a year only above about 86 to 90% backing (74 to 77% for the opt-in design in Stress), and runs at 15 to 53 points a year at the mechanism's own point. The poverty effects barely depend on backing; inflation and median wealth do. *Note (Nov 17, 2026):* below full backing, the poverty effects hold because the model has no limit on what the economy can supply. Demand never runs into what can be produced, wages follow prices in full, and the Basic Unit and the cost-of-living basket follow the same prices. With no new output, the real goods the programme's recipients gain are paid for only by holders of savings and lenders, through higher prices. So these figures are not evidence that the design works without backing. At no backing and 40 years, the opt-in design lowers median real wealth.

## Paid for by a contribution instead (shown, never led with)

Chart: the lower row of each curve chart.

If the programme is paid for by a contribution, with the rest borrowed, the full-coverage design needs a mean contribution of 63 to 77% of all money income and lowers basket poverty by at most 17.5 points (in Stress at 20 years it raises it, +0.6); the opt-in design, at 46 to 71% of wages, raises basket poverty by up to 9.6 points. Government debt stays under GDP at the main financed rows, but 46 of the 48 financed poverty and wealth curves are fragile (the two that hold are the opt-in design's basic-living effect in Reference, at both horizons), depending on how the contribution is set up. These rows were run without the weighted top tail.

## Who gains

The full-coverage design lowers the top 1%'s share of wealth by 4.6 points (31.6% to 27.0%) and raises the bottom half's from 2.9% to 9.2%; the opt-in design moves both about half as far. Families in debt fall from 21.9% to 0.7% (full coverage) and 7.4% (opt-in design). In dollars the gains are spread across the distribution, so they are largest in proportion at the bottom: the full-coverage design raises real wealth by $128,000 at the 10th percentile (from −$2,300) and $218,800 at the 90th. Below the top fifth of starting wealth, the slightly higher prices of the programme run lower what adults owe, a gain of 0.5 to 1.7% of their wealth gain; at the top, where money is lent, they are a loss. Adults outside the labour force (disability, early retirement, care, school) stay far more often below the cost of living than adults in it: under the full-coverage design, 8.5 to 16.6% of their adult-years, against 1.8%; under the opt-in design, 28.8 to 58.5%, against 9.5% (no programme: 54 to 82%, against 29%).

## Unfavourable results

Shown together, with the same prominence as the headline:
- Programme inflation is above no programme in every cell: immaterial at the main row, 18 to 53 points a year at no backing.
- Fewer adults work: participation falls 1 to 5 points (adults who leave work for the programme), with their earnings forgone.
- Less movement out of the lowest wealth fifth: 69.8% of adults who start there are still there at year 20 under the full-coverage design, against 66.3% without the programme.
- Labour's share of money income falls by 11.7 to 30.5 points in Reference at 20 years (1.1 to 32.1 across every cell), because the programme's payments are income that is not wages.
- The opt-in design's effects shrink by two thirds in Stress.
- 46 of 48 financed poverty and wealth curves are fragile (the opt-in design's basic-living effect in Reference holds), and the opt-in design paid by a contribution on wages raises basket poverty.

## What no figure here covers

The seed intervals measure the model's randomness only. They do not cover the choice of main row or full backing (a design statement); the readings the screen held fixed; Stress, which was not screened; or the engine's structure: a fixed population in the main row (no ageing, births or deaths; added Nov 17, 2026), one price rule for the whole economy, no central bank, no migration, no value of care, community work or new ventures, PTFs modelled from the Hub's statements and measured costs, 500 adults (a 10,000-adult pair agrees on hours and the top of the wealth distribution). The financed rows leave out the weighted top tail. The model has not been reviewed by an independent economist.

## Where each figure comes from (basis class: simulation release and command)

Engine `104691f`, v5.9 batch, seeds 1-500, run on GitHub Actions Nov 14-15, 2026, as frozen in research-update `prereg/2026-11-s63-round2-freeze.md` (registered on OSF, https://osf.io/msdzk/overview). Results: compassionism-sim-results `r2-<part>-<env>-<years>-104691f/`; tables `r2-tables-104691f/`; erosion trace `r2-erosion-104691f/`. Commands: `dev/tools/s64_tables.py`, `dev/tools/s64_erosion.js` and `s64_erosion_table.py`, `dev/tools/s64_charts.py`.
