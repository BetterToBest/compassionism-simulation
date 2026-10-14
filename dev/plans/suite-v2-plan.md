# Visual suite page, second pass: plan

Oct 14, 2026. For the next session to read after `HANDOFF.md`. Scope: `suite.html` and the data behind it. The page launched with three of the BLEI paper's six measures not computed; this plan says what it would take to compute each, what else the page leaves out, how to make every card clear, and the separate go-live step (link it from the findings explorer, remove `noindex`, change the domtest check).

Labels used below: **[Correction]** something on the page is wrong or contradicts itself; **[Addition]** new content the goal needs; **[Polish]** optional. Items marked **[Verify]** rest on my reading of a source and must be checked before anything is printed.

## 0. The goal, and one rule

Goal of the page: show what the usual measures (a poverty line, median income, Gini, GDP) do not show when economic systems are compared, Compassionism being the case at hand. The page should leave a reader able to say, for each measure, one of three things: *here is the number*, *here is the number measured differently from the paper, and why*, or *the model cannot say, and this is what it would need*.

The rule for every edit: **a reader who sees one card must understand it without reading another section.** Define each term at first use, give the question in plain words, then the number, then how it was computed, then what it does not show.

## 1. Timing (read first)

`HANDOFF.md` says Claude Code's Pro plan ends Thursday (Oct 15) and the Runpod results token expires 2026-10-17 04:16 UTC. The ledger adds that Thursday morning is the last safe session (the cut-off time is not published) and that a pod can only be launched while Claude Code is available. Every page change needs Node for `validate`, `unit`, `domtest`, `check_figures.js` and `no_figure_change.py`. **Today's session launches the study; Thursday morning ingests its results and updates the page** (`dev/plans/next-study-plan.md`, sections 0, 6 and 7).

