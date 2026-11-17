# The v5.9 model, question 5: the designs paid for by a contribution, the rest borrowed

Nov 15, 2026. The financed rows of the v5.9 batch, read as frozen. **By Duke's decision, these rows are carried beside the main rows and never led with.** Engine `104691f`, 500 adults, seeds 1-500, three environments, 20 and 40 years. Preregistered: research-update `prereg/2026-11-s63-round2-freeze.md` (Design, financed rows; decision rule 5; Amendment 3). Results: compassionism-sim-results `r2-m-*-104691f/` (the financed main rows, full precision) and `r2-f-*-104691f/` (their curves). Tables: `dev/runs/s64-round2/s64-q5-financed.md`, and the financed section of `s64-q2-curves.md`.

## In short

1. **What the rows are.** No new money and no assumed backing: the programme is paid for by a contribution, and what the contribution does not raise is borrowed by the government. The full-coverage design, built to meet NEEC's criterion C2.2, is paid by a contribution on all money income (rate capped at 90%); the opt-in design by a flat contribution on wages. Both run without the weighted top tail (its weights are not read by the contribution's bases), and that absence is stated with every figure here.
2. **The rates are very high.** The full-coverage design needs a mean contribution of 63-77% of all money income; the opt-in design 46-71% of wages in Reference and Adverse, 15-18% in Stress (where fewer take part).
3. **The debt stays manageable at the main financed rows and falls over time.** The deficit is 0-6% of the payout; debt is 2-25% of GDP at year 20 (median) and 0-14% at year 40. It passes GDP within the run in no more than 4% of seeds; no main financed row is "unsustainable" by rule 5.
4. **Paid this way, the poverty effects are much smaller and partly reversed.** The full-coverage design still lowers basic living by 17-20 points, but basket poverty by only −17.5 to +0.6 points and wealth poverty by 0.3-6.9 points, and it lowers median real wealth by up to $28,000 at 20 years. The opt-in design lowers basic living by 1-6 points but **raises basket poverty by up to 9.6 points** (Reference and Adverse, 20 years) and lowers median real wealth by up to $49,000.
5. **Nearly every financed result is fragile across its curve** (46 of 48 poverty and wealth curves; the exceptions are the opt-in design's basic-living effect in Reference) (question 2's report): how the contribution is set up (its base, the share it must raise, how the rest is met, the cap) reverses the effects at some readings in every cell, and debt passes GDP within the run at 32-39 of the 117 readings.

## The main financed rows (rate, deficit and debt; median over seeds for debt)

| Design | Environment | Years | Contribution rate | Deficit (% of payout) | Debt at the end (% of GDP) | Debt passes GDP within the run (share of seeds) |
|---|---|---|---|---|---|---|
| Full coverage (all money income, cap 90%) | Reference | 20 | 68.0% | 1.2 | 14.6 | 0% |
| | Reference | 40 | 62.6% | 0.0 | 0.0 | 0% |
| | Adverse | 20 | 76.4% | 2.9 | 25.3 | 0% |
| | Adverse | 40 | 77.1% | 1.3 | 13.9 | 0% |
| | Stress | 20 | 74.3% | 2.5 | 18.5 | 0% |
| | Stress | 40 | 75.2% | 1.1 | 9.5 | 0% |
| Opt-in design (wages) | Reference | 20 | 70.8% | 4.7 | 22.4 | 3% |
| | Reference | 40 | 63.6% | 6.4 | 10.5 | 4% |
| | Adverse | 20 | 58.9% | 3.1 | 7.5 | 0% |
| | Adverse | 40 | 46.1% | 0.9 | 0.0 | 0% |
| | Stress | 20 | 17.7% | 2.3 | 2.3 | 0% |
| | Stress | 40 | 15.4% | 0.8 | 0.1 | 0% |

Without the programme the government account carries no debt. The rest of the payout is met entirely by borrowing at these rows (the share not raised by contribution or borrowing is 0). The opt-in design's deficit in Reference at 40 years has a wide interval (1.5 to 15.9% of the payout): a few seeds run large deficits.

## The five headline outcomes on the financed main rows (points unless stated)

| Design | Environment | Years | basic living | basket poverty | wealth poverty | median real wealth | programme inflation |
|---|---|---|---|---|---|---|---|
| Full coverage | Reference | 20 | −16.9 | −10.8 | −0.3 | −$28,000 | +0.14 |
| | Reference | 40 | −17.8 | −17.5 | −6.9 | −$6,300 | +0.06 |
| | Adverse | 20 | −17.3 | −1.3 | −0.3 | −$20,200 | +0.16 |
| | Adverse | 40 | −20.3 | −8.0 | −3.9 | +$12,200 | +0.07 |
| | Stress | 20 | −17.4 | **+0.6** | −0.7 | −$17,200 | +0.13 |
| | Stress | 40 | −20.1 | −3.5 | −3.6 | +$7,600 | +0.07 |
| Opt-in design | Reference | 20 | −5.1 | **+9.5** | +0.2 | −$35,500 | +0.05 |
| | Reference | 40 | −5.8 | **+2.2** | −0.3 | −$49,200 | +0.04 |
| | Adverse | 20 | −2.3 | **+9.6** | +0.3 | −$22,100 | +0.00 |
| | Adverse | 40 | −1.4 | **+5.2** | +0.4 | −$17,100 | +0.00 |
| | Stress | 20 | −1.2 | +0.4 | −0.6 | −$2,000 | +0.00 |
| | Stress | 40 | −1.0 | 0.0 | −0.6 | +$1,400 | +0.00 |

Every interval is in the tables. Basket poverty rises under the opt-in design probably because the contribution on wages takes more from working households near the basket line than the payout gives them (not traced here). Materiality: wealth poverty changes under 1 point in most cells are "no material change"; so is programme inflation everywhere.

## Unfavourable and null results

All of point 4 above, and: the financed rows' effects are fragile at every curve; debt passes GDP within the run at about a third of the preregistered readings; the mean contribution rates of 46-77% would be a very large change in how households are taxed.

## What these figures do not cover

The financed rows run without the weighted top tail, so the top of the wealth distribution is less extreme than on the main rows. Backed share 0: no output is assumed to match the payout. The government account has no central bank and one interest rule. The seed intervals do not cover the financing set-up, which question 2's curves show matters most.
