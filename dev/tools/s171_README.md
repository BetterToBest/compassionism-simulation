# Study s171: what this folder holds and what to do with it

Written Oct 15, 2026 by Claude Code, for a chat that has no code access. One Runpod study, engine commit and command in `run.txt`. Every figure is the mean over simulated people, seeds 1-500 paired (the same people in every arm), 500 adults per run. Today's safety net (SNAP with its work rule, EITC, CTC) is in every arm, with the slope fix. Limits: the model has not been reviewed by an independent economist; read results as exploratory.

## Files

| File | For | What it is |
|---|---|---|
| `release-panel[-40]-ENV.json` (ENV = ref, adv, st) | ledger s117 | The release panel, 20 years (no `-40`) and 40 years. Each row has the usual release keys and, new here: `pjHrs` (hours a year given to community projects per participant), `pjWork` (share of participants who took project work, %), `pjDisp` (hours of those taken from paid work), each with `...D` = [mean difference against no programme, low, high] (95%). Row `release` is the main row. If `pjDisp` is 0 everywhere, say so: in this model project hours add to paid work rather than replace it. |
| `match-ENV-YEARS-FIN.txt` | ledger s95 / s171 | Markdown tables: the Hub-specification Compassionism design beside UBI, a negative income tax and an asset endowment sized to equal its cost, X-Cents and public grocery at their own cost, plus the "two former stand-ins on" shaded row (the untested mechanisms). `FIN` = `money` (the Source pays; v5.0 and later reading, the released main row) or `tax` (a flat contribution on wages pays; the old comparison's rule). Read the first line of each file for the exact command. Each design appears with BLEI, basket and wealth poverty, FGT2, earnings and group effects, with 95% intervals. |
| `python-reference-500.json` | ledger s118 | The real engine's output for the five validation presets, seeds 1-500, for checking the independent Python version on 500-seed means. |
| `status.txt`, `*.log`, `SHA256SUMS` | all | Which pieces finished and when; `DONE` means every piece is in. If `DONE` is missing, the run stopped early: list the missing pieces from `status.txt` and rerun (finished pieces are skipped). |

## Next steps for the chat that reads this

1. **s117 (hours).** Read row `release` in each `release-panel*.json`: report `pjHrs`, `pjWork`, `pjDisp` for Reference, Adverse and Stress at 20 and 40 years, with intervals. Add one paragraph beside the page's "Beyond money: time and taking part" text, keeping the label "Claude's reading of the design" and the limit: hours are not wellbeing, and the model does not know whether they were chosen, enjoyable or useful. The repository needs `index.html` (grep `rel-flourish`) and `data/` updated by someone with code access; write the paragraph and the table so they can paste it.
2. **s95 / s171 (compare page).** `compare.html` Part 1 is from the old v4.22 engine. Write a Part 1b from the `match-*` tables: for each financing rule, one table per environment, in plain words, with the Compassionism Core (untested mechanisms off) as the like-for-like row. State that all arms have today's safety net and are paid for by the same rule. Say where Compassionism costs more or raises prices more than another design.
3. **s118.** Compare the Python version's 500-seed means with `python-reference-500.json` (five presets); accept per the rule in `dev/packets/s118-brief.md`.
4. Hand the paragraphs and tables back to whoever has repository access (Claude Code, next week or later), which also runs `node domtest.js --write-counts` and `node dev/tools/check_figures.js` after the page changes.
