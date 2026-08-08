# STATE - agent-skills (updated 2026-08-08 by claude @ main-pc)
## Progress
phase: build | percent: 85
done: repo scaffolded as the umbrella home for free skills; prompt-coach written (SKILL.md, reference.md, prompt-template.md); hub README with install steps for Claude Code, Codex, and paste-in agents
blocked: GitHub repo not created yet, so the link promised in the "how to prompt" video description does not resolve
## Now
prompt-coach is complete locally and unpushed. It grades a request against eight pieces in three levels, reports present / missing / not needed here per piece, and offers yes / no / show me. Level-aware reporting was chosen over a flat "4 of 8" score because the video script says you may not need every piece.
## Next
1. Create public repo github.com/Rlegaspi562/agent-skills and push (needs Rumil's go-ahead)
2. Test prompt-coach live: install to ~/.claude/skills, run it on a weak prompt and on a trivial request, confirm it skips the trivial one
3. Add the registry entry to hq-entry-point CONTEXT.md
4. Fill the CTA/Outro section of rumil-dummy-os/content/videos/_pipeline/how-to-prompt/script.md with the repo link
## Decisions
decided: umbrella repo named agent-skills rather than a standalone prompt-coach repo or bundling into agent-handoff-skill, which has a recorded no-bundling decision; level-aware reporting with a third "not needed here" state; invoked-by-default with opt-in session-long persistent mode; public distributable package, so it omits CLAUDE.md and AGENTS.md under the hq-entry-point exception
tried: design was brainstormed 2026-08-02 and stalled unanswered; two later sessions searched for the skill and found nothing
rejected: flat "n of 8" scoring, it teaches people to pad prompts with pieces they do not need; ambient always-on grading, it gets the skill uninstalled
## Open questions
- none
## Sync
last push: never | repo not created
