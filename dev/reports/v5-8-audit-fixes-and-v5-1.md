# v5.1: what the audit fixes changed, and what I found (plain words, for Duke)

Written Oct 3, 2026 (session 34). This is Claude's report on the second pull request of the audit round. It needs no code reading; the tables come straight from the 500-run files.

## In one paragraph

The external audit of v5.0 found one real timing error in the model, several things the page did not say plainly, and some gaps in how we check ourselves. Version 5.0.1 (pull request 3) fixes the text problems and corrects the version labels. Version 5.1 (pull request 4) fixes the timing error, regenerates every 500-run result once, adds the Hub's own targets beside the results, and adds a chart of the question the page calls its decisive unknown: how much of what the Source pays out new output has to back. The timing error is small in its effect. **The most important thing I found is not in the audit: in the Adverse and Stress environments the model's own rule for when the BU is indexed to prices holds back the "optimistic end" (section 4a).**

## What you need to do

1. Read sections 3 and 4. Say if anything misrepresents your vision; section 4a is a design question, not a code one.
2. Merge pull request 3 (v5.0.1) first, then pull request 4 (v5.1). Merging is the release; the release workflow tags each version. The `v5.0` tag stays where it is.
3. Optional, by hand: the old "apply a zip" workflow fails at its last step because of a `.gitignore` added in session 33. Deleting the two `':(exclude)...'` pieces from the `git add` line in `.github/workflows/apply-upload.yml` fixes it (details in `dev/PROGRESS.md`). I did not change workflow files.
4. There is a stray branch called `v5-1` on GitHub, made by a mistyped command of mine; the connection refused my attempt to delete it. It points at the same work as the real branch and does nothing. Delete it under Branches whenever convenient.

## 3. What the timing fix changed (V5-02)

The model decides each year whether a person's wage grows faster, by checking whether their resources cover enough days of basic living. For people on the programme that check used the BU they spent on essentials **last year**, not this year. The fix makes it read this year's. It was built as a switch, and with the switch off every result is identical to v5.0 (checked by comparing full outputs). With it on, the number it reads equals the engine's own later figure in about five million person-years checked, with no mismatch.

At 500 runs the effect is small. Only the reading of basic living that applies the same rules to everyone moves; every other headline figure moves by 0.1 point or less:

| Environment, years | Below 30 days of basic living, design-neutral reading: before | after | Every other headline figure |
|---|---|---|---|
| Reference, 20 years | 22.1% | 21.2% (−0.9 points) | moves by at most 0.0 point |
| Adverse, 20 years | 40.3% | 38.5% (−1.8 points) | moves by at most 0.1 point |
| Stress Test, 20 years | 56.9% | 56.6% (−0.3 points) | moves by at most 0.0 point |
| Reference, 40 years | 17.1% | 16.4% (−0.7 points) | moves by at most 0.0 point |
| Adverse, 40 years | 63.1% | 61.1% (−2.0 points) | moves by at most 0.1 point |
| Stress Test, 40 years | 75.1% | 74.9% (−0.2 points) | moves by at most 0.0 point |

Poverty, wealth, prices and cost are, for practical purposes, unchanged. The audit's own 60-run table said the same.

## 4. What I found that you should know

### 4a. The "optimistic end" is held back by the BU indexing rule in two environments

The page's optimistic end (called H1) asks: if every dollar the Source pays out were backed by new output, what happens? I ran the points in between (none, a quarter, half, three quarters, all backed) on the same 500 simulated adults, and drew them on the replication page. The change in the share of adults with too little wealth, against no programme, is:

| Environment | a = 0 (release row) | a = 0.25 | a = 0.5 | a = 0.75 | a = 1 (H1) |
|---|---|---|---|---|---|
| Reference | −16.3 points; inflation 34.9% | −21.8 points; inflation 26.0% | −29.1 points; inflation 17.0% | −34.5 points; inflation 8.3% | −36.5 points; inflation 0.0% |
| Adverse | +4.4 points; inflation 45.5% | −1.9 points; inflation 34.2% | −11.8 points; inflation 22.5% | −31.6 points; inflation 10.9% | −30.1 points; inflation 0.0% |
| Stress Test | +7.9 points; inflation 23.8% | +5.2 points; inflation 18.3% | +1.1 points; inflation 12.5% | −5.6 points; inflation 6.4% | −10.1 points; inflation 0.0% |

