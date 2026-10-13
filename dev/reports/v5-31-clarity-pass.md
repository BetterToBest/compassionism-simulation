# The plain-language pass over the pages and reports

Oct 13, 2026 (ledger step s147). No engine code changed and no figure changed. This note says what was reworded, how we know no number moved, and the wording questions that are Duke's to decide (section 3). None of those was applied.

## 1. What changed, in plain words

The rule for the pass: keep every fact and every number; shorten long sentences; spell out an abbreviation where a reader first meets it; define a word the page uses as a term (a "reading", a Gini coefficient) where it first appears; never leave a bare label such as d175 without words before it.

| Where | What changed |
|---|---|
| Findings page, guided-read text (written by `dev/tools/release_data.py`, shown for the current release) | The opening line now says what a "paired run" is (the same adults run twice on the same random luck). Long sentences about the Source, the Year 7 targets, the sweep of how much new output backs the payout, the household rows, the release changes, the jobs-and-homes-and-shops text and the readings were split into short ones. Basic Units, Public Trust Housing, the Basic Living Economic Index and a Gini coefficient are spelled out where each is first used. |
| Findings page, fixed text (`findings.html`) | "Three plain results first" now reads "The headline results come first" (the page has had a fourth card since v5.3). The no-script note and the table section named the old v5.2 data file; they now name the v5.4 file that holds the numbers shown. |
| Findings page, chart row names (`site/findings.js`) | Four row names spell out their terms: the community businesses (PTF), community housing and community businesses in the v5.3 row, the surplus for an even chance of advancing (FBS50), and U-6. |
| Study page (`dev/tools/study_data.py`) | "Cell" became "combination of health system and economy"; B and C are named where they are first used; "paired seeds" reads "paired runs (seeds)"; the Morris and Sobol methods are named; PTH, PTF, CCO and SNAP are spelled out. |
| Front page (`index.html`, text only; the scripts are byte-identical) | Five long paragraphs and bullets were split into short sentences, and "a reading" is defined where the page first uses it. |
| README | The two long opening paragraphs became short sentences. The attribution paragraph is untouched. |
| Economist checklist (`dev/tools/review_rows.py`, regenerated) | Rows 1, 2, 6 and 10 spell out CCO, PTF, PTH, BU, basket poverty and wealth poverty. |
| Notes on stale records | `CONTRIBUTING.md` now says its open-items table shows where each item stood at v5.2 and has not been re-checked against v5.3 to v5.5. `dev/PROGRESS.md` now says to start from `HANDOFF.md` because some boxes were left unticked after the work was done. Neither table was re-judged row by row (see section 3, item 6). |
| Reports | Three lines in two reports named a bare label (d137 to d139, d194); each now says what the label stands for. The other reports already put every label after words. |

Left as they were, on purpose: `earlier-engine.html` (the frozen v4.22 page, "as coded"); the technical body of `replication.html` (about 60,000 words of formulas and parameters; its opening, "What is being replicated", was read and already reads plainly); the data tables' row labels; and release data for v5.0 to v5.3 (archives of what those releases said).

## 2. The no-figure-changed test

Run before the first edit and after the last. Output files are in the session's scratch space and the key lines are copied here.

| Check | Before | After |
|---|---|---|
| `node dev/tools/check_figures.js` | all 16 passed | all 16 passed |
| `python3 dev/tools/release_data.py --check` | up to date (14 files) | up to date (14 files) |
| `python3 dev/tools/study_data.py --check` | matches the generator (9 tables) | matches the generator (9 tables) |
| `node domtest.js` | 130 checks, all passed | 130 checks, all passed |
| `python3 dev/tools/review_rows.py --check` | 12 rows match | 12 rows match |

Those four checks show the data files are what the generators write and the page reads them correctly. They would not catch a number that changed in both the generator and the page, so a stronger test was added: `dev/tools/no_figure_change.py`. It records before and after:

- a fingerprint of `harness.js` and of every script block in `index.html` (the engine is read out of `index.html`): **identical**;
- a fingerprint of every numeric value, with its path, in all 34 data files: **identical**;
- how many times each number appears in the words of 103 files (pages, reports, site scripts, data text): **8 numbers moved, all expected and named in `dev/tools/no_figure_change_allow.txt` with the reason**: the file name "v5.2" to "v5.4" twice in `findings.html` (the corrected data-file link), and six version labels in the new `CONTRIBUTING.md` note. No result figure, percentage or dollar amount moved.

Command: `python3 dev/tools/no_figure_change.py snapshot before.json` before editing, `... snapshot after.json` after, then `... compare before.json after.json`.

Limit: the test shows that no number was added, removed or changed in the words, not that a reworded sentence still means the same thing. That is read by eye; the sentences that might change meaning are in section 3 and were not changed.

## 3. Wording questions for Duke (none applied)

1. **Which programmes does the damping constant belong to?** The study page's table of unsourced constants says "PTF and PTH inflation damping: how much of outside inflation the food and the health programmes absorb". Everywhere else PTH is Public Trust Housing (community housing), not health. The economist checklist (row 2) now spells PTF as community businesses and PTH as community housing, so the two pages disagree until this is settled. Proposed wording: "how much of outside inflation community businesses (PTF) and community housing (PTH) absorb". The engine line reads the share of PTF and PTH members, which supports that wording, but the original sentence may have meant something else, so it is Duke's call.
2. **What does "design-neutral" mean?** The words "design-neutral reading" label a second version of the 30-days-of-basic-living measure (table headers, the targets chart, the replication page) and are never defined in plain words. The reports suggest it leaves out the benefit from lower prices and in-kind support, but that is Claude's reading. Proposed: write one plain definition once Duke confirms it.
3. **Spelling.** The pages use "programme", "labour", "ageing" and "behavioural"; the project instructions and the book's readers are American ("program"). Changing it touches several hundred strings across the pages and generators and does not change a meaning. Proposed: switch to US spelling in one later step if Duke wants it.
4. **A glossary on the findings page.** The front page has a glossary panel; the findings page does not, so it relies on spelling terms out in the text. A glossary there would be new content and a new test. Proposed: add the front page's glossary to the findings page.
5. **The header strip on the front page** shows "CCO · PTF · PTH · SZH · CIP · BLEI-calibrated" with no words. Spelling it out would lengthen a header Duke may have set on purpose.
6. **Two stale records need a row-by-row check, which is a content task, not a wording one.** The open-items table in `CONTRIBUTING.md` (about 50 rows, last judged at v5.2) and 18 unticked boxes in `dev/PROGRESS.md`. Proposed: a separate ledger step that checks each row against the code and ticks or rewrites it.
7. **Claude's reading of the sensitivity results** (the study page's "What would have to be true" panel) is still Claude's reading, as the earlier handoff said. This pass reworded around it but did not touch its claims.
