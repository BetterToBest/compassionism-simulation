# v5.2.2: the audit fixes, in plain words

Oct 6, 2026 · Claude · one pull request into `main`; merging it is the release · no figure changes

## What this release is

Three outside reviews of v5.2.1 (by GPT, Grok and Muse) found no mistake in the model or in any figure. They found words that were wrong, two places where a number was typed by hand instead of read from the model, and documents that an outside expert would need and could not find. This release fixes those. Every result on the pages is exactly what it was in v5.2 and v5.2.1; the computer files behind them are unchanged to the byte.

## What was wrong, and is now fixed

1. **"Nine runs in ten" should have said "eight runs in ten".** Where the page gives the range of the price level, it quotes the spread from the 10th to the 90th of the 500 runs. That range holds eight runs in ten, not nine. The page now works out the words from the range it actually shows, and the page test now checks that the words match the range, so the two cannot disagree again. (Before, the test itself checked for the wrong words, which is why nobody caught it.)
2. **Eight old statements on the replication page.** Its list of the model's limits still described problems that were fixed long ago: for example, that each person's automation risk is drawn evenly between 0.2 and 1.0 (it has followed the job data since v4.3), and that the headline figures come from a v4.4 study (they come from the release model since v5.0). Each of the eight now says what is true today and what is still open. A new automatic check now fails if any of these old statements comes back to a public page.
3. **The $25,000 line was typed by hand in two places.** It now comes straight from the model's settings, so if the line ever changes, every page changes with it, and a check confirms they agree.
4. **"Savings" should have said "net wealth".** The measure "too little wealth" counts what someone owns minus what they owe (it can be below zero), and the cards now say so. The earlier releases in the version menu say it too; their numbers are unchanged.
5. **The README pointed to old figures.** It sent readers to a part of the replication page that holds the earlier model's numbers; it now points to the findings page and the new model description.

## What was added

- **How the confidence ranges are worked out.** The replication page now says in one line that each change is measured run by run (with the programme minus without it, on the same simulated people) and its range comes from those 500 differences. The share of runs in which the programme does better needs each run's own result, which the saved files do not keep; v5.3 will keep them.
- **What the inequality figure (Gini) estimates.** Each Gini is slightly adjusted upward so that it estimates the inequality of the whole population the 500 adults stand for, not only these 500. The page now says this, and the unadjusted figure for the 500 adults themselves is in the data file beside it.
- **The Phi step, measured** (a separate short note: `dev/reports/v5-11-phi-step.md`). In the model, the Phi bonus (×1.618) switches on the moment a person's quality passes 70% of the top. For one person right at that line, a tiny gain in quality raises what they keep per converted unit by about a quarter. But only about 6 in 1,000 participant-years sit near the line, so it hardly moves the results. Your papers describe Phi as a level one qualifies for, so the step stays; the 70% is the model's own choice and is labelled that way, and the next round's sensitivity study will test it.
- **A full description of the model for outside experts.** Four documents: `MODEL_SPEC.md` (exactly what the main result does, step by step through a simulated year, and what each headline number measures), `TESTBED_SPEC.md` (every alternative switch and labelled reading, with its status and the decision behind it), `REPRODUCE.md` (the command behind every published table and a fingerprint to check a rerun against) and `ODD.md` (the standard format model libraries ask for, with every setting marked as sourced, derived, a design choice of yours, or an assumption).
- **For outside reviewers on GitHub**: a citation file (so GitHub shows "Cite this repository"), an archive of everything needed to reproduce each release attached automatically when a release is tagged, and three "good first issue" tasks for volunteers (the population-weighted living wage, a table of jobs with their automation risk and wages, and cost-of-living figures by region).

## Decisions made this round (one line each; full reasons in `dev/DECISIONS.md`, Session 37)

- The wording fixes above (items 1 to 5) are corrections: each was wrong.
- The Known Limitations items were rewritten, not deleted, so the history stays visible.
- The Phi threshold stays as you designed it; its 70% level is labelled a modelling assumption and joins the v5.4 sensitivity study.
- The CoMSES model-library package waits until after v5.3, as you chose on the dashboard.
- "Savings" stays as an everyday word elsewhere on the pages (for example "median savings"); only the definition of "too little wealth" changed. This is optional polish if you would like it changed everywhere.

## Does anything here misrepresent your vision?

Two places quote your Hub in this round: the Phi note (Phi as a level one qualifies for, with both beauty and usefulness assessed) and the model description's summary of the framework. Please say if either reads wrong.

## What you need to do

Read this note, and merge the pull request if it reads right; merging is the release (the version becomes v5.2.2). Nothing else is needed. The next round, v5.3 (households and children), starts after the merge.
