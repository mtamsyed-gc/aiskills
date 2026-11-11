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
