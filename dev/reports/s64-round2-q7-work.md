# The v5.9 model, question 7: work, participation and hours at the main row

Nov 15, 2026. Engine `104691f`, the main row (full backing, a design parameter), seeds 1-500, three environments, 20 and 40 years; 500 adults, with the 10,000-adult main pair beside it. Preregistered: research-update `prereg/2026-11-s63-round2-freeze.md` (Q7; secondary family, Holm within each table). Results: compassionism-sim-results `r2-m-*-104691f/` and `r2-b-*-104691f/`. Tables: `dev/runs/s64-round2/s64-q7-work.md` (`python3 dev/tools/s64_tables.py`).

## In short

1. **Fewer adults work under both designs.** The full-coverage design lowers participation by 3.0-4.8 points of adult-years; the opt-in design by 0.9-2.6 points. Every one of these is a programme leaver: an adult who would have worked without the programme and does not with it (the participation-margin study's participation margin, 43% of the income effect taken as leaving work).
2. **Programme leavers are 3.0-4.7% of adult-years under the full-coverage design and 0.9-2.6% under the opt-in design.** Their earnings forgone average $1,700-1,760 per adult-year (spread over all adults) under the full-coverage design, and $300-1,280 under the opt-in design.
3. **Hours per adult rise under the full-coverage design (+7 to +12% of the base level) and fall slightly under the opt-in design (−1 to −3%).** At 10,000 adults the figures are the same within their intervals (full coverage, Reference, 20 years: +10.2% at 500 adults, +9.5% at 10,000).
4. **The number of adults outside the labour force does not change** (17.3% of adult-years in both runs): the movement in and out of the labour force for reasons such as disability, care, school and retirement (the participation-margin study's yearly flows) is the same with and without the programme; adults who stop working because of the programme are counted separately, as leavers.
5. **What the model does not count:** the value of care, community work and new ventures that adults who leave paid work may take up (the participation-margin study section 6). The earnings forgone are a cost the model sees; the value of what leavers do instead is a benefit it does not.

## The figures (effect against no programme; intervals in the tables)

| | Reference 20 y | Reference 40 y | Adverse 20 y | Adverse 40 y | Stress 20 y | Stress 40 y |
|---|---|---|---|---|---|---|
| **Full coverage** participation (points) | −3.5 | −3.1 | −4.3 | −4.6 | −4.4 | −4.8 |
| programme leavers (% of adult-years) | 3.5 | 3.0 | 4.2 | 4.5 | 4.3 | 4.7 |
| earnings forgone ($ per adult-year) | 1,751 | 1,763 | 1,729 | 1,745 | 1,709 | 1,726 |
| hours (share of the base level) | +0.102 | +0.115 | +0.102 | +0.108 | +0.073 | +0.075 |
| **Opt-in design** participation (points) | −2.6 | −2.3 | −2.4 | −2.0 | −1.0 | −0.9 |
| programme leavers (% of adult-years) | 2.6 | 2.3 | 2.4 | 2.0 | 1.0 | 0.9 |
| earnings forgone ($ per adult-year) | 1,266 | 1,278 | 948 | 735 | 381 | 304 |
| hours (share of the base level) | −0.025 | −0.015 | −0.033 | −0.025 | −0.016 | −0.014 |

Employment moves with participation (full coverage −3.0 to −4.7 points). Every effect in this table except "outside the labour force" survives Holm.

## Hours at 10,000 adults

The v5.9 cross-tests (part 2) found that, on its candidate row, the hours response depended on the population size (+11% at 500 adults, +1.8% at 10,000) and set the rule that no hours figure from 500 adults is printed without the 10,000-adult figure. On the frozen main row the two agree in every cell: full coverage +0.070 to +0.120 at 10,000 adults against +0.073 to +0.115 at 500; the opt-in design −0.015 to −0.033 at both sizes. Participation and the weighted top-1% wealth share also agree to within 0.1 points. Why the frozen row no longer shows the v5.9 cross-tests' gap is not traced here; the rows differ in backing (full here) and in the second implementation's reporting corrections.

## Unfavourable results

Lower participation and employment under both designs, in every cell; earnings forgone. These are printed beside every participation figure.

## What these figures do not cover

The participation margin is one reading (43% of the income effect taken as leaving work); question 2's curves carry 0% and 100%. The model has no value of non-market work. The engine's hours measure (`hrs`) is hours per adult-year relative to its base level.
