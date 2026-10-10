---
name: motion-lab
description: >-
  Direct Claude to write motion graphics as code (plain HTML/CSS, Remotion,
  HyperFrames, or Three.js) and render them frame-exact to MP4 or GIF. Use when
  making title cards, lower thirds, 9:16 inserts for Shorts, product shots, or
  animated explainers, or when the user says /motion-lab. Skip when the job is
  copying an edit look from a Reel into DaVinci Resolve presets (that is
  motion-presets) or analyzing why a video went viral (viral-analyze).
user-invocable: true
argument-hint: "[what to animate, canvas, length]"
---

# Motion Lab

Packaged from "Opus 5.5 Motion Lab: Make Claude Animate Like a Studio" by
Florence ([@flxrnc](https://x.com/flxrnc)), X Article, Sep 30 2026:
https://x.com/flxrnc/status/2105311836190978392. All prompts, numbers, tables
and scripts are the author's; this folder only organizes them. Version 0.1.

Core idea: the model does not generate pixels, it writes code that draws each
frame. So replace adjectives with numbers (easing curves, damping ratios, frame
ranges, hex colors, a ban list), then run a render, look, fix loop on stills
and contact sheets.

**Sibling skill:** `motion-presets` = recreate an observed edit look inside
Resolve (Text+, Fusion, Fairlight). **This skill** = generate a new motion clip
from code and drop the MP4 into the edit.

## When this fires

- Title cards, lower thirds, logo stings, 9:16 inserts, product shots,
  animated explainers or loops, made as code and rendered to MP4/GIF.
- The user says `/motion-lab`, "animate this in code", "make a Remotion clip",
  "render a title card".

## 1. Pick the engine

Read `reference/tool-picker.md`. Rule of thumb: one idea under 10 s, plain
HTML. Series, template or data-driven, Remotion. Web pages and GSAP thinking,
HyperFrames. Anything 3D, Three.js. Setup commands: `reference/setup.md`.

## 2. Write the directed brief

Fill `reference/brief-template.md` (GOAL OUTPUT TIME LOOK MOTION SHOTS BANNED
QA, plus MODEL and CAMERA for 3D). Pull numbers from
`reference/motion-numbers.md` and the ban list from
`reference/banned-defaults.md`. Paste `reference/render-contract.md` under it.
For the canvas, pick before the first frame (Shorts: 1080 x 1920).

Worked examples to adapt: `prompts/prompts.md` (liquid chrome title loop,
vague vs directed earbuds product shot, 3D mascot principles loop, all
follow-ups and sound prompts, verbatim). Author's advice for a first run: keep
the numbers, change only the words; on the second run change one number at a
time.

## 3. Render, look, fix

1. `node scripts/render.mjs anim.html <seconds> <fps>` freezes the page at each
   t and saves PNGs to `out/frames`. Set the viewport in the script to your
   canvas (it defaults to 1200 x 675).
2. Paste `scripts/freeze-frame.html` before `</body>` to open any exact frame
   via `anim.html?t=2.5`.
3. Contact sheet, MP4, GIF and loop check: `scripts/ffmpeg-commands.sh`.
4. Review with one or two follow-ups per round from `prompts/prompts.md`
   (stills at frames 0/24/48/72/96, contact sheet hierarchy, onion skin,
   position plot, senior motion designer notes). Notes name frames, not
   feelings. Two to four rounds is normal.
5. Something breaks: `reference/fixes.md`. When a fix works, add it to the
   render contract.

Shared motion tokens and a closed-form spring: `scripts/motion.js`.

## 4. Sound and export

Picture must work muted first. Sound last, scored against frame numbers, each
hit 1 frame after its picture, about -14 LUFS, peak -1 dBTP. Specs, loop rules
and X limits: `reference/sound-and-export.md`.

## 5. Drop into Descript and Resolve

Rumil's edit path is Descript for cuts, then DaVinci Resolve Studio for
graphics, captions and finish; Shorts in 9:16.

- Render at the delivery canvas: 1080 x 1920 for Shorts inserts, 1920 x 1080
  for 16:9. Match the project frame rate in the TIME line so frames map 1:1.
- Export the H.264 MP4 (`-pix_fmt yuv420p -crf 18`) from
  `scripts/ffmpeg-commands.sh`. Keep the PNG sequence in `out/frames` as the
  master if the clip needs a regrade or re-encode.
- Inserts that interrupt the talking head (title cards, explainers, product
  shots) can go in during the Descript cut so pacing is decided with them in
  place. Graphics layered over picture (lower thirds, captions) belong in
  Resolve on a track above the edit.
- Leave sound to Fairlight if the edit already has music and SFX; render the
  clip silent or keep its WAV as a separate stem.
- The article does not cover transparent (alpha) output. For overlays on
  picture, design the clip on a flat background you can key in Resolve, or
  add alpha support as a separate, tested step.
- Run the contrast and hold rules (4.5:1 text, 0.3 s per word plus 0.5 s)
  against the final Resolve frame, since captions may sit on top.

## Guardrails

- Never invent numbers the user or the source did not give; ask or start from
  the cheat sheet.
- Do not post or publish renders without the user asking.
- Credit Florence (@flxrnc) when sharing prompts from `prompts/prompts.md`.
