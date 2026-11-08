# Open PTF access: who may buy at PTF prices (S55, part 1, Nov 8, 2026)

Claude's reading of the design, and what it changes in the model. The full note, with what the Hub says and Duke's answers, is in research-update `audits/2026-11-ptf-access.md` (ledger D16, answered Nov 7).

## The question
In the design anyone may shop at a Public Trust Foundation (PTF) business, a grocer for example, paying in dollars or in Basic Units (BU), at one posted price. Until now the model let only PTF members pay PTF prices: "member" stood for "customer" everywhere. The two tests that depend on how dense the PTF network is (the food price cut is smaller below 40%; the synergy coefficient θ is zero below 55%) counted members.

## What changes
A switch, `PTF_ACCESS`. With `'members'` (the default) the model is exactly what it was: every published figure and the frozen study batch are unchanged, and a test proves it figure by figure. With `'open'`:

- **Every adult buys the same share at PTF prices.** Each zone (one of the community layer's communities, or the whole population without the layer) has a PTF share of its essential sales: how much of its food and utilities is bought at PTF businesses. Every adult in the zone, member or not, buys that share at PTF prices and the rest at market prices. Nobody buys more than the zone's share.
- **Both density tests read that share**, not the share of adults who are members. A zone where PTFs sell 70% of the food passes the 40% test even if few of its residents are members.
- **Membership keeps only membership.** Joining and leaving still happen as before, and so does everything about housing PTF (PTH). Membership no longer decides who pays PTF prices.

## Every member-only rule, sorted
The engine had 18 places where being a PTF member mattered. Eight are about buying (customer rules) and are opened to every shopper at the zone's share: the price cut itself, wherever it enters (the cost of living, what BU buy, the joining decision, PTH's cut on utilities); the ESP surplus's price pool, its sizing and its private-business mirror; θ's lowering of the cost of basic living; the discount PTFs fund from forgone profit (accounting); and the health-sector cut on the public plan (zero in every main row). Two are the density tests. One, PTF's damping of the outside inflation rate, is a market effect and now reads the PTFs' share of sales. The other seven stay as they were: joining and leaving, the capacity limit on joining, the conversion-rate bonus (below), the ESP workforce option, PTH, the community layer's placement of starting members, and how results are reported by group. The table is in `dev/DECISIONS.md` (S55).

One rule needed a closer look. Members get a higher conversion rate (1.30 plus θ). The Hub gives that bonus to PTF *workers*, as an employment incentive, not to customers or members. The model has no PTF workforce, and members stood for workers. The bonus stays with members, unchanged, so that comparing open access with members-only measures access alone. Who works at PTFs is a stated limit of the model (a modelling assumption).

## Choices where the Hub is silent (modelling assumptions)
- **Where each zone starts:** at its share of adults who start as members. That is the environment's starting share (18% in Reference and Adverse, 8% in Stress) up to sampling, read as a share of sales, as Duke agreed. It also means both readings start with the same density tests, so the difference between them begins as a difference in who gets the price.
- **Buying is proportional:** for the zone's share of their purchases every adult is what a member was for all of them. How shoppers choose between PTF and private sellers is the demand limit of part 2.
- **Only with the release model's PTF** (PTF by sector). The switch refuses older PTF models rather than open them halfway.

## What part 1 does not do
- The share does not grow yet. Part 2 builds the growth rule Duke asked for: the share grows as far as capacity (capital), operations (sales covering operating costs) and demand (how much shoppers buy at PTF prices) allow, whichever binds first, each from sourced figures or labelled and swept design parameters.
- A row can hold every zone's share fixed (`pa: {fix: 0.4}`, for example). That is how the preregistered sweep from 10% to 100% will run, with growth off.
- No study has run with the switch. Nothing here is a result. The rows are preregistered (research-update `prereg/`) before any run, and the first runs are a pilot on GitHub Actions.

## Checks
- Guard test: every figure of 25 release-panel rows, seeds 1 to 20, all three environments, identical with the switch off.
- Four unit tests (`paUnitSuite`): off equals the model as it was, with and without the community layer, and the no-programme run is untouched; a member and a non-member in the same zone pay the same price; the 40% and 55% tests read the share of sales; BU spent at PTFs is the zone's share of every holder's BU; at a share of zero no one pays a PTF price; bad settings are refused.
- Engine lineage: the 12-seed release panels made by the changed engine have the same fingerprints as the published ones.
