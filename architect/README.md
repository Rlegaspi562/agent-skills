# Architect

Architect turns a rough software or product idea into a build packet that
another AI agent can execute without guessing.

It separates two jobs that are often mixed together:

- **Architect:** inspects the project, makes the important decisions, defines
  contracts, and breaks the work into verifiable slices.
- **Builder:** implements one bounded slice, proves it works, and reports back
  for review.

This is useful when a project is too complex for "just start coding," when you
want your strongest model making the high-leverage decisions, or when several
agents will work on the same build.

## Install

Clone the public skill collection:

```bash
git clone https://github.com/Rlegaspi562/agent-skills
```

Claude Code on macOS or Linux:

```bash
mkdir -p ~/.claude/skills && cp -R agent-skills/architect ~/.claude/skills/
```

Claude Code on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null; Copy-Item -Recurse -Force .\agent-skills\architect "$HOME\.claude\skills\"
```

For Codex, use the same command and replace `.claude/skills` with
`.codex/skills`.

For another AI tool, paste [`SKILL.md`](SKILL.md) into its project instructions
or custom-instructions area.

## Use it

Start with:

```text
/architect Build a client portal where customers can upload documents and see review status.
```

Or say:

```text
Architect this feature before any code is written.
```

The skill will inspect the current project when one exists, ask only the
questions that materially change the design, and produce an implementation-ready
packet with decisions, contracts, tasks, acceptance checks, risks, and a first
Builder handoff.

If you want the agents to continue after the plan, say:

```text
Use the build packet. Give the first slice to a Builder and review the result.
```

The agent should not implement or mutate the project during the architecture
pass unless you explicitly ask it to continue into the build.