**Split the work by whether it needs new numbers, because most of it does not.**
- **Stage 1, no new run:** everything that reads data the release already carries: the corrections (section 2), the card layout and status badges (5.1), IPBI's public-cost items (3.4), the cost-side tie-in (section 4, item 3), the persistence view from the release's spell series (section 4, item 1, first part), the wording audit (5.3). Do this first; it needs no Runpod.
- **Stage 2, the next study:** the fields the last export did not carry (EPPM's per-person parts, FBS for non-participants, Acre Equity days, six-tier transitions, 3.1 to 3.3 and section 4 item 1 second part), and more. Duke has chosen a dedicated study; its scope, tiers, run design and audit gate are in **`dev/plans/next-study-plan.md`**. Prove the fields on a two-seed dry run first. If the study has not run when Stage 1 is ready, the page ships Stage 1 and says which measures are waiting on it.

Part B (go-live) is small and waits for Duke's approval; it must not be done in the same pull request as Part A.

## 2. Corrections found on the live page

Found by reading `suite.html` (lines near `function indices` and `function limits`) and `dev/reports/v5-33-visual-suite.md`.

- **C1 [Correction] EPPM is described two incompatible ways.** The measures table says EPPM's parts "are in the model", while the paragraph under it says EPPM describes gains "the model has no way to produce or measure", and the limits list groups it with the crime and health channels. Only IPBI fits that description. Fix in the wording described in section 3, not by editing the sentences in isolation.
- **C2 [Correction] "so there is no figure to compare" (FBS).** The paper itself compares FBS across arms (its baseline example is $0 against $2,281). FBS is a formula on income, cost and drain; it can be computed for every adult in both arms (the allowance is simply zero without the program). See 3.2.
- **C3 [Correction, verify] the price sentence.** The report says that in the main reading "prices rise 50.8% a year faster than without the program". A price level rising 50.8% a year faster would be hyperinflation, so this probably means a price level 50.8% higher after 20 years, or a different quantity. Grep `suite.html` for the sentence, trace it to its data path, and state the quantity exactly (what is measured, over what period, in which reading). This sentence carries the page's main warning about savings losing their worth, so it must be exact. Supporting hint: the release's panel rows carry `infl` (50.3 in one Reference row) beside `pLevEnd`, which reads like the cumulative price-level rise by the end of the run, not an annual rate; confirm in `harness.js` before rewording.
- **C4 [Correction] "Flourishing" for both arms.** The page already says this in its limits. Keep, but also say it where the tier names are first shown (the ladder section), since a reader of the ladder alone will not see the limits.

## 3. The measures not computed: what it would take

What the last export (the one behind `suite-20.json` and `suite-40.json`) already carries, by series name: the BLEI ladder, its three parts in days, `medInc`/`meanInc`/`meanBu` (in days of basic living, not dollars), `relPov`, the shares below 30 days on both readings, and per-arm `edcM` and `fbsAbove` in the release panels. It does **not** carry, in anything I could find: per-person dollars of income, allowance spent, rent, interest or fees; the adult's own basket price index; Acre Equity; FBS for adults outside the program; or six-tier transitions. That is why 3.1 to 3.3 need new fields. They are small, but the data cannot be rebuilt from the series above without guessing. No engine change is expected for any of them. Each is a **reporting-only** addition to `dev/tools/explore_export.js --suite` (see `suiteYear`) reading quantities the engine already keeps. If a quantity turns out not to be exposed, add an accessor behind a switch, prove switch-off is bit-identical (`guard_test.js`, `engine_lineage.js prove`), and say so in the report. Pair the rows by latent adult: the same 500 latent adults are instantiated into every row (MODEL_SPEC, construction stream), so a person's "with" and "without" can be matched inside one seed's loop.

### 3.1 EPPM (Effective Purchasing Power Multiplier): doable

**What the paper means.** [Verify against the paper's section on Index III before printing any paper number; my reading came through a summary.] EPPM = [Y + BU·ε_blended − EDC_CCO·Y] / [Y·(1 − EDC_baseline)], with BU·ε_blended = $2,502 (food 360 × $2.75 plus utility 840 × $1.80); worked examples 5.80× and 2.79× for two near-poverty profiles. The idea: how far one person's money goes with the program against the same income without it.

**Why not just apply the paper's formula.** It values the allowance at 2.085 times face value through ε. The simulation values one BU at $1 and applies community price cuts separately (MODEL_SPEC 6.3 and 6.4: PTF members' basket cut 12% + 4% × coherence; PTH housing cut 35%). The paper itself lists "BU·ε double-counting" and "BU face-value misvaluation" among five errors it corrects. Applying ε on top of the model's price cuts would reintroduce the first. Also, the paper's examples are near-poverty households with baseline EDC 0.625, whereas the model's population-wide EDC with no program is 26.0% (Reference, 20 years; 15.9% with Compassionism). A population EPPM from the model will therefore be **well below the paper's worked examples**, and that is a finding about the example's assumptions, not a defect. Show it by income group so the comparable group (the poorest fifth, near-poverty) is visible. I have not computed any of this; the size of the gap is unknown until the export runs.

**Proposed definition, in the model's own terms** (a decision for the session; record it in `dev/DECISIONS.md` with alternatives):

For each adult-year, with the adult's no-program twin (same latent adult, same seed):

- real resources = (cash income + allowance spent + other transfers − rent − interest − fees) ÷ the adult's own basket price index relative to year 0
- EPPM = real resources with the program ÷ real resources of the twin without it.

Show it as **three parts that multiply or add to the whole**, because the parts are what current metrics cannot show:

1. **The allowance** (the transfer, counted at face value, as the paper's partition rule requires).
2. **Lower rent and interest** (the drain; this is the EDC card's mechanism).
3. **Prices**: community discounts, **net of the program's effect on the general price level**. Report this part separately and plainly; if the program raises prices for everyone, EPPM at "the participant's own prices" overstates what money buys. Show both "at community prices" and "after general price changes".

Choose an exact decomposition (log shares, or sequential substitution) and say which in the card.

Design points to settle and record:
- **Statistic.** Ratio of group totals, or median of person ratios. Person ratios blow up when the twin's net resources are near zero; set and state a floor or use group totals. Show the share of participants with EPPM above 1.
- **Who.** All participants; the poorest fifth of participants measured by the twin's no-program income; non-participants (whose EPPM is only the price effect, and may be below 1; this is the cost side, show it, consistent with the "who takes part" section).
- **Selection.** The twin construction compares a person with themselves, so the usual self-selection warning does not apply to EPPM the way it does to the participant versus non-participant medians. Say so in one line, and say that general-equilibrium effects (prices, wages) are included.
- **Self-check in the export:** the parts must reproduce the whole, and the group's mean no-program real resources must equal the no-program run's own series.

### 3.2 FBS (Financial Bandwidth Score): extend to both arms **[Correction + Addition]**

Today the page reports only the share of participant-years at or above the level where the chance of advancing is even. Add, for **all adults in both arms**: the median monthly surplus above basic living ($, today's prices), and the share with a surplus of zero. Use the model's own basket and drain, not the paper's $1,950 and 0.12; say that the model's cost basket (MIT living-wage) differs from the paper's.

Keep the advancement reading but state its limits where it appears: the paper's own λ range saturates (89.8% to 100% chance at $2,281), so the model uses a separate provisional range that is not empirically validated (MODEL_SPEC 6.8: FBS gates yearly advancement through λ' = λ × (1 + 0.20 × cipDemo)). A reader seeing "even odds of advancing" should know the chance is a model rule, not an observed rate.

### 3.3 CSI (Compound Stability Index): answer it by simulation, add Acre Equity **[Addition]**

The paper's CSI is a closed-form projection: BLEI(0) × (1 + r_wealth/12)^t × (1 − EDC) + AE(t) ÷ C_basic, with AE accumulating from $600 a month at 4% (range 2% to 7%) and constant growth rates. The paper gives no worked CSI number, so there is nothing to benchmark against. The model simulates the years, which is a stronger answer to the same question; the current card says so, and that is correct. What is missing is the part of the paper's idea the ladder leaves out: **Acre Equity**.

The engine keeps `acreEquity` apart from `wealth` for community-housing (PTH) members, with a tenure-based liquid share (grep `pthLiquidShare`, `acreEquity` in `index.html`). The BLEI numerator uses `0.20 × max(0, wealth)`, so Acre Equity is not in the ladder. So:

- Add a layer to "What the days are made of": **Acre Equity in days of basic living**, labelled as *not accessible now*, for PTH members, and the median and mean for all adults.
- Add a "ladder including Acre Equity" reading (BLEI days + equity days) next to the main ladder, or at least the share at or above 730 days with and without it. Label it **"CSI, simulated reading"** and **"Claude's reading of the design"** (CLAUDE.md rule); say that the paper's closed form is not used and why.
- **[Verify]** that Acre Equity is not also counted inside `wealth` before adding the layer (the tenure-cohort accounting around `a._acE0`/`acctChk` exists to keep this straight). If it is double-counted anywhere, that is a finding for the report, not something to patch quietly.
- Do not copy the paper's `(1 − EDC)` factor onto a stock without checking what it means; if it is not reproduced, say so.

### 3.4 IPBI (Indirect Participant Benefit Index): partly computed already; use what exists

**Correction to an earlier draft of this plan:** it said the model has no crime or health channels. That was wrong. The release carries **public costs avoided** (index.html section `#cost`, tiles rendered by `site/simpage.js` near line 231, computed in `harness.js` near lines 4788 to 4811, constants in `AVOID_HOMELESS` and `AVOID_WIDE`, each "from a published causal estimate"):

- homelessness: fewer unhoused person-years per 1,000 adults, and the shelter, health-care and justice costs saved (`unhousedAvoided`, `avoidLo`, `avoidHi`);
- prisons (`avoidJail`) and hospital and psychiatric stays (`avoidHealth`), from the change in the poverty gap; `avoidW` is the main reading of the sum and `avoidWHi` the largest published prison effect applied to everyone; emergency use is in the high reading only.

All are per adult per year, today's dollars, already in `data/releases/v5.6.json` for every environment and horizon. No run is needed to show them.

**What they are and are not.** The paper's IPBI sums five channels: crime reduction (CR, $3,500 to $9,000), public health (PH, $800 to $2,400), labor productivity (LP, $4,000 to $12,000), property values (PV, $13,000 to $32,500) and market expansion (ME, $1,500 to $4,000), a total of $22,800 to $59,900 a year per $200,000 non-participant household, with no weights and no causal identification claimed; the paper prefers the lower bound because CR and PV overlap (10% to 20% overstatement). [Verify all against the paper.] The model's avoided costs are **public-budget savings per adult across the whole population**, not dollars gained by non-participant households. They correspond to the public-cost side of CR and PH, not to the whole of either channel (for example, losses to crime victims are not counted), and they are not specific to non-participants. So:

| IPBI channel | In the model today | Page treatment |
|---|---|---|
| CR crime reduction | public cost of prison avoided (`avoidJail`); victims' losses not counted | show the avoided cost, label it "public cost only" |
| PH public health | hospital and psychiatric stays avoided (`avoidHealth`); homelessness-related health cost inside `avoidLo`/`avoidHi` | show, labelled the same way |
| ME market expansion | none (MODEL_SPEC has a recession multiplier only, no demand multiplier on non-participants' income) | "Not modelled"; needs a sourced demand multiplier, first in order |
| LP labor productivity | none for non-participants (no employers) | "Not modelled" |
| PV property values | none (no neighbourhoods) | "Not modelled"; needs a housing market and an expert |

**Page treatment for this update (no run):**
1. IPBI card status: **Partly modelled**. Add this fourth badge to the set in 5.1.
2. Show the avoided-cost items through the **same data paths the cost section uses** (one source of truth; `check_figures.js` already checks them for `index.html` and the findings explorer), beside the cost per adult, in the same environment, horizon and reading the reader chose. Say plainly what the page's existing code already says: each is from a published estimate, child welfare is not counted, and together they are a small share of the program's cost when that is true (the cost section has this test, `var small = ...`; reuse it, do not retype it).
3. Do **not** sum these with the paper's ranges and do **not** convert them into the paper's per-household figures. If Duke wants the paper's ranges shown, label them "the paper's estimate, not tested by this model, no causal claim" and keep them apart.
4. Keep the existing "direct effect on adults who do not take part" (prices, wages, safety net) as its own line; it is a different thing from IPBI.
5. Decide, and record, whether the avoided costs also belong on the findings explorer's page for this release (`findings?v=5.6`); they are already on the main page's cost section, so the suite should link to or reuse, not copy.

## 4. What the page still leaves out

Ranked by how much each matters to the goal (what current metrics miss when systems are compared).

1. **[Addition] How individuals move, not only how shares change.** (Stage 1 for the spell and re-entry figures already in the release; Stage 2 only for the six-tier transitions.) The ladder shows each year's shares; two very different worlds can show the same shares (people churning through Crisis versus a fixed group stuck there). The page says it "follows the same simulated adults", but it never shows them moving. Add: where adults who start in Crisis are 5 and 10 years later (tier-to-tier transition table), years spent in Crisis per adult, and how often people fall back after leaving. **Data:** the release already carries poverty spells and the v5.4 risk measures (savings fall, income recovery, re-entry); `lives-*.json` has per-person flags (below 30 days, below cost of living, too little wealth, taking part) for one seed's adults. Six-tier transitions need a per-adult tier export added to `--suite`. Check what the release already has before adding series.
2. **[Addition] EDC-adjusted wealth Gini.** The paper's sharpest contrast with the Gini is wealth net of drain (W_net = W_nominal − EDC × Y × 12). The release carries many Gini series; I did not find this one under an obvious name. Check whether the model computes it; if not, it is a reporting-only addition and belongs beside EDC.
3. **[Addition] The cost side.** The page shows outcomes with no price tag, while the main page's cost section (`#cost`) already shows cost per adult, who pays, and the public costs avoided. Reuse those data paths (see 3.4) rather than copying figures: one line per environment (cost per adult-year, the avoided public costs beside it), and a link to the cost section, so the suite cannot be read as outcomes without cost.
4. **[Addition, structural] Build the page so other systems can be added later.** Today the series are keyed to the two arms (`base`, `release`) plus backing readings. The comparison page comes later; if the measure code and the data schema are keyed by arm, any design under identical accounting can be added without rewriting the cards. State this requirement in the report; do not build the comparison now.
5. **[Addition] Say who is not on the ladder.** The ladder is adults only; households and children are in the model (a child allowance, pooled household money) but not shown. One line in the limits.
6. **[Polish] Jargon at first use** (see 5.3).

Already covered and not gaps: the program's two arms side by side, the three environments, 20 and 40 years, the backing assumption, four poverty lines, what the days are made of, participants versus non-participants, the spread across runs.

## 5. Making the page clear

### 5.1 One anatomy for every measure card
1. **The question**, in plain words, one sentence.
2. **The answer**: the number for no program and for Compassionism (both from the data; nothing typed in).
3. **How it is computed here**: one or two sentences.
4. **How it differs from the paper** (only if it does), one sentence, with the reason.
5. **What it does not show**: one sentence.
6. **A status badge** from a fixed set, so the reader can scan all six at a glance: **Measured** · **Measured differently from the paper** · **Partly modelled** · **Not modelled**. For "Partly modelled" and "Not modelled", add **what it would need** in one sentence (from section 3), never "a possible next measure".

Replace the "–" cells and the table's "No program / Compassionism" columns with this card layout; keep the CSV and JSON downloads (domtest Phase 15 checks the tables have them).

### 5.2 Proposed card status after this update (for the session to adapt)
- BLEI: Measured. EDC: Measured.
- EPPM: Measured differently from the paper (3.1).
- FBS: Measured differently from the paper (3.2); both arms.
- CSI: Measured differently from the paper: simulated years, with Acre Equity added (3.3).
- IPBI: Partly modelled: public costs avoided (prison, hospital and psychiatric, homelessness) shown from existing data, labelled "public cost only"; market expansion, productivity and property values "not modelled", each with what it would need (3.4).

### 5.3 Wording checklist (audit the page against it; fix by definition at first use)
BLEI and its six tier names; "days of basic living"; "backing reading (main, middle, every dollar backed)", which needs one plain sentence on what is being backed and by what; the three environments (Reference, Adverse, Stress Test); "same-rules reading" versus "the paper's reading" (the data and reports once called it "design-neutral"; use one name everywhere, as the page's header, the report and `explore_export.js` must agree); "Source", "allowance", "Basic Unit"; "participant" and "non-participant"; "Compassionism" versus the model's version of it. Every percentage should say of what (adults, person-years, runs).

## 6. Build order (Part A: one pull request, the page update)

1. Read `HANDOFF.md`, then this plan. Grep for the sentences named in section 2 before changing anything.
2. Extend `explore_export.js --suite` (reporting only) for: EPPM parts, FBS in both arms, Acre Equity days, tier transitions and per-adult time in Crisis, and the EDC-adjusted Gini if it is not already present. Add self-checks (parts sum to whole, new series agree with the run's own totals, the existing `bO` self-check still passes).
3. **Stage 2 only:** run the study defined in `dev/plans/next-study-plan.md` (two-seed dry run first, then the 500-seed job on Runpod in resumable pieces; record the exact commands and commit in each file's `_meta.commands`). Start the job, check once that it started, end the session (CLAUDE.md). Ship Stage 1 without waiting for it.
4. `python3 dev/tools/release_data.py` to copy the new series into `data/releases/v5.6/` (or the next version). Do not change any existing number.
5. Edit `suite.html`: the cards (5.1), the new sections, the corrections (section 2). Every number from data, through `site/findings.js`.
6. Extend `dev/tools/check_figures.js` block 11 (every new number equals the data in every view) and `domtest.js` Phase 15 (new sections draw, tables have downloads, charts answer the keyboard). After adding checks, `node domtest.js --write-counts`.
7. `no_figure_change.py compare` must pass: no existing number moves; new fields add counts, each needing a reasoned line in `dev/tools/no_figure_change_allow.txt`.
8. `validate`, `unit`, `domtest`, `check_figures.js`; `guard_test.js` only if the engine was touched.
9. Version: page-and-data only, so use `set_version.py` for a patch or minor label as the session judges, then `check_versions.js`.
10. Write the plain-words report in `dev/reports/` (no bare labels such as s161), record decisions in `dev/DECISIONS.md`, update `HANDOFF.md`. Draft pull request into `main`; never push to `main`. No model or assistant names in any pushed file.

## 7. Decisions to put in the report for Duke's reading (not blockers)

Duke has delegated the math and code, so these are **flagged, not asked**: each touches a claim in his BLEI paper, so the report should say it plainly and ask only whether it misrepresents his vision.

- **D1.** EPPM is shown in the model's own terms, not by the paper's formula, and will be well below the paper's worked examples. The paper's formula is not applied because it values the allowance at 2.085 times face value and then the model's price cuts would count again. (Alternative not chosen: reproduce the paper's number with the paper's ε.)
- **D2.** IPBI is shown as "partly modelled": the model's public costs avoided stand in for the public-cost side of the crime and health channels (not for the paper's per-household dollars), and the other channels are "not modelled" with what each would need. The paper's dollar ranges are not shown beside simulated results. (Alternative: print the paper's ranges, labelled as untested.)
- **D3.** CSI is answered by simulation and labelled "simulated reading", with Acre Equity added; the paper's closed form is not computed.
- **D4.** Whatever the paper's own discrepancies are (its BLEI Month-0 figure 71.3 against 70.7 from its own arithmetic; EDC 0.744 against 0.625 for the same profile; the λ range that saturates) are **not** copied onto the page; if the page cites a paper number, it says which one and that the paper's own figures disagree. [Verify: I found these in a summary of the paper; re-check each in the text.]

## 8. Part B: go-live (a separate, small pull request, only after Duke says the page is ready)

The main page's treatment is decided after Part A, so **do not link from `index.html`, `study.html` or `replication.html`**.

1. **Link from the findings explorer.** `findings.html`: add `<a href="suite.html">Visual suite</a>` to the nav (near line 67, beside Study and Replication) and to the footer line (near line 119). Check the nav at phone width; a sixth link may wrap.
2. **Remove "don't list in search engines".** `suite.html` line 9: delete `<meta name="robots" content="noindex, follow">`. While there, add what `findings.html` has and `suite.html` lacks: `<link rel="canonical" href="https://bettertobest.github.io/compassionism-simulation/suite.html">` and the `og:url`, `og:title` and `og:description` tags (`findings.html` lines 11 to 13 are the pattern); `suite.html` already has JSON-LD Dataset, check its `url`. Without a canonical, search engines will treat the extensionless address (`/suite`) and `/suite.html` as two pages; pick one and make the other agree.
3. **Change the domtest check that expects no other page to link to it.** `domtest.js`, Phase 15, the check near line 1263 to 1264 ("the suite page stands alone: no other page links to it yet"). Do not just delete it: rename it and assert the intended state: **`findings.html` links to `suite.html`, and `index.html`, `study.html`, `replication.html` and `earlier-engine.html` do not** (the main-page decision is still open). If the number of checks changes, run `node domtest.js --write-counts`. Also check the comment above Phase 15 (lines 1228 to 1231), which says "no other page links to it", and the `HANDOFF.md` "stand-alone" wording, and update both.
4. **Outside this repo.** This repository has no `sitemap.xml` or `robots.txt`. If the site-wide indexing files live in the root-domain repository, the suite URL needs adding there; that is a separate change.
5. Run the three checks, `check_versions.js` and `no_figure_change.py compare` (the link adds no numbers). Draft pull request; update `HANDOFF.md` (remove "stand-alone"; remove the next-action line about linking).
