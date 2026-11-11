---
name: merit-outputs
description: Use for any question about Merit's output files and their column headers - dim_life, fact_member_month, fact_claims, ultimates, cf_selected, recon, exceptions, run_manifest, diagnostics, the *_excluded tables and the Excel outputs (Extract, TreatyMetrics, PNLR base, RateExposure, Headline, Checks, 03b Development) - what a column means, how tables join, how to reproduce a dashboard figure from the files, or why two totals differ.
version: 1.0.0 (2026-11-11) - generated from Merit v9.2.0, output contract IP4-13
---

# Merit outputs skill

## 1. What this skill is for
Merit is GC's medical-reimbursement data pipeline. It turns each payer x TPA's premium and claims extracts into
one reconciled set of output tables (the **output contract**, `model_contract.json`), which feed the Merit Power BI
dashboard, the Excel extracts and the treaty / pricing tools. This skill is the reference for those outputs. Typical
questions:
- "What does InExperience / MatchStatus / CountFlag / PayerShareCapped mean?"
- "Which file holds earned premium by month? How do I join claims to the member's attributes?"
- "Rebuild the ultimate loss ratio by UW year and TPA from the CSVs."
- "Why does written premium in the extract differ from a pivot of the raw file / from the dashboard?"
- "What is on the TreatyMetrics sheet and how is a claim assigned to a segment?"

## 2. Files and when to load them
Each file stands alone. Load only what the question needs.

| File | Load when |
|---|---|
| `references/01-core-tables.md` | Any column of `dim_life`, `fact_member_month` or `fact_claims` (and their `_excluded` twins); grains, keys, joins |
| `references/02-reserving-tables.md` | `ultimates`, `cf_selected`, IBNR / IBNP, completion factors, the 03b `dev_*` tables |
| `references/03-control-tables.md` | `recon_premium` / `recon_claims`, `exceptions*`, `run_manifest*`, `scope_tags`, `diagnostics`, `dq_*` tables; tying totals |
| `references/04-excel-outputs.md` | `Merit_Extract`, `Merit_TreatyMetrics`, `Merit_PNLR_Base` / PNLR, `Merit_RateExposure`, `Merit_Headline`, `Merit_Checks`, `Merit_Preflight`, `Merit_03b_Development`, `Merit_RunCompare` |
| `references/05-measures-and-recipes.md` | Reproducing a dashboard measure from the files; worked pandas recipes; the traps that give wrong totals |
| `references/09-source-register.md` | Which Merit / contract version this skill describes; how to check a run matches it; test questions |

## 3. Where the outputs are
A Merit client folder has `04_Outputs\` with these sub-folders:

| Sub-folder | Holds |
|---|---|
| `csv\` | Every output table as CSV (UTF-8, header row, dates `yyyy-mm-dd`, `.` decimal, no thousands separator) |
| `parquet\` | The same tables as Parquet (identical content) |
| `xlsx\` | The workbooks: `Merit_03b_Development.xlsx`, `Merit_Checks.xlsx`, `Merit_Extract.xlsx`, `Merit_Headline.xlsx`, `Merit_PNLR.xlsx`, `Merit_Preflight.xlsx`, `Merit_RateExposure.xlsx`, `Merit_TreatyMetrics.xlsx`, `Merit_Diagnostics.xlsx`, `Merit_RunCompare_<date>.xlsx` |
| `collated\` | `Premium_SchemeA_collated.csv`, `Claims_SchemeA_collated.csv` (+ Parquet): the intake's in-scope source rows, input to the workflows (not outputs) |
| `stage\` | Internal hand-over files between workflows. Never analyse them |

`04_Outputs\Previous_run\` (last completed run) and `04_Outputs\Baseline\` (frozen signed-off run) have the same tree.

## 4. The tables at a glance
| Table (csv\ and parquet\) | Grain | Key | Columns | Details in |
|---|---|---|---|---|
| `dim_life.csv` | life-period: Payer\|TPA\|policy\|member x UWY | LifeKey + UWY | 73 | 01 |
| `fact_member_month.csv` | life-period x calendar month | LifeKey + UWY + MonthStart | 17 | 01 |
| `fact_claims.csv` | claim line (reversals netted within ClaimID upstream or kept as lines; sums are additive) | ClaimKey | 59 | 01 |
| `cf_selected.csv` | TPA x Basis (Reported/Paid) x Measure (Amount/Count) x Lag 0-12 | TPA + Basis + Measure + Lag | 11 | 02 |
| `ultimates.csv` | Payer x TPA x incurred month x UWY (reported claims keep their UWY; IBNR allocated to UWY by earned premium of the month, SPEC P5.7) | Payer Name + TPA + IncurredMonth + UWY | 23 | 02 |
| `recon_premium.csv, recon_claims.csv` | one row per TPA, one column per control total (all UW years, no date cut) | - | one per measure | 03 |
| `exceptions.csv, exceptions_claims.csv` | one row per finding | - | 10 | 03 |
| `run_manifest_premium.csv, run_manifest_claims.csv` | one row per setting (Key, Value) | - | 2 | 03 |
| `scope_tags.csv` | tag x row (a life-period or a claim line) x rule | LifeID + ClaimID + Tag + ScopeRule | 4 | 03 |
| `diagnostics.csv` | finding: Code x Side x TPA x UWY (counts and amounts only) | - | 9 | 03 |
| `dq_recon_scope.csv` | Side x TPA x UWY ('(all)' = every year) x Measure (rows / amount) | - | 12 | 03 |
| `dq_recon_control.csv` | control total: Payer x TPA x Side x Measure x Period | - | 13 | 03 |
| `dq_quarantine.csv` | quarantined source row x failed rule (no identifiers) | - | 10 | 03 |
| `dim_life_excluded.csv`, `fact_member_month_excluded.csv`, `fact_claims_excluded.csv` | as their main table (excluded by the scope register) | as main | as main | 01 |

## 5. The ten rules that prevent wrong answers
1. **Grain first.** `dim_life` is one row per **life-period** (`LifeKey` x `UWY`), not per member: a renewing member
   has one row per UW year. Join claims and member-months to it on **`LifeKey` + `UWY`** (or `LifeID`), never on
   `LifeKey` alone (that duplicates claims across years).
2. **Never join two fact tables to each other** (`fact_claims` to `fact_member_month`). Aggregate each to the same
   cut first (e.g. UWY x TPA), then join the aggregates and divide (drill-across).
3. **Experience filter on claims:** the dashboard counts only `fact_claims` rows with `InExperience = 1` (treated on
   or before the valuation date). Lines with `InExperience = 0` are kept for reconciliation only.
4. **StatusClass Rejected** lines carry no Paid and no OS. Use `Paid`, `OS`, `UltimateAmount` columns as they are;
   do not re-derive them from `PayerShare`.
5. **Claim counts are visits, not lines:** sum `CountFlag` (one flagged line per visit with payer share > 0). Never
   count rows or distinct `ClaimKey`.
6. **Premium basis:** every premium and life-year column exists as `_Gross` and `_Net`. State the basis; the run's
   default is the key `default_premium_basis` in `run_manifest_premium.csv` (else Net).
7. **Written vs earned:** written premium in `fact_member_month` is **booked** in the period-start month (refunds in
   the month after the last covered day); earned premium is spread daily up to the valuation date. A "by month"
   question must say which.
8. **Claims UWY is assigned, not supplied:** `fact_claims.UWY` = the linked life-period's UWY (fallbacks in the column
   dictionary). Premium UWY = year of the policy coverage start date.
9. **Ultimates are claim-level:** `UltimateAmount` (IBNR basis) and `UltimateAmount_IBNP` sum under any cut, but
   factors are set per TPA x lag, so fine cuts (benefit, provider, region) are indicative.
10. **Check the version** before relying on any column: `run_manifest_claims.csv` key `contract_version` must be
    `IP4-13`. If it differs, say so: columns may have been added or changed since this skill was built.

## 6. How to answer
1. Name the table(s) and column(s) used, with the grain. Quote the column definition from the reference files; do
   not paraphrase it into something stronger.
2. For any figure: state premium basis (Gross / Net), claims basis (Paid / Incurred = Paid + OS / Ultimate), reserve
   basis (IBNR / IBNP) and the experience-to month, as the dashboard does.
3. When computing from files: give the exact filter and grouping (recipes in file 05). Print summaries only; never
   print row-level member or claim data.
4. If the files and this skill disagree, the files and `model_contract.json` in the client's
   `02_Inputs\Mapping\` win: say what differs.
5. Questions about **why** Merit derived a value (endorsement logic, mapping, linking rules) go to the Merit
   encyclopedia (`README\26_LenAI_encyclopedia.md` in the pack) or the tool owner; this skill covers what the
   outputs contain and how to use them.
6. Never invent a column, a code or a rule. If a column is not in the reference files, say it is not in contract
   IP4-13.


<!-- ===== FILE: references/01-core-tables.md ===== -->

# 01 Core tables: dim_life, fact_member_month, fact_claims

Contract IP4-13. Column definitions below are copied from `model_contract.json` (`describe` block)
without rewording; the notes above each table are the rules for using it.

## How the three tables link
```
dim_life (LifeKey, UWY) 1 ---- * fact_member_month (LifeKey, UWY, MonthStart)
dim_life (LifeKey, UWY) 1 ---- * fact_claims (LifeKey, UWY; blank LifeKey = not linked to a life)
```
- `LifeID` is a number for the same life-period (1..n). It is **renumbered every run**: use it inside one run
  only, never to compare runs (compare on `LifeKey` + `UWY`).
- `LifeKey` = Payer | TPA | policy | member, keys normalised the same way on premium and claims (upper case, trimmed,
  `_ - / '` removed; member keys also lose `.` and spaces; leading zeros kept).
