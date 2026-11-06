"""The lesson's voice-over manifest - lesson_vo_manifest.xlsx, read from card.json (game order) and the clips on disk.

Sheets:
  VO Manifest     every clip where it is heard, in game order: slide, phase, role, Audio ID, the Hindi script (spoken
                  exactly), duration, status (ON DISK / TO RECORD)
  Recording list  each recording once, with its file name - what a VO artist (or AI Studio) records
A recording goes in with  python tools/build_vo.py --from <folder>  (files named <Audio ID>.wav / .mp3), then
python tools/lessons.py  (the cue times are measured from the clips) and  node tools/gen_asset_sizes.js.

    python tools/gen_vo_manifest.py
"""
import json, os, subprocess
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CARD = json.load(open(os.path.join(ROOT, "card.json"), encoding="utf-8"))
TEXT = CARD["assets"]["audio_text"]
VO_DIR = os.path.join(ROOT, "assets", "voiceover")


def dur(cid):
    f = os.path.join(VO_DIR, cid + ".ogg")
    if not os.path.exists(f):
        return None
    try:
        return round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                          capture_output=True, text=True).stdout.strip()), 2)
    except Exception:
        return None


rows = [("START", "landing", "greeting", "vo_landing")]
for k in ("vo_pt_tutorial", "vo_pt_guided", "vo_pt_practice"):
    rows.append(("PHASE", k[6:], "phase screen", k))
for s in CARD["slides"]:
    for role, cid in s.get("audio", {}).items():
        rows.append((s["id"], s["phase"], role, cid))
for k in ("vo_idle_build_t", "vo_idle_build_o"):
    rows.append(("ANY", "-", "7 s build reminder", k))

wb = Workbook(); ws = wb.active; ws.title = "VO Manifest"
head = ["Slide", "Phase", "Role", "Audio ID", "Hindi script (spoken exactly)", "Duration (s)", "Status"]
ws.append(head)
seen, order = set(), []
for sid, ph, role, cid in rows:
    if cid not in TEXT:
        continue
    d = dur(cid)
    ws.append([sid, ph, role, cid, TEXT[cid], d, "ON DISK" if d else "TO RECORD"])
    if cid not in seen:
        seen.add(cid); order.append(cid)
ws2 = wb.create_sheet("Recording list")
ws2.append(["#", "Audio ID", "File name", "Hindi script (spoken exactly)", "Status"])
todo = 0
for i, cid in enumerate(order, 1):
    st = "ON DISK" if dur(cid) else "TO RECORD"; todo += st == "TO RECORD"
    ws2.append([i, cid, cid + ".wav", TEXT[cid], st])
for w in (ws, ws2):
    for c in w[1]:
        c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1F4E79")
    for col, width in zip("ABCDEFG", (8, 10, 18, 24, 80, 12, 12)):
        w.column_dimensions[col].width = width
    for r in w.iter_rows(min_row=2):
        for c in r:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            if c.value == "TO RECORD":
                c.fill = PatternFill("solid", fgColor="FFE699")
wb.save(os.path.join(ROOT, "lesson_vo_manifest.xlsx"))
print(f"lesson_vo_manifest.xlsx: {len(order)} recordings, {todo} to record")
