# Policy levers: what a government running the programme could set, and what each does (pilot, stages 1-3)

Nov 5, 2026 · research-update plan step S54 · study N · Claude

**PILOT.** Seeds 1-50 on GitHub Actions. These numbers decide only what the full study (seeds 1-500 to choose, 501-1000 to confirm, after the design freeze) must contain. They are not figures of the model and should not be quoted as findings. Stage 3 (the confirmation on fresh seeds 51-100) is reported below; it is labelled pilot too.

- Preregistration: research-update `prereg/2026-11-levers-addendum.md` (written before any run). Its Amendment 1 (Nov 5, after stages 1-2) lists stage 3's rows and how the analysis reads what the addendum leaves open.
- What each lever is, who would set it, its range and the expected direction, written before any run: `dev/reports/s54-levers-reading.md`.
- Every table: `dev/reports/s54-levers-tables.md`, written by `dev/tools/s54_levers.py` (committed before the results were read). The script uses a paired bootstrap over seeds: 2,000 replicates, resampler seed 54. Every cell, as CSV: `dev/runs/s54-levers/stage1-effects.csv.gz`, `stage2-effects.csv.gz` and `stage3-effects.csv.gz`.
- Per-seed results: compassionism-sim-results `s54-levers1-e6da050/` (stage 1, 520 rows per environment) `s54-levers2-e6da050/` (stage 2, 1,164 rows per environment) and `s54-levers3-e6da050/` (stage 3, 250 rows per environment). All three were made by engine e6da050; every checksum, row and key was verified by `s54_levers.py --check`.

## The question

The backing study (S51) found that the release row pays out about 60% of a year's earned income in new money, every year. In the model, prices rise with new money relative to output, so this becomes programme inflation of about 51% a year in Reference. Duke's answer to ledger decision D12 was to test every lever a government running the programme could set before choosing a fix.

The levers fall into three families:
- **Taking money back:** the conversion tax, its progression, a business tax, the Source keeping project sales, retiring expired BU, and outside finance.
- **Paying out less or more slowly:** the business conversion rate, the BU amount, the top multiplier, octave capacity, the number of octaves, the Phi tier, a phase-in, and an issuance cap.
- **Protecting value:** BU indexation, a protected savings account, and a rent cap.

Duke's rule (D13) picks the best setting:
1. **No harm first.** Adults outside the programme must be no worse off on basket poverty, wealth poverty, big income falls with no buffer, and having under three months of basics covered. Wealth poverty must be no worse than with no programme.
2. **Then** programme inflation must be under 5% a year.
3. **Then** the lowest basket poverty wins.

Each test must hold in all three environments: Reference, Adverse and Stress.

Two designs: **the release row** as released, and **the C2.2 design** (the BU indexed to the price of basic needs and given to everyone automatically). Two wage readings: wages keep up 100% or 90% with the programme's prices.

Each lever was compared with its own design under "joining that sees what joining pays". This is the test reading: an adult's decision to join also counts the conversion income they can expect after tax. At the released tax it is calibrated to give today's participation.

Reading notes for the numbers below:
- "Points" are percentage points of adults (or of adult-years). Inflation is in points a year.
- Unless a sentence says otherwise, numbers are for the release row at wages 100%, as means over the three environments.
- "Works" and "harms" are the preregistered verdicts: a change whose interval excludes zero, in all three environments ("works") or in any one environment ("harms"), against the design without the lever.

## In short

1. **No setting tested meets Duke's rule, in either design, at either wage.** Of 435 candidates per design (255 at 90% wages), none passed both the no-harm test and the inflation test on the choosing seeds. Rule 4 therefore chose no setting. On fresh seeds (stage 3), no point of the trade-off front passes the poverty, no-harm and inflation tests together either (item 8).
2. **Inflation is the barrier, and the levers inside the design cannot remove it.** Every lever that keeps the programme paying in new money leaves inflation above about 21% a year in at least one environment. Among the C2.2 settings that pass the no-harm test (175 of them, at 100% wages), the lowest is 45% a year.
   - The reason is the one the reading note gave before any run: the BU are spent at face value, and that face value is new money. The levers can only trim the premium paid on top of it.
   - At 2%, 4% and 8% the issuance cap gives identical results. The BU's face value alone is about 32% of earned income, so every cap removes the whole premium, and inflation is still about 32% a year.
