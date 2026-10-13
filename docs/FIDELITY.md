# pstack Codex upstream-fidelity audit

Compared pinned and live upstream main on 2026-10-13. Both were
`1dcc2bacde73ddd284803b7af28164d0436198fc`, version 0.15.21.

The initial port unnecessarily simplified several workflows. Matching guide
filenames did not establish semantic fidelity. Those losses are now corrected
in this published skill package.

## Restored capabilities

| Area | Restoration |
| --- | --- |
| Setup | Actual model detection, inherited defaults, four budgets, validated per-role/panel choices, optional idempotent project/personal preferences, and verification harness/feature-map inspection and offer. |
| automate-me | The actual personal-style skill workflow: existing-mode update preservation, scoped history mining, repeated-evidence confidence, user interview, clustering, authoring and iteration. Its incorrect scheduling replacement is removed. |
| Recall | Explicit topic/workspace/time window, seven-day default, efficient sliced mining, mandatory shared-record why sweep for a named subsystem, live-state checks, and capsule/status tags/problems/next move. |
| Reflect | Three review lenses, synthesis, structural enforcement routing, authorized accepted-change scope, trivial/substantive/trigger/new-skill routing and full outcome reporting. |
| Help | Full specialist map, routing distinctions, customization, troubleshooting and prompting/recipe references. |
| Planning | Complete ordered plan skeleton, ten live scenario lanes, boot/evidence recipes, trunk regression, perf blocks, interaction screenshot/video review gates, appendices and executable linter. |
| PR lifecycle | Conventional title and one-minute briefing template, ordered commits, stack parent semantics, continue-building handoff and separately requested babysitting. |
| Babysit | Lowest frontier, single babysitter, no topology mutations, owning-PR fixes, conflicts/threads/CI order, one fresh-build flake retry with reclassification, bot triage and actual watcher stop conditions. |
| Orchestrate | No-code coordinator boundary, full briefs/standing orders, pilot, rolling refill, continuous authorized landing, single-writer store, completion drains, child accounting, bounded retries, late-result reconciliation and durable close/handoff. |
| Autopilot | Early durable checkpoints, children/liveness ledger, committed-head checks, safe authorized lease publication, owner/root topology boundaries, budget countersigns after verifier proof, holds and final drains. |
| Delegation/autonomy | Fresh consolidated scopes, costly-live-state reuse exceptions, ownership of worker diffs, candid judgment, smallest evidence-backed iterations and discard/pivot/predicate discipline. |
| Helpers | All 21 original plan-linter, GitHub-watcher, atomic store, worktree-audit, bootstrap/package/lock/test files. Dependencies are explicit and optional. |
| Supplemental material | Original tutorials/artwork/agent prompts and dormant Benny extension source preserved as historical references. Cursor-only integrations are not falsely presented as working Codex features. |

All 52 top-level upstream skill definitions (51 specialists plus the mode),
all 23 playbooks, and all upstream skill support files have mapped destinations.
The complete mapping is [file-parity.json](file-parity.json). Three source packaging files
are deliberately excluded: .gitignore, the portable plugin.json, and the
Cursor-specific plugin manifest. The port is a single Codex skill layout;
installing the original manifests would not wire this layout correctly.
The MIT license and original README source are retained.

## Intentional Codex differences

Actual tools/models replace unsupported Cursor arguments and providers. Models
inherit by default, with user-approved pstack JSON preferences read by the
skill rather than pretending to modify native Codex settings. Delegates share
a filesystem unless explicitly isolated. Ten lanes queue within host capacity.
Future wakeups require a real explicitly requested automation.

No private chat-store inference, blanket external messages, out-of-scope repair
PRs, destructive dirty-work resets, or deletion of unresolved safety constraints.
Every base/head change requires fresh independent verification even when patch
IDs match. Watcher readiness and head-only ledger rows never waive live/diff
proof or base validity.

Graphite frontier discovery requires real gt metadata; the source CLI has no
invented --file import flag. Without Graphite, the coordinator uses an explicit
forge/git single-writer frontier ledger. Historical source commands/Benny
trigger APIs stay reference-only until a supported authorized integration exists.

## Validation performed

- Two independent source comparisons identified semantic omissions.
- A separate independent reviewer rechecked restorations and corrected findings;
  final static acceptance PASS within reviewed scope.
- Helper suite: 63 tests passed, 0 failed, 232 assertions across 5 files.
- Declared helper TypeScript typecheck passed.
- Plan linter accepted a complete plan and rejected each missing live lane,
  pass predicate, and performance baseline.
- Worktree classifier preserved paths with spaces, did not treat missing chat
  evidence as deletion approval, and removed no worktrees.
- Isolated setup created a grounded verification skill and actual feature map;
  real CLI journeys passed and evidence survived cleanup.
- Independent generated-harness run passed; a negative control restoring the
  original bug failed its behavioral assertion and retained failure evidence.
- Both generated-skill and pstack metadata validators passed.
- Resource links, one discoverable skill, all playbook categories, portable
  instruction scan and attribution checks passed.
- The audited skill package contained 171 files; the local installed copy matched it exactly before publication.

## Remaining limits

This does not prove every playbook in production. Real forge merges and thread
mutations, UI/webhook integrations, remote fleets, provider-diverse panels,
Benny triggers and unattended automations were not exercised. Helper tests
use fake forge responses. Model preference persistence is instruction-based,
not native host configuration. Feature-map execution used an isolated fixture;
a consumer's actual application must be initialized separately. This audit describes the pre-publication fidelity review.
