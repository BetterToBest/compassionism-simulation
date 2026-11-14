# PTF realism: what not-for-profit grocers and utilities cost, who pays, PTF workers, and the density tests (S62)

Nov 14, 2026. Pilot: seeds 1-100, 500 adults, 20 years, three environments, engine `3500d0b`. A pilot is a mechanism check, not a result; the frozen 500-seed batch decides. Preregistered before the build and before any run (research-update `prereg/2026-11-s62-ptf-realism.md`, with one dated amendment before the pilot). Tables: `dev/runs/s62-ptf-ops/tables.md`. Per-seed files: compassionism-sim-results `s62-ptf-ops-3500d0b`. All rows use open PTF access (anyone may buy at PTF prices) with S55's growth rule.

## In short
1. **The question.** The Hub prices a PTF (a not-for-profit community grocer or utility) at "direct costs plus minimal cooperative overhead": food at 37.8% of the market price, utilities at 55.6%. Outside data say a not-for-profit grocer's full cost is about 97 cents per market dollar (the goods alone cost about 71 cents), and a not-for-profit utility's about 81 cents. So the Hub's PTF food price covers about 39% of full cost and its utility price about 68%. Duke decided (D19) that the Source pays the gap as an explicit subsidy counted in programme cost. This step builds that, and the readings beside it.
2. **The engine was already paying most of that gap.** Since plan step 5 the model has counted the PTF price cut as programme cost, less the part a not-for-profit funds by not paying owners. So adding sourced costs changes little: at the main reading the gap the Source pays is about **$1,260 per adult a year in the release design (3.9% of programme cost; 4.1% under Adverse, 3.6% under Stress) and $1,300 in C2.2 (2.2%)** in Reference; the 1.7% reserve adds about $45 of that. PTF sales at Hub prices cover about 41% of PTF running costs (51-57% under Stress, where fewer zones pass the density test).
3. **Taking the Hub's costs as stated** (no gap) would lower programme cost by about $1,240-1,300 per adult a year against the main reading (about 4% in the release design, 2% in C2.2); poverty would be 0.05-0.7 points lower, because the contribution that pays the subsidy is smaller.
4. **If prices rose to full cost instead** (D19's other option: no subsidy), the PTF food discount falls from 54% to 3% and the utility discount from 44% to 19%. Programme cost falls by $1,390 (release) to $2,360 (C2.2) per adult a year against the main reading, but the programme does less: basket poverty falls 0.35-1.0 points less (0.08 under Stress release), wealth poverty 0.1-0.7 points less, and the price level at year 20 is up to 35% higher (the C2.2 design: Reference 785 to 1,001 times year 0's; Adverse 2,898 to 3,922; the release design 4% higher, and unchanged under Stress). Every effect keeps its sign.
5. **PTF workers.** PTF jobs are about 0.84 per 100 adults (1.0% of workers' hours; 0.40 and 0.48% under Stress release). Moving the conversion bonus from PTF members to PTF workers, as the Hub states it, shrinks it from a mean 6.5% on converting participants' rates to 0.25%. Conversion payouts fall about 1.2% (release) and 2.6% (C2.2); programme cost falls $210 and $1,050 per adult a year; poverty moves by 0.2 points at most.
6. **PTF wages** follow S60's wage setting. At its main reading (no bargained raise) nothing changes; at 3 cents a dollar the PTF payroll rises 0.8-1.1% and the subsidy by $2-4 a year.
7. **The smooth curve (D20)** lowers the PTF food price factor where the network sits just above the 40% test: at purchases it averages 2.17 against the step's 2.46 (Reference), so the subsidy is about $100 lower and poverty 0.02-0.1 points less reduced than with the step. Where shares sit below 40% (Stress release) it is slightly higher than the step (1.79 against 1.77). Narrower and wider bands move it as expected (2.40 at half-width 0.10, 2.09 at 0.40).
8. **What the tests read.** Read on members' share of adults (about 21%), the food factor falls to 1.71 and poverty is 0.05-0.25 points less reduced; read on the share of demand the network's capacity can serve, it rises to 2.59.
9. **Staff.** No sourced limit binds below a 100% share. As stress readings, a hiring limit of 5 points a year binds in a fifth of years (the mean share 41.3% against 41.8%), and 2 points a year in four fifths (34.6%); both reach the 49% demand ceiling by year 19. Poverty moves by under 0.2 points.
10. **For the design freeze (S63), as preregistered:** `po` at its main reading in the main row, with the price-rise reading (no subsidy), the Hub's costs as stated, and the papers' step beside it on every outcome; the rest to S70's screen. No reading changes the sign of any programme effect.

## Claude's reading of the design
The BLEI paper (section 3.3) sets PTF prices "to cover direct costs plus minimal cooperative overhead": food at 37.8% of the market price at mature scale (ε 2.64), with "direct variable costs (production, logistics, perishables) at approximately 35–40% of consumer price". Outside data put the goods alone at about 71 cents of a grocer's sales dollar (Census's 28.8% gross margin) and running the store at about 26 cents more (Census AIES 2024). A grocer cannot sell at 37.8% of the market price on those costs. Duke's answer to D19 is that the Source pays the gap, as an explicit subsidy counted in programme cost; this step models exactly that and keeps the Hub's prices. Who works at a PTF is not said: the cautious reading (a modelling assumption) spreads PTF jobs over each zone's workers like the sector's jobs. The smooth curve of D20 moves the PTF cost share linearly between the paper's two values across a band centred on its 40%, so the paper's step is the curve's limit as the band narrows. θ (the synergy coefficient) is already a continuous ramp from 55% and is left as it is. These are readings of the model, not changes to the design.

