> Codex port: apply [the runtime contract](../../codex-runtime.md) before this workflow.

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active history

Read this conversation or an explicitly scoped accessible Codex chat through
thread tools. Use raw history when exposed, otherwise a source-linked digest
of goals, decisions, tools, results, and failures. State missing raw-history
limits. Do not scan private chat stores or unrelated projects.

## 2. Spawn three reviewers in parallel

Use three fresh read-only default-role Codex reviewers with the runtime contract and available tool access. Read role choices from explicit validated model preferences; otherwise inherit the parent. Queue within actual host capacity.

| Lens | Role line | Default `model` | Prompt template |
|---|---|---|---|
| Judgment | `reflect judgment, divergent, synthesizer` | `inherit-parent` | `references/judgment-reviewer.md` |
| Tooling | `reflect tooling` | `inherit-parent` | `references/tooling-reviewer.md` |
| Divergent | `reflect judgment, divergent, synthesizer` | `inherit-parent` | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. Reviewers return delivered final reports; spawn_agent returns identity, not the review. Observe delivered results and actual wait/list tools before synthesis.

## 3. Synthesize

Use one fresh read-only synthesizer under the runtime model contract. It spot-verifies citations with actual available tools. Pass `references/synthesizer.md` verbatim, with each reviewer's full output inlined where marked. It returns an Accepted / Rejected / Backlog list.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and apply Accepted edits only when those specific changes are already authorized, otherwise request approval before applying them. The user picks the subset and may redirect routings. Shared skill changes affect future users of the modified skill. Do not auto-apply.

Keep Backlog items in a task-local artifact unless external tracker filing is authorized. Preserve the explicit approval gate for Accepted edits unless the user already authorized the specific edits under review.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to Codex's `skill-creator` skill and run its draft / test / iterate loop.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): hand to `skill-creator` and run its description-optimization loop.
- `new skill via create-skill: <kebab-name>`: hand creation to `skill-creator`. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
