# Limits on supply, wages that lag prices and a delayed BU: what the v6 engine finds

Nov 18, 2026. The results of the preregistered study of limits on supply and indexing, on engine v5.9.19 (compassionism-simulation `aa2a4e0`). Preregistration: BetterToBest/research-update `prereg/2026-11-s82-v6-supply-indexing.md`, with Amendments 1-7. How the model reads the design where Duke Johnson's writing is silent: `dev/reports/s82-supply-reading.md` (Claude's reading of the design, written before the build). Tables: `dev/runs/s82-batch/`. Results: compassionism-sim-results `s82-v6-<environment>-<years>-aa2a4e0`, the ageing rows rerun on the fixed engine in `s82-v6-age-<environment>-<years>-ab11c05`, and the tables in `s82-tables-ab11c05` (the batch's first tables, `s82-tables-aa2a4e0`, are kept; only their ageing rows are superseded).

## 1. What was asked

The outside reviews of v5.9 found that, below full backing, the model had no limit on what the economy can supply, and that wages, the Basic Unit (BU) and the cost-of-living basket all followed prices in full and at once. With no backing, the programme still cut basket poverty by about 31 points while prices rose 40% a year. This study adds three readings, each behind its own switch, and asks how much of the programme's effect survives each one at every backed share (0, 0.25, 0.5, 0.75 and full backing):

- **A. A limit on supply** for the three goods with physical capacity: housing, medical care and food. Supply starts from the economy's headroom (from opened sources), then capacity is built over the years. What is still unmet is cut, shared by one of three rules: the market's (those least able to pay go short first), even, or the design's (basics bought with the BU are served first).
- **B. Wages that follow programme inflation only in part**: three quarters or half of it, either never made up or made up a year later.
- **C. The BU following the price of the needs with a delay**: a month (the design's monthly adjustment), a quarter, a year (as Social Security's), or two years (a bound).

It also asks whether they interact, who goes short, a set of smaller readings from the reviews, and how an earlier screen of assumptions reads in the Stress environment.

**The backed share** is the part of the programme's payout matched by new output. Full backing is the main row, and its published figures cannot change here (the limit is inactive there: check 3). **Environments:** Reference (today's economy), Adverse (repeated recessions and an automation wave), and Stress (the Adverse economy with the programme's own settings at their weakest). Seeds 1-500, paired across every row; 500 adults; 20 years (the primary horizon) and 40.

Effects are the programme run minus its own no-programme run, in percentage points (wealth in Year-0 dollars), with 95% intervals from 10,000 bootstrap replicates. "The change a reading makes" is the reading's effect minus the effect without it, at the same share. Every change quoted below survives a Holm correction across the six primary readings unless said otherwise.

## 2. The answer in short

1. **The supply limit costs little.** Under the sourced limit, the programme's cut in basket poverty is at most 0.54 points smaller than without it (no backing, the market's sharing rule, Stress, 20 years). At the strict bound (no essentials at all beyond today's needs consumption; not the economy and not the design) it is at most 3.7 points smaller at 20 years and 5.1 at 40. **But the limit as built can move only basket poverty.** The money a cut leaves unspent goes to other goods and the cut moves no price, so wealth, days of basic living and inflation are identical with and without it in every seed. So the one real test is basket poverty. Its effect holds under the sourced limit at every share, in every environment and at both horizons, with all three sharing rules. It also holds at the strict bound, at the slowest building speed swept, and at half and double the essentials' price response. The other five primary readings pass the same test only by construction, which is not a finding.
2. **Wages that lag prices are what make the results depend on backing.** If wages follow half of programme inflation and the rest is never made up, the programme with no backing leaves basket poverty 9.6 points *higher* than no programme (Reference; 5.0 in Adverse, 9.6 in Stress). Inflation runs 146-190 points a year, and the programme is no better than no programme on basket poverty below a backed share of 0.08-0.26 at 20 years and 0.30-0.49 at 40. If the lost part is made up a year later, the cost falls to 0.3-1.5 points.
3. **The design's monthly and quarterly adjustments of the BU cost little; a yearly one costs a lot.** With no backing, a monthly delay costs 0.7-1.3 points of basket poverty and a quarterly one 1.5-2.7. A yearly delay costs 7.0-11.1 points and the two-year bound 12.0-17.2. At full backing the monthly delay costs 0.04 points or less and the two-year bound 0.8 or less.
4. **Together** (sourced limit, wages at three quarters made up a year later, the BU a year behind), the programme loses 8.4-8.6 points of its basket-poverty cut with no backing in Reference and 13.2-13.9 in Adverse and Stress. The yearly delay accounts for 81-93% of that. The readings interact (chiefly the wage lag with the delay), so the joint figure is the one to quote.
5. **Who goes short.** With no programme, the poorest fifth already leaves 54-58% of its needs basket unpaid: the market rations by ability to pay today. Under the market's sharing rule, a shortage falls about nine times as hard on the poorest fifth as on the richest. The design's rule (BU purchases served first) puts slightly less of it on the poorest fifth than on the richest.
6. **Ageing** (adults who age, retire and are replaced): the programme cuts basket poverty 6.6-8.8 points more than with a fixed population at 20 years, with or without backing. The first batch's ageing rows measured an engine defect (wages that outran prices many times over); it was found, fixed and the ageing rows rerun before any of their figures were reported (section 9).

## 3. Checks, and what was fixed before these figures

Every preregistered check passed before any table was read, in all three environments and both horizons (`dev/runs/s82-batch/s82-checks.md`):
- the results files match their checksums, and the 20 pieces of each run cover seeds 1-500 once, on the pinned engine with a clean checkout;
- the supply limit with full supply equals the base row at no backing in every key (check 2);
- the strict bound at full backing equals the main row in every key, with each rule (check 3);
- the no-programme run is unchanged by the wage readings (check 4);
- every value is finite, and every run read the same seed's no-programme median.

**The first batch was not used.** It ran on engine `eb0969c`. Inspection after its checks found that the design's sharing rule cut two to four times its target: it divided this year's cut by last year's totals, and the share bought with cash swings from year to year. The rule was fixed (v5.9.19) and the whole batch rerun (Amendment 5); only the rerun is reported here. Two checks were added for the rerun, and both pass. Every row that does not use the design's rule below full backing is identical to the first batch in every key and seed: 179 of 231 rows (check 11). Under the design's rule, the total cut now equals the even rule's in every seed (check 12).

## 4. The supply limit (question 1)

### How much of the programme's cut in basket poverty is lost

The change the limit makes, in points of basket poverty, at no backing and at half backing (20 years). The effect without the limit is in the first row; a positive change means the programme does less. Rules: market / even / design's.

| Reading | Reference, share 0 | share 0.5 | Adverse, share 0 | share 0.5 | Stress, share 0 | share 0.5 |
|---|---|---|---|---|---|---|
| Effect without the limit | −30.96 | −31.64 | −38.66 | −39.65 | −37.11 | −38.75 |
| Sourced | 0.38 / 0.20 / 0.24 | 0.11 / 0.06 / 0.07 | 0.50 / 0.27 / 0.31 | 0.15 / 0.08 / 0.10 | 0.54 / 0.31 / 0.35 | 0.17 / 0.09 / 0.11 |
| Restricted (a policy reading: every sourced value halved, standing for today's land-use, residency and farm policies) | 0.91 / 0.50 / 0.57 | 0.35 / 0.19 / 0.22 | 1.35 / 0.75 / 0.84 | 0.49 / 0.26 / 0.31 | 1.54 / 0.88 / 0.99 | 0.60 / 0.32 / 0.39 |
| The strictest case: no essentials beyond today's needs consumption; not the economy and not the design | 2.06 / 1.12 / 1.23 | 0.86 / 0.46 / 0.53 | 3.13 / 1.74 / 1.86 | 1.24 / 0.66 / 0.77 | 3.68 / 2.12 / 2.21 | 1.60 / 0.88 / 1.01 |

With no programme, basket poverty is 36.1% in Reference and 44.6% in Adverse and Stress. Every change in the table has an interval that excludes zero. The market's rule always costs most: it cuts those least able to pay, who are the ones nearest the poverty line.

### Does each result hold? (decision rules 2 and 3; Amendments 3 and 4)

A result "holds under a supply limit" when, under the sourced reading and with all three sharing rules, it keeps its sign and its interval excludes zero. Every one of the six primary readings holds at every share from 0 to 0.75, in every environment, at 20 and 40 years. That is basket poverty, below 30 days of basic living, wealth poverty (yearly and at the last year), and median real wealth (weighted and unweighted). None rests on the sharing rule (decision rule 3): each holds with the market's rule too. Each also holds:
- **at the slowest building speed swept for medical care and food** (0 a year, which puts those two sectors at the strict bound; the sourced row uses 0.25, a design parameter). In Reference at no backing, the market's rule then costs 0.88 points instead of 0.38;
- **at half and at double the essentials' price response** (θ, an unsourced engine value). It decides how far prices rise and how much better-off households give up. At half θ the sourced limit costs 0.48 points (Reference, no backing, the market's rule); at double, 0.25;
- under the restricted reading and at the strict bound, with all three rules.

**What "holds" means here.** The limit as built cuts the housing, care and food that households receive. The money they could not spend on them goes to other goods, and the cut does not move prices (the engine reads essentials demand before the cut). So days of basic living, both wealth poverty readings, both median wealth readings and programme inflation are identical with and without the limit, in every seed. For these five readings the test above passes by construction. The limit's real cost shows in basket poverty, read on what households received, and in the shortfall table (section 8). A reading in which the shortage raises prices or forces saving is not in this engine (a stated limit, section 11).

### Break-even backed shares

Under every supply reading, including the strict bound on its finer grid (every eighth of backing), no primary reading reaches the point where the programme is no better than no programme, at any share, in any environment, at either horizon. The limit does not change where programme inflation falls below 5 points a year: above a backed share of about 0.88 in Reference, 0.89 in Adverse and 0.90 in Stress (20 years). With no backing, programme inflation is 40 points a year in Reference, 46 in Adverse and 49 in Stress, under every supply reading.

### The limit's own figures (Reference, 20 years)

At no backing the programme's extra need is 14.4% of needs consumption. Under the sourced reading the target cut is 1.1% of housing and 2.6% of medical care and food; the realised cut over all three is 1.7%. At the strict bound it is 12.6% of each. The realised cut runs at about (T−1)/T of the target's mean even for a rule that cuts its target exactly: year 0 has no cut, and the last target is for a year never run. At half backing the sourced cut is 0.6%; at three-quarters, 0.2%.

## 5. Wages that follow prices in part (question 2)

Basket poverty: the programme's effect at no backing, and the break-even backed share (20 years). Wage readings are design parameters: no source was found for how wages respond to an inflation the programme itself makes. The readings never made up are the pessimistic end of the range swept; which reading is nearest reality is not known.

| Wages follow programme inflation | Reference | Adverse | Stress |
|---|---|---|---|
| In full (today's engine) | −30.96; none | −38.66; none | −37.11; none |
| Three quarters, made up a year later | −30.66; none | −38.22; none | −36.48; none |
| Half, made up a year later | −30.28; none | −37.64; none | −35.63; none |
| Three quarters, never made up | −23.76; none | −25.49; none | −16.87; none |
| Half, never made up | **+9.58**; 0.13 | **+4.99**; 0.08 | **+9.63**; 0.26 |

"None": the effect stays favourable at every share on the grid. With half never made up, the programme with no backing leaves more people below the basket's cost than no programme does. Other readings at no backing (Reference) with half never made up:
- inflation 146 points a year (161 in Adverse, 190 in Stress), against 40 with full indexing;
- the mean wage at year 20 falls to $22,246 a year in Year-0 prices, against $94,430 with full indexing and $92,205 with no programme;
- wealth poverty falls by 10.4 points instead of 19.0;
- median real wealth falls by $5,749 against no programme, instead of rising by $86,845. Its break-even backed share is 0.08 (weighted) and 0.12 (unweighted).

**At 40 years** the lag compounds:
- with half never made up, the break-even share for basket poverty is 0.38 in Reference, 0.30 in Adverse and 0.49 in Stress; for median real wealth it is about 0.75 in Reference, 0.30-0.31 in Adverse and 0.47-0.49 in Stress; and for wealth poverty at the last year, 0.33 in Reference;
- with three quarters never made up, basket poverty breaks even at 0.07 in Reference and 0.12 in Stress, wealth poverty at the last year at 0.06 in Reference, and median real wealth at 0.60-0.61 in Reference, 0.06-0.09 in Adverse and 0.26-0.28 in Stress;
- with the lost part made up a year later, no reading breaks even, except median unweighted wealth in Reference at half indexing (0.012; 11% of the bootstrap replicates are below 0).

At full backing the wage readings change nothing (identical in every seed): there is no programme inflation to follow.

## 6. The BU's delay (question 3)

The design's monthly and quarterly adjustments come first (decision rule 6). The change in basket poverty, at no backing / half backing / full backing (20 years):

| The BU follows the needs' price | Reference | Adverse | Stress |
|---|---|---|---|
| A month behind (the design's monthly adjustment: half a month's average delay plus a month for the figures) | 0.69 / 0.30 / 0.01 | 1.10 / 0.46 / 0.03 | 1.30 / 0.68 / 0.04 |
| A quarter behind | 1.52 / 0.64 / 0.01 | 2.42 / 1.02 / 0.06 | 2.67 / 1.42 / 0.09 |
| A year behind (as Social Security's adjustment) | 6.97 / 3.62 / 0.05 | 10.77 / 5.82 / 0.24 | 11.06 / 6.51 / 0.36 |
| Two years behind (a bound) | 11.99 / 7.37 / 0.12 | 17.22 / 11.97 / 0.52 | 16.97 / 12.68 / 0.77 |

What a month of the BU buys at the needs' price, at no backing (Year-0 dollars; $1,788 with no delay):
- a month behind: $1,691-1,721;
- a quarter behind: $1,593-1,654;
- a year behind: $1,152-1,280;
- two years behind: $843-970.

Other readings at no backing, Reference:
- wealth poverty rises 0.44 points (monthly), 0.90 (quarterly), 3.1 (yearly) and 4.7 (two years);
- median real wealth falls $4,398, $8,568, $23,784 and $28,612;
- the share of adults below 30 days of basic living rises 0.10, 0.20, 1.73 and 3.76 points.

At 20 years no delay brings any reading to break-even. At 40 years in Reference, median real wealth breaks even at 0.17-0.21 with a yearly delay and 0.28-0.31 with two years; no other reading does. Today's safety net keeps its own indexing in both runs, so the delay falls only on the programme run (the cautious side).

## 7. The three together (question 4)

The 2 × 2 × 2 design at the preregistered central readings:
- A: the sourced limit, with the market's rule or the design's;
- B: wages at three quarters, made up a year later;
- C: the BU a year behind. This is the yearly delay, not the design's quarterly one, so the joint figures are a cautious case.

Basket poverty, no backing (20 years), market's rule / design's rule:
- **Joint change:** Reference 8.57 / 8.42; Adverse 13.43 / 13.23; Stress 13.85 / 13.66.
- **Shares of the joint change** (Shapley values): the BU's delay 86-88%, wages 9-10%, the limit 3-5%.
- **Interactions** (each claimed only where its interval excludes zero):
  - wages × delay adds 0.84 points in Reference, 1.59 in Adverse and 1.54 in Stress;
  - limit × wages and limit × delay add 0.01-0.11 points;
  - all three together are claimed in a few cells, at 0.02 points or less.
  - The interactions make the joint change larger than the sum of the parts, so the parts are not added anywhere (decision rule 7).

Other readings, no backing:
- wealth poverty's joint change is 3.8 points (Reference), 4.5 (Adverse) and 4.2 (Stress);
- median real wealth's is −$29,462, −$25,780 and −$19,771;
- the limit adds nothing to either (identical in every seed);
- at half backing the joint change in basket poverty is 4.1-4.2 points in Reference and 6.6-7.5 in Adverse and Stress.

## 8. Who goes short (question 5)

Shares of the needs basket, mean over adult-years, by fifth of cash income over the cost of living (fifth 1: the least able to pay). Reference, 20 years, no backing.

| | Fifth 1 | Fifth 2 | Fifth 3 | Fifth 4 | Fifth 5 | All |
|---|---|---|---|---|---|---|
| No programme: need nobody paid for | 54.26 | 11.92 | 0.13 | 0.06 | 0.01 | 13.28 |
| Programme, no limit: need nobody paid for | 3.69 | 0.24 | 0.11 | 0.06 | 0.01 | 0.82 |
| Sourced limit, the market's rule: supply cut | 1.22 | 0.96 | 0.67 | 0.39 | 0.13 | 0.67 |
| Sourced, even: supply cut | 0.68 | 0.71 | 0.71 | 0.71 | 0.71 | 0.71 |
| Sourced, the design's rule: supply cut | 0.59 | 0.67 | 0.68 | 0.71 | 0.77 | 0.68 |
| Strict bound, the market's rule: supply cut | 8.62 | 6.82 | 4.83 | 2.88 | 0.95 | 4.82 |
| Strict bound, the design's rule: supply cut | 4.69 | 4.95 | 5.05 | 5.21 | 5.43 | 5.07 |

The no-programme run is never cut by the limit. Its poorest go without through prices, as today, and on that measure the poorest fifth leaves more than half its basket unpaid (57.7% in Adverse and Stress). Under any limit and rule, the programme's poorest fifth goes far less short than with no programme.

Adverse and Stress have the same shape. With the sourced limit, the market's rule cuts the poorest fifth 1.51% and the richest 0.16-0.17%. The design's rule cuts them 0.71-0.74% and 0.96-0.99%.

A caution on reading basket poverty under the limit: a household counts as short only when its income, less the money a shortage left unspendable on needs, falls below its cost. A better-off household can be cut without being counted. This table counts every cut. Every adult takes part under full coverage, so the participants' figures equal the totals.

## 9. The smaller readings (question 6)

Each is its own pair, at no backing and at full backing. These are changes to the effect in Reference at 20 years (no backing / full backing); Adverse and Stress are in the tables.
- **The share of extra wage income spent, 0.862 instead of the engine's** (theme 9):
  - basic living +0.15 / +0.14 points;
  - wealth poverty −0.04 / −0.07;
  - median real wealth −$299 (not significant after Holm) / +$21,143.
- **The wealth tail's exponent at plus and minus two standard errors** (theme 11): under 0.01 points on every poverty reading; median wealth moves by $11-745.
- **The tail cut at the 95th percentile** (theme 11): the programme cuts basket poverty 0.34-0.35 points more, basic living 0.29 and wealth poverty 0.33-0.36.
- **The PTH equity base from the basket** (theme 15): 0.02 points or less; about $100 of median wealth.
- **Ageing** (theme 13: adults age, retire and are replaced, with yearly moves in and out of the labour force). Each figure is the change ageing makes to the programme's effect; no backing / full backing:
  - basket poverty −8.67 / −8.81 points (the programme does more: with ageing the no-programme run has more people below the line);
  - basic living −1.16 / −1.08;
  - wealth poverty −1.52 / −1.35 (yearly) and −3.10 / −2.61 (last year);
  - median real wealth +$20,783 / −$1,102 (the second not significant after Holm);
  - programme inflation +2.2 points a year at no backing (42.6 against 40.3); unchanged at full backing.
  - Adverse and Stress: basket poverty −6.6 to −6.9 points, the same signs elsewhere.
  - At 40 years (labelled, as the triage asks: partnerships stay fixed), Reference: basket poverty −14.6 / −15.4 points; median real wealth +$63,639 / −$160,053. With ageing, median real wealth with no programme is far lower at 40 years ($127,000 against $413,000 with a fixed population), because each new adult starts with little. Against that lower level the unbacked programme adds more ($79,000 against $12,000), and full backing adds less ($284,000 against $442,000), since new adults have had fewer years of the BU.
  - Inspection (no threshold): the mean wage over the general price level at year 20 is $94,826 at no backing and $102,201 at full backing with ageing, against $94,430 and $101,372 without it.

  **The defect behind the first ageing figures, and the rerun.** The batch's ageing rows (engine `aa2a4e0`) at no backing showed wages outrunning prices many times over (a mean wage over the general price level of $655,202 to $1.37 million at year 20, against $61,000-102,000 in every other row). They were not reported (preregistration Amendment 6). The cause: with ageing, each adult who dies is replaced by a new adult whose wage is set in that year's prices. A new adult can start outside the labour force. The engine kept that adult's wage but not the price level at the time, so when the adult later went back to work it raised the wage by all the price rises since year 0, not just those since the adult arrived. Prices were counted twice, and those wages fed the average that sets later new adults' wages, so the error grew. It needs ageing, the yearly labour-force moves and a price level that has moved. The fix stores the price level when the adult is drawn (compassionism-simulation pull request 160; `dev/DECISIONS.md`, "the ageing defect located and fixed"); every row without ageing is unchanged.

  The three ageing rows were rerun on the fixed engine (`ab11c05`, seeds 1-500, all six environment-horizons). Their check (check 13) found that in Adverse and Stress the no-programme ageing run had also moved: outside inflation moves prices there even with no programme, so the defect had reached it too, slightly (at 40 years, wealth poverty 39.7 to 41.1 points and median real wealth $68,107 to $62,299). The check had assumed that run could not move; it was corrected before the ageing outcomes were read (Amendment 7), and every ageing effect above pairs runs on the fixed engine. In Reference that run is identical. The full-backing figures barely moved (Reference: within 0.01 points on every poverty reading and $41 of median real wealth; Adverse and Stress at 40 years, basket poverty about 0.3 points more and wealth poverty at the last year about 0.9 more), and are no longer provisional. The batch's ageing figures stay in `s82-tables-aa2a4e0`, marked superseded.

Section D's reporting keys (Reference, 20 years):
- **Wealth poverty at half the same seed's no-programme median** (theme 24): the programme cuts it by 15.4 points at no backing and 19.2 at full backing (yearly average), and by 15.6 and 28.2 at the last year.
- **The share below 30 days of basic living, weighted by the wealth tail's weights** (theme 10): the programme's effect is −19.6 points at no backing and −19.2 at full backing; the level with no programme is 20.1% (19.6% unweighted).
- **Wages over factor income** (theme 22): 84-85% in every row, against 84.5% with no programme.
- **Labour's share of money income:** 82.5% with no programme, 61.4% at no backing and 52.0% at full backing. The BU is money income that is not pay for work.

## 10. The assumptions screen in Stress and with the weighted tail (question 7)

The screen (the earlier assumptions screen's design, unchanged) was run on engine `eb0969c` and stands. It sets no supply limit, so the fix of section 3 cannot reach it. Folders: compassionism-sim-results `s82-screen-{s-str,ft,f-str}-eb0969c`; tables `dev/runs/s82-screen/`.
- **In Stress**, the earlier screen's list of the inputs that matter (those carried forward) covers both blocks of rows. Five Source-row inputs and three financed-row inputs are weaker there than in Reference and Adverse; none is stronger.
- **With the weighted wealth tail on the financed rows** (block FT, the contribution's base held at wages), four inputs move up:
  - the employer markdown and the policy-rate rule's response to the output gap, to carried in full;
  - the band of the PTF density tests, to full;
  - the PTF reserve, to one reading.
- The tail's own cutoff and the number of households per type are carried in full; the borrowing limit drops to held.

## 11. What this means, and its limits

**The dated note "the poverty effects barely depend on backing."** Under every supply reading, the programme's effect on poverty still barely depends on backing, and no break-even share appears: that holds with the restricted reading and with the strict bound, at 20 years and 40. In Reference at 20 years:
- with the sourced limit and the market's rule, basket poverty falls 30.6 points at no backing against 32.4 at full backing;
- with the strict bound, 28.9 against 32.4.

What does make the effects depend on backing is how fully wages and the BU keep up with the inflation an unbacked payout causes. If half of the inflation is never made up in wages, the programme with no backing is worse than no programme on basket poverty, and breaks even only at a backed share of 0.08-0.26 (20 years) or 0.30-0.49 (40 years). If wages are made up within a year, they cost 0.3-1.5 points of basket poverty at no backing. A monthly or quarterly BU adjustment, as the design says, costs 0.7-2.7 on its own. These two were not run together; the joint run uses the yearly delay (section 7). Programme inflation itself stays high below full backing in every reading: 40-49 points a year with no backing, under 5 only above about 0.88-0.90.

**Limits, stated:**
1. The limit cuts quantities only. Its unspent money goes to other goods, and it moves no price, so a shortage does not show in wealth, basic living or inflation (section 4). A reading in which a shortage raises prices further, or is saved, is not built.
2. Only housing, medical care and food can be short (Duke's narrowing). Other goods, and copied goods such as software, are never cut.
3. The extra need is spread over the three sectors in the basket's proportions. A cut answers last year's gap.
4. Design parameters, swept and labelled wherever shown:
   - the building speed of medical care and food;
   - the essentials' price response θ;
   - the wage readings (wIdx, wc);
   - the BU's delays (the monthly and quarterly ones follow the design's stated adjustment).
5. The BU's relief to the cost of living runs a damped two-year cycle in every programme row, the main row included. It predates this study and is its own inspection step in research-update's plan. *Nov 18:* the cause is the private businesses' lower BU price, which was paid from last year's premium instead of at the sale as the design has it; a fix is built behind an option and its rerun is preregistered (`dev/reports/s90-private-price-at-sale.md`).
6. The ageing reading was rerun after a defect was fixed (section 9). The batch's ageing figures are superseded, not quoted.
7. The population is fixed in every row but the ageing reading.
8. The design's surge protocol (luxury restrictions, conversion limits) is not modelled: the cautious side. The shortages here may be larger than under the design.
9. Building capacity costs nothing in the model's accounts, so the building-speed sweep is a physical sweep, not a fiscal one. The Creative Collectives' lending and output per hour are the next engine step, which is what can make backing produced rather than assumed.
10. Duke's views on supply policy (that the levers should be set by the people, and that the design supplies the basics with providers given a reason to supply them) are his and are kept apart from these results. Nothing here tests them.

## 12. Where everything is

- **Preregistration:** research-update `prereg/2026-11-s82-v6-supply-indexing.md` (Amendment 5: the first batch superseded; Amendment 6 and its addendum: the ageing reading flagged, the defect fixed; Amendment 7: the ageing rerun's check corrected).
- **Engine:** v5.9.19, `aa2a4e0`; the ageing rows on `ab11c05` (the same engine with the ageing fix).
- **Job:** compassionism-sim-results `runner/jobs/s82.js` at `4881a84`.
- **Tables tool:** `dev/tools/s82_tables.py`.
- **Results:** `s82-v6-{ref,adv,str}-{20,40}-aa2a4e0`; the ageing rows `s82-v6-age-{ref,adv,str}-{20,40}-ab11c05`. Each folder has `run.txt` with the command and `SHA256SUMS`.
- **Analysis:** `s82-tables-ab11c05` (`python3 dev/tools/s82_tables.py <results> <out> --engine aa2a4e0 --first eb0969c --age ab11c05`); the first tables `s82-tables-aa2a4e0`, their ageing rows superseded.
- **The first batch:** `-eb0969c`, marked superseded; no figure is quoted from it.
- **Decisions:** `dev/DECISIONS.md`, the entries of Nov 18, 2026 on this study (part 3, part 3b, the ageing defect located and fixed, and reading the ageing rerun).
