# What a government could set: Claude's reading of the policy levers

Nov 5, 2026 · research-update plan step S54 (ledger D12, D13) · written before any run · Claude

Duke, this note is my reading of the levers a government running Compassionism could actually set, and how the model will represent each one. Please say if anything misrepresents your design. Where your writing is silent I took the most cautious option and labelled it a modelling assumption or a design parameter. Nothing here changes a released figure: every lever sits behind a switch (row option `lv`), and with the switch off the model is bit-identical to today's.

## Why this step

The backing study (S51) found that the release row pays out about 60% of a year's earned income in new money every year, and that no plausible amount of new output backs it. Your answer to D12 was to test every lever a policymaker could set before choosing one. Finding that a lever does not work is a result, and it will be published as one.

## Where the new money comes from (what the levers can act on)

In the release row the Source pays, each year:
1. **BU spent at face value.** A business that accepts a BU for food or rent is paid a dollar for it by the Source. This is the largest single flow.
2. **The business conversion premium.** The business converts the BU at 3x, less the conversion tax, and the premium over face value is paid out the next year (price cuts, reinvestment, a profit share for workers, lower BU prices at private businesses).
3. **ESP payroll conversions** at the worker's own rate, above face value.
4. **Project conversions** of expired BU. The model already counts these as backed: the project work is output worth what it paid.

The conversion tax is withheld from every conversion, so it already lowers the new money. One consequence follows before any run, and I want it on the record now: **no conversion tax below 100% can make the Source self-funding by itself**, because the face value of every BU spent is new money and the tax applies only to conversions. A business converting at 3x under a tax τ is paid 3(1 - τ) per BU; that is new money unless τ is 100%. So the "self-funding" break-even rate will very likely not be reached in the swept range. The sweep still shows how far each rate goes.

## The levers

Each entry: what the Hub says; who would set it; the range swept; the direction I expect. "Design parameter" means the Hub does not give a value and the model sweeps one.

### Taking money back

1. **Conversion tax, base rate.** The BLEI paper (6.3) estimates self-funding at 60-65% participation with a 12% conversion tax and says a formal fiscal model is still needed. Set by: the Source (Treasury), as a published rate schedule. Swept: 0, 4, 8, 12, 16, 20, 25, 30, 40% (12% is the release row). Expected: less new money and lower inflation as the rate rises; conversion income falls with it.
2. **Its progression.** Today the rate rises 4 points for each rate point above 3x, capped at 75%. That schedule comes from the earlier engine; the Hub text I have read does not give it (design parameter). Swept: 0, 4 or 8 points per rate point above 3x; cap 50% or 75%. Expected: small effects, because few conversions run above 3x.
3. **A separate rate on business (ESP) conversions.** Not in the Hub (design parameter). Set by the Source. Swept: 0, 25, 50, 75%. Expected: the strongest of the tax levers, because business conversions are the largest flow after face value. **Modelling assumption:** a business is never paid less than the face value of the BU it accepted (otherwise it would stop accepting them), so the premium cannot go below zero. At 3x this binds only above a 67% tax.
4. **The Source keeping a share of the projects' proceeds** (D12's second lever, as a dial). The model counts project work as output worth what it paid. Under this lever the projects sell that output, and the Source keeps a share of the sales and retires that money. It needs an institution the writing does not describe. Swept: 0, 10, 25, 50%. Expected: small, because projects are about 7.7% of the payout (S51).
5. **Expired BU retired instead of recycled to projects.** The Hub says expired BU "either revert back to their source, the treasury, or get converted into primary notes" (your article, 2024). The release row sends all of them to projects. Swept: 100% (as released), 50%, 0% recycled; the rest is retired unconverted. Expected: little effect on prices, since project pay is counted as backed; participants lose project income.
6. **Outside finance instead of the Source.** Not described by the Hub. The model has three rows already: a progressive income tax, a land-value tax, and a flat contribution on wages. Set by: the legislature. Expected: little or no programme inflation, at the cost of taxes on earners (with the labour response).

### Paying out less, or more slowly

