# S74 build map (Nov 14, 2026; part 1)

The design is preregistered in research-update `prereg/2026-11-s74-central-bank.md`. Read its "What is built" and "Unit tests" sections; nothing here overrides them. This file records where each part enters the engine, found by reading the code in part 1, so that part 2 can start building without searching.

## Data (done in part 1)
- `sources/s74_history.py` builds `sources/s74_history.json` (2005-2025, one value per year per series; `check` rebuilds it and fails on any difference). Raw downloads and SHA-256 hashes are in `sources/s74_history/raw/`. The engine needs a copy of the paths it uses inside `index.html` (as `CFG.HX`), and the unit test checks that copy against the json.
- Series the history environment reads: `cpi` (outside inflation, Dec/Dec), `homeCSReal` and `eqReal` (real gains of homes and shares, year-end), `ff` (the actual policy rate), `shadow` (the stance, with Wu-Xia below the floor), `m30` (the mortgage rate), `ugap` and `ygap` (unemployment and output gaps), `recMonths` (NBER months). The recession rule also needs real median income from `sources/history/macro_drivers.csv`.

## Where outside inflation enters (the history environment replaces a fixed rate with a yearly path)
- `runYear` (`index.html`, about line 6035): `var inflRate = p.inflRate || 0`. The PTF and PTH damping (the next lines) scales it, and it is compounded as `Math.pow(1 + inflRate, yr)` in about 10 places: `dollarCost`, `colaF` (twice), `pmFull`, `agP`, `svP`, `rtP`, `jnIdx`, `priceIdx`, `LEDGER.idx`. `hlYear` and `snYear` take the year's rate. Plan: one function `outIdx(p, yr, damp)`. It returns the product of `(1 + damped π_t)` over years 1..yr when `p.hx` is set, else `Math.pow(1 + inflRate, yr)`, so off stays bit-identical. Every call site uses it, and the yearly rate passed to `hlYear` and `snYear` is that year's π.
- `index.html` about line 4408 (a new adult's starting savings, `pLev`): the same compounding.
- `harness.js`: 35 mentions of `inflRate`. Grep them before the build; most are environment presets (`ADVERSE_REFERENCE`, `STRESS_TEST` and the study's environment list), where `hx` is added as a fourth environment.
- `baselineFor` (`index.html`, about line 6611): the no-programme run takes the scenario's inflation; it must also take `hx`, as it already does for `sx`.

## Recessions
- `tbRunCore` and its sibling (about lines 6775 and 6907): `recPath = p.shock ? (REC_SCRIPT ? recScriptPath(p.years) : buildRecessionPath(p.years, seed)) : null`. The history environment builds its path from the preregistered rule (a flagged year has any NBER month or an unemployment gap of 2 points or more; its income multiplier is real median income over its highest earlier level, capped at 1) in the same `{active, incomeMultiplier}` form, with no draw.

## Asset classes and rates (`rt`; MODEL_SPEC 14.6)
- `rtStep(b, flow, pi, R, cr)` (about line 4147). Each real class grows at `f = (1 + ix π)(1 + ρ_c) − 1`; nominal assets at `phi π`; floating debt at `psi π`; fixed debt at `chi π`. History replaces ρ_c by the year's real gain (homes and other real estate: `homeCSReal`; shares and business: `eqReal`). The rule (`cb`) replaces `phi π` by `phi × i`, and `psi π` by `i + spread`. The nesting test: with `cb {a: 0, b: 0, r: 0}` and spread 0, `i = π`, which gives today's figures exactly.
- Refinancing acts on `b.df` (fixed-rate debt) for households whose home equity is at least 20% of home value. The home value is `b.r[0]`; the debt to set against it is the household's mortgage share of `b.df`, a choice to record in DECISIONS.
- Forced sales act on `b.r[2]`, then `b.r[1]`, then `b.r[0]`, when the borrowing limit (`dr.lim`, MODEL_SPEC 14.5) binds. Buyers: households with `b.n` above six months of spending.
- S72's `gvStep` (about line 4900) takes the rate from `cb` when both are on.

## Job loss (MODEL_SPEC 12.1)
- `EMPL_P` (8.51%) and `EMPL_P_REC` (14.23%). The recession anchor's unemployment is read from the CPS source script behind them (grep `sources/` for `EMPL_P_REC`) and recorded in a prereg amendment before the pilot.

## Order of work for part 2
1. `outIdx` and the history environment (`hx`) with the rule off; guard test; the History checks on the no-programme run at 20 seeds (a check, not a result).
2. `cb`: the rule, purchases, the deposit and floating rates, refinancing, asset prices, job loss, `dm`; unit tests.
3. Forced sales (`cb.fs`); unit tests; `R2_ALT` gains `'cb'`; `node dev/tools/s68_pairs.js ENV 5` in four environments.
4. Amendment 1 to the prereg (pilot engine commit, the recession anchor, the commands), then the 100-seed pilot on the session machine.
