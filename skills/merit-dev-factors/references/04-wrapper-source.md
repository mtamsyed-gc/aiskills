# 04 Wrapper source (for packs that do not ship it)

Use only when `<client>\03_Workflows\_Build_tools\tools\lenai_dev_factors.py` does not exist. The file below is
`lenai_dev_factors.py` LD-1.0, check hash `d1ec9627a6205df7`. It contains no method: it calls the pack's own
`development.py`.

## Write it out (one PowerShell command, exactly as below)
Copy the code block **character for character** between the two here-string lines; the closing `'@` must start its line.
```
New-Item -ItemType Directory -Force "<client>\07_LenAI" | Out-Null
$code = @'
<the whole code block below>
'@
Set-Content -Path "<client>\07_LenAI\lenai_dev_factors.py" -Value $code -Encoding UTF8
```
Then verify (the hash ignores the BOM and CRLF that PowerShell adds):
```
py "<client>\07_LenAI\lenai_dev_factors.py" --version
```
Expected: `lenai_dev_factors LD-1.0 check d1ec9627a6205df7`. If it differs, the copy is not exact: do not run it.
Delete it and write it again, or ask the user for the file from the Merit repository.

## lenai_dev_factors.py
```python
"""Derived development factors (Merit 03b) for LenAI, from a run's output files (skill 'merit-dev-factors').

    py lenai_dev_factors.py --outputs "<client>\\04_Outputs" [--dest <folder>] [--build-tools <_Build_tools>]
                            [--inputs <Merit_INPUTS.xlsx>] [--dev <Merit_DEVELOPMENT.xlsx>]
                            [--mode SIMPLE|FULL] [--window 6|9|12|18|24|36|ALL] [--source INPUTS|DERIVED_ELSE_INPUTS|DERIVED]
                            [--bases BOTH|IBNR|IBNP] [--credibility BINARY|PARTIAL] [--tpa A,B]

Runs Merit's own reference implementation, oracle/development.py of the pack (03_Workflows\\_Build_tools\\oracle),
unchanged: this file only supplies its inputs and decides where the results go. Every method rule is in
development.py; nothing here computes a factor.

Inputs, each from the first source found (the source used is printed and written to RUN_NOTE.txt):
  dates      --inputs workbook (Run settings) > <client>\\02_Inputs\\Merit_INPUTS.xlsx > run_manifest_claims.csv
             (valuation_date, claims_extract_date)
  user CFs   --inputs workbook (Development factors) > <client>\\02_Inputs\\Merit_INPUTS.xlsx > cf_selected.csv CF_Used
             (the factors the run applied) > none (CF_Inputs blank)
  settings   --dev workbook (Settings, Parameters) > <client>\\02_Inputs\\Merit_DEVELOPMENT.xlsx > Merit's defaults
             (Simple, Source INPUTS, both bases, window 12; every parameter at its default)
  --mode / --window / --source / --bases / --credibility override the settings of every TPA.

Outputs, in --dest (default <client>\\07_LenAI\\<yyyymmdd-hhmm>_dev_factors): csv\\dev_*.csv, Merit_03b_Development.xlsx,
csv\\would_apply_factors.csv and csv\\would_apply_bf.csv (what the claims workflow's second pass would apply under
these settings) and RUN_NOTE.txt. Never writes into 04_Outputs, 02_Inputs or 01_Info_Supplied (the stage files there
drive the next Merit run): such a --dest is refused. --version prints the version and a check hash of this file
(BOM and CRLF ignored) to verify a copy. Stdlib + openpyxl (both in the Merit runtime). Exit 0 done,
2 refused / input missing.
"""
import argparse
import csv
import hashlib
import importlib.util
import sys
import time
from pathlib import Path

VERSION = "LD-1.0"
OUT_SUBDIRS = ("csv", "parquet", "xlsx", "collated", "stage")
PROTECTED = ("04_Outputs", "02_Inputs", "01_Info_Supplied")
OVERRIDES = {"mode": "Mode", "window": "Window", "source": "Source", "bases": "Bases", "credibility": "Credibility"}


def fail(msg):
    print(f"lenai_dev_factors {VERSION}: STOP {msg}")
    raise SystemExit(2)


def short_hash(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]


def self_hash():
    """Hash of this file's text with any BOM removed and CRLF as LF, so a copy written on Windows checks the same."""
    b = Path(__file__).read_bytes().lstrip(b"\xef\xbb\xbf").replace(b"\r\n", b"\n")
    return hashlib.sha256(b).hexdigest()[:16]


def client_of(outputs):
    """The client folder of an outputs path (04_Outputs, or one of its sub-folders), else None."""
    p = Path(outputs).resolve()
    if p.name in OUT_SUBDIRS:
        p = p.parent
    return p.parent if p.name == "04_Outputs" else None


def find_development(build_tools, client):
    here = Path(__file__).resolve().parent
    cands = []
    if build_tools:
        bt = Path(build_tools)
        cands += [bt / "oracle" / "development.py", bt / "development.py"]
    if client:
        cands.append(client / "03_Workflows" / "_Build_tools" / "oracle" / "development.py")
    cands.append(here.parent / "oracle" / "development.py")      # inside a pack: _Build_tools\tools -> \oracle
    for c in cands:
        if c.exists():
            return c
    fail("oracle\\development.py not found: give --build-tools <client>\\03_Workflows\\_Build_tools "
         f"(looked in {', '.join(str(c) for c in cands)})")


def load(path):
    spec = importlib.util.spec_from_file_location("merit_development", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)          # development.py puts its _Build_tools folder on sys.path for layout.py
    return mod


def read_rows(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def safe_dest(dest):
    d = Path(dest).resolve()
    hit = [p for p in d.parts if p in PROTECTED]
    if hit:
        fail(f"--dest {d} is inside {hit[0]}: write the results to another folder (default 07_LenAI)")
    return d


def manifest(LY, outputs):
    p = LY.find_output(outputs, "run_manifest_claims.csv")
    if not p.exists():
        return {}
    return {r["Key"]: r["Value"] for r in read_rows(p) if r.get("Key")}


def cf_selected(DV, LY, outputs):
    """(TPA, basis, measure, lag) -> CF_Used of cf_selected.csv, keyed as development.input_factors keys them."""
    p = LY.find_output(outputs, "cf_selected.csv")
    if not p.exists():
        return None
    out = {}
    for r in read_rows(p):
        try:
            k = (r["TPA"].strip().upper(), r["Basis"].strip().upper(), r["Measure"].strip().title(), int(float(r["Lag"])))
            cf = float(r["CF_Used"])
        except (KeyError, TypeError, ValueError):
            continue
        if k[1] in DV.BASES and k not in out:
            out[k] = cf if 0 < cf <= 1 else 1.0
    return out


def apply_overrides(rows, over):
    if not over:
        return rows
    rows = [dict(r, **over) for r in rows]
    if not any(r.get("TPA", "").strip() == "*" for r in rows):
        rows.append({"TPA": "*", **over})
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--version", action="store_true", help="print the version and the file's check hash, then stop")
    ap.add_argument("--outputs")
    ap.add_argument("--dest")
    ap.add_argument("--build-tools")
    ap.add_argument("--inputs")
    ap.add_argument("--dev")
    for k in OVERRIDES:
        ap.add_argument(f"--{k}")
    ap.add_argument("--tpa", help="comma list of TPAs to keep (blank = all)")
    a = ap.parse_args(argv)
    if a.version:
        print(f"lenai_dev_factors {VERSION} check {self_hash()}")
        return
    if not a.outputs:
        fail("--outputs is required")
    t0 = time.time()

    outputs = Path(a.outputs)
    if not outputs.exists():
        fail(f"--outputs {outputs} not found")
    client = client_of(outputs)
    dev_py = find_development(a.build_tools, client)
    DV = load(dev_py)
    LY = sys.modules["layout"]
    note = [f"lenai_dev_factors {VERSION}; development.py {DV.VERSION} sha256 {short_hash(dev_py)} at {Path(dev_py).resolve()}",
            f"outputs: {outputs.resolve()}"]

    fc, fm = LY.find_output(outputs, "fact_claims.csv"), LY.find_output(outputs, "fact_member_month.csv")
    for p in (fc, fm):
        if not p.exists():
            fail(f"{p.name} not found under {outputs}")
    claims, mm = DV.read_csv(fc), DV.read_csv(fm)
    if a.tpa:
        keep = {t.strip().upper() for t in a.tpa.split(",") if t.strip()}
        claims = [r for r in claims if (r.get("TPA") or "").strip().upper() in keep]
        mm = [r for r in mm if (r.get("TPA") or "").strip().upper() in keep]
        note.append(f"TPAs kept: {', '.join(sorted(keep))}")

    inputs = Path(a.inputs) if a.inputs else (client / "02_Inputs" / LY.INPUTS_XLSX if client else None)
    inputs = inputs if inputs and inputs.exists() else None
    devx = Path(a.dev) if a.dev else (client / "02_Inputs" / LY.DEV_XLSX if client else None)
    devx = devx if devx and devx.exists() else None

    if inputs:
        V, X = DV.run_dates(inputs)
        note.append(f"dates: Run settings of {inputs}")
    else:
        m = manifest(LY, outputs)
        V, X = DV._d(m.get("valuation_date")), DV._d(m.get("claims_extract_date"))
        if V is None or X is None:
            fail("no Merit_INPUTS.xlsx and run_manifest_claims.csv has no valuation_date / claims_extract_date: give "
                 "--inputs")
        note.append("dates: run_manifest_claims.csv (no inputs workbook)")
    note.append(f"valuation date {V}, claims extract date {X}")

    if inputs:
        ucf = DV.input_factors(inputs)
        note.append(f"user factors (CF_Inputs): Development factors tab of {inputs} ({len(ucf)} rows)")
    else:
        ucf = cf_selected(DV, LY, outputs)
        if ucf is None:
            ucf = {}
            note.append("user factors (CF_Inputs): none (no inputs workbook, no cf_selected.csv)")
        else:
            note.append(f"user factors (CF_Inputs): cf_selected.csv CF_Used = the factors this run applied "
                        f"({len(ucf)} rows; no inputs workbook)")

    if devx:
        st, pr = DV.read_settings(devx)
        note.append(f"settings: Settings and Parameters tabs of {devx}")
    else:
        st, pr = [], []
        note.append("settings: Merit defaults (no development workbook): Simple, Source INPUTS, both bases, window 12; "
                    "parameters at their defaults")
    over = {col: str(getattr(a, k)).strip().upper() for k, col in OVERRIDES.items() if getattr(a, k)}
    if over:
        st = apply_overrides(st, over)
        note.append("overrides for every TPA: " + ", ".join(f"{k} = {v}" for k, v in over.items()))

    dest = safe_dest(a.dest if a.dest else (client / LY.LENAI_DIR / time.strftime("%Y%m%d-%H%M_dev_factors")
                                            if client else fail("give --dest (outputs not in a Merit client folder)")))

    d = DV.Dev(claims, mm, st, pr, ucf, V, X)
    T, sf, sb, _rerun = d.compute()
    T = DV.sort_tables(T)
    for n, rows in T.items():
        DV.write_csv(rows, DV.COLS[n], dest / "csv" / f"{n}.csv")
    DV.write_csv(sorted(sf, key=lambda r: (r["TPA"], r["Basis"], r["Measure"], r["Lag"])), DV.STAGE_FACTOR_COLS,
                 dest / "csv" / "would_apply_factors.csv")
    DV.write_csv(sorted(sb, key=lambda r: r["TPA"]), DV.STAGE_BF_COLS, dest / "csv" / "would_apply_bf.csv")
    DV.write_xlsx(T, dest / LY.DEV_OUT_XLSX)

    sev = {}
    for r in T["dev_checks"]:
        sev[r["Severity"]] = sev.get(r["Severity"], 0) + 1
    note.append(f"TPAs: {len(d.tpas)}; findings: " + (", ".join(f"{k} {v}" for k, v in sorted(sev.items())) or "none"))
    note.append(f"results: {dest}")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "RUN_NOTE.txt").write_text("\n".join(note) + "\n", encoding="utf-8")

    # digest (<= 20 lines): the notes, then one line per TPA x basis
    for line in note:
        print(line)
    rows = [r for r in T["dev_tpa"]]
    cf = {(r["TPA"], r["Basis"], r["Lag"]): r for r in T["dev_factors"] if r["Measure"] == "Amount"}
    for r in rows[:8]:
        lags = " ".join(f"{cf[(r['TPA'], r['Basis'], k)]['CF_Derived']:.3f}" if isinstance(
            cf.get((r['TPA'], r['Basis'], k), {}).get("CF_Derived"), float) else "-" for k in range(4))
        print(f"{r['TPA']} {r['Basis']}: Applied {r['Applied']} {r['Reason'] or ''} | CF_Derived lags 0-3: {lags}")
    if len(rows) > 8:
        print(f"... {len(rows) - 8} more TPA x basis rows in dev_tpa.csv")
    print(f"done in {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
```
