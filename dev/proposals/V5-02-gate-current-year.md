# Proposal: the framework BLEI gate should read this year's BU (ChatGPT V5-02, confirmed)

**Status:** proposed, not applied. It changes simulated numbers, so it needs a mechanics-audit release (a version bump, a regenerated panel, a DECISIONS entry). `V5-02-gate-current-year.patch` is the change behind a switch that is **off by default**; with it off, output is byte-identical to v5.0.

## The defect

`runYear()` calls `agentBLEI(a, buEff, ...)` (line ~4385 of `index.html`, ~996 of `harness.js`) before it writes this year's `a._fwBUm` (line ~4431). In framework mode `agentBLEI` and `tbGate` use `a._fwBUm` once it exists, so from year 1 the BLEI gate reads **last year's** BU spend on essentials. That gate decides the wage-growth bonus (`WAGE_BLEI_BONUS`), so the lag feeds wealth and later BLEI.

## Evidence

- The hoisted expression (the same `min(12 x buEff, cost x essF)` the engine assigns later) equals the later assignment in **all 367,660** framework agent-years checked (0 mismatches).
- The stale value differs from the current one in **73%** of those agent-years.
- Paired runs, release row, 60 seeds x 500 adults, 20 years, `harness.js` as shipped vs. the patch with `GATE_CURRENT=1`:

| | BLEI below 30 days, own reading | BLEI below 30 days, design-neutral | Below cost of living | Wealth poverty | Programme inflation | Price level, yr 20 |
|---|---|---|---|---|---|---|
| Reference | 18.8 -> 18.7 | 22.1 -> **21.2** | 22.1 -> 22.0 | 35.6 -> 35.6 | 35.0 -> 35.0 | 304.3 -> 304.0 |
| Adverse | 33.2 -> 33.2 | 40.3 -> **38.5** | 42.2 -> 42.1 | 87.3 -> 87.3 | 45.8 -> 45.7 | 1901.6 -> 1898.5 |
| Stress | 54.9 -> 54.9 | 56.7 -> **56.5** | 65.4 -> 65.4 | 90.5 -> 90.5 | 24.0 -> 24.0 | 88.6 -> 88.6 |

Reading: the fix leaves poverty, wealth, prices and cost essentially unchanged. It moves one number visibly: the **design-neutral** BLEI-poverty reading falls 0.9 points (Reference), 1.8 (Adverse) and 0.2 (Stress). The change versus no programme on that reading goes from -24.7 to -25.7 (Reference) and -19.7 to -21.5 (Adverse). So the shipped figure understates the programme's design-neutral gain by 1-2 points. These are 60-seed figures; the 500-seed panel must be regenerated.

ChatGPT's V5-03 (the gate should use `fwB`, not `fwB0`) does **not** hold: `fwB0 = min(fwBudget, cost x essF)` is already capped at essentials, and `dev/DECISIONS.md` records the choice to keep the neutral gate counting the BU a participant would have spent without the price cut. Only the comment at the `agentBLEI` call site ("the BU actually spent") is loose; reword it.

## How to implement (fresh session)

1. `patch -p1 < dev/proposals/V5-02-gate-current-year.patch` in the repo root. Replace the experiment's `process.env.GATE_CURRENT` read with a normal switch (default `false` first), following the repo's pattern for harness switches.
2. Run `python3 dev/tools/port_engine.py` so the page's release engine stays a verbatim copy; `node domtest.js` Phase 12 must pass.
3. Prove the switch is inert: `node harness.js validate`, `node harness.js unit`, and a full-output diff of `node harness.js testbed 12 release ref` with the switch off against v5.0.
4. Add a unit test: a framework agent whose `buEff` changes between years has `_fwBUm` equal to this year's value when `agentBLEI` runs (fails today).
5. Turn the switch on, then regenerate the 20- and 40-year panels (`dev/runs/`, `dev/tools/merge_panel.py`), the replication figures (`dev/tools/release_figs.py`), the embedded JSON, and the 500-seed numbers quoted in `CONTRIBUTING.md` and the README. Record the decision and the before/after table in `dev/DECISIONS.md`. Release as a mechanics release.
