---
name: merit-draft-run
description: Use only when the user asks for an unattended Merit draft run (also "draft run", "auto run", "run Merit end to end without me") on a client folder whose raw files are in place - copies the folder, runs intake profile, values, apply and the workflows without stopping for review, fills the Mapping workbook itself and reports every judgement it made. Needs the client folder path, payer code, the client's constants and the run dates at the start. Not for a reviewed production run, not for mapping help inside a normal run, not for questions about Merit results.
version: 0.1.0 (15 Nov 2026) - UD-0.1; run end to end on a synthetic client outside LenAI; not yet run in LenAI
---

# Merit unattended draft run (UD-0.1)

## 1. What this skill does
Given a Merit client folder with the raw files in `01_Info_Supplied` and the inputs of section 2, you take it from
intake profile to the workflows' outputs **without asking the user anything after the start**: you fill the Mapping
workbook yourself, clear the dry run's stops, apply, run the workflows and write a report of what came out and of
every judgement you made.

**The result is an UNREVIEWED DRAFT**, a first look at the numbers, never a run to quote from. Two things follow:
- You work in a **copy** of the client folder (the draft folder, WORK). Merit's apply teaches the library inside the
  folder it runs in, so unreviewed mappings must never reach the real folder. The original is not written to.
- Every cell you fill is logged with its basis (user input, data, Merit's proposal, an assist, or a guess). Guesses
  are allowed, because this is a draft, and each one is listed in the report.

Use Claude Sonnet (judgement work); if the chat is on another model, say so once and carry on.

## 2. Inputs (the user gives them at the start)
```text
REQUIRED
CLIENT                 = full path of the client folder, no trailing backslash
PAYER                  = the client's short code (e.g. ABC)
Payer name             = as booked in the premium files
Risk carrier           =
Master cedant name     =
Currency               = 3-letter code (AED, SAR ...)
Country                =
Valuation date         = yyyy-mm-dd
Premium extract date   = yyyy-mm-dd
Claims extract date    = yyyy-mm-dd
Large claim threshold  = payer share per visit
Default premium basis  = Net or Gross

OPTIONAL (default in brackets)
RI name by TPA         = {"TPA": "Reinsurer"} for TPAs whose files carry no reinsurer [none]
SME max lives          = [Merit's default]
TPA by folder          = {"folder name": "TPA code"} where a folder name is not the TPA's name [folder name in capitals]
Development factors    = INPUTS or DERIVED [INPUTS: the inputs workbook's factors; a new client has none, so no IBNR]
                         DERIVED = workflow 03b's factors from the data, applied without the review gate
Workflows              = default or all [default: every workflow but the extract]
Draft root             = folder to make the draft copy in [beside CLIENT]
```
If a REQUIRED input is missing, ask ONCE for all the missing ones together. After that, ask nothing: decide, log,
go on, or stop with a code. Never fill a required input yourself.

```text
SCRIPTS = the scripts folder of THIS skill (ud_run.py)
RUN     = py -B "SCRIPTS\ud_run.py"
WORK    = the draft folder that setup prints; TOOLS = WORK\03_Workflows\_Build_tools; DR = WORK\02_Inputs\Draft_run
```

## 3. Rules
```text
R1  PowerShell tool only, one command at a time, the py launcher. No .ps1, .bat or .cmd files of your own. Never
    install anything. Full paths in every command.
R2  You write only inside WORK. Never write to CLIENT, and never run a Merit step on CLIENT: every Merit step goes
    through  RUN step  (it refuses a folder that setup did not make).
R3  Mapping workbook cells are written only by  RUN set / RUN payer  or by the mapping and endorsement assists run
    through  RUN step. Never edit an .xlsx yourself. Never edit Merit_INPUTS.xlsx, WORK\02_Inputs\Mapping, the
    library (TOOLS\specs) or the raw files.
R4  Every edit carries "basis" (user input | data | merit proposal | assist | guess) and "why" (what decided it,
    one line). Prefer data over a guess; a guess is honest when nothing better exists.
R5  Never invent a constant, a date, a threshold, a reinsurer or a development factor: those come from section 2
    only. If one is needed and was not given: E-UD31, stop, say exactly what is missing.
R6  Never clear a stop by raising a limit, by accepting a type check you have not verified, or by dropping data
    quietly. Where section 6 allows a sheet to be excluded, the exclusion is logged and reported as a limitation.
R7  Your own probes (short read-only Python files in DR\probes, written with a here-string, run with py -B) print
    at most ~40 lines, never a row of data; identifiers, names and dates of birth only as shapes (A / 9).
R8  Time. A command should stay under ~5 minutes. For values, apply and workflows on anything but a small client
    (raw files above ~20 MB, or  py -B "TOOLS\run_menu.py" estimate "WORK"  above 3 minutes) add --bg, then poll:
    Start-Sleep -Seconds 60   then   RUN status "WORK"   until it prints FINISHED. If a --bg step never starts or
    never finishes its log, run it once without --bg and add a NEWLIM line.
R9  Bounded. At most 8 dry runs. The same stop still there after you fixed it once: E-UD33, stop.
R10 The code of the pack outranks this skill: where they differ, follow the code and add a NOTE line.
```

## 4. The script
```text
RUN setup   "<inputs.json>"            checks the inputs, makes the draft copy, snapshots the original; prints WORK
RUN show    "WORK" <tab> [--where Col=Value] [--blank Col] [--cols A,B] [--limit 60]
                                       rows of a Mapping workbook tab; tab _lists = the allowed fields and classes
RUN set     "WORK" "<edits.json>"      writes cells; refuses anything but the columns a user fills; logs every cell
RUN payer   "WORK"                     writes the section 2 constants and dates to the Payer tab
RUN step    "WORK" <name> [--bg]       profile | values | dry | apply | ma-extract | ma-apply | ea-extract |
                                       ea-apply | workflows      (workflows: add --direct if the launcher cannot run)
RUN status  "WORK"                     the --bg step: RUNNING with the log's last lines, or FINISHED with the result
RUN dev     "WORK"                     development factors as section 2 asked (after apply)
RUN results "WORK"                     the run's checks, headline by UW year, decisions by basis, the guard line
```
Edits file (write it to DR with a single-quoted here-string and Set-Content -Encoding UTF8):
```text
{"step": "<what this batch is>", "edits": [
  {"tab": "Files",   "where": {"id": "<id>"}, "set": {"TPA": "X", "Include": "Y"}, "basis": "data", "why": "..."},
  {"tab": "Columns", "where": {"Source ID": "<id>", "Raw column": "<name>"}, "set": {"Mapped field": "<Merit field>"},
   "basis": "guess", "why": "..."},
  {"tab": "Values",  "where": {"Field": "Gender", "TPA": "X", "Raw value": "M"}, "set": {"Standard value": "Male"},
   "basis": "data", "why": "..."},
  {"tab": "Endorsements", "where": {"TPA": "X", "Raw value": "<type>"}, "set": {"Class": "Addition"}, ...},
  {"tab": "Date rules", "add": {"TPA": "X", "Output": "Endorsement Effective Date", "Value 1": "<raw column>"}, ...}
]}
```
"where" must match exactly one row (add "all": true to mean several). "add" is for the Date rules tab only (a TPA
without rows of its own). A Mapped field is the Merit field name exactly as in list 1 of  RUN show "WORK" _lists
(several fields: "A; B"). A rejected batch writes nothing: fix it and run it again.

## 5. Phases
```text
P0  Inputs. Write them as JSON to "$env:TEMP\merit_draft_inputs.json" (keys: CLIENT, PAYER, payer_name, risk_carrier,
    master_cedant_name, currency, country, valuation_date, premium_extract_date, claims_extract_date,
    large_claim_threshold, default_premium_basis; optional ri_name_by_tpa, sme_max_lives, dev_factors, workflows,
    draft_root), then  RUN setup "<that file>".  E-UD01 lists every problem: if it is a missing or malformed
    REQUIRED input, that is the one question you may ask. Note WORK.
P1  Profile.  RUN step "WORK" profile   then   RUN show "WORK" Files
P2  Files tab, one row per file x sheet. Decide and set:
    TPA where blank (the user's "TPA by folder", else the folder name in capitals without spaces); Role; Header row;
    Include = N for a summary, pivot, lookup, notes or empty sheet, for an unreadable sheet and for .xls / .xlsb /
    .xlsm files (limitation); Priority where two sheets carry the same members or lines; Claims status (Paid, OS,
    Paid + OS) from the status values, not only the file name; Scope; Date order.
    Evidence, in this order: WORK\02_Inputs\Preintake\preintake_recommendations.json if the pre-intake reference
    was made for this client; profile's own row; your probes of the raw files. Leave what profile set unless the
    evidence says otherwise.
P3  Columns tab. Known sheets arrive mapped: leave them. For Drifted and Novel sheets:
    RUN step "WORK" ma-extract ; read each WORK\02_Inputs\Mapping_assist\ma_context_<k>.md ; write
    ma_proposals_<k>.json beside it exactly as WORK\README\20_LenAI_mapping_assist.md says (its JSON schema and
    its "How to decide") ; RUN step "WORK" ma-apply.  The assist writes proposals of 0.60 and above. What a
    required field still lacks you decide yourself and write with  RUN set  (basis data, merit proposal or guess).
P4  Payer tab.  RUN payer "WORK"
P5  Values.  RUN step "WORK" values   then:
    Endorsements:  RUN show "WORK" Endorsements --blank Class.  If any: RUN step "WORK" ea-extract ; read
      ea_context_<TPA>.md in WORK\02_Inputs\Endorsement_assist ; write ea_proposals_<TPA>.json as
      WORK\README\25_LenAI_endorsement_assist.md says ; RUN step "WORK" ea-apply.  Types still blank: set the Class
      (list 2 of _lists; Ignore only for a type that carries no cover and no premium).
    Date rules: every premium TPA needs Endorsement Effective Date, Member Coverage Start Date and Member Coverage
      End Date. A TPA without rows of its own: add them ("add").
    Values: Gender and Relation need a Standard value on every row of a premium TPA. Nationality, Region and Gender
      take one of the field's groups. Take the Proposed standard where there is one. Other fields may stay blank
      (the raw value is kept).
    Claim status tab, if present: Paid, OS or Rejected for each value.
    After any change to the Files or Columns tab: RUN step "WORK" values again.
P6  Dry run loop.  RUN step "WORK" dry.  For each stop, act as section 6 says, then run it again (R9).
P7  Apply.  RUN step "WORK" apply.  Exit 4 = a crash, not a mapping problem: E-UD34, stop.
P8  Development factors.  RUN dev "WORK"
P9  Workflows.  RUN step "WORK" workflows --bg , poll (R8). If the launcher cannot be run from here, use
    RUN step "WORK" workflows --bg --direct  and add a NOTE line. A failed workflow does not end your job: go on
    to P10 and report where it stopped.
P10 Results.  RUN results "WORK".  Write DR\DRAFT_RUN_REPORT.md (section 7), tell the user, end with the Run Digest.
```

## 6. What to do on a stop
| Stop | Do |
| --- | --- |
| S-REQ | Map the column that holds the field (look again at the sheet's columns and values), or a constant on the Fields tab `{"const": "..."}` only when section 2 gives the value. A required field that the file does not hold at all: E-UD31 |
| S-FIELD, S-RULE | Correct the field name (list 1 of `_lists`) or the JSON |
| S-TPA, S-PROFILE | Fill TPA, Role, Header row or Priority on the Files tab |
| S-STATUS, S-CLSTATUS | Files tab Claims status; a class for every value on the Claim status tab |
| S-ENDO | A class for the type (P5) |
| S-VALUE, S-GROUP | A standard for the value; a group from the field's groups |
| S-DATES | The missing date rule (P5); a date that is not yyyy-mm-dd is an input problem: E-UD31 |
| S-DATEORDER | Files tab Date order: DMY, MDY or MDY-XL, from the text dates |
| S-VALUES | Run the values step again |
| S-VALUES-ID | Clear or correct that Mapped field (an identifier was mapped to a value field), then values again |
| S-PAYER | An input is missing or malformed: E-UD31 |
| S-FORMAT, S-READ | Include = N for that sheet (limitation). If no premium sheet is left: E-UD32 |
| S-TYPE, S-DATE-UNREAD | Check the mapped column and the Date order once and correct them. Still stopping: E-UD32. Never set "Type check: accept" to get past it |
| S-QUARANTINE, S-TRUNCATED, S-NOPREMIUM | The data fails one of Merit's gates: E-UD32. Never raise the limit |
| S-INPUTS, S-FORMULA, S-OUTPUTS-OPEN, S-LIBRARY, S-SOURCE, any other | E-UD34: stop and report the lines as printed |

On E-UD31 to E-UD34 you still run `RUN results "WORK"`, write the report as far as the run got, and give the digest.

## 7. Report and Run Digest
`DR\DRAFT_RUN_REPORT.md` (here-string, Set-Content -Encoding UTF8), in this order:
```text
0  First line: "UNREVIEWED DRAFT RUN, UD-0.1. Made without review in a copy of the client folder. Not for quotation."
1  Outcome in 5 lines: how far it got; the checks (premium ties out, claims tie out, match rate per TPA against the
   gate); what makes the numbers unreliable, biggest first.
2  Inputs used (section 2 as given) and the draft folder.
3  Headline by UW year, as  RUN results  printed it, and the basis: premium basis, development factors INPUTS
   (no IBNR for a new client) or DERIVED (03b, unreviewed), experience to the valuation date.
4  Judgements: cells by basis; every "guess" in full (tab, row, what, why); what the two assists filled (their own
   digest counts); sheets excluded and why.
5  Limitations: no RI shares, no user development factors, values left without a standard (F-VALUE), anything
   Merit flagged that bears on the numbers (F-, W- and Q- codes with their counts).
6  Before anyone relies on this: the checks a reviewer must make, most material first.
7  Next step: the reviewed run is made in the ORIGINAL folder in the normal way; the draft's Mapping workbook and
   DR\decisions.csv are a reference for it. Do not copy the draft's library, Mapping folder or outputs into the
   original folder.
```
Tell the user the same in at most 15 lines, then the RUN DIGEST (at most 12 lines; no client, file, sheet or person
names and no figures from the data; TPA and payer codes are fine):
```text
RUN <yyyymmdd-HHMM> UD-0.1 h<4 chars from the script's version line> merit=<pack version>
PHASE 10 OK            (or: STOPPED at <phase> <code>)
CTRL tpas=<n> sheets=<n> include_y=<n> known=<n> drifted=<n> novel=<n> dry_runs=<n>
<the APPLY line RUN results printed>
<the WORKFLOWS line>
CTRL fandiff_ok=<Y/N> tieout_ok=<Y/N> match_min=<lowest match rate> tpa=<its code>
<the DECISIONS line>
<the GUARD line>
PATCH <one line per self-repair>     NOTE <skill vs code>     NEWLIM <a LenAI limitation met>
```

## 8. Codes
| Code | Means |
| --- | --- |
| E-UD01 | Inputs missing or malformed, or CLIENT is not a Merit client folder with raw files; nothing copied |
| E-UD02 | The folder given is not a draft folder made by setup |
| E-UD03 | The draft folder's paths would pass the Windows length limit: give a shorter Draft root |
| E-UD10 to E-UD14, E-UD17, E-UD19 | An edits batch refused (no row, several rows, column not editable, tab missing, a formula, basis or why missing, not JSON); nothing written |
| E-UD15, E-UD16, E-UD18 | The Mapping workbook is open or missing; the development workbook is not as expected |
| E-UD20 | Unknown step name |
| E-UD31 | A value only the user can give is needed |
| E-UD32 | The data fails one of Merit's gates: a person must look |
| E-UD33 | The same stop survived a fix |
| E-UD34 | A crash or a stop outside the mapping |
Source, tests and first-run checks: references/09-source-and-tests.md.
