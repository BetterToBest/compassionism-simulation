# US policy eras and their stability: the descriptive panel and the engine readings (S75)

Preregistration: BetterToBest/research-update `prereg/2026-11-s75-deep-history.md` (committed before any figure), with Amendments 1-3 (part 1, the panel) and Amendment 4 (part 2, the engine build, written before any study run). Part 1's note is `dev/reports/s75-panel.md`; its tables are `dev/runs/s75-panel/tables.md`. Part 2's tables are `dev/runs/s75-eras/tables.md`; results are in BetterToBest/compassionism-sim-results (`s75-panel-54e88bc`, `s75-eras-77a85d6`).

The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson's book *Better To Best* and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome.

## In plain words
- **The published record (part 1, no engine):** on no measure was 2005-2025 clearly less stable than all three earlier postwar eras (0 of 14 measures support it, 5 go against it, 9 are mixed). 1973-1983 was the unstable era. Tax rates actually paid were far more progressive in the 1950s (Piketty, Saez and Zucman: the top 0.1% paid 57.3% of income in all taxes, the top 1% 45.5%). For-profit hospitals' share of beds doubled in 1973-1983 and their share of community hospital admissions doubled from 1975 to 2015, while non-profits held about 71-74% of admissions throughout. The full panel is in `dev/reports/s75-panel.md`.
- **The engine readings (part 2): without the programme, today's households are not steadier in every way under an earlier era's settings.** Under each era's own path, the earlier eras give smaller falls in real wealth and smaller swings in yearly income than 2008-2025, but larger swings in the price of the basket (1947-1972 and 1973-1983), slower recovery from an income shock (1947-1972 and 1984-2007), and more people pushed below the basket line in recession years (1973-1983 and 1984-2007). Counting the 15 cells (three eras, five outcomes): the earlier era is steadier in 8, less steady in 6, no clear difference in 1. **Mixed, as the record is.**
- **Today's households would have had more basket poverty, not less, under every earlier era's path** (without the programme: 47.2% of person-years in 1947-1972, 57.7% in 1973-1983 and 48.6% in 1984-2007, against 44.4% in 2008-2025). This is a property of the model's paths (recession years, the fall in family income in them, and outside inflation on today's basket), not a measure of how people lived then: the engine keeps today's population, prices and institutions.
- **Which setting matters, inside the model:** the central bank's rule moves the largest falls in real wealth most (by $12,000-19,000 in 1973-2025, as S74 found: easing raises asset prices in a recession and the later tightening lowers them). The era's tax schedule barely moves stability and lowers basket poverty a little in every era (0.1-0.4 points): once the equal amount per adult is returned, each era's change takes a little more from higher earnings than from lower ones. The era's health cost growth raises basket poverty (0.1-1.1 points) and, in 1947-2007, the share pushed below the line in recession years. No setting moves the swings in the basket's price (P1): the rule has no channel to essential prices.
- **Today's rule put into 1947 is not a fair test.** Read against the Fed's pegged rates after the war, S74's rule tightens by up to 28 points in 1947 (it reads 1946's 18% inflation, the end of price controls), and the engine's stance slopes, estimated for moves of a point or two, turn that into a $261,000 larger median fall in real wealth. This cell is reported, but it says more about the model's reach than about the era.
- **The programme's effect keeps S74's direction under every era's settings, for both designs**, with few exceptions (C2.2: 111 of 120 cells kept, 3 no measurable difference, 6 reversed; release design: 115 kept, 5 no measurable difference, 0 reversed). Kept means the same direction, good or bad: both designs cut basket poverty (C2.2 by 41-52 points, the release design by 23-32), shrink the largest fall in real wealth and push fewer people below the basket line in recession years; both also make the basket's price and incomes in dollars swing more (as S74), and the release design lengthens recovery from an income shock. The six reversals are all C2.2's P1 in 2008-2025: there the programme makes the basket's price swing slightly less (-0.07 points), not more.

## The stability outcomes (as S74)
P1 the spread of the yearly change in the basket's price level; P2 the spread of yearly changes in real cash income (dollars); P3 the largest fall in real wealth (the median adult's); P4 the years to recover from an income shock (mean); P5 the share of adults above the basket line who fall below it in a recession year. Lower is steadier on all five. Basket poverty and wealth poverty are secondary. "Steadier" or "less steady" is said only where the Holm-adjusted 95% interval excludes zero; P3 and P5 also carry a paired bootstrap interval in the tables. The two designs' no-programme rows are identical, so Q3 is the same for both.

