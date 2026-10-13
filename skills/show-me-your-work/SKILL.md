---
name: show-me-your-work
description: "Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a reviewer needs the trail to trust the result. Use for $show-me-your-work, autonomous or multi-phase runs, or work a human reviews after stepping away."
---

# pstack: show-me-your-work

This entry point selects the upstream `show-me-your-work` workflow. Resolve links
from this installed skill directory, not the project's working directory.
Read the shared [Codex runtime](../pstack/references/codex-runtime.md),
[core constraints](../pstack/SKILL.md), and
[selected workflow](../pstack/references/workflows/show-me-your-work/guide.md).

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
