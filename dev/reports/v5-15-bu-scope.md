# What BU can buy: your full list, tried in the model

Oct 7, 2026 · v5.3, follow-up to plan item B3 · Claude · 500 paired runs in each of the three environments · a labelled reading being built; nothing on the live page changes until the v5.3 release

## What was asked

You confirmed on the dashboard that BU can buy the full list in your glossary: housing, food, healthcare, education and transportation (the draft Act's section 103 also lists PTF services). Since September the model has let BU buy only food, housing (with utilities) and medical care. You chose to add the full list first as a labelled reading, with the v5.3 restudy deciding whether it joins the main result.

## What the model does in this reading

- BU can also buy transport, for everyone.
- In households, BU can also pay for childcare at community (PTF) childcare centres. Public school has no fee in the model, so childcare is how education reaches BU.
- Transport and childcare prices follow the general price level. No source gives how their prices respond to BU demand, so the price model's own responses for food, housing and medical care are unchanged.
- What BU can buy grows as a share of the cost of living: for a single adult, from 43.5% to 63.0%; for a single parent with one young child, from 39.5% to 67.0%.

## What the 500 runs show

All figures are Compassionism against no programme in the same runs, paired run by run. The 95% intervals are narrow (within ±0.8 point for every share below).

**Reference environment**

| Measure | Today's list, adults | Full list, adults | Today's list, households | Full list, households |
|---|---|---|---|---|
| Adult-years below the cost of living | 55.2% → 22.0% | 55.2% → 25.2% | 46.0% → 13.3% | 46.0% → 16.0% |
| Adults with too little wealth at the end | 52.0% → 35.7% | 52.0% → 47.1% | 42.6% → 20.0% | 42.6% → 34.7% |
| Adult-years below 30 days of basic living | 46.7% → 18.7% | 46.7% → 21.9% | 37.5% → 9.3% | 37.5% → 11.3% |
| Children below the cost of living | — | — | 74.4% → 24.0% | 74.4% → 28.5% |
| Children in households with too little wealth (last year) | — | — | 71.8% → 37.2% | 71.8% → 54.9% |
| Cost per adult a year | $29,616 | $27,157 | $36,114 | $31,506 |
| Price rise a year | 34.9% | 42.8% | 32.5% | 46.9% |
| Project payouts per adult a year | $6,772 | $128 | $13,878 | $1,870 |

**Adverse and Stress Test environments**

| Measure | Adverse: today's list | Adverse: full list | Stress Test: today's list | Stress Test: full list |
|---|---|---|---|---|
| Adult-years below the cost of living (adults alone) | 78.2% → 42.1% | 78.2% → 46.5% | 78.2% → 65.6% | 78.2% → 65.7% |
| Too little wealth at the end (adults alone) | 82.6% → 87.1% (worse) | 82.6% → 90.9% (worse) | 82.6% → 90.6% (worse) | 82.6% → 90.7% (worse) |
| Too little wealth at the end (households) | 76.5% → 73.8% (better) | 76.5% → 89.7% (worse) | 76.5% → 89.1% (worse) | 76.5% → 90.4% (worse) |
| Children below the cost of living | 91.3% → 43.4% | 91.3% → 50.4% | 91.3% → 75.4% | 91.3% → 76.4% |
| Price rise a year (adults alone) | 45.5% | 55.2% | 23.8% | 24.1% |

In the Stress Test the two lists give nearly the same results: few people take part there, and project work is already small.

**In short:** with the full list, every gain is smaller. The programme still cuts the share of people below the cost of living by about 30 points in Reference (33 with today's list), but it does much less for wealth, and in the Adverse environment the households' small improvement in wealth turns into a large loss (−2.7 points becomes +13.1).

## Why: one allowance, two uses

In the model, each month's BU either buy essentials or go unspent and expire. Expired BU are not wasted: the design directs them to creative projects. People hired for project work are paid by converting those BU, and the model counts their work as new output. That output backs part of what the Source pays, so that part is not new money.

With today's list, BU can buy less than half of a single adult's cost of living, so a large share of BU expire and fund project work: $6,772 per adult a year in Reference. With the full list, almost every BU is spent on essentials, and project work nearly disappears ($128). In Reference, adults alone:

- BU spent at face value rise from $9,604 to $11,217 per adult a year (people buy more essentials with BU);
- conversion income falls from $17,514 to $13,450 (the project pay is gone);
- the output that backs the Source's payout falls from $6,081 to $911, so the new money the Source creates rises from $21,038 to $23,756 per adult a year;
- prices rise faster (34.9% to 42.8% a year), which wears down savings: more adults end with too little wealth.

The same happens with households, more strongly, because children's BU no longer go unspent once childcare can be bought with them.

The official poverty line moves too: adult-years below it are 2.6% with no programme, 2.4% with today's list and 4.5% with the full list. BU spent on essentials are not money income, and the full list cuts the conversion income that is.

## What this means

1. **This is how the model works, not a bookkeeping slip.** Every accounting check passes in all twelve readings (three environments, four readings each): 156 million checks of a person's money, 25 million of couples' shared money and 10.5 million of community-housing equity, plus every yearly total. The largest gap anywhere was a ten-billionth of a dollar.
2. **It shows how much the current main result rests on project work.** With today's list, project work backs about a fifth of what the Source pays in Reference ($6,081 of $27,118). The model values that work at market rates. It is a modelling choice that matters a great deal, and the restudy will report it as one.
3. **How the restudy will decide.** You confirmed the full list is the design. So my plan for the restudy is to make the full list the main result unless the restudy finds a modelling error in it. A result that looks worse is not a reason to keep the narrower list, because results do not choose the design. I have recorded this rule in `dev/DECISIONS.md` before the restudy, so the restudy cannot be steered by its own results.

## Claude's reading of the design (please check)

- **Childcare counts as something BU can buy.** The Act lists "Education" and "PTF services"; the model has community childcare centres, and public school is free. College is not modelled.
- **All of a household's transport budget counts.** The Act says "Transportation (non-luxury)". MIT's transport budget, which the model uses, is a basic budget (a used car's running costs or transit), so all of it counts.

## What you need to do

Nothing yet: this is one step of v5.3, which arrives as one pull request. Please say if either reading above is not what you intend, or if this explanation misreads how expired BU should work in your design.

The runs and their exact commands are in `dev/runs/scope-check-ref.json`, `-adv.json` and `-st.json` (`node dev/tools/scope_check.js ENV 500`).
