# Step 9 report: public costs of poverty avoided

Oct 1, 2026 · plan step 9 · Claude · 500 paired seeds, three environments · harness only

## What is counted, and from where

**Homelessness**, including the health care and justice costs that come with it. The model already estimates how many adults are unhoused: it starts from the HUD 2025 point-in-time count (22 per 10,000) and moves with housing distress (people whose income and savings fall short of their costs). Each unhoused person-year is costed at two sourced ends, in 2025 dollars:

- **Low, $10,462:** emergency-shelter cost only, $581 a month for an individual (Spellman and others, *Costs Associated with First-Time Homelessness for Families and Individuals*, HUD and Abt Associates, 2010).
- **High, $100,608:** every public cost of homeless residents in Santa Clara County, $520 million a year (health care 53%, justice 34%), over the 7,631 people counted homeless there in January 2013 (Flaming, Toros and Burns, *Home Not Found*, Economic Roundtable, 2015). This end is high because it counts the costs of everyone homeless at any point in a year against a one-night count, and a few very costly people dominate.

**Not counted:** health care and crime among adults who are poor but housed. I found no primary source giving a causal public cost per poor adult-year. Leaving them out understates the costs avoided; it does not overstate them.

## Results

| Per adult a year | Reference | Adverse | Stress |
|---|---|---|---|
| Unhoused share of person-years: programme / no programme | 0.26% / 0.47% | 0.45% / 0.61% | 0.58% / 0.61% |
| Public cost avoided, low to high | $22 to $212 | $17 to $161 | $3 to $29 |
| Programme cost | $27,633 | $26,103 | $10,468 |
| If every Source dollar were backed by output: avoided | $29 to $281 | $27 to $261 | $11 to $101 |

**In everyday words: Compassionism roughly halves homelessness at reference and cuts it by a quarter in Adverse, but the public money this saves is small next to what the programme costs**, under 1% of it even at the high end. The case for the programme cannot rest on savings in homelessness services.

## Limits

- Only homelessness is costed.
- Both cost figures are from single places (Des Moines; Santa Clara County) and from 2009-2013, brought to 2025 prices.
- The model's homelessness figure is an overlay on housing distress, not a model of who becomes homeless.

## Exact commands and files

- `node harness.js testbed 500 avoid ref`, `… adv`, `… st` (outputs in `dev/runs/step9-avoid-500-*.txt`). Constants and sources: `AVOID_HOMELESS` in `harness.js`. Test: `avoidUnitSuite`.
