# Community-project hours (the third flourishing measure): what is needed

Oct 15, 2026. The simulation page now shows two rough flourishing measures from figures the release already carries: time freed from work (the change in hours worked) and enrolment by year 20. The third measure Duke named, **hours given to community projects**, is not yet in any released figure.

## What exists
- The engine counts project hours when project hiring is on (`PROJ`; accumulators `pjHrs` per participant-year, `pjWork` the share of participants who took project work, `pjDisp` the hours displaced from paid work). The main release row is the Hub specification with project hiring on, so the numbers are computed on every run, but they are not among the written-out keys (`TB_KEYS`, index.html), so the released rows do not carry them. Verify this first with a two-seed run before any pod time is spent.
- `harness.js` returns them from `tbRunCore` (`pjHrs`, `pjDisp`, `pjWork`) in the results of a study.

## What to do (a Runpod job, resumable pieces)
1. (Done Oct 15: the three keys were already in `TB_KEYS`; the release rows did not write them. `harness.js testbed ... release --hours` now adds them to every row. Study s171, `dev/tools/s171_jobs.sh`, runs it with the six-design comparison and the Python reference.)
2. Re-run the release panel for the main row and its no-programme pair, 500 seeds, Reference, Adverse and Stress, 20 and 40 years, via `dev/tools/s165_jobs.sh` (pieces are resumable; seeds are paired). Record the exact command and the commit beside the result, and push the result to BetterToBest/compassionism-sim-results.
3. Show on the simulation page, beside the existing flourishing paragraph: hours a year given to projects per participant, the share of participants who took project work, and how many of those hours came out of paid work. Keep the label "Claude's reading of the design" and the cautious reading (projects counted at the cost of their hours) beside the market-value reading.
4. Update the domtest count (`node domtest.js --write-counts`) and `check_figures.js`.

## Limits to state
Hours given to a project are not a measure of wellbeing or of what a community values. The model counts hours; it does not know whether they were enjoyable, freely chosen or useful.
