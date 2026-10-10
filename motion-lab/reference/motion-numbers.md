# Motion numbers cheat sheet

From Florence (@flxrnc), "Opus 5.5 Motion Lab". Give the model curves and frames, not adjectives.

## Easing (cubic-bezier, from Andrey Sitnik's Easings reference)

| Name | cubic-bezier | Use it for |
|---|---|---|
| ease-out-expo | 0.16, 1, 0.3, 1 | Text and logo reveals |
| ease-out-quint | 0.22, 1, 0.36, 1 | Premium entrances |
| ease-in-out-quart | 0.76, 0, 0.24, 1 | Moves and camera pushes |
| ease-in-expo | 0.7, 0, 0.84, 0 | Fast exits |
| ease-out-back | 0.34, 1.56, 0.64, 1 | A playful pop with overshoot |

- Enter with ease-out, exit with ease-in, exits 40 to 50% shorter (Material 3: 400 ms in, 200 ms out). Move across the screen with ease-in-out.
- Linear only for rotation, progress bars and the phase of a loop. Linear on a move makes a render look like a render.

## Springs (damping ratio)

- 1.0 never bounces. 0.7 to 0.85 premium. 0.4 to 0.6 playful. Under 0.3 cartoon.
- Remotion default (mass 1, damping 10, stiffness 100) = 0.5. react-spring default (tension 170, friction 26) = 1.0.
- Position and size may bounce; opacity and color never do.
- Tokens file and a closed-form spring(t): see scripts/motion.js. Tell the model: use only these tokens, no inline numbers.

## Durations and stagger

- UI feedback 100 to 200 ms (100 ms feels instant). UI moves 200 to 500 ms. Hero reveals 600 to 900 ms.
- Stagger: letters 1 frame apart, words 60 to 120 ms, list items 40 to 80 ms.
- Start the next element when the previous one is 30 to 50% done.
- Say it in frames: at 24 fps one frame is about 42 ms, so 400 ms = 10 frames, 750 ms = 18.

## Beat grid

- Frames per beat = fps x 60 / BPM. 120 BPM at 24 fps = 12 frames. 128 BPM at 30 fps = 14.06.
- Compute every beat from time and round each one; adding a rounded 14 repeatedly drifts 2 frames after 32 beats.
- Cut on the beat, change the layout on the bar (every 4 beats).

## Holds, camera, contrast

- On-screen text holds at least 0.3 s per word plus 0.5 s (two-word title = 1.1 s). Slow 2% push during holds.
- Camera gets the softest curves (ease-in-out-quart); objects get snappier ones. Parallax 1.0 foreground, 0.5 middle, 0.2 background. Three.js FOV 35 to 50 degrees is a good start.
- Text at 4.5:1 contrast on every frame; never more than 3 flashes per second (WCAG).
- Exaggerate key poses 10 to 30% further than feels right; the feed shrinks everything.

## Animation principles as prompt numbers (Experiment 2)

| Principle | What it does | Write it in the prompt as |
|---|---|---|
| Anticipation | Winds up before the move | 11-frame crouch (1.2x0.75) |
| Squash and stretch | Shows weight and speed | stretch 0.85x1.28 at takeoff, squash 1.25x0.7 on landing |
| Overlapping action | Limbs start later than the body | arms lag 4 frames, legs 6 |
| Follow-through | Parts keep moving after the body stops | arms settle at 2.2 Hz, damping 0.22 |
| Arcs | Makes motion feel natural | a flip along a dotted arc, 3.5 high |
| Slow in and slow out | Speeds up and settles softly | spring back at damping 0.55 |
| Timing | Frame count sets weight | 25 frames of air per hop, 18 frames of crouch before the flip |

Staging is the one-hero rule. Ask for a playhead and frame labels while iterating; switch them off for the final render.

## Feeling to number

- "Make it pop": scale 1.0 to 1.08 to 1.0 over 6 frames, peak on the beat.
- "Make it feel premium": ease-out-quint on entrances, springs at damping ratio 0.8, no overshoot on text.
- "It drags": shorten each hold by 12 frames (one beat at 120 BPM and 24 fps).
- "It feels busy": one hero move at a time; everything else starts 150 ms later at 60% of its travel.
- "It looks like AI": list the defaults it used by name, ban each one, render again.
