# Step 3 report and checkpoint: how Compassionism pays for itself, and where the results stand

Oct 1, 2026 · plan step 3 (checkpoint after it) · Claude · 500 paired seeds, three environments · harness only

## What this step changes, in plain words

Until now the model paid for everything Compassionism costs with a flat contribution taken from every adult's wages: about 80-84% of wages at the reference settings. That is not your design. My reading of the Hub (in `03a-financing-reading.md`) is:

- a **Source** (the Treasury) issues the Basic Units;
- when anyone converts BU (an essential-service business, a project hirer, an ESP worker), the **Source pays the dollars** and keeps the conversion tax;
- expired BU return to the Source and go to projects;
- the Hub names no tax that pays the Source, so **what it pays out is new money**, except the part backed by new output (step 2).

The wage contribution remains only for what the Source does not pay: the community businesses' and housing's price cuts and housing appreciation (about 5% of wages).

## The result

Against no programme, same people. Poverty severity (FGT2; negative = less poverty), with the two checks every gain must pass: basket poverty (share of person-years below the cost of living) and wealth poverty (share with too little wealth at year 20).

| Paid for by the Source | Reference | Adverse | Stress |
|---|---|---|---|
| Poverty severity vs no programme | **−5.71** | **−14.14** | **−6.94** |
| Basket poverty: programme / no programme | 28.9% / 55.2% | 50.5% / 78.2% | 66.5% / 78.2% |
| Wealth poverty: programme / no programme | **87.5% / 54.7%** | **98.8% / 87.1%** | **98.0% / 87.1%** |
| Prices rise each year (from the programme) | **39.8%** | **51.1%** | **23.3%** |
| Price level at year 20 (1 = today) | 584 | 3,742 | 79 |
| Wage contribution | 5.4% | 8.0% | 3.8% |

Against the same design paid for by the wage contribution (step 2): poverty severity −21.4 / −25.6 / −10.5; basket poverty −46 / −30 / −14 points; wealth poverty **+9.5 / +14.2 / +9.3 points**.

**In everyday words: paid for by new money, Compassionism cuts the share of people living below the cost of living by roughly half at reference, because nobody pays an 80% wage contribution any more. But prices rise about 40% a year, and savings are wiped out: almost nine in ten adults end with too little wealth, against about five in ten with no programme.** The gain shows on income but not on wealth, so by the project's rule it is **not a confirmed gain**.

Every group (participants, non-participants, the poorest third, the richest third) has more real income than with no programme, and every group ends with more wealth poverty.

## Why prices rise

The Source pays out about $25,000 per adult a year at reference: the face value of the BU spent on essentials ($10,500) plus every conversion reward. It keeps $4,000 in conversion tax. Only about $1,000 is backed by output the model can count (step 2's capital and project hours). The rest, about $24,000 per adult a year, is new money. In the model's price rule, new money raises prices in proportion to its share of everyone's cash income, so about 40% a year.

The conversion tax the Source keeps equals 36% of the BU it issues at reference (34% Adverse, 51% Stress). The Hub's self-funding estimate (60-65% participation at a 12% tax) cannot be checked from the text; in this model the Source's payout is about 2.2 times the BU it issues, because each converted BU pays out several dollars.

## What would change it

- **If everything the Source pays were backed by new output (H1):** no programme inflation, and the gain is confirmed on all three measures. At reference: poverty severity −6.23, basket poverty 21.5%, wealth poverty 24.6% (against 54.7% with no programme); nobody is worse off on any test. In Adverse: −13.77, wealth poverty 59.3% against 87.1%. In Stress: −6.28, wealth poverty 77.3% against 87.1%. So the whole case rests on how much real output the conversions call forth. The model cannot measure that; H1 is the optimistic end, step 3's main row the cautious end.
- **If the essentials bought with BU counted as backed** (they were produced and sold), inflation roughly halves (23.5% a year at reference) and wealth poverty is 72.9%: still worse than no programme.
- **If every essential-service business split its premium** (no private owners): a little better on poverty severity (−0.9 to −2.7), a little worse on prices.
- **Your split versus today's stand-in:** today's stand-in, paid for by the Source, does slightly better on poverty severity (−6.62 at reference) than your split (−5.71); the difference is the private owners' share (step 1).

## Where the results stand (checkpoint)

1. **The ESP split (step 1)** sends most essential-service earnings to private owners in proportion to wealth. Under the wage contribution this made poverty deeper in every environment.
2. **The production side (step 2)** builds PTF capacity and counts some output, but the effect is small.
3. **Paying through a Source (step 3)** removes the 80% wage contribution, and with it most of the poverty the old financing caused. In its place it creates new money worth roughly half of everyone's cash income each year, which the model turns into very high inflation and lost savings.
4. **The decisive unknown** is how much new output conversion rewards produce. Between "none beyond what the model counts" and "all of it" lies the difference between wiping out savings and a large, confirmed reduction in poverty. No source in the Hub or the literature I have measures it; it is reported as a range, not settled.
5. **Model limits that matter here:** the price rule is simple (new money raises prices in proportion to income); nominal savings are not indexed; there is no central bank response and no interest. A real economy would respond (taxes, interest rates, output), and each response would change the answer.

I proceed on this reading to steps 4 onward, with the Source as the main row and the wage contribution and H1 as rows beside it. Duke, if the Source is meant to be paid for in some way the Hub does not describe (for example a tax, or a cap on what is converted), say so; it would change the main row more than any other choice.

## Exact commands and files

- `node harness.js testbed 500 fin ref`, `… adv`, `… st` (outputs in `dev/runs/step3-fin-500-{ref,adv,st}.txt`).
- Code: the testbed's financing mode `'source'` in `harness.js`, with the Source's ledger; tests: `srcUnitSuite`, 4 tests.
- Choices made: `dev/DECISIONS.md`, "Step 3".
