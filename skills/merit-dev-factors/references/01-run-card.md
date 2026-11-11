# 01 Run card

Runs on the user's laptop through LenAI's PowerShell tool with the `py` launcher (never `python`, never a .ps1).
Use absolute paths in double quotes. Replace `<client>` with the Merit client folder (the one holding `04_Outputs`).

## Step 0. Find the script
| Pack | Script |
|---|---|
| Merit packs that ship it | `<client>\03_Workflows\_Build_tools\tools\lenai_dev_factors.py` |
| Earlier packs (Merit v9.2.0 and before) | not shipped: write it from `references/04-wrapper-source.md` to `<client>\07_LenAI\lenai_dev_factors.py` |

Check it before every first use in a chat:
```
py "<script>" --version
```
The line must read `lenai_dev_factors LD-1.0 check d1ec9627a6205df7`. Any other hash = a damaged or different copy:
do not run it; rewrite it from reference 04 (or ask the user for the pack's copy).

## Step 1. Run
Client folder with its workbooks (the normal case):
```
py "<script>" --outputs "<client>\04_Outputs"
```
A copy written to `07_LenAI` (earlier packs) also needs the pack's build tools:
```
py "<client>\07_LenAI\lenai_dev_factors.py" --outputs "<client>\04_Outputs" --build-tools "<client>\03_Workflows\_Build_tools"
```
Only output CSVs in some folder (not a client folder): give the build tools and a results folder outside it:
```
py "<script>" --outputs "<folder with fact_claims.csv>" --build-tools "<client>\03_Workflows\_Build_tools" --dest "<results folder>"
```
Options (add only what the user asked for; reference 02 explains each):
`--mode FULL` · `--window 6|9|12|18|24|36|ALL` · `--source INPUTS|DERIVED_ELSE_INPUTS|DERIVED` · `--bases IBNR|IBNP|BOTH`
· `--credibility PARTIAL` · `--tpa NAME1,NAME2` · `--inputs "<Merit_INPUTS.xlsx>"` · `--dev "<Merit_DEVELOPMENT.xlsx>"`.

## What it reads (first source found wins; the script prints which)
| Input | 1st | 2nd | 3rd |
|---|---|---|---|
| Valuation and claims extract dates | `--inputs` workbook, Run settings | `<client>\02_Inputs\Merit_INPUTS.xlsx` | `run_manifest_claims.csv` (`valuation_date`, `claims_extract_date`) |
| User factors (`CF_Inputs`, the comparison and the fallback) | `--inputs` workbook, Development factors | `<client>\02_Inputs\Merit_INPUTS.xlsx` | `cf_selected.csv` `CF_Used` (the factors that run applied), else none |
| Settings per TPA, parameters | `--dev` workbook | `<client>\02_Inputs\Merit_DEVELOPMENT.xlsx` | Merit defaults: Simple, Source INPUTS, both bases, window 12, every parameter at its default |
| Claims, exposure | `fact_claims.csv`, `fact_member_month.csv` of the run (csv\ or the folder given) | | |

Option flags override the settings of **every** TPA. Claims used: `InExperience = 1`, StatusClass Paid or Outstanding
(development.py's own filter).

## What it writes (in `--dest`, default `<client>\07_LenAI\<yyyymmdd-hhmm>_dev_factors`)
`csv\dev_*.csv` (11 tables), `Merit_03b_Development.xlsx` (same tables, one sheet each, README first),
`csv\would_apply_factors.csv` and `csv\would_apply_bf.csv` (what Merit's claims workflow would apply under these
settings; empty with Source INPUTS), `RUN_NOTE.txt` (versions, the inputs used, findings count).

## Step 2. Check and report
- Exit code 0 and a `results:` line = done. `STOP ...` (exit 2) = a refusal or a missing input: report the line as is.
- Expect about 5 s on a synthetic portfolio of 5 TPAs; real runs scale with `fact_claims` rows. If a command nears
  5 minutes, run TPA by TPA with `--tpa`.
- Report per reference 03; quote `RUN_NOTE.txt`.

## Do not
- run Merit's launchers, workflows or `development.py` directly (it writes stage files into the run);
- pass a `--dest` inside `04_Outputs`, `02_Inputs` or `01_Info_Supplied`;
- install packages (the Merit runtime already has openpyxl); edit any workbook.
