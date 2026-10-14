# Duke's answers to the seven wording questions, applied

Oct 14, 2026 (ledger step s160, with issue i20). Wording only: no engine code changed and no figure changed. This note says what each answer changed, one place where a later decision changed the meaning of Duke's pick, and how we know no number moved.

The questions were in `dev/reports/v5-31-clarity-pass.md`, section 3. Duke answered them in the project ledger (decisions d201 to d207), and one more decision (d213) was added before this session.

## 1. Where d213 changed the meaning of Duke's pick for d201 (read this first)

The question (d201) was which programs the inflation-damping constant belongs to. Duke picked the second option, which described community housing (PTH) as the program "which holds rents down".

That description is not what the model does. In the engine, PTH membership lowers the **overall** inflation rate of the whole simulated economy (the inflation rate is multiplied by one minus 0.10 times the share of people who are PTH members). No rent calculation uses that constant. Writing "which holds rents down" on the study page would have claimed a mechanism the code does not have.

So a follow-up decision (d213) was put to Duke in the ledger, and confirmed: name both programs without a claim about rents, and say the damping applies to the overall inflation rate. The study page and the economist checklist now read:

> Inflation damping by community businesses (PTF, which cut prices) and community housing (PTH): how much of outside inflation they absorb, applied to the overall inflation rate

What this changes from Duke's pick: the page no longer says PTH holds rents down. It keeps what Duke's pick added (naming what the programs are, rather than "the food and the health programmes"), and it says plainly where the effect lands. If Duke's vision is that PTH's effect on prices should come through rents specifically, that is a modelling change, not a wording one, and would need its own step.

## 2. What each answer changed

| Decision | What Duke chose | What was done |
|---|---|---|
| d201 with d213 | Name the programs the damping belongs to (wording as in section 1) | Study page table of constants with no source, and row 2 of the economist checklist, now say the same thing and match the code. The stale HANDOFF.md warning that the two disagreed is removed. |
| d202 | Define the second BLEI reading and rename it the "same-rules reading" | The definition already written on Oct 1 (`dev/reports/08-blei.md`) is now on the pages: the same rules for everyone (12% of a month's wage and the ordinary daily cost of living) plus one month of whatever regular support a design pays; it leaves out the two extras the BLEI paper gives participants (20% of wage, and a lower daily cost in community housing). It appears where each page first shows the reading: the front page's results text and glossary, the findings page's description of the measures. There, the pages say "earlier called design-neutral". Chart and table labels use the new name. The replication page has one note on the new name; its technical body is otherwise unchanged. |
| d202, a correction found on the way | (follows from the definition) | The front page said the gap between the two readings "is the benefit from lower prices and in-kind support". By the definition, the gap is what the two participant extras add, and the page now says that. |
| d203 | US spelling on the generators and live pages | Done last, as its own commit (program, labor, aging, behavior, modeled, labeled, and about 40 other words; about 450 lines). Left as they were: `earlier-engine.html` (frozen), the archived release data for v5.0 to v5.3, the engine code inside `index.html`, the page's embedded data and its search-engine description block (both are checked byte for byte), code names and file names, and the developer records (`CONTRIBUTING.md`, `dev/`). |
| d204 | Findings page gets the front page's glossary, from one shared source | The glossary's entries now live once, in `site/glossary.json`. `dev/tools/glossary.py` writes them into both pages, and its check runs in CI, so the two cannot drift apart. On the findings page it is a collapsed "Terms used on this page" panel at the top. |
| d205 | No change to the front page's header strip | Nothing changed (the strip already shows each name on hover, with a link). |
| d206 | Mark the old open-items table and progress boxes as dated historical records | `CONTRIBUTING.md`'s table and `dev/PROGRESS.md`'s tick boxes are now labelled "historical record, closed on October 14, 2026; read-only", pointing to HANDOFF.md and the ledger as the live record. No row was re-checked. |
| d207 | Keep the "What would have to be true" panel, labelled Claude's reading, and name it for the outside audits | The study page's panel title now says "(Claude's reading)" and its first line says it is not yet checked by an outside reader. The economist checklist has a new row (13) asking a reviewer to check it. |
| i20 | (issue, not a question) | The checks and release workflows are pinned to the ubuntu-24.04 runner image, Node 22.22.0 (the version the 500-seed runs record) and, for the checks, Python 3.13. The default runner image moves to Ubuntu 26 on Oct 19; pinning keeps the bit-identical tests meaningful. |

Not changed on purpose: the column names in the downloadable CSV and JSON files (for example `design_neutral_change_pts`) stay as they are, because they are names other people's scripts may read.

## 3. How we know no number moved

The no-figure-change test (`dev/tools/no_figure_change.py`) was run against `main` as it stood when this work began (the merge of pull request 26), and again after the last edit.

One improvement to the test came first, because two of the answers change words that the page's own code writes. Before, any change to the front page's script failed the test. Now:

- the engine (the exact code `harness.js` cuts out of `index.html` and runs) must be byte-identical;
- the page's other script blocks (the embedded 500-seed results and the search-engine description) must be byte-identical;
- every number in the page-drawing code is counted, the same way the numbers in the words are counted.

So the test is as strict as before on the engine and stricter on numbers.

Result after the last edit: **PASS**. Engine and embedded data identical; all 34 data files' numbers identical; 104 files' number counts compared. 21 number counts moved, all listed with a reason in `dev/tools/no_figure_change_allow.txt`:

- the same-rules definition quotes the existing BLEI rules (12% and 20%) on the front page, its code and the replication page; the replication note says "releases up to v5.5";
- the findings page's new glossary brings the numbers in the front page's definitions (for example the ~4% a year in Acre Equity's definition);
- CONTRIBUTING.md's dated note (14 for the date; three release numbers no longer listed);
- the economist checklist's new row 13.

HANDOFF.md is no longer compared: it is the session log, rewritten every session, and publishes no figure.

The figure check scans the findings page for typed percentages; it now skips the glossary panel, as it already skipped the front page's (the definitions state design parameters, not results).

## 4. Checks

`harness.js validate`, `check_figures.js` (16 of 16), `release_data.py --check`, `study_data.py --check`, `review_rows.py --check`, `glossary.py --check` and `domtest.js` pass on the final commit; the session's handoff records the exact counts. `guard_test.js` is unaffected (no engine change) and runs in CI.

One knock-on: the earlier-engine page carries the same script as the front page (domtest checks this), so the script's new wording was copied into it with `dev/tools/sync_earlier.py`. That page's own text is unchanged.

## 5. For Duke

- Section 1 is the one place where the words on the page differ from the option you picked. Say if "applied to the overall inflation rate" misrepresents what PTH should do.
- Everything else is as you chose.
