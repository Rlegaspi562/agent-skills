# Opus 5.5 — $0 launch videos (full course)

- **Status:** shelved (look back / possibly adopt later)
- **Added:** 2026-09-29 PT (Rumil drop)
- **Source:** [@twoclipping](https://x.com/twoclipping) (Zero) — X Article
- **Post:** https://x.com/twoclipping/status/2104446706741825818
- **Article:** https://x.com/i/article/2104355223565197312
- **Title:** How I Make $10K Launch Videos for $0 with Opus 5.5 (Full Course)
- **Snapshot metrics (fetch ~2026-09-29):** ~141k views · 787 likes · 2.3k bookmarks · 60 RTs

## Why it matters

Open-sourced motion-design workflow that turns Claude Code (Opus 5.5) into a mini studio: one HTML file with `seek(t)` draws every frame, Playwright screenshots, ffmpeg stitches MP4. Claims studio-priced launch motion ($5k–$15k) with $0 tooling beyond Claude — no After Effects, no MCP, no paid motion stack.

## Fabinal angle (when we revisit)

Useful for product/OS launch loops, freebie walkthroughs, and polished promo bumpers without a Resolve motion pass. Adjacent to short-form edit craft, but **code-first** (not Descript→Resolve). Prefer 2D warm-white minimal (Apple keynote), not default dark-3D Claude look.

## Workflow (6 steps)

1. **Steal the idea** — feed a reference launch video to Claude; extract ~2 fps contact sheets; map beats, transitions, camera, color, fonts; rewrite for our product. Style push: *2D only, warm white bg, black UI, one accent, Geist/Inter — no 3D/dark/glow/particles.*
2. **Studio setup** — Claude installs ffmpeg + Playwright/Chromium; prove with a 2s spring circle→pill render at 60fps.
3. **Assets (all free)** — Mixkit music + SFX, Pexels media, Google Fonts, plus our screenshots/logo. Ask Claude to download + beat-grid the track and peak-align SFX (real SFX only — synthesized sounds read cheap).
4. **Prompt packs** — three demo film prompts in the article (food-order chat, Apple-keynote print shop, Dribbble UI morph loop). Each asks for inputs → beat map + stills → then full code.
5. **Expensive look rules** — shape morphs not fades; continuous take; hit every music beat; tiny land bounce; one camera move at a time; real click/whoosh SFX; self-check frames before review.
6. **Finalize** — render 60fps + motion blur, place SFX, loudnorm; give director notes (“too slow”, “fade looks cheap → change shape”, “zoom on the drop”), 2–3 rounds.

## Core prompts (keep)

**Reference breakdown**
```
Extract 2 frames per second from reference.mp4 with ffmpeg and put them on contact sheets. Go through them and break the video into beats: what happens on each beat, how each scene turns into the next, the camera moves, the colors and the fonts. Then write the same structure for my product: [your product + link].
```

**Style lock**
```
Style: 2D only. Warm white background, black UI, one accent color, one clean font (Geist or Inter). No 3D, no dark mode, no glows, no particles. Think Apple keynote, not a video game trailer.
```

**Studio bootstrap**
```
Set up a motion design studio in this folder. Install ffmpeg and Playwright with Chromium. Then render a 2 second test where a black circle grows into a pill on a spring, 60fps, and show me the first and last frame.
```

**Asset + beat grid**
```
Download a royalty-free track around 120 BPM with a clear drop from mixkit.co/free-stock-music. Analyze it with numpy and give me the beat grid and the exact time of the drop. Then download one sound effect per event from mixkit.co/free-sound-effects and measure where each one peaks.
```

**Final render**
```
Render the final video in 60fps with motion blur. Put every sound effect exactly on the moment it belongs to, balance the audio, and check every frame for glitches before you show me.
```

Full long-form demo prompts (food chat / print keynote / UI morph) live in the X Article — re-open the post when adopting; too long to mirror here in full.

## Non-goals for this card

- Not queued on Rumil OS Content.
- Not converting into an active skill until Rumil greenlights a test render.
- Ignore the Affiliate Network CTA at the end of the article unless distribution work is separately assigned.

## Next when adopting

1. Pick one Fabinal surface (e.g. Rumil OS feature, Company Brain kit, Skool freebie).
2. Run studio bootstrap + style lock on a throwaway folder.
3. One 10–15s test against a real product screenshot set.
4. Decide keep / tweak / park vs Resolve motion-presets path.
