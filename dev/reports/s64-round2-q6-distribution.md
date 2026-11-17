# The v5.9 model, question 6: who gains, at the main row

Nov 15, 2026. The distribution measures' distribution measures on the v5.9 main row (full backing, a design parameter; today's price rule). Engine `104691f`, seeds 1-500, three environments, 20 and 40 years. Preregistered: research-update `prereg/2026-11-s63-round2-freeze.md` (Q6; secondary family, Holm within each table; Amendment 3 item 5). Results: compassionism-sim-results `r2-m-*-104691f/`. Tables: `dev/runs/s64-round2/s64-q6-distribution.md` (`python3 dev/tools/s64_tables.py`).

## In short

1. **Both designs make wealth and income more equal.** The full-coverage design, built to meet NEEC's criterion C2.2, lowers the top 1%'s share of wealth by 4.6 points (from 31.6% to 27.0%, Reference, 20 years) and the top 10%'s by 9.4 points; the opt-in design by 2.3 and 4.7 points. The bottom half's share of wealth rises from 2.9% to 9.2% (full coverage) and 5.8% (opt-in design).
2. **Income inequality falls under the full-coverage design, and barely moves under the opt-in design.** The full-coverage design lowers the Palma ratio (the top 10%'s income over the bottom 40%'s) from 2.68 to 1.64; the opt-in design raises it slightly, to 2.75 (+0.07, interval +0.06 to +0.08), and leaves the top 10%'s income share unchanged (+0.03 points, interval includes zero).
3. **Families in debt fall sharply:** from 21.9% to 0.7% under the full-coverage design and to 7.4% under the opt-in design.
4. **Gains are spread across the distribution in dollars, so they are largest in proportion at the bottom.** The full-coverage design raises real wealth by $128,000 at the 10th percentile (from −$2,300), $208,400 at the median and $218,800 at the 90th; real income by $32,300 at the 10th percentile (from $21,100) and $82,900 at the 90th.
5. **Two results are unfavourable or need care.** Mobility out of the lowest wealth fifth *falls*: 69.8% of adults who start in the lowest fifth are still there at year 20 under the full-coverage design, against 66.3% without the programme (72.2% under the opt-in design). The fifths are relative: when everyone gains, ranks change less. And **labour's share of money income falls by 30 points under full coverage** (82.5% to 52.0%) and 12 under the opt-in design, because the programme's payments are income that is not wages.
6. **Erosion of opening balances is a small gain below the top fifth and a loss at the top** (added Nov 15). In each of the lowest four fifths of opening wealth, adults owe more in money terms than they hold on average, so the slightly higher prices of the programme run lower their real debts: a gain of $80 to $2,200 per adult at year 20, 0.5 to 1.7% of the fifth's wealth gain. In the top fifth, where money claims are held, the erosion is a loss (in every cell but one: the opt-in design in Stress at 40 years). At the median it is at most 1.5% of the effect (question 1's report).
7. **Adults outside the labour force stay far more often below the cost of living than adults in it, under both designs** (added Nov 15). Without the programme, 54 to 82% of their adult-years are below the basket (disability, early retirement, care, school), against 29% for adults in the labour force (Reference, 20 years). The full-coverage design brings them to 8.5 to 16.6% (1.8% in the labour force); the opt-in design only to 28.8 to 58.5% (9.5%). Under the opt-in design more than half of the adult-years of adults out for school or disability stay below the basket (58.5% and 52.4%).

## The figures (Reference, effect against no programme; every cell is in the tables)

| Measure | No programme (20 y) | Full coverage, 20 y | Full coverage, 40 y | Opt-in design, 20 y | Opt-in design, 40 y |
|---|---|---|---|---|---|
| top 1% share of wealth (%) | 31.6 | −4.6 | −5.5 | −2.3 | −2.9 |
| top 10% share of wealth (%) | 71.6 | −9.4 | −10.8 | −4.7 | −5.6 |
| bottom 50% share of wealth (%) | 2.9 | +6.3 | +7.1 | +2.9 | +3.3 |
| top 1% share of income (%) | 11.4 | −3.2 | −4.6 | −0.9 | −2.0 |
| Palma ratio of income | 2.68 | −1.04 | −1.58 | +0.07 | −0.33 |
| stayed in the lowest wealth fifth (%) | 66.3 | +3.5 | +0.3 (interval includes zero) | +5.9 | +2.9 |
| stayed in the top wealth fifth (%) | 94.0 | −1.9 | −2.7 | −1.1 | −1.9 |
| labour's share of money income (%) | 82.5 | −30.5 | −26.8 | −11.7 | −9.7 |
| families in debt (%) | 21.9 | −21.3 | −18.7 | −14.6 | −14.0 |

