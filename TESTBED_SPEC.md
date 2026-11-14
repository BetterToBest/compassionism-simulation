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
| `SURPLUS_CONSUMPTION_SHARE`, `_BASE` (row option `sc`) | 0, 'wage' / 0.9 'cash' (NR6) / 0.593 'cash' (sourced) / 0.877 'cash' (frozen) | Main result as released: 0.593 of cash surplus. Frozen model: 0.877 (`SPEND_FROZEN`, re-derived by the same method on the frozen no-programme run, MODEL_SPEC.md 13.3); 0.593 kept as a reading in study R | plan step 7 (`SPEND_SOURCED`, BEA 2025); S47 (dev/reports/s47-spend.md; run manifest Amendment 3) |
| `N7_BLEI` | false / true | Main result: true (testbed profile) | d40 |
| `PTF_MODE` | 'shipped' / 'food30' / 'food62' | Main result: 'shipped'. Others: sensitivity | D4 (session 2) |
| `PATHWAY_OFF` | flags relief, conversion, octave, octaveWage, bleiWage, pthCost, pthEquity | Main result: octaveWage off (the octave wage raise is replaced by project hiring). Others: attribution and sensitivity | d19, d46 |
| `SAVE` (savings that keep up with prices) | null / {r 0.0097, debt 'none'} | Labelled reading | v5.2 step 3 (d147) |
| `AGE` (ageing, retirement at 67, replacement) | null / {ret 'keep' / 'noconv' / 'none', ss 'average' / 'pia', earn 'flat' / 'cps'} | Labelled reading; `earn 'cps'`: wages by age (v5.3 B7) | v5.2 step 4 (decision A, d152); DECISIONS Session 39 (B7) |
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
| `BU_SCOPE` (what BU can buy; row option `bs`) | 'core' (food, housing, medical) / 'hub' (+ transport; + childcare for households) | Main result from v5.3: 'hub' (`REL_V53.bs`; Duke's answer d173, the rule recorded before the restudy). Reading: 'core' (row `core`) | DECISIONS Session 39 (B3f, B10) |
| `SPEND_GRADE` (income-graded spending; row option `sg`) | null / {eps 0.5573} (`sg: true`, or a number) | Main result from v5.3: on, in the no-programme run too (`REL_V53.sg`). Reading: off (row `nosg`) | DECISIONS Session 39 (B7, B10) |
| `FBS50` (advancement in FBS50 units; row option `fb`) | null / {dist 'lambda' / 'fbs50', scale 1} | Reading (v5.3 B7); with lambda kept and scale 1 it only reports (`FBS_KEYS`) | DECISIONS Session 39 (B7) |
| `EDC_MEASURE` (the measured EDC; row option `em`) | false / true | Reporting only (v5.3 B6): adds `EDC_KEYS`; changes no result | DECISIONS Session 39 (B6) |
| `HOUSEHOLDS` (households and children; row option `hh`) | null / {pool 'household' / 'individual', childBU 0.25 (0 to 0.5), estate 'heirs' / 'leave', shock 0 / 'shore' / a correlation in [-1, 1], wealth 'model' / 'scf'} | Main result from v5.3: {pool 'household', childBU 0.25, shock 'shore', wealth 'scf'} (`REL_V53.hh`; d167, d168, d170, d172, the rule recorded before the restudy), in the no-programme run too. Readings: adults alone (rows `adults`, `v52`), 'individual' (`indiv`), childBU 0 and 0.5 (`cb0`, `cb50`), wealth 'model' (`wmodel`), shock 0.5 (`shock50`). With ageing (row option `ag`): children's lives and estates (B4, B5; d169; rows `age`, `ageleave`, ...); `estate` is read only then | DECISIONS Session 39 (B3, B4, B10) |
| `ACCT` (the accounting check) | null / `acctNew()` | Checking only: no draw, nothing any rule reads; results are bit-identical with it on (`acctUnitSuite`). See MODEL_SPEC.md, section 11 | v5.3 B2 |
| `AUD` (the S13 audit's corrections; row option `au`) | null / {gate, sg, fbs, wOut} (`au: true` = gate, sg, fbs) | Off as released (every figure unchanged). Frozen model: on (`au: true`) in every row of the batch (MODEL_SPEC.md 13.1); `wOut` is a labelled reading in study R | S13 (dev/reports/s13-engine-audit.md) |
| `FX` (the second implementation's fixes; row option `fx`) | null / {pthb, hb, ab, sp} (`fx: true` = all four) | Off as released. Frozen model: on in every row of the batch (MODEL_SPEC.md 13.2) | S47 (dev/reports/s47-fx.md; run manifest Amendment 2) |
| `C22` (coverage and adequacy; row option `c22`) | null / {u 0, auto, idx false / 'needs'} | Off as released. The batch's headline design: `c22Design` = {auto, idx 'needs'} with the BU at `c22NeedsBU()` (MODEL_SPEC.md 13.4); `u` swept in study K | S6 (dev/reports/c22-coverage-adequacy.md); ledger D8 |
| `LVS` (the policy levers; row option `lv`) | null / {jn 'conv', tref, pr, pc, bt, keep, br, oc, ph, cap, sv, svc, rc} | Off as released (`lv: {}` moves no figure). The levers study (S54, research-update `prereg/2026-11-levers-addendum.md`) sweeps them; keys `LV_KEYS` | S54 (dev/reports/s54-levers-reading.md) |
| `PTF_ACCESS` (who may buy at PTF prices; row option `pa`) | 'members' / 'open' (`pa: 'open'`, or `{fix}` to hold every zone's PTF share of essential sales at fix; growth options `{grow, cap: 'own'\|'none', ops: 'hub'\|'outside', dem}`, defaults true, 'own', 'hub', 0.49) | Off as released and in the frozen batch ('members': every figure unchanged). Under 'open' every adult in a zone buys the zone's PTF share of the PTF sectors at PTF prices and both density tests read that share; from year 1 the share grows as far as capacity (the capital rule), operations and demand allow (part 2); needs PTF by sector (`ptfs`); keys `PA_KEYS`. S55's rows set it once preregistered | S55 (dev/DECISIONS.md S55 and S55 part 2; dev/reports/s55-ptf-access-reading.md, s55-ptf-growth.md) |

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

## 6. The frozen engine and the full study batch (S47)

The batch (research-update `prereg/run-manifest.md`) runs every row with `harness.js` `frozenRow(c)`: `au: true` (gate, sg, fbs), `fx: true` (pthb, hb, ab, sp) and `sc: 0.877`, the no-programme rows included (MODEL_SPEC.md, section 13). The headline programme row is the C2.2 design (`c22Design(c)`); the release design ($1,200, opt-in) runs beside it. What each job switches beyond that:

| Job | Switches beyond the frozen engine | Status |
|---|---|---|
| R (release panel and bridge) | the published engine (no `au`, `fx`, `sc` 0.593) and `au` alone, for none, the release design and the C2.2 design; on the frozen engine the middle backing (`aK`), every dollar backed (`a: 1`), FBS50 (`fb: {dist: 'fbs50'}`), wages following outside inflation (`au.wOut`) and the spending share at 0.593; study option `sec` | The bridge to the published figures; labelled readings |
| A, B, B10, C, D, D10, F | the preregistered rows of the study programme (scale, the 32-cell factorial with the CCO raise, ageing `ag`, participation `partRate`, the debt reading `dr`), on both designs (D and D10: the release design only) | Main study rows |
| G, G10, H, I, J | the community and zone layer (`cl`, COMM) | Reading (S37) |
| K | coverage and adequacy (`c22.u`, the status rule) | S6's rows |
| L | the cost-of-living line (`LW`: ext, bea) | S14's rows |
| M | the backing mechanism (`o.bkm`), wage indexation (`wIdx`), savings that keep up with prices (`sv`), the BU raised every year (`ci`) | S51's rows |
| N1, N2, N3, N3x | the policy levers (`o.lv`); N3x adds the outside supply shock's main path (`o.sx`) | S54's rows |
| O | the outside supply shock (`o.sx`) | S52's rows |
| P | the security outputs (`o.sec`, reporting only), `sv` | S53's rows |
| X | none (the per-year series of no programme, the C2.2 design and the release design) | Reporting |

## 7. Plain names of every row option (S68 part 2)

A study row is an object of options (`tbStudy`'s configurations). This table gives each two-letter option its plain name, its value when absent, the value in the candidate main row of round 2 (`harness.js` `r2MainRow`; MODEL_SPEC.md 14.0) and where it is described. "Absent" always means the engine as it was before the option existed (guardrail 1).

### 7.1 Row options

| Option | Plain name | Absent | Candidate main row | Described in |
|---|---|---|---|---|
| `p` | the environment's preset for this run (programme on or off, the BU, the parts) | required | `tbPresets(P).baseline()` / the C2.2 design's preset | MODEL_SPEC 10, 13.4 |
| `o` | the row's own study options (financing and the like; section 7.2) | the study's | `{fin: 'source', a: 0}` (programme run) | section 2 |
| `cm` | the conversion model | 'engine' | 'framework' | section 1 |
| `pj`, `es`, `sp`, `pd`, `jn`, `cs`, `oc` | project hiring; ESP payroll; the surplus split; the production side; open enrolment; the PTF discount from forgone profit; the octave gap | off | as the release row | section 1; MODEL_SPEC 6 |
| `ml` | the spending layer (`nt`: idle labour in normal years) | off | recession years only (as released) | section 1; MODEL_SPEC 6.12 |
| `gc` | the BLEI gate reads this year's BU | false | true | section 1 |
| `pw` | parts of the pathway switched off (attribution) | none | the octave wage raise off | section 1 |
| `g` | engine settings for this row (the accounting profile) | the testbed profile | as the release row | section 1 |
| `sc` | the share of the cash surplus consumed | 0 | 0.877 (frozen) | MODEL_SPEC 13.3 |
| `sg` | income-graded spending | off | on | MODEL_SPEC 6.4 |
| `hh` | households and children | adults alone | `REL_V53.hh` | MODEL_SPEC 6.13 |
| `bs` | what BU can buy | 'core' | 'hub' | section 1 |
| `fb` | advancement in FBS50 units | off | off | section 1 |
| `em` | the measured EDC (reporting) | off | on | section 1 |
| `v54` | the v5.4 parts: job loss, PTH's books, PTF by sector, risk measures | off | `V54_MAIN` | MODEL_SPEC 12 |
| `sn` | today's safety net (`abawd` SNAP's work rule, `slope` the phase-out) | off | `{abawd: true, slope: true}` | MODEL_SPEC 12.4 |
| `lt` | US-data readings (`s` wage spread, `m` wage median: 'all' = CPS earnings) | off | `{s: 'all', m: 'all'}` | section 1 |
| `sv` | savings that keep up with prices | off | off | section 1 |
| `ag` | ageing, retirement at 67, replacement | off | off | section 1 |
| `hc`, `rv` | landlords capture BU spent on rent; unearned high rates in the review | off | off | section 1 |
| `hl`, `pv` | health coverage; the prevention link | off | off | section 1 |
| `lw` | the cost-of-living line (S14) | the MIT line | the MIT line | section 6 (job L) |
| `cl` | the community and zone layer | off | off | section 6 (jobs G-J) |
| `au` | the outside audit's corrections (gate, sg, fbs; `wOut`) | off | `true` (frozen) | MODEL_SPEC 13.1 |
| `fx` | the second implementation's fixes, and parts added since | off | `{pthb, hb, ab, sp, fin: 'report', pe: true}` | MODEL_SPEC 13.2, 14.10; section 7.3 |
| `c22` | coverage and adequacy (the C2.2 design) | off | `{auto: true, idx: 'needs'}` (programme run) | MODEL_SPEC 13.4 |
| `lv` | the policy levers | off | off | section 1 |
| `pa` | open PTF access and the growth of the PTF share of sales | members only | 'open' | MODEL_SPEC 14.1 |
| `po` | PTF running costs, who pays, PTF workers, the density tests' curve | off | `true` | MODEL_SPEC 14.2 |
| `pr` | the capacity price rule (options `q`, `bv`, `bd`) | today's rule | today's rule (absent) | MODEL_SPEC 14.3 |
| `lf` | adults outside the labour force (`conv` 'keep' or 'none') | everyone in it | `{}` ('keep') | MODEL_SPEC 14.4 |
| `dr` | borrowing for ordinary spending (`lim` the limit, `liq` the liquid share, `fl` the floor) | off | `{lim: 2500}` | MODEL_SPEC 14.5 |
| `rt` | wealth held by asset class (options below) | all wealth is cash | `{bo: true, ci: true, ng: 'base', cr: true}` | MODEL_SPEC 14.6, 14.7 |
| `wt` | the weighted top tail | off | `true` | MODEL_SPEC 14.8 |
| `bg` | bargaining: the outside option and the markdown | off | `{pi: 0, m: 1/1.21}` (identical to off) | MODEL_SPEC 14.9 |

### 7.2 Study options added in round 2 (and `o.wy`, which may also sit on a row)

| Option | Plain name | Absent | Candidate main row | Described in |
|---|---|---|---|---|
| `dm` | distribution measures | off | on | MODEL_SPEC 14.11 |
| `mf` | the money-flow table | off | on | MODEL_SPEC 14.11 |
| `wtm` | the tail's weighted measures | off | on | MODEL_SPEC 14.8 |
| `wy` | costs at the within-year price level | off | on (equal to the published measures under today's rule) | MODEL_SPEC 13.2a |
| `fin` | how the programme is paid for ('tax', 'source', 'money', 'hybrid', 'none') | 'tax' at study level | 'source' (programme run) | section 2; MODEL_SPEC 11 |

### 7.3 Parts and sub-options

| Option | Plain name | Values (absent first) | Candidate main row |
|---|---|---|---|
| `fx.pthb`, `fx.hb`, `fx.ab`, `fx.sp` | PTH's books after households; the PTH home's price and receipt; SNAP's month count; the essentials' supply path | false / true | true |
| `fx.fin` | who pays the part a capped contribution does not raise | none / 'report' / 'money' ('debt' refused until S72) | 'report' |
| `fx.pe` | the PTH trust's books when a member dies (with ageing) | false / true | true (moves nothing without ageing) |
| `pa.fix`, `pa.grow`, `pa.cap`, `pa.ops`, `pa.dem` | a fixed share; growth on; capacity from owned capital or none; operations at the Hub's prices or outside costs; the demand ceiling | null, true, 'own', 'hub', 0.49 | the defaults |
| `po.cost`, `po.pay`, `po.res`, `po.bonus`, `po.curve`, `po.w`, `po.test`, `po.hire` | running costs ('full', 'sector', 'hub'); who pays ('source', 'price'); the reserve; the bonus ('workers', 'members'); the curve ('smooth', 'step'); the band's half-width; what the tests read ('sales', 'members', 'capacity'); a hiring limit | `PO_DEFAULTS` | the defaults |
| `pr.k`, `pr.k2`, `pr.r`, `pr.a`, `pr.h`, `pr.rs`, `pr.um` | κ, κ₂, ρ, α, normal-years slack, recession slack, the stretch cap (reporting) | `PR_DEFAULTS` | (rule off) |
| `pr.q`, `pr.bv`, `pr.bd` | sub-steps within the year; the velocity response; the velocity drift | 1, 0, 0 | (rule off) |
| `rt.ix`, `rt.phi`, `rt.psi`, `rt.chi`, `rt.rho` | real assets' indexation; nominal assets' share of inflation; floating debt's; fixed-rate debt's (0 debt relief, 1 none); real gains by class | 1, 0.46, 1, 0, Shiller's | the defaults |
| `rt.ns`, `rt.all`, `rt.ng`, `rt.rg` | where saving goes ('nom', 'port'); all wealth in one class ('nom', 'real'); the nominal rate by group ('base', 'all'); higher top real-estate returns | 'nom', null, false, false | `ng: 'base'` |
| `rt.bo`, `rt.ci` | business owners; the income wealth pays | false, false | true, true |
| `rt.cr` (`inc`, `pop`, `out`, `w`) | the creditor side: who bears the loss ('pass', 'hold', 'hedge'); the model as all households; nothing outside; weights read | false; 'pass', 0, 0, 1 | true (the defaults) |
| `wt.m`, `wt.form`, `wt.cut`, `wt.a`, `wt.flat` | tail households per type; Pareto or generalised Pareto; the cutoff ('main', 'p99', 'p90'); the exponent; no tail (weights 1) | 3, 'pareto', 'main', fitted, false | the defaults |
| `bg.pi`, `bg.m` | the pass-through; the markdown | 0, 1/1.21 | the defaults |
| `lf.conv` | conversion outside the labour force | 'keep' / 'none' | 'keep' |
| `dr.lim`, `dr.liq`, `dr.fl` | the borrowing limit (year-0 $); the liquid share of savings; the floor ('fpl') | 0, 1, none | 2500, 1, none |
