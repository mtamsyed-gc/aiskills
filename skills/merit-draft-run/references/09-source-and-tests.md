# Source register and tests: merit-draft-run

## Source
| Item | Value |
| --- | --- |
| Skill version | 0.1.0 (15 Nov 2026), prompt and script version UD-0.1 |
| Purpose | An unattended DRAFT run of Merit for a first look at a client's numbers. It works in a copy of the client folder; the result is unreviewed and not for quotation |
| Written against | Merit v10.5.0 (ete-dashboard main 9830ee9): `tools/intake.py` IN-3.10 (commands, stop codes, the editable columns of the Mapping workbook), `lenai/mapping_assist.py`, `lenai/endo_assist.py` EA-1.0, `tools/run_menu.py` RM-1.1, `tools/dev_review.py` DR-1.0, the workflows launcher in `pack.py`, `test/catalogue_run.py` (the chain run tool by tool) |
| Script | `scripts/ud_run.py`; prints `UD-0.1 ud_run h<4 chars>` (first 4 hex characters of the file's SHA-256) |
| Runs on | Native Python on the laptop through LenAI's PowerShell tool (`py -B`), the Merit pack's pinned packages. Standard library + openpyxl in the script itself. No network, no installs |
| Writes | Only the draft folder `<client folder>_DRAFT` that `setup` makes (marker `02_Inputs\Draft_run\DRAFT_RUN.json`); every other command refuses a folder without the marker |
| Data | The skill holds no client data. The run's files stay in the draft folder; the Run Digest carries no names or figures |
| Companion | `merit-preintake-profile`: if its reference exists in the client folder it is copied with it and used as evidence for the Files tab |

## How Merit's own safeguards are kept
| Safeguard in Merit | In a draft run |
| --- | --- |
| A person confirms the Mapping workbook | Replaced by the model's judgement, logged cell by cell in `decisions.csv` with a basis; guesses listed in the report |
| Apply teaches the library | Only the draft folder's copy of the library learns; the original folder is untouched (GUARD line) |
| Stops (S- codes) | Never bypassed: a stop is fixed in the workbook, or the run ends with E-UD31 to E-UD34 |
| Data gates (quarantine limit, unreadable dates, truncated sheet, type check) | Never relaxed: the run ends with E-UD32 |
| 03b review gate | Kept by default (Development factors = INPUTS). Lifted only when the user asks for DERIVED at the start |
| Constants and dates | From the user's inputs only |

## Tested before upload (Claude's sandbox: Linux, Python 3.13, duckdb 2.0.0, pyarrow 25.0.1, openpyxl 3.1.5)
Synthetic demo client of the Merit repository (`synth/demo_portfolio.py`: one known TPA with a drifted premium
layout, one new TPA, one in-house system; 656 premium rows, 2,122 claim lines) in a client folder made from a
v10.5.0 pack build.
| # | Check | Result |
| --- | --- | --- |
| S1 | `setup` with missing and malformed inputs | E-UD01 listing all 11 problems; nothing copied |
| S2 | `setup` | Draft copy made; a second run makes `_DRAFT2` |
| S3 | `step profile`, `show` (Files, Columns with filters, Payer, `_lists`) | Profile ran in the draft; tabs printed |
| S4 | `set` with a batch holding five planted errors | E-UD10, E-UD11, E-UD12, E-UD14, E-UD17; nothing written |
| S5 | `set` with the demo client's answers (134 Files / Columns cells and date rules, then 29 Values / Endorsements cells, 7 added date-rule rows), `payer` | All written and logged (183 decisions) |
| S6 | `step values`, `step dry` before and after the answers | Stops reported line by line (17 S-ENDO, then 3 S-DATES), then "the Mapping workbook validates" |
| S7 | `step ma-extract`, `step ea-extract` | Context files written by Merit's own assists |
| S8 | `step apply`, `dev` (DERIVED) | Apply OK, 10 sources, 5 new layouts; development workbook set |
| S9 | `step workflows --bg --direct`, `status` | Preflight, premium, claims, 03b, review gate, claims second pass, rate exposure, diagnostics, headline, checks guide: all exit 0 in 22 s |
| S10 | `results` | No Stop exception; premium and claims tie out; match rate 0.999 or better per TPA; headline by UW year with IBNR from the derived factors; GUARD original unchanged |

**Not tested** (no Windows or LenAI here): the launcher route (`cmd /c 05_Run_workflows.cmd nopause diag`), a
background step surviving the end of a LenAI PowerShell command, long steps on a large client, and the model's own
judgement (the test fed the demo client's answer key through `set`).

## First-run tests in LenAI (use a small or synthetic client first; record the Run Digest)
| # | Test | Pass when |
| --- | --- | --- |
| T1 | `/merit-draft-run` with the inputs of section 2 | It asks at most once (only for missing required inputs) and never afterwards |
| T2 | Setup | `ud_run.py` runs from the skill's scripts folder; WORK is `<client>_DRAFT`; the original folder has no new or changed file at the end (GUARD line) |
| T3 | Edits | Every cell it filled is in `decisions.csv` with a basis and a reason; no .xlsx was edited any other way |
| T4 | Assists | `ma_proposals_*.json` and `ea_proposals_*.json` were accepted by the assists' own apply |
| T5 | Dry run loop | It ends in "validates" within 8 rounds, or in an E-UD code with the report written |
| T6 | Background steps | `step ... --bg` returns at once and `status` reaches FINISHED; if not, it fell back to the foreground and wrote a NEWLIM line |
| T7 | Workflows | The launcher route ran (or `--direct` with a NOTE line); `results` shows the checks |
| T8 | Report | `DRAFT_RUN_REPORT.md` opens with the UNREVIEWED DRAFT line and lists every guess; the Run Digest has no names or figures |

## Change log
- 0.1.0 / UD-0.1 (15 Nov 2026): first build.