7. **The business conversion rate.** 3x is an assumed placeholder (the Hub's café example says 2-4x). Swept: 1x, 1.5x, 2x, 3x. Expected: the biggest single effect on new money; lower private BU prices and profit shares with it.
8. **The BU amount.** $1,200 a month in the release row; the C2.2 design pays the cost of basic needs. Swept: 60, 80, 100% of the design's amount. Expected: less poverty relief and less new money.
9. **The top multiplier.** 9x in the release row. Swept: 3, 6, 9. Expected: lower conversion pay at the top; modest effect on new money (projects are counted as backed).
10. **Octave capacity and the number of octaves** (D12's third lever). The dual-currency paper (3.4) says conversion is limited by octave capacity, "creating an endogenous ceiling on monetary expansion". In the release row the capacity (12 x 1,000 x 2^octave BU a year) is not enforced on project work. **Modelling assumption:** the lever enforces it, at 25, 50 or 100% of that capacity. The number of octaves (6 today) is swept at 2, 4 and 6. Expected: the capacity rarely binds, because project pools per person are far below 12,000 BU a year; I expect little effect, and will say so if that is what happens.
11. **The Phi tier** (x1.618 above a quality line), on or off. Expected: small.
12. **A phase-in of conversions** over 1, 5 or 10 years. Not in the Hub (design parameter). **Modelling assumption:** in year t the premium above par of every conversion rate is scaled by (t + 1) / N, up to 1: at 3x and N = 5, businesses convert at 1.4x in year 0 and 3x from year 4. Expected: less new money early, the same later.
13. **An issuance rule that caps the Source's net new money** at 2, 4 or 8% of earned income a year, rationing conversions pro rata. **Modelling assumption:** each year the Source sets next year's conversion budget from this year's figures: the cap, less the new money that does not depend on conversions (chiefly BU spent at face value), over what conversions would pay at full rates. It then scales the premium above par of every conversion rate by that factor (between 0 and 1). The face value of BU is always honoured, so if BU spent at face value alone exceed the cap, the cap cannot be met; the model reports how often it is met.

### Protecting value

14. **BU indexation** (D12's fourth lever). The Hub's Inflation Surge Protocol raises the BU only in a year prices rise more than 5%. Swept: that rule, every year to the price level, and every year to the price of basic needs (as in C2.2). Expected: from S51, every-year indexation removes the 2-5% gap where the BU loses value unprotected.
15. **Savings that keep up with prices, as a policy** (an inflation-protected account, like US I bonds). Not in the Hub (design parameter). **Modelling assumption:** every adult's positive savings are credited the year's price rise plus 0.97% real (the engine's existing rate), and the Source pays that interest as new money, so it is not free: it counts in the new money and the cost. The no-programme run keeps ordinary savings, because the account is part of the programme.
16. **Rent increases for BU tenants capped at prices** (the counterpart of the rent risk, row option `hc`). **Modelling assumption:** a participant who rents outside community housing pays rent that rises no faster than the general price level: the part of the housing price above the general level is removed from their costs, and landlords may not mark up rents for BU tenants (`hc`). Landlords bear it; it is not programme cost. A stated limit: the model has no landlords and no housing supply response, so it cannot show rent control's long-run effect on supply. This favours the lever, and the report will say so.

## Joining that sees what joining pays (a second reading, behind the switch)

Today an adult joins when the BU they would use exceed a revealed cost, set so that year 0 has today's participation. The joining rule does not see the conversion tax, so a tax sweep would show higher taxes as all upside. **The new reading** adds the adult's expected conversion income after tax: last year's project pool per unit of allocation weight, times the adult's weight (octave capacity x quality), times their rate after tax, counted only if project work would pay them more than an hour of their wage (as the hiring rule already requires). The revealed cost grows in the same proportion, measured at the released tax schedule, so at a 12% tax year-0 participation is exactly unchanged, adult by adult. In any year the rule is:

join if (BU used + expected conversion income at the row's tax) >= (BU at full use + expected conversion income at the released tax) x (the adult's latent cost share).

Under C2.2 the BU is paid automatically, so joining does not change. Both readings are run; the preregistration says which is the test.

## How the best settings are chosen (D13, confirmed Nov 2)

No harm first: non-participants no worse off, and wealth poverty no worse than with no programme on the preregistered savings reading. Then, among those, the lowest basket poverty with programme inflation under 5% a year. The full trade-off front is published beside it. Settings are chosen on one set of seeds and confirmed on seeds never used to choose them; only confirmed settings are reported as findings.

## What I expect before any run

- No single lever makes the release row self-funding (the face-value argument above).
- The levers that cut the business premium (business rate, business tax, the issuance cap) move inflation most; the octave levers and the Phi tier move it little.
- Every-year indexation helps basket poverty; the inflation-protected account helps wealth poverty but adds new money.
- If no setting passes the no-harm test with inflation under 5%, the report will say so plainly. The release row stays as released either way, and the policy comparison stays frozen (d94) unless you lift it.
