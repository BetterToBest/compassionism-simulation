# The price level in an outside engine: BeforeIT.jl with a Basic Unit (S39)

Part 1, Nov 8, 2026: the design, the engine side, the outside engine built and checked, the runs dispatched. Part 2 (next session) adds BeforeIT's results. Preregistration: research-update `prereg/2026-11-s39-outside-crosscheck.md`. Code: compassionism-sim-results `runner/jobs/s39-path.js`, `runner/jobs/beforeit.js`, `runner/jobs/beforeit/`. No engine change.

## In plain words
The Compassionism Simulation's prices rise fast under the programme. Under the C2.2 design (automatic BU at the cost of food, housing and medical care) the price level is about 410 times its starting level by year 20 in the Reference environment, and the figure is the same at 500 and at 50,000 adults (study A). This step asks an outside, published model of a whole economy what it does with the same money.

The engine's reason for the rise is one rule. Each year it counts the money the programme pays out that is not matched by new output, divides it by the year's cash income, and raises the general price level by that share. It is the quantity theory of money with a pass-through of 1, and the engine's own notes call it "a logged placeholder, swept 0.25-1". Under C2.2 the Source pays about $61,500 per adult a year in today's dollars (BU and conversion pay), the engine counts about 37% of it as matched by new output, and the rest, about $38,700, is new money: 30% to 50% of the year's cash income, every year. So prices rise by about that much each year.

The outside model is BeforeIT.jl, the Bank of Italy's open implementation of Poledna, Miess, Hommes and Rabitsch (2023), the first agent-based model of a whole economy to forecast as well as the standard models. It is calibrated to Austria and can run with one agent for every person and every firm (8.9 million agents). We add a module that pays every person the same share of household income as new money, year by year, as the engine's C2.2 design creates, and compare BeforeIT's price level with its own run without the payout, seed by seed.

What we already know from building it (before any study run, and stated in the preregistration so it is not read as a finding): BeforeIT's firms set prices from their costs and the inflation they expect, not from excess demand. Extra spending raises output, wages (up to a limit) and imports, and demand that cannot be met stays in bank accounts. In a one-seed pilot at 1:1000 scale, paying 10% or 35% of household income a year as new money left the price level within about 8% of the no-payout run over 20 years, while government debt grew without limit. If the study confirms this, the two engines disagree by a factor of hundreds, and the disagreement comes from one assumption each: the engine's quantity-theory rule against BeforeIT's cost-based prices. Neither engine has been shown right about an injection this large (30-50% of income a year), which is far outside anything either was built or tested for. Part 2 reports the figures, whichever way they point.

## 1. The engine side (study A's rows, year by year)
Study A kept the price level only at years 10, 20 and 40 (`pLev10`, `plv_19`, `plv_39`), though the run manifest lists `plv_0` to `plv_39` for this step. `s39-path.js` reruns study A's rows on the frozen engine (`ce8d030`) and copies the year path each run already returns: the general price level (`PG`), the full price level (`full`, the basket's cost over its starting cost), the basket index, the unmatched money (`U`) and the year's cash income (`Y`: wages, conversion pay and Social Security). Every row's last-year price level equals study A's, seed by seed (seeds 1-500, three environments; the sizes script stops otherwise). Results: compassionism-sim-results `s39-path-ce8d030/`.

| Environment | Design | Unmatched money, share of cash income (mean of years) | year 1 | year 20 | Payout matched by output | General price level after 3 years | after 19 years | Full price level after 3 years | after 19 years | Yearly rate (full level) |
|---|---|---|---|---|---|---|---|---|---|---|
| Reference | C2.2 | 36.9% | 30.9% | 32.2% | 32.3% | 2.59 | 408 | 2.64 | 415 | 37.2% |
| Reference | release | 31.4% | 16.1% | 30.6% | 8.7% | 2.04 | 180 | 2.07 | 183 | 31.4% |
| Adverse | C2.2 | 43.8% | 30.9% | 46.5% | 30.5% | 2.64 | 982 | 2.85 | 1461 | 46.6% |
| Adverse | release | 37.9% | 16.1% | 44.5% | 8.1% | 2.06 | 425 | 2.22 | 627 | 40.2% |
| Stress | C2.2 | 45.8% | 31.1% | 51.8% | 25.4% | 2.69 | 1266 | 2.90 | 1883 | 48.5% |
| Stress | release | 16.6% | 6.1% | 19.4% | 2.6% | 1.40 | 18 | 1.49 | 27 | 18.7% |

