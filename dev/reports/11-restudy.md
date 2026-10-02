# Step 11 report: the restudy, every mechanism in

Oct 1-2, 2026 · plan step 11 · Claude · 500 paired seeds, three environments · this is the report the release gate asks Duke to read

## What was run

Compassionism with everything built in steps 1-9, against no programme, on the same 500 simulated adults for 20 years, 500 times (each run with its own random draws, the same draws for both), in three environments:

- the **ESP split** (community businesses share their earnings; private ones keep theirs);
- the **production side** (community-business capacity built by reinvestment; output counted);
- **Source financing** (the Treasury issues BU and pays conversions; the cautious reading treats what it pays as new money except what output backs);
- **open enrolment** each year;
- **sourced costs** for community businesses and housing;
- today's **octave rule**;
- the **spending rule** matched to the US saving rate;
- **BLEI** first;
- the **public costs of homelessness** avoided.

The two former stand-ins (the octave wage raise and the inflation slow-down) are **off**, each kept as a labelled row.

## The main result

The ESP profit share goes to participating ESP workers only (your answer, recorded in the project ledger; steps 1-9 had used every ESP worker).

| Against no programme | Reference | Adverse | Stress |
|---|---|---|---|
| Below 30 days of basic living (your BLEI), share of adult-years | **25.2% vs 46.7%** | **41.0% vs 60.0%** | **57.0% vs 60.0%** |
| Same, design-neutral reading | 30.3% vs 46.7% | 48.9% vs 60.0% | 59.2% vs 60.0% |
| Typical adult's basic living covered at year 20 (your BLEI) | 125 days vs 41 | 24 days vs 3 | 6 days vs 3 |
| Below the cost of living, share of adult-years | **30.0% vs 55.2%** | **51.7% vs 78.2%** | **67.5% vs 78.2%** |
| Poverty severity (FGT2), change | -5.62 | -13.92 | -6.74 |
| Too little wealth at year 20 | **47.5% vs 52.0%** | **87.0% vs 82.6%** | **89.3% vs 82.6%** |
| Confirmed gain on all three measures? | **Yes** | **No** (wealth worse) | **No** (wealth worse) |
| Prices: rise a year from the programme | 39.7% | 51.0% | 23.3% |
| Hours worked | -6.7% | -10.2% | -4.8% |
| Cost per adult a year (today's dollars) | $27,635 | $26,106 | $10,469 |
| Wage contribution (for community price cuts only) | 5.0% | 7.5% | 3.5% |
| Taking part at year 19 | 77.8% | 77.8% | 39.9% |

Every 95% interval is narrow (within about ±0.2 points), so these differences are not chance.

**In everyday words:**

- **At the reference settings Compassionism cuts poverty on every measure.** About half as many adult-years fall below the cost of living, half as many fall within a month of not covering basic living, and somewhat fewer people end with too little savings.
- **In the Adverse Environment and the Stress Test it cuts poverty measured on income and on BLEI, but more people end with too little savings than with no programme.** Prices rise fast (23-51% a year in the model), the allowance keeps its value through the cost-of-living adjustment, but savings do not.
- **Everyone has more real income than with no programme** (at reference: participants +$24,844 a year, non-participants +$3,167, the poorest third +$16,064, the richest third +$25,583). The groups that are worse off are worse off only on savings: non-participants and the richest third at reference; every group in Adverse and Stress.
- **Public costs avoided are small:** homelessness falls by about half at reference, saving $22 to $209 per adult a year, under 1% of the programme's cost.

## What decides it: how much real output the rewards call forth

| | Reference | Adverse | Stress |
|---|---|---|---|
| Release (cautious end): too little wealth at year 20 | 47.5% | 87.0% | 89.3% |
| If essentials bought with BU count as backed | 37.7% | 78.8% | 84.0% |
| If every Source dollar is backed (H1, optimistic end) | **21.8%** | **58.1%** | **73.8%** |
| No programme | 52.0% | 82.6% | 82.6% |

At the optimistic end the gain is confirmed in all three environments, and no group is worse off on any test. At the cautious end it is confirmed at reference only. The truth lies between, and the model cannot place it: it would need evidence on how much new production conversion rewards bring.

## Other readings (reference; change against the release row on poverty severity, basket poverty, wealth poverty)

- **Paid for by a wage contribution instead of the Source:** much worse (+22.4 severity; basket poverty 76.8%, wealth poverty 77.7%). The 84% contribution this needs is what made earlier versions look bad.
- **One split for every business (no private owners keeping their earnings):** better on income measures, slightly worse on wealth in Adverse and Stress (more new money).
- **Everyone joins:** better on income; more inflation.
- **Price cuts free:** a little better on all three.
- **The two former stand-ins on:** better on all three (−0.36 severity; wealth poverty 33.9%), but they are theoretical and stay off.

## Model limits that matter for these results

- The price rule is simple: new money raises prices in proportion to income, with no central bank, no interest and no protection of savings.
- Single adults only; one country (US); no places.
- Only homelessness is costed among the public costs avoided.
- No independent economist has reviewed the model.

## Release gate status

- **Built:** every step 1-9 mechanism; the page is rebuilt (step 12).
- **Restudy:** 500 seeds in three environments, done.
- **Checks:** validate, unit and domtest (97 of 97) pass.
- **Page and harness agree** on the same seeds.
- **Gains confirmed on basket and wealth poverty:** at reference yes; in Adverse and Stress, **no** (wealth poverty is worse). The gate asks that gains be confirmed. This report states plainly where they are not, rather than calling them gains.
- **Former stand-ins off by default:** yes.
- **Duke has read this report:** pending.

## Exact commands and files

- `node harness.js testbed 500 release ref --json=dev/runs/release-panel-ref.json` (and `adv`, `st`), then `python3 dev/tools/merge_panel.py`.
- Outputs: `dev/runs/step11-release-500-{ref,adv,st}.txt` and `dev/runs/release-panel.json` (embedded in the page).
