# The v5.9 model, question 4: how much the results depend on full backing

> **Note (Nov 28, 2026).** The results repository named in this document, `BetterToBest/compassionism-sim-results`, is offline: GitHub disabled it. Every figure can be reproduced from the engine commit named beside it, with the commands in `REPRODUCE.md`. The results folders are deposited in an archive with a permanent identifier, DOI 10.5281/zenodo.24615619 (copied on OSF at osf.io/7v5ur); folders not in the archive are listed in `data/results-manifest.json`.

Nov 15, 2026. The backing curve of the v5.9 batch, read as frozen, with the v5.6 model's backing curve beside it. Engine `104691f`, 500 adults, seeds 1-500, three environments, 20 and 40 years. Preregistered: research-update `prereg/2026-11-s63-round2-freeze.md` (Design, Source rows, item 5; Amendment 3 records how the mechanism's point was read). Results: compassionism-sim-results `r2-s-<env>-<years>-104691f/` (part `S`, points 71-81 and the main point). Tables: `dev/runs/s64-round2/s64-q4-backing.md` (`python3 dev/tools/s64_tables.py`); the v5.6 model: `dev/runs/s64-round2/m-ce8d030-backing-tables.md` (`python3 dev/tools/s51_backing.py`, study M, compassionism-sim-results `m-ce8d030`, run Nov 7 and tabulated here for the first time).

## In short

1. **The main row assumes full backing: every dollar the programme pays is matched by new output.** That is how the design is stated (Nov 14), so it is labelled a design parameter wherever the main row is shown. It is not something the model shows will happen.
2. **The model's own mechanism for new output reaches 0.2-1.9% backing, or 14-20% without its ceiling** (less at 40 years than at 20; why is not traced here). The replay of these two points reproduced every value the batch stored, exactly. At those points programme inflation runs at 31-53 points a year in the full-coverage design, built to meet NEEC's criterion C2.2, and 15-46 in the opt-in design. The v5.6 model found the same at 20 years (0.7-1.4%; 19.5% without the ceiling).
3. **Programme inflation passes 5 points a year once less than about 86-90% of the payout is backed** (74-77% for the opt-in design in Stress). The mechanism's point lies far below this break-even in every cell. By the preregistered rule, the findings page says so in the same paragraph as any inflation headline.
4. **The poverty effects barely depend on backing.** At no backing at all, the full-coverage design still lowers basket poverty by 30-44 points and wealth poverty by 18-22 points, against 31-46 and 19-24 at full backing. The opt-in design's poverty effects at no backing are 0.9 to 2 times their size at full backing (larger in Adverse and Stress). Wealth poverty never becomes worse than with no programme at any point of the curve ("below 0" in every cell and every resample). *Note (Nov 17, 2026; the release reviews' triage, research-update `audits/2026-11-release-review-triage.md`):* this holds because the model has no limit on what the economy can supply. Demand never runs into what can be produced, wages follow prices in full (`wIdx` 1), and the Basic Unit and the basket follow the same prices. With no new output, the real goods the programme's recipients gain are paid for only by holders of savings and lenders, through higher prices. It is a property of the model, not evidence that the design works without backing; a reading with limits on supply and indexing is planned for the next engine.
5. **Median real wealth is what backing moves.** The full-coverage design's gain in median real wealth falls from $208,400 at full backing to $86,800 at no backing (Reference, 20 years), and to $16,000 at 40 years; the opt-in design's turns into a loss of $20,500 at 40 years with no backing.
6. **This is a change from the v5.6 model.** There, with every dollar of wealth held as cash, the inflation of an unbacked programme wiped out savings, and wealth poverty rose by up to 65 points at the mechanism's point; the opt-in design needed 71-84% backing before wealth poverty fell at all. The v5.9 model holds wealth in asset classes whose returns partly follow prices, so the same inflation leaves most adults' wealth standing. Basket poverty already fell with no backing in the v5.6 model for both designs.

## What was run

The backed share `a` is the share of the programme's payout that is matched by new output, so that it adds no net demand for existing goods. Points: `a` = 0, 0.25, 0.5, 0.75 (programme runs, against the main row's no-programme run), and `a` = 1, the main row. Two points of the mechanism: the backing study's main reading (only output the programme's projects add absorbs new money, ceiling 8% of earned income, lag 2 years, wear 5%) at the most productive setting the backing study shows (all of the payout funding supply-adding projects, 0.32 of output a year per dollar), and the same without the ceiling. At `a` = 0, the price rule's five other readings (each with its own no-programme run), because only there does new money reach prices (the assumptions screen rule 6).

Break-even shares (preregistered): scanning down from 1, the backed share at which programme inflation reaches 5 points a year, and the share at which wealth poverty (yearly average) is no better than with no programme, by linear interpolation between grid points, with the bootstrap interval of the crossing; never extrapolated.

## The curve (full coverage, Reference, 20 years; every cell is in the tables)

