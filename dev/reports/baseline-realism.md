# How close is the "no programme" yardstick to the US today?

Oct 30, 2026 · plan step S34 · Claude · preregistered before any run (research-update `prereg/s34-baseline-realism.md`, with two dated amendments) · engine commit e8f8a77 · 500 paired runs, 20 years · every table in full: `baseline-realism-tables.md`

## Why this matters

Every result of the simulation compares Compassionism with "no programme" on the same simulated people. That no-programme run is the yardstick. If the yardstick's people are poorer, more equal or more in debt than real Americans, every "Compassionism cuts poverty by X points" is measured from the wrong starting line. This step compares the yardstick, as released (v5.6, with today's safety net), with four outside sources for the same ages (adults 25 to 64 and their children):

- **Income and official poverty:** the Census Bureau's Current Population Survey, 2026 Annual Social and Economic Supplement (CPS ASEC, income in 2025), computed from the public microdata.
- **Wealth:** the Federal Reserve's Survey of Consumer Finances 2025 (and 2022, which the model's starting wealth comes from), families with a head aged 25 to 64 who earn wages.
- **Work:** the Bureau of Labor Statistics' 2025 averages (employment, labour force and unemployment at 25 to 54).
- **Today's safety net:** PolicyEngine-US, an independent open-source calculator of US taxes and benefits, for six typical households.

The outside figures were computed by `sources/baseline_realism_us.py`, which reproduces the Census Bureau's own published headline figures exactly (official poverty 10.2% for everyone and 9.2% at ages 18 to 64, the Supplemental Poverty Measure 13.1%, the household income Gini 0.490), so the microdata are read correctly. The model's figures come from `dev/tools/baseline_realism.js`, which reproduces the release's own no-programme figures exactly (49.25% of adult-years below the cost of living and 32.726% of adults with too little wealth at Reference), so it runs the released yardstick.

A **gap** (fixed before the run): a share more than 3 points from the US figure, a dollar amount below 0.80 or above 1.25 times it, a Gini more than 0.03 from it, a benefit more than the larger of $100 a year and 5% from PolicyEngine's.

## The answer in short

1. **Today's safety net is coded correctly.** For all six households, the engine's SNAP, earned income tax credit and refundable Child Tax Credit match PolicyEngine-US to within $10 a year, with one exception of $138 that has a clear cause (section 3). None is a gap.
2. **The yardstick's people earn far less than real Americans, and too evenly.** The median adult in the model earns $39,200 a year; the median American aged 25 to 64 with earnings makes $60,000. The top tenth of the model earns half what the top tenth of Americans earn. The cause is the wage scale: it was set in v4.3 from the median personal income of *everyone* aged 15 and over ($42,220, CPS ASEC 2023), including students, retirees and people with no earnings, but every adult in the model is 25 to 64 and works full time.
3. **This gap drives the headline baseline.** With wages read from the CPS earnings of adults 25 to 64 (an exploratory reading, section 4), the share of adult-years below the cost of living with no programme falls from **49.2% to 27.1%**, and adults with too little wealth from **32.7% to 20.3%**. Every programme effect the simulation reports is measured from the 49% starting line. Nothing released changes now (released figures can change only at the S7 release); the reading is ready, off by default, for the study programme to preregister.
4. **Everyone in the model works.** In the US, 19% of adults aged 25 to 64 had no earnings in 2025; in the model, none. So the model's adult official-poverty rate (5.0%) matches US adults *with earnings* (3.7%), not all US adults (8.5%). This is a limit of scope: the model is of working adults and their families, and the Hub should say so.
5. **Households drift into debt.** At the start 15.5% of the model's families are in debt (the survey: 9.3%); after 20 years, 33.4%, and three in four single parents. The drift is not caused by children never growing up (with ageing on it is 31.9%) and is only partly caused by the low wages (with US wages, 21.4%). It comes from the spending rule: a household whose income is below its living-wage budget still spends more than its income every year, until it reaches the debt floor. This gap is open (section 5).
6. **Work, poverty of children and the safety net's reach** are close or explained: the model's adults are out of work 2.4% of the time (US unemployment 3.6%: not a gap by the rule); children's official poverty 11.3% (US 13.4%: not a gap at Year 0).

## 1. The released yardstick against the US (Reference)

