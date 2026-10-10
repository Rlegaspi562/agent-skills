# The render contract

Paste it under any motion prompt so every frame can be rendered, checked and fixed. Verbatim from Florence (@flxrnc).

```text
Output one self-contained HTML file. Only the libraries the prompt names, pinned to a version.
No network requests except fonts and those pinned libraries.
Every frame must be a pure function of time t, in seconds.
If JavaScript drives any motion, expose window.renderAt(t) that draws exactly that frame.
Animate with CSS keyframes, the Web Animations API, SVG, Canvas 2D or WebGL.
No Date.now, no setTimeout or setInterval starts, no unseeded Math.random.
Loops: render frames 0 to N-1 only, and frame N-1 must flow into frame 0.
```

Why each line exists:

- A clock or a timer makes frame 84 come out different on every run.
- Unseeded randomness makes shapes jitter from frame to frame.
- Rendering frame N of a loop shows the first frame twice: the hiccup at the seam.

When a fix works, add it to the contract. The contract is the lab's memory: every line is a failure you never have to see again.

Known trap: in three.js r160, TextGeometry reads `height` for extrusion depth; a `depth` parameter is overwritten with 50. Pin the version and name the right parameter.
