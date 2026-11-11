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
