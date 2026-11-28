# The Creative Collectives' lending to community businesses, and charters of public utilities: what the model finds

> **Note (Nov 28, 2026).** The results repository named in this document, `BetterToBest/compassionism-sim-results`, is offline: GitHub disabled it. Every figure can be reproduced from the engine commit named beside it, with the commands in `REPRODUCE.md`. The results folders are deposited in an archive with a permanent identifier, DOI 10.5281/zenodo.24615619 (copied on OSF at osf.io/7v5ur); folders not in the archive are listed in `data/results-manifest.json`.

Nov 21, 2026 · engine v5.9.21 (`c5682f9`) · preregistered before any build or run (BetterToBest/research-update `prereg/2026-11-s94-collectives-lending.md`, with two amendments written before any run) · Claude. How the design was read before the build: [the reading note](s94-collectives-lending-reading.md).

## 1. What was asked

Duke said the Creative Collectives can lend to, or support, start-ups that banks will not lend to: for small businesses that provide essentials, help with premises, logistics and set-up costs; for large utility and transport projects, which are already financed by municipal bonds and public debt, a move of public operators to Collective charters. These are his statements, kept apart from the results. The Hub's papers give the Collectives no lending role, so the model treats this as an addition to the design.

The study adds two things to the main row (open access, the private price at the sale), each in both designs, **full coverage** (every adult takes part) and **opt-in** (the release design):

- **A fund** for the community businesses that sell essentials (grocers, counter-service restaurants, utilities). In the main row their share of essential sales can grow only as far as the capital they own allows. The fund pays for the capacity that zones want and owned capital cannot supply, at most at the pace at which new establishments add capacity in these sectors (2.96 points of the sector a year, counting reinvestment's growth against it; Census Business Dynamics Statistics, weighted by BEA capital). 14% of the money is grants and the rest loans (Pennsylvania's Fresh Food Financing Initiative). The community businesses pay depreciation and real interest on the loans (4.53% and 3.67%), and the interest comes back to the programme. New businesses fail at the rates of young firms' establishments in these sectors (22% in the first year; 45% survive five years). The outlay is programme money in the year it is paid.
- **Charters** of public utilities: the customers of public power get the community-business price for electricity without new capital, and the Source pays the gap to the full running cost, as it does for every community business. Public power serves one electricity customer in seven (APPA); a third and two thirds are design parameters, swept.

Rows: the fund's main reading; eight other readings of it (half and double the pace, no pace limit, the pace limiting the fund's additions only, mature firms' failure rate, no failures, all loans, all grants); charters at 1/7, 1/3 and 2/3 without the fund; the fund and charters at 1/7 together; and a check row with the switch on at zero. Environments: Reference, Adverse (repeated recessions and an automation wave) and Stress (the Adverse economy with the programme's settings at their weakest). Seeds 1-500, paired; 500 adults; 20 years (the primary horizon) and 40.

**Terms.** Each figure is the row minus the main row of the same design, paired by seed. *Basket poverty* is the share of adult-years below one's own cost of living; *wealth poverty* the share with wealth below the poverty line (the yearly average, and the last year); *median real wealth* is weighted and unweighted; *savings* is the share of adult-years whose liquid savings cover under three months of need. Shares are in points. Intervals are 95%, from 10,000 bootstrap replicates. A reading *improves* or *worsens* only where it survives a Holm correction across the six readings of its row, environment, horizon and design.

## 2. The answer in short

