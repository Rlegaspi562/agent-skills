# Opus 5.5 Motion Lab: make Claude animate like a studio

- **Status:** shelved (look back / possibly adopt later)
- **Added:** 2026-10-10 PT (Rumil drop)
- **Source:** [@flxrnc](https://x.com/flxrnc) (Florence), X Article
- **Post:** https://x.com/flxrnc/status/2105311836190978392
- **Article:** https://x.com/i/article/2105052379590578176
- **Published:** 2026-09-30, 8:00 AM PT
- **Title:** Opus 5.5 Motion Lab: Make Claude Animate Like a Studio
- **Snapshot metrics (fetch 2026-10-10):** about 45.8K views, 213 bookmarks, 66 likes
- **Skill:** packaged as [`motion-lab/`](../../motion-lab/SKILL.md)

## Why it matters

A lab notebook for the part "one prompt" posts skip: three Opus 5.5 animations (liquid chrome title loop, vague vs directed earbuds product shot, 3D voxel mascot) with the exact prompt plus every follow-up, picture and sound. Thesis: the model writes code that paints pixels, so replace adjectives with numbers, then render, look, fix on stills and contact sheets. A 27-word prompt got the default AI look; a 448-word directed prompt plus 15 follow-ups got a studio product film.

## Fabinal angle (when we revisit)

Source for title cards, lower thirds, 9:16 inserts, product shots and short explainers rendered to MP4, then dropped into Descript for the cut and Resolve for finish. More rigorous companion to the @twoclipping card: same code-rendered pipeline, but with a brief template, a number cheat sheet, a fixes table and measured sound sync.

## Key takeaways

1. **Directed brief:** GOAL, OUTPUT, TIME, LOOK, MOTION, SHOTS, BANNED, QA (plus MODEL and CAMERA for 3D). Write GOAL first, then TIME.
2. **Render contract:** one self-contained HTML file, pinned libraries, every frame a pure function of t via `window.renderAt(t)`, no clocks, timers or unseeded random, loops render 0 to N-1.
3. **Numbers over adjectives:** ease-out-expo 0.16,1,0.3,1 for reveals; springs by damping ratio (0.7 to 0.85 premium); words staggered 60 to 120 ms; text holds 0.3 s per word plus 0.5 s; frames per beat = fps x 60 / BPM, rounded per beat.
4. **Ban the defaults by name:** purple/blue gradients, glow, lens flares, decorative particles, everything fading in at once, fade-and-slide-up, centered-everything, text moving while read. Extend after each first render.
5. **Lab loop:** freeze frames by URL (`?t=2.5`), contact sheet of every 12th frame, onion skin, speed graph; one or two frame-numbered notes per round, 2 to 4 rounds.
6. **Engine:** under 10 s plain HTML; series or data-driven Remotion; GSAP thinking HyperFrames; 3D Three.js.
7. **Sound last:** picture must work muted; each hit 1 frame after its picture; -14 LUFS, -1 dBTP; check the 200 Hz to 6 kHz phone band; verify by decoding the MP4, not by ear.
8. **Receipts:** count and post every follow-up (10, 15 and 4 creative follow-ups in the lab).

## Non-goals for this card

- Not queued on Rumil OS Content.
- Prompts and scripts live in the skill folder; do not render anything from this card unless Rumil asks.

## Next when adopting

1. Run the setup in `motion-lab/reference/setup.md` on a throwaway folder.
2. Make one 1080 x 1920 title card or insert from the brief template.
3. Drop it into a real Descript then Resolve edit and decide keep / tweak / park.
