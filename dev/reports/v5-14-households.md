# Households: who lives with whom, what a family needs, and what changes

Oct 7, 2026 · v5.3, plan item B3 · Claude · 500 paired runs in each of the three environments · a labelled reading being built; nothing on the live page changes until the v5.3 release

## What was asked

Until now every simulated adult lived alone. That left out children, the child allowance you chose (a quarter of the adult BU per child), childcare, shared costs, and anything about families. This step groups the adults into households. You chose two things on the dashboard: people in a household pool their money, with each adult keeping their own as the comparison; and households first appear as a labelled reading beside the adult-only main result.

## What the model now does (when households are switched on)

**Who lives with whom.** At the start of each run, the 500 adults are grouped by the Census Bureau's 2023 figures for adults aged 25 to 64:
- 32% in a couple with children under 18;
- 33% in a couple without children;
- 5% single parents;
- 30% living alone or with other adults, treated as single budgets.

Families have one to four children, with ages spread as in the Census figures. In a typical run that makes about 80 couples with children, 80 without, 25 single parents and 150 single adults, and 170 children. Partners are paired at random. In real life people tend to pair with people who earn similar amounts; the Census tables do not give that figure, so the model leaves it out and says so. Every adult keeps everything that made them who they were in the adult-only model, so the two readings stay comparable.

**What a family needs.** The cost of living comes from the same source as before, the MIT Living Wage Calculator, now for each family type (one or two working adults; up to three children). Childcare is its own item, at MIT's prices: $12,914 a year for the first child under 13, $11,638 for the second, $7,824 for each one after (at the model's price level). A single adult's needs are exactly the same as before. Two examples: a single parent of a four-year-old needs $87,603 a year before tax; a working couple with children aged two and seven needs $121,891.

**The child allowance.** Each child brings a quarter of the adult BU ($300 a month at the reference). The household's allowance is shared equally between its adults.

**Pooling.** In the main household reading, a couple's money is pooled:
- their surplus is pooled before the spending rule takes its share;
- what they own is shared equally;
- the debt floor applies to the household;
- whether they are poor is decided for the household as a whole.

In the comparison reading, each adult pays an equal share of the household's costs from their own income and keeps their own savings.

**Decisions are the household's.** A couple takes part in the programme, joins a community business and lives in community housing together.

**Basic living (BLEI).** Your BLEI paper defines the daily cost of basic living as rent, food, utilities and transport. A household's daily cost uses those same items for its family type.

