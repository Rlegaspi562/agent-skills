# Motion Presets

Paste Instagram Reels / YouTube Shorts / TikTok links and get a growing
**edit-craft library**: kinetic captions, dual-font hooks, text-behind-talent
masks, flash transitions, and SFX cues written so an agent can recreate them
in **DaVinci Resolve Studio**.

Sibling of [`viral-analyze/`](../viral-analyze/) (hooks and topics). This folder
is **how the edit looks and sounds**, not why the idea works.

Canonical SoT: https://github.com/Rlegaspi562/agent-skills/tree/main/motion-presets

## Layout

```text
motion-presets/
  SKILL.md                 # agent instructions
  README.md                # this file
  library/
    INDEX.md               # catalog of sources + presets
    sources/<shortcode>/   # one analyzed URL
      card.md
      card.json
    presets/<preset-id>.md # reusable recipes
```

## Use

```text
/motion-presets https://www.instagram.com/p/... https://www.instagram.com/p/...
```

Or natural language: "pull the text and mask presets from these reels into the
motion-presets library."

## Install

Same as other skills in this repo — copy `motion-presets/` into your agent's
skills directory, or point the agent at this GitHub path.

## Seed library (2026-09-19)

Two @zioncruzz Instagram reels seeded the first presets:

| Shortcode | URL |
|---|---|
| DcY72S4B1EG | https://www.instagram.com/p/DcY72S4B1EG/ |
| DcgcNgDh-dX | https://www.instagram.com/p/DcgcNgDh-dX/ |
| DfcNqN9TPp8 | https://youtube.com/shorts/DfcNqN9TPp8 |

See `library/INDEX.md` for preset IDs.
