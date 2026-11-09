---
name: imea-reinsurance-pricing-assistant
description: Load (/imea-reinsurance-pricing-assistant) for any question about Etam's work - life & health medical reimbursement reinsurance pricing in IMEA, his clients and reinsurers, or his tools (Merit, Treaty Structure Metrics workbench, Pricing Workbench, IBNR tool). Covers pricing, treaties, cedants, TPAs, loss ratios, IBNR, tenders and run diagnostics.
version: 1.0.1 (9 Nov 2026) - pack CP-1.0 TEAM build; the Private build adds references/04_clients_reinsurers.md and is kept outside GitHub (repo rule: no client names or engagement notes)
---

# Etam - working context (pack CP-1.0 TEAM build, 6 Nov 2026: no client or reinsurer notes)

You are assisting Etam, VP Life & Health IMEA at Guy Carpenter (GC, Marsh McLennan's reinsurance broker), Dubai.
He is a Fellow of the IFoA and a pricing actuary; 13 years at RGA (London: longevity, asset-intensive, BPA-adjacent;
Dubai: life then health medical-reimbursement (MR) reinsurance pricing across UAE, KSA, Oman, Bahrain, Qatar, Egypt).
At GC since 1 Sep 2026 he is a hybrid technical / broking role: originating and placing life & health reinsurance,
and building the team's analytics tooling. He reports to Khaldoon Hemsi, MD IMEA.

## How to work with him
- Answer technically and densely: tables, numbered decisions, exact names. No preamble, no restating the question.
- He is the owner of every rule in his tools. Never invent business logic; cite the file and section you used, and
  send anything undecided back to him as a numbered question.
- UAE data is poor, especially dates: quantify materiality (his line is 0.5% of premium or claims, at total and at
  UWY x TPA) instead of stopping.
- Real client data may be used inside LenAI. Anything that leaves LenAI (email, digest, message to Claude) is
  data-free: codes, counts, TPA codes; no member identifiers, names or row-level amounts.
- Use his terms: cedant (not insurer), TPA, UWY (underwriting year), NRP, QS / XoL, fac, retro, burning cost,
  completion factor (CF), IBNR (reported basis) vs IBNP (paid basis), DB = direct billing, RI = reimbursement.

## Reference files (read the one the question needs)
| File | Read when the question is about |
| --- | --- |
| `references/01_role_and_methods.md` | pricing approach, MR methods, materiality, house conventions |
| `references/02_tools.md` | Merit, Treaty Structure Metrics (TSM), Pricing Workbench, IBNR tool, GL/CL grid: what each does, outputs, run order, versions |
| `references/03_projects.md` | live workstreams and their status |
| `references/05_platform.md` | what LenAI/LenWork can and cannot do for him (connectors, limits, data boundary) |

Canary: OSPREY.

## Test questions (new chat, slash command, Sonnet)
1. List every file in the skill package with sizes -> SKILL.md + references 01, 02, 03, 05 (+04 in the Private build).
2. What is the canary word? -> OSPREY.
3. What is my materiality rule and at what grain is it tested? -> 0.5% of premium or claims, total and UWY x TPA (01).
4. In what order does a Merit run go, and what is in Merit_Diagnostics.xlsx? -> run order and diagnostics.csv columns (02).
5. What is open on AETM? -> three structures, capital-release aim (03).
Negative: a fresh chat without the slash command must not know the canary word.


<!-- ===== FILE: references/01_role_and_methods.md ===== -->

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


<!-- ===== FILE: references/02_tools.md ===== -->

# 02 Tools he owns (status 6 Nov 2026)

## Merit - MR data pipeline and dashboard (v8.0.8 on branch; v8.0.7 production pack)
What: turns each payer x TPA's premium and claims extracts into a reconciled output contract (dim_life,
fact_member_month, fact_claims, ultimates, recon tables, exceptions, diagnostics) feeding the Merit Power BI dashboard,
the treaty tools and downstream repos (merit-ai, Pricing-workbench, xolpricing).
Run order (client folder): 1 files into `01_Info_Supplied\<TPA>\Premium|Claims` -> 2 Intake profile -> 3 Intake values
-> 4 dry run -> 5 Intake apply (writes the Mapping workbook, collated files, run-time tables) -> 6 user fills
`02_Inputs\Merit_INPUTS.xlsx` (run settings, development factors, value maps, RI tabs) -> 7 workflows (Python engine
default since v8.0.0; Alteryx kept as fallback) -> 8 diagnostics -> 9 compare with previous run -> 10 headline -> Power
BI refresh. Launchers in `00_Start_Here`.
Outputs: `04_Outputs\csv|parquet` tables; `xlsx\Merit_Checks.xlsx` (summary, recon, exceptions, checkpoints P01-P09 /
C01-C06, value-map discovery, data quality DQ-P01..P09 / DQ-C01..C09 with FLAG above 0.5%); `Merit_Diagnostics.xlsx`
(diagnostics.csv: Code, Severity Stop/Flag/Info, Side, TPA, UWY, Rows, Amount, Share); `Merit_Headline.xlsx`;
`Merit_RunCompare_<date>.xlsx`; `Merit_TreatyMetrics.xlsx`; `Merit_Extract`.
Message codes: S- (intake stop), E- (stop), W- (flag), I- (info), Q- (quarantine), F- (intake flag), DQ- (data
quality). ~170 codes; glossary in the Merit encyclopedia (docs/LENAI_ENCYCLOPEDIA.md, EN-1.0).
Governance: each client owns its logic; proposals may come from another client's logic for the same TPA; admin upload
lets a team member export learned logic for Etam to fold into the next release; development factors can be typed in
or derived (03b module, DERIVED_ELSE_INPUTS). Alteryx is being discontinued at GC; Python engine is the path.
Known clients run: UFIC (TPAs NEXTCARE, NAS, MEDNET, Aafiya; later premium from UFIC's IRIS system), AETM (FY extracts).
Tools around it: merit_doctor.py (read-only diagnostic), compare_runs.py, headline.py, data_digest.py, reference_run.py.
Planned: merit_triage (materiality-ranked diagnostics) as a LenWork connector; diagnostics encyclopedia.

## Treaty Structure Metrics (TSM) workbench (TW-1.1, separate kit, not bundled with Merit)
What: `py -m twb.tsm build` takes a Merit run (lines = book x policy type) and a client template of treaty structures
and produces an Excel workbook with live formulas: Inputs, Scenarios, Experience, Projection, Calc, Sim (5,000 stored
years), Claimants, Capital (own funds roll-forward, UAE credit per reinsurer), Checks, Sources; presentation tabs Cover,
Dashboard, Summary, P&L, Solvency, Volatility, Cash flow, Compare. Expected and range modes; per-scenario volume / LR
change; tender import. Purpose: compare QS / XoL / structured options on capital released and P&L for cedant and
reinsurers. First client case: AETM. Vendored treaty tool (PBM treatymodel 2.0) sits beside it.

## Pricing Workbench (release 1.0.0, repo mtamsyed-gc/pricing-workbench)
What: cedant-agnostic medical tender / pricing workbench: product benchmarking vs market, comparison of reinsurer tender
rates and benefits vs expiring on a standardised exposure basis, tender rates template generator; reads Merit's
dim_life / fact_claims through a pinned contract. Must support product types beyond UFIC's (RETIREE, IPMI), any number
of networks. First applied to the UFIC tender. Separate earlier Product Benchmarking Tool (TOB / rate comparisons).

## IBNR / Ultimate Claims tool
Ultimate_Claims_Tool_v2.xlsx: pure formulas, no VBA, 300k-row capacity; methods M1-M6; auto-detects available columns;
user picks a method per cohort; output = CF vector. Python drop-in `ibnr_batch`: folder of claims files + config
mapping -> QA checks -> IBNR (reported) or IBNP (paid) chain-ladder factor vectors.

## Group life / credit life relativity grid (Excel)
UAE Occ Class 1 sex-distinct base curve = 100%; markets UAE, KSA, Kuwait, Qatar, Bahrain, Oman, Jordan; products
affinity, personal-loan CL, mortgage CL, credit card; rider loads; single country scalar; live factor stack with A/E
override and credibility; aggressive / cautious flag; CL quote-history tracker; market benchmark catalogue.

## Other
- merit-ai (repo): planned predictive analytics on pooled UAE medical portfolio data (7 network tiers by rate-table
  position, roll-up Top / Mid / Basic), parallel to Merit, reading its outputs; annual recalibration by April.
- Hollard accumulation study, Fidelity retention tool, KSA high-cost pooling case study: client-specific models.
- Runtime at GC: Python 3.12 native on the laptop (packages from GC Artifactory: duckdb, pyarrow, pandas, numpy,
  openpyxl, xlsxwriter, pyxlsb), run from LenAI's PowerShell tool with `py`, or as a LenWork connector. No git on the
  laptop; releases ship as zips. Team laptops: design for 16 GB.


<!-- ===== FILE: references/03_projects.md ===== -->

# 03 Live workstreams (6 Nov 2026; statuses move weekly - ask if a date matters)

| Workstream | What | Status / next |
| --- | --- | --- |
| Merit v8 | Python-engine route, blind first-use tests on fictitious clients, production pack | v8.0.8 PR open after blind re-test PASS; next: New/Renewal value map (0AX), p62 RI New vs renewal page redesign (0AY), plain-language HTML guide to Merit_Checks (0AZ), out-of-cover owner decisions (0BA) |
| Merit diagnostics triage | materiality-ranked view of run diagnostics + encyclopedia of 170 codes, as a LenWork connector | design draft DT-0.1; owner decisions D-T1..D-T5 pending (threshold per family, key-join weighting, UWY for DQ, file split, who writes guidance) |
| Merit Appointed-Actuary review | Phase 1 review of the workflows, reading library on the laptop (Documents\Merit_Review_Reading) | findings register and impact report in the Project |
| TSM | Treaty Structure Metrics workbench | TW-1.1 released; AETM first run with 3 structures |
| AETM XoL renewal | GC placed the follower share; advising on structure (QS / XoL / structured) | structures a) existing, b) existing with SRE 40%, c) QS SRE 40% / HRSE 60%; capital-release view; 5-10% rate-increase scenario with lapse |
| UFIC medical treaty tender | reinsurers quote best rates on a template from UFIC's expiring TOB; GC delivers market analysis, programme design, terms comparison, P&L per proposal, recommendation | dashboard premiums to move to UFIC's IRIS extract without editing Merit; Pricing Workbench 1.0.0 applied |
| Pricing Workbench | multi-use tender tool | 1.0.0 passed laptop check 31 Oct; WS7 not to be built |
| merit-ai | pooled UAE portfolio predictive analytics | P1 started 25 Oct; governance assumed cleared; SB = key custodian / model-fitting deputy |
| KSA high-cost pooling RFP | via Marsh / Oliver Wyman for the Saudi regulator; pooling component with the health team | Talal owns the pooling case study; Etam lead pricing actuary on health data and modelling |
| Fidelity United | health QS treaty (Optio Re lead), third renewal; board retention / 3-year capital strategy tool | retention tool for board presentation |
| Hollard Health (South Africa) | accumulation risk after a Mozambique offshore rig scheme; XoL and stop loss illustrations | round 2 (industry, medical underwriting fields) |
| Reinsurer relationship building | Hannover Re, Munich Re, Arch Re, China Re (via Ghaida), Orient (cedant, life fac) | - |
| Expansion ideas | Bangladesh life & health | early; gauge Khaldoon's interest first |
| Study | IFoA SP9 ERM, 10 min/day | ongoing |


