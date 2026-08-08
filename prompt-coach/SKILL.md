---
name: prompt-coach
description: Checks a request against the eight pieces of a complete prompt and offers to fill the gaps before answering. Use when the user runs /prompt-coach, asks whether a prompt is good enough, asks for help writing or improving a prompt, or asks what a prompt is missing. Also use for the rest of the session once the user asks to keep checking their prompts.
user-invocable: true
argument-hint: "[the prompt to check, or nothing to check the previous message]"
---

# Prompt Coach

Most bad AI output is a bad prompt. The fix is front-loading the specifics
instead of correcting the answer five turns later.

This skill checks a request against eight pieces, reports what is missing,
and offers to build the missing parts with the user. It does not rewrite
their intent and it does not demand all eight.

## The eight pieces

| Level | Piece | One-line test |
|---|---|---|
| 1 | Goal | Does it say what outcome is wanted? |
| 1 | Context | Does it say what the agent needs to know to not guess? |
| 1 | Action | Does it name the actual task verb? |
| 1 | Output format | Does it say what the answer should look like? |
| 2 | Constraints | Does it say what to avoid, stay within, or not touch? |
| 2 | Example | Does it show a sample of the thing wanted? |
| 2 | Role | Does it say who the agent should answer as? |
| 3 | Safety net | Does it invite clarifying questions before work starts? |

Full definitions, weak and strong examples, and the "not needed" rules are in
[reference.md](reference.md). Read it before grading anything, and quote its
examples rather than inventing new ones.

## What to check

- Invoked with text: grade that text.
- Invoked bare: grade the user's previous message.
- No previous message: say so and offer the template instead.

## Skip the coaching when it does not apply

Do not grade these. Just answer:

- A quick factual question ("what port does Postgres use?")
- A one-line task with no room for ambiguity ("rename this variable to `total`")
- A reply inside an exchange where the context is already established
- Anything where the coaching would take longer than the answer

Say one line ("that one is clear enough, here you go") and move on. A skill
that fires on everything gets uninstalled.

## Grade every piece into one of three states

**present**, **missing**, or **not needed here**.

The third state is the point. A prompt does not need all eight. Example is
not needed when nothing is being matched to a format. Role is not needed when
the task has one obvious correct answer. Calling those "missing" teaches
people to pad prompts, which is the opposite of the goal.

Every "not needed here" carries a one-line reason. If a reason cannot be
given, the piece is missing.

**A piece that is present but too vague to constrain anything counts as
missing.** "Build a website" gestures at an Action without saying how far to
take it, and "for my gym" gestures at a Goal without naming an outcome. When
marking one of these missing, quote the words they used and say what would
make it count:

```
Goal:    missing. "for my gym" names who it's for, not what you want
         to happen. What should a visitor do?
```

This is the difference between the skill teaching and the skill scolding.

## Report by level, never as a raw score

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

Never report "4 of 8". Levels stack: Level 1 is a complete prompt on its own,
Level 2 adds control, Level 3 is insurance against a wrong turn. Say which
level the prompt reached and what the next level would buy for this specific
request.

Keep the whole report under fifteen lines.

## Then offer three ways forward

```
Want me to build out the missing pieces with you?
  yes        walk me through them
  no         just answer it as-is
  show me    I'll rewrite it, you review
```

**yes**: ask about one missing piece at a time, in this order: Goal, Action,
Context, Output format, Constraints, Example, Role, safety net. One question
per turn, with a concrete suggestion the user can accept. Never ask for a
piece already marked present or not needed. When done, assemble the rewritten
prompt, show it in full, and ask before running it.

**no**: answer the original request as it stands. Do not re-raise the gaps.

**show me**: rewrite it in one pass. Mark every assumption filled in as
`[assumed: ...]` so the user can see exactly what was invented on their
behalf, then ask them to correct the assumptions before running it.

## Rules

1. **Never invent Context.** Missing context gets a question, not a guess. An
   assumption in "show me" mode is always labeled.
2. **Never change what they asked for.** The rewrite adds specifics to their
   intent. It does not redirect the task toward a better idea.
3. **Keep their words** wherever the original phrasing works. A rewrite in
   the agent's voice is harder for the user to reuse.
4. **Grade the prompt, not the person.** Report gaps flatly. No praise, no
   scolding.
5. **One report per request.** Do not re-grade a prompt the user already
   chose to send as-is.

## Persistent mode

Off by default. It fires when invoked, then goes quiet.

Turn it on when the user says something like "keep checking my prompts" or
"stay on for this session". Then grade every substantive request before
answering it, keeping the report to three lines unless something in Level 1
is missing. The skip rules above still apply, and they matter more in this
mode.

Turn it off on "stop checking", "quiet down", or any sign of irritation.

This mode lasts for the session only. To make it permanent, tell the user to
add one line to their `CLAUDE.md` or `AGENTS.md`:

```
Before answering any substantive request, run prompt-coach on it.
```

## Handing over the template

[prompt-template.md](prompt-template.md) is a fill-in-the-blank version of
all eight pieces. Offer it when the user asks for something reusable, when
they are writing a prompt from scratch rather than fixing one, or when they
say the coaching is too slow.
