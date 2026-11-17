# Limits on supply, cost-of-living adjustments and who goes without: Claude's reading of the design (v6 engine, before it is built)

Nov 17, 2026. Written before any part of the v6 engine is built or run. Preregistration: BetterToBest/research-update `prereg/2026-11-s82-v6-supply-indexing.md`. This note says how the model will read the design where Duke Johnson's writing is silent, and why. It reports no result.

## Why the engine needs this

The outside reviews of v5.9 and the in-house audit found the same thing. Below full backing, the model has no limit on what the economy can supply. With no backing at all, the programme still cuts basket poverty by about 31 points while prices rise 40% a year, because wages, the Basic Unit (BU) and the cost-of-living basket all follow prices in full and at once, and no household is ever short of housing, care or food. The only people who pay for the goods the programme's recipients gain are holders of savings and lenders. That is a property of the model, not of the design, and the reports now say so in dated notes. The v6 engine adds the missing parts as readings, each behind its own switch, so that the backing curve can be read with them.

## What the engine does today (read in the code, Nov 17)

1. **Essentials.** Each year the engine measures how much of their needs basket households could pay for (what they could not pay for, at the debt floor or through the spending cut for low incomes, is counted as unmet). The programme run's figure is compared with the no-programme run's own figure, and prices of housing and medical care rise with the difference (by 0.6 and 0.5 times it; food 0). Everyone then receives what they paid for. In supply-and-demand terms this is a market in which any extra need is met at a slightly higher price: the engine never lets supply run short.
2. **The capacity price rule's "rationed share"** (the share of demand no output could meet) and its "shadow price" readings are reported beside the results, but nothing feeds back into what households receive.
3. **Wages** rise with the year's programme inflation in full (wage indexation 1).
4. **The BU** under the full-coverage design is reset every year to the year's price of the needs basket, with no delay.

## Duke's points (Nov 17) and how the model will read them

**1. No arbitrary ceiling.** Duke: a low ceiling on demand would fuel extraction when efficiency can make life easier; "more for less is the design, not less for more." *Reading:* the limit in the model is what the economy can produce, never a cap on anyone's demand, sales or earnings, and it applies only to housing, medical care and food, the three goods with physical capacity (agreed with Duke earlier the same day). Copied goods, such as downloads and software, are never limited. The supply the model starts from is not today's consumption of the needs baskets. Today's economy produces far more housing, care and food than the needs baskets use. Better-off households consume well above needs, and some capacity sits idle. Extra need is met first from that headroom, as prices move. The headroom is measured from opened sources, sector by sector, before anything runs.

**2. Prices move with supply and demand, modelled as well as we can.** *Reading:* in each sector, in order: (a) prices rise with demand, as today; (b) idle capacity and the above-needs consumption that better-off households give up as prices rise meet what they can at once; (c) new capacity is built over the following years (homes, clinics, planting), at a speed taken from sources; (d) only what is still unmet is shared out, as a cut in the housing, care or food households receive. At full backing the programme's own output meets its demand, so the limit never binds and the main results cannot move.

**3. Balance is not always left to the market.** Duke: farm programmes pay farmers not to produce in some years, and these levers should be set by the people, not by special interests or by banks that gain from austerity. *Reading:* that is right, and the model will say so plainly. How fast supply can answer need is set partly by policy in all three sectors: land-use and zoning rules for housing, the number of funded residency places and licensing rules for doctors, and farm programmes that pay to keep land idle. The model's low supply reading stands for those policies as they are today. The report will name them as policy levers, not as facts of nature. This is Claude's reading of the design and of the evidence. Duke's view that these levers should be set democratically is his, and the report will attribute it to him.

**4. How a shortfall is shared will likely harm the poor.** Duke: in a market, the people whose only capital is their labour are the first to go without, and an injury or a medical bill can ruin them, which is why the design supplies the basics, with providers given a reason to supply them. *Reading:* the model will not pick one rule. It runs three and shows them side by side:
- **The market's rule:** those least able to pay go short first. This is what happens without a policy that protects the basics. Today's economy already does this: in the no-programme run, the households who cannot pay are the ones who go without. It is the most cautious rule for the programme's claims, so it comes first in every table.
- **An even share:** every household's essentials are cut by the same proportion.
- **The design's rule:** basics bought with BU are served first. The design gives providers a reason to do this. An essential-service provider converts the BU it accepts at three times face value, under the progressive tax (the model already pays this), so a BU sale is worth more to the provider than a cash sale. Under this rule the cut falls on essentials bought with cash.

Where a result depends on the rule, the report will say so, and say that the market's rule is what a shortage does when nothing protects the basics.

**5. Cost-of-living adjustments.** Duke: a yearly COLA is fine, but the ideal is quarterly or monthly. The Hub's Inflation Surge Protocol says the same: "Monthly COLA adjustments to basic units" when prices rise more than 5% (integrated implementation roadmap). *Reading:* the BU is run with a monthly adjustment (an average delay of about an eighth of a year), a quarterly one (a quarter of a year), a yearly one (one year, as Social Security does it) and a two-year delay (a bound). The monthly and quarterly readings are the design's and are reported first. Wages are run following programme inflation in part: half or three-quarters at once, with the rest either never made up or made up a year later.

**6. Creative Collectives as lenders.** Duke: the collectives can cover gaps where people cannot get bank loans or investment for beneficial work. *Reading:* that is a way new capacity gets built, and it belongs with the next engine step, which models output per hour in PTF, collective and project work with its inputs (work, capital, time). This step does not model it. Until then, capacity grows at the speed the sources show for today's economy.

## What this step does not model

- Shortages of anything other than housing, medical care and food (Duke's narrowing). The general shortage the price-rule study found (money spent before prices adjust) stays a reported reading at shadow prices.
- The Inflation Surge Protocol's other two measures, "enhanced luxury restrictions" and "temporary conversion limits". The Hub gives no amounts. Each would lower demand when prices surge, so leaving them out is the cautious side for the design. They are listed for a later step.
- Any shortage in the no-programme run. Its supply is its own demand, so it is never short. Its poorest households already go without through prices.
- Rows paid for by a contribution, where backing has no meaning. The limit is applied to the rows paid for by the Source.

## Modelling assumptions (labelled; where the writing is silent)

1. The extra need is spread over housing, care and food in the basket's proportions (the engine measures needs met as one share of the basket).
2. A cut uses last year's gap, the same timing as the engine's essentials prices.
3. Money that cannot buy essentials is spent on other goods, so a shortage does not raise anyone's savings. This is the cautious reading for the wealth results. Keeping it as savings is a second reading.
4. Basket poverty, under the limit, is measured on what households received: money that cannot buy the needs does not count toward them.
5. The market's rule cuts each household in proportion to its essentials, weighted from twice the average for the household least able to pay down to nothing for the most able (ranked by cash income against its needs).
6. The engine's essentials price response (0.6 housing, 0.5 medical, 0 food) is kept as it is. It is unsourced. With the limit on, prices and quantities are no longer derived from one elasticity: a stated limit.
