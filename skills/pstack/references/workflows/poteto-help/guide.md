> Codex port: apply [the runtime contract](../../codex-runtime.md) before this workflow.

# Poteto help

Answer the user's question about pstack, hand them a prompt they can send, and link the file the answer came from. For a help question, don't start the work. The user asked how, and a pstack run spends real tokens, so let them send the prompt.

A message that asks for work, such as "use pstack to fix this bug", is not a help question. Read [`poteto-mode`](../poteto-mode/guide.md), do the work under it, and mention once that a explicit conversational mode activation keeps it on.

This file maps questions to the bundled specialists and upstream guide pages that hold the answers. Those files own the details. Read the file you route to before you quote it, and trust it when it disagrees with this map. Local links describe the adapted port. Link upstream only when discussing upstream behavior, never as if it documented Codex-specific changes.

## Find out what they need

Infer the need from the message and the conversation. A named situation, such as "which skill reviews a PR?", goes straight to its section. If the need is still unclear, ask one multiple-choice question with these options, then answer only the section they pick:

- Get set up
- Start a task with `$pstack`
- Pick a skill for a situation
- Fix a run that went wrong
- Make pstack my own

Check the state that changes the answer, and mention it only when it does:

- No approved pstack role preferences means every role inherits this Codex chat's settings; project verification setup may still be needed.
- No `verify-*` skill or other app harness in the project means agents have no scripted way to drive the app. Mention `create-verification-skill` when the question is about proving a change works.

When the explicit model preferences are absent and it matters, ask whether the user wants to pick a model for each role and a reasoning budget now. It matters when the user is new, the question is about setup or cost, or the answer depends on which models run. Ask at most once per chat. If the need is also unclear, ask both questions together. Offer two choices:

- Now: suggest `$pstack set up this project`, and answer their question too.
- Later: answer their question; roles remain inherited until explicit choices are configured.

## Get set up

Install the Codex pstack skill, then use `$pstack set up this project` to
configure optional model roles and inspect/create the real verification skill
and feature map. Model inheritance needs no configuration; project verification
does. See [setup](../setup-pstack/guide.md). No Cursor slash command, keyboard
shortcut, or global Custom Mode is registered here. Explicit mode activation
persists conversationally until opt-out. Reinstate it in a new chat/handoff.

Read [prompting](references/prompting.md) before helping word a task. A prompt
names goal and observable completion check. Keep skipped steps with reasons.

## Pick a skill

The default entry point is `$pstack`, which runs most of the others when its steps need them. Name a skill directly when the user wants more or less of something than the playbook gives. Read the skill before you recommend it, and give one example prompt.

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | [`$pstack`](../poteto-mode/guide.md) |
| Know how code works now, or where new code should live | [`how`](../how/guide.md) |
| Know why code is shaped this way, or where a number came from | [`why`](../why/guide.md) |
| Understand a change or subsystem, explained plainly | [`teach`](../teach/guide.md) |
| Catch up on their own recent work on a topic | [`recall`](../recall/guide.md) |
| Catch up on everything in this chat since their last message, with enough context to decide each action item | [`ketchup`](../ketchup/guide.md) |
| Know what a small diff could break outside itself | [`blast-radius`](../blast-radius/guide.md) |
| Settle types and module shape before code that crosses a function boundary | [`architect`](../architect/guide.md) |
| Get several attempts at one brief, merged into the best one | [`arena`](../arena/guide.md) |
| Run parallel checks over slices, or race workers, as isolated Codex workers | [`swarm`](../swarm/guide.md) |
| Have different models review a diff and try to break it | [`interrogate`](../interrogate/guide.md) |
| Fix a bug test-first when a cheap local test exists | [`tdd`](../tdd/guide.md) |
| Apply TypeScript rules to `.ts` or `.tsx` work | [`typescript-best-practices`](../typescript-best-practices/guide.md) |
| Strip comments before review, using a reviewer that didn't write them | [`no-comments`](../no-comments/guide.md) |
| Clean AI tells out of prose | [`unslop`](../unslop/guide.md) |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | [`technical-writing`](../technical-writing/guide.md) |
| Hear the last reply again in plain words | [`bro`](../bro/guide.md) |
| Give agents a scripted way to drive the app and prove behavior | [`create-verification-skill`](../create-verification-skill/guide.md) |
| Bring a verification skill and its feature map back in line with the app | [`maintain-verification-skill`](../maintain-verification-skill/guide.md) |
| Vet a performance number before reporting or acting on it | [`benchmark-checklist`](../benchmark-checklist/guide.md) |
| Run a large or cross-cutting change, or one to review after stepping away | [`figure-it-out`](../figure-it-out/guide.md) |
| Keep a decision log during a run, and review it afterward | [`show-me-your-work`](../show-me-your-work/guide.md) |
| Pick a model for each role and a reasoning budget | [`setup-pstack`](../setup-pstack/guide.md) |
| Turn their own working habits into a personal mode skill | [`automate-me`](../automate-me/guide.md) |
| Turn what a finished task taught into skill edits | [`reflect`](../reflect/guide.md) |
| Stop agents from repeating the same mistakes in this repo | [`correct`](../correct/guide.md) |
| Build a page whose buttons wake an actual configured agent service over a webhook | [`make-bot-ui`](../make-bot-ui/guide.md) |
| Find their way around pstack | `poteto-help` |

