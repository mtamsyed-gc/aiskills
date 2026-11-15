# aiskills

Skills deployed to GC's LenAI / LenWork (Customize > Skills), kept here as the source of truth.

| Skill | Version | Coverage | LenAI status |
|---|---|---|---|
| `skills/insurance-capital-ifrs17` | 1.0.1 (6 Nov 2026) | Solvency regulation + IFRS 17 for insurers; UAE (CBUAE onshore) layer | Live, Private; triggers automatically (confirmed 9 Nov 2026) |
| `skills/merit-preintake-profile` | 0.3.0 (15 Nov 2026) | Independent pre-intake reference (not an input to Merit): a profile of a client's raw premium and claims files before Merit's intake profile: recommendations for the Mapping workbook's Files, Columns, Fields, Date rules and Payer tabs. Runs native Python through LenAI's PowerShell tool; carries its own scripts | Built, not yet uploaded or run in LenAI |

## Layout
- `skills/<name>/` – what gets uploaded: `SKILL.md` plus `references/`.
- `skills/<name>/scripts/` – only for a skill that runs code (`merit-preintake-profile`): uploaded with the skill and run in place. Such a skill has no single-file build.
- `dist/<name>_SINGLE-FILE.md` – the same content as one file, for routes that accept a single file. Rebuild with `tools/bundle.sh <name>`.

## Updating a skill
1. Edit the files under `skills/<name>/`, bump `version:` in `SKILL.md`, and add the change to the skill's source register.
2. Run `tools/bundle.sh <name>`.
3. Re-upload to LenWork and run the skill's test questions in a new chat.

## Rules
- No client names, engagement notes or deal terms in any skill (LenAI interim rule for Skills).
- Country overlays for `insurance-capital-ifrs17` follow `references/templates/jurisdiction-overlay-template.md` (KSA next).
