# Changelog

The release notes of every version before the current one, and the notes written between releases, moved here from CONTRIBUTING.md in v5.2 (Oct 3, 2026) without changes, newest first, so CONTRIBUTING.md can stay about how to contribute and what is open. The current release's notes are in [CONTRIBUTING.md](CONTRIBUTING.md); at each release they move here. References elsewhere to "CONTRIBUTING.md's vX Release Notes" (code comments, the replication page, the earlier engine) mean the section of the same name below. Headings are kept exactly, so their links still resolve on this page.

The "Unreleased" sections were written between v4.22 and v5.0 for harness-only work; that work reached the page in v5.0.

---

## v5.0.1 Release Notes

**v5.0.1 (Oct 3, 2026): the external audit pass on v5.0, applied as a pull request.** Text, tests and three page fixes; the engine is unchanged and every shipped figure is bit-identical. Prompted by two external audits of v5.0 (xAI and ChatGPT) and a third pass that checked their claims by running the code. The `v5.0` tag still points at the commit with the stale version fields; it is not moved. This version is the corrected citation.

The same fixes were first sent as `apply-audit-v5.0.zip`; that run's checks passed but its commit step failed (`git add` refused the ignored `node_modules` path), so none of them went live until this pull request.

**Fixed in this pass**
- **A single live run said "No group is worse off than with no programme on any test" whatever its numbers showed.** `relLiveRows` hard-coded `worse:'none'`. In Reference, seeds 1-6, adults who did not take part lose $415-$1,441; in Adverse and Stress, seeds 1-6, wealth poverty rises. A live run now reads the sign of its own group results and its own wealth-poverty change (`relLiveWorse`).
- **The earlier-engine explorer stalled without Chart.js.** `finish()` threw in `drawThresholdCharts`, and the status bar stuck at "Simulating year 20 of 20…100%". Charts are now no-ops with a visible note when the library is missing.
- **Static version fields said 4.22 in a 5.0 release:** the page `<title>`, JSON-LD `softwareVersion`, the two static `.meta-ver` labels, the script banner, this file's signature line, and (on the replication page) the JSON-LD name, the seal tooltip, the Python-snapshot caveats and both meta descriptions. `dev/tools/check_versions.js` now fails on any of them (domtest Phase 13), and `set_version.py` writes them.
- The "mixed result" sentence named inflation as the cause even for runs with none; the results panels are announced to screen readers (`aria-live`).
- **Price level, wording (F3, first part).** Where the programme's price level passes 1,000 times today's, the front door no longer prints the figure (821,679,717 times at 40 years in the Adverse Environment read like a forecast). It says that the model's price rule has no central bank, no interest rate and no protection for savings, so prices run away in that environment, and that this is a limit of the model, not a forecast. The exact figure moved to a new column of the replication page's two release tables (`dev/tools/release_figs.py`); `domtest` Phase 13 checks both.

**Found, not applied (each changes numbers or the page's claims, so each needs a mechanics-audit release behind a switch)**
- **Framework BLEI gate timing (ChatGPT V5-02, confirmed).** `agentBLEI` is called before this year's `_fwBUm` is written, so from year 1 the gate reads last year's value. The stale value differs from the current one in about two thirds of agent-years. A switch-gated fix is in `dev/proposals/` with its paired-run comparison. ChatGPT's V5-03 (full budget versus actual spend) does not hold: `fwB0` is already capped at essentials, and `dev/DECISIONS.md` records the choice.
- **The price level at year 20 (and 40) is an arithmetic mean over seeds of a compounding quantity** and is stored under the key `pLev20` even in the 40-year panel. A median and a range would describe a typical run better (the wording above is the only part of F3 done in this version).
- **Gini and the Hub's targets (poverty below 2%, Gini at most 0.25) are computed by the release engine (`giniD`, `giniX`) but not exported to the front door.**
- **Parity coverage:** the behavioural page-versus-harness check uses seeds 1-2, 3 of 11 rows, 20 years only; there is no commit or file-hash manifest in the exported `_meta`.

---

## v5.0 Release Notes

**Released Oct 2, 2026 as v5.0** (Duke said "release" on Oct 2; `python3 dev/tools/set_version.py 5.0` set every label). Built on the branch `next-release` in sessions 30 and 31 (Oct 1-2, 2026) following `dev/PLAN.md` and Duke's four added items (Oct 2); every decision is in `dev/DECISIONS.md` and every mechanism has a plain-words report in `dev/reports/`.

### Why a new major version

The page now runs Compassionism as specified on the Research Hub, with every planned mechanism, instead of the v4.22 engine as coded, and it opens with that model's results instead of a comparison with other designs. The headline figures change meaning, not just value.

### What the release contains

| Plan step | What | Where |
|---|---|---|
| 1 | The ESP split: community businesses split their premium (prices, capacity, workers); private ones keep it | `SURP` in `harness.js`; `dev/reports/01-esp-split.md` |
| 2 | The production side: PTF capacity built by reinvestment; project work and capital counted as output | `PROD`; `02-production-side.md` |
| 3 | Source financing: the Treasury issues BU and pays conversions; net payout is new money less output that backs it | testbed `fin: 'source'`; `03a-financing-reading.md`, `03-financing.md` |
| 4 | Joining and leaving each year | `JOIN`; `04-joining.md` |
| 5 | PTF running costs and PTH capital from BEA and Census figures | `COST`; `05-ptf-pth-costs.md` |
| 6 | The octave rule kept; slower advancement as a sensitivity | `OCT`; `06-octave-rule.md` |
| 7 | The spending rule matched to the 2025 US saving rate (59.3% of surplus spent) | `SPEND_SOURCED`; `07-spending-rule.md` |
| 8 | BLEI leads every result | every step section; `08-blei.md` |
| 9 | Public costs of homelessness avoided, sourced low and high | `AVOID_HOMELESS`; `09-avoided-costs.md` |
| 10 | The engine ported into the page verbatim, with source and same-seed parity checks | `dev/tools/port_engine.py`; domtest phase 12 |
| 11 | The 500-seed restudy, three environments | `dev/runs/step11-release-500-*.txt`; `11-restudy.md` |
| 12 | The page rebuilt; the comparison saved unlinked; assumptions and history moved to the replication page; three wording fixes; attribution | `12-page.md` |
| 14 | Private ESPs pass the conversion premium to BU customers as lower prices; their workers paid like profit-share workers (Duke's correction) | `SURP.priv 'prices'`; `v5-1-private-esp-correction.md` |
| 15 | Creative output counted at market value; community capacity within a year, its borrowed capital charged; ESP conversion capped by capacity | `PROD.match 'market'`, `PROD.speed 'oneyear'`; `v5-2-creative-output-reading.md` |
| 16 | The spending layer: the programme's spending fills recession losses at a sourced multiplier | `MULT`; `v5-3-spending-layer.md` |
| 17 | Wider public costs avoided: prisons, hospital and psychiatric care | `avoidWide`; `v5-4-public-costs.md` |
| 18 | v5.0's main row includes steps 14-16; the 500-seed panel regenerated | `REL_V5`; `v5-5-restudy.md` |

### Headline (500 paired seeds; release row against no programme)

| Environment | Below 30 days of basic living | Below the cost of living | Too little wealth, year 20 | Programme inflation | Too little wealth if every Source dollar were backed (H1) |
|---|---|---|---|---|---|
| Reference | 18.7% vs 46.7% | 22.0% vs 55.2% | 35.7% vs 52.0% | 34.9% | 15.4% |
| Adverse | 33.1% vs 60.0% | 42.1% vs 78.2% | 87.1% vs 82.6% | 45.6% | 52.5% |
| Stress | 54.9% vs 60.0% | 65.6% vs 78.2% | 90.6% vs 82.6% | 23.8% | 72.6% |

The gain is confirmed on all three measures at reference; in Adverse and Stress more adults end with too little wealth than with no programme. See `dev/reports/v5-5-restudy.md` (session 30's figures, before Duke's four items, are in `11-restudy.md`).

### Checks

`node harness.js validate`, `node harness.js unit` (new suites: surp, prod, src, join, cost, oct, spend, avoid, priv, v5Prod, mult, avoidWide) and `node domtest.js` (97 checks; phase 11 rewritten for the new front door, phase 12 new). With every new switch off, the v4.22 engine's outputs are byte-identical (full-output diffs of the testbed sections and validate after each step).

---

## Unreleased: BLEI by group beside FGT₂ (s41; issue i10-1; harness only)

Duke asked (i10) how ESP payroll affects BLEI, not only FGT poverty. The testbed now reports BLEI and FGT₂ separately for participants and for adults who chose not to take part. Nothing the model does changes: the addition is reporting only, draws no random number, and leaves every earlier figure identical (session 21 diffed the full output of `testbed esp`, `projcore`, `a5` and `match` against `f961adc`; only elapsed times differ).

- **`tbBleiYear()`** runs after each year of every testbed run and reads three versions of each adult's BLEI, deflated to year-0 prices:
  - **design-neutral (N)**: Baseline rules plus one month of the design's regular support. It heads the tables (d34).
  - **the design's own (O)**: the page's definition.
  - **net of the contribution (X)**: N with income read as the year's wage earnings after the contribution and any change in hours, in place of the gross wage rate. This is a labelled sensitivity (d83).
- **Groups:** all adults, participants, and non-participants. They are the same adults in every row.
- **Measures:** the person-year share below 30 days (BLEI poverty) and below 7 days (Crisis) over 20 years; the year-20 share below 30 days; and the year-20 median. Person-year FGT₂ is also reported by group (`gPartF2`, `gNonF2`).
- **Output.** `testbed … esp`, `proj` and `projcore` print two new tables: levels by group, and changes against no program and against each row's comparison row, with 95% intervals on the design-neutral reading. The other sections compute the new keys but do not print them. `a5` gets them at the N1 release (s35).
- **`bleiUnitSuite()`**, five tests, run by `unit`:
  - the year-20 N and O shares for all adults equal the testbed's existing `nbleiPov` and `bleiPov` exactly;
  - the two groups partition every share and FGT₂;
  - reading X falls by γ × the added contribution and N does not;
  - the accumulation changes no agent and draws no random number;
  - one month of BU keeps a participant out of Crisis on N, which is why participants' Crisis share is 0.
- **Run time.** Testbed sections run about 20% longer.
- **Result (500 seeds; `N1-blei-by-group-500.md`).**
  - **ESP payroll moves BLEI in opposite directions for the two groups** (Hub-spec model, reading N, against today's rule). For participants / non-participants the change is −0.26 / +4.44 points at reference, −2.37 / +2.56 in Adverse and −1.09 / +0.68 in the Stress Test.
  - **Against no program, non-participants' BLEI poverty rises** by 16 points as coded (project hiring, reference) and by 33 points specified on the Hub with ESP payroll.
  - **Why.** The loss comes from the flat wage contribution, which reaches BLEI through savings. BLEI's income term reads the gross wage rate, which the contribution does not change.
- **The engine in `index.html` is unchanged**, and so is the page.
- **Checks.** `validate` passes, `unit` passes (the new suite 5 of 5), and `domtest` passes all 95.

---

## Unreleased: ESP payroll in expired BU at workers' own rates (N1, s38; harness only)

In the Hub-spec (framework) model, businesses convert every BU they accept at a flat 3× and pay the premium over a cash sale to every adult in proportion to wages: the model's largest flow, with no mechanism behind it. Duke's rule R7 (Sep 29) supplies one for the wage part: essential service providers (ESPs) may pay workers in expired BU, and the workers convert them at their own earned rates. The design and its decisions (d70–d76) are in `N1-design-esp-payroll.md` (session 18).

- **`ESP` in `harness.js`** (null by default, so every run is bit-identical: session 19 diffed the full output of `testbed projcore`, `proj` and `a5`, `ledger` and `price framework` against `b1bc475`). Hub-spec model only; the engine model has no business conversion and ignores it (d70). Each year:
  - **Payroll pool (d71).** 20% of the BU ESPs accepted last year: compensation ÷ gross output in the essential industries, weighted by the basket's essentials (BEA GDP-by-industry, 2024 values; range 0.15–0.26; derived by `sources/esp_payroll_share.py`, which also derives the workforce share). The ESP converts the rest at 3× as now.
  - **ESP workers (d72).** 23.0% of adults (BLS CES Table B-1, August 2026), fixed by agent index, so they are the same adults in every design and seed and no random number is drawn. The pool is shared in proportion to last year's wage, each share capped at that wage.
  - **Who converts (d73).** Participating ESP workers whose own rate after tax, times the CIP bonus, beats par take their share as expired notes and convert it at their own rate. Everyone else is paid in dollars, and the ESP converts those BU at 3× this year.
  - **Capacity (d74).** 12,000 × 2^octave BU a year, net of project BU; BU above it are paid in dollars. It binds for 0.04% of participating ESP worker-years at reference (issue i9: octave advancement saturates).
  - **The rest (d75).** The ESP's own premium is paid as today, to every adult by wage, as the stand-in for its other costs and surplus.
  - **Income and work.** Wages are unchanged, so BU pay counts at face value in wages and the contribution base. The premium, BU × (rate × (1 − tax) × CIP bonus × income shock − 1), is conversion income and program cost. It is earned, so it enters the wage elasticity as a raise, with no income effect (the fairness rule).
  - **Switches.** `lam`, `work` (a share, `'ptf'` or `'all'`), `take` (`'par'` or `'biz'`), `cap` (`'dollars'`, `'save'` or `'none'`) and `rest` (`'all'` or `'esp'`).
- **`espUnitSuite()`**, eleven tests, run by `unit`: ESP off creates no state; λ = 0 reproduces ESP off exactly; BU conservation every year; the wage cap; octave capacity; non-participants never convert; no added random draws and a fixed workforce; the engine model unaffected; ledger rows and the premium formula; the labor raise; the worker-cooperative and "beats 3×" alternatives.
- **The testbed reports** each run's business premium as paid, and payroll premium by group, over years 1–19 (year 0 pays none). This is reporting only.
- **`node harness.js testbed N esp ENV`** reproduces the restudy: today's Hub-spec main row, ESP payroll at the defaults, every d71–d75 alternative, the page's other rows with and without it, and hybrid financing at a = 0 and a = 1. Its "today" rows equal session 16's 500-seed core rows.
- **Result (500 seeds, tax-financed at own cost).** ESP payroll makes the Hub-spec main row worse in all three environments: the 20-year average FGT₂ rises by 2.71 points at reference, 1.20 in the Adverse Environment and 0.26 in the Stress Test (95% intervals within ±0.04). Under hybrid financing it rises by 0.13–0.41, with or without H1.
  - **Every alternative is also worse, with one exception.** That exception is making every adult an ESP worker in the Adverse Environment (−0.24).
  - **The reason.** The premium moves from every adult by wage to participating ESP workers, so non-participants lose: about $6,000 a year at reference against today's rule. Workers' own rates (4.23× on average at reference) beat the ESP's 3×, so the total premium also rises (9% at reference), and at reference the wage contribution that pays for it rises from 74.9% to 80.0% of wages.
- **The engine in `index.html` is unchanged**, and so is the page. Per d76 the Hub-spec main row changes at the N1 release (s35).
- **Checks.** `validate` passes, `unit` passes (the new suite 11 of 11), and `domtest` passes all 95.

---

## Unreleased: uploading a session's files as one zip (session 17)

GitHub's web upload flattens folders and cannot unzip, so session 16's walk-through landed in the repository root and its tour page replaced README.md (commit `169e065`; `domtest` failed 94 of 95). The new workflow `.github/workflows/apply-upload.yml` fixes this for every later upload:

- **How to use it.** A session delivers one zip named `apply-session-NN.zip`. Drop it on the repository's root upload page and commit. The workflow unzips it with its folders intact, removes any paths listed in its `DELETE.txt`, runs `validate`, `unit` and `domtest` on the result, and commits it to main only if all three pass, removing the zip. It then starts `checks` (and `release`, if `index.html` changed) on the new commit, since commits made by the workflow start no other workflow on their own.
- **Safeguards.** A zip may not touch `.github/` or reach outside the repository. If a check fails, nothing is committed; the zip stays on main and the run's log names the failure. Actions > apply upload > Run workflow retries it.
- **The repair.** `apply-session-16.zip` carried session 16's `README.md`, this file and the `walkthrough/` folder, and its `DELETE.txt` removed the 27 walk-through files from the root.

---

## Unreleased: the revised opening line (i5) and the walk-through (s29)

After the v4.22 tag (`777d9b3`, Sep 28, 2026), Duke revised the page's opening line (`589a127`) to: "Compassionism aspires to enhance cultures by eradicating extreme poverty while incentivizing participation and contribution: test that claim against five other designs on the same simulated people." The tagged v4.22 release, and the session 11 note below, carry the earlier wording (d41).

- **README.md** opens with the revised sentence. Until it did, `domtest` Phase 11's first check failed on `main` (94 of 95), because README.md must open with the page's sentence.
- **One sentence added to the front door's subtitle and to README.md (d51):** "The model measures poverty, cost and work, not the cultural effects Compassionism aspires to." The opening line now names culture, which nothing in the model measures, so the page says so beside its note on how poverty is measured. The design panel already frames the framework's cultural value as its intent, not a measured result (d47).
- **The opening line's ending (d51, session 13).** Duke chose to end the line by naming what the page measures as well: "...participation and contribution: see how it does on poverty and work against five other designs on the same simulated people." It replaces "test that claim", which a reader could take to cover the cultural aim. The page's `<h1>` and README.md line 3 carry it; the subtitle sentence above stays.
- **Walk-through narration (s39, session 16).** `make_walkthrough.py` now reads each caption aloud with a synthetic American-English female voice (Kokoro-82M, Apache-2.0, voice `af_heart`, run locally through `kokoro-onnx`; the model files are downloaded on the first build into `~/.cache/` and are not in the repository). Each caption stays up for its reading time or its narration, whichever is longer, so captions, voice and video share one clock. A `SPOKEN` table sets how the voice reads acronyms, file names and dollar figures without changing the captions. `--silent` builds the old silent video.
- **Walk-through (s29, session 13).** `walkthrough/` holds a captioned video tour of the page (about five minutes, no sound until session 16), the same tour as a written page with screenshots (`walkthrough/README.md`), caption files (`captions.vtt`, `captions.srt`) and `make_walkthrough.py`, which rebuilds all of them from `index.html` (Python, Playwright and ffmpeg; not part of `npm test`, and no change to `package.json`). Every figure in the captions is read from the front door's `#fd-data`, and the build stops, naming the caption, if the data no longer supports a caption's wording, so a rebuild after N1 either carries the new figures or says which sentence to rewrite. README.md links to it; the page does not yet (d57). Nothing in the engine or the page's figures changes.
- **Three stale labels in this file (corrections).** The signature line read v4.21; Code Contributions gave `domtest` as 82 checks as of v4.21 (now 95); Academic Peer Review linked the replication page at its old Hub address, which redirects. All three now match v4.22.
- **Checks.** Text and new files only: the engine is unchanged, `validate` and `unit` pass, and `domtest` passes all 95 checks. `META.VERSION` stays 4.22, so the release workflow does nothing; these notes join the next version's.

---

## Unreleased: project hiring paid in expired BU (N1, s33; harness only)

Decision d46 replaces the engine's octave wage raise (0.3% a year of extra wage growth per octave held, which every adult in the Compassionism scenarios received at their starting octave, including those who chose not to take part) with the design's own mechanism: creative projects hiring participants at elevated conversion rates, paid in expired BU. The design and its decisions (d58–d66) are in the session 14 and 15 hand-offs.

- **`PROJ` in `harness.js`** (null by default, so every run is bit-identical, checked by `unit`). Both conversion models. Each year:
  - **Pool.** Last year's expired BU (engine: the unspent balance that expires; Hub spec: the BU budget left unspent), plus the rollout plan's launch gift of 1,000 expired BU per participant in year 1.
  - **Pay and hiring.** The pool pays for project hours at $23.74 BU an hour (the model's living wage at par, indexed to prices). Hours go to participants for whom a project hour pays more than their own wage, weighted by octave capacity × quality.
  - **Rate.** Each BU converts at the higher of the worker's own rate and the capacity × quality-weighted mean rate.
  - **Capacity.** No cap (d64, Duke's pick). A switch caps project BU at the octave capacity left after the engine's own-spending conversion (12,000 × 2^octave BU a year) and saves the excess; in the restudy it binds for no one, so the two give the same results.
  - **Hours.** Project hours are added on top of wage work (d63, Duke's pick), with no income effect. A switch has them replace wage hours instead.
  - **Financing (d66; session 16, issue i7).** The flat contribution pays for the one-time gift in the year it is converted (`giftFin: 'payg'`, Duke's pick: the design as intended), which raises the year-2 contribution by about 5 points (seed 1, engine, reference; 26.2% against 21.0% with no gift). `giftFin: 'run'` spreads it over the remaining years, the rule the testbed applies to the asset endowment (d26), adding about 0.2–0.3 points a year. The cost counted is the same either way; only its timing, and so the work response, differs. Both are reported (see below). Session 15's hand-off put the pay-as-you-go jump at "about half a point"; that was off by a factor of ten.
  - **Switches.** Every alternative in d59–d63 is a switch.
- **`projUnitSuite()`**, nine tests, run by `unit`: an empty pool equals `PROJ` off; BU conservation; octave capacity; the rate rule; willingness; no added random draws; the launch gift; hours; gift financing.
- **`node harness.js testbed N proj ENV`** reproduces the restudy: every row CRN-paired against no program and against the raise switched off. Its default row now pays for the gift as you go, and a new row pays for it over the run. Session 15's sensitivity figures were computed with the gift paid over the run and remain correct as that comparison.
- **`node harness.js testbed N projcore ENV`** (session 16) runs only the rows the page will carry at the N1 release (d65), each with the gift paid both ways: the design as intended and, on equal terms with the endowment, over the run.
- **Result (Duke's configuration at 200 seeds; the displacement version at 500).** Project hiring does not replace what the raise did.
  - In the engine model at reference, the 20-year average FGT₂ cut is −1.78 with project hiring, against −1.76 with the raise simply off and −3.21 with it on. It costs about $1,130 more per adult a year.
  - Elsewhere it is slightly worse than raise-off (by 0.02 to 0.13), and so is the displacement version in every cell (by 0.04 to 0.26).
  - The reason: the pay reaches participants by capacity and quality, not need, and the wage contribution that pays for it lowers work and falls on everyone.
- **The engine in `index.html` is unchanged**, and so is the page. Per d65 the main Compassionism row changes at the N1 release (s35).
- **Checks.** `validate` passes, `unit` passes (the new suite 9 of 9), and `domtest` passes all 95.

---

## v4.22 Release Notes

v4.22 (Sep 28, 2026) releases the policy-testbed round: sessions 1–11 of *Next Round Plan: Simulation Testbed and Claims Ledger* (Sep 26). Each session's notes follow as a "v4.22, session N" section, newest first. **The engine in `index.html` is unchanged: the seed-42 regression and every preset's figures are bit-identical** (`validate` passes). What a visitor sees does change: the page opens with a comparison of Compassionism against five other anti-poverty designs. `unit` passes (11 tests, 8 price-module tests, 4 labor-module tests, 6 session 5 tests and 16 testbed tests, 1 of them new); `domtest` passes all 94 checks (2 new). Hand-off: `session-10-handoff.md`.

### What the release contains

| Plan item | Where it lives | Sessions |
|---|---|---|
| A0 flow map: where program money enters, moves and leaves | `A0-flow-map.md` (project files) | 1 |
| A1 issuance ledger | `node harness.js ledger` | 1 |
| A2 money-creation and price module, breakeven additionality, price-neutral point | `PRICE`; `node harness.js price` | 2, 3, 5 |
| A3 labor supply: one income effect per unconditional dollar (ρ 0.16), one compensated elasticity (0.33) | `LABOR`; `node harness.js labor` | 4, 5 |
| A4 testbed: basic income, negative income tax, asset endowment, public grocery, X-Cents, one cost ledger, tax / money / hybrid financing | `node harness.js testbed … match / frontier / alts / decomp` | 6, 7 |
| A5 reporting: FGT₀–₂ at year 20 and over 20 years, spells, cost per point, prices, hours, income Gini, group losses in dollars | `node harness.js testbed … a5` | 8 |
| A6 front door on the page | `index.html`; `node harness.js frontdoor` | 8, 9, 10 |
| The replication page moves into this repository | `replication.html`; `domtest` Phase 10 | 7 |

Every harness addition sits behind switches whose defaults leave the engine bit-identical, and `validate`, `unit` and `domtest` run on every push.

### Reading the comparison

- **Same people, same rules.** Every design runs on the same 500 simulated single adults for 20 years with paired random seeds, is paid for by a flat contribution on wages set each year to cover its cost, and meets the same work response. The basic income, negative income tax and asset endowment are matched to Compassionism's gross cost per adult-year; the public grocery network and X-Cents run at their own cost.
- **The shaded row.** Wherever Compassionism appears, the row beneath it switches off its two mechanisms that are theoretical, yet to be empirically tested, and cost nothing in the model (both the model's stand-ins, not the design; session 11): the octave wage raise (d19) and the PTF/PTH inflation damping (d33). Across the round these carried most of Compassionism's edge (see `round-close-out-and-next-round-plan.md` in the project files).
- **The headline measure** is poverty severity (FGT₂ on the living-wage basket) averaged over all 20 years, with year 20 beside it (d37); year 20 alone overstated Compassionism's gains.
- **Pre-computed, on the testbed's profile.** The table is data written by `node harness.js frontdoor` from `testbed … a5`, not a live run (d36). The testbed's profile differs from the live scenarios (θ on realised PTF density, PTH cuts housing only, discounts skip the basket's tax share, wages indexed to prices, the work response, the design-neutral BLEI gate, and `N7_BLEI`), so the two sets of figures differ. The table's caption says so.
- **Not modelled, for any design:** public costs of poverty (d29), a production side for conversion rewards (H1), households and children.

### Session 11: what changed (Duke's review of the prepared page)

- **The opening line (d41, Duke's option 5).** "Compassionism aims to end extreme poverty while incentivizing participation and contribution: test that claim against five other designs on the same simulated people." It is a statement, so Phase 11's first check now accepts one sentence ending in a full stop or a question mark. The subtitle adds that poverty is measured against a living-wage basket, a higher bar than extreme poverty, with the deepest shortfalls weighted most (FGT₂), so the claim is tested on a stricter line than the one it names. README.md opens with the same sentence.
- **Wording.** Everything a reader sees now calls the octave wage raise and the PTF/PTH inflation damping "theoretical, yet to be empirically tested", and says both are the model's stand-ins, not the design (d46). Earlier session notes below keep the word they used ("unsourced").
- **The design panel.** Compassionism's entry is rewritten from Duke's notes: BU as a restricted currency that expires; conversion at elevated rates set by market demand and by community-validated quality (the multiplier rate); the octave as conversion capacity, a safeguard against exploitation and an open ceiling for creators with demand; wage work still paid in dollars, with creative projects able to hire at elevated rates paid in expired BU; an allowance that can vary by region, age and labor-market needs (the model holds it flat). A second paragraph says what sets the design apart: it creates both a supply of a new restricted currency and a demand for it, and aims to hold basic living costs steady through community-owned supply before letting prices fall, where current policy manages inflation through the money supply and interest rates (d47: stated by mechanism). The negative income tax entry no longer says the allowance is the same for every participant by design. The grocery and X-Cents entries are rewritten (below).
- **A needs-based top-up (d39, d44).** `PR.ccoTop(G, s, t)`: Compassionism with its flat BU cut by a share s, and the savings paid as extra BU to participants only, max(0, G − t × wage earnings), t = 0.5 (`nit.part`, read by `tbGate`, `tbLab` and `tbCashFlow`; unset everywhere else, so every other row is bit-identical). `tbMatch('ccoTop', …)` sets G so the total cost equals Compassionism's. A 30-seed sweep (`testbed 30 topup ref,adv,st`) tried s = 0.1, 0.25 and 0.5 and a 0.3 phase-out: only s = 0.1 deepened the 20-year FGT₂ cut in all four reference and Adverse cells (the Stress Test was added afterwards), so a5 and the page use it. At full seeds (a5):

| Environment, model | Compassionism: FGT₂ 20-yr change / share in poverty / hours | With the top-up (same cost) |
|---|---|---|
| Reference, engine | −3.21 / 45.4% / −4.9% | −3.38 / 47.4% / −7.2% |
| Reference, Hub | −1.76 / 53.1% / −14.5% | −1.87 / 60.4% / −21.7% |
| Adverse, engine | −7.67 / 74.4% / −7.5% | −7.76 / 75.5% / −10.2% |
| Adverse, Hub | −4.18 / 83.9% / −25.8% | −5.30 / 87.3% / −30.6% |
| Stress Test, engine | −3.71 / 76.1% / −3.5% | −3.70 / 76.3% / −4.5% |
| Stress Test, Hub | −3.58 / 76.5% / −5.5% | −3.53 / 78.1% / −8.6% |

  The top-up deepens the cut in four of six cells and leaves it about the same (within 0.05) in the Stress Test; it raises the share in poverty and lowers hours in all six, because a benefit that shrinks as earnings rise works like a tax on work. It is shown as its own row beneath Compassionism's mechanisms-off row, with its own mechanisms-off figure in the note, rather than replacing the main row (d44).
- **Grocery at its real scale.** The Mayor puts New York's existing grocery stores at more than 1,000 (nyc.gov transcript, Jul 27, 2026), so five stores of the same size would serve about 0.5% of shoppers (`TB_GROC_PILOT`, derived; the 9,000 sq ft La Marqueta store makes it if anything high). The page shows the plan as announced (five stores: about $4 per adult-year, no measurable change) and the network at full scale (every adult 15% off food: $807, −0.04 at reference). Neither models the effect on other grocers' prices.
- **X-Cents from its paper (d48).** The paper was read in full, and the page links https://bettertobest.github.io/x-cents/. `PR.xcFull(f, h)` adds the Power of 1 to the adult exchange: one designated day a week, coins count as $1 for food, so food bought with pennies costs 1 cent per dollar (`TB_XC_P1` 0.99), with the week's food shopping moved to that day (f = 1; f = 1/7 if no shopping moves). The main row covers food (reference: $8,017 per adult-year, −1.17; exchange alone $3,613, −0.56; f = 1/7 $4,243, −0.65). Food and housing (`groc.housing`) is a sensitivity row, since paying rent and utilities in coins needs landlords and utilities to join: $21,514, −2.00 at reference, and +0.24 in Adverse, where its contribution cuts hours by 37%.
- **Each design at its proposers' size (d45).** The page gains a second view. Basic income $12,000 a year (`TB_UBI_PROP`, the $1,000 a month paid in Vivalt et al.'s study); a negative income tax guaranteeing the 2026 HHS poverty guideline for one person, $15,960, with a 50% phase-out (`TB_NIT_PROP`); the stakeholder grant, $80,000 of 1999 × 321.943 / 166.6 (CPI-U annual averages) = $154,594, once, to adults under $25,000 (`TB_ENDOW_PROP`; no return in the model). Reference: $11,999, −1.67; $1,607, −0.09; $2,922, −0.44. Because designs of different sizes are not a fair contest by themselves, every costed row in both views now shows its change in 20-year FGT₂ per $1,000 (reference, engine: Compassionism −0.28, with the top-up −0.30, without the two theoretical mechanisms −0.16; matched basic income −0.14, matched NIT −0.20; X-Cents −0.15; basic income at $12,000 −0.14; stakeholder grant −0.15).
- **Link and layout review (Duke's screenshots).** The row labels, the "What each design is" link and the caveats box's "Assumptions and Known Limitations" link were same-page fragment links (`href="#…"`). They work on GitHub Pages, but claude.ai's file preview routes every link click as a URL on claude.ai, so they opened a new chat. They are now buttons (`.fd-go`, with `data-go` naming the target), which no host can send off the page; the page has no fragment links left, and Phase 11 checks that. All 49 external links on the page, the replication page and the README were requested: each resolves (the six that answer 403 are publishers and sites that refuse scripted requests; the two DOIs redirect to the right papers). Below 1,180 px the caveats box stood taller than its text: the base `.fd-side` rule came after the narrow-screen rule and overrode its direction, so each box took its 300 px flex-basis as a height; fixed. The replication page's section links stay fragment links (d49): correct on the live site, but they misroute in claude.ai's preview.
- **Worse off, and participation as a choice (d50).** The column compares each group with itself under no program, and its losses come from the contribution that pays for each design. Under Compassionism they fall mainly on adults who do not take part, who pay the contribution and receive no BU. The column now names them "adults who chose not to take part", its tooltip and the table's caption say so, and the design panel states that participation is open to every adult. It also states the model's limit: each adult's choice is set at the start and kept for 20 years, so an adult who would gain by joining cannot.
- **Checks.** `unit`: two new testbed tests (the top-up at G = 0 equals Compassionism at the smaller BU, and pays participants only; Power of 1 at f = 0 equals the flat exchange, housing raises the cut, five stores cost a small fraction of the full network). `domtest` Phase 11: the statement check, both views in the data and in rendering (24 views), and one new check (the view switch moves the comparators and not Compassionism, every costed row states its change per $1,000, X-Cents links its site, and no visible text calls the mechanisms unsourced): 95 checks. The engine in `index.html` is unchanged; `validate` passes.
- **Reproduce.** `node harness.js testbed 500 a5 ref --json=a5.json`, `node harness.js testbed 200 a5 adv,st --json=a5.json` (about 9 minutes each), `node harness.js frontdoor a5.json`; the sweep, `node harness.js testbed 30 topup ref,adv,st --pilot=20` (about 4 minutes).

### Session 10: what changed

- **Tooltips (dashboard i4, and Duke's review).** Every tooltip was a CSS `::after` box drawn inside the element it explains. Inside the front door's table, which scrolls sideways on narrow screens, the scroll box clipped the top of every column tooltip, so the first lines were hidden behind the column labels. The same boxes, though invisible, widened the page to 421 px on a 390 px phone. One floating box placed by script (`initTips`, `position:fixed`) now serves every tip: it cannot be clipped, it opens below its host when there is no room above, it stays 8 px inside the window, it opens on hover, tap and keyboard focus (not on a mouse-click focus, as v4.20 intended; a tapped tip stays open until the next tap, since phones send mouse events around a tap), and it closes on leave, blur, scroll, resize and Escape. Checked on a touch-phone viewport as well. The CSS boxes remain as a fallback when scripts do not run. Checked in a headless Chromium: the column tooltips show in full, and the page is 390 px wide at 390 px. `domtest` checks the behaviour (it has no layout engine); decision d42.
- **What each design is.** A panel under the comparison with one entry per design: the proposal, how the model simplifies it, and its source, linked. Every row label links to its entry, and the "Compassionism as" switch has its own ⓘ explaining the engine and Hub versions. Sources: Vivalt et al., NBER Working Paper 32719 (basic income; also the source of ρ); Moffitt (2003), *Journal of Economic Perspectives* 17(3) (negative income tax); Ackerman and Alstott, *The Stakeholder Society* (1999), and Hamilton and Darity (2010), *Review of Black Political Economy* 37 (asset endowment); NYC Mayor's Office, July 27, 2026 (public grocery; the 30% and 15% are the city's projections, not results); the CurrentSea X-Change paper on Academia.edu (X-Cents). `domtest` Phase 11 checks every entry, every source link and every row link.
- **The front door's question** (d41, following d35): "Dollar for dollar, which does more against poverty: Compassionism, a basic income, or a negative income tax?" README.md opens with the same sentence, as Phase 11 requires. The subtitle now says which designs are matched to Compassionism's cost and which run at their own.
- **`N7_BLEI` in the testbed profile (d40).** `TB_PROFILE_G` turns it on for every testbed row that does not set it (the `n7` section still sets it both ways); the global default stays `false`, so the checks still test `index.html`. The front door was regenerated (`testbed 500 a5 ref`, `testbed 200 a5 adv,st`, then `frontdoor`). Against session 9's figures, engine-model rows move by 0.06 point of 20-year FGT₂ or less (0.16 at year 20) and hours by 0.2 point or less; the largest move is the framework-scale basic income at reference, 0.15 point over 20 years and 1.18 at year 20, in the fiscal-breakdown regime (an 89% contribution). No conclusion changes. At reference, per $1,000 of cost, 20-year FGT₂ cut: Compassionism (engine) 0.28, without its two unsourced mechanisms 0.16, matched basic income 0.14, matched negative income tax 0.20.
- **Metadata (d43).** The page's description had last been updated at v4.15; it and the sharing descriptions now say what the page compares. The replication page's JSON-LD cited the simulation as v4.17; now v4.22.
- **Version labels.** `META.VERSION` 4.22; the page's static labels, title and JSON-LD; the replication page's eight labels (Phase 10), its highlights, and a v4.22 panel in each Version History list; the "Unreleased" headings below renamed for this release.

---

## v4.22, session 9: the N7 attribution of the BLEI raise (i3-2), and front-door wording

Next-round session 9 (Sep 28, 2026). Released in v4.22. **The engine in `index.html` is unchanged and every shipped figure is bit-identical.** `validate` passes; `unit` passes (11 tests, 8 price-module tests, 4 labor-module tests, 6 session 5 tests and 15 testbed tests, 1 of them new); `domtest` passes all 92 checks. Tables and decisions: `session-9-handoff.md`; the round's close-out: `round-close-out-and-next-round-plan.md`. Raw output: `session-9-results.txt`.

- **`N7_BLEI`** (dashboard i3-2; default `false`). The N7 split counted the octave and CIP raises as program-induced and the BLEI-gated raise as not. With `true`, the BLEI raise counts as program-induced in the adult-years where the design's own support is what carries the adult over the gate (the gate passes as the run reads it, and fails on Baseline rules with no program support); the same rule for every design. It moves the labor module's raise and, where aw < 1, the price module's premium; the raise itself is unchanged. The testbed now reports the share of adult-years with a BLEI raise and the share the design carried over the gate.
- **`node harness.js testbed <seeds> n7 [ref,adv,st]`**: the attribution off and on, for Compassionism and the matched UBI and NIT. At engine scale it moves FGT₂ by 0.07 point or less for every design; only framework-scale cash designs move materially (up to 1.2 points at year 20).
- **Front door wording** (data written by `frontdoor`): each environment's caption now says the comparison runs on the testbed's profile, which the live scenarios do not use; the NIT row notes that it is means-tested while Compassionism's BU is flat by design.

---

## v4.22, session 8: reporting upgrade (A5) and the front door (A6)

Next-round session 8 (Sep 27, 2026). Released in v4.22. **The engine in `index.html` is unchanged and every shipped figure is bit-identical** (`validate` passes; domtest's seed-42 fixtures and source-parity checks pass). The page gains a front door above the layout. `unit` passes (11 tests, 8 price-module tests, 4 labor-module tests, 6 session 5 tests and 14 testbed tests, 3 of them new); `domtest` passes all 92 checks (7 new, Phase 11). Tables and decisions: `session-8-handoff.md`. Raw output: `session-8-results.txt`.

### The front door (plan A6)

A band above the page's layout, so it is the first screen on phones too:

- **one question in one sentence**, which README.md now also opens with;
- **Compare designs**: the testbed's comparison for the reference, adverse and stress environments, with Compassionism as coded in the engine or as specified on the Hub, and optional sensitivity rows. Figures come from `testbed … a5` and are written into the page's `#fd-data` block by `node harness.js frontdoor <a5.json>`; the page does not run the comparators live;
- **Run a Compassionism scenario**: the six presets, each loaded into the controls and run;
- **one caveats box**: the old notice (`#uncertainty-notice`), moved here and rewritten; a run no longer hides it;
- **method links**: the replication page, the repository and the command that reproduces the comparison.

**domtest Phase 11** checks all of this, including one honesty rule: wherever the Compassionism row appears, the same design with its two unsourced mechanisms switched off (the octave wage raise, d19; the PTF/PTH inflation damping, d33) sits directly beneath it.

**After any engine change,** regenerate the comparison before releasing:

```
node harness.js testbed 500 a5 ref --json=a5.json
node harness.js testbed 200 a5 adv,st --json=a5.json
node harness.js frontdoor a5.json
```

The table states the engine version its figures came from, so a page-only release can keep them.

### What was added to `harness.js` (plan A5)

- **Testbed metrics:** poverty spells (ever poor, mean spell length, poor in 10 or more of 20 years; spells censored at the window); years in poverty per adult (the area under the headcount curve); employment and hours (earnings over the same adult's earnings with no labor response, i.e. hours at a fixed wage); real wage earnings; the price level in years 10 and 20 and the real value of $1 of cash or BU; a year-20 **disposable-income Gini on the OECD definition** (wages + conversion + cash transfers − the contribution), needed by the Hub's C30, and the same with in-kind cuts added; cost per point of poverty removed.
- **`node harness.js testbed <seeds> a5 [ref,adv,st] [--json=path]`**: the reporting upgrade in four tables (poverty; cost and efficiency; prices, work and distribution; groups in dollars), tax-financed at matched cost, with the octave raise (d19) and the damping (d33) on and off and the d26 hybrid at a = 0 and a = 1 beside every Compassionism result.
- **Person-year FGT₂ beside year 20** in `decomp`, `alts`, `match` and `frontier`.
- **d33 everywhere:** `match`, `frontier` and `alts` add damping-off rows for Compassionism. The damping scales exogenous inflation only, so where that is 0 (the reference) the rows would equal those shown; they are skipped with a note, and `unit` checks the equality.
- **`node harness.js frontdoor <a5.json> [index.html]`**: writes the front door's data.
- `giniOfArr()` and three tests: the d33 skip rule; spells, person-years and Gini on known vectors; the price path.

### Headline results (engine model, tax-financed at matched cost; reference 500 seeds, adverse and stress 200)

- **The year-20 measure flatters Compassionism.** Averaged over all 20 years, its FGT₂ cut is −3.21 at the reference against −4.46 in year 20, and −7.66 against −18.08 in the adverse environment. The framework model with the octave raise off cuts year-20 FGT₂ by 1.23 at the reference but raises it by 1.26 over the 20 years.
- **Per $1,000, averaged over 20 years,** Compassionism with its two unsourced mechanisms off still beats a matched basic income in every environment (0.16 against 0.14 at the reference, 0.16 against 0.06 adverse, 0.22 against 0.12 stress). At the reference a matched negative income tax does better on FGT₂ (0.20) while raising the share of adult-years in poverty from 55% to 81%.
- **More adults are ever poor under Compassionism** (72% against 68% with no program at the reference) because of the contribution, though for fewer years (9.1 against 11.0 per adult) and in shorter spells.
- **Hours fall** 4.9% under Compassionism, 9.0% under the basic income and 22.6% under the negative income tax (reference).
- **Disposable-income Gini at year 20:** 0.297 for Compassionism (engine) and 0.309 (framework) against 0.292 with no program; 0.268 and 0.261 with in-kind cuts counted. The Baseline's figure is close to that of the model's wage distribution, a lognormal with σ = 0.5 (Gini 0.276), which is not calibrated to US income inequality; so only the change between designs is informative, and the level cannot test the Hub's ≤0.25 target.

---

## v4.22, session 7: decomposing the testbed result, and the replication page moves here

Next-round session 7 (Sep 27, 2026). Released in v4.22. **The engine in `index.html` is unchanged and every shipped figure is bit-identical; the page changed only where it links to the replication page.** `validate` passes; `unit` passes (11 tests, 8 price-module tests, 4 labor-module tests, 6 session 5 tests and 11 testbed tests, 2 of them new); `domtest` passes all 85 checks (3 new, Phase 10). Tables and decisions: `session-7-handoff.md`. Raw output: `session-7-results.txt`.

### The replication page lives in this repository

`replication.html` replaces the Research Hub's `cco-ptf-simulation-replication.html`, which becomes a redirect (Hub ledger s1). Through v4.21 it was the only file outside this repository that had to change with every release, and its version labels went stale four times. Now:

- every label that names the engine version carries class `repl-ver`, and the page declares the version in `<meta name="sim-version">` and in its JSON-LD;
- **domtest Phase 10 fails if any of them differs from `META.VERSION`**, so a release that bumps `META` without the page fails CI;
- Phase 10 also checks the page's canonical address and that every `index.html` link to it points here.

**On each release:** change every `repl-ver` label (six), the `sim-version` meta tag and the JSON-LD `version` in `replication.html`, alongside `META.VERSION`.

The page's text is carried over from the Hub page; a token comparison finds nothing lost except the old toggle and banner labels. What changed is presentation: the simulation's palette, header and dark mode; a sticky section list with scrollspy and a section picker on phones; code and JSON blocks behind collapsible boxes with a Copy button; definitions on hover, focus or tap for 146 first uses of glossary terms; one panel per release in Version History, newest first (the detailed notes previously ran v3.1 to v4.6 and then v4.21 back to v4.7); links back to the Hub made absolute. Decisions d30–d32 cover the address, the headline figures and two metadata lines.

### What was added to `harness.js`

- **`FBS_BU_ONCE`** (dashboard i3-1). The engine's FBS gate reads the monthly basic cost after the CCO relief and then adds BU again; `true` reads the pre-relief cost, as the framework branch already does. Default `false` (the page).
- **The conversion switch now also covers the framework model's business-side conversion**, so `PATHWAY_OFF.conversion` turns off all conversion in both models.
- **Testbed reporting:** a targeting share (program dollars that close a shortfall before transfers ÷ program dollars) and design-neutral BLEI poverty beside the shipped definition (d28).
- **Financing:** a `hybrid` mode (transfers taxed, conversion rewards money-created at additionality a; d26 option c) and `buAtA` (d24 option b: output matched at a to a converted BU's face value as well as its reward).
- **Per-row engine-question switches** in `tbStudy` (`g: {FBS_BU_ONCE, PTH_APPR_CONSERVE}`), restored after each row.
- **`node harness.js testbed <seeds> decomp [ref,adv,st]`**: each channel off in turn at BU $1,200, tax-financed, CRN-paired, with a matched UBI.
- **`node harness.js testbed <seeds> alts [ref,adv,st]`**: Duke's d24–d29 follow-ups side by side, with each group's losses in dollars and poverty points (d29).

### Headline results (tax-financed, BU $1,200; reference 500 seeds, Adverse and Stress Test 200)

- **Two unsourced mechanisms with no cost in the ledger carry most of Compassionism's per-dollar edge.** The octave wage raise (d19) accounts for 45% of the engine model's FGT₂ cut at reference, 65% in Adverse and 48% in the Stress Test. The PTF/PTH inflation damping (i3-4), which lowers everyone's basket inflation for free, accounts for 21% in Adverse and 32% in the Stress Test (nothing at reference, which has no inflation).
- **With both off and the i3 fixes on, Compassionism still beats a matched UBI per dollar, by much less.** FGT₂ cut per $1,000: 0.22 against 0.15 at reference; 0.20 against −0.07 in Adverse; 0.40 against 0.08 in the Stress Test (engine model). In Adverse it was 1.79 with everything on.
- **The CCO relief and conversion buy little poverty reduction at their cost.** Turning the relief off halves the engine model's cost and loses 0.26 points of FGT₂ at reference (0.66 Adverse, 0.03 Stress Test). Turning conversion off saves $2,000–2,500 per adult-year at reference and in Adverse ($600 in the Stress Test) and moves FGT₂ by 0.1 point or less; in the framework model it improves FGT₂ (by 0.2 at reference and 1.3 in Adverse).
- **The i3 engine questions are small.** FBS counting BU twice (i3-1) is worth 0.09–0.24 points; the PTH appreciation double-count (i3-3) is within ±0.1.

---

## v4.22, session 6: the A4 policy testbed (harness-only)

Next-round session 6 (Sep 27, 2026). Released in v4.22. **Nothing in `index.html` changed, and every shipped figure is bit-identical.** `validate` passes; `unit` passes (11 tests, 8 price-module tests, 4 labor-module tests, 6 session 5 tests and 9 new testbed tests); `domtest` passes all 82 checks. Tables, sources and decisions: `session-6-handoff.md`. Raw output: `session-6-results.txt`.

### What was added to `harness.js`

- **Comparator presets** (`tbPresets`):
  - a universal basic income;
  - a negative income tax (G, t);
  - a public grocery network (a cut on the food component for a covered share, plus capital);
  - a one-time asset endowment below a wealth threshold;
  - X-Cents, as a flat adult daily exchange and as a community-work variant;
  - Compassionism in the engine and framework models, and CCO alone.

  Each is matched to Compassionism's gross cost by `tbMatch`.
- **One cost ledger.** Every program dollar at face value per adult-year, in year-0 dollars.
- **A financing switch.**
  - Tax: a flat contribution on wage earnings set from last year's cost ÷ base, capped at 90%, with an optional threshold `X` indexed to the basket and the treasury reported.
  - Money: every program dollar is new money, with transfer output-matching `aT`, price-cut efficiency `eP` and conversion additionality `a`.
- **Fairness rules applied to every design.**
  - One income effect ρ on every unconditional dollar, price-cut dollars included.
  - One elasticity (ε − ρ) on every change in the net return to work: contribution, phase-out, raises.
  - A design-neutral gate for the engine's BLEI-gated wage bonus.
- **Measures.**
  - Basket FGT₀–₂ at year 20 and over person-years.
  - Wealth poverty.
  - A group check: would-be participants, non-participants, PTH members, and bottom and top thirds by year-0 wage, each on resources, person-year basket FGT₀ and year-20 wealth poverty.
- **Per-row pathway switches in `tbStudy`**, so every Compassionism row can be shown with the octave wage bonus off (d19).
- **`tbUnitSuite()`**, run by `unit`. It checks that:
  - the hooks are inert, and `tbRun` with no comparator reproduces `priceRun` exactly;
  - an NIT at t = 0 is a UBI, and flat X-Cents is a UBI of $3,613.50;
  - the income effect is exactly ρ × UBI;
  - the treasury balances to within 5%;
  - money financing at aT = 1 adds no inflation;
  - the cost ledger is exact;
  - the per-row switch restores itself;
  - a threshold above every earner collects nothing.
- **`node harness.js testbed <seeds> match|frontier [ref,adv,st] [--pilot=N] [--models=...] [--fin=tax,money] [--X=N]`**.

### Sources

Public grocery: nyc.gov press release, Jul 27, 2026. It announces 30% off a core basket, projected to cut the average grocery bill by 15%, and a $70M capital budget for five stores. It is a promise, not an observed result, and it states no operating subsidy. The capital cost per covered adult-year ($140) rests on an unsourced shopper count and is swept.

### Headline results (seeds 1–500, 500 agents, tax-financed, reference environment)

- **At matched cost ($11,338 per adult-year), Compassionism (engine model) cuts year-20 basket FGT₂ by 4.46 points.** A UBI cuts it by 1.71 and an NIT (t 0.5) by 2.90. With the octave wage bonus off (d19), Compassionism's cut is 2.46.
- **In the Adverse Environment, Compassionism cuts FGT₂ by 18.05 (6.18 with the bonus off), while a matched UBI and NIT raise it** (+0.78, +8.24).
- **The framework model's own cost ($32,151 per adult-year) needs a 61% wage contribution.** Matched cash designs hit the 90% cap and run deficits.
- **Money-created, with transfers unmatched by output, every large design inflates.** Compassionism runs 18.6 points a year at a = 0 and 14.4 at a = 1; the UBI runs 22.8. The breakeven and price-neutral figures from sessions 3–5 hold only if BU and price cuts are financed outside money creation.
- **No design above about $1,000 per adult-year passes the no-group-worse-off check under tax financing.** Decision d29.
- **A contribution threshold at the basket line does not work at these costs.** With wages below $49,370 exempt, every design above about $3,600 per adult-year hits the 90% cap and runs an unfunded deficit.
- **Population size:** session 5's labor comparison at 5,000 agents (100 seeds) reproduces the 500-agent results: earnings to within 0.01 point, poverty to within 0.1 point.

---

## v4.22, session 5: the A2 carry-over and the large-N restudy (harness-only)

Next-round session 5 (Sep 27, 2026). Released in v4.22. **Nothing in `index.html` changed, and every shipped figure is bit-identical.** `validate` passes, `unit` passes (11 tests, 8 price-module tests, 4 labor-module tests and 6 new session 5 tests) and `domtest` passes all 82 checks. Tables, sources and decisions: `session-5-handoff.md`; raw output: `session-5-results.txt`.

### What was added to `harness.js`

- **Three restudy switches**, each off by default: `THETA_GATE = 'density'` reads SZH θ off the realised PTF share instead of the SZH coherence slider (claims ledger C08, dashboard d12); `PTH_MODE = 'housing'` applies PTH's 35% to the housing component only (d4); `DISC_BASE = 'pretax'` keeps PTF, PTH and CCO relief off the basket's 18% tax share (d5).
- **The joint run**: `priceRun()` takes a `labor` option, so the A2 price module and the A3 labor response run together.
- **`s5Neutral()`** (d18): the price-neutral point, the output per dollar of conversion reward at which endogenous inflation is zero. Additionality may exceed 1.
- **A λ_G = 1.41 sweep row**: the quantity-theory reading at US M2 velocity (FRED M2V, Q1 2026: 1.409).
- **`s5UnitSuite()`**, run by `unit`: the switches are inert at their defaults; the housing and pre-tax algebra reduces to the shipped chain where it should; skipping the tax share raises every discounted agent's cost and no one else's; the density gate gives θ = 0 below 55%; the joint run with zero coefficients is bit-identical to the price run alone; the neutral search finds a known root above 1.
- **`node harness.js restudy <seeds> lam|grid|labor [fi,adv,st] [rows]`**, and **`labor ... --env=ref,adv,st`**.

### Sourcing λ_G

λ_G (pass-through of unmatched new money to the general price level) stays at 1 in the reference and is now a sourced range rather than a placeholder. High end: under the quantity theory λ_G equals the velocity of the money conversion creates, and US M2 velocity is 1.409 (FRED, Q1 2026); McCandless and Weber (1995) find an almost-unity long-run correlation between money growth and inflation across 110 countries. Low end: De Grauwe and Polan (2005) find the relation weak in countries with inflation under 10%; 0.25 stays a logged placeholder. Transfer studies measure pass-through and additionality together, so they bound the product, not λ_G: Egger et al. (2022) find average price inflation of 0.1% from a transfer of over 15% of local GDP, attributed to slack capacity; Jordà et al. (2022) attribute about 3 points of 2021 US inflation to pandemic transfers, at the upper end of published estimates.

### Headline results

- **`price 500 be` reproduces session 3's breakevens exactly** and adds the price-neutral point: Full Integration 1.091 (engine) / 1.011 (framework); Adverse Environment 1.110 / 1.013; Stress Test 1.193 / 1.021.
- **The price-neutral point does not depend on λ_G** (engine: 1.091 at λ_G 0.25, 1 and 1.41), while the breakeven does (0.578, 0.964, none). It is the headline least exposed to the contested pass-through evidence.
- **Restudy, Full Integration, engine model** (seeds 1–500, 500 agents): the joint run moves the breakeven by 0.001. The three text-versus-engine corrections together (θ density gate, PTH housing only, discounts skip the tax share) raise wealth / BLEI / basket poverty with no price feedback from 26.3 / 20.4 / 9.7% to 31.5 / 23.2 / 12.2%, and lower the breakeven from 0.963 to 0.910. Wage indexation cuts basket poverty at the breakeven from 13.0% to 10.2%.
- **d19 confirmed at 500 seeds**: CCO alone's earnings edge over a matched-cost UBI is 2.69 points with the octave wage bonus and 0.05 without it (engine model).

---

## v4.22, session 4: A3 labor supply and a release workflow

Next-round session 4 (Sep 27, 2026). Released in v4.22. **Nothing in `index.html` changed, and every shipped figure is bit-identical.** `validate` passes, `unit` passes (11 tests, 8 price-module tests and 4 new labor-module tests) and `domtest` passes all 82 checks. Tables, sources and decisions: `session-4-handoff.md`; raw output: `session-4-results.txt`. Status and open decisions now live on the project dashboard.

### What was added

- **`LABOR`** (harness-only, off by default): each agent's wage earnings respond to unconditional support at rate ρ (0.16, NBER w32719, revised Aug 2026: individual income excluding the transfer fell about 16 cents per dollar received), to BU spent on the agent's own essentials at the same rate (inframarginal in-kind aid acts like cash: Hoynes & Schanzenbach 2009; the mental-accounting counter-evidence, Hastings & Shapiro 2018, is a swept sensitivity), and to the program's raises through the uncompensated elasticity ε − ρ (ε = 0.33, Chetty 2012). Conversion proceeds enter as a rent (δ = 0) or as project time that displaces wage time (δ = 1).
- **`p.ubi`**: a flat cash transfer to every adult, for the matched-cost UBI comparator. Counted as cash income in the income and basket measures.
- **`laborRun()`, `laborStudy()`, `laborUnitSuite()`** and **`node harness.js labor <seeds> [head|sweep|all]`**.
- **`.github/workflows/release.yml`**: when `META.VERSION` names a version with no tag, it tags the commit that first set that version and publishes a release with that version's Release Notes section. Run it by hand with a version to backfill one (for example 4.20).

---

## v4.22, session 3: A2 sweeps and the breakeven report (harness-only)

Next-round session 3 (Sep 26, 2026). Released in v4.22. **Nothing in `index.html` changed, and every shipped figure is bit-identical.** `validate` passes, `unit` passes (11 tests, plus 8 price-module tests, 2 of them new) and `domtest` passes all 82 checks. Full tables, sources and decisions: `session-3-handoff.md`; raw output: `session-3-results.txt`.

### What was added to `harness.js`

- **Breakeven search** (`s3BaseS`, `s3Point`, `s3Breakeven`, `s3Config`). CRN makes the mean over a fixed set of seeds an exact function of every input, so breakeven additionality is found by a bracketed secant search instead of read off a coarse grid. Each breakeven comes with a 95% bootstrap interval over seeds, the share of seeds above the tolerance at that point, and the additionality at which 90% of seeds are within it.
- **`S3_ROWS`**, the one-at-a-time sweep, and **`s3StabArms()`**, the recession stabilizer arms.
- **`node harness.js price <seeds> <section> [fi,adv,st]`**, new sections: `be`, `inert`, `sweep`, `corners`, `stab`.
- **Decision S3-1** (price module only; inert by default). When program-induced raises are treated as unmatched (`aw` < 1), only each year's *change* in the aggregate premium enters as new money: a raise paid from revenue with no added output passes through to prices once. `awLevel: true` restores session 2's reading, which re-created the whole premium as money every year.

### Headline results

Breakeven additionality: the smallest share of conversion-created currency that must be matched by new output to keep the program's endogenous inflation within 0.5 point (D3) / 1 point a year. Seeds 1–500; reference settings, including λ_G = 1, a logged placeholder.

| Scenario | Engine model | Framework model |
|---|---|---|
| Full Integration | 0.964 / 0.837 | 0.989 / 0.966 |
| Adverse Environment | none / 0.900 | 0.994 / 0.975 |
| Stress Test | 54.9% vs 60.0% | 65.6% vs 78.2% | 90.6% vs 82.6% | 23.8% | 72.6% |

- The 95% intervals are within ±0.004. A 5,000-agent check (50 seeds) gives the same Full Integration figures.
- "None": at a = 1 the Adverse Environment still has 0.52 point a year from PTH appreciation credited as cash (N13). Counted as matched, the engine breakeven is 0.892.
- The breakeven depends mostly on λ_G. At λ_G = 0.25, Full Integration needs 0.578 (engine) and 0.922 (framework).
- It also depends on whether program-induced raises are productivity. If they are not (S3-1), no a keeps Full Integration within tolerance: they add about 2 points a year.
- **Staying within tolerance still costs poverty when wages are nominal.** At the 0.5-point breakeven, Full Integration's basket poverty is 13.4% against 9.9% with no price feedback (engine), and 7.0% against 5.1% (framework).
- **Recession stabilizer.** It adds 3–5% more BU over the run. The extra inflation scales with the unmatched share: at a = 0 it raises the year-after-recession rate by 0.3–7.4 points; at a = 1 it changes it by less than 0.05 point. It moves the 0.5-point breakeven by 0.01 or less.
- **Under capacity supply** the essentials channel is negligible: θ from 0 to its high end changes inflation by 0.02 point a year or less.

**A correction to the session 2 notes.** "Housing θ changes nothing under capacity supply" holds only approximately. Program demand exceeds capacity in year 0, which causes a one-year essentials price rise of up to 0.9%. It does not change the breakeven to three decimals.

---

## v4.22, session 2: basket split, framework conversion model and the price module (harness-only)

Next-round session 2 (Sep 26, 2026). Released in v4.22. **Nothing in `index.html` changed, and every shipped figure is bit-identical.** `validate`, `unit` (11 tests, plus 6 new price-module tests) and `domtest` (82 checks) pass, and `ledger 5 identity` is identical in all 35 runs. Full tables, sources and decisions: `session-2-handoff.md`.

### What was added to `harness.js`

- **`CFG.BASKET`** (decision N10). The $49,370 basket by component, from the MIT Living Wage Calculator (Feb 15, 2026 data, 1 adult, 0 children). `LIVING_WAGE_ANNUAL` is the unweighted mean of the 51 state living wages × 2,080 hours ($49,369.82, checked). The site asks not to be scraped, so the components are fitted from 8 state pages read by hand: food 9.0%, housing (with utilities) 27.6%, medical 6.9%, transportation 19.6%, civic 6.6%, internet and mobile 3.1%, other 9.2%, taxes 18.0%. Essentials (food, housing, medical) are 43.5%.
- **`PTF_MODE`** (D4): `'shipped'` (12% + 4% × SZH off the whole basket), `'food30'`, `'food62'`.
- **`CONVERSION_MODEL = 'framework'`** (N1–N4): one BU budget of 12 × BU a year, spent on essentials at the agent's own prices; businesses convert the BU they accept at `FW.bizRate` (placeholder 3×) and pay the premium over a cash sale to all agents by wage the next year; unspent BU go to projects and are converted by participants within octave capacity.
- **`PRICE`**, the A2 issuance and price module, driven by `priceRun()` and `priceStudy()`: an essentials index P_E, a general index P_G, COLA read off the endogenous headline rate, wage indexation to P_G, poverty lines deflated by the index (D2), floor write-offs as unmet need (N5), and program raises matched by output (N7).
- **`NEXT_ROUND`**, the D1 consumption rule (0.9 of all cash surplus) as a profile. The global switches keep their v4.21 defaults so the checks still test `index.html`.
- **`priceUnitSuite()`**, run by `unit`: zero issuance leaves the index at exactly 1 and the run bit-identical; fully matched issuance does the same in both conversion models; inflation falls monotonically as additionality rises; the framework model's BU and payout accounting balances.
- **`node harness.js price <seeds> [section]`**: `basket`, `d1`, `framework`, `ptf`, `breakeven`, `sens`, `all`.

### Findings that need a decision

- **The shipped PTH cut exceeds the whole housing component.** 35% of the basket is $17,280; MIT's housing component is $13,631 (127%). The shipped PTF cut (12% of the basket, $5,924) is 133% of the food component. Every discount is also taken on the basket's 18% tax share.
- **COLA feeds inflation when additionality is low.** With BU indexed and wages nominal, created money grows as a share of income. Adverse Environment, engine model, a = 0: 11.7 points a year with D6's COLA, 5.2 without it.
- **What is left at full additionality is PTH appreciation.** Liquid PTH appreciation has no counterparty and is counted as unmatched new money; it adds 0.24–0.52 points a year at a = 1.

### Headline results

D1, Full Integration, seeds 1–500 (nominal lines, no price module): wealth poverty 15.3% → 24.9%, BLEI poverty 12.4% → 19.7%, basket poverty 9.9% (unchanged), unmet need 3.7% of basket cost. Reduction against the matched Baseline under D1: 54.4% / 62.0% / 78.9% (wealth / BLEI / basket).

Preliminary breakeven additionality (seeds 1–200; λ_G = 1, a logged placeholder; capacity supply):

| Scenario | Engine model (0.5 pt / 1 pt) | Framework model (0.5 pt / 1 pt) |
|---|---|---|
| Full Integration | 0.964 / 0.837 | 0.989 / 0.966 |
| Adverse Environment | none / 0.898 | 0.993 / 0.974 |
| Stress Test | 0.870 / 0.547 | 0.979 / 0.936 |

These depend on λ_G. At λ_G = 0.25 the Full Integration figures are 0.578 / 0.065 (engine) and 0.922 / 0.832 (framework). Session 3 sweeps the inputs.

---

## v4.22, session 1: issuance ledger and a consumption-base switch (harness-only)

Next-round session 1 (Sep 26, 2026). Released in v4.22. **Nothing in `index.html` changed, and every shipped figure is bit-identical.** `validate`, `unit` and `domtest` (82 checks) pass.

### What was added to `harness.js`

- **`LEDGER`** (reporting only, off by default). When set, `runYear()` adds each money flow it already computes to a per-year tally: BU credited, spent and expired; CCO relief; conversion gross, tax and net, by rate tier; PTF and PTH cost reductions; PTH equity routing and appreciation; wealth-floor absorption; wage income and basket cost. It draws no random number and writes nothing a dynamic reads.
- **`node harness.js ledger <seeds> [section]`**, the A1 issuance ledger of the Next Round Plan. Sections: `identity` (the ledger on and off give identical `runScenario()` output on every scenario), `scenarios`, `tiers`, `years`, `deciles`, `framework` (derived arithmetic, labeled as such), `all`, and `consume` (not in `all`).
- **`SURPLUS_CONSUMPTION_BASE`** (`'wage'` by default, v4.21's behaviour). `'cash'` applies `SURPLUS_CONSUMPTION_SHARE` to all cash surplus: wage + net conversion + PTH liquid appreciation − basket − PTH equity routing, taken at the end of the agent's year. Inert while the share is 0.

### Headline results (`node harness.js ledger 500`)

Full Integration, per participant per year, year-0 dollars: CCO relief $8,723, conversion net of tax $3,249 (mean rate 4.21×), conversion tax $838, BU expired $285. As shares of cash income: relief and conversion 14.2%, PTF and PTH cost reductions 8.7%, wealth-floor absorption 2.5%. The floor absorbs 13.3% of cash income in the matched Baseline and 32.8% in the shipped Baseline @3%. Bottom-decile floor absorption in Full Integration is $257,338 per agent over 20 years (v4.21: about $259,000 at 200 seeds).

### A correction to the v4.21 notes

v4.21 found that "the poverty findings are robust to" the consumption rule. That held because conversion proceeds were always saved: the switch consumed a share of wage surplus only. Applied to all cash surplus (`node harness.js ledger 200 consume`):

| Rule | FI wealth poverty | FI BLEI poverty | Reduction vs matched Baseline (wealth / BLEI) |
|---|---|---|---|
| Shipped (save everything above the basket) | 15.3% | 12.5% | 69.6% / 74.4% |
| 0.9 of wage surplus (v4.21's option B) | 19.6% | 14.7% | 64.2% / 71.7% |
| 0.9 of all cash surplus | 25.0% | 19.9% | 54.3% / 61.7% |

Near-poverty participants whom conversion lifts just above the basket spend most of that margin under the second rule. The wealth levels and the headline reductions both depend on the consumption rule. See `session-1-handoff.md` for the rule adopted for the next round and the alternatives.

---

## v4.21 Release Notes

v4.21 investigates the v4.19–v4.20 figures that read counter-intuitively, fixes the one bug that turned up, and reruns the headline figures with ten times the population per run. It also closes three open items.

**The seed-42/Full Integration/20yr regression is unchanged** (1,975d · $570,661 · 0.518 · 15.8% · 88.8%). The fix acts only where inflation and CCO are both on: Adverse Environment and Stress Test move, and every 0%-inflation preset is bit-identical. `harness.js validate` now asserts all six presets at seed 42, and that a legacy switch reproduces v4.20's two inflation presets. `domtest.js`, now 82 checks, passes in full; the 4 new Phase 9 checks each fail against v4.20.

**Flagged as a decision:** the relief fix below is applied, with v4.20's rule kept behind `RELIEF_PRICE_LEGACY` in `harness.js`. It changes every figure from a run with inflation, including the published Adverse Environment and COLA tables.

### The bug: CCO relief under inflation

v4.19 made CCO's cost relief scale with BU: 20% of the basket at $1,200 (Option B). The $1,200 is a year-0 amount. The rule compared nominal BU with it and applied the resulting share to the nominal basket, which already rises with prices. Two errors followed:

- **Without COLA, the relief kept its full real value.** It stayed a flat 20% of a basket that grows with prices. The v4.19 notes and the COLA tooltip said an unindexed BU erodes; in the relief channel, which carries most of BU's value, it did not.
- **With COLA, inflation was counted twice.** The indexed BU raised the share itself, to 20% × the price index.

The share now reads BU in year-0 dollars: effective BU divided by the price index that `mainLoopCostUSD` and COLA already use. Relief dollars are then proportional to nominal BU. At 0% inflation the index is exactly 1.

Relief share of the basket for a participant outside PTF and PTH (Adverse Environment settings, recessions off, seed 1; `node harness.js v421 200 relief`):

| | Year 1 | Year 5 | Year 10 | Year 15 | Year 20 |
|---|---|---|---|---|---|
| v4.20, no COLA | 20.0% | 20.0% | 20.0% | 20.0% | 20.0% |
| v4.20, COLA | 20.0% | 21.4% | 23.1% | 24.8% | 26.3% |
| **v4.21, no COLA** | 20.0% | 18.7% | 17.3% | 16.1% | **15.2%** |
| **v4.21, COLA** | 20.0% | 20.0% | 20.0% | 20.0% | **20.0%** |

**What moved** (seeds 1–500, 500 agents, final year; v4.20 from its release notes or `RELIEF_PRICE_LEGACY`):

| Scenario | Wealth poverty | BLEI poverty | Median wealth | Median BLEI |
|---|---|---|---|---|
| Adverse Environment, v4.20 | 38.42% | 34.92% | $169,911 | 606d |
| **Adverse Environment, v4.21** | **40.33%** | **36.63%** | **$146,364** | **526d** |
| Stress Test, v4.20 | 61.18% | 59.14% | −$10,000 | 16d |
| **Stress Test, v4.21** | **62.00%** | **59.90%** | −$10,000 | 16d |
| CCO Only, adverse environment, v4.20 | 53.50% | 51.87% | −$2,175 | 38d |
| **CCO Only, adverse environment, v4.21** | **56.26%** | **54.64%** | **−$8,916** | **26d** |
| Full Integration at 3%, v4.20 | 28.84% | 25.88% | $343,488 | — |
| **Full Integration at 3%, v4.21** | **31.13%** | **27.46%** | **$306,660** | 1,079d |

The last pair feeds the headline table's "both at 3%" comparator, which falls from 59.7% / 63.3% (wealth / BLEI poverty) to 56.5% / 61.0%.

**COLA, redone** (seeds 1–200, 500 agents, wealth poverty, final year; `node harness.js v421 200 relief`):

| Scenario | v4.20: no COLA → COLA | COLA's gain | v4.21: no COLA → COLA | COLA's gain |
|---|---|---|---|---|
| Adverse Environment (2%) | 38.49% → 35.30% | −3.19 pp | 40.38% → 37.72% | −2.66 pp |
| Adverse Environment at 5% | 55.51% → 44.62% | −10.89 pp | 60.01% → 53.50% | −6.51 pp |
| Full Integration at 5.5% | 42.14% → 30.37% | −11.77 pp | 47.04% → 40.09% | −6.95 pp |

v4.19's COLA table overstated COLA's benefit by about 20% at 2% inflation and about 70% at 5–5.5%. Without COLA, outcomes are also worse than it reported, because BU now loses real value as the notes said it did.

**Stabilizer defaults, rechecked** (`node harness.js stabilizer 300 neutral`):

| Environment | Participants' excess, no stabilizer | After the hub's ×1.20 | Shock-neutral multiplier |
|---|---|---|---|
| Full Integration + recessions | 3.08 pp | 1.49 pp | ×1.35 (unchanged) |
| Adverse Environment | 2.31 pp | 1.19 pp | **×1.40** (v4.20: ×1.35) |
| CCO Only + recessions | 4.00 pp | 2.01 pp | ×1.35 (unchanged) |
| Stress Test | 2.46 pp | 1.64 pp | **×1.55**, ×1.57 unrounded (v4.20: ×1.50) |

Without COLA, each step of the multiplier buys less real relief as prices rise, so the two inflation environments need more. At 5,000 agents and 100 seeds Stress Test's unrounded value is ×1.58, which rounds to ×1.60; the two agree within their seed noise. `STAB_NEUTRAL_MULT` and `STAB_NEUTRAL_K` are calibrated to the reference settings at 0% inflation, and stand.

### Why several figures read counter-intuitively

`node harness.js v421 200 <section>` reproduces every table in this section (seeds 1–200, 500 agents).

**1. BLEI poverty "ends above year 0" (12.4% against 10.3%).** It rises and then falls, and year 20 sits on the way down (section `hump`):

| Year | 0 | 1 | 3 | 5 | 7 | 10 | 15 | 20 | 24 | 30 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BLEI poverty (policy-neutral rules) | 10.3% | 13.4% | 19.8% | 22.0% | 22.6% | 21.8% | 18.1% | 13.4% | 10.2% | 6.7% | 3.3% |
| … CCO participants (scenario rules) | 0.5% | 6.5% | 13.0% | 15.5% | 16.1% | 15.3% | 11.4% | 7.1% | 4.6% | 2.2% | 0.5% |
| … non-participants | 9.5% | 20.1% | 31.4% | 35.8% | 37.6% | 38.0% | 35.8% | 31.4% | 27.2% | 21.1% | 12.5% |

- **The cause is the calibration logged in v4.17.** Two-thirds of agents start with wage income below the basket, the model has no consumption response, and deficits run straight to the floor. Wages then grow 1–3% a year and flows turn positive. BLEI poverty peaks around year 7 and returns to its year-0 level at year 24.
- **The year-20 BLEI-poor are mostly different people from the year-0 BLEI-poor.** 1.8% of agents are poor at both points; 8.4% only at year 0; 10.7% only at year 20. Year-0 BLEI poverty is low starting wealth, drawn independently of wage. Year-20 BLEI poverty is a persistent deficit: 73% of the year-20 poor are at the wealth floor, and 77% ran a cash deficit that year.
- **By group at year 20:** non-participants outside PTH 36.5% (contributing 6.5 of the 12.5 points); CCO participants outside PTH 8.9% (5.6 points); non-participants in PTH 11.1% (0.5 points); CCO participants in PTH **0.0%**.
- **The 0.0% is by construction.** `agentBLEI()` adds one month of BU's food value ($990 at $1,200) and divides by the CCO+PTH daily cost ($31.67): 31.3 days, above the 30-day line, whatever the member's wealth or wage. It holds at any BU from $1,152. This follows the BLEI paper's definition, which counts a month of flows toward coverage, and is now disclosed in Known Limitations.

**2. Median wealth of about $530,000.** Agents spend exactly their own (discounted) basket, so every dollar above it is saved (section `decile` of `node harness.js saving 200`):

| Final-wealth decile | Wage income, 20 yr | Basket cost, 20 yr | Final wealth | 20-yr saving rate |
|---|---|---|---|---|
| D1 | $510,730 | $852,844 | −$9,687 | −60% |
| D3 | $804,410 | $753,117 | $160,611 | 12% |
| D5 | $1,062,792 | $726,459 | $454,921 | 35% |
| D8 | $1,564,582 | $704,540 | $1,002,793 | 57% |
| D10 | $2,661,219 | $691,852 | $2,151,221 | 75% |

Across the population the 20-year saving rate is 43.8%. The US personal saving rate averaged 3.4–5.6% a year in 2022–2025 (BEA, FRED series PSAVERT; a share of disposable income, where this engine has no taxes). Basket cost barely varies across deciles, so income differences pass almost entirely into wealth. Two side effects: the bottom decile's deficits (about $259,000 per agent over 20 years) are absorbed by the wealth floor, and long-horizon wealth grows without bound (logged in v4.6).

Consuming a share of the surplus above the basket (`SURPLUS_CONSUMPTION_SHARE`, harness-only; section `sweep`):

| Share consumed | FI saving rate | FI wealth poverty | FI BLEI poverty | FI median wealth | Reduction vs matched Baseline (wealth / BLEI) |
|---|---|---|---|---|---|
| 0 (shipped) | 43.8% | 15.3% | 12.5% | $528,341 | 69.5% / 74.4% |
| 0.50 | 21.7% | 16.8% | 13.2% | $321,474 | 67.5% / 73.7% |
| 0.75 | 10.6% | 18.1% | 14.0% | $212,227 | 65.7% / 72.7% |
| 0.90 | 4.0% | 19.6% | 14.7% | $139,516 | 64.2% / 71.7% |

**The poverty findings are robust to this assumption; the wealth levels are not.** At a saving rate in the observed range, median wealth falls by three-quarters while the reduction against the matched Baseline falls by about five points. Agents near the poverty lines have little surplus, so how the surplus is spent barely reaches them. Basket poverty does not move, because it compares income with the basket. A consumption rule is logged as a decision below.

**3. Recessions add less housing distress in harsher environments** (participants: Adverse Environment 2.31 pp and Stress Test 2.46 pp, against 3.08 pp for Full Integration; `stabilizer 300 neutral`). Outcomes are bimodal, and in a harsher environment more participants are already in distress, so fewer are within reach of the line (section `margin`):

| Environment | Participants in distress, no recession | Within one recession of distress | Excess distress | Excess ÷ calm distress |
|---|---|---|---|---|
| Full Integration + recessions | 10.6% | 2.5% | 3.05 pp | 29% |
| CCO Only + recessions | 16.5% | 3.2% | 4.01 pp | 24% |
| Adverse Environment | 23.2% | 1.3% | 2.24 pp | 10% |
| Stress Test | 35.4% | 1.1% | 2.38 pp | 7% |

Excess distress in points measures how many people a recession tips over the line, not how hard an environment is. The stabilizer studies use it correctly, as the target a stabilizer must offset.

**4. The shock-neutral multiplier is ×1.35 in every $1,200 environment, and ×1.50 at $900.** Neutrality takes a roughly fixed amount of extra relief, about 6–8% of the basket, whatever the environment (section `neutralbu`, Full Integration + recessions):

| BU | No stabilizer | Neutral multiplier (unrounded) | Extra BU at neutrality | Extra relief |
|---|---|---|---|---|
| $900 | 3.59 pp | ×1.520 | $468/month | 7.8% of the basket |
| $1,200 | 3.05 pp | ×1.366 | $439/month | 7.3% |
| $1,500 | 2.51 pp | ×1.263 | $395/month | 6.6% |
| $1,800 | 1.80 pp | ×1.207 | $373/month | 6.2% |

The recession-depth distribution and the relief per BU dollar are the same in every environment; the environment changes only how many participants sit at the margin. That scales the excess and the offset together, so the neutral point stays put. A smaller BU needs a larger multiplier to supply the same dollars.

**5. Stabilizers that leave recession years better than calm ones** (participants at ×1.50: −1.43 pp; non-participants with emergency enrollment at 100% take-up: −8.38 pp, both from v4.19). This is arithmetic, not a defect. At ×1.35 the relief is 27% of the basket, about $13,300 a year at year-0 prices; a typical engine recession cuts income by about 12%, about $4,800 for a median earner. With no price response and no budget constraint, a transfer larger than the loss makes the recession year better. Emergency enrollment also reaches every eligible non-participant, not only those who lost income.

**6. Seed 42's High Automation poverty fell in v4.20 (28.8% → 27.8%) although automation risk rose.** Two steps were folded into one row (section `ha42`): the sampler switch alone, a new random realisation, moved it to 25.6%; the recalibration then raised it to 27.8%. With the sampler held fixed, raising the weight from 0.47 to 0.63 never lowers wealth poverty, in 200 of 200 seeds.

**7. Poverty lines under inflation.** Wealth poverty uses a nominal $25,000, and BLEI divides nominal resources by the year-0 daily cost, so under inflation both read slightly low. Measured (section `lines`), the effect is small, because few agents sit near either line:

| Scenario | Final price index | Wealth poverty, nominal line → real line | BLEI poverty, year-0 cost → current cost |
|---|---|---|---|
| Baseline @3% (shipped comparator) | 1.754 | 71.4% → 72.4% | 70.4% → 70.9% |
| Adverse Environment (2%) | 1.317 | 40.4% → 41.0% | 36.8% → 37.3% |
| Full Integration @3% | 1.509 | 31.2% → 32.0% | 27.5% → 29.0% |

Disclosed in Known Limitations; not changed. The price index is also recomputed each year from that year's damped rate, so as PTF adoption grows, earlier years' prices are in effect revised down; the resulting annual inflation is slightly below the damped rate.

### The large-N study

**Two axes.** The project's earlier "N=5,000" studies were 5,000 seeds of 500 agents. The headline figures through v4.20 were 500 seeds of 500 agents. Averaging over seeds narrows the confidence interval, but only a larger population per run can reveal effects that depend on population size. This study holds seeds at 500 and raises the population to 5,000 agents (`--agents=5000`, new), then checks population size directly.

**Headline** (`node harness.js largen 500 headline --agents=5000`; means across runs, ±95% CI):

| Figure | 500 agents | 5,000 agents |
|---|---|---|
| Wealth poverty | 15.27% ±0.14 | 15.26% ±0.05 |
| BLEI poverty | 12.43% ±0.13 | 12.48% ±0.04 |
| Basket poverty (net) | 9.92% ±0.12 | 9.93% ±0.04 |
| Median wealth | $528,624 ±2,948 | $527,328 ±900 |
| Median BLEI | 1,834d ±11 | 1,827d ±3 |
| Gini (EDC-adjusted) | 0.518 | 0.519 |
| Year 0: wealth / BLEI / basket poverty | 37.8% / 10.3% / 66.3% | 37.8% / 10.4% / 66.4% |
| Reduction vs shipped Baseline (wealth / BLEI) | 78.6% / 82.4% | 78.7% / 82.3% |
| Reduction vs matched Baseline | 69.7% / 74.6% | 69.7% / 74.5% |
| Reduction vs both at 3% | 56.5% / 61.0% | 56.5% / 61.1% |
| Reduction vs year 0 (wealth) | 59.6% | 59.6% |
| Highest measure (net basket vs shipped Baseline) | 87.9% | 87.9% |

**Confirmed.** Every Full Integration figure agrees within its interval at the two sizes.

**Presets** (`largen 500 presets`, wealth poverty / BLEI poverty / median wealth):

| Preset | 500 agents | 5,000 agents |
|---|---|---|
| CCO Only | 24.16% / 21.11% / $391,095 | 24.09% / 21.05% / $390,510 |
| High Automation (25 yr) | 29.16% / 26.65% / $340,928 | 29.17% / 26.66% / $339,975 |
| Adverse Environment | 40.33% / 36.63% / $146,364 | 40.37% / 36.68% / $145,206 |
| Stress Test | 62.00% / 59.90% / −$10,000 | 62.09% / 59.99% / −$10,000 |
| Weaker settings @ reference environment | 33.29% / 30.39% / $250,339 | 33.34% / 30.44% / $249,902 |
| Baseline, adverse environment (3%) | 83.56% / 82.89% / −$10,000 | 83.67% / 83.00% / −$10,000 |

**Population size** (`largen 500 popsize`: Full Integration, about 1.25 million agent-runs at each size):

| Agents per run | Seeds | Wealth poverty | BLEI poverty | Median wealth | Gini |
|---|---|---|---|---|---|
| 250 | 5,000 | 15.27% ±0.06 | 12.49% ±0.06 | $527,982 ±1,311 | 0.5169 |
| 500 | 2,500 | 15.22% ±0.06 | 12.44% ±0.06 | $527,503 ±1,350 | 0.5177 |
| 1,000 | 1,250 | 15.31% ±0.06 | 12.52% ±0.06 | $527,364 ±1,353 | 0.5183 |
| 2,000 | 625 | 15.32% ±0.06 | 12.53% ±0.06 | $526,835 ±1,275 | 0.5187 |
| 5,000 | 250 | 15.24% ±0.06 | 12.46% ±0.06 | $527,023 ±1,340 | 0.5187 |
| 10,000 | 125 | 15.29% ±0.06 | 12.49% ±0.06 | $526,497 ±1,433 | 0.5187 |
| 20,000 | 63 | 15.28% ±0.07 | 12.49% ±0.07 | $527,833 ±1,453 | 0.5186 |

**Two finite-population effects, neither in a headline poverty figure:**

- **Gini reads slightly low in small populations.** The sample Gini formula is biased down by a factor of (n − 1)/n: 0.2% at 500 agents, which matches the 0.001–0.002 rise at 5,000 in every scenario. Multiplying by n/(n − 1) would remove it; logged, not applied, because it would move every documented Gini.
- **A median can be biased where a large share of agents sits at the wealth floor.** The median then lands in a sparse part of the distribution, and a mean of run medians overstates it at 500 agents. The matched Baseline's median wealth is $26,546 ±2,399 at 500 agents but $19,678 ±800 at 5,000; its median BLEI 88d against 65d. CCO Only in the adverse environment: −$8,916 against −$10,000. Poverty rates in the same runs agree.

**With recessions on, seeds matter more than agents.** Every agent in a run shares one recession path, so Adverse Environment's interval on basket poverty narrows only from ±0.31 to ±0.25 at ten times the population. Studies of shock scenarios should add seeds, not agents.

**Run time**, for planning: a 20-year run costs about 40–50 µs per agent on one CPU core, so 500 seeds × 5,000 agents takes about 100 seconds per scenario.

### Open items closed

- **CCO/PTH pathway decomposition** (Good First Issues, v4.14 (b)). `node harness.js pathways 200` switches off one channel at a time (harness-only `PATHWAY_OFF`, paired runs). Contribution of each channel, full run minus the run without it (±95% CI):

  | Channel | Median wealth | Wealth poverty | BLEI poverty |
  |---|---|---|---|
  | CCO cost relief | +$141,921 ±1,833 | −7.47 pp | −6.14 pp |
  | Octave wage bonus | +$134,215 ±1,492 | −6.20 pp | −6.20 pp |
  | Octave advancement | +$120,466 ±1,675 | −5.76 pp | −5.48 pp |
  | BLEI-gated wage bonus | +$87,826 ±566 | −1.66 pp | −1.07 pp |
  | PTH cost reduction (and the equity it funds) | +$57,368 ±2,204 | −2.33 pp | −1.07 pp |
  | Conversion proceeds | +$53,091 ±1,072 | −2.70 pp | −2.21 pp |
  | PTH equity routing and appreciation | −$2,192 ±299 | 0.00 pp | 0.00 pp |
  | All four CCO channels together | +$325,749 ±2,512 | −20.97 pp | −19.05 pp |

  - **Cost relief and octave-driven wages carry most of CCO's effect.** Conversion proceeds, the channel with no production constraint, carry about a sixth of the wealth effect: BU is credited once a year.
  - **The channels overlap.** The four CCO channels' single effects sum to $123,944 more than their joint effect, because octave advancement feeds both wages and conversion rates.
  - **PTH's equity routing slightly lowers reported wealth.** It moves savings into `acreEquity`, which no metric reads, and returns only the liquid share of appreciation (the v4.16 accounting decision).
- **Stored regression fixtures** (v4.12 item (a), in part). `validate` asserts every preset at seed 42, and `RELIEF_PRICE_LEGACY`'s reproduction of v4.20, and exits 1 on any mismatch.
- **The tables v4.20 left unreproduced.** Regenerated at N=500 on the v4.21 engine, as it asked:

  `node harness.js extreme 500` (per 10,000; housing distress in percent):

  | Scenario | Extreme poverty | Economic | SMI | Voluntary | Housing distress |
  |---|---|---|---|---|---|
  | Year 0 (every scenario) | 22.0 | 16.1 | 5.5 | 0.4 | 16.9% |
  | Baseline @3% (shipped) | 73.1 | 67.2 | 5.5 | 0.4 | 70.1% |
  | Baseline @0% (matched) | 49.1 | 43.2 | 5.5 | 0.4 | 45.1% |
  | CCO Only | 22.4 | 16.5 | 5.5 | 0.4 | 17.3% |
  | Full Integration | 13.1 | 9.2 | 3.5 | 0.4 | 9.6% |
  | Adverse Environment | 40.0 | 36.0 | 3.5 | 0.4 | 37.6% |
  | Stress Test | 62.4 | 57.5 | 4.5 | 0.4 | 60.0% |

  Full Integration is 40.3% below year 0, 82.0% below the shipped Baseline and 73.3% below the matched one. CCO Only is 2.0% above year 0.

  `node harness.js stress 500`:

  | Scenario | Wealth poverty | BLEI poverty | Basket poverty (net) | Median wealth |
  |---|---|---|---|---|
  | Full Integration | 15.3% | 12.4% | 9.9% | $528,624 |
  | Adverse environment @ reference settings | 40.3% | 36.6% | 60.8% | $146,364 |
  | Weaker settings @ reference environment | 33.3% | 30.4% | 26.7% | $250,339 |
  | Stress Test (both) | 62.0% | 59.9% | 80.6% | −$10,000 |
  | Baseline under the adverse environment (3%) | 83.6% | 82.9% | 95.9% | −$10,000 |

  The v4.17 reading holds: the adverse environment alone multiplies Full Integration's wealth poverty by 2.6, the weaker settings alone by 2.2, and together they compound.

### Decisions for Duke

- **A consumption rule.** Agents consume exactly their basket and save 44% of income in aggregate. The options: **(A)** keep it and state it wherever wealth levels are quoted; **(B)** consume a fixed share of the surplus, set so the aggregate saving rate matches the BEA range (about 0.9 on the sweep above); **(C)** a consumption function that rises with income and wealth, sourced from the literature. (B) or (C) would move every wealth figure, most poverty figures by 1–5 points, and the seed-42 regression, and would bound the long-horizon growth logged in v4.6. The harness switch is there to test it.
- **Poverty lines under inflation.** Keep them nominal (status quo, effect under 1.5 points) or deflate both lines by the price index. Low stakes; it matters only where the headline comparison uses the Baseline at 3%.

### What did NOT get done, and why

- **Nothing else in the engine changed.** The octave sampler, wage-linked automation risk, θ on realised PTF density and the other logged decisions remain open.
- **No layout check.** v4.21 changes page text and a tooltip, not layout.
- **The Gini small-sample correction** is logged above, not applied.

### Regression: seed 42 / Full Integration / 20yr, v4.20 → v4.21

Unchanged: 1,975d · 13.2% BLEI poverty · $570,661 · 0.518 · 15.8% · 88.8% · 24.2% EDC · 8.8% at the floor.

**Seed 42, every preset** (wealth poverty / median wealth / median BLEI / Gini):

| Preset | v4.20 | v4.21 |
|---|---|---|
| Full Integration | 15.8% / $570,661 / 1,975d / 0.518 | unchanged |
| CCO Only | 24.8% / $427,239 / 1,283d / 0.575 | unchanged |
| Traditional Welfare (3%) | 68.8% / −$10,000 / 8d / 0.824 | unchanged |
| High Automation | 27.8% / $382,123 / 1,351d / 0.603 | unchanged |
| Adverse Environment | 35.0% / $218,851 / 819d / 0.646 | **36.8% / $205,005 / 723d / 0.658** |
| Stress Test | 59.0% / −$10,000 / 16d / 0.781 | **59.8% / −$10,000 / 16d / 0.785** |

---

## v4.20 Release Notes

v4.20 answers three external audits of v4.19 (Grok, Claude Sonnet and ChatGPT, run from the same prompt), checked claim by claim, plus an internal audit. **Duke signed off on the four decisions they raised**: recalibrating `automationRisk`, CI with jsdom as a dev dependency, the engine-split question, and tagged releases. Each is below, with the path taken.

**The seed-42/Full Integration/20yr regression moves, once, by design** (1,965d · $559,223 · 0.534 · 16.6% · 88.5% → **1,975d · $570,661 · 0.518 · 15.8% · 88.8%**). The cause is the sampler change in the first section: the same population statistics, a different random realisation. At N=500 Full Integration is unchanged within noise. `harness.js validate` now asserts both the new figures and that a legacy switch reproduces v4.19 exactly. `domtest.js`, now 78 checks, passes in full; the 10 new Phase 8 checks each fail against an unmodified v4.19 page, without throwing.

### automationRisk: recalibrated, and decoupled from the rest of agent construction

**The data (Sonnet's lead, verified).** `plotly/datasets`' `job-automation-probability.csv` (MIT-licensed repository) has 702 rows. This session checked **every row** against Frey & Osborne's own appendix (pp. 57–72, text extracted from the Oxford Martin PDF), and all 702 match on SOC code, rank and probability. That completes step (a) of the occupation good-first-issue, beyond the spot-check it asked for. Employment weights are the file's `numbEmployed` column (May-2016 BLS OES). Its `employed_may2016` column has two rows (47-1011, 13-1023) where an occupation title sits in place of a number; `numbEmployed` is numeric throughout.

**The finding, restated.** Sonnet compared 66% of employment at or above 0.5 with the model's 47%. The 47% is actually F&O's headline figure: the share of 2010 US employment with a probability *above 0.7*. Since v4.3 it has served as the weight of a Beta(6,1)/Beta(1,6) mixture, a different quantity. The `drawAutomationRisk()` comment also called it a share "of occupations"; it is a share of employment, and the in-app v4.3 entry already said so. Compared like for like, the model is still low on every measure:

`node harness.js automation 1 fit` (data: employment-weighted):

| Variant | Mean risk | Share > 0.7 | Share < 0.3 | Share ≥ 0.5 | Largest gap to the data's CDF (tenths) |
|---|---|---|---|---|---|
| **Data** | **0.592** | **0.501** | **0.293** | **0.660** | — |
| v4.19: weight 0.47 | 0.479 | 0.415 | 0.468 | 0.471 | 0.189 |
| weight 0.50 | 0.500 | 0.442 | 0.442 | 0.500 | 0.160 |
| **v4.20: weight 0.63 (mean-matched)** | **0.592** | **0.555** | **0.328** | **0.625** | **0.051** |
| weight 0.66 (likelihood fit, shapes fixed) | 0.614 | 0.583 | 0.300 | 0.655 | 0.079 |
| free shapes: 0.706 × Beta(4.02,1) + Beta(1,11.03) | 0.590 | 0.538 | 0.294 | 0.663 | 0.084 |

**Why 0.63.** `automationRisk` enters `runYear()` linearly: the wage drag is the displacement rate × risk. The mean therefore sets the population's aggregate drag, and 0.63 reproduces it. It also sits closest to the data's distribution of the candidates tested. The likelihood fit with fixed shapes gives 0.659, but it overshoots the mean, because the shapes' within-group means (0.857 / 0.143) sit a little inside the data's (0.835 / 0.120). Freeing the shapes improves the likelihood without improving the fit to the distribution, and it changes the v4.3 design as well as the weight. **Flagged as the one judgement call in this item:** 0.66 would also be defensible, and the sweep below shows what it would change.

**The sampler, and why it mattered more than the weight.** `beta()` draws through `gamma()`'s rejection loop, which consumes a variable number of random numbers. `automationRisk` is drawn mid-construction, so changing the weight flipped some agents' mixture component, shifted the draw count, and re-streamed every later draw: wealth, wage, λ and the latent participation uniforms. **Under v4.3–v4.19, changing the weight from 0.47 to 0.63 moved seed 42 to 15.0% / $583,843 even with automation off**, although Full Integration never reads `automationRisk`. Both components now use their exact inverse CDF, Beta(a,1) = U^(1/a) and Beta(1,b) = 1 − (1 − U)^(1/b): two draws per agent, whatever the weight. The weight now reaches only runs with AI automation on. `domtest.js` checks that every other latent trait of every agent is identical at weights 0.47 and 0.63. The switch itself shifted every later draw once, which is why the regression moved.

**What moved.** `node harness.js automation 500 sweep` (seeds 1–500, mean across runs, final year):

| Scenario | Variant | Wealth poverty | BLEI poverty | Median wealth | Median BLEI |
|---|---|---|---|---|---|
| High Automation (25 yr) | v4.19 | 25.87% | 23.53% | $417,131 | 1,454d |
| | weight 0.47, new sampler | 25.70% | 23.33% | $416,280 | 1,457d |
| | **v4.20 (0.63)** | **29.16%** | **26.65%** | **$340,928** | **1,196d** |
| | 0.66 | 29.80% | 27.26% | $327,737 | 1,148d |
| Adverse Environment | v4.19 | 35.86% | 32.63% | $206,930 | 733d |
| | weight 0.47, new sampler | 35.87% | 32.54% | $207,718 | 735d |
| | **v4.20 (0.63)** | **38.42%** | **34.92%** | **$169,911** | **606d** |
| Stress Test | v4.19 | 58.69% | 56.64% | −$9,948 | 18d |
| | **v4.20 (0.63)** | **61.18%** | **59.14%** | **−$10,000** | **16d** |
| Full Integration (AI off) | v4.19 | 15.30% | 12.58% | $526,629 | 1,824d |
| | **v4.20, any weight** | **15.27%** | **12.43%** | **$528,624** | **1,834d** |

Read the rows in pairs. The sampler change alone (v4.19 against "weight 0.47, new sampler") moves nothing beyond noise. The recalibration moves every scenario with AI on: roughly +3.5 points of wealth poverty and −18% median wealth under High Automation. The model had understated automation exposure since v4.3.

**What remains.** Risk is still drawn independently of wage. Across the 702 occupations, log median wage and automation probability correlate at **−0.65** (employment-weighted). The model therefore spreads automation's wage drag evenly across the wage distribution, where the data concentrate it among lower earners. This is now the substance of the occupation good-first-issue (Model Architecture Feedback).

### A validation check that was measuring noise

After the sampler change, `nonpart` ("non-participants no worse off than the all-mechanisms-off baseline, +2pp") failed 4/5. The check compared the ~45 non-participants in one arm with the **whole population** of the other: a random subset against everyone, with a per-seed standard error near 7pp against a 2pp tolerance. Run over VAL_SEEDS plus seeds 1–10, that difference ranges from −21pp to +3pp **in both v4.19 and v4.20**. v4.19's five seeds happened to fall inside the tolerance, and v4.20's new realisation put seed 3456 at +2.9pp.

The claim is about the same people, and the two arms are common-random-numbers paired: one latent population, eight draws per agent-year. The check now reads the first arm's non-participants' own outcomes in both arms. Over 20 seeds that difference is **never positive** (mean −8.7pp; −8.3pp on the v4.19 engine), and the worst of the five VAL_SEEDS is −4.9pp. The tolerance is unchanged. **Flagged as a decision:** it changes what the check measures, to what its name always said it measured.

### Accessibility (Sonnet's finding, extended)

- **Names.** No slider, On/Off pair or seed field had a programmatic name. Every slider and the seed field now point at their visible label with `aria-labelledby`, and every On/Off pair is a `role="group"` named the same way.
  - Where a label contains an ⓘ, the ⓘ is kept out of the name.
  - Sonnet suggested an `aria-label` on each On/Off button ("Enable PTF: On"). Group labelling was used instead, because an `aria-label` would replace visible button text such as "On (1.618×)".
- **Values.** Sliders announce their displayed value ("$1,200", "×1.35") through `aria-valuetext`, which `sv()` keeps current.
- **Tooltips.** All 29 were hover-only.
  - `initA11y()` makes each of the 15 ⓘ icons focusable, with its tooltip text as its name. It describes each of the 14 tooltip-bearing buttons and links with theirs.
  - The text is read from `data-tip` at load, so nothing is written twice.
  - Tooltips open on `:focus-visible`, so a mouse click on a preset does not pin its tooltip open.
- **Focus (internal finding).** `input[type=range]{outline:none}` removed every slider's focus indicator, with nothing in its place. Sliders now show a focus ring.
- **Limits.** jsdom renders nothing, so Phase 8 confirms the focus rules exist, not how they look. A keyboard pass in a real browser, and one with a screen reader, remain worth doing after deploy.

### Smaller fixes

- **Seed readout (Sonnet, extended).** A shared link with `?seed=abc` showed "NaN". The internal check found a worse case: `?seed=12abc` showed "12" while the run was unseeded, because a number field discards the whole string. The readout now shows what `initRNG()` will read.
- **Extreme poverty in JSON (Grok).** The card and CSV already called it an overlay; the JSON block, the one parsers read without the notes, gains a `basis` key saying so. It is a new key; existing keys are unchanged.
- **Attribution card (Grok).** It now says each bar is a compound effect through FBS, octave and wage growth, so the bars need not sum to the combined gain. The pathway decomposition itself remains open (v4.14 item (b)).
- **Cost anchors (Grok).** The run-configuration line shows both anchors, $49,370/yr for the wealth loop and $68.33/day for BLEI, FBS and PTH sizing, read from `CFG`. With AI on, it also shows the high-risk share.
- **LHS export (internal).** Its note and comments said the design suits Sobol and Morris analysis. Both need their own sampling designs. An arbitrary sample like this one supports first-order indices by RBD-FAST or the delta method, and regression or surrogate methods. Checked with SALib 1.6 on the Ishigami function, RBD-FAST from an LHS recovers the analytic first-order indices, to about ±0.08 at this export's 100 points and ±0.02 at 1,000. Recipe under Model Architecture Feedback.
- **Stale figures.** The PTF-cap tooltip's "seed 42 reaches 53.4%" is now 52.2%; with the cap, the year-0 draw is 17.8% and the run ends at 18.0% (v4.19: 19.0% throughout). A note heads the in-app Cumulative Bug Fixes: each entry's figures are as of its own release.
- **Staleness (Sonnet).** `harness.js`'s header gains the v4.19 entry it lacked. This file's signature line said v4.16, and Code Contributions said "56 checks as of v4.18". `harness.js validate` labelled its figures "v4.5/v4.6/v4.7".
- **README (internal).** Its licence section still read "Released under CC BY 4.0" for everything, stale since the v4.8 split; it now states the split, and its citation matches `META.CITATION`.

### Found by the first CI run: a race in `domtest.js` since v4.13

The first GitHub Actions run failed two Phase 7 checks that pass here on every Node version tried, including the runner's (22.23.3). The failing check's own output gave the cause. The page reported the seed-42 **Full Integration** figures ($570,661; CCO Only $427,239) where an **Adverse Environment** run was expected (harness: $262,968).

- **The false premise.** `domtest.js`'s header said the page is evaluated after jsdom's DOMContentLoaded and load events have fired, so the page's auto-run never starts. That was never true: at evaluation `readyState` is still "loading", and both events fire afterwards.
- **What that caused.** The page's DOMContentLoaded handler re-applied the reference preset, and its load handler started the seed-42 reference run 300ms later.
- **Why it only failed on CI.** Here, Phase 7's run was still going at 300ms, so the page's own guard ignored the auto-run. On the faster runner, the run finished first and the auto-run replaced its results. The second failure, the exports check, followed from the first.
- **Scope.** Every check since v4.13 ran in the same kind of window, so the race was latent from then. It surfaced now because v4.20's runs are fast enough to beat 300ms on a GitHub runner.

`makeWindow()` now never registers the page's load handler, and runs its DOMContentLoaded handler only when a check dispatches that event itself, as Phases 5 and 8 already do. A new Phase 8 check fails if a test window's auto-run ever fires. **No page code changed for this;** the page behaves as intended in a browser, where the auto-run is the reference run readers see on opening it.

### The Automatic Stabilizers panel, reworded (Duke's request)

Display text only.

- **The panel.** A one-line introduction now says what the panel is, and that every lever is off by default and needs recessions or inflation switched on.
- **Labels.** Each label says what the control does, e.g. "Raise BU during recessions", "How the raise is set", "Trigger: smallest income loss that counts".
- **Hints.** Each hint says when the control acts and what its default means, e.g. "×1.35 means BU is 35% higher in a triggered year".
- **COLA spelled out.** It reads "cost-of-living adjustment (COLA)" in the panel, its tooltip, the run warning, the run-configuration line and the Shock Response card.
- **What did not change.** Control ids, URL parameters, CSV row labels and JSON keys, so shared links and parsers keep working.

### The four decisions, and the path taken

1. **automationRisk:** recalibrated and resampled, as above.
2. **CI.** `.github/workflows/checks.yml` runs `harness.js validate`, `harness.js unit` and `domtest.js` on every push and pull request. `package.json` pins jsdom 30.1.1 as the only dev dependency and carries no version field, so there is one fewer place to bump.
   - `validate` used to print its figures and always exit 0, so a CI job could never have failed on a regression. It now exits 1 on any mismatch.
   - ESLint and Prettier (ChatGPT) were not added: a style pass over ~5,300 lines of deliberately ES5 code would be churn, and CI already catches syntax and runtime errors, because domtest.js executes the page.
3. **The engine split (Grok, ChatGPT): its goal adopted, its form not.** The goal is one engine instead of two copies that can drift apart. The form, `engine.js` plus a build step to reassemble the page, would make the shipped file the output of another source, breaking download-and-open, the OSF archive and this file's "single HTML file, no build tooling" rule. Instead, Phase 8 compares the source of every function the page and `harness.js` share, with comments and whitespace removed.
   - 35 functions must be identical.
   - Five differ by design and are listed with reasons (harness-only switches in `runYear()` and `drawAutomationRisk()`; display fields in `getTier()`; a renamed local in `agentBLEI()`; guard order in `incomeBasketMetrics()`). Each is covered by a behavioural check.
   - Any new or edited shared function that drifts now fails CI.
4. **Tagged releases** (open since v4.15) are a repository action that a chat session cannot take. From v4.20, on GitHub:
   - open **Releases → Draft a new release**, and type `v4.20` under **Choose a tag** (it is created on publish);
   - set the target to `main`, the title to `v4.20`, and paste the summary at the top of these notes;
   - optionally attach `index.html`, then **Publish release**.

   Earlier versions stay reachable through the commit history.

### What the audits said that did not hold, or was already done

| Claim | From | Finding |
|---|---|---|
| Title, JSON-LD and `META` say v4.13; this file stops at v4.13; 4,093 lines | ChatGPT | An old snapshot. All said 4.19; this file ran through v4.19; `index.html` was 5,302 lines |
| Enable the Issues tracker | ChatGPT | Already enabled, with no open issues |
| `innerHTML` injection (XSS) risk | ChatGPT | Checked: URL parameters reach only `parseFloat`, `'0'`/`'1'`, an input's value and `textContent`. No path from input to markup |
| CSP header | ChatGPT | GitHub Pages cannot set headers, and a meta-tag policy would need `'unsafe-inline'` for the page's inline handlers, which removes most of its value. Not adopted |
| The UI freezes on long runs; use Web Workers | Grok | Runs already yield to the browser once per simulated year (`setTimeout` per step), and Cancel works mid-run. Not needed now |
| Extract a data-driven RNG schedule | Grok | `runYear()`'s draw count is machine-checked (8 per agent-year) since v4.16. The weak point was construction, fixed for `automationRisk` above; the rest is logged below |
| Unit tests for pure functions | Grok, ChatGPT | Done: `unitSuite()`, 15 tests, run against both files |
| Guided tour or progressive disclosure | Grok | Declined for now: a sizeable UI change that cannot be checked visually in this environment. Logged as an enhancement |
| Modernise `var` to `const`/`let` | Grok | Declined: churn across the engine for no behavioural gain, and the parity check requires both files to change in lockstep |
| Saltelli export | Grok | Not built. The existing LHS supports first-order indices (above); total-order indices need a Saltelli design, logged below |

### Checks

- **`harness.js validate`** asserts eight figures for v4.20, and the same eight for v4.19 under `AUTOMATION_SAMPLER_LEGACY` at weight 0.47.
- **`harness.js unit`**: 11 tests run; four are skipped because those functions exist only in the page.
- **`domtest.js` Phase 8 (10 checks):**
  - accessible names;
  - tooltip reachability, and idempotent initialisation;
  - `aria-valuetext`;
  - the seed readout;
  - the JSON basis;
  - all 15 unit tests against the page;
  - source parity, and identical `drawAutomationRisk()` sequences;
  - agent construction independent of the weight;
  - the paired non-participant check;
  - a test window never starts the page's load-time reference run (see "Found by the first CI run", below).
- **Earlier phases.** Phase 2's and Phase 4's pinned seed-42 figures moved with the regression, including the inflation-matched Baseline ($49,876 / 48.2%; v4.19 $13,612 / 50.8%). Phase 3's six internal-consistency checks pass.
- **Stabilizer defaults rechecked.** `node harness.js stabilizer 300 neutral` gives:

| Environment | Participants' excess, no stabilizer | After the hub's ×1.20 | Shock-neutral multiplier |
|---|---|---|---|
| Full Integration + recessions | 3.08 pp (v4.19: 2.99) | 1.49 pp (1.45) | ×1.35 (unchanged) |
| Adverse Environment | 2.34 pp (2.40) | 1.06 pp (1.09) | ×1.35 (unchanged) |
| CCO Only + recessions | 4.00 pp (3.83) | 2.01 pp (1.83) | ×1.35 (unchanged) |
| Stress Test | 2.50 pp (2.59) | 1.57 pp (1.65) | ×1.50, ×1.51 unrounded (unchanged) |

`STAB_NEUTRAL_MULT` and `STAB_NEUTRAL_K` stand.

**Headline figures refreshed** (`node harness.js headline 500`; v4.17 values in brackets):
- **Wealth poverty:** Full Integration 15.3%. That is a 78.6% reduction against the shipped Baseline [78.7%], 69.7% against the inflation-matched one [69.7%], and 59.6% against year 0 [59.5%].
- **BLEI poverty:** reductions of 82.4% [82.2%] and 74.6% [74.4%]. It still ends above its year-0 level: 12.4% against 10.3% [12.6% against 10.3%].
- **Highest measure:** net basket poverty against the shipped Baseline, 87.9% [87.8%].
- **Other figures:** median wealth $528,624 [$526,629]; 66.3% of agents start in basket poverty [66.6%].

The v4.17 decision to reconcile the papers' 98% figure is unaffected.

### What did NOT get done, and why

- **Wage-linked automation risk.** It needs a design choice about how to draw occupation or risk conditional on wage, and a restudy. Logged, with the −0.65 correlation as its starting point.
- **Other construction draws** still use rejection sampling: `octaveShape`'s Beta(2,5). Any change to their parameters re-streams construction in the same way. Beta(2,5) is exactly the second-smallest of six uniforms, a fixed six draws, but switching would move the regression again. Logged.
- **Figures from v4.17–v4.19 that are not reproduced here.** Extreme-poverty tables and the stress decomposition move for runs with AI on, and slightly for all runs through the new realisation. Regenerate them with `node harness.js extreme 500` and `stress 500`. Each earlier release's tables stay as that release's record.
- **Visual verification.** No real-browser keyboard or screen-reader pass was possible here. Phase 8 checks the attributes and CSS rules, not the experience.

### Regression: seed 42 / Full Integration / 20yr, v4.19 → v4.20

| Metric | v4.19 | v4.20 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,975d | +10d |
| BLEI poverty | 13.6% | 13.2% | −0.4 |
| Median wealth | $559,223 | $570,661 | +$11,438 |
| Gini (EDC-adj.) | 0.534 | 0.518 | −0.016 |
| Wealth poverty | 16.6% | 15.8% | −0.8 |
| System Stability | 88.5% | 88.8% | +0.3 |
| Avg EDC | 24.9% | 24.2% | −0.7 |
| Pinned at Wealth Floor | 10.6% | 8.8% | −1.8 |

Every row is the same engine and population statistics on a different random realisation. At N=500 Full Integration's wealth poverty is 15.30% (v4.19) against 15.27% (v4.20).

**Seed 42, every preset** (wealth poverty / median wealth / median BLEI / Gini):

| Preset | v4.19 | v4.20 |
|---|---|---|
| Full Integration | 16.6% / $559,223 / 1,965d / 0.534 | 15.8% / $570,661 / 1,975d / 0.518 |
| CCO Only | 25.8% / $386,836 / 1,164d / 0.588 | 24.8% / $427,239 / 1,283d / 0.575 |
| Traditional Welfare (3%) | 71.0% / −$10,000 / 7d / 0.854 | 68.8% / −$10,000 / 8d / 0.824 |
| High Automation | 28.8% / $463,313 / 1,711d / 0.595 | 27.8% / $382,123 / 1,351d / 0.603 |
| Adverse Environment | 37.4% / $258,045 / 950d / 0.639 | 35.0% / $218,851 / 819d / 0.646 |
| Stress Test | 56.0% / −$10,000 / 19d / 0.771 | 59.0% / −$10,000 / 16d / 0.781 |

If you track a regression baseline across versions, restart it from v4.20.

---

## v4.19 Release Notes

v4.19 adds **automatic stabilizers**, requested by Duke: the Research Hub's crisis protocols, built as opt-in levers and calibrated for poverty reduction. It also changes one engine rule at Duke's decision, so that **CCO's cost relief scales with the BU issued**, and it rewords the **Poverty by Five Measures** card for clarity.

**The seed-42/Full Integration/20yr regression is unchanged** (1,965d · $559,223 · 0.534 · 16.6% · 88.5%). Every new lever is off by default and draws no random number. The new relief rule equals the old flat 0.80 exactly at the $1,200 reference, so every $1,200 preset is bit-identical. **Stress Test ($900 BU) moves**; its figures are below. `harness.js validate` reproduces the regression, and `domtest.js`, now 68 checks, passes in full. Against an unmodified v4.18 page, Phase 7 fails (it exits early and reports eight failures) while the 56 earlier checks still pass.

### Where the design comes from

Appendix G of the Research Hub's Integrated Implementation Roadmap sets out crisis protocols. Each maps onto the engine as follows:

| Protocol | Research Hub text | In the engine |
|---|---|---|
| Recession | GDP decline >2% for two quarters → increase basic units 20% within 72 hours, relax requirements | Trigger: a recession year whose population income loss is at least a threshold (default 2%; the engine has no GDP, and every engine recession cuts income 5–30%). Increase: a fixed multiplier, or one scaled to the income loss. "Relax requirements": emergency enrollment of non-participants |
| Natural disaster | Preload emergency units, suspend expiration | Suspended BU expiry while triggered. Disasters themselves are not modelled |
| Inflation surge | CPI >5% → COLA adjustments to basic units | BU indexed to the basket's price index above an inflation trigger (default 0%, i.e. always; the hub's 5% is marked on the slider) |

### A decision that changed on closer reading, and what Duke chose

The scoping study recommended settling "monthly BU tranches" before calibrating, because `runYear()` annualises wages (×12) but credits one allocation of the BU setting per simulated year. Building it showed that was not the right fix on its own. Through v4.18, BU reached a household two ways: conversion proceeds, credited once a year, and a flat 20% cost relief whenever BU > 0. So **the BU amount mattered only through conversion.** The Research Hub glossary describes BU as redeemable at PTF businesses for essential goods, which is a cost-relief effect.

`node harness.js stabilizer 300 decision`:

| Option | Seed 42: wealth poverty / median wealth / BLEI / Gini | Stress Test, seed 42 | Participants' excess distress, no stabilizer / hub ×1.20 | Shock-neutral multiplier |
|---|---|---|---|---|
| v4.18 engine (flat relief) | 16.6% / $559,223 / 1,965d / 0.534 | 53.2% / −$10,000 | 2.99 / 2.61 pp | ×2.35 |
| A: 12 allocations a year (not adopted) | 9.2% / $1,190,066 / 4,077d / 0.388 | 41.6% / $150,307 | 0.29 / 0.06 pp | ×1.25 |
| **B: relief scales with BU (shipped)** | **16.6% / $559,223 / 1,965d / 0.534** | **56.0% / −$10,000** | **2.99 / 1.45 pp** | **×1.35** |

Option A more than doubles median wealth and scales twelvefold the conversion channel, which has had no production or treasury constraint since v4.0. **Duke chose Option B.** CCO's cost factor is now `1 − min(CCO_RELIEF_CAP, CCO_RELIEF_AT_REF × effective BU / CCO_RELIEF_REF_BU)`, i.e. 20% of the basket at $1,200, proportional above and below it. `CCO_RELIEF_CAP` = 0.50 is a placeholder with no source; it binds only from $3,000 of effective BU (the BU slider tops out at $1,800). Conversion is still credited once a year. `harness.js` keeps `CCO_RELIEF_FLAT` and `BU_ALLOCATIONS_PER_YEAR` as harness-only switches for before/after comparison; both default to the shipped engine.

### The levers

All act through a per-year **effective BU** inside `runYear()`, which replaces `p.bu` at every read: allocation, the 3× cap, FBS, the BLEI check behind the wage-growth bonus, and now the cost relief.

- **Recession BU increase** (`p.stab`): fixed multiplier `p.stabMult`, or scaled, 1 + `p.stabK` × income loss (`p.stabSev`), in any recession year whose loss is at least `p.stabThresh`. The trigger reads the current year's shock; what a data lag costs is measured below, in the harness only.
- **Suspended expiry** (`p.stabSusp`): unspent BU carries over while triggered, up to the 3× cap.
- **Emergency enrollment** (`p.emerg`, `p.emergTakeup`): while triggered, a non-participant whose latent CCO uniform lies below partRate + take-up × (1 − partRate) receives the CCO cost relief for that year. The uniform is drawn at construction and now kept on the agent (`a.uCCO`), so take-up is deterministic. Enrollees do not enter octave advancement or conversion. **The 50% take-up default is a placeholder with no source.**
- **COLA** (`p.cola`, `p.colaThresh`): BU × (1 + inflation)^year, the index `mainLoopCostUSD` uses, when the inflation slider is above the trigger. Inflation is a constant rate in this engine, so the trigger applies to the whole run.

None draws a random number; `domtest.js` checks that every lever on draws exactly as many as every lever off, so stabilizer arms stay common-random-number paired. CCO Only mirrors all of them, because they are CCO settings.

**Reporting.** A new **Shock Response** card shows this run's recession years, the years the stabilizer fired, and the extra BU as a share of the base allocation. Its button runs a **30-seed paired study**:
- each seed is run with recessions off and on, under no stabilizer, the hub's ×1.20 and your settings;
- the measure is excess housing distress in recession years (the v4.18 measure), for participants and non-participants, plus the excess expected extreme poverty it implies;
- it then searches for the shock-neutral multiplier for your settings (false position from ×1 and ×2, widening to ×3 and ×4, bisecting when refinements stall, to a ±×0.025 bracket), with a button that sets the slider to it.

`harness.js shockStudy()` is the same code; domtest checks the two agree exactly. BU amounts are reported only as shares of the base allocation, not dollars, because of the once-a-year crediting above.

### "Optimal" is a target, not the peak of a curve

Returns to a larger increase are close to linear, and the engine has no price response to BU issuance (NEEC note 9) and no budget constraint. So a larger increase never looks worse, and the model cannot test whether it is inflationary. The default is therefore defined, as Duke settled, as **shock-neutral for participants**: the smallest multiplier that brings CCO participants' excess housing distress in recession years to zero.

### Results at the reference settings

`node harness.js stabilizer 300 rules` (Full Integration + recessions, seeds 1–300, 500 agents, 20 years; excess = recession years minus the same seed with recessions off):

| Rule | Participants (pp) | Non-participants (pp) | Excess extreme poverty (/10k) | Extra BU (% of base) |
|---|---|---|---|---|
| No stabilizer | 2.99 | 4.29 | 3.11 | — |
| Hub: ×1.20 when income falls ≥2% | 1.45 | 4.29 | 1.97 | 3.0% |
| Hub ×1.20, 2-quarter detection lag (study only) | 1.87 | 4.29 | 2.28 | 2.2% |
| ×1.30 | 0.58 | 4.29 | 1.33 | 4.5% |
| **×1.35 (default)** | **0.11** | 4.29 | 0.98 | **5.2%** |
| ×1.40 | −0.37 | 4.29 | 0.62 | 6.0% |
| ×1.50 | −1.43 | 4.29 | −0.17 | 7.5% |
| ×1.35, one-year data lag (study only) | 1.44 | 4.29 | 1.96 | 4.9% |
| ×1.35, held one year after (study only) | 0.04 | 4.29 | 0.92 | 7.7% |
| ×1.50 when income loss ≥10% | −0.02 | 4.29 | 0.88 | 5.1% |
| ×1.50 when income loss ≥15% | 1.85 | 4.29 | 2.26 | 2.1% |
| Scaled, +2.75% per 1% loss (default +2.8%) | 0.09 | 4.29 | 0.96 | 5.2% |
| Scaled, +3% per 1% loss | −0.22 | 4.29 | 0.73 | 5.7% |
| ×1.35 + expiry suspended | −0.58 | 4.29 | 0.46 | 5.2%* |
| ×1.35 + emergency enrollment, 50% take-up | 0.11 | −1.93 | −0.32 | 8.1% |
| ×1.35 + emergency enrollment, 100% take-up | 0.11 | −8.38 | −1.66 | 10.9% |
| Always-on raise, same 20-year budget as ×1.50 (study only) | 1.37 | 4.30 | 1.91 | 7.5% |

\*Carried-over BU is not counted as new issuance, which flatters this row. The shock-neutral point is ×1.36 unrounded (×1.35 on the slider) and +2.8% per 1% income loss, at about 5% of the 20-year BU budget.

`node harness.js stabilizer 300 neutral` (the in-page search):

| Environment | Participants' excess, no stabilizer | After the hub's ×1.20 | Shock-neutral multiplier |
|---|---|---|---|
| Full Integration + recessions | 2.99 pp | 1.45 pp | ×1.35 |
| Adverse Environment | 2.40 pp | 1.09 pp | ×1.35 |
| CCO Only + recessions | 3.83 pp | 1.83 pp | ×1.35 |
| Stress Test | 2.59 pp | 1.65 pp | ×1.50 (×1.52 unrounded) |

**What this tells a reader:**

1. **The hub's +20% is in the right range.** It offsets about half of a recession's rise in housing distress for participants; about +35% offsets all of it at the reference settings, and about +50% under the weaker Stress Test settings.
2. **Timeliness matters for the trough.** A trigger on annual data (one-year lag) leaves 1.44 pp of excess distress, against 0.11 for a timely one at the same multiplier. A two-quarter detection lag on the hub rule costs about a quarter of its effect.
3. **A stabilizer protects the trough; a permanent raise protects the level.** With the same 20-year budget as ×1.50, an always-on raise leaves 1.37 pp of excess distress in recession years, against −1.43 for the triggered rule.
4. **Thresholds can target cost.** ×1.50 only when income falls ≥10% reaches neutrality at about the same cost as ×1.35 in every recession, because it concentrates the money on deeper recessions.
5. **Non-participants are out of reach of a BU increase.** Their 4.29 pp is untouched by every multiplier. Emergency enrollment reaches them through the cost relief; at 50% take-up it more than offsets their rise, because the relief at ×1.35 (27% of the basket) exceeds a typical recession's income loss.

### COLA

`node harness.js stabilizer 300 cola` (final year, seeds 1–300):

| Scenario | Wealth poverty | Basket poverty (net) | Housing distress | Extreme poverty (/10k) | Median wealth |
|---|---|---|---|---|---|
| Adverse Environment (2%), no COLA | 35.8% | 50.6% | 32.9% | 35.4 | $206,713 |
| … COLA, always | 32.7% | 45.6% | 29.6% | 32.2 | $246,261 |
| … COLA, hub trigger (>5%) | unchanged: the trigger never fires at 2% | | | | |
| Adverse Environment at 5%, no COLA | 52.7% | 71.7% | 50.7% | 52.5 | $3,239 |
| … COLA, always | 41.9% | 55.6% | 38.5% | 40.8 | $132,273 |
| Full Integration at 5.5%, no COLA | 42.2% | 45.7% | 39.6% | 41.9 | $144,093 |
| … COLA, always or hub trigger | 30.2% | 27.3% | 24.5% | 27.4 | $314,017 |

The hub's trigger is strict (>5%), so at exactly 5% it does not fire. An unindexed BU loses about a third of its real value over 20 years at 2% inflation.

### What moved

Only runs at a BU other than $1,200. Of the documented figures, that is the Stress Test rows (N=500, `node harness.js stress 500` and `extreme 500`):

| Stress Test, seeds 1–500 | v4.18 | v4.19 |
|---|---|---|
| Wealth poverty | 56.8% | 58.7% |
| BLEI poverty | 54.9% | 56.6% |
| Basket poverty (net) | 72.3% | 73.7% |
| Median wealth (mean of run medians) | −$9,407 | −$9,948 |
| Extreme poverty (/10k) | 57.4 | 59.2 |
| Housing distress | 54.6% | 56.5% |

The v4.17 stress decomposition's "weaker settings @ reference environment" row uses the same $900 BU and moves too: wealth poverty 32.0% → 33.3%, BLEI poverty 29.3% → 30.4%, basket poverty 25.7% → 26.8%, median wealth $269,562 → $249,105. Every other row of the v4.17 and v4.18 tables reproduces unchanged. OAT and LHS runs that vary BU also move, since BU now moves the relief as well as conversion.

### Poverty by Five Measures, reworded

Display text only. Row keys, CSV labels and the JSON key (`povertyByFourMeasures`) are unchanged, so existing parsers keep working.

- **Headings:**
  - the title asks one plain question: the share of people in poverty at year 0 and in the final year, and how Your Settings compares;
  - the columns read "Change since year 0" and "Difference from Baseline".
- **Definitions** use words rather than symbols, e.g. "net wealth below $25,000", and "savings, income and BU cover fewer than 30 days of basic living costs".
- **Notes:**
  - a new opening says what each group of measures asks;
  - the flow notes explain why relative income poverty can rise when most incomes rise together;
  - the extreme-poverty notes are split into shorter sentences.

**Flagged as a decision rather than polish:** none of the figures, definitions or constants changed.

### Checks

`domtest.js` Phase 7 (12 checks):
- controls and defaults (all off; ×1.35 and +2.8%);
- URL round-trip;
- inertness when off or unable to fire;
- an unchanged RNG draw count with every lever on;
- page/harness agreement on every lever;
- the relief rule bit-identical to v4.18 at $1,200 and different at $900;
- emergency enrollment only in triggered years, for exactly the expected agents;
- a seed-42 Adverse Environment run with every lever on against `harness.js`, for Your Settings and CCO Only;
- the card, warnings and run-configuration line;
- the in-page study against `harness.shockStudy()`;
- the "set slider" button;
- both exports.

The Phase 3 internal-consistency suite, including BU-monotonicity, still passes 6/6.

### What did NOT get done, and why

- **Disasters are not modelled.** They are localized, larger and shorter than recessions, and often destroy assets. A disaster shock needs sourced incidence and loss data. The suspended-expiry lever is ready for it.
- **The zone premium is a reader note, not a result.** The engine has no geography, and there is little evidence on how residency payments move people. The note sits in the Shock Response card.
- **Four figures remain placeholders or inherited:** the 50% emergency take-up, the 50% relief cap, the 20%-at-$1,200 relief carried over from earlier releases, and once-a-year conversion crediting.
- **Timing variants (lag, hold) are harness-only.** The page ships the timely trigger.
- **No browser layout check this session.** The new sidebar panel and card reuse existing classes and styles, and `domtest.js` verifies behaviour, not appearance.

### Regression: seed 42 / Full Integration / 20yr, v4.18 → v4.19

| Metric | v4.18 | v4.19 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |
| System Stability | 88.5% | 88.5% | — |
| Pinned at Wealth Floor | 10.6% | 10.6% | — |

New pinned figure: seed 42 Stress Test, 56.0% wealth poverty (v4.18: 53.2%). The seed-42 Adverse Environment run is unchanged (37.4%, $258,045).

---

## v4.18 Release Notes

v4.18 adds a fifth poverty measure, **extreme poverty**, and restyles the poverty card to match the rest of the page. Both were requested by Duke. It also repairs three `domtest.js` checks from v4.17 and verifies v4.17's unverified layout.

**The seed-42/Full Integration/20yr regression is unchanged** (1,965d · $559,223 · 0.534 · 16.6% · 88.5%). Nothing in this release draws RNG or feeds back into the dynamics. `harness.js validate` reproduces it, and `domtest.js`, now 56 checks, passes in full. The 8 new checks each fail against an unmodified v4.17 page, while all 48 earlier checks still pass there.

### Extreme poverty: definition and construction

**Definition (the framework author's):** homeless, with necessities provided by charity, if at all. It includes people unhoused because of serious mental illness, and people who live this way by choice: ascetics, shamans, yogis, itinerant monastics, and others who subsist on the goodwill of others.

**This differs from the World Bank's definition.** The World Bank's "extreme poverty" is an income line ($3.00 a day). This one is housing-based. Both the card and the exports state the definition beside the figure.

**Why it is an overlay, not an engine output.** The engine models no housing tenure, mental illness or vocation. At US scale, about 22 per 10,000, the measure is about one agent in a 500-agent run, so a headcount would be sampling noise. It is therefore an **expected share**, built from three pathways on top of engine state:

| Pathway | Share at year 0 | Rule | What moves it |
|---|---|---|---|
| Economic | 73% | scales with **housing distress** (D) relative to year 0 (D0) | everything the engine models: CCO income, PTF/PTH cost relief, inflation, recessions, automation |
| Serious mental illness (SMI) | 25% | × (1 − wellness-zone reach) | only PTH **and** SZH together (wellness zones): reach = `EP_WZ_EFFECT` × zone coherence. Income does not reach it, so CCO Only leaves it unchanged |
| Voluntary | 2% | constant | nothing: identical in every scenario by construction |

**Housing distress** means this year's cash income plus all savings on hand at the start of the year cannot cover this year's living-wage basket at the prices the agent faces. At year 0 the same test uses year-0 wage income, initial wealth and the undiscounted basket. Year 0 equals `EP_Y0_RATE` in every scenario by construction.

The constants, all in `CFG`:

| Constant | Value | Source |
|---|---|---|
| `EP_Y0_RATE` | 0.0022 | HUD, *2025 AHAR Part 1*: 745,652 people homeless on a single night in January 2025, nearly 22 per 10,000 |
| `EP_SMI_SHARE` | 0.25 | Gutwinski et al. (2021), *PLOS Medicine* meta-analysis: schizophrenia spectrum 12.4%, major depression 12.6% |
| `EP_VOL_SHARE` | 0.02 | Set by Duke. No US source located; the true share may vary and should be updated as data sources become available |
| `EP_WZ_EFFECT` | 0.50 | At Home/Chez Soi RCT (Goering et al., 2014), final six months: housed all of the time 62% (Housing First) vs 31% (usual care); none of the time 16% vs 46% |

**Two assumptions, adopted by Duke and open to revision as data sources become available:**
- economic homelessness moves in proportion to housing distress (elasticity 1);
- the SMI pathway does not worsen as the economy does; it responds only to wellness zones.

Duke also confirmed that wellness zones require both PTH and SZH.

### Results

`node harness.js extreme 500` (seeds 1–500, 500 agents, 20 years, shocks off unless stated). Per 10,000 people; housing distress in percent.

| Scenario | Extreme poverty | Economic | SMI | Voluntary | Housing distress |
|---|---|---|---|---|---|
| Year 0 (every scenario) | 22.0 | 16.1 | 5.5 | 0.4 | 16.9% |
| Baseline @3% (shipped) | 73.6 | 67.6 | 5.5 | 0.4 | 70.4% |
| Baseline @0% (matched) | 49.3 | 43.3 | 5.5 | 0.4 | 45.2% |
| CCO Only | 22.5 | 16.5 | 5.5 | 0.4 | 17.3% |
| Full Integration | 13.2 | 9.3 | 3.5 | 0.4 | 9.7% |
| Adverse Environment | 35.5 | 31.5 | 3.5 | 0.4 | 32.9% |
| Stress Test | 57.4 | 52.4 | 4.5 | 0.4 | 54.6% |

Reductions (ratio of means):

- **Full Integration:** 39.8% below year 0, 82.0% below the shipped Baseline, 73.1% below the matched Baseline.
- **CCO Only:** 2.1% *above* year 0, but 69.5% below the shipped Baseline and 54.4% below the matched one.

**CCO Only holds extreme poverty at its year-0 level while the Baseline more than triples it.** Among participants it falls as the framework intends: housing distress drops from 16.9% to 10.7%. The 22% of agents outside CCO rise to 40.6%, because they inherit the Baseline's deterioration. That traces to the wage-versus-basket calibration logged in v4.17, not to anything in the new measure. Under Full Integration, participants' distress ends at 5.1% and non-participants' at 26.2%.

**The result is driven by the engine, not the constants.** Each constant varied alone, Full Integration against year 0:

| Constant | Values tested | FI vs year 0 | CCO Only vs year 0 |
|---|---|---|---|
| `EP_SMI_SHARE` | 0.15 / 0.25 / 0.35 | −40.5% / −39.8% / −39.2% | +2.4% / +2.1% / +1.8% |
| `EP_VOL_SHARE` | 0 / 0.02 / 0.05 | −40.7% / −39.8% / −38.6% | +2.2% / +2.1% / +2.0% |
| `EP_WZ_EFFECT` | 0.30 / 0.50 / 0.65 | −36.2% / −39.8% / −42.5% | +2.1% (unchanged) |

### The card, restyled

Now **Poverty by Five Measures**:
- scenario columns carry the same badges as the System Comparison table (Baseline red, CCO Only blue, Your Settings gold, which is also tinted);
- rows are grouped Stock / Flow / Extreme;
- each value has a bar in its scenario's chart colour, scaled within its row;
- change cells are green ▼ or red ▲, like the KPI deltas.

Definitions are visible sub-lines rather than hover tips, because a tip inside the table's horizontal-scroll wrapper would be clipped at the top rows. The long caption moved into a "How these are measured" expander. Extreme rows read per 10,000 people, HUD's convention: as a percentage, the voluntary pathway rounds to 0.00% at two decimals. On narrow screens the measure column stays pinned while the numbers scroll.

**Exports.** The CSV section is renamed POVERTY BY FIVE MEASURES and adds:
- the extreme rows (in percent, four decimals);
- the constants;
- housing distress per scenario;
- the wellness-zone reach.

JSON adds `results.extremePoverty`. **The JSON key `povertyByFourMeasures` is kept** so existing parsers keep working; it now also carries the extreme rows, keyed `extreme`, `extremeEcon`, `extremeSmi` and `extremeVol`.

### Found and fixed along the way

1. **A v4.17 check never exercised the code it guarded.** The version-label check dispatched `DOMContentLoaded` on `document`. The page listens on `window`, and a non-bubbling event never reaches it. The check compared static markup with `META` and passed only because both said v4.17. It now stales every label first and fires the event where the page listens.
2. **Two v4.17 checks pinned the poverty panel at exactly six rows**, which any new measure breaks. They now check that the six v4.17 measures are present and that every panel row renders.
3. **The tab title is now filled from `META.VERSION`**, and the static copy is kept current for crawlers.
4. **The page's structured-data description still described v4.16.** It is updated.
5. **v4.17's layout caveat is closed.** The poverty card and the sixth preset button were checked in headless Chromium at 1,400px and 390px, in light and dark schemes. The Adverse Environment tooltip stays on screen. This was a one-off check in this session: no browser dependency is added to the repository, so the v4.13 question of how far to take automated layout testing stays open.

### What did NOT get done, and why

- **None of the five v4.17 decisions was applied.** Each moves the seed-42 regression and the papers' headline figures, and should not ride along with a reporting release.
- **Everything else logged at v4.14–v4.17 remains open** (see Model Architecture Feedback).

### Regression: seed 42 / Full Integration / 20yr, v4.17 → v4.18

| Metric | v4.17 | v4.18 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |
| System Stability | 88.5% | 88.5% | — |
| Pinned at Wealth Floor | 10.6% | 10.6% | — |

New figures at seed 42, for pinned checks (per 10,000: total / economic / SMI / voluntary; housing distress):

| Scenario | Extreme poverty | Housing distress |
|---|---|---|
| Year 0 | 22.00 | 18.0% |
| Full Integration | 13.95 / 9.99 / 3.52 / 0.44 | 11.2% |
| Its Baseline (3%) | 67.32 / 61.38 / 5.50 / 0.44 | 68.8% |
| Its CCO Only | 21.64 / 15.70 / 5.50 / 0.44 | 17.6% |
| Adverse Environment | 35.19 / 31.23 / 3.52 / 0.44 | 35.0% |

**`harness.js`** mirrors the overlay verbatim, adds `CCO_ONLY` and `ccoOnlyFor()`, returns the overlay from `runScenario()`, and gains an `extreme` mode that prints every table above. **`domtest.js`** gains Phase 6 (8 checks): harness parity in every component and scenario, and the structural invariants (year 0 = `EP_Y0_RATE`; voluntary identical everywhere; SMI moved only by PTH + SZH). It also checks the restyled card, the title fill, and both exports.

---

## v4.17 Release Notes

v4.17 responds to three sources, each checked by direct computation before anything was acted on:

- this session's own audit of v4.16;
- ten notes from the independent NEEC maintainers, found while running the pinned v4.15 engine (`cd0ceec`) in their Sessions 38 and 40;
- an external Claude Sonnet audit of v4.15.

It ships:

- three bug fixes and one harness parity fix;
- two new poverty measures, each reported against year 0 as well as the Baseline;
- a new preset that separates environmental stress from weaker settings;
- recessions in `harness.js`;
- four disclosures that change how the project's headline claims should be read.

**The seed-42/Full Integration/20yr regression is unchanged** (1,965d · $559,223 · 0.534 · 16.6% · 88.5%). Nothing in this release draws RNG or feeds back into the dynamics. The regression is confirmed by `harness.js validate` and by `domtest.js`, now 48 checks, all passing. The ten new checks were each confirmed to fail against an unmodified v4.16 page, while the original 38 still pass there.

**Five items need a decision from Duke** and are logged under Model Architecture Feedback rather than applied:

- how to reconcile the papers' 98% / $82,000 headline with the engine;
- whether to recalibrate the wage distribution or the living-wage basket;
- whether θ should read realised PTF density;
- whether to build the 55% participation threshold as a dynamic;
- an endogenous price channel.

### Bugs fixed

1. **The page said v4.15.** v4.16 updated `META.VERSION` but not the header or footer, which were hardcoded. The single-source-of-truth rule `META` was created for in v3.5 had never been applied to the page's own markup. Every visible label (header, footer, Assumptions panel) now carries `class="meta-ver"` and is filled from `META.VERSION` at load. `domtest.js` checks it.
2. **BU Expiry was missing from every CSV export** (Claude Sonnet audit). It was the only run parameter absent from an export that exists for reproducibility. It has been added.
3. **The LHS Sensitivity export had a dead dimension** (Claude Sonnet audit). `ptfShare` is sampled in every design row, but PTF's on/off toggle was inherited from the page. With PTF off, the column was inert in all 100 rows. Nothing in the CSV said so. The fix follows the convention CCO already used: `params.ptf = params.ptfShare > 0`. The sampled range is [0.05, 0.35], so PTF is on in every row; with the toggle already on, the line is a no-op. The CSV now also records every fixed setting the rows inherit. Checked: 100/100 rows have PTF on, versus 0/100 before.
4. **Harness parity drift** (NEEC note 8). `harness.js`'s `structuralStability()` still used `Math.max(1, …)`, the window v4.13 fixed in `index.html` (it returned 0.99 for every 5–7 year run). It now uses `Math.max(2, …)`. Runs of 8 or more years are unaffected.

**Claude Sonnet's third finding, a race condition, was already fixed in v4.16.** A seeded run could be corrupted by overlapping background work. That is the reproducibility fix in v4.16's notes, and `domtest.js` Phase 4 passes against v4.16.

**Polish from v4.16's list, done:** `(a.automationRisk||0.5)` would read a draw of exactly 0 as 0.5. It is now an explicit guard, in both files. No figure moves.

### Four poverty measures, against year 0 and against the Baseline (NEEC notes 2 and 3)

Every headcount through v4.16 was a **stock** measure: net wealth below `POVERTY_LINE`, or BLEI below 30 days. BLEI is itself built mostly from 20% of wealth. The papers, and NEEC's C1.1, use an **income** measure.

`runYear()` now records four quantities it already computed: wage income after the income shock, CCO conversion proceeds, the agent's own basket cost, and the gross basket. It uses no RNG and nothing reads them back. A new **Poverty by Four Measures** card reports each measure's year-0 value, the final Baseline, CCO Only and Your Settings values, and the change against year 0 and against the Baseline. The same block is in the CSV and JSON exports. The definitions:

- **Cash income** = wage income + CCO conversion proceeds. PTH appreciation is excluded: it is a capital gain, which the OECD/EU income convention excludes.
- **Relative income poverty** = cash income < 60% of that scenario's own median. Agents are single adults with no taxes or transfers, so there is no equivalence scale and nothing to net out. A variant adds the in-kind value of the agent's CCO/PTF/PTH cost reductions to income first.
- **Basket poverty (net)** = cash income < the agent's own inflation-adjusted `LIVING_WAGE_ANNUAL` after cost reductions. It asks: can this year's income buy the living-wage basket at the prices this agent faces? **Gross** uses the undiscounted basket.
- **Year 0** is measured on the initial population before any year runs. Wealth and income measures are identical across scenarios there, because every scenario starts from the same latent population. BLEI is not: `agentBLEI()` credits BU, γ = 0.20 and a reduced daily cost the moment an agent enrols. So the card shows BLEI at year 0 under Baseline rules (policy-neutral), with the figure under the scenario's own rules beneath it.

`node harness.js headline 500` (Full Integration, seeds 1–500, 500 agents, 20 years, shocks off):

| Measure | Year 0 | Baseline @3% (shipped) | Baseline @0% (matched) | Full Integration | vs shipped Baseline | vs matched Baseline | vs year 0 |
|---|---|---|---|---|---|---|---|
| Wealth poverty | 37.8% | 71.8% | 50.5% | 15.3% | −78.7% | −69.7% | −59.5% |
| BLEI poverty | 10.3% | 70.8% | 49.1% | 12.6% | −82.2% | −74.4% | **+22%** |
| Relative income poverty (cash) | 15.3% | 16.3% | 17.7% | 18.0% | **+10%** | +2% | +18% |
| … incl. in-kind cost relief | 15.3% | 16.3% | 17.7% | 14.8% | −9.4% | −16.2% | −3.5% |
| Basket poverty (net) | 66.6% | 82.1% | 47.0% | 10.0% | −87.8% | −78.7% | −84.9% |
| Basket poverty (gross) | 66.6% | 82.1% | 47.0% | 19.7% | −76.0% | −58.1% | −70.4% |

**On relative income poverty, Full Integration shows no reduction.** The relative line moves with the median, and Full Integration raises median cash income from $50.7k to $79.6k, mostly through octave-driven wage growth. Participants with low base wages and all non-participants stay below the higher line. Counting in-kind cost relief as income gives a modest reduction. On the absolute basket measure the reduction is large. This is the familiar behaviour of relative measures under broad-based growth, but it matters here because it is the papers' own measure. How to present it is Duke's call.

### NEEC note 1: the 98% / $82,000 headline is not produced by this engine

The maintainers' 78.5% and 82.1% are reductions against the shipped Baseline. The harness gives 78.7% and 82.2% at N=500, agreeing within sampling. The table above shows the full picture:

- No measure and comparator reaches 98%. The largest is 87.8%: net basket poverty against the shipped Baseline.
- Against the inflation-matched Baseline, wealth poverty falls 69.7%.
- Against year 0, wealth poverty falls 59.5%.
- **BLEI poverty ends above its policy-neutral year-0 level**, 12.6% against 10.3%.
- Median wealth is $526,629, not $82,000.

`TARGET_WEALTH`, `TARGET_POVERTY` and `TARGET_GINI` are paper targets carried as constants, not engine outputs. The KPI badges have said so since v4.4. A Known Limitations entry now says it plainly. The model behind 98% is not in this repository, so this release cannot reproduce it. Publishing that model or restating the papers against the current engine is the decision logged below.

### NEEC notes 3 and 4: why the Baseline deteriorates, and Full Integration's early BLEI rise

Both trace to one calibration fact. **The median year-0 wage income is $39,945 (`exp(3.5) × 12 × WAGE_TO_USD`), against a $49,370 `LIVING_WAGE_ANNUAL` basket, so 66.6% of agents start in basket poverty.** The Baseline has no transfers, so those agents run an annual deficit from year 1 and draw down their wealth. The deficit then evolves differently at each inflation rate:

- At 3% CPI, costs outgrow wages, which grow about 1–1.8% a year. Wealth poverty climbs from 37.8% to 71.8%, and basket poverty from 66.6% to 82.1%.
- At 0%, wage growth slowly closes the gap. Basket poverty falls to 47.0%, while wealth poverty rises to about 50% and plateaus as stocks run down.

Neither is a code defect. Whether the wage distribution or the basket should be recalibrated is logged as a decision.

`node harness.js year0 500` (means over seeds):

| Full Integration, year | 0 | 1 | 2 | 3 | 5 | 10 | 20 |
|---|---|---|---|---|---|---|---|
| BLEI poverty (scenario rules) | 2.6% | 9.4% | 14.1% | 16.9% | 19.8% | 20.1% | 12.6% |
| … CCO participants | 0.6% | 6.4% | 10.4% | 12.9% | 15.2% | 15.0% | 7.2% |
| … non-participants | 9.6% | 20.2% | 27.3% | 31.5% | 35.9% | 38.3% | 31.7% |
| Basket poverty (net) | 66.6% | 40.6% | 38.2% | 35.7% | 30.7% | 21.1% | 10.0% |

The early rise (note 4) has two parts:

1. **About 7.7 points of it is measurement.** At year 0, BLEI already credits participants' BU and cost relief: 2.6% under Full Integration rules, but 10.3% for the same agents under Baseline rules. Measured from the policy-neutral 10.3%, BLEI poverty rises about 9.5 points, not 17.
2. **The rest is a genuine transient, not an initialisation bug.** Basket poverty falls steadily from year 1, so flows improve at once. But initial wealth is drawn independently of wage, and 40.6% of agents still run deficits in year 1. They draw down a stock the flow model would not have given them. BLEI is mostly 20% of wealth, so it tracks that run-down before flows turn positive.

A wage-conditional initial wealth draw would shrink the transient, but it would change the regression. That is a calibration decision, not something to apply here.

### NEEC notes 5 and 6: recessions in the harness, and an Adverse Environment preset

`harness.js` now carries `updateRecession()` and `buildRecessionPath()` verbatim, and `runScenario()` honours `p.shock`. Until now the harness silently ignored `p.shock`. The path draws on its own stream (seed + 700000) and restores `RNG`, so enabling shocks moves no agent draw, the same paired-shock design `simulate()` uses. Checked against the page: the seed-42 Adverse Environment run is **bit-identical** through `domtest.js` and `harness.js` (37.4% wealth poverty, $258,045, 950d, Gini 0.639).

The **Stress Test** preset changes the environment (recessions, 2% inflation, AI automation) and the settings (40% participation, $900 BU, lower PTF/PTH/SZH/CIP) at once. A new **Adverse Environment** preset applies the same environment to the unchanged reference settings. `harness.js` mirrors both as `STRESS_TEST` and `ADVERSE_REFERENCE`. `node harness.js stress 500`:

| Scenario (seeds 1–500) | Wealth poverty | BLEI poverty | Basket poverty (net) | Median wealth (mean of run medians) |
|---|---|---|---|---|
| Full Integration | 15.3% | 12.6% | 10.0% | $526,629 |
| Adverse environment @ reference settings | 35.9% | 32.6% | 50.5% | $206,930 |
| Weaker settings @ reference environment | 32.0% | 29.3% | 25.7% | $269,562 |
| Stress Test (both) | 56.8% | 54.9% | 72.3% | −$9,407 |
| Baseline under the adverse environment (3% CPI) | 81.9% | 81.2% | 94.4% | −$10,000 |

The environment and the settings each roughly double wealth poverty, and together they compound. A stress criterion that means "does the reference design hold up under adverse conditions" should be tested against Adverse Environment, not Stress Test.

### NEEC note 7, and a related finding: two thresholds described as dynamics are not

- **55% CCO participation.** Three documents described this as a network threshold below which effects collapse:
  - the reference table above;
  - the page's sensitivity table ("network effects collapse");
  - the replication page ("minimum viable 55%").

  It is only a run warning: no line of `runYear()` reads aggregate CCO participation. `node harness.js participation 200` shows a smooth response: 23.2% wealth poverty at 45%, 20.9% at 55%, 18.4% at 65%, about −0.24 points per point of participation. The warning, sensitivity row, `CFG` comment and replication page now describe it as the papers' design reference.
- **SZH synergy θ.** Found in this audit. The BLEI paper gates θ on *PTF merchant density* (0 below 55%, 0.25 at 90%). The code applies that threshold to `szhCoh`, the zone-coherence slider, and realised PTF density never enters. The reference run's θ is 0.121 whether realised PTF membership is 18% or 53%. The comments, CSV mechanics line, Assumptions card and replication page now say it is a proxy.

  Measured for the decision: gating θ on realised PTF share would move seed 42 to 16.8% / $556,503 / 1,897d. At N=200 it would raise wealth poverty 15.28% → 15.50% and lower median wealth 0.7%.

### NEEC notes 9 and 10

- **Note 9 (exogenous prices)** is logged, not built. Inflation is an input rate, damped only by realised PTF/PTH membership. No price responds to demand, BU issuance, conversion volume, recession or automation. A Known Limitations entry says so, and the item below explains why it bears on any claim that the framework is non-inflationary.
- **Note 10:** the regression is unchanged, as stated at the top and in the table below. New pinned figures for NEEC's checks are listed there too.

### What checking this session's own work turned up

1. **A units error caught before shipping.** The new card's wealth-poverty cell first multiplied `SIM_RESULTS.finalPov`, already a percentage, by 100. The harness cross-check (`domtest.js` Phase 5 compares every panel figure with `runScenario()`) was written to catch exactly this class of error.
2. **The relative income result was not what the brief expected.** It is reported as found, with an in-kind variant for fairness, rather than dropped or redefined.
3. **The maintainers' year-0 Baseline BLEI figure (2.7%) matches Full Integration's year-0 figure under Full Integration's own rules** (2.6% here). The Baseline's own year-0 BLEI poverty is about 10.3%. Their conclusion that the Baseline deteriorates sharply stands; the starting point is higher than stated.

### What did NOT get done, and why

- **None of the five decisions was applied** (see Model Architecture Feedback).
- **No layout verification.** The new card uses the existing table markup and the sixth preset button fills the preset grid's empty slot, but `domtest.js` verifies behaviour, not appearance. Both warrant the usual visual check after deploying.
- **Everything else logged at v4.14–v4.16 remains open:** the flow-of-funds ledger, monthly BU tranches, CCO/PTH pathway decomposition, λ heterogeneity, the fuller recession and automation models, PTH entry/exit, PTH appreciation accounting, the Baseline inflation default, and Git tags.

### Regression: seed 42 / Full Integration / 20yr, v4.16 → v4.17

| Metric | v4.16 | v4.17 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |
| System Stability | 88.5% | 88.5% | — |
| Pinned at Wealth Floor | 10.6% | 10.6% | — |

New figures at the same seed, for pinned checks:

| Figure | Value |
|---|---|
| Relative income poverty | 19.8% (17.4% incl. in-kind) |
| Basket poverty | 11.6% net, 22.4% gross |
| Year 0: wealth poverty | 35.2% |
| Year 0: BLEI poverty | 10.0% (2.0% under Full Integration rules) |
| Year 0: relative income poverty | 17.0% |
| Year 0: basket poverty | 65.6% |
| Adverse Environment (seed 42) | 37.4% wealth poverty, $258,045, 950d, Gini 0.639 |

**`harness.js` gains four modes:** `headline`, `year0`, `stress` and `participation` print every figure in the tables above. `domtest.js` gains Phase 5 (ten checks).

---

## v4.16 Release Notes

v4.16 is an internal audit of v4.15: the engine core (`simulate()`, `runYear()`, the metric functions, the asynchronous run machinery) was read line by line, and every finding was confirmed by direct computation — in `harness.js` for engine questions, and in `domtest.js`/jsdom for anything involving the live page — before it was acted on or logged. It ships one genuine reproducibility bug fix, one comparison confound disclosed and made matchable (opt-in, default unchanged), two open Good First Issues closed ((e) and (f) from the v4.14 list), and three documentation corrections. **The seed-42/Full Integration/20yr regression is unchanged** (Median BLEI 1,965d, Median wealth $559,223, Gini 0.534, Wealth poverty 16.6%): `harness.js validate` reproduces it bit-for-bit, and `domtest.js` reproduces it through the live page five separate times, including under the interleavings that broke it in v4.15.

**Two items need a decision from Duke** and are deliberately not applied: the Baseline comparison's inflation default, and PTH appreciation accounting. Both are measured below and logged under Model Architecture Feedback.

### Bug found and fixed: a seeded run could fail to reproduce if started while earlier background work was still computing

This document's own reproducibility promise (Reproducibility Testing, below: same seed and parameters, same output — "this should not happen") held only for a run started from a quiet page. `simulate()` runs Your Settings one year per `setTimeout` step and assumed nothing touched the shared `RNG` global between steps. Two things did:

- **The attribution ablation.** `finish()` launches `runAblation()` 80ms after every run. Each of its chunks installs its own stream and yields with that stream still installed; when the batch completes it restores a stream saved *before* any newer run began — the previous run's exhausted main stream.
- **The validation suite.** Every `VAL_TESTS` check calls `initRNG()` for its own seeds and never restores the global.

The Run button stays enabled during both, and `runSim()` compounded the exposure: it set the seed with `initRNG()` but `simulate()` only read the global 50ms later, inside a `setTimeout`. Reproduced in jsdom against the unmodified v4.15 page:

| Seed 42, Full Integration, 20yr — started… | v4.15 median wealth | v4.16 |
|---|---|---|
| from a quiet page (the documented case) | $559,223 | $559,223 |
| the instant the previous run finished (ablation pending) | **$545,506** | $559,223 |
| while the validation suite was computing | **$555,354** | $559,223 |

The window after a finished run is short (the 80ms timer plus the ablation itself), but the page's own reference run opens it on every page load, and the validation suite holds its window open for several seconds.

**Fix, defended in depth:** `step()` re-asserts its own stream at the top of every simulated year; `runSim()` hands its stream to `simulate()` explicitly instead of letting it re-read the global; each ablation chunk restores the global it found, and a run-generation counter (`SIM_GEN`) makes a batch abandon itself — and never render its stale chart over a newer run's — once a newer run has started; `runValTests()` restores the global around each check. OAT and LHS already followed the save-and-restore pattern and needed no change. **Every change is a no-op for an uninterrupted run** (the global already *is* the right stream at each of those points), which is why no documented figure moves.

For contributors, the rule this establishes is now stated under Code Contributions: any code that reassigns `RNG` and then yields to the event loop must restore it first.

### Comparison confound disclosed, measured, and made matchable: the Baseline has always run at a different inflation rate than Full Integration

Since v4.0, the Traditional Welfare Baseline comparison (`pBase`) has been anchored to `CFG.BASELINE_CPI_RATE` = 3%, deliberately ("the baseline is meant to be a fixed real-world reference point"), while Your Settings and CCO Only use the inflation slider — **0% in Full Integration, CCO Only, and High AI**. Every vs-Baseline figure in those presets therefore mixes the policy effect with a 3-percentage-point inflation difference. The 0% side has a stated rationale — the replication page calls it "the price-stability hypothesis of cooperative essential goods provision" — and it is a legitimate hypothesis. But as implemented it is an assumed *input*, not a model *output*: at 0% the engine's own PTF/PTH inflation-damping mechanisms (fixed in v4.14/v4.15) have nothing to act on, and CCO Only, which has neither PTF nor PTH, runs at 0% too. The hypothesis's assumed effect is therefore counted inside every vs-Baseline gap. Running both sides at 3% (option (C) under Model Architecture Feedback) is the way to let the damping mechanisms produce whatever price stability they actually produce. CCO Only was already inflation-matched, so the CCO-Only comparison is unaffected. `node harness.js infl-match 500` (new this release; seeds 1–500, 500 agents, 20 years, shocks off):

| Scenario | Wealth poverty | BLEI poverty | Median BLEI | Median wealth (median of runs) | Runs with median pinned at floor | Pinned at floor (mean share) |
|---|---|---|---|---|---|---|
| Baseline @ 3% (shipped comparison) | 71.8% | 70.8% | 7.4d | −$10,000 | 100% | 69.9% |
| Baseline @ 0% (matched to Full Integration) | 50.5% | 49.1% | 85.6d | $17,914 | 0.6% | 44.2% |
| Full Integration @ 0% (shipped) | 15.3% | 12.6% | 1,824d | $527,037 | 0% | 9.2% |
| Full Integration @ 3% (matched to Baseline) | 28.8% | 25.9% | 1,193d | $341,864 | 0% | 24.1% |

(The Full Integration @ 0% row agrees with the v4.4 N=5,000 study to within sampling error — wealth poverty 15.3% vs 15.4%, BLEI poverty 12.6% vs 12.5%, median BLEI 1,824d vs 1,824d, mean median wealth $526,629 vs $526,120 — a useful check that the harness aggregates are sound.)

**How much of the headline gap is inflation.** The unmatched wealth-poverty gap is 56.5 points. Matched at 0% it is 35.2; matched at 3%, 43.0. So **roughly 24–38% of the headline gap is the inflation difference, not the policy** (23–37% for BLEI poverty). The policy effect remains large on every matched comparison. But one finding this document has leaned on since v4.4 does not survive matching: **"Baseline's median is pinned at `WEALTH_FLOOR` in 100% of runs" falls to 0.6% of runs once the Baseline runs at the same 0% as Full Integration.** The Model Architecture Feedback item on `WEALTH_FLOOR` attributed that pinning to "the ongoing annual cost/wage gap under 20 years of 3% CPI compounding" — accurate, but the 3% was applied to one side of the comparison only. A v4.16 note on that item says so.

**What shipped (no documented figure moves):**

- A **Match Baseline inflation to my settings** toggle (Economic Environment), **off by default**. On, `pBase.inflRate = p.inflRate`. It changes the Baseline trajectory only, never Your Settings' own — verified through the live page: with it on, seed 42's Your Settings is still $559,223, and the Baseline becomes median $13,612 / 50.8% poverty, bit-identical to `harness.js`'s independent computation of the same scenario.
- A **run warning** whenever the two rates differ and the toggle is off — which includes the default reference run. That is a visible change to the page's first impression, made deliberately: this is a confound on the headline comparison, and the project's practice since v4.12 has been to say so where the reader is looking. Duke may reasonably prefer a quieter placement.
- The Baseline rate used is recorded in the CSV and JSON exports, the run-configuration line, and a shared URL (`baseInflMatchOn`). A Known Limitations entry and a sentence in the Baseline preset's tooltip carry the numbers above.

**Why not change the default:** it would move every vs-Baseline figure this document reports and reframe the project's headline comparison — a framework-level decision, the same category as `WEALTH_FLOOR` and `TARGET_*`, and the same opt-in-first treatment the v4.6 PTF cap received. Options and their consequences are laid out for Duke under Model Architecture Feedback.

### Open item closed: `runYear()`'s annual schedule, enumerated (Good First Issues v4.14 item (e))

v4.14 declined to transcribe an audit's attempt at this, recommending that "a future session with the bandwidth to verify each step against the code line-by-line should do this properly." This one did. The schedule now lives in the ODD panel as **Overview: Process Overview & Scheduling** — also the ODD standard's third element, which the panel had been missing entirely — and is reproduced here:

- **Once per year, before any agent moves:** (1) PTH appreciation bonus from SZH coherence; (2) θ and the two terms it gates (PTF conversion bonus, SZH→PTF induction probability); (3) a snapshot of realised PTF membership; (4) realised PTH membership; (5) population-wide inflation damping, PTF then PTH, each scaled by its realised share; (6) `dollarCost` (`BASE_DAILY_COST`-based, used by FBS and PTH sizing); (7) the recession income multiplier; (8) the live PTF count, only if the cap is on; (9) the AI displacement rate.
- **Then each agent in turn, in array order:** (1) NaN rescue; (2) exactly eight RNG draws in a fixed order — wage variance, BU spend fraction, CIP quality bump, octave advancement, SZH→PTF induction, SZH→PTF share, PTH appreciation noise, PTF adoption — whatever the agent's status; (3) BLEI on start-of-year state; (4) wage growth, floored at 80% of last year's wage; (5) cost-reduction factor from start-of-year membership; (6) wealth += wage income × `incomeShock` − inflation-adjusted `LIVING_WAGE_ANNUAL` × cost factor; (7) CCO participants: BU decay and new allocation (capped at 3× monthly BU), spend, CIP quality bump, conversion (× `incomeShock`), then FBS-gated octave advancement on the *new* wage, then SZH→PTF induction; (8) PTH members: tenure, payment→equity contribution, appreciation; (9) agents not yet in PTF, from the second year: innovation + distress + Bass adoption; (10) wealth floor clamp.
- **Timing consequences:** PTF cost relief begins the year *after* adoption; within-year adoptions do not change that year's Bass term (a start-of-year snapshot) but count against the optional cap immediately; FBS pairs this year's grown wage with a cost factor set by start-of-year membership; and agents read one another's state only through the two start-of-year counts and the live cap counter, so array order matters only when the cap is on.

Step B(2) is the v4.3 common-random-numbers guarantee every Baseline/CCO-Only/Main pairing rests on. Until now it was asserted only in prose; it is now machine-checked (next section). The Submodels card's one-line summary, which had omitted SZH→PTF induction and every once-per-year term, now points to the full schedule.

### Open item closed: an itemised invariant suite, plus a validation check that tested three things at once (Good First Issues v4.14 item (f))

**The 'benefit' check was confounded.** "Full integration outperforms baseline" compared the Reference preset (shocks off, 0% inflation) with the Baseline *preset* as-is (shocks on, 3% inflation) — policy, shock exposure, and inflation all differed — and the shock-on arm's `updateRecession()` drew from the same stream as agent draws, so the arms were not CRN-paired after year 1. It passed regardless. The Baseline arm now takes the Reference arm's shock and inflation settings, leaving policy as the only difference; it still passes 5/5.

**The 'invariants' check now itemises what item (f) asked for, and more:** BU balance within [0, 3×BU]; Acre Equity non-negative; every λ within [`FBS_LAMBDA_LO`, `FBS_LAMBDA_HI`] (which, with FBS clamped at ≥0, is what keeps P(advance) in [0,1)); the same seed reproduces every agent's final wealth exactly; a different seed changes it; **exactly eight RNG draws per agent-year** across four presets with the PTF cap off and on (by wrapping `RNG` in a counter); and the PTF cap's documented ceiling (realised membership never ends above max(year-0 draw, ⌈n × slider⌉)). The suite still reports six checks, 6/6 passing. "Probability bounds" is covered by the λ-range precondition rather than by instrumenting `runYear()`'s local `pAdvance`, which would have meant touching the engine for a test.

### Documentation corrections

1. **A fifth stale claim inside `runYear()`.** The v4.3 wealth-flow comment still said BLEI/FBS/Gini "deliberately keep their existing SIU_TO_USD-based conversion." `SIU_TO_USD` was retired in v4.4; the v4.13 sweep corrected four other stale claims in this function and missed this one. Corrected in place, with a note naming the divergence that *is* still current (the cost side: `LIVING_WAGE_ANNUAL` vs `BASE_DAILY_COST`).
2. **Recession's scope was understated.** Known Limitations (v4.14) and the Model Architecture Feedback item below said recession "only ever multiplies earned wage income." `convGain` is multiplied by the same `incomeShock`, so recession also scales CCO conversion proceeds; and `incomeShock` carries every agent's ordinary ±10% annual wage-variance draw, recession or not. Both places corrected.
3. **The PTH card v4.15 rewrote still did not match the code.** v4.15 corrected the Empirical Calibration panel's PTH card to say a tenure-based share of appreciation goes to liquid wealth "with the remainder tracked to `acreEquity`." The code is `a.acreEquity+=appr; a.wealth+=appr*pthLiquidShare(tenure)`: the *full* appreciation goes to `acreEquity` *and* the liquid share is credited to wealth, so the liquid share sits in both stocks and keeps compounding inside `acreEquity`. The card now describes the code, and adds a fact no document had stated: `acreEquity` is read by no metric, so **every reported wealth figure excludes PTH equity entirely**, members' own contributions included. Whether the code should change is a decision, measured next.

**The PTH accounting decision, measured** (`node harness.js pth-accounting 500`; the harness's new `PTH_APPR_CONSERVE` switch defaults to `false`, which is bit-identical to `index.html`):

| Full Integration, seeds 1–500 | Median wealth (mean) | Median BLEI | Wealth poverty | Gini |
|---|---|---|---|---|
| Current (full appreciation → `acreEquity`) | $526,629 | 1,824.3d | 15.30% | 0.517 |
| Value-conserving (`acreEquity` keeps only the non-liquid remainder) | $525,176 | 1,820.4d | 15.36% | 0.518 |
| Same, PTH uptake 50%: current → conserving | $611,684 → $608,065 | 2,557.7 → 2,542.1d | 11.19% → 11.33% | 0.478 → 0.479 |

Small (−0.3% at the reference 20% uptake, −0.6% at 50%), but it would move the seed-42 regression from $559,223 / 1,965d to **$558,001 / 1,951d**. Those happen to be exactly v4.4's documented figures; the most likely explanation is that the median pair of agents is the same non-PTH pair in both runs, a coincidence of rank rather than a sign the change reverts v4.5 — not independently verified.

### What checking this session's own work turned up

1. **A regression guard that guarded nothing, caught before shipping.** The first draft of the "re-run while the ablation is mid-flight" check waited 120ms before re-running — by which time, in jsdom, the ablation had already finished. It passed against v4.15 as well as v4.16. It now queues the re-run from inside the ablation's first chunk (by hooking `buildPop()`'s `mulberry32(9973)` call), so the remaining chunks are genuinely pending. Run against an unmodified v4.15 `index.html`, **all nine new `domtest.js` checks now fail** and the original 29 pass.
2. **The handoff's figures were at N=100; the shipped ones are at N=500.** The previous session's handoff estimated the inflation share of the gap at "24–38%" from 100 seeds; 500 seeds give the same range. Its PTH estimate (−$1,672) was superseded by the N=500 figure (−$1,454).
3. **Both harness studies are reproducible from the harness itself.** Instead of shipping figures from throwaway scripts, `harness.js` gained `infl-match` and `pth-accounting` modes that print every figure in the two tables above.

### What did NOT get done, and why

- **Neither decision was applied.** Baseline inflation matching ships as an opt-in; the PTH accounting is documented and measured only. Both are Duke's call — see Model Architecture Feedback.
- **Polish noted, not changed:** `agentEDC()`'s non-participant `Math.min(0.75,…)` cap can never bind (the expression peaks at 0.58); `(a.automationRisk||0.5)` would read a draw of exactly 0 as 0.5 (not reachable in practice); `runValidation()` does not disable the Run button (harmless now that streams are isolated). None affects any output.
- **Everything else logged at v4.14/v4.15 remains open**, unchanged: the flow-of-funds ledger, monthly BU tranches, CCO/PTH pathway decomposition, λ heterogeneity, the fuller recession and automation models, PTH entry/exit, and Git tags per release.
- **No layout verification.** One new sidebar control was added, using the existing `.cr`/`.tg` markup pattern exactly; `domtest.js` verifies its behaviour, not its appearance, so it warrants the usual visual look after deploying.

### Regression: seed 42 / Full Integration / 20yr, v4.15 → v4.16

| Metric | v4.15 | v4.16 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |
| System Stability | 88.5% | 88.5% | — |
| Pinned at Wealth Floor | 10.6% | 10.6% | — |

The default Baseline comparison is also unchanged (seed 42: 71.0% wealth poverty, median −$10,000, 68.6% pinned). With the new toggle on, the seed-42 Baseline is 50.8% / $13,612 / 45.8%.

Confirmed by `harness.js validate` (JSON reproduced exactly) and by `domtest.js`, now **38 checks**, all passing, nine new this release: the shared-URL round-trip of the new toggle; its default-run warning; its export fields; the extended invariants; the paired benefit check; seed 42 reproducing when re-run the instant a run finishes, while the ablation is mid-flight, and while the validation suite is computing; and the inflation-matched Baseline agreeing with `harness.js`.

---

## v4.15 Release Notes

v4.15 responds to two independent external audits of v4.14, forwarded by Duke together: **MuseAI**, a focused code-level audit, and **Grok**, a broad clarity-and-rigor review. Per this project's standing practice, every claim was checked against source — and, where it made an empirical claim, by direct computation — before anything was acted on. Four items shipped: one genuine mechanics bug, one robustness fix, one statistical correction, and one documentation correction. **Zero effect on the documented seed-42/Full Integration/20yr regression** (Median BLEI 1,965d, Median wealth $559,223, Gini 0.534, Wealth poverty 16.6%) — confirmed by `harness.js validate` reproducing every figure bit-for-bit, and by `domtest.js` driving the fixed engine through a real DOM.

### How these audits differed from prior ones

Two things changed the shape of the verification work this time, and both are worth naming because they affect how much of it this document has to show.

- **MuseAI ran this project's own tooling before reporting** — `harness.js validate` and `domtest.js` — which no external audit had done before. Every earlier audit's claims were verified afterwards by a Claude session that first had to build a harness from scratch. Here the findings arrived already grounded in the project's own regression machinery, so verification meant reproducing them and then *extending* them (scope sweeps, negative controls) rather than establishing them from nothing.
- **Grok's review deliberately avoided re-flagging items already logged in this file**, and reached its own conclusion that it found no additional mechanics bugs on the default or documented paths that would move the seed-42 regression or the shipped presets. That is independent corroboration of the same thing MuseAI's harness run showed: the four fixes below are the whole story for the documented configurations.

### Bug found and fixed: PTH's inflation damping was a flat toggle-triggered discount, not scaled by realised membership

The line directly beneath the v4.14 PTF fix:

```js
if(p.pth&&inflRate>0)inflRate*=0.90;
```

applied a flat 10% reduction to the whole population's cost inflation whenever PTH was toggled on and inflation was nonzero — **regardless of `p.pthUptake`**. This is the v4.14 defect class again, in a coarser form: the PTF line at least read a slider (the wrong one); this one referenced no adoption-scale quantity at all. Confirmed by isolating the two-line computation from every downstream mechanism: at `inflRate=0.02` the factor was bit-identically 0.90× whether 5%, 20%, or 50% of a 500-agent population was in PTH. A stronger form of the same fact turned up while verifying: **PTH switched on with zero members still damped inflation.** `domtest.js` now reproduces this live against an unmodified v4.14 page (otherwise-identical runs, PTH-on/zero-members vs PTH-off: median wealth $54,147 vs $45,444; on v4.15 they are bit-identical).

**Fix.** Same shape as the PTF fix — count existing membership flags, reuse the count:

```js
var pthMemberFrac=0;
if(p.pth){var pthCount0=0;agentSet.forEach(function(a){if(a.inPTH)pthCount0++;});pthMemberFrac=pthCount0/Math.max(1,agentSet.length);}
...
if(p.pth&&inflRate>0)inflRate*=(1-pthMemberFrac*0.10);
```

The 0.10 coefficient is `1−0.90`, unchanged from the historical value; it is now the ceiling, reached at 100% membership — exactly as the v4.14 PTF fix kept its own 0.5 and replaced only the input variable. Two design notes:

- **Why not track adoption over time, as `ptfAdoptFrac` does for PTF?** PTH membership is drawn once, at construction (`instantiateAgent()`), and never changes during a run — there is no Bass/distress adoption path for PTH. `pthMemberFrac` is therefore the population's fixed *realised* share, which carries Bernoulli sampling variance around the slider exactly as the PTF year-0 draw does (see the v4.6 PTF-cap notes): at seed 42 with 500 agents, a 5% slider realises 6.4%. The damping now tracks who is actually in PTH, not the dial. Modelling PTH entry/exit is a separate design question, subsumed by the rollout/transition-path item under Good First Issues.
- **It draws no RNG** — it counts already-set `a.inPTH` flags — so it shifts no stream position anywhere in the function.

**Verified inert on every documented figure — proven by sweep, not argued.** Full Integration and hiAI have `inflRate=0`; Baseline and CCO-Only have `pth=false`. Rather than stop at reading that off the configs, all five shipped presets were run under the v4.14 and v4.15 engines at seed 42 and every agent's final wealth compared: **four of five are bit-for-bit identical (hiAI included, with AI automation on); only Stress Test differs** — the only preset combining `pth:true` with nonzero inflation. `harness.js validate` reproduces the regression JSON exactly:

```
{"pov":16.6,"gini":0.534,"wealth":559223,"p10":-10000,"p90":1616445,"bleiMed":1965,"bleiPovPct":13.6,"pctFlourishing":69.8,"avgEDC":24.9,"stab":88.5,"fracAtFloor":0.106,"medianPinned":false}
```

A PTH-uptake sweep on a synthetic isolate (CCO + PTH + 4% inflation, no PTF/SZH/CIP; seed 42, 20yr, 500 agents) maps where the fix does and doesn't apply. It is identical at every uptake when inflation is 0, identical at 100% uptake for any inflation (the new formula equals the old flat one at full membership), and diverges most at low uptake:

| PTH uptake (realised) | v4.14 median wealth / poverty | v4.15 median wealth / poverty |
|---|---|---|
| 5% (6.4%) | $84,783 / 47.0% | $45,595 / 49.4% |
| 10% (10.8%) | $93,195 / 46.2% | $52,474 / 48.6% |
| 20% (19.6%) | $157,016 / 43.4% | $118,888 / 45.2% |
| 30% (31.0%) | $213,780 / 41.2% | $183,659 / 42.8% |
| 50% (53.0%) | $297,073 / 35.4% | $280,106 / 36.6% |
| 75% (78.2%) | $366,914 / 27.2% | $358,858 / 28.0% |
| 100% (100.0%) | $429,231 / 21.6% | identical |

The only `VAL_TEST` that reaches this line is `ptf_infl`; both its arms share the same reference PTH uptake, so the fix scales them identically. Re-verified 5/5 seeds (1234, 5678, 9012, 3456, 2468) under both engines in the harness, and through the live page in `domtest.js`'s Phase 3.

**Effect size where the fix does apply** (harness-computed, seed 42/20yr, recession shocks and AI automation held off — the harness's simplified recession handling does not reproduce the in-app preset's stochastic-shock path, a documented scope limit of `harness.js`, so these are effect-size illustrations of the fix, not the in-app Stress Test run's own output):

| Config | Metric | Before (v4.14) | After (v4.15) |
|---|---|---|---|
| Stress Test preset | Poverty | 41.8% | 43.2% |
| | Gini (EDC-adj.) | 0.696 | 0.702 |
| | Median wealth | $158,155 | $143,494 |
| | Median BLEI | 482d | 436d |
| Synthetic isolate (PTH + 4% inflation, no PTF/SZH/CIP) | Poverty | 43.4% | 45.2% |
| | Gini (EDC-adj.) | 0.688 | 0.701 |
| | Median wealth | $157,016 | $118,888 |
| | Median BLEI | 568d | 456d |

**The direction is the opposite of the v4.14 PTF fix, and that is worth stating plainly.** The PTF fix *strengthened* damping, because real PTF adoption ran above its slider. This one *weakens* it, because at a 10–20% realised uptake the flat 0.90 overstated what a small PTH-participating minority should do to population-wide inflation. A reader should not infer that "fixing a damping bug" always points one way.

**A sweep for the same defect class.** Every population-level `p.*` read in `runYear()` was enumerated and classified. No further instance of "a scalar or bare toggle standing in for realised membership" exists. The remaining reads are SZH's zone-coherence scalar (by design — coherence *is* the zone-level quantity the θ gate is defined on), CIP's participation scalar (applied uniformly by design; CIP has no per-agent membership flag — agents carry only `inCCO`/`inPTF`/`inPTH`), and the PTF-cap comparison (where the slider *is* the intended ceiling). `runYear()` never reads `p.partRate` or `p.pthUptake` at all — both are consumed once, at construction.

Ported into `harness.js` for parity, with the same reasoning recorded in its own comment.

### Robustness fix: a missing `expiry` would have resolved to NaN

`Math.max(1,p.expiry)` returns `NaN`, not 1, if `p.expiry` is `undefined` — `Math.max` propagates `NaN` from any argument rather than ignoring it. **This was never a live defect**: every current caller supplies `expiry` explicitly (the slider, `pBase`/`pCCO` in `simulate()`, `mkMiniP()`'s hardcoded default), so no documented or shipped figure was ever affected. But it sat one un-set object key away from a quiet failure for anyone hand-building a test or mini-scenario object. Measured, the failure is worse than a NaN total: `decay` becomes `NaN`, `totalBU`/`totalConversion` become `NaN`, and — because the pre-existing `isNaN` rescue on `a.wealth` resets it to 0 — **every CCO participant's wealth is silently zeroed each year** (median wealth $0 in a 200-agent check), with no error thrown.

Fixed to `var decay=Math.max(0,1-1/Math.max(1,p.expiry||1));`. `p.expiry||1` is a no-op for every value the UI can produce: decay at expiry=1 and expiry=6 is bit-identical before and after; expiry=0 (never UI-reachable) already resolved to `decay=0` via the existing floor and still does; a missing value now behaves as expiry=1 (verified bit-identical to an explicit 1). Ported into `harness.js`.

### Statistical correction: Monte Carlo 95% CIs now use Student's t, not a fixed z

`renderMultiRunSummary()` computed `ci=1.96*s/Math.sqrt(n)` for every n, which is correct only in the large-sample limit. The correct two-tailed multiplier is Student's t with n−1 degrees of freedom:

| Button | n | df | correct t | interval too narrow by (fixed z=1.96) | actual coverage of the nominal 95% |
|---|---|---|---|---|---|
| Run 10× | 10 | 9 | 2.262 | 13.4% | 91.8% |
| Run 50× | 50 | 49 | 2.010 | 2.5% | 94.4% |

(Coverage assumes an approximately normal run-level statistic. **A correction to the audit handoff's own arithmetic:** it described t(9)=2.262 as "~13% larger than 1.96." It is 15.4% larger; it is the fixed-z *interval* that was 13.4% too narrow. Both statements are true and are now stated correctly here and in `index.html`.) The 3× button does not display a CI and is unaffected.

New `tCritical95(df)`: the standard two-tailed-95% table (df 1–30, then 40/50/60/80/100/120), linearly interpolated between listed df, converging to 1.96 beyond df=120. **All 36 table entries were checked against an independent implementation of the t quantile function** (agreement to within rounding); linear interpolation between listed entries errs by at most 0.0014 over df 1–120; beyond df=120 the 1.96 asymptote is within ~1% (max 0.02, at df=121). The summary header now states the t and df actually used, e.g. `t=2.262, df=9`, so the displayed interval is checkable rather than asserted. Display-only: it reads already-computed `MR.results`, draws no RNG, touches no agent state, and cannot affect any simulation output or the documented regression table.

**Scope, checked:** `harness.js`'s own sweep summary keeps `ci95=1.96*sd/√n` — it is used with N≥100 seeds there (N=500 for the documented `WEALTH_FLOOR` table), where t and z differ by at most 1.2%, so it is left as is. The N=5,000 and N=500 large-N tables in this file report CIs on the mean across runs at sample sizes where t≈z; they are unaffected.

### Documentation correction: a fourth stale PTH card, missed by the v4.12 sweep

v4.12 corrected three places where the interactive tool's panels described pre-v4.3/pre-v4.4 mechanics as current. MuseAI found a fourth instance the same sweep missed: the **Empirical Calibration** panel's "PTH Acre Equity — payments now build equity" card still described housing-cost reduction as "35% of `SIM_COST_SCALE`" (which no function in the file reads — the actual mechanic is a dimensionless `cf*=0.65` applied to the main loop's `LIVING_WAGE_ANNUAL`-based cost) and appreciation as a flat "× 0.5" 50% haircut (superseded in v4.5 by `pthLiquidShare()`'s 15%→85% tenure ramp). Its third sub-claim — the 25% equity-contribution share — was and remains accurate. Corrected in place with a note recording what was wrong, per this project's established practice.

One precision on the finding itself: the audit placed this in the "ODD panel." The stale card lives in the **Empirical Calibration** panel (third of its four cards). The ODD panel's own "Details: Submodels" card was a separate, adjacent place that needed one accurate sentence added — that population-wide inflation damping now scales with realised PTF and PTH shares — and got it. This project is careful to distinguish the two panels (see the v4.12 fixes), so the distinction is kept.

### What the audits confirmed or restated, and the one item logged for Duke

Checked against source and found already addressed or already logged, not treated as new:

- **A monolithic single-file `index.html`, the BU-expiry annual approximation, and `harness.js`'s documented coverage limits** — all already logged (single-file is an explicit standing constraint; the approximation's scope is stated in the v4.14 notes; the harness's scope limits are stated in the v4.8 and v4.9 notes).
- **"`SIM_COST_SCALE` should carry a historical-only marker."** It already does, inline at the constant's own definition in `CFG` (`// historical constant only — read by no function in this file …`), and again in the Empirical Calibration panel's cost-scales card. Arguably better-placed than a summary at the top of `CFG`, since it sits where a reader editing the constant will see it. Checked; no change.
- **Formal Git tags or GitHub Releases per version** — genuinely new, and a repository action rather than a code change; logged below under Model Architecture Feedback for Duke.

### What checking the handoff itself turned up

This release's own working documents were verified with the same discipline as the audits, and the verification found errors in them — recorded here because catching them is the point of the practice:

1. **The "13% larger" figure** (above) was really 15.4%.
2. **The partially-built v4.15 `index.html` carried forward from the previous session was not a faithful copy of v4.14.** It had silently dropped many CSS comment blocks (all the `/* v4.8 fix: … */` explanations, among others) and rewritten the JSON-LD escape sequences. Rather than complete it, `index.html` was rebuilt from the untouched v4.14 source with assertion-checked edits (every replacement asserts it matched exactly the expected number of times), and the draft was used only as a source for new prose. A line-by-line diff of the shipped file against v4.14 shows only intended hunks.
3. **The draft's description of the missing-`expiry` failure understated it** (it mentioned only the NaN totals, not the zeroed participant wealth). Measured and corrected above.
4. **A draft note in the Empirical Calibration card described Grok as approving the existing `SIM_COST_SCALE` marker**, when the audit had suggested adding one. The marker already exists (above), so no change was needed — but the note mischaracterised the audit and was dropped rather than shipped.

### Found in passing: the replication page's header toggle was clipping its own content

Adding a v4.15 paragraph to the replication page's collapsible "Version highlights" block (in its header) turned up an existing defect: `.hdr-toggle-body.open` capped the block at `max-height:700px` with `overflow:hidden`, but its content was already about 5,800 visible characters — roughly 900px on desktop by estimate, considerably more on a phone. The oldest lines were therefore being silently clipped before this release, and every release since v4.8 that prepended text made it worse. The cap is raised to 8000px, the same technique `.changelog-body` already uses (20000px). **This is an estimate from character counts, not a browser measurement** — `domtest.js`/jsdom has no layout engine — so it warrants a visual look at a couple of widths after deploying. It is the only CSS change in this release.

### What did NOT get done, and why

- **PTH entry/exit dynamics.** PTH membership remains a one-time draw. This is a design simplification present since v4.0 (housing transitions are slow relative to a model year, and PTH construction capacity is not modelled), not something this release changes; it belongs with the rollout/transition-path item under Good First Issues.
- **Everything logged at v4.14 remains open and unchanged:** the full flow-of-funds ledger, monthly BU tranches, CCO/PTH pathway decomposition, λ heterogeneity beyond fixed-and-independent, AI automation as an employment-transition model and a fuller macro-recession model, the explicit enumeration of `runYear()`'s annual state-transition schedule, and the expanded invariant/mechanism/calibration test taxonomy.
- **No fresh N=5,000 study.** None is needed: the mechanics fix is provably inert on every documented configuration, so no documented large-N figure moves. This is the second consecutive release where that is true, and the reason is the same — the fix was proven inert *before* being written, on every shipped preset and every `VAL_TEST`.
- **No CSS, markup, or layout change to the interactive tool (`index.html`).** The only CSS change in the release is the replication page's header-toggle cap, above; `domtest.js` does not verify layout.

### Regression: seed 42 / Full Integration / 20yr, v4.14 → v4.15

| Metric | v4.14 | v4.15 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |
| System Stability | 88.5% | 88.5% | — |
| Pinned at Wealth Floor | 10.6% | 10.6% | — |

Confirmed three ways: `harness.js validate` (both fixes ported for parity; JSON above reproduced exactly, including `fracAtFloor` matching the documented 10.6% Wealth Floor Diagnostic); `domtest.js` driving the actual edited `index.html` end-to-end through a real DOM — **29 checks now, four new this release** — reproducing the regression exactly through the live page; and the old-vs-new preset comparison (every agent's final wealth identical in four of five presets, Stress Test the sole exception by construction).

**`domtest.js` gained four checks this release, and they are demonstrably real guards.** Each is written to fail gracefully rather than throw, and the same file run against an unmodified v4.14 `index.html` fails exactly these four and passes the other 25: PTH-on with zero members must be bit-identical to PTH-off; a missing `expiry` must behave as the default; `tCritical95` must return Student's t; and the rendered CI must use it and state t and df. A regression guard that has never been seen to fail is a claim, not a guard — these have been seen to fail.

---

## v4.14 Release Notes

v4.14 responds to a two-pass external ChatGPT audit — a general review of `index.html` and `CONTRIBUTING.md`, followed by a second pass focused exclusively on the economic mathematics and causal structure of `runYear()`. Duke forwarded both passes together. Per this project's standing practice, every claim was checked against source before acting on it. The second pass earned that discipline: it found two genuine mechanics bugs that seven prior audits and this project's own six-check validation suite had missed, both now fixed. **Zero effect on the documented seed-42/Full Integration/20yr regression** (Median BLEI 1,965d, Median wealth $559,223, Gini 0.534, Wealth poverty 16.6%) — confirmed by re-running `harness.js`, by driving the fixed engine through `domtest.js` end-to-end, and by isolated before/after checks on every configuration either fix actually touches.

### How this audit differed from prior ones, and why it's treated more carefully

Most external audits this project has received are general-purpose reviews of the shipped page and its documentation. This one's second pass did something none of the others did: it read `runYear()` as a dynamical system rather than a list of independent annual adjustments, and asked what feedback loops the actual equations create. That angle found two real defects — not restatements of known limitations, not misreadings of existing guard clauses (the failure mode of several past audits' rejected findings), but genuine mismatches between what a parameter's label promises and what its equation delivers. Both are documented in detail below, including the verification work that confirmed each one before it was touched.

### Bug found and fixed: the BU-expiry slider implemented two behaviours, not six

The UI presents "BU expiry (months)" as a slider from 1 to 6. The code that consumes it:

```js
var decay=p.expiry<2?0:0.7;
a.buBalance=Math.min(a.buBalance*decay+p.bu,p.bu*3);
```

`p.expiry<2` is only ever true at exactly `expiry=1`. Every other slider position — 2, 3, 4, 5, 6 — evaluates the same `false` branch and gets the identical `decay=0.7`. A six-position slider that implements exactly two distinct behaviours, with no way for a user to tell from the UI that dragging from 2 to 6 does nothing.

**Verified directly before touching anything.** A standalone before/after harness run (seed 42, CCO-only isolate so the effect is attributable to this one mechanism, no PTF/PTH) confirmed `expiry=3` and `expiry=6` produced bit-identical output on the unedited engine — median wealth $402,103, poverty 25.0%, BLEI poverty 21.2%, all three digits matching to the last place. That's not a plausible coincidence; it's the step function doing exactly what the code says.

**Fix.** Replaced the step function with a continuous annual-approximation decay, `decay=1-1/expiry` — the same kind of documented interpretation `pthLiquidShare()` already uses for a comparably under-specified continuous quantity (that function interpolates linearly between two cited anchor points; this one interpolates a plausible curve through the one anchor the shipped code actually pins, `expiry=1`). A full "proper" fix — monthly BU tranches tracked and expired individually, since `runYear()` runs once per simulated year but BU expiry is stated in months — was considered and set aside: it's a materially larger rearchitecture of an annual-cadence loop, and this project's practice is not to take on a rearchitecture of that size inside an audit-response release. Logged as a Good First Issue, below, with the annual-approximation fix's own honest scope stated so nobody mistakes it for the monthly-tranche model.

**Verified to be inert on everything documented.** `expiry=1` is the value used by all five shipped presets (`baseline`, `cco`, `reference`, `stress`, `hiAI`), by `mkMiniP()`'s hardcoded default (used by every `VAL_TEST`), and by every OAT/LHS scenario (neither `RANGE` nor `LHS_RANGE` ever varies `expiry`) — confirmed by grep before writing a line of the fix, not assumed. At `expiry=1`, `decay=1-1/1=0`, identical to the old value. **This fix therefore cannot move a single documented figure anywhere in this project** — it only changes behaviour for a user who manually drags this one slider away from its default. After the fix, six slider positions now produce six genuinely distinct, monotonically-ordered results (seed 42, same isolate config):

| expiry | decay | median wealth | wealth poverty | BLEI poverty |
|---|---|---|---|---|
| 1 | 0.000 | $386,836 | 25.8% | 22.2% |
| 2 | 0.500 | $396,600 | 25.0% | 21.8% |
| 3 | 0.667 | $401,139 | 25.0% | 21.4% |
| 4 | 0.750 | $403,587 | 24.8% | 21.0% |
| 5 | 0.800 | $405,117 | 24.8% | 21.0% |
| 6 | 0.833 | $406,164 | 24.6% | 21.0% |

Ported into `harness.js` for parity, with the same reasoning recorded in its own comment. Re-confirmed via `harness.js validate` (seed-42 regression unchanged) and via a fresh N=100 `harness.js sweep` run whose `WEALTH_FLOOR=-10000` Full Integration figures (Gini mean 0.516, wealth-poverty mean 15.3%) land within normal N=100-vs-N=500 sampling noise of the documented N=500 sweep table (v4.8) — nothing about the sweep machinery broke.

### Bug found and fixed: PTF's inflation-damping effect tracked the initial slider, not actual adoption

```js
var inflRate=p.inflRate||0;
if(p.ptf&&inflRate>0)inflRate*=(1-p.ptfShare*0.5);
```

`p.ptfShare` is the **static initial-adoption-probability slider** — the same value the UI's own tooltip already says organic adoption "can exceed" (v3.6+; confirmed in practice at 53.4% realised vs. an 18% slider, per v4.6's own findings). Meanwhile, three lines above this in the exact same function, `runYear()` already computes the thing that should have been used instead:

```js
var ptfAdoptFrac=0;
if(p.ptf&&p.ptfShare>0){var ptfCount=0;agentSet.forEach(function(a){if(a.inPTF)ptfCount++;});ptfAdoptFrac=ptfCount/Math.max(1,agentSet.length);}
```

`ptfAdoptFrac` — the population's **actual current** PTF membership fraction — exists specifically to feed the Bass-diffusion adoption term a few lines later. It was never reused here. This is a genuine state-variable/effect mismatch, not a design choice: the per-agent cost factor a few lines further down already gates correctly on each agent's real `a.inPTF` flag (`if(p.ptf&&a.inPTF)cf*=(1-...)`), so the codebase clearly knows the difference between "the slider" and "who's actually in PTF" — it just used the wrong one for this one macro-level effect.

**Fix.** Moved `ptfAdoptFrac`'s computation earlier in the function (it draws no RNG and reads only already-set `a.inPTF` flags on the existing `agentSet`, so this reordering shifts no draw, anywhere, for anyone) and reused it: `inflRate*=(1-ptfAdoptFrac*0.5)`.

**Verified to be inert on every documented figure, then measured where it isn't.** Checked systematically before writing the fix: Full Integration, hiAI, and CCO-Only all have `inflRate=0` at this exact line (the `inflRate>0` guard never fires); Baseline and CCO-Only both have `ptf=false` (the `p.ptf&&` guard never fires); so **none of the four internally-defined comparison configurations, and none of the documented regression or large-N figures, are touched by this fix at all.** Of the five shipped presets, only **Stress Test** combines `ptf:true` with nonzero `inflRate` (2%). Of the six `VAL_TESTS`, only **`ptf_infl`** exercises this exact line (`mkMiniP(PRESETS.reference,{inflRate:0.03})` vs. the same with `ptf:false`) — re-run after the fix and confirmed still 5/5.

Effect size where the fix does apply, seed 42/20yr:

| Config | Metric | Before | After |
|---|---|---|---|
| Stress Test preset | Poverty | 43.0% | 41.8% |
| | Gini (EDC-adj.) | 0.703 | 0.696 |
| | Median wealth | $141,814 | $158,155 |
| | Median BLEI | 431d | 482d |
| Synthetic isolate (PTF + 4% inflation, no PTH/SZH/CIP) | Poverty | 46.0% | 43.0% |
| | Gini (EDC-adj.) | 0.712 | 0.695 |
| | Median wealth | $73,335 | $116,901 |

Both move in the economically expected direction: Stress Test's actual PTF adoption (starting at an 8% slider, growing via Bass diffusion and economic-distress adoption under 40% overall participation) runs above the static slider on average over 20 years, so the fix applies *stronger* damping than the bug did, not weaker — lower poverty, lower Gini, higher wealth. Ported into `harness.js` for parity, same reasoning recorded in its own comment.

### New reporting feature: Wealth Floor Diagnostic

The audit's general-review pass asked for exactly the thing its own suggested recommendation named: an in-app diagnostic showing how much of a Baseline-vs-Your-Settings gap reflects `WEALTH_FLOOR`'s exact value rather than a genuine policy effect. This project had already answered a version of that question — but only offline, in CONTRIBUTING.md's own four-floor-value sensitivity sweep (v4.8), which most users of the deployed page will never see.

Two new KPIs — **"Pinned at Wealth Floor, final year"**, for Your Settings and for Baseline — show the share of the final-year population sitting exactly at `WEALTH_FLOOR`. Pure snapshot of already-final agent state: one `.filter()` over the `agents` array, no new simulation, no RNG. At the seed-42 reference configuration: Your Settings 10.6% (matching `harness.js`'s own `fracAtFloor` output to the decimal), Baseline 68.6% — consistent with, though not identical to, the v4.8 sweep's "Baseline's median is pinned in 100% of N=5,000 runs" finding, since a 68.6% floor-pinned share is comfortably over the 50% a pinned median requires. **This is a companion to the offline sweep, not a replacement for it** — seeing today's pinning doesn't show how *sensitive* that pinning is to `WEALTH_FLOOR`'s own value, which only the multi-floor-value sweep answers; both the in-app tooltip and this document cross-reference the other. Exported to CSV and JSON.

### Documentation clarifications (no code or mechanics changes)

Several of the audit's findings were real but didn't call for a code change — the underlying mechanic was already correct, the issue was that a reader could reasonably misread what it means. Each is now stated explicitly, in the location named:

- **EDC-adjusted Gini** is computed as `W_nominal - EDC×Y×12` — a wealth *stock* minus one year of EDC-implied extraction, a *flow*. The audit is right that this isn't "wealth after all extractive costs" in a conventional accounting sense; it's a stock adjusted by one year's estimated extractive burden, a deliberately constructed inequality index rather than canonical net worth. The formula is exactly BLEI paper Table 6's own specification and is unchanged — only the interpretation needed stating plainly. Now explicit in both the Gini KPI's tooltip and the code's own comment at the computation site.
- **A dual-cost-anchor table** — `LIVING_WAGE_ANNUAL` ($49,370, main wealth loop) vs. `BASE_DAILY_COST` ($68.33/day, BLEI/FBS/PTH-equity) — added directly to the Empirical Calibration card, so a reader doesn't have to reconstruct from surrounding prose that these are deliberately different concepts (an ongoing-cost-of-living anchor vs. a subsistence-floor anchor) rather than two measurements of the same thing.
- **The ODD panel's Design Concepts card**, and an inline comment at the octave-advancement site inside `runYear()` itself, now name the reinforcing loops the audit's `runYear()` review correctly identified: BLEI(prior year) → wage growth → wage → FBS → octave → {next year's wage growth, next year's conversion-rate ceiling} → wealth, and separately PTH → lower cost → higher FBS → octave → wage. Neither loop is a bug — both are the intended behavioural design — but a headline "CCO effect" or "PTH effect" is a *compound* of several coupled mechanisms (cost relief, financial bandwidth, skill advancement, wage growth, conversion compounding), not one isolated channel, and nothing previously said so explicitly. The audit's suggestion to go further and formally decompose a headline delta into its component pathways (`ΔW = ΔW_direct + ΔW_wage + ΔW_octave + ΔW_conversion`) is a legitimate, larger feature — logged below, not attempted this pass.
- **A new Known Limitations entry** states plainly that "recession" only ever shocks earned wage income (no asset prices, employment status, housing costs, transfers, or interest rates) and "AI automation" is a reduced-form wage-growth penalty (no explicit job loss, search, or re-employment transition) — both real, calibrated mechanisms, both narrower than their names might suggest to a reader who hasn't read the code.
- **The standing "exploratory simulation — not a forecast" banner** gained one sentence, taken close to verbatim from the audit's own suggested wording: results demonstrate the implications of the implemented assumptions; they do not by themselves establish that the underlying assumptions or parameter values are empirically valid.

### What the audit got right that this project had already substantially addressed

Distinguishing a genuine new finding from a restatement of existing work is the entire point of a verification pass, not a formality — several of the audit's recommendations, checked against source, turned out to already be shipped or already logged in detail:

- **"Formally divide validation into Level 1–5"** — this exact language, verbatim, has been in the validation panel's own subtitle since v4.2: *"ODD Level 1–3: code correctness, mathematical invariants, behavioral validation... not external empirical validation (Level 4–5, not yet performed; see Known Limitations)."* Nothing to formalize that wasn't already explicit and in-app.
- **FBS λ "still heavily calibrated by assumption," and the FBS₅₀ = ln(2)/λ reparameterization** — the λ Calibration Status note (below) already treats λ as a behavioral parameter with an explicit calibration range, not an empirically-validated one, and the FBS₅₀ reparameterization the audit recommends was shipped as `CFG.FBS_HALF_SAT_LO/HI` in v4.6.
- **The CCO stock-flow accounting gap** ("no system-level counterparty for conversion proceeds") — this has been an explicit, named Known Limitation since v4.0 ("CCO conversion proceeds are tracked but not production-constrained"). The audit's specific proposed ledger schema (BU issued/redeemed/expired/converted, conversion-tax receipts, treasury balance, PTF operating surplus, aggregate production/consumption) is a genuinely more detailed elaboration of that same open item — logged below with the fuller schema attached, not attempted as code.
- **Splitting `index.html` into `src/` modules with a build step** — the identical suggestion from an external ChatGPT audit at v4.7, rejected then as conflicting with this project's explicit single-buildless-file distribution constraint. Same conclusion here, for the same reason; not re-litigated.
- **Playwright/Chromium browser testing beyond `domtest.js`** — already an explicitly flagged open decision in v4.13's own Model Architecture Feedback, with three options weighed (status quo, headless browser, reference screenshots). The audit reinforces the same point with no new information; still Duke's call.
- **The dominance-check terminology concern** ("readers may upgrade a pointwise comparison into a stochastic-dominance result") — v4.13 already added exactly this distinction to both chart captions: *"it is evaluated at the thresholds actually plotted, not continuously... and it describes this single stochastic run, not a confidence statement."*

### Considered and declined: renaming "System Stability"

The audit suggests relabeling the System Stability KPI to something like "Late-Run Trajectory Stability," since a smoothly worsening trajectory can score as "stable." The underlying concern is real and has been an explicit, named Known Limitation since v4.4 ("System Stability can score a stagnant floor as more stable than a thriving population"), with its own KPI tooltip and multiple large-N demonstrations (Baseline scoring 99.0% precisely because it has nowhere left to fall). Renaming a headline KPI referenced throughout exported CSV/JSON column headers, chart labels, and several releases' worth of documentation is a genuinely disruptive change for a label that is already comprehensively caveated at the point of display. This mirrors the audit's *own* stated preference elsewhere in the same document — it explicitly declines to recommend renaming the "wealth" variable for exactly this reason ("changing the terminology throughout the project would be disruptive... I would strongly prefer" keeping the name and defining it precisely instead). Applying that same logic here: not renamed. If Duke judges the disruption worth it, that's a naming call for the framework's author, not a code-audit finding — logged as an option, not acted on unilaterally.

### What did NOT get done, and why

By scope, several of the audit's recommendations are legitimate but substantially larger than an audit-response release should take on unilaterally — each is logged below with a precise scope, not a vague "future work" gesture:

- **A full aggregate flow-of-funds ledger** with explicit conservation identities (BU issued/redeemed/expired/converted, conversion-tax receipts, treasury balance, PTF operating surplus/deficit, PTH equity inflows/outflows, aggregate production/consumption) — elaborates the existing stock-flow Known Limitation with the audit's specific proposed schema. A substantial economic-modelling undertaking, not a bug fix.
- **Monthly BU tranches**, replacing the annual-approximation `decay=1-1/expiry` fix shipped this release with the audit's own suggested "proper" mechanism (individual monthly BU allocations tracked and expired on their own schedule within an annual-cadence loop). Logged precisely so a future session knows the shipped fix's honest scope.
- **CCO/PTH pathway decomposition** — formally splitting a headline effect into `ΔW_direct + ΔW_wage + ΔW_octave + ΔW_conversion` via structured ablation (Model A: full CCO; B: no conversion proceeds; C: no octave advancement; D: no octave→wage bonus; E: no cost reduction). A legitimate, large extension of the existing ablation engine.
- **Time-varying or wage-correlated λ heterogeneity** — the audit correctly notes that fixed, persistent per-agent λ is "a coherent heterogeneity assumption" but one worth sensitivity-testing against alternatives (time-varying λ, λ correlated with initial wage, λ independent of other latent traits). Extension of the existing λ Calibration Status note, below.
- **AI automation as an employment-transition model** (job displacement → search → re-employment) rather than a reduced-form wage-growth penalty, and **a fuller macro-recession model** (asset prices, employment transitions, government transfers, interest rates) rather than an income-only shock — both cross-referenced from the new Known Limitations entry above, both substantial modelling undertakings in their own right.
- **An expanded invariant/mechanism/calibration test taxonomy.** `VAL_TESTS` already has a genuine invariants check (population conservation, octave/wealth-floor/participation bounds, Gini bounds, since v4.2) and NaN/Inf guards exist throughout the engine's own code — but several specific checks the audit lists are not currently asserted as tests: same-seed-reproduces-identical-output, different-seed-changes-output, PTF-cap-never-exceeded-when-enabled, and probability values staying in [0,1] as explicit assertions rather than implicit guarantees. A legitimate, scoped extension of the existing suite.
- **Explicitly enumerating `runYear()`'s full annual state-transition schedule** as a numbered, ordered list (the audit supplies its own 16-step attempt) — genuinely valuable and genuinely not written down anywhere as an explicit sequence today, but re-deriving it correctly from the actual code, line by line, carries real risk of introducing a documentation error if rushed alongside everything else in this release. Deliberately deferred rather than risk shipping an inaccurate sequence; logged as a Good First Issue with that caution stated.
- Also not attempted, unchanged from v4.13: `LIVING_WAGE_ANNUAL` population-weighting, `WEALTH_INIT_MU`/SCF gap, `TARGET_*` recalibration, occupation-stratified `automationRisk`, unbounded long-horizon wealth growth, per-agent longitudinal tracking, and the replication page's out-of-chronological-order revision tail.

### Regression: seed 42 / Full Integration / 20yr, v4.13 → v4.14

| Metric | v4.13 | v4.14 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |
| System Stability | 88.5% | 88.5% | — |
| Pinned at Wealth Floor (new) | — | 10.6% | new metric |

Confirmed four ways: `harness.js validate` (both mechanics fixes ported for parity, regression unchanged); `domtest.js` driving the actual edited `index.html` end-to-end through a real DOM (25 checks now, six new this release guarding directly against the two bugs just fixed — a slider-value-collapse check and a static-vs-actual-adoption check, so neither can silently return); a fresh N=100 `harness.js sweep` run whose figures land within normal sampling noise of the documented N=500 WEALTH_FLOOR table; and the isolated before/after checks shown inline above for every configuration either fix actually touches.

**`domtest.js` gained six checks this release** — two proving the two mechanics fixes are actually inert at the shipped default and actually different at other slider values (a direct regression guard: if either bug is ever reintroduced, these fail immediately), and four covering the new Wealth Floor Diagnostic's bounds and its CSV/JSON export.

---

## v4.13 Release Notes

v4.13 is an independent-audit pass, run on `index.html` and this document for "clarity, rigor, and technical issues." It is the first release in this project's history in which the audit **ran the shipped page** rather than reading it — and that single methodological change is what produced most of what follows. **Zero simulation-mechanics changes for any run of 8 or more simulated years**: the seed-42/Full Integration/20yr regression (Median BLEI 1,965d, Median wealth $559,223, Gini 0.534, Wealth poverty 16.6%) is unchanged and was confirmed three ways this session — by re-running the untouched `harness.js`, by driving the actual edited page end-to-end in a headless DOM, and by a direct sweep proving the one metric change is inert at every run length from 8 to 30 years.

### The methodological point first, because it explains the findings

This project's validation checklist — div balance, CSS brace balance, `node --check`, JSON-LD parse, harness regression — is genuinely strong, and it is structurally incapable of catching an entire class of defect, because **not one of those checks ever runs the page**. `harness.js` transcribes the engine's pure functions and verifies the numbers; it has no DOM, no event handlers, no render path. Every UI change from v4.8 through v4.12 therefore shipped with an explicit "not verified in an actual browser" caveat, and that caveat was load-bearing: two real, user-visible defects had been live for eight releases.

This session added `domtest.js`, a jsdom harness that loads `index.html` with `runScripts:'outside-only'` (so the page's own auto-run never fires and every function can be exercised deliberately), stubs Chart.js, and asserts DOM behaviour — 19 checks covering classes, attributes, render paths, export payloads, and a full seed-42 run driven through the live page. It found both defects immediately. **It is now committed alongside `harness.js`**, and its own header states plainly what it does *not* cover: CSS layout, tooltip positioning, responsive behaviour, and Chart.js pixel output are all still unverified and still want a human look after deploy. A green `domtest.js` run is not "the UI is verified."

### Defect 1 — a shared parameter link silently disabled every preset tooltip

`applyParamsFromURL()` cleared the preset buttons' "active" highlight by resetting each button's class to a bare `pbtn`. That also removed `.tip-host`, the class the v4.5 preset-description tooltips are attached to. **Any visitor opening the tool through a "Copy parameters as URL" link lost all five preset hover descriptions for the entire session** — silently, with nothing visibly wrong and no error.

This is the *same* bug v4.5's own release notes record catching, one function away:

> Caught in testing: `applyPreset()`'s active-button styling directly overwrote `className` on every preset click, which would have silently stripped the new tooltip class the first time any preset was selected — fixed as part of this change, not a separate regression.

The identical pattern was written into `applyParamsFromURL()` in that same release and survived seven subsequent audits, for a specific and instructive reason: the shared-link path is the one entry point a reviewer reading `index.html` top to bottom never mentally executes, and the one path no automated check had ever taken. Fixed to `'pbtn tip-host'` (the no-preset-is-active intent is preserved — `pbtn-active` is simply never added), and now regression-tested.

### Defect 2 — the sensitivity panel duplicated its tip box on every run

`renderSens()` wrote its "💡 One-at-a-Time (OAT) Sensitivity" note with `insertAdjacentHTML('afterend', …)`, which inserts a **sibling** of `#sens-inner`. The function's own `inn.innerHTML = h` reset clears that element's *children*, never its siblings — and `renderSens()` runs once per completed simulation. Three runs in one page session left three stacked copies of the tip box. Confirmed in the harness (3 boxes after 3 renders before the fix, 1 after) and rewritten as a single stable-id node created once and updated in place.

### A metric that reported a perfect score where it had no data

`structuralStability()` is the inverse coefficient of variation of median wealth and median BLEI over the run's final quarter, with the window computed as `Math.max(1, Math.floor(years/4))`. The Simulation-years slider's own minimum is **5** — and for any run of 5, 6 or 7 years, `Math.floor(years/4)` is 1. `coeffVar()` correctly returns 0 for a single sample (the variance of one observation is undefined), giving `1/(1+0) = 1` for both series, and the metric returned **exactly 0.99 — its own clamp ceiling — for every 5–7 year run this tool has ever executed**, whatever happened in it.

Verified rather than reasoned: a strictly-increasing five-point series scored 0.990000, as did every other short series tried. This is the same failure the Known Limitations panel already describes for a floor-pinned population ("flat outcomes score as maximally stable"), except arising from having *no data in the window* rather than from the data being flat — and it reported a maximum where the honest answer is "not enough of the run to measure."

**Fix and its exact scope.** The floor is now 2. A sweep across every supported run length confirms lengths **8–30 are bit-identical to v4.12** (at 8 years `floor(8/4)` is already 2), so every preset, the 20-year reference configuration, the seed-42 regression baseline, and every OAT/LHS/ablation/validation mini-run at 10 or 20 years is untouched. Only 5–7 year runs change, and only in this one displayed number. A matching Known Limitations entry now states that System Stability needs roughly 8+ simulated years to mean anything, on top of the separate CV-formula limitation already documented.

Worth naming: this is a *mechanics-adjacent* change by this project's own standards, since it alters a reported number for some configurations. It is shipped in a non-mechanics release because the affected set is provably disjoint from every documented figure, and because leaving a metric reporting a constant maximum is worse than a scoped correction. If a future session prefers the stricter reading, the alternative is to display "n/a" below 8 years instead — noted rather than assumed away.

### Stale documentation *inside* the engine, where v4.12 fixed it only *around* the engine

v4.12 corrected the ODD Protocol panel, the Empirical Calibration panel, and the top-of-file `UNIT SYSTEM` comment for describing pre-v4.3/pre-v4.4 mechanics as current. The same staleness was sitting inside `runYear()` the entire time — the function all three of those panels describe, and the copy a contributor editing the engine actually reads. Four claims, each contradicted by code beside it:

- **"SIM_COST_SCALE … remains load-bearing only as an input to the legacy SIU_TO_USD derivation … that BLEI/FBS/Gini still use, deliberately un-migrated."** `SIU_TO_USD` was retired in v4.4 and those formulas moved to `WAGE_TO_USD`. Grep confirms `CFG.SIM_COST_SCALE` now has **zero read sites anywhere in the file** — it appears only in its own definition and in prose.
- **"dollarCost … still used only by the FBS advancement gate below."** It has two consumers: the FBS gate's `cBasicMonthly` *and* the PTH block's `pthSaving`.
- **"Yusd/cBasicMonthly use SIU_TO_USD/dollarCost."** The line directly beneath reads `CFG.WAGE_TO_USD`.
- **"FBS doesn't feed back into wealth."** It does — FBS gates octave advancement, octave sets CCO conversion capacity and adds a wage-growth bonus. This is precisely the feedback path v4.4's own release notes give as the reason `FBS_LAMBDA` needed a compensating rescale, so the comment contradicts this project's documented account of its own release.

Plus `CFG.SIM_COST_SCALE`'s inline comment claiming it is "retained for CCO/PTF/PTH cost-factor calc only" — the cost factor is a product of dimensionless multipliers and never reads it. All corrected in place, each with a short note recording what was wrong, per the established practice of documenting a correction rather than swapping text silently.

### Two reporting additions

**Cumulative Poverty Exposure.** Every poverty figure this tool reported was a final-year snapshot. Two runs can end with the same headline rate having put very different numbers of agents through very different numbers of poor years — a gap the v4.12 external audit raised directly (its person-years-in-poverty suggestion, logged then as deferred). Two new KPIs report the **mean number of years an agent spends below the wealth-poverty line, and below the BLEI poverty line, across the whole run**, for Your Settings against the Traditional Welfare Baseline.

The derivation is exact, not an approximation. Each year's figure is a share of the same population, so

```
Σ_t share_t  =  (1/N) · Σ_t Σ_i 1[poor_{i,t}]  =  mean years poor per agent
```

At the seed-42 reference configuration the final-year wealth-poverty rate is **16.6%**, but the average agent spends **4.81 of 20 years** below that line — against the Baseline's **11.80**. BLEI-poverty exposure is 3.74 years against the Baseline's 11.09. That is a materially different and previously invisible view of a run this project has quoted dozens of times.

Purely a reporting transform of arrays the engine already computes. The only new computation anywhere is one extra `bleiMetrics()` call per baseline year, to obtain the baseline's annual poverty *share* (its annual *median* was already tracked, and a median cannot give a headcount); `bleiMetrics()` is pure, draws no RNG and mutates nothing — confirmed by the unchanged regression. Exported to CSV and JSON. **One honest limit, stated in Known Limitations rather than only here:** this is aggregate exposure, not a spell-length distribution. It cannot distinguish "everyone poor for 3 years" from "30% of agents poor for 10 years," which needs per-agent longitudinal tracking this engine does not keep.

**The v4.12 dominance check is now exportable.** It was screen-only — a reader could see the finding but had no way to archive or cite it with the run that produced it, unlike every other figure this tool computes. Now captured into the run snapshot and written to both export formats, together with the view it was computed in and the number of threshold grid points it was evaluated at. `setThreshView()` refreshes the snapshot so an export always matches what is on screen. The on-page caption also gained two caveats it should have had at v4.12: dominance is checked **at the plotted thresholds only** (a crossing narrower than one grid step would not be reported), and it describes **one stochastic run**, not a confidence statement.

### Smaller fixes

- **Wealth Poverty KPI arrow.** It prefixed a hardcoded `▼` to a *signed* delta, so a configuration doing worse than baseline rendered as "▼ -3.2pp". Reachable in ordinary use — select the Traditional Welfare preset and Your Settings and Baseline are near-identical, so the delta can land either side of zero. Arrow now follows the sign; magnitude is unsigned.
- **Two grids built in JS template strings still used a bare `1fr` track** — the exact CSS Grid overflow pattern v4.8 swept out of the stylesheet, missed then because that sweep grepped CSS and these are inline strings in `renderMultiRunSummary()` and `renderValidation()`. The Monte Carlo summary's three fixed columns also never reflowed on a phone; it is now `auto-fit` with a real 140px minimum, and `.ci-card` gained `min-width:0`.
- **`aria-pressed` on every toggle button.** Until now each On/Off pair communicated its state through colour and a CSS class alone — a screen reader heard two identically-labelled buttons with no indication of which was active, the same class of gap v3.7 closed for the charts. Set statically in the markup so the attribute is correct before any script runs, and kept in sync by `tog()`. The harness caught a JS-only first attempt leaving the PTF-cap pair unlabelled, since no preset calls `tog()` for it.
- **Exported JSON asserted a flat `"CC BY 4.0"` license**, unchanged since before the v4.8 relicensing split — every export since has quietly asserted one license for a project that has had two. Now states both explicitly (exported data: CC BY 4.0; simulation source: Apache 2.0).
- **The CSV's mechanics list was still headed `--- v4.0 FIXES ---`** nine releases later, enumerating a hand-picked selection that stopped being "the fixes" long ago. Relabelled to describe what it is — an orientation subset — and pointed at this document as the canonical account rather than growing a changelog inside a CSV.
- **`CFG.POVERTY_LINE` now carries a note at the constant itself** recording that it has no citation anywhere in this codebase. That has been an open `calibration:` item in the table below since v4.10, with nothing at the code to warn a reader who never opens this file — and it is now also the denominator of a new headline metric, which raises the cost of leaving it unmarked.
- **On the replication page:** the header subtitle still read v4.9 and the Version History toggle label still read "(v3.1 → v4.9)", both four releases stale. The second is the very label v4.9's own entry records fixing when it had drifted to "v3.1 → v4.7" — it has now gone stale, and been caught, twice. Both corrected, with the recurrence named rather than quietly re-numbered; highlight-box and revision-note counts were recounted by direct count (13 and 21).
- **In this document: two release sections had lost their `## …Release Notes` headings entirely** — v4.11's and v4.5's — so each rendered as a continuation of the section above it and neither appeared in any generated table of contents. The second was found only because the first prompted listing *every* `## ` heading in the file rather than assuming one casualty; a single grep would have caught either at any point in the last eight releases. Both restored, each with an inline note.

### What did NOT get done, and why

The five structural proposals logged at v4.12 all remain open and unstarted: the executable test hierarchy, the positional-argument refactor, a calibrated current-U.S.-policy comparison scenario, a rollout/transition-path model, and per-agent longitudinal metrics. Two notes on how v4.13 changes their standing rather than their status:

- The **test hierarchy** is now partly begun, not by design but as a by-product: `domtest.js` covers the "does the page behave" layer that neither `harness.js` nor `VAL_TESTS` touch. What is still missing is the rest of the audit's proposed structure — pure-function tests, accounting-invariant tests, scenario-pairing tests, stored regression fixtures beyond the single seed-42 table, and documentation-snapshot tests. Someone picking this up should build *around* `domtest.js` rather than starting over. Note the single-buildless-file constraint applies to `index.html`, not to Node-side dev tooling — `harness.js` and now `domtest.js` are both outside it, and `domtest.js` adds one dev-only dependency (`jsdom`), which is worth flagging explicitly for Duke's approval since it is the project's first.
- **Per-agent longitudinal metrics** are now the most clearly motivated of the five, because the new exposure metric runs directly into their absence — it can say how many agent-years of poverty a configuration produces but not how they are distributed, and that distinction is exactly what the audit's time-to-tier and recovery-rate suggestions would answer.

Also not attempted: `LIVING_WAGE_ANNUAL` (unchanged — still needs its own mechanics-audit release), `WEALTH_INIT_MU`/SCF, `WEALTH_FLOOR`/`TARGET_*` recalibration, occupation-stratified `automationRisk`, the unbounded long-horizon wealth question, a normalized (ratio) poverty-gap view, and the replication page's out-of-chronological-order revision tail — all unchanged from v4.12.

### Regression: seed 42 / Full Integration / 20yr, v4.12 → v4.13

| Metric | v4.12 | v4.13 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |
| System Stability | 88.5% | 88.5% | — |

Confirmed three ways: `harness.js` (untouched, still `Math.max(1,…)` in its own copy of `structuralStability` — which at 20 years resolves to the same window, and so is an independent confirmation that the change is inert here); `domtest.js` driving the actual edited page end-to-end in a DOM; and a direct old-vs-new sweep of `structuralStability()` across run lengths 5–30, showing divergence at exactly 5, 6 and 7 and nowhere else.

**New in this release, and worth adding to the reproducibility routine:** `node domtest.js` (after `npm install jsdom`) runs 19 DOM-behaviour checks plus a full seed-42 run through the live page in roughly two minutes. Run it alongside `node harness.js validate` before shipping any change that touches markup, CSS classes, or a render function.

---

## v4.12 Release Notes

v4.12 is a documentation-and-verification pass prompted by an external audit (Perplexity AI, forwarded by Duke with an explicit instruction not to assume it was error-free), plus one small feature addition the audit's own suggestions pointed toward directly. Per this project's standing practice, every checkable claim in the audit was verified against source code or by direct computation before anything was acted on. **Zero simulation-mechanics changes**: nothing here touches `makeAgent()`/`instantiateAgent()`, `runYear()`, or any metric function, so the v4.11 seed-42/Full Integration/20yr regression figures (Median BLEI 1,965d, Median wealth $559,223, Gini 0.534, Wealth poverty 16.6%) still apply unchanged — confirmed three separate ways this session: by re-running `harness.js` untouched, by a fresh standalone Node.js harness built for the PTF-cap investigation below, and by a full end-to-end integration test that evaluated the *actual edited* `index.html` script (not a hand-copied approximation) in a stubbed DOM-free sandbox and reproduced every headline figure exactly.

### The audit, and how this session approached it

The audit covers a lot of ground — a findings table, "clarity and interpretation" issues, a proposed technical-debt roadmap, and a four-release sequencing plan. Its own stated scope excluded items this project already tracks at length (the wealth-init/SCF gap, `WEALTH_FLOOR`/`TARGET_*` recalibration, long-horizon unbounded wealth, the production/treasury constraint, the low-wage mechanism gap, occupation-stratified `automationRisk`, `LIVING_WAGE_ANNUAL` re-estimation) — that scoping was accurate and is respected here. Of what remained, one finding pointed at a genuine, previously-unnoticed **bug** (not just documentation drift) in this project's own PTF-cap documentation; several findings pointed at genuine, previously-unnoticed **documentation staleness** (technical panels describing superseded mechanics as current); one finding's central suggestion became this release's **new feature**; a few findings restated **already-documented, deliberate design choices** rather than previously-hidden defects; a few findings didn't hold up against the actual code when checked; and several findings were reasonable **larger proposals** (a full test hierarchy, positional-argument refactoring, a stock-flow ledger, a fourth baseline scenario, a rollout/transition model) that are legitimate future work but not something a documentation-focused session should undertake unilaterally — each is logged below and in Good First Issues / Model Architecture Feedback for Duke's consideration.

### Bug found and fixed: the PTF adoption-cap panel cited the wrong number

The audit's single most concrete, checkable finding: `index.html`'s own in-app "Cumulative Bug Fixes" entry for the v4.6 PTF adoption cap states that seed 42 / Full Integration / 18% slider converges to **23.8%** under the shipped agent-granularity cap. This directly contradicts this document's own v4.6 Release Notes, which have always said **19.0%** (see the "the same seed/config lands at 19.0% instead of 53.4% when enabled" bullet, above). The audit correctly flagged the inconsistency but couldn't say which side was right, since it was working from the documentation alone rather than the code.

**Settled by direct computation, not by re-reading prose harder.** A Node.js harness was built this session — using the same functions this project's existing `harness.js` already implements (`makeLatentPopulation`, `instantiateAgent`, `runYear`, all copied verbatim), first validated by confirming it reproduces the documented seed-42 regression figures exactly (median wealth $559,223 to the dollar, median BLEI 1,965d, Gini 0.534, wealth poverty 16.6%) before being trusted for anything new — and then used to reproduce the exact configuration in question: seed 42, Full Integration, `ptfCap:true`.

**Result: 19.0% is correct. CONTRIBUTING.md was right; `index.html`'s own panel was wrong.** Tracing the mechanism explains why precisely: `ptfLiveCount` is recomputed at the top of every `runYear()` call from the agent set's *actual current* `inPTF` membership, and `ptfCapAllows()` gates every subsequent admission attempt against it. For seed 42, the year-0 Bernoulli draw in `instantiateAgent()` (before any dynamics run) already lands at 95/500 = 19.0% — *above* the 18% cap threshold (90/500) — so `ptfCapAllows()` returns false from the very first check of year 0 onward, and stays false for the entire 20-year run, since nothing in this codebase removes an agent from PTF once admitted. The final share therefore equals the year-0 share exactly: 19.0%, not 53.4% (uncapped) and not 18.0% (the nominal cap value). This is precisely the "it doesn't retroactively correct sampling variance already present in that year-0 draw itself" caveat the in-app toggle's own tooltip already states — playing out concretely at this specific seed.

23.8% was never a property of the shipped implementation. Cross-referencing the replication page's own account of this feature (which has separately and correctly described 23.8% as the output of "a first implementation attempt that still overshot" — an earlier, once-per-year-checked prototype that was tested and discarded before the agent-granularity version shipped) makes the likely history clear: the discarded prototype's number appears to have been carried into `index.html`'s own in-app documentation at v4.6 and never caught until this session, even though this document's Release Notes had the correct figure the whole time.

**A 10-seed sweep (seeds 1–10) confirms the general mechanism, not just this one seed.** Six of the ten seeds tested have a year-0 draw starting *below* 18%; every one of those grows under the cap and lands at **exactly** 18.0% (500×0.18=90 is a whole number for this specific slider/population combination, so there's no fractional-agent overshoot to observe here — a subtlety worth naming, since the general mechanism *can* overshoot by one agent when the cap threshold isn't a whole number, confirmed separately via constructed test cases with non-round agent-count/share combinations). The other four seeds, whose year-0 draw already sits at or above 18%, hold at their year-0 level for the whole run, exactly as seed 42 does.

**Fixed:** `index.html`'s Cumulative Bug Fixes entry now states 19.0%, explains the year-0-freeze mechanism precisely, and documents the correction plainly rather than silently swapping the number — matching this project's own established practice for handling a caught error (compare the v4.4 `FBS_LAMBDA` "dimensionally-necessary" correction). This document's own v4.6 entry needed no change; it was already correct.

### Stale technical documentation: three panels describing superseded mechanics as current

The audit's second concrete finding: `index.html`'s own ODD Protocol panel and Empirical Calibration panel each contain prose that was accurate when written but was never revisited after later mechanics-changing releases superseded it — a different failure mode from the PTF-cap bug (that was a wrong *number*; this is accurate-when-written prose that quietly went stale), but worth catching for the same reason: readers trust these panels to describe the model as it actually runs today, not as it ran two or three releases ago.

- **ODD panel, "Overview: State Variables" card:** stated `automationRisk ∈ [0.2,1.0]` — the exact bounds of the retired pre-v4.3 uniform draw — while the "Details: Initialization" card two rows below it, in the *same panel*, has correctly said "47%/53% bimodal mixture, Beta(6,1)/Beta(1,6)" since v4.3. Two adjacent cards in one panel contradicted each other; the audit caught this specific internal inconsistency precisely.
- **ODD panel, "Details: Submodels" card:** described the annual wealth update as `SIM_COST_SCALE`-driven and BLEI's wage term as `SIU_TO_USD`-converted — both accurate through v4.2, both superseded by v4.3's wealth-loop unit fix (`WAGE_TO_USD`/`LIVING_WAGE_ANNUAL`) and v4.4's `SIU_TO_USD` retirement respectively. The dedicated Cumulative Bug Fixes entries for both releases were correctly written and remain correct; this specific ODD card, describing the same mechanics in a different place, was simply never updated in step.
- **Empirical Calibration panel, "Daily vs. simulation cost scales" card:** framed entirely around "what v4.0 fixed and what it deliberately didn't," and still asserted the main wealth loop was "deliberately NOT changed" — a true statement at v4.0, false since v4.3. Rewritten to tell the fuller v4.0→v4.3→v4.4 story while preserving the original v4.0 reasoning (still the correct explanation for why v4.0 shipped a partial fix rather than a risky full one).
- **Top-of-script `UNIT SYSTEM` code comment:** same underlying problem — asserted "The MAIN wealth-accumulation step (runYear) is UNCHANGED from pre-v4.0" as a standing fact, three mechanics-changing releases after that stopped being true. Rewritten the same way.

None of this affected any computed output — these are description-only panels whose job is explaining the model, not running it. Each is now corrected in `index.html`, each carries a short inline note explaining what was wrong and why, following this project's established practice of documenting a correction rather than silently swapping text (see, for instance, the replication page's own "arithmetically wrong" recession-mode correction at v4.0, or the `FBS_LAMBDA` correction at v4.4/v4.6).

**Deliberately not chased further:** a handful of *dated, versioned* changelog entries elsewhere in `index.html`'s "Cumulative Bug Fixes" panel and top-of-script comment history also describe pre-v4.3 mechanics — for example, the v4.0-dated "Dimensional (unit) coherence" entry still says "The main wealth-accumulation loop was deliberately left unchanged." These are different in kind from the three items above: they're explicitly dated, versioned changelog entries (the same documentation pattern this entire panel uses throughout, going back to v3.1), meant to be read as "what was true when this shipped," not as timeless current-state descriptions. The three items actually fixed this session were *not* dated per-entry — the ODD panel and the Empirical-Calibration card are written as general, current descriptions of the model, which is exactly what made their staleness a real bug rather than an expected property of a changelog. Rewriting every historical dated entry that happens to describe old mechanics would be a much larger undertaking with real risk of introducing new errors into otherwise-accurate historical records, for no real reader benefit — the most recent (v4.12) entry in the same changelog already tells the current story first, which is how a newest-first changelog is meant to work.

### New feature: a dominance check on the Threshold Sensitivity charts

The audit's strongest *constructive* suggestion, and the one most in keeping with this project's own recent feature direction: "test for first-order stochastic dominance over the displayed range... a clear statement when curves cross... do not imply a universal welfare ordering when curves cross." The v4.10/v4.11 Threshold Sensitivity charts already let a reader *eyeball* whether one scenario's curve sits below another's across the full range shown — this makes that comparison exact and explicit rather than requiring visual inspection, extending the same reporting-only feature family (`povertyCDF`/`buildPrefixSum`/`povertyGapAvg`) with one more pure function.

**What shipped.** A new `checkDominance(labels, ysA, ysB)` function compares the currently-displayed "Your Settings" curve against Baseline and against CCO-Only, point by point across the full threshold grid, and classifies the relationship as one of: `a_dominates` (Your Settings sits at-or-below the other curve at *every* threshold — less-or-equal poverty/shortfall everywhere), `b_dominates` (the reverse), `identical`, or `cross` (the sign of the difference flips at least once — reported with the approximate threshold where it happens). Both chart callouts now end with a "Dominance check" line built from this. `dominanceClause()` formats the result into a short reader-facing sentence, phrased identically whether the answer is "yes, dominates everywhere" or "no, the curves cross" — the feature is built to report either outcome honestly, not to manufacture a favorable-sounding finding.

**Validation, in two stages, matching this project's established discipline.** First, `checkDominance()` was checked against 9 constructed test cases before it ever touched real simulation data: A strictly below B (dominates), A strictly above B (dominated), identical curves, a single genuine crossing (with the crossing index correctly identified), weak dominance with tied values at some points, a tiny-but-real above-epsilon difference correctly *not* treated as a tie, and sub-epsilon floating-point noise correctly *treated* as a tie (relevant in principle, though in practice every value reaching this function has already been rounded to display precision — 1 decimal for %, whole numbers for $/days — by the existing `curve()` helper, so real floating-point noise below that precision never actually reaches it). All 9 passed.

Second, a full end-to-end Node.js integration test evaluated the *actual edited* `index.html` script (not a hand-copied approximation) in a stubbed DOM-free sandbox: it reproduced the documented seed-42/Full Integration/20yr regression figures exactly (median wealth $559,223, median BLEI 1,965d, Gini 0.534, wealth poverty 16.6%) — confirming this release introduced zero mechanics drift — and then drove the real `renderThresholdSensitivity()`/`drawThresholdCharts()` render path, in both the headcount and gap views, confirming the new "Dominance check" text is built correctly and the function doesn't throw against realistic curve shapes (including the WEALTH_FLOOR-pinned region, where both Baseline and Main sit at exactly 0% below −$10,000, correctly classified as `identical` rather than a spurious cross).

**What the feature actually shows, and an honest note about that.** At the seed-42 Full Integration reference configuration, "Your Settings" dominates both Baseline and CCO-Only, on both charts, in both views — a genuine, computed finding, not an assumption wired into the feature. A Stress Test preset re-run (40% participation, $900 BU, 18% tax, seed 42, shocks held off in this specific re-run since the harness's simplified recession handling doesn't reproduce the in-app preset's full shock behavior — flagged plainly rather than presented as a validated Stress-Test regression figure) also showed dominance rather than a crossing — worth naming honestly rather than quietly omitting, since it means this specific model's mechanics don't currently produce many genuine crossing cases between "more active systems" and "fewer active systems" configurations (PTF/PTH/SZH/CIP each only ever help or do nothing in this engine's cost/benefit structure, so a superset-of-mechanisms comparison tends toward dominance by construction). The crossing-detection code path is real and tested — it was exercised against constructed adversarial curves during unit testing — it's just that this project's own mechanics don't happen to produce many real-data examples of it under the configurations tried this session. A future session with more adversarial parameter combinations (e.g., CCO off but PTF/PTH on, which the tool's sliders do allow) might find one; not chased further here.

**Purely a reporting-transform addition**, same guarantee as v4.10/v4.11: computes no new agent state, draws no RNG, reads only the already-computed sorted/prefix-summed arrays the rest of this feature already builds. Cannot affect the Main run, Baseline, or CCO-Only trajectories.

### Smaller fixes

- **Poverty-gap toggle tooltip mislabeled.** The `#thresh-view-gap` button's own hover tooltip called the v4.11 metric "the poverty gap *ratio*" — but what it actually shows is the *absolute* dollar/day shortfall, not the textbook normalized ratio, which is the entire documented reason v4.11 reports it that way (normalizing by a negative or zero threshold breaks down, and the wealth chart's range deliberately includes negative thresholds — see v4.11's own entry, above). The word "ratio" in that one tooltip was simply wrong. Corrected.
- **Validation-suite button name inconsistent with its own panel.** The sidebar's "✅ Run Validation Suite" button opens a panel titled "Internal Consistency & Behavioral Test Suite" — renamed at v4.2 specifically to avoid overstating what six internal checks establish (the panel's own caption already says "not external empirical validation... see Known Limitations"). The button text never got the same treatment. Renamed to "✅ Run Consistency & Behavioral Checks."
- **Traditional Welfare Baseline's tooltip overstated its realism.** The preset button's tooltip called this scenario "the real-world reference point," which could read as a claim it models actual U.S. transfer programs. It doesn't: the baseline sets every architecture off and applies a flat 3% CPI, with no SNAP, EITC, TANF, SSI/SSDI receipt, Medicaid, housing assistance, or unemployment insurance credited to any agent as income. (The Social Security-Anchored Cohorts table tags agents by wage *relative to* real benefit levels for comparison — it doesn't credit those benefits as baseline income.) Softened to describe it as a no-intervention counterfactual, with a new matching Known Limitations entry in `index.html`.

### What the audit flagged that was already true, or already deliberately designed

Worth stating plainly, since distinguishing a genuine finding from a restated or dismissed one is the entire point of a verification pass, not a formality:

- **The Comfortable/Flourishing tier-label split**, flagged by the audit as risking an inflated cross-scenario comparison (two different words for the identical 730-day threshold), is not a previously-hidden defect — it's a deliberate, extensively pre-documented framework narrative choice with its own dedicated "v3.4 naming note" on the replication page and explicit disclosure in this tool's own system-comparison table caption, present since v3.1/v3.4. This is a framework-design decision belonging to Duke, not a code-audit finding, and was not changed unilaterally.
- **The BU-conversion "reciprocal debit" concern** doesn't hold against the actual `runYear()` code: `a.buBalance -= spend` and `convGain = spend*rate*(1-progTax)*cipB*incomeShock` both derive from the *same* `spend` amount, in the same statement block — the BU balance genuinely is decremented by exactly what gets converted, not retained alongside it. Checked by direct code trace; not something a fresh simulation run was needed to settle.
- **The internal test suite's framing, the LHS export's fixed-seed design, and the CCO "conversion ledger" suggestion** each restate design choices or limitations already documented at length — the suite's ODD Level 1-3 framing since v4.2, the LHS seed convention explicitly matching OAT's own convention since v4.6 (documented in that release's own notes), and the "tracked but not production-constrained" caveat in Known Limitations since v4.0. None of these were treated as newly-found.

### What did NOT get fixed, and why

By scope, this was a documentation-and-verification pass plus one small, well-precedented feature addition — not a mechanics-audit release and not a framework-redesign session. Not attempted: a full executable test hierarchy (pure-function/accounting-invariant/scenario-pairing/regression/documentation-snapshot tests) — a genuinely good idea, and a substantial engineering investment in its own right, possibly in tension with this project's explicit single-buildless-file constraint depending how it's built; replacing positional function arguments with context objects across `agentBLEI()`/`bleiMetrics()`/`runYear()` — a large refactor touching the mechanics engine for a clarity gain, carrying real risk for a documentation-focused session to attempt unilaterally; a full per-agent stock-flow ledger with explicit stock/flow/counterparty accounting — a genuine elaboration of the existing "tracked but not production-constrained" Known Limitation, not a defect fix; a fourth, empirically-calibrated "current U.S. policy" comparison scenario alongside the existing no-intervention baseline; a rollout/transition-path model distinguishing steady-state institutional availability from realistic adoption ramps; additional heterogeneity dimensions (age, disability, household size, region); and person-years-in-poverty / time-to-tier-attainment / recovery-rate metrics as a richer complement to the final-year-only Threshold Sensitivity charts. Each is logged in Good First Issues or Model Architecture Feedback, below, for a future session or Duke's own judgment — none is a quick fix, and several are genuine framework-design decisions this document has consistently deferred to Duke rather than deciding unilaterally.

### Regression: seed 42 / Full Integration / 20yr, v4.11 → v4.12

| Metric | v4.11 | v4.12 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |

Expected and confirmed three ways this session: `harness.js` (untouched) reproduces this table exactly; a fresh standalone harness built for the PTF-cap investigation independently reproduces it; and a full end-to-end integration test against the *actual edited* `index.html` script reproduces it before the new dominance-check code is ever exercised against the same data. None of v4.12's changes touch `makeAgent()`/`instantiateAgent()`, `runYear()`, or any metric function — the PTF-cap and documentation-staleness fixes are text-only corrections to panels that describe the model, the dominance check is a new pure function reading already-computed arrays, and the smaller fixes are a tooltip string, a button label, and a preset tooltip.

---

## v4.11 Release Notes

<!-- v4.13 note: this heading was MISSING. Every other release in this file has a
     `## vX.Y Release Notes` heading; v4.11's was dropped somewhere between drafting and
     shipping, so its whole section — including four `###` subsections — rendered as if it
     belonged to v4.12's, and it was absent from any generated table of contents. Caught by
     an independent audit pass at v4.13 and restored rather than silently patched, matching
     the practice the v4.11 signature-line note at the foot of this file already set. -->

v4.11 is a small, single-feature follow-on to v4.10, prompted by relaying that release's own design to an external AI system (Grok) for a methodology critique, plus a second, independent data-gathering pass from the same system on two long-open items (the `LIVING_WAGE_ANNUAL` population-weighting task and further verification of the occupation-risk Kaggle dataset lead). Per this project's now well-established rule, neither was taken on the external system's word — every checkable claim in both was verified against primary sources before anything was acted on. **Zero simulation-mechanics changes**: nothing here touches `makeAgent()`/`instantiateAgent()`, `runYear()`, or any metric function, so the v4.10 seed-42/Full Integration/20yr regression figures (Median BLEI 1,965d, Median wealth $559,223, Gini 0.534, Wealth poverty 16.6%) still apply unchanged.

### What shipped: a poverty-gap ("depth") view for the v4.10 Threshold Sensitivity charts

Grok's methodology review reconfirmed the v4.10 feature's use of Atkinson (1987) as correct and the World Bank multi-line-reporting comparison as apt, then recommended a specific, concrete extension: the existing headcount-ratio curves (what fraction of the population sits below a given threshold — FGT-0 in the poverty-measurement literature) can't distinguish a scenario where the poor are barely below a line from one where they're far below it. Two scenarios can post identical headcount curves across the whole range while differing substantially in how deep the remaining poverty runs. The standard companion measure for exactly this is the poverty gap (FGT-1: Foster, J., Greer, J., & Thorbecke, E. (1984). "A Class of Decomposable Poverty Measures." *Econometrica*, 52(3), 761-766) — the mean shortfall below the threshold, averaged across the *whole* population (agents at or above the line count as zero).

A new **"Avg. shortfall" / "% below line"** toggle now switches both existing charts (wealth and BLEI) between the v4.10 headcount view and this new gap view, without re-running the simulation or touching RNG — same reporting-only guarantee as v4.10 itself. One deliberate departure from the textbook FGT-1 definition: it's normally expressed as a *ratio* (gap normalized by the threshold value itself, so it's dimensionless and comparable across different thresholds). That normalization divides by the threshold, which breaks down at threshold ≤ 0 — and the wealth chart's own threshold range deliberately extends to −$20,000 specifically so Baseline's `WEALTH_FLOOR`-pinned distribution renders as a real step rather than an off-chart flat line (a v4.10 design choice, unaffected here). Reporting the *absolute* per-capita shortfall (in the same dollars/days as the chart's own axis) sidesteps that division problem entirely, and arguably reads more naturally for a policy tool anyway — "the average dollar short, per person, if the line were drawn here" is a direct "cost to close the gap" framing.

### Validation

`buildPrefixSum()`/`povertyGapAvg()` were built and checked before ever touching `index.html`, exactly mirroring the discipline `povertyCDF()` got in v4.10: a naive brute-force reference implementation (literal `sum(max(0,threshold-x_i))/N`, no indexing tricks) checked against the production prefix-sum-plus-binary-search implementation across 22,210 random trials — random continuous distributions of varying size, duplicate-heavy arrays specifically constructed to mimic `WEALTH_FLOOR` pinning (since that's Baseline's actual shape and the case this function most needs to get right), BLEI-shaped right-skewed arrays, and degenerate edge cases (empty array, single element, all-identical values, thresholds far outside the array's range). Zero mismatches beyond ordinary floating-point rounding (max observed error ~1.3×10⁻⁶).

After integrating into `index.html`, a full end-to-end Node.js test evaluated the *actual edited script* (not a hand-copied approximation) in a stubbed DOM-free sandbox, drove the real `makeLatentPopulation()`/`instantiateAgent()`/`runYear()` functions against the documented seed-42/Full Integration/20yr configuration for both the Full Integration and Traditional Welfare Baseline scenarios, and checked: (1) the existing `povertyCDF()` figures were undisturbed by editing nearby code — confirmed exact match, 16.6%/13.6%; (2) the new function is non-negative and monotonically non-decreasing in the threshold across a dense sweep, for all four tested distributions; (3) an independent cross-check against a discretized numerical integral of the already-validated `povertyCDF()` curve, using a genuine mathematical identity (mean absolute gap at threshold *z* equals the integral of the CDF from −∞ to *z*) computed at a much finer resolution than the production chart's own grid, specifically so it's an independent check rather than a restatement of the same discretization.

**One honest complication, fully chased down rather than smoothed over.** That third check disagreed at exactly one point: threshold = −$9,999, one dollar above `WEALTH_FLOOR`, where 68.6% of a sampled Baseline population sits at exactly −$10,000. Rather than treat this as inconclusive, it was run to ground: an independent *direct* per-agent sum (`agents.reduce((s,a)=>s+Math.max(0,-9999-a.wealth),0)/agents.length`) matched `povertyGapAvg()`'s output *exactly* (0.6860 both ways) — confirming the production function is correct — while refining the auxiliary integral check's own step count from 20,000 to 200,000 to 2,000,000 shrank its error from 0.171 to 0.017 to 0.0016, the textbook signature of a coarse Riemann-sum discretization artifact converging toward the true value near a sharp jump discontinuity. The discrepancy was in the *supplementary cross-check's* own resolution, not in the shipped code — but it's reported here in full rather than quietly re-running the test with finer settings until it stopped complaining, since getting this distinction right (and being able to show the work) is the actual point of validating a numerical function this way.

### The external review, checked claim-by-claim

Grok's answer to the methodology question (Atkinson citation, FGT-0 vs. FGT-1, cherry-picking risk) held up well under scrutiny — its World Bank figures were checked directly and are current: the international poverty line moved from $2.15 to $3.00, the lower-middle-income line from $3.65 to $4.20, and the upper-middle-income line from $6.85 to $8.30, all in the June 2025 revision to 2021 PPP terms (Grok used the *current* figures rather than the $2.15/$3.65/$6.85 set that predates this project's own knowledge-cutoff era) — and the Foster/Greer/Thorbecke citation (*Econometrica* 52(3), 761-766, 1984) was independently confirmed. Its cherry-picking mitigations (always show the full range by default, overlay scenarios on shared axes, avoid auto-zooming to a favorable region) describe what this feature already does, not a gap to close.

Grok's *second* answer, responding to the data-gathering questions carried over from the v4.10 session, get more mixed marks — one contribution checked out well, one couldn't be confirmed or denied, and it surfaced a genuinely useful new lead this project hadn't found on its own. Detail below.

### `LIVING_WAGE_ANNUAL` population-weighting: the state-level data checks out; the weighted total is documented, not adopted

Grok reported all 51 jurisdictions' current MIT "1 Adult, 0 Children" figures, an unweighted mean of $23.7355/hr, and — using U.S. Census Bureau Vintage 2025 population estimates (total 341,784,857, released ~January 27, 2026) — a population-weighted mean of **$24.6160/hr** ($51,201/yr at 2,080 hrs/yr).

Verified directly this session, the same "don't trust the first thing that loads" way this project checks everything external: five of Grok's 51 state figures were spot-checked against live fetches of `livingwage.mit.edu` (California, DC, Mississippi, West Virginia via direct fetch; Hawaii via an independent March 2026 news article) — all five matched exactly, against the same build (dated 2026-02-15, git commit `55b4996`) this project has cited since v4.9. The total-population figure (341,784,857) independently matches Census-citing secondary sources for the same Vintage 2025 release. A partial reconstruction using the four largest-population states (CA/TX/FL/NY, ≈33% of the U.S. population) gives a population-weighted average for just those four of ≈$26.64/hr — comfortably above both the unweighted 51-jurisdiction mean and Grok's claimed full-51-state weighted figure, which is exactly the direction and rough magnitude you'd expect once the other 47 (mostly smaller, more moderate-cost) states pull the full average back down from that top-heavy subset. This is a *plausibility and spot-check* verification, not a full independent re-derivation — MIT's site asks not to be scraped, so a systematic 51-page pull wasn't attempted, and the exact $24.6160 figure was not independently reproduced to the dollar.

Two things worth flagging on their own. First, the unweighted mean Grok reports ($23.7355/hr → $49,370/yr at 2,080 hrs/yr) matches the currently-shipped `CFG.LIVING_WAGE_ANNUAL` almost exactly — a reassuring finding in its own right: the existing figure remains accurate against *current* MIT data via the same unweighted methodology it was originally computed with, not just an artifact of when it happened to be sourced. Second, the population-weighted figure would move the constant **up**, not down — the opposite direction from Meta's stale-data proposal in v4.9, and for an entirely different, better-sourced reason.

**Not adopted.** Consistent with this project's standing rule that `LIVING_WAGE_ANNUAL` needs its own dedicated mechanics-audit-plus-large-N-restudy before any change (it's genuinely baked into `runYear()`'s wealth-accumulation trajectory, unlike `POVERTY_LINE`), and consistent with only partially — not fully — independently verifying the weighted arithmetic itself, this session documents the new figure as well-sourced reference data for a future dedicated release to weigh, exactly the same "sweep, don't decide" treatment the `WEALTH_FLOOR` sensitivity sweep got in v4.8. See the Calibration Validation table and Good First Issues, below, for the precise, narrowed scope of what a future session would still need to do.

### Occupation-risk dataset: the Kaggle license claim couldn't be confirmed *or* refuted — and a better-documented alternative source turned up

Grok's second finding was that the Kaggle dataset (`andrewmvd/occupation-salary-and-likelihood-of-automation`) — the same one a v4.8 session found "stronger, still-incomplete corroboration" for, including a third-party card claiming it was MIT licensed — actually carries a Kaggle-native license field of "Other (specified in description)," with the description itself reportedly stating "License was not specified at the source." This would directly *contradict* the earlier "third-party card says MIT" finding.

This session could not independently confirm or deny it: Kaggle's dataset page remains JS-rendered (a direct fetch returns only Open Graph/Twitter meta tags, no license field, the same wall every prior session studying this dataset has hit), and a search for third-party citations of this specific dataset's license came up empty. **The honest status is: unconfirmed either way.** Given the specific, contradicting nature of the claim, the earlier "third-party card said MIT" finding should now be treated as suspect rather than as corroboration — anyone picking this up next needs direct Kaggle account/API access to settle it, not another round of web search.

**A new, more promising lead, found independently this session while chasing the license question.** `job-automation-probability.csv` in the `plotly/datasets` GitHub repository has **703 lines — 702 data rows after the header, an exact match to Frey & Osborne's own occupation count** — with richer columns than reported for the Kaggle dataset (SOC code, probability, median annual wage, May-2016 BLS employment, education level). The repository carries a genuine, first-party `LICENSE` file stating MIT (Plotly Technologies Inc., 2019–2024) — a materially cleaner starting point than Kaggle's ambiguous per-dataset licensing. One complication surfaced and not swept aside: the repo has its own open GitHub issue (#23) questioning whether that MIT grant cleanly covers third-party-*sourced* data files the way it covers Plotly's own code — a real nuance, not a solved problem, but a meaningfully better-documented starting point than the Kaggle listing either way. This session did not attempt a row-by-row fidelity check of this CSV against the Frey & Osborne appendix (the same next step this project has flagged for the Kaggle dataset since v4.7) — a natural next step for whoever picks this up, and one that doesn't require a Kaggle account.

### What did NOT get fixed, and why

By scope, this was a single small feature addition plus its own verification and one data-gathering follow-up, not a mechanics-audit release. Not attempted: adopting the population-weighted `LIVING_WAGE_ANNUAL` figure into `CFG` (deliberately — see above); a row-by-row fidelity check of the new `plotly/datasets` CSV lead against the Frey & Osborne appendix; a normalized (ratio) variant of the poverty-gap view alongside the absolute one shipped here (would need separate axis ranges or a second toggle dimension — not scoped this pass); additional named external benchmark points on the threshold-sensitivity charts beyond the single federal poverty guideline added in v4.10; making `LIVING_WAGE_ANNUAL` itself explorable the way `POVERTY_LINE` already is (unchanged from v4.10 — still its own dedicated, mechanics-adjacent release); every other long-standing open item this session didn't touch (`WEALTH_INIT_MU`/SCF gap, `WEALTH_FLOOR`/`TARGET_*` recalibration, the unbounded long-horizon wealth-growth question) — unchanged from v4.10.

### Regression: seed 42 / Full Integration / 20yr, v4.10 → v4.11

| Metric | v4.10 | v4.11 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |

Expected and confirmed: v4.11's only changes to `index.html` are two new pure functions (`buildPrefixSum`, `povertyGapAvg`) never called by `runYear()`, `calcMetrics()`, or any other mechanics function; a restructuring of the existing `renderThresholdSensitivity()` into a caching entry point plus a `drawThresholdCharts()` renderer and a `setThreshView()` toggle handler (same inputs, same outputs for the existing headcount view — confirmed via the integration test's Check 1, an exact-match re-confirmation of the v4.10 16.6%/13.6% figures); one new HTML toggle control reusing existing CSS classes (no new CSS); and documentation/version-string updates. No `CFG` value used by the simulation engine changed, and no RNG call sequence changed.

---

## v4.10 Release Notes

v4.10 adds one new reporting feature — Poverty & Wealth Threshold Sensitivity charts — prompted directly by Duke, plus the verification work and one small documentation-gap fix that came out of building it. **Zero simulation-mechanics changes**: nothing here touches `makeAgent()`/`instantiateAgent()`, `runYear()`, or any metric function, so the v4.9 seed-42/Full Integration/20yr regression figures (Median BLEI 1,965d, Median wealth $559,223, Gini 0.534, Wealth poverty 16.6%) still apply unchanged — confirmed by re-running `harness.js` (untouched this session) and, for the new code specifically, by a full end-to-end Node.js integration test described below.

### The problem this responds to

This project has now had the same argument twice: v4.3 committed `LIVING_WAGE_ANNUAL` to a single defended dollar figure, and v4.9's Meta AI audit tried to overturn it with a different single dollar figure that turned out to rest on stale data. Both rounds spent real effort defending or attacking one specific number. Duke's proposal: instead of resting a poverty-reduction claim on getting one contested figure exactly right, show the *range* — report outcomes across every threshold a reasonable person might pick, and let the reader see whether the conclusion holds up across that whole range, not just at one point.

This is not a new idea invented here — it's the standard "poverty dominance" approach in the poverty-measurement literature: comparing headcount ratios across a full range of possible poverty lines rather than committing to a single one (Atkinson, A.B. (1987). On the measurement of poverty. *Econometrica*, 55(4), 749-764). The World Bank does exactly this in practice, routinely reporting global poverty at several lines simultaneously ($2.15/$3.65/$6.85 per day as of the 2024 revision) for the same reason: no single poverty line commands universal agreement, so showing the whole curve is more defensible than picking one point and arguing for it.

### What shipped: two new charts, "Wealth poverty rate by threshold" and "BLEI poverty rate by threshold"

Both plot a cumulative distribution — at every threshold across a plausible range ($−20,000 to $100,000 for wealth; 0 to 800 days for BLEI), what fraction of the final-year population falls below it — with Baseline, CCO-Only, and Your Settings overlaid on the same axes. If one scenario's curve sits below another's across the *whole* range shown, it reduces poverty regardless of exactly where the "true" line is drawn — a materially more robust claim than any single headline percentage, and one that doesn't hinge on getting `CFG.POVERTY_LINE`, `CFG.LIVING_WAGE_ANNUAL`, or the BLEI tier cutoffs exactly right.

Underneath the charts, a callout reads off two named reference points directly from the same curves: this simulation's own definitions (`CFG.POVERTY_LINE` = $25,000; the BLEI poverty line = 30 days and the Threshold-tier line = 120 days), plus — for wealth only — one external comparison point, described below.

**Why a static curve rather than an interactive slider.** A live slider that recomputed on drag would need either (a) re-running the simulation per tick, which isn't cheap and isn't necessary since wealth/BLEI values for the current run already exist, or (b) recomputing against already-known final-year values, which is what a full CDF curve already shows in one static image — every threshold at once, not one at a time. The curve also means a reader skimming or screenshotting the page for a report sees the full picture without needing to interact with anything. A draggable marker reading the exact value off the existing curve remains a reasonable future enhancement (Chart.js's built-in hover tooltips already give an approximation of this for free, reading off any point on the curve), but the static dual-axis-free curve is the core deliverable and needed no new interaction machinery.

**Why `POVERTY_LINE` and not `LIVING_WAGE_ANNUAL`, at least not yet.** These are two structurally different constants, confirmed by grep before writing a line of code: `POVERTY_LINE` has exactly one call site in the entire engine, inside `calcMetrics()`'s poverty computation — it's a pure post-hoc classification threshold applied to already-computed wealth values, never touching RNG or any dynamics. `LIVING_WAGE_ANNUAL` is genuinely baked into `runYear()`'s annual wealth update (`mainLoopCostUSD=CFG.LIVING_WAGE_ANNUAL*Math.pow(1+inflRate,yr)`) — it's a flow/cost anchor that mechanically shapes the wealth trajectory itself, not a reporting threshold. Exploring `POVERTY_LINE` across a range costs nothing extra: the wealth values are already computed, only the classification changes. Exploring `LIVING_WAGE_ANNUAL` across a range would mean re-running the simulation once per candidate value — cheap enough for an offline sweep (exactly what the v4.8 `WEALTH_FLOOR` sweep already does), but a materially different, larger feature than a same-run reporting transform, and one that touches simulation mechanics in a way this reporting-only release deliberately doesn't. Making `LIVING_WAGE_ANNUAL` (and, similarly, `BASE_DAILY_COST`, which anchors BLEI's own daily-cost denominator) explorable the same way is scoped as the clear next step — see Good First Issues, below.

One consequence worth naming directly: the BLEI tier cutoffs (`BLEI_CRISIS_MAX`, `BLEI_PRECARIOUS_MAX`, etc.) are *not* in the same free category as `POVERTY_LINE`, even though they look similar on the surface (both are "where do we draw the poverty line" numbers). `BLEI_PRECARIOUS_MAX` (30 days) is read twice inside `runYear()` itself — once gating the wage-growth stability bonus, once gating the PTF economic-distress adoption bonus — so it's genuinely mechanics-relevant, not just a reporting convention. The new BLEI threshold-sensitivity chart doesn't touch this: it reads the already-computed *continuous* BLEI score (`agentBLEI()`'s raw day-count, before `getTier()` buckets it) at many different threshold points for display, which is exactly as safe as `POVERTY_LINE` exploration — it's only the CFG *constants themselves* that would be unsafe to slide, not the act of asking "what if the line were somewhere else" of an already-computed continuous value.

### The one external reference point added: 2026 HHS federal poverty guideline

The wealth chart's callout includes one labeled external comparison, `CFG.FED_POVERTY_LINE_1P = 15960` (2026, one-person household, 48 contiguous states + DC), clearly marked "external reference, not a simulation parameter" — same category as `CFG.NORDIC_GINI` elsewhere in this file. Verified this session the way this project now verifies everything external: a first fetch attempt against `aspe.hhs.gov/poverty-guidelines` returned a stale cached snapshot from 2017 — caught immediately (the 1-person figure it showed, $15,060, was the 2017 figure, not remotely current) rather than used. Cross-checked instead against an independently-dated primary-source PDF (a Lifeline Safe Connections Act eligibility table, explicitly dated "Source: ... U.S. Department of Health & Human Services, January 15, 2026," showing 200% of the 1-person guideline as $31,920 — i.e. the underlying guideline is exactly $15,960) plus three further independent third-party citations (a Michigan municipal utility program, a PNM utility program, a poverty-guideline lookup tool), all converging on the identical figure. This is a much easier verification than the `LIVING_WAGE_ANNUAL` episodes — a single government-published number with no methodology dispute attached, unlike a state-by-state living-wage calculation — but the same "don't trust the first thing that loads" discipline applied anyway, and it's a good thing it did.

Deliberately scoped to *one* reference point, not a menu: additional named benchmarks (a different year, a different country, a different definition like 200% of the guideline or a relative-poverty measure) are real, valuable extensions Duke specifically raised ("past/future wealth lines, hypothetical scenarios, or other even nations") but each one needs its own sourcing pass with the same rigor applied here — not something to add casually in the same session that already added one. See Good First Issues, below, for how this generalizes cleanly: any dollar or day figure, from any era or country, can be read directly off the existing curve without further engineering — the curve doesn't need to know what a number *means*, only what fraction of the population sits below it.

### Validation

The core `povertyCDF()` function (binary search over an already-sorted array — the standard "count elements below X" idiom) was unit-tested against a naive linear-scan reference across 12,500 random trials before it went anywhere near the actual file: zero mismatches, including the realistic duplicate-heavy case of hundreds of agents pinned at exactly `WEALTH_FLOOR` (Baseline's actual shape). After integrating into `index.html`, the standard checklist passed (HTML div-balance 525/525, CSS brace-balance 210/210, `node --check` on the extracted script, JSON-LD re-parse) — and, going further than a syntax check, a full end-to-end Node.js integration test evaluated the *actual edited script* in a stubbed DOM-free sandbox, drove the real `makeLatentPopulation()`/`instantiateAgent()`/`runYear()` functions against the documented seed-42/Full Integration/20yr configuration, and cross-checked the new `povertyCDF()` function's output against `calcMetrics()`'s and `bleiMetrics()`'s own existing, already-trusted figures at the model's default thresholds. Exact match on both: 16.6% wealth poverty at `CFG.POVERTY_LINE`, 13.6% BLEI poverty at the 30-day cutoff — the same documented headline figures this file has carried since v4.5. This is a stronger validation pass than most prior UI-only releases received, precisely because the underlying computation could be tested against a known-correct reference (the engine's own existing metrics), even though — like every CSS/UI change since v4.8 — the actual Chart.js rendering and DOM behavior in a live browser is **not verified**; flag for Duke to check visually.

### A small documentation gap, found and fixed while adding the v4.10 entry

`index.html`'s own Assumptions panel has a "🔧 Cumulative Bug Fixes" section with dedicated entries for most releases since v4.0. Its header had read "(v3.1 → v4.6)" through v4.7, v4.8, and v4.9 — not because those releases didn't happen (they're fully documented in this file's own Release Notes and in `index.html`'s top-of-script changelog), but because none of the three added a *new mechanism* warranting a dedicated entry in that specific panel (v4.7 was dependency/documentation hygiene, v4.8's UI fixes were CSS-only and its `WEALTH_FLOOR` sweep got folded as a footnote onto the existing v4.3 entry rather than its own, v4.9 was a CSS fix plus audit verification). Not the same category of bug as the replication page's own v4.9-fixed toggle label (which implied stale *coverage*, actively misleading a reader about what the panel covered) — this was just an unexplained number sitting three releases behind reality. Bumped to "(v3.1 → v4.10)" and added one sentence explaining why v4.7-v4.9 don't have their own entries, rather than silently re-numbering it and leaving the same kind of unexplained gap for someone to catch later.

### What did NOT get fixed, and why

By scope, this was a single new reporting feature plus its own verification, not a mechanics-audit release. Not attempted: making `LIVING_WAGE_ANNUAL` (or `BASE_DAILY_COST`) explorable the same way — deliberately, since that's mechanics-adjacent and belongs in its own dedicated, fully-audited release, not bundled into a reporting-only pass; additional named external benchmark points beyond the single federal poverty guideline added here; an interactive slider/marker on top of the static curves (a real future enhancement, not attempted this pass since the static curve already delivers the core value); the long-standing open items this session didn't touch at all (`WEALTH_INIT_MU`/SCF gap, `WEALTH_FLOOR`/`TARGET_*` recalibration, occupation-stratified `automationRisk`, the `LIVING_WAGE_ANNUAL` 51-state population-weighted recomputation, unbounded long-horizon wealth growth) — unchanged from v4.9, see Model Architecture Feedback and Good First Issues, below, both updated this session with where the new feature does and doesn't change their urgency.

### Regression: seed 42 / Full Integration / 20yr, v4.9 → v4.10

| Metric | v4.9 | v4.10 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |

Expected and confirmed: v4.10's only changes to `index.html` are two new pure functions (`povertyCDF`, plus the `sortedWealthArr`/`sortedBLEIArr` wrappers) that are never called by `runYear()`, `calcMetrics()`, or any other mechanics function, one new render function, one new HTML section, one new CFG constant that's never read by any mechanics function, and documentation/version-string updates — no `CFG` value used by the simulation engine changed, and no RNG call sequence changed.

---

## v4.9 Release Notes

v4.9 is a UI-fix-plus-external-review-verification pass — one concrete bug found by Duke using the deployed page, and a full claim-by-claim check of a Meta AI audit and two accompanying contributions (a harness rewrite and a proposed calibration change), following this project's standing rule that an external AI's claims get verified against the actual source and outside sources before anything is acted on, the same discipline already applied to two rounds of ChatGPT review in v4.7. **Zero simulation-mechanics changes** — nothing here touches `makeAgent()`/`instantiateAgent()`, `runYear()`, or any metric function, so the v4.8 seed-42/Full Integration/20yr regression figures (Median BLEI 1,965d, Median wealth $559,223, Gini 0.534, Wealth poverty 16.6%) still apply unchanged, confirmed by re-running the harness, not just by inspection.

### UI fix: Social Security-Anchored Cohorts table clipped at 100% browser zoom

Duke supplied two screenshots of the same section at 80% and 100% browser zoom — the table rendered fully at 80% but had its rightmost column ("Top-tier rate") cut off entirely at 100%, with no way to scroll to it — and suggested the fix should look like the horizontal-scroll behavior the System comparison table already has.

**Root cause, traced rather than guessed at:** the System comparison table lives inside `.ctable`, which already carries its own `overflow-x:auto` — when that table needs more width than its box has, it gets a local scrollbar. The Social Security-Anchored Cohorts table (`ss-cohorts-inner`, v4.5) is a plain `<table>` dropped into a `.ccard`, which has no such rule. Table headers use `white-space:nowrap` (so short labels like "MEDIAN BLEI" stay on one line), and with six columns that add up to more width than a typical 100%-zoom viewport has left after the 290px sidebar, the table needs more room than its box provides. With nowhere local for that overflow to go, it runs into `.main`'s own `overflow-x:hidden` — a defensive rule added so no single wide element (a resizing chart canvas, say) can blow out the whole page's width — which clips the excess instead of scrolling it. At 80% zoom there's simply more CSS-pixel width available, so the same table fits without ever hitting that ceiling. This is the same underlying category of bug as v4.8's grid-track `minmax(0,1fr)` fix (content that needs more room than its container allows), just surfacing through a table instead of a grid this time.

**Fix:** a new `.tbl-scroll{overflow-x:auto}` utility class, applied to `ss-cohorts-inner`'s wrapper div — the exact same technique `.ctable` already uses, scoped to just this element rather than duplicating `.ctable`'s full background/border/padding treatment inside a `.ccard` that already provides those. Written as a reusable class (not an ID-specific rule) in case a future table gets added to a `.ccard` the same ad hoc way — grep for `.tbl-scroll` before assuming a new table needs its own bespoke fix. As with v4.8's CSS fixes, **this was not verified in an actual browser** (no browser-rendering tool in this session's sandbox either) — it's a standard, well-understood fix for a standard, well-understood CSS overflow pattern, but a visual check at a few zoom levels (the same 80%/100% comparison that surfaced the bug, plus 125% and mobile width) would be worth doing after this deploys.

**The v4.8 tooltip fix, by contrast, is now confirmed working in production** — Duke reported it explicitly. Combined with this session's table fix, that leaves the v4.8 chart-grid `minmax(0,1fr)` fix as the one remaining CSS fix from that release without direct visual confirmation either way.

### External review: a Meta AI audit and two contributions, verified against source

Duke shared a Meta AI chat (audit of v4.8, plus a harness rewrite and a living-wage recalibration proposal) with an explicit warning not to assume it was error-free. It wasn't, in one significant respect — but it also contained a genuinely correct, verified contribution. Both are detailed below because getting this distinction right is the entire point of a verification step, not a formality.

**What checked out: a modular (ES-module) rewrite of the v4.8 Node.js harness.** Meta split `harness.js` into `src/cfg.js`/`rng.js`/`agents.js`/`metrics.js`/`sim.js` plus a regression test, and separately supplied `harness_v2.js`, essentially the original monolithic file with an expanded scope-caveat header. Neither was taken on Meta's own word that it "passed" — both were actually run this session. `harness_v2.js` reproduces the documented seed-42 figures exactly, as expected since it's the same engine with a better comment block, not a rewrite. The modular version is a genuine rewrite (ES modules, `let`/`const`, arrow functions) and was worth real scrutiny — in particular, whether `agents.js` and `sim.js` importing a live `RNG` binding from `rng.js` and having it reassigned via a `setRNG()` setter would actually propagate correctly across module boundaries, rather than each importer capturing a stale reference. It does: run against the seed-42/Full Integration/20yr configuration, it reproduced Median BLEI 1,965d, Median wealth $559,223 exact, Gini 0.534, System Stability 88.5%, avg EDC 24.9% — every figure matching. A quick N=100 reproduction of the v4.8 `WEALTH_FLOOR` sweep through the same modular code also reproduced the documented direction and approximate magnitude (Gini 0.514→0.518, wealth poverty 14.1%→17.4%, BLEI poverty 10.6%→15.8% as the floor deepens from $0 to −$50,000, against the N=500 study's 0.515→0.520 / 14.1%→17.5% / 10.6%→15.8%). This is a legitimate, verified contribution — not committed anywhere in this pass (Duke would need to decide whether the harness should move to a modular layout at all), but available if a future session wants it. Meta separately flagged the general-purpose `gamma(a)` rejection sampler's fallback (`return a` after 5,000 iterations without an accepted sample) as a biased-constant risk if ever triggered — technically correct, but immaterial in practice: every `gamma()` call in this codebase uses `a ∈ {1, 2, 5, 6}` (via `beta(2,5)` for octave shape and `beta(6,1)`/`beta(1,6)` for automation risk), the `a=1` case already has its own exact closed-form path, and for `a>1` the rejection rate for this algorithm is high enough that 5,000 consecutive misses is not a practically reachable event. Reviewed, not actioned — the theoretical concern doesn't translate into a real bug at the values this codebase actually uses, and "fix things that are actually broken in practice" (see the `System Stability` and `benefitDays` findings, v4.8) is the standard this project holds itself to in both directions.

**What didn't check out: the proposed `LIVING_WAGE_ANNUAL` recalculation.** Meta's central claim was that the current `$49,370` figure (`$23.735/hr` — cited since v4.3 as a 51-jurisdiction average from World Population Review's MIT-sourced table) "cannot be" MIT's single-adult-0-children figure, because MIT's own max for that family type is `$20.80/hr` (DC) and an average can't exceed its max — and proposed replacing it with a population-weighted `$35,021` computed from a 51-row table of 2024 MIT figures. Meta's own arithmetic on that table was verified and is correct (re-run independently this session: unweighted `$33,932`/yr, population-weighted `$35,020`/yr, essentially matching Meta's `$35,021`) — **but the underlying data was stale, and that's decisive here.** Checking `livingwage.mit.edu` directly (not through a third-party rollup) for the current data build (dated February 15, 2026) found the "1 Adult, 0 Children" figure for **California at $30.48/hr, DC at $26.72/hr, and Mississippi — one of the lowest-cost states — at $20.69/hr**; a separately-sourced October 2025 news article citing MIT's calculator put New Hampshire, an unremarkable-cost state, at $24.78/hr. Every one of these is at or above Meta's claimed $20.80/hr ceiling from 2024 data, and Mississippi alone (traditionally near the low end nationally) now sits almost exactly where Meta's proposed 51-jurisdiction *average* was supposed to land. The clear implication: MIT's figures have risen substantially since whatever 2024 snapshot Meta (and, per its own comments, the World Population Review rollup it drew from) was using — this is not a small rounding difference, DC alone moved from $20.80 to $26.72, roughly +28%, and California moved from $19.41 to $30.48, roughly +57%. Against *current* data, the existing $23.735/hr figure looks considerably more plausible than Meta's proposed $35,021/yr replacement, which would have been a real regression dressed up as a correction. **Not adopted.** This session did not attempt a fresh full 51-jurisdiction pull of current MIT data (that would mean directly fetching all 50 state pages plus DC, not reusing a third-party rollup that may itself lag MIT's own updates, as WPR's own page — still showing DC at $20.80/hr at the time of this check — appears to) — a legitimate future good-first-issue if a rigorously current, dated population-weighted figure is wanted, but the urgency Meta's audit implied does not hold up, and if anything the direction of any future correction is more likely to be upward than downward. See Good First Issues, below, for the precise scope of what a real version of this task would need. The `data/living_wage_population_weighted.js` file Meta drafted is preserved as a record of the (verified-correct-but-stale-input) methodology, not as a source of a number to ship.

**Everything else in Meta's audit** was a mix of re-statements of already-documented open items (the `WEALTH_INIT_MU`/SCF gap, the unbounded long-horizon wealth growth, the low-wage-population mechanism gap, `TARGET_*` recalibration, occupation-risk stratification) — all already tracked in Model Architecture Feedback and Good First Issues below, none newly discovered by this audit — plus suggestions (a production-constraint mechanism for CCO conversion proceeds, a long-horizon wealth ceiling, modularizing `index.html` itself) that are real, substantive framework-design questions for Duke to weigh, not code fixes a review pass should apply unilaterally; modularizing `index.html` specifically would also contradict this document's own explicit, previously-reaffirmed single-file constraint (the same objection already raised against the first v4.7 ChatGPT audit's similar suggestion).

### The harness is now in the actual repo

Per Duke's confirmation this session, `harness.js` has been committed to [the project repo](https://github.com/BetterToBest/compassionism-simulation) — see the WEALTH_FLOOR sensitivity sweep entry under v4.8, above, for the addendum with its current location and a restated scope caveat (Main trajectory only; no ablation/OAT/LHS/validation-suite; no shock mechanics; validated against exactly one regression point).

### What did NOT get fixed, and why

By scope, this was a UI-fix-and-verification pass, not a mechanics-audit release. Not attempted: any `LIVING_WAGE_ANNUAL` change (deliberately — see above, the evidence points the other direction from what was proposed); adopting Meta's modular harness layout (a real option, not decided here); the long-standing open items this audit re-surfaced but did not newly identify (unchanged from v4.8 — see Model Architecture Feedback).

### Regression: seed 42 / Full Integration / 20yr, v4.8 → v4.9

| Metric | v4.8 | v4.9 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |

Expected and confirmed by re-running `harness.js`: v4.9's only change to `index.html` is the `.tbl-scroll` CSS rule and its application to one element — no JS logic, `CFG` constant, or RNG call sequence is touched anywhere.

---

## v4.8 Release Notes

v4.8 combines two different kinds of work: five concrete UI fixes found by Duke actually using the deployed page (not a code audit this time), and completion of two items HANDOFF.md flagged as ready-but-blocked at the end of v4.7 — the `WEALTH_FLOOR` sensitivity sweep and further verification of the occupation-risk dataset lead. A licensing decision that had been logged as open since v4.7 was also resolved this release, on Duke's explicit authorization.

### Licensing: source code moves to Apache License 2.0

Both v4.7 external reviews independently flagged CC BY 4.0 as unconventional for software — Creative Commons' own guidance recommends against using its licenses for code, since they don't address source-distribution terms or patent rights the way an OSI-approved license does — and suggested the common pattern of keeping CC BY 4.0 for papers/documentation while moving code to something like MIT or Apache-2.0. This was logged as an open governance question in v4.7's Model Architecture Feedback rather than acted on. Duke authorized the change this session.

**Decision: Apache License 2.0 for the simulation's source code** (`index.html`, and the harness/tooling scripts referenced throughout this document), **effective v4.8**. Apache 2.0 was chosen over MIT specifically for its explicit patent grant and patent-retaliation clause — a defensive feature with some relevance if this framework's mechanisms were ever built on commercially, and otherwise just as permissive and widely understood as MIT. The full license text is in `LICENSE-CODE.txt`. **Papers, this document, and the replication page's prose are unaffected — still CC BY 4.0.** The DOI-archived snapshot at `10.17605/OSF.IO/QWTE2` predated this change and its own OSF metadata still read CC BY 4.0 at the time this section was written. **Resolved in v4.9** — Duke has since updated the OSF record directly to reflect the split; see the License section, below, for the current account. See the updated footer/citation text in `index.html` and the replication page for how the split is disclosed to readers.

### UI fixes (found via direct testing of the deployed page)

1. **Tooltip text overflowing the viewport.** Root cause: `.abbr-link` was originally written for short (2-4 word) header acronym tips — `white-space:nowrap`, no width cap — but has since been reused for several full-sentence or multi-sentence ⓘ explanations (the longest, on the PTF adoption-cap toggle, is roughly 500 characters rendered as one unbroken nowrap line). Fixed by giving `.abbr-link` the same `width:max-content` + `max-width` wrapping behavior `.tip-host` already had — short tips stay visually identical, long ones now wrap at a sane width instead of running off-screen. Separately, the Scenario Presets grid (two ~130px-wide columns inside a 290px sidebar) centered each button's tooltip on the button itself, which needs roughly 85-95px of clearance on *each* side that a 130px column doesn't have — left-column preset tooltips ran off the browser's left edge, confirmed by inspecting the exact grid/button dimensions. Fixed with `nth-child`-based left/right edge anchoring scoped to that specific grid, since it's a narrow, fixed-column layout where a static rule can be correct (a general JS-based smart-positioning fix, the kind a library like Popper.js provides, would be more robust across arbitrary layouts but is a bigger lift than this fix warranted).
2. **Chart-grid CSS that could overflow at non-default browser zoom, and container boxes not fitting their content.** Several `grid-template-columns` declarations used a bare `1fr` (`.cgrid`, `.kgrid-4/3/2`, `.assump-grid`, `.ms-grid`, `.sens-grid`, `.oat-grid`, and the main `.layout` column) — a bare `1fr` track's minimum width defaults to the content's own intrinsic size (`auto`), not 0, so a wide chart canvas or table could keep a track from shrinking below that width at some viewport/zoom combinations, which reads exactly like "charts not visible at certain zoom %, then zooming out shows portions at small sizes." Changed every one of these to `minmax(0,1fr)` — the standard, well-known fix for this specific class of CSS Grid bug — added `min-width:0` to `.ccard`/`.kpi` (grid *items* also default to a non-shrinking minimum independent of the track fix, so both sides are needed), and added `canvas{max-width:100%;display:block}` as a defensive backstop. **Found and fixed in passing:** a second, later-cascading `.kgrid-2` definition, without the `minmax(0,1fr)` fix, that was silently overriding the first, correctly-fixed one — CSS cascade rules mean the later same-specificity rule always wins, so patching only the first definition would have shipped a fix that silently didn't apply to `.kgrid-2` at all. Caught by grepping for every grid-track definition in the file rather than trusting a single edit location.
3. **BLEI-components chart: the `benefitDays` line looked like it was missing.** Verified via a fresh Node.js harness (see below) that this is **not a computation bug** — at seed 42, Full Integration, 20yr: `cashDays` runs 201d→1,915d (a compounding wealth buffer) while `incomeDays` runs 10.8d→20.1d and `benefitDays` sits at a flat 15.14d the entire run (BU is a fixed monthly allocation, so its BLEI contribution genuinely doesn't grow year over year). `cashDays`' ~100x-larger scale was squashing both smaller series into a few visually indistinguishable pixels near the bottom of one shared linear axis — not a rendering bug in the sense of wrong z-order or a color clash, just an honest consequence of three quantities with wildly different magnitudes sharing one linear scale. Fixed by moving `incomeDays`/`benefitDays` onto their own right-hand axis (`y1`), which now shows their actual shape clearly, including a real crossover around year 11-12 where `incomeDays` overtakes the flat `benefitDays` line as wages grow. Chart caption updated to explain the dual axis and why `benefitDays` is expected to look nearly flat.
4. **System Stability showing the Traditional Welfare Baseline scoring higher than Full Integration was reported as possibly a bug.** It is not — this is the already-disclosed coefficient-of-variation behavior from v4.2/v4.4 (Known Limitations: "System Stability can score a stagnant floor as more stable than a thriving population"): a population pinned at a hard wealth floor has near-zero variance left to measure, so it scores as maximally "stable" by this specific metric's own definition, regardless of whether that flatness reflects a thriving equilibrium or a population with nowhere left to fall. No code change needed here — the metric is behaving exactly as designed and documented. The tooltip fix above should make this explanation actually readable in place, which is plausibly *why* it read as a bug: the explanatory ⓘ tooltip on this exact KPI was one of the long-text ones affected by the overflow issue.
5. **Replication page: the page-header subtitle had grown into a full paragraph-length version-by-version highlight reel** (v4.0 through the current release, all in one always-visible sentence), duplicating content the page's own "Version History" toggle already covers in full further down. Shortened the header subtitle to one line and moved the highlight-reel text into its own small collapsed-by-default toggle in the header, mirroring the existing `.concepts-toggle`/`.changelog-toggle` pattern but styled for the header's dark background.

None of the five items above touch `makeAgent()`/`instantiateAgent()`, `runYear()`, or any metric function — all CSS/markup/chart-config changes. Regression baseline confirmed unchanged (see table below).

### WEALTH_FLOOR sensitivity sweep (the item HANDOFF.md flagged as blocked-on-a-harness)

**The harness, and why it can be trusted.** A standalone Node.js harness was built this session from scratch (no prior harness file was available to copy) — every function (`mulberry32`, `lognormal`/`beta`/`gamma`/`standardNormal`, `drawAutomationRisk`, `makeLatentAgent`/`instantiateAgent`, `szhTheta`, `pthLiquidShare`, `agentBLEI`, `agentEDC`, `bleiMetrics`, `runYear`, `calcMetrics`, `structuralStability`, `getTier`, and the full `CFG` object) transcribed directly from `index.html`. Before being trusted for anything, it was run once at seed 42, Full Integration, 20 years, and checked against every documented regression figure: **median wealth $559,223 exact to the dollar**, Gini 0.534, median BLEI 1,965d, BLEI poverty 13.6%, System Stability 88.5%, avg EDC 24.9%, and Flourishing rate 69.8% (matching the v4.4 regression table's own seed-42 column) — every single one matched exactly, not just within the ~1-3% tolerance this document's own Reproducibility Testing section allows for cross-engine floating-point drift. That gave enough confidence to use it for the sweep below. **v4.9 update:** this file is now committed at `harness.js` in [the project repo](https://github.com/BetterToBest/compassionism-simulation) — it had been a sandbox-only artifact through the end of v4.8 (with an explicit warning in that session's own handoff notes that sandbox files don't persist on their own), so this closes that loose end. Its scope is unchanged and worth restating plainly, since it's easy to over-trust a file just because it's now version-controlled: it reproduces only the Main trajectory (not the paired Baseline/CCO-Only comparison machinery), does not implement `runAblation()`/`runOATSensitivity()`/`runLHSSensitivity()`/`VAL_TESTS`, and has no recession/shock mechanics. It has been validated against exactly one regression point (seed 42, Full Integration, 20yr, shock off) — re-run `node harness.js validate` (~1 second) before leaning on it for anything new, especially after any `index.html` mechanics change, since nothing currently keeps the two in sync automatically.

**Design:** N=500 seeds (1-500), 500 agents, 20 years, shock disabled — matching this document's own large-N study convention — for both Full Integration and the Traditional Welfare Baseline, at four candidate `WEALTH_FLOOR` values: $0, −$10,000 (the shipped default), −$25,000, and −$50,000.

**Headline finding — the two scenarios behave completely differently, for a specific, verifiable reason.** Going in, the naive expectation (mine, initially, from reading the clamping logic) was that `WEALTH_FLOOR`'s value should barely matter to anything except the raw wealth number, since `agentBLEI()`'s liquid-wealth term and both Gini branches already clamp negative wealth to 0 before using it. That's exactly what the data shows **for Baseline** — but not for Full Integration, and the difference is mechanistically clean:

| Metric (mean across 500 seeds) | Full Integration, floor=$0 | floor=−$10,000 (current) | floor=−$25,000 | floor=−$50,000 |
|---|---|---|---|---|
| Median wealth | $526,627 [±3,119] | $526,629 [±3,119] | $526,629 [±3,119] | $526,629 [±3,119] |
| p90 wealth | $1,540,394 | $1,540,394 | $1,540,394 | $1,540,394 |
| Gini (EDC-adjusted) | 0.515 [±0.001] | 0.517 [±0.001] | 0.519 [±0.001] | 0.520 [±0.001] |
| Wealth poverty | 14.08% [±0.14] | 15.30% [±0.14] | 16.55% [±0.15] | 17.48% [±0.15] |
| BLEI poverty | 10.58% [±0.13] | 12.58% [±0.13] | 14.30% [±0.14] | 15.82% [±0.15] |
| Median BLEI | 1,824.2d | 1,824.3d | 1,824.3d | 1,824.3d |
| Flourishing rate | 71.78% | 71.62% | 71.59% | 71.58% |
| System Stability | 88.59% | 88.59% | 88.59% | 88.59% |
| % of agents pinned at floor, final yr | 9.2% | 9.2% | 9.2% | 9.1% |

| Metric (mean across 500 seeds) | Baseline, floor=$0 | floor=−$10,000 | floor=−$25,000 | floor=−$50,000 |
|---|---|---|---|---|
| Median wealth | $0 (100% of seeds pinned exactly) | −$10,000 (100%) | −$25,000 (100%) | −$50,000 (100%) |
| p90 wealth | $544,317 | $544,317 | $544,317 | $544,317 |
| Gini (EDC-adjusted) | 0.858 | 0.858 | 0.858 | 0.858 |
| Wealth poverty | 71.79% | 71.79% | 71.79% | 71.79% |
| BLEI poverty | 70.78% | 70.78% | 70.78% | 70.78% |
| Median BLEI | 7.4d | 7.4d | 7.4d | 7.4d |
| Flourishing rate | 18.45% | 18.45% | 18.45% | 18.45% |
| System Stability | 98.46% (mean) | 98.46% | 98.46% | 98.46% |

**Baseline is bit-for-bit identical across every floor value on every metric except the trivial "median wealth equals whatever the floor is" fact.** This confirms the clamping-logic reasoning exactly: once a Baseline agent starts declining, nothing in the model ever turns that around (no cost-reduction mechanism, and 3% CPI makes the gap worse every year), so they simply sit at the floor for the rest of the run regardless of how deep it is — there's no "recovery dynamics" for the floor's depth to affect.

**Full Integration shows a real, modest, monotonically increasing sensitivity — because some of its agents genuinely do recover from a negative-wealth trough during the 20-year run** (this is the same mechanism behind the already-documented finding that the near-poverty cohort reaches Flourishing within 20 years post-v4.3). For an agent on that recovery path, `agentBLEI()`'s liquid-wealth term is clamped to exactly 0 for every year their wealth is negative, *however negative* — so a deeper floor doesn't make any single year's BLEI worse, but it does mean the agent spends **more years** underwater before their wealth finally turns positive again, because they have further to climb back from. Multiplied across the ~9% of the population who touch the floor at some point, this adds up to the observed effect: Gini +0.005, wealth poverty +3.4pp, and BLEI poverty +5.24pp moving from the shallowest floor tested ($0) to the deepest (−$50,000). Median wealth, p90, and System Stability are untouched even for Full Integration, because the floor-sensitive minority sits below the median, not at it.

**Not acted on.** The shipped `WEALTH_FLOOR` default is unchanged at −$10,000. This sweep is data for the framework's authors to weigh — e.g., a shallower floor measurably improves Full Integration's poverty/Gini/BLEI figures with zero effect on the median-and-above majority, but also removes some of the "realistic insolvency dynamics" v3.1 specifically introduced the floor to allow — not a decision this document is positioned to make unilaterally, consistent with how the λ Calibration Status sweep (below) was also presented as data rather than acted on.

### Occupation-risk dataset lead — further verification (partial)

v4.7 flagged that a Kaggle dataset (`andrewmvd/occupation-salary-and-likelihood-of-automation`) *might* be a machine-readable, complete version of Frey & Osborne's 702-occupation table, but noted its completeness and license weren't checked. This session did more, though still not the full verification HANDOFF.md called for:

- **Confirmed the dataset exists** by fetching its Kaggle listing directly (though Kaggle's page is JS-rendered, so no metadata came through the fetch itself).
- **Found independent, non-Kaggle corroboration**: a separate write-up (an NYC Data Science Academy project building on the same underlying data) states explicitly "the dataset consists of 702 different job titles and their probabilities to automation" — the same row count Frey & Osborne's own paper uses, from a source with no obvious incentive to inflate Kaggle's own listing claims.
- **Found a third-party dataset card** describing the exact column structure needed for the mapping this document has scoped (Occupation, Automation Probability 0-1, Employment, Median Annual Wage, Education Level) and stating the dataset is **MIT licensed** — though this is a third party's description of the Kaggle listing, not Kaggle's own first-party license metadata, which this session's sandboxed network couldn't reach directly (Kaggle isn't in the sandbox's allowed domains, and downloading requires either a Kaggle account or API token).
- **Still no trace of "FOWIGS"** — the specific crosswalk dataset the second v4.7 ChatGPT pass cited. A fresh search this session found nothing, same as v4.7's conclusion. Continue treating this specific citation as unverified/unreliable.

**Net effect: meaningfully stronger evidence than v4.7 had, still short of the row-by-row fidelity check HANDOFF.md asked for.** The next step — pulling the actual CSV (via a Kaggle account/API token) and spot-checking a sample against the original paper's appendix (pp. 57-72) for completeness and fidelity, then confirming the MIT license claim directly against Kaggle's own listing — needs access this session didn't have. See Good First Issues, below, for the precise remaining task.

### What did NOT get fixed, and why

By scope, this was a mixed UI-fix/data-gathering/governance-decision release, not a mechanics-audit one. Not attempted: acting on the `WEALTH_FLOOR` sweep's findings (deliberately — see above); pulling and verifying the occupation-risk CSV itself (blocked on Kaggle access this session's network didn't have); the "no plateau" long-horizon wealth-growth question from v4.6 (still open, still needs its own dedicated release); `TARGET_WEALTH`/`TARGET_POVERTY`/`TARGET_GINI` recalibration (still a framework-author decision).

### Regression: seed 42 / Full Integration / 20yr, v4.7 → v4.8

| Metric | v4.7 | v4.8 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |

Expected and confirmed: none of v4.8's changes touch simulation mechanics — the five UI fixes are CSS/chart-config only, the licensing change is a legal/metadata change, and the `WEALTH_FLOOR` sweep ran against a copy of the engine in an external harness without touching the shipped `CFG.WEALTH_FLOOR` default.

---

## v4.7 Release Notes

v4.7 is a dependency-and-documentation hygiene pass, not a mechanics release — nothing in it changes a single simulation output number. It was prompted by two rounds of external review: a "deep research"-style ChatGPT audit of this project, and a second ChatGPT pass specifically answering six follow-up questions raised in response to the first. Per this project's standing practice, every claim from both was checked against the actual shipped code (and, where it made an empirical claim, against outside sources) before anything was acted on — several claims from both passes did **not** hold up and were not acted on; see "What the audits got wrong," below.

- **Chart.js is now loaded from a version-pinned jsDelivr npm mirror with a verified Subresource Integrity hash — closes an item open since v3.8.** Two earlier reviewers (v3.8, v3.9) each supplied an SRI hash for the cdnjs-hosted file "from memory," and both were unusable (one the wrong character length for a real sha384 digest, the other never checked against a live fetch) — this document's own standing position since then has been that SRI is worth doing but "needs a hash generated and verified directly against the deployed file." This time the hash was computed directly against the actual npm-published `chart.js@4.4.1` package (version confirmed via the file's own banner comment) rather than recalled, and — independently — the second ChatGPT pass computed and reported the identical 64-character hash from the same npm artifact, which is a meaningful cross-check given SHA-384 is a deterministic function of file bytes: `sha384-dug+JxfBvklEQdJ4AYuBBAIScUz0bVN73xpy273gcAwHjb3qI0fXmuYNaNfdyYJG`. Rather than pin that hash against the still-unpinned cdnjs URL (which would only be as trustworthy as cdnjs's own build step matching what it publishes — the exact failure mode both earlier attempts ran into), the script tag now points at `cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.js`, a CDN that serves npm packages byte-for-byte by construction, so the pinned hash is valid by construction rather than by hope.

- **A quick in-app scatter now renders after every LHS export, before the CSV downloads.** The "🧮 Export LHS Sensitivity Design" button previously gave zero in-page feedback — 100 mini-simulations would run and a CSV would appear with no visual gut-check in between. `renderLHSPreview()` plots wealth poverty against monthly BU allocation across the 100 sampled design points (point shade encodes sampled participation rate), reading straight from `LHS_STATE.rows`, already in memory — no new RNG draws, no re-run, no change to the exported CSV itself. Explicitly a sanity-check convenience, not a replacement for the CSV-plus-external-Sobol/Morris workflow the button already exists to hand off to.

- **A new open calibration item, found and logged this pass — not fixed.** Agent wealth is drawn `lognormal(WEALTH_INIT_MU, WEALTH_INIT_SIGMA)` = `lognormal(10.5, 1.2)` (these two constants are new this pass — see the Calibration Validation table, below — promoted from anonymous literals inline in `makeLatentAgent()`, same values, zero RNG or output change). Its median is exactly $e^{10.5} \approx \$36{,}316$ by construction, matching this file's and the interactive tool's own long-standing "Fed SCF 2022" citation. The actual 2022 Survey of Consumer Finances reports median household net worth at **≈$193,000** (Kuhn & Ríos-Rull, NBER working paper, 2025, computed from 2022 SCF microdata) — roughly **5.3× higher**. Both external reviews independently surfaced this same finding; the second ChatGPT pass additionally confirmed the math that makes it a genuinely separate issue from an already-known one: Gini of a lognormal distribution is $2\Phi(\sigma/\sqrt2)-1$, a function of $\sigma$ (`WEALTH_INIT_SIGMA`) alone — so correcting the median (`WEALTH_INIT_MU`) would not move the wealth-init distribution's already-documented inherent Gini ≈0.60 at all. What it *would* move: absolute wealth-poverty rates, especially in early simulated years, since `POVERTY_LINE` is a fixed dollar figure rather than a population-relative one. Not corrected this pass — every downstream wealth/Gini/BLEI/poverty figure in the model starts from this one draw, so a fix needs the same mechanics-audit-plus-large-N-restudy treatment as v4.0/v4.3/v4.4, not a value swap alongside a dependency-pinning release. See Model Architecture Feedback, below.

- **Replication page: PTF's "40–60% overhead reduction" figure disambiguated from the 12–16% cost-reduction rate the engine implements.** The Key Concepts card and the JSON appendix's `ptf_parameters.overhead_reduction` field both stated a Mondragon-analogy "40–60% overhead reduction" figure, undistinguished from the 12–16% `PTF_savings_rate` this engine actually applies to consumer costs — the same two numbers this document's own v4.2 changelog already had to disentangle once before in an old README ("PTF is a 12-16% cost-reduction mechanism only"). Both spots now say so explicitly. Worth naming plainly: the first ChatGPT audit cited "40-60% cost reduction in PTF establishments" as if it were the simulation's own parameter — exactly the confusion this fix closes.

### What the audits got wrong

Documented here because catching these is the whole point of the verify-before-applying step, not a criticism of the reviews for existing. **First ChatGPT pass:** claimed the UI "only has CSV" export (false — `downloadJSON()` and the "⬇ JSON" button have existed since v3.3, already documented in this file's own contribution instructions); claimed a "Citation Generator" link exists in the footer (false — the footer's `.cite-note` span is a static string; nothing generates or customizes it); described "inflation shocks" as using the beta(5,2) distribution (conflates two mechanisms — beta(5,2) governs the *recession* income-multiplier, inflation is a separate flat compounding rate); attributed the $1,200 BU figure to "US CEX data" (this document ties that figure to the Alaska PFD analogue; CES/CEX sources `BASE_DAILY_COST`, a different constant); recommended splitting `index.html` into modules (contradicts this document's own explicit, previously-reaffirmed constraint to stay a single buildless file); recommended a Dockerfile for reproducibility (misdiagnoses the actual risk, which is cross-*browser* floating-point rounding drift on end users' own machines, already correctly described in Reproducibility Testing, below — not a maintainer-side environment issue a container would touch). **Second ChatGPT pass** (otherwise substantially corroborating, see above): cited a "FOWIGS pandemic dataset" as an existing Frey & Osborne/BLS-OES crosswalk; a direct search could not find any trace of it, so it's treated as unverified and not relied on for the Good First Issues update, below — the broader claim that *some* machine-readable Frey & Osborne table exists (e.g. via Kaggle) is independently corroborated and is reflected below, but that specific named source is not.

### What did NOT get fixed, and why

By explicit scope, this was a hygiene pass, not a mechanics or calibration-correction release. Not attempted: actually correcting `WEALTH_INIT_MU` against the SCF figure above (needs its own audit + large-N restudy, see Model Architecture Feedback); the WEALTH_FLOOR/TARGET_* sensitivity sweep floated as a v4.7 candidate (blocked on validating a Node harness against the documented seed-42 regression figures first — not attempted blind, to avoid introducing exactly the kind of unverified-model-output risk this project's audit process exists to catch); occupation-stratified `automationRisk` (a promising Kaggle-hosted lead surfaced this pass, but its completeness and license need direct verification before anything is built on it — see Good First Issues); and relicensing the code away from CC BY 4.0 (both audits independently flagged this as unconventional for software and pointed toward an OSI license like MIT/Apache-2.0 while papers stay CC BY — a real, precedented pattern, but a licensing decision for this project's authors, not something to change unilaterally in a hygiene pass).

### Regression: seed 42 / Full Integration / 20yr, v4.6 → v4.7

| Metric | v4.6 | v4.7 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |

Expected and confirmed by inspection: none of v4.7's four changes touch `makeAgent()`/`instantiateAgent()`'s output, `runYear()`, or any metric function — the Chart.js swap is a `<script>` tag, the LHS preview reads already-computed `LHS_STATE.rows` after the fact, the wealth-init constants are a same-value refactor, and the replication-page wording fix doesn't touch `index.html` at all.

---

## v4.6 Release Notes

v4.6 is another good-first-issues pass, not a mechanics-audit release — three items from the Good First Issues list plus one Model Architecture Feedback item, all completable without a framework-author calibration call. Two items touch simulation output only for users who explicitly opt into a new, off-by-default toggle; the third is export-only; the fourth is a re-run of an existing study, not a code change.

- **Latin Hypercube sensitivity export — implements the exact spec from Good First Issues.** A new "🧮 Export LHS Sensitivity Design" button (sidebar, appears alongside the OAT button after a run) builds a stratified Latin Hypercube design over the same five parameters and ranges OAT already perturbs (BU, participation, Initial PTF share, inflation, conversion tax), reusing `mulberry32` for the design draw itself as specified. Each of 100 design points (default `LHS_N`) runs as its own 200-agent/10-year mini-simulation, all at the same fixed seed (7777, matching OAT's own convention of holding the stochastic realization fixed so cross-row variation is attributable to parameters, not RNG noise) — and the design matrix plus outcome metrics (wealth poverty, median BLEI, participant/non-participant poverty) export as CSV for external Sobol/Morris/regression-based analysis in Python or R. This is deliberately **not** a Sobol sampler — genuine Sobol total/first-order indices need paired Saltelli-structured sample sets beyond a single LHS design; what this delivers is well-stratified parameter-space coverage plus real model output, which is the actual gap the CSV-export-for-external-analysis spec was describing. Verified directly against the shipped `latinHypercubeDesign()`/`runMiniSim()` functions: each of the 5 parameter dimensions is confirmed properly stratified (sorted draws fall one-per-stratum into each of the 100 equal-width bins), and a 10-row sample run through the real engine produces poverty/BLEI outputs that track sensibly with the sampled parameters (e.g. a row with 91% participation and $1,231 BU returns 27.0% poverty/705d BLEI; a row with 10% participation and $359 BU returns 44.5%/183d). Export-only — no effect on any existing run.

- **Feedback-clamped PTF adoption — opt-in, off by default.** Model Architecture Feedback flagged that "the PTF slider sets the t=0 adoption probability only... a quota-based or feedback-clamped adoption model remains open," since organic per-agent adoption (Bass diffusion + economic distress, plus a separate SZH→PTF induction pathway) has no ceiling and realised share can run well past the slider. Confirmed directly: an uncapped seed-42/20yr Full Integration run reaches 53.4% realised PTF share against an 18% slider. A new "Cap adoption at slider value" toggle in the PTF section — **off by default** — makes the slider a genuine ceiling when enabled: both adoption pathways now check a shared, continuously-updated live membership count and stop firing once realised share reaches the configured share, agent-by-agent within a year rather than only checked once per year (the same seed/config lands at 19.0% instead of 53.4% when enabled — see the note below on why it isn't exactly 18.0%). Implemented as a use-side gate on RNG draws (`uPtfAdopt`, `uSzhInduce`, `uSzhPtfShare`) `runYear()` already draws unconditionally every year regardless of branch (the v4.3 RNG-coupling discipline) — enabling the cap adds no new RNG call and does not shift stream position, so every existing preset, the seed-42 regression baseline, and every OAT/validation/ablation mini-simulation (none of which set this flag) are byte-identical to v4.5. **A caveat worth stating precisely, caught during testing:** the cap constrains organic *growth* beyond the year-0 random assignment, not the year-0 assignment itself — `instantiateAgent()`'s Bernoulli draw (`uPTF<ptfShare` per agent) already has sampling variance around the slider value independent of anything this cap touches, and a seed whose initial draw happens to land above the slider (confirmed for seed 42: 95/500 agents = 19.0% at year 0, from that pre-existing randomness alone, before any dynamics run) will hold at that level rather than being forced down to the slider's exact value. This is the correct, intended scope — retroactively correcting t=0 sampling noise would require re-drawing agents, a different and larger change not attempted here. Surfaced in run-config, CSV export, and the run-warnings banner when active.

- **FBS₅₀ half-saturation bandwidth exposed as a derived constant.** The "λ Calibration Status" note (below) recommended reporting the FBS gate's λ coefficient via its half-saturation bandwidth, FBS₅₀=ln(2)/λ, and had already hand-computed the resulting range in prose (≈$524–$4,191/month). `CFG.FBS_HALF_SAT_LO/HI` now compute that range directly from `FBS_LAMBDA_HI/LO` and display it in the Assumptions panel, so it can't silently drift out of sync if the λ range is ever revised again. **Reporting change only** — `makeLatentAgent()` still draws λ directly and uniformly from `FBS_LAMBDA_LO/HI` exactly as in v4.5; confirmed the seed-42 regression is unaffected. A genuine reparameterization — sampling FBS₅₀ as uniform and deriving λ from it, rather than the reverse — would change the shape of the λ distribution (a uniform-in-1/x transform isn't uniform in x) and remains a separate, larger open item, not attempted here.

- **Near-poverty cohort's 40-year extension, rebuilt under current (v4.5) mechanics.** Unreconfirmed since v4.1 — flagged in every release since as "now N mechanics-changing releases stale." Rebuilt via the same methodology as v4.1's own extension (N=1,000 seeds, a fresh draw — not a subset of any other study's seed range — Full Integration, 500 agents, run to 40 years instead of 20, cohort median BLEI recorded at every year). Full results and discussion below, under "40-Year Near-Poverty Cohort Extension (v4.6)" — the short version: the original v4.1 question ("does the cohort ever reach Flourishing, and does a 40+-year horizon change the answer?") is now moot, because v4.3's wealth-loop fix already answers it within the existing 20-year table (median 13.0 years to Flourishing, 5,000/5,000 runs) — this rebuild reconfirms that finding at N=1,000 almost exactly (median 13 years, mean 13.4 years to Flourishing; secure/stable milestones both within a percentage point of the existing 20-year figures). The genuinely new information the 40-year window provides is different and arguably more important: **cohort median BLEI shows no sign of plateauing** — it continues climbing at an accelerating pace past year 20 (1,618d → 7,058d by year 40, more than quadrupling), and population-wide median wealth reaches roughly $2.12M by year 40 with no indication of a ceiling. This surfaces a new open question, not resolved here — see Model Architecture Feedback.

### What did NOT get fixed, and why

This was a good-first-issues pass by explicit scope. Occupation-*stratified* automationRisk, `WEALTH_FLOOR`/`TARGET_*` recalibration, the framework-level low-wage-mechanism question, and a genuine production/treasury constraint on BU conversion proceeds all remain open, unchanged from v4.5 — see Model Architecture Feedback and the remaining Good First Issues, below. The new long-horizon wealth-growth question the 40-year cohort rebuild surfaced is also not resolved here — flagged as a new open item, below.

### Regression: seed 42 / Full Integration / 20yr, v4.5 → v4.6

| Metric | v4.5 | v4.6 | Δ |
|---|---|---|---|
| Median BLEI | 1,965d | 1,965d | — |
| Median wealth | $559,223 | $559,223 | — |
| Gini (EDC-adj.) | 0.534 | 0.534 | — |
| Wealth poverty | 16.6% | 16.6% | — |

Zero movement, confirmed directly against the shipped engine rather than assumed from code inspection alone — none of v4.6's three code changes touch default-configuration output: the PTF adoption cap defaults off (and is not set by any preset), the FBS₅₀ constants are a display-only computation over existing values, and the LHS export runs its own isolated mini-simulations without touching the main run. The 40-year cohort study is a fresh large-N study, not a mechanics change, so it has no seed-42/20yr regression entry of its own.

### 40-Year Near-Poverty Cohort Extension (v4.6)

Methodology mirrors v4.1's own extension exactly: N=1,000 seeds (1–1,000, a fresh draw), Full Integration, 500 agents, 40-year horizon instead of 20, cohort tagged by year-0 wealth < $25,000 (37.8% of the population, mean — consistent with every prior version), cohort median BLEI recorded at every year.

**Milestones (cohort median crossing each BLEI tier, per-seed, then aggregated across the 1,000 seeds) — reconfirm the existing 20-year figures almost exactly:**

| Milestone | 20yr table (N=5,000, v4.4/v4.5) | 40yr rebuild (N=1,000, v4.6) |
|---|---|---|
| Threshold (≥30d) | immediate (month 0), 5,000/5,000 | immediate (month 0), 1,000/1,000 |
| Stable (≥120d) | 36.0 months (3.0 yr) [mean 38.6mo] | 36.0 months (3.0 yr) [mean 39.0mo] |
| Secure (≥365d) | 104.9 months (8.7 yr) | 105.2 months (8.8 yr) |
| Flourishing (≥730d) | 156.0 months (13.0 yr) [mean 161.0mo], 5,000/5,000 | 156.0 months (13.0 yr) [mean 161.2mo], 1,000/1,000 |

This close a match across an independent seed range and a 5× smaller N is itself informative: it confirms the 20-year figures are not an artifact of the specific 5,000-seed draw, and that extending the horizon doesn't change *when* the cohort crosses milestones it was already crossing well inside 20 years.

**What extending to 40 years actually adds — no plateau, and a new open question:**

| Year | Cohort median BLEI (days) |
|---|---|
| 5 | 201 |
| 10 | 488 |
| 15 | 951 |
| 20 | 1,618 |
| 25 | 2,522 |
| 30 | 3,706 |
| 35 | 5,190 |
| 40 | 7,058 |

Rather than flattening out after the cohort clears Flourishing (as the pre-v4.3 mechanics did — that study's cohort median climbed only to ≈428d by year 40, still short of the 730d line), the post-v4.3 cohort's median BLEI keeps compounding, quadrupling between year 20 and year 40 alone. Year-40 population-wide headline figures (same N=1,000 runs, whole population not just the cohort) show the same pattern: median wealth ≈$2,115,547 (mean $2,117,807), EDC-adjusted Gini 0.422 (down from 0.518 at year 20 — continued equalization, not a reversal), wealth poverty 3.8%, BLEI poverty 3.2%, Flourishing rate 91.8%, population median BLEI ≈7,252 days.

**This is a genuinely new finding, not a repeat of v4.3's already-documented redistribution story, and it isn't resolved here.** The main wealth-accumulation loop (§2, Mathematical Framework in the replication page) has no explicit long-run ceiling — no retirement, no consumption floor that scales with wealth, no diminishing-returns term beyond the existing wage-growth dampening — so once an agent's annual wage-plus-conversion surplus consistently exceeds cost, wealth compounds essentially without bound over multi-decade horizons. Whether this is a problem depends entirely on what a 40-year run is being used for: as a stress-test of whether the *poverty-elimination* mechanisms keep working at longer horizons, this is arguably a non-issue (nobody is worse off). As a claim about *plausible* absolute wealth levels 40 years out, a median of $2.1M per adult household is well outside any real-world reference point this document uses elsewhere (Fed SCF, Census/BLS) and should not be read as a projection. Tracked as a new open item — see Model Architecture Feedback.

---

## v4.5 Release Notes

<!-- v4.13 note: this heading was also missing, the same defect as v4.11's below —
     found while fixing that one, by listing every `## ` heading in the file rather than
     assuming v4.11 was the only casualty. Two of the eleven release sections had lost
     their headings; a single grep would have caught either at any point since. Restored. -->

v4.5 is a good-first-issues pass, not a mechanics-audit release like v4.3/v4.4 — five items pulled directly from this document's own Good First Issues list (below), all completable without new external data or a framework-author calibration call. Validation scope matches the smaller stakes: a moderate-N sanity check for the one item that changes simulation output, not a fresh N=5,000 study.

- **PTH liquidity haircut implemented — tenure-cohort schedule replaces the flat 50%.** v4.3 added per-agent `pthTenure` tracking as a first step toward this; v4.5 implements the haircut itself via `pthLiquidShare(tenure)` — a linear ramp from 15% at tenure=1 (the closest available point to the BLEI paper Table 1a's "6 months" anchor, given tenure is tracked in whole years) to 85% at tenure≥5 (the paper's "5+ years" anchor), replacing the flat 50% share of annual Acre Equity appreciation counted as liquid wealth used through v4.4. Both anchors are the midpoint of the paper's cited range (10–20% / 80–90%) — the paper gives two qualitative points, not a closed-form curve, so the ramp between them is a documented interpretation choice, not a re-derivation. Since PTH membership doesn't change once assigned, most PTH agents spend the majority of a 20-year run at the mature 85% rate (16 of 20 years) — higher than the old flat 50% for most of the run, lower only in years 1–4.
- **"Copy parameters as URL."** Serializes the current sliders/toggles/seed into a query string, copied via the Clipboard API. Loading a shared link applies its params on top of the Full Integration defaults before the page's own auto-run, so a link only needs to specify what differs from the reference config; the seed-42 "illustrative reference run" banner only fires when no recognized params are present in the URL.
- **Social Security-anchored cohorts surfaced as in-app UI, not harness-only.** The N=5,000 study this document has carried since v4.3 (below) now also appears as a final-year table in the results panel — SSI-level, SSDI-level, and Retirement-level rows, computed from the same final agent state and `calcMetrics()`/`bleiMetrics()` calls the headline KPIs already use. Cross-sectional by design, matching this document's own method: cohort membership is fixed at year 0, not tracked over time. Single-run figures will vary seed-to-seed, especially for the small SSI-level cohort (≈0.8% of a 500-agent population) — this document's own N=5,000 table remains the citable figure.
- **BLEI tier definitions and preset descriptions on hover** — two smaller good first issues, done together. An ⓘ next to the tier-distribution chart's title shows each tier's day-range; each of the five preset buttons shows a one-sentence description of what it actually configures, on hover.
- **Cosmetic, no output effect:** `instantiateAgent()`'s `pthTenure:inPTH?0:0` ternary (identical branches — a copy-paste leftover, previously noted and left alone at v4.4) simplified to `pthTenure:0`.

### Regression: seed 42 / Full Integration / 20yr, v4.4 → v4.5

| Metric | v4.4 | v4.5 | Δ |
|---|---|---|---|
| Median BLEI | 1,951d | 1,965d | +14d |
| BLEI poverty | 13.6% | 13.6% | — |
| Median wealth | $558,001 | $559,223 | +$1,222 |
| Wealth poverty | 16.6% | 16.6% | — |
| Gini (EDC-adj.) | 0.535 | 0.534 | −0.001 |
| System Stability | 88.6% | 88.5% | −0.1pp |
| Avg EDC | 24.9% | 24.9% | — |

All movement traces to the PTH liquidity haircut alone — the only item in this release that touches simulation output — confirmed with an isolated N=300 seed-paired comparison (same population/RNG per seed, only `pthLiquidShare()` toggled between the old flat 0.5 and the new schedule): median wealth $523,958→$526,941 (+0.6%), median BLEI 1,820.6d→1,826.0d (+0.3%), all other headline metrics unchanged to the precision reported. All six `VAL_TESTS` pass 5/5 post-change.

### What did NOT get fixed, and why

This was a good-first-issues pass by explicit scope, not an audit release. `WEALTH_FLOOR` and `TARGET_*` recalibration, the Sobol/LHC sensitivity export, occupation-*stratified* automationRisk, the near-poverty cohort's stale 40-year extension, and the framework-level low-wage-mechanism question all remain open, unchanged from v4.4 — see Model Architecture Feedback and the remaining Good First Issues, below.

---

## v4.4 Release Notes

v4.4 is a mechanics-changing release, and the first shipped only after putting the prior release through two independent adversarial code audits rather than trusting internal validation alone — this document's own account of the v4.0-v4.3 history is a record of real bugs slipping through multiple prior passes, so an audit step is now the default before further mechanics changes to a published research artifact, not a formality.

**The audit process.** First pass: an open-weight model (Qwen3-Coder-30B-A3B-Instruct) orchestrated via RunPod Serverless, given an explicitly skeptical prompt instructing it not to assume anything was correct. It returned seven structured, plausible-looking findings. Every one was independently re-verified against the actual code and **rejected as a false positive** — a self-contradicting RNG-stream claim that named no actual conditional draw, a misread of an existing `Math.max` guard, a misunderstanding of the documented PTH-equity accounting, among others. None were applied. Second pass: a more rigorous review returned twelve findings; most held up under the same direct-code verification this time. Four were judged substantive and consequential enough to implement as a real mechanics-changing release rather than a quiet patch — the four items below.

- **Wage/income scale unified across BLEI, FBS, and Gini.** v4.0 fixed unit-mixing inside these formulas using `SIU_TO_USD` (≈16.63) — a cost-side-derived approximation, invented because no real wage-side dollar anchor existed at the time. v4.3's `WAGE_TO_USD` (≈100.52, Census/BLS-sourced) was scoped to the main wealth loop only, leaving the same agent's wage worth roughly $3,518/month for wealth accumulation and roughly $582/month for welfare measurement simultaneously — a ~6× divergence the second audit correctly identified as no longer defensible once one anchor is empirically grounded and the other isn't. `SIU_TO_USD` is **retired**. `agentBLEI()`'s income-buffer term, `calcBLEIComponents()`, the FBS gate's `Yusd`, and the EDC-adjusted-Gini calculation now all use `WAGE_TO_USD`. `agentEDC()` was and remains unaffected — it's a dimensionless SIU/SIU ratio that never touched either constant.

- **`FBS_LAMBDA` recalibrated — and the reason has since been corrected following post-release review.** `λ`'s units are 1/USD by its own original code comment; once its dominant input (`Yusd`) grew ~6× under the wage-scale fix, `λ` left unscaled pushed octave-advancement probability toward saturation regardless of BU level, measurably weakening the BU-monotonicity `VAL_TEST` (one seed dropped from a clean win to an exact tie at n=200). Rescaled ÷6.0456 — the precise `WAGE_TO_USD`/legacy-`SIU_TO_USD` ratio — from 0.001/0.008 to 0.0001654/0.0013233, preserving the 8× HI/LO heterogeneity shape. **This document originally described that rescale as a "dimensionally-necessary consequence" of λ's units — that overstated the case.** FBS combines the wage-derived term that changed scale with fixed-dollar terms (BU face value, basic cost) that did not, so FBS as a whole does not scale by a single clean factor; dividing λ by exactly 6.0456 is a *chosen behavioral recalibration* to restore useful dynamic range across the model's population, not a unit identity. It is retained because the paper's own original range (λ ~ U(0.001, 0.008)) produces near-saturated advancement probability (89.8–100%) even at the BLEI paper's own worked-example FBS ($2,281/month), leaving little of λ's intended role as an "individual capability coefficient" — see the calibration-status note added to the BLEI paper (Index IV) and to the replication framework (Mathematical Framework §4) for the full account, including the recommendation to eventually reparameterize by half-saturation point (FBS₅₀ = ln(2)/λ) rather than a raw 1/USD coefficient. All six `VAL_TESTS` pass 5/5 post-change — that establishes internal behavioral consistency, not empirical correctness of the absolute λ values; λ's empirical grounding remains open, as it was before v4.4.

- **True common-random-numbers pairing across Baseline / CCO-Only / Main.** v4.2 paired the three scenarios' *populations*; their year-by-year trajectories still ran on three independently-offset RNG streams (`seed+700001`/`seed+700002`/unoffset), decorrelated from each other and from Main — not just from population construction, as v4.2's own note already flagged as a remaining gap. Since v4.3 made `runYear()` draw a fixed count and order of RNG calls per agent per year regardless of policy toggles, three independent same-seed `mulberry32()` closures now necessarily produce identical draw sequences at each (agent, year) position — verified this has zero effect on Main's own trajectory, since `mulberry32()` returns a fresh, independent closure on every call. The ablation engine already used this same same-seed pattern successfully; this brings the main comparison in line with it.

- **Baseline's undocumented ×0.85 initial-wealth haircut removed, and automation exposure now paired.** Baseline agents received an extra ×0.85 wealth adjustment on top of sharing v4.2's paired population, applied before CCO has had any chance to act — no external citation existed for the figure, and it embedded part of the treatment effect into the counterfactual's own starting point. Removed. Separately, Baseline was hardcoded exempt from AI automation exposure even when a user enabled it for the tested scenario, while CCO-Only already mirrored the setting — now paired. Neither fix meaningfully moves the standard reference-configuration figures below (automation defaults off; Baseline's median wealth remains exactly floor-pinned regardless — now confirmed in **100% of N=5,000 runs**, not "more than half" as v4.3 described, since the binding constraint turned out to be the ongoing annual cost/wage gap, not the year-0 starting point).

**A genuine bug, found independently of either audit while building this release's N=5,000 harness.** The general-purpose gamma-distribution sampler divides by `(a−1)` inside a log term; at `a=1` exactly this is `x/0`, making the acceptance test `0×log(∞)=NaN` and therefore always false. Every call exhausted all 5,000 rejection iterations and silently returned the constant `1` — confirmed: 20 of 20 samples identical in testing — not a random Exponential(1) draw. This directly narrows `drawAutomationRisk()`'s `beta(6,1)`/`beta(1,6)` components, used once per agent on every simulation run (browser or harness), and wasted the full 5,000 dead iterations each time. Fixed with the exact closed-form solution — Gamma(shape=1) is exactly Exponential(1), so `-Math.log(RNG())` replaces the rejection loop entirely for this case. Side effect: population construction is now roughly **200× faster**, without which this release's fresh N=5,000 study would not have been practical to run in the time available.

### What the v4.4 fixes actually do

Figures below are N=5,000, same methodology as v4.3's study (seeds 1–5,000, 500 agents, 20 years, shock disabled). Full headline table under Reproducibility Testing.

Full Integration median wealth rose modestly, $495,411→$526,120 (+6.2% — not a repeat of v4.3's much larger jump; this release mostly corrects a measurement formula, not the wealth-accumulation mechanism itself, apart from the FBS-gate feedback described above). BLEI poverty fell 17.1%→12.5%; wealth poverty fell 19.5%→15.4%; EDC-adjusted Gini fell 0.536→0.518 (Full Integration and CCO-Only both became *more* equal, not less). Participant poverty (wealth) fell 15.4%→10.0%; **non-participant poverty is exactly unchanged, 34.3%→34.3%** — a clean mechanistic confirmation the fix behaves as intended, since non-participants never execute the FBS-gated code path this release touches.

The Social-Security-anchored cohorts (v4.3) improved measurably but not qualitatively: SSDI-level median BLEI 16.4d→22.6d, retirement-level 16.6d→a median-of-medians 25.1d. **A methodological correction worth naming, caught before publication:** BLEI is right-skewed for these small (≈4–86 agent) cohorts, and an initial mean-based reading of the retirement-level cohort (mean 32.0d) would have overstated it as crossing the 30-day Threshold. The median-of-medians (25.1d) and the actual per-seed crossing rate (31.1% of 5,000 seeds) both show the typical case still falls short — see the updated table below. The relative-improvement multiplier over Baseline, originally reported as 20–30× under v4.3 mechanics, is now **~7–10×** under v4.4 — not because Full Integration helps this population less, but because Baseline's own BLEI also rose under the corrected wage-buffer term (from near-zero to a few days), narrowing the ratio even as both sides' absolute figures moved in the right direction. The qualitative conclusion is unchanged: Full Integration helps this population enormously in relative terms without lifting the typical case out of poverty by the simulation's own tier definitions, for any of the three anchors.

### What did NOT get fixed, and why

`WEALTH_FLOOR`, and the pre-existing `TARGET_WEALTH`/`TARGET_POVERTY`/`TARGET_GINI` design targets, remain open — both explicitly framework-level decisions requiring the framework's own authors' judgment, not code fixes (see Model Architecture Feedback, below, now considerably more pressing given the wealth figure has moved even further from the original target). This release adds a direct in-app disclosure on the affected KPI badges (the ⓘ icons next to Gini, Median Wealth, System Stability, Flourishing Rate, and EDC in the interactive tool) pointing to this section, without picking new numbers itself. A genuine production/treasury constraint on BU conversion proceeds remains unscoped. The v4.1 40-year cohort-Flourishing extension remains unreconfirmed, now three mechanics-changing releases stale — given how far the 20-year figures have moved, a fresh 40-year run would very likely show materially different results; tracked as an open item rather than assumed either way. The Replication Framework HTML, deliberately unsynced past v4.2 pending this release's audit, is updated alongside this document — its own Version History now covers v4.3 and v4.4 together, since no intermediate v4.3 snapshot of that page was ever published.

---

## v4.3 Release Notes

v4.3 is a mechanics-changing release — **it changes the RNG call sequence and the main wealth-accumulation loop's calibration, so seed-42 output does not reproduce v4.2's** (see the new regression table under Reproducibility Testing, below). Four items:

- **Main wealth-accumulation loop unit fix (resolves the highest-priority open item carried since v4.0).** The wage(SIU)/wealth(USD) mismatch in the main annual wealth update is fixed with two new constants: `WAGE_TO_USD ≈ 100.52` converts wage to real USD (derived from $42,220 median personal income, Census/BLS CPS ASEC 2023, ÷ 35 SIU × 12); `LIVING_WAGE_ANNUAL = $49,370` anchors the cost side (a national living-wage figure for a single adult with no children — $23.735/hr average across 50 states + DC, from World Population Review's MIT-sourced table, × 2,080 hrs/yr; this is an *unweighted* average across jurisdictions, not population-weighted like MIT's own paid Living Wage Calculator product — see the caveat below). This replaces netting WAGE_TO_USD-converted wage against `BASE_DAILY_COST` — a bare-subsistence floor, correct for BLEI's poverty-line use but wrong for a 20-year compounding loop netted against real wage, and which produced an ~11x wealth explosion and broke BU-monotonicity (2/5 seeds) when tested. All six `VAL_TESTS` pass under the shipped anchor, including BU-monotonicity (5/5). `dollarCost`/`BASE_DAILY_COST` is unchanged everywhere else (BLEI, FBS, Gini, and the PTH equity contribution — see the code comment at the PTH block for why that specific choice was tested against the alternative and kept as-is) — only the main loop's cost side changes.

  **This is not a clean win — it redistributes as well as it grows, and it does so along more than one axis. See "What the wage/cost fix actually does," immediately below, for the full picture — this bears directly on the framework's central poverty-elimination claim and should not be read from the headline wealth figure alone.**

- **`runYear()` RNG coupling fixed (resolves the item found in v4.2).** Every conditional quantity inside the per-agent loop (BU spend fraction, CIP quality bump, octave advancement, SZH→PTF induction and share, PTH appreciation noise, PTF Bass adoption) is now drawn unconditionally every year for every agent; only the *use* of the drawn value is gated — mirroring the v4.2 `makeLatentAgent()` eligibility-draw fix. The non-participant-poverty validation check is tightened back to strict per-seed agreement at n=200 (was a mean-across-5-seeds workaround at n=500) and passes 5/5.

- **Per-agent PTH tenure tracking (first step, not the full fix).** Agents now carry `pthTenure` (years held in PTH residency), incremented each year while in PTH and reset on exit. This is tracking data only — the variable tenure-cohort liquidity haircut itself (BLEI paper Table 1a) is not implemented this pass; the flat 50% haircut is unchanged. Tracked as a Good First Issue, below. **v4.5 update: implemented — see Release Notes, above.**

- **Bimodal `automationRisk` distribution.** Replaces uniform[0.2,1.0] with a 47%/53% mixture — high-risk agents ~ Beta(6,1) (mean ≈0.857), low-risk agents ~ Beta(1,6) (mean ≈0.143) — sourced to Frey & Osborne (2013)/Autor (2015): ~47% of US employment sits above a 70% computerization-probability threshold across 702 O\*NET occupations. Verified to have no material effect on aggregate outcomes on its own (isolated in testing before the other three items were combined with it).

### What the wage/cost fix actually does

The single-seed spot-check that first surfaced this (seed 42, reported when the fix was first validated) is now reconfirmed at scale: a 5,000-seed large-N study (seeds 1–5,000, 500 agents, 20 years, same methodology as the v4.0/v4.2 studies below) shows the same pattern holds robustly, and reveals two further effects the single seed didn't have the power to show cleanly. All three are real, and none of them is a reason to revert the fix — `BASE_DAILY_COST` (the pre-v4.3 anchor) is arithmetically wrong for this specific loop, in a way that produced an 11x wealth explosion when tested; `LIVING_WAGE_ANNUAL` is the anchor that passes validation. But "this anchor is more correct" and "this anchor is comfortable" are different claims, and the second one is false in an important way.

1. **Within Compassionism, the fix redistributes as well as grows.** At N=5,000, Full Integration median wealth rises from $80,008 to $495,411 (a ~6.2x increase, consistent with the seed-42 spot-check's $514,502), but EDC-adjusted Gini rises from 0.479 to 0.536 and wealth poverty rises from 14.4% to 19.5%. Mechanism: low-wage-draw, high-`automationRisk`, and non-participating agents don't share proportionally in the wage-side correction the way median-and-above-wage agents do, who now compound a much larger annual surplus.

2. **The Traditional Welfare Baseline collapses far more severely than before.** This is the larger effect, and it wasn't visible in the single-seed check. Baseline agents get no CCO/PTF/PTH cost relief, so their full weight lands on the new $49,370 cost anchor — and a median-wage worker's annual wage income (~$39,800 at year-0 wage, via `WAGE_TO_USD`) doesn't cover that figure even before the baseline's existing 3% CPI compounding widens the gap every year. At N=5,000: median wealth falls from $7,316 to **exactly the wealth floor, −$10,000** — meaning more than half the baseline population is pinned at the debt ceiling by year 20 — wealth poverty rises from 52.2% to 72.3%, and Gini rises from 0.800 to 0.855. This is a legitimate, mechanistically-understood consequence of the new anchor, not a bug — but a median outcome sitting exactly at a hard floor is a blunter result than the pre-v4.3 baseline's, and raises a real question of its own: **is `WEALTH_FLOOR = −$10,000` still the right floor value now that the cost anchor roughly doubled?** Flagged as a new open item below, not resolved here.

3. **The near-poverty (low-*wealth*) cohort now reaches Flourishing — a complete reversal.** The existing near-poverty cohort (year-0 wealth < $25,000, 37.7% of the population) is defined by low starting *wealth*, not low *wage* — and most of its members have ordinary wage draws. Under the new anchor they benefit enormously: cohort-median time to Stable (≥120d) drops from 158.8 months (13.2 years) to 48 months (4 years); a new Secure (≥365d) milestone is reached at 108 months (9 years); and the cohort median reaches **Flourishing (≥730d) in 5,000 of 5,000 runs** within the 20-year horizon — versus 0 of 5,000 runs even after extending to 40 years under pre-v4.3 mechanics (see the v4.1 extension study, below). This is the flip side of finding 1: agents whose *wage* is decent do very well under this fix, regardless of how little wealth they started with.

Findings 1 and 3 together say something more precise than "wealth up, Gini up": **the fix helps agents by wage level, not by starting wealth.** A wealth-poor-but-decent-wage agent now does about as well as anyone; a low-wage agent does not, no matter their wealth. This is exactly the distinction BLEI/EDC-based analysis is supposed to surface over a raw dollar comparison, and it's the reason a wage-anchored cohort — not just the existing wealth-anchored one — is worth tracking directly. See the new Social-Security-anchored cohort study, below, which does exactly that and confirms the concern precisely: even under Full Integration, a cohort whose wage sits at real-world Social Security benefit levels remains deeply impoverished by the simulation's own tier definitions, despite being dramatically better off than under the baseline.

### Social Security-anchored income cohort (new this release)

Prompted by a question raised in review: comparing Compassionism to the US baseline using median-income anchors doesn't show how the framework treats the population most relevant to a poverty-elimination claim — people living on a fixed, sub-median income, not median-wage workers. Real 2026 Social Security figures (SSA's official COLA Fact Sheet, ssa.gov/news/en/cola/factsheets/2026.html) give three anchors:

| Anchor | Monthly / annual | Wage equivalent (SIU, via `WAGE_TO_USD`) | Share of population at or below |
|---|---|---|---|
| SSI federal payment standard, individual | $994/mo, $11,928/yr | 9.89 SIU | 0.8% |
| SSDI average, all disabled workers | $1,630/mo, $19,560/yr | 16.22 SIU | 7.7% |
| Average retired-worker benefit | $2,071/mo, $24,852/yr | 20.60 SIU | 17.1% |

These are reference points, not a simulated Social Security mechanism — the model has no age, disability, or retirement structure (see Known Limitations), so "SSDI cohort" here means *agents whose initial wage happens to sit at this level*, tracked with the same mechanics as everyone else, not agents receiving a modeled benefit with COLA adjustment or recession insulation. That distinction matters and is stated plainly rather than implied away. Tagged from each agent's initial (pre-dynamics) wage, same convention as the existing near-poverty cohort's year-0 wealth tag. `CFG.SS_ANCHOR_SSI_ANNUAL`/`SS_ANCHOR_SSDI_ANNUAL`/`SS_ANCHOR_RETIRE_ANNUAL` hold the dollar figures.

N=5,000 results, Full Integration vs. Traditional Welfare Baseline (same seeds, methodology as above):

| Cohort | Scenario | Wealth poverty | BLEI poverty | Median BLEI | Flourishing rate |
|---|---|---|---|---|---|
| SSI-level (0.8% of pop.†) | Full Integration | 96.5% | 83.0% | 26.3d | 1.6% |
| | Baseline | 99.9% | 99.9% | 1.1d | — |
| SSDI-level (7.7% of pop.) | Full Integration | 84.2% | 80.3% | 16.4d | 7.9% |
| | Baseline | 99.8% | 99.8% | 0.5d | — |
| Retirement-level (17.1% of pop.) | Full Integration | 74.0% | 67.9% | 16.6d | 13.7% |
| | Baseline | 99.7% | 99.7% | 0.6d | — |

† The SSI-level cohort is small (≈4 agents per 500-agent run), so its per-seed median is noisy even at 5,000 seeds — directionally informative, not precision-grade. The SSDI- and retirement-level cohorts (≈38 and ≈85 agents per run) are on firmer statistical ground.

**Read plainly: Compassionism helps this population enormously in relative terms — 20-30x the median BLEI of the baseline, where these agents are functionally at zero — but does not come close to lifting them out of poverty in absolute terms.** Median BLEI in the teens of days is deep in the Precarious tier, nowhere near the 30-day Threshold, let alone the reference configuration's own headline 67.8% population-wide Flourishing rate. The mechanism is direct: even with PTF/PTH cost reductions (~46% combined) and BU support, an agent whose wage sits near or below Social-Security-benefit levels doesn't generate enough annual surplus for the model's other mechanisms (octave advancement, PTF conversion gains, PTH equity building) to compound meaningfully within 20 years. **This is the sharpest test of the framework's poverty-elimination claim run so far, and the framework does not pass it** — a finding that should sit alongside the headline large-N figures in any public-facing summary, not be filed only here.

---

## v4.1 Release Notes

v4.1 is an audit-driven bug-fix release (Claude/Anthropic chat audit, Aug 2026) — unlike v4.0, it does not change simulation mechanics, so the regression baseline and large-N figures below carry over from v4.0 unchanged (confirmed, not assumed — see the v4.1 regression check under Reproducibility Testing). Three fixes:

- **PTF attribution leak in ablation.** `runAblation()`'s paired-population design (v4.0) intentionally builds every removal scenario's agents under the full config for RNG-pairing, but `agentBLEI()`'s SZH+PTF synergy term had no `ptfOn` parameter to gate on — unlike `ccoOn`/`pthOn`, which already gated the equivalent CCO/PTH terms. Result: the "Remove PTF" ablation result could retain a synergy bonus it shouldn't have whenever SZH was also active, understating PTF's contribution on the Attribution chart (~12 BLEI days per affected agent in testing). If you've cited or screenshotted Attribution-chart output from v4.0 or earlier with SZH active, it's worth a re-run under v4.1. Normal (non-ablation) runs are numerically unaffected.
- **Illustrative reference-run label was never shown.** The `IS_REF_RUN` flag (added v3.4) was set but never read, so the "illustrative reference run" banner never actually displayed. Wired up; purely cosmetic.
- **Several UI hint strings had drifted from the formulas they describe** — a recession-duration/severity hint, the Max Octave conversion-capacity hint, a stale default display value, a baseline-chart caption, and one OAT sensitivity range — none of these affect computed results, only what the UI *says* about them. Full detail in `index.html`'s own changelog (search "v4.1").

---

## v4.2 Release Notes

v4.2 is a mechanics-changing release (external audit + internal review, Aug 2026) — **unlike v4.1, it changes the RNG call sequence, so seed-42 output no longer reproduces v4.1's** (see the regression table under Reproducibility Testing, below). This is allowed under this document's own rule that an intentionally mechanics-changing PR should say so explicitly (Code Contributions, below):

- **Common-random-numbers population pairing.** `makeAgent()` is now a thin wrapper over `makeLatentAgent()` (draws pre-policy latent traits, no scenario-specific logic) and `instantiateAgent()` (pure, zero-RNG, scenario-specific mapping). The main run, CCO-Only, and baseline comparisons now share one canonically-drawn latent population instead of three independently-sampled ones — closing the item raised in the Aug 2026 external review ("the baseline and CCO-only populations are not actually the same individuals") and in Model Architecture Feedback, below. Verified with unit tests: agent *i*'s wealth/wage/automationRisk/λ are bit-identical across all three scenario instantiations, differing only in octave/quality (correctly, since those scale by scenario-specific `maxOct`/`maxMult`) and participation flags.
- **Independently found while building the above.** `makeAgent()`'s three eligibility draws used short-circuit `&&`, so the number of RNG calls consumed during agent construction depended on which subsystems were toggled on. Two scenarios built from the "same" seed but different toggle states — e.g. the validation suite's own PTF-on vs PTF-off check — silently diverged in every draw after the first toggle difference, not just membership. Fixed by drawing all three eligibility uniforms unconditionally in `makeLatentAgent()`.
- **Does not extend to full within-run trajectory pairing.** `runYear()` still consumes a variable number of RNG calls per agent depending on which of its *own* conditional branches fire that year, so two scenarios with different participation *composition* still decorrelate agent-level trajectories after year 0, even from an identical starting population. Population-level aggregates (poverty rate, median BLEI) are unaffected. **Fixed in v4.3 — see above.**
- **Structural System Stability metric**, replacing the v3.6-flagged trend-plus-noise heuristic — resolves a good-first-issue below. `structuralStability()` is the inverse coefficient of variation of median wealth and median BLEI over the run's final quarter: no RNG call, no manual per-mechanism bonus. Baseline/CCO-Only comparison rows, previously hardcoded "~65%"/"~88%", now compute the same metric from their own trajectories.
- **Validation suite → 6 checks.** The original four now run across 5 seeds (`VAL_SEEDS`) and require unanimous agreement, instead of one hardcoded seed each (all four are robust 5/5). Added a non-participant-poverty check (resolves a second good-first-issue, below) and a structural-invariants check (population conservation, octave/wealth-floor/participation bounds, Gini bounds). Renamed "Internal Validation Suite" → "Internal Consistency & Behavioral Test Suite," labeled against an ODD Level 1–5 hierarchy (this suite covers Levels 1–3 only).
- **"Policy-grade" language tightened** to "research-oriented exploratory... for comparative policy analysis" throughout title/meta/social tags, matching framing already used elsewhere in the same file (CSV export, Known Limitations).

The replication document was updated in parallel — a new Version History toggle, refreshed Known Limitations, and version numbers throughout — but its headline large-N figures have **not** yet been reconfirmed under v4.2 mechanics (see Reproducibility Testing, below). Full derivation in `index.html`'s own changelog comment (search "v4.1 → v4.2").

---

## Reference configuration: notes by version

These notes followed the Reference Parameter Configuration table in CONTRIBUTING.md until v5.2.

**v5.0 (released Oct 2, 2026):** the page now runs Compassionism as specified on the Hub with every planned mechanism, paid for by a Source, at a spending share matched to the US saving rate; the earlier engine's reference values above are unchanged and still drive its settings panel. See v5.0 Release Notes.

**v4.22:** no reference value changed, and every preset's seed-42 figures are bit-identical. The page now opens with a comparison of Compassionism against five other anti-poverty designs, pre-computed by the policy testbed in `harness.js`. See v4.22 Release Notes.

**v4.21:** no reference value changed, and the seed-42 figures did not move. CCO's cost relief now reads BU in year-0 dollars, which changes only runs with inflation on (Adverse Environment, Stress Test). A 5,000-agent study confirms the headline figures. See v4.21 Release Notes.

**v4.20:** no reference value changed, but the seed-42 figures did, once: `automationRisk` is now sampled with a fixed number of draws, and its high-risk weight is 0.63 (was 0.47). See v4.20 Release Notes.

**v4.19:** the automatic stabilizers (recession BU increase, suspended expiry, emergency enrollment, COLA) are off in every preset. CCO's cost relief now scales with BU; at the $1,200 reference it is the same 20% as before.

**v4.17:** a sixth preset, **Adverse Environment**, runs these settings unchanged under recessions, 2% inflation and AI automation — the environment the Stress Test preset uses, without its weaker settings.