**What is not in yet.** Children do not grow up, are not born and do not leave home in this step; each household keeps its children as drawn. That arrives next (plan item B4: births by the mother's age, leaving home, children replacing the unrelated new adults), together with what happens when someone dies (B5). Households and ageing cannot be combined until then.

## How it was checked

- **Off means off.** With households switched off, every published figure is reproduced exactly (the release panels keep their fingerprints in all three environments, at 20 and 40 years).
- **Households of one.** If every household is a single adult, every result equals the adult-only model to the last digit.
- **No borrowed luck.** Grouping people uses its own random numbers; no adult's yearly draws change.
- **The books balance.** The accounting checks from the last step all pass with households: about 21 million checks per reading. A new check confirms that what one partner gains from pooling, the other gives.

## What the 500 runs show

These are early results for this step alone. Children are frozen at their ages, and the calibration steps still to come (household wealth, how spending rises with income, earnings by age) will move the numbers. The figures below are shares, with Compassionism against no programme in the same households, paired run by run (the 95% intervals are narrow: within ±0.8 point for every figure below).

**Reference environment**

| Measure | Adult-only model | Households |
|---|---|---|
| Adult-years below the cost of living | 55.2% → 22.0% | 46.0% → 13.3% |
| Adults with too little wealth at the end | 52.0% → 35.7% | 42.6% → 20.0% |
| People below the cost of living (children counted) | — | 53.8% → 16.3% |
| Children below the cost of living | — | 74.4% → 24.0% |
| Children below 30 days of basic living | — | 65.1% → 12.5% |
| Children in households with too little wealth | — | 71.8% → 37.2% |
| Cost per adult a year | $29,616 | $36,114 |
| Price rise a year | 34.9% | 32.5% |

**By family type** (Reference, people below the cost of living): single adults 55.2% → 18.4%; single parents 92.6% → 57.6%; couples without children 14.6% → 3.9%; couples with children 65.8% → 12.9%.

**Adverse and Stress Test environments**

| Measure | Adverse: adult-only | Adverse: households | Stress Test: adult-only | Stress Test: households |
|---|---|---|---|---|
| Below the cost of living (adult-years) | 78.2% → 42.1% | 72.0% → 26.9% | 78.2% → 65.6% | 72.0% → 55.4% |
| Too little wealth at the end | 82.6% → 87.1% (worse) | 76.5% → 73.8% (better) | 82.6% → 90.6% (worse) | 76.5% → 89.1% (worse) |
| Children below the cost of living | — | 91.3% → 43.4% | — | 91.3% → 75.4% |

**What stands out**

1. **Children are much poorer than adults, and the programme helps them most in points.** In Reference, three children in four live below their family's cost of living without the programme, against about half of all people. Childcare is the main reason: MIT's family budgets are far above two typical wages in the model. With Compassionism, child poverty on this measure falls by 50 points to 24%.
2. **Families with children gain the most; single parents stay the hardest case.** Couples with children go from 66% below the cost of living to 13%; single parents from 93% to 58%.
3. **The child allowance matters a great deal.** Children below the cost of living with Compassionism, in Reference: 37.5% with no child allowance, 24.0% at a quarter, 18.9% at a half. The cost per adult rises from $30,423 to $36,114 to $41,263.
4. **In the Adverse environment, the sign on wealth changes.** Adult-only, more adults end with too little wealth under Compassionism than without it. With households, slightly fewer do (−2.7 points). Without the child allowance it goes back to worse (+4.1). In the Stress Test, wealth is still worse with the programme (+12.5 points).
5. **Pooling matters for wealth, less for income.** When each adult keeps their own money, more adults end with too little wealth: 47.3% against 42.6% with no programme in Reference, and 24.4% against 20.0% with Compassionism. A lower-earning partner no longer shares the other's savings. The programme's effect on the cost of living is about the same either way.
6. **Prices rise a little more slowly with households, and the reason is about what BU can buy.** A family's BU budget, with its children's allowances, is often larger than what BU can buy today: food, housing and medical care only, not childcare. So most of the extra BU expire unspent. Expired BU fund project work. The model counts that work as new output, which backs part of the Source's payout, so less of it is new money. In Reference, project payouts double (about $6,700 to $13,800 per adult a year, measured on 20 runs), the output backing doubles, and prices rise 2.4 points a year less (500 runs). You confirmed on the dashboard that BU can buy the full list in your glossary (transport and education too, with childcare at community providers), added first as a labelled reading. This result shows why it matters for families. I am building that reading next, beside this one.
7. **The official poverty line hardly registers.** Adults in the model all earn wages, and couples have two, so very few households fall below the official line: about 2% of people in Reference with no programme, against the national 10%. The same was true of the adult-only model. The cost-of-living measure, from MIT, is the one that shows hardship here.

## Decisions made (full reasons in `dev/DECISIONS.md`, Session 39)

- The adults stay the model's people and are grouped into households; children are dependants of a household.
- Composition, budgets, childcare and poverty lines come from the Census Bureau (2023 household tables; 2025 poverty thresholds) and MIT (2026 family budgets).
- Childcare uses MIT's own prices for children under 13.
- Couples share decisions; under pooling they also share money, the debt floor and their poverty status.
- The $25,000 "too little wealth" line had no recorded source. It is within 1.3% of six months of one adult's cost of living ($24,685), so the model now reads it that way and gives households the same rule: six months of their own costs. The adult figures keep $25,000, so they stay comparable across releases.
- People are counted with their household's status, children included; income is compared per equivalent adult (household income over the square root of its size).
- The no-programme run is also made of households (households are part of the population, not of the programme).

## Claude's reading of the design (please check)

- **The child allowance belongs to the household.** It is shared equally between the adults, and under pooling it pays for the household's needs. You confirmed a quarter for each child and that the Act's text should be updated to include it; the "no child allowance" reading sits beside it, as you asked.
- **Partners decide together** whether to take part, join a community business and live in community housing. Your Hub speaks of housing and costs by household; it does not say whether partners can decide separately.

## What you need to do

Nothing yet: this is one step of v5.3, which arrives as one pull request. Please say if either reading above is not what you intend. Your two answers on the dashboard (a quarter for each child, with the Act's text to be updated; the glossary's full list of what BU can buy) are what the model follows. When you next edit the Hub, the Act's Section 102 is the place the child allowance would go.
