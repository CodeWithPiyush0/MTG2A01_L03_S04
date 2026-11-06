"""MTG2A01_L03_S04 - the lesson, page by page (SME deck MTG2A01_L03_S04_review.pptx).

The one place the content lives: every slide, its on-screen text and its VO lines. Writes
    card.json               - the card (also embedded in index.html, <script id="cardData">)
    tools/vo_script.json    - clip id -> Hindi line, for tools/build_vo.py
and copies index.html to MTG2A01_L03_S04.html (the same game under the skill code's name).

    python tools/lessons.py

Built on MTG2A01_L03_S03's shell (File8: the same flow, layout, buttons, animation, colours, type), with File7's
(MTG2A01_L04_S02) ten-making kit for the regrouping. Lines are the deck's, verbatim, with these slips fixed (CHANGES.md):
page 5 "23 और 18 का जोड़ 42 है" -> 41; page 9 "35 और 25 का जोड़ 43 है" -> 60; page 7 "3 इकाइयाँ है" -> हैं; page 12
"1 इकाइयाँ हैं" -> "1 इकाई हैं".
"""
import json, os, re, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CODE = "MTG2A01_L03_S04"

VO = {}          # clip id -> line


def vo(cid, line):
    if cid in VO and VO[cid] != line:
        raise SystemExit(f"clip {cid} given two different lines")
    VO[cid] = line
    return cid


# ---- shared lines (ids kept from File8 where the words are the same - their clips are reused) ----------------------
vo("vo_landing", "नमस्ते दोस्त! मैं हूँ स्विफ्टी! आज हम ऐसी संख्याओं को जोड़ना सीखेंगे, जिनमें इकाइयों से नई दहाई बनती है।")   # deck page 1
vo("vo_pt_tutorial", "ध्यान से देखिए और मेरे साथ जानिए। चलिए, शुरू करें!")                     # (File8's phase screens)
vo("vo_pt_guided", "बहुत बढ़िया! अब हम साथ मिलकर शुरू करते हैं। चलिए, साथ में करें!")
vo("vo_pt_practice", "वाह! अब आपकी बारी।")
vo("vo_idle_build_t", "अब दहाई बनाइए।"); vo("vo_idle_build_o", "अब इकाई बनाइए।")               # (File8's 7s build reminders)
ASK_PICK = vo("vo_ask_pick", "सही जोड़ चुनिए।")                                                  # deck page 11's VO (also the 7s re-ask)
ASK_TYPE = vo("vo_ask_type", "सही जोड़ टाइप करिए।")                                              # (the 7s re-ask on a keypad page)
TAP = {"tap_o": vo("vo_tap_o", "इकाई पर टैप करके जोड़िए।"), "tap_t": vo("vo_tap_t", "दहाई पर टैप करके जोड़िए।")}   # (File8: 7s idle while blocks are to be tapped down)
H_PICK = vo("vo_h1_pick", "ब्लॉक्स को गिनिए और सही जोड़ चुनिए।")
H_TYPE = vo("vo_h1_type", "ब्लॉक्स को गिनिए और सही जोड़ टाइप करिए।")

CAST = {"रवि": "ravi", "सोना": "sona"}
PEOPLE = [{"who": "ravi", "name": "रवि"}, {"who": "sona", "name": "सोना"}]
NUMS = ["एक", "दो", "तीन", "चार", "पाँच", "छह", "सात", "आठ", "नौ", "दस"]


def split(n):
    return n // 10, n % 10


slides = []

# deck page 2 - 10 इकाइयाँ = 1 दहाई: 13 ones, the first ten counted, ringed, made into a rod by the child, the rod to the tens,
# the three left counted, "13" under the table
slides.append({
    "id": "T1", "phase": "tutorial", "eis": "iconic", "type": "PV_MAKE_TEN", "prompt_hi": "10 इकाइयाँ = 1 दहाई",
    "audio": {"count": vo("vo_t1_count", "यहाँ कुछ ब्लॉक्स हैं। चलिए, इन्हें गिनते हैं—एक, दो, तीन, चार, पाँच, छह, सात, आठ, नौ, दस।"),
              "know": vo("vo_t1_know", "जैसा कि हम जानते हैं, 10 इकाइयाँ मिलकर 1 दहाई बनाती हैं।"),
              "tap": vo("vo_t1_tap", "इस बटन पर टैप करिए और दहाई बनाइए।"),
              "made": vo("vo_t1_made", "बहुत बढ़िया! 10 इकाइयों से 1 दहाई बन गई।"),
              "move": vo("vo_t1_move", "अब इस दहाई को दहाई की जगह पर रखते हैं।"),
              "rest": vo("vo_t1_rest", "अब बाकी ब्लॉक्स गिनते हैं—एक, दो, तीन।"),
              "total": vo("vo_t1_total", "हमारे पास 1 दहाई और 3 इकाइयाँ यानी कुल 13 ब्लॉक्स हैं।")},
    "data": {"n": 13}})