- A `fact_claims` row with `MatchStatus = Ambiguous` has no single life (blank `LifeID`): it stays in claims totals
  but drops out of any cut by a `dim_life` attribute unless you keep unmatched rows (left join from claims).
- `Payer Name` and `TPA` are on all three tables: filter each table on them directly rather than through a join.

## dim_life
Grain: life-period: Payer\|TPA\|policy\|member x UWY. Key: `LifeKey` + `UWY`.
- Holds every member and policy attribute (bands, policy type, region, network, RI share) and the written totals
  per life-period. Earned figures here run to the valuation date; for an experience-to cut use `fact_member_month`.
- `UWY` = year of the policy coverage start date.
- Zero-premium life-periods (net premium summing to zero) carry no written or earned life-years.

| Column | Type | Meaning |
|---|---|---|
| `LifeID` | int | v7.2.0: whole-number key of the life-period (1..n over LifeKey, UWY; numbered afresh each run): the key the dashboard joins Member Month and Claims on |
| `LifeKey` | text | Payer\|TPA\|policy key\|member key (keys normalised: upper case, trimmed, '_' '-' '/' removed; member key also '.' and spaces) |
| `Payer Name` | text | Payer: the booking entity of the file (file register) |
| `Risk Carrier` | text | Risk carrier from the collated file |
| `MasterCedantName` | text | Master cedant (user input in every Alteryx workflow) |
| `TPA` | text | TPA (upper case) |
| `PolKey` | text | Normalised policy key |
| `MemKey` | text | Normalised member key |
| `UWY` | int | Underwriting year = year of policy coverage start |
| `PolicyStart` | date | Policy coverage start |
| `PolicyEndAdj` | date | Policy end after the TPA expiry convention (last covered day) |
| `AnnualBasisDays` | int | Days in the policy year from inception (365/366): life-year denominator |
| `CovStart` | date | First covered day of the life-period |
| `CovEnd` | date | Last covered day of the life-period |
| `Periods` | int | Coverage periods of the member in the term (after supersedes) |
| `CovDays` | int | Covered days, all periods |
| `EarnedDays` | int | Covered days up to the valuation date |
| `ZP_Gross` | int | 1 if the life-period's gross premium is non-zero (else no exposure counted, SPEC 3.7) |
| `ZP_Net` | int | 1 if the life-period's net premium is non-zero |
| `WrittenLY_Gross` | double | Written life-years = CovDays / AnnualBasisDays x ZP_Gross |
| `WrittenLY_Net` | double | Same on the net basis |
| `EarnedLY_Gross` | double | Earned life-years = EarnedDays / AnnualBasisDays x ZP_Gross |
| `EarnedLY_Net` | double | Same on the net basis |
| `WrittenPrem_Gross` | double | Sum of the life-period's gross premium rows (additions, refunds, corrections) |
| `WrittenPrem_Net` | double | Same on the net basis |
| `EarnedPrem_Gross` | double | Gross premium earned to the valuation date (each row daily pro-rata over its own period) |
| `EarnedPrem_Net` | double | Same on the net basis |
| `RI Name` | text | Reinsurer: standard value from the inputs workbook, else the raw value upper-cased |
| `Policy Type` | text | Policy type: standard value from the inputs workbook, else the raw value upper-cased |
| `PolicyTypeUsed` | text | Policy type used: the Policy type calcs rule where one applies, else supplied, else SME if the lives in force at inception are below sme_max_lives (default 200), else Group (IP4-9, owner 2026-10-26 Q-07) |
| `PolicyTypeSource` | text | raw (supplied) / calc (Policy type calcs rule) / derived (lives): lives in force at inception against sme_max_lives |
| `Master Contract ID` | text | Master contract (links renewals) |
| `Contract Name` | text | Contract name |
| `Relation` | text | Relation: standard value, else the raw value upper-cased |
| `Gender` | text | Gender as supplied |
| `Marital Status` | text | Marital status: standard value, else the raw value upper-cased |
| `Nationality` | text | Nationality as supplied |
| `Region` | text | Region / health authority as supplied |
| `Network` | text | Network: standard value from the inputs workbook, else the raw value upper-cased |
| `Plan / Category` | text | Plan or category |
| `Member DOB` | date | Date of birth |
| `AgeAtInception` | int | Completed years at cover start |
| `AgeBand` | text | Age band (config/run.json) |
| `GroupSize` | int | Distinct members on the policy term |
| `GroupSizeBand` | text | Group-size band |
| `NewRenewal` | text | New / Renewal (v6.4 evidence rule; Unknown before v6.4) |
| `NewRenewalSource` | text | master contract link / member continuity / inception date / no link to the prior UW year; first UW year of the payer x TPA (IP4-9): inception date / raw column / endorsement type / first UW year, no evidence |
| `Joiner` | int | 1 if cover starts after the policy start |
| `Leaver` | int | 1 if cover ends before the policy end |
| `Tenure` | int | UWY - first UWY of the master contract in the data |
| `Currency` | text | Currency |
| `Country` | text | Country |
| `EndoGroup` | text | Endorsement-logic grouping, one per life-period, first match in this order: No coverage period, Void ab initio (every period void), Reinstated (policy reactivation), Member reactivation, Closing row without opening, Re-opened (overlap), Cancelled, Deleted, Addition in force, Initial/Renewal in force |
| `EndoPath` | text | Periods in order as Opening>Closing, ' \| ' between periods; '(void)' = closed on or before its start; Closing: open, Deletion, Cancellation, Overlap |
| `VoidPeriods` | int | Periods void ab initio (closure on or before the start, incl. overlap closures, R1) |
| `OverlapVoidPeriods` | int | Periods voided by an overlap closure on their own start day (R1) |
| `ReinstatedPeriods` | int | Periods reopened by a policy reactivation (R2: only members closed by the cancellation) |
| `MemberReactPeriods` | int | Periods opened by a member reactivation |
| `Region Group` | text | Health authority from the inputs workbook (e.g. HAAD / DHA / MOH); no rule = the raw value, upper-cased; empty = Not Available |
| `Nationality Group` | text | Nationality group from the inputs workbook (GCC Arab / Other Arab / Indian-Subcontinent / Asian / Western Expat / Other; tab Nationality groups); a spelling with no rule = Other; empty = Not Available |
| `Gender Group` | text | Male / Female / Maternity Eligible Female (female aged 18-45 at inception); no rule = the raw value, upper-cased; empty = Not Available |
| `Distribution` | text | Distribution channel as supplied (owner 2026-10-08) |
| `Opt_1` | text | Optional field 1 as supplied (raw text; v8.0.4, TPA_RULES 93.2): its display label and type (Text / Number) are on the Mapping workbook's Payer tab and reach the dashboard through run_manifest; blank when not mapped |
| `Opt_2` | text | Optional field 2 as supplied (raw text; v8.0.4, TPA_RULES 93.2): its display label and type (Text / Number) are on the Mapping workbook's Payer tab and reach the dashboard through run_manifest; blank when not mapped |
| `Opt_3` | text | Optional field 3 as supplied (raw text; v8.0.4, TPA_RULES 93.2): its display label and type (Text / Number) are on the Mapping workbook's Payer tab and reach the dashboard through run_manifest; blank when not mapped |
| `Opt_4` | text | Optional field 4 as supplied (raw text; v8.0.4, TPA_RULES 93.2): its display label and type (Text / Number) are on the Mapping workbook's Payer tab and reach the dashboard through run_manifest; blank when not mapped |
| `Opt_5` | text | Optional field 5 as supplied (raw text; v8.0.4, TPA_RULES 93.2): its display label and type (Text / Number) are on the Mapping workbook's Payer tab and reach the dashboard through run_manifest; blank when not mapped |
| `ReinsuredPct` | double | Reinsured % of the life's policy, 0-1 (TPA_RULES 25.1): the inputs workbook tab 'RI policy shares' for a payer listed there (0 = retained policy; blank = listed with no share or not listed: not known), 1 for a payer not on the tab; a RESHARE scope rule's share wins |
| `ReinsuredPctSource` | text | Where ReinsuredPct comes from: Policy table / Policy table: not yet known / Not in the policy table / Payer not in the policy table: 100% / Scope rule <id> |
| `TreatyCededPct` | double | Sum of the non-retained shares of the life's RI Name x UWY on the inputs workbook tab 'RI treaty shares' (blank = no treaty rows) |
| `CededPct` | double | ReinsuredPct x TreatyCededPct: the share of the life's premium and claims ceded under the treaty (blank when either is blank) |
| `ScopeStatus` | text | In scope (main tables) or Excluded (the *_excluded twin tables): the scope register (v7.6.0, intake apply) |
| `ScopeRule` | text | Main tables: the scope rules applied to the row (RESHARE, CARVEOUT, CAP ids); twin tables: the rule that excluded it |

