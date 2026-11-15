---
name: merit-preintake-profile
description: Use only when the user asks for a Merit pre-intake profile (pre-intake review) of a client folder - a look at the raw premium and claims files in 01_Info_Supplied BEFORE Merit's intake profile step runs, giving recommendations for the Merit_MAPPING workbook's Files, Columns, Fields, Date rules and Payer tabs. Needs the client folder path and the payer code. Not for mapping after profile has run (mapping assist), not for questions about Merit outputs or results.
version: 0.3.0 (15 Nov 2026) - PP-0.3, independent-reference build (own view first, Merit cross-check after); not yet run in LenAI
---

# Merit pre-intake profile (PP-0.3)

## 1. What this skill does
Before Merit's own intake profile (Step 1) runs for a new client, you look at the raw premium and claims files and
tell the user what the Mapping workbook (02_Inputs\Merit_MAPPING.xlsx; tabs Files, Columns, Fields, Date rules,
Payer) should end up saying, and why.

**This is an independent reference for the user, not an input to Merit.** Nothing in Merit reads what you write,
and nothing you write is meant to be loaded into it: the user keeps your report beside the Mapping workbook and
decides by hand what to take over. So the order matters. You form your OWN view from the data first (you may use
Merit's readers and detectors as tools, and its field definitions as the vocabulary), you test it with your own
probes, and only when your view is fixed do you look at what Merit's profile would propose, as a cross-check shown
beside yours. A second opinion that starts from the first one is not independent.

Use Claude Sonnet for this (judgement work); if the chat is on another model, say so once and carry on.

## 2. Inputs (ask once if either is missing; nothing else is needed)
```text
CLIENT = full path of the client folder, no trailing backslash (it holds 01_Info_Supplied, 02_Inputs, 03_Workflows ...)
PAYER  = the client's short code

OUT     = CLIENT\02_Inputs\Preintake          (the only folder you may write to)
TOOLS   = CLIENT\03_Workflows\_Build_tools    (Merit's code and its library, TOOLS\specs)
RAW     = CLIENT\01_Info_Supplied             (the client's files)
SCRIPTS = the scripts folder of THIS skill    (p00_guard.py, p90_export.py, probe_template.py)
```
If the user types `compare` after an earlier run, go straight to Phase 6.

## 3. Rules
```text
R1  PowerShell tool only, one command at a time, the py launcher (python is not on PATH). No .ps1, .bat or .cmd
    files. Never install anything. Replace CLIENT, OUT, TOOLS, RAW, SCRIPTS by full paths in every command.
R2  Read-only everywhere except OUT. Never change, rename, move, convert or delete anything in RAW. Never write
    Merit_MAPPING.xlsx, intake_profile.json, 05_Checks or TOOLS\specs. Never run a Merit launcher or the command
    line of an intake step (profile, values, apply) or of mapping_assist / endo_assist.
R3  You MAY reuse Merit's code: import and call the functions the intake profile step uses (file discovery, TPA and
    role from the folder, readers, header-row detection, kind and mask of a column, date order, layout fingerprint
    against the library, field proposals). Read a function before you call it. Call functions, never a script's
    main / command line, and nothing that writes outside OUT. If a function takes an output path, give it one
    inside OUT. If you cannot tell whether it writes, do not call it: write the small part yourself.
R4  Everything you run beyond the fixed commands and this skill's scripts is a Python probe: a file
    OUT\probes\pNN_<what>.py written with a here-string and run with  py -B  (pattern in SETUP). At most ~60 lines each, one question each. Keep
    every probe: they are the record of what you did. Probes open files read-only, use only the installed packages
    (standard library, pandas, openpyxl, pyarrow, duckdb, numpy), no network, no subprocess, no delete.
R5  Print budget: at most ~40 lines per command, never a row of data as it stands. Anything that could identify a
    person or a policy (member, policy, claim, card, national ID numbers, names, dates of birth, phones, emails) is
    shown only as a shape (letters -> A, digits -> 9). Category values with counts, min / max of dates, and
    aggregates of amounts are fine.
R6  Time: sample first (the first 50,000 data rows of a sheet). Read a whole large sheet only for a named question
    (latest date, key overlap, row-limit check), only the columns needed, one file at a time. Keep a command under
    ~5 minutes; say so before one you expect to take over ~2 minutes.
R7  Evidence, not guesses. Never invent a constant, a date, a class or a business rule. Where the code is silent,
    or the data contradicts the code's assumption, put it under "Questions" or "You decide". The code of THIS
    pack outranks this skill: where they differ, follow the code and add a NOTE line saying what differed.
R8  You may fix path, encoding, header-row offset and dtype problems in your own probes yourself (log each as
    PATCH <what>). If the same command fails twice, drop that line of inquiry, note it, go on.
R9  Do not wait for the user's approval between phases. Stop only on an E-PP code.
```

## 4. Setup (fixed commands)
```text
S1  New-Item -ItemType Directory -Force -Path "OUT\probes" | Out-Null
S2  This skill's scripts are run as they are, never retyped or changed:
      py -B "SCRIPTS\p00_guard.py" "CLIENT" snap
    It prints its version line (PP-0.3 p00_guard h....) and "GUARD snapshot files=<n>".
    If RAW is missing or holds no files: E-PP11, stop.
    If the scripts cannot be run from the skill's folder: copy the three files unchanged into OUT\probes and use
    that folder as SCRIPTS; say so in a NOTE line. If they cannot be found at all: E-PP13, stop.
S3  Your own probes start from SCRIPTS\probe_template.py (read it once: it puts Merit's modules on the path and
    gives you mask() and top()). Write each probe with this pattern. Nothing is indented in the real command:
    @' ends its line, the script follows from column 1, and the closing '@ is at column 1 of its own line.
@'
<probe text>
'@ | Set-Content -Path "OUT\probes\pNN_<what>.py" -Encoding UTF8
    Run:  py -B "OUT\probes\pNN_<what>.py" "CLIENT" <other arguments>
```

## 5. Phases
```text
PHASE 1 - Learn Merit from this pack (read; run nothing of Merit's yet)
1.1 Pack version:  Get-Content "CLIENT\README\VERSION.txt"
1.2 Find the code and the field catalogue:
      Get-ChildItem -Recurse -File "TOOLS" -Include *.py,*.json,*.csv,*.md | Select-String -Pattern "Unique Member Identifier","req_exempt" -List | Select-Object -ExpandProperty Path
    Read the files that hold: (a) the standard (SchemeA) fields per role, premium and claims: exact names, which
    are required, type (Date / Amount / text), the usual header words; (b) the fields set elsewhere, which a column
    must not feed (Payer tab, Files tab, Date rules tab, the engine, a constant); (c) the intake profile step: how
    it finds files, takes TPA and role from folder names (aliases), detects the header row, classes a sheet Known /
    Drifted / Novel against the library, guesses Claims status, Scope and Date order, treats a sheet at Excel's row
    limit and split sets, pre-fills the Payer tab for --payer, and which columns each tab of the workbook has;
    (d) req_exempt: which required fields are resolved outside the Columns tab.
1.3 The library: TOOLS\specs (formats = known layouts and their column maps, TPA families, payer overlays, runs).
    Note which TPAs and layouts it knows, and whether PAYER or a similar client is already in it. Do NOT open the
    layouts' column maps or another client's rules yet: they belong to the cross-check (Phase 3, part I).
1.4 Guides, if present (search them, do not load big ones whole): CLIENT\README\26_LenAI_encyclopedia.md,
    20_LenAI_mapping_assist.md (its "How to decide" rules are yours for the Columns tab),
    25_LenAI_endorsement_assist.md, 02_Change_guide.md; CLIENT\02_Inputs\Mapping\TPA_RULES.md;
    TOOLS\config\message_codes.csv (the S- / F- / Q- / W- codes you will cite).
1.5 If you cannot find the field catalogue (1.2a): E-PP10, stop and tell the user what you searched. Never work from
    field names you remember or that this skill mentions.
Say in at most 15 lines what you found: version, files read, fields and required fields per role (counts), tabs
and their columns, anything missing.

PHASE 2 - Inventory and structure
2.1 Files:  Get-ChildItem -Recurse -File "RAW" | Select-Object FullName, Length, LastWriteTime | Format-Table -AutoSize -Wrap
2.2 Row counts, if the pack has it (documented as writing nothing):  py -B "TOOLS\count_rows.py" "RAW"
2.3 Structure. For every file x sheet, on a 50,000-row sample: header row, columns, and per column its kind,
    non-empty % and values shown (categories with counts, shapes for identifiers). Merit's readers and its
    header / kind / mask / date-order detectors may do this work (R3). Do NOT call its field proposer or its
    layout match against the library yet. Print one line per sheet.
2.4 Group sheets with the same column set into layout groups G01, G02 ... (one decision per layout).

PHASE 3 - Investigate and decide (your own view; this is where you go beyond the code)
Work like an analyst who must sign the mapping: form a hypothesis, write a probe, read the result, follow up on
anything odd. Budget about 40 probes. Parts A to H are decided from the data and the field definitions alone.
Cover at least:
A  Files tab. For each sheet: is it data or a pivot / summary / lookup / notes tab (Include N)? Is the header row
   right (title lines, two-row or merged headers, repeated header rows, total or subtotal rows, trailing blank
   rows)? Hidden sheets. Files profile will not read or apply will refuse (.xls, .xlsb, .xlsm; a CSV that is not
   comma-separated; names starting with _). A sheet ending exactly at 1,048,576 or 65,536 rows (truncated extract,
   or one part of a split set?). The same file twice, last month's file left in, year tabs, two sheets carrying the
   same members or the same claim lines (which should win: Priority; or remove one). TPA or role the folder name
   does not give. Claims status from the status column's values and the amounts, not only from the file name
   (paid, outstanding, both in one sheet, rejected lines). Scope from the claim type values. Date order from the
   text dates themselves (count first part > 12 and second part > 12).
B  Columns tab. For every raw column of every layout group: the standard field(s) it should feed, or none. Read
   the header as a TPA analyst would (abbreviations, joined words, typos, Arabic or transliterated headers), then
   test it on the values: kind against the field's type; categories (gender, relation, endorsement or member
   status words); identifiers by shape; start / end pairs at policy and at member level; policy vs member vs
   master-contract identifiers; gross vs net premium and their components; claimed, approved, member share and
   payer share (test the arithmetic between them before you say which is the payer share); dates that only mean
   something with the transaction type (leave those to the Date rules tab); columns fixed by a constant (leave
   blank). Repeated header names. Confidence: 0.90+ header unambiguous and values agree; 0.70-0.89 strong synonym
   with support from the values; 0.50-0.69 plausible; below 0.50 a guess (give it, marked as a guess).
C  Linkage forecast (do this for every TPA with both sides). Clean keys the way Merit's code does, then measure
   what share of claim lines, and of the payer share, finds its member in the premium file, for each plausible
   pair of key columns (member id, card number, policy + member). Merit flags a TPA below its match-rate gate
   (read the gate from the code). Recommend the key columns that link best. Report key hazards: scientific
   notation, lost leading zeros, apostrophes, trailing ".0", spaces, mixed formats between the two sides.
D  Fields tab. Per layout group, every required field: resolved by a column, the Date rules tab, the Payer tab,
   the Files tab, a constant the user must supply (say which cell and that the form is {"const": "..."}; do not supply the
   value unless the data proves it), or MISSING (what to ask the client for). Several payers in a payer column
   (a fronted file?) and a TPA whose files carry no reinsurer are Fields / Payer tab matters: flag them.
E  Date rules tab (per premium TPA). Is there an endorsement / transaction type column? List its values with
   counts and the sign of the premium on each (positive, negative, zero shares). Which column is the transaction
   date; where the deletion date sits (member end column, a separate column, or only the transaction date: compare
   them on the deletion-like rows); member start and end; endorsement number; processing date. Propose the rows in
   the tab's own shape (TPA, Output, If type, Value 1, Value 2, Null if) with a confidence each. If the file is a
   member snapshot with no transactions, say so and what the code does with that.
F  Payer tab. Evidence for each key the code lists: the payer name(s) as booked, currency (a currency column, or
   none), country, which TPAs need "RI name by TPA", premium basis available (gross, net or both), and LATEST
   DATES per source (endorsement / member start; treatment, payment, reported or processed) as candidates for the
   valuation and extract dates. The dates, thresholds and names are the user's to decide: mark them "You decide".
G  Early view of Step 2. Gender and Relation values (every one needs a standard), endorsement types (every one
   needs a class), claim status values of a combined sheet, policy type, nationality and region spellings, any
   value field that looks like an identifier. Counts only; the values step and the endorsement assist decide.
H  Sense checks across files: period covered by premium against treatment dates per TPA, months with no or few
   claims, more than one currency, negative or zero premium and payer share, members in two TPAs at once.
I  Cross-check against Merit - only now, with A to H written down (save them as OUT\own_view.json first).
   With Merit's own functions (R3), on the same sample, get what profile will put for every file x sheet: TPA,
   Role, Header row, Status Known / Drifted / Novel and the layout matched, Claims status, Scope, Date order,
   Include, and Proposal 1 with its confidence for every column. Save it as OUT\profile_forecast.json. If the
   functions cannot be called safely, read the library's layouts yourself and mark the forecast "own estimate".
   Where Merit differs from you, do not simply adopt it: test the difference with a probe. Keep your view, or
   change it and write "changed after cross-check: <why>" in the evidence. A Known layout whose map an earlier
   client confirmed is strong evidence; a proposal scored from the header alone is not. Both views are reported.

PHASE 4 - Write the recommendations (into OUT)
4.1 preintake_recommendations.json, written with a single-quoted here-string and Set-Content -Encoding UTF8.
    Nothing in Merit reads this file: it only lets p90_export check your field names and build the two CSVs.
    {
      "version": "PP-0.3", "model": "<model>", "merit_version": "<from 1.1>", "payer": "PAYER",
      "allowed_fields":  {"premium": ["<every standard field of the role, exactly as in the code>"], "claims": [...]},
      "required_fields": {"premium": [...], "claims": [...]},
      "files":   [{"file": "<path below 01_Info_Supplied>", "sheet": "<sheet, or empty for csv / parquet>",
                   "tpa": "", "role": "premium|claims", "include": "Y|N", "header_row": 1, "priority": 1,
                   "claims_status": "", "scope": "", "date_order": "", "predicted_status": "Known|Drifted|Novel|Empty|Unreadable",
                   "layout_group": "G01", "rows": 0,
                   "profile_will": "<from the cross-check: what profile will put, where it differs from yours>",
                   "note": "<the reason, one line>"}],
      "columns": [{"layout_group": "G01", "raw_column": "<exactly as in the file>", "fields": ["<field>"],
                   "confidence": 0.00, "profile_proposal": "<from the cross-check: Merit's own Proposal 1, or empty>",
                   "evidence": "<at most 12 words>"}],
      "fields":  [{"layout_group": "G01", "field": "<required field>",
                   "resolved_by": "column|date_rules|payer_tab|files_tab|constant_needed|MISSING", "detail": ""}],
      "date_rules": [{"tpa": "", "output": "", "if_type": "", "value_1": "", "value_2": "", "null_if": "",
                      "confidence": 0.00, "evidence": ""}],
      "payer":   [{"key": "", "recommendation": "", "evidence": "", "decision": "evidence|You decide"}],
      "questions": ["<for the client or TPA, most material first>"]
    }
    One "columns" entry per raw column of each layout group, also when the answer is not used ("fields": []).
    Several fields in "fields" only when the column truly is each of them. For a large client write "columns": []
    here and one file per layout group, OUT\preintake_columns_G01.json = {"columns": [...]}, and so on.
4.2 Check and export:  py -B "SCRIPTS\p90_export.py" "CLIENT"
    It refuses a field that is not in allowed_fields for the sheet's role (E-PP03), an unknown layout group or a
    group that mixes roles (E-PP02), a bad confidence (E-PP04) and invalid JSON (E-PP01): fix the JSON, run it
    again. It writes preintake_files.csv and preintake_columns.csv and prints the CTRL line.
4.3 Preintake_report.md (here-string, Set-Content -Encoding UTF8), in this order, short lines, no data rows:
    0 First line: "Independent pre-intake reference, PP-0.3. Prepared from the raw files. Not read by Merit."
    1 Verdict in 5 lines: ready for profile or what to fix first; the three biggest risks.
    2 Before you run profile: files to convert, remove, rename or move, with the reason.
    3 Files tab: a table, one row per file x sheet: your view, why, and (cross-check) what profile will put.
    4 Columns tab: per layout group, the required fields and which column feeds each, then only the columns where
      you differ from Merit's proposal or are below 0.70 (the full list is preintake_columns.csv).
    5 Fields tab: constants needed and MISSING fields, per layout group.
    6 Date rules tab: the proposed rows per TPA, with the evidence table of types, counts and premium signs.
    7 Payer tab: key, evidence, "You decide" items.
    8 Linkage forecast: per TPA, match % by lines and by payer share for the recommended keys and the next best.
    9 Early view of Values / Endorsements / Claim status.
    10 Questions for the client or TPA.
    11 What I could not check, NOTE lines (skill vs code), PATCH lines.

PHASE 5 - Close
5.1 py -B "SCRIPTS\p00_guard.py" "CLIENT" check
    "GUARD unchanged" is required. Files of Merit's own read cache, if its readers made any, are acceptable: name
    them. Anything else changed: E-PP12, list it and tell the user first.
5.2 Tell the user, briefly: the verdict, what to fix before profile, where you differ from what profile will propose
    (counts and the five most material), the linkage forecast, the "You decide" items and the questions.
5.3 End with the RUN DIGEST, at most 12 lines, with no client, file, sheet or person names and no values from the
    data (TPA and payer codes are fine):
      RUN <yyyymmdd-HHMM> PP-0.3 merit=<pack version>
      PHASE 5 OK            (or: STOPPED at <phase> <E-PP code>)
      CTRL tpas=<n> files=<n> sheets=<n> include_y=<n> layouts=<n> known=<n> drifted=<n> novel=<n>
      <the CTRL line p90_export printed>
      SCRIPTS p00=h<4 chars> p90=h<4 chars>      (from the version lines the two scripts printed)
      CTRL differ_from_profile=<n> you_decide=<n> questions=<n> probes=<n>
      CTRL link_min=<lowest match % by lines> tpa=<its code>
      <the GUARD line>
      PATCH <one line per self-repair>
      NOTE <one line per place this skill and the code differed>
      NEWLIM <any LenAI limitation you met, one line>
5.4 Then say: "Fix section 2 of the report, run Step 1 (profile) with the payer typed, close the workbook, and type
    compare."

PHASE 6 - Only when the user types: compare   (profile has run; Merit_MAPPING.xlsx is closed)
Take a new guard snapshot (p00_guard.py ... snap). With a probe, open CLIENT\02_Inputs\Merit_MAPPING.xlsx
read-only and compare it with preintake_recommendations.json, matching by file, sheet and raw column. List only
differences: Files tab (TPA, Role, Header row, Include, Priority, Claims status, Scope, Date order, Status against
your predicted status), Columns tab (Mapped field / Proposal 1 against your fields, and every MISMATCH), Fields /
Coverage (MISSING against your "fields"), Date rules and Payer tab rows that arrived pre-filled from another
client. Say for each whether the user should change the workbook or whether profile was right and you were wrong. Write
it to OUT\Preintake_compare.md, run the guard check, change nothing in the workbook.
```

## 6. Codes
| Code | Means | Do |
| --- | --- | --- |
| E-PP01 | Recommendations JSON missing, not valid, or a top-level key absent | Fix the file, run p90_export again |
| E-PP02 | Unknown layout group, a group mixing roles, or a role that is not premium / claims | Fix the files / columns entries |
| E-PP03 | A recommended field is not a standard field of the sheet's role | Use the exact name from the pack's code, or leave the column unmapped |
| E-PP04 | Confidence not between 0 and 1 | Fix the entry |
| W-PP05 | Two columns feed one field in a layout group | Keep one unless a date rule or calculation needs both |
| E-PP10 | The standard field catalogue was not found in the pack | Stop; tell the user what was searched |
| E-PP11 | 01_Info_Supplied missing or empty | Stop |
| E-PP12 | The guard found a change outside Preintake | List it; tell the user before anything else |
| E-PP13 | This skill's scripts cannot be found or run | Stop; tell the user |

## 7. What is fixed and what is yours
The outputs are a reference for the user only: no step of Merit reads them, and none should be built to.
Fixed by the scripts: nothing outside OUT changes (p00_guard), every recommended field is a field of this pack
(p90_export, against the list you copied from the code: report its counts in Phase 1). Yours, under the rules: which
of Merit's functions to call, what to investigate, and the recommendations. Tests and source: references/09-source-and-tests.md.
