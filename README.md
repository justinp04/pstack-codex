# pstack for Codex

An unofficial, experimental Codex adaptation of **[pstack](https://github.com/cursor/plugins/tree/main/pstack) created by [Lauren Tan](https://github.com/poteto)**.

Lauren designed the original engineering principles, specialist workflows and
playbooks. This repository adapts that work to Codex's available tools and
authorization model. It is maintained by [Justin Pan](https://github.com/justinp04)
and was prepared with Codex. It is not an official Cursor, OpenAI or Lauren Tan
release, and does not imply their endorsement.

pstack gives Codex a structured approach to investigation, implementation,
review and verification. The port retains all **23 playbook categories** and
**52 upstream guide definitions**, including the coordinator mode, along with
supporting references and optional helper tools.

## Install

In Codex, ask its built-in skill installer:

```text
Use $skill-installer to install the pstack skill from
https://github.com/justinp04/pstack-codex/tree/main/skills/pstack
```

The installable directory is **skills/pstack**, not the repository root.
This is a skill repository, not a Cursor plugin; `/add-plugin pstack` does not
install this port. The skill installer refuses to overwrite an existing
installation. Back up an existing pstack skill and review differences before
replacing it. The installed skill is available on the next turn.

For a manual installation on macOS/Linux, choose a fresh checkout directory:

```sh
git clone https://github.com/justinp04/pstack-codex.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
```

Copy `pstack-codex/skills/pstack` into that skills directory only if `pstack`
does not already exist there. Use the installer for platform-specific handling.

## Set up each project

Open your application's repository in Codex and run:

```text
$pstack Set up this project. Keep the current model defaults,
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

You can name a specialist in a `$pstack` request: `recall`, `architect`, `arena`,
`interrogate`, `reflect`, `automate-me`, or `create-verification-skill`.
`automate-me` creates a personal working-style skill; it is not a scheduler.
These are bundled guide names, not independently registered slash commands.

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
