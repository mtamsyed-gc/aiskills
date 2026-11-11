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