In the Reference environment the curve falls steadily, as you would expect. In the Adverse and Stress environments it bends at the right end: going from three quarters backed to fully backed makes the cost-of-living and basic-living measures **worse** and the programme **cheaper**. I tested why. The model indexes the BU to prices only in a year when prices rise faster than 5% (the Hub's Inflation Surge Protocol). Outside inflation in those two environments is 2%. When the programme adds some inflation of its own (three quarters backed: about 11% a year in the Adverse Environment) the 5% rule is on and the BU keeps its value. When the programme adds none (fully backed) the rule is never triggered and the BU loses a third of its real value over 20 years. With the BU indexed every year instead, the fully backed end looks like this:

| Environment, a = 1 | Wealth poverty | Cost-of-living poverty | Below 30 days of basic living | Cost per adult a year |
|---|---|---|---|---|
| Adverse, as modelled (BU indexed only above 5% a year) | 52.5% | 48.9% | 27.0% | $25,607 |
| Adverse, BU indexed every year | 31.8% | 33.0% | 19.8% | $37,142 |
| Stress Test, as modelled (BU indexed only above 5% a year) | 72.6% | 67.3% | 47.2% | $8,702 |
| Stress Test, BU indexed every year | 67.0% | 63.4% | 44.0% | $11,835 |

So in Adverse and Stress the H1 end is **not** the best a fully backed programme could do; it is held back by the 5% rule meeting the 2% outside inflation. I have said this on the page (a sentence under the optimistic end and in the chart's caption), and described it as a finding about the rule, not a proposal to change it. Whether the rule should index at a lower threshold is your design call; the model simply does what the Hub's rule says.

### 4b. The Hub's own targets (poverty under 2%, Gini 0.25 to 0.30 at Year 7)

The page now shows them beside the results. They are in the Hub's Integrated Implementation Roadmap (Success Metrics by Year 7; Appendix I). What the model reaches:

| Environment, years | Gini of disposable income: no programme | Compassionism | Gini counting price cuts | Unhoused share | Poverty measures under 2%? |
|---|---|---|---|---|---|
| Reference, 20 years | 0.292 | 0.276 | 0.230 | 0.19% | none (lowest: 18.7%) |
| Adverse, 20 years | 0.378 | 0.350 | 0.249 | 0.35% | none (lowest: 33.1%) |
| Stress Test, 20 years | 0.378 | 0.371 | 0.321 | 0.55% | none (lowest: 54.9%) |
| Reference, 40 years | 0.306 | 0.266 | 0.223 | 0.15% | none (lowest: 14.8%) |
| Adverse, 40 years | 0.637 | 0.556 | 0.258 | 0.56% | none (lowest: 51.7%) |
| Stress Test, 40 years | 0.637 | 0.626 | 0.397 | 0.73% | none (lowest: 72.3%) |

Reading it plainly:
- **No poverty measure comes near 2%.** The Hub does not say which measure its 2% is, so each of the model's is shown against it. The model's measures are stricter than the official rate (the Hub starts from about 12%), so none of them is the Hub's rate.
- **The unhoused (extreme poverty) figure is under 2% in every case, but it starts at 0.22% by construction**, so that is not evidence for the programme.
- **The model's no-programme Gini is already below the Hub's starting 0.48** (0.29 to 0.38 at 20 years, up to 0.64 at 40 in the Adverse and Stress environments). The model does not start where the Hub's path starts, so the Gini rows are not a test of that path. Counting the value of price cuts as well, the Reference and Adverse results at 20 years are at or just under 0.25.
- The Hub dates its targets at Year 7; the model reports its last year (20 or 40).

### 4c. One Gini reading sits exactly on a line

The Adverse Environment's Gini counting price cuts at 20 years is 0.2495, with a sampling error of 0.0004. The usual small-population correction for the Gini formula (a factor of 500/499) would put it at 0.2500, just on the other side of 0.25. I did not apply the correction (it would move every documented Gini). Any reading within 0.002 of a line is labelled "on the line" on the page. My first draft of the table's note said no verdict depended on the correction; the precise figure showed that was wrong, and I changed the note before anything was published.

### 4d. Prices: the typical run, and what runaway means

The price level compounds, so the average over runs sits above the typical run. The page now gives the typical run (the median) and where nine in ten runs fall. Above 1,000 times today's prices, it says the model's price rule has no central bank, no interest rate and no protection for savings, so prices run away in that environment; that is a limit of the model, not a forecast. The exact figures are on the replication page:

| Environment, years | Typical run (median) | Nine runs in ten | Mean over seeds |
|---|---|---|---|
| Reference, 20 years | 294 times | 246 to 353 | 297 |
| Adverse, 20 years | 1,824 times | 1,460 to 2,287 | 1,848 |
| Stress Test, 20 years | 84 times | 66 to 110 | 86 |
| Reference, 40 years | 31,559 times | 22,764 to 43,396 | 32,344 |
| Adverse, 40 years | 709,069,754 times | 363,054,826 to 1,439,605,682 | 819,027,776 |
| Stress Test, 40 years | 392,531 times | 195,264 to 804,723 | 449,761 |

### 4e. Page and harness: a wider comparison, and three differences the audit did not count

The check that the page and the Node copy of the model agree now covers the no-programme baseline and all eleven readings in all three environments at 20 and 40 years, plus every top-level name the two share (170 of them). The audit's two known differences are there (two display-only poverty-line keys; the tier colours). Beyond them there are three functions that differ in code: one returns the tier's colour for the page, one has a legacy random-sampler branch that is off by default, and one adds a basic-income term that is zero everywhere except the comparison designs. None enters the release run, which the row-by-row comparison confirms. All five are listed with their reasons, and the check fails if one stops being true.

## 5. Other things added

- The price level, Gini and extreme-poverty figures are now in the 500-run files, with a fingerprint of how they were made (the exact code version, the model's source files and the Node version). The tests check the fingerprint, so the model cannot change without the 500-run figures being regenerated.
- A test runs the model with each module added in turn (project hiring, the community businesses' payroll, the other modules, prices, labour, everything together) and checks the books balance, results repeat exactly, no module draws a random number, and no switch is left on. Nothing was wrong; I broke things on purpose to be sure the test notices.
- The figures on the front door can be downloaded (CSV or JSON), with the version and the command that reproduces them; a view can be linked (`?env=adv&years=40`); the numbers of tests quoted in the README and CONTRIBUTING are checked by the tests themselves, so they cannot drift again.
- The walk-through video was rebuilt (same voice, new figures, title card v5.1). The builder always rebuilds the whole video from the page, so the narration was regenerated too.

## 5b. For the next model round (your decision d146 in the ledger)

Two findings from this release belong at the top of that round:

1. **The no-programme run against US data.** The model's no-programme Gini of disposable income is 0.29 (Reference) to 0.38 (Adverse and Stress) at 20 years, below the Hub's starting 0.48. Checking the baseline against US data is already on the list; this is the first number to check.
2. **Savings and the indexing rule.** The wealth-poverty weakness in the Adverse and Stress environments is tied to two rules about prices: savings are not protected from inflation, and the BU is indexed only above 5% a year. The backing-share chart shows that with the BU indexed every year the fully backed Adverse Environment's wealth poverty falls from 52.5% to 31.8%. Both rules are the Hub's design as modelled; the round should look at them together.

## 6. Limits

- No independent economist has reviewed any of this.
- The backing-share chart is a sweep of a design parameter, not a forecast; the Hub does not give the share.
- The tests I wrote were each checked by breaking the thing they guard; a test I could not make fail would not have been kept.

## 7. Where things are

`dev/DECISIONS.md` (Session 34), `dev/PROGRESS.md`, the 500-run files and their commands in `dev/runs/` (`v51-*`), `dev/tools/backing_chart.py`, `dev/tools/cola_check.js`, the chart and the Hub-target table on `replication.html`.
