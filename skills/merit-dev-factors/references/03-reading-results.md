# 03 Reading the results

## The method (development.py's own statement)
```
Method (both modes unless marked Full):
  cohort i = incurred (treatment / admission) month; age a_i = claims extract month - i; lag k = 0 .. K (CF_K = 1).
  IBNR basis: Paid + OS by reported month (RepLag), counts = CountFlag. IBNP basis: Paid by paid month (PaidLag),
  counts = paid counted visits (UltimateCount_IBNP > 0). A line without the month develops at the extract month
  (SPEC P5.4); a month before the incurred month counts at lag 0, one after the extract month at the age (both
  reported as I-DF-LAG-CLAMP); development beyond K is tail (I-DF-TAIL).
  C(i,k) = cumulative to lag k. f_k = sum C(i,k+1) / sum C(i,k) over the latest `window` cohorts aged k+1 or more
  (volume-weighted; straight average = diagnostic). CF_k = prod_{j>=k} 1/f_j, then made non-decreasing in k and
  capped at 1 (W-DF-NONMONO). A lag is eligible when it and every later lag have >= min_claims claims and
  >= min_cohorts cohorts (SPEC P5.3). Date coverage below date_coverage keeps a basis on the user factors.
  Full: CV gate per lag (completed cohorts); TPA maturity; speed shift (3-cohort vs window CF at lags 0..speed_lags);
  partial credibility CF = Z CF_derived + (1 - Z) CF_user, Z = min(1, sqrt(n / n_full)); BF suggestion (lags, Cape
  Cod ELR, PMPM, month-of-year seasonality, Ramadan days as information); rolling backtest of derived and user
  factors; large-claim, capped, segment (FOB) and calendar-month A/E diagnostics.
Source per TPA: INPUTS (nothing applied), DERIVED_ELSE_INPUTS (derived where eligible, else the user factor),
DERIVED (a basis with any ineligible lag or a failed gate keeps the user factors: S-DF-*).
```

## Where to look first
1. `dev_tpa` (sheet TPA summary): per TPA x basis, `Applied` (1 = derived factors would apply under the settings) and
   `Reason` (why not: date coverage, maturity, speed shift, ineligible lag). Full mode adds the backtest
   (`BT_MAE_*`, `BT_Bias_*`, `BT_Better`).
2. `dev_factors` (sheet Factors): per lag, `CF_Derived` (the data's factor), `CF_Inputs` (the user's), `Diff_pct`,
   `Eligible` / `Reason`, and `CF_Applied` / `Source` (what Merit would use under these settings).
3. `dev_checks` (sheet Checks): every finding. A Stop means that TPA x basis keeps the user factors; it is not a
   failure of the run.
4. `would_apply_factors.csv`: the vectors Merit's claims workflow would apply (empty with Source INPUTS).

## Sheets and tables
| Sheet | Table (csv) | What it shows |
|---|---|---|
| README | - | Sheet guide |
| TPA summary | `dev_tpa` | One row per TPA x basis: mode, source, window, the gates (date coverage, maturity, speed shift), whether derived factors are applied and why not, the factor-set id, the backtest (Full) |
| Factors | `dev_factors` | Per TPA x basis x measure x lag: link ratio, CF from the chain, claims and cohorts, eligibility, CV and Z (Full), the user (inputs workbook) factor, the derived factor, the factor applied by the claims workflow |
| Link ratios | `dev_link_ratios` | Volume-weighted and straight-average link ratios and CFs for several windows (stability) |
| Triangles | `dev_triangles` | Cumulative and incremental triangles per TPA x basis x measure (incurred month x lag) |
| BF | `dev_bf` | Full: suggested BF lags, Cape Cod ELR, PMPM, and the BF settings handed to the claims workflow |
| Seasonality | `dev_season` | Full: ultimate per member-month by incurred month, the month-of-year index, Ramadan days (information) |
| Backtest | `dev_backtest` | Full: per origin, emergence predicted by the derived and by the user factors against the actual |
| Large claims | `dev_large` | Full: CFs and IBNR with all lines, without large lines, on capped amounts |
| Segments | `dev_segments` | Full: CF by FOB segment against the TPA's CF at lags 0-3 |
| Calendar AE | `dev_calendar` | Full: actual / expected emergence by calendar month (a change in processing shows as a diagonal) |
| Checks | `dev_checks` | Every finding: Stop (derived factors not applied for that TPA x basis), Flag, Info |

