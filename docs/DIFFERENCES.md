# Differences from upstream pstack

The port preserves all 23 playbook categories and 52 top-level guide definitions
(including the mode), all skill support resources and optional helper tools.
The initial port simplified several procedures too far; the fidelity audit
restored those before this public repository was prepared.

| Area | Preserved behavior | Codex-specific change |
| --- | --- | --- |
| Setup | Budget/role choices, existing preferences, validation and project verification-map onboarding. | Approved JSON preferences are read by pstack; no Cursor .mdc rule or implied native Codex setting. |
| Delegation | Scoped briefs, fresh reviews, dependency context, owned outputs, rolling queues and complete coverage. | Use actual host roles/tools, inherited models and real capacity. Same-host delegates do not get separate machines automatically. |
| Models | Role/panel choices and explicit budget preferences. | Only actual available model/effort pairs. Same-model independent review is labeled honestly; provider diversity is not invented. |
| History | Recall shared-record sweep, live-state checks and structured capsule; reflection and decision trails. | Scoped accessible chat tools/exports, never guessed private transcript locations. |
| Loops | Predicate-driven iterations, events, decision rows, pivoting and durable resumption. | No unsupported /loop command or promise of work after a turn ends. Future wakeups require requested real automation. |
| Authorization | The engineer owns requested reversible work and operator gates remain explicit. | Mode invocation does not authorize unrelated PRs, messages, deployments, merges, deletions or schedules. |
| Proof | Real-surface reproduction, behavioral checks, baselines, independently reviewed receipts and stack safety. | Every base/head change invalidates acceptance; upstream patch-ID/build-noise reuse waivers are intentionally removed. |
| Program planning | Full template, ten live lanes, performance blocks, regression and interaction review. | Ten lanes are total coverage queued within capacity; evidence matches the actual surface. Inapplicable dimensions require reasons; inaccessible proof is not N/A. |
| Comment review | Investigate constraints, reject bad reports, encode root causes and report all findings. | Never delete unresolved correctness/safety suppressions merely to remove comments. |
| Worktrees | Inventory, ownership, preserved work, explicit cleanup candidates and measured reclaimed space. | No reset-hard repair or blanket simulator/cache deletion; prefer recoverable managed worktree archives. |
| Helpers | Original plan linter, watcher, atomic store, classifier, package/lock/test files. | Plan marker strings and worktree chat discovery are adapted; tools are optional, dependencies explicit. |
| Graphite | Validated ordered frontier when real metadata exists. | Optional. The CLI has no fabricated import flag; without gt use actual forge/git order in a single-writer ledger. |
| Webhook UI | Server-held credentials, validated JSON, bounded delivery, harmless probe and real wake proof. | Require an actual available webhook provider. No invented Cursor routine endpoint or secret-request card. |
| Benny/tutorials/agents | Original source preserved for reference. | Historical .md.txt files do not register skills or enable event integrations. |

The port adds explicit independent acceptance for nontrivial local-only changes.
Missing reviewers or real-surface drivers remain BLOCKED. Code is not done
because it compiles or CI is green.

This repository has a shared core under skills/pstack and 52 lightweight
entry-point skills. The source invocation policies are preserved; tdd and teach
are exposed as pstack-tdd and pstack-teach to avoid existing skills. See
[ENTRYPOINTS.md](ENTRYPOINTS.md). The upstream plugin manifests are not installed because they
do not wire this skill layout. Original MIT attribution remains intact.