3. **The conversion tax has no break-even within 0-40%.**
   - *Self-funding:* not reached. At 40% the Source's new money is still 48-59% of earned income in Reference and Adverse, and 23% in Stress.
   - *Lowest basket poverty:* the 0% rate, in every design, wage and environment.
   - *Deterrence:* not reached. Participation barely moves with the tax: at most about 1 point across 0-40% (83.6% at 12% against 83.5% at 40% in Reference).
   - Duke recalls an earlier engine with a break-even at about 8-12%. Nothing like it appears under either joining reading.
4. **Only outside finance brings inflation under 5%, and then someone else pays.**
   - *C2.2 with a flat contribution on wages:* inflation 0.1 points a year, basket poverty down 18-29 points, wealth poverty down 18-28 points. It is the setting closest to meeting the rule. It fails on one test: big income falls with no buffer become more common, by 1.4 to 5.2 per 100 adult-years.
   - *The release row with the same contribution:* worse than no programme. Basket poverty rises 6-19 points and non-participants' basket poverty rises 14-34 points.
5. **Levers that help somewhat, in both designs:**
   - The Source keeping project sales.
   - The rent cap for BU tenants.
   - A slower phase-in, which lowers inflation in the release row and, there, also wealth poverty.
   - Fewer octaves, in C2.2.
   - Retiring expired BU, the protected account paid with new money, enforced octave capacity, a smaller top multiplier and the rent risk all harm.
6. **The protected savings account runs away when the Source pays for it with new money.** Protecting all savings gives about 1,100-1,400% inflation a year (release row, full wages). Rule 8 says to report this as it is, not drop it. A capped account (the first $10,000) cuts wealth poverty by 18 points but adds 10 points of inflation a year.
7. **In combination (Morris screening), two factors dominate:** the protected account and the BU amount. The structural levers (octaves, Phi tier, progression, recycling) barely matter once the others are set.
8. **Stage 3, on seeds never used to choose (51-100), confirms the picture.** Of 246 points of the front, three pass the poverty and no-harm tests in every environment, all in the C2.2 design: the Source keeping half of project sales (wages 100%), and the capped protected account (wages 100% and 90%). All three run at 29-82% inflation a year, so they are confirmed points of the trade-off front, not a best setting. No release-row point passes. The flat wage contribution (C2.2) is again the only point under 5% inflation everywhere, and it fails again on big income falls, by the same amount as on the choosing seeds.

## What was run

- **Stage 1:** each lever on its own: 65 programme rows per design and wage, each also with savings that keep up with prices (the second savings reading).
- **Stage 2:** all 17 levers together: a Morris screening (10 trajectories of 18 points) and a 200-point Latin hypercube per design and wage.

Both stages ran on seeds 1-50 in Reference, Adverse and Stress, with 500 adults over 20 years. Every comparison is paired on the same seeds.

## The two designs against no programme (the starting point)

| Design (wages 100%) | Environment | Basket poverty | Wealth poverty | Programme inflation (points a year) | Participation | Non-participants' wealth poverty |
|---|---|---|---|---|---|---|
| release row | Reference | -29.8 | +11.4 | +50.8 | 83.6% | +27.9 |
| release row | Adverse | -35.1 | +36.2 | +60.9 | 83.7% | +44.9 |
| release row | Stress | -13.4 | +31.5 | +27.7 | 44.1% | +39.1 |
| C2.2 design | Reference | -25.5 | -19.9 | +37.7 | 100% | -19.4 |
| C2.2 design | Adverse | -36.1 | -23.5 | +44.3 | 100% | -23.3 |
| C2.2 design | Stress | -35.3 | -11.3 | +46.3 | 100% | -10.9 |

