# Part-time work and the child and dependent care credit in the "no programme" yardstick: Claude's reading

Nov 21, 2026 · Claude · written before the preregistered run (research-update `prereg/2026-11-s100-part-time-dcc.md`) · sources: `sources/s100_earnings_by_household.py` and its output `sources/s100_earnings_by_household.json`

## The question

The baseline-realism check (`baseline-realism.md`) found that 11.9% of the model's adults live in households receiving the earned income tax credit (EITC), against 15.3% in the Census Bureau's survey, and put it down to the model having no part-time work. The engine also had no child and dependent care credit. Both change how poor the "no programme" people are, so both change the size of every programme effect measured against them.

This note is about the yardstick, which is today's United States. It is not about the Compassionism design, so it is settled by US data and US tax law, not by a reading of the framework's papers. Where the data leave a choice, the note takes the reading that does not flatter the programme and says so.

## 1. The gap was mostly in how it was measured

Both sides were checked again on today's candidate main row, which already reads US earnings and adults outside the labour force.

- **The US figure counts more than the model's household.** The 15.3% is the share of adults aged 25 to 64 whose Supplemental Poverty Measure unit receives the credit. That unit can hold several tax units: a cohabiting partner who files apart, a grown child, a relative. A model household is one tax unit (couples file jointly). Counting only the adult's own tax unit, the US figure is **11.8%**. The other 3.5 points come from someone else's tax return.
- **The survey's credit assumes everyone eligible claims it.** The survey's tax credits come from the Census Bureau's tax model, which gives the credit to every eligible tax unit. The engine applies the measured take-up (80.8%). At full take-up, the model's figure is **10.9%**.

Like for like, the model is 10.9% against 11.8%: under one point apart, which is not a gap by the rule the check set (three points). Today's main row with take-up, as it reports it, is 8.8%.

## 2. What the single figure hid: where low pay falls

By household type, the model and the survey differed more than the total shows (own tax unit, full take-up, no-programme run, 100 runs):

| Household | Share of adults (model / US) | Model | US |
|---|---|---|---|
| Single adults | 30.6% / 29.9% | 6.1% | 8.6% |
| Single parents | 5.0% / 5.1% | 37.1% | 49.8% |
| Couples without children | 32.8% / 34.2% | 2.8% | 4.5% |
| Couples with children | 31.6% / 30.8% | 19.7% | 16.5% |

The household shares match; the credit's reach does not. The cause is the wage draw: every adult's yearly pay comes from one distribution, the earnings of all US earners aged 25 to 64 (median $60,000), whatever the household. In the survey, earners' pay differs by household type:

| Earners aged 25-64 | Median | Spread of log pay | Part time | Full time, part of the year |
|---|---|---|---|---|
| All | $60,000 | 0.737 | 12.2% | 9.3% |
| Single adults | $50,000 | 0.727 | 12.8% | 10.7% |
| Single parents | $45,000 | 0.679 | 16.7% | 10.3% |
| Couples without children | $65,000 | 0.679 | 11.4% | 8.7% |
| Couples with children | $70,000 | 0.766 | 11.7% | 8.6% |