Model figures are means over 500 runs; Year 20 is the last simulated year. Dollars are 2025 dollars (later years in the model's own prices). In the model, "families" are its households. The full tables for the run without today's safety net, the exploratory rows and the Adverse environment are in `baseline-realism-tables.md`.

**Reference, the released no-programme run (with today's safety net)**

| Measure | US | Source | Model, Year 0 | Model, Year 20 | Year 0 | Year 20 |
|---|---|---|---|---|---|---|
| Median earnings, adults with earnings | $60,000 | CPS ASEC 2026, ages 25-64 | $39,200 | $49,300 | gap | - |
| 10th percentile of earnings | $20,000 | CPS ASEC 2026 | $18,800 | $22,300 | - | - |
| 25th percentile | $37,000 | CPS ASEC 2026 | $27,100 | $32,900 | gap | - |
| 75th percentile | $100,000 | CPS ASEC 2026 | $56,000 | $71,100 | gap | gap |
| 90th percentile | $155,000 | CPS ASEC 2026 | $76,300 | $96,000 | gap | gap |
| Gini of earnings, adults with earnings | 0.450 | CPS ASEC 2026 | 0.294 | 0.301 | gap | gap |
| Adults with any earnings in the year | 80.9% | CPS ASEC 2026, ages 25-64 | 100.0% | 99.8% | gap | gap |
| Official poverty, adults | 8.5% | CPS ASEC 2026, ages 25-64 | 5.0% | 3.0% | gap | gap |
| Official poverty, adults (US: adults with earnings) | 3.7% | CPS ASEC 2026, ages 25-64 with earnings | 5.0% | 3.0% | - | - |
| Official poverty, children | 13.4% | CPS ASEC 2026, under 18 | 11.3% | 6.4% | - | gap |
| Official poverty, adults and children | 10.0% | CPS ASEC 2026, ages 25-64 and under 18 | 6.7% | 4.0% | gap | gap |
| Median household money income | $105,000 | CPS ASEC 2026, householder 25-64 | $58,800 | $72,900 | gap | gap |
| Gini of household money income | 0.467 | CPS ASEC 2026, householder 25-64 | 0.316 | 0.326 | gap | gap |
| Median family net worth | $185,600 | SCF 2025, head 25-64 with wages | $156,800 | $202,000 | - | - |
| Families in debt (net worth below zero) | 9.3% | SCF 2025 | 15.5% | 33.4% | gap | gap |
| Families with net worth below $25,000 | 23.5% | SCF 2025 | 27.0% | 35.5% | gap | gap |
| Median net worth, single adults | $62,700 | SCF 2025 | $71,900 | $104,800 | - | gap |
| In debt, single adults | 15.6% | SCF 2025 | 19.6% | 37.6% | gap | gap |
| Median net worth, single parents | $49,000 | SCF 2025 | $32,900 | $-10,100 | gap | gap |
| In debt, single parents | 19.2% | SCF 2025 | 35.5% | 75.8% | gap | gap |
| Median net worth, couples without children | $268,300 | SCF 2025 | $365,000 | $652,100 | gap | gap |
| In debt, couples without children | 5.9% | SCF 2025 | 5.6% | 8.9% | - | - |
| Median net worth, couples with children | $318,500 | SCF 2025 | $268,800 | $209,600 | - | gap |
| In debt, couples with children | 4.1% | SCF 2025 | 11.5% | 37.4% | gap | gap |
| At work (share of working-age adult-years; whole run) | 80.6% | BLS CPS 2025, employment-population ratio 25-54 | 97.6% | (same) | gap | |
| Out of work (share of adult-years; whole run) | 3.6% | BLS CPS 2025, unemployment rate 25-54 | 2.4% | (same) | - | |
| Adults in households receiving SNAP (whole run) | 8.7% | CPS ASEC 2026, ages 25-64 (as reported) | 18.0% | (same) | gap | |
| Adults in households receiving EITC (whole run) | 15.3% | CPS ASEC 2026, ages 25-64 (as reported) | 11.9% | (same) | gap | |
| Adults in households receiving refundable CTC (whole run) | 10.3% | CPS ASEC 2026, ages 25-64 (as reported) | 10.0% | (same) | - | |

Model's own measures (no outside series): adult-years below the cost of living 49.2%, adults with too little wealth at the end 32.7%, people in households below the official line (person-years) 5.0%.

## 2. Each gap, what it means, and what was done

Classes (preregistered): **scope**, a stated limit of the model; **constant**, a constant that differs from a cited source, fixed only behind a switch that is off by default; **open**, not explained or not fixable this session.

| Gap | Class | What it means | Done |
|---|---|---|---|
| Earnings too low (median $39,200 against $60,000) and too even (Gini 0.29 against 0.45; the 75th and 90th percentiles about half the US figures) | constant | The wage scale was set from the median personal income of everyone 15 and over, earners or not ($42,220, CPS ASEC 2023), and a spread of 0.5 in log wages, while every model adult is 25 to 64 and works full time. | New constants from the CPS ASEC 2026 (`CFG.CPS_EARN`): adults 25-64 with earnings (median $60,000, spread 0.737) and full-time, year-round workers ($70,000, 0.626), through the existing wage reading (`lt.s`, `lt.m` = `'all'` or `'ft'`), off by default. Effect: section 4. |
| Household money income too low and too even (median $58,800 against $105,000; Gini 0.32 against 0.47) | constant, then scope | Mostly the earnings gap. With US earnings the median is $93,300 (no gap); the Gini stays low (0.40) because the model's households have no income from property or businesses and no other adults living with them. | Reported. |
| Everyone works (100% have earnings against 80.9%; at work 97.6% of the time against an employment rate of 80.6% at 25 to 54) | scope | The model has no adults outside the labour force: no caregivers at home, no disability, no students. Its official poverty rate for adults therefore matches US adults with earnings (5.0% against 3.7%: no gap), not all adults (8.5%: gap). | Reported. The Hub should describe the simulated people as working adults and their families (a wording correction for S24). |
| Official poverty of adults and children together lower (6.7% against 10.0%) | scope | Follows from the line above: no non-working adults. Children alone are close at Year 0 (11.3% against 13.4%). | Reported. |
| Families in debt: 15.5% at Year 0 against 9.3%, rising to 33.4% at Year 20; single parents 35.5% rising to 75.8% (19.2% in the survey); couples with children 11.5% rising to 37.4% (4.1%) | open | A household whose income falls below its living-wage budget spends less than the full budget (income-graded spending, BLS Consumer Expenditure Survey) but still more than its income, every year, until it reaches the debt floor (−$10,000), and almost nothing brings it back. Not caused by children never growing up (with ageing: 31.9% in debt at Year 20); partly the low wages (with US wages: 21.4%). | Open, for S32 and S47 (section 5). |
| Families below $25,000 of net worth: 27.0% against 23.5% at Year 0, 35.5% at Year 20 | constant, then open | At Year 0 it is the low wages (with US wages 23.0%, no gap); the rise is the debt drift above. | Reported. |
| Median net worth by type at Year 20 (couples without children $652,000 against $268,000; single parents −$10,100 against $49,000) | open (drift) | The model's people do not age (in the released run), so after 20 years every adult has saved, or borrowed, for 20 more years than anyone in today's survey; a cross-section of all ages does not do that. Couples without children pile up savings; single parents sit at the debt floor. | Reported (section 5). |
| SNAP reach: 18.0% of adults live in households receiving it, against 8.7% as reported in the CPS | constant, then explained | The low wages put more households under SNAP's income limit; with US wages it is 9.9% (no gap). The CPS under-reports SNAP, so the true US figure is higher than 8.7%. | Reported. |
| EITC reach: 11.9% against 15.3% (with US wages 6.5%) | scope | The EITC goes mostly to people with low or part-year earnings; the model has no part-time or part-year work beyond spells out of work. | Reported. |
| Gini of earnings with US wages still 0.41 against 0.45 | scope | A lognormal spread fitted to the quartiles cannot reproduce the very top of US earnings. | Reported. |

Close or not gaps: the 10th percentile of earnings ($18,800 against $20,000), time out of work (2.4% against 3.6%), children's official poverty at Year 0, the refundable CTC's reach (10.0% against 10.3%), median family net worth at Year 0 ($156,800 against $185,600; the model's starting wealth comes from the SCF 2022, $208,600 in 2025 dollars), and couples without children in debt (5.6% against 5.9%).

**Today's safety net lowers the official measure's money income.** Without the safety net the model's adults are below the official line 2.7% of the time at Year 0; with it, 5.0%, and the 10th percentile of earnings falls from $20,600 to $18,800. The official measure leaves out SNAP and tax credits, and the model's single work response (guardrail 7) cuts the hours of people facing the benefits' phase-out rates. This is the known behaviour described in `v5-35-safety-net-poverty.md`; studies of the EITC find more people working rather than fewer hours (Eissa and Liebman 1996; Eissa and Hoynes 2006), so the model probably overstates this cut. Reported, not changed.

## 3. Today's safety net: the engine against PolicyEngine-US

Six households in Florida (SNAP's 200% gross income limit, no state income tax), working-age adults, all income from earnings. Rent and childcare are the engine's own lines for the household's type (MIT's rent with utilities; MIT's childcare for children under 13), entered in PolicyEngine as rent and childcare expenses (no separate utility bill, since the engine's rent includes utilities). Tax credits for tax year 2025; SNAP at its fiscal 2026 amounts (January 2026 times 12). Take-up is set to "takes up" on both sides: this checks the rules, not who claims. PolicyEngine-US version 2.80.0.

| Household | Rent | Childcare | Engine: SNAP / EITC / CTC | PolicyEngine | Difference |
|---|---|---|---|---|---|
| Single adult, earning $15,000 | $13,631 | $0 | 3,394 / 314 / 0 | 3,384 / 314 / 0 | 10 / 0 / 0 |
| Single adult, earning $30,000 | $13,631 | $0 | 288 / 0 / 0 | 288 / 0 / 0 | 0 / 0 / 0 |
| Single parent, one child aged 3, earning $22,000 | $18,502 | $12,914 | 6,552 / 4,328 / 1,700 | 6,552 / 4,328 / 1,700 | 0 / 0 / 0 |
| Single parent, children aged 4 and 9, earning $35,000 | $18,502 | $24,551 | 9,420 / 4,699 / 3,262 | 9,420 / 4,699 / 3,400 | 0 / 0 / −138 |
| Couple, children aged 7 and 12, one earner at $40,000 | $18,502 | $24,551 | 11,928 / 5,145 / 3,400 | 11,928 / 5,145 / 3,400 | 0 / 0 / 0 |
| Couple without children, earning $25,000 together | $15,007 | $0 | 3,183 / 93 / 0 | 3,180 / 93 / 0 | 3 / 0 / 0 |

No difference is a gap. The two small SNAP differences are rounding: SNAP rounds net income and the benefit to whole dollars each month, and the engine does not. The $138 is the child and dependent care credit: it is applied before the Child Tax Credit and wipes out this family's $1,138 of income tax, so the whole Child Tax Credit is left to refund (up to $1,700 a child). The engine has no child and dependent care credit, so it uses part of the Child Tax Credit against the tax. This matters only for families paying for childcare who owe a little income tax; it is recorded as a small open item, not changed.

## 4. What the earnings gap does to the yardstick (exploratory)

These rows were added after the first results (prereg amendment) and are labelled exploratory. Each keeps today's safety net and changes only the wage reading. Reference, 500 runs, no programme.

| Measure | Released (model wages) | US earnings, adults with earnings | US earnings, full-time year-round | Earlier SCF reading |
|---|---|---|---|---|
| Median earnings, Year 0 | $39,200 | $59,500 | $69,500 | $54,200 |
| Adult-years below the cost of living | 49.2% | 27.1% | 19.0% | 32.0% |
| Adults with too little wealth (last year) | 32.7% | 20.3% | 14.6% | 23.8% |
| People in households with too little wealth (last year) | 38.2% | 24.2% | 18.5% | 27.6% |
| Poverty severity (FGT2 × 100) | 7.17 | 4.21 | 2.38 | 5.96 |
| Families in debt, Year 20 | 33.4% | 21.4% | 15.6% | 24.9% |

The release's no-programme run puts about half of all adult-years below the cost of living. With the earnings of US adults who work, it is about a quarter. The cost of living itself (MIT's living-wage budget, $49,370 for one adult) is unchanged; only who earns what changes. So the simulation's large programme effects are measured from a starting point about twice as poor as working Americans. Whether the programme's effect is larger or smaller from the US starting point is not known yet: no programme row has been run with the new reading, and none should be until the study programme preregisters it (below).

Recommendation (Claude's, recorded in `dev/DECISIONS.md`, S34): **the study programme (S32) should preregister the "adults with earnings" reading as a row beside the released yardstick, and the S47 design freeze should decide, before any programme result with it is seen, which yardstick the main results use.** I recommend the "adults with earnings" reading over the full-time one: the model gives every adult one pay rate and has no part-time work, and the spread of all earnings is the better stand-in for that. The full-time reading is the upper end.

## 5. The debt drift and Year 20 (exploratory, and open)

With ageing on (children grow up and leave, adults retire and die, new adults arrive), the share of families in debt at Year 20 is 31.9% (released: 33.4%). Single parents improve (58.7% against 75.8%) but the total hardly moves, so never-ending childcare is not the main cause. With US earnings and ageing together it is 20.7%, still more than twice the survey's 9.3%.

The mechanism: when a household's income is below its living-wage budget, the model has it spend `budget × (income / budget)^0.557` (BLS Consumer Expenditure Survey 2024), which is less than the budget but more than the income. So it dissaves every year until it reaches the debt floor, and stays there while its income stays low. Real households below their budget also borrow, receive help from family, and cut further; the model has no such limit. Possible readings for the study programme (none built this session): spending capped at income plus a borrowing limit; or the graded rule applied only to the part of spending above a subsistence floor. Choosing one is a modelling choice for S32 or S47, preregistered before results.

Year 20 against today's survey is partly not like for like: in the released run nobody ages, so after 20 years everyone has saved or borrowed for 20 more years. That is why couples without children reach a median of $652,000. With ageing the figure is $434,000.

**Adverse and Stress Test.** The two no-programme runs are identical (the environments differ only in the programme's settings). At Year 0 they equal Reference. Over 20 years real earnings fall by a quarter (median $29,300 at Year 20), with recessions, the automation wave and 2% outside inflation, and families in debt rise to 44%. The Adverse environment is a stress case, not a forecast; US real median earnings did not fall like this over 2005 to 2025, a period with two recessions. Reported, not classed (the outside data are of one year).

## Limits

- The outside figures are for one recent year (2025 income; the SCF's 2025 wealth). The model's Year 20 is compared with them only to show drift.
- The SCF counts one family per household head; the model's households are its own grouping of adults (CPS ASEC 2023 shares of adults by family type). The shares of each family type are therefore not compared.
- The CPS under-reports SNAP and other benefits; recipiency figures are as reported.
- Survey sampling error is small next to every gap above (the SCF and CPS samples are 12,655 families and 134,729 people).
- The exploratory rows were chosen after the first results; they show what would close a gap, not a tested hypothesis.

## Decisions made (full reasons in `dev/DECISIONS.md`, S34)

- The released yardstick is the run with today's safety net (the release panel's command); both are reported.
- Outside figures computed from microdata for the model's ages, checked against the Census Bureau's published figures.
- The CPS earnings readings, behind the existing wage switch, off by default; the recommendation above for S32 and S47.
- PolicyEngine-US set-up as in section 3.

## Claude's reading of the design (please check)

None of this is a question about Compassionism's design: it is about the people the model simulates. One point touches the Hub's wording: the simulation's people are working adults aged 25 to 64 and their children, with no one outside the labour force. Pages that say "Americans" or "US adults" should say "working adults" (for the corrections package, S24).

## What you need to do

Nothing now. When the study programme is preregistered (S32), the choice of yardstick is set there, before any result.

## Reproduce

All from a clean checkout of commit e8f8a77 (results: BetterToBest/compassionism-sim-results, folder `s34-baseline-realism-e8f8a77`, with run.txt and SHA256SUMS):

- `node dev/tools/baseline_realism.js ENV 500 20` and `node dev/tools/baseline_realism.js ENV 500 20 --explore` for ENV in ref, adv, st (about 2 and 8 minutes each on one core).
- `python3 sources/baseline_realism_us.py DATA_DIR` (CPS ASEC 2026 public-use CSV, SCF 2025 and 2022 summary extracts; FRED series downloaded).
- `node dev/tools/sn_households.js --out=E.json`, then `python dev/tools/pe_households.py E.json P.json` (needs `pip install policyengine-us`).
- `python3 dev/tools/baseline_realism_table.py ENV ROWS` writes the tables.