| Backed share | basic living | basket poverty | wealth poverty | median real wealth | programme inflation (points a year) |
|---|---|---|---|---|---|
| 0 | −19.1 | −31.0 | −19.0 | +$86,800 | 40.3 |
| 0.25 | −19.1 | −31.3 | −19.4 | +$103,300 | 30.5 |
| 0.5 | −19.1 | −31.6 | −19.6 | +$129,000 | 20.5 |
| 0.75 | −19.0 | −32.1 | −19.6 | +$170,600 | 10.1 |
| 1, full backing as the design states (main row) | −18.7 | −32.4 | −18.6 | +$208,400 | 0.15 |
| mechanism, main reading | −19.1 | −31.0 | −19.1 | +$86,900 | 40.0 |
| mechanism, no ceiling | −19.1 | −31.2 | −19.4 | +$98,200 | 32.6 |

Basic living and wealth poverty are slightly *better* below full backing than at it (by 0.3-1.0 points). A likely reason, not traced here: inflation lowers the real value of debts as well as of savings (the low-share trace found this for the adults who start in debt).

## Break-even backed shares

| | Reference 20 y | Reference 40 y | Adverse 20 y | Adverse 40 y | Stress 20 y | Stress 40 y |
|---|---|---|---|---|---|---|
| Full coverage: inflation reaches 5 points a year at | 0.88 | 0.87 | 0.89 | 0.89 | 0.90 | 0.90 |
| Opt-in design: inflation reaches 5 points a year at | 0.87 | 0.86 | 0.89 | 0.90 | 0.74 | 0.77 |
| Either design: wealth poverty no better than no programme at | below 0 | below 0 | below 0 | below 0 | below 0 | below 0 |
| Programme inflation at no backing: full coverage / opt-in design | 40.3 / 35.3 | 36.5 / 33.8 | 46.0 / 40.9 | 48.3 / 46.3 | 48.7 / 18.2 | 53.3 / 20.6 |

The intervals of the crossings are within ±0.01 (tables). "Below 0": no point of the curve reaches the threshold; the share is not extrapolated below 0.

**Rule 4, applied.** In every cell, the break-even share for 5% inflation (0.74-0.90) lies above the mechanism's point (0.002-0.019, or 0.14-0.20 without the ceiling). The findings page must say so in the same paragraph as any inflation headline. Suggested wording: "The main row assumes every dollar paid is matched by new output, as the design states. The model's own mechanism for new output matches 0.2-1.9% of it (14-20% with no ceiling); inflation stays under 5% a year only above about 86-90% backing."

## The price rule's readings at no backing

At `a` = 0 the price rule matters to inflation and wealth, not to poverty. Its demand response at 0.2 lowers the full-coverage design's inflation from 40.3 to 31.7 points a year (Reference, 20 years); the velocity drift raises it to 46.7 and cuts the median-wealth gain from $86,800 to $79,000. No price reading moves a poverty effect by a full point (the largest: the velocity drift, 0.85 points of the full-coverage design's basket poverty in Stress at 40 years). These readings are inactive at full backing, as the assumptions screen found: on the main row's curve every price reading is within seed noise of the main row (question 2's report).

## The v5.6 model beside the v5.9 model

| | The v5.6 model (study M, engine `ce8d030`, wages fully indexed) | The v5.9 model (engine `104691f`) |
|---|---|---|
| Inflation at no backing, Reference, 20 y | Full coverage 37.2, opt-in 51.0 points a year | Full coverage 40.3, opt-in 35.3 |
| Backed share where inflation reaches 5 points | Full coverage about 0.86, opt-in about 0.90 | Full coverage 0.88, opt-in 0.87 |
| Mechanism's backed share (main reading / no ceiling) | 0.7-1.4% / 19.5% (20 years) | 0.5-1.9% / 19.4-19.6% at 20 years; 0.2-0.7% / 13.6-13.8% at 40 years |
| Basket poverty at no backing, Reference | Full coverage −24.5, opt-in −29.5 | Full coverage −31.0, opt-in −19.1 |
| Wealth poverty at the mechanism's point (the v5.6 model: wages 90% indexed, year 20) | Full coverage +47.2, opt-in +65.0 points (worse than no programme) | Full coverage −19.1, opt-in −13.8 (yearly average; better) |
| Backed share where wealth poverty stops being worse (wages fully indexed) | Full coverage 1%, opt-in 71% | below 0 for both |

The v5.6 model's opt-in row is a different design reading (released wages); the comparison is of the backing mechanism, not of the designs' levels. One oddity of the v5.6 model's tables, not examined here: the opt-in row's basket-poverty effect at 95% backing (−25.9) is smaller than at 90% (−34.4) and 100% (−34.7).

## Unfavourable results

- Below full backing, inflation is far above any target in every cell, and the model's own mechanism does not come close to preventing it.
- At no backing and 40 years, the opt-in design lowers median real wealth (Reference −$20,500; interval −$22,700 to −$18,400).
- Basic living and basket poverty effects survive, but they are effects on poverty measured against prices that rise 35-50% a year: a world no one would run.

## What these figures do not cover

The backed share is a design parameter swept here, not estimated. The mechanism's point is the backing study's reading at its most productive setting; less productive settings reach less. Seed intervals do not cover the engine's structure (one price rule, no central bank, no migration, 500 adults) or the choice of main row. Wealth figures rest on today's price rule; their erosion share is computed in the v5.9 batch.
