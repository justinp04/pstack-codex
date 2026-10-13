---
name: pstack
description: Use when the user invokes pstack or poteto-mode, or requests pstack-style engineering for investigation, bug fixes, features, performance work, refactoring, PR verification, or autonomous work.
---

# pstack for Codex

Read [Codex runtime](references/codex-runtime.md) first. Then read the
[mode guide](references/workflows/poteto-mode/guide.md), select the matching
playbook, and load only its relevant specialist guides. All 23 upstream
playbooks are bundled under `references/workflows/poteto-mode/playbooks/`.
`$pstack` is the convenience coordinator entry point; the complete bundle also registers the original specialist names. A request mentioning poteto-mode uses
this same entry point; Cursor slash commands are not registered here.

After loading the relevant guides, create the selected playbook checklist as
the first task action, before inspecting task source or running a reproduction.
Maintain its steps and evidence throughout execution. Use a plan
tool when available, otherwise a small local Markdown checklist. Keep skipped
steps visible with the reason. A failed or unavailable verification stays open.

This skill explicitly requests scoped subagent delegation where a playbook
needs it. Use the runtime mapping and the actual available tools. Independent
verification must come from a fresh agent that did not write the change.

Preserve the user's scope and authorization in every brief. A read-only task
ends with a cited answer. An implementation request does not by itself request
a PR, merge, deploy, external message, or recurring automation. Execute those
steps when the user's request authorizes them. Do not let a playbook add scope.

On explicit mode activation, carry the mode through this chat until the user
opts out. Keep it in any handoff. This is a conversational convention, not a
global Codex setting. Do not activate the mode for unrelated casual questions.

Before claiming completion, rerun the relevant check on the actual artifact.
For every nontrivial implementation, including local-only fixes, obtain a
fresh independent review and verification receipt before accepting it. This
gate applies even when no PR is created. Unavailable independence is BLOCKED.
For PRs, obtain an independent verdict at the exact base and head, confirm
the remote head still matches, and attach the PR in Codex. A changed head
requires fresh verification. Report measured facts, limits, and remaining gaps.

Source attribution and port changes are in [provenance](references/provenance.md).

## Setup and named specialist requests

For setup/configuration requests, route first to
[setup-pstack](references/workflows/setup-pstack/guide.md), including its
project verification harness and feature-map check. Installation alone is
not project setup. If the user already requested a verification skill/map,
run the generator rather than ask permission for that same work again.

For a named specialist such as automate-me, recall, reflect, or make-bot-ui,
read its actual bundled guide rather than substitute a generic playbook.
Use [help](references/workflows/poteto-help/guide.md) for the complete routing
map and prompt references. The complete bundle exposes these guides through Codex dollar-name entry points; Cursor slash commands are not registered. Otherwise the mode selects the matching engineering playbook.
Read [helper tools](references/helper-tools.md) when a procedure needs them.

## Direct entry points

Specialist entry points explicitly select their named guide after loading this
core and runtime. Honor that selection rather than rerouting to a generic
playbook. They do not enable persistent coordinator mode unless the user asks;
poteto-mode explicitly activates the coordinator. The complete bundle retains
upstream invocation policies. tdd and teach use pstack-tdd/pstack-teach names to
avoid existing skills. Resource paths and implementations remain shared here.
