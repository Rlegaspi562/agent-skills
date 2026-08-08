# STATE - agent-skills (updated 2026-08-08 by claude @ main-pc)
## Progress
phase: live | percent: 90
done: umbrella repo for free skills; prompt-coach complete (SKILL.md, reference.md, prompt-template.md); hub README with install steps for Claude Code, Codex, and paste-in agents; public repo created and pushed
blocked: none
## Now
prompt-coach grades a request against eight pieces in three levels, marks each piece present / missing / not needed here, and offers yes / no / show me. Smoke tested against the weak prompt from the companion video; that test added the rule that a piece too vague to constrain anything counts as missing. Installed locally at ~/.claude/skills/prompt-coach.
## Next
1. Publish the Skool resource post pointing at this repo, matching the Agent Handoff post format
2. Watch for the first real-use failure mode: whether the skip rules fire often enough that the skill does not feel like a nag
3. Second skill for this repo is undecided; keep the README hub table ready for it
## Decisions
decided: umbrella repo rather than a standalone prompt-coach repo or bundling into agent-handoff-skill, which has a recorded no-bundling decision; level-aware reporting with a third "not needed here" state; invoked by default with opt-in session-long persistent mode; persistent mode is session-scoped only, permanence is documented as a one-line CLAUDE.md addition rather than faked; public distributable package, so it omits CLAUDE.md and AGENTS.md under the hq-entry-point exception
tried: smoke test on "build a website for my gym" surfaced the vague-but-present gap and the fix landed in the same session
rejected: flat "n of 8" scoring, it teaches people to pad prompts with pieces they do not need; ambient always-on grading, it gets the skill uninstalled
## Open questions
- none
## Sync
last push: 2026-08-08 | ok
