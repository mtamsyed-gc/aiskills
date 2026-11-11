# aiskills

Skills deployed to GC's LenAI / LenWork (Customize > Skills), kept here as the source of truth.

| Skill | Version | Coverage | LenAI status |
|---|---|---|---|
| `skills/insurance-capital-ifrs17` | 1.0.1 (6 Nov 2026) | Solvency regulation + IFRS 17 for insurers; UAE (CBUAE onshore) layer | Live, Private; triggers automatically (confirmed 9 Nov 2026) |
| `skills/merit-outputs` | 1.0.0 (11 Nov 2026) | Merit's output files: every column of the output contract (IP4-13, Merit v9.2.0), joins, dashboard measures, Excel deliverables, pandas recipes | Built, not yet uploaded |
| `skills/merit-dev-factors` | 1.0.0 (11 Nov 2026) | Runs Merit's 03b development-factor engine (`development.py` DF-1.0) on a run's outputs through the laptop's `py` (wrapper `lenai_dev_factors.py` LD-1.0) and explains the results | Built, not yet uploaded |

## Layout
- `skills/<name>/` – what gets uploaded: `SKILL.md` plus `references/`.
- `dist/<name>_SINGLE-FILE.md` – the same content as one file, for routes that accept a single file. Rebuild with `tools/bundle.sh <name>`.

## Generated skills
`skills/merit-outputs` and `skills/merit-dev-factors` are **generated**: do not edit them here. Their text lives in mtamsyed-gc/ete-dashboard
`side_tools/merit/lenai/outputs_skill/` and `lenai/devfactors_skill/`; the dictionaries, settings, codes and the
embedded wrapper come from Merit's code (`model_contract.json`, `oracle/development.py`, `tools/lenai_dev_factors.py`). After a
contract or text change, from an ete-dashboard clone next to this one:
```
python side_tools/merit/tools/build_outputs_skill.py --dest ../aiskills/skills/merit-outputs --date <yyyy-mm-dd>
tools/bundle.sh merit-outputs
python side_tools/merit/tools/build_devfactors_skill.py --dest ../aiskills/skills/merit-dev-factors --date <yyyy-mm-dd>
tools/bundle.sh merit-dev-factors
```
Bump `SKILL_VERSION` in the builder first. Test questions: `references/09-source-register.md` of each (T1-T8, D1-D6).

## Updating a skill
1. Edit the files under `skills/<name>/`, bump `version:` in `SKILL.md`, and add the change to the skill's source register.
2. Run `tools/bundle.sh <name>`.
3. Re-upload to LenWork and run the skill's test questions in a new chat.

## Rules
- No client names, engagement notes or deal terms in any skill (LenAI interim rule for Skills).
- Country overlays for `insurance-capital-ifrs17` follow `references/templates/jurisdiction-overlay-template.md` (KSA next).
