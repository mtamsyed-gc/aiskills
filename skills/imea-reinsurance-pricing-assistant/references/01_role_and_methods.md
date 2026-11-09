# 01 Role and methods

## Role (GC, from 1 Sep 2026)
- VP Life & Health IMEA, Guy Carpenter Dubai (DIFC/DFSA-regulated entity). Manager: Khaldoon Hemsi, MD IMEA.
- Two halves: (a) origination and placement of life & health reinsurance (treaty and fac) with cedants across IMEA and a
  reinsurer panel; (b) the team's technical lead: pricing, portfolio analytics, treaty structuring, and the tools below.
- Khaldoon's concern is placed deals and brokerage revenue; he wants opportunities where GC has an edge and a visible
  revenue line. Technical detail is Etam's; Khaldoon reviews and moves things forward in short in-person exchanges.

## Core expertise
- Health MR reinsurance pricing: burning cost, credibility, experience monitoring, completion factors / IBNR, large-claim
  and accumulation analysis, XoL per-event pricing, stop loss, quota share economics, treaty structure comparison on a
  capital-release basis.
- Life reinsurance: group life, credit life (personal loan / mortgage / credit card), individual life, unit-linked,
  longevity swaps; relativity-grid pricing anchored on a base mortality curve with country, product and rider factors.
- Toolkit: Excel / Power Query / VBA, Python (pandas, DuckDB, pyarrow), R, Power BI, Alteryx (being retired at GC),
  Moody's AXIS background.

## House conventions
- Materiality: 0.5% of premium or claims, tested at total and at UWY x TPA. Below = negligible / note; above = flagged.
  Phase-1 review rule: flag only objectively wrong techniques; valid alternatives are left alone.
- Dates: no STOPs on conversion failures; a quantified data-quality section instead.
- Zero-premium lives never inflate written exposure. Claims capped only when a limit actually resolves to the member.
- Trend default 10% p.a. (adjustable). Trending matters for best-estimate burning cost / severity, not for
  profitability views.
- Claim-to-life matching on any combination of policy no / member no / DOB / gender / relation; match rate < 95% is a
  stop.
- New / Renewal: from a raw column, user input, or a date rule (policy effective later than contract date; policy
  number present in the previous UWY).
- IBNR methods he uses (from his own manual "Deriving Ultimate Claims in Medical Reimbursement Reserving"): M1 reported
  chain ladder, M2 paid chain ladder, M3 count chain ladder, M4 frequency x severity, M5 Bornhuetter-Ferguson (a-priori
  = user / Cape Cod / mature burn cost), M6 burning cost. Monthly cohorts, 12-month sunset, net of reversals.
- Deterministic, reproducible outputs: same inputs + versions = identical files. Every rule change is his decision and
  is recorded (TPA_RULES / audit trail) before it ships.
- Model governance: an independent reviewer outside the build for anything client-facing; Appointed-Actuary-style
  review standards for Merit.
