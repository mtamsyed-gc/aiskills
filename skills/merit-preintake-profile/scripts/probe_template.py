# PP-0.2 probe pNN_<what>: <the one question this probe answers>
import sys, os
CLIENT = sys.argv[1]
sys.path.insert(0, os.path.join(CLIENT, "03_Workflows", "_Build_tools"))   # Merit's own modules, for reuse
def mask(v, n=24):
    """Shape of a value: letters -> A, digits -> 9. Use for anything that could identify a person or policy."""
    return "".join("9" if ch.isdigit() else "A" if ch.isalpha() else ch for ch in str(v)[:n])
def top(series, k=8):
    """Category values with counts, only when a column has few distinct values; otherwise shapes."""
    s = series.dropna().astype(str).str.strip()
    vc = s.value_counts()
    if len(vc) <= 25 and len(s) >= 4 * len(vc):
        return "; ".join("%s=%d" % (str(a)[:30], b) for a, b in vc.head(k).items())
    return "shapes: " + "; ".join("%s=%d" % (a, b) for a, b in s.map(mask).value_counts().head(3).items())
# ... open files READ-ONLY, print at most 40 lines, never a data row as it stands ...