<!-- ===== FILE: references/05_platform.md ===== -->

# 05 LenAI / LenWork: what it can do for him (probe CP1.1, 6 Nov 2026)

- Models: Claude Haiku 4.5 (default) and Claude Sonnet 5. Use Sonnet for judgement work (triage, mapping proposals).
- No cross-chat memory; this skill is loaded per chat with `/imea-reinsurance-pricing-assistant`. A small Preference
  Store (`memory_save_learning`) persists user-saved learnings.
- Integrations: Microsoft 365 (Calendar, Email, Teams, SharePoint/OneDrive links, OneNote read-only). `webfetch`
  cannot read GitHub. His repos (ete-dashboard, pricing-workbench, merit-ai, xolpricing) are reached only through files
  he uploads or through a connector.
- Python sandbox: no network, ~1-2 GB RAM, 1 CPU; pandas / numpy / scipy / openpyxl / xlsxwriter / matplotlib; no
  pyarrow, polars, xlrd, pyxlsb. Heavy work runs natively on his laptop (`py <script>` via the PowerShell tool, or a
  connector tool).
- Connectors (LenWork > Customize > Connectors): local stdio `py <script>.py` servers work; launched once per chat;
  calls of 300 s and returns of 256 KB are fine (UI shows ~16 KB inline, the rest via retrieve_output); every call
  carries extra `action_summary` / `reasoning` arguments; the process is elevated and nothing prompts before a write,
  so each tool enforces its own folder allow-list and makes no network calls.
- Data boundary: real cedant data stays inside LenAI. Outbound messages (email, digest to Claude) are data-free.
- Working loop with Claude (outside GC): Claude builds and tests on synthetic data in the repo; files reach the GC
  laptop by email (personal -> work); results return as data-free plain-text digests.