# deck page 3 - "कुल कितने ब्लॉक्स?" Ravi and Sona with their blocks and numbers, 23 / + 18, in sync with the VO (one deck
# line, said as three clips so the pictures can follow it - as File8)
slides.append({
    "id": "T2", "phase": "tutorial", "eis": "iconic", "type": "STORY_ADD", "prompt_hi": "कुल कितने ब्लॉक्स?",
    "audio": {"a": vo("vo_t2s_a", "रवि और सोना ब्लॉक्स से घर बना रहे हैं।"),
              "b": vo("vo_t2s_b", "रवि के पास 23 ब्लॉक्स हैं और सोना के पास 18 ब्लॉक्स हैं।"),
              "ask": vo("vo_t2s_ask", "चलिए पता करते हैं, दोनों के पास मिलाकर कुल कितने ब्लॉक्स हैं?")},
    "data": {"mode": "ask", "a": 23, "b": 18, "people": PEOPLE}})

# deck page 4 - replaced: 23 + 18 in the stacked table: Swiftee builds 23, the child builds 18, moves the ones, makes the ten,
# drags it to the tens (after the ghost drag), moves the tens; 41
slides.append({
    "id": "T3", "phase": "tutorial", "eis": "iconic", "type": "PV_ADD_DEMO", "prompt_hi": "",   # (no heading text - as File8, user 2026-11-06; its line is said)
    "audio": {"head": vo("vo_t3_head", "आइए, 23 और 18 को जोड़ते हैं।"),
              "intro": vo("vo_t2_intro", "सबसे पहले ब्लॉक्स की सहायता से दोनों संख्याएँ बनाते हैं।"),
              "r1": vo("vo_t2_r1", "23 में 2 दहाई और 3 इकाई हैं।"),
              "tens": vo("vo_t2_tens", "पहले 2 दहाई के लिए 2 बंडल रखते हैं।"),
              "ones": vo("vo_t2_ones", "अब 3 इकाई के लिए 3 ब्लॉक रखते हैं।"),
              "r2": vo("vo_t3_r2", "इसी तरह, 18 में 1 दहाई और 8 इकाई हैं।"),
              "build": vo("vo_t3_build", "अब आप ब्लॉक्स की सहायता से 18 बनाइए।"),
              "go": vo("vo_t2_go", "बहुत बढ़िया! अब दोनों संख्याओं को जोड़ते हैं।"),
              "o_add": vo("vo_t2_o_add", "पहले इकाइयों को जोड़ते हैं।"),
              "o_sum": vo("vo_t3_o_sum", "3 इकाई और 8 इकाई मिलाकर हुई, 11 इकाई।"),
              "ten_know": vo("vo_t3_know", "जैसा कि हम जानते है 10 इकाइयाँ मिलकर 1 दहाई बनाती हैं।"),
              "ten_tap": vo("vo_t1_tap", "इस बटन पर टैप करिए और दहाई बनाइए।"),
              "ten_place": vo("vo_t3_place", "नई दहाई को दहाई की जगह रखते है।"),
              "t_add": vo("vo_t2_t_add", "अब दहाइयों को जोड़ते हैं।"),
              "t_sum": vo("vo_t3_t_sum", "2 दहाई, 1 दहाई और 1 नई दहाई मिलाकर हुईं 4 दहाइयाँ।"),
              "total": vo("vo_t3_total", "अब हमारे पास कुल 4 दहाइयाँ और 1 इकाई हैं, यानी 41"),
              "done": vo("vo_t3_done", "शाबाश! 23 और 18 को जोड़ने पर 41 मिलता है।"), **TAP},
    "data": {"a": 23, "b": 18, "demo": True, "idle_hand": True}})

