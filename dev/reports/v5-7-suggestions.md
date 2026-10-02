# Ways to improve the model, beyond what the ledger already lists

Session 33, Oct 2, 2026. Written by Claude for Duke. Plain words; each item says what is missing, why it matters, and how it could be built. None of this is built yet. The ledger already has: children and households (s52), the disposable-income Gini and poverty spells (s25), today's safety net as a comparison row, more designs, a full sensitivity analysis, and 30- and 40-year horizons (compare study s46-s49). Those are not repeated here.

Ranked by how much each could change what the page says.

## 1. Savings that keep up with prices

**What is missing.** In the model, savings earn no interest. When prices rise 35% a year (Reference) or 46% a year (Adverse), anyone's savings lose most of their value within a few years. This is the main reason the page finds more people with too little wealth in the Adverse and Stress environments.

**Why it matters.** In a real economy with prices rising that fast, banks would pay interest that rises with prices (or people would hold their savings in things that keep their value). The model's result partly reflects a missing bank, not the design.

**How.** A switch that pays interest on savings equal to the year's inflation plus a small real rate (sourced from Treasury inflation-protected bond yields), for everyone and in the no-programme run too. Shown as a reading beside the main one, not replacing it.

## 2. A middle, evidence-based answer to the "decisive unknown"

**What is missing.** The page shows two ends: conversion payments backed by almost no new output (prices rise fast) or fully backed (prices flat). The truth is probably in between, and the page gives no middle figure.

**Why it matters.** It is the single assumption that most changes the results.

**How.** The best real-world evidence is the large Kenya cash-transfer study (Egger, Haushofer, Miguel, Niehaus and Walker, *Econometrica*, 2022): cash given to poor villages raised local spending and output by about 2.5 times the transfer, with almost no price rise (about 0.1%). That is a very different economy from the US, so it cannot set the number directly, but it can anchor a labelled middle reading (for example, half of conversion backed), swept across a range.

## 3. People who age, retire and are replaced

**What is missing.** The adults never age. Over 40 years, a 45-year-old would be 85, still working at the same wage.

**Why it matters.** Now that the page shows 40 years, this is the most visible gap. Retirement, Social Security and new young adults entering would change wealth, work and who takes part.

**How.** Give each adult an age from Census age data; retire them at 67 with a Social Security benefit (the model already has the SSA figures as reference points); apply SSA life tables for deaths; bring in new 25-year-olds each year. Behind a switch, so the current results stay reproducible.

## 4. Sellers capturing part of the allowance

**What is missing.** When people receive money that can only be spent on essentials, some sellers may raise prices, especially landlords. The model's essentials prices respond to demand only through a general rule.

**Why it matters.** Studies of US housing vouchers found rents rose for other low-income renters (Susin, *Journal of Urban Economics*, 2002, found about 16% in metro areas with many vouchers). If part of the BU ends up as higher rents, the gains shrink. Community-owned housing (PTH) and businesses (PTF) are the design's answer to this, so showing it would also show why they matter.

**How.** A housing-specific capture share, sourced from the voucher studies, applied where PTH does not cover demand.

## 5. Mistakes and gaming in setting conversion rates

**What is missing.** In the model, the Creative Collectives' review of work is perfect: a rate above 1x is earned only by work actually delivered.

**Why it matters.** Any review system makes mistakes, and some people will try to game it (friends rating each other highly). Economists will ask about this first.

**How.** A review that sometimes rates too high or too low, and a share of colluding groups, with the Collectives' audits catching some of it. Show how much the results change when 5%, 10% or 20% of high rates are unearned.

## 6. Idle workers outside recessions

**What is missing.** The model says spending only creates jobs in recessions, because outside them everyone who wants work has it.

**Why it matters.** In reality there are always some people out of work or wanting more hours (about 7 to 8% of the US workforce on the broad BLS measure, U-6, in recent years). Some of the programme's spending could put them to work even in good years, which would mean more output and less inflation.

**How.** Add a sourced level of slack (BLS U-6) and let the spending layer fill part of it in normal years too, with the published normal-times multiplier.

## 7. Checking the no-programme run against real US data

**What is missing.** The no-programme run is the yardstick for every result, but it has not been checked against how poverty actually moves in the US.

**Why it matters.** If the yardstick is off, every comparison is off. It is also the first thing an outside expert will check.

**How.** Compare the no-programme run with published facts: how long poverty spells last (Panel Study of Income Dynamics), how wealth is spread (Federal Reserve Survey of Consumer Finances), and the Census Supplemental Poverty Measure. Report the match and the gaps on the replication page.

## 8. Show the path, not only the end point

**What is missing.** The page gives figures for the whole run and for the last year, in sentences. It does not show how things change year by year.

**Why it matters.** "Prices are 297 times today's by year 20" is hard to picture and can alarm. A simple chart of poverty, savings and real purchasing power (what a month's income buys) over the 20 or 40 years would show whether things settle, keep improving, or keep getting worse.

**How.** The engine already records each year; the page needs one small chart per measure, with no programme beside Compassionism.

## 9. Other ways the Source could be paid for

**What is missing.** The Hub does not say what pays the Source, so the model treats its payments as new money (the cautious reading), and shows one alternative: a flat contribution on wages.

**Why it matters.** Readers will ask what happens if the Source is paid for in other ways that do not discourage work as much.

**How.** Two more labelled readings, each clearly marked "not specified by the Hub": a progressive income tax and a land-value tax, each sized to cover the Source's net payout. These are modelling alternatives, not claims about the design.

## For the page itself

- **Move the earlier engine (v4.22) to its own page.** It takes up most of the page below the results, uses different words (for example, "CCO only"), and its glossary describes the old engine. A newcomer can easily confuse its figures with the release results. A link "Explore the earlier engine" would keep it available.
- **Show prices next to purchasing power.** Wherever the page says how much prices rise, say beside it what a month of the allowance and a month of wages still buy.