## fact_member_month
Grain: life-period x calendar month. Key: `LifeKey` + `UWY` + `MonthStart`.
- The sum over months of each life-period equals its `dim_life` totals (the `FanDiff_*` checks in `recon_premium`
  are this difference; they must be 0 within 0.01 per TPA).
- Earned columns run to the valuation date; written columns are booked in their booking month. Filter
  `MonthStart <= experience-to month` to reproduce the dashboard at an experience-to cut.

| Column | Type | Meaning |
|---|---|---|
| `LifeID` | int | v7.2.0: LifeID of the life-period (dim_life) |
| `LifeKey` | text | Life key (dim_life) |
| `UWY` | int | Underwriting year |
| `Payer Name` | text | Payer |
| `TPA` | text | TPA |
| `MonthStart` | date | Calendar month (first day) |
| `EarnedDays` | int | Covered days in the month, up to the valuation date |
| `EarnedLY_Gross` | double | Earned life-years in the month (gross zero-premium rule) |
| `EarnedLY_Net` | double | Same, net rule |
| `EarnedPrem_Gross` | double | Gross premium earned in the month |
| `EarnedPrem_Net` | double | Net premium earned in the month |
| `WrittenPrem_Gross` | double | Gross premium booked in the month (member-start month; refunds in the refund month) |
| `WrittenPrem_Net` | double | Same on the net basis |
| `WrittenLY_Gross` | double | Written life-years booked in the period-start month |
| `WrittenLY_Net` | double | Same, net rule |
| `ScopeStatus` | text | In scope (main tables) or Excluded (the *_excluded twin tables): the scope register (v7.6.0, intake apply) |
| `ScopeRule` | text | Main tables: the scope rules applied to the row (RESHARE, CARVEOUT, CAP ids); twin tables: the rule that excluded it |

## fact_claims
Grain: claim line (reversals netted within ClaimID upstream or kept as lines; sums are additive). Key: `ClaimKey`.
- Every claim line linked to a life (in or out of cover) or ambiguous. Unmatched lines and lines treated before the
  TPA's first policy inception are **not** in this table: they are counted in `recon_claims` (`excluded_unmatched`,
  `excluded_pre_inception`).
- Paid + OS = the reported payer share of a line. `PayerShare` is the amount as supplied.
- Identities on each line: Approved = Claimed - Declined - Discounts (where supplied).

