# Agent Skills

Free skills for AI coding agents. Each folder is one skill. Install the ones
you want, ignore the rest.

| Skill | What it does |
|---|---|
| [`prompt-coach/`](prompt-coach/) | Checks your request against the eight pieces of a complete prompt, then offers to fill the gaps before answering |

## Install

Clone the repository:

```bash
git clone https://github.com/Rlegaspi562/agent-skills
```

### Claude Code

macOS or Linux:

```bash
mkdir -p ~/.claude/skills && cp -R agent-skills/prompt-coach ~/.claude/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null; Copy-Item -Recurse -Force .\agent-skills\prompt-coach "$HOME\.claude\skills\"
```

### Codex

Same commands, replacing `.claude/skills` with `.codex/skills`.

### Any other agent

The skills are plain Markdown. Paste `prompt-coach/SKILL.md` into your
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

## Why this exists

Most bad AI output is a bad prompt. People ask an agent to guess what they
want, get frustrated when it guesses wrong, then spend the next hour
correcting it, burning tokens and patience, before starting a fresh session
and prompting exactly the same way.

Front-loading the specifics is faster than correcting the answer five turns
later. There is no perfect prompt, but there is a formula, and knowing the
pieces means you stop being the bottleneck.

MIT licensed. Built by [Rumil Legaspi](https://github.com/Rlegaspi562).
