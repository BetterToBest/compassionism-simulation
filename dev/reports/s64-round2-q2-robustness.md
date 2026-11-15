# Round 2, question 2: do the effects hold across the preregistered readings? (S64)

Nov 15, 2026. The specification curves of the round-2 batch, read as frozen. Engine `104691f`, 500 adults, seeds 1-500, three environments, 20 and 40 years. Preregistered: research-update `prereg/2026-11-s63-round2-freeze.md` (Design; decision rules 1-3; Amendment 3). Results: compassionism-sim-results `r2-s-*-104691f/` (Source rows) and `r2-f-*-104691f/` (financed rows). Tables: `dev/runs/s64-round2/s64-q2-curves.md`; one CSV per curve in `dev/runs/s64-round2/curves/` (`python3 dev/tools/s64_tables.py`).

## In short

1. **On the main row's design (full backing, paid by the Source), every poverty and wealth effect is robust.** For both designs, all four outcomes (basic living, basket poverty, wealth poverty, median real wealth), three environments and two horizons, every one of the 62 preregistered readings (61 where a bound equals a single reading) gives an effect with the main row's sign and an interval that excludes zero: 48 of 48 curves robust, all material.
2. **The ranges are the headline.** Across the 62 readings, C2.2 lowers basket poverty by 26 to 33 points in Reference at 20 years (main row 32.4); the release design by 16 to 22 (main row 20.9). The widest range is median real wealth: C2.2 raises it by $188,000 to $660,000 (main row $208,400), because the share of spare cash adults spend moves wealth more than anything else.
3. **Programme inflation is no material change at every point of every Source curve** (0.00 to 0.22 points a year).
4. **The financed rows are fragile everywhere.** Paid for by a contribution with the rest borrowed, the poverty and wealth effects keep their sign at most readings but reverse at some in every cell: C2.2's basket-poverty effect reverses at 18-46 of 117 readings, the release design's wealth-poverty effect at up to 62. The readings that reverse them are how the contribution is set up: its base, the share it must raise, how the rest is met, and the cap on the rate. By decision D23 these rows are never led with.
5. **The price rule's readings change nothing at full backing**, as S70 expected: every one is within seed noise of the main row, except one shift in one cell that is below materiality (table "The price rule's readings at full backing").

## What a curve is

For each outcome, design, environment and horizon, the curve holds the programme's effect at 62 points on the Source rows: the main row; the 32 single readings S70's rules carry (each assumption moved to the end of its range, the others at main); the 28 pairs S70 flagged, at their joint point; and the least-favourable bound, every carried assumption at the end that works against the programme together. On the financed rows: 117 points (49 single readings, 66 pairs, the bound). Each point is a paired run on seeds 1-500 with its own no-programme run.

The preregistered rule (rule 2): **robust** when every point's interval excludes zero with the main row's sign; **mostly robust** when at least 90% do and none excludes zero with the opposite sign; **fragile** otherwise. An effect below materiality at the main row is "no material change" (rule 3).

## Headline sentences, Source rows (rule 1)

Range across the curve first, then the main row with its seed interval. Reference shown; every environment and horizon is in the tables.

- **C2.2, basic living** (adult-years below 30 days of basic living): across the 62 readings, lowered by 16.5 to 19.7 points at 20 years; at the main row 18.7 (seed interval 18.6 to 18.8). Robust.
- **C2.2, basket poverty:** lowered by 26.0 to 33.3 points; main row 32.4 (32.2 to 32.5). Robust.
- **C2.2, wealth poverty** (yearly average): lowered by 15.7 to 19.7 points; main row 18.6 (18.5 to 18.7). Robust.
- **C2.2, median real wealth:** raised by $187,600 to $659,600; main row $208,400 ($207,100 to $209,900). Robust. Rests on today's price rule.
- **Release design, basic living:** lowered by 10.7 to 13.0 points; main row 12.3. Robust.
- **Release design, basket poverty:** lowered by 16.2 to 22.3 points; main row 20.9. Robust.
- **Release design, wealth poverty:** lowered by 9.0 to 12.7 points; main row 10.9. Robust.
- **Release design, median real wealth:** raised by $84,600 to $282,100; main row $99,400. Robust. Rests on today's price rule.
- **Programme inflation, both designs:** 0.00 to 0.22 points a year across every curve: no material change.

In Stress the release design's ranges are smaller but still robust: basket poverty lowered by 5.9 to 8.4 points at 20 and 40 years.

## What moves the Source curves

- **Least favourable:** the bound is at or near the low end of almost every curve. For C2.2's basket poverty (Reference, 20 years) it is −25.9 points against −32.4 at main. It sets eleven assumptions together, among them: no conversion income for adults outside the labour force, no yearly flows in and out of work, the whole income effect taken as leaving work, the high income effect (0.3), a lower spending share (0.593), PTF running costs passed into prices, and the high bargaining markdown. Every unfavourable end together still leaves 80% of the effect.
- **Single readings:** for C2.2's basket poverty, the largest is the conversion of adults outside the labour force (−29.7 with none); for the release design, the income effect at its high end. For median wealth, the spending share (0.593 instead of 0.877) dominates, alone and in its pairs.
- **Most favourable median wealth** comes from the spending share's pairs with where new saving goes and with how far real assets follow inflation (question 3's report: these interact).

## The financed rows

Every financed curve but programme inflation is fragile (C2.2's programme inflation is robust in five cells, but immaterial at the main row; below 0.2 points a year there). Most frequent reversing readings (count of curve-cells, poverty and wealth outcomes): the contribution's base (33), the income effect (22), how the rest is met (20), the share the contribution must raise, alone and in its pairs (14 alone, 15-19 in each pair), the cap on the rate (17 in pairs). Debt passes GDP within the run (median) at 32-39 of the 117 readings in every cell, mostly where the contribution raises little and the rest is borrowed; at the main financed rows it stays below GDP (question 5's report).

## Unfavourable and null results

- The financed rows' poverty and wealth effects are fragile in every cell: the result depends on how the payment is set up.
- Programme inflation is positive at every Source point (worse than no programme), though immaterial.
- The release design's programme inflation in Stress at 40 years is fragile: 49 of 62 points exclude zero with the main row's (positive) sign; it is 0.0000 to 0.0004 points a year, no material change.

## What these figures do not cover

The curve covers the readings S70's screen carried; the readings it held at main are listed in the freeze file ("Screened out"), and the Stress environment was not screened. Ranges are the preregistered ends, not every value between. The seed intervals do not cover the engine's structure. Wealth figures rest on today's price rule; their erosion share is computed in S64 part 3.