| Column | Type | Meaning |
|---|---|---|
| `ClaimKey` | text | Unique claim line key |
| `Payer Name` | text | Payer |
| `TPA` | text | TPA |
| `UWY` | int | UWY of the matched life-period; else of the policy term holding the treatment date; else the claims file UWY; else the treatment year (Q-C1) |
| `LifeKey` | text | Matched life (blank = unmatched) |
| `LifeID` | int | v7.2.0: LifeID of the linked life-period (dim_life); blank = not linked (Ambiguous) |
| `PolKey` | text | Normalised policy key |
| `MemKey` | text | Normalised member key |
| `ClaimID` | text | Claim identifier (Q-C5): TPA\|policy\|member\|treatment date\|provider\|ICD\|payer share#n (n = running number of identical lines) |
| `ClaimantKey` | text | Claimant (life key, else raw keys) |
| `MatchTier` | text | T1 policy + member, in cover / T1 policy + member, out of cover / T2 member + treatment date / Ambiguous / Unmatched |
| `MatchStatus` | text | Matched / Matched-OutOfCover / Ambiguous / Unmatched (SPEC P4) |
| `InCover` | int | 1 if treatment date within a coverage period |
| `InExperience` | int | 1 if treated on or before the valuation date (Q-V1); 0 = in recon only |
| `StatusClass` | text | Paid / Outstanding / Rejected / Unknown (claim status of the source sheet or the Claim status tab; Rejected counts in neither Paid nor OS) |
| `Claim Type` | text | As supplied (claims status / approval decision column); a pivot only, nothing excluded (Q-C7) |
| `FOB` | text | Benefit class (field of benefit), standard value from the Value maps tab (Out-Patient / In-Patient / Maternity / Dental / Optical / Psychiatry / ...) |
| `FOC` | text | Sub-class (field of cover), standard value from the Value maps tab |
| `ICD Code` | text | Diagnosis code split from the supplied value (ICD-10 with the dot after the 3rd character, or ICD-9); Not Available when the value holds no code (some TPAs supply chapters only) |
| `ICD Description` | text | Description of the code from the ICD codes tab of the inputs workbook (CDC ICD-10-CM), else the text supplied after the code |
| `ICD Chapter` | text | ICD-10-CM chapter of the code (ICD codes tab), else the supplied chapter by the 'ICD Chapter' rules (TPAs that supply chapters only) |
| `Provider Name` | text | Provider |
| `Provider Type` | text | Standard value from the Value maps tab (Hospital / Clinic / Medical Center / Pharmacy / Diagnostic Center ...) |
| `Provider Region` | text | Provider region as supplied |
| `TreatmentDate` | date | Date of treatment |
| `IncurredMonth` | date | Treatment month |
| `ReportedMonth` | date | Reporting date, else processed date, else payment date, else (outstanding) the claims extract month |
| `PaidMonth` | date | Payment date, else processed date (paid lines; blank if unpaid) |
| `RepLag` | int | Months from treatment to report |
| `PaidLag` | int | Months from treatment to payment |
| `Claimed` | double | Amount claimed (blank when the claims files do not supply it) |
| `Declined` | double | Amount declined |
| `Discounts` | double | Provider discounts |
| `Approved` | double | Claimed - Declined - Discounts |
| `BeneficiaryShare` | double | Member co-pay |
| `PayerShare` | double | Payer share as supplied (reported amount) |
| `Paid` | double | Payer share of the paid sheets |
| `OS` | double | Payer share of the outstanding (OS) sheets |
| `CountFlag` | int | 1 on one line of a visit (TPA, policy, member, provider, treatment date) whose payer share totals > 0 (O7): its first line with a payment when the visit's net paid is above zero, else its first line (source order; IP4-9, owner 2026-10-26 Q-17) |
| `LargeFlag` | int | 1 if the visit's payer share >= run.json large_claim_threshold (O8: AED 100k) |
| `SrcOrder` | int | Source position x 1,000,000 + Excel row |
| `MasterCedantName` | text | Master cedant (user input in every Alteryx workflow) |
| `RI Name` | text | Reinsurer from the claims file (user input for a TPA whose file has none) |
| `DevLag` | int | Months from the incurred month to the claims extract month |
| `CF_Basis` | text | IBNR basis (factor applied to paid + pending): IBNR, or No factor (CF = 1) when the TPA has no IBNR factors. never the text None, which pandas and other readers turn into a blank |
| `CF_Amount` | double | IBNR amount completion factor of the TPA and lag (inputs workbook; 1 if none or beyond the last lag) |
| `CF_Count` | double | IBNR count completion factor likewise (1 if no count factors are supplied) |
| `UltimateAmount` | double | Claim-level ultimate, IBNR basis: (paid + pending) / CF_Amount; a lag-0 cell of a TPA with a BF expected loss ratio (Run settings): the cell's Bornhuetter-Ferguson ultimate spread over its lines pro rata to paid + pending (IP4-9) |
| `UltimateCount` | double | Claim-level ultimate count, IBNR basis: CountFlag / CF_Count |
| `Provider Region Group` | text | Provider region mapped by the Region rules of the inputs workbook (DXB / AUH / NE / Not Mapped) |
| `CF_Basis_IBNP` | text | IBNP basis (factor applied to paid): IBNP, or No factor (CF = 1) when the TPA has no IBNP factors (v5.15) |
| `CF_Amount_IBNP` | double | IBNP amount completion factor of the TPA and lag (1 if none or beyond the last lag) |
| `CF_Count_IBNP` | double | IBNP count completion factor likewise (1 if none) |
| `UltimateAmount_IBNP` | double | Claim-level ultimate, IBNP basis: paid / CF_Amount_IBNP; BF cells as UltimateAmount, pro rata to paid (IP4-9) |
| `UltimateCount_IBNP` | double | Claim-level ultimate count, IBNP basis: CountFlag of a visit whose net paid is above zero / CF_Count_IBNP |
| `ScopeStatus` | text | In scope (main tables) or Excluded (the *_excluded twin tables): the scope register (v7.6.0, intake apply) |
| `ScopeRule` | text | Main tables: the scope rules applied to the row (RESHARE, CARVEOUT, CAP ids); twin tables: the rule that excluded it |
| `PayerShareCapped` | double | Payer share after the claimant's CAP (scope register, per life-period, allocated chronologically by treatment date then source order); = PayerShare without a cap |
| `PayerShareExcess` | double | PayerShare - PayerShareCapped (the amount above the cap) |

## The excluded twins
- `dim_life_excluded`: same columns as `dim_life`; grain life-period: Payer\|TPA\|policy\|member x UWY (excluded by the scope register).
- `fact_member_month_excluded`: same columns as `fact_member_month`; grain life-period x calendar month (excluded by the scope register).
- `fact_claims_excluded`: same columns as `fact_claims`; grain claim line (reversals netted within ClaimID upstream or kept as lines; sums are additive) (excluded by the scope register).

