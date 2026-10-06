# Testbed specification: every switch and alternative mechanism

The release model ([MODEL_SPEC.md](MODEL_SPEC.md)) is one setting of a larger testbed in `harness.js`. This file lists every switch and alternative mechanism the testbed carries, its **status**, and the decision that set it. The rule since v5.0: every new mechanism sits behind a switch; with the switch off, output is bit-identical to before (proved by full-output diffs and the panel hashes); a new mechanism first appears as a **labelled reading** beside the main result, and joining the main result is a separate, recorded decision after a 500-seed restudy.

**Status words.** *Main result*: on in the release row. *Labelled reading*: a row of the published 500-seed panel, shown beside the main result on the pages, never mixed into it. *Sensitivity*: available in the testbed and used in a study or a report, not on the pages. *Earlier engine only*: part of the v4.22 engine on `earlier-engine.html`, not used by the release engine. *Reporting only*: draws nothing and changes no adult. *Retired*: kept only so an old figure can be reproduced.

Decisions: "d" numbers are the project ledger's (exported in `dev/background/ledger-export.md`); other entries name the section of `dev/DECISIONS.md`.

## 1. Engine switches (global settings in harness.js)

| Switch | Values (default first) | Status | Decision |
|---|---|---|---|
| `CONVERSION_MODEL` | `'engine'` (the v4.22 page's rule) / `'framework'` (the Hub's description: one BU budget, BU buy essentials, businesses convert, expired BU fund projects) | Main result: `'framework'` | N1-N4 (session 2); release gate |
| `PROJ` (project hiring paid in expired BU) | null / object (`PROJ_DEFAULTS`) | Main result: on | d58-d66 (session 15) |
| `ESP` (ESP payroll in expired BU at workers' own rates) | null / object (`ESP_DEFAULTS`: lam 0.20, work 0.230, take 'par', cap 'dollars', rest 'all') | Main result: on | d70-d76 (session 19) |
| `SURP` (the ESP surplus split) | null / object; `priv` 'owners' / 'same' / 'prices' | Main result: on, priv 'prices' | d97-d106 (plan step 1); d140 (private ESPs pass the premium to BU customers) |
| `PROD` (production side: PTF capacity, matched output) | null / object; `match` 'face' / 'own' / 'market'; `speed` 'reinvest' / 'oneyear' | Main result: match 'market', speed 'oneyear'. Readings: 'face' (row `cost`), 'reinvest' (row `cap5`) | plan step 2; d137-d139 |
| `JOIN` (open enrolment) | null / {cost 'revealed' / 'nominal' / 'none', stay 2} | Main result: 'revealed'. Reading: 'none' (row `all`) | plan step 4 |
| `COST` (PTF discount funded from forgone profit) | null / {food 0.0494, util 0.0260} | Main result: on | plan step 5 |
| `OCT` (at most one octave per N years) | null / {gap 3} | Sensitivity | plan step 6 (the Hub's rule kept) |
| `MULT` (the spending layer) | null / {m 1.5}; `nt` {m, s} for normal years | Main result: recession years only. Readings: `nt` (rows `slack`, `slacku6`) | plan step 16; v5.2 step 6 (decision B) |
| `GATE_CURRENT` (BLEI gate reads this year's BU) | false / true | Main result: true | audit V5-02 (v5.1) |
| `LABOR` (labour supply response) | null / `LABOR_DEFAULTS` (rho 0.16, rhoBU 0.16, rhoR 0, eps 0.33, delta 0) | Main result: on (central values) | d14, d15, d2 (session 4); fairness rule |
| `PRICE` (the price module: created money and essentials prices) | testbed state; options in `PM_DEFAULTS` | Main result: on, a = 0 | sessions 2-3 (d22-d24); D2 lines deflated |
| `THETA_GATE` | 'szh' / 'density' | Main result: 'density' (NR6 profile) | d12 (session 5) |
| `PTH_MODE` | 'basket' / 'housing' | Main result: 'housing' | d4 (session 5) |
| `DISC_BASE` | 'basket' / 'pretax' | Main result: 'pretax' | d5 (session 5) |
| `SURPLUS_CONSUMPTION_SHARE`, `_BASE` | 0, 'wage' / 0.9 'cash' (NR6) / 0.593 'cash' (sourced) | Main result: 0.593 of cash surplus | plan step 7 (`SPEND_SOURCED`, BEA 2025) |
| `N7_BLEI` | false / true | Main result: true (testbed profile) | d40 |
| `PTF_MODE` | 'shipped' / 'food30' / 'food62' | Main result: 'shipped'. Others: sensitivity | D4 (session 2) |
| `PATHWAY_OFF` | flags relief, conversion, octave, octaveWage, bleiWage, pthCost, pthEquity | Main result: octaveWage off (the octave wage raise is replaced by project hiring). Others: attribution and sensitivity | d19, d46 |
| `SAVE` (savings that keep up with prices) | null / {r 0.0097, debt 'none'} | Labelled reading | v5.2 step 3 (d147) |
| `AGE` (ageing, retirement at 67, replacement) | null / {ret 'keep' / 'noconv' / 'none', ss 'average' / 'pia'} | Labelled reading | v5.2 step 4 (decision A, d152) |
| `LATENT` (US-data readings: wealth, risk, wage spread, wage median) | null / {wealth, risk, wsd, wmed} | Labelled reading | v5.2 step 5 |
| `HCAP` (landlords capture BU spent on rent) | null / {c, all} | Labelled reading | v5.2 step 7 (decision C) |
| `REVIEW` (unearned high rates in the Collectives' review) | null / {u, q} | Labelled reading | v5.2 step 7 (decision C) |
| `FBS_BU_ONCE` | false / true | Sensitivity (i3-1) | session 7 |
| `PTH_APPR_CONSERVE` (PTH appreciation that conserves wealth: the cash part of the appreciation leaves the Acre Equity) | false / true | v5.3 correction: true in every v5.3 row (the accounting check, B2, found the cash part counted twice); false reproduces v5.2 | v4.16; Muse audit; DECISIONS Session 39 |
| `SURP_CUT_MARKUP` (the split's price cut sized on the rent after the landlords' mark-up) | false / true | v5.3 correction: true in every v5.3 row (B2 found the cut handed out more than the pool in the rent mark-up readings); changes nothing without `HCAP`; false reproduces v5.2 | DECISIONS Session 39 |
| `AUTOMATION_SAMPLER_LEGACY` | false / true | Retired (reproduces v4.19 in `validate`) | v4.20 |
| `RELIEF_PRICE_LEGACY` | false / true | Retired (reproduces v4.20 in `validate`) | v4.21 |
| `CCO_RELIEF_FLAT`, `BU_ALLOCATIONS_PER_YEAR` | false, 1 | Earlier engine only (stabiliser studies) | v4.19 |
| `LEDGER`, `REP_HOOK` | null | Reporting only | A1; v5.2 |
| `ACCT` (the accounting check) | null / `acctNew()` | Checking only: no draw, nothing any rule reads; results are bit-identical with it on (`acctUnitSuite`). See MODEL_SPEC.md, section 11 | v5.3 B2 |

## 2. Testbed options (per study or per row)

| Option | Values (default first) | Status | Decision |
|---|---|---|---|
| `fin` (financing) | 'tax' (a flat contribution on wages) / 'source' / 'money' / 'hybrid' / 'none' | Main result: 'source'. Readings: 'tax' (row `tax`); with `taxBase` 'prog' (row `progtax`) and 'land' (row `landtax`) | plan step 3; v5.2 step 7 |
| `a` (share of the Source's payout backed by new output) | 0 / 0 to 1 | Main result: 0 (cautious). Readings: 1 (H1, row `h1`); the backing-share sweep (0, 0.25, 0.5, 0.75, 1) | plan step 3; audit E2 (v5.1) |
| `aK` (output backs the payout up to a share of earned income) | 0 / 0.08, 0.12, 0.16 | Labelled readings (rows `midlo`, `mid`, `midhi`) | v5.2 step 6 (decision B) |
| `faceM` (essentials bought with BU counted as backed) | false / true | Labelled reading (row `face`) | plan step 18 |
| `eP` (price cuts counted as capacity, not a transfer) | 0 / 1 | Labelled reading (row `free`) | d24 |
| `noDamp` (PTF/PTH inflation damping off) and the octave wage raise | damping off, raise off / both on | Main result: off. Reading: both on (row `standins`, theoretical) | d86, d46 |
| `ci` (BU indexed every year instead of only above 5%) | off / on | Labelled readings (rows `idx`, `h1idx`, `h1both`) | v5.2 step 3 (d147) |
| `gift` | paid as you go / 'run' | Main result: as you go. Reading: row `giftrun` | d66, d67 |
| `lines` | 'deflate' / 'nominal' | Main result: 'deflate'. Fixed-dollar lines reported beside it | D2; v5.2 step 2 |
| `rep52`, `giniNN1` | off / on | Reporting only; on in the v5.2 panels | v5.2 step 2 (d148, d149) |
| `lamG`, `theta`, `ptfCap`, `pgOnE`, `supply`, `gS`, `aw`, `wIdx` | `PM_DEFAULTS`; `wIdx` 1 in the testbed | Main result: the defaults. Sweeps: sensitivity | sessions 2-3 |
| `years` | 20 / 40 | Both published (20 and 40) | session 33 |

## 3. The published rows (release panel, 500 seeds, three environments, 20 and 40 years)

Main result: `release`. Paired no-programme runs: the no-programme row and, for readings that change something in both runs, `bases` (`sv`, `sv0`, `ag`, `agpia`, `ltw`, `ltr`, `lts`, `ltm`, `lta`).

| Row | Status | What it changes |
|---|---|---|
| `release` | Main result | Compassionism with every mechanism, paid for by the Source, nothing backed (a = 0) |
| `v422` | Labelled reading (history) | The v4.22 main row (wage contribution) |
| `h1` | Labelled reading | Every Source dollar backed by new output |
| `face`, `tax`, `cost`, `cap5`, `s30`, `all`, `free`, `standins` | Labelled readings | As in section 2 and the rows' labels on the explorer |
| `sav`, `sav0`, `idx`, `h1idx`, `h1both` | Labelled readings | Savings that keep up with prices; the BU indexed every year |
| `age`, `agenc`, `agenone`, `agepia` | Labelled readings | Ageing and retirement |
| `fixw`, `fixr`, `fixs`, `fixm`, `fixall` | Labelled readings | Closer to US data |
| `mid`, `midlo`, `midhi`, `slack`, `slacku6` | Labelled readings | Middle backing; idle labour in normal years |
| `hcap`, `hcaphi`, `rev5`, `rev10`, `rev20`, `rev20n`, `giftrun`, `progtax`, `landtax` | Labelled readings | Robustness |

No reading has joined the main result (v5.2 step 9: each new mechanism first appears beside it).

## 4. Comparators (not published)

`tbPresets` also builds other designs on the same simulated people, for the compare page (planned after v5.4): a universal basic income (`ubi`), a negative income tax (`nit`), a public grocery network (`groc`, `grocPilot`), an asset endowment (`endow`), X-Cents (`xc`, `xcFull`) and Compassionism with a needs-based top-up (`ccoTop`). They share one cost ledger, one income effect per unconditional dollar and one wage elasticity (the fairness rule). Status: sensitivity (the drafts are in `dev/drafts/`).

## 5. Random streams

Every reading that needs random numbers has its own stream (MODEL_SPEC.md, section 8); `matrixUnitSuite` checks that the main stream's 8 draws per adult-year are untouched, that only ageing rows use the ageing stream and only review rows the review stream, and that no switch leaks from one row into the next.
