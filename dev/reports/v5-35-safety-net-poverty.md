# Why today's safety net slightly raises basket poverty (issue i24-1)

Session 9, Oct 14, 2026. A 20-seed trace, made before the 500-seed study (ledger step s165) was launched; the 500-seed figures are in section 5 (session 10). Tool: `dev/tools/sn_v54_trace.js`; results: `dev/runs/sn/v54trace-ENV.json`.

## 1. The question

Adding today's safety net (SNAP, the earned income tax credit and the refundable Child Tax Credit) to the v5.4 runs raised the share of adult-years below the cost of living slightly: by about +0.04 points with no program and +0.11 with Compassionism at Reference, +0.54 with Compassionism in the Stress Test (`v5-33-snap-work-rule.md`, section 5). Extra money should not, on its own, push anyone below the line. Was it a bug?

## 2. The answer in two lines (for the study report)

**It is mostly behaviour.** As benefits phase out, people near the cost-of-living line work a little less (hours fall 3 to 4%), so some of them land just below it, while the poorest are helped and the depth of poverty falls clearly. A smaller part comes from prices: the safety net lets the poorest buy more of their basket, which pushes essential prices up a little for everyone. One small flaw was found and fixed behind a switch (section 4).

## 3. How it was traced

The v5.4 main row and its no-program run, seeds 1 to 20, each without and with the safety net, paired by seed. The same comparison was repeated under four engines: as released; the work response off; prices held flat; both off. The figures are the safety net's effect (with it minus without it), percentage points of adult-years below the cost of living, with the 95% interval over seeds.

| Reference | As released | Work response off | Prices flat | Both off |
|---|---|---|---|---|
| No program | +0.04 [+0.03, +0.05] | +0.11 [+0.09, +0.13] | +0.01 [−0.01, +0.02] | −0.03 [−0.04, −0.02] |
| With Compassionism | +0.11 [−0.02, +0.23] | **−1.34** [−1.50, −1.19] | −0.12 [−0.23, −0.01] | −0.74 [−0.86, −0.61] |

| With Compassionism | As released | Work response off | Prices flat | Both off |
|---|---|---|---|---|
| Adverse | −0.20 [−0.37, −0.04] | −2.46 [−2.66, −2.26] | −0.08 [−0.20, +0.04] | −1.16 [−1.25, −1.07] |
| Stress Test | +0.54 [+0.44, +0.65] | −0.46 [−0.56, −0.37] | +0.29 [+0.22, +0.37] | −0.32 [−0.36, −0.28] |

What the tables show:
- **The work response is the main channel.** Turn it off and the safety net cuts poverty with Compassionism in every environment (by 0.5 to 2.5 points). With it on, hours fall by 2.8% (Reference) to 4.1% (Adverse) across all adults. The households receiving benefits face a combined marginal rate of about 20 to 28% (each extra $1,000 earned loses $200 to $280 of benefits). The model applies the same work response to this as to Compassionism's own rates and to every other change in the return to work (standing guardrail 7). So a household just above the line that works a little less can fall just below it.
- **Prices are a smaller channel.** With no program at Reference, the safety net raises poverty by +0.11 when the work response is off but prices move, and lowers it (−0.03) when both are off. The extra spending on essentials by the poorest raises essential prices slightly (the same price rule the program goes through).
- **The depth of poverty falls in every case** (by 0.2 to 2.2 points on the severity measure), and most with the work response off. The safety net mostly reaches people far below the line, so it shrinks their gap more than it lifts people over it.
- **Wealth poverty** rises slightly with Compassionism (+0.8 to +1.1 points): less pay means less saving. With the work response off it does not move.

## 4. The one flaw found: SNAP's income limit was read as a work disincentive on all earnings

The model reads each household's marginal rate as "benefits lost if it earned $1,000 more". For a household within $1,000 below SNAP's gross income limit (200% of the poverty guideline), that $1,000 crosses the limit and loses all of its SNAP at once. The model then treated this as a rate of up to 90% on **every** dollar the household earns. In a yearly model with one work elasticity, that cuts such a household's pay by roughly a third, to keep a SNAP benefit that is often $24 a month. Compassionism's own rates are read as true marginal rates and never get this treatment.