These hold what the scope register (`02_Inputs\Merit_CONTROLS.xlsx`) excluded at intake. They are **not** part of any
dashboard total. Use them only to show what was excluded and why (`ScopeRule`). In `scope_tags` a negative `LifeID`
points to `dim_life_excluded`.


<!-- ===== FILE: references/02-reserving-tables.md ===== -->

# 02 Reserving tables: ultimates, cf_selected, 03b dev_*

Contract IP4-13. Column definitions copied from `model_contract.json`.

## The two reserving bases
| Basis | Base amount | Factor means | Ultimate column (fact_claims) | Reserve |
|---|---|---|---|---|
| IBNR (default) | Paid + OS (paid + pending) | share of the ultimate **reported** by that lag | `UltimateAmount` | IBNR = Ultimate - Reported |
| IBNP | Paid | share of the ultimate **paid** by that lag | `UltimateAmount_IBNP` | IBNP = Ultimate_IBNP - Paid |

- Lag = months from the incurred month to the **claims extract month** (`DevLag` on each line).
- Each line's ultimate = its base / the TPA's completion factor at its lag; a TPA with no factors has CF = 1 and
  `CF_Basis` = "No factor (CF = 1)". Merit applies the factors; it does not select them (inputs workbook, or 03b's
  derived vectors where the development workbook switches a TPA to them).
- A lag-0 cell of a TPA with a Bornhuetter-Ferguson expected loss ratio uses the BF ultimate, spread over its lines
  pro rata (see `Method`).
- Example: a claim of 1,000 paid + outstanding, lag 3, factor 0.9649 -> ultimate 1,036.35, IBNR 36.35.

## ultimates
Grain: Payer x TPA x incurred month x UWY (reported claims keep their UWY; IBNR allocated to UWY by earned premium of the month, SPEC P5.7). Key: `Payer Name` + `TPA` + `IncurredMonth` + `UWY`.
- `Ultimate` equals the sum of `fact_claims.UltimateAmount` (InExperience = 1) for the same cell, so either source gives
  the same totals at payer x TPA x incurred month x UWY. Use `fact_claims` for any other cut.

| Column | Type | Meaning |
|---|---|---|
| `Payer Name` | text | Payer |
| `TPA` | text | TPA |
| `IncurredMonth` | date | Incurred month |
| `UWY` | int | Underwriting year |
| `Lag` | int | Months from the incurred month to the claims extract month |
| `CF_Used` | double | Amount completion factor at the lag (1 if none) |
| `CF_Count_Used` | double | Count completion factor (1 if none) |
| `Reported` | double | Reported payer share (paid + outstanding), in experience |
| `Paid` | double | Paid payer share |
| `OS` | double | Outstanding payer share |
| `IBNR` | double | Ultimate - Reported |
| `Ultimate` | double | Sum of the claim-level ultimates (fact_claims UltimateAmount) of the cell; a BF cell: Reported + (1 - CF_Used) x expected loss ratio x the month's net earned premium (IP4-9) |
| `ReportedCount` | double | Reported claim count (CountFlag) |
| `UltimateCount` | double | Sum of the claim-level ultimate counts of the cell |
| `Method` | text | IBNR factor basis used ('<basis> factors (inputs workbook)' / 'No factors (CF = 1)'); a BF cell: 'BF: expected loss ratio x net earned premium (...)' naming the bases it applies to (IP4-9); v7.7.0 (IP4-11): '<basis> factors (03b)' for a 03b vector, 'BF (03b): ...' / 'Benktander (03b): expected loss ratio x net earned premium \| PMPM x member-months (...)' for a cell 03b's BF settings changed |
| `PaidCount` | double | Claims paid: counted visits whose net paid is above zero |
| `CF_Basis` | text | IBNR / No factor (see fact_claims) |
| `CF_Used_IBNP` | double | IBNP amount completion factor at the lag (1 if none) |
| `CF_Count_Used_IBNP` | double | IBNP count completion factor (1 if none) |
| `IBNP` | double | Ultimate_IBNP - Paid |
| `Ultimate_IBNP` | double | Sum of the claim-level IBNP-basis ultimates (fact_claims UltimateAmount_IBNP) of the cell; a BF cell: Paid + (1 - CF_Used_IBNP) x expected loss ratio x net earned premium (IP4-9) |
| `UltimateCount_IBNP` | double | Sum of the claim-level IBNP-basis ultimate counts of the cell |
| `CF_Basis_IBNP` | text | IBNP / No factor (see fact_claims) |

## cf_selected
Grain: TPA x Basis (Reported/Paid) x Measure (Amount/Count) x Lag 0-12. Key: `TPA` + `Basis` + `Measure` + `Lag`.
- The factors used in the run, one row per TPA x basis x measure x lag. A lag beyond the last factor uses 1.

| Column | Type | Meaning |
|---|---|---|
| `TPA` | text | TPA |
| `Basis` | text | IBNR (applied to paid + pending) or IBNP (applied to paid) |
| `Measure` | text | Amount or Count (separate factors) |
| `Lag` | int | Months from incurred month to claims extract month |
| `CF_Derived` | double | Blank for an inputs-workbook factor; v7.7.0 (IP4-11): 03b's derived factor where it is applied (Source '03b derived') |
| `CF_Override` | double | Blank |
| `CF_Used` | double | The factor applied: the inputs workbook's, or 03b's vector for a TPA x basis the development workbook switches to derived factors (v7.7.0) |
| `Source` | text | Inputs workbook (placeholder / synthetic placeholder when the Note says so); v7.7.0: '03b derived', '03b fallback: inputs workbook', '03b fallback: 1 (no user factor)' |
| `Credible` | int | 1 for an inputs-workbook factor; 03b: 1 = the lag cell is eligible (volume and every later lag), 0 = fallback |
| `Cohorts` | int | Blank; 03b: incurred months behind the link ratio of the lag |
| `Claims` | int | Blank; 03b: claims (counted visits) behind the link ratio of the lag |

## 03b development tables (`csv\dev_*.csv`, `xlsx\Merit_03b_Development.xlsx`)
Written by the optional 03b development step (derived completion factors with diagnostics). Not part of the
output contract's column list; the sheet and table pairs are:

| Sheet / table | Key columns | Read it for |
|---|---|---|
| TPA summary / `dev_tpa` | Coverage, MatureCohorts, SpeedMaxDev, SpeedStatus, Applied, Reason, FactorSetID, BT_* | Was each basis applied, and why not |
| Factors / `dev_factors` | LinkRatio, CF_Raw, CF_Chain, Claims, Cohorts, Eligible, Reason, CV, Z, CF_Inputs, CF_Derived, Diff_pct, CF_Applied, Source | The vectors, lag by lag |
| Link ratios / `dev_link_ratios` | per window 3/6/12/24/ALL (+ yours) | Stability |
| Triangles / `dev_triangles` | Cumulative, Incremental | The data behind the factors |
| BF / `dev_bf` | SuggestedMaxLag, ELR_CapeCod, PMPM, ImpliedELR, MaxLag, Weight, Prior, Applied | BF settings |
| Seasonality / `dev_season` | UltimateTrended, MemberMonths, PMPM, Used, RamadanDays, Index | Seasonal pattern |
| Backtest / `dev_backtest` | Actual, Pred_Derived, Pred_Inputs, Err_* | Which factor set predicts better |
| Large claims / `dev_large` | CF_All / NoLarge / Capped, IBNR_*, Delta_*, LargeShare | Large-claim sensitivity |
| Segments / `dev_segments` | CF_Segment, CF_TPA, Ratio | FOB differences |
| Calendar AE / `dev_calendar` | Actual, Expected, AE | Diagonal effects |
| Checks / `dev_checks` | Code, Severity, Message | Every finding |

