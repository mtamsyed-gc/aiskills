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