Price levels: means over seeds (1 before any payout). The engine sets a year's price level from the new money of the years before it, so its level in year index k (the year path's entry k) is the level after k years of payout; the run's last entry is after 19 years. The yearly rate is the geometric mean over those 19 years, from the mean log.
The engine pass-through is 1 for the general level by construction (PG grows by exactly U/Y each year); the full level adds the essentials rule.

- Adverse, C2.2: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.08, after 19 years 1.06; general level 1.00, 1.00.
- Adverse, release: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.10, after 19 years 1.06; general level 1.00, 1.00.
- Reference, C2.2: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.02, after 19 years 1.00; general level 1.00, 1.00.
- Reference, release: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.02, after 19 years 1.00; general level 1.00, 1.00.
- Stress, C2.2: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.08, after 19 years 1.06; general level 1.00, 1.00.
- Stress, release: pass-through, ln(price level) / sum of ln(1 + U/Y) over the years paid: full level after 3 years 1.20, after 19 years 1.13; general level 1.00, 1.00.

In Adverse and Stress the full level also carries the environment's own price path (1.46 by year 20 without the programme), which is why its pass-through there is above 1. Tables: `dev/runs/s39-crosscheck/tables.md` (tool `dev/tools/s39_crosscheck.py`).

Facts the rerun establishes:
- In these rows U is exactly the Source's payout less the part matched by output (`srcPay - srcM`, to the dollar per adult-year), and the general price level grows each year by exactly U/Y.
- The conversion tax the Source keeps (about $13,500 per adult-year in C2.2 Reference) does not reduce U. If the tax takes money back out of circulation, the rule overstates the new money by that amount; if the Source spends it again, it does not. This is an open engine question for the next engine round (preregistration rule 4), not a change here.
- The price level does not depend on population size (study A: 500 to 50,000 adults agree within Monte Carlo error), because the rule reads only ratios.