Which 03b factor sets and BF settings the claims run applied: `run_manifest_claims` keys `development_factors` and
`development_bf`. For the method behind these tables use `README\24_Development_factors.md` in the pack.


<!-- ===== FILE: references/03-control-tables.md ===== -->

# 03 Control tables: recon, exceptions, run_manifest, scope, diagnostics

Contract IP4-13. Column definitions copied from `model_contract.json` where the contract defines them.

## recon_premium.csv, recon_claims.csv
Shape: one row per TPA, one column per control total (the dashboard unpivots it to Measure / Value). **All UW years, no date cut.**

**recon_premium (per TPA):** rows_in, rows_unmapped, rows_ignored, rows_missing, rows_duplicate, rows_excluded (row
filters), rows_overlap (source priority), life_periods, Gross_in, Net_in, expiry_exclusive,
expiry_modal_excess_days, WrittenPrem / EarnedPrem / WrittenLY / EarnedLY x Gross / Net, and each `FanDiff_*`
(monthly table minus dim_life; must be 0 within 0.01 per TPA).
- `Net_in` / `Gross_in` = premium read on every collated row before any drop. So `Net_in - WrittenPrem_Net` = the
  premium on the rows the premium workflow dropped (each listed in `exceptions.csv` with its code and source row).

**recon_claims (per TPA):** claim_lines_in, payer_share_in, paid_in, os_in (check: payer share in = paid in + OS in),
no_treatment_date, claims_after_valuation, payer_share_experience, matched_lines, member_date_lines (tier 2),
out_of_cover_lines, ambiguous_lines, unmatched_lines, matched_share, match_rate_amount, visits_counted,
ultimate_experience, excluded_pre_inception, excluded_unmatched, excluded_paid, excluded_paid_os.
- Match Rate (Count) = (matched_lines + out_of_cover_lines) / claim_lines_in; Match Rate (Amount) = matched_share /
  payer_share_in; whole extract before exclusions, by TPA. Below 95% = E-CL-MATCHRATE (warning, run continues).
- Rows held back **before** the workflows (quarantined, excluded by a scope rule, collapsed as exact duplicates at
  intake) never reach recon: they are in `dq_recon_scope` and `dq_quarantine`.

## exceptions.csv (premium), exceptions_claims.csv (claims)
Grain: one row per finding. Codes start E- (stop), W- (flag) or I- (info). Look up a code in the encyclopedia's
message-code glossary (`README\26_LenAI_encyclopedia.md` section 5) rather than guessing its meaning.

| Column | Type | Meaning |
|---|---|---|
| `Code` | text | Finding code (E- stop, W- flag, I- info) |
| `Severity` | text | Stop / Flag / Info |
| `TPA` | text | TPA |
| `PolKey` | text | Policy key |
| `MemKey` | text | Member key |
| `SrcOrder` | int | Source row |
| `Message` | text | Plain-language finding |
| `Gross Premium` | double | exceptions.csv only (v8.0.4, TPA_RULES 93.6): Gross Premium of the collated premium row the finding is about; blank for a finding about a life, a policy or a TPA |
| `Net Premium` | double | exceptions.csv only (v8.0.4): Net Premium of that row; blank as Gross Premium |
| `Payer Share` | double | exceptions_claims.csv only (v8.0.4): payer share of the claim line the finding is about; E-CL-MATCHRATE: the TPA's payer share not linked to a life (recon payer_share_in - matched_share); blank otherwise |

## run_manifest_premium.csv, run_manifest_claims.csv
Two columns, `Key` and `Value` (text). One row per setting of the run. Keys in contract IP4-13:
`valuation_date`, `claims_extract_date`, `premium_extract_date`, `workflow`, `workflow_version`, `default_premium_basis`, `currency`, `large_claim_threshold`, `has_member_dob`, `has_claim_dob`, `has_paid_date`, `has_reported_date`, `has_icd`, `has_provider`, `has_fob`, `contract_version`, `development_factors`, `development_bf`

Defined keys:
| Column | Type | Meaning |
|---|---|---|
| `Key` | text | Setting name |
| `Value` | text | Setting value (text) |
| `contract_version` | | v7.3.2: the version of this contract (its version field) the run was written to; in run_manifest_premium and run_manifest_claims; read by downstream consumers (Pricing-workbench V0, Merit AI G1.1) to refuse a run of another version |
| `development_factors` | | v7.7.0: the 03b factor-set ids applied by the claims workflow (';' separated), or 'inputs workbook' |
| `development_bf` | | v7.7.0: the 03b BF settings applied, TPA:max lag:weight:prior (';' separated), or 'none' |

- Which file holds which key: the premium manifest holds the premium settings (`workflow`, `workflow_version`,
  `default_premium_basis`, `currency`, `premium_extract_date`); the claims manifest holds the claims ones, with the
  workflow keys prefixed (`claims_workflow`, `claims_workflow_version`), plus `large_claim_threshold`, the `has_*`
  flags and the `development_*` keys. Both hold `valuation_date`, `claims_extract_date` and `contract_version`. Read
  a key from whichever file has it.
- `valuation_date`: exposure and earned premium run to it; claims treated after it have `InExperience = 0`.
- `claims_extract_date`: development lags run to its month.
- Capability flags `has_*` say which optional source fields existed (e.g. no `has_paid_date` = no paid lags).

## scope_tags
Grain: tag x row (a life-period or a claim line) x rule.

| Column | Type | Meaning |
|---|---|---|
| `LifeID` | int | The tagged life-period (dim_life or, negative, dim_life_excluded); blank for a claim-line tag |
| `ClaimID` | text | The tagged claim line (fact_claims / fact_claims_excluded); blank for a life-period tag |
| `Tag` | text | The tag (Scope tags tab of 02_Inputs\Merit_CONTROLS.xlsx) |
| `ScopeRule` | text | The rule that gave the tag (Scope rules / Special acceptances) |

## diagnostics.csv and the dq_ tables (post-run diagnostics, optional)
Shown in `xlsx\Merit_Diagnostics.xlsx` and on the dashboard's data-quality pages. Only a Stop means the run is not fit
to use. Counts and amounts only, never identifiers.

### diagnostics
Grain: finding: Code x Side x TPA x UWY (counts and amounts only).

