---
name: make-bot-ui
description: "Use when creating a custom UI that sends validated actions to a configured webhook agent service, including server-held credentials and optional Tailscale exposure."
---

# pstack: make-bot-ui

This entry point selects the upstream `make-bot-ui` workflow. Resolve links
from this installed skill directory, not the project's working directory.
Read the shared [Codex runtime](../pstack/references/codex-runtime.md),
[core constraints](../pstack/SKILL.md), and
[selected workflow](../pstack/references/workflows/make-bot-ui/guide.md).

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
