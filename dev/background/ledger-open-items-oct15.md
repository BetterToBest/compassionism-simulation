# Simulation project: open items from the ledger (saved Oct 15, 2026)

The ledger is the claude.ai artifact the project owner keeps; this file is a copy of what is still open, for chats that cannot open it. Decisions show the default that applies if the owner does not answer.

## Next action

Claude Code, in order: (1) session A, s170: Duke's Oct 14 page notes (Health Study links, the findings page's reading notes, suite defaults, the history check on the Health Study page, CI pin); (2) session B, s171: the Compare page from existing results; (3) Thursday morning, early: chat packets for the free plan (s135), keeping at least 8% of the weekly limit for it. The CoMSES package (s119) and share kit (s144) move to the free plan unless limit is left after (2). Duke: approve the suite page for linking from the findings explorer (s162) once session A's defaults are in.

## Open decisions


## Open issues

- **i19** [med] Claude Pro Plan - expires on Thursday Oct 15, 2026. It's unclear what time it expires that day, probably at the same time I started the plan a month ago (in the late evening), which will provide a few extra sessions on Thursday. I won't renew the Runpod Key, as the Pro plan expires prior to Runpod's access limit.
    - Oct 13: Anthropic's help article says a cancelled plan keeps paid access until the end of the current billing period; it gives no time of day. So the plan treats Thursday morning as the last safe session (s135) and anything later as a bonus. The weekly limit resets Monday, after the plan ends, so the 71% left on Oct 13 is all there is.
    - [x] If you can verify what time the Pro Plan gets shut off on Thursday, that will help plan out the rest of the steps. It's either when I started (late evening) or a set time of day that Anthropic has set.
- **i21** [med] Release data lacks series the BLEI visuals and the Five Measures chart need
    - See decision d208. Exported now (data/releases/v5.4.json and v5.4/bands-*.json): yearly basket poverty, wealth poverty, BLEI poverty (with p10, p50, p90 across runs), median wealth; run totals for extreme poverty and both BLEI readings. Not exported: BLEI tiers (Crisis to Flourishing), median BLEI, its three parts (savings, income, BU days), relative income poverty, extreme poverty by year.
    - [ ] Confirm the list against the engine's per-year outputs
    - [ ] Act on d208
- **i22** [low] Verify one sentence on the Hub's BLEI page: it may say the simulation's poverty line is BLEI at or above 30 days (inverted)
    - Seen in a machine summary of https://bettertobest.github.io/research-hub/basic-living-economic-index.html on Oct 13, not yet read by eye. The simulation counts BLEI poverty as below 30 days. If the page says 'at or above', it needs a one-word fix on the Hub.  Oct 13 (Claude, machine read of the page again, still not read by eye): Section 8 table, row 'Poverty definition', BLEI-Corrected column, reads 'BLEI >= 30 days (Tier 2: Threshold)'. If that cell is meant as the poverty definition it is inverted against the simulation (poverty = below 30 days); if it means the line a household must reach 
    - [ ] Read the sentence on the page and fix it if inverted
- **i23** [high] d209 is the biggest decision: SNAP's work rule as the main row changes every headline figure in a v5.6 release
    - Plain words: today the model treats SNAP as if every eligible household can always get it. The 2025 law limits SNAP for many adults without dependants who work under 20 hours a week. Adding the rule makes today's safety net weaker, in both the 'with Compassionism' and 'without' runs, so poverty levels in every table move, and Compassionism's measured gain may move too. Safeguards: (1) it is built behind a switch that stays OFF while it is built and tested, so the live page and every current figure are unchanged until release; (2) the first pull request carries no figures, only the switch and t
    - [ ] Read the SNAP report (dev/reports/v5-33-snap-work-rule.md) before merging the release pull request
    - [ ] Decide whether to keep d209 as the main row once you've seen the figures side by side
- **i24** [high] The published main results have no today's safety net (SNAP, EITC, CTC); d209's note assumed they did
    - Found Oct 14 while preparing the study (dev/reports/v5-33-snap-work-rule.md, section 5). The safety net is only in the study page's SN rows. The work rule lives inside SNAP, so a v5.6 'with the rule' adds the safety net too, and that moves figures on its own (20 seeds, basket poverty with Compassionism +0.11 Reference, -0.20 Adverse, +0.54 Stress; no programme +0.03 to +0.04). That the safety net slightly raises basket poverty needs explaining before any release (likely its own work response). The s165 job measures the rule's own effect separately so the v5.6 report can show each.  Oct 14: gat
    - [x] Explain why adding today's safety net raises basket poverty slightly (before v5.6) — Done Oct 14: mostly behaviour (the work response to benefit phase-outs, plus a smaller price effect); one small flaw (SNAP's income limit in the marginal rate) fixed behind SNET.slope. dev/reports/v5-35-safety-net-poverty.md
    - [ ] Duke: decide with i23 whether v5.6's main rows include today's safety net and the rule
- **i25** [med] The outside history data are unverified, and seven cells are disputed between the two packs
    - Both packs were gathered by AIs with web access; each opened ten random values and found them right, but nothing is checked against Census, BLS or the Federal Reserve from the Claude Code machine. The seven disputed cells are the supplemental poverty rate for 2014 (three age groups), 2015 (two), 2018 (65 and over) and 2020 (65 and over); only the 2020 one lies in a period the history check uses (0.1 point apart). Only Muse's pack has the economic, SNAP, relief-law and wealth series, so those were never cross-checked. For a rough shape check this is acceptable if it is said plainly; it would no
    - [x] Claude Code: say in the history-check report that the data are unverified and name the disputed cells — Done Oct 14: dev/reports/v5-34-history-check.md, section 4
    - [ ] Optional, you: ask a free AI with web access to open Table 8 of Census report P60-290 and settle the seven disputed cells; bring the answer back to a Claude chat
    - [ ] Optional, low value: the four blank corrected renters' thresholds (2020-2023, BLS blocks automated download) and Muse's equal real median income for 2011 and 2012 (69,070)