Every change in this table has an interval that excludes zero.

The release row cuts basket poverty but raises wealth poverty, most of all for adults outside it. Their savings lose value to the programme's inflation and they get nothing back. With savings that keep up with prices (the second reading), the release row's wealth poverty falls instead: by 20 points in Reference.

The C2.2 design gives the BU to everyone and raises it with the price of basic needs. Its wealth poverty falls, and its "non-participants" (the adults who would not have chosen to join) receive the BU too. It fails the no-harm test only narrowly: big income falls with no buffer rise by 0.16 per 100 adult-years in Reference (interval +0.07 to +0.24).

The two designs measure need against different cost-of-living lines, so their levels are not comparable with each other; each is compared only with its own no-programme run.

## Each lever on its own (stage 1)

### Taking money back

- **Conversion tax (0-40%).** In the release row a higher tax trades basket poverty for inflation.
  - At 0%: basket poverty 2.6 points lower than at the released rate, inflation 2.8 points a year higher.
  - At 40%: basket poverty 5.3 points higher, inflation 6.3 points lower, and inflation is still 44% a year in Reference.
  - In the C2.2 design a higher tax raises both basket poverty and inflation; a lower tax lowers both. In the model, the tax lowers what project work pays after tax, so project hours fall (hours change +3.7% at a 0% tax, -4.0% at 40%, Reference). Prices rise with new money relative to output, so the lost output outweighs the money the tax takes back.
  - The tax hardly changes who joins. In the release row participation moves by at most about 1 point across the whole range; in C2.2 everyone takes part. The joining rule weighs the BU an adult would use together with their expected conversion income after tax. That participation hardly moves means the BU outweighs conversion income for almost every adult near the margin.
- **Progression and its cap.** Small effects. A steeper progression (8 points per rate point above 3x) raises basket poverty about 0.4 points, cuts inflation about 0.3 points and lowers participation about 0.6 points. Removing progression does the reverse. The 4-point progression with a 50% cap repeats the design's own setting and moves nothing (a built-in check).
- **A separate tax on business conversions.**
  - No business tax: basket poverty 2.1 points lower, inflation 2.4 points higher.
  - A 75% business tax: inflation 15.5 points lower, basket poverty 10.5 points higher.
- **The Source keeps part of the projects' sales and retires it.** This works on every primary outcome in both designs, but modestly.
  - Release row: keeping 50% cuts inflation by 0.8 points and wealth poverty by 0.5.
  - C2.2: keeping 50% cuts inflation by 9.7 points and wealth poverty by 5.3, and lowers basket poverty.
  - The one cost is a tiny rise in big income falls for non-participants (about +0.01 to +0.10 per 100 adult-years).
- **Retiring expired BU instead of paying them to project work.** This harms in both designs, strongly in C2.2: retiring all of them raises wealth poverty by 26 points and basket poverty by 4. The recycled BU pay for project work, which is income to the people who do it.
- **Outside finance** (the payout financed by a tax rather than new money).
  - *Flat contribution on wages:* removes programme inflation entirely.
  - *Land-value tax:* leaves 1-14 points a year.
  - *Progressive income tax:* does worse than the flat contribution on every primary measure, in both designs. In the release row it is worse than no programme (basket poverty +12 to +21 points). In C2.2 it raises wealth poverty above no programme in Adverse and Stress (+32 and +47 points).
  - In the release row, the flat contribution and the progressive income tax make basket poverty worse than with no programme, most of all for non-participants, who pay without receiving. The land-value tax keeps a basket-poverty gain (17 points in Reference), but non-participants' wealth poverty rises in Adverse (+35).
  - In C2.2, where everyone receives the BU, the flat contribution keeps large gains in every environment (basket poverty -18.5, -29.5 and -25.7; wealth poverty -18.4, -27.7 and -25.0; Reference, Adverse, Stress). But big income falls with no buffer become more common for everyone: +5.2, +3.7 and +1.4 per 100 adult-years, from about 0.9 without the programme.
  - The pilot has not traced why. The full study's descriptive measure of money-income falls by cause (S53, Amendment 1) is the tool for it.

