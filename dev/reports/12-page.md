# Step 12 report: the page, rebuilt for the release

Oct 1, 2026 · plan step 12 · Claude · on `next-release` only; the live page on `main` is unchanged

Following the outline in `00-page-outline.md`:

- **Title and attribution.** The title now ends "see how it does." Directly under it sits the attribution in the wording from `CLAUDE.md`. The same text is in the README and under the replication page's title.
- **What Compassionism is.** Six short points. The financing point carries the label "Claude's reading of the design".
- **The results.** The precomputed 500-seed panel, one environment at a time (Reference, Adverse, Stress). BLEI comes first (your definition, with the design-neutral reading beside it), then one everyday sentence each on living below the cost of living, savings, whether the gain is confirmed, who gains, work, prices, cost and how it is paid, public costs avoided, and the optimistic end. Each figure carries its 95% interval. A fold-out shows the other readings side by side, and the command that reproduces everything is named.
- **Run it yourself.** One button runs the release model in the browser for one seed (a few seconds), using the page's own engine; a check confirms it matches `harness.js` exactly.
- **Limits.** Seven short lines, the decisive unknown first. The full list, the calibration notes and the version history moved to the replication page, in a new section "Assumptions, ODD protocol, calibration notes and version history". The page's 161 KB panel now points there, and the page shrank from 889 KB to 643 KB.
- **The comparison is gone.** The "Compare designs" controls, the six-design table, "What each design is" and every "five other designs" line are removed, and so is the README's walk-through link. The comparison is saved, unlinked, as `dev/drafts/compare-designs.html`.
- **The earlier engine.** Its settings and dashboard stay below the front door for exploration, labelled "the earlier engine (v4.22, as coded)", with a note that its figures differ from the results above.
- **Three wording fixes:**
  - the poverty card is "Five Measures" everywhere;
  - the glossary no longer says BU are spent only at community businesses (all essential-service businesses accept them);
  - the 30% PTF figure is now labelled a caution threshold with no source (the model applies no efficiency loss), instead of a stated "distortion threshold".

Checks: domtest's front-door phase was rewritten for the new page (10 checks). Three older checks were updated where they counted removed content. 97 of 97 pass. Seen in Chromium at desktop and phone width: the live run works and the phone layout has no sideways scroll. The chart library could not load in the sandbox (blocked network), so the charts were not seen.
