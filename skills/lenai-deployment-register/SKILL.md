---
name: "lenai-deployment-register"
description: "Use whenever something is built for, uploaded to, changed in, or removed from GC's LenAI/LenWork (skills, connectors, uploaded manuals, laptop kits): records the live inventory with versions and sources, and checks for drift between Claude's repos and what LenAI actually has."
---

# LenAI deployment register (v5, 9 Nov 2026)

The single list of what Etam has put into LenAI / LenWork, where its source lives on the Claude side, and whether the
two still match. This file IS the register: when an item ships, changes or is withdrawn, propose an updated version of
this skill with the row changed and the version bumped. Read it at the start of any session that touches LenAI and at
the end of any session that produced something LenAI will receive.

## 1. How items reach LenAI (the only routes)
| Route | Mechanism | Notes |
| --- | --- | --- |
| Skill | LenWork > Customize > Skills: SKILL.md + `references/` folder, semver, Private / named people / Teams channel / Public | Can be loaded per chat with `/<name>`. Automatic triggering did not fire for R01 (CP1, 6 Nov 2026) but **did fire for R12 (9 Nov 2026)**: a specific, topic-led `description:` line appears to be what makes it trigger. Saving publishes a patch version; installers pick it up on the next scan |
| Connector | LenWork > Customize > Connectors > Add connector: `py <abs path>.py`, comma-separated args, encrypted env | Applies to new chats; one process per chat; elevated, no approval prompts; tool enforces its own allow-list |
| Uploaded file | a .md / .xlsx / .csv attached in a chat (persistence across chats: pending I4) | Used for the Merit encyclopedia and run cards until the Skill route carries them |
| Laptop kit | zip emailed personal -> work, unpacked on the GC laptop; LenAI runs it through its PowerShell tool (`py`) or a connector | Merit packs, TSM kit, Pricing Workbench release |

Transfer constraint: files go personal -> work by email; nothing comes back but data-free plain text.

