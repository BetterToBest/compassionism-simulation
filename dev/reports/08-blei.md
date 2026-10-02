# Step 8 report: BLEI leads

Oct 1, 2026 · plan step 8 · Claude · 500 paired seeds, three environments · harness only

## What changed

Every result table now opens with **BLEI, the number of days of basic living a person's resources cover**: 20% of their savings, plus a share of a month's wage, plus a month of the BU they use, divided by the daily cost of basic living (in today's prices). Two readings sit side by side:

- **Your BLEI** (the BLEI paper's definition, the page's): participants count 20% of a month's wage instead of 12%, and participants living in community housing face a lower daily cost.
- **Design-neutral**: the same rules for everyone (12%, the ordinary daily cost) plus one month of whatever regular support a design gives.

"BLEI poverty" is the share of person-years below 30 days of basic living.

## Results: all mechanisms, paid for by the Source

| | Reference | Adverse | Stress |
|---|---|---|---|
| Your BLEI, median days at year 20 (no programme) | 126 (41) | 24 (3) | 6 (3) |
| Your BLEI poverty, change vs no programme | −21.8 points | −19.2 | −3.0 |
| Design-neutral BLEI poverty, change | −16.6 | −11.2 | −0.9 |
| If every Source dollar were backed by output (your BLEI) | −28.6 | −28.4 | −10.6 |

**In everyday words: on both readings, fewer people are within a month of not covering basic living, in every environment**: about a fifth fewer at reference and in Adverse, a little fewer in the Stress Test. The two readings agree in direction here; the design-neutral one is about a quarter smaller.

**Where they disagree:** for the old row paid for by a wage contribution, your BLEI shows a gain (−7.7 points at reference) and the design-neutral reading a loss (+10.5), because your definition credits participants with a larger share of their wage and the neutral one counts the wage contribution's bite through savings only. That is why the neutral reading has to stay beside yours on the page.

## Confirming design default 8

The results support leading with your BLEI, provided the design-neutral reading sits right beside it with the same prominence. For the main row both tell the same story; where they do not, the page will say so in one sentence. The precomputed 500-seed panel will show both.

## Exact commands and files

- `node harness.js testbed 500 blei ref`, `… adv`, `… st` (outputs in `dev/runs/step8-blei-500-*.txt`). Every later section prints the same BLEI table first.
