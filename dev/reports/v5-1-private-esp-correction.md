# Correction: privately owned essential-service businesses pass the conversion premium to customers

Session 31, Oct 2, 2026. Design note before code (ledger step s66, decision d140). Written by Claude.

## What changes, in plain words

An essential-service business (an ESP: a grocer, a utility, a clinic, a restaurant) that accepts Basic Units (BU) converts them into dollars at more than face value. The session-30 build gave that extra amount (the "premium") to the owners of privately owned ESPs, shared by wealth. That was wrong. Duke's design, as he described it on Oct 1:

> A privately owned ESP cuts its prices for customers paying in BU so that it stays revenue neutral. At a 3x conversion rate, a $9 / $12 / $15 menu becomes $3 / $4 / $5 in BU.

So the premium becomes **lower prices for the customer**, not profit for the owner. The business takes in the same dollars per meal as before (3 BU converted at 3x is $9). Owners still compete for workers, so **workers at private ESPs earn what a worker at a profit-sharing (community-owned) ESP earns**.

## How the model will do it (Claude's decisions)

1. **Price.** For BU spent at a private ESP, one BU buys as many essentials as the ESP's conversion rate in dollars (at 3x, 1 BU buys $3 of essentials). The ESP's dollar revenue per item is unchanged. No premium goes to owners.
2. **What this does to the money supply.** The Source (the Treasury that issues BU and pays conversions) pays out the full market value of the essentials the customer received, and nothing more. Under the old branch, the owners' premium was new money with no goods behind it. Under the correction, every converted dollar at a private ESP pays for goods actually delivered. That should reduce the price rises that the session-30 restudy found in the Adverse and Stress environments (23-51% a year). I will report what happens, not assume it.
3. **Participants need fewer BU for the same essentials.** BU they do not need expire and go back to the Source, as the session-30 financing already does. The monthly BU amount is not changed.
4. **Capacity still limits it.** A private ESP can only sell as much as it can supply. That limit is built in the creative-output step (d139: an ESP's octave cap follows its capacity), so the two steps are built together and tested together.
5. **Worker pay.** Participating workers at private ESPs receive the same profit-share amount per worker as participating workers at community-owned ESPs (your earlier rule: only participating ESP workers share). The model has no individual firms, so the report will say plainly that this pay is assumed to be funded by the extra sales that lower prices bring.
6. **A check on that assumption (shown, not hidden).** A second row caps the private-ESP pay rise at the profit margin on the added sales, using the published margin for retail, food service and utilities (BEA corporate profits by industry and Census Annual Retail Trade Survey sales; exact tables cited in the code). If the cap binds, the report says how far the design's pay match exceeds what added sales can fund.

## Switches and checks

- New switch `SURP_PRIV`: `'owners'` (the session-30 behaviour) or `'prices'` (the correction, used for v5.0). With `'owners'` every output is bit-identical to session 30 (proved by a full-output diff).
- No new random draws (the eight-draws-per-adult-year guarantee holds).
- Unit tests: (a) an ESP's dollar revenue per unit is the same in both branches; (b) at rate r, 1 BU buys r dollars of essentials at a private ESP; (c) no premium reaches owners under `'prices'`; (d) a participating private-ESP worker gets the same profit share as a community-ESP worker; (e) the margin-capped row never pays more than the margin on added sales.
- Restudy: seeds 1-500, paired, Reference, Adverse and Stress; poverty below the cost of living (basket), wealth poverty, days of basic living covered (BLEI), cost, work, prices, and participants against non-participants.

## What Duke should check

Only this: is "the premium becomes lower prices for BU customers, and private-ESP workers are paid like profit-share workers" what you meant? Everything else is a modelling decision recorded in `dev/DECISIONS.md`.

## Built (session 31, Oct 2, 2026), and one change from the plan above

Built as switch `SURP.priv = 'prices'` in `harness.js`, with 6 unit tests (`privUnitSuite`). With the old setting every output is identical to session 30 (full output of `testbed 10 release` in all three environments diffed).

**One change from point 6 above.** I planned to fund the workers' pay match from "the extra sales lower prices bring", with a row capping it at the profit margin on those sales. The model has a fixed basket: lower BU prices let participants buy the same essentials with fewer BU, so there are no extra sales to fund anything. Instead, the match comes out of the premium itself: a private ESP gives its workers the same fraction of its premium that a community ESP gives its workers (one third until there is enough community capacity, then 40%), and the rest becomes lower BU prices. Every worker who takes part then gets the same profit share, wherever they work, and every dollar stays accounted for. A second row gives the whole premium to lower prices (no match), so you can see the difference.

## Results: 500 paired runs, against session 30's build (`dev/runs/step14-priv-500-*.txt`)

| | Reference | Adverse | Stress |
|---|---|---|---|
| Below the cost of living, share of adult-years | **30.0% → 22.6%** | **51.7% → 44.5%** | 67.5% → 66.6% |
| Too little wealth at year 20 | **47.5% → 40.4%** | 87.0% → 90.4% (worse) | 89.3% → 91.3% (worse) |
| Real resources a year, adults who did not take part, against no programme | +$3,167 → −$1,071 | +$4,655 → +$1,380 | +$3,059 → +$422 |

In everyday words:

- **At Reference the correction helps on every measure.** Participants' BU go further at private businesses, so fewer people live below the cost of living and fewer end with too little savings.
- **In Adverse and Stress it lowers income poverty but slightly raises wealth poverty**, because the BU freed by lower prices go on to pay project work, which adds new money and prices rise a little faster.
- **Adults who do not take part lose the most.** Under session 30's build, they received part of the premium as business owners. Now they receive none of it, and at Reference they end up with slightly less real income than with no programme (−$1,071 a year), because prices still rise. This is what the corrected design implies in the model, and the page says so.
- I expected the correction to slow price rises (point 2 above). It did not: the model already counted the owners' dollars as new money, and the freed BU add a little more. I report this as it came out.
