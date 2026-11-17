# Reader-facing wording: what readers saw that they did not need (inventory, Nov 17, 2026)

Duke asked (Nov 17, 2026) that what readers see should not carry the project's internal bookkeeping: step and ledger codes (`S55`, `D26`), job ids (`X3`), `session 12`, `part M`, `round 2`, `release 1` and `release 2` for the two model generations, and `C2.2` (NEEC's criterion code) as the name of a design. This note counts every such occurrence in the text a reader opens, before any edit. The names that replace them are recorded in `dev/DECISIONS.md` (reader-facing names, Nov 17): `release 1` is v5.6, `release 2` is v5.9, `C2.2` is the full-coverage design, the release design is the opt-in design, and a study is named by what it asks.

**How it was counted.** `python3 dev/tools/reader_codes.py` (this repository), with `--root ../research-hub --preset hub` and `--root ../bettertobest.github.io --preset root` for the Research Hub and the root site. Reader-visible text is a page's text outside scripts, styles and `<code>`, its title, alt, aria-label and placeholder attributes, the prose strings of its scripts and `site/*.js`, Markdown outside code, and the text fields of the JSON files pages render. A path or file name in `<code>` or backticks is where a reader finds something and is not counted. The last column (row ids such as `c22` and `rel`, key and switch names such as `giniW` or `CFG.*`) is listed for the edit pass and not failed by the check; most of its matches on the simulation page are HTML `rel=` attributes inside script strings. `node dev/tools/reader_check.js` counts the same codes in each page as rendered with its data, which adds the labels the scripts print: 428 occurrences in 10 views before the edit.

## The Simulation's pages and documents

| file | step/ledger code | session number | part letter | job id | `round 2` | `release 1/2` | `C2.2` | row id or key | total |
|---|---|---|---|---|---|---|---|---|---|
| CHANGELOG.md | 31 | 55 | 0 | 3 | 4 | 35 | 2 | 0 | 130 |
| CONTRIBUTING.md | 1 | 5 | 0 | 0 | 0 | 5 | 1 | 0 | 12 |
| data/manifest.json | 8 | 0 | 0 | 0 | 2 | 5 | 2 | 0 | 17 |
| earlier-engine.html | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 8 |
| findings.html | 4 | 0 | 0 | 0 | 3 | 20 | 1 | 0 | 28 |
| index.html | 6 | 0 | 0 | 0 | 1 | 17 | 2 | 6 | 32 |
| replication.html | 2 | 1 | 0 | 0 | 2 | 10 | 1 | 2 | 18 |
| site/cb.js | 1 | 0 | 0 | 0 | 0 | 3 | 8 | 0 | 12 |
| site/glossary.json | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| site/notes.js | 1 | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 12 |
| site/round2.js | 0 | 0 | 0 | 0 | 3 | 1 | 3 | 0 | 7 |
| site/studies.js | 14 | 0 | 0 | 0 | 6 | 6 | 0 | 0 | 26 |
| suite.html | 0 | 0 | 0 | 3 | 0 | 40 | 6 | 0 | 49 |

## The Simulation's reports (`dev/reports/`, 95 files)

| file | step/ledger code | session number | part letter | job id | `round 2` | `release 1/2` | `C2.2` | row id or key | total |
|---|---|---|---|---|---|---|---|---|---|
| all 95 reports | 572 | 81 | 7 | 21 | 52 | 45 | 589 | 30 | 1397 |

Per-report counts: `python3 dev/tools/reader_codes.py | grep dev/reports`. Most reports carry their step code in the title line and cite other steps by code throughout.

## The Research Hub (pages and papers; the frozen `/v1/` archive excluded)

| file | step/ledger code | session number | part letter | job id | `round 2` | `release 1/2` | `C2.2` | row id or key | total |
|---|---|---|---|---|---|---|---|---|---|
| basic-living-economic-index.html | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |
| cco-ptf-integrated-framework.html | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| citizens-internet-portal.html | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| community-monetary-development.html | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| corrections.html | 16 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 17 |
| cultural-value-integration.html | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| data/claims-summary.md | 11 | 0 | 0 | 0 | 0 | 1 | 14 | 0 | 26 |
| democratic-governance-pth.html | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| drug-policy-reform.html | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| dual-currency-inflation.html | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 |
| economic-modeling-simulation.html | 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 5 |
| integrated-digital-governance.html | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| optimal-transfer-design.html | 3 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 7 |
| referendum.html | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| risk-mitigation-framework.html | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| us-policy-eras.html | 4 | 0 | 0 | 0 | 0 | 0 | 12 | 8 | 24 |
| wiki/index.html | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 |
| **all** | 55 | 0 | 1 | 0 | 0 | 8 | 28 | 9 | 101 |

## The root site (bettertobest.github.io)

| file | step/ledger code | session number | part letter | job id | `round 2` | `release 1/2` | `C2.2` | row id or key | total |
|---|---|---|---|---|---|---|---|---|---|
| ai-index.json | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 |
| ai-manifest.json | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| llms.txt | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| research-index.json | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 |
| **all** | 8 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 10 |

## Out of scope

Code comments, `dev/DECISIONS.md`, test and check names, preregistrations, commit history, the research-update repository, and data keys and labels stored in data files (pages map stored labels to the plain names when they print them).

## Part 2 (Nov 17, 2026): CHANGELOG.md and the reports

Before: 1,516 occurrences that fail the check in CHANGELOG.md (129) and the reports in `dev/reports/` (1,387): `C2.2` 596, step and ledger codes 605, session numbers 137, `release 1/2` 84, `round 2` 61, job ids 25, part letters 8. After: none. Most were reworded by a rule pass (the same names as the pages); every change was then read, and the rest were reworded by hand. Where a code stood for a decision of Duke's, the text says "Duke's decision"; where it stood for a working session, it gives the date or names the build (for example "the first v5.0 candidate"). A report that numbers its own statements or parts keeps those labels; they are listed with a reason in `dev/tools/reader_codes_allow.txt`. The check now covers both, with no files pending. Only the reports in subfolders of `dev/reports/` (the second implementation's packet notes) are outside it.
