# PP-0.3 p90_export: checks preintake_recommendations.json (+ preintake_columns_<Gnn>.json parts), writes the two CSVs
import sys, os, json, csv, glob
import hashlib
print("PP-0.3 p90_export h" + hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:4])
out = os.path.join(sys.argv[1], "02_Inputs", "Preintake")
try:
    d = json.load(open(os.path.join(out, "preintake_recommendations.json"), encoding="utf-8-sig"))
    files, cols = d["files"], list(d.get("columns", []))
    for part in sorted(glob.glob(os.path.join(out, "preintake_columns_*.json"))):
        cols += json.load(open(part, encoding="utf-8-sig"))["columns"]
    allowed, required = d["allowed_fields"], d["required_fields"]
except Exception as e:
    print("E-PP01 recommendations file missing, not valid JSON, or a top-level key is absent: %r" % e); sys.exit(1)
errs, warns, role_of = [], [], {}
for f in files:
    g, r = f.get("layout_group", ""), str(f.get("role", "")).lower()
    if f.get("include") == "Y" and r not in allowed:
        errs.append("E-PP02 %s | %s: role must be one of %s" % (f.get("file"), f.get("sheet"), sorted(allowed)))
    if g and role_of.setdefault(g, r) != r:
        errs.append("E-PP02 layout group %s mixes roles" % g)
by_field, mapped = {}, {}
for c in cols:
    g = c.get("layout_group", "")
    if g not in role_of:
        errs.append("E-PP02 column %r: layout group %r is not on any file row" % (c.get("raw_column"), g)); continue
    if not 0 <= float(c.get("confidence", -1)) <= 1:
        errs.append("E-PP04 column %r (%s): confidence must be 0-1" % (c.get("raw_column"), g))
    for fld in c.get("fields", []):
        if fld not in allowed.get(role_of[g], []):
            errs.append("E-PP03 %s: %r -> %r is not a standard field of role %s" % (g, c.get("raw_column"), fld, role_of[g]))
        by_field.setdefault((g, fld), []).append(c.get("raw_column"))
        if float(c.get("confidence", 0)) >= 0.6:
            mapped.setdefault(g, set()).add(fld)
for (g, fld), raws in sorted(by_field.items()):
    if len(raws) > 1:
        warns.append("W-PP05 %s: %d columns feed %r (keep one unless a Date rule or calculation needs both)" % (g, len(raws), fld))
settled = {(x.get("layout_group"), x.get("field")) for x in d.get("fields", []) if x.get("resolved_by") != "MISSING"}
missing = [(g, fld) for g, r in sorted(role_of.items()) for fld in required.get(r, [])
           if fld not in mapped.get(g, set()) and (g, fld) not in settled]
for line in errs + warns:
    print(line)
if errs:
    print("STOP %d error(s): fix the JSON and run this again; no CSV written" % len(errs)); sys.exit(1)
with open(os.path.join(out, "preintake_files.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    keys = ["file", "sheet", "tpa", "role", "include", "header_row", "priority", "claims_status", "scope",
            "date_order", "predicted_status", "layout_group", "rows", "profile_will", "note"]
    w = csv.writer(fh); w.writerow(keys)
    for f in files:
        w.writerow([f.get(k, "") for k in keys])
n = 0
with open(os.path.join(out, "preintake_columns.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["file", "sheet", "layout_group", "raw_column", "recommended_mapped_field", "confidence",
                "profile_proposal", "same_as_profile", "evidence"])
    for f in files:
        for c in cols:
            if c.get("layout_group") == f.get("layout_group") and f.get("layout_group"):
                rec = "; ".join(c.get("fields", []))
                w.writerow([f.get("file"), f.get("sheet"), c["layout_group"], c.get("raw_column"), rec, c.get("confidence"),
                            c.get("profile_proposal", ""), "Y" if rec == c.get("profile_proposal", "") else "N", c.get("evidence", "")])
                n += 1
inc = sum(1 for f in files if f.get("include") == "Y")
print("CTRL sheets=%d include_y=%d layouts=%d column_rows=%d required_unresolved=%d warnings=%d"
      % (len(files), inc, len(role_of), n, len(missing), len(warns)))
for g, fld in missing[:15]:
    print("  unresolved %s %s" % (g, fld))
