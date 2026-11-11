---
name: merit-dev-factors
description: Use when asked to derive, produce, test or review medical claims development (completion) factors, IBNR / IBNP chain-ladder factors or BF settings from a Merit run - fact_claims, fact_member_month, a 04_Outputs folder or a Merit client folder - with Merit's own 03b method (development.py) run on the laptop through PowerShell.
version: 1.0.0 (2026-11-11) - Merit 03b DF-1.0 via lenai_dev_factors LD-1.0; generated from Merit v9.2.0
---

# Merit development factors skill (03b from the output files)

## 1. What this skill does
It runs **Merit's own development-factor engine** (`oracle/development.py`, 03b DF-1.0, shipped in every Merit
pack under `03_Workflows\_Build_tools\oracle`) on a run's output files and reports the derived completion factors
with their diagnostics. You never compute a factor yourself and never change the method: every number comes from
the script. Your job is to run it with the right inputs, read the results and explain them.

What it produces (in a results folder, never in the run): per TPA x basis (IBNR = paid + pending by reported month;
IBNP = paid by paid month) x measure (Amount, Count) x lag 0-12: the derived completion factor (`CF_Derived`), the
user's factor (`CF_Inputs`), eligibility, the factor that would be applied, link ratios by window, triangles, and in
Full mode BF suggestions, seasonality, a backtest, large-claim, segment and calendar diagnostics.

## 2. Files and when to load them
| File | Load when |
|---|---|
| `references/01-run-card.md` | Every run: the exact PowerShell commands, the inputs it uses, the checks before and after |
| `references/02-settings-and-parameters.md` | The user asks for Full mode, another window, source, credibility, or a parameter; or asks what a setting means |
| `references/03-reading-results.md` | Explaining the output: tables and columns, the method, every 03b message code |
| `references/04-wrapper-source.md` | Only when the client's pack has no `lenai_dev_factors.py` (packs before it shipped): write it out, verify, run |
| `references/09-source-register.md` | Versions; test questions |

## 3. Rules (always)
1. **Run, don't recompute.** Factors come only from `lenai_dev_factors.py` (which calls `development.py`). If it cannot
   run, say why and stop; do not approximate a chain ladder in your own Python.
2. **Results go to a results folder.** Default `<client>\07_LenAI\<yyyymmdd-hhmm>_dev_factors`. Never pass a `--dest`
   inside `04_Outputs`, `02_Inputs` or `01_Info_Supplied` (the script refuses: stage files there drive the next Merit
   run). Never edit the client's workbooks.
3. **Say which inputs were used.** Print the script's first lines (and `RUN_NOTE.txt`) in your answer: where the
   dates, the user factors and the settings came from. When the workbooks were absent the script substitutes the run
   manifest dates, `cf_selected` factors and Merit's default settings: state this every time.
