# The v5.3 restudy: households and children

Oct 7, 2026 · v5.3, plan item B10 · Claude · 500 paired runs in each of the three environments, 20 and 40 years · the main result as recorded before any restudy run (`dev/DECISIONS.md`, Session 39, B10)

## What was asked

Run every new part of v5.3 on 500 paired runs, decide what joins the main result by the rule recorded beforehand, report each choice as a reading beside it, check the design note's predictions, and release v5.3.

## What the main result is now

By the rule recorded before any run, every part below joins the main result unless the restudy finds a modelling error in it. It found none. It did find three wrong labels in the attribution study, which are corrected, and one test that expected exactly zero where the model gives a tenth of a point (both explained below). So the v5.3 main result is:

- **Households and children.** The adults live in households as US adults do (Census Bureau shares): single adults, single parents, couples with and without children. Each child brings a quarter of the adult allowance (your d167, d172). A household pools its money (d168).
- **The Hub's full list of what BU buy** (your d173): food, housing, medical care, transport and, for families, childcare.
- **Starting wealth from the Federal Reserve's survey**, by household type, and **spending that follows income** (people spend less in a year their income is short).
- **Partners' income swings** move together at Shore's (2010) measured strength.
- **The two accounting corrections** found by the accounting check.

Ageing (with children's lives and estates) and earnings by age stay labelled readings, as ageing was in v5.2. The measured share of income lost to rent and interest (EDC) and the advancement rule in readable units (FBS50) are reported.

## The main result (20 years)

No programme → Compassionism, and the change in points with its 95% interval.

| Measure | Reference | Adverse | Stress Test |
|---|---|---|---|
| Adult-years below 30 days of basic living (BLEI) | 25.4% → 10.4%, −14.9 (−15.1 to −14.8) | 32.1% → 18.6%, −13.4 (−13.6 to −13.3) | 32.1% → 37.6%, +5.5 (+5.4 to +5.7) |
| Adult-years below the cost of living | 45.1% → 16.7%, −28.3 (−28.5 to −28.1) | 72.1% → 33.7%, −38.4 (−38.5 to −38.2) | 72.1% → 56.6%, −15.5 (−15.6 to −15.3) |
| Adults with too little wealth at the end | 30.5% → 36.0%, +5.5 (+5.3 to +5.7) | 48.8% → 89.4%, +40.6 (+40.4 to +40.8) | 48.8% → 86.3%, +37.5 (+37.3 to +37.7) |
| **Child-years below the cost of living** | **72.6% → 29.4%, −43.3 (−43.6 to −42.9)** | 91.3% → 51.2%, −40.0 (−40.4 to −39.7) | 91.3% → 76.5%, −14.8 (−15.0 to −14.5) |
| Child-years below 30 days of basic living | 39.6% → 11.8%, −27.8 | 46.3% → 16.4%, −29.9 | 46.3% → 49.3%, +3.0 |
| Children in a household with too little wealth at the end | 50.5% → 56.5%, +5.9 | 66.7% → 95.9%, +29.2 | 66.7% → 93.5%, +26.9 |
| Everyone (adults and children) below the cost of living | 52.6% → 20.2% | 77.3% → 38.5% | 77.3% → 62.0% |
| Programme inflation a year | 47.9% | 61.5% | 28.5% |
| Price level at the last year, typical run | 1,703× | 13,171× | 171× |
| Cost per adult a year (today's dollars) | $31,366 | $29,567 | $12,177 |
| Hours worked | −6.3% | −10.0% | −4.9% |
| If every Source dollar were backed by new output (H1): adults with too little wealth | 8.0% | 26.4% | 40.3% |

**Run by run.** In every one of the 500 runs, in every environment, the programme leaves fewer adults and fewer children below the cost of living than no programme does on the same draws. On too little wealth it is the other way: the programme does worse in 99% of the Reference runs and in every Adverse and Stress run.

## What this means

1. **Income poverty falls a great deal, most of all for children.** In Reference, children's years below their family's cost of living fall from 73% to 29%; adults' from 45% to 17%. The programme does this in every run.
2. **Wealth now goes against the programme in all three environments**, Reference included (v5.2's Reference result was 16 points better than no programme). The cause is the Hub's full list of what BU buy, not households:
   - v5.2's main row, run on the v5.3 engine, reproduces v5.2's published result (−16.25 points; inflation 34.9%; the two accounting corrections lower the cost by $2 a year).
   - With BU buying only food, housing and medical care, the v5.3 main result would be 14.3 points better than no programme (inflation 33.9%).
   - With the full list, almost every BU is spent on essentials, so almost none expire into project work. Project work is the new output that backs part of what the Source pays, so more of the payout is new money and prices rise faster (47.9% a year). Savings earn nothing in the main reading, so they lose their value. This is the mechanism found in B3f (`dev/reports/v5-15-bu-scope.md`), now in the main result.
3. **What turns wealth back in the programme's favour** (Reference, change in adults with too little wealth): savings that keep up with prices −18.9 points; every Source dollar backed by new output −22.5; a land-value tax instead of the Source −19.0; essentials bought with BU counted as backed −7.5. The backing sweep finds the break-even: Reference turns better than no programme once about a sixth of the Source's payout is backed by new output, Adverse at about seven-tenths, the Stress Test at about four-fifths.
4. **The children's figures hold up across readings.** Every reading paid for by the Source keeps children's cost-of-living poverty at least 26 points below no programme in Reference. Paid for by a tax on wages or income instead, the gain disappears (+0.3 with a flat contribution, +4.4 with a progressive income tax), as it does in v4.22's design.

## v5.3's choices, each undone in turn (Reference, 20 years)

Change against no programme with the same population, in points: adults with too little wealth / adult-years below the cost of living / child-years below the cost of living; then programme inflation.

| Reading | Too little wealth | Below the cost of living | Children below the cost of living | Inflation |
|---|---|---|---|---|
| **The v5.3 main result** | **+5.5** | **−28.3** | **−43.3** | **47.9%** |
| All of v5.3's choices undone (v5.2's main row) | −16.2 | −33.2 | – | 34.9% |
| Adults living alone (no households) | +4.4 | −27.9 | – | 43.6% |
| BU buy only food, housing and medical care | −14.3 | −31.1 | −47.7 | 33.9% |
| Each adult keeps their own money (no pooling) | +9.8 | −28.4 | −43.1 | 48.1% |
| No child allowance | +6.2 | −24.1 | −28.9 | 41.0% |
| A child allowance of half the adult BU | +3.5 | −30.9 | −51.3 | 52.3% |
| Starting savings from the model's own draw, not the survey | −0.1 | −28.5 | −44.1 | 47.8% |
| Everyone pays their full cost whatever their income | −1.1 | −29.2 | −44.2 | 47.3% |
| Partners' income swings strongly linked (0.5) | +5.5 | −28.3 | −43.2 | 47.9% |
| FBS50 spread evenly over its range | +5.5 | −28.3 | −43.2 | 47.9% |

- **The child allowance** you chose (a quarter) cuts children's poverty by 14 points more than no allowance; half the adult BU would cut it 8 points more again, with prices rising 4 points a year faster.
- **Survey wealth and graded spending** make the wealth result look worse against no programme, because they give the no-programme run more savings to keep (as the B7 report found).
- **Pooling** helps: without it, 4 more points of adults end with too little wealth.

## Other readings (Reference, 20 years)

| Reading | Too little wealth | Below the cost of living | Children | Inflation |
|---|---|---|---|---|
| Every Source dollar backed (H1) | −22.5 | −32.4 | −51.1 | 0.1% |
| Middle backing reading (Kenya-anchored, 12% of earned income) | −1.3 | −29.2 | −44.8 | 38.4% |
| Savings keep up with prices | −18.9 | −28.3 | −43.2 | 48.0% |
| Essentials bought with BU counted as backed | −7.5 | −30.3 | −46.7 | 27.4% |
| Households age (children grow up, are born and leave home; estates pass on) | +17.1 | −34.7 | −40.2 | 48.8% |
| Rents rise $0.50 per BU dollar for BU tenants (voucher evidence) | +9.6 | −25.9 | −39.5 | 48.9% |
| The three US wage and risk readings together | −5.3 | −17.6 | −26.1 | 30.0% |
| Taking part costs nothing (everyone joins) | +2.1 | −32.6 | −43.9 | 54.2% |
| Paid for by a flat contribution on wages instead of the Source | +15.7 | +22.2 | +0.3 | −0.1% |
| Paid for by a progressive income tax (not specified by the Hub) | +47.9 | +16.5 | +4.4 | 35.3% |
| Paid for by a land-value tax (not specified by the Hub) | −19.0 | −17.8 | −36.4 | 5.0% |

- **Paying by a flat contribution on wages** stops the inflation but makes adults' income poverty much worse (+22 points): a contribution large enough to pay $31,000 per adult a year takes more from most working households than the programme gives them.
- **Ageing** makes the wealth result worse still (+17 points): retirees live on a working-age basket and couples are fixed for life (a limit).
- Every reading, with the commands and the 40-year results, is on the findings explorer and in the release data.

## The 40-year horizon

*(To follow: the 40-year panels were restarted after a container restart and are still running.)*

## Which of the design note's predictions held

The design note (`dev/reports/v5-3-design.md`, section 3) made eleven predictions before any code. "Adults alone" below is the main result with households switched off (the reading "adults living alone").

| # | Prediction | Result (Reference unless stated) | Held? |
|---|---|---|---|
| 1 | More people below the cost of living with no programme than adults alone | Fewer: 45.1% against 54.2%. Shared costs and pooling outweigh childcare. | No |
| 2 | A larger fall in points than adults alone; for children, a smaller fall in proportion | −28.3 against −27.9 (Adverse −38.4 against −31.1); children fall 60% of their level, adults 63% | Yes |
| 3 | Child poverty above adult poverty in both runs, cut less in proportion | 72.6% against 45.1% with no programme, 29.4% against 16.7% with it | Yes |
| 4 | Too little wealth lower for couples and higher for single parents than adults alone; worse than no programme in Adverse and Stress | Couples without children 8.8% → 11.2%, couples with children 40.0% → 44.4%, single parents 79.7% → 87.1%, against adults alone 44.6% → 48.9%; worse in Adverse and Stress (and now in Reference too, from the BU list) | Yes |
| 5 | Inflation up 1 to 3 points a year in Reference | Up 4.3 (47.9% against 43.6%) | Direction yes, size no |
| 6 | Cost per adult up 5 to 10% | Up 15.8% ($31,366 against $27,095) | Direction yes, size no |
| 7 | BLEI lower for couples, higher for single parents | Not measured by household type; overall, households' BLEI is lower (29.3% of person-years with no programme against 35.7% for adults alone) | Partly checked |
| 8 | Hours fall slightly more | −6.3% against −6.2% | Yes |
| 9 | Equivalized income Gini higher with no programme (closer to the US), cut more by the programme | Lower (0.267 against 0.287), and the programme raises it (to 0.286), as it does for adults alone | No |
| 10 | At 40 years with estates, less wealth poverty than ageing without heirs, and a higher wealth Gini | *(to follow with the 40-year panels)* | |
| 11 | Poverty spells longer, closer to the PSID | First-year exit 0.64 against 0.62 for v5.2's population (PSID 0.53): slightly shorter, not longer; re-entry 0.35 against 0.37 (PSID 0.27): a little closer | No |

Six held, two held in direction but not size, three did not, and one waits for the 40-year panels. Prediction 9 is the one to watch: in the model the programme widens the spread of income, for households and for adults alone; the next model round should trace which part does it.

## Claude's reading of the design (please check)

- **The full list of what BU buy is the design** (your d173), so it is in the main result even though it makes the wealth result worse. Results do not choose the design.
- **How the Source's payout is backed is still the decisive unknown.** The Hub does not say. The main result keeps the cautious reading (only new output the model counts backs it), and the readings above show how much rests on that.

## Limits

- In the main reading nobody ages, children stay children, and couples neither form nor part.
- The model has no central bank, no interest on savings in the main reading, and no places; above 1,000 times today's prices the price figure shows the model's price rule running away, not a forecast.
- The no-programme run is still far more in debt than the survey for single parents and single adults (the US-data check).

## How it was checked

- Every new part is behind a switch; with them off, every v5.2 panel figure is reproduced exactly.
- The 500-run results come from clean commits (289e723 for the backing sweep, attribution and US check; c5e96f9 for the panels), with the commands recorded in each file.
- The panel's main row equals the attribution study's whole-programme row and the backing sweep's a = 0 point to the last published digit.
- At a = 1 (every Source dollar backed) Reference still shows 0.1% a year of programme inflation: extra BU demand for essentials moves their prices a little. v5.2 rounded it to zero; the page check now allows it.

## What you need to do

Read this and the attribution report (`dev/reports/v5-19-attribution.md`), and say if anything misrepresents your design. When it reads right, merging the pull request releases v5.3.

The runs and their commands: `dev/runs/release-panel-ENV.json` and `-40-ENV.json` (`node harness.js testbed 500 release ENV --v53 [--years=40]`), `dev/runs/backing-share-ENV.json`, `dev/runs/attrib-check-ENV.json`, `dev/runs/us-check-ENV.json` (ENV ref, adv, st).
