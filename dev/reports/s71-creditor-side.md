# Who loses when inflation wipes out a debt: a creditor side for household debt (S71)

Nov 13, 2026. Pilot: seeds 1-100, 500 adults, 20 years, three environments, engine `f7572fd`. A pilot is a mechanism check, not a result; the frozen 500-seed batch decides. Preregistered before the build, before any coefficient was computed and before any run (research-update `prereg/2026-11-s71-creditor-side.md`, with one dated amendment before the pilot). Tables: `dev/runs/s71-creditors/tables.md`. Per-seed files: compassionism-sim-results `s71-creditors-f7572fd`.

## In short
1. **The gap this closes.** With wealth held by asset class, a fixed-rate mortgage keeps its dollar value while the programme's inflation runs 30-45% a year. The borrower's gain is real, and until now nobody in the model lost it. The earlier report said the programme's effect on the top 1% share of wealth turned on that missing lender.
2. **Who holds a dollar of household fixed-rate debt** (the Fed's Financial Accounts, end of 2022, traced through banks and funds to final owners): households hold 32 cents (24 as bank deposits and money market shares, 8 as bonds and bond funds); businesses hold 32 cents, which belong to their shareholders; the government holds 27 cents (the Federal Reserve's mortgage securities, federal student loans, public deposits); foreigners 8 cents.
3. **Part of the loss was already in the model, unlabelled.** The model pays savers only 46% of inflation on deposits and bonds, so they were already losing 54% of inflation on every dollar. Of each dollar of debt wiped out, 11 cents were already being lost by the model's savers. The option adds the rest: 2 cents more on their bond-like savings and 20 cents on their shares. The other 66 cents fall outside the model: 30 on the government, 16 on foreigners, 20 on households the model does not hold (mostly retired).
4. **Wealth poverty does not change.** The programme's effect on wealth poverty at year 20 is −12.5 points (release design, Reference) with or without the creditor side, and between −12.4 and −12.5 under every reading tested, including the one where households in the model bear every dollar. Without debt relief at all it is −6.7. The reason: the poorest fifth of adults get $40,900 of debt relief each over the run and bear $580 of the new charges; the richest fifth get $211,300 and bear $102,300.
5. **The programme still lowers the top 1% share once lenders are in the model.** −1.02 points (release) and −1.64 (C2.2) in Reference under the main creditor reading, against −1.14 and −1.75 without a creditor side. The sign holds, with intervals excluding zero, in all five creditor readings in all three environments (the preregistered test). It is weakest when nothing is left outside: −0.67 (−0.86 to −0.49).
6. **So the sign never turned on the lender. It turns on whether the debt relief happens.** The earlier "no debt relief" reading (+1.23) removes the borrower's gain; it does not add a lender's loss. They are different things. Whether fixed-rate debts would really stay fixed in dollars through twenty years of such inflation is a question about loan contracts, and both readings stay beside every wealth result.
7. **On the broad measures the creditor side makes the programme more equalising, not less, and average wealth lower.** In Reference, for the release design, the top 10% share falls by 3.63 points instead of 3.28, the bottom half gains 2.77 instead of 2.61, the wealth Gini falls by 0.046 instead of 0.043. The programme's effect on average real wealth goes from −$57,700 to −$96,000 per adult; on the median from +$36,000 to +$31,500. The median adult still gains in every creditor reading (+$21,200 when nothing is outside).
8. **The assumption that matters most is whether lenders' shareholders are charged.** If they are not (banks' deposits protect their equity, as one strand of evidence says), the new charges are 2 cents on the dollar and every result equals the earlier main reading.

## What was built
Option `cr` of wealth by asset class (`rt`). Off unless a study row asks for it; off, every figure of the engine is unchanged (guard test; engine lineage; the pilot's rows without it reproduce the earlier pilot's 3,186 per-seed series exactly). 7 new unit tests.

**The ledger.** One dollar of household fixed-rate debt (home mortgages less home equity loans; non-revolving consumer credit) is followed to its final owner by the rule of Doepke and Schneider (*Journal of Political Economy*, 2006): funds that issue only their own shares pass to their shareholders; banks and all other businesses are owned through their shares; defined-benefit pension assets belong to the sponsor; the government includes the central bank. Mortgages held by the government-sponsored enterprises pass to whoever holds their securities. Banks' holdings pass to depositors for the deposit-funded part (74%) and stay with the banks for the rest.

| Final holder of one dollar of household fixed-rate debt | End of 2022 (used) | Mid-2026 (check) |
|---|---|---|
| Households, as deposits and money market shares | 23.9 cents | 22.0 |
| Households, as bonds and bond funds | 8.4 | 8.3 |
| Businesses (for their shareholders) | 32.4 | 37.2 |
| Government (Federal Reserve, student loans, state and local) | 25.6 | 21.7 |
| Foreigners | 6.4 | 7.2 |
| Deposits of the government and of foreigners | 3.2 | 3.6 |