# deck page 5 - replaced: their blocks come together (ten of the ones become a new rod), 23 / + 18 / 41
slides.append({
    "id": "T4", "phase": "tutorial", "eis": "iconic", "type": "STORY_ADD", "prompt_hi": "",   # (no heading - as File8, user 2026-11-06)
    "audio": {"eq": vo("vo_t4_eq", "23 और 18 का जोड़ 41 है।"),                              # (deck: "42" - a slip, 23 + 18 = 41)
              "tot": vo("vo_t4_tot", "रवि और सोना के पास कुल मिलाकर 41 ब्लॉक्स हैं।")},
    "data": {"mode": "sum", "a": 23, "b": 18, "people": PEOPLE}})

# deck page 6: deleted

# deck page 7 (G1) - 28 + 15: the child builds both numbers (rows tapped by themselves), moves the ones, makes the ten, puts it
# in the tens (the ghost only after 5 s idle), moves the tens
slides.append({
    "id": "G1", "phase": "guided", "eis": "iconic", "type": "PV_ADD", "prompt_hi": "संख्याएँ जोड़िए।",
    "audio": {"intro": vo("vo_g1_intro", "पहले ब्लॉक्स की सहायता से दोनों संख्याएँ बनाते हैं।"),
              "r1": vo("vo_g1r_r1", "28 में 2 दहाई और 8 इकाई हैं। ब्लॉक्स की सहायता से 28 बनाइए।"),
              "r2": vo("vo_g1r_r2", "15 में 1 दहाई और 5 इकाई हैं। ब्लॉक्स की सहायता से 15 बनाइए।"),
              "go": vo("vo_g1_go", "बहुत बढ़िया! अब दोनों संख्याओं को जोड़ते हैं।"),
              "o_add": vo("vo_g1_o_add", "पहले इकाइयों को जोड़ते हैं।"),
              "o_sum": vo("vo_g1r_o_sum", "8 इकाई और 5 इकाई मिलाकर हुईं, 13 इकाइयाँ।"),
              "ten_tap": vo("vo_g1r_tap", "10 इकाइयों से 1 दहाई बनती है। इस बटन पर टैप करके दहाई बनाइए।"),
              "ten_place": vo("vo_g1r_place", "नई दहाई को दहाई की जगह रखिए।"),
              "t_add": vo("vo_g1r_t_add", "अब दहाइयों को जोड़िए।"),
              "t_sum": vo("vo_g1r_t_sum", "2 दहाई, 1 दहाई और 1 नई दहाई मिलाकर हुईं 4 दहाइयाँ।"),
              "total": vo("vo_g1r_total", "अब हमारे पास कुल 4 दहाइयाँ और 3 इकाइयाँ हैं, यानी 43"),   # (deck: "…इकाइयाँ है" - हैं)
              "correct": vo("vo_g1r_correct", "शाबाश! 28 और 15 को जोड़ने पर 43 मिलता है।"), **TAP},
    "data": {"a": 28, "b": 15, "build": True, "answer": "none", "idle_hand": True, "place_idle": 5000}})


def pv_add(sid, a, b, answer, text, options=None):
    """deck pages 9, 8, 10: the tables come with a and b built one by one, the "दहाई बनाइए" button there from the start; the
    child moves the ones, makes the ten, puts it in the tens, moves the tens; then the answer - three cards (the sum row moves
    to the middle) or the keypad (typed into the written sum's "?")"""
    s = a + b; st, so = split(s); low = sid.lower()
    pick = answer == "mcq"
    au = {"prompt": vo(f"vo_{low}r_prompt", f"{a} और {b} को जोड़िए।" if pick else f"{a} और {b} को जोड़िए और सही जोड़ टाइप करिए।"),
          "h1": H_PICK if pick else H_TYPE,
          "h2": vo(f"vo_{low}r_h2", f"ध्यान से देखिए, नई दहाई को मिलाकर कुल {st} दहाइयाँ और {so} इकाइयाँ हैं।"),
          "correct": vo(f"vo_{low}r_correct", f"शाबाश! {a} और {b} का जोड़ {s} है।"),
          "reask": ASK_PICK if pick else ASK_TYPE}
    au.update(TAP)
    if pick:
        au["ask"] = vo("vo_ask_pick2", "बहुत बढ़िया! अब सही जोड़ चुनिए।")
    d = {"a": a, "b": b, "build": False, "answer": answer, "prompt2": text, "make_btn": True}
    if options:
        d["options"] = options
    return {"id": sid, "phase": "guided", "eis": "iconic", "type": "PV_ADD", "prompt_hi": text, "audio": au, "data": d}


