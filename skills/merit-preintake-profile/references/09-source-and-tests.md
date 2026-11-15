# Source register and tests: merit-preintake-profile

## Source
| Item | Value |
| --- | --- |
| Skill version | 0.2.0 (15 Nov 2026), prompt version PP-0.2 |
| Written from | The Merit user manual, admin guide, mapping-assist run card and browser-page specification (pack versions up to v9.1). Not checked against the Merit v10.x code: the skill makes the model read the pack's own code first, and the pack wins where they differ (NOTE lines in the Run Digest record every difference) |
| Pasted-prompt twin | `LENAI_PREINTAKE_PROFILE.md` PP-0.1 (same rules and phases, scripts embedded in the prompt): fallback only |
| Scripts | `scripts/p00_guard.py`, `scripts/p90_export.py`, `scripts/probe_template.py`. Each prints `PP-0.2 <name> h<4 chars>` (the first 4 hex characters of the SHA-256 of the file) |
| Runs on | Native Python on the laptop through LenAI's PowerShell tool (`py -B`), the Merit pack's pinned packages. No network, no installs |
| Data | The skill holds no client data, names or figures. Everything it writes stays in the client folder's `02_Inputs\Preintake` |

## Tested before upload (Claude's sandbox, synthetic client folder, Python 3.13, pandas 3.0.5, openpyxl 3.1.5)
| # | Check | Result |
| --- | --- | --- |
| S1 | Guard: snapshot, then check with nothing changed | GUARD unchanged |
| S2 | Guard: files written inside `02_Inputs\Preintake` | ignored (unchanged) |
| S3 | Guard: a file added in `05_Checks` and a library file changed | GUARD CHANGED, both listed |
| S4 | Export: valid recommendations, with and without per-layout column parts | both CSVs written, CTRL line, unresolved required fields listed |
| S5 | Export: a field outside the allowed list, an unknown layout group, two columns for one field, invalid JSON | E-PP03, E-PP02, W-PP05, E-PP01; no CSV written |
| S6 | Scripts saved with a UTF-8 BOM and CRLF line ends (as PowerShell 5.1 writes them) | run unchanged |
| S7 | Template helpers: identifier column shown as shapes, category columns as values with counts | as expected |

## First-run tests in LenAI (run on a client folder; record the Run Digest)
| # | Test | Pass when |
| --- | --- | --- |
| T1 | Type `/merit-preintake-profile` with CLIENT and PAYER | The skill loads; it does not start on a general Merit question without being asked |
| T2 | Setup | `p00_guard.py` runs from the skill's scripts folder and prints its version line and GUARD snapshot (or the copy route is used and a NOTE says so) |
| T3 | Phase 1 | It names the file holding the standard fields and reports field and required-field counts per role; E-PP10 if it cannot. Check the counts against the pack once |
| T4 | Phase 2 | It states whether the forecast came from Merit's own functions or is its own estimate; no Merit launcher or intake command line was run |
| T5 | Print discipline | No data row, name or identifier value appears in the chat: shapes only |
| T6 | Phase 4 | `p90_export.py` exits clean; `Preintake_report.md`, `preintake_files.csv`, `preintake_columns.csv` exist in `02_Inputs\Preintake` |
| T7 | Phase 5 | GUARD unchanged (apart from files of Merit's own read cache, named); Run Digest at most 12 lines with no client, file or person names |
| T8 | After Step 1, type `compare` | Only differences are listed; `Merit_MAPPING.xlsx` is unchanged (guard) |

## Change log
- 0.2.0 / PP-0.2 (15 Nov 2026): first skill build. Scripts shipped in the skill and run in place (PP-0.1 had the
  model write them from the prompt); version and hash line added to both scripts; Run Digest gains a SCRIPTS line.