(Part time: usually under 35 hours a week; part of the year: under 50 weeks; spread from the quartiles, as the release's wage reading.)

## 3. What part-time work is in the model

The model has no separate hours: an adult's pay is a yearly amount, cut by spells out of work and moved by the labour response. Part-time and part-year work are already inside the earnings distribution the main row reads, because that distribution is the yearly pay of everyone with earnings, part-timers included. They sit at the bottom of it: 43% of the bottom fifth of earners work part time and 18% full time for part of the year, against 3% and 5% in the top fifth. Adding hours on top of this distribution would count part-time work twice.

So Claude's reading is that part-time work enters the model through **who** has low yearly pay, not through a separate hours variable. The new reading (row option `eh`, off by default) gives each adult the earnings distribution of its household type. Each adult keeps its own place in the distribution (no new random draw), so the run's people, households and spells out of work are the same; only the scale of each adult's pay moves. Partners' pay is correlated as in the survey (0.22 on the normal-score scale; 0 is today's independent draw).

Where hours would still matter, and the model does not have them:

- **SNAP's work rule** asks for 20 hours a week. The model counts any week at work as meeting it. In the survey, 3.1% of earners aged 25 to 64 usually work under 20 hours a week, and the rule applies only to adults without a child under 14, so the error is small. It is a stated limit.
- **The labour response** acts on yearly pay, which carries hours and effort together. That is the form of the elasticities it uses (Chetty 2012), so no separate hours margin is added.

## 4. The child and dependent care credit

The rules are those of tax year 2025, the year of the engine's other credits (26 U.S.C. 21; IRS Publication 503 for 2025, opened Nov 21, 2026):

- the credit is a percentage of work-related care expenses for children under 13, counting at most $3,000 of expenses for one child and $6,000 for two or more, and at most the pay of the lower-earning spouse (a spouse who is a full-time student or unable to care for themselves is treated as earning $250 a month, or $500 with two or more children; in the model, adults outside the labour force for disability or school);
- the percentage is 35% up to $15,000 of adjusted gross income, one point less for each $2,000 or part of it above, and 20% above $43,000;
- it is not refundable: it is at most the income tax before credits, and it is claimed before the Child Tax Credit, so it can turn part of a family's Child Tax Credit into the refundable part.

**Who pays for care.** The model's budget charges every family with a child under 13 the Massachusetts Institute of Technology's childcare price for each such child. Many US families pay nothing: in the survey, among families with a child under 13 in which every adult works, 25.5% of single parents and 32.0% of couples report paying for childcare. If the credit read the budget line for every family, 60% of such households would receive it, against about 21% of US families in the tax data (Internal Revenue Service, Statistics of Income, tax year 2023: 5.72 million returns, $3.47 billion; families with a child under 13 in the survey: 26.8 million). So with the credit on (`sn.cdc` true), it reads the budget line only for a share of households equal to the survey's share who pay, chosen by a fixed hash of the household, as take-up is (no random stream). Reading the budget line for every family (`sn.cdc` `'all'`) is kept as the upper bound.

**The credit with the programme.** In the programme run, the Basic Unit can buy childcare. Expenses paid by a public scheme are not the family's own expenses under the credit. The model does not track which childcare dollars were paid in Basic Units, so the main reading pays the credit in both runs on the same base, and the study also reports the bound that favours the programme least: the credit paid in the no-programme run only.

**What is not changed.** The model's childcare spending itself (every family with a young child pays the full price in its budget) and SNAP's deduction for it stay as they are. They are a separate question, recorded as a limit.

## 5. What the readings do, in short (no-programme run, 50 runs, Reference)

| Reading | Basket poverty, adult-years | EITC reach (take-up as measured) | Care credit: share of households with a child under 13 / mean per receiving household |
|---|---|---|---|
| Today's main row | 36.1% | 8.8% | none |
| Earnings by household type | 36.4% | 9.0% (full take-up 11.2%) | none |
| Both, with the credit | 36.5% | 9.0% | 17.8% / $842 |

With pay by household type, the credit's reach by household matches the survey closely (single parents 48.7% against 49.8%, couples with children 16.5% against 16.5%, single adults 9.5% against 8.6%), except couples without children (2.0% against 4.5%). The refundable Child Tax Credit's reach by household moves the same way (single parents 46.9% against 45.3%). The care credit's mean is higher than the tax data's ($842 against $606 per return): the model's families all pay the full care price, so more of them reach the $3,000 or $6,000 limit than US families do. That is a gap by the check's rule (a dollar figure more than 1.25 times the US one), and it is reported, not tuned.

These are pilot figures, read to build the readings. The preregistered run decides what they do to the programme's effects.
