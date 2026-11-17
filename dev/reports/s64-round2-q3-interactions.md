# The v5.9 model, question 3: do the flagged assumptions interact?

Nov 15, 2026. The 2 × 2 pairs of the v5.9 batch, read as frozen. Engine `104691f`, 500 adults, seeds 1-500, three environments, 20 and 40 years. Preregistered: research-update `prereg/2026-11-s63-round2-freeze.md` (Design, Source rows item 3 and financed rows item 3; Analysis). Tables: `dev/runs/s64-round2/s64-q3-pairs.md` (`python3 dev/tools/s64_tables.py`).

## In short

1. **On the Source rows, interactions are common but small.** Of 1,680 contrasts (28 pairs × 5 outcomes × 2 designs × 3 environments × 2 horizons), 427 have an interval that excludes zero, so the two assumptions do not simply add. Only 22 are material, and all 22 are median real wealth.
2. **No poverty outcome and no inflation figure on the Source rows has a material interaction.** The poverty effects of the main design are not built on a combination of assumptions that only matters together.
3. **The 22 material ones involve how wealth is held:** where new saving goes (portfolio or nominal assets), how far real assets follow inflation, the interest pass-through, and the spending share. The largest: the spending share with where new saving goes, which adds $340,800 to the full-coverage design's median-wealth gain at 40 years in Adverse beyond the two alone ($135,000 and $644,500).
4. **On the financed rows, interactions are the rule.** Of 5,544 contrasts, 3,125 exclude zero and 1,003 are material. Most involve the share the contribution must raise or how the rest is met, which interact with almost everything. These rows are never led with.

## What was measured

For each pair of assumptions A and B that the assumptions screen flagged: the effect at the main row (or the pair's base), with A alone moved, with B alone moved, and with both moved. The **interaction contrast** is (both) − (A alone) − (B alone) + (base): zero when the two effects add up exactly. Paired over seeds 1-500, with a 95% bootstrap interval. A synergy or antagonism is claimed only where the interval excludes zero (research rule 4); "material" uses the same thresholds as the headline (1 point; 1 point a year; 5% of the no-programme median wealth; 10 points of GDP for debt).

## The Source rows

| Pair | Contrasts with interval excluding zero (of 60) | Material |
|---|---|---|
| where new saving goes × the spending share (`rtNs` × `sc`) | 57 | 11, median wealth (6 full coverage, 5 opt-in design; +$18,500 to +$340,800) |
| the interest pass-through × the spending share (`rtPhi` × `sc`) | 45 | 6, median wealth (4 full coverage, 2 opt-in design; up to +$139,800) |
| how far real assets follow inflation × where new saving goes (`rtIx` × `rtNs`) | 46 | 5, median wealth (4 full coverage, 1 opt-in design; −$11,000 to −$66,500) |
| the other 25 pairs | 0-53 each | 0 |

Every pair's full count is in the tables. Thirteen of wage indexation's 14 pairs have no contrast excluding zero at all: at full backing there is almost no programme inflation for wages to follow. The fourteenth, with the price rule's persistence (`prR`), has 51 contrasts excluding zero and none material.

## The financed rows

The pairs with the share the contribution must raise (`gvSh`) and how the rest is met (`fin`) carry most of the material contrasts, on every outcome. An example: the bargaining pass-through with how the rest is met adds 1.9-2.9 points to the full-coverage design's basket poverty in Adverse. These say that the financed rows' results depend on the financing set-up jointly, not one assumption at a time; question 5's report gives the main financed rows.

## Unfavourable and null results

- The negative wealth contrasts (`rtIx` × `rtNs`) mean that with real assets only half-following inflation and new saving in portfolios, the full-coverage design's wealth gain is smaller than the two alone suggest, by up to $66,500 (Adverse, 40 years).
- 1,253 of the 1,680 Source contrasts are null (interval includes zero), including every one on inflation.

## What these figures do not cover

The pairs are the ones the assumptions screen flagged on Reference and Adverse at 20 years and 40 seeds; pairs it did not flag were not run. Each pair is tested at one end of each assumption (Amendment 1), not every combination. Wealth figures rest on today's price rule.
