# Wealth held by asset class: what changes when a house is not treated as cash (S59, part 1)

Nov 10, 2026. Pilot: seeds 1-100, 500 adults, 20 years, three environments, engine `1d2cf29`. A pilot is a mechanism check, not a result; the frozen 500-seed batch decides. Preregistered before the build and before any run (research-update `prereg/2026-11-s59-asset-classes.md`, with two dated amendments). Tables: `dev/runs/s59-assets/tables.md`. Per-seed files: compassionism-sim-results `s59-assets-1d2cf29`.

## In short
1. **Until now the model treated all wealth as cash.** A house, a share portfolio and a business were each one number of dollars that never repriced. The programme's modelled inflation is about 30-45% a year, so after 20 years those dollars bought almost nothing. That single assumption produced most of every published wealth result.
2. **In the survey data, the model's families hold little net cash.** For the families the engine starts from, homes, shares, businesses and other real assets are about 98% of net worth. Nominal assets (deposits, bonds) are 20% of net worth and debts are 18%, most of them fixed-rate mortgages (2022 Survey of Consumer Finances).
3. **With wealth held by asset class, the programme's wealth-poverty harm becomes a reduction in every environment under the main reading.** In Reference, the release design moves from +21.5 points (more adults under $25,000 of real wealth) to −12.7; the C2.2 design from +0.7 to −18.2.
4. **Part of that reduction is debt relief that nobody in the model pays for: about half for the release design and a quarter for C2.2.** Inflation wipes out fixed-rate mortgages, and the model has no lender who loses. In the reading where fixed-rate debt reprices instead, the reductions are −6.7 (release) and −13.3 (C2.2) in Reference.
5. **One assumption can reverse the release design's result.** If houses, shares and businesses follow only half of the programme's inflation, the release design raises wealth poverty in Adverse (+9.1) and Stress (+3.6), and the C2.2 design's effect in Stress is nil. So for the release design the sign is not established. For C2.2 the effect is a reduction in 26 of the 27 asset-class cells (nine readings, three environments) and nil in the other.
6. **Basket poverty, the cost of living and inflation do not move.** The switch changes wealth only.
7. **The well-off still lose.** The top fifth by starting wealth loses about $240,000 per adult in real terms under either design in Reference, mostly nominal assets eroded by inflation. The other four fifths gain.

## What was built
Switch `RETURNS` (study row option `rt`), off by default. Off, every figure is identical (guard test, engine lineage, and a check row in the pilot).

**The opening split.** At the start each household's net worth is split by its wealth group. There are seven groups: net worth below zero, then up to the 25th, 50th, 75th, 90th and 99th percentile of the starting population, and above. Each group has its own balance sheet from the survey (`sources/s59_portfolio.py`):

| Group | Families | Debts over assets | Homes | Other real estate | Shares | Private business | Vehicles, other goods | Nominal assets | Fixed-rate share of debts |
|---|---|---|---|---|---|---|---|---|---|
| below zero | 7.7% | 1.82 | 43% | 2% | 8% | 1% | 27% | 19% | 93% |
| zero to P25 | 17.3% | 0.68 | 41% | 1% | 5% | 1% | 39% | 13% | 90% |
| P25 to P50 | 25.0% | 0.56 | 67% | 2% | 6% | 1% | 13% | 10% | 91% |
| P50 to P75 | 25.0% | 0.32 | 61% | 4% | 10% | 2% | 8% | 14% | 91% |
| P75 to P90 | 15.0% | 0.19 | 45% | 8% | 20% | 3% | 5% | 19% | 91% |
| P90 to P99 | 9.0% | 0.09 | 24% | 8% | 30% | 15% | 2% | 20% | 89% |
| P99 and above | 1.0% | 0.03 | 8% | 9% | 20% | 49% | 2% | 13% | 75% |

Asset columns are shares of the group's gross assets. The split uses only the household's starting net worth, so both runs of a pair start identical, with no random draw.

