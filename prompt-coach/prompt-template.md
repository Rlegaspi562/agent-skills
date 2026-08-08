# Prompt template

Copy this, fill in what applies, delete the rest. Skipping a piece on purpose
is fine. Skipping it because you forgot is what costs you the correction
rounds.

Definitions and examples for each piece are in [reference.md](reference.md).

---

```
Role: [who should answer, if it changes the answer]

Goal: [the outcome you want, as a result not an activity]

Context: [what I know that you can't see: what exists, who it's for,
          what I already tried, what's in the way]

Action: [the task, scoped: what to do and how far to take it]

Output format: [what the answer should look like: file, table, list,
                length, structure]

Constraints: [what to avoid, stay within, or not touch]

Example: [a sample of what I want, or a link to something close]

If any part of this is ambiguous, or if you're missing information that would
help you give a better answer, ask me clarifying questions before you write
anything. Otherwise, just proceed.
```

---

## Short version

Most requests do not need all eight. This covers the core four and takes
twenty seconds:

```
I want [goal]. Here's what you need to know: [context].
Please [action] and give it to me as [output format].

If anything's ambiguous, ask before you write. Otherwise proceed.
```

## Which pieces to add first

If the answers keep missing the point, add **Context**.

If the answers are right but the wrong shape, add **Output format**.

If the answers are good but unusable, add **Constraints**.

If you keep saying "not like that, more like this", add an **Example**.

If the answers are technically correct but from the wrong perspective, add a
**Role**.