| Column | Type | Meaning |
|---|---|---|
| `Code` | text | Finding code (E-/S- stop, W- flag, I- information; user guide 'What the codes mean') |
| `Severity` | text | Stop / Flag / Info |
| `Side` | text | premium / claims / both |
| `TPA` | text | TPA (blank = all) |
| `UWY` | text | Underwriting year (blank = all) |
| `Rows` | double | Rows concerned |
| `Amount` | double | Amount concerned (net premium or payer share) |
| `Share` | double | Share of the TPA's (or the run's) total the finding concerns |
| `Message` | text | Plain-language finding |

### dq_recon_scope
Grain: Side x TPA x UWY ('(all)' = every year) x Measure (rows / amount). Identity: Difference = Read - (InScope + Excluded + Quarantined + Duplicates); PASS when 0.

| Column | Type | Meaning |
|---|---|---|
| `Side` | text | premium / claims |
| `TPA` | text | TPA |
| `UWY` | text | Underwriting year; '(all)' = the TPA's total |
| `Measure` | text | rows or amount |
| `Read` | double | Read by intake apply |
| `InScope` | double | In the in-scope collated file |
| `Excluded` | double | Excluded by the scope register |
| `Quarantined` | double | Held in quarantine (Stage A) |
| `Duplicates` | double | Collapsed as duplicates |
| `CarvedOut` | double | Premium removed by CARVEOUT rules (amount only) |
| `Difference` | double | Read - (in scope + excluded + quarantined + duplicates) |
| `Status` | text | PASS / E-RECON-SCOPE |

### dq_recon_control
Grain: control total: Payer x TPA x Side x Measure x Period. Compares Merit with control totals the user entered (Control totals tab of
`Merit_CONTROLS.xlsx`).

| Column | Type | Meaning |
|---|---|---|
| `Payer` | text | Payer |
| `TPA` | text | TPA |
| `Side` | text | premium / claims |
| `Measure` | text | Controlled measure |
| `PeriodBasis` | text | How Period is read (UWY / month ...) |
| `Period` | text | Period of the control total |
| `Control` | double | The control total given (Control totals tab of Merit_CONTROLS.xlsx) |
| `Merit` | double | Merit's total on the same cut |
| `Difference` | double | Merit - Control |
| `DifferencePct` | double | Difference / Control |
| `Source` | text | Where the control total came from |
| `AsAt` | text | Date of the control total |
| `Status` | text | PASS / W-CONTROL / E-CONTROL / I-CONTROL / W-CONTROL-NODATA |

### dq_quarantine
Grain: quarantined source row x failed rule (no identifiers).

| Column | Type | Meaning |
|---|---|---|
| `Code` | text | Quarantine code |
| `Rule` | text | The data-quality rule that held the row |
| `Side` | text | premium / claims |
| `TPA` | text | TPA |
| `UWY` | text | Underwriting year of the row |
| `SourceFile` | text | Source file name |
| `SourceRow` | int | Row in the source file |
| `Field` | text | Field that failed |
| `AmountField` | text | Amount field held |
| `Amount` | double | Amount held |