- **i27** [med] Latest Grok Audit - https://grok.com/share/c2hhcmQtMw_3ddece2d-1a0d-48e8-8916-7d22a7bbb559

## Steps not done

- **s37** (blocked, low priority) Submit the model to the CoMSES model library, and a Show HN fact sheet (yours to write)
    - Oct 6: split by the outreach decision: submit to CoMSES now with v5.2.2 (Claude Code prepares the package; ask for CoMSES peer review); the Show HN fact sheet waits for v5.3, so the numbers people quote include households and children.  Earlier notes: Oct 6: unblocked: v5.2 is live, so the figures sent out include savings, ageing and the US-data check.  Earlier notes: Oct 3: now waits for v5.2, so the figures sent out already include savings that keep up with prices, ageing and the check against
- **s95** (todo) Then the compare page, built on the same shared charts and data format
    - Oct 14: reshaped as s171 (build the Compare page from existing results, no restudy). Oct 13 reassessment (d196): not in the Pro week. Its 500-run restudy took 7-8 hours on Claude Code's 4-core machine, and Runpod is not renewed. study.html already reads every result against today's safety net (d192), which covers the main comparison a reporter asks for. Duke writes the definition; session 9 packs it with a run script that can run on your own computer.  Earlier notes: Oct 6: moved after v5.3 and 
- **s117** (todo) Simple measures of what money does not capture: hours given to community projects, time freed from work, participation
    - Oct 13 reassessment (d198): after Pro. New measures are open-ended design work; a chat packet with the definitions is enough to start them with Sonnet or Haiku.  Earlier notes: Grok audit. The framework aims at flourishing as well as poverty; even rough, clearly labelled measures would start to show that side.
- **s118** (todo, top priority) A second, independent implementation of the core yearly loop (for example in Python) checked against the released results
    - Oct 13 reassessment: stays with free AIs (s136); session 9 packs ODD.md and the core loop file for it.  Earlier notes: Grok audit. Until an outside economist reviews the model, an independent re-implementation is the strongest check one author can arrange.
- **s119** (todo) Session 7: prepare the CoMSES model-library package and the wide-audience fact sheet (figures traced to the release data)
    - Oct 13 reassessment: unblocked (d199): v5.5 is the settled engine. Session 7, Wednesday afternoon (Sonnet, medium effort). Takes over the fact sheet from s134. Each figure in the fact sheet names the release file and row it comes from, and a test checks them, so a reporter can quote it safely. Includes the backtest result if session 6 ran. Rough cost: 6-10%.  Earlier notes: Claude Code prepares; you submit. The package: the reproduction archive, ODD.md, a short description, keywords and the lice
- **s144** (todo) Share and access kit: embeddable charts, shareable scenario links, and a screen-reader, contrast and reduced-motion pass
    - Oct 13 reassessment: Session 8, Wednesday evening (Sonnet, medium effort), only if at least 15% of the weekly limit is left after session 7. Shareable scenario links matter most to reporters; do those first, then the accessibility pass. Rough cost: 8-12%.  Earlier notes: Aimed at the press and policy audience. Embeddable charts and links that reopen a chosen scenario let a reporter cite exactly what they saw. Check first which of these the live page already has (downloads and a phone and keyboar
- **s135** (todo) Last Pro session (Sonnet, low effort, keep short): chat packets for the free plan
    - Oct 13 reassessment: Session 9, Thursday morning, start it early (Sonnet, low effort); keep at least 8% of the weekly limit for it. The cut-off time on Thursday is not published (i19), so this session must not be left for the evening. Add dev/background/ledger-export.md (this ledger's decisions and open items) so free-plan chats without the ledger still have them (the i11 suggestion). Packets for: the outside audits (s148), the Python re-implementation (s118), the flourishing measures (s117), th
- **s136** (todo) Finish what is left from the chat packets; the Python re-implementation goes to free AIs
    - The independent Python version of the yearly loop suits outside AIs: give them ODD.md and the core loop file, then have Sonnet compare their output with the released results. Then the Research Hub and NEEC ledgers.
- **s148** (todo) Outside audits after v5.5 is live
    - Claude writes one targeted prompt per auditor, each with a different angle: the arithmetic and accounting, the economic assumptions, the health-system claims and country comparisons, and press-readiness and clarity. You paste the replies into a fresh chat, and the findings are sorted into corrections, decisions and optional polish. Each audit is a separate task so a free plan can handle it.
- **s162** (doing, medium priority) You: review the visual suite page and choose which visuals, if any, go onto the simulation, findings and replication pages
    - Claude adds one decision per candidate visual after you've seen the page. Nothing moves onto the existing pages until you confirm.
- **s171** (todo, high priority) Claude Code session B (Opus, medium effort, about 12-18%): the Compare page from results already computed
    - Builds compare.html for the policy comparison study using data that already exist (the v4.22 comparison of six designs and the Health Study's today's-safety-net rows), on the shared charts and data format. No new 500-run study: that took 7-8 hours and needs a Runpod pod. The page says which figures come from which engine version, and where the like-for-like 'Compassionism Core' differs from Compassionism as designed. Linked from the findings page; kept noindex until Duke approves it. If the sess
