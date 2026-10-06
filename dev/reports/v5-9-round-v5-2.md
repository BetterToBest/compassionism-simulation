# v5.2: what this round added, what it found, and what it cannot tell you yet (plain words, for Duke)

Written Oct 6, 2026 (session 35). This is Claude's report on the v5.2 round, the nine steps you set out on Oct 3. It needs no code reading. Every figure comes from the one 500-run regeneration made at the end of the round (500 pairs of simulated runs, each with 500 adults, in the Reference, Adverse and Stress Test environments, over 20 and 40 years). "Points" below means percentage points: if the share with too little wealth goes from 52.0% to 35.7%, that is 16.3 points lower.

## In one paragraph

The main result on the page did not change: it is the same cautious reading as v5.1, and every one of its figures is identical except the inequality figures (Ginis), which now carry a small correction for the number of adults (0.2% higher). What this round adds is a set of readings beside the main result, each built from your answers and decisions of Oct 3: more poverty measures and both Ginis against the Hub's own targets, at Year 7 as well as at 20 and 40 years; savings that keep up with prices; adults who age, retire and are replaced; a check of the no-programme run against US data; a middle reading of how much of the Source's payout new output backs, anchored by the Kenya study; idle workers in normal years; landlords raising rents; mistakes in the Collectives' review; other ways to pay; year-by-year charts; and the earlier engine on its own page. **The three findings that matter most:** (1) in the Adverse and Stress environments, savings that lose their value to the programme's price rise remain the main reason more people end up with too little wealth than with no programme; protect savings and those gaps reverse. (2) When adults age and retire over 40 years, the Reference gain in wealth shrinks from 28.9 points to 8.8. (3) Landlords raising rents is the largest of the risks an economist will ask about, and it is the clearest case for community-owned housing (PTH).

## What you need to do

1. Read sections 1 to 5. Say if anything misrepresents your vision. Where your writing is silent I made the most cautious choice and labelled it on the page as "Claude's reading of the design" or "not specified by the Hub"; those places are listed in section 6.
2. Merge pull request 5 (v5.2). Merging is the release; the release workflow tags v5.2. Earlier tags stay where they are.

## 1. The main result (unchanged, now against your targets)

The main result is Compassionism with every mechanism, paid for by the Source, read cautiously: none of what the Source pays out is assumed to be backed by new output, so it raises prices. Against no programme:

| Environment, years | Below the cost of living (share of adult-years) | Too little wealth at the end | Below 30 days of basic living (BLEI) | Price rise a year | Cost per adult a year |
|---|---|---|---|---|---|
| Reference, 20 | 22.0% vs 55.2% | 35.7% vs 52.0% | 18.7% vs 46.7% | 34.9% | $29,618 |
| Adverse, 20 | 42.1% vs 78.2% | 87.1% vs 82.6% | 33.1% vs 60.0% | 45.5% | $27,677 |
| Stress Test, 20 | 65.6% vs 78.2% | 90.6% vs 82.6% | 54.9% vs 60.0% | 23.8% | $10,494 |
| Reference, 40 | 15.3% vs 47.4% | 15.3% vs 44.2% | 14.8% vs 46.6% | 30.4% | $32,274 |
| Adverse, 40 | 62.1% vs 86.7% | 97.9% vs 94.5% | 51.7% vs 75.1% | 65.4% | $27,013 |
| Stress Test, 40 | 79.3% vs 86.7% | 98.8% vs 94.5% | 72.3% vs 75.1% | 36.4% | $10,685 |

**Your Oct 3 answers on reporting, as built.**

