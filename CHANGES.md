# MTG2A01_L03_S04 — हासिल वाली जोड़ (Adds vertically with regrouping) · change checklist

Source: `MTG2A01_L03_S04_review.pptx` (SME review 1, 17 deck slides = cover + overview + pages 1–15).
Rebuilt on File8's shell (`../MTG2A01_L03_S03 (File8 Maths)` — layout, buttons, animation, colours, type, flow,
phase screens, Swiftee, celebration); the regrouping (make a ten) from File7's kit (`../MTG2A01_L04_S02 (File7 Maths)`).
The SME's first draft (another engine) is kept in `_archive_v1/`.

User decisions (2026-11-06): page 4/5 headings as File8 (none, the line still spoken) · page 10 keypad as the deck
(one answer box, 9 then 2) · Ravi & Sona new portraits (generated) · no game (the deck has none).

Status: ✅ DONE · ⚑ FLAGGED-BACK · ⏳ PENDING · N/C (no change asked)

| # | PPT page | target | change (verbatim / summary) | where | status | proof |
|---|---|---|---|---|---|---|
| 1 | cover | — | title slide | — | N/C | N/C |
| 2 | overview | — | overview / open questions of the old draft (no asks) | — | N/C | N/C |
| 3 | p1 landing | cover | Text: "संख्या जोड़, नई दहाई बनाकर।" | card | ✅ DONE | cover title painted (headless capture land_04) |
| 4 | p1 landing | cover | 26 + 18 = ? (written one under the other) | card | ✅ DONE | 26 / + 18 / ? appear with the greeting; Rumi 26, Rohan 18 blocks |
| 5 | p1 landing | cover | VO: "नमस्ते दोस्त! मैं हूँ स्विफ्टी! आज हम ऐसी संख्याओं को जोड़ना सीखेंगे, जिनमें इकाइयों से नई दहाई बनती है।" | card+VO | ✅ DONE | card vo_landing (clip ⏳ #63) |
| 6 | p2 T1 | make ten | VO1 "यहाँ कुछ ब्लॉक्स हैं। चलिए, इन्हें गिनते हैं—एक … दस।" 13 blocks in Ones; first 10 lit one by one with the count; at 10 outline + show "दहाई बनाइए" | engine+card | ✅ DONE | 13 cubes; first 10 lit one by one on the count cues; ring + button on 'दस' (autoplay T1) |
| 7 | p2 T1 | make ten | VO2 "जैसा कि हम जानते हैं, 10 इकाइयाँ मिलकर 1 दहाई बनाती हैं।" outline kept | card | ✅ DONE | ring kept through vo_t1_know |
| 8 | p2 T1 | make ten | VO3 "इस बटन पर टैप करिए और दहाई बनाइए।" button pulses; on tap 10 blocks come together into 1 rod | engine | ✅ DONE | button pulses on 'बटन'; child tap → 10 stack → 1 rod (autoplay 'make ten') |
| 9 | p2 T1 | make ten | VO4 "बहुत बढ़िया! 10 इकाइयों से 1 दहाई बन गई।" new rod highlighted | engine | ✅ DONE | rod blinks/sweeps on vo_t1_made |
| 10 | p2 T1 | make ten | VO5 "अब इस दहाई को दहाई की जगह पर रखते हैं।" rod moves Ones → Tens | engine | ✅ DONE | rod glides to दहाई (putRod) |
| 11 | p2 T1 | make ten | VO6 "अब बाकी ब्लॉक्स गिनते हैं—एक, दो, तीन।" 3 blocks lit one by one | engine | ✅ DONE | 3 left lit one by one on the count cues |
| 12 | p2 T1 | make ten | VO7 "हमारे पास 1 दहाई और 3 इकाइयाँ यानी कुल 13 ब्लॉक्स हैं।" rod + 3 lit in sync, then the 13 card JUST BELOW the table (not right) | engine | ✅ DONE | rod, cubes beat in sync; 13 card under the table (capture) |
| 13 | p3 T2 story | story | Text "कुल कितने ब्लॉक्स?"; Ravi and Sona with their blocks and numbers | card+art | ✅ DONE | heading 'कुल कितने ब्लॉक्स?'; Ravi/Sona portraits with blocks (art placeholder ⏳ #64) |
| 14 | p3 T2 story | story | VO "रवि और सोना ब्लॉक्स से घर बना रहे हैं। रवि के पास 23 ब्लॉक्स हैं और सोना के पास 18 ब्लॉक्स हैं। चलिए पता करते हैं, दोनों के पास मिलाकर कुल कितने ब्लॉक्स हैं?" | card+VO | ✅ DONE | 3 clips a/b/ask, name + number cues |
| 15 | p3 T2 story | story | equation completes in sync with VO | engine | ✅ DONE | 23, + 18, line + ?? appear on cues |
| 16 | p4 T3 | stacked blocks | replace the slide: heading "आइए, 23 और 18 को जोड़ते हैं।" (said; not shown — as File8, user) | card | ✅ DONE | line said (vo_t3_head), not shown — as File8 (user decision) |
| 17 | p4 T3 | stacked blocks | VO1–VO4: Swiftee builds 23 (row taps in, card, digits lit; 2 rods, 3 blocks via + buttons) | card | ✅ DONE | Swiftee hand + source box builds 2 rods, 3 cubes |
| 18 | p4 T3 | stacked blocks | VO5–VO6: 18 row + card, digits lit; child builds 18 (tens + 1 tap, ones + 8 taps, re-pulse when idle) | card | ✅ DONE | child builds 18 (autoplay: 1 tens tap, 8 ones taps); 7 s re-pulse |
| 19 | p4 T3 | stacked blocks | VO7 "बहुत बढ़िया! अब दोनों संख्याओं को जोड़ते हैं।" buttons go, sum row shows | card | ✅ DONE | src box fades, '+' and sum row on cues |
| 20 | p4 T3 | stacked blocks | VO8 ones tapped down (tens disabled), grey copies stay | card | ✅ DONE | ones tapped down, grey copies stay, tens dimmed |
| 21 | p4 T3 | stacked blocks | VO9 "3 इकाई और 8 इकाई मिलाकर हुई, 11 इकाई।" blocks lit in sync | card | ✅ DONE | blocks beat on cues; nothing written for 11 |
| 22 | p4 T3 | stacked blocks | VO10 "जैसा कि हम जानते है 10 इकाइयाँ मिलकर 1 दहाई बनाती हैं।" outline on 10 blocks | engine | ✅ DONE | ring on '10 इकाइयाँ' |
| 23 | p4 T3 | stacked blocks | VO11 "इस बटन पर टैप करिए और दहाई बनाइए।" "दहाई बनाइए" button appears + pulses; tap → rod | engine | ✅ DONE | 'दहाई बनाइए' appears + pulses; tap → rod (capture z.png) |
| 24 | p4 T3 | stacked blocks | VO12 "नई दहाई को दहाई की जगह रखते है।" rod pulses, target tile in Tens, ghost-drag demo; child drags | engine | ✅ DONE | rod pulses, green target tile, ghost drag with hand, then child drags |
| 25 | p4 T3 | stacked blocks | VO13 "अब दहाइयों को जोड़ते हैं।" tens tapped down, grey copies | card | ✅ DONE | tens tapped down |
| 26 | p4 T3 | stacked blocks | VO14 "2 दहाई, 1 दहाई और 1 नई दहाई मिलाकर हुईं 4 दहाइयाँ।" rods lit in sync | engine | ✅ DONE | row-1, row-2 rods then the new rod + red 1 light, tens digit 4 written |
| 27 | p4 T3 | stacked blocks | VO15 "अब हमारे पास कुल 4 दहाइयाँ और 1 इकाई हैं, यानी 41" rods, blocks, digits, 41 in sync | card | ✅ DONE | rods, cubes, digits, 41 on cues |
| 28 | p4 T3 | stacked blocks | Completion VO "शाबाश! 23 और 18 को जोड़ने पर 41 मिलता है।" | card | ✅ DONE | vo_t3_done, numbers lit |
| 29 | p5 T4 | story sum | replace: images as written, 23 + 18 = 41 | engine | ✅ DONE | blocks fly into one pile; 10 ones form the new rod; 23/+18/41 (capture T4) |
| 30 | p5 T4 | story sum | VO1 "23 और 18 का जोड़ 42 है।" → said as 41 (deck slip: 23 + 18 = 41) | card | ✅ DONE | said as 41 |
| 31 | p5 T4 | story sum | VO2 "रवि और सोना के पास कुल मिलाकर 41 ब्लॉक्स हैं।" blocks + numeral lit in sync | card | ✅ DONE | pile + 41 beat on vo_t4_tot |
| 32 | p6 T5 | book sum | delete | card | ✅ DONE | slide not in card |
| 33 | p7 G1 | 28 + 15 build | Text "संख्याएँ जोड़िए।"; same PV table | card | ✅ DONE | heading 'संख्याएँ जोड़िए।'; same stacked table |
| 34 | p7 G1 | 28 + 15 build | VO1–VO3: rows auto-tapped; child builds 28 then 15 (+ buttons pulse / disable) | card | ✅ DONE | rows auto-lit; + buttons pulse/disable (autoplay G1) |
| 35 | p7 G1 | 28 + 15 build | VO4–VO6: "अब दोनों…", ones tapped down (tens disabled), "8 इकाई और 5 इकाई मिलाकर हुईं, 13 इकाइयाँ।" lit | card | ✅ DONE | '+' on 'दोनों', ones down, sum line cues |
| 36 | p7 G1 | 28 + 15 build | VO7 "10 इकाइयों से 1 दहाई बनती है। इस बटन पर टैप करके दहाई बनाइए।" outline + button; tap → rod | engine | ✅ DONE | ring + button on vo_g1r_tap; tap → rod |
| 37 | p7 G1 | 28 + 15 build | VO8 "नई दहाई को दहाई की जगह रखिए।" target tile; ghost-drag only after 5 s idle | engine | ✅ DONE | target tile; ghost drag only after 5 s idle (data.place_idle 5000, no hand) |
| 38 | p7 G1 | 28 + 15 build | VO9–VO11: tens down, "2 दहाई, 1 दहाई और 1 नई दहाई मिलाकर हुईं 4 दहाइयाँ।", "…4 दहाइयाँ और 3 इकाइयाँ है, यानी 43" | card | ✅ DONE | tens down; t_sum/total cues; 'है'→'हैं' |
| 39 | p7 G1 | 28 + 15 build | Completion "शाबाश! 28 और 15 को जोड़ने पर 43 मिलता है।" | card | ✅ DONE | vo_g1r_correct, numbers lit |
| 40 | p9 (deck slide 10) G2 | 35 + 25 mcq | Text "संख्याएँ जोड़िए और सही संख्या चुनिए।"; tables built one by one; "दहाई बनाइए" from the start; idle hints | engine+card | ✅ DONE | heading verbatim; tables built one by one; greyed button from start; idle: blocks/button pulse, ghost drag (capture G4/G2) |
| 41 | p9 G2 | 35 + 25 mcq | VO1 "35 और 25 को जोड़िए।" VO2 "बहुत बढ़िया! अब सही जोड़ चुनिए।" options 50 / 60 / 6 | card | ✅ DONE | prompt + 'बहुत बढ़िया! अब सही जोड़ चुनिए।', options 50/60/6 |
| 42 | p9 G2 | 35 + 25 mcq | Correct "शाबाश! 35 और 25 का जोड़ 43 है।" → said as 60 (deck slip); answer flies into "?" | card | ✅ DONE | said as 60; card flies into ? |
| 43 | p9 G2 | 35 + 25 mcq | WA1 "ब्लॉक्स को गिनिए और सही जोड़ चुनिए।" WA2 "ध्यान से देखिए, नई दहाई को मिलाकर कुल 6 दहाइयाँ और 0 इकाइयाँ हैं।" WA3 right card lit, others fade | card | ✅ DONE | WA1 vo_h1_pick, WA2 vo_g2r_h2 (columns beat), WA3 right lit + others faded (autoplay --wrong 3) |
| 44 | p8 (deck slide 11) G3 | 46 + 26 mcq | Text "संख्याएँ जोड़िए और सही जोड़ चुनिए।"; as #40; VO1 "46 और 26 को जोड़िए।"; options 9 / 72 / 27 | card | ✅ DONE | heading verbatim; options 9/72/27; vo_g3r_prompt |
| 45 | p8 G3 | 46 + 26 mcq | Correct "शाबाश! 46 और 26 का जोड़ 72 है।"; WA1/WA2 ("…7 दहाइयाँ और 2 इकाइयाँ हैं।")/WA3 | card | ✅ DONE | correct + WA1/WA2/WA3 as #43 |
| 46 | p10 G4 | 53 + 39 keypad | Text "संख्याएँ जोड़िए और सही जोड़ टाइप करिए।"; tables built; "दहाई बनाइए" from start; idle hints | card | ✅ DONE | heading verbatim; greyed button from start; idle hints |
| 47 | p10 G4 | 53 + 39 keypad | VO "53 और 39 को जोड़िए और सही जोड़ टाइप करिए।"; answer counter + hand nudge; tap opens keypad | engine | ✅ DONE | one answer in the written sum's ?? (hand after 7 s), keypad on tap (user decision: as deck) |
| 48 | p10 G4 | 53 + 39 keypad | Correct "शाबाश! 53 और 39 का जोड़ 92 है।" numerals lit in sync | card | ✅ DONE | vo_g4r_correct with numbers lit |
| 49 | p10 G4 | 53 + 39 keypad | WA1 "ब्लॉक्स को गिनिए और सही जोड़ टाइप करिए।" WA2 "…कुल 9 दहाइयाँ और 2 इकाइयाँ हैं।" WA3 keys 9 then 2 lit | engine+card | ✅ DONE | WA1/WA2 lines; WA3 keys 9 then 2 (autoplay: 'guided key 9', 'guided key 2') |
| 50 | p11 P1 | 67 + 29 mcq | Text "संख्याएँ जोड़िए और सही संख्या चुनिए।"; options 816 / 86 / 96; VO "सही जोड़ चुनिए।" | card | ✅ DONE | heading verbatim; options 816/86/96; vo_ask_pick (File8 clip, same words) |
| 51 | p11 P1 | 67 + 29 mcq | Correct "शाबाश! 67 और 29 का जोड़ 96 है।" answer into "?" | card | ✅ DONE | card flies into ? |
| 52 | p11 P1 | 67 + 29 mcq | WA1 tables built + "ध्यान से देखिए, क्या इकाइयों से नई दहाई बन रही है?" | engine+card | ✅ DONE | WA1: tables built + vo_new_ten_q (autoplay --wrong 3) |
| 53 | p11 P1 | 67 + 29 mcq | WA2 blocks move to the third table (options hidden), first two go, sum centred + "ब्लॉक्स को गिनिए और सही जोड़ चुनिए।" | engine | ✅ DONE | WA2: options hidden, merge incl. new ten + red 1, sum row alone, then vo_h1_pick |
| 54 | p11 P1 | 67 + 29 mcq | WA3 right option lit | engine | ✅ DONE | WA3: right card lit, others faded |
| 55 | p12 P2 | 47 + 34 keypad | Text "संख्याएँ जोड़िए और सही संख्या टाइप करिए।"; VO "47 और 34 को जोड़िए और सही जोड़ टाइप करिए।"; answer counter + hand; keypad | card | ✅ DONE | heading verbatim; prompt line; ?? + hand after 7 s; keypad on tap |
| 56 | p12 P2 | 47 + 34 keypad | Correct "शाबाश! 47 और 34 का जोड़ 81 है।" | card | ✅ DONE | vo_p2r_correct |
| 57 | p12 P2 | 47 + 34 keypad | WA1 wiggle · WA2 blocks built + moved to the third row + "…कुल 8 दहाइयाँ और 1 इकाइयाँ हैं।" (said "1 इकाई") · WA3 keys 8 then 1 | engine+card | ✅ DONE | WA1 wiggle only; WA2 merge + line ('1 इकाई'); WA3 keys 8 then 1 (autoplay) |
| 58 | p13 P3 | 27 + 66 keypad | Text "संख्याएँ जोड़िए और सही संख्या टाइप करिए।"; VO "27 और 66 को जोड़िए और सही जोड़ टाइप करिए।" | card | ✅ DONE | heading verbatim; prompt line |
| 59 | p13 P3 | 27 + 66 keypad | Correct "शाबाश! 27 और 66 का जोड़ 93 है।" | card | ✅ DONE | vo_p3r_correct |
| 60 | p13 P3 | 27 + 66 keypad | WA1 wiggle · WA2 blocks + "…कुल 9 दहाइयाँ और 3 इकाइयाँ हैं।" · WA3 keys 9 then 3 | engine+card | ✅ DONE | WA1 wiggle; WA2 merge + line; WA3 keys 9 then 3 (autoplay) |
| 61 | p14 P5 | 48 + 34 | delete | card | ✅ DONE | slide not in card |
| 62 | p15 CEL | celebration | "शाबाश! आपने संख्याओं को जोड़ना सीख लिया, जिनमें इकाइयों से नई दहाई बनती है।" | card+VO | ✅ DONE | vo_cel10 + File8 celebration Swiftie (lip-sync measured on rebuild) |
| 63 | all | voice-over | 55 new lines rendered as audio (Gemini TTS, voice Kore, as File8) | VO | ⏳ PENDING | key returns HTTP 402 "prepayment credits depleted"; lines are in the card, play as silent beats; `python tools/build_vo.py` then `python tools/lessons.py` |
| 64 | p3/p5 | art | Ravi & Sona portraits (user: generate new) | art | ⏳ PENDING | same 402; placeholders = draft's Aaru/Pari art; `bash tools/gen_story_kids.sh` |

## Deck slips fixed (said / shown correctly)
- p5 VO1 "23 और 18 का जोड़ 42 है।" → 41 · p9 (slide 10) correct "35 और 25 का जोड़ 43 है।" → 60
- p7 VO11 "…3 इकाइयाँ है" → हैं · p12 WA2 "1 इकाइयाँ हैं" → "1 इकाई हैं"
- p1 title "संख्या जोड़, नई दहाई बनाकर।" painted without the danda (a title)

## Verification
Headless autoplay of every slide (a bot that taps the pulsing blocks, the + buttons, "दहाई बनाइए", places the rod,
answers): all 12 slides play to the end, **0 console errors**; answer screens re-run with 3 wrong answers first - every
help step fires (G2, G4, P1, P2, P3). Not yet heard with the real voice (#63) - the cue timings are estimates until the
clips exist (`lessons.py` re-measures them from the clips).

## Changed beyond the deck
- The whole game moved from the draft's engine onto File8's shell (the user's instruction) - so a card diff against the
  draft is not meaningful; every slide was rebuilt from the deck.
- File8 behaviours kept that the deck doesn't mention: 7 s idle reminders, "शाबाश" only on a first try, the sum row
  alone + digit badges in the P-hints (File8's soloSum), the walking cover children (Rumi & Rohan).
- Removed: File8's game (no game page), File8-only voice clips and portraits (pruned from assets).

## Observations - noticed, NOT changed
- Deck slide order: "Page 9" (35 + 25) comes before "Page 8" (46 + 26) - built in the deck's slide order.
- G4 / P2 / P3: the deck's "9, then 2" types the tens first; File8 (your direction 2026-10-29) types the ones first
  ("addition always starts from ones"). Built as the deck - say if you want ones-first here too.
- P2/P3 WA1 is a wiggle only (no line), as the deck - the child hears nothing new on the first mistake.
- Register: all आप (टैप करिए / बनाइए) - consistent.
