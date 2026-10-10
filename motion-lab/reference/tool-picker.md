# Tool picker: HTML vs Remotion vs HyperFrames vs Three.js

From Florence (@flxrnc). Name the engine in the OUTPUT line, or the model chooses for you.

| Need | Engine | Notes from the article |
|---|---|---|
| One idea under 10 s (type, shapes, UI) | Plain HTML/CSS | Zero installs; render.mjs turns it into MP4/GIF |
| Series, template, or data-driven video | Remotion | React components, frame-exact, official Agent Skills (`npx remotion skills add`). Free for individuals and companies up to 3 employees; bigger companies need a company license |
| You think in web pages and GSAP | HyperFrames (HeyGen) | Open source, Apache 2.0 (Apr 17 2026). HTML, CSS, GSAP timelines in, MP4 out via CLI. Needs Node 22+ and FFmpeg. No company-license rule |
| Anything 3D | Three.js | WebGL scenes, lights, materials, shaders. Drive time from frame number, never the clock. Pin the version (the lab pins 0.160.0) |
| Motion inside a live product, not a video | Motion (ex Framer Motion, MIT) or GSAP | Motion has no video renderer. GSAP is now 100% free incl. SplitText, MorphSVG, DrawSVG, ScrollTrigger |

Install commands: reference/setup.md.
