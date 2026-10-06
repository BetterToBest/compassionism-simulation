# Adding a release (the data, the pages, the checks)

Since v5.2.1 every number on the simulation page's guided sections, the findings explorer (`findings.html`) and the replication page's summary comes from one data file per release. A new release adds a file and an entry; it needs new page code only when it brings a new *kind* of figure. This is the whole recipe, in order. Run every command from the repository root.

## 1. Regenerate the 500-seed results (only for a release whose figures change)

From a clean commit (no uncommitted changes; the panels record the commit and refuse a dirty tree in the checks), one process per environment and horizon, so no single run outlasts a session (seeds are paired, so the split changes no figure):

```
node harness.js testbed 500 release ENV --json=dev/runs/release-panel-ENV.json              > dev/runs/vX-release-500-ENV.txt
node harness.js testbed 500 release ENV --years=40 --json=dev/runs/release-panel-40-ENV.json > dev/runs/vX-release40-500-ENV.txt
node harness.js testbed 500 backing ENV --json=dev/runs/backing-share-ENV.json               > dev/runs/vX-backing-500-ENV.txt
node dev/tools/us_check.js ENV 500 20                                                       (ENV ref and adv)
node dev/tools/explore_export.js ENV 20 500 1  and  node dev/tools/explore_export.js ENV 40 500 1
```

for ENV `ref`, `adv` and `st`. Then merge: `python3 dev/tools/merge_panel.py`, `python3 dev/tools/merge_panel.py 40`, `python3 dev/tools/backing_chart.py` (the sweep's merged file). `explore_export.js` refuses to write if its yearly means do not equal the panel's published path, so run it after the panels.

## 2. Write the release data

1. In `dev/tools/release_data.py`, set `CURRENT` (version of the figures, date, tag, one-line summary; `shownIn` is the page version when it differs).
2. `python3 dev/tools/release_data.py` writes `data/releases/v<version>.json`, the explore files in `data/releases/v<version>/`, the entry in `data/manifest.json` (the previous current release becomes "earlier"), and the headline numbers in the pages' static blocks (`<!-- figs:NAME -->`).
3. An earlier release is added with `python3 dev/tools/release_data.py --backfill vX.Y` (it reads the files committed at that tag), and only after its panels were regenerated from the tag and match the published ones exactly (as in `dev/runs/v521-backfill-check.txt`).

## 3. When the release brings a new kind of figure

- A new reading row in the panel appears by itself in the explorer's readings chart and table and in the simulation page's "How sure are we?" chart. Give it a short label and a group in `site/findings.js` (`SHORT`, `GROUPS`); without one it shows its panel label in the "other" group.
- A new table or text: add its generator to `release_data.py` (`tables`, `texts`); a new guided read: add it to `STORIES` there, and a chart kind to `CHARTS` in `site/findings.js` only if none of the existing kinds fits (`dumbbell`, `targets`, `fixed`, `backing`, `readings`, `us`).
- Numbers are never typed into a page or into page code: put them in the release file and print them with `CSF.num(R, path, format)` (or `{{path|format}}` in a text). The check below fails on a typed percentage, dollar figure or price level.

## 4. Version, notes, checks

1. `python3 dev/tools/set_version.py <page version>` then `node dev/tools/check_versions.js`.
2. Notes: the new `## v<version> Release Notes` at the top of CONTRIBUTING.md (the release workflow reads it); move the previous release's notes to the top of CHANGELOG.md; add a panel to the replication page's version timeline (`#hl-list`).
3. The three checks, exactly as `.github/workflows/checks.yml` runs them: `npm install --no-audit --no-fund`, then `node harness.js validate`, `node harness.js unit`, `node domtest.js`. Phase 14 of `domtest` is the figure check (`node dev/tools/check_figures.js` runs it alone, in about 20 seconds). If the count of checks changed, `node domtest.js --write-counts`.
4. Look at the three pages at 390 px and 1280 px wide, in light and dark, before opening the pull request.