Of the 23 measures per table, 19 to 23 have intervals excluding zero and survive Holm in every table. The ones that do not: the very top of the wealth distribution (the 99.9th percentile of the weighted tail; the 99th percentile in two Adverse and Stress cells), the rare move from the lowest to the top fifth (0.00-0.05% of adults), the opt-in design's top-10% income share (Reference and Stress, 20 years), the full-coverage design's staying in the lowest fifth at 40 years (Reference) and the opt-in design's staying in the top fifth in Stress.

## Erosion by fifth of opening wealth (added Nov 15)

Mean real-wealth gap (programme minus no programme) and mean erosion term per adult present at year 0, year-0 dollars, by fifth of opening net worth; definitions in question 1's report and freeze file Amendment 4. The means are unweighted, so the top fifth is dominated by the few adults of the weighted tail, who stand for a small part of the population but hold very large balances; read the top fifth as "the creditors", not as a population average.

| Environment | Design | Fifth 1 | Fifth 2 | Fifth 3 | Fifth 4 | Fifth 5 |
|---|---|---|---|---|---|---|
| Reference | Full coverage | +$149,400 / +$1,100 | +$189,900 / +$1,400 | +$209,400 / +$2,200 | +$215,300 / +$2,100 | −$460,800 / −$306,500 |
| Reference | release | +$53,400 / +$800 | +$84,900 / +$1,100 | +$102,500 / +$1,800 | +$106,400 / +$1,600 | −$422,400 / −$240,900 |
| Adverse | Full coverage | +$131,600 / +$900 | +$178,200 / +$1,100 | +$200,500 / +$1,800 | +$202,900 / +$1,600 | −$412,700 / −$281,000 |
| Stress | release | +$9,500 / +$80 | +$20,400 / +$100 | +$29,000 / +$160 | +$29,200 / +$150 | −$18,900 / −$21,000 |

Year 20; each cell is gap / erosion term. Every environment, design and horizon is in `dev/runs/s64-erosion/tables.md`. In most cells the top fifth's wealth *falls* against no programme, and at year 20 erosion is 57% to all of that fall. The trace's check on real holdings shows a further loss that also comes from prices rising slightly faster in the programme run: the creditor charge on shares, −$65,000 per adult on average across all adults in Reference, full coverage, year 20, falling where shares are held; it was not split by fifth. These unweighted means are not the weighted top shares above.

## Basket poverty by labour-force reason (added Nov 15)

The share of adult-years whose income is below the basket of essentials, by the adult's status in that year (the baseline-scope study's reasons; under the participation-margin study's flows adults move in and out). Years 0 to 19, seeds 1-500; the statuses sum to the published basket-poverty measure exactly. Descriptive: no preregistered rule applies. Adults out of the labour force are 17% of adult-years (disability 5.8%, care 6.3%, early retirement 4.1%, school 1.1%).

| Environment | Status | No programme | Full coverage | Opt-in design |
|---|---|---|---|---|
| Reference | in the labour force | 29.0% | 1.8% | 9.5% |
| Reference | out: disability | 77.1% | 16.6% | 52.4% |
| Reference | out: early retirement | 54.0% | 8.5% | 28.8% |
| Reference | out: care | 71.6% | 11.3% | 38.5% |
| Reference | out: school | 81.8% | 16.2% | 58.5% |
| Stress | in the labour force | 38.5% | 2.5% | 30.6% |
| Stress | out: disability | 79.6% | 17.6% | 74.2% |
| Stress | out: care | 77.2% | 13.2% | 69.4% |

Every effect's interval excludes zero (tables). At 40 years the full-coverage design's figures fall further (out of the labour force: 4.7 to 9.7% in Reference). In Stress the opt-in design lowers basket poverty for adults out for disability by only 5.4 points.

## What these figures do not cover

The measures are weighted (the top tail's weights) and taken at the end of the run. Wealth rests on today's price rule and on full backing; question 4's report shows median wealth gains shrinking sharply below full backing. The erosion share and basket poverty by labour-force reason come from the v5.9 batch trace of the main row (`dev/tools/s64_erosion.js`; results in compassionism-sim-results `r2-erosion-104691f/`), not from the batch; the trace reproduced the batch's stored figures in every seed. The percentiles other than the median and the top shares were not traced one by one; the fifths stand in for them.
