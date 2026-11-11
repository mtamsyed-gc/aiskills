# aiskills

Skills deployed to GC's LenAI / LenWork (Customize > Skills), kept here as the source of truth.

| Skill | Version | Coverage | LenAI status |
|---|---|---|---|
| `skills/insurance-capital-ifrs17` | 1.0.1 (6 Nov 2026) | Solvency regulation + IFRS 17 for insurers; UAE (CBUAE onshore) layer | Live, Private; triggers automatically (confirmed 9 Nov 2026) |
| `skills/merit-outputs` | 1.0.0 (11 Nov 2026) | Merit's output files: every column of the output contract (IP4-13, Merit v9.2.0), joins, dashboard measures, Excel deliverables, pandas recipes | Built, not yet uploaded |

## Layout
- `skills/<name>/` – what gets uploaded: `SKILL.md` plus `references/`.
- `dist/<name>_SINGLE-FILE.md` – the same content as one file, for routes that accept a single file. Rebuild with `tools/bundle.sh <name>`.

## Generated skills
`skills/merit-outputs` is **generated**: do not edit it here. Its text lives in mtamsyed-gc/ete-dashboard
`side_tools/merit/lenai/outputs_skill/` and the column dictionaries come from Merit's `model_contract.json`. After a
contract or text change, from an ete-dashboard clone next to this one:
```
python side_tools/merit/tools/build_outputs_skill.py --dest ../aiskills/skills/merit-outputs --date <yyyy-mm-dd>
tools/bundle.sh merit-outputs
```
Bump `SKILL_VERSION` in the builder first. Test questions T1-T8: `references/09-source-register.md`.

## Updating a skill
1. Edit the files under `skills/<name>/`, bump `version:` in `SKILL.md`, and add the change to the skill's source register.
2. Run `tools/bundle.sh <name>`.
3. Re-upload to LenWork and run the skill's test questions in a new chat.

## Rules
- No client names, engagement notes or deal terms in any skill (LenAI interim rule for Skills).
- Country overlays for `insurance-capital-ifrs17` follow `references/templates/jurisdiction-overlay-template.md` (KSA next).
