# PP-0.2 p00_guard: proves the pre-intake profile changed nothing outside 02_Inputs\Preintake
import sys, os, json
import hashlib
print("PP-0.2 p00_guard h" + hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:4])
client, mode = sys.argv[1], sys.argv[2]
out = os.path.join(client, "02_Inputs", "Preintake")
snap_path = os.path.join(out, "guard_snapshot.json")
watch = ["01_Info_Supplied", "02_Inputs", "05_Checks", os.path.join("03_Workflows", "_Build_tools", "specs")]
def scan():
    seen = {}
    for w in watch:
        for root, dirs, files in os.walk(os.path.join(client, w)):
            if os.path.abspath(root).startswith(os.path.abspath(out)):
                continue
            for f in files:
                p = os.path.join(root, f)
                st = os.stat(p)
                seen[os.path.relpath(p, client)] = [st.st_size, st.st_mtime_ns]
    return seen
now = scan()
if mode == "snap":
    os.makedirs(os.path.join(out, "probes"), exist_ok=True)
    json.dump(now, open(snap_path, "w", encoding="utf-8"))
    print("GUARD snapshot files=%d" % len(now))
else:
    old = json.load(open(snap_path, encoding="utf-8"))
    added = sorted(set(now) - set(old)); gone = sorted(set(old) - set(now))
    changed = sorted(k for k in now if k in old and now[k] != old[k])
    if not (added or gone or changed):
        print("GUARD unchanged files=%d" % len(now))
    else:
        print("GUARD CHANGED added=%d removed=%d changed=%d" % (len(added), len(gone), len(changed)))
        for tag, items in (("added", added), ("removed", gone), ("changed", changed)):
            for k in items[:10]:
                print("  %s %s" % (tag, k))
