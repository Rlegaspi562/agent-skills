# Agent Skills

Free skills for AI coding agents. Each folder is one skill. Install the ones
you want, ignore the rest.

| Skill | What it does |
|---|---|
| [`prompt-coach/`](prompt-coach/) | Checks your request against the eight pieces of a complete prompt, then offers to fill the gaps before answering |
| [`morning-brief-builder/`](morning-brief-builder/) | Interviews you about priorities, follow-ups, meetings, and sources, then helps your agent build and refine a personalized morning brief |
| [`creative-research-batch/`](creative-research-batch/) | Runs a recurring TikTok creative research batch for one niche: Apify scrape, two-score ranking, Apify watches the top five, then a formatted brief and four-tab workbook in Drive plus a local review desk |
| [`architect/`](architect/) | Turns a build idea into an implementation-ready architecture packet, hands bounded work to Builder agents, and reviews their results against the agreed contracts |
| [`viral-analyze/`](viral-analyze/) | Reverse-engineers pasted YouTube Shorts, TikTok, and Instagram Reels URLs into hook, topic, format, and remix cards, with a pattern synthesis on batches |

## Install

Clone the repository:

```bash
git clone https://github.com/Rlegaspi562/agent-skills
```

### Claude Code

macOS or Linux:

```bash
mkdir -p ~/.claude/skills && cp -R agent-skills/prompt-coach agent-skills/morning-brief-builder agent-skills/creative-research-batch agent-skills/architect agent-skills/viral-analyze ~/.claude/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null; Copy-Item -Recurse -Force .\agent-skills\prompt-coach, .\agent-skills\morning-brief-builder, .\agent-skills\creative-research-batch, .\agent-skills\architect, .\agent-skills\viral-analyze "$HOME\.claude\skills\"
```

### Codex

Same commands, replacing `.claude/skills` with `.codex/skills`.

### Any other agent

The skills are plain Markdown. Paste the skill's `SKILL.md` into your
system prompt, project instructions, or custom-instructions box.

## prompt-coach

Say `/prompt-coach` before a request, or paste a prompt and ask it to check.

It grades your request against eight pieces across three levels, tells you
which ones are missing and which ones this particular request does not need,
then offers three ways forward: walk through the gaps together, answer it
as-is, or let it rewrite the prompt for you to review.

```
Level 1 (core four):  complete
Level 2 (control):    1 of 3
  Constraints:  missing
  Example:      not needed here, you're not matching a format
  Role:         present
Level 3 (safety net): missing

Solid Level 1 prompt. Adding Constraints and the safety net
would tighten it.
```

It is off unless you call it. Say "keep checking my prompts" and it stays on
for the session. Say "stop checking" and it stops.

**The eight pieces:** Goal, Context, Action, Output format (level 1),
Constraints, Example, Role (level 2), and the clarifying-question safety net
(level 3). Definitions and worked examples are in
[`prompt-coach/reference.md`](prompt-coach/reference.md). A fill-in-the-blank
version is in
[`prompt-coach/prompt-template.md`](prompt-coach/prompt-template.md), and you
can use that without installing anything.

## morning-brief-builder

Say `/morning-brief-builder` to turn the way you work into a reusable morning
brief. The skill interviews you a few questions at a time, tests vague rules
against real examples, scopes the sources your agent can access, and produces
a first brief with actions, reasons, source references, and coverage gaps.

It works with installable-skill agents and as plain pasted instructions. Live
connectors and scheduling are optional. Setup, a paste-ready version, and a
fictional example are in [`morning-brief-builder/`](morning-brief-builder/).

## Why this exists

Most bad AI output is a bad prompt. People ask an agent to guess what they
want, get frustrated when it guesses wrong, then spend the next hour
correcting it, burning tokens and patience, before starting a fresh session
and prompting exactly the same way.

Front-loading the specifics is faster than correcting the answer five turns
later. There is no perfect prompt, but there is a formula, and knowing the
pieces means you stop being the bottleneck.

MIT licensed. Built by [Rumil Legaspi](https://github.com/Rlegaspi562).

## architect

Say `/architect` before a software or product idea when the important
decisions should be settled before implementation begins.

The skill inspects the current project, distinguishes confirmed facts from
assumptions, recommends an architecture, defines contracts and acceptance
checks, and splits the build into bounded tasks. Each task can be handed to a
Builder agent with a clear scope, verification method, and stop condition.
Builder results come back to the Architect for evidence-based review.

Use it when a project crosses components, changes data or public interfaces,
introduces meaningful risk, or will be implemented by multiple agents. It
deliberately stays lightweight for small edits.

Setup and examples are in [`architect/README.md`](architect/README.md). A
paste-ready School post is in
[`architect/COMMUNITY-POST.md`](architect/COMMUNITY-POST.md).

## creative-research-batch

Say `/creative-research-batch` once Apify and Google Drive are connected.

It scrapes your niche's hashtags, ranks every video twice (once for reach,
once for relevance to what you sell), picks three Viral and two Targeted,
has Apify watch all five and describe them scene by scene, then writes a
formatted strategy brief and a four-tab research workbook into a dated Drive
folder and builds a local desk page showing the whole shortlist with scores.
About a dollar in Apify per batch.

Ships configured for DTC skincare on TikTok Shop; the niche is one block at
the top of the skill. Setup for Cowork, Claude Code, and other agents is in
[`creative-research-batch/README.md`](creative-research-batch/README.md).

To analyze specific Shorts, TikToks, or Reels you already have, use
[`viral-analyze/`](viral-analyze/).

## viral-analyze

Say `/viral-analyze` and paste one or more YouTube Shorts, TikTok, or
Instagram Reels links.

The skill watches what it can (a host watch skill, yt-dlp, or an Apify
watch actor), reads whatever stats exist, and returns a structured card
per video: hook, topic, format, beat structure, why it works, and remix
angles. Two or more links get a synthesis pass: recurring patterns and
three to five next-video ideas. Default batch cap is 15.

It is the URL-in analysis skill. For hashtag scraping into Drive, use
[`creative-research-batch/`](creative-research-batch/). Setup and the
tool matrix are in [`viral-analyze/README.md`](viral-analyze/README.md).
