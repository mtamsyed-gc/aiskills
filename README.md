# aiskills

Skills deployed to GC's LenAI / LenWork (Customize > Skills), kept here as the source of truth.

| Skill | Version | Coverage | LenAI status |
|---|---|---|---|
| `skills/insurance-capital-ifrs17` | 1.0.1 (6 Nov 2026) | Solvency regulation + IFRS 17 for insurers; UAE (CBUAE onshore) layer | Live, Private; triggers automatically (confirmed 9 Nov 2026) |
| `skills/imea-reinsurance-pricing-assistant` | 1.0.1 (9 Nov 2026), TEAM build | Etam's working context: role, methods, tools (Merit, TSM, Pricing Workbench, IBNR), live workstreams, LenAI platform facts | Uploaded 9 Nov 2026 (Private build, which adds a clients/reinsurers file kept outside this repo); test questions in SKILL.md; loads by slash command, automatic trigger not observed |
| `skills/lenai-deployment-register` | v1 (6 Nov 2026) | Claude-side register of everything deployed to LenAI (skills, connectors, uploaded manuals, laptop kits) with versions, sources and a drift log | Claude account skill, not uploaded to LenAI; this repo is its source |

## Layout
- `skills/<name>/` – what gets uploaded: `SKILL.md` plus `references/`.
- `dist/<name>_SINGLE-FILE.md` – the same content as one file, for routes that accept a single file. Rebuild with `tools/bundle.sh <name>`.

## Updating a skill
1. Edit the files under `skills/<name>/`, bump `version:` in `SKILL.md`, and add the change to the skill's source register.
2. Run `tools/bundle.sh <name>`.
3. Re-upload to LenWork and run the skill's test questions in a new chat.

## Related
- Platform limits (sandbox, native Python, connectors): the `lenai-target` skill in Claude; connector probe and results in ete-dashboard `probe_pack/connector/`.

## Rules
- No client names, engagement notes or deal terms in any skill (LenAI interim rule for Skills).
- Country overlays for `insurance-capital-ifrs17` follow `references/templates/jurisdiction-overlay-template.md` (KSA next).