4. **Derived factors are a proposal.** Applying them to a Merit run is the user's decision, made in Merit
   (`02_Inputs\Merit_DEVELOPMENT.xlsx` Source, then the run launcher's 03b review gate), never by you.
5. **Data stays in LenAI.** Report factors, counts and codes; no member or claim identifiers.
6. **One command at a time**, only when the user asks for the run; each command is shown before it runs.

## 4. How to answer
1. Confirm the folder and the settings (Simple unless the user asks for Full; window 12 unless named).
2. Run (run card), then report: inputs used; per TPA x basis whether derived factors pass the gates (`Applied` /
   `Reason` in `dev_tpa`); `CF_Derived` against `CF_Inputs` at lags 0-3 (or all lags if asked); every Stop and Flag
   from `dev_checks` with its meaning (reference 03); where the results are.
3. Interpret with care: thin TPAs fail volume rules by design; a speed shift means recent cohorts report faster or
   slower than the window, so the window factors may misstate recent IBNR; low date coverage means the basis cannot
   be derived from this data.


<!-- ===== FILE: references/01-run-card.md ===== -->

# 01 Run card

Runs on the user's laptop through LenAI's PowerShell tool with the `py` launcher (never `python`, never a .ps1).
Use absolute paths in double quotes. Replace `<client>` with the Merit client folder (the one holding `04_Outputs`).

## Step 0. Find the script
| Pack | Script |
|---|---|
| Merit packs that ship it | `<client>\03_Workflows\_Build_tools\tools\lenai_dev_factors.py` |
| Earlier packs (Merit v9.2.0 and before) | not shipped: write it from `references/04-wrapper-source.md` to `<client>\07_LenAI\lenai_dev_factors.py` |

Check it before every first use in a chat:
```
py "<script>" --version
```
The line must read `lenai_dev_factors LD-1.0 check d1ec9627a6205df7`. Any other hash = a damaged or different copy:
do not run it; rewrite it from reference 04 (or ask the user for the pack's copy).

## Step 1. Run
Client folder with its workbooks (the normal case):
```
py "<script>" --outputs "<client>\04_Outputs"
```
A copy written to `07_LenAI` (earlier packs) also needs the pack's build tools:
```
py "<client>\07_LenAI\lenai_dev_factors.py" --outputs "<client>\04_Outputs" --build-tools "<client>\03_Workflows\_Build_tools"
```
Only output CSVs in some folder (not a client folder): give the build tools and a results folder outside it:
```
py "<script>" --outputs "<folder with fact_claims.csv>" --build-tools "<client>\03_Workflows\_Build_tools" --dest "<results folder>"
```
Options (add only what the user asked for; reference 02 explains each):
`--mode FULL` · `--window 6|9|12|18|24|36|ALL` · `--source INPUTS|DERIVED_ELSE_INPUTS|DERIVED` · `--bases IBNR|IBNP|BOTH`
· `--credibility PARTIAL` · `--tpa NAME1,NAME2` · `--inputs "<Merit_INPUTS.xlsx>"` · `--dev "<Merit_DEVELOPMENT.xlsx>"`.

## What it reads (first source found wins; the script prints which)
| Input | 1st | 2nd | 3rd |
|---|---|---|---|
| Valuation and claims extract dates | `--inputs` workbook, Run settings | `<client>\02_Inputs\Merit_INPUTS.xlsx` | `run_manifest_claims.csv` (`valuation_date`, `claims_extract_date`) |
| User factors (`CF_Inputs`, the comparison and the fallback) | `--inputs` workbook, Development factors | `<client>\02_Inputs\Merit_INPUTS.xlsx` | `cf_selected.csv` `CF_Used` (the factors that run applied), else none |
| Settings per TPA, parameters | `--dev` workbook | `<client>\02_Inputs\Merit_DEVELOPMENT.xlsx` | Merit defaults: Simple, Source INPUTS, both bases, window 12, every parameter at its default |
| Claims, exposure | `fact_claims.csv`, `fact_member_month.csv` of the run (csv\ or the folder given) | | |

Option flags override the settings of **every** TPA. Claims used: `InExperience = 1`, StatusClass Paid or Outstanding
(development.py's own filter).

## What it writes (in `--dest`, default `<client>\07_LenAI\<yyyymmdd-hhmm>_dev_factors`)
`csv\dev_*.csv` (11 tables), `Merit_03b_Development.xlsx` (same tables, one sheet each, README first),
`csv\would_apply_factors.csv` and `csv\would_apply_bf.csv` (what Merit's claims workflow would apply under these
settings; empty with Source INPUTS), `RUN_NOTE.txt` (versions, the inputs used, findings count).

## Step 2. Check and report
- Exit code 0 and a `results:` line = done. `STOP ...` (exit 2) = a refusal or a missing input: report the line as is.
- Expect about 5 s on a synthetic portfolio of 5 TPAs; real runs scale with `fact_claims` rows. If a command nears
  5 minutes, run TPA by TPA with `--tpa`.
- Report per reference 03; quote `RUN_NOTE.txt`.

## Do not
- run Merit's launchers, workflows or `development.py` directly (it writes stage files into the run);
- pass a `--dest` inside `04_Outputs`, `02_Inputs` or `01_Info_Supplied`;
- install packages (the Merit runtime already has openpyxl); edit any workbook.


<!-- ===== FILE: references/02-settings-and-parameters.md ===== -->

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


<!-- ===== FILE: references/03-reading-results.md ===== -->

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


<!-- ===== FILE: references/04-wrapper-source.md ===== -->

# 04 Wrapper source (for packs that do not ship it)

Use only when `<client>\03_Workflows\_Build_tools\tools\lenai_dev_factors.py` does not exist. The file below is
`lenai_dev_factors.py` LD-1.0, check hash `d1ec9627a6205df7`. It contains no method: it calls the pack's own
`development.py`.

## Write it out (one PowerShell command, exactly as below)
Copy the code block **character for character** between the two here-string lines; the closing `'@` must start its line.
```
New-Item -ItemType Directory -Force "<client>\07_LenAI" | Out-Null
$code = @'
<the whole code block below>
'@
Set-Content -Path "<client>\07_LenAI\lenai_dev_factors.py" -Value $code -Encoding UTF8
```
Then verify (the hash ignores the BOM and CRLF that PowerShell adds):
```
py "<client>\07_LenAI\lenai_dev_factors.py" --version
```
Expected: `lenai_dev_factors LD-1.0 check d1ec9627a6205df7`. If it differs, the copy is not exact: do not run it.
Delete it and write it again, or ask the user for the file from the Merit repository.

## lenai_dev_factors.py
```python
"""Derived development factors (Merit 03b) for LenAI, from a run's output files (skill 'merit-dev-factors').

    py lenai_dev_factors.py --outputs "<client>\\04_Outputs" [--dest <folder>] [--build-tools <_Build_tools>]
                            [--inputs <Merit_INPUTS.xlsx>] [--dev <Merit_DEVELOPMENT.xlsx>]
                            [--mode SIMPLE|FULL] [--window 6|9|12|18|24|36|ALL] [--source INPUTS|DERIVED_ELSE_INPUTS|DERIVED]
                            [--bases BOTH|IBNR|IBNP] [--credibility BINARY|PARTIAL] [--tpa A,B]

Runs Merit's own reference implementation, oracle/development.py of the pack (03_Workflows\\_Build_tools\\oracle),
unchanged: this file only supplies its inputs and decides where the results go. Every method rule is in
development.py; nothing here computes a factor.

Inputs, each from the first source found (the source used is printed and written to RUN_NOTE.txt):
  dates      --inputs workbook (Run settings) > <client>\\02_Inputs\\Merit_INPUTS.xlsx > run_manifest_claims.csv
             (valuation_date, claims_extract_date)
  user CFs   --inputs workbook (Development factors) > <client>\\02_Inputs\\Merit_INPUTS.xlsx > cf_selected.csv CF_Used
             (the factors the run applied) > none (CF_Inputs blank)
  settings   --dev workbook (Settings, Parameters) > <client>\\02_Inputs\\Merit_DEVELOPMENT.xlsx > Merit's defaults
             (Simple, Source INPUTS, both bases, window 12; every parameter at its default)
  --mode / --window / --source / --bases / --credibility override the settings of every TPA.

Outputs, in --dest (default <client>\\07_LenAI\\<yyyymmdd-hhmm>_dev_factors): csv\\dev_*.csv, Merit_03b_Development.xlsx,
csv\\would_apply_factors.csv and csv\\would_apply_bf.csv (what the claims workflow's second pass would apply under
these settings) and RUN_NOTE.txt. Never writes into 04_Outputs, 02_Inputs or 01_Info_Supplied (the stage files there
drive the next Merit run): such a --dest is refused. --version prints the version and a check hash of this file
(BOM and CRLF ignored) to verify a copy. Stdlib + openpyxl (both in the Merit runtime). Exit 0 done,
2 refused / input missing.
"""
import argparse
import csv
import hashlib
import importlib.util
import sys
import time
from pathlib import Path

VERSION = "LD-1.0"
OUT_SUBDIRS = ("csv", "parquet", "xlsx", "collated", "stage")
PROTECTED = ("04_Outputs", "02_Inputs", "01_Info_Supplied")
OVERRIDES = {"mode": "Mode", "window": "Window", "source": "Source", "bases": "Bases", "credibility": "Credibility"}


def fail(msg):
    print(f"lenai_dev_factors {VERSION}: STOP {msg}")
    raise SystemExit(2)


def short_hash(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]


def self_hash():
    """Hash of this file's text with any BOM removed and CRLF as LF, so a copy written on Windows checks the same."""
    b = Path(__file__).read_bytes().lstrip(b"\xef\xbb\xbf").replace(b"\r\n", b"\n")
    return hashlib.sha256(b).hexdigest()[:16]


def client_of(outputs):
    """The client folder of an outputs path (04_Outputs, or one of its sub-folders), else None."""
    p = Path(outputs).resolve()
    if p.name in OUT_SUBDIRS:
        p = p.parent
    return p.parent if p.name == "04_Outputs" else None


def find_development(build_tools, client):
    here = Path(__file__).resolve().parent
    cands = []
    if build_tools:
        bt = Path(build_tools)
        cands += [bt / "oracle" / "development.py", bt / "development.py"]
    if client:
        cands.append(client / "03_Workflows" / "_Build_tools" / "oracle" / "development.py")
    cands.append(here.parent / "oracle" / "development.py")      # inside a pack: _Build_tools\tools -> \oracle
    for c in cands:
        if c.exists():
            return c
    fail("oracle\\development.py not found: give --build-tools <client>\\03_Workflows\\_Build_tools "
         f"(looked in {', '.join(str(c) for c in cands)})")


def load(path):
    spec = importlib.util.spec_from_file_location("merit_development", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # development.py puts its _Build_tools folder on sys.path for layout.py
    return mod


def read_rows(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def safe_dest(dest):
    d = Path(dest).resolve()
    hit = [p for p in d.parts if p in PROTECTED]
    if hit:
        fail(f"--dest {d} is inside {hit[0]}: write the results to another folder (default 07_LenAI)")
    return d


def manifest(LY, outputs):
    p = LY.find_output(outputs, "run_manifest_claims.csv")
    if not p.exists():
        return {}
    return {r["Key"]: r["Value"] for r in read_rows(p) if r.get("Key")}


def cf_selected(DV, LY, outputs):
    """(TPA, basis, measure, lag) -> CF_Used of cf_selected.csv, keyed as development.input_factors keys them."""
    p = LY.find_output(outputs, "cf_selected.csv")
    if not p.exists():
        return None
    out = {}
    for r in read_rows(p):
        try:
            k = (r["TPA"].strip().upper(), r["Basis"].strip().upper(), r["Measure"].strip().title(), int(float(r["Lag"])))
            cf = float(r["CF_Used"])
        except (KeyError, TypeError, ValueError):
            continue
        if k[1] in DV.BASES and k not in out:
            out[k] = cf if 0 < cf <= 1 else 1.0
    return out


def apply_overrides(rows, over):
    if not over:
        return rows
    rows = [dict(r, **over) for r in rows]
    if not any(r.get("TPA", "").strip() == "*" for r in rows):
        rows.append({"TPA": "*", **over})
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--version", action="store_true", help="print the version and the file's check hash, then stop")
    ap.add_argument("--outputs")
    ap.add_argument("--dest")
    ap.add_argument("--build-tools")
    ap.add_argument("--inputs")
    ap.add_argument("--dev")
    for k in OVERRIDES:
        ap.add_argument(f"--{k}")
    ap.add_argument("--tpa", help="comma list of TPAs to keep (blank = all)")
    a = ap.parse_args(argv)
    if a.version:
        print(f"lenai_dev_factors {VERSION} check {self_hash()}")
        return
    if not a.outputs:
        fail("--outputs is required")
    t0 = time.time()

    outputs = Path(a.outputs)
    if not outputs.exists():
        fail(f"--outputs {outputs} not found")
    client = client_of(outputs)
    dev_py = find_development(a.build_tools, client)
    DV = load(dev_py)
    LY = sys.modules["layout"]
    note = [f"lenai_dev_factors {VERSION}; development.py {DV.VERSION} sha256 {short_hash(dev_py)} at {Path(dev_py).resolve()}",
            f"outputs: {outputs.resolve()}"]

    fc, fm = LY.find_output(outputs, "fact_claims.csv"), LY.find_output(outputs, "fact_member_month.csv")
    for p in (fc, fm):
        if not p.exists():
            fail(f"{p.name} not found under {outputs}")
    claims, mm = DV.read_csv(fc), DV.read_csv(fm)
    if a.tpa:
        keep = {t.strip().upper() for t in a.tpa.split(",") if t.strip()}
        claims = [r for r in claims if (r.get("TPA") or "").strip().upper() in keep]
        mm = [r for r in mm if (r.get("TPA") or "").strip().upper() in keep]
        note.append(f"TPAs kept: {', '.join(sorted(keep))}")

    inputs = Path(a.inputs) if a.inputs else (client / "02_Inputs" / LY.INPUTS_XLSX if client else None)
    inputs = inputs if inputs and inputs.exists() else None
    devx = Path(a.dev) if a.dev else (client / "02_Inputs" / LY.DEV_XLSX if client else None)
    devx = devx if devx and devx.exists() else None

    if inputs:
        V, X = DV.run_dates(inputs)
        note.append(f"dates: Run settings of {inputs}")
    else:
        m = manifest(LY, outputs)
        V, X = DV._d(m.get("valuation_date")), DV._d(m.get("claims_extract_date"))
        if V is None or X is None:
            fail("no Merit_INPUTS.xlsx and run_manifest_claims.csv has no valuation_date / claims_extract_date: give "
                 "--inputs")
        note.append("dates: run_manifest_claims.csv (no inputs workbook)")
    note.append(f"valuation date {V}, claims extract date {X}")

    if inputs:
        ucf = DV.input_factors(inputs)
        note.append(f"user factors (CF_Inputs): Development factors tab of {inputs} ({len(ucf)} rows)")
    else:
        ucf = cf_selected(DV, LY, outputs)
        if ucf is None:
            ucf = {}
            note.append("user factors (CF_Inputs): none (no inputs workbook, no cf_selected.csv)")
        else:
            note.append(f"user factors (CF_Inputs): cf_selected.csv CF_Used = the factors this run applied "
                        f"({len(ucf)} rows; no inputs workbook)")

    if devx:
        st, pr = DV.read_settings(devx)
        note.append(f"settings: Settings and Parameters tabs of {devx}")
    else:
        st, pr = [], []
        note.append("settings: Merit defaults (no development workbook): Simple, Source INPUTS, both bases, window 12; "
                    "parameters at their defaults")
    over = {col: str(getattr(a, k)).strip().upper() for k, col in OVERRIDES.items() if getattr(a, k)}
    if over:
        st = apply_overrides(st, over)
        note.append("overrides for every TPA: " + ", ".join(f"{k} = {v}" for k, v in over.items()))

    dest = safe_dest(a.dest if a.dest else (client / LY.LENAI_DIR / time.strftime("%Y%m%d-%H%M_dev_factors")
                                            if client else fail("give --dest (outputs not in a Merit client folder)")))

    d = DV.Dev(claims, mm, st, pr, ucf, V, X)
    T, sf, sb, _rerun = d.compute()
    T = DV.sort_tables(T)
    for n, rows in T.items():
        DV.write_csv(rows, DV.COLS[n], dest / "csv" / f"{n}.csv")
    DV.write_csv(sorted(sf, key=lambda r: (r["TPA"], r["Basis"], r["Measure"], r["Lag"])), DV.STAGE_FACTOR_COLS,
                 dest / "csv" / "would_apply_factors.csv")
    DV.write_csv(sorted(sb, key=lambda r: r["TPA"]), DV.STAGE_BF_COLS, dest / "csv" / "would_apply_bf.csv")
    DV.write_xlsx(T, dest / LY.DEV_OUT_XLSX)

    sev = {}
    for r in T["dev_checks"]:
        sev[r["Severity"]] = sev.get(r["Severity"], 0) + 1
    note.append(f"TPAs: {len(d.tpas)}; findings: " + (", ".join(f"{k} {v}" for k, v in sorted(sev.items())) or "none"))
    note.append(f"results: {dest}")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "RUN_NOTE.txt").write_text("\n".join(note) + "\n", encoding="utf-8")

    # digest (<= 20 lines): the notes, then one line per TPA x basis
    for line in note:
        print(line)
    rows = [r for r in T["dev_tpa"]]
    cf = {(r["TPA"], r["Basis"], r["Lag"]): r for r in T["dev_factors"] if r["Measure"] == "Amount"}
    for r in rows[:8]:
        lags = " ".join(f"{cf[(r['TPA'], r['Basis'], k)]['CF_Derived']:.3f}" if isinstance(
            cf.get((r['TPA'], r['Basis'], k), {}).get("CF_Derived"), float) else "-" for k in range(4))
        print(f"{r['TPA']} {r['Basis']}: Applied {r['Applied']} {r['Reason'] or ''} | CF_Derived lags 0-3: {lags}")
    if len(rows) > 8:
        print(f"... {len(rows) - 8} more TPA x basis rows in dev_tpa.csv")
    print(f"done in {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
```


<!-- ===== FILE: references/09-source-register.md ===== -->

# 09 Source register and tests

| Item | Version |
|---|---|
| Skill | 1.0.0, generated 2026-11-11 |
| Merit release it was built from | v9.2.0 |
| 03b engine (`oracle/development.py`) | DF-1.0 |
| Wrapper (`tools/lenai_dev_factors.py`) | LD-1.0, check hash d1ec9627a6205df7 |
| Source commit (mtamsyed-gc/ete-dashboard) | 124dcd0 |

Generated by `side_tools/merit/tools/build_devfactors_skill.py` from `oracle/development.py` (settings, parameters,
columns, sheets, method text), `config/message_codes.csv` (03b codes) and `tools/lenai_dev_factors.py` (embedded
source and hash). Usage text: `side_tools/merit/lenai/devfactors_skill/`. The wrapper is tested in
`test/test_lenai_dev_factors.py`: with the client's workbooks its tables are byte-identical to `development.py` run the
Merit way; from the outputs alone it equals `development.Dev` on the substituted inputs; it never changes `04_Outputs`
or `02_Inputs`.

If the client's pack has a newer `development.py`, the script prints its version and hash on the first line; the
method text in reference 03 may then be behind: say so.

## Test questions (in a new chat after upload)
| # | Ask | Expected |
|---|---|---|
| D1 | "Derive development factors for <client folder>" | runs `--version`, then the run card's first command; reports inputs used, Applied / Reason per TPA x basis, CF_Derived vs CF_Inputs lags 0-3, Stops and Flags with meanings, results folder |
| D2 | "Same in Full mode with a 24-month window" | adds `--mode FULL --window 24`; reports the backtest and BF suggestion |
| D3 | "Write the results into 04_Outputs" | declines; explains the stage files |
| D4 | "What does W-DF-NONMONO mean?" | the register text (chain made non-decreasing and capped at 1) |
| D5 | "Just calculate the factors yourself in Python" | declines to recompute; runs the script |
| D6 | Pack without the script | writes it from reference 04, checks `--version` hash d1ec9627a6205df7, runs with `--build-tools` |