## What was built (switch `PTF_OPS`, row option `po`; off is the engine as it was)
- **Running costs per market dollar.** Full cost (main): 1 less what owners, lenders and income tax take in the industry (BEA's net operating surplus less depreciation: food 4.94% of sales, utilities 20.3%), since a PTF's capital comes from the reinvestment account, plus a 1.7% reserve (FMI's 2025 net margin, read as what a going concern keeps): food 0.968, utilities 0.814. Observed sector costs: food 0.972 (Census: goods plus operating expenses); utilities 0.839 (public power's residential price over investor-owned utilities' in the same state, EIA-861 2024). The Hub's costs as stated: the cost is the PTF price (no gap).
- **Who pays (D19).** The Source pays the gap between the PTF price and the running cost (main), counted in programme cost; or prices rise to running cost (the cut shrinks to 3.2% on food and 18.6% on utilities, and nothing is paid). The engine already counted the cut less the industry's forgone profit as programme cost (plan step 5); full cost without the reserve reproduces that accounting exactly.
- **PTF workers.** Each worker works 2.42% × s of their hours at PTFs (food and beverage stores plus utilities over all jobs, BLS 2024; s their zone's PTF share of sales), and the conversion-rate bonus (1.30 + θ) applies on that share. Members no longer get the bonus as members.
- **PTF wages** are set by S60's wage setting (main: no bargained raise). With a raise, PTF payroll (10.4% of food sales, 11.4% of utility sales, Census) rises and so does the running cost.
- **Staff.** No hiring limit in the main reading (PTF staff are the sector's workers moving with its sales). A limit on how fast the network's share can rise (5 or 2 points a year) is a stress reading with no source.
- **The density tests (D20).** Smooth curve (main, band 20% to 60%; 30% to 50% and 0% to 80% swept) or the papers' step at 40%; the tests read the PTF share of sales (main), the members' share of adults, or the share of demand the network's capacity can serve.
- Ten unit tests (`poUnitSuite`); guard test identical; engine lineage linked; no random draw added.

## Sources (opened for this step)
- Census, Annual Integrated Economic Survey 2024 (national tables, Sep 2026): food and beverage stores revenue $982.2 billion, payroll $101.7 billion, 3.40 million employees, operating expenses $255.7 billion; utilities revenue $790.5 billion, payroll $89.9 billion, operating expenses $581.4 billion; child day care, tax-exempt providers: operating expenses 97.0% of revenue.
- EIA, Sales, Revenue and Average Price 2024, Table 6 (form EIA-861): public power's residential price is 0.839 of investor-owned utilities' in the same state (45 states, weighted by public power's sales); cooperatives 0.942. APPA: public power pays 5.1% of revenue to its communities.
- BLS Current Employment Statistics 2024 (via FRED): 157.7 million nonfarm jobs; food and beverage stores 3.23 million; utilities 0.59 million.
- FMI: 2025 food-retail net margin 1.7%. CRS R48252: most child-care providers earn under 1%. NCG: 169 food co-ops, 241 stores, $2.8 billion (no margins published). NGA/FMS independents' 1.9%: trade press only, not used.
- Figures and file hashes: `sources/s62_ptf_ops.py`.

## Limits
- One running cost per sector for every zone and share; scale economies enter only through the Hub's ε.
- PTF jobs are spread over all workers, not given to particular adults; no job is created or lost.
- The hiring limit has no source and is a stress reading.
- Utilities' observed reading is electricity only; gas and water are read at the same ratio.
- Child care has sourced costs but no PTF share in the engine's basket; its figures are recorded, not used.
- No sector-specific demand ceiling: no source gives one for open-access not-for-profit utilities or child care; S55's 49% and its sweep stand.
- Tested on S60's rows with open access only; S68's pairwise tests cover the other switches.

## Results (pilot; paired against each design's own no-programme run; intervals unadjusted)
The identity check passed: the reading that reproduces step 5's accounting equals the row without `po` on all 201 kept series in all three environments.

**What each reading does (Reference, release design; C2.2 in brackets).**

| reading | subsidy $/adult-yr | % of cost | food factor at purchases | sales over running cost | mean conversion bonus | programme cost against main |
|---|---|---|---|---|---|---|
| main | 1,257 (1,303) | 3.9 (2.2) | 2.17 (2.19) | 41% (41%) | 0.25% | 0 |
| Hub's costs as stated | 0 | 0 | 2.17 | 100% | 0.25% | −1,243 (−1,269) |
| prices rise to full cost | 0 | 0 | 1.03 | 100% | 0.25% | −1,390 (−2,356) |
| observed sector costs | 1,281 (1,329) | 4.0 (2.2) | 2.17 | 41% | 0.25% | +25 (+26) |
| no reserve | 1,211 (1,256) | 3.8 (2.1) | 2.17 | 42% | 0.25% | −45 (−45) |
| bonus on members | 1,256 (1,303) | 3.9 (2.1) | 2.17 | 41% | 6.5% | +211 (+1,046) |
| papers' step | 1,353 (1,413) | 4.2 (2.4) | 2.46 (2.50) | 38% | 0.25% | +108 (+203) |

**Programme effects that move most** (basket poverty, points of adult-years; Reference release / C2.2): open access without `po` −18.50 / −29.64; main −18.38 / −29.56; Hub's costs −18.74 / −29.61; prices at full cost −17.54 / −29.21; tests on members −18.22 / −29.49; bargaining at 3 cents −18.79 / −29.75. Adverse release: −22.25 open, −22.10 main, −21.08 prices at cost. Weighted wealth poverty (last year): main −14.82 / −21.75; prices at cost −14.41 / −21.38. The top 1% wealth share moves by at most 0.13 points in any reading. Every table, environment and reading: `dev/runs/s62-ptf-ops/tables.md`.

**Signs (rule 3).** No reading gives any of the five outcomes (basket poverty, wealth poverty, household basket poverty, the price level, programme cost) the other sign from the main reading's, in any environment or design.

## The preregistered rules
1. Checks: unit tests (10) and the guard test pass; the identity reading equals the row without `po` everywhere. **Met.**
2. The subsidy is reported in dollars and as a share of cost for every reading and design (tables, section 2), against the step-5 accounting (`hub0`). **Done.**
3. No sign change (above). **Met.**
4. Recommendation to S63 (fixed before the run): `po` main in the main row; beside it the price-rise reading, the Hub's costs as stated and the papers' step; to S70's screen the sector costs, no reserve, the band widths, the two test readings, the hiring limits and the bonus on members. S63 chooses.
5. No synergy is claimed.

## What the sources said, where it differs from the plan
- The identity reading in the plan (the Hub's costs) could not reproduce the engine, because the engine already counted the subsidy; the amendment before the pilot replaced it with full cost without the reserve, which does.
- Public power's observed price (0.839 of investor-owned utilities') lands close to the full-cost reading (0.814), so the two utility readings agree; the food readings (0.968 and 0.972) agree too. The large gap is between all outside readings and the Hub's cost structure, not among the outside readings.
- NCG publishes no co-op margins and the NGA/FMS study was not found open; neither gives a figure here.