- *Several poverty measures beside the Hub's "under 2%".* The new table on the page reads each measure at Year 7 and at the last year. The share below the US official poverty line (the measure behind the Hub's "about 12%" starting point; $16,749 a year for one person in 2025, moved with prices): at Year 7, 2.8% with Compassionism against 3.0% without (Reference), 4.6% against 5.9% (Adverse), 6.3% against 5.9% (Stress Test); at year 20, 0.7% against 1.6%, 24.1% against 48.9%, 40.5% against 48.9%. Only Reference gets under 2% on this measure, and only by year 20. The model starts far below the US's 10.2% because its adults are all working-age earners who live alone; US workers' rate is 4.3%, and the model's first year gives 4.0%.
- *A BLEI figure.* Below 30 days of basic living at Year 7: 21.4% (Reference), 25.8% (Adverse), 46.4% (Stress Test), against about 48% to 54% with no programme. The design-neutral reading sits beside it.
- *An income Gini and a wealth Gini, each against its own Hub number.* Income at Year 7: 0.307, 0.315 and 0.299 (Hub: 0.25 to 0.30, from 0.48; no programme about 0.28, already below the Hub's starting point because the model's wages are narrowly spread). Counting the price cuts as income: 0.256, 0.258 and 0.276, inside the Hub's range. Wealth at Year 7: 0.558, 0.593 and 0.702 (the BLEI paper's 0.25; no programme 0.73 to 0.76). Two readings sit within 0.002 of a target line and are labelled "on the line", because 500 adults cannot place them on either side.
- *The BU indexed every year beside the 5% rule.* In the main result it changes nothing: the programme's own price rise is above 5% every year, so the Hub's rule already indexes the BU every year. It matters at the optimistic end (everything backed, prices steady), where the 5% rule never triggers: in the Adverse Environment the share with too little wealth falls from 52.5% to 31.8%, at a cost of $37,142 instead of $25,607 per adult a year.

## 2. Your four decisions, as built

**A. Retirees keep the BU for life, stop ESP work at 67 and can still convert through creative work.** Built that way, with two other readings beside it (no conversion after 67; retirees leaving the programme). Adults get real ages (Census), can die (the 2022 US life table), retire at 67 on the average Social Security benefit, and new 25-year-olds replace those who die. Results against no programme with the same ageing, share with too little wealth:

| | Reference | Adverse | Stress Test |
|---|---|---|---|
| Main result (no ageing), 40 years | −28.9 points | +3.4 | +4.3 |
| With ageing, your decision A, 40 years | −8.8 | +0.3 | +1.5 |
| With ageing, no conversion after 67 | −2.6 | +0.0 | +1.5 |
| With ageing, retirees leave the programme | +1.2 | +1.1 | +1.6 |

By 40 years 36.5% of adults are retired. Ageing cuts the Reference wealth gain by more than two thirds. It widens the gain in the share below the cost of living (−40.8 points against −32.2), because retirees on Social Security alone fall below the living-wage basket and the BU lifts them. The model does not yet report results by age group, so I cannot yet tell you how much of the wealth difference is retirees; that breakdown is a next step.

**B. A middle backing reading as a labelled band, with the Kenya study named with its limits.** The Kenya study (Egger and others, 2022) gave one-time cash transfers in rural villages; local output rose to meet the new spending and prices barely moved. What carries over is a size: new output can back the Source's payout up to 12% of a year's earned income (the band is 8% to 16%). Share with too little wealth at year 20, against no programme:

| | Reference | Adverse | Stress Test |
|---|---|---|---|
| Main result (nothing backed) | −16.3 points | +4.4 | +7.9 |
| Middle reading (12%; band 8% to 16%) | −22.6 (−20.2 to −25.4) | +0.5 (+1.9 to −1.1) | +2.5 (+4.7 to −0.4) |
| Optimistic end (everything backed) | −36.5 | −30.1 | −10.1 |
| Price rise a year: main / middle | 34.9% / 25.0% | 45.5% / 36.1% | 23.8% / 13.5% |

So the middle band roughly closes the Adverse and Stress wealth gaps, and most of the distance to the optimistic end remains. The page names the study's limits beside the band: the transfers were paid once, not every year; they came from outside the area; and the Source's payout is about two to four times larger relative to income (25% to 58% of earned income a year, against Kenya's 16% in the peak year). The headline stays at the cautious end.

**C. A progressive income tax and a land-value tax, sized to the Source's payout, marked "not specified by the Hub".** Both are built, and where a tax cannot raise enough the Source pays the rest, so no funding gap is hidden. The progressive tax (the shape of today's federal schedule, scaled up) covers only 60% of the cost in Reference and 48% in Adverse, and leaves people worse off than no programme (too little wealth +31.7 and +15.5 points), because to raise that much its rates reach 90% from modest incomes up and people work less. The land tax covers 97% in Reference, with too little wealth 30.6 points lower (better than the main result, because prices barely rise), but only 53% in Adverse. The model has no land, so the land tax falls on savings, and at this size it would take all US land's value within about four years; it shows who would pay, not a tax that could exist.

**D. The earlier engine on its own page.** Done: `earlier-engine.html`, linked from the front door as "Explore the earlier engine", with a link back. The v4.22 tag is untouched.

## 3. The other new readings