If a skill directory next to this one is missing from the table, read the named guide and route by its stated purpose. The `principle-*` directories are covered under principles below.

Close calls:

- `how` explains what the code does. `why` explains the reasons. `teach` runs one or both and explains the result plainly.
- `arena` gives every worker the same brief and merges the best parts. `swarm` splits work into slices or a race and returns one report.
- `architect` implements right after it settles the design. Add "with checkpoint" to review the design before it writes code.
- `interrogate` reviews the diff. `blast-radius` looks for breakage outside the diff and proves the one fact that makes the change safe.
- `recall` rebuilds context across recent chats. `ketchup` covers only this chat since the user's last message. Resuming one specific chat or branch is the Session pickup playbook.
- `figure-it-out` designs one rigorous run. The Orchestrate playbook runs a program that spans days and many PRs. The Autonomous run playbook drives one task to a finish condition.

Runtime tool mappings and companion diff/surface behavior live in the Codex runtime contract. The complete bundle registers these specialist names with Codex dollar-name syntax; tdd and teach use pstack-tdd and pstack-teach.

## Playbooks and principles

Playbooks are step lists inside `$pstack`, not skills, so they have no slash command. Inside `$pstack`, describing the task picks one, and these phrases name one directly:

- "babysit this pr" or "check on pr 123" runs Babysit. It drives the PR to merge-ready and stops there. It doesn't merge unless the user asks to merge, land, or ship.
- "land the stack" runs Shipping.
- "take over this branch" runs Session pickup.
- "pause safely" runs Pause safely.
- "full autopilot on this queue" runs Autopilot-full. "stack them, don't ship" runs Autopilot-stack.
- "run the eval playbook" runs Eval.

Use $pstack when you want this bundled playbook to own the request. The Playbooks section of [`poteto-mode`](../poteto-mode/guide.md) lists every playbook and when it applies. [Guide page 6](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/docs/guide/06-verify-and-ship.md) covers opening, babysitting, and landing a PR.

For plan-only requests use the Multi-phase plan playbook; it produces the plan rather than implementation. For work that spans phases or stacked PRs, asking `$pstack` for a plan runs the [Multi-phase plan playbook](../poteto-mode/playbooks/multi-phase-plan.md), which writes the plan and doesn't implement it. For a design question, the Prototype playbook or `architect` settles it in code first.

Principles are one-rule skills that `$pstack` reads and cites in its replies. The user rarely invokes one. They steer with the names instead, as in "apply prove it works. show me the real output." Ask $pstack to apply the named principle to load its guide on demand. [Guide page 8](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/docs/guide/08-principles.md) lists them.

## Fix a run that went wrong

| Symptom | Fix |
| --- | --- |
| Mode stopped applying | Reinvoke $pstack or restore explicit mode intent in the handoff. |
| Question mistaken for the next task | State the new task or say the turn is help-only. |
| Role choice had no effect | Verify the approved pstack JSON preferences are read and validated on invocation. |
| More tokens than expected | Inspect panel count and budget; retain required verification coverage, and choose supported effort/model settings explicitly. |
| Specialist didn't load | Use the installed dollar-name entry point, or invoke $pstack with the named specialist. The core resource bundle is required. |
| Workers overwrite files | Give explicit owned checkouts or disjoint files. Same-host delegates share the filesystem. |
| Overnight promise without progress | Require a checkable done predicate and an actually requested future-wakeup automation. |
| Claimed success from green build | Require actual runtime action/result evidence and fresh independent acceptance. |

For task prompts and practical one-line steers, read
[prompting](references/prompting.md) and [recipes](references/recipes.md).

## Make pstack my own

- [`automate-me`](../automate-me/guide.md) drafts a personal mode skill from the user's own history, to use alongside `$pstack`.
- [`reflect`](../reflect/guide.md) after a session turns its lessons into skill edits the user approves.
- `$poteto-mode write a skill for <workflow>` runs the authoring playbook. The eval playbook tests a skill change blind.
- Diagnose a misbehaving skill separately; repair it or open a PR only within the authorized scope.

[Guide page 9](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/docs/guide/09-make-it-yours.md) covers each of these.

## Reply

Lead with the answer. Give at most one example prompt in a code block, adapted from [`references/recipes.md`](references/recipes.md) when one fits, then the link to that file. Keep it short unless the user asked for the whole map.