## Q3: without the programme, under each era's path (arm P), era minus 2008-2025
| outcome | 1947-1972 | 1973-1983 | 1984-2007 |
|---|---|---|---|
| P1 spread of the basket's yearly price change (points) | less steady (+0.65) | less steady (+1.63) | steadier (-0.62) |
| P2 spread of yearly changes in real cash income ($) | steadier (-448) | steadier (-4,305) | steadier (-1,549) |
| P3 largest fall in real wealth ($, median, whole run) | steadier (-1,735) | steadier (-7,525) | steadier (-1,292) |
| P3 over years 0-11 (like for like; $) | -21,329 [-21,786, -20,872] | -6,243 [-6,750, -5,735] | -17,680 [-18,198, -17,163] |
| P4 years to recover from an income shock | less steady (+0.37) | steadier (-0.69) | less steady (+0.31) |
| P5 % pushed below the basket line in a recession year | no clear difference (-0.08) | less steady (+5.68) | less steady (+1.13) |
| basket poverty (points; secondary) | +2.81 [2.68, 2.94] | +13.3 [13.1, 13.6] | +4.23 [4.09, 4.38] |
| wealth poverty, yearly average (points; secondary) | +0.37 [0.27, 0.48] | -0.21 [-0.36, -0.06] | -1.95 [-2.06, -1.84] |

The other arms (the era's rule, today's rule, the tax schedule, the health cost growth, all together) give the same picture on P1, P2, P4 and P5, with two changes on P3: under the era's own rule, 1947-1972 has much smaller wealth falls than 2008-2025 (-$19,039) and 1984-2007 no clear difference; under today's rule every earlier era has larger falls (1947-1972 by $261,034, see above). Every cell is in `dev/runs/s75-eras/tables.md`.

## Which setting moves it (no programme, each arm minus arm P in the same era)
| era | the era's rule | today's rule | the era's tax schedule | the era's health cost growth |
|---|---|---|---|---|
| 1947-1972 | P3 no clear difference; P5 -0.11; basket poverty -1.04; wealth poverty (average) -5.41 | P3 +272,464; basket poverty -4.00; wealth poverty -12.0 | basket poverty -0.40 | basket poverty +0.88; P5 +0.20 |
| 1973-1983 | P3 +12,801; P5 -0.53; basket poverty -0.16; wealth poverty -1.05 | P3 +27,434; basket poverty +0.45 | basket poverty -0.30; P5 -0.13 | basket poverty +0.27; P5 +0.16 |
| 1984-2007 | P3 +18,654; P5 +0.31; basket poverty +0.53; wealth poverty +3.18 | P3 +20,909; basket poverty +0.41 | basket poverty -0.19 | basket poverty +1.14; P5 +0.39 |
| 2008-2025 | P3 +17,171; basket poverty +0.28; wealth poverty +3.03 | P3 +9,695; P5 +0.28; basket poverty +0.50 | basket poverty -0.11 | basket poverty +0.12 |

(P3 in dollars, poverty in points; only cells whose interval excludes zero are named, and P1 moves by 0.01 point or less in every cell.) The era's own rule set a mean policy rate of 4.0% in 1947-1972 (the actual rate averaged 3.1%), 9.2% in 1973-1983 (9.6%), 5.1% in 1984-2007 (5.3%) and 1.0% in 2008-2025 (1.4%). These readings do not separate which of the rule's channels (deposits, floating debt, refinancing, asset prices, job loss, forced sales) moves wealth poverty in each era.

## The tax schedule (arm T)
The change by group, in points of income (the era's mean PSZ rate minus 2019's): 1947-1972 bottom half -4.45, middle 40% -5.55, next 9% -1.86, top 1% +11.92; 1973-1983 -0.63, +1.04, +1.73, +6.61; 1984-2007 +1.95, +1.47, +1.51, +2.37; 2008-2019 -0.80, -0.80, +0.47, +0.52. Charged on earnings and Social Security only (see Limits), it moves $400-2,600 per adult-year in either direction, and the equal amount per adult returns it within 1.3% (1947-1972), 1.6% (1984-2007) and 0.03% (2008-2025) of the charges; in 1973-1983, a short era of falling incomes, the amount set from last year's incomes returns 12.7% more than it raised. With nothing returned (a reading), wealth poverty and the programme's effects stay within about 1.5 points of the revenue-neutral readings. Its effect on stability is negligible and on basket poverty small.

## The rule's stance
How far the rule's stance moves from the actual one (the largest yearly tightening and easing against it, points; first 21 engine years): the era's own rule 9.9 and -1.9 (1947-1972), 6.3 and -3.9 (1973-1983), 3.8 and -6.4 (1984-2007), 2.6 and -3.2 (2008-2025); today's rule 27.9 and -5.0, 12.3 and -6.5, 3.8 and -7.0, 9.3 and -0.3. The engine's stance slopes come from moves of a point or two, so readings beyond about 5 points (today's rule in 1947-1983, and the era's rule in 1947-1972) extend them far past their evidence.

