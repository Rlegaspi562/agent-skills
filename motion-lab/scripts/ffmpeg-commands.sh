#!/usr/bin/env bash
# ffmpeg commands from "Opus 5.5 Motion Lab" by Florence (@flxrnc), copied verbatim. Run one at a time; not meant to run top to bottom.

# Frames to MP4 (from render.mjs footer)
ffmpeg -framerate 24 -i out/frames/%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart out/anim.mp4

# Contact sheet: every 12th frame, 4 across, 3 down
ffmpeg -framerate 24 -i out/frames/%04d.png -vf "select='not(mod(n\,12))',scale=400:-1,tile=4x3" -frames:v 1 out/contact.png

# Music + sound effects, mixed, normalized to -14 LUFS, muxed under the picture
ffmpeg -i out/anim.mp4 -i music.wav -i sfx.wav -filter_complex "[1:a][2:a]amix=inputs=2:duration=first,loudnorm=I=-14:TP=-1:LRA=11[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart out/final.mp4

# MP4 for an X post: H.264 High, yuv420p, starts playing at once
ffmpeg -framerate 24 -i out/frames/%04d.png -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 18 -movflags +faststart out/anim.mp4

# GIF for an X Article: one palette for the whole clip, 1200 px wide
ffmpeg -framerate 24 -i out/frames/%04d.png -vf "scale=1200:-1:flags=lanczos,split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle" -loop 0 out/anim.gif

# Loop check: play it three times back to back and watch the seam
ffmpeg -stream_loop 2 -i out/anim.mp4 -c copy out/loop_check.mp4
