"""Stand-in Hindi VO with edge-tts (Microsoft neural, Indian Hindi) while the Gemini key has no credit - so the animation
can be aligned and synced to real clips. Renders every line of tools/vo_script.json that is not on disk into
assets/voiceover/<id>.ogg, finished exactly as tools/build_vo.py does (pauses pulled in, x1.028, 0.28 s lead / 0.36 s tail,
-18.5 LUFS, Ogg/Opus 48 kHz mono 32 kbps), so the cue timing math in lessons.py holds.

    python tools/build_vo_edge.py                 # the missing ones
    python tools/build_vo_edge.py vo_t1_count     # just these (re-render)
    VO_EDGE_VOICE=hi-IN-MadhurNeural python tools/build_vo_edge.py ...

Then  python tools/lessons.py  (cue times from the clips) and  node tools/gen_asset_sizes.js.
These are PLACEHOLDERS: re-render with Gemini (python tools/build_vo.py --force <ids>) or a VO artist's recordings
(python tools/build_vo.py --from <folder>) before release. Needs internet + ffmpeg.
"""
import asyncio, json, os, sys, tempfile
import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_vo import finish, OUT   # noqa: E402  (the same finishing chain as the Gemini clips)

VOICE = os.environ.get("VO_EDGE_VOICE", "hi-IN-SwaraNeural")
RATE = os.environ.get("VO_EDGE_RATE", "-6%")      # a calm pace for young children


async def render(items, tmp):
    failed = []
    for k, text in items:
        mp3 = os.path.join(tmp, k + ".mp3")
        for attempt in range(3):
            try:
                await edge_tts.Communicate(text, VOICE, rate=RATE).save(mp3)
                finish(mp3, os.path.join(OUT, k + ".ogg"))
                print("ok", k, flush=True); break
            except Exception as e:
                if attempt == 2:
                    failed.append(k); print("FAILED", k, str(e)[:160], flush=True)
                else:
                    await asyncio.sleep(2)
    return failed


def main(args):
    script = json.load(open(os.path.join(HERE, "vo_script.json"), encoding="utf-8"))
    named = [a for a in args if not a.startswith("--")]
    todo = [(k, v) for k, v in script.items() if (k in named) or (not named and not os.path.exists(os.path.join(OUT, k + ".ogg")))]
    if not todo:
        print("VO: nothing to render"); return
    os.makedirs(OUT, exist_ok=True)
    failed = asyncio.run(render(todo, tempfile.mkdtemp(prefix="vo_edge_")))
    print(f"VO ({VOICE}): {len(todo) - len(failed)}/{len(todo)} clips rendered" + (f"; FAILED: {failed}" if failed else ""))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
