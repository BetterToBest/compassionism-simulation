# The v5.4 round: labour and markets (report)

Oct 7, 2026 · v5.4 · Claude · 500 paired runs in each of the three environments, 20 years · design note: `dev/reports/v5-21-v54-design.md` (written before any code or run)

## What was asked

Five things (plan `dev/plans/v5.3-plan-prompt.md`, section 4): job loss and re-employment instead of automation as a straight pay cut; PTH as a housing balance sheet; PTF members leaving as well as joining, with capacity by sector; which assumptions the results depend on; risk measures. The plan also lists the disaster shock and a test of the 55% floor. Each is built behind its own switch; with every switch off, the release figures are unchanged (proved four times with `dev/tools/engine_lineage.js`, and the three checks pass).

## The short answer

- **Job loss matters more than the other four parts put together.** Once people can lose a job and come back at lower pay, the programme still cuts the share of adult-years below the cost of living by about the same amount (Reference: −29.8 points, against −28.3 before), but **its wealth result gets worse in Reference**: adults with too little wealth at the end rise by +11.5 points against no programme, against +5.5 before. In Adverse and Stress it is the other way round: modelling automation as job loss instead of a pay cut for everyone is gentler on both runs, and the programme's wealth gap narrows (+36.1 against +40.6 in Adverse).
- **Most of that comes from one design parameter**, the pay cut after a permanent job loss (0 to 20%, main 10%): with no cut, the Reference wealth gap is +6.8; with a 20% cut, +16.5. No primary source fixes this number for all permanent job losers, so it stays a labelled design parameter, and the report shows the range.
- **PTH's books balance, and the homes' gains go mostly to the community.** Over 20 years a PTH home is worth about $99,000 (year-0 dollars) against $27,000 of debt; members hold about $7,000 of Acre Equity and the community about $65,000. Members' own wealth results hardly move.
- **PTF by sector gives members a smaller cut than the flat 12%** (6.8% of their cost of living, food and utilities only), lowers the programme's cost by about $1,100 per adult-year, and leaves the headline results almost unchanged.
- **The 55% floor never switches on in the released model**, and moving it changes almost nothing (details below).
- **What the results depend on most:** how many people take part and the BU amount, then the income effect (how much unconditional money reduces earnings) and, for wealth, the share of extra cash people spend.

## 1. Losing a job and finding another (`EMPL`)

