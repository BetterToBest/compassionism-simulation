# Round 2, question 6: who gains, at the main row (S64)

Nov 15, 2026. S57's distribution measures on the round-2 main row (full backing, a design parameter; today's price rule). Engine `104691f`, seeds 1-500, three environments, 20 and 40 years. Preregistered: research-update `prereg/2026-11-s63-round2-freeze.md` (Q6; secondary family, Holm within each table; Amendment 3 item 5). Results: compassionism-sim-results `r2-m-*-104691f/`. Tables: `dev/runs/s64-round2/s64-q6-distribution.md` (`python3 dev/tools/s64_tables.py`).

## In short

1. **Both designs make wealth and income more equal.** C2.2 lowers the top 1%'s share of wealth by 4.6 points (from 31.6% to 27.0%, Reference, 20 years) and the top 10%'s by 9.4 points; the release design by 2.3 and 4.7 points. The bottom half's share of wealth rises from 2.9% to 9.2% (C2.2) and 5.8% (release design).
2. **Income inequality falls under C2.2, and barely moves under the release design.** C2.2 lowers the Palma ratio (the top 10%'s income over the bottom 40%'s) from 2.68 to 1.64; the release design raises it slightly, to 2.75 (+0.07, interval +0.06 to +0.08), and leaves the top 10%'s income share unchanged (+0.03 points, interval includes zero).
3. **Families in debt fall sharply:** from 21.9% to 0.7% under C2.2 and to 7.4% under the release design.
4. **Gains are spread across the distribution in dollars, so they are largest in proportion at the bottom.** C2.2 raises real wealth by $128,000 at the 10th percentile (from −$2,300), $208,400 at the median and $218,800 at the 90th; real income by $32,300 at the 10th percentile (from $21,100) and $82,900 at the 90th.
5. **Two results are unfavourable or need care.** Mobility out of the lowest wealth fifth *falls*: 69.8% of adults who start in the lowest fifth are still there at year 20 under C2.2, against 66.3% without the programme (72.2% under the release design). The fifths are relative: when everyone gains, ranks change less. And **labour's share of money income falls by 30 points under C2.2** (82.5% to 52.0%) and 12 under the release design, because the programme's payments are income that is not wages.
6. **Not yet computed:** the erosion share of each wealth figure (how much of the gain or loss is the change in the real value of the balances adults held at the start; S66). The batch does not store the per-adult opening balances it needs; S64 part 3 runs S66's trace on the frozen row.

## The figures (Reference, effect against no programme; every cell is in the tables)

| Measure | No programme (20 y) | C2.2, 20 y | C2.2, 40 y | Release design, 20 y | Release design, 40 y |
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

Of the 23 measures per table, 19 to 23 have intervals excluding zero and survive Holm in every table. The ones that do not: the very top of the wealth distribution (the 99.9th percentile of the weighted tail; the 99th percentile in two Adverse and Stress cells), the rare move from the lowest to the top fifth (0.00-0.05% of adults), the release design's top-10% income share (Reference and Stress, 20 years), C2.2's staying in the lowest fifth at 40 years (Reference) and the release design's staying in the top fifth in Stress.

## What these figures do not cover

The measures are weighted (the top tail's weights, S59) and taken at the end of the run. Wealth rests on today's price rule and on full backing; question 4's report shows median wealth gains shrinking sharply below full backing. The erosion share and basket poverty by labour-force reason (S61's key, not among the engine's outputs) are not yet computed.
