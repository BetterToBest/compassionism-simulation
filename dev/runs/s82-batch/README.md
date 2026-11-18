# S82 batch tables (engine aa2a4e0, v5.9.19; the ageing rows on ab11c05)

The tables of the S82 batch (limits on supply, wages that follow prices in part, the BU's delay, and the triage's smaller readings), as rerun under research-update `prereg/2026-11-s82-v6-supply-indexing.md` Amendment 5. Made by:

    python3 dev/tools/s82_tables.py <compassionism-sim-results checkout> <out> --engine aa2a4e0 --first eb0969c --age ab11c05

- Results: compassionism-sim-results `s82-v6-{ref,adv,str}-{20,40}-aa2a4e0` (seeds 1-500, 500 adults). The ageing rows (E.age.none, E.age.a0, E.age.a1) come from the rerun on the fixed engine, `s82-v6-age-{ref,adv,str}-{20,40}-ab11c05` (Amendment 6's addendum and Amendment 7). The same tables with the summary JSON are in that repository's `s82-tables-ab11c05/`; the first tables, `s82-tables-aa2a4e0/`, differ only in question 6's ageing rows and the checks.
- `s82-checks.md` first: every check passed.
- Questions 1-6: `s82-q1-supply.md` to `s82-q6-smaller.md` (20 years, the primary horizon), and the same names ending `-40y` (40 years).
- Question 7 (the assumptions screen) is in `dev/runs/s82-screen/`.
- The plain-words report: `dev/reports/s82-supply-indexing.md`.
- **The ageing reading** (`ageing, AGE with lf.fl panel`) in `s82-q6-smaller*.md` is the rerun on the fixed engine (Nov 18, 2026, S91). The batch's own ageing rows measured a defect (wages counted prices twice; preregistration Amendment 6) and are superseded; they stay in `s82-tables-aa2a4e0/`, not quoted.