### Paying out less or more slowly

- **Business conversion rate (1x, 1.5x, 2x instead of 3x), BU amount (60%, 80%), issuance cap (2%, 4%, 8%).** All three cut inflation by the same route: less new money. All three cost basket poverty.
  - A 1x business rate: inflation 15.9 points lower, basket poverty 9.9 points higher.
  - 60% of the BU: inflation 15.4 points lower, basket poverty 9.0 points higher.
  - Any issuance cap: inflation 17.3 points lower, basket poverty 12.0 points higher. The three caps give identical results because each removes the whole premium above face value (the cap is met in no year).
  - In C2.2 the same levers raise wealth poverty by 15-30 points.
- **Phase-in over 5 or 10 years.** This lowers inflation (10 years: 4.2 points a year less) and basket poverty rises by 2.5 points. In the release row it also lowers wealth poverty (1.1 points) and improves non-participants' months of cover.
- **Top multiplier, octave capacity, number of octaves, Phi tier.** Small effects, mostly harmful when the design's own setting is changed.
  - Enforcing octave capacity raises wealth poverty (0.5-1.5 points in the release row; 18-23 points in C2.2).
  - Two octaves instead of the design's number helps a little in C2.2: basket poverty -0.4, inflation -1.8.
  - Turning the Phi tier off changes almost nothing.

### Protecting value

- **BU indexation.**
  - Release row: the 5% surge protocol and every-year indexation give identical results, because programme inflation is above 5% every year, so the surge fires every year anyway.
  - Release row: indexing to the price of basic needs lowers basket poverty by 1.1 points and raises participation by 1.2 points, at 1.2 points more inflation.
  - C2.2: moving away from basic-needs indexation harms (wealth poverty +3.2).
- **The protected savings account, paid for by the Source with new money.**
  - Protecting all savings runs away: about 1,100-1,400% inflation a year in the release row at full wages, more at 90%. Wealth poverty falls because savings are protected by construction, but basket poverty rises 16 points.
  - The capped account (the first $10,000 a person) cuts wealth poverty by 18 points and non-participants' wealth poverty by 15, at 9.7 points more inflation a year.
- **Rent cap for BU tenants.** Small gains in both designs: basket poverty -0.5 (release row) and -0.3 (C2.2); inflation -0.2 and -1.5. Landlords bear it. The model has no housing supply response, which favours this lever.
- **Rent risk** ($1.41 of higher rent per BU dollar). This harms in both designs (basket poverty +6.0 in the release row). With the rent cap added, C2.2 is exactly as with the cap alone. In the release row the combination still raises non-participants' big income falls (+4.3 per 100 adult-years).

### At wages 90%

The same pattern holds. Inflation is higher, wealth poverty is worse, and the release row's basket-poverty gain shrinks to 2-13 points.

Outside finance gives the same result at both wages: with no programme inflation, wage indexation to it has nothing to index.

## The conversion tax's three break-even rates (Q21)

| Design | Wages | Self-funding rate | New money at the released rate / at 40% (Reference, % of earned income) | Lowest basket poverty | Deterrence rate |
|---|---|---|---|---|---|
| release row | 100% | not reached by 40%, in every environment | 59.7 / 48.3 | 0% everywhere | not reached by 40% |
| release row | 90% | not reached by 40% | 82.3 / 65.5 | 0% | not reached |
| C2.2 design | 100% | not reached by 40% | 51.3 / 45.1 | 0% | not reached (everyone takes part) |
| C2.2 design | 90% | not reached by 40% | 68.0 / 60.2 | 0% | not reached |