**What changed.** Each year an adult at work can lose or leave their job into unemployment (8.5% a year in normal years, 14.2% in recession years; BLS Current Population Survey flows), is out of work for a spell drawn from the measured lengths (about 12 weeks on average in the model; 15% of spells longer than 26 weeks), and comes back. A permanent loss (41% of spells) cuts pay on return by 0-20% (mean 10%). Unemployment insurance is paid in both runs as in the US (27% of spells insured, 32% of pay, up to 26 weeks). In Adverse and Stress the automation wave now works through extra job loss in high-risk occupations instead of slower pay growth for everyone. Occupations (700, with Frey and Osborne's risks) follow pay rank.

**Results (500 runs; no programme → Compassionism, change in points).**

| | Reference | Adverse | Stress Test |
|---|---|---|---|
| Below the cost of living, v5.3 | 45.1% → 16.7%, −28.3 | 72.1% → 33.7%, −38.4 | 72.1% → 56.6%, −15.5 |
| … with job loss | 49.2% → 19.4%, −29.8 | 66.0% → 31.4%, −34.6 | 66.0% → 52.6%, −13.4 |
| Too little wealth, v5.3 | 30.5% → 36.0%, +5.5 | 48.8% → 89.4%, +40.6 | 48.8% → 86.3%, +37.5 |
| … with job loss | 32.6% → 44.1%, +11.5 | 45.1% → 81.1%, +36.1 | 45.1% → 76.2%, +31.2 |
| … with job loss, no pay cut on return | 31.3% → 38.1%, +6.8 | 42.8% → 74.2%, +31.4 | 42.8% → 70.3%, +27.5 |
| … with job loss, 20% mean pay cut | 34.0% → 50.5%, +16.5 | 47.0% → 85.8%, +38.8 | 47.0% → 81.3%, +34.3 |
| Below 30 days of basic living (BLEI), v5.3 → with job loss | −14.9 → −14.8 | −13.4 → −14.0 | +5.6 → +3.8 |

Every interval is within ±0.3 points of the figure shown.

**Why the programme's wealth result worsens in Reference.** A pay cut pushes people across the wealth line only if they are near it. With the programme, real savings sit much closer to the line (prices rise about 48% a year in Reference, and savings that do not keep up lose value), so the same cuts push more programme adults under it. This is the model's existing inflation result showing up through a new door, not a new flaw of the design.

**Smaller findings.** Unemployment insurance changes almost nothing (it replaces about 7% of the pay lost to unemployment, because only a quarter of spells are insured and the benefit is a third of pay). The model's unemployment is 2.4% of adult-years in Reference (3.6% in Adverse), below the official 4.2%, because the model has no one entering the labour force from outside it (a stated limit). Occupation follows pay rank exactly: the spread of pay across occupations in the data is larger than the model's whole spread of pay, a limit carried from earlier rounds.

## 2. PTH as a housing balance sheet (`PTHB`)

**What changed.** Each PTH home now has the trust's books: its value (18.2 years of its market housing cost; Federal Reserve and BEA), land (38%), upkeep (2.3% of the building a year), property tax (0.65%), debt (at 1.8% above the price rise), the member's Acre Equity and the community's equity. The identity "homes − debt = members' equity + community equity" is checked for every home every year and holds. Acre Equity grows with the home but at most at the price rise + 2% (your cap; question d175). Members leave the network at renters' rate of moving to another county (6.2% a year) and take 40% of their equity in cash (your Real Estate paper's figures; question d174); the next household waiting moves in.

**Results (Reference, end of year 20, year-0 dollars per home).**

| | Value | Debt | Members' equity | Community equity |
|---|---|---|---|---|
| Your cap (main) | $98,841 | $27,286 | $6,862 | $64,693 |
| The old 3-5% rule | $98,841 | — | $1,010 | $74,183 |
| Leavers take all their equity | $98,841 | — | $6,862 | $59,915 |

- The trust's rent and members' contributions cover its real costs in 93% of home-years (Reference).
- Of the homes' yearly gain (per home-year), about $34,700 is only the general price rise, $1,900 is real growth, and the community keeps nearly all of it ($34,100) beyond the members' credit.
- Under the old 3-5% rule, members' equity shrinks to almost nothing in real terms: prices rise far faster than 3-5% a year with the programme. Your cap keeps it growing with the homes.
- Headline results barely move (too little wealth with the programme: 36.0% → 35.9% in Reference), because Acre Equity is a small part of members' wealth and PTH members are a fifth of adults.

## 3. PTF by sector, and members who leave (`PTFS`)

**What changed.** A member's cut is now built from sectors: food at your BLEI paper's ε of 2.64 (62% off; 1.65 when fewer than 40% of adults are members, your paper's words), utilities at ε 1.80 (44% off, on the 13% of housing costs that are utilities; BEA 2025), and nothing yet for transport, health care and childcare, where the Hub gives no figure (swept to 12% and 25%). Members leave when they move to another county (3.2% a year; Census) and can join again.

**Results.** The cut is 6.8% of a member's cost of living (16.2% if the other sectors get 25%), against the flat 12% before. The programme's cost falls by about $1,100 per adult-year; poverty and wealth results move by under a point. Leaving lowers average membership from 28% to 22% of adults in Reference.

## 4. The disaster shock (`DIS`)

In Year 7 a quarter of households lose $10,000 and four weeks' pay; half get FEMA's average award ($3,092; OpenFEMA, 2018-2026 disasters) in both runs; the programme adds 20% of the year's BU for hit participants (the Recession Protocol's figure; the disaster protocol gives none). The disaster's own effect is about the same with and without the programme: hit adults trail unhit ones in getting back to their earlier real wealth by about 10 points at three years in both runs (Reference: 61% against 72% without the programme, 26% against 36% with it). Everyone takes longer with the programme because prices rise faster, so the programme does not speed recovery from a disaster in this model. Larger disasters (half of households, $25,000, 12 weeks) change headline results by about a point.

## 5. The 55% floor

The released model measures the floor by the share of adults who are PTF members. Membership is capped at 18% in Reference and 8% in Stress, so the network synergy is zero in every released run (my design note said it read Social Zone cohesion; that was wrong, and is corrected here). Raising the membership cap from 20% to 90% under floors of 40%, 55% and 70% (20 paired runs per point) moves results smoothly and slightly: the programme's cut in time below the cost of living grows from 30.2 to 31.1 points in Reference, whichever the floor. There is no cliff at 55%, and the floor's level hardly matters. Higher membership also raises the programme's cost and its wealth gap a little.

## 6. Which assumptions the results depend on

**Three kinds of uncertainty.**
- **Run to run** (same settings, different random draws): one run's programme effect varies by about 2 points (standard deviation; 100 runs per environment); over 500 runs the average is known to about ±0.1 points.
- **Parameters** (Morris screening of 17 inputs over their ranges, Reference, 10 trajectories of 10 paired runs; table below). Sobol total indices for the six leading inputs (section 6b) confirm it: participation and the BU amount explain most of the spread in poverty, BLEI, cost and inflation; the spending share and the income effect most of the spread in wealth.
- **Structure** (different models, not different numbers): the readings above. For too little wealth in Reference, the programme's effect runs from +5.2 (PTH leavers keep all their equity) to +16.5 (job loss with a 20% pay cut), a far wider spread than run-to-run noise.

**Morris screening, Reference: the inputs that move the programme's effect most** (mean absolute effect of moving the input across its range).

| Measure | Leading inputs (effect in points, or $ for cost) |
|---|---|
| Below the cost of living | participation 17.8, BU amount 9.7, the BLEI wage gain 6.1, income effect 5.9 |
| Too little wealth | share of extra cash spent 21.2, income effect 9.4, participation 8.1, pay cut after job loss 7.9, BU amount 5.8, job-loss rate 4.9 |
| Below 30 days of basic living | participation 16.1, BU amount 5.5, income effect 1.8 |
| Cost per adult | participation $15,265, BU amount $10,503, conversion tax $1,640, top conversion rate $1,322 |
| Programme inflation | participation 29.8, BU amount 12.1, income effect 4.2 |

PTF and PTH inputs (membership ceiling, uptake, leaving rate, sector cuts), Social Zone cohesion and the number of octaves are near the bottom for every measure.

### 6b. Sobol indices

Total-effect indices (the share of the spread in the programme's effect that each input causes, alone or with others), for the six inputs Morris ranked highest, each over its range with the others at their main values (64 base points, 512 settings of 10 paired runs each, per environment):

| Measure | Reference | Adverse |
|---|---|---|
| Below the cost of living | participation 0.67, BU amount 0.20, BLEI wage gain 0.07, income effect 0.06 | participation 0.59, BU 0.26, income effect 0.09 |
| Too little wealth | share of extra cash spent 0.51, income effect 0.15, BU 0.10, participation 0.08, pay cut 0.07 | spending share 0.38, income effect 0.20, pay cut 0.11, participation 0.10 |
| Below 30 days of basic living | participation 0.89, BU 0.13 | participation 0.82, BU 0.17 |
| Cost per adult | participation 0.61, BU 0.35 | the same |
| Programme inflation | participation 0.80, BU 0.16 | participation 0.79, BU 0.16 |

With 64 base points the first-order indices are rough (some come out slightly negative, which is sampling error), so the total indices are the ones to read; they agree with the Morris ranking. Totals above the first-order index (participation, the spending share) mean those inputs work mostly through interactions with the others.

## 7. Risk measures (`RISK`)

Reference, v5.3 main result, no programme → Compassionism:
- **Falling back below the cost of living** within five years of climbing above it: 55% → 37% (the PSID's figure for the official poverty line is about half). Adverse: 95% → 56%.
- **Largest fall in BLEI days** (median adult): 0 → 389 days. With the programme people hold far more days of basic living, so their largest fall is larger in days; the measure reads the size of a swing, not its harm.
- **Largest fall in real wealth** (median adult): 0.1 → 22.9 months of basic living; 68% of adults lose more than six months of basic living from a peak with the programme against 25% without. This is the programme's inflation eroding savings again.
- **Income shocks** (a year with real cash income under 80% of the year before): with job loss on, 3.7 per 100 adult-years with no programme and 3.9 with it; half recover within three years with the programme (49%), against 60% without.

## 8. The predictions, checked

| Prediction (design note, section 3) | Held? |
|---|---|
| Job loss raises time below the cost of living with no programme by 1-4 points in Reference, more in Adverse | Reference +4.1 (just above); Adverse **fell** 6 points (automation through job loss is gentler than the old pay drag) |
| The programme's gain on the cost of living grows by 1-3 points | Reference yes (+1.5); Adverse and Stress no (smaller by 2-4) |
| Too little wealth rises in both runs; the programme's sign unchanged | Sign unchanged everywhere; in Adverse and Stress both runs fell |
| Income inequality rises 0.01-0.03 with no programme | Reference yes (+0.01); Adverse fell |
| Adverse: higher pay, poverty the same or higher | Higher pay yes; poverty lower |
| PTH members' wealth lower with the cap and exits | **No: higher** (the old rule lost value to inflation) |
| Too little wealth up 0.5-2 points with the balance sheet | No: unchanged |
| The trust's identity holds; community equity grows | Yes |
| PTF members' saving smaller than the flat 12% early on | Yes, smaller throughout (6.8%) |
| Below the cost of living up 0-2 points with PTF sectors | Yes (+0.3) |
| PTF membership 5-15% lower at the end | Lower by about a fifth (more than predicted) |
| About half fall back into poverty within 5 years with no programme; fewer with it | Reference yes (55% → 37%); Adverse 95% with no programme |
| BLEI drawdown smaller with the programme in Reference and Adverse | No: larger in every environment (see section 7) |
| Disaster recovery about a year faster with the programme | No: slower for everyone, with the disaster's own effect about equal |
| A step in results at the 55% floor under the density gate | No step |
| BU amount, conversion rate and spending share lead the sensitivity; PTF and PTH small | BU and spending share yes; participation leads; conversion rate small; PTF and PTH small yes |

## 9. Limits of this round

- The pay cut after job loss is a design parameter; it drives the largest new result.
- The model has no labour-force entrants, so its unemployment is below the official rate.
- PTF sectors share one capacity rule; the Hub gives no figures for transport, health care or childcare cuts.
- The disaster's damage and lost weeks are design parameters; emergency employment and Reconstruction Collectives are not modelled.
- Insurance for PTH homes and taxes on unemployment benefits are not modelled.
- The sensitivity study covers Reference (and Adverse for Sobol) at 10 runs per point.

## 10. What happens next

By the rule recorded before any run, each part joins the main result unless the restudy found a modelling error in it; none was found. Joining means remaking the release panels and the pages with the v5.4 parts as the main result (and the v5.3 result beside it), then version 5.4. That is the next step. Your three questions (d174-d176) stand: the figures above use the defaults.

## How these were made

From a clean worktree of commit aacaf24: `node dev/tools/v54_check.js ENV 500 --rows=v53,empl,emplPay,emplCut0,emplCut20,emplNoUI,pthb,pthbOld,pthbFull,pthbNone,pthbOwn,ptfs,ptfs12,ptfs25,ptfsStay,dis,disSmall,disBig,all,allDis --out=r500` (ENV ref, adv, st; `dev/runs/v54/r500-ENV.json`), `node dev/tools/gsa.js morris ref 10 10`, `node dev/tools/gsa.js noise ENV 100`, `node dev/tools/floor_test.js ENV 20` (ref, st). From clean worktrees of bb4522b (same engine): `node dev/tools/gsa.js sobol ENV 64 10 --params=part,bu,rho,spend,payCut,bleiBonus` (ref, adv). The noise and floor files record a "dirty" tree only because earlier output files of the same batch sat in it; no code differed.