**Fix, behind a switch (`SNET.slope`, off by default):** for a household receiving SNAP, the rate is read with SNAP's income test held passed, so it measures the slope of the benefit schedule, not the cliff. The cliff still acts when the household's income actually passes the limit (it loses SNAP the next year). Effect at 20 seeds: basket poverty with Compassionism −0.11 (Reference), −0.12 (Adverse), −0.05 (Stress); no program about 0. It is a small part of the rise, not its cause.

**Decision (Claude's, recorded in `dev/DECISIONS.md`, session 9):** the switch is on in every safety-net run of the s165 study (`--slope`), so the study's engine is re-pinned to the commit that has it. With the switch off every earlier figure is bit-identical (`guard_test.js`, `snap_rule_check.js`).

## 5. In the study

The study job adds a cheap 500-seed version of this trace (`sn-trace-ENV.json`: as released, work response off, prices flat; about 1.4 core-hours), so the v5.6 report can give these two lines with 500-seed figures.

**500-seed figures (added in session 10, Oct 14, 2026).** The study ran this trace on seeds 1-500 (engine commit 5bf5bcc, clean tree), with the section 4 fix on in every safety-net run (`--slope`); files `dev/runs/sn/sn-trace-ENV.json`. Figures are the safety net's effect (with it minus without it) on the share of adult-years below the cost of living, in points, with the 95% interval over seeds. The two lines of section 2, at 500 seeds:

1. **It is mostly behaviour.** With the work response off, the safety net with Compassionism lowers basket poverty in every environment: −1.26 [−1.30, −1.22] at Reference, −2.48 [−2.54, −2.43] Adverse, −0.44 [−0.46, −0.42] Stress Test. With it on (as released) the effect is −0.08 [−0.11, −0.05], −0.26 [−0.29, −0.23] and +0.48 [+0.46, +0.50]: hours fall 2.7% (Reference) to 3.8% (Adverse, Stress Test), and some people near the line land just below it. With no program the safety net raises basket poverty by +0.05 (Reference) and +0.02 (Adverse and Stress Test); with the work response off, by +0.10 and −0.01. The depth of poverty falls in every case (−0.13 to −2.09 on the severity measure).
2. **A smaller part is prices.** Holding essential prices flat moves the as-released figures by 0.03 to 0.21 points: with Compassionism −0.15 (Reference, against −0.08), −0.09 (Adverse, against −0.26) and +0.27 (Stress Test, against +0.48); with no program +0.02 at Reference (against +0.05). The direction of the price channel is not the same in every environment (at Adverse, flat prices make the safety net's effect slightly less favourable), so it is a small, mixed channel, not a constant push.

What changed from the 20 seeds: with the section 4 fix on, the safety net with Compassionism now lowers basket poverty slightly at Reference (−0.08, against +0.11 without the fix at 20 seeds) and at Adverse (−0.26, against −0.20), and still raises it in the Stress Test (+0.48, against +0.54). The 20-seed answer stands: the rise, where there is one, is the work response, not a bug.

## 6. Limits

- Sections 3 and 4 are 20-seed figures; section 5 gives the 500-seed figures. The intervals are over the seeds used and do not include the model's own uncertainties (for example, the size of the work response, a design parameter that is swept elsewhere).
- The size of the work response to benefit phase-outs is the model's single elasticity, not an estimate for SNAP and the EITC. Studies of the EITC find that it raises work among single mothers (more people working) and small or no cuts in hours among those already working (Eissa and Liebman 1996; Eissa and Hoynes 2006). The model has no decision to start or stop working, only hours, so it may overstate the hours cut for the safety net. This is reported, not changed: guardrail 7 requires one elasticity for every change in the return to work.
- The price effect uses the model's essential-price rule, which was built for the program's larger demand push; it is not estimated for SNAP.

## 7. For Duke

Nothing on the pages changes. The question for you is unchanged (issue i23: whether v5.6's main results include today's safety net). This note means that if they do, a reader will see the safety net lower the depth of poverty but not the share below the line, and the two lines above say why.