## Q4: the programme's effect under every era's settings
| era | C2.2: basket poverty (points) | C2.2: largest fall in real wealth ($) | release: basket poverty | release: largest fall |
|---|---|---|---|---|
| 1947-1972 (path) | -44.4 [-44.7, -44.0] | -41,319 | -26.7 [-27.1, -26.3] | -13,217 |
| 1973-1983 (path) | -51.5 [-51.9, -51.1] | -35,997 | -31.8 [-32.2, -31.5] | -22,499 |
| 1984-2007 (path) | -45.6 [-46.0, -45.2] | -41,362 | -23.0 [-23.3, -22.6] | -7,016 |
| 2008-2025 (path) | -40.7 [-41.1, -40.3] | -29,044 | -23.5 [-23.9, -23.1] | -16,365 |

Across every era and arm, both designs cut basket poverty, shrink the largest fall in real wealth and lower the share pushed below the line in recession years; both raise the swings in the basket's price (by 0.02-0.28 points; C2.2 in 2008-2025 is the exception) and in yearly income in dollars (C2.2 by $9,900-15,600, the release design by $2,300-3,000), as in S74. The release design lengthens recovery from an income shock (by 0.2-0.6 years) except in 1973-1983 (0.07 years under today's rule, otherwise no measurable difference). C2.2 shortens it (by 0.05-0.5 years) except in three cells with no measurable difference. **Decision rule (Q4): the programme's effect keeps its direction in every era**, apart from C2.2's P1 in 2008-2025, which reverses in the favourable direction.

## What the engine readings are, and what they are not
They are a model counterfactual: **today's households** (the 2022-based population of 500 adults) live through each era's measured settings, without the programme and with it, for both designs (C2.2 and the release design). They are not a reconstruction of the era: the population, its jobs, its homes, the basket's prices and today's institutions stay as they are, apart from the setting changed. The eras differ from one another in many ways at once (the US's postwar position, union membership, demography, fixed exchange rates to 1971, wars, the size of government, the rules of finance), and the engine changes only the settings below.

- **The eras** (fixed before any figure): 1947-1972, 1973-1983, 1984-2007, 2008-2025. Each run starts in the December before its era (no revaluation and no recession in that starting year), so each era keeps all of its own yearly changes; the runs last 27, 12, 25 and 19 engine years.
- **Arm P, the era's path:** its CPI-U inflation, real home and share price changes, policy rate, 30-year mortgage rate, recession years (any NBER recession month or an unemployment gap of 2 points or more) and the fall in real median family income in them, with the central bank off (the actual rates).
- **Arm R, plus the era's rule:** the policy-rate rule with the response to inflation and to the output gap that best fits the era's own quarters (part 1's estimate).
- **Arm S, plus S74's rule:** today's rule (S74's main values) in every era.
- **Arm T, plus the era's tax schedule:** each income group's average tax rate (all taxes, from Piketty, Saez and Zucman's accounts) in the era minus 2019's, charged on earnings and Social Security, with an equal amount per adult returned so the size of the state does not change.
- **Arm H, plus the era's health cost growth:** the basket's medical price rises against the rest at the era's mean real medical inflation.
- **Arm A:** R, T and H together.

Every substitute for a series that does not reach back is listed by year in `sources/s75_hx.json` (`_meta.substitutes`) and is a modelling assumption: the 3-month bill as the policy rate before 1955; the long-term government rate plus its 1972-1981 spread over the mortgage rate before 1972; CBO's 1949 noncyclical unemployment rate held back to 1946; the output gap as -2 times the unemployment gap before 1949; real median family income (Census Table F-7) for the recession income multiplier in every era (1946 takes 1947's).

## Limits (stated in advance, and found)
- **The capital income that wealth pays is not taxed in arm T.** The main row's weighted top tail cannot be read by any rule, and unweighted, its 18 adults' capital income would set most of the charge. So arm T changes the tax on work and pensions only. Much of the top 1%'s higher tax rate in 1947-1972 fell on capital (corporate, estate and property taxes); that part is not in the model.
- **The engine has no expectations channel.** A rule whose response to inflation is below one for one (1947-1972, 1973-1983) or about zero (2008-2025) cannot show the instability it is thought to cause.
- **The rule's stance channels are applied far outside the range they were estimated for** where the rule and the actual stance part by many points (see "The rule's stance" below). The slopes (Bernanke and Kuttner for shares, Williams for homes and jobs) come from moves of a point or two.
- The model does not represent war, military spending or corruption, so no figure here is about them.
- Era samples are short, and the readings use one population and 100 seeds; the intervals measure the model's randomness, not uncertainty about history.