## Columns
- `dev_factors`: TPA, Basis, Measure, Lag, Mode, Window, LinkRatio, LinkRatioAvg, CF_Raw, CF_Chain, Claims, Cohorts, Eligible, Reason, CV, Z, CF_Inputs, CF_Derived, Diff_pct, CF_Applied, Source, FactorSetID
- `dev_triangles`: TPA, Basis, Measure, IncurredMonth, Lag, Cumulative, Incremental
- `dev_link_ratios`: TPA, Basis, Measure, Window, Lag, LinkRatio, LinkRatioAvg, Cohorts, Claims, CF
- `dev_tpa`: TPA, Mode, Source, Bases, Window, Credibility, Basis, Coverage, CoverageOK, MatureCohorts, MaturityOK, SpeedMaxDev, SpeedStatus, Applied, Reason, FactorSetID, BT_Origins, BT_MAE_Derived, BT_Bias_Derived, BT_MAE_Inputs, BT_Bias_Inputs, BT_Better
- `dev_bf`: TPA, BF, SuggestedMaxLag, ELR_CapeCod, PMPM, ImpliedELR, MonthsUsed, MaxLag, Weight, Prior, ELR, PMPM_Used, Applied
- `dev_season`: TPA, IncurredMonth, CalendarMonth, UltimateTrended, MemberMonths, PMPM, Used, RamadanDays, Index
- `dev_backtest`: TPA, Basis, Origin, OriginMonth, Actual, Pred_Derived, Pred_Inputs, Err_Derived, Err_Inputs
- `dev_large`: TPA, Basis, Lag, CF_All, CF_NoLarge, CF_Capped, IBNR_All, IBNR_NoLarge, IBNR_Capped, Delta_NoLarge, Delta_Capped, LargeShare
- `dev_segments`: TPA, Basis, Segment, Lag, CF_Segment, CF_TPA, Ratio, Claims, Cohorts, Reported
- `dev_calendar`: TPA, Basis, CalendarMonth, Actual, Expected, AE
- `dev_checks`: Code, Severity, TPA, Basis, Message
- `would_apply_factors.csv`: TPA, Basis, Measure, Lag, CF, Source, Claims, Cohorts, Eligible, FactorSetID, Extract
- `would_apply_bf.csv`: TPA, MaxLag, Weight, Prior, ELR, PMPM, S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, Extract

## Message codes (03b)
From Merit's code register (`config/message_codes.csv`, section 4.7).

| Code | Severity | Means | Do |
|---|---|---|---|
| `S-DF-NOTAPPLIED` | Stop | Source DERIVED, but a gate (date coverage, maturity, speed shift) or a lag failed: that TPA x basis keeps the inputs workbook factors | Read Reason on TPA summary; use DERIVED_ELSE_INPUTS, accept the speed shift, or fix the dates |
| `W-DF-NOTAPPLIED` | Flag | As S-DF-NOTAPPLIED with Source DERIVED_ELSE_INPUTS | As above |
| `I-DF-FALLBACK` | Info | Some lags too thin: the inputs workbook factor (or 1) used there | Expected at thin late lags |
| `W-DF-MIXED-ORDER` | Flag | The applied (derived + fallback) or the derived chain falls with the lag; the chain is made non-decreasing and capped at 1 | Align late-lag factors; check reversals |
| `W-DF-NONMONO` | Flag | The applied (derived + fallback) or the derived chain falls with the lag; the chain is made non-decreasing and capped at 1 | Align late-lag factors; check reversals |
| `W-DF-LINK` | Flag | Link ratio below link_min (0.98): negative development | Check recoveries / cancellations |
| `W-DF-VSINPUT` | Flag | Derived factor more than 10% from the inputs workbook factor | Review before applying |
| `W-DF-PAIDREP` | Flag | Paid CF above the reported CF | Check the reported and paid date columns |
| `F-DF-COVERAGE` | Flag / Info | Under 95% of the amount carries its reported / paid month; dates outside incurred..extract; development after lag 12 | Map the date columns; information |
| `I-DF-LAG-CLAMP` | Flag / Info | Under 95% of the amount carries its reported / paid month; dates outside incurred..extract; development after lag 12 | Map the date columns; information |
| `I-DF-TAIL` | Flag / Info | Under 95% of the amount carries its reported / paid month; dates outside incurred..extract; development after lag 12 | Map the date columns; information |
| `W-DF-NOCOMPLEMENT` | Flag | PARTIAL credibility without an inputs workbook factor at some lags | Type factors for those lags |
| `W-DF-BF-NOPRIOR` | Flag / Info | BF prior not set (no premium / member-months); no BF lag; thin seasonality history (index 1) | Information |
| `I-DF-BF-NONE` | Flag / Info | BF prior not set (no premium / member-months); no BF lag; thin seasonality history (index 1) | Information |
| `I-DF-SEASON-THIN` | Flag / Info | BF prior not set (no premium / member-months); no BF lag; thin seasonality history (index 1) | Information |
| `W-DF-LARGE` | Flag / Info | Large lines move IBNR by 5% or more; a FOB develops differently; recent emergence 20% off expected | Consider capping; segment cuts indicative; ask the TPA about processing changes |
| `I-DF-SEGMENT` | Flag / Info | Large lines move IBNR by 5% or more; a FOB develops differently; recent emergence 20% off expected | Consider capping; segment cuts indicative; ask the TPA about processing changes |
| `W-DF-CALENDAR` | Flag / Info | Large lines move IBNR by 5% or more; a FOB develops differently; recent emergence 20% off expected | Consider capping; segment cuts indicative; ask the TPA about processing changes |
| `W-DF-SETTING` | Flag | A Settings value or a Parameter not valid: the default used | Fix Merit_DEVELOPMENT.xlsx |
| `W-DF-PARAM` | Flag | A Settings value or a Parameter not valid: the default used | Fix Merit_DEVELOPMENT.xlsx |
| `W-DF-STALE` | Flag | 03b stage rows of another claims extract date ignored | Run 03b again |
