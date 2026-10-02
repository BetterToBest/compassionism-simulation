# Step 4 report: joining and leaving

Oct 1, 2026 · plan step 4 · Claude · 500 paired seeds, three environments · harness only

## What this step changes, in plain words

Until now each adult decided once, at the start, whether to take part, and kept that choice for 20 years. Now there is **open enrolment every year**: an adult joins when the Basic Units they would actually use are worth more than taking part costs them, and leaves when they are worth less. After joining, a person stays at least 2 years; they can rejoin later; there is no fee. Emergency enrolment during recessions stays as it was.

**What "what they would pay" means (Claude's reading of the design; a modelling assumption).** In the model a participant pays nothing that a non-participant does not, so read literally every adult would join. I read the cost of taking part (time, obligations) from the choices people make at the start: each adult's yearly cost is set so that, in year 0, exactly the adults who take part today take part (78% at reference, 40% in the Stress Test). After that, people join or leave only when the value of the BU to them changes: inflation, cost-of-living adjustments, price cuts, PTF membership. "Taking part costs nothing" (everyone joins) is shown beside it.

## What it does

On step 3's row (paid for by the Source), against the same row with fixed participation:

| | Reference | Adverse | Stress |
|---|---|---|---|
| Poverty severity | +0.00 | +0.01 | +0.00 |
| Participation in year 19 | 77.8% | 77.8% | 39.9% |
| Leaves per 100 adults over 20 years | 0.1 | 0.1 | 0.0 |

**In everyday words: with the Source paying, almost nobody changes their mind**, because the cost-of-living adjustment keeps the BU worth the same in real terms, even with prices rising 23-51% a year.

**If taking part cost nothing, everyone would join**, and poverty severity falls further: −1.10 at reference, −2.69 in Adverse, −6.56 in Stress. Basket poverty falls (−6.1 / −6.0 / −11.7 points), but prices rise faster (47% a year at reference instead of 40%), and wealth poverty rises a little (+1.5 / +0.0 / +0.6), so it is not a confirmed gain either.

**Where it does bite: under the wage contribution, when BU lose value.** In the Adverse Environment, inflation is 2% a year, below the 5% trigger for adjusting BU, so BU lose a third of their value over 20 years. About a quarter of adults leave, participation falls from 78% to 53%, and poverty severity rises by 5.6. In the Stress Test participation falls from 40% to 28%; poverty severity falls slightly (−0.88), because a smaller programme needs a smaller contribution.

## What it means

Open enrolment matters most where the BU lose value. Under your financing (the Source, with the cost-of-living adjustment) it changes little. The 5% inflation trigger for adjusting BU is worth a second look: below it, BU quietly lose value and people leave.

## Limits

- The cost of taking part is inferred, not measured; the "everyone joins" row bounds it.
- The minimum stay barely matters here (sweeps of 1 and 5 years give identical results), because people who leave rarely come back.
- Tables keep "participants" as the adults who took part in year 0, so the same people are compared in every row.

## Exact commands and files

- `node harness.js testbed 500 join ref`, `… adv`, `… st` (outputs in `dev/runs/step4-join-500-*.txt`).
- Code: `JOIN` in `harness.js` (off by default; earlier outputs byte-identical). Tests: `joinUnitSuite`, 4 tests.
- Choices made: `dev/DECISIONS.md`, "Step 4".
