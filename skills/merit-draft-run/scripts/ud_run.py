# UD-0.2 ud_run.py - unattended DRAFT run of Merit in a COPY of a client folder (LenAI skill merit-draft-run)
"""Commands (py -B ud_run.py <command> ...):
  setup   <inputs.json>          check the inputs, copy the client folder to a draft folder, snapshot the original;
                                 the draft's raw files keep only the first sample_rows data rows of each sheet
                                 (inputs key sample_rows, default 10000; 0 = every row)
  payer   <WORK>                 write the user's constants and run dates to the Payer tab (after profile)
  set     <WORK> <edits.json>    write judgement cells into the draft's Merit_MAPPING.xlsx; every cell is logged
  show    <WORK> <tab> [--where Col=Value ...] [--blank Col] [--cols A,B,C] [--limit 60]
                                 print rows of a Mapping workbook tab (also _lists: the allowed standards)
  dev     <WORK>                 development factors as the inputs asked (after apply)
  step    <WORK> <name> [--bg]   run one Merit step; names: profile values dry apply ma-extract ma-apply ea-extract
                                 ea-apply workflows   (--bg: start it and return; then poll with status)
  status  <WORK>                 state of the step started with --bg
  results <WORK>                 the run's own checks, the headline by UW year, the decisions count, the guard
  guard   <WORK>                 the original client folder is unchanged since setup
Writes only inside the draft folder it made (marker 02_Inputs\\Draft_run\\DRAFT_RUN.json). Standard library + openpyxl."""
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

VERSION = "UD-0.2"
SUB = Path("02_Inputs") / "Draft_run"
MARK = "DRAFT_RUN.json"
TOOLS = Path("03_Workflows") / "_Build_tools"
MAPPING = Path("02_Inputs") / "Merit_MAPPING.xlsx"
SKIP_DIRS = {"Previous_run", "Baseline", "07_LenAI", "ui_state", "_ui_backup", "__pycache__", "Draft_run"}
EDITABLE = {"Files": ("TPA", "Role", "Header row", "Priority", "Claims status", "Scope", "Include", "Date order",
                      "Split set"),
            "Columns": ("Mapped field", "Type check: accept"), "Fields": ("Constant / rule",),
            "Values": ("Standard value",), "Endorsements": ("Class",), "Claim status": ("Class",),
            "Date rules": ("If type", "Value 1", "Value 2", "Null if"), "Payer": ("Value",)}
DEFAULT_SAMPLE = 10000
HEAD_ROOM = 50                       # rows searched for the header (title lines may sit above it)
BASES = ("user input", "data", "merit proposal", "assist", "guess")
REQUIRED = ("CLIENT", "PAYER", "payer_name", "risk_carrier", "master_cedant_name", "currency", "country",
            "valuation_date", "premium_extract_date", "claims_extract_date", "large_claim_threshold",
            "default_premium_basis")
STEPS = {"profile": ["intake.py", "profile", "{W}", "--payer", "{P}"], "values": ["intake.py", "values", "{W}"],
         "dry": ["intake.py", "apply", "{W}", "--dry-run"], "apply": ["intake.py", "apply", "{W}"],
         "ma-extract": ["mapping_assist.py", "extract", "{W}"],
         "ma-apply": ["mapping_assist.py", "apply", "{W}", "--in-place"],
         "ea-extract": ["endo_assist.py", "extract", "{W}"], "ea-apply": ["endo_assist.py", "apply", "{W}", "--in-place"]}
CHAIN = [("01_Preflight", "Merit_01_Preflight"), ("02_Premium", "Merit_02_Premium"), ("03_Claims", "Merit_03_Claims"),
         ("03b_Development", "Merit_03b_Development"), ("rerun", ""), ("04_Extract", "Merit_04_Extract"),
         ("05_Rate_exposure", "Merit_05_Rate_exposure")]


def die(msg, code=1):
    print(msg)
    sys.exit(code)


def txt(v):
    return "" if v is None else str(v).strip()


def work_of(arg):
    w = Path(arg.strip('"')).resolve()
    if not (w / SUB / MARK).exists():
        die(f"E-UD02 not a draft folder made by 'setup' (no {SUB / MARK}): refusing to work in {w}")
    return w, json.loads((w / SUB / MARK).read_text(encoding="utf-8"))


def scan(root):
    seen = {}
    for d, dirs, files in os.walk(root):
        for f in files:
            p = Path(d) / f
            try:
                st = p.stat()
            except OSError:
                continue
            seen[str(p.relative_to(root))] = [st.st_size, st.st_mtime_ns]
    return seen


