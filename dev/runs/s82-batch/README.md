# S82 batch tables (engine aa2a4e0, v5.9.19)

The tables of the S82 batch (limits on supply, wages that follow prices in part, the BU's delay, and the triage's smaller readings), as rerun under research-update `prereg/2026-11-s82-v6-supply-indexing.md` Amendment 5. Made by:

    python3 dev/tools/s82_tables.py <compassionism-sim-results checkout> <out> --engine aa2a4e0 --first eb0969c

- Results: compassionism-sim-results `s82-v6-{ref,adv,str}-{20,40}-aa2a4e0` (seeds 1-500, 500 adults). The same tables with the summary JSON are in that repository's `s82-tables-aa2a4e0/`.
- `s82-checks.md` first: every check passed.
- Questions 1-6: `s82-q1-supply.md` to `s82-q6-smaller.md` (20 years, the primary horizon), and the same names ending `-40y` (40 years).
- Question 7 (the assumptions screen) is in `dev/runs/s82-screen/`.
- The plain-words report: `dev/reports/s82-supply-indexing.md`.
- **Do not read** the ageing reading (`ageing, AGE with lf.fl panel`) at share 0 in `s82-q6-smaller*.md`. It measures a defect (preregistration Amendment 6; the report's section 7). Its full-backing row reads normally.
