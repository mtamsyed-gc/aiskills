# 04 Excel and CSV deliverables

All in `04_Outputs\xlsx\` (the CSV versions in `csv\`). Each is built from the output tables, so any figure ties back
to `dim_life`, `fact_member_month` and `fact_claims`. Versions in this skill: extract EX-1.2, treaty metrics
TM-1.3.

## Merit_Extract.xlsx / Merit_Extract.csv (extract EX-1.2)
Grain: one row per life attribute set x exposure month. Premium measures come from `fact_member_month` (written in
the booking month, earned in the month); claims from `fact_claims` lines with `InExperience = 1`, by incurred month.
- Sheets: Extract (continues on Extract (2), (3) above 1,000,000 rows; the CSV holds every row), Ceded by reinsurer,
  Policies without Reinsured %, Totals, Dictionary.
- Attribute columns (the row key), in order: Payer Name, RI Name, TPA, Policy Type, UWY (Policy), UWM (Policy), ExposureMonth, Master Contract ID, Unique Policy Identifier, Policy Coverage Start Date, Gender, Marital Status, Nationality, Region, Age Band, New/Renewal, Renewed/Non-Renewed, Group_Size_Band, Network, Currency (Premium Data), then Currency (Claims Data).
- RI share columns: Reinsured %, Reinsured % Source, Treaty Ceded %, Ceded %.
- Measures: Gross Premium, Net Premium, Gross Net Premium, Administration Fee, TPA Fee, Broker Commission, ERP, Gross Earned Premium, Net Earned Premium, Gross Net Earned Premium, Paid Claim, OS Claim, Reported Claim, Paid Claim Count, OS Claim Count, Reported Claim Count.
- **Totals** sheet: per TPA, the extract's totals, the same totals from the output tables (must be equal) and from the
  collated premium file (the difference = rows the premium workflow did not take).

Dictionary (as written to the workbook's Dictionary sheet):

| Column / sheet | Definition |
|---|---|
| Payer Name | Booking entity of the premium file (file register), as dim_life |
| RI Name | Reinsurer standard value (Value maps), as dim_life |
| TPA | Third-party administrator |
| Policy Type | Policy type standard value (Value maps; calculated for some TPAs), as dim_life |
| UWY (Policy) | Underwriting year = year of the policy coverage start |
| UWM (Policy) | Month of the policy coverage start, yyyymm |
| ExposureMonth | Month of the row, yyyymm: premium booking / earning month; claims incurred (treatment) month |
| Master Contract ID | As dim_life |
| Unique Policy Identifier | The pipeline's policy key (upper case; _ - / and apostrophes removed) |
| Policy Coverage Start Date | Policy start of the term |
| Gender | Gender Group (Value maps), with 'Maternity Eligible Female' shown as Female (the age band carries age) |
| Marital Status | Standard value (Value maps), as dim_life |
| Nationality | Nationality Group (inputs workbook 'Nationality groups'; owner's example 'Arab') |
| Region | Region Group (Value maps: health authority / emirate; owner's example 'DUBAI') |
| Age Band | Age at inception band, NN-[lo-hi] (run.json age_bands; blank age = the run's default band) |
| New/Renewal | As dim_life (raw column, endorsement type, or derived from the prior UW year) |
| Renewed/Non-Renewed | Renewed = the same TPA and policy (else master contract) has a term in the next UW year; Non-Renewed = none; the latest UW year of the data = Not yet due |
| Group_Size_Band | Lives of the policy term, NN-[lo-hi] (run.json group_size_bands) |
| Network | Network standard value (Value maps), as dim_life |
| Currency (Premium Data) | Currency of the life (premium file) |
| Currency (Claims Data) | Currency of the row's claim lines (claims file); MIXED if several; blank without claims |
| Gross Premium | Written gross premium booked in the month (dim_life / fact_member_month WrittenPrem_Gross) |
| Net Premium | Written net premium booked in the month |
| Gross Net Premium | Written Gross Net premium booked in the month (carried like Gross / Net) |
| Administration Fee | Written administration fee booked in the month (carried like Gross / Net) |
| TPA Fee | Written TPA fee booked in the month (carried like Gross / Net) |
| Broker Commission | Written broker commission booked in the month (carried like Gross / Net) |
| ERP | Earned risk proportion: earned life-years in the month (days / annual basis; gross basis, zero-premium lives excluded) |
| Gross Earned Premium | Gross premium earned in the month |
| Net Earned Premium | Net premium earned in the month |
| Gross Net Earned Premium | Gross Net premium earned in the month (earned like Gross) |
| Paid Claim | Paid amount of claim lines in experience, by incurred month (payer share) |
| OS Claim | Outstanding amount of claim lines in experience, by incurred month |
| Reported Claim | Paid + OS |
| Paid Claim Count | Visits counted (CountFlag) with a net paid amount |
| OS Claim Count | Reported count - paid count |
| Reported Claim Count | Visits counted (CountFlag) |
| Reinsured % | Reinsured share of the policy (inputs workbook 'RI policy shares'; 100% for a payer not listed there); blank = not yet known |
| Reinsured % Source | Where Reinsured % comes from (dim_life ReinsuredPctSource) |
| Treaty Ceded % | Sum of the non-retained treaty shares of the RI Name and UW year ('RI treaty shares'); blank = no treaty rows |
| Ceded % | Reinsured % x Treaty Ceded % |
| Sheet 'Ceded by reinsurer' | Per reinsurer of the treaty (retained line included, Retained = Y): amount x Reinsured % x Treaty Share, for rows whose Reinsured % is known |
| Sheet 'Policies without Reinsured %' | Policies whose Reinsured % is not known yet, with their amounts: fill in 'RI policy shares' and re-run premium, claims and the extract |
| Sheet 'Totals' | Per TPA: the extract's totals, the same totals from the output tables (must be equal) and the collated premium file (the difference = rows the premium workflow did not take: stops, ignored types, duplicates, overlaps, exclusions; or fees on rows without premium) |
| Sheets 'Extract (2)', 'Extract (3)' | Rows beyond 1,000,000 continue there (an Excel sheet holds 1,048,576); the CSV file holds every row |

## Merit_TreatyMetrics.xlsx / .csv (treaty metrics TM-1.3)
Sums at 100% of each book of business ("segment", inputs workbook tab 'Treaty segments') per UW year, for the treaty
restructuring tool. No treaty shares, no ratios, no row-level data.
- Columns, in order: Row type \| Segment # \| Segment \| Payer Name \| RI Name \| Reinsured % \| Book \| UWY \| Gross written premium \| Net written premium \| Net earned premium \| Reported claims \| Ultimate claims.
- Row type: SEGMENT (one row per Segment # x UWY, zeros included), UNASSIGNED (per payer x RI Name x UWY), OTHER (per
  UWY), ALL (per UWY). Sorted by UWY, then Row type in that order.
- Sources: Gross / Net written premium = `dim_life.WrittenPrem_Gross` / `_Net`; Net earned premium =
  `dim_life.EarnedPrem_Net` (earned to the valuation date); Reported claims = `fact_claims` Paid + OS; Ultimate claims
  = `fact_claims.UltimateAmount`. Premium by `dim_life.UWY`, claims by `fact_claims.UWY`.
- A life goes to the segment whose Payer Name and RI Name match and whose Reinsured % is blank or equals the life's
  ReinsuredPct. Payer + RI Name of a segment but no share match -> UNASSIGNED; two matches -> UNASSIGNED and the
  check "Lives in two segments" fails; no segment with that payer + RI Name -> OTHER. A claim line follows its
  life's segment (through LifeKey + UWY); a line with no life goes by its own Payer Name + RI Name when exactly one
  segment has them, else UNASSIGNED / OTHER.
- Written premium (gross and net) of a UW year still running at the valuation date is **annualised**; earned premium
  and claims are not. Annualisation per TPA x policy type uses the prior UW year's own booking pattern where it has
  one (WP(E - 1, all) / WP(E - 1, booked up to the same month a year earlier)), else x 12 / months elapsed.
- Sheet Checks (PASS / FAIL): SEGMENT + UNASSIGNED + OTHER = ALL; ALL premium = dim_life totals; ALL ultimate and
  reported = ultimates totals; lives and lines in UNASSIGNED; no life or line in two segments. Sheet About: valuation
  date, run, versions, segment rows used.

## Merit_PNLR_Base.csv and Merit_PNLR.xlsx (Projected Net Loss Ratio)
`Merit_PNLR_Base.csv` (sheet 'PNLR base'): the treaty-metrics sums by class x segment x TPA x policy type x UW year x
business status (dim_life NewRenewal). Columns: Row type \| Segment # \| TPA \| Policy Type \| UWY \| Business Status \| Net written premium \| Net written premium (annualised) \| Net earned premium \| Ultimate claims.

The PNLR of the upcoming policy year, per cell (segment) x TPA x policy type, from the expiring UW year E and E - 1:
```
NWP    = net written premium of E, annualised (as treaty metrics); all business of E renews in E + 1
NB     = NWP x NB share of the policy type
LR_E   = Z x LR(E) + (1 - Z) x LR(E-1) x (1 + t)        LR = ultimate claims / net earned premium
LR_pre = LR_E x (1+t) / ((1 + a t)(1 + b g))             a = trend passed on (1/0), b = global increase applied (1/0)
x      = max(0, LR_pre / T - 1)                          residual increase to the target net LR T
R      = (1 + a t)(1 + b g)(1 + h x) - 1                 h = haircut (share of the residual passed on)
e      = (1 + R) / (1 + t) - 1                           increase beyond trend
rho    = max(0, ceiling - step x max(0, e) / 5%)         retention by policy type
P_R    = NWP x rho x (1 + R);   C_R = NWP x rho x LR_E x (1 + t)
tau    = (1 + a t)(1 + nb_extra) - 1;  P_NB = NB x (1 + tau);  C_NB = NB x LR_E x (1 + t)
PNLR   = (C_R + C_NB) / (P_R + P_NB)   for any group of cells
```
Default assumptions (assumptions workbook sheet 'PNLR', else these): Target NLR = 0.95; Medical trend = 0.08; Haircut = 1.0; Trend passed on = Yes; Global increase applied = Yes; Credibility (expiring year) = 1.0; Rate level = Policy type x TPA.
Defaults by policy type (retention ceiling, step per 5%, NB tariff extra, NB share): GROUP (0.9, 0.03, 0.0, 0.0); INDIVIDUAL (0.7, 0.05, 0.0, 0.0); SME (0.8, 0.04, 0.0, 0.0); OTHER (0.9, 0.03, 0.0, 0.0).

## Merit_RateExposure.xlsx / .csv
The exposure a rate proposal is weighted by: Net written premium of one UW year (default the latest), booked up to the
experience-to month (the dashboard's Written Premium, Net basis, same experience-to).
- Columns: UWY \| TPA \| Policy Type \| Network \| Rate Tab \| Member \| Lives \| Written LY (Net) \| Net WP. Sheets Exposure and Control.
- Rate Tab = AUH where Region Group = HAAD, else DXB. Member = Child (age at inception <= child max age and not a
  maternity-eligible female), else Adult; no age = Adult. Blank policy type or network = "(Blank)".
- Lives = distinct life-periods with written life-years (Net) in the selection (the dashboard's Lives Written).

## Merit_Headline.xlsx
Sheets: Read me (run, bases, definitions); By UW year; UW year x policy type; UW year x TPA; UW year x TPA x type;
Checks. Columns: earned LY, written / earned premium, paid, OS, paid + OS, IBNR, ultimate, paid + OS LR, ultimate LR,
gain / loss, ultimate count, frequency per 1,000 LY, burning cost, earned premium per LY. Equals the dashboard's
Executive summary at the same bases and experience-to (no cut unless built with `--experience-to`). Checks flag
ultimate LR outside 20%-150% on >= 1% of earned premium, negative premium, claims without premium, earned above
written.

## Merit_Checks.xlsx
Summary tab first; premium / claims recon; exceptions (capped at 500,000 rows in the workbook; the CSVs hold all);
checkpoint matrices (premium P01-P09, claims C01-C06: rows and sums by UWY x TPA x policy type x RI name with a
Movements column); value-map discovery; premium / claims data quality (FLAG above 0.5%). Core checks: no Stop
exceptions; every sheet read; premium ties (FanDiff < 0.01 per TPA); claims tie (payer share in = paid + OS); match
rate >= 95% per TPA; descriptions mapped; real development factors; dashboard refreshed on this run.

## Merit_Preflight.xlsx
Read OVERALL first. FAIL = a missing tab, file or setting: fix and re-run intake apply before the workflows.

## Merit_03b_Development.xlsx
See `02-reserving-tables.md` (dev_* tables).

## Merit_RunCompare_<date>.xlsx / Merit_BaselineCompare_<date>.xlsx
Compares two runs table by table. Row status SAME, MOVED, NEW (this run only), GONE (previous only), EXPLAINED
(matched by `00_Start_Here\explanations.csv`). VERDICT "IDENTICAL within tolerance" = nothing unexplained. Sheets:
Summary, Tables, By TPA x UWY, By key, Columns, Exceptions, Recon, Manifest, Explanations, Restatements, Restatement
cells. No member or claim keys unless run with `--keys`; LifeID ignored.
