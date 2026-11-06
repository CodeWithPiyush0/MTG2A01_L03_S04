#!/usr/bin/env bash
# Ravi (रवि) and Sona (सोना), the story pages' children (deck page 3: "Visuals: Ravi and Sona") - new round portraits in
# the style of File8's Akash / Moni, generated with Gemini and cut with make_portrait.py (+ the eyes-shut copy for the
# blink). Run from the lesson folder:   bash tools/gen_story_kids.sh     (needs the key in .env and credit on it)
# Until it has run, assets/char_ravi.webp / char_sona.webp are PLACEHOLDERS (the first draft's Aaru / Pari art).
set -e
set -a; . ./.env; set +a; export GEMINI_KEY=${GEMINI_KEY:-$GKEY}
T=$(mktemp -d)
python - "$T" <<'PY'
import sys
from PIL import Image
for n in ("akash", "moni"):
    Image.open(f"../MTG2A01_L03_S03 (File8 Maths)/assets/char_{n}.webp").convert("RGB").save(f"{sys.argv[1]}/ref_{n}.png")
PY
STYLE="Draw in EXACTLY the same children's illustration style as the reference portrait (soft 2D cartoon, big friendly eyes, warm skin shading, clean outlines). Head and shoulders only, facing the viewer, centred, gentle smile. Plain flat solid magenta background (#FF00FF) filling the whole image, no circle, no border, no text, no shadow."
SHUT="Copy this picture exactly - same character, same pose, same colours, same background, same framing - but with both eyes gently CLOSED (a soft curved eyelid line). Change nothing else."
python tools/gen_image.py "$T/ravi.png" "A cheerful 7-year-old Indian boy named Ravi with short neat black hair (no glasses), wearing a yellow-and-blue checked shirt. $STYLE" --ref "$T/ref_akash.png" --aspect 1:1
python tools/gen_image.py "$T/sona.png" "A cheerful 7-year-old Indian girl named Sona with black hair in a single neat ponytail tied with a red ribbon, small gold stud earrings, wearing a light green frock. $STYLE" --ref "$T/ref_moni.png" --aspect 1:1
python tools/gen_char_art.py "$T/ravi.png" "$T/ravi_blink.png" "$SHUT"
python tools/gen_char_art.py "$T/sona.png" "$T/sona_blink.png" "$SHUT"
python tools/make_portrait.py "$T/ravi.png" "$T/ravi_blink.png" assets/char_ravi 227,238,255
python tools/make_portrait.py "$T/sona.png" "$T/sona_blink.png" assets/char_sona 255,236,216
node tools/gen_asset_sizes.js
echo "done - look at assets/char_ravi.webp / char_sona.webp"