def is_date(s):
    try:
        time.strptime(txt(s), "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ------------------------------------------------------------------------------------------------------------- setup
def setup(inputs_path):
    try:
        inp = json.loads(Path(inputs_path.strip('"')).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as e:
        die(f"E-UD01 the inputs file cannot be read as JSON: {e!r}")
    bad = [f"'{k}' is missing" for k in REQUIRED if not txt(inp.get(k))]
    for k in ("valuation_date", "premium_extract_date", "claims_extract_date"):
        if txt(inp.get(k)) and not is_date(inp[k]):
            bad.append(f"'{k}' must be yyyy-mm-dd")
    if txt(inp.get("default_premium_basis")) and txt(inp["default_premium_basis"]) not in ("Net", "Gross"):
        bad.append("'default_premium_basis' must be Net or Gross")
    if txt(inp.get("currency")) and not re.fullmatch(r"[A-Z]{3}", txt(inp["currency"])):
        bad.append("'currency' must be a 3-letter code such as AED")
    try:
        float(str(inp.get("large_claim_threshold", "")).replace(",", ""))
    except ValueError:
        bad.append("'large_claim_threshold' must be a number")
    if txt(inp.get("dev_factors", "INPUTS")) not in ("INPUTS", "DERIVED"):
        bad.append("'dev_factors' must be INPUTS or DERIVED")
    try:
        inp["sample_rows"] = int(str(inp.get("sample_rows", DEFAULT_SAMPLE)).replace(",", "").strip() or DEFAULT_SAMPLE)
        if inp["sample_rows"] < 0:
            raise ValueError
    except ValueError:
        bad.append("'sample_rows' must be a whole number of rows (0 = every row)")
    if txt(inp.get("workflows", "default")) not in ("default", "all"):
        bad.append("'workflows' must be default or all")
    if not isinstance(inp.get("ri_name_by_tpa", {}), dict):
        bad.append("'ri_name_by_tpa' must be an object such as {\"TPA\": \"Reinsurer\"}")
    src = Path(txt(inp.get("CLIENT")).strip('"')).resolve() if txt(inp.get("CLIENT")) else None
    if src is not None:
        raw = src / "01_Info_Supplied"
        n_raw = sum(1 for d, _, fs in os.walk(raw) for f in fs if not f.startswith("_")) if raw.is_dir() else 0
        if not n_raw:
            bad.append(f"no raw files in {raw}")
        if not (src / TOOLS / "intake.py").exists():
            bad.append(f"{src / TOOLS / 'intake.py'} not found: CLIENT must be a Merit client folder")
        if (src / SUB / MARK).exists():
            bad.append("CLIENT is itself a draft folder: give the original client folder")
    if bad:
        die("E-UD01 inputs not usable (nothing was copied):\n  " + "\n  ".join(bad))
    root = Path(txt(inp.get("draft_root")).strip('"')).resolve() if txt(inp.get("draft_root")) else src.parent
    dst, n = root / (src.name + "_DRAFT"), 1
    while dst.exists():
        n += 1
        dst = root / f"{src.name}_DRAFT{n}"
    before = scan(src)
    keep = [r for r in before if not (set(Path(r).parts[:-1]) & SKIP_DIRS)]
    longest = max((len(r) for r in keep), default=0) + len(str(dst)) + 1
    if longest > 250:
        die(f"E-UD03 the draft folder's longest path would be {longest} characters (Windows limit 260): give a shorter "
            f"'draft_root' in the inputs (nothing was copied)")
    t0 = time.time()
    shutil.copytree(src, dst, ignore=lambda d, names: [x for x in names if x in SKIP_DIRS])
    sub = dst / SUB
    (sub / "logs").mkdir(parents=True)
    samp = sample_raw(dst / "01_Info_Supplied", inp["sample_rows"])
    (sub / "sample.json").write_text(json.dumps(samp, indent=1), encoding="utf-8")
    (sub / "backups").mkdir()
    (sub / "source_snapshot.json").write_text(json.dumps(before), encoding="utf-8")
    inp["CLIENT"] = str(src)
    (sub / MARK).write_text(json.dumps({"version": VERSION, "source": str(src), "work": str(dst),
                                        "created": time.strftime("%Y-%m-%d %H:%M"), "inputs": inp}, indent=1),
                            encoding="utf-8")
    with open(sub / "decisions.csv", "w", newline="", encoding="utf-8-sig") as fh:
        csv.writer(fh).writerow(["time", "step", "tab", "row", "column", "old", "new", "basis", "why"])
    mb = sum(before[r][0] for r in keep) / 2 ** 20
    print(f"SETUP ok: {len(keep)} files, {mb:,.1f} MB copied in {time.time() - t0:.0f} s")
    cut = [f for f in samp["files"] if f["cut"]]
    if inp["sample_rows"]:
        print(f"SAMPLE {inp['sample_rows']:,} data rows per sheet: {len(cut)} of {len(samp['files'])} raw file(s) cut; "
              f"{sum(1 for f in samp['files'] if f['how'] == 'copied whole')} copied whole"
              + (f"; NOT cut (kept whole): {', '.join(f['file'] for f in samp['files'] if f['how'].startswith('not cut'))}"
                 if any(f['how'].startswith('not cut') for f in samp['files']) else ""))
    else:
        print("SAMPLE off: every row of every file")
    print(f"WORK={dst}")
    print("Every later command takes WORK. The original client folder is not written to again.")


# ------------------------------------------------------------------------------------------------------ the sample
def sample_raw(raw, n):
    """Cut every raw file of the DRAFT copy to its first n data rows (+ HEAD_ROOM rows for title lines and the
    header). The original folder is never touched. .xlsx: values only, every sheet; .csv: the same encoding, records
    read with the csv module; .parquet: the first n rows. Other formats are copied whole (profile lists them)."""
    out = {"sample_rows": n, "files": []}
    if not n:
        return out
    for p in sorted(x for x in Path(raw).rglob("*") if x.is_file() and not x.name.startswith("_")):
        rec = {"file": str(p.relative_to(raw)), "cut": False, "how": "copied whole"}
        try:
            ext = p.suffix.lower()
            if ext == ".xlsx":
                rec.update(cut_xlsx(p, n))
            elif ext == ".csv":
                rec.update(cut_csv(p, n))
            elif ext == ".parquet":
                rec.update(cut_parquet(p, n))
        except Exception as e:  # noqa: BLE001  a file that cannot be cut stays whole and is reported
            rec["how"] = f"not cut ({type(e).__name__}): kept whole"
        out["files"].append(rec)
    return out


def header_index(first):
    """Index of the header among the first rows: the first row with at least half the cells of the fullest row
    (a title line above the header has one or two cells). Profile finds the header again on the cut file."""
    fill = [sum(1 for v in r if txt(v)) for r in first]
    top = max(fill or [0])
    return next((i for i, f in enumerate(fill) if top and f >= max(2, top / 2)), 0)


def take(rows, n):
    """The rows up to the header and n data rows after it; cut = True when the source had more."""
    out, it = [], iter(rows)
    for r in it:
        out.append(r)
        if len(out) == HEAD_ROOM:
            break
    h = header_index(out)
    out = out[:h + 1 + n] if len(out) > h + 1 + n else out
    for r in it:
        if len(out) == h + 1 + n:
            return out, True
        out.append(r)
    return out, False


def cut_xlsx(p, n):
    from openpyxl import Workbook, load_workbook
    src = load_workbook(p, read_only=True, data_only=True)
    dst, cut, sheets = Workbook(write_only=True), False, {}
    for ws in src.worksheets:
        w = dst.create_sheet(ws.title)
        rows, c = take(ws.iter_rows(values_only=True), n)
        for row in rows:
            w.append(list(row))
        cut = cut or c
        sheets[ws.title] = len(rows)
    src.close()
    tmp = p.with_name(p.stem + "._cut.xlsx")
    dst.save(tmp)
    os.replace(tmp, p)
    return {"cut": cut, "how": "xlsx values, first rows of every sheet", "rows_kept": sheets}


def cut_csv(p, n):
    raw = p.read_bytes()
    for enc in ("utf-8-sig", "cp1256", "latin-1"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    import io
    rows, cut = take(csv.reader(io.StringIO(text, newline="")), n)
    if not cut:
        return {"cut": False, "how": "csv shorter than the sample: unchanged"}
    with open(p, "w", newline="", encoding=enc) as fh:
        csv.writer(fh).writerows(rows)
    return {"cut": True, "how": f"csv first records ({enc})", "rows_kept": len(rows)}


def cut_parquet(p, n):
    import pyarrow as pa
    import pyarrow.parquet as pq
    f = pq.ParquetFile(p)
    if f.metadata.num_rows <= n:
        return {"cut": False, "how": "parquet shorter than the sample: unchanged"}
    batch = next(f.iter_batches(batch_size=n))
    tmp = p.with_name(p.stem + "._cut.parquet")
    pq.write_table(pa.Table.from_batches([batch]), tmp)
    os.replace(tmp, p)
    return {"cut": True, "how": "parquet first rows", "rows_kept": n}


# -------------------------------------------------------------------------------------------- the Mapping workbook
def editable(work):
    try:
        sys.path.insert(0, str(work / TOOLS))
        import intake as IN  # noqa: E402  the pack's own list, so a newer pack's columns are accepted
        return dict(IN.EDITABLE)
    except Exception:  # noqa: BLE001
        return dict(EDITABLE)


def same(cell, want):
    a, b = txt(cell), txt(want)
    if a == b:
        return True
    try:
        return float(a) == float(b)
    except ValueError:
        return a.upper() == b.upper()


def set_cells(work, edits, step):
    from openpyxl import load_workbook
    ed, book = editable(work), work / MAPPING
    if not book.exists():
        die(f"E-UD16 {MAPPING} not found in the draft folder: run 'step profile' first")
    try:
        wb = load_workbook(book)
    except PermissionError:
        die("E-UD15 the draft's Merit_MAPPING.xlsx is open in another program: close it and run this again")
    errs, todo, adds = [], [], []
    for i, e in enumerate(edits, 1):
        tab, where, new = txt(e.get("tab")), e.get("where") or {}, e.get("set") or {}
        tag = f"edit {i} ({tab} {json.dumps(where or e.get('add'), ensure_ascii=False)})"
        if tab not in wb.sheetnames or tab not in ed:
            errs.append(f"E-UD13 {tag}: no editable tab '{tab}'")
            continue
        if txt(e.get("basis")) not in BASES or not txt(e.get("why")):
            errs.append(f"E-UD17 {tag}: 'basis' must be one of {BASES} and 'why' must say what decided it")
        ws = wb[tab]
        head = {txt(c.value): c.column for c in ws[1] if txt(c.value)}
        if e.get("add") is not None:                         # a new row: the Date rules tab only (a TPA without rows)
            row = e["add"]
            ok = ("TPA", "Output") + tuple(ed["Date rules"])
            if tab != "Date rules" or not txt(row.get("TPA")) or not txt(row.get("Output")) or \
                    any(k not in ok for k in row) or any(txt(v).startswith("=") for v in row.values()):
                errs.append(f"E-UD12 {tag}: 'add' is for the Date rules tab only, with TPA, Output and {list(ed['Date rules'])}")
            else:
                adds.append((e, ws, head))
            continue
        miss = [k for k in list(where) + list(new) if k not in head]
        if miss or not where or not new:
            errs.append(f"E-UD12 {tag}: column(s) not on the tab, or 'where' / 'set' empty: {miss}")
            continue
        locked = [k for k in new if k not in ed[tab]]
        if locked:
            errs.append(f"E-UD12 {tag}: not a column the user fills: {locked} (editable: {list(ed[tab])})")
        if any(txt(v).startswith("=") for v in new.values()):
            errs.append(f"E-UD14 {tag}: a formula is not accepted as a value")
        rows = [r for r in range(2, ws.max_row + 1)
                if all(same(ws.cell(row=r, column=head[k]).value, v) for k, v in where.items())]
        if not rows:
            errs.append(f"E-UD10 {tag}: no row matches")
        elif len(rows) > 1 and not e.get("all"):
            errs.append(f"E-UD11 {tag}: {len(rows)} rows match; narrow 'where' or add \"all\": true")
        todo.append((e, ws, head, rows))
    if errs:
        wb.close()
        die("\n".join(errs) + f"\nSTOP {len(errs)} error(s): nothing was written; fix the edits file and run it again")
    n_bak = len(list((work / SUB / "backups").glob("*.xlsx"))) + 1
    shutil.copy2(book, work / SUB / "backups" / f"Merit_MAPPING_{n_bak:03d}_before_{step}.xlsx")
    log, tabs = [], set()
    for e, ws, head, rows in todo:
        for r in rows:
            key = " | ".join(f"{k}={txt(v)}" for k, v in e["where"].items())
            for k, v in e["set"].items():
                c = ws.cell(row=r, column=head[k])
                if txt(c.value) == txt(v):
                    continue
                log.append([time.strftime("%Y-%m-%d %H:%M:%S"), step, e["tab"], key, k, txt(c.value), txt(v),
                            e["basis"], txt(e["why"])[:300]])
                c.value = v
                tabs.add(e["tab"])
    for e, ws, head in adds:
        r = ws.max_row + 1
        for k, v in e["add"].items():
            if txt(v):
                ws.cell(row=r, column=head[k]).value = v
        log.append([time.strftime("%Y-%m-%d %H:%M:%S"), step, e["tab"], f"TPA={txt(e['add'].get('TPA'))} | Output="
                    f"{txt(e['add'].get('Output'))}", "(new row)", "", json.dumps(e["add"], ensure_ascii=False),
                    e["basis"], txt(e["why"])[:300]])
        tabs.add(e["tab"])
    try:
        wb.save(book)
    except PermissionError:
        die("E-UD15 the draft's Merit_MAPPING.xlsx is open in another program: close it and run this again")
    with open(work / SUB / "decisions.csv", "a", newline="", encoding="utf-8-sig") as fh:
        csv.writer(fh).writerows(log)
    total = sum(1 for _ in open(work / SUB / "decisions.csv", encoding="utf-8-sig")) - 1
    print(f"SET {len(log)} cell(s) on {sorted(tabs) or 'no tab (already as asked)'}; decisions logged so far: {total}")


def show(work, a):
    from openpyxl import load_workbook
    tab, opts = a[0], a[1:]
    wb = load_workbook(work / MAPPING, read_only=True, data_only=True)
    if tab not in wb.sheetnames:
        die(f"E-UD13 no tab '{tab}'; tabs: {wb.sheetnames}")
    rows = [r for r in wb[tab].iter_rows(values_only=True) if r and any(txt(v) for v in r)]
    wb.close()
    if not rows:
        die(f"tab '{tab}' is empty")
    if tab == "_lists":                                      # the dropdown lists, one per column, no header row
        for i in range(max(len(r) for r in rows)):
            vals = [txt(r[i]) for r in rows if i < len(r) and txt(r[i])]
            if vals:
                print(f"list {i + 1} ({len(vals)}): " + "; ".join(v[:64] for v in vals[:80]))
        return
    head = [txt(h) or f"col{i + 1}" for i, h in enumerate(rows[0])]
    where = [o.split("=", 1) for o in (opts[i + 1] for i, x in enumerate(opts[:-1]) if x == "--where") if "=" in o]
    blank = [opts[i + 1] for i, x in enumerate(opts[:-1]) if x == "--blank"]
    cols = next((opts[i + 1].split(",") for i, x in enumerate(opts[:-1]) if x == "--cols"), head)
    limit = int(next((opts[i + 1] for i, x in enumerate(opts[:-1]) if x == "--limit"), 60))
    cols = [c.strip() for c in cols if c.strip() in head]
    data = [dict(zip(head, r)) for r in rows[1:]] if tab != "README" else [{head[0]: r[0]} for r in rows]
    keep = [d for d in data if all(same(d.get(k), v) for k, v in where) and all(not txt(d.get(k)) for k in blank)]
    print(f"{tab}: {len(keep)} of {len(data)} row(s)" + (f", first {limit} shown" if len(keep) > limit else ""))
    print(" | ".join(cols))
    for d in keep[:limit]:
        print(" | ".join(txt(d.get(c))[:44] for c in cols))


def payer(work, mark):
    i = mark["inputs"]
    vals = {"Payer Name": i["payer_name"], "Risk Carrier": i["risk_carrier"], "MasterCedantName": i["master_cedant_name"],
            "Currency": i["currency"], "Country": i["country"], "Default premium basis": i["default_premium_basis"],
            "Valuation date": i["valuation_date"], "Premium extract date": i["premium_extract_date"],
            "Claims extract date": i["claims_extract_date"], "Large claim threshold": i["large_claim_threshold"]}
    if i.get("ri_name_by_tpa"):
        vals["RI name by TPA"] = json.dumps(i["ri_name_by_tpa"])
    if txt(i.get("sme_max_lives")):
        vals["SME max lives"] = i["sme_max_lives"]
    vals.update(i.get("payer_tab_extra") or {})
    set_cells(work, [{"tab": "Payer", "where": {"Key": k}, "set": {"Value": v}, "basis": "user input",
                      "why": "given by the user at the start of the run"} for k, v in vals.items()], "payer")


def dev(work, mark):
    want = txt(mark["inputs"].get("dev_factors", "INPUTS"))
    if want != "DERIVED":
        print("DEV factors = INPUTS (the inputs workbook's factors; a new client has none, so factor 1 and no IBNR)")
        return
    from openpyxl import load_workbook
    p = work / "02_Inputs" / "Merit_DEVELOPMENT.xlsx"
    if not p.exists():
        die("E-UD18 Merit_DEVELOPMENT.xlsx not found: intake apply writes it; run 'step apply' first")
    wb, log = load_workbook(p), []
    for sheet, key_col, key, col, val in (("Settings", "TPA", "*", "Source", "DERIVED_ELSE_INPUTS"),
                                          ("Parameters", "Parameter", "review_unattended", "Value", "APPLY")):
        ws = wb[sheet]
        head = {txt(c.value): c.column for c in ws[1] if txt(c.value)}
        rows = [r for r in range(2, ws.max_row + 1) if txt(ws.cell(row=r, column=head[key_col]).value) == key]
        if len(rows) != 1:
            die(f"E-UD18 Merit_DEVELOPMENT.xlsx, {sheet}: expected one row '{key}', found {len(rows)}; nothing written")
        c = ws.cell(row=rows[0], column=head[col])
        log.append([time.strftime("%Y-%m-%d %H:%M:%S"), "dev", f"DEVELOPMENT {sheet}", key, col, txt(c.value), val,
                    "user input", "dev_factors = DERIVED in the inputs"])
        c.value = val
    wb.save(p)
    with open(work / SUB / "decisions.csv", "a", newline="", encoding="utf-8-sig") as fh:
        csv.writer(fh).writerows(log)
    print("DEV factors = DERIVED: every TPA DERIVED_ELSE_INPUTS, applied without the review gate (unattended)")


# ------------------------------------------------------------------------------------------------------------- steps
def commands(work, mark, name):
    py, bt = [sys.executable, "-B"], work / TOOLS
    if name in STEPS:
        a = [x.replace("{W}", str(work)).replace("{P}", mark["inputs"]["PAYER"]) for x in STEPS[name]]
        return [(name, py + [str(bt / a[0])] + a[1:], None)]
    if name != "workflows":
        die(f"E-UD20 unknown step '{name}'")
    every = mark["inputs"].get("workflows", "default") == "all"
    launcher = work / "00_Start_Here" / "steps" / "05_Run_workflows.cmd"
    if os.name == "nt" and launcher.exists() and "--direct" not in sys.argv:
        return [("05_Run_workflows.cmd", ["cmd", "/c", str(launcher), "nopause", "diag"] +
                 (["select", "1-6"] if every else []), None)]
    out = []
    for d, stem in CHAIN:                                    # the launcher's chain, tool by tool (no .cmd available)
        if d == "04_Extract" and not every:
            continue
        if d == "rerun":
            out.append(("dev_review", py + [str(bt / "dev_review.py"), str(work), "--unattended"], None))
            out.append(("RERUN?", None, None))
            continue
        p = work / "03_Workflows" / d / f"{stem}.yxmd"
        if p.exists():
            out.append((stem, py + [str(bt / "merit_native.py"), str(p)], str(p.parent)))
    o = str(work / "04_Outputs")
    out += [("diagnostics", py + [str(bt / "oracle" / "diagnostics.py"), "--outputs", o, "--inputs",
                                  str(work / "02_Inputs")], None),
            ("headline", py + [str(bt / "headline.py"), "--outputs", o], None),
            ("checks_guide", py + [str(bt / "checks_guide.py"), "--outputs", o], None)]
    return out


def run_step(work, mark, name):
    logs = work / SUB / "logs"
    log = logs / f"{len(list(logs.glob('*.log'))) + 1:02d}_{name}.log"
    state = work / SUB / "state.json"
    st = {"step": name, "log": str(log), "started": time.time(), "pid": os.getpid(), "exit": None}
    state.write_text(json.dumps(st), encoding="utf-8")
    rc = 0
    with open(log, "w", encoding="utf-8", errors="replace") as fh:
        for label, cmd, cwd in commands(work, mark, name):
            if label == "RERUN?":
                m = work / "04_Outputs" / "stage" / "Merit_stage_dev_rerun.csv"
                if m.exists() and "RERUN,1" in m.read_text(encoding="utf-8", errors="replace"):
                    p = work / "03_Workflows" / "03_Claims" / "Merit_03_Claims.yxmd"
                    label, cmd, cwd = "Merit_03_Claims (second pass)", [sys.executable, "-B",
                                                                         str(work / TOOLS / "merit_native.py"), str(p)], str(p.parent)
                else:
                    continue
            fh.write(f"\n===== {label} =====\n")
            fh.flush()
            r = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT, cwd=cwd, stdin=subprocess.DEVNULL)
            fh.write(f"\n===== {label} exit {r.returncode} =====\n")
            rc = max(rc, r.returncode)
            if r.returncode >= (2 if name == "workflows" and label != "05_Run_workflows.cmd" else 1):
                break
    st.update(exit=rc, seconds=round(time.time() - st["started"], 1))
    state.write_text(json.dumps(st), encoding="utf-8")
    return st


def summary(st):
    lines = Path(st["log"]).read_text(encoding="utf-8", errors="replace").splitlines()
    codes = {}
    for ln in lines:
        for c in set(re.findall(r"\b([SFQWEI]-[A-Z][A-Z0-9-]+)\b", ln)):
            codes[c] = codes.get(c, 0) + 1
    mean = {0: "OK", 1: "STOP or data warnings", 2: "errors", 3: "stopped at a prompt", 4: "CRASH (not a mapping problem)"}
    print(f"STEP {st['step']} exit {st['exit']} ({mean.get(st['exit'], '?')}) in {st.get('seconds', 0):,.0f} s; log {st['log']}")
    for ln in [x for x in lines if x.startswith("RESULT:")][-1:]:
        print(ln[:300])
    stops = [x for x in lines if x.startswith("! ")]              # apply / values: the stops; profile: its flags
    for ln in stops[:30]:
        print(ln[:400])
    if len(stops) > 30:
        print(f"... {len(stops) - 30} more '!' line(s) in the log")
    if codes:
        print("codes seen: " + ", ".join(f"{k} x{v}" for k, v in sorted(codes.items())))
    if st["exit"] not in (0,) and not stops:
        print("last lines:")
        for ln in lines[-12:]:
            print("  " + ln[:300])


def step(work, mark, name, bg):
    if name not in STEPS and name != "workflows":
        die(f"E-UD20 unknown step '{name}'")
    if not bg:
        summary(run_step(work, mark, name))
        return
    flags = 0x08000000 | 0x00000200 if os.name == "nt" else 0          # no window, own process group: survives this call
    extra = ["--direct"] if "--direct" in sys.argv else []
    subprocess.Popen([sys.executable, "-B", str(Path(__file__).resolve()), "_child", str(work), name] + extra,
                     stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                     creationflags=flags, start_new_session=os.name != "nt")
    print(f"STARTED {name} in the background. Poll:  status \"{work}\"  (about once a minute)")


def status(work):
    p = work / SUB / "state.json"
    if not p.exists():
        die("no step has been started")
    st = json.loads(p.read_text(encoding="utf-8"))
    if st["exit"] is not None:
        print("FINISHED")
        summary(st)
        return
    lines = Path(st["log"]).read_text(encoding="utf-8", errors="replace").splitlines() if Path(st["log"]).exists() else []
    print(f"RUNNING {st['step']} for {time.time() - st['started']:,.0f} s; last lines of the log:")
    for ln in lines[-6:]:
        print("  " + ln[:200])


# ----------------------------------------------------------------------------------------------------------- results
def rows_of(p):
    if not Path(p).exists():
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def num(x):
    try:
        return float(str(x).replace(",", ""))
    except (TypeError, ValueError):
        return 0.0


def guard(mark):
    src = Path(mark["source"])
    old = json.loads((Path(mark["work"]) / SUB / "source_snapshot.json").read_text(encoding="utf-8"))
    now = scan(src)
    diff = sorted(set(now) ^ set(old)) + sorted(k for k in now if k in old and now[k] != old[k])
    line = f"GUARD original unchanged files={len(now)}" if not diff else f"GUARD ORIGINAL CHANGED files={len(diff)}"
    print(line)
    for k in diff[:10]:
        print("  " + k)
    return line


def results(work, mark):
    o, res = work / "04_Outputs", {}
    ap = work / "02_Inputs" / "intake_apply.json"
    man = json.loads(ap.read_text(encoding="utf-8")) if ap.exists() else {}
    res["apply"] = {"done": bool(man) and not man.get("stops"), "stops": len(man.get("stops", [])),
                    "flags": len(man.get("flags", [])), "new_formats": len(man.get("new_formats", [])),
                    "sources": len(man.get("sources", []))}
    exc = [r for f in ("exceptions.csv", "exceptions_claims.csv", "diagnostics.csv") for r in rows_of(o / "csv" / f)]
    sev = {}
    for r in exc:
        k = (str(r.get("Severity", "")).capitalize(), r.get("Code", ""))
        sev[k] = sev.get(k, 0) + 1
    res["stop_codes"] = sorted({c for (s, c) in sev if s == "Stop"})
    res["flag_codes"] = len({c for (s, c) in sev if s == "Flag"})
    pr, cr = rows_of(o / "csv" / "recon_premium.csv"), rows_of(o / "csv" / "recon_claims.csv")
    res["premium_fandiff_max"] = max([abs(num(v)) for r in pr for k, v in r.items() if k and k.startswith("FanDiff")] + [0.0])
    res["claims_tieout_max"] = max([abs(num(r.get("payer_share_in")) - num(r.get("paid_in")) - num(r.get("os_in")))
                                    for r in cr] + [0.0])
    mr = {r.get("TPA", "?"): num(r.get("match_rate_amount")) for r in cr if r.get("match_rate_amount") not in (None, "")}
    res["match_rate_by_tpa"] = {k: round(v, 4) for k, v in mr.items()}
    res["workflows_ran"] = (o / "csv" / "dim_life.csv").exists() and (o / "csv" / "fact_claims.csv").exists()
    dec = rows_of(work / SUB / "decisions.csv")
    by = {}
    for r in dec:
        by[r["basis"]] = by.get(r["basis"], 0) + 1
    res["decisions"] = {"cells": len(dec), "by_basis": by}
    res["guard"] = guard(mark)
    sp = work / SUB / "sample.json"
    sm = json.loads(sp.read_text(encoding="utf-8")) if sp.exists() else {"sample_rows": 0, "files": []}
    res["sample"] = {"rows_per_sheet": sm["sample_rows"], "files_cut": sum(1 for f in sm["files"] if f["cut"]),
                     "files": len(sm["files"])}
    head = o / "xlsx" / "Merit_Headline.xlsx"
    table = []
    if head.exists():
        from openpyxl import load_workbook
        wb = load_workbook(head, read_only=True, data_only=True)
        if "By UW year" in wb.sheetnames:
            table = [[("" if v is None else v) for v in r] for r in wb["By UW year"].iter_rows(values_only=True)
                     if r and any(v is not None for v in r)]
        wb.close()
    (work / SUB / "results.json").write_text(json.dumps(dict(res, headline_by_uw_year=table), indent=1, default=str),
                                             encoding="utf-8")
    print(f"APPLY done={res['apply']['done']} stops={res['apply']['stops']} flags={res['apply']['flags']} "
          f"sources={res['apply']['sources']} new_layouts={res['apply']['new_formats']}")
    print(f"WORKFLOWS ran={res['workflows_ran']} stop_codes={res['stop_codes'] or 'none'} flag_codes={res['flag_codes']}")
    print(f"CHECKS premium_fandiff_max={res['premium_fandiff_max']:.4f} claims_tieout_max={res['claims_tieout_max']:.4f} "
          f"match_rate_min={round(min(mr.values()), 4) if mr else 'n/a'} (gate 0.95) by_tpa={res['match_rate_by_tpa']}")
    if sm["sample_rows"]:
        print(f"SAMPLE rows_per_sheet={sm['sample_rows']} files_cut={res['sample']['files_cut']} of "
              f"{res['sample']['files']}: the figures below are on the SAMPLE, not the portfolio (exposure, claims, "
              "match rates and loss ratios are not representative)")
    print(f"DECISIONS cells={len(dec)} " + " ".join(f"{k.replace(' ', '_')}={v}" for k, v in sorted(by.items())))
    print("HEADLINE by UW year (aggregates; from Merit_Headline.xlsx):" if table else "HEADLINE not written")
    for r in table[:14]:
        print("  " + " | ".join(f"{v:,.2f}" if isinstance(v, float) else str(v) for v in r[:11]))
    print(f"results.json and decisions.csv are in {work / SUB}")


def main(a):
    for st_ in (sys.stdout, sys.stderr):                    # a console that cannot show a character must not stop a step
        try:
            st_.reconfigure(errors="replace")
        except (AttributeError, ValueError):
            pass
    here = Path(__file__).resolve()
    print(f"{VERSION} ud_run h{hashlib.sha256(here.read_bytes()).hexdigest()[:4]}")
    if len(a) < 2:
        die(__doc__)
    if a[0] == "setup":
        return setup(a[1])
    work, mark = work_of(a[1])
    if a[0] == "payer":
        payer(work, mark)
    elif a[0] == "set" and len(a) > 2:
        try:
            d = json.loads(Path(a[2].strip('"')).read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as e:
            die(f"E-UD19 the edits file cannot be read as JSON: {e!r}")
        set_cells(work, d.get("edits", []), txt(d.get("step")) or "set")
    elif a[0] == "show" and len(a) > 2:
        show(work, a[2:])
    elif a[0] == "dev":
        dev(work, mark)
    elif a[0] == "step" and len(a) > 2:
        step(work, mark, a[2], "--bg" in a)
    elif a[0] == "_child" and len(a) > 2:
        run_step(work, mark, a[2])
    elif a[0] == "status":
        status(work)
    elif a[0] == "results":
        results(work, mark)
    elif a[0] == "guard":
        guard(mark)
    else:
        die(__doc__)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except BrokenPipeError:                                  # the output was piped into something that stopped reading
        sys.exit(0)