No bootstrap replicate reaches self-funding or deterrence. Today's joining rule gives the same answers (rule 3).

Self-funding cannot be reached because the BU are spent at face value, and that face value is new money that no conversion tax below 100% takes back (rule 2; the reading note said so before any run). Deterrence is not reached because participation hardly responds to the tax.

## All levers together (stage 2)

**Morris screening** (descriptive; no claim rests on it):
- In the release row, the factors that move basket poverty most over their full ranges are the protected account (11 points), the BU amount (7 points in Reference, 3 in Stress), then the issuance cap, the business rate and the business tax (under 1 point each, with large spreads).
- Everything else moves basket poverty by less than half a point once the other levers vary: indexation, the rent cap, the tax, the multiplier, phase-in, octaves, Phi tier, progression and recycling.
- Inflation is dominated by the protected account (its runaway) and the BU amount.
- C2.2 looks the same, with the BU amount first.

**Recycling does nothing in combination.** In the release row, the share of expired BU recycled to projects changed nothing in any trajectory. That is not a fault of the job: BU expire unspent only when the BU is near its full amount (seed 1: 548 at the full BU, 109 at 87%). Most combinations leave nothing for the share to act on. These were seed-1 checks on the session machine, not preregistered, and they explain the null result.

**The trade-off front** (basket poverty, wealth poverty, participation and inflation, averaged over the environments):
- Release row: 162 points at wages 100%, 74 at 90%. Every one of them fails the no-harm test in some environment, mostly on non-participants' wealth poverty and months of cover.
- C2.2 design: 5 points at each wage, the same five: no conversion tax; the Source keeping half the projects' sales; the capped protected account; the flat wage contribution; the land-value tax.

## The best setting by Duke's rule: none on these seeds

