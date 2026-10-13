# pstack for Codex

An unofficial, experimental Codex adaptation of **[pstack](https://github.com/cursor/plugins/tree/main/pstack) created by [Lauren Tan](https://github.com/poteto)**.

Lauren designed the original engineering principles, specialist workflows and
playbooks. This repository adapts that work to Codex's available tools and
authorization model. It is maintained by [Justin Pan](https://github.com/justinp04)
and was prepared with Codex. It is not an official Cursor, OpenAI or Lauren Tan
release, and does not imply their endorsement.

pstack gives Codex a structured approach to investigation, implementation,
review and verification. The port retains all **23 playbook categories** and
**52 upstream guide definitions**, including the coordinator mode. Each original
workflow has a direct Codex entry point, backed by shared references and optional
helper tools.

## Install

For all original entry points, install the complete bundle:

```sh
git clone https://github.com/justinp04/pstack-codex.git
cd pstack-codex
python3 scripts/install_skills.py
```

The installer honors CODEX_HOME and installs **53 skills**: the shared pstack
core plus 52 original workflow entry points. Identical existing copies are
preserved. Different existing skills cause a refusal before any changes;
back up and review an older owned pstack installation before replacing it.
It never overwrites unrelated skills to resolve conflicts.

For a smaller install, ask the built-in installer for the core and selected
entry points, for example:

```text
Use $skill-installer to install skills/pstack and skills/setup-pstack
from justinp04/pstack-codex.
```

If the compatible core is already installed, request only the missing entry
point. Wrappers require the sibling pstack core; installing a wrapper alone
without that core cannot run its workflow. The repository root is not a skill
and Cursor's /add-plugin command does not install this port. Start a fresh chat
after installation; restart Codex if the new names do not appear in its picker.

See [the complete entry-point map](docs/ENTRYPOINTS.md) for installation paths,
invocation policies and name differences.

## Set up each project

Open your application's repository in Codex and run:

```text
$setup-pstack Set up this project. Keep the current model defaults,
reuse existing verification harnesses, and create a feature map if missing.
```

Setup includes optional reasoning budgets and per-role model choices, followed
by inspection of the project's real launch/drive harness and feature map.
If missing, it offers to create a project-local `verify-<app>` skill. When you
already requested creation, it proceeds directly. The generator discovers how
to launch, check, drive, observe and clean up the actual application, maps its
user-facing features, and proves one mapped journey end to end. Evidence must
survive cleanup. **Installing pstack alone does not initialize your project.**

Models inherit the current chat by default. Explicit model preferences can be
recorded in `.agents/pstack-models.json`, or `~/.codex/pstack-models.json` when
personal persistence is requested. These are preferences read by pstack,
not native Codex model configuration. Only available, user-approved model and
reasoning-effort combinations are used; no Claude/Grok access is implied.

## Use

```text
$pstack Fix this bug. Reproduce it on the real surface first,
then verify the fix. Local changes only.
```

```text
$pstack Explain how authentication works and why it is structured this way.
Read-only; cite the source and flag uncertain conclusions.
```

```text
$pstack Create a multi-phase plan for this migration. Plan only.
```

```text
$pstack Review this PR and bring it to merge-ready. Do not merge.
```

You can invoke specialists directly: `$recall`, `$architect`, `$arena`,
`$interrogate`, `$reflect`, `$automate-me`, or `$create-verification-skill`.
You can still name them in a `$pstack` request.
`automate-me` creates a personal working-style skill; it is not a scheduler.
Codex uses dollar-name skill invocation; Cursor slash commands are not registered.
`$poteto-mode` is the original coordinator entry, and `$pstack` remains its
convenience entry. `$pstack-tdd` and `$pstack-teach` avoid replacing other
installed tdd/teach skills. Other upstream names are preserved. Every specialist
except setup retains upstream explicit-only invocation, so the full bundle
does not enable dozens of competing automatic workflows.

Explicit mode activation carries through the chat until you opt out. Say
“Keep pstack mode on” or “Stop pstack mode.” This is a conversational convention,
not a global Custom Mode. Invoke `$pstack` again in a new chat, and preserve
mode intent in handoffs.

## What differs from upstream

| Upstream assumption | Codex adaptation |
| --- | --- |
| Cursor Task/agent flags and hardcoded provider models | Actual host tools and validated roles; models inherit by default. |
| Cloud agents and dedicated machines | Explicit checkout/file ownership; same-host delegates share a filesystem. Required lanes queue within capacity. |
| Cursor `/loop` and private transcript stores | Active-turn event waits, accessible scoped history, and real requested Codex automations for future wakeups. |
| Blanket external action defaults | The user's task controls PRs, messages, pushes, merges and schedules. The mode itself adds no action grant. |
| Patch-ID waivers after a rebase | Exact base/head changes require fresh independent verification. |
| Aggressive comment deletion and destructive checkout repair | Preserve unresolved safety constraints and unrelated work; use owned checkouts and recoverable archives. |
| Companion control/deslop skills | Available real surface drivers and scoped diff-hygiene instructions. |

Reproduce-first debugging, evidence-backed hypotheses, behavioral tests,
baseline measurements, independent acceptance, ten-lane program verification,
operator review for interaction changes, and bottom-up stack safety remain.
Missing or inconclusive proof is **BLOCKED/FAIL**, never a passing receipt.

See [the complete differences](docs/DIFFERENCES.md),
[upstream fidelity audit](docs/FIDELITY.md), and
[validation limits](docs/VALIDATION.md).

## Requirements and optional tools

Codex must support skills and the tools your application's proof needs. Fresh
independent acceptance requires an available subagent mechanism; unavailable
independence remains a named blocker. Real UI/CLI/API verification also needs
the corresponding driver or project harness. Shell access alone does not prove
a UI works.

The instruction workflows need no new dependency by default. Optional bundled
helpers include a Node plan validator, Bun/gh PR watcher, atomic orchestration
store, and a worktree classifier. Read
[helper tools](skills/pstack/references/helper-tools.md) before running them.
The watcher observes readiness; it never grants merge authority. Graphite
frontier discovery is optional and requires actual `gt` metadata. Helper
dependencies should be prepared in an owned scratch workspace rather than
silently modifying the shared installation.

Original tutorials, artwork, agent prompts and the dormant Benny automation
pack are retained as [historical source](skills/pstack/references/upstream-materials/INDEX.md).
They do not register or enable Cursor webhook/Slack triggers in Codex.

## Validate this package

```sh
python3 scripts/check_package.py
```

This checks packaging, attribution and local resource links. It does not prove
runtime behavior. The optional upstream helper tests are documented in
[VALIDATION.md](docs/VALIDATION.md). No blanket claim of production readiness
is made for merges, webhooks, UI or unattended execution.

## Attribution, license and maintenance

The original pstack is by **Lauren Tan**. Preserve her copyright and the MIT
permission notice when redistributing. See [LICENSE](LICENSE) and
[ATTRIBUTION.md](ATTRIBUTION.md). The upstream revision is recorded in
[UPSTREAM.json](UPSTREAM.json); the current port is based on upstream 0.15.21.

There are no automatic upstream updates. Changes should be compared for
semantic fidelity, adapted to real Codex capabilities, and verified on the
actual affected surface. Contributions should keep the smallest complete
change, concrete evidence and honest limits. Please report reproducible issues
through this repository's issue tracker.
