# Viral Analyze

Paste short-form video links and get a structured analyze card: hook,
topic, transcript, format, why it works, and remix angles. One URL is
one card. Two or more also gets a pattern synthesis and three to five
next-video ideas.

The skill is a plain Markdown recipe. It works on Claude Code, Codex,
Cursor, Grok Bot, and any harness that can read a `SKILL.md`. It does
not wrap Sandcastles, require Claude Desktop, or depend on a specific
MCP.

```text
You: /viral-analyze https://www.youtube.com/shorts/... https://www.tiktok.com/...

Agent: Two URLs. Watching what this host can reach.
       ...
       Card 1: hook, format, beats, remix angles, JSON
       Card 2: same
       Synthesis: recurring hooks, formats, topics,
       openings that win, four next-video ideas
       Coverage: watched via yt-dlp; view counts not available
```

Inspired by Kane Kallaway's public `/analyze` short-form workflow
(Sandcastles). This folder is an independent, agent-agnostic skill. It
is not affiliated with Sandcastles and is not a plugin for that
product.

## Install

Clone the public skill collection:

```bash
git clone https://github.com/Rlegaspi562/agent-skills
```

Claude Code on macOS or Linux:

```bash
mkdir -p ~/.claude/skills && cp -R agent-skills/viral-analyze ~/.claude/skills/
```

Claude Code on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null; Copy-Item -Recurse -Force .\agent-skills\viral-analyze "$HOME\.claude\skills\"
```

For Codex, use the same command and replace `.claude/skills` with
`.codex/skills`.

For another AI tool, paste [`SKILL.md`](SKILL.md) into its project
instructions or custom-instructions area. That file is the whole
skill.

## Use it

Start with one link:

```text
/viral-analyze https://www.youtube.com/shorts/xxxxxxxxx
```

Or several:

```text
/viral-analyze
https://www.tiktok.com/@creator/video/...
https://www.instagram.com/reel/...
https://www.youtube.com/shorts/...
```

Natural language works the same way:

```text
Why did this short take off? Reverse-engineer the hook and format.
https://www.youtube.com/shorts/xxxxxxxxx
```

```text
Batch-analyze these competitor Reels and tell me what openings repeat.
```

`/analyze` in a content-research context should also run this skill.
If the user is asking to analyze code or a document, leave it alone.

Default batch cap is 15. The agent should ask before going higher.

## What you need

An agent that can read this skill. That is enough for a useful card
from a pasted transcript, a visible thumbnail, and any stats you type
in.

Everything else is optional and harness-adaptive. The agent uses what
exists and labels what does not.

## Tool matrix

| Capability | Use if present | If missing |
|---|---|---|
| Watch, frames, transcript | Host `/watch` skill; `yt-dlp` + `ffmpeg`; an Apify watch actor already connected | Title, caption, thumbnail, user-pasted transcript. Card still ships |
| Performance stats | vidIQ, YouTube Data API, a platform scraper, or numbers you paste | `views` / `likes` / `comments` stay `null`. Craft analysis still runs |
| Own-channel script | Descript or similar, only for your own video | Skip. Do not invent a script |
| Save the card | A Content Scripts folder, idea backlog API, or drop path you name. Rumil OS / Fabinal if those tools are already there | Return Markdown + JSON in chat |

No paid SaaS is required. Apify, vidIQ, Descript, and Drive-style
destinations are upgrades, not prerequisites.

## Related: creative-research-batch

[`creative-research-batch/`](../creative-research-batch/) scrapes
TikTok hashtags through Apify, ranks a shortlist, watches the top
five, and writes a Drive brief plus workbook.

This skill does the other job: you already have URLs, and you want
Sandcastles-style `/analyze` cards on those links. Do not run both
for the same request unless you asked for both.

## Non-goals

- Not a video editor, caption burner, or posting scheduler.
- Not Sandcastles, not a Sandcastles plugin, and not an installer
  for Claude Desktop.
- Not a hashtag scraper or niche discovery run. That is
  `creative-research-batch`.
- Not a downloader for keeping or redistributing other people's
  videos. Temp frames or captions are a means, then they go away.
- Not a promise that every host can watch video. The card degrades
  in public and still has to be useful.

## Package contents

- [`SKILL.md`](SKILL.md): the complete installable skill

MIT licensed as part of the parent repository. Built by
[Rumil Legaspi](https://github.com/Rlegaspi562).
