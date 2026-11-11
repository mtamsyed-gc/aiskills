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
