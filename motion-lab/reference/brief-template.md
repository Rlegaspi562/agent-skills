# Directed motion brief template

From Florence (@flxrnc), "Opus 5.5 Motion Lab". Fill every line before you press enter. For 3D, add MODEL and CAMERA lines (Prompt B in prompts/prompts.md is this template filled in).

```text
GOAL: what the viewer should feel or do, in one sentence
OUTPUT: one self-contained HTML file (or Remotion, HyperFrames), W x H
TIME: seconds x fps = total frames. Loop: yes or no
LOOK: palette in hex, one accent, typeface + weight + size + tracking
MOTION: easing as cubic-bezier, springs as damping ratio, durations in frames
SHOTS: frame ranges, one hero move per shot, how each shot hands off
BANNED: the defaults you never want to see
QA: stills at named frames, a contact sheet, fix, then the full render
```

Then paste the render contract (render-contract.md) under it.

## How to fill it

- Write GOAL first. If you cannot say in one sentence what the viewer should feel or do, no easing curve will rescue the piece.
- Then TIME, because every other number hangs off the frame count.
- SHOTS is where the story lives: a frame range, one hero move and a handoff per shot (hard cut on the beat, match cut where one shape becomes the next, or a mask wipe). Default to the cut. A transition should be a decision.
- QA makes the model check stills before rendering the whole clip.
- Put the engine in OUTPUT with its numbers, e.g. "A Remotion composition, 1920 x 1080, 30 fps, 450 frames".
- Every style you care about needs a guardrail line saying what may not change (the mascot prompt pins exact voxel proportions).
- Replace adjectives with numbers: "premium" becomes materials, "cool" becomes a lighting setup, "modern" becomes a camera, "animation" becomes beats and springs.

## Hierarchy rules for SHOTS

- One hero per shot. Everything else waits, dims to 40%, or holds still.
- Secondary moves travel 50 to 70% as far as the hero and start 100 to 200 ms after it.
- Ambient motion stays under 5% of the hero's travel, runs on a slow sine and never stops.

## Canvas sizes (pick before the first frame)

1920 x 1080 (16:9), 1080 x 1080 (1:1), 1080 x 1350 (4:5), 1080 x 1920 (9:16). X accepts video between 1:3 and 3:1.