slides.append(pv_add("G2", 35, 25, "mcq", "संख्याएँ जोड़िए और सही संख्या चुनिए।", [50, 60, 6]))   # deck slide 10 ("page 9"); its "43" a slip - 60
slides.append(pv_add("G3", 46, 26, "mcq", "संख्याएँ जोड़िए और सही जोड़ चुनिए।", [9, 72, 27]))      # deck slide 11 ("page 8")
slides.append(pv_add("G4", 53, 39, "numpad", "संख्याएँ जोड़िए और सही जोड़ टाइप करिए।"))            # deck page 10


def mental(sid, a, b, answer, text, options=None):
    """deck pages 11-13: only the sum, written one under the other; the answer in three cards or typed"""
    s = a + b; st, so = split(s); low = sid.lower(); pick = answer == "mcq"
    au = {"prompt": ASK_PICK if pick else vo(f"vo_{low}r_prompt", f"{a} और {b} को जोड़िए और सही जोड़ टाइप करिए।"),
          "correct": vo(f"vo_{low}r_correct", f"शाबाश! {a} और {b} का जोड़ {s} है।"),
          "reask": ASK_PICK if pick else ASK_TYPE}
    if pick:   # WA1: the tables built + this line; WA2: the blocks merged + "ब्लॉक्स को गिनिए…"; WA3: the right card lit
        au["h1"] = vo("vo_new_ten_q", "ध्यान से देखिए, क्या इकाइयों से नई दहाई बन रही है?")
        au["h2"] = H_PICK
    else:      # WA1: a wiggle; WA2: the blocks built and merged + this line; WA3: the keys in turn
        au["h2"] = vo(f"vo_{low}r_h2", f"ध्यान से देखिए, नई दहाई को मिलाकर कुल {st} दहाइयाँ और {so} {'इकाई' if so == 1 else 'इकाइयाँ'} हैं।")
    d = {"a": a, "b": b, "answer": answer}
    if options:
        d["options"] = options
    return {"id": sid, "phase": "practice", "eis": "symbolic", "type": "MENTAL_ADD", "prompt_hi": text, "audio": au, "data": d}


slides.append(mental("P1", 67, 29, "mcq", "संख्याएँ जोड़िए और सही संख्या चुनिए।", [816, 86, 96]))    # deck page 11
slides.append(mental("P2", 47, 34, "numpad", "संख्याएँ जोड़िए और सही संख्या टाइप करिए।"))           # deck page 12
slides.append(mental("P3", 27, 66, "numpad", "संख्याएँ जोड़िए और सही संख्या टाइप करिए।"))           # deck page 13
# deck page 14: deleted. No game (the deck has none - user 2026-11-06)

# deck page 15 - the end
CEL_VO = vo("vo_cel10", "शाबाश! आपने संख्याओं को जोड़ना सीख लिया, जिनमें इकाइयों से नई दहाई बनती है।")
slides.append({"id": "CEL", "phase": "practice", "eis": "enactive", "type": "CELEBRATION", "prompt_hi": "",
               "audio": {"prompt": CEL_VO},
               "data": {}})

# ---- checks: every sum is the sum it claims to be, and every one needs regrouping (this skill: WITH regrouping) ----
for s_ in slides:
    d = s_["data"]
    if "a" in d:
        a, b = d["a"], d["b"]
        assert a % 10 + b % 10 >= 10 and a + b < 100, f"{s_['id']}: {a}+{b} does not regroup"
    if "options" in d:
        assert d["options"].count(d["a"] + d["b"]) == 1, s_["id"]

phase_n = {}
for s_ in slides:
    phase_n[s_["phase"]] = phase_n.get(s_["phase"], 0) + 1


def clip_len(cid):
    f = os.path.join(ROOT, "assets", "voiceover", cid + ".ogg")
    if not os.path.exists(f):
        return None
    try:
        return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                    capture_output=True, text=True).stdout.strip())
    except Exception:
        return None