## 2. The outside engine and the module
- **BeforeIT.jl 0.6.0**, Julia 1.11.5, every package fixed by the committed `Manifest.toml`. Austria, 2010Q1 calibration. Nothing in BeforeIT's package code is edited: the module (`runner/jobs/beforeit/s39.jl`) overloads its social benefit rule and its central bank rule, and acts through its shock hook, the extension routes its documentation shows.
- **Full scale.** The packaged Austria has one agent per 1,000 people. BeforeIT's own calibration code scales a country by multiplying the numbers of people and firms and dividing the amounts per agent (output and wages per worker, benefits per person); the module applies that rule to the packaged country. At 1:1 there are 8.9 million agents; a quarter takes about 100 s on one thread (5.5 GB).
- **One thread.** With several threads BeforeIT does not repeat a seed (its goods market is matched in parallel); on one thread it does (checked). Every run is single-threaded so payout and no-payout runs are paired seed by seed.
- **The payout (Basic Unit and conversion together).** Each quarter: the year's share times the households' nominal income of the previous quarter (payouts included, as the engine's Y includes conversion pay), the same amount to every person, through BeforeIT's per-person benefit, so it is government spending. BeforeIT's households all spend the same share of their income, so who receives it does not change total demand; the BU and conversion pay are therefore one flow here.
- **New money.** The payout adds to the government's deficit. BeforeIT keeps no separate money and bond accounts: the deficit ends as household deposits, the closest it has to the engine's new money.
- **Readings beside it.** The whole payout as new money (gross: none matched by output); the payout financed by an income-tax surcharge; a central bank that answers Austria's own inflation (a national central bank, as in the US) instead of the euro area's; fixed doses of 1%, 3%, 10% and 30% of household income for the pass-through; the Adverse and Stress environments' amounts (only the amounts: BeforeIT's economy stays Austria's); and 1:1000 beside 1:1.
- **Horizon.** 80 quarters (20 years). BeforeIT is built and validated for 12-quarter forecasts; beyond that its no-payout run drifts (in the pilot, unemployment falls to zero after year 5). Both readings are reported; the 20-year one carries this caveat.

## 3. Runs (dispatched Nov 8, 2026)
All on GitHub Actions (free), the run-study workflow, engine commit `ce8d030`, job `beforeit.js`; results commit themselves to compassionism-sim-results with run.txt, SHA256SUMS and a `DONE` file.

| Study | What | Arguments | Runs | Shards | Workflow run | Folder |
|---|---|---|---|---|---|---|
| dry-s39 | dry run: 13 scenarios, 1:1000, 4 quarters | `--scale=1 --quarters=4 --reps=1`, runs 1-13 | 13 | 1 | 42510677223 (shard passed in 3.5 minutes) | `dry-s39-ce8d030` |
| s39-full | full scale (1:1, 8.9 million agents), 80 quarters, seeds 1-5 per scenario | `--scale=1000 --quarters=80 --reps=5`, runs 1-65 | 65 | 65 | 42511582006 | `s39-full-ce8d030` |
| s39-k1 | 1:1000, 80 quarters, seeds 1-100 per scenario | `--scale=1 --quarters=80 --reps=100`, runs 1-1300 | 1,300 | 13 | 42511585190 | `s39-k1-ce8d030` |

Run index i is scenario (i - 1) div reps (base-ea, base-dom, c22-ref-ea, c22-ref-dom, c22-adv-ea, c22-st-ea, rls-ref-ea, c22-ref-gross-ea, c22-ref-tax-ea, dose01-ea, dose03-ea, dose10-ea, dose30-ea) on BeforeIT seed (i - 1) mod reps + 1. Part 2 runs `python3 dev/tools/s39_crosscheck.py --engine RESULTS/s39-path-ce8d030 --full RESULTS/s39-full-ce8d030 --k1 RESULTS/s39-k1-ce8d030 --out dev/runs/s39-crosscheck` and writes sections 3-4 of the findings from its tables, by the preregistration's decision rules.

## 4. What a US calibration would take
BeforeIT's calibration (`get_params_and_initial_conditions`) reads a country's quarterly national accounts, a 62-industry input-output table, industry output, wages, employment, firm counts and fixed assets, the household, firm, bank and government balance sheets, government spending and benefits by type, and a "rest of the world" (for Austria, the euro area, whose central bank sets Austria's interest rate). For the United States:
- **Data, all public:** BEA's quarterly national accounts and price indexes; BEA's input-output Use and Make tables (71 industries, mapped to BeforeIT's 62 or the model re-dimensioned; FIGARO, which BeforeIT uses for Europe, also has a US table); BEA GDP by industry (output, compensation, employment) and fixed assets; Census SUSB or BDS for firm counts by industry; BLS for unemployment and the inactive population; the Federal Reserve's Financial Accounts (Z.1) for deposits and loans of households, firms and banks; BEA and Treasury government accounts for Social Security, unemployment insurance and other transfers, debt and interest; FRED for the policy rate. The calibration package CalibrateBeforeIT.jl does this for the 27 EU countries from Eurostat; a US version means writing the same mapping from US sources.
- **Model changes:** the US is not a small economy inside a currency union. The rest of the world becomes a world aggregate, and the central bank must answer US inflation and growth (this study's domestic closure is that rule). Imports are a smaller share than Austria's, so less of any demand leaks abroad.
- **Scale:** about 335 million people and 6 million employer firms. At about 0.6 KB per agent, full scale needs about 200 GB of memory, beyond GitHub's free runners (16 GB). Options: run at 1:20 or less (BeforeIT's own calibrations use 1:1000 and 1:2000; Q8 of this study measures what scale changes), or a large-memory machine, which costs money (Runpod: a ledger decision).
- **Validation:** BeforeIT's forecasting record is for Austria and Italy. A US calibration would need its own out-of-sample check before its figures could stand beside the engine's.
- **Effort:** the data mapping and checks are about three to five sessions; the runs at 1:20 fit the free runners.
- **What it would not change:** BeforeIT's price rule. A US calibration changes the size of the leakages (imports) and the central bank's answer; it does not give BeforeIT's firms a price response to excess demand. Whether that response exists at the engine's scale of new money is the real open question, and no calibration of either engine settles it.

## 5. Limits
- The two engines model different economies (the US through 500 to 50,000 adults; Austria through every person and firm). The match is the size of the new money relative to household income, year by year; nothing else is matched.
- The payout is far outside both engines' tested range (30-50% of income a year as new money).
- BeforeIT has no poverty measure; this step compares prices only.
- BeforeIT's no-payout run drifts beyond 12 quarters.
