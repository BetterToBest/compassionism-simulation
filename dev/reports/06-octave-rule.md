# Step 6 report: how an adult moves up an octave

Oct 1, 2026 · plan step 6 · Claude · 500 paired seeds, three environments · harness only

## What the rule is (kept as it is, labelled plainly)

Each year a participant below the top octave may move up one octave. The chance grows with their **financial breathing room**: monthly income plus BU, less the basic cost of living and the share of income lost to rent, interest and fees. The more room, the likelier the step up. This is the model's reading of "advancement gated by financial stability", and it stays the default. On the page it will be described in those words.

## The test: slower advancement

As your design default asked, I tested a cap: at most one octave every 2, 3 or 5 years.

| Against today's rule (Source financing) | Reference | Adverse | Stress |
|---|---|---|---|
| One octave per 3 years: poverty severity | −0.00 | +0.02 | +0.01 |
| … basket poverty (points) | +0.16 | +0.42 | +0.13 |
| … wealth poverty (points) | +0.10 | −0.01 | −0.00 |
| One octave per 5 years: poverty severity | +0.01 | +0.08 | +0.03 |
| Prices at year 20, today's rule / one per 5 years | 582 / 523 | 3,715 / 3,504 | 79 / 75 |

**In everyday words: slowing octave advancement barely changes poverty.** Most participants reach the top octaves within the 20 years either way (the average at year 20 is about 6 of 6 today and 4.2 with one per 5 years). Slower advancement means slightly smaller conversion rewards, so slightly less new money (prices rise a little less) and slightly more basket poverty. Under the wage contribution, one octave per 3 years is a little worse at reference and in Adverse (+0.48, +0.39) and a little better in Stress (−0.09).

## What it means

The octave rule is not what drives the results; financing and the split are. Advancement in the model is close to automatic for anyone with some breathing room, which is a limit worth stating on the page: the model does not represent the community assessment of quality or contribution that the Hub describes.

## Exact commands and files

- `node harness.js testbed 500 oct ref`, `… adv`, `… st` (outputs in `dev/runs/step6-oct-500-*.txt`).
- Code: `OCT` in `harness.js` (off by default). Test: `octUnitSuite`.
