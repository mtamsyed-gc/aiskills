# aiskills

Skills deployed to GC's LenAI / LenWork (Customize > Skills), kept here as the source of truth.

| Skill | Version | Coverage | LenAI status |
|---|---|---|---|
| `skills/insurance-capital-ifrs17` | 1.1.0 (9 Nov 2026) | Solvency regulation + IFRS 17 for insurers; UAE (CBUAE onshore) layer; Qatar QFC (QFCRA) layer | 1.0.1 live, Private; triggers automatically (confirmed 9 Nov 2026). 1.1.0 to upload |

## Layout
- `skills/<name>/` – what gets uploaded: `SKILL.md` plus `references/`.
- `dist/<name>_SINGLE-FILE.md` – the same content as one file, for routes that accept a single file. Rebuild with `tools/bundle.sh <name>`.

## Updating a skill
1. Edit the files under `skills/<name>/`, bump `version:` in `SKILL.md`, and add the change to the skill's source register.
2. Run `tools/bundle.sh <name>`.
3. Re-upload to LenWork and run the skill's test questions in a new chat.

## Rules
- No client names, engagement notes or deal terms in any skill (LenAI interim rule for Skills).
- Country overlays for `insurance-capital-ifrs17` follow `references/templates/jurisdiction-overlay-template.md` (KSA and onshore Qatar QCB next). Folder numbering: uae 10-19, ksa 20-29, qa-qfc 30-39.
