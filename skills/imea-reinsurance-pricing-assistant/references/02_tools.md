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
