# Creative-output backing, capacity speed and the octave limit: Claude's reading of the design

Session 31, Oct 2, 2026. Ledger step s67; Duke's answers to d137, d138 and d139 (Oct 2). Written by Claude before any code. Everything below headed "Claude's reading of the design" is labelled that way wherever it appears on the page.

## Duke's three answers (quoted)

- **How fast ESPs add capacity (d137):** show both. On the main run, ESPs add enough capacity within a year to serve underserved demand. The 5-year rule (capacity built only as fast as reinvestment reaches today's capital per adult) is shown as a labelled other reading.
- **What backs a creative payment (d138):** "New output is offered to the public like a community chest of sorts, both belonging to the citizens, and offered a lower price than private market goods/services. This is the difference between price and value. For example, open-source software is free, but closed software costs 100/month. ... Collective contributors get a higher conversion rate and unlimited octave capacity for offering their software for free or for 1 dollar per month. Likewise, a band can sell out a stadium for ticket prices at $100, but they can offer tickets to collective members for 6 expired BUs. If the band has an earned conversion rate of 9*Phi or 14.56, they stay revenue neutral."
- **What the octave limits (d139):** "ESPs who accept BUs have octave caps based on their capacity. Individuals and Creative Collective member groups have unlimited octave caps, but they must show their work to earn an elevated conversion rate."

The Research Hub agrees with the d139 answer: "For PTF businesses, octave capacity tracks market throughput" (Glossary, Octave Levels), and Creative Collectives "manage peer-reviewed conversion processes" (Research Summary).

## Claude's reading of the design

1. **Creative work is paid like the ESP correction: revenue neutral.** A Creative Collective group offers its output to members far below the market price (6 BU for a $100 ticket). It converts those BU at its earned rate (6 x 14.56 = about $87), so its dollar income is close to what the market would have paid. The conversion payout is therefore matched by output members actually receive, valued at what a private seller would charge for it.
2. **"Show their work" is the brake.** A group earns a rate above 1x only for output it has delivered and had reviewed. In the model: the part of a creative payout above face value is paid only against delivered output. A group with nothing to show converts at 1x.
3. **The total limit comes from the ESP side.** BU can only be spent on essentials, and each ESP can convert only as many BU as its capacity supplies. So the BU that reach ESPs cannot exceed what ESPs can supply. Individuals and Collectives have no octave cap.
4. **Creative output mostly adds things beyond essentials** (Duke's examples are software and concerts). It counts as backing for the general price level, not as essentials supply. It does not lower basket prices directly.
5. **Expired BU can pay Collective groups** ("6 expired BUs"). In the model, part of a member's expired BU may be directed to Collective groups instead of returning to the Source. How much is not stated anywhere, so it is a design parameter, swept (0%, 25%, 50% of expired BU), labelled a modelling assumption. If the session-30 build already lets participants direct BU to projects, this route uses that same path.

## Where Claude's modelling has to be cautious (and why both readings are shown)

The design counts a creative payout as backed by the market value of what members get. That is right **when the output is new**: a concert put on for members adds real output, so the new money has something to buy. It is not right when the output would have existed anyway: if members simply take seats that cash buyers would have bought, output is unchanged and the payout is new money with nothing new behind it. The model cannot see individual concerts, so:

- **Main run (the design's reading):** creative payouts for shown work are backed at market value. In the model this means the elevated part of each project payout counts in full as output, beyond essentials.
- **Other reading (cautious, labelled):** backing counts only the cost of the hours and materials the project paid for (the session-30 production-side rule).
- **Sensitivity row:** every converted dollar backed (the old "H1" row), kept as before.

All three are shown; the page says which is the design's reading and which is the cautious one.

## Capacity speed (d137), as it will be built

- **Main run, within a year:** when BU spending at ESPs in a year exceeds their capacity, capacity rises the next year to meet it. Faster capacity is not free: the new capital is charged every year at its depreciation plus interest, from sourced figures (BEA Fixed Asset Tables, current-cost depreciation and net stock for retail trade, food services and utilities; the interest rate from the Federal Reserve H.15 release). Its capital per adult is the same $18,862 the 5-year rule uses (BEA and Census 2025, already in the session-30 build).
- **Other reading, the 5-year rule:** capacity grows only as fast as ESP reinvestment pays for it (session 30's rule, about year 5 at Reference).
- In both, when BU demand exceeds capacity in a year, participants spend the BU they can and pay cash for the rest; the unspent BU expire to the Source (or, under point 5, partly to Collectives).

## Switches, tests and the restudy

- Switches: `CAPSPEED` (`'reinvest'` = session 30, `'oneyear'` = main), `CREATIVE` (`'cost'` = session 30, `'market'` = main, `'all'` = H1), `ESPCAP` (ESP octave cap from capacity, on/off), `EXPIRED_TO_CC` (share 0 = session 30). With all switches at their session-30 values every output is bit-identical (full-output diff).
- No new random draws.
- Tests: total BU converted at ESPs never exceeds ESP capacity; a group with no delivered output converts at 1x; under `'market'` the counted output equals the elevated part of the payout; capital charge under `'oneyear'` equals capital x (depreciation + interest); expired BU directed to Collectives never exceed expired BU.
- Restudy: seeds 1-500, Reference, Adverse and Stress; basket and wealth poverty confirmed, not only the severity index.

## Waiting on nothing from Duke

Duke's answers settle the design questions. If any line above misreads him, say which.

## Built (session 31, Oct 2, 2026): what the code does, and what the model already had

- **Creative output at market value:** `PROD.match = 'market'`. Each project worker's whole payout counts as new output, beyond essentials. In the model, a project payout always comes with hours worked, which is the model's version of "showing the work".
- **Capacity within a year:** `PROD.speed = 'oneyear'`. Adults who were turned away from a community business for lack of capacity are served the next year. The capacity reinvestment has not yet paid for is borrowed and charged every year at **8.20%**: depreciation of 4.53% (BEA Fixed Assets Tables 3.4ESI and 3.1ESI, 2025, grocers, food services and utilities) plus a real interest rate of 3.67% (2025 averages from FRED: Moody's Baa 6.00% less the 10-year Treasury 4.29% plus the 10-year inflation-protected Treasury 1.96%). Community businesses pay it out of their earnings before the rest is split.
- **The ESP octave cap (d139)** holds in the model without new code. BU can only buy the essentials people already consume, which businesses already supply, so no business converts more BU than it sells. A unit test checks this.
- **Individuals and Collectives uncapped, and expired BU paying Collectives:** the model already worked this way (project hiring has no conversion cap, and every expired BU pays project work). No new switch was needed, so the parameter I said I would sweep in point 5 is not needed.
- 5 unit tests (`v5ProdUnitSuite`). With the session-30 settings, output is identical.

## Results: 500 paired runs, against step 14 (`dev/runs/step15-creative-500-*.txt`)

| | Reference | Adverse | Stress |
|---|---|---|---|
| Below the cost of living | 22.6% → 22.0% | 44.5% → 43.6% | 66.6% → 66.6% |
| Too little wealth at year 20 | **40.4% → 35.7%** | **90.4% → 88.1%** | 91.3% → 91.2% |
| Price level at year 20 (no programme: 1.0 at Reference) | 671 → 297 | 4,660 → 2,082 | 96 → 92 |
| Cautious reading (creative work at the cost of its hours) | no change from step 14 | no change | no change |
| Capacity only as fast as reinvestment pays (the 5-year rule) | same as within a year | same | almost the same |

In everyday words:

- **Counting creative work at market value roughly halves how far prices rise by year 20** at Reference and Adverse, so savings hold up better. Fewer people end with too little wealth (−4.7 points at Reference, −2.3 in Adverse).
- **How fast community businesses add capacity makes almost no difference in the model.** Community-business membership grows slowly, so the capacity limit rarely binds. Both readings stay on the page, as you asked, but they give the same result.
- **In Stress, little changes**, because fewer people take part and project work is small.
