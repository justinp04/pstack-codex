---
name: create-verification-skill
description: "Generate a project-local verification skill that drives your app the way a user does — any language, framework, or platform. Use for $create-verification-skill, \"make a control skill for this repo\", or when a project has no scripted way to prove UI/CLI/service behavior."
---

# pstack: create-verification-skill

This entry point selects the upstream `create-verification-skill` workflow. Resolve links
from this installed skill directory, not the project's working directory.
Read the shared [Codex runtime](../pstack/references/codex-runtime.md),
[core constraints](../pstack/SKILL.md), and
[selected workflow](../pstack/references/workflows/create-verification-skill/guide.md).

Run that selected workflow, loading its relevant references by their actual
paths. Create its checklist before task actions. The named selection takes
precedence over the coordinator's general playbook routing. Preserve the
user's scope, actual tool/model limits, independent verification and evidence
requirements. Do not substitute another installed skill with a similar name.

This selects one specialist; it does not activate persistent coordinator mode unless requested.

The companion `pstack` skill must be installed alongside this entry point.
If its resources are missing, stop with a precise installation gap rather
than guessing paths or claiming the workflow ran. Install the complete bundle
or the core plus this entry point.

Original pstack by Lauren Tan; see [MIT attribution](../pstack/LICENSE).