def weight(t):
    """a rough spoken length: a number is a word (two digits ~ 7 letters), a pause mark a beat"""
    t = re.sub(r"\d{2,}", "ooooooo", t); t = re.sub(r"\d", "ooo", t)
    return len(re.sub(r"[।,.!?—;]", "oo", t))


def frac(cid, phrase, after=None):
    """where `phrase` starts in clip `cid`, as a share of its length (the 0.28s lead and 0.36s tail of build_vo.py known)"""
    text = VO[cid]; i0 = text.index(after) + len(after) if after else 0
    return frac_at(cid, text.index(phrase, i0))


def frac_at(cid, i):
    text = VO[cid]; dur = clip_len(cid)
    pos = weight(text[:i]) / weight(text)
    if not dur:
        return round(.06 + .88 * pos, 3)
    return round((0.28 + pos * (dur - 0.28 - 0.36)) / dur, 3)


def count_cues(cid, n, after):
    """the number words एक … in a counting line, each one's start"""
    text, out = VO[cid], []
    i = text.index(after) + len(after)
    for w in NUMS[:n]:
        i = text.index(w, i); out.append(frac_at(cid, i)); i += len(w)
    return out


# "शाबाश" only for a first-try right answer (File7/File8): after a wrong one the same line without it
for sl in slides:
    au = sl.get("audio", {})
    if sl["type"] in ("PV_ADD", "MENTAL_ADD") and au.get("correct") and VO[au["correct"]].startswith("शाबाश! ") and sl["data"].get("answer") != "none":
        au["correct_late"] = vo(au["correct"] + "_late", VO[au["correct"]][len("शाबाश! "):])