| Design | Wages | Candidates | Pass no harm | Also under 5% inflation | Closest (what fails) |
|---|---|---|---|---|---|
| release row | 100% | 435 | 0 | 0 | land-value tax (non-participants' wealth poverty and security; inflation 5.3 and 13.5 points in Reference and Adverse); the next four are stage-2 points with inflation over 20% |
| release row | 90% | 255 | 0 | 0 | land-value tax; flat wage contribution (non-participants' basket poverty +13 to +34) |
| C2.2 design | 100% | 435 | 175 | 0 | flat wage contribution (only big income falls: +1.4 to +5.2 per 100); land-value tax (income falls, and inflation 5.0-6.1) |
| C2.2 design | 90% | 255 | 0 | 0 | flat wage contribution; land-value tax |

Rule 4 says that when no setting meets the rule, none is reported as a finding. Stage 3 reruns every point of the front on seeds 51-100 (research-update addendum Amendment 1), so the front itself is confirmed or not on seeds that played no part in choosing it.

## Stage 3: confirmation on fresh seeds

**What ran.** Every point of the trade-off front (246 settings) and each design's no-programme row, on seeds 51-100, which played no part in choosing them. That is 250 rows per environment, in Reference, Adverse and Stress (study `s54-levers3`, engine e6da050, compassionism-sim-results run 42112585864, 25 shards; folder `s54-levers3-e6da050/`; checksums and `--check` pass). The settings file matches the one listed in research-update addendum Amendment 1 (SHA-256 `6b906101...`). Every cell is in the tables' stage 3 section and in `dev/runs/s54-levers/stage3-effects.csv.gz`.

**The test** (decision rule 5), in every environment:
- basket poverty falls (the interval of the change against no programme lies below zero);
- each no-harm measure (non-participants' basket poverty, wealth poverty, big income falls with no buffer, and under three months of basics covered; and wealth poverty overall) has its interval's upper end at or below +0.5 points;
- programme inflation's upper end is under 5 points a year. For points of the front this is reported, not required.

Rule 4 chose no setting, so stage 3 cannot confirm a best setting. A point that passes is a confirmed point of the trade-off front, reported with its inflation.

| Design | Wages | Points tested | Pass poverty and no harm | Of those, inflation under 5 points everywhere | Under 5 points everywhere, any |
|---|---|---|---|---|---|
| release row | 100% | 162 | 0 | 0 | flat wage contribution only (fails no harm) |
| release row | 90% | 74 | 0 | 0 | flat wage contribution only (fails no harm) |
| C2.2 design | 100% | 5 | 2 | 0 | flat wage contribution only (fails no harm) |
| C2.2 design | 90% | 5 | 1 | 0 | flat wage contribution only (fails no harm) |

**The three confirmed points** (change against no programme on seeds 51-100, Reference / Adverse / Stress):

| Point | Basket poverty | Wealth poverty | Non-participants' big income falls, per 100 adult-years | Programme inflation, points a year |
|---|---|---|---|---|
| C2.2, wages 100%, the Source keeps half of project sales | -25.4 / -36.2 / -35.4 | -20.2 / -28.6 / -21.1 | +0.20 (+0.10, +0.30) / -0.33 / -0.71 | 28.7 / 33.4 / 37.1 |
| C2.2, wages 100%, capped protected account (first $10,000) | -25.2 / -35.7 / -34.6 | -20.2 / -29.0 / -27.2 | +0.09 (+0.00, +0.18) / -0.40 / -0.62 | 41.4 / 50.6 / 53.8 |
| C2.2, wages 90%, capped protected account | -23.9 / -31.4 / -26.9 | -19.6 / -25.8 / -19.8 | +0.12 (+0.02, +0.22) / -0.39 / -0.71 | 54.4 / 71.9 / 82.2 |

Each cuts basket poverty by 24-36 points and wealth poverty by 20-29 points, and harms no one beyond the margin. But prices rise by 29-82% a year. That inflation is why none of them is a best setting under Duke's rule.

These three failed rule 4's no-harm test on the choosing seeds, and pass rule 5 here. That is how the two rules were written, before any run: rule 4 asks for no harm at all (the seed mean at or below zero), while rule 5 asks that the interval rule out harm larger than half a point (a non-inferiority margin). Their one shortfall, in Reference only, is a small rise in non-participants' big income falls (+0.1 to +0.3 per 100 adult-years), inside that margin.

**What is not confirmed, and why:**
- *C2.2, no conversion tax; the land-value tax; the flat wage contribution:* non-participants' big income falls with no buffer rise beyond the margin in every environment (no tax +0.9 to +4.1 per 100 adult-years; land-value tax +1.0 to +4.3; flat contribution +1.4 to +5.2). The flat contribution keeps inflation at 0.1-0.2 points a year and cuts basket poverty by 18-29 points, the pilot's near-miss again.
- *C2.2 at wages 90%, no tax and half of project sales kept:* wealth poverty, overall and among non-participants, also rises in Stress, by 12 and 21 points (as on the choosing seeds).
- *Release row, every point:* most fail four no-harm tests at once: non-participants' wealth poverty, their months of cover, their big income falls, and wealth poverty overall (131 of 162 points at wages 100%). At wages 90%, every point also raises non-participants' basket poverty beyond the margin, in every environment. The nearest are three settings with the uncapped protected account: they fail only on non-participants' basket poverty in Stress (about +4 points), but at 1,100-1,400% inflation a year. The flat contribution leaves everyone worse off than no programme (basket poverty +6 to +19 points).

**The fresh seeds agree with the choosing seeds.** Across the 246 points, the estimates on seeds 51-100 differ from those on seeds 1-50 by a median of 0.1-0.4 points, depending on the outcome. The largest gaps on the poverty and no-harm measures are 2.3 points (C2.2) and 1.8 points (release row). For example, the flat contribution's rise in big income falls was +5.24, +3.70 and +1.43 then, and is +5.17, +3.68 and +1.43 now. The front's shape is not an artefact of the seeds that chose it.

**One identity explained.** Under the flat wage contribution, the two wage readings (wages keeping up 100% or 90%) give identical rows, in both designs and every environment. The model indexes wages to its general price level, which moves only with new money. A payout fully paid by tax creates none, so the wage reading has nothing to act on. The 0.1-0.2 points of inflation shown are in the prices of essentials, which the wage rule does not follow.

## What this means for the design (Duke's decision)

Inside the design as it stands, the model finds no lever setting that meets Duke's rule. The obstacle is the same one S51 found. The BU are new money at face value, and in the model new money relative to output sets prices. Every lever that keeps the payout large keeps inflation large. Every lever that cuts inflation cuts the payout, and with it the poverty gain.

The only route under 5% is to pay for the BU from outside, with a tax. That is a change to the design itself, not to the model of it, so it is Duke's call (decision rule 6; ledger decision).

The pilot's one near-miss is that route: the C2.2 design paid for by a flat contribution on wages. It cuts basket and wealth poverty by 18-30 points in every environment, with no inflation. Its one failure is more frequent big income falls, the cause of which is not yet traced. Stage 3 found the same failure, of the same size, on fresh seeds. If Duke wants it tested, it becomes a new row and a dated amendment before the freeze. The release row stays as released either way.

## Limits

- **Pilot:** 50 seeds to choose (1-50) and 50 to confirm (51-100); the full study uses 500 of each.
- **Two no-harm tests.** Choosing (rule 4) asks for no harm at all; confirming (rule 5) allows half a point. A point can therefore be confirmed that rule 4 would not choose, as three were here. Both are preregistered.
- **The model's price rule** is the quantity theory's: prices rise with new money relative to output. The model has no interest rates, exchange rate or asset market through which inflation could play out differently. All of this study's inflation figures rest on it.
- **The protected account** is paid by the Source with new money, the only means it has in the model. A real government could pay it from taxes; that row was not tested.
- **Outside finance rows** set the tax to fund the payout. The model has no tax avoidance or migration response beyond its labour response.
- **"Non-participants"** are the adults the model marks at the start as unwilling to join, the same adults in every row. Under C2.2 they receive the BU too.
- **Wealth poverty on ordinary savings** is the preregistered reading. With savings that keep up with prices (the `.sv` rows), the release row's wealth harm turns into a gain.

## What S47 carries

1. **Stages 1-3 as preregistered:** choose on seeds 1-500, confirm on 501-1000. Stage 2 may run at fewer seeds (at least 100) by amendment, since stage 3 confirms.
   - Runtime at 50 seeds was about 37 processor-hours for stages 1-2 together (11 and 26). Stage 3 took 5.9 processor-hours (142 seconds per seed per environment on one process, for 250 rows), so about 59 processor-hours at 500 seeds if the full study's front is the same size.
   - Unless Duke changes the design (above), the full study will most likely confirm that no setting meets the rule. Its value is then the intervals on each lever's effect and on the front.
2. **Output size:** 45 MB (stage 1) and 65 MB (stage 2) at 50 seeds, so about 1.1 GB at 500 seeds. Trim the keys or compress before the batch.
3. **The issuance-cap rows** (2%, 4%, 8%) are identical, because each cap removes the whole premium. Keep one, or, if Duke wants a cap on the face value itself, that is a new lever and a dated amendment.
4. **Big income falls under outside finance.** Run S53's descriptive measure of money-income falls by cause on the outside-finance rows, so the full study can say why the C2.2 flat-contribution row has more of them.
5. **On S52's main shock path:** whatever the full study's stage 3 confirms (S52 addendum). In the pilot, that is the three C2.2 points above.
6. **Already carried:** S53's security measures (`secU25`, `secM3`) on both savings readings in every lever row.
7. **The flat contribution's 90% wage row** is identical to its 100% row (no new money, so nothing for wage indexation to act on). Keep it as a check or drop it; nothing depends on it.