## Other CSVs you may see in csv\
- `value_map_discovery*.csv`: raw values left unmapped, weighted by amount (feed the Mapping workbook's Values tab).
- Anything else not listed in this skill or in `model_contract.json` is internal: do not build analysis on it.


<!-- ===== FILE: references/04-excel-outputs.md ===== -->

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


<!-- ===== FILE: references/05-measures-and-recipes.md ===== -->

# 05 Dashboard measures and recipes from the files

## 1. How the dashboard reads the files
Power BI loads the `csv\` (or `parquet\`) tables as they are; every calculation is a DAX measure. Relationships:

| From | Column | To |
|---|---|---|
| fact_member_month, fact_claims | LifeID | dim_life (LifeID) |
| fact_member_month | MonthStart | Date |
| fact_claims, ultimates | IncurredMonth | Date |
| fact_member_month, fact_claims, ultimates | UWY / TPA / Payer Name | UW Year / TPA / Payer dimensions |
| cf_selected, recon, exceptions, diagnostics, dq_recon_scope | TPA | TPA |

So a dashboard UW year means **each fact's own UWY** (premium: life-period UWY; claims: assigned claim UWY), and a
dashboard month means **MonthStart** for premium and **IncurredMonth** for claims.

## 2. Bases and the experience cut
- **Premium basis** Gross / Net: slicer, else the run default (`run_manifest_premium` `default_premium_basis`, else Net).
- **Claims basis** Paid / Incurred (paid + outstanding; default) / Ultimate.
- **Reserve basis** IBNR (ultimate from paid + pending; default) / IBNP (ultimate from paid; Outstanding shown as 0).
- **Experience to** (month): slicer, else the report parameter `pExperienceTo`, else the valuation month; never after
  the valuation month. Claims incurred, premium earned and written premium booked up to it; ultimates are still
  developed to the same claims extract (it means "as known at the extract", not "as reported at that date").
- **Claims amount** Uncapped / Capped: Capped uses Paid and OS x PayerShareCapped / PayerShare.

## 3. Main measures (definitions)
| Measure | Definition | From the files |
|---|---|---|
| Written Premium | selected basis, booked up to Experience-to | Σ fact_member_month.WrittenPrem_<basis>, MonthStart <= cut |
| Earned Premium | earned to the cut, selected basis | Σ fact_member_month.EarnedPrem_<basis>, MonthStart <= cut |
| Written LY / Earned LY | life-years written / earned; zero-premium life-periods excluded | Σ WrittenLY_<basis> / EarnedLY_<basis>, MonthStart <= cut |
| Lives Earned | life-periods with earned days | distinct LifeID with EarnedDays > 0, MonthStart <= cut |
| Paid | payer share paid, claims treated by the cut | Σ fact_claims.Paid, InExperience = 1, IncurredMonth <= cut |
| Outstanding (Case) | TPA-reported outstanding, any reserve basis | Σ fact_claims.OS, same filter |
| Reported Claims | Paid + Outstanding (Case) | |
| Incurred | Paid + Outstanding (IBNR basis) / Paid (IBNP basis) | |
| Ultimate Claims | sum of claim-level ultimates on the reserve basis | Σ UltimateAmount (IBNR) or UltimateAmount_IBNP (IBNP), same filter |
| IBNR / IBNP | Ultimate - (paid + pending) / Ultimate - paid | |
| Claim Count | counted visits | Σ CountFlag, same filter |
| Ultimate Claim Count | count ultimates | Σ UltimateCount (or _IBNP), same filter |
| Loss Ratio | claims (selected basis) / earned premium (selected basis); also Paid LR, Incurred LR, Ultimate LR | |
| Frequency | claims per earned life-year | Claim Count / Earned LY |
| Burning Cost per LY | claims / earned LY (= frequency x severity) | |
| Gain / Loss | earned premium - claims, selected bases | |
| Earned Premium per LY / PMPM | average premium per earned LY / per member-month | |
| Match Rate (Count / Amount) | from recon_claims; red below 95% | see 03-control-tables |

Two adjustments can make the dashboard differ from a plain file sum, and both are visible on its pages: a
pre-adjudication basis other than Full claimed (changes reported outstanding and counts only), and UWY ultimate
adjustment factors on the Adjustment factors page (100% = none). Ask which are set before reconciling.

## 4. Recipes (pandas)
Read every key column as text. CSV in the LenAI Python sandbox (no Parquet there); Parquet or CSV with native `py`.
```python
import pandas as pd
o = r"<client>\04_Outputs\csv"
dl = pd.read_csv(f"{o}\\dim_life.csv", dtype={"LifeKey": str, "UWY": int})
mm = pd.read_csv(f"{o}\\fact_member_month.csv", dtype={"LifeKey": str}, parse_dates=["MonthStart"])
fc = pd.read_csv(f"{o}\\fact_claims.csv", dtype={"LifeKey": str, "ClaimKey": str, "ClaimID": str},
                 parse_dates=["IncurredMonth"])
man = dict(pd.read_csv(f"{o}\\run_manifest_claims.csv", dtype=str).values)
assert man.get("contract_version") == "IP4-13", man.get("contract_version")
cut = pd.Timestamp(man["valuation_date"]).to_period("M").to_timestamp()   # or the experience-to month
basis = "Net"                                                              # or "Gross"
```
**Ultimate loss ratio by UW year x TPA (drill-across, never join the facts):**
```python
prem = (mm[mm.MonthStart <= cut].groupby(["UWY", "TPA"])[[f"EarnedPrem_{basis}", f"EarnedLY_{basis}"]].sum())
clm = (fc[(fc.InExperience == 1) & (fc.IncurredMonth <= cut)]
       .groupby(["UWY", "TPA"])[["Paid", "OS", "UltimateAmount", "CountFlag"]].sum())
t = prem.join(clm, how="outer").fillna(0)
t["Incurred LR"] = (t.Paid + t.OS) / t[f"EarnedPrem_{basis}"]
t["Ultimate LR"] = t.UltimateAmount / t[f"EarnedPrem_{basis}"]
t["Freq per 1,000 LY"] = 1000 * t.CountFlag / t[f"EarnedLY_{basis}"]
```
**Cut by a member attribute** (e.g. Policy Type): attach the attribute to each fact on `LifeKey` + `UWY` (one row per
key in dim_life, so the join cannot duplicate), then aggregate as above.
```python
attr = dl[["LifeKey", "UWY", "Policy Type"]]
fc2 = fc.merge(attr, on=["LifeKey", "UWY"], how="left", validate="many_to_one")   # unlinked lines keep NaN
assert len(fc2) == len(fc) and abs(fc2.Paid.sum() - fc.Paid.sum()) < 0.01         # join invariance
```
**Written premium by UW year that ties to recon_premium:** Σ `fact_member_month.WrittenPrem_<basis>` with no month
cut = Σ `dim_life.WrittenPrem_<basis>` = `recon_premium` WrittenPrem_<basis> per TPA.

## 5. Traps (each has caused a real wrong answer)
| Trap | Effect | Do instead |
|---|---|---|
| Join on LifeKey without UWY | claims or premium counted once per UW year of the member | join on LifeKey + UWY (or LifeID within one run) |
| Join fact_claims to fact_member_month | claims x months fan-out | aggregate each, then join the aggregates |
| Sum earned premium from dim_life for an experience-to cut | dim_life earns to the valuation date | use fact_member_month with MonthStart <= cut |
| Count rows or ClaimKey as claims | frequency inflated for TPAs that split visits | Σ CountFlag |
| Forget InExperience = 1 | claims treated after the valuation date included | filter it |
| Mix Gross premium with a Net run default | LR off by the commission / fee gap | state and use one basis |
| Pivot raw premium by approval date or a UWY column | UW year mismatch | UWY = year of the policy coverage start date |
| Compare written premium at a cut with a raw pivot | refunds book in the month after the last covered day | prove the tie with no cut first, then apply the cut |
| Use LifeID to compare two runs | renumbered every run | LifeKey + UWY |
| Sum OS across extracts or months as a flow | OS is a balance at the extract | use it at one extract only |
| Read the `_excluded` tables into totals | adds scope-excluded business | main tables only |
| Treat fine-cut ultimates as precise | factors are per TPA x lag | call them indicative below payer x TPA x UWY x month |


<!-- ===== FILE: references/09-source-register.md ===== -->

# 09 Source register and checks

## What this skill describes
| Item | Version |
|---|---|
| Skill | 1.0.0, generated 2026-11-11 |
| Merit release | v9.2.0 |
| Output contract (`model_contract.json` version) | IP4-13 |
| Workflows | IP2-0.33 (premium), IP3-0.24 (claims), DF-1.0 (03b development factors), EX-1.2 / TM-1.3 (extract, treaty metrics), RX-1.2 (rate exposure) |
| Extract / treaty metrics | EX-1.2 / TM-1.3 |
| Source commit (mtamsyed-gc/ete-dashboard) | db686bc |

Generated by `side_tools/merit/tools/build_outputs_skill.py` from: `config/model_contract.json` (every table's grain,
key, columns and `describe` text), `oracle/extract.py` (extract columns and Dictionary), `oracle/treaty_metrics.py`
(treaty metrics and PNLR base columns), `oracle/pnlr.py` (PNLR defaults), `oracle/rate_exposure.py` (rate exposure
columns) and `layout.py` (folder and file names). The usage notes are hand-written in
`side_tools/merit/lenai/outputs_skill/` from the Merit admin guide, the LenAI encyclopedia, `powerbi/MEASURES.md`
and `docs/DEVELOPMENT_FACTORS.md`. Coverage check at generation: all 243 columns of the 13 main contract tables present; the 3 excluded twins by reference.

## Checking a run against this skill
1. `04_Outputs\csv\run_manifest_claims.csv`, key `contract_version`: must be IP4-13.
2. If it is newer, the client's `02_Inputs\Mapping\model_contract.json` is the authority for columns this skill does
   not list. Say so in the answer.

## Test questions (run in a new chat after each upload)
| # | Question | Expected answer contains |
|---|---|---|
| T1 | What does InExperience mean in fact_claims? | 1 if treated on or before the valuation date; 0 = in recon only |
| T2 | How do I join fact_claims to dim_life? | LifeKey + UWY (or LifeID within one run); never LifeKey alone |
| T3 | How is a claim counted? | Σ CountFlag: one line per visit (TPA, policy, member, provider, treatment date) with payer share > 0 |
| T4 | What is the grain of fact_member_month? | life-period x calendar month |
| T5 | Give me the ultimate loss ratio by UW year from the CSVs | aggregate fact_claims (InExperience = 1) and fact_member_month separately, then divide; states the premium basis |
| T6 | What is UNASSIGNED on the TreatyMetrics sheet? | payer + RI Name of a segment but no Reinsured % match, or a life in two segments |
| T7 | Which output version does this skill describe? | v9.2.0, contract IP4-13 |
| T8 | What is the column "Foo Bar" in fact_claims? | not in contract IP4-13; no invented meaning |
