---
name: motion-presets
description: >-
  Reverse-engineer short-form text, mask, motion, and SFX recipes from pasted
  Instagram Reels, YouTube Shorts, or TikTok URLs into a reusable DaVinci
  Resolve–oriented preset library. Use when the user drops edit-craft links,
  wants CapCut/DaVinci text presets, masking recipes, kinetic captions, or says
  /motion-presets. Skip when they only want hooks/topics (that is viral-analyze)
  or hashtag scraping (creative-research-batch).
user-invocable: true
argument-hint: "[one or more Reels/Shorts/TikTok URLs]"
---

# Motion Presets

By Rumil / Fabinal content lane (Eren). Version 0.1.

Turn pasted short-form video URLs into **edit-craft cards** and reusable
**presets**: fonts, kinetic captions, masks, transitions, and sound hits that
an agent (or human) can recreate in **DaVinci Resolve Studio** (Text+, Fusion,
Fairlight). One URL = one source card + any new presets extracted. Two or more
also gets a cross-source pattern note.

This is a portable Markdown skill. Work with the host agent's real tools.
Never invent a connector or SaaS that is not present.

**Sibling skill:** `viral-analyze` = why the video works (hook, topic, format,
remix). **This skill** = how the edit looks and sounds (text, mask, motion,
SFX). Run both on the same URL when useful; do not collapse them into one card.

## When this fires

Run when the user:

- pastes Instagram Reels / Shorts / TikTok links and cares about **on-screen
  graphics, text animation, masking, fonts, or sounds**
- says `/motion-presets`, "pull the text presets", "study the captions",
  "DaVinci text pack", or "build my preset folder"
- wants a growing library any agent can read before editing

If they only ask why it went viral / what to remake as a topic, use
`viral-analyze` instead (or in addition).

## 1. Collect URLs

Deduplicate. Cap default batch at **10** (heavier than viral-analyze because
of frame/mask work). Ask before going higher.

## 2. Capture what the host can actually see

Prefer, in order:

1. Host `/watch` / `watchVideo` / video-review tool on the downloaded file.
2. `yt-dlp` download + `ffmpeg` frames (dense early seconds for hooks; mid/end
   for caption systems). Delete temp media when done if the host allows.
3. Degrade: thumbnails + caption text only — still write a card, label Coverage.

Never invent a mask or font you did not observe. Mark uncertain fields.

## 3. Emit one source card per URL

Write Markdown + JSON under this skill's library:

```text
motion-presets/library/sources/<platform-shortcode>/
  card.md
  card.json
  watch-notes.md   # optional raw watch dump
```

### card.json schema

```json
{
  "type": "motion_preset_source",
  "url": "https://www.instagram.com/p/...",
  "platform": "instagram_reels|youtube_shorts|tiktok|other",
  "shortcode": "DcY72S4B1EG",
  "creator": "@handle",
  "duration_sec": 54,
  "title_or_caption": "...",
  "coverage": "watched|frames_only|metadata_only",
  "typography": [
    {
      "id": "hook-heavy-sans",
      "role": "hook|body|accent|lower_third|logo",
      "sample_text": "I DON'T HAVE 10",
      "case": "all_caps|sentence|mixed",
      "font_guess": "heavy extended sans (Monument Extended / Helvetica Neue Ext–like)",
      "weight": "black|bold|medium|regular",
      "color": "#FFFFFF",
      "stroke_or_shadow": "soft black drop shadow",
      "size_vs_frame": "large ~18% frame height",
      "position": "center|upper_center|lower_third"
    }
  ],
  "motion": [
    {
      "id": "scale-pop-bounce",
      "applies_to": "hook-heavy-sans",
      "description": "Scale 50%→110%→100% over ~8–12 frames",
      "easing": "overshoot / bounce"
    }
  ],
  "masking": [
    {
      "id": "text-behind-subject",
      "description": "Kinetic text sits behind legs/laptop via rotoscope or polygon mask",
      "difficulty": "medium|hard"
    }
  ],
  "overlays": [
    {
      "id": "ig-profile-card",
      "description": "Rounded IG UI card with drop shadow, scale pop"
    }
  ],
  "transitions": [
    {
      "id": "white-flash-shutter",
      "description": "Full-frame white opacity pulse + shutter SFX"
    }
  ],
  "sfx": [
    {
      "id": "text-pop",
      "cue": "each hook word appear",
      "character": "short pitched pop/click"
    }
  ],
  "music": "lo-fi / chill hip-hop bed under VO",
  "preset_ids": ["kinetic-hook-dual-font", "capcut-center-captions", "text-behind-talent", "white-flash-shutter"],
  "davinci_notes": "Short Resolve Studio recreation hints for this source"
}
```

Also write a human `card.md` with the same facts in prose + timestamp beats.

## 4. Upsert reusable presets

If a technique repeats or is worth stealing for Rumil's shorts, add or update:

```text
motion-presets/library/presets/<preset-id>.md
```

Each preset file must include:

1. **Name + id**
2. **When to use** (Rumil short-form context)
3. **Look** (font, color, shadow)
4. **Motion** (keyframes / Text+ settings in plain language)
5. **Mask / composite** if any
6. **SFX** pairing
7. **DaVinci Resolve Studio steps** (Edit page Text+, Fusion if needed, Fairlight)
8. **Source shortcodes** that demonstrated it
9. **Closest free fonts** (never claim a licensed font is free)

Update `library/INDEX.md` whenever you add a preset or source.

## 5. Batch synthesis (2+ URLs)

After cards: 3–7 recurring edit patterns + which presets to standardize for
Rumil's pack first.

## 6. Hand-off

- Tell the user the GitHub paths (this repo) and summarize new presets.
- Offer to keep ingesting links into `library/`.
- Packaging titles/thumbs still Mikasa; scripting still Eren. This library is
  shared edit craft for whoever cuts (human or AI in Resolve).

## Non-goals

- Not a full auto-Resolve renderer (yet). Output is recipes agents can execute.
- Not viral-analyze. Not creative-research-batch.
- Do not commit binary video into git. Sources are URLs + notes only.