for sl in slides:
    au, d = sl["audio"], sl["data"]; cues = {}
    if sl["type"] == "PV_MAKE_TEN":
        cues["count"] = count_cues(au["count"], 10, "गिनते हैं")
        cues["rest"] = count_cues(au["rest"], 3, "गिनते हैं")
        cues["total"] = {"t": frac(au["total"], "1 दहाई"), "o": frac(au["total"], "3 इकाइयाँ"), "n": frac(au["total"], "13")}
        cues["tap"] = {"b": frac(au["tap"], "बटन")}
        d["cues"] = cues
        continue
    if "a" not in d:
        continue
    a, b = d["a"], d["b"]; s = a + b
    (at, ao), (bt, bo), (st, so) = split(a), split(b), split(s)
    if sl["type"] == "STORY_ADD":
        names = {}
        for role, cid in au.items():
            txt = VO[cid]; hits = []
            for word, who in CAST.items():
                i = txt.find(word)
                while i >= 0:
                    hits.append([frac(cid, word, after=txt[:i] if i else None), who]); i = txt.find(word, i + 1)
            if hits:
                names[role] = sorted(hits)
        cues["names"] = names
        if "b" in au:
            cues["b"] = {"a": frac(au["b"], str(a)), "b": frac(au["b"], str(b))}
            cues["a"] = {"bld": frac(au["a"], "ब्लॉक्स")}
            cues["ask"] = {"p": frac(au["ask"], "दोनों"), "q": frac(au["ask"], "मिलाकर")}   # the "+", then the line and the "?" boxes
        if "eq" in au:   # "23 और 18 का जोड़ 41 है।"
            cues["eq"] = {"a": frac(au["eq"], str(a)), "op": frac(au["eq"], "और"), "b": frac(au["eq"], str(b)),
                          "eq": frac(au["eq"], "का जोड़"), "n": frac(au["eq"], str(s), after="का जोड़")}
            cues["tot"] = {"n": frac(au["tot"], str(s))}
    if sl["type"] in ("PV_ADD_DEMO", "PV_ADD"):
        if "r1" in au:
            cues["r1"] = {"t": frac(au["r1"], f"{at} दहाई"), "o": frac(au["r1"], f"{ao} इकाई")}
            cues["r2"] = {"t": frac(au["r2"], f"{bt} दहाई"), "o": frac(au["r2"], f"{bo} इकाई")}
            for r_ in ("r1", "r2"):                # "…8 इकाई हैं। ब्लॉक्स की सहायता से…": the glow off as the sentence ends
                if "।" in VO[au[r_]].rstrip("।"):
                    cues[r_]["x"] = frac(au[r_], VO[au[r_]].split("।")[1].strip().split()[0])
        if "go" in au:      # "अब दोनों संख्याओं को जोड़ते हैं।": the "+" on "दोनों", the sum row on "जोड़ते"
            cues["go"] = {"p": frac(au["go"], "दोनों"), "s": frac(au["go"], "जोड़ते")}
        elif "prompt" in au:   # "35 और 25 को जोड़िए।": the "+" on "जोड़िए"
            cues["prompt"] = {"p": frac(au["prompt"], "जोड़िए")}
        if "o_sum" in au:
            cues["o_sum"] = {"a": frac(au["o_sum"], f"{ao} इकाई"), "b": frac(au["o_sum"], f"{bo} इकाई", after="और"),
                             "s": frac(au["o_sum"], f"{ao + bo} इका", after="मिलाकर")}
            cues["t_sum"] = {"a": frac(au["t_sum"], f"{at} दहाई"), "b": frac(au["t_sum"], f"{bt} दहाई", after=f"{at} दहाई"),
                             "n": frac(au["t_sum"], "नई दहाई"), "s": frac(au["t_sum"], f"{st} दहाइयाँ", after="मिलाकर")}
            cues["total"] = {"t": frac(au["total"], f"{st} दहाइयाँ"), "o": frac(au["total"], f"{so} इका"),
                             "n": frac(au["total"], str(s), after="यानी")}
        if "ten_know" in au:
            cues["ten_know"] = {"r": frac(au["ten_know"], "10 इकाइयाँ")}
        if "ten_tap" in au:
            cues["ten_tap"] = {"r": frac(au["ten_tap"], VO[au["ten_tap"]].split()[0]), "b": frac(au["ten_tap"], "इस बटन")}
        for role in ("done", "correct", "correct_late"):
            if role in au:
                cues[role] = {"a": frac(au[role], str(a)), "b": frac(au[role], str(b), after=str(a)),
                              "n": frac(au[role], str(s), after=str(b))}
        if "h2" in au:
            cues["h2"] = {"t": frac(au["h2"], f"{st} दहाइयाँ"), "o": frac(au["h2"], f"{so} इका")}
    if sl["type"] == "MENTAL_ADD":
        if "h2" in au and "दहाइयाँ" in VO[au["h2"]]:
            cues["h2"] = {"t": frac(au["h2"], f"{st} दहाइयाँ"), "o": frac(au["h2"], f"{so} इका")}
        for role in ("correct", "correct_late"):
            if role in au:
                cues[role] = {"a": frac(au[role], str(a)), "b": frac(au[role], str(b), after=str(a)),
                              "n": frac(au[role], str(s), after=str(b))}
    if cues:
        d["cues"] = cues

# the landing follows the greeting word by word: the times (s) of its words in the landing line (estimated from the clip's
# length, re-made on every build): glide = "नमस्ते दोस्त", drop = "मैं हूँ स्विफ्टी" (the blocks), a = "आज हम" (26),
# b = "संख्याओं" (+ 18), q = "जोड़ना" (the line and the "?"), cheer = "सीखेंगे", end = the line's end
LAND = "vo_landing"
_ld = clip_len(LAND)
def _at(phrase):
    return round(frac(LAND, phrase) * _ld, 2) if _ld else None
BEATS = {"glide": 0.28, "drop": _at("मैं हूँ") or 1.3, "a": _at("आज हम") or 2.6, "b": _at("संख्याओं") or 3.2,
         "q": _at("जोड़ना") or 4.0, "cheer": _at("सीखेंगे") or 4.6, "end": round(_ld - 0.36, 2) if _ld else 7.0}

