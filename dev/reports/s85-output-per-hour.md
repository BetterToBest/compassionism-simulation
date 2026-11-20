# Automation, output per hour and the backing the programme's own work produces: what the model finds

Nov 20, 2026 · engine v5.9.21 (`503fa48`) · preregistered before any run (BetterToBest/research-update `prereg/2026-11-s85-output-per-hour.md`, with three amendments, the last written before any table was read) · Claude. How the design was read before the build: [the reading note](s85-output-reading.md).

**One outcome is still to come.** The preregistered savings measure (the share of adult-years whose liquid savings cover less than three months of need) was not switched on in the batch. A supplementary run of the headline rows with it on is under way (`s85sec-<env>-<years>-503fa48`). Until it is read, the savings line below uses the batch's nearest stored measure, adult-years below 30 days of basic living, and says so.

## 1. What was asked

Duke asked how the model treats AI and automation: output per hour will rise, but paid hours will fall in many professions, and in the near term more of the labour force may be displaced. His view is that, implemented and maintained well, the programme can prevent much of the distress this would otherwise cause. That view is his and is kept apart from the results; whether the programme prevents the distress is what the run measures, not an input.

The study runs displacement in **both** runs of every pair, so the no-programme run faces the same automation:

- **Displacement**, net of new work: 10%, 30%, 50% or 70% of today's paid work gone by year 20 along an S-shaped path, then held. Two forms: **lost jobs** (adults leave paid work for good, the most exposed first by the engine's automation risk) or **shorter hours** (everyone's hours fall, the most exposed most). 50% and 70% by year 20 are **stress readings, beyond the forecasts**: output per remaining hour would have to be 2.0 and 3.3 times today's by then, 3.5% and 6.2% a year above trend.
- **Output is kept.** The automated work is still done. Output per hour also grows by a sourced forecast: low (Penn Wharton's levels, 2.2% higher by year 20) or high (a decade of Goldman Sachs' 1.5 points a year, 16%). Seven tenths of the gain reaches pay (Stansbury and Summers).
- **The dividend.** The output of automated work, and the part of the gain not paid as pay, goes to owners. US households hold 54% of US corporate equity (Rosenthal and Burke), so that share is paid to the model's adults by their holdings; the rest goes to owners outside the model.
- **The backing produced.** The main rows assume full backing: every programme dollar is matched by new output (a design parameter). A separate block drops that assumption and counts only what the programme's own work produces: project hours valued at their pay over the labour share (BLS, 0.542), times m, the share of programme work whose output people would otherwise buy (goods and services alike; a design parameter, 0.25, 0.5 or 1), plus the yield of the capital the providers reinvest (BEA, 0.164 a dollar).

Two designs: **full coverage** (every adult takes part) and **opt-in** (the release design: in Reference 78% take part). Environments: Reference, Adverse (repeated recessions and an automation wave) and Stress (the Adverse economy with the programme's settings at their weakest). Seeds 1-500, paired; 500 adults; 20 years (the primary horizon) and 40.

**Terms.** *Displacement's cost* is a run at a displacement level minus the same run with none, signed so that positive is harm. *The offset* is the cost with no programme minus the cost with the programme; *the offset share* is the part of the cost the programme takes away. Intervals are 95%, from 10,000 bootstrap replicates; every offset statement survives a Holm correction across 48 tests (six readings of the four primary outcomes, times eight displacement cells) unless said otherwise.

## 2. The answer in short

1. **Displacement hurts with no programme.** By year 20, basket poverty (adult-years below one's own cost of living) is 2.0, 5.6, 9.0 and 12.6 points higher at 10%, 30%, 50% and 70% lost jobs (Reference; 1.6-9.6 in Adverse and Stress), and median real wealth is $7,158 to $48,326 lower. At 40 years basket poverty rises 3.1 to 20.3 points in Reference.
2. **With full coverage at full backing, the programme takes away most of the harm to poverty and savings, and a small part of the harm to wealth.** It offsets 80-96% of the rise in basket poverty with lost jobs and 94-100% with shorter hours. Across both forms it offsets 59-93% of the rise in yearly wealth poverty, 97-100% of the rise in adult-years below 30 days of basic living, and 13-40% of the fall in median real wealth (13-24% with lost jobs, 18-40% with shorter hours). Every one of this design's 144 tests at 20 years is significant: 136 "offsets in part" and 8 "offsets fully". **But full backing is assumed, and the programme's own work does not produce it** (point 4): at the backing it does produce (5-18% of the payout in this design), programme inflation is 48-69 points a year at 20 years across the three environments.
3. **The opt-in design offsets far less, and with lost jobs it often makes displacement's cost larger.** It offsets up to 69% of the rise in basket poverty with shorter hours (and in one cell it worsens it), and with lost jobs between −23% and +17%: in 9 of the 12 lost-jobs cells the rise in basket poverty is larger with the programme than without it. Of its 144 tests at 20 years, 98 offset in part, 31 do not offset and 15 worsen (at 40 years: 80, 32 and 32). Displaced adults' basket poverty in their last year is 47-61% with the opt-in programme (Reference), against 73-79% with none and 3% with full coverage.
4. **The backing produced is far from enough.** In every one of the 44 produced-backing rows, in each design, environment and horizon, programme inflation's interval lies above 5 points a year: 48-63 points in Reference with full coverage at 20 years; 18-71 across both designs and environments at 20 years, and up to 82 at 40. In the main reading the programme's own work matches 5-18% of the payout with full coverage and 3-8% opt-in (19% and 11% with the fuller valuation of capital). Even if all of it were output people would otherwise buy (m 1), inflation stays above 5 points everywhere, so no break-even m exists on the grid. Displacement raises this inflation, by 1-8 points at 20 years and up to 14 at 40 (the price rule's income falls, and the dividend is not in it).
5. **Free time is mostly insecure without the programme.** At 50% lost jobs, an adult who was in paid work at the start has on average 494 more unpaid hours a year over the run (1,032 in year 20). With no programme, 76-81% of those hours fall in households below their cost of living. With full coverage, 4-10% do; opt-in, 55-77%.
6. **The design's maintained take-home**, with shorter hours and the automated hours' output paid to the workers whose hours fell, removes displacement's cost to median wealth in the programme run: the programme's effect on median wealth grows by $18,746 and $30,874 at 30% and 50% (Reference, full coverage). In this model that pay comes out of the owners' dividend.
7. **Together with the supply limit, wages that follow prices at three quarters made up a year later, and the BU a month behind**, at the produced backing, programme inflation is 50-67 points a year with full coverage (20 years), the programme still cuts basket poverty by 29-40 points, and it offsets 0-68% of the rise in basket poverty at 50% lost jobs. Opt-in, it worsens that rise in 10 of its 12 tests.

## 3. Checks, before any table was read

Every check passed in all six result folders (`s85-tables-503fa48/s85-checks.md`):

- The results files match their checksums; 20 shards cover seeds 1-500 once, on the pinned engine, from a clean checkout, and the release start's baseline check passed in each.
- **The main rows are unchanged.** With the option off, the two designs' main rows and their no-programme run equal the published main rows with the private price at the sale in every key and seed (`s90-sale-<env>-<years>-b8ccd8d`). With no displacement and no gain, the option equals the main row in every key but its own.
- Displacement is exactly as set in every row, year and seed; wages plus the dividend equal every adult's earnings times the gain within 4e-15; the rows that produce nothing produce nothing; every stored value is finite.
- The rows that add participants' own conversions equal their counterparts in every key and seed: in the main rows every expired BU goes to the project pool, so there are no such conversions (as found in the build).
- The money accounts rest on the build's unit test. The engine's Source-financing residual is not zero on these rows by construction (they are financed by the flat contribution), so it was printed, not tested.

## 4. Displacement and the programme (question 1)

The offset share, by form and design, across the three environments at 20 years (the 40-year range in brackets). Each cell's full figures, its costs in both runs and its category are in `s85-q1-displacement.md` and `s85-q1-displacement-40y.md`.

| Reading | Full coverage, lost jobs | Full coverage, shorter hours | Opt-in, lost jobs | Opt-in, shorter hours |
|---|---|---|---|---|
| Basket poverty | 80-96% (81-97%) | 94-100% (90-101%) | −23% to 17% (−32% to 15%) | −3% to 69% (−19% to 73%) |
| Wealth poverty, yearly average | 59-87% (75-95%) | 85-93% (88-98%) | −7% to 18% (−9% to 21%) | 4-47% (−1% to 56%) |
| Wealth poverty, last year | 72-94% (82-97%) | 88-97% (90-100%) | −5% to 20% (−14% to 25%) | 2-54% (−5% to 62%) |
| Median real wealth, weighted | 14-24% (7-33%) | 18-40% (7-44%) | 1-8% (−5% to 18%) | 6-21% (1-19%) |
| Median real wealth, unweighted | 13-22% (8-31%) | 18-38% (6-42%) | −3% to 10% (−4% to 16%) | 6-20% (0-19%) |
| Below 30 days of basic living (in place of the savings measure) | 97-102% (98-100%) | 99-100% (99-100%) | 4-38% (−2% to 42%) | 9-61% (2-67%) |

**Every cell, by category** (after Holm across the 48 tests of its environment, horizon and design). Each group of six letters is one cell, and its letters are the six readings in the order of the table above (basket poverty, the two wealth poverty readings, the two median wealth readings, below 30 days of basic living): F offsets fully, P offsets in part, N does not offset, W worsens. The eight groups are the cells in the order 10%, 30%, 50%, 70% lost jobs, then 10%, 30%, 50%, 70% shorter hours.

| | Reference | Adverse | Stress |
|---|---|---|---|
| Full coverage, 20 years | PPPPPF PPPPPF PPPPPF PPPPPP FPPPPF FPPPPF PPPPPP PPPPPP | PPPPPF PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP | PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP |
| Opt-in, 20 years | PPPNNP PPPPPP PNPPPP WNPPPP PPPPPP PPPPPP PPPPPP PPPPPP | WNPNNP WNNNPP WNNNNP WWWNNP PPPPPP PPPPPP PPPPPP PPPPPP | WNNNNP WNNNNP WWNNNP WWWNNP PPPPNP PPPPPP PPPPPP WPNPPP |
| Full coverage, 40 years | PPPPPF PPPPPF PPPPPP PPPPPP FPFPPF FPPPPF PPPPPP PPPPPP | PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP | PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP PPPPPP |
| Opt-in, 40 years | PPPNNP PPPNNP PPPNNP WPPPPP PPPNNP PPPPPP PPPPPP PPPPPP | WNNPPP WNWNNP WWWNNP WWWWWN PPPPPP PPPPPP WPPPPP WPWPPP | WNNNNN WWWNNN WWWNNN WWWWWW PPPNPP WPPPPP WPNPPP WNWNNP |

**What "worsens" means here.** The opt-in programme still cuts basket poverty by 7-26 points against no programme at every displacement level. "Worsens" means that cut is smaller with displacement than without it: displacement raises basket poverty more in the programme run than in the no-programme run (by up to 2.2 points at 70% lost jobs in Adverse). The displaced adults' figures (section 8) show where: in the opt-in programme run, most displaced adults stay below their cost of living. An inspection of the Adverse rows (seeds 1-100; not a preregistered test) points to two causes. First, a counting effect: with the opt-in programme, 23% of those who take part are below their cost of living with no displacement, against 45% with no programme, so more of them sit just above the line, held there by their wage. When automation takes the job, they fall below it; with no programme most of the same adults were below the line already, so the lost job adds less to the count. Among those who take part, basket poverty rises 8.4 points at 50% lost jobs with the programme and 7.0 without; with shorter hours, where no one loses the whole wage, it rises 7.0 with the programme and 8.3 without. Second, the flat contribution that finances the programme rises as the wage base shrinks (3.5% of pay with no displacement, 4.1% at 50% lost jobs, 4.5% at 70%), and those who do not take part pay it without the payout. A full trace is listed for the next step.

**At full backing only.** These are the main rows' terms: every programme dollar matched by new output, a design parameter. Section 7 shows that the programme's own work produces 5-18% of that backing in the full-coverage design and 3-8% opt-in, at programme inflation of 18-71 points a year at 20 years (up to 82 at 40). Every figure in this section should be read with that beside it.

## 5. Lost jobs against shorter hours, and the order (question 2)

- **Shorter hours** spread the same loss of paid work over everyone. With no programme, they raise basket poverty about as much as lost jobs (Reference: 9.5 against 9.0 points at 50%). The programme offsets more of it: in the full-coverage design 94-100% against 80-96%; opt-in, up to 69% against at most 17%.
- **The order.** Displacing adults evenly rather than the most exposed first raises the no-programme cost of 50% lost jobs from 9.0 to 10.6 points of basket poverty (Reference), and the full-coverage programme's cut grows by 1.5 points. With shorter hours the even order changes the cut by under a point.

## 6. Output per hour, and who gets it (question 3)

- **The high gain** (16% more output per hour by year 20, against 2.2%) lowers poverty in both runs, so the programme's cut in basket poverty is 1.2 points smaller at 50% lost jobs (full coverage, Reference) and 1.5 points smaller with no displacement. It barely changes displacement's cost (9.3 against 9.0 points with no programme).
- **The pass-through** to pay (none or all of the gain instead of seven tenths) changes the programme's effects by 0.3 points or less.
- **The dividend** at 50% lost jobs is 19% of wages; the labour share of income falls from 99.6% with no displacement to 84%, and the programme barely changes it. The model's households receive 48% of the dividend within the run (the sourced 54%, less the last year's, the largest as displacement grows, which falls after the run). If they held all of it, the full-coverage programme's effect on median real wealth would be $902 larger.
- **Who gains.** Displacement moves wealth toward the top. With no programme, the top 1% share of wealth rises from 31.5% to 32.4% at 50% lost jobs (Reference) and the poorest fifth's mean real wealth falls from $32,103 to $23,166. The full-coverage programme lowers the top 1% share to 27.6% and raises the poorest fifth's mean to $158,768 (at full backing). The tables by fifth are in `s85-q2-q3-q7-readings.md`.

## 7. The backing the programme's own work produces (question 4)

Here nothing is assumed backed. What the programme's own work produces, valued as above, replaces the main rows' assumption.

| | Full coverage | Opt-in |
|---|---|---|
| Produced share of the payout, over the run (m 0.25 to 1) | 5-18% | 3-8% |
| Programme inflation, points a year (20 years) | Reference 48-63; Adverse 54-69; Stress 53-69 | Reference 36-44; Adverse 41-50; Stress 18-23 |
| Category (all 44 rows in each design, environment and horizon) | does not back enough | does not back enough |
| m at which inflation reaches 5 points a year | above 1 everywhere | above 1 everywhere |

- **m names the share of programme work whose output people or businesses would otherwise buy**, from a shop or a service provider: food, housing and repairs, health and personal care, childcare and elder care, transport, utilities, education, and the essential providers' services, including work that replaces a purchase. At m 1, all programme work counts. Even then inflation stays at 48-56 points a year (Reference, full coverage, 20 years).
- **With nothing produced** (the floor), inflation is 58-63 points a year; at m 1 it is 48-56. The produced output takes off 1 to 10 points, depending on m; reaching 5 points a year would take 53 to 58 off the floor's rate.
- **Stricter accounting**, in which only each year's added output absorbs new money, leaves a produced share near 1% and inflation 56-63 points.
- **The fuller valuation of capital** (all value added per dollar, capped at 0.32) raises the share to 19% and lowers inflation by about 1 point.
- **The high gain on programme output** and participants' own conversions add almost nothing (the conversions are none in these rows).
- **Displacement raises inflation** at every m, by 2 to 5 points at 50% lost jobs at 20 years (up to 9 at 40): the price rule's income falls with wages, and the dividend is not counted in it.

**What this means for the main rows.** The published main rows assume full backing. This study finds that the programme's own work, as the model can measure it, produces at most 18% of it. The measure of programme work is narrow by design (project hours only, at pay over the labour share; the cautious side). The gap between 18% and the whole is not explained by the model, and every full-backing figure carries it.

## 8. Where the programme falls short (question 5)

**Displaced adults** (lost jobs) at the last year, Reference, 20 years:

| | No programme | Full coverage | Opt-in |
|---|---|---|---|
| Below their cost of living | 73-79% | 2.7-2.9% | 47-61% |
| Too little wealth | 38-39% | 2.3-2.8% | 20-22% |
| Median months of costs covered by all their wealth | 27-31 | 241-250 | 115-125 |

In Adverse, the displaced adults' basket poverty is 81-83% with no programme, 3% with full coverage and 69-76% opt-in.

**Every cell that does not offset or worsens** is in the category table of section 4. In the full-coverage design there are none, in any environment or horizon. In the opt-in design: at 20 years, 31 cells do not offset and 15 worsen, nearly all with lost jobs, and most in Adverse and Stress. Basket poverty worsens at every lost-jobs level in Adverse and Stress, and at 70% in Reference. At 40 years: 32 and 32. The full list, with each cell's costs and offset, is in `s85-q5-q6-shortfall-free-time.md`.

**The figures by fifth of starting wealth** are given for all adults (section 6). The engine does not store displaced adults' outcomes by fifth (a limit).

## 9. Free time (question 6)

Hours a year no longer paid, per adult in paid work at the start (a full year is 2,080 hours), at 50% lost jobs by year 20, mean over the run. *Secure*: the household is above its cost of living that year. *Insecure*: below it.

| | Freed hours | Secure | Insecure |
|---|---|---|---|
| No programme, Reference | 494 | 117 | 377 |
| Full coverage, Reference | 494 | 473 | 21 |
| Opt-in, Reference | 494 | 222 | 272 |
| No programme, Stress | 494 | 93 | 401 |
| Full coverage, Stress | 494 | 447 | 47 |
| Opt-in, Stress | 494 | 116 | 379 |

With shorter hours the hours are the same and more of them are secure (no programme: 191 of 494 in Reference). The programme does not create the free time; displacement does, in both runs. What the programme changes is whether that time is lived above or below the cost of living. Every figure here is at full backing.

## 10. The design's maintained take-home (question 7)

With shorter hours, the design reading pays the output of the automated hours to the workers whose hours fell, as pay, in the programme run. At 30% and 50%, the programme run then loses no median wealth to displacement (−$431 and −$649, against $18,315 and $30,225 without it; Reference, full coverage), and wealth poverty falls a further 0.12-0.26 points. Basket poverty barely moves with full coverage (0.01-0.05 points); opt-in, it falls a further 1.7 and 4.0 points. In this model that pay is the owners' dividend moved to the workers. Who would bear it outside the model (owners abroad, pension funds) is not modelled. The four-day week pilot (hours 38 to 34 a week, revenue up 1.4%, volunteer companies, no comparison group) is context for this reading, not evidence for it.

## 11. Together (question 8)

The produced backing (m 0.5 or 1, low or high gain) with the sourced supply limit and the design's sharing rule, wages that follow programme inflation at three quarters with the rest made up a year later, and the BU a month behind:

- **Programme inflation:** 50-67 points a year with full coverage, 18-47 opt-in (20 years); 47-78 and 18-56 at 40 years.
- **The programme's cut in basket poverty:** 29-40 points with full coverage, 7-21 opt-in. Against the produced backing alone, the three readings shrink it by 1.1-2.8 points (full coverage, Reference) and add 1.6-2.3 points of inflation.
- **The offset at 50% lost jobs:** with full coverage, 0-68% of the rise in basket poverty, 0-41% of wealth poverty's, 50-61% of median wealth's and 77-95% of the basic-living measure's (67 tests offset in part, 5 do not). Opt-in, it worsens the rise in basket poverty in 10 of its 12 tests and offsets 26-43% of median wealth's fall.

## 12. The slower path and 40 years

Displacement reached by year 40 instead of 20 costs less over a 40-year run, because fewer years are spent displaced. At 50% lost jobs, basket poverty rises 9.4 points with no programme (Reference), against 14.1 when it is reached by year 20. The full-coverage programme offsets 96% of it; the opt-in programme 5% (both in Reference), and it worsens it in Adverse and Stress. The 40-year tables (`-40y`) give every figure of the 20-year ones.

## 13. What this means, and its limits

**On Duke's question.** His view, stated before the run, is that implemented and maintained well the programme can prevent much of the distress automation would cause. The run's answer, in its preregistered terms: **with every adult taking part and every programme dollar backed**, the programme takes away 80-100% of displacement's rise in basket poverty and nearly all of its rise in adults below 30 days of basic living, in every environment; it takes away 13-40% of the fall in median wealth (13-24% with lost jobs); and the free time displacement brings is mostly secure. **With the opt-in design**, it takes away much less, and with lost jobs it often makes the rise in poverty larger. **And the backing is not produced**: the programme's own work, as measured here, matches at most 18% of the payout, and at that backing prices rise 18-71% a year at 20 years (up to 82% at 40). "Prevents much of the distress" is not one of the preregistered categories, so the run gives the shares above instead.

**Limits, stated in advance:**

- No demand shortfall: owners' lower spending out of the dividend is not modelled (the cautious side for the design, whose spending would fill it).
- Prices follow the engine's quantity rule with no central-bank response (the central-bank study is separate), and the model is not a general-equilibrium model: wages, employment and prices outside the essentials do not adjust to one another. At inflation of 20-80% a year a real central bank, and real wage setting, would respond; the inflation figures measure the size of the unbacked money, not a forecast of prices.
- Lower prices from automation reach buyers only through the pass-through to pay.
- Lost jobs count adults, not hours, because hours are not tied to occupation in the engine. There is one ranking for the run; new occupations enter only through the net displacement.
- The dividend raises no investment, so no capital deepening in either run.
- One pass-through for every wage level; the low-paid may get less.
- Contract pay values a programme hour below many workers' own wage (the cautious side for the backing).
- The model's adults are 25 to 64, so part of the households' equity share belongs to older households outside the model.
- Not modelled: the corporate revenue tax (a separate study), health and security raising output per hour (no opened source sizes it), and the Creative Collectives' lending to start-ups (a later step).
- The produced share depends on m, which the design does not state; every statement here names it.
- The savings measure as preregistered is still to come (the supplementary run).

## 14. Text for the findings page

> **Automation.** The model was run with 10% to 70% of today's paid work automated away by year 20, as lost jobs or shorter hours, in both the programme and the no-programme run; 50% and 70% are stress readings, beyond the forecasts. With no programme, basket poverty rises by 2 to 13 points and median wealth falls by $7,000 to $48,000. With every adult taking part and full backing, the programme takes away 80-100% of the rise in poverty and 13-40% of the fall in wealth, and keeps most of the freed time above the cost of living. In the opt-in design it takes away much less, and with lost jobs it often makes the rise in poverty larger. **Full backing is assumed, not produced:** the programme's own work, as the model can measure it, matches 5-18% of the payout, and at that backing prices rise 48-69% a year in the full-coverage design across the three environments (Reference: 48-63%). Figures are for 20 years. Every cell, favourable or not, is in the study's tables.

## 15. Where everything is

- **Preregistration:** research-update `prereg/2026-11-s85-output-per-hour.md` (Amendment 1: three choices that favoured the programme without a source, fixed before the build; Amendment 2: the sourced values and the build; Amendment 3: the savings measure's supplementary run, the Holm family, the references and the rebuilt checks, before any table was read).
- **Engine:** v5.9.21, `503fa48`; the option is described in MODEL_SPEC section 17. Sources: `sources/s85_output.md`, `sources/s85_values.py`.
- **Job:** compassionism-sim-results `runner/jobs/s85.js` (the supplement: `--sec`).
- **Results:** `s85-{ref,adv,str}-{20,40}-503fa48`, each with `run.txt` and `SHA256SUMS`; the supplement `s85sec-{ref,adv,str}-{20,40}-503fa48` when it lands.
- **Tables:** `s85-tables-503fa48` (`python3 dev/tools/s85_tables.py <results> <out>`): the checks, displacement, the readings, the backing produced, shortfalls and free time, together, each at 20 and 40 years, and `s85-summary.json` with every figure and interval.
- **Decisions:** `dev/DECISIONS.md`, the entry of Nov 20, 2026 on reading this study.