1. **The fund helps in no environment or design, and in each it makes at least two of the six readings slightly worse.** Under the preregistered rule (it helps where it improves basket poverty or yearly wealth poverty and worsens none of the six), the answer is no in all six cells at 20 years and all six at 40.
2. **In Reference and Adverse, and in Stress with full coverage, there is little for the fund to do.** The community businesses' share reaches its demand ceiling (49% of essential sales) by year 10 without the fund. The fund lends early, raises the share at year 5 by 0.4-4.6 points, and changes almost nothing from year 10. It costs $37-63 per adult a year at 20 years: the fund's net outlay ($21-23) and the running-cost subsidy on the extra early sales ($20-46). The worsenings are very small: yearly wealth poverty up 0.008-0.024 points, savings shortfall up 0.005-0.013 points, median wealth down up to $64.
3. **Where capital does hold the share back (Stress, opt-in), the fund lifts the share and the cost, and the outcomes worsen.** The share rises by 7.5 points at year 5, 11.3 at year 10 and 13.9 at year 20 (from 34% to 48%). Programme cost rises by $412 per adult a year: $291 of running-cost subsidy on the extra sales and $142 of the fund's net outlay. The contribution that finances the programme rises by $261 per adult a year (0.48 points of pay). Poverty severity falls (0.12 points), but basket poverty rises by 0.07 points, yearly wealth poverty by 0.02, median wealth falls by $391 (weighted), and mean wealth falls in every fifth of starting wealth ($310-729).
4. **No reading of the fund changes this.** Of the eight other readings, none passes the rule anywhere. Double the pace and no pace limit cost more and worsen most readings more; some readings improve slightly in single cells (for example basket poverty with all grants in Adverse and Stress with full coverage), but yearly wealth poverty worsens in every cell of every reading at 20 years.
5. **Charters improve every reading where they act, by small amounts.** At 1/3 and 2/3 they improve basket poverty, yearly wealth poverty and savings in every cell, and at 2/3 every one of the six readings in every cell. No charter row worsens any reading. At 1/7, the share public power actually serves, they act only in Stress (elsewhere every zone's share is already above 1/7): basket poverty falls by 0.001-0.002 points. At 2/3, basket poverty falls by 0.02-0.06 points and median wealth rises by $69-192 at 20 years, at an added cost of $53-95 per adult a year: $1,000-5,200 per adult a year for each point of basket poverty.
6. **The main row is unchanged.** The fund is reported as a reading beside it (decision rule 6).

## 3. Checks, before any table was read

Every check passed in all six result folders (compassionism-sim-results `s94-tables-c5682f9/s94-checks.md`):

- The results files match their checksums; 20 shards cover seeds 1-500 once, on the pinned engine, from a clean checkout, and the release start's baseline check passed in each. Every value the analysis reads is finite.
- **The main rows are the published ones.** The two designs' main rows and the no-programme run equal the published main rows with the private price at the sale (`s90-sale-<env>-<years>-b8ccd8d`) in every key and seed.
- **On at zero equals off.** The check row equals the main row in all 1,405-1,414 keys they share, in every seed, design, environment and horizon. The no-programme run, which the switch does not read, is identical with the switch set on it (shown in the dry run).
- **The fund's accounts close.** Every outlay equals the funded capacity still standing plus the capacity lost, times the capital per adult, within 1e-15 in every row and seed. Charter rows without the fund lend nothing; fund rows without charters pay no charter subsidy.
- **The fund acts.** Under Stress, opt-in, seed 1, the fund lends in year 1 and the pace limit binds in 95% of adult-years.
- The pace limit, the failure rates (45.4% of a cohort survive five years), the charter price cut, the money accounts and the random draws rest on the engine's unit tests for the switch (8 of 8 pass on `c5682f9`).

## 4. The fund, where capital does not hold the share back

In Reference and Adverse in both designs, and in Stress with full coverage, the main row's community-business share is at or near the 49% demand ceiling by year 5 to 10 (48.5% at year 5 in Reference with full coverage, 42-44% opt-in, 23% in Stress with full coverage), and at the ceiling from year 10. Capital binds the share in 21-39% of adult-years.

The fund lends in those first years. In Reference and Adverse it lends the same amount in every seed ($28 per adult a year on average over 20 years, of which $4 grants; $21 net of interest received), because the start is the same in every seed and the share reaches the ceiling before the seeds' paths differ much. The funded capacity is 1.5 points of the sector at year 5 and 0.5 at year 20, after failures have taken 2.5 points.

| 20 years | share at year 5 | programme cost ($ a year) | basket poverty | yearly wealth poverty | median wealth, weighted ($) | savings shortfall |
|---|---|---|---|---|---|---|
| Reference, full coverage | +0.4 | +45 | 0.001 (−0.000 to 0.003) | **+0.008** (0.006 to 0.010) | **−64** (−96 to −32) | **+0.006** (0.004 to 0.007) |
| Reference, opt-in | +2.6 | +40 | **+0.006** (0.002 to 0.010) | **+0.015** (0.013 to 0.018) | −23 (−65 to 39) | **+0.010** (0.007 to 0.014) |
| Adverse, full coverage | +0.5 | +45 | −0.002 (−0.004 to −0.000) | **+0.008** (0.006 to 0.010) | −11 (−45 to 22) | **+0.005** (0.003 to 0.007) |
| Adverse, opt-in | +2.9 | +37 | **+0.010** (0.006 to 0.014) | **+0.015** (0.012 to 0.017) | **−50** (−70 to −29) | **+0.011** (0.008 to 0.014) |
| Stress, full coverage | +4.6 | +63 | −0.003 (−0.007 to 0.000) | **+0.024** (0.022 to 0.027) | −7 (−41 to 29) | **+0.013** (0.011 to 0.015) |

Bold: worsens after Holm. Unweighted median wealth also worsens in Reference opt-in (−$56) and Adverse opt-in (−$52). Wealth poverty in the last year changes in none of these cells.

The changes are very small beside the programme's own effect (the main row lowers basket poverty by 19-41 points and yearly wealth poverty by 10-20 points against no programme), but they are all on the unfavourable side. The fund's money is spent on capacity the share would have reached a few years later anyway. The added cost is the fund's net outlay ($21-23 per adult a year) and the running-cost subsidy on the extra early sales ($20-46), and it raises the contribution that finances the programme by $20-45 per adult a year.

## 5. The fund, where capital holds the share back (Stress, opt-in)

Here the main row's share grows slowly: 12% at year 5, 19% at year 10, 34% at year 20, and capital binds it in every adult-year. This is the case the fund is for.

The fund lends $176 per adult a year (of which $25 grants and $110 later written off as failures; $142 net of interest received), and the pace limit binds in 92% of adult-years. The funded capacity is 6.5 points at year 5 and 5.1 at year 20, after failures have taken 13.5 points. The share rises by 7.5 points at year 5, 11.3 at year 10 and 13.9 at year 20, to 48%.

| Stress, opt-in, 20 years | change (interval) |
|---|---|
| programme cost, per adult a year | +$412 ($407 to $417) |
| of which the community businesses' running-cost subsidy | +$291 |
| the fund's net outlay | $142 |
| the contribution that finances the programme, per adult a year | +$261 (its rate +0.48 points of pay) |
| the payout per participant, a year | −$73 |
| basket poverty | **+0.071** (0.063 to 0.079) |
| wealth poverty, yearly | **+0.024** (0.019 to 0.029) |
| wealth poverty, last year | **+0.034** (0.012 to 0.056) |
| median real wealth, weighted | **−$391** (−$501 to −$283) |
| median real wealth, unweighted | **−$360** (−$452 to −$271) |
| savings shortfall | **+0.008** (0.001 to 0.014) |
| poverty severity | −0.121 (−0.123 to −0.118) |
| mean real wealth of the poorest fifth at the start | −$310 (−$319 to −$300) |
| mean real wealth of the richest fifth at the start | −$729 (−$752 to −$705) |

All six primary readings worsen after Holm, and mean wealth falls in every fifth of starting wealth ($310 to $729). Poverty severity falls: those furthest below their cost of living gain from the cheaper essentials. But each extra point of community-business share costs the Source the gap between the community-business price and the full running cost, the fund's own outlay comes on top, and the contribution that pays for both rises by $261 per adult a year while participants' payout falls by $73. At 40 years the pattern is the same: the share's gain is unchanged, cost +$270 per adult a year, basket poverty +0.065 points, median wealth −$632.

## 6. The other readings of the fund

| reading | cells where the fund helps (of 12) | what changes |
|---|---|---|
| pace × 0.5 | 0 | about half the cost and half the changes; fewer cells worsen at 40 years |
| pace × 2 | 0 | more cost; in Stress with full coverage basket poverty and last-year wealth poverty improve while yearly wealth poverty, median wealth and savings worsen |
| no pace limit | 0 | the most cost; last-year wealth poverty improves in the full-coverage cells, everything else worsens; Stress opt-in: cost +$1,226 a year, basket poverty +0.24, median wealth −$1,420 |
| the pace limits the fund's additions only | 0 | as pace × 2 |
| mature firms' failure rate | 0 | as the main reading, slightly larger; last-year wealth poverty improves in Stress with full coverage |
| no failures | 0 | as the main reading, slightly larger |
| all loans | 0 | as the main reading |
| all grants (nothing repaid) | 0 | basket poverty improves in Adverse and Stress with full coverage, and median wealth in one or both of its readings there; yearly wealth poverty worsens in every cell; savings improve in Stress opt-in |

Decision rule 4 asks that a headline about the fund keep its direction in the pace × 0.5 and all-grants rows. There is no favourable headline to test: no cell passes rule 3. Every cell's verdict by reading, environment, horizon and design is in the tables (`s94-tables-20.md`, `s94-tables-40.md`).

## 7. Charters of public utilities

Charters give the customers of public operators the community-business price for electricity (55% of household utility spending) where their zone's share is below the charter share. The Source pays the running-cost gap on that part.

| 20 years | charter subsidy ($ a year) | programme cost ($ a year) | basket poverty | yearly wealth poverty | median wealth, weighted ($) | savings shortfall |
|---|---|---|---|---|---|---|
| 1/7, Reference and Adverse | 0 | 0 | no change | no change | no change | no change |
| 1/7, Stress | 2-4 | +2 to +3 | −0.001 to −0.002 | −0.001 to −0.002 | no change | −0.002 to −0.003 |
| 1/3 | 6-35 | +5 to +25 | −0.002 to −0.019 | −0.003 to −0.014 | +3 to +44 | −0.003 to −0.024 |
| 2/3 | 67-113 | +53 to +95 | −0.018 to −0.063 | −0.019 to −0.040 | +69 to +192 | −0.021 to −0.072 |

Ranges run over the six cells (three environments, two designs). At 1/7 the charter acts only in Stress, where some zones' share is below one in seven; elsewhere every zone is already above it. At 1/3 and 2/3 basket poverty, yearly wealth poverty and savings improve in every cell; at 2/3 every one of the six readings improves in every cell, at 20 and 40 years. **No charter row worsens any reading in any cell.** The largest gains are in the opt-in design under Stress.

**Cost per point of basket poverty.** Charters cost $900-1,600 per adult a year for each point of basket poverty in the opt-in design and $2,100-7,600 with full coverage. Where a reading of the fund lowers basket poverty at all (Adverse and Stress with full coverage), it costs $10,900-60,600 per point, and it worsens yearly wealth poverty in the same cells.

## 8. The fund and charters together

Together, the fund's main reading and charters at 1/7 give the fund's result: the same readings worsen in the same cells. Their interaction (the joint change minus the sum of the two alone) has an interval that excludes zero for at least one of the six readings in all twelve cells (47 of the 72 readings), and for programme cost in all twelve. (Corrected Nov 21, 2026: this said nine of twelve; the summary file gives twelve.) It is negligible in size: at most 0.002 points of any share and $4 of median wealth, and the joint cost is up to $1.76 a year below the sum. Of the 47 readings whose interval excludes zero, 41 are on the unfavourable side, 4 on the favourable side (under $4 of median wealth or 0.001 points of a share) and 2 are zero to six decimals. (Corrected Nov 21, 2026: this said every one was unfavourable.) In Stress the reason is mechanical: once the fund has lifted a zone's share above 1/7, the charter has nothing left to add there. Under decision rule 5 no headline joins the two.

## 9. What this means, and its limits

**On Duke's question.** In this model the Creative Collectives' fund does what it is built to do, it adds community-business capacity faster than reinvestment alone, but that does not make anyone better off. Where the share would reach its ceiling within ten years anyway (five of the six cells), the fund only brings the gain forward by a few years, at a cost. Where capital truly holds the share back (Stress, opt-in), each extra point of share costs the programme a running-cost subsidy as well as the fund's money, and the contribution that pays for both outweighs what the cheaper essentials return. Charters of public utilities, which need no new capital, improve every reading where they act, by small amounts.

**Limits, stated in advance:**

- The model has no private firms, so lending to private start-ups that are not community businesses cannot be represented. The fund finances community-business capacity only.
- Transport, health care and child care have no community-business price in the model, so charters of roads, transit, airports and ports change nothing in it. Collectives issuing or managing bonds is not modelled.
- Capacity is for the whole population, not by zone (as for reinvestment).
- The pace limit is a whole-economy rate of new establishments, generous to one network. Acquisitions of existing stores are not separated from new building.
- No concessional rate and no recovery on failures (no source opened). The loan's principal is never repaid: the fund in effect holds a stake in the network.
- One utility share stands for electricity; charters act on electricity only, since no ownership share was opened for gas or water.
- The fund's money is new programme money, matched by the main row's full backing as every programme dollar is. Under the supply limit it would compete for real resources; that interaction is not in this design.
- The trace in sections 4 and 5 reads the stored totals (cost, subsidy, contribution, payout); it does not test a cause by switching each part off.

## 10. Text for the findings page

> **The Creative Collectives' lending.** Duke proposed that the Creative Collectives lend to community businesses that sell essentials, for premises, equipment and set-up costs, where banks will not, and that public utilities move to Collective charters. In the model, a fund paced at the rate new stores open in these sectors, with young firms' failure rates, helps in no environment or design: where the community businesses would reach their demand ceiling within ten years anyway, it brings the gain forward at a cost of $37-63 per adult a year; where capital holds them back (the opt-in design under stress), it lifts their share from 34% to 48% by year 20, but the running-cost subsidy and the fund's outlay raise the programme's contribution, and basket poverty rises by 0.07 points and median wealth falls by $391. The changes are small beside the programme's own effect, and no reading of the fund (slower or faster, fewer failures, all grants) changes the verdict. Charters of public utilities improve every reading where they act and worsen none: at one customer in seven, the share public power serves today, only under stress, and at two in three, basket poverty falls by 0.02-0.06 points at $53-95 per adult a year. The release's main row is unchanged.

## 11. Where everything is

- **Preregistration:** research-update `prereg/2026-11-s94-collectives-lending.md` (Amendment 1: the outside readings, before the build; Amendment 2: choices made in the build, with dated notes on the engine commit and the dry run).
- **Engine:** v5.9.21, `c5682f9`; the switch is row option `lend`. Sources: `sources/s94_lending.py`. The reading note: [s94-collectives-lending-reading.md](s94-collectives-lending-reading.md).
- **Job:** compassionism-sim-results `runner/jobs/s94.js`.
- **Results:** `s94-{ref,adv,str}-{20,40}-c5682f9` (runs 167-172), each with `run.txt` and `SHA256SUMS`.
- **Tables:** `s94-tables-c5682f9` (`python3 dev/tools/s94_tables.py <results> <out>`): the checks, the tables at 20 and 40 years, decision rule 6, and `s94-summary.json` with every figure and interval.
- **Decisions:** `dev/DECISIONS.md`, the entry of Nov 21, 2026 on reading this study.
