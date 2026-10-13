> Codex port: apply [the runtime contract](../../codex-runtime.md) before this workflow.

# Setup pstack for Codex

Setup configures optional model roles and checks the project verification
harness. Model defaults can stay inherited; the feature-map check still runs.

## 1. Detect actual capabilities

Inspect the actual Codex delegation schema for available models and supported
reasoning efforts. Do not guess slugs, combine model names with effort suffixes,
or assume cross-provider models are available. inherit-parent and auto mean
omit model/effort overrides. Check context-isolation and concurrency support.

## 2. Load existing choices

When in a repository, read `.agents/pstack-models.json` if it exists. If the
user has configured personal pstack choices, read `~/.codex/pstack-models.json`.
Project roles override matching personal roles; absent roles inherit. These
are pstack preferences read by this skill, not native global Codex settings.
Preserve previously chosen models and aliases on a budget-only update. Show
unknown/retired roles before removing them. No config file is needed to run.

## 3. Choose budget and roles

Offer the upstream budget levels with supported effort targets:

- unlimited: max reasoning.
- large: xhigh reasoning.
- medium: high reasoning.
- small: medium reasoning.

Show the current budget, or inherited settings when no budget is configured.
An inherited role remains inherited until the user chooses an explicit model
or effort. For explicit choices, use the highest effort supported at or below
the target; show any downgrade. Never turn an unavailable slug into a guess.

Show all roles: feature/refactoring, bug-fix, perf-issue, hillclimb, judgment
and prose, hardest tasks, how explorer/explainer, why investigators/synthesizer,
reflect tooling and judgment/divergent/synthesizer, arena runners/cross-judge
pool, swarm workers, architect runners, and interrogate reviewers. Panel values
are lists; every entry is a separate seat, inherited entries included. More
seats queue within capacity. Arena selects a cross-judge different from the
parent's model family only when such a model is actually available/authorized.
Same-model independence is labeled honestly.

Use the actual clarification tool for the budget and role preferences. Keep
questions concise. If the user wants defaults, continue without manufacturing
configuration. Ask whether choices should be task-local, project-wide, or
personal only when persistence matters and the request did not specify it.

## 4. Validate and persist when requested

Validate every explicit model/effort pair against the actual host schema.
Model and reasoning_effort are separate fields. Invalid selections stay open.
For persisted preferences, write versioned JSON with `version: 1`, `budget`,
and `roles`. A role is an object `{ "model": "inherit-parent" }`, or an
explicit available model plus optional `reasoning_effort`; panels use arrays
of these objects. Preserve unrelated roles and replace the chosen file
idempotently. Never edit native Codex config.toml to simulate Cursor rules.
Use task-local recorded choices when persistent configuration wasn't asked for.
Do not put personal paths, secrets, or credentials in model preferences.

## 5. Confirm configuration

Report inherited versus explicit roles, actual effort fallbacks, persisted
path when any, and that these preferences apply when pstack reads them on
the next invocation. No editor restart or Cursor setup command is involved.

## 6. Check the project's verification harness and feature map

Inspect for an existing verify-* skill, actual launch/drive harness, and mapped
user journeys. Reuse what works. If missing, offer once to create the
[verification skill and feature map](../create-verification-skill/guide.md).
If the user already requested that setup, proceed directly. The generator
must discover launch/doctor/drive/evidence/cleanup from the actual repository,
seed the top 3-5 feature journeys, and prove one end to end while retaining
evidence after cleanup. A broken/unavailable runtime is a named gap, never
evidence that setup is complete. If no project is identified, report that
project-specific setup needs a repository rather than inventing an app.

If a map exists but is stale, use
[maintain verification skill](../maintain-verification-skill/guide.md).
On a declined offer, stop offering until the user asks again. This project
setup is distinct from installing the global pstack skill.