## 2. Live inventory
| ID | Item | Type | LenAI name / version | Source of truth (Claude side) | Pack / build | Sharing | Last shipped | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | Etam context pack | Skill | `imea-reinsurance-pricing-assistant` v1.0.0 (skeleton); v1.0.1 = pack CP-1.0 once uploaded | this conversation's build (`context-pack/private`); to be committed to ete-dashboard `lenai/context_pack/` | CP-1.0 private (SKILL.md + references 01-05) | Private | 6 Nov 2026 | upload of CP-1.0 pending |
| R02 | Team context pack | Skill | not created | same, `team` build (no 04_clients_reinsurers.md) | CP-1.0 team | Teams channel (planned) | - | planned |
| R03 | Connector probe | Connector | `mcp_probe` (tools `mcp_mcp_probe_probe_*`) | ete-dashboard `probe_pack/connector/lenwork_mcp_probe.py` CP1.1 | - | per user | 6 Nov 2026 | installed; remove after merit_triage replaces it |
| R04 | Merit encyclopedia for LenAI | Uploaded file | `26_LenAI_encyclopedia.md` EN-1.1 (v9.0.0-a) + history file; the Merit page's LenAI card prepares it as a 07_LenAI folder | ete-dashboard `side_tools/merit/docs/LENAI_ENCYCLOPEDIA.md` | ships inside the Merit pack README set | n/a | with Merit v9.1.0 pack | current with code at v9.1.0 (no page-specific section yet) |
| R05 | Merit production pack | Laptop kit | Merit_v9.1.0_2026-11-09.zip (17.8 MB, 2,625 files, sha256 eaa35efea78404bb..., built from main 745cc6c; assembled in Documents\Merit_v910_Release on T-SURFACE) | ete-dashboard `side_tools/merit` (`pack.py`), tag merit-v9.1.0 (local; tag/release push not permitted from the build session) | per release | team laptops | 9 Nov 2026 (personal laptop; email to the GC laptop pending) | live; first pack with the Merit page (00_Start_Here\00_Merit_UI.cmd, port 8766) and the vendored gc-ui-kit 1.0.4 |
| R06 | Treaty Structure Metrics kit | Laptop kit | TW-1.1 (Documents\TSM_Release, unpacked Documents\TSM_kit_TW-1.1) | ete-dashboard `side_tools/treaty_workbench` (`tools/pack_tsm.py`) | per release | owner only so far | 4 Nov 2026 | live; AETM first run |
| R07 | Pricing Workbench | Laptop kit | release 1.0.0 | repo mtamsyed-gc/pricing-workbench | per release | owner | 31 Oct 2026 | live |
| R11 | XoL pricing tool | Laptop kit | 0.9.1 (page on gc-ui-kit 1.1.1, XU-1.0): xolpricing_user_0.9.1.zip (103 files, sha256 93b35afa...) and xolpricing_admin_0.9.1.zip (248 files, sha256 55a4cc3e...), built from main 095337b; on T-SURFACE in Documents\XoL_v091_Release with SHA256SUMS.txt | repo mtamsyed-gc/xolpricing (`tools/release/make_packs.py`) | per release (user pack without synthetic data, admin pack with everything) | owner | 9 Nov 2026 (personal laptop; email to the GC laptop pending) | live; laptop check Documents\20261109_v2 PASS |
| R12 | Insurance capital and IFRS 17 (UAE layer) | Skill | `insurance-capital-ifrs17` v1.0.1 | repo mtamsyed-gc/aiskills `skills/insurance-capital-ifrs17/` (main 791acf1); single file in `dist/`, rebuilt with `tools/bundle.sh` | 9 files, ~21k tokens | Private (no client data) | 9 Nov 2026 | live; tests T1-T7 passed; triggers automatically. Next: KSA overlay `references/ksa/` |
| R08 | Merit diagnostics triage | Connector (planned) | `merit_triage` | ete-dashboard `side_tools/merit/tools/merit_triage.py` + `docs/DIAG_TRIAGE_DESIGN.md`, `DIAG_ENCYCLOPEDIA_SEED.csv` | - | per user, then team | - | design DT-0.1; decisions D-T1..D-T5 pending |
| R09 | LenAI run cards / manuals | Uploaded file | LENAI_MANUAL.md, LENAI_MAPPING_ASSIST.md, LENAI_ENDORSEMENT_ASSIST.md, LENAI_PORTFOLIO_PROMPT.md, LENAI_MAPPING_REVIEW.md, LENAI_QUARANTINE_REVIEW.md; from v9.1.0 the Merit page's LenAI cards write each prompt with CLIENT / SCRIPT filled into 07_LenAI\<time>_<assist>\PROMPT.md + ATTACH | ete-dashboard `side_tools/merit/docs/` (single source; `ui/merit/manifest.json` names section + attachments) | inside Merit pack | n/a | with each pack | live |
| R10 | GC UI kit | Laptop kit (vendored) | 1.0.4 inside Merit v9.1.0 (`03_Workflows\_Build_tools\ui\kit`); 1.1.1 inside XoL 0.9.1 (`ui/kit`, PR #6) | private repo mtamsyed-gc/gc-ui-kit (main, 1.1.1); `UI_STANDARD.md` UI-0.3 | vendored per tool with VERSION + HASHES.json (`tools/vendor.py`) | with the tool's pack | 9 Nov 2026 | live in both; two kit builds in the field until Merit re-vendors 1.1.x at its next pack |

Observed but not his (GC built-ins, for orientation only): skills docx, pdf, pptx, xlsx, marsh-branding, 2026-year-end-review; integration Microsoft 365; remote connector catalogue Azure DevOps, Databricks.

## 3. Procedure
**When something ships to LenAI** (skill saved, connector added, pack emailed): add or update its row (version, source commit or pack name, date, sharing), and note in the Status column anything still pending on the LenAI side (upload not yet done, test not yet run). Bump this skill's version in the title.

**At the start of a LenAI-touching session**: read section 2; for each item the task touches, state its LenAI version and its source version. If they differ, that is drift: say so before building on either.

**Drift check (ask Etam to run in LenWork, ~2 min)**: Customize > Skills shows each skill's version; Connectors shows each connector; in a chat ask "list the files in the <skill> package with sizes". Compare with the Source column. Record the outcome as a dated line under section 4.

**Naming**: LenAI skill names are permanent (cannot be renamed); choose them once. Connector tools appear as `mcp_<connector>_<tool>`: keep connector and tool names short.

**Sharing rule**: anything carrying cedant, reinsurer or contact notes stays Private or named-people. Team or Public builds carry tools and methods only.

**Related registers**: platform limits live in the `lenai-target` skill (constraint register); Merit's own change history lives in TPA_RULES.md / AUDIT_TRAIL; HANDOVER.md carries the session-by-session state. This file records only what is deployed where.

## 4. Drift log
- 2026-11-09: R12 added. insurance-capital-ifrs17 v1.0.1 loaded into LenWork (Private) and answered all test questions correctly. It fired without a slash command. Source committed to mtamsyed-gc/aiskills main 791acf1, so LenAI and the repo are in step.
- 2026-11-09 (later): XoL 0.9.1 released: PR #6 merged fb2532b + 095337b (kit 1.1.1 vendored, manifest in the kit schema, old tools/ui/serve.py removed); laptop check Documents\20261109_v2 ui_check 42/42, Excel round trip both ways, run 00->03 from the page; packs in Documents\XoL_v091_Release. Lesson: the kit's `_ui_backup/` beside an edited workbook inside the repo was swept into the first admin pack build; now git-ignored and excluded by make_packs (test_packs checks). Merit still carries kit 1.0.4.
- 2026-11-09: R05 -> Merit v9.1.0 (merge 745cc6c, PR #49); laptop check of the pack's page on T-SURFACE PASS (HANDOVER 0BK); release zip assembled in Documents\Merit_v910_Release; not yet emailed to the GC laptop. R10 added (gc-ui-kit 1.0.4). GitHub tags/releases cannot be pushed from Claude sessions: the pack is distributed by email as before.
- 2026-11-06: R01 skeleton v1.0.0 verified by slash command (canary OSPREY found only after SKILL.md body was fixed; automatic trigger N). R03 verified: 9 tools listed, all probe sections A-H passed. R04 known behind (EN-1.0 vs code v8.0.8).