**Each year:**
- Real assets move with the price level and add a real price gain: homes 0.94% a year, shares 4.02% (Robert Shiller's published series, 1953-2022; price only, no dividends or rents). Other real estate takes the homes' rate and private business the shares' rate. Those two are modelling assumptions, because no price series was opened for them. Vehicles and other goods keep their real value.
- Nominal assets earn 0.46 of inflation. The source is Drechsler, Savov and Schnabl (*Quarterly Journal of Economics*, 2017): deposit rates rise 46 basis points for every 100 of the policy rate. Taking the policy rate to follow inflation one for one is a modelling assumption.
- Floating debt (credit cards, lines of credit, the 6.6% of mortgage dollars that are adjustable-rate) reprices in full. Fixed-rate debt keeps its dollar value.
- The year's saving repays floating debt first, then goes to nominal assets. A shortfall draws nominal assets to zero, then borrows at the floating rate. Real assets are never sold and fixed debt is never repaid.

Every one of these is swept below.

## Results

### The programme's effect on wealth poverty (points; programme minus no programme; year 20)
| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| today: all wealth is cash | +21.5 | +0.7 | +45.0 | +30.2 | +24.8 | +41.7 |
| by asset class, main reading | −12.7 | −18.2 | −13.2 | −20.2 | −7.1 | −18.7 |
| nominal assets earn nothing | −11.4 | −17.0 | −11.8 | −18.0 | −6.4 | −16.5 |
| nominal assets keep up with prices in full | −13.8 | −18.7 | −15.4 | −22.1 | −8.0 | −21.6 |
| real assets follow half of inflation | −2.1 | −14.1 | **+9.1** | −8.2 | **+3.6** | **0.0** |
| no real price gain | −14.3 | −20.2 | −14.8 | −22.5 | −8.4 | −20.9 |
| real price gains of 1983-2022 | −11.7 | −16.9 | −12.1 | −18.8 | −6.4 | −17.4 |
| real price gains of 1890-2022 | −13.3 | −19.0 | −13.8 | −21.2 | −7.6 | −19.6 |
| new saving split by the group's asset shares | −13.6 | −18.5 | −15.2 | −21.9 | −7.9 | −21.4 |
| fixed-rate debt reprices too (no debt relief) | −6.7 | −13.3 | −7.8 | −15.7 | −2.8 | −13.4 |

Intervals (2.5th to 97.5th percentile of 2,000 paired bootstrap replicates, unadjusted) are within ±0.6 points of each figure; the Stress C2.2 cell under half indexing is −0.03 (−0.58 to +0.49). The "today" row reproduces the earlier trace's published figures exactly.

### Other outcomes (Reference; programme minus no programme)
| Outcome | Release, today | Release, main | Release, no debt relief | C2.2, today | C2.2, main | C2.2, no debt relief |
|---|---|---|---|---|---|---|
| Median real wealth | −$182,800 | +$43,600 | −$43,800 | −$171,500 | +$65,700 | −$22,500 |
| Real wealth at the 10th percentile | +$12,200 | +$51,900 | +$20,900 | +$26,800 | +$80,500 | +$50,800 |
| Real wealth at the 90th percentile | −$1,254,500 | −$166,900 | −$326,700 | −$1,248,700 | −$153,800 | −$314,100 |
| Wealth Gini (debts kept) | −0.249 | −0.050 | −0.006 | −0.378 | −0.071 | −0.027 |
| Top 1% share of wealth (points) | −12.4 | −1.0 | +1.2 | −13.7 | −1.5 | +0.6 |
| Bottom 50% share of wealth (points) | +11.9 | +3.2 | +0.9 | +20.9 | +4.4 | +2.2 |
| Families in debt (points) | −12.4 | −15.1 | −10.9 | −21.2 | −19.6 | −16.9 |
| Basket poverty (points of adult-years) | −16.7 | −16.7 | −16.7 | −24.6 | −24.6 | −24.6 |
| Programme inflation (points a year) | +31.5 | +31.5 | +31.5 | +37.4 | +37.4 | +37.4 |

Two earlier findings do not survive. The halving of the wealth Gini and the 12-14 point fall in the top 1% share were the all-cash assumption: with assets by class the Gini falls by 0.05-0.07 and the top 1% share by 1.0-1.5 points, and without debt relief the top 1% share rises slightly.

### The three parts (Reference, main reading; real dollars per adult at year 20, programme minus no programme)
Each adult's real wealth is split into the opening nominal position held untouched (nominal assets and floating debt with their interest, less fixed-rate debt), the opening real assets held untouched, and the rest (saving since the start and what it earned). The three sum to real wealth exactly (unit test).

| Group by starting wealth | Release: opening nominal position | Release: saving | Release: whole | C2.2: opening nominal position | C2.2: saving | C2.2: whole |
|---|---|---|---|---|---|---|
| All adults | +$5,700 | −$24,000 | −$18,300 | +$3,500 | −$400 | +$3,100 |
| Lowest fifth | +$36,100 | −$15,800 | +$20,300 | +$36,100 | +$8,500 | +$44,600 |
| Second fifth | +$44,600 | −$3,700 | +$40,900 | +$44,500 | +$22,500 | +$67,000 |
| Middle fifth | +$74,000 | −$9,600 | +$64,500 | +$73,700 | +$14,800 | +$88,400 |
| Fourth fifth | +$54,800 | −$26,800 | +$28,100 | +$53,500 | −$3,300 | +$50,200 |
| Top fifth | −$181,000 | −$64,000 | −$245,000 | −$190,100 | −$44,400 | −$234,600 |

The opening real assets are the same in both runs (they follow the price level in full), so the programme's revaluation effect is zero by construction in the main reading. It appears only in the half-indexing reading, where it is about −$750,000 per adult: that reading is close to today's all-cash result for the same reason.

What this shows:
- **The mean real-wealth gap almost disappears.** The earlier trace measured −$561,600 (release) and −$551,700 (C2.2) per adult in Reference, 90-92% of it erosion of opening balances. With assets by class the gaps are −$18,300 and +$3,100.
- **The bottom four fifths gain on their opening position; the top fifth loses.** Families below about the 75th percentile owe more in fixed-rate debt than they hold in nominal assets, so inflation lowers their debts faster than it erodes their deposits. The top fifth holds nominal assets and little debt.
- **Under the release design new saving loses value** (−$24,000 per adult): it goes into nominal assets that earn less than inflation. If nominal assets kept up with prices, or new saving followed each group's asset mix, the saving part would be about +$60,000 to +$65,000 (release) and +$126,000 to +$132,000 (C2.2).
- **Without debt relief** the opening nominal position costs the average adult about $99,000 under the release design, and the whole gap is −$119,900.

### The no-programme run
In Reference the no-programme run has no inflation, so the all-cash assumption cost it nothing; the switch changes it only through real price gains (median real wealth at year 20: $212,300 today, $265,800 with the main gains). In Adverse and Stress the no-programme run has outside inflation, so the switch also stops that erosion (median $116,000 today, $232,500 main). The preregistration's Amendment 1 said the no-programme run has no inflation; that is true of Reference only (Amendment 2 corrects it).

The start is unchanged by the switch: the top 1% hold 20.8% of wealth against the Fed's 32.5% (Distributional Financial Accounts), a gap the weighted top tail (part 2) addresses. After 20 years with no programme the top 1% share is 18.2% today and 21.2% under the main reading. The top 1% of adults hold 47.5% of private business equity at the start and 48.1-48.2% at year 20 in every run: with no business income or ownership dynamics yet, this measure cannot move (part 2).

## Limits
1. **No creditor side.** When inflation wipes out a fixed-rate mortgage, a lender loses the same amount. The model has no lenders, so that loss lands on no one. The no-debt-relief reading removes the gain entirely; the truth lies between the two, and at 30-45% inflation it is doubtful that fixed-rate lending would continue at all.
2. **Do real assets keep up with 30-45% inflation?** The main reading says fully. Evidence from moderate inflation does not settle it, and the half-indexing reading changes the release design's sign in two environments. This is the assumption an economist should look at first.
3. **The 0.46 pass-through** is measured at US policy rates between 0 and about 6%, and applied here to 30-45% inflation.
4. **No capital income.** Dividends, rents and business profits are not paid to households; price gains only.
5. **Real assets are never sold and fixed debt is never repaid.** A household that runs short borrows at the floating rate rather than selling shares; mortgage payments stay inside the cost of living.
6. **Vehicles are treated as keeping their real value** (they are 27-39% of the assets of the two lowest groups); in life they wear out and are replaced out of spending.
7. **The split is by wealth group only**, not by age or tenure; renters and owners in the same group get the same mix.
8. **The starting table is the 2022 survey**, matching the engine's starting wealth; the 2025 survey is out and both should move together.
9. **Not yet tested with ageing or with the debt reading's liquid share** (for the pairwise switch tests).

## For the freeze (S63) and the findings page
- Recommended: `rt` main as a main-row candidate, with "all wealth is cash" beside it and two readings always shown with any wealth result: fixed-rate debt reprices (no debt relief), and real assets follow half of inflation.
- Wealth claims that rested on the all-cash assumption (the wealth-poverty harm, the fall in the wealth Gini and top shares, the fall in median real wealth) should be described as that assumption's result, not the programme's.
- A favourable wealth-poverty result for C2.2 can be stated as a conditional model result: it holds in every reading run here except half indexing in Stress, where it is nil, and it shrinks by about a quarter without debt relief.
- For the release design the direction is not established.

## Reproduce
```
python3 sources/s59_portfolio.py           # the split, from the survey's public files
python3 sources/s59_real_gains.py          # real price gains
node dev/tools/s59_assets.js ref 100 20    # also adv, st
python3 dev/tools/s59_table.py DIR         # tables.md
```
