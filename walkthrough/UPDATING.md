# Updating the walk-through

The video, its captions and the written tour (`README.md`) are all built from one script file, `tour.json`, and the live page. Never edit `README.md`, `captions.vtt` or `captions.srt` by hand; the build overwrites them.

## Change a sentence

1. Open `walkthrough/tour.json` and edit the `"t"` text of a caption. Keep `{figure_names}` in braces where a number belongs; they are filled from the page's own results (`#rel-data` in `index.html`).
2. Rebuild: `python3 walkthrough/make_walkthrough.py` (about 10 minutes; most of it the video encode).
3. Commit the changed files (`walkthrough/walkthrough.mp4`, `captions.vtt`, `captions.srt`, `README.md`, `img/`) on a branch and open a pull request into `main` (the zip route is retired; see CLAUDE.md).

## Add, remove or reorder a shot

Each entry in `"shots"` is one screen. Its caption list `"caps"` is read aloud one caption at a time. Fields: `ch` (chapter number), `yrs` (20 or 40, the Years switch), `scroll` (a CSS selector to bring near the top, or `0`), `dim` (one element to spotlight), `env` (`ref`, `adv` or `st`), `more` (open the "other readings" table), `run` (press "Run it yourself", seed 42), `url` (another page), `hide` (CSS selectors to hide for this shot, such as the v5.2 reading notes when a shot's captions do not concern them), `card` (a full-frame card: `title`, `terminal`, `contribute`, `end`). Add alt text for the written tour under `"alt"`.

## Refresh the figures after the results are regenerated

Nothing to edit: rebuild. Figures in captions come from the page. Each caption's `"needs"` names a condition its wording depends on (for example, "reference confirmed gain" or "adverse wealth worse"); if a regenerated result breaks one, the build stops and names the caption to rewrite. Add a new condition in `CHECKS` in `make_walkthrough.py`.

## The voice

The same synthetic voice as the first walk-through: Kokoro-82M, voice `af_heart`, run locally. Clips are cached in `~/.cache/compassionism-walkthrough/clips/` by what is spoken, so after an edit only the changed captions are voiced again. The `SPOKEN` table in `make_walkthrough.py` says how the voice reads acronyms and file names (for example BU as "B U"). `--silent` builds a captions-only video.

## Needs

Python 3.9+, ffmpeg, and `pip install playwright pillow numpy kokoro-onnx soundfile`, then `python -m playwright install chromium`. The build needs a network connection (fonts, Chart.js, and the voice model on the first run).