U.S. shares are owned 73% by households, 20% by foreigners and 7% by the government and its pension funds.

**Who bears a claim's loss.** Three readings; the main one was fixed before any figure, by a rule (follow the named paper's method with the engine's own constants):
- *Main (`pass`).* A bond loses in full. A deposit is paid 46% of inflation as before; what the depositor does not lose on a deposit-funded loan, the lender's shareholders lose. Businesses' own holdings are their shareholders' loss.
- *Holders of record (`hold`).* Deposits that fund the debt lose in full, like bonds.
- *Shareholders not charged (`hedge`).* Drechsler, Savov and Schnabl (2021) find banks' equity close to insulated from interest-rate changes because deposit rates move so little. Under this reading the shareholders' part is stated and left outside.

**The model's families are not all households.** They have a head aged 25 to 66 with wage income. They hold 79% of all families' fixed-rate debt but only 52% of deposit-like assets, 48% of bond-like assets and 49% of stocks (Survey of Consumer Finances 2022). So the model's savers bear about 0.6 to 0.66 of the household-held loss per dollar of the model's own debt; the rest falls on households outside the model.

**How it is charged.** Each year the claims are spread over everyone who holds that kind of asset, in proportion to holdings: bond-like savings (a share of each wealth group's nominal assets, 38% for the poorest group to 73% near the top, from the survey) and shares. Private-business equity, homes and other real estate are not charged. Debtors keep their relief. Nothing else in the model reads the option.

**Three scope readings.** Main: the government's, foreigners' and outside households' parts are stated and left outside. `pop`: the model's families are treated as the whole household sector. `out`: nothing is outside; every dollar of relief is lost by a household in the model (the upper bound on creditor losses).

## Results

**The ledger under the programme** (Reference, release design; Year-0 dollars per adult over 20 years; tables section 1). Debt inflated away: $102,451 per adult, nearly all the fixed-rate debt the model's adults start with.

| Share of the debt relief | Main | Holders of record | Shareholders not charged | Model = all households | Nothing outside |
|---|---|---|---|---|---|
| Already on the books (savers paid 46% of inflation) | 11.3% | 11.3% | 11.3% | 17.5% | 26.9% |
| New charge on bond-like and deposit savings | 2.4% | 9.6% | 2.4% | 3.9% | 6.0% |
| New charge on shares | 20.5% | 14.8% | 0 | 32.8% | 67.0% |
| Outside: government | 29.7% | 29.7% | 26.5% | 29.7% | 0 |
| Outside: foreigners | 16.1% | 14.2% | 7.2% | 16.1% | 0 |
| Outside: households not in the model | 20.1% | 20.5% | 7.8% | 0 | 0 |
| Outside: lenders' shareholders, not charged | 0 | 0 | 44.9% | 0 | 0 |

The shares are the same in every environment and for both designs (they are set by the coefficients). The ledger balances to rounding in every seed of every row (largest gap 1.2e-14 of the relief). Claims never exceeded holdings except in the nothing-outside reading (0.05% of relief unplaced).

**Who gets the relief and who bears the new charges** (Reference, release; dollars per adult over the run; tables section 2)

| Fifth of starting wealth | Poorest | 2nd | 3rd | 4th | Richest |
|---|---|---|---|---|---|
| Debt relief | 40,908 | 53,539 | 93,565 | 112,761 | 211,260 |
| New charges (main reading) | 578 | 1,135 | 3,149 | 9,657 | 102,280 |

The top 1% of adults by starting wealth bear 26% of the new charges.

**The programme's effect at year 20** (programme minus no programme, same seeds; 95% intervals in tables section 3)

| | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| **Wealth poverty (points)** | | | | | | |
| No creditor side (earlier main reading) | −12.53 | −18.13 | −12.96 | −20.15 | −7.01 | −18.63 |
| Creditor side, main | −12.48 | −18.12 | −12.94 | −20.16 | −6.98 | −18.63 |
| Creditor side, nothing outside | −12.38 | −18.08 | −12.90 | −20.21 | −6.89 | −18.65 |
| No debt relief | −6.65 | −13.33 | −7.78 | −15.59 | −2.77 | −13.26 |
| **Top 1% share of wealth (points)** | | | | | | |
| No creditor side | −1.14 | −1.75 | −1.11 | −1.70 | −0.88 | −1.47 |
| Creditor side, main | −1.02 | −1.64 | −1.00 | −1.61 | −0.77 | −1.37 |
| Creditor side, holders of record | −1.04 | −1.66 | −1.04 | −1.65 | −0.79 | −1.42 |
| Creditor side, shareholders not charged | −1.14 | −1.74 | −1.11 | −1.71 | −0.87 | −1.48 |
| Creditor side, model = all households | −0.93 | −1.57 | −0.92 | −1.55 | −0.70 | −1.30 |
| Creditor side, nothing outside | −0.67 | −1.35 | −0.67 | −1.34 | −0.48 | −1.07 |
| No debt relief | +1.23 | +0.59 | +0.74 | +0.12 | +0.76 | +0.39 |
| **Top 10% share (points)** | | | | | | |
| No creditor side | −3.28 | −4.56 | −3.14 | −4.39 | −2.38 | −3.95 |
| Creditor side, main | −3.63 | −4.96 | −3.40 | −4.71 | −2.58 | −4.25 |
| Creditor side, nothing outside | −4.50 | −5.98 | −4.07 | −5.51 | −3.08 | −5.01 |
| No debt relief | +0.81 | −0.54 | +0.04 | −1.25 | +0.42 | −0.74 |
| **Bottom 50% share (points)** | | | | | | |
| No creditor side | +2.61 | +3.68 | +2.45 | +3.47 | +1.61 | +3.16 |
| Creditor side, main | +2.77 | +3.89 | +2.58 | +3.65 | +1.69 | +3.33 |
| No debt relief | +0.76 | +1.82 | +1.03 | +1.99 | +0.44 | +1.66 |
| **Median real wealth (Year-0 dollars)** | | | | | | |
| No creditor side | +36,000 | +58,600 | +37,000 | +57,400 | +33,400 | +48,100 |
| Creditor side, main | +31,500 | +54,100 | +33,800 | +54,000 | +30,600 | +44,600 |
| Creditor side, nothing outside | +21,200 | +43,800 | +26,300 | +46,300 | +24,000 | +37,100 |
| No debt relief | −46,000 | −25,100 | −19,700 | +500 | −22,100 | −8,500 |
| **Mean real wealth (Year-0 dollars)** | | | | | | |
| No creditor side | −57,700 | −37,800 | −49,300 | −29,900 | −35,900 | −39,300 |
| Creditor side, main | −96,000 | −77,200 | −77,300 | −58,900 | −60,300 | −68,400 |
| Creditor side, nothing outside | −182,600 | −166,600 | −141,400 | −125,300 | −115,600 | −134,900 |
| No debt relief | −156,800 | −139,200 | −118,500 | −101,700 | −98,600 | −110,800 |

Reading it:
- **Wealth poverty.** The creditor side moves the programme's effect by 0.16 points at most (nothing outside, Reference, release), and by 0.05 under the main reading. Adults under the wealth line hold few bonds and shares; the charges pass them by.
- **The top 1%.** Charging lenders' losses to shares and bonds makes the fall in the top 1% share a little smaller (by 0.09 to 0.13 points under the main reading, 0.36 to 0.47 with nothing outside), because the top 1% bear a smaller part of the charges (26%) than their part of wealth (30%): most of their wealth is private business, which is not charged. The adults just below them, who hold more of their wealth in shares, bear more. Hence the top 10% share falls further.
- **Why the top 1% share still falls.** Their nominal assets lose value, and the rest of the distribution gains from debt relief and from saving out of the programme's income. Neither is undone by adding the lender.
- **Average wealth.** The creditor side removes $38,000 of real wealth per adult from the model (main reading): that is the 23 cents on each dollar of relief that the model's savers newly bear. The programme lowers average real wealth in every reading; the median adult gains in every reading with debt relief.

**Does it move anything else?** No. Programme inflation, the cost of living and basket poverty change by 0.06 points or less in every reading (tables section 3, last three blocks). The charges fall on wealth that the model's spending rules barely read.

**Without the tail** (the two rows with no very wealthy households): the creditor side moves the same measures in the same direction by similar amounts (top 1% share −0.86 against −0.98 in Reference, release; wealth poverty −12.43 against −12.50). The tail does not decide these results.

**Weighted or unweighted totals.** With the weighted top tail the option reads adults' weights, through four yearly totals only, so that losses and relief balance in the population the measures describe. With unweighted totals the charges are about a fifth as large (the model economy holds about three times as many very wealthy households as the population, so each claim is charged too little), and every result sits within 0.03 points of the earlier main reading. The weighted version is the main one.

## The preregistered rules
1. **Checks: pass.** Unit tests and guard test pass; the largest ledger gap is 1.2e-14 of the relief (limit one millionth); unplaced claims are at most 0.05% (limit 5%).
2. **Direction of the effect on the top 1% share: established for both designs under the rule as written** (one sign, 95% interval excluding zero, in all five creditor readings and all three environments: the programme lowers it). The rule covers creditor readings only. The no-debt-relief reading still gives the opposite sign, so the plain statement is: the programme lowers the top 1% share if fixed-rate debts keep their dollar value, whoever bears the loss; it raises it if they do not.
3. **Bounds.** The plan expected the earlier two readings (main, and no debt relief) to bound the creditor readings. They do for wealth poverty, the top 0.1% and 1% shares and median wealth (apart from differences of 0.06 points or less, inside the intervals). They do not for the top 10% share, the bottom half's share and the Gini, where the creditor readings lie beyond the earlier main reading (more equalising), nor for average wealth when nothing is outside (below the no-debt-relief reading). The no-debt-relief reading is not "the creditor side at its strongest": it takes the gain from borrowers, where a creditor side takes the loss from savers.
4. **How much of the wealth-poverty reduction rests on debt relief:** about half for the release design, as the earlier report said (−12.5 against −6.7 in Reference). None of it rests on the lender being missing.
5. **Recommended to the design freeze (S63), as fixed before the results:** the creditor side under the main reading as a main-row candidate for every wealth and concentration outcome, with the earlier main reading and the no-debt-relief reading kept beside it, and holders of record, shareholders not charged and model-as-all-households as readings. Added from rule 3: carry the nothing-outside reading too, as the upper bound on creditor losses. S63 chooses.
6. No synergy is claimed: these rows are not a factorial design.

## A correction to the earlier report's wording
The report on the top tail (S59, part 2) said the fall in the top 1% share "comes from fixed-rate mortgages being inflated away with nobody bearing the loss" and that the direction "turns on the missing creditor side". With the creditor side built, the direction is unchanged. What the direction turns on is whether the debt relief happens at all. A dated note is added to that report; no figure in it changes.

## What the sources said, where it differs from the plan
- **The plan named pension claims as a channel.** Under the paper's rule, defined-benefit pension assets belong to the sponsor, so the pension channel is small: defined-contribution funds are looked through to households (part of the 8 cents of bond-like claims).
- **Businesses hold as much as households (32 cents).** This is mostly the part of banks' balance sheets not funded by deposits, deposits held by businesses, and the enterprises' and finance companies' own holdings. It is why the treatment of shareholders is the assumption that matters most.
- **The government is a large creditor of households** (27 cents): the Federal Reserve held $2.3 trillion of agency securities at the end of 2022 and the federal government $1.5 trillion of student loans.
- **The Distributional Financial Accounts** describe all U.S. households in five wealth groups; the engine's wealth groups describe its own families. The split inside the model therefore comes from the survey the accounts are built on, and the accounts are an outside check: applied to all U.S. households, the coefficients put 46-48% of the new charges on the top 1%, 38% on the next 9%, 13-15% on the next 40% and under 1% on the bottom half. The model puts 26% on its top 1% of adults. The gap has two sources that cannot be separated here: the accounts include retired households, who hold much of the country's shares, and the model's link between very high wealth and share holdings is weaker than the survey's. If the model's top 1% bore as much as the accounts suggest, the fall in the top 1% share would be larger, not smaller.

## Limits
1. **One ledger only.** Businesses and the government are borrowers too. In Doepke and Schneider's accounts shareholders gain from inflation on corporate debt (since the 1980s by more than lenders lose), and the government gains on its own debt. Neither is in the model. The main reading therefore charges shareholders a loss without the offsetting gain; the shareholders-not-charged reading and the earlier main reading show the other side.
2. **Lenders do not fail.** A loss of this size on fixed-rate loans is several times banks' equity. The model spreads it over all shareholders and nothing else happens: no bank failures, no rescue paid by taxpayers, no squeeze on new lending.
3. **The outside parts stay outside.** The government's 30 cents are not passed on to taxpayers; retired households are not in the model; foreigners' losses have no effect on the exchange rate or on anything else.
4. **Savers' losses on deposits that fund floating-rate loans** (a gain to banks) remain unattributed, as before.
5. **Claims are spread over holders each year, not tracked.** Fixed-rate debt is never repaid or newly issued in the engine; nearly all of it is inflated away within the run, most of it in the first years.
6. **Coefficients are one year's levels** (end of 2022; mid-2026 moves the businesses' part from 32 to 37 cents and the government's from 27 to 22). Holders of adjustable-rate mortgages and of revolving credit are taken as proportional to all holders; banks keep more adjustable-rate loans than others, so the banks' part of fixed-rate debt is somewhat overstated.
7. **The model's top 1% bear less of the charges than the outside check suggests** (26% against 46-48%).
8. **Year 20 only.** These rows report wealth at year 20; under any price rule other than today's the frozen design must also read yearly averages (the price-rule report explains why).
9. **A weight is read by a rule for the first time** (through four totals). It must be rechecked at 10,000 adults with the rest of the tail.
10. Tested with wealth by asset class only, without ageing, the capacity price rule or adults outside the labour force; those combinations belong to the pairwise tests (S68).