- **Savings that keep up with prices** (in both runs; interest equal to the price rise plus 0.97% a year, the long-run real yield on inflation-protected Treasury bonds). Share with too little wealth at year 20 against no programme: Reference −32.3 points (main −16.3), Adverse −40.3 (main +4.4), Stress Test −14.2 (main +7.9). The Adverse and Stress gaps reverse. The catch, stated on the page: the interest is about $46,000 to $48,000 per adult a year in the Reference and Adverse environments (today's dollars), mostly compensation for the programme's own price rise, and the model has no bank to say who would pay it. In this model the price rise is how the Source's new money gets real resources, so fully protecting savings would mean someone else supplies them.
- **Idle workers in normal years.** The spending layer now also reaches workers who are idle outside recessions (the part of US underused labour that comes and goes with demand). It adds $232 to $401 of wages per adult a year and moves results by under 1 point. With all of US underused labour treated as idle: up to 6 points.
- **Landlords raising rents** (from US housing-voucher studies). If landlords take 50 cents of each BU dollar spent on rent, the Reference wealth gain shrinks from 16.3 points to 6.1; if every renter outside PTH pays $1.41 more per BU dollar on rent, to 0.8. In the Adverse Environment the gap widens by 4 to 5 points; in the Stress Test by about 1. PTH members are never marked up, because community-owned housing is the design's answer to this risk.
- **Mistakes and collusion in the Collectives' review.** Your Hub describes graduated scrutiny and auditable scoring but gives no error rate (my note: `dev/reports/v5-9-note-collectives-review.md`). With 20% of high-rate conversions unearned and half caught, the Reference gain shrinks from 16.3 to 14.8 points. Small.
- **The launch gift paid over the run** instead of pay as you go: no difference.

## 4. The no-programme run against US data

The no-programme run is the yardstick for every result, so it was checked against Census poverty and income figures, the Federal Reserve's survey of household wealth and US poverty spells.

- **Where it matches:** below the official poverty line in the first year, 4.0% against 4.3% for US workers.
- **Where it differs, and why:** incomes are more equal than in the US (Gini 0.28 against 0.45), because the model's wages are narrowly spread; median savings are lower ($31,500 against $74,400 for comparable US adults); and far more adults fall into debt (46% at Year 7 against 12.6%). That debt gap is the largest: every adult pays the full living-wage basket, which two in three earn less than, while real people with less income spend less. Poverty is also more short-lived than in the US (62% leave in a spell's first year, against 53%), because the model has no one out of work, disabled or changing household.
- **A reading "closer to US data"** (savings drawn from the survey, automation risk linked to wages, wages spread and centred as in the survey) shrinks the programme's gains. Below the cost of living: Reference −21.0 points instead of −33.2. Too little wealth: Reference −12.6 instead of −16.3. Stress Test +8.2 instead of +7.9.

## 5. What the model cannot tell you yet

- **Children and households.** Every simulated adult lives alone with no children, so the child allowance and household sharing are not modelled. This is the next model step, and comparisons with programmes for families wait for it.
- **The comparison page follows.** Compassionism against current US policy and other designs, on the same simulated people, comes after this release.
- **Real wages fall in the Adverse and Stress environments, with or without the programme.** By year 20 a month of the median wage buys about half of what it did ($1,600 of today's goods with the programme, $1,400 without); by year 40 about a sixth with the programme and a twelfth without. The BU keeps its value because your rule indexes it in years of high inflation. This comes from how those environments are built (automation and recessions), not from a forecast.
- **The backing question is still the decisive unknown.** The middle reading rests on one study of a different situation.
- **Some readings have no source for their size**, and say so: audits catching half of unearned rates, the land tax falling on savings, and who pays the interest on protected savings.
- **No independent economist has reviewed the model yet.**

## 6. Where I made a choice your writing does not make

Each is labelled on the page and recorded in `dev/DECISIONS.md` (Session 35):

- retirees under decision A are always willing to do creative work (they give up no wage to do it);
- audits catch half of unearned rates in the review reading ("not specified by the Hub");
- the middle backing reading's size comes from the Kenya study and US underused labour, not from the Hub;
- the land tax falls on savings because the model has no land;
- none of the new readings joins the main result in this release, because each new mechanism first appears as a reading beside it. Ageing and the "closer to US data" reading are the strongest candidates for the next round.

## How the figures were made

One regeneration, from one clean commit (`42cd8b9`, version 5.2). The commands, the files in `dev/runs/` and the checks are in `CONTRIBUTING.md`, "v5.2 Release Notes". The three checks pass: `validate`, `unit` (171 tests) and `domtest` (113 checks).
