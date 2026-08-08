# The eight pieces

Three levels. Level 1 is a complete prompt on its own. Level 2 adds control.
Level 3 is insurance against a wrong turn.

The weak prompt used throughout:

> build a website for my gym

It has a Goal and an Action and nothing else, so the agent has to guess the
audience, the pages, the stack, the tone, and what "done" means. Every wrong
guess costs a correction round.

---

## Level 1: the core four

### Goal

The outcome you want, stated as a result rather than an activity.

- **Weak:** "build a website for my gym"
- **Strong:** "get more free-trial signups from people who find the gym on their phone"

The Goal is what lets an agent make the hundred small calls you did not
specify. Without it, it optimizes for whatever it assumes.

**Not needed when:** the task is mechanical and has one correct result. A
rename, a format conversion, a lookup.

### Context

What the agent needs to know that it cannot see or infer.

- **Weak:** nothing
- **Strong:** "24-hour gym in Tucson, 400 members, mostly 25 to 40, competing on price against a Planet Fitness two blocks away. No logo yet. I have twelve photos of the floor."

Context is the piece people skip most and the one that costs most. Include
constraints of reality: what exists, what does not, who it is for, what you
already tried.

**Not needed when:** the agent can already see everything relevant, usually
because it is in the open files or earlier in the conversation.

### Action

The task verb. What you are actually asking it to do right now.

- **Weak:** "build a website" (build how much? design it? code it? deploy it?)
- **Strong:** "write the HTML and CSS for the landing page only, no backend"

Vague Actions produce work you did not want. Scoping the Action is usually
the fastest single fix to a prompt.

**Not needed when:** never. If an agent cannot tell what to do, nothing else
in the prompt saves it.

### Output format

What the answer should look like when it arrives.

- **Weak:** nothing, so you get whatever shape the model prefers
- **Strong:** "one HTML file with inline CSS, no build step, no frameworks"

Format covers shape (file, table, list, prose), length, and structure. It is
the difference between an answer you can use and an answer you have to
reformat.

**Not needed when:** you genuinely do not care, or the format is fixed by the
task, such as editing an existing file in place.

---

## Level 2: adding control

### Constraints

The boundaries. What to avoid, stay within, or not touch.

- **Weak:** nothing, so it uses React and a component library you do not want
- **Strong:** "no JavaScript frameworks, must load under 1 second on 4G, do not touch the existing booking page"

Constraints prevent the expensive kind of wrong: work that is good but
unusable. Budget, deadline, stack, tone, and off-limits files all live here.

**Not needed when:** any reasonable approach works for you.

### Example

A sample of the thing you want, or of something close to it.

- **Weak:** "make it look professional"
- **Strong:** "the layout should work like basecamp.com: one column, big type, one call to action per screen"

One example replaces a paragraph of adjectives. A link, a snippet of your
existing code, or a before-and-after pair all count.

**Not needed when:** you are not matching an existing style, format, or
pattern. Do not invent an example for the sake of having one.

### Role

Who the agent should answer as.

- **Weak:** nothing
- **Strong:** "answer as a conversion copywriter who has launched gym sites, not as a web developer"

Role changes which tradeoffs get made and which vocabulary comes back. It
matters most when a question has several defensible answers from different
professions.

**Not needed when:** the task has one obviously correct answer. A Role on a
factual lookup is decoration.

---

## Level 3: the safety net

### The clarifying question

One line, always the same, at the end:

> If any part of this is ambiguous, or if you're missing information that
> would help you give a better answer, ask me clarifying questions before you
> write anything. Otherwise, just proceed.

This is the cheapest line in prompting. It converts a wrong assumption into a
question, which costs one turn instead of a full rewrite. The "otherwise,
just proceed" half matters as much as the first: without it, you get
questions on requests that were already clear.

**Not needed when:** the request is trivial, or you would rather see a first
attempt than answer questions.

---

## The same prompt, complete

> **Role:** Answer as a conversion copywriter who has launched gym sites.
>
> **Goal:** Get more free-trial signups from people who find us on their phone.
>
> **Context:** 24-hour gym in Tucson, 400 members, mostly 25 to 40, competing
> on price against a Planet Fitness two blocks away. No logo yet. I have
> twelve photos of the floor.
>
> **Action:** Write the copy and markup for the landing page only.
>
> **Output format:** One HTML file with inline CSS, no build step.
>
> **Constraints:** No frameworks. Must load under 1 second on 4G. Mobile
> first. Do not mention prices, they change monthly.
>
> **Example:** Layout should work like basecamp.com, one column, big type,
> one call to action per screen.
>
> If any part of this is ambiguous, or if you're missing information that
> would help you give a better answer, ask me clarifying questions before you
> write anything. Otherwise, just proceed.

Same request. The first version buys you a generic gym site and an hour of
corrections. The second buys you something you can ship or reject on the
first pass.
