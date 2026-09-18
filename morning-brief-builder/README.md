# Morning Brief Builder

Build a personalized AI morning brief around the way you actually work. The skill interviews you about your priorities, responsibilities, follow-up rules, meetings, and information sources, then helps your agent create a brief with clear actions and evidence.

It is for people who want one useful place to check each morning instead of manually scanning email, calendars, chats, tasks, and business systems.

## Install it

Clone or download the [`agent-skills`](https://github.com/Rlegaspi562/agent-skills) repository, then copy this folder into your agent's skills directory.

Claude Code on macOS or Linux:

```bash
mkdir -p ~/.claude/skills
cp -R agent-skills/morning-brief-builder ~/.claude/skills/
```

Claude Code on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force .\agent-skills\morning-brief-builder "$HOME\.claude\skills\"
```

For Codex, use the same commands and replace `.claude/skills` with `.codex/skills`.

If your agent does not support installable skills, upload [`SKILL.md`](SKILL.md) to a new chat or paste [`PASTE-INTO-YOUR-AGENT.txt`](PASTE-INTO-YOUR-AGENT.txt) into its instructions. The workflow is plain Markdown and does not require a specific AI product.

## Start here

Send this after installing or attaching the skill:

> Use the Morning Brief Builder skill. Interview me about how I work, what matters to me, and what I need to know each morning. Ask a few questions at a time, challenge vague answers with concrete examples, and help me build my first useful brief using the tools I already have. Start with the interview.

The agent should first learn:

- what outcomes you own and what deserves your attention
- which follow-ups, meetings, deadlines, or changes should be escalated
- what you want hidden as routine noise
- which sources your agent can actually read
- when, where, and how you want the brief delivered

It then creates a reusable configuration and runbook, produces a first source-backed brief, and asks for feedback so its ranking rules improve over time.

See [`EXAMPLE-BRIEF.md`](EXAMPLE-BRIEF.md) for a fictional example.

## What you need

- An AI agent that can read an attached file or accept custom instructions.
- A rough idea of your current priorities and the apps where your work lives.
- Optional connectors for email, calendars, chats, tasks, CRM records, or documents.

No paid connector is required. You can start with pasted notes or exports. Live connections, saved files, scheduling, and unattended runs depend on the capabilities and permissions of your agent.

## Run it again

After the first setup, use:

> Run my morning brief using my saved morning-brief-config.md and morning-brief-runbook.md. Check today's priorities, open commitments, follow-ups, and upcoming meetings. Give me actions, reasons, and sources. Flag missing access and uncertainty. Update permitted run state after successful processing; do not send replies or change source records.

The skill defaults to read-only briefing. It does not authorize your agent to send messages, update records, or expose information to a shared destination.

## Package contents

- [`SKILL.md`](SKILL.md): the complete installable skill
- [`PASTE-INTO-YOUR-AGENT.txt`](PASTE-INTO-YOUR-AGENT.txt): a standalone paste-ready version
- [`EXAMPLE-BRIEF.md`](EXAMPLE-BRIEF.md): a fictional example output

MIT licensed as part of the parent repository. Built by [Rumil Legaspi](https://github.com/Rlegaspi562).
