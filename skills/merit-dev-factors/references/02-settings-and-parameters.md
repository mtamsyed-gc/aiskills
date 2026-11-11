# 02 Settings and parameters (03b DF-1.0)

Generated from `development.py` (`SETTING_RULES`, `PARAMS`). In a client folder they live in
`02_Inputs\Merit_DEVELOPMENT.xlsx` (tab Settings: one row per TPA, `*` = every other TPA; tab Parameters). The run
card's flags override the Settings columns for every TPA; parameters are changed only in the workbook.

## Settings (per TPA)
A blank or invalid value takes the default (W-DF-SETTING). In Simple mode the Full-only columns take their defaults.

| Column | Values [default] | Mode |
|---|---|---|
| `TPA` | TPA name, or * for every TPA | Both |
| `Mode` | SIMPLE \| FULL  [SIMPLE] | Both |
| `Source` | INPUTS \| DERIVED_ELSE_INPUTS \| DERIVED  [INPUTS] | Both |
| `Bases` | BOTH \| IBNR \| IBNP  [BOTH] | Both |
| `Window` | 6 \| 9 \| 12 \| 18 \| 24 \| 36 \| ALL cohorts  [12] | Both |
| `Credibility` | Full: BINARY \| PARTIAL  [BINARY] | Full only |
| `Speed shift accepted` | Full: blank \| WINDOW \| SHORT | Full only |
| `BF` | Full: OFF \| SUGGESTED \| MANUAL  [OFF] | Full only |
| `BF max lag` | Full, MANUAL: -1 (none) .. 12; blank = suggested | Full only |
| `BF weight` | Full: BF \| BENKTANDER  [BF] | Full only |
| `BF prior` | Full: ELR \| PMPM  [ELR] | Full only |
| `BF ELR` | Full, MANUAL: e.g. 0.85; blank = Cape Cod | Full only |
| `BF PMPM` | Full, MANUAL: amount per member-month; blank = suggested | Full only |
| `Seasonality` | Full: OFF \| MONTH  [OFF] | Full only |
| `Note` | free text | Both |

What the main ones mean (development.py's own help text, then the method notes):
- **Settings tab**: One row per TPA (the TPA name as in the claims data) and a row '*' whose values every TPA without its own row - or with a blank cell - takes. Blank everywhere = the default in brackets in the header note. Mode SIMPLE = plain chain ladder (Source, Bases, Window only); FULL = every column.
- **Source**: INPUTS (default): nothing changes, 03b only reports. DERIVED_ELSE_INPUTS: the derived factor where its lag is eligible, else the inputs workbook's. DERIVED: all derived; if any lag is not eligible or a gate fails, the basis keeps the inputs workbook's factors and 03b reports a Stop.
- **Window**: the latest cohorts (incurred months) the volume-weighted link ratios use.
- **Credibility** (Full): BINARY = derived or user factor per lag; PARTIAL = Z x derived + (1 - Z) x user,
  Z = min(1, sqrt(n / n_full)).
- **Speed shift accepted** (Full): a speed shift (CF of the latest `speed_window` cohorts vs the window's, lags
  0..`speed_lags`, above `speed_tol`) blocks the derived factors unless accepted: WINDOW = use the window anyway;
  SHORT = use the short-window link ratios at lags 0..`speed_lags`.
- **BF** (Full): SUGGESTED = the suggested BF lags and prior; MANUAL = the BF max lag, ELR and PMPM columns as given
  (blank = suggested / Cape Cod).

## Parameters
Values: the Parameters tab, else the default. `Basis` = the source of the default.

| Parameter | Default | Mode | Meaning | Basis |
|---|---|---|---|---|
| `K` | 12 | Both | Last lag of the factor vectors; CF at K = 1 (development after K is tail) | SPEC D10 |
| `min_claims` | 30 | Both | Claims (counted visits) a lag cell needs, over the window's cohorts | SPEC P5.3 |
| `min_cohorts` | 6 | Both | Incurred months (cohorts) a lag cell needs | SPEC P5.3 |
| `date_coverage` | 0.95 | Both | Share of a basis' amount that must carry its own reported / paid month | Judgement (owner 2026-10-28) |
| `link_min` | 0.98 | Both | Link ratio below which DV02 flags (reversal allowance) | SPEC DV02 |
| `paid_rep_tol` | 0.005 | Both | Paid CF above the reported CF by more than this flags DV06 | SPEC DV06 |
| `vs_inputs_tol` | 0.1 | Both | Derived vs user factor difference that DV08 flags | SPEC DV08 |
| `tail_info` | 0.01 | Both | Share of amount developing after lag K that is reported | Judgement |
| `cv_max` | 0.1 | Full | Coefficient of variation of a lag's completion ratios at or above which the lag is a BF lag (and flagged) | SOA 2007 statistical guide |
| `cv_amber` | 0.05 | Full | CV amber band (information) | SOA 2007 statistical guide |
| `cv_cohorts` | 12 | Full | Latest completed cohorts the CV uses (3 or more needed) | Judgement |
| `min_tpa_cohorts` | 12 | Full | Cohorts a TPA needs with at least min_tpa_age lags observed | Judgement |
| `min_tpa_age` | 6 | Full | Lags observed for a cohort to count towards maturity | Judgement |
| `speed_window` | 3 | Full | Cohorts of the short window the speed test (and SHORT) uses | SOA 2009 disruption tests |
| `speed_lags` | 2 | Full | Speed test on lags 0 .. speed_lags | Judgement |
| `speed_tol` | 0.05 | Full | Relative difference short vs window CF that flags a speed shift | Judgement |
| `n_full` | 1082 | Full | Claims for full credibility (PARTIAL: Z = min(1, sqrt(n / n_full))) | Limited-fluctuation standard 90% / 5% |
| `cf_credible` | 0.5 | Full | CF below which an incurred month is a BF month | SOA 2009 IBNR comparison |
| `bf_lag_cap` | 3 | Full | Highest lag the BF suggestion may cover | Judgement |
| `prior_min_cf` | 0.75 | Full | CF a month needs to feed the Cape Cod ELR / PMPM / seasonality | SOA 2009 (HLR) |
| `prior_window` | 12 | Full | Latest such months the ELR and PMPM use | SOA 2009 (HLR) |
| `prior_trend` | 0.0 | Full | Annual trend applied to each month's ultimate in the PMPM and seasonality | SPEC P5b (premium not trended) |
| `season_min_years` | 2 | Full | Months of one calendar month a seasonality index needs (else 1) | Judgement |
| `large_materiality` | 0.05 | Full | IBNR change without large lines that flags W-DF-LARGE | SOA 2007 (5%) |
| `seg_min_claims` | 30 | Full | Claims a segment (FOB) needs to be compared | SPEC P5.3 |
| `seg_max` | 8 | Full | Segments compared per TPA (largest by amount) | Judgement |
| `seg_tol` | 0.1 | Full | Segment vs TPA CF difference (lags 0-3) that is reported | Judgement |
| `diag_months` | 12 | Full | Calendar months of the A/E table | Judgement |
| `diag_recent` | 3 | Full | Latest calendar months the A/E flag looks at | Judgement |
| `diag_tol` | 0.2 | Full | A/E distance from 1 that flags W-DF-CALENDAR | Judgement |
| `bt_origins` | 12 | Full | Backtest origins (1 .. n months before the extract) | ASOP 5 follow-up; CBUAE hindsight |
