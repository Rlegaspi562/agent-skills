# Symptom to fix

From Florence (@flxrnc), "When an experiment breaks".

| Symptom | Paste this fix |
|---|---|
| Flicker or jitter | Make every value a pure function of t. Replace Math.random with a seeded generator. Remove timers and CSS transitions. |
| Wrong or fallback font | Load the font with display=block and wait for document.fonts.ready before the first frame. |
| Hiccup at the loop seam | Render frames 0 to N-1 only. Drive the loop from phase = frame / N with whole cycles. |
| Audio drifts off the beat | Compute each beat as n x 60 / BPM and round per beat. Never add a rounded frame count. |
| Jank or dropped frames | Animate only transform and opacity. No width, height, top or left. |
| Banding in the GIF | No gradients. Flat colors only, or dither the palette. |
| Blurry or shimmering text | Snap resting text to whole pixels. Render at 2x and scale down. |
| Text moves before you can read it | Hold every text state 0.3 s per word plus 0.5 s before it moves. |
| Everything moves at once | One hero move at a time. Others start 150 ms later at 60% of its travel. |

If a fix does not hold:

```text
The fix at frame 84 did not hold. Render frames 83 and 85 as PNGs, put them side by side and list every difference you can see. Find the line of code that causes it, fix only that line, then render both frames again.
```
