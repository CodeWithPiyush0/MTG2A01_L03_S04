# MTG2A01_L03_S04 — संख्या जोड़, नई दहाई बनाकर (Adds vertically with regrouping)

**Grade:** G2 · **LO:** MTG2A01_L03 · **Attribute:** A01 · **Type:** CORE
**Slides:** 12 · Tutorial 4 / Guided 4 / Practice 3 + the celebration
**Source:** `MTG2A01_L03_S04_review.pptx` (SME review 1). Every deck page is mapped in `CHANGES.md`.

## Built on File8's shell
Flow, layout, buttons, animation, colours and type are File8's (`../MTG2A01_L03_S03 (File8 Maths)`, itself on File7's
shell): the meadow cover with the wall title and the walking children, the tutorial card, the header band with Swiftie's
moods, the → button, SFX + music, the three phase screens, confetti, the nudge hand, the stacked दहाई | इकाई table with the
written sum beside it, the + source box, the answer cards and the 3 × 4 keypad, the 7 s reminders, "शाबाश" only on a
first-try answer, the celebration Swiftie. The SME's first draft (another engine) is kept in `_archive_v1/`.

What this skill adds (`app.js` / `style.css`, marked `[pv regroup add]`):
- **making a ten in the stacked table**: the sum row's इकाई cell gets File7's lane (`R.onesBox`, `R.laneRod`), so File7's
  `makeTen` / `ring` / `placeRod` work on it. `PVK.regroup`: the dotted ring round ten ones, the "दहाई बनाइए" button
  (`makeButton` greyed from the start on G2-G4, centred under the table; `childMake`), the new rod dragged to a **target
  tile in the carry row** — the table's head band, no words, taller (`vtable` `carry`, `placeCarry`; it shrinks there; the
  ghost drag with the hand on T3, by itself after 5 s on G1, after 7 s on G2-G4); the child taps it down with the tens.
- **the carried 1 in a green circle** (File8's digit badge) over the first number's tens digit (`W.carry`, `.pv-carry`).
- `autoMove` regroups too (the P1-P3 hint animation); `pvAddSumLine` for "…11 इकाई" (nothing written yet) and
  "…और 1 नई दहाई…" (the new rod and the red 1 light).
- `PV_MAKE_TEN` (page 2): 13 ones, the first ten counted one by one with the VO, ringed, made into a rod by the child,
  moved to the tens, the three left counted, "13" just below the table.
- the story sum (page 5): ten of the 11 ones fly onto the new rod's place and become it.
- the keypad's `cfg.ltr`: the written sum's boxes fill tens first, so the 3rd help lights 9 then 2 (deck pages 10, 12, 13).

## The lesson
| slide | deck | type | what happens |
|---|---|---|---|
| cover | p1 | — | "संख्या जोड़, नई दहाई बनाकर"; Rumi and Rohan walk in, their 26 and 18 drop beside them, 26 / + 18 / ? with the greeting |
| T1 | p2 | PV_MAKE_TEN | 10 इकाइयाँ = 1 दहाई — 13 ones → the child makes a ten → 1 दहाई 3 इकाई = 13 |
| T2 | p3 | STORY_ADD ask | "कुल कितने ब्लॉक्स?" Ravi 23, Sona 18, 23 / + 18 in sync with the VO |
| T3 | p4 | PV_ADD_DEMO | Swiftee builds 23, the child builds 18, ones down (11), make a ten, drag it (ghost demo), tens down → 41 |
| T4 | p5 | STORY_ADD sum | "23 और 18 का जोड़ 41 है।" — their blocks into one pile, ten ones become a rod |
| G1 | p7 | PV_ADD build | 28 + 15: the child builds both, ones (13), make a ten, drag it (ghost only after 5 s idle), tens → 43 |
| G2 | p9 (deck slide 10) | PV_ADD mcq | 35 + 25 (50 / 60 / 6), the button from the start |
| G3 | p8 (deck slide 11) | PV_ADD mcq | 46 + 26 (9 / 72 / 27) |
| G4 | p10 | PV_ADD numpad | 53 + 39 → 92 typed into the written sum (one answer, as the deck) |
| P1 | p11 | MENTAL_ADD mcq | 67 + 29 (816 / 86 / 96); help: tables built → blocks merged with the new ten → the right card lit |
| P2 | p12 | MENTAL_ADD numpad | 47 + 34 → 81; help: wiggle → blocks merged → keys 8, 1 |
| P3 | p13 | MENTAL_ADD numpad | 27 + 66 → 93; help: wiggle → blocks merged → keys 9, 3 |
| CEL | p15 | CELEBRATION | "शाबाश! आपने संख्याओं को जोड़ना सीख लिया, जिनमें इकाइयों से नई दहाई बनती है।" |

Deleted (deck): pages 6 and 14. No game (the deck has none). Every sum regroups (`tools/lessons.py` asserts it).

## Still to do — needs a Gemini key with credit
- **59 VO lines are edge-tts stand-ins** (`hi-IN-SwaraNeural`, `python tools/build_vo_edge.py`) so the animation could be
  synced; 25 more are File8's own clips (identical words). Before release re-render the stand-ins with Gemini
  (`python tools/build_vo.py --force <ids>`) or a VO artist (`--from <folder>`), then `python tools/lessons.py`.
- **Ravi & Sona portraits** are placeholders (the first draft's Aaru / Pari art): `bash tools/gen_story_kids.sh`.

## Rebuilding
```
python tools/lessons.py          # card.json + tools/vo_script.json; embeds the card in index.html, copies MTG2A01_L03_S04.html
python tools/build_vo.py         # renders any VO line not yet on disk (GEMINI_KEY in the environment; ffmpeg)
python tools/lessons.py          # again after new VO: the cue times are measured from the clips
python tools/gen_vo_manifest.py  # lesson_vo_manifest.xlsx (what is still to record)
node tools/gen_asset_sizes.js    # the preload manifest - after ANY asset change
```
The key in `.env` is named `GKEY`: `set -a; . ./.env; set +a; export GEMINI_KEY=$GKEY`.
Recordings made elsewhere: `python tools/build_vo.py --from <folder>` (files named `<Audio ID>.wav`).
Dev: `index.html?slide=N` opens slide N directly; `?dev=1` adds the slide navigator.

## Deploying (Vercel)
As File8: a plain static site; `vercel.json` pins no build and the output directory `.`; `.vercelignore` keeps the dev
files out. The upload is `index.html`, `MTG2A01_L03_S04.html`, `app.js`, `style.css`, `swiftpal-bridge.js`, `vercel.json`, `assets/`.
