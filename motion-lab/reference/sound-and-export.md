# Sound, loops and export specs

From Florence (@flxrnc), "The last mile".

## Sound

- The feed plays muted until a tap: the picture must work in silence first.
- Sound comes last, one prompt per piece, scored against frame numbers.
- Each hit lands 1 frame after its picture, never before. Light beats sound.
- Target about -14 LUFS, peak -1 dBTP, 48 kHz stereo WAV, muxed into the MP4.
- Hits 3 to 6 dB over the bed; nothing above 8 kHz in the lab prompts; mono-safe.
- The model cannot listen: verify by decoding the final MP4 and measuring each hit against its frame.
- Check the phone band (200 Hz to 6 kHz). The first Experiment 1 mix had 80.6% of its energy under 60 Hz, where phone speakers play nothing.
- Phase tones so the first waveform peak lands on frame + 1 (cosine start, short attack).
- AAC encode lifted true peak from -1.3 to -0.4 dBTP: limit the WAV to -2.2 dBTP so the MP4 stays under -1.
- AAC adds about 16 ms padding at a loop seam: keep the seamless WAV as master; for a single-loop MP4 add a 2 ms raised-cosine fade to the first and last 96 samples.
- The lab synthesized all sound with the Web Audio API, no samples. Mix command for music + SFX files: scripts/ffmpeg-commands.sh.

## Loops

- Render frames 0 to N-1, never N.
- Drive every loop from phase = frame / N with whole-number cycles.
- For organic drift, sample noise along a circle.
- Frame 0 must be a finished composition (it shows while a GIF loads).
- GIF delays are stored in hundredths of a second: at 24 fps use five frames at 40 ms then one at 50 ms to keep a 6 s loop at exactly 6.00 s.

## X specs

| Spec | GIF | Video |
|---|---|---|
| Size limit | 15 MB | 140 s without Premium |
| Frame size | up to 1280 x 1080 | 1920 x 1080 for 16:9 |
| Frames and speed | at most 350 frames | up to 60 fps |
| Format | one palette, loop forever | H.264 High, yuv420p, AAC audio |
| Lab default | 1200 px wide, 24 fps | CRF 18, faststart |

At 24 fps the 350-frame GIF cap is about 14.5 s.