AUDIO_IDS = sorted(set(VO) | {"sfx_celebrate"})
card = {
    "version": "0.2",
    "skill_code": CODE,
    "lo_code": "MTG2A01_L03",
    "grade": "G2",
    "attribute": "A01",
    "skill_type": "CORE",
    "part_label": "",
    "theme": "toybox",
    "title": {"hi": "संख्या जोड़, नई दहाई बनाकर", "en": "Adds vertically with regrouping"},
    # the cover (deck page 1): two children with their blocks, 26 / + 18 / ? written one under the other between them, in
    # step with the greeting. The children are File8's cover children (Rumi & Rohan), walking in side-on as there.
    "landing_hero": {"kind": "pv_story", "people": ["rumi", "rohan"], "build": "addv", "title_look": "wall", "title_paint": "meadow",
                     "walk": True, "pile": False, "start_at": 0, "a": 26, "b": 18, "beats": BEATS,
                     # side: each child's side-view walking puppet (File8's tools/make_walk.py numbers)
                     "kids": [{"who": "rumi", "side": {"h": 0.975, "ar": 0.508, "cut": 0.721, "split": 0.4935, "px": 0.4935, "py": 0.686, "a": 51.6, "bob": 0.0339}},
                              {"who": "rohan", "side": {"h": 0.9766, "ar": 0.44, "cut": 0.7574, "split": 0.4639, "px": 0.4639, "py": 0.7224, "a": 52.3, "bob": 0.0308}}]},
    "skill_description_hi": "दो अंकों की दो संख्याओं को ऊपर-नीचे लिखकर (हासिल के साथ) जोड़ता है: पहले इकाई, 10 इकाइयों से नई दहाई, फिर दहाई।",
    "phase_distribution": phase_n,
    "scaffold_rules": {"nudge_timeout_ms": {"tutorial": 7000, "guided": 7000, "practice": 7000, "independent": 7000},
                       "max_attempts": 3},
    "signals_expected": ["slide_entered", "slide_completed", "pv_build_done", "pv_block_moved", "pv_ten_made", "mcq_correct",
                         "numpad_correct", "mastery_score", "lesson_completed"],
    "assets": {"audio_ext": "ogg", "img_ext": "webp",
               "audio": {k: f"assets/voiceover/{k}.ogg" for k in AUDIO_IDS},
               "audio_text": {k: VO[k] for k in sorted(VO)}},
    "slides": slides,
}

# the celebration Swiftie - File8's (File4's kit sheets), lip-synced to OUR line (the track re-measured on every build)
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("make_lipsync", os.path.join(HERE, "make_lipsync.py")); _ml = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_ml)
_cel = os.path.join(ROOT, "assets", "voiceover", CEL_VO + ".ogg")
_bits, _ms = _ml.lipsync(_cel) if os.path.exists(_cel) else ("0", 25)
card["end_anim"] = {"base": "assets/celebration/", "vo": CEL_VO,
    "meta": {"cols": 6, "frames": 36, "fw": 329, "fh": 440,
             "shabaash": {"src": "cel_shabaash.webp", "pre": [0, 1, 2, 3, 4, 5], "word": list(range(6, 30)), "post": list(range(30, 36))},
             "talk": {"src": "cel_talk.webp", "open": [0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32]},
             "idle": {"src": "cel_idle.webp", "loop": [0, 1, 2, 3, 4, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]}},
    "track": {"bits": _bits, "step_ms": 25, "ms": _ms}}

with open(os.path.join(ROOT, "card.json"), "w", encoding="utf-8") as f:
    json.dump(card, f, ensure_ascii=False, indent=1)
with open(os.path.join(HERE, "vo_script.json"), "w", encoding="utf-8") as f:
    json.dump({k: VO[k] for k in sorted(VO)}, f, ensure_ascii=False, indent=1)

# embed the card in index.html, and keep the page title and the landing's title in step
idx = os.path.join(ROOT, "index.html")
html = open(idx, encoding="utf-8").read()
blob = json.dumps(card, ensure_ascii=False, indent=1)
html, n = re.subn(r'(<script type="application/json" id="cardData">\n).*?(\n</script>)',
                  lambda m: m.group(1) + blob + m.group(2), html, count=1, flags=re.S)
assert n == 1, "cardData block not found in index.html"
html = re.sub(r"<title>.*?</title>", f"<title>SwiftPAL · {card['skill_code']} · {card['title']['hi']}</title>", html, count=1)
open(idx, "w", encoding="utf-8", newline="\n").write(html)
shutil.copyfile(idx, os.path.join(ROOT, CODE + ".html"))
missing = [k for k in sorted(VO) if not os.path.exists(os.path.join(ROOT, "assets", "voiceover", k + ".ogg"))]
print(f"card: {len(slides)} slides {phase_n} · {len(VO)} VO lines · {len(missing)} not rendered yet" + (": " + ", ".join(missing) if missing else ""))
