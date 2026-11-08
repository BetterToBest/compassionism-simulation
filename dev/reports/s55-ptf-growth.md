# Open PTF access, part 2: how far the PTFs' share of sales grows (S55, Nov 8, 2026)

Claude's reading of the design, and what it adds to the model. Part 1 (`dev/reports/s55-ptf-access-reading.md`) let every adult buy at PTF prices for their zone's PTF share of essential sales, and held that share at its start. This part lets the share grow, as Duke asked on Nov 7 (research-update `audits/2026-11-ptf-access.md`, reading 6 and ledger D16): with capacity, and with capital, operations and market demand as factors too. Nothing here is a result: no study has run, and the rows are preregistered before any run.

## The rule
Each year, before anything reads the share, every zone's PTF share of essential sales grows as far as three limits allow, whichever binds first. It never falls: the limits stop expansion, and nothing here closes a PTF.

- **Capacity (capital).** The PTFs can only sell what their stores, kitchens and plants can supply. The model already has a sourced rule for that: it takes $18,862 of capital per adult to serve all of a population's food and utilities (US capital stock of food stores, food services and utilities per adult, BEA). The PTFs' capacity is their starting share plus the capital they have built from the ESP surplus's reinvestment, divided by $18,862, up to 100%. The release model also lets PTFs borrow to meet last year's unmet demand within a year. That rule still serves membership as before, but it is not extended to sales. Applied to shoppers it would move the share from 18% to the demand ceiling in one year, which no retail network does.
- **Operations.** A PTF expands only where its sales cover its operating costs. In the Hub's own cost structure (the BLEI paper, section 3.3), PTF prices are *set* at cost: direct costs plus a small cooperative overhead. So at the Hub's prices, sales cover costs at every share, and this limit never binds, by construction. The report says so instead of hiding it. A second reading uses outside running costs: what US grocers and utilities actually spend per dollar of sales (BEA and Census, the figures the model already uses to count what PTF price cuts cost). By that measure, sales at the Hub's prices cover about two thirds of running costs where a zone is below the 40% test and less than half above it. A PTF network on those costs could not expand without a subsidy, so under that reading the share stays where it started.
- **Market demand.** Even at lower prices, shoppers will not buy everything at PTFs: the Hub says PTFs "complement private markets". The Hub gives no figure, so this is a labelled design parameter: the largest share of their essentials a zone's shoppers buy at PTFs. Its main value, 49%, is the share of Finland's grocery sales held in 2025 by S Group, a consumer cooperative anyone can shop at (Finnish Grocery Trade Association, from NielsenIQ). It is the largest share found for an open-access cooperative grocery network in a national market. It is cautious, because S Group charges market prices and PTFs charge less. The study also runs 25%, 75% and 100%.

With zones (the community layer), capacity is counted for the whole population. Where the zones together want more growth than the capacity left, every growing zone gets the same fraction of what it wants. Capacity by zone is not modelled.

## What a first look shows (diagnostics only, two seeds, no outcome read)
- Reference environment, release design: the share follows capacity for about eight years, from 18% to about 33% at year 5, then stops at the 49% demand ceiling. So zones pass the 40% test partway through the run, and never reach the 55% test.
- Stress environment, release design: capacity binds the whole run (about 12% at year 5, 19% at year 10, 40% at year 20).
- With no demand ceiling, the Reference share reaches 100% by year 20. With outside running costs, it stays at its start.

These are a check that the rule runs as written. The preregistered rows, on 500 seeds, will say what open access does to poverty, cost and prices.

## Choices where the Hub is silent (modelling assumptions)
- The demand ceiling is a constant. It does not rise when a zone passes the 40% test and its price gap widens: the reading with the smaller effect.
- The share never falls. No limit here falls below a zone's start, except outside running costs, which hold it at the start.
- Capacity is shared evenly across growing zones, not sent first to the densest.
- The operations limit's main reading takes the Hub's cost structure as given, as the model already takes the Hub's price cuts as given. The outside-cost reading is run beside it.

## Checks
- Guard test: with the switch off, every figure of 25 release-panel rows, seeds 1 to 20, all three environments, is identical.
- Four new unit tests: capacity binding alone (the share follows the capital rule, checked against the capital account each year); demand binding alone, with zones; operations binding alone (no zone grows, and the cost coverage equals a hand calculation); and the sharing of capacity between zones, by hand.
- Engine lineage: the 12-seed release panels keep their fingerprints.
