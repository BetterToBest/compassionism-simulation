# When prices jump from outside: Claude's reading of how PTF and PTH protect the basics

Nov 2, 2026 · research-update plan step S52 · written before any run · Claude

Duke, this note sets out my reading of what your writing says PTF and PTH do when the price of the basics jumps for reasons outside the economy: a war, bad weather, a cartel. It then describes how the model now represents such a shock. Please say if it misrepresents your design. Where the text is silent I took the most cautious option and labelled it a modelling assumption.

## Why this matters

The Hub says PTF and PTH give people "stable, affordable access to housing and essentials". The modelling paper says "PTF residents [are] insulated from housing cost inflation". The integrated-framework paper says that in an 8% inflation scenario, local inflation is held to 3.2% while the national rate reaches 8.1%. The risk paper names "energy price manipulation" as a threat that PTF's "community resilience" defends against. None of these was tested against a shock that comes from outside. The model has had recessions and steady outside inflation, but never a sudden jump in the price of the basics. The earlier figures (3.2% against 8.1%, for example) are not targets for this study.

## What the writing says

1. **What PTF removes.** The BLEI paper splits a food price into the raw cost (production, logistics, perishables: about 35-40% of the price), overhead (marketing, distribution, financing: 20-25%) and shareholder return and profit (15-20%). PTF, "operating as nonprofit cooperatives under collective purchasing arrangements", removes the profit and cuts overhead by 40-55%. That is where the model's food price cut comes from (a food BU is worth about 2.64 times its face value at PTF prices; utilities, 1.80 times).
2. **What PTF does not remove.** Nothing in the writing says PTF can make the raw cost of food or energy fall. An energy shock raises exactly that raw cost: fuel, fertiliser, freight, heating. A cooperative cannot buy diesel for less than diesel costs.
3. **Local production.** The community development paper says wealth comes "through local production rather than external transfers". The PTH governance paper lists "collective electricity purchasing (CCA model)" and "shared solar installations and battery storage". The modelling paper's environmental section mentions "local production emphasis". The writing gives no share of PTF's supply that is local.
4. **PTH.** PTH removes the landlord's markup on rent; Acre Equity "insulates residents from housing market fluctuations". The writing does not say PTH pays its residents' utility bills.
5. **Pooling.** The integrated-framework paper says PTF "provides economic stabilization through diversified asset portfolios following Alaska Permanent Fund principles". It does not describe a price reserve that would spread a jump in costs over several years.

## My reading, as rules the model can run

- **X1. The shock comes from outside and is relative.** The real price of energy (energy over all other prices) rises, and the basics that use energy rise with it. The model does not represent why it rises. Wages follow the general price level, not this rise, so the shock is a real loss to every household that pays it, as it was in 2022.
- **X2. Size and length come from history.** US consumer prices since 1967 hold three large episodes: 1972-74 (real energy price up 24.6% in two years), 1978-80 (32.8%) and 2020-22 (37.3%). The main shock is the middle one: up 32.8% over two years, starting in year 5 of the run, and two years after the peak 88% of the rise is still there (the middle episode again; 2020-22 kept 51%, 1972-74 all of it). The other two episodes, and a shock twice the middle one (beyond anything since 1967, labelled so), are swept. These are the calibration, not targets.
- **X3. How far each basic moves.** From the same data: transport prices move 0.39% for each 1% of real energy price, household energy (utilities and heating) 0.49%, food 0.10%. Rents and medical care do not move with energy over two years (their estimates are not different from zero), so they do not move here. The model's housing category includes utilities (12.8% of it), so housing moves by that share of the utilities' rise. With the main shock the market basket of a household rises about 2-3%.
- **X4. Markup and scarcity.** Part of a price rise in a shock is wider margins: firms raising prices by more than their costs. The rest is real cost. The evidence ranges from almost none ("available data do not point to a widespread increase in markups", IMF, 2023) to more than half (US markups rose 3.4% in 2021 against 5.8% inflation, and then fell in the second half of 2021 as energy prices rose; Kansas City Fed, 2023). The main reading takes a quarter; none and a half are swept. This share is a design parameter, not a sourced constant.
- **X5. PTF removes the markup part and pays the real-cost part.** A PTF member's food and utilities cost is PTF's price before the shock plus the member's share of the market's dollar rise: (1 - markup share) of it. This is the cautious reading: in dollars, the member pays the same real cost the market pays. (Applying PTF's percentage cut to the shocked price instead would hand members a large part of the real cost rise for free, which nothing in the writing supports.) PTF does not sell transport in the model (it covers food and utilities), so a member pays the transport rise in full.
- **X6. Local sourcing is a design parameter.** A share of PTF's supply (none in the main reading; a quarter, half and all swept) comes from local producers. The outside shock reaches local supply only half as much (local farms and generators still buy fuel and fertiliser; fully protected local supply is swept). Local supply's normal price is not modelled: local food often costs more in normal times, so the sweep is an upper bound on what local sourcing buys. This is a modelling assumption.
- **X7. PTH removes the rent markup, which this shock does not move.** A PTH household pays its utilities' rise in full, unless it is also a PTF member (then X5 applies). So, by construction, PTH protects against this kind of shock only through PTF. This is the cautious reading of item 4; the collective electricity purchasing the governance paper describes is not credited, because it buys at market prices.
- **X8. No price reserve in the main reading.** PTF passes each year's cost change through in that year. A reserve that spreads it over three years and is then repaid (members pay the same in total, later and more evenly) is swept.
- **X9. The BU is the design's other protection.** Participants spend their BU on food, housing and medical care at their own prices. While the BU covers a household's basics, a price rise is paid in BU, not in money. That is the CCO protecting participants, not PTF, and the measures keep the two apart.

## What the study measures

For each group (PTF members, PTH members, other participants, adults in none of these, and adults who chose not to take part, who are the same people in every design), before, during and after the shock:
1. the share of the shock that reaches the group's own money costs (the rise in what they pay over the rise in the same basket at market prices, against the same run without the shock);
2. how much their costs jump from year to year;
3. basket poverty (below the cost of living) during and after the shock.

## What this means before any run

The shock is small for the basket as a whole (about 2-3% at its peak in the main reading), because energy is a small share of what households buy, and its biggest channel, transport, is outside PTF. PTF's own protection is then limited by construction to the markup part of food and utilities, plus what local sourcing buys. A first one-seed test run (not a result) shows that the BU, not PTF, absorbs most of the shock for participants, and that adults outside the programme pay all of it. The study is built to measure this honestly and to say plainly which protections are by construction and which emerge.

## Not changed

The released figures do not move: the shock is behind a switch (preset key `sx`). The policy comparison stays frozen (ledger d94): the shock runs within the study programme only.
