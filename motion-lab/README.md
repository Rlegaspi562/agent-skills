# motion-lab

Make Claude write motion graphics as code (HTML, Remotion, HyperFrames, Three.js) and render them frame-exact to MP4 or GIF: title cards, lower thirds, 9:16 inserts, product shots, animated explainers.

Packaged from "Opus 5.5 Motion Lab: Make Claude Animate Like a Studio" by Florence ([@flxrnc](https://x.com/flxrnc)), Sep 30 2026: https://x.com/flxrnc/status/2105311836190978392. Prompts, numbers and scripts are the author's.

| Path | What it is |
|---|---|
| `SKILL.md` | The workflow: engine, brief, render loop, sound, drop into Descript/Resolve |
| `reference/brief-template.md` | GOAL OUTPUT TIME LOOK MOTION SHOTS BANNED QA |
| `reference/render-contract.md` | The lines to paste under every motion prompt |
| `reference/motion-numbers.md` | Easing, springs, durations, stagger, beat grid, holds, principles as numbers |
| `reference/banned-defaults.md` | The default looks to ban by name |
| `reference/tool-picker.md` | HTML vs Remotion vs HyperFrames vs Three.js vs Motion/GSAP |
| `reference/sound-and-export.md` | Sound sync and loudness, loops, X export limits |
| `reference/fixes.md` | Symptom to fix table plus the debug prompt |
| `reference/setup.md` | Mac and Windows setup, Remotion and HyperFrames commands |
| `scripts/render.mjs` | Playwright frame renderer |
| `scripts/freeze-frame.html` | `?t=` frame freeze snippet |
| `scripts/motion.js` | Motion tokens and closed-form spring |
| `scripts/ffmpeg-commands.sh` | MP4, GIF, contact sheet, loop check, audio mix |
| `prompts/prompts.md` | Every prompt and follow-up from the article, verbatim |
