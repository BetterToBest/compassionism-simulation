# Who pays the programme, and what a year's rising prices cost households (S68, part 1)

Nov 14, 2026. Pilot: seeds 1-100, 500 adults, 20 years, three environments, engine `e03aa73` (clean worktree). A pilot is a mechanism check, not a result; the frozen 500-seed batch decides. Preregistered before the build and before any run (research-update `prereg/2026-11-s68-financing-identity.md`, with one dated amendment before the pilot). It answers findings 1 and 4 of the Nov 13 audit (research-update `audits/2026-11-13-simulation-audit.md`). Tables: `dev/runs/s68-financing/tables.md`; per-seed results: compassionism-sim-results `s68-financing-e03aa73`.

## In short
1. **The question.** When a contribution on wages pays for the programme, its rate is capped at 90%. Until now, whatever the capped rate could not raise was paid by no one in the engine's books. The progressive and land-value taxes already counted their shortfall as new money; the flat contribution, and the taxed part of the `hybrid` and Source readings, did not.
2. **A books check for every way of paying.** Each year the engine can now check that the programme's payout equals taxes raised, plus new money, plus output that backs it, plus a stated unpaid part, less any surplus. It holds in every reading (largest error about 10⁻¹⁶ of the flows). The unpaid part is now a printed line (`finGap`, `finGapSh`), and a new option (`fx: {fin: 'money'}`) counts it as new money, as the other taxes already do. Everything is off by default; every published figure is unchanged.
3. **The C2.2 design paid by a flat contribution is not paid for.** Its rate averages 84% of wages and sits at the cap by year 20 in all 100 seeds in every environment. 38% (Reference), 51% (Adverse) and 45% (Stress) of its cost is unpaid. Its "0.1 points of inflation a year" comes from that gap. Counting the gap as new money gives inflation of 21%, 33% and 29% a year. Basket poverty still falls, by 13.0, 17.6 and 8.6 points against no programme (against 17.1, 28.0 and 23.8 with the gap unpaid). Wealth poverty at year 20 rises by 37, 61 and 62 points (on the frozen engine's all-cash wealth, which overstates erosion). Hours worked fall by 24-28% against the no-programme run. This confirms the audit's figures at 100 seeds.
4. **The release design and C2.2 under the Source are paid for.** The unpaid part of their taxed transfers is 0.02-0.18% of payout. By the preregistered rule (below 0.5% everywhere) they are carried unchanged.
5. **Two smaller gaps the audit did not measure.**
   - The release design paid wholly by the flat contribution leaves 4.9-6.9% unpaid.
   - C2.2 under `hybrid` leaves 3.2-3.8% unpaid.
   - Counting those gaps as money adds 0.7-3.4 points of inflation (release) and 1.4-1.6 points (`hybrid`).
   - In Adverse, the release design under the flat contribution then raises basket poverty by 9.7 points against no programme, against 3.3 points with the gap unpaid.
6. **Households pay more than the books say during a year of rising prices.** On the quarterly count of today's price rule, prices average 6-15% above the year's opening level during the year, while households are charged opening prices. Counting each year's costs at the year's average level:
   - The release design's cut in basket poverty is 2.2 (Reference), 3.7 (Adverse) and 2.5 (Stress) points smaller.
   - C2.2's cut (under the Source) is 0.7-1.4 points smaller.
   - Every effect keeps its sign.
   - By the preregistered rule (1 point or more), S63 carries this reading beside every basket-poverty headline.
7. **The per-run reset.** Module-level state that a row could inherit from the previous run (the production side's yearly record and six others) now starts empty in every testbed run. The leak S60 reported was not reproduced on the rows tried; a run-order unit test now checks every output of a no-programme row against the same row run alone.

## What was built (engine; every part off by default, guard test identical)
- **The financing identity** (`ACCT` id `fin`; MODEL_SPEC 11), `finStep`. Payout at face value under the reading's timing = taxes + new money for the payout (`U` less the floor's unmatched part and the wage bonus, which are new money in every reading) + matched or backing output + the unpaid part − surplus. The unpaid part is `max(0, need − tax)` where a capped contribution pays `need`, and, under `'none'`, the transfers and price cuts it leaves unfinanced by definition.
- **`fx.fin`** (MODEL_SPEC 13.2; not part of `fx: true`, so the frozen batch reproduces): `'report'` adds `FIN_KEYS` and moves no figure; `'money'` adds the unpaid part to the year's new money under the flat contribution, `hybrid` and the Source; `'debt'` is reserved for S72 (government borrowing) and refused.
- **`o.wy`** (MODEL_SPEC 13.2a; reporting only): each adult-year's cost of living and its reference times `exp(avg)`, the within-year level over the opening level behind `prAvg`; basket poverty and its depth recounted (`WY_KEYS`). It equals the published measure when the year is not split.
- **Per-run reset** of `FWS`, `PJS`, `ESS`, `SPS`, `PDS`, `JNS`, `HCS` at the start of each testbed run.
- **Tests:** 8 in `s68UnitSuite`. 'report' moves nothing; the identity holds on all seven readings with 'report' and 'money'; the check changes nothing; 'money' leaves no gap for the three capped readings and changes nothing for the others; 'debt' is refused; `wy` is reporting only and equals the published measure on an unsplit year; on the quarterly count `wyAvg` equals `prAvg`; and run order. Unit 336, validate, domtest 153 and the guard test pass; the lineage is linked.

## The pilot (rows and readings as preregistered)
The frozen row (today's safety net, CPS earnings), round-2 switches off. (A) No programme; the release design and C2.2 under the Source; C2.2 under the flat contribution and under `hybrid`, each with the gap unpaid ('report') and as new money ('money'); the release design under the flat contribution, both ways. (B) No programme, the release design and C2.2 under the Source, on the quarterly count of today's rule (`pr: {q: 4, k: 1, a: 0, r: 0, h: 0, rs: false}`), with `o.wy`. Paired differences with 95% intervals, unadjusted.

| C2.2 under the flat contribution | Reference | Adverse | Stress |
|---|---|---|---|
| Mean rate, % of wages | 83.7 | 83.8 | 83.4 |
| Seeds at the cap in year 20 | 100 of 100 | 100 of 100 | 100 of 100 |
| Unpaid, % of payout (range over seeds) | 38.1 (31.7-43.4) | 51.4 (47.2-57.3) | 44.8 (40.1-51.9) |
| Inflation, % a year: gap unpaid / gap as new money | 0.08 / 21.4 | 0.11 / 33.2 | 0.10 / 28.9 |
| Basket poverty against no programme, points: unpaid / as money | −17.1 / −13.0 | −28.0 / −17.6 | −23.8 / −8.6 |
| Wealth poverty at year 20 against no programme, points: unpaid / as money | −15.2 / +36.7 | −22.9 / +61.3 | −17.4 / +62.1 |
| Hours against no programme, %: unpaid / as money | −19.2 / −24.4 | −19.6 / −27.2 | −22.1 / −28.4 |

| The programme's cut in basket poverty, points | Reference | Adverse | Stress |
|---|---|---|---|
| Release design, published / at within-year prices | 16.7 / 14.5 | 22.6 / 18.8 | 8.7 / 6.2 |
| C2.2 (Source), published / at within-year prices | 24.6 / 23.9 | 35.3 / 34.2 | 34.5 / 33.1 |
| Within-year level over opening, release / C2.2 | 1.108 / 1.126 | 1.128 / 1.147 | 1.059 / 1.153 |

Every interval on the changes in this table excludes zero (tables file).

## Decision rules (fixed before the pilot), applied
- (A) The flat contribution and `hybrid`: no row is carried by S63 without `fx.fin` set; S63 chooses between 'money' and S72's 'debt' with S72's frontier in hand (D23 stands: the Hub does not lead with the financed row until then). The release design and C2.2 under the Source: unpaid below 0.5% of payout in every environment (largest 0.18%), so they are carried unchanged.
- (B) The within-year reading moves the release design's effect by 2.2-3.7 points (1 point or more), so S63 carries `wy` beside every basket-poverty headline.

## Limits
- Wealth poverty under the gap-as-money reading uses the frozen engine's all-cash wealth (S59 showed it overstates erosion); `rt` was not run here.
- At rates of 84-90% the labour response is the engine's one elasticity, measured on much smaller changes; avoidance, informal work and shifting effort to conversion income (outside the contribution's base) are not modelled.
- `wy` scales costs by the general level; spending, saving and wealth are still at opening prices, and outside inflation (Adverse, Stress) is not split within the year in either run, so the no-programme run's within-year level is 1.
- The new money for the gap is a reading, not a design. Borrowing (S72) and a wider base (S72's frontier) are the other ways to pay.
- Adverse and Stress share one no-programme run (as the audit noted).

## For later steps
- **S72:** build `fx.fin 'debt'` and the frontier; D21's row (C2.2, flat contribution) is one point on it. The figures above are its two ends: no payer for 38-51% of the cost, or 21-33% inflation.
- **S63:** carry `wy` beside every basket-poverty headline; no row under the flat contribution or `hybrid` without `fx.fin`; the Source rows unchanged.
- **S68, remaining items:** the spec and plain-names table (item 1); pairwise on-together tests (item 3, with the pairs listed in item 7); the packet (item 4); the 10,000-adult checks.
