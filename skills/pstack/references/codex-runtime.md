# Codex runtime contract

This contract supplies the runtime semantics for every bundled guide,
playbook, reviewer prompt, and template. Apply it before their procedural
steps. It replaces upstream host assumptions without replacing their proof
requirements. User instructions and the actual host tool contracts prevail.

## Paths and skill routing

Resolve resources from this installed skill directory, never from the caller's
working directory. The mode lives at `workflows/poteto-mode/guide.md` relative
to this file. A named bundled specialist lives at `workflows/<name>/guide.md`.
Within the mode, `playbooks/<name>.md` is relative to its directory. Within a
playbook, a `playbooks/<name>.md` cross-reference is relative to the mode
directory, not nested under the current playbook. Reference templates are
relative to their containing specialist directory. The `guide.md` files are shared support documents. The complete bundle registers
lightweight sibling SKILL.md entry points that explicitly select these guides. For authoring new
skills, the output manifest is still `SKILL.md`.

## Tool mapping

| Workflow operation | Codex implementation |
| --- | --- |
| Read, search, edit, execute | Available file tools and shell; use rg for search |
| Delegate | `collaboration.spawn_agent`, or the actual host's equivalent |
| Observe delegates | `list_agents`, delivered reports, and `wait_agent` |
| Interrupt or continue | `interrupt_agent`, `send_message`, `followup_task` as their schemas allow |
| Explore | An available explorer role with a narrow read-only brief |
| Implement | An available worker role with explicit file and checkout ownership |
| Verify or cross-judge | A fresh default-role agent with a read-only evidence brief |
| Browser/native UI | Available computer-use tools, existing harness, or relevant installed skill |
| CLI/TUI | Shell, PTY, stdin interaction, and real command output |
| Create a skill | Available Codex skill-creator guidance and validator |
| PR operations | Connected forge tools when supported, otherwise authenticated gh |
| PR attachment | Codex `attach_artifact` for every created or worked-on PR |
| Worktree isolation | Inspect attached worktrees, reuse a suitable one or create a managed worktree |
| Durable schedule | Codex automation tool, only when the user requests future or recurring work |

Do not invent unavailable tool names, agent types, cloud environments, or
flags. Codex workers can share the filesystem. Every writer receives its actual
absolute checkout path and owned files; workers must not revert others' work.
Separate writes with worktrees or disjoint files. Bound active delegates by
the host's concurrency limit; queue the remaining lanes without reducing
required scenario coverage. A role is a brief, not a special Cursor agent type.

Read-only is an instruction, not a fabricated tool argument. A reviewer may
run a safe test in its isolated scratch checkout and read connected evidence.
It must not edit the producer's files or mutate external state. Include this
root SKILL.md path, the runtime path, relevant guide/template paths, the user's
constraints, exact SHAs, required artifact, and pass predicate in each brief.

For blinded evaluation candidates and judges, use `fork_turns: "none"` when
the host supports it. Pass only the sanitized candidate brief and permitted
raw inputs to candidates; pass sanitized artifacts and the rubric to judges.
Do the same for Arena cross-judges and independent acceptance verifiers to
avoid inheriting producer conclusions. Default full-history forks are not
blinded. If the host cannot isolate context, disclose that evidence gap.

## Models and independent review

Inherit the parent model and reasoning effort by default; omit overrides.
Upstream role tables are conceptual role labels. They do not configure Codex.
Use a model override only when the user or applicable host instructions
explicitly authorize it, and only from models the host actually exposes. The
host may require a fresh context when overriding. Do not retry guessed model
names or open an unrelated repair PR when a model is unavailable.

Design candidates must be structurally different and independent. Distinct
review briefs can cover behavior, lifetimes/races, and data/config safety on
the same model. Label such a panel as same-model independent review, never
as cross-provider or diverse-family review. If cross-provider diversity is
required and unavailable, record that gap. Independence is a fresh reviewer
that did not implement the artifact, not a change of model alone.

If delegation is unavailable, do useful implementation and local verification,
but report the independent verification gate as BLOCKED. Do not silently
replace that gate with self-review or claim shipping readiness.

## Scope and authorization

Mode invocation grants the requested engineering work, not unrelated external
actions. Do not automatically send team chat, emails, PR comments, ticket
updates, deploys, merges, or automation requests. Apply the user's explicit
action scope and host authorization rules. Keep verdicts local or in this
chat unless external posting is authorized. User instructions such as
"do not merge", "do not message", "plan only", and "hold" propagate to all
workers. A full-autonomy request stays within the user's task and does not
bypass forge, sandbox, or approval restrictions.

Preserve uncommitted work. Never use reset --hard, forced removal, or sweeping
cache deletion as a worktree repair technique. A broken helper is a limitation
to diagnose; an unrelated repair is not automatically part of the task.

## Loops, orchestration, and session state

Run bounded evidence-driven iterations while this turn is active. Use tool
events or delegate completion to wait; give progress updates and avoid busy
polling. A request to keep going is not a promise of unattended execution
after the turn ends. Only an explicitly requested Codex automation supplies
future wakeups. No Cursor loop command, cloud fleet, transcript database, or private dashboard
is required. Restored watcher/store helpers are optional; read helper-tools.md
for their actual dependencies, operations, and fallback limits.

For orchestration use a small task ledger in the task workspace with unit,
owner, owned paths, dependency, branch, base/head SHA, state, verdict, and
evidence paths. Update it at wave boundaries and head changes. Keep a decision
trail through `workflows/show-me-your-work/guide.md`. Read only this chat's
context or an explicitly identified accessible chat through Codex thread
tools. Do not scan unrelated private chat stores. Resumption validates current
git and PR state, preserves prior receipts, and reruns only invalidated checks.

## Surface verification and diff hygiene

The names control-ui and control-cli in upstream guides mean the corresponding
available surface driver above. They are not dependencies on another plugin.
Use the actual application surface. An inaccessible surface is a named gap.
Compilation, lint, unit tests, a mocked API, or a reviewer assertion cannot
substitute for live proof of the behavior the change affects.

The upstream deslop step is a direct scoped diff review: remove accidental
debugging output, dead code, unused imports, needless wrappers, duplicate
validation, boilerplate, and unrelated changes. Preserve accessibility,
security guards, validation at boundaries, error handling, license comments,
and comments explaining a real constraint. Apply the no-comments guide's
review discipline; never delete a safety suppression or constraint just to
make the diff look clean. Any claim behind it must be resolved first.

## Verification receipt

Every acceptance verdict records:

- Artifact or PR, base SHA and head SHA, and base-to-head patch identity.
- Verifier identity and whether it implemented the change.
- Original reproduction or consumer scenario, actual driver and environment.
- Commands, exit codes, observed expected/actual results, and evidence paths.
- Unit/build gates, live behavior, and applicable performance evidence.
- PASS, PASS+NOTES, FAIL, or BLOCKED, with every finding and missing lane.

A known behavioral defect is FAIL even when reported as a note. PASS+NOTES
contains only non-blocking observations with reasons. Missing lanes,
wrong-surface checks, stale screenshots, and inconclusive runs do not pass.
For a dimension that cannot meaningfully apply, record N/A with a concrete
reason agreed in the plan; do not mark a required but inaccessible check N/A.
At minimum, live proof exercises the actual delivered artifact. For an
instruction skill that includes an independent realistic execution scenario.

Performance changes require a pre-change baseline and matched, preferably
interleaved, measurements. If trunk lacks a new feature, gate its added work
and user-visible end state with absolute budgets rather than inventing a
trunk/head ratio. Read the bundled benchmark-checklist before reporting gains.

Use strict exact-head verification in this port. A rebase, retarget, head,
or base change invalidates the verdict and requires fresh review, live proof,
and CI at the new revision, even if stable patch IDs match. Record patch IDs
for diagnosis, not as a waiver. Confirm remote base/head immediately before
declaring a PR verified or performing an authorized merge. Land only the
contiguous independently verified stack from its bottom. Green CI alone,
bot approval, and a producer's self-report cannot authorize acceptance.

## Optional pstack model preferences

At invocation, read existing `.agents/pstack-models.json` in the identified
project and `~/.codex/pstack-models.json` if present. Project role entries
override matching personal entries; unspecified roles inherit. These are
pstack preferences, not native host settings. Validate version 1, budget,
role objects/panel arrays, available model names and actual supported effort
pairs before use. Preserve the user's chosen aliases. Invalid or unavailable
explicit entries require a named fallback decision, not guessed slugs.
The JSON model and reasoning_effort fields map to separate host arguments.
inherit-parent/auto omits both overrides. User-authored or explicitly approved
role choices are the authority for overrides; never write choices on the
user's behalf merely to optimize a task. Context isolation and actual host
capacity still apply. Setup also checks the verification harness and feature
map even when all models stay inherited.

## Preserved helper and source material

Read [helper tools](helper-tools.md) before using the restored plan linter,
GitHub watcher, atomic orchestration store, or worktree classifier. They are
portable optional support with real dependencies, not fabricated Codex APIs.
Copy script dependencies to a task-local scratch workspace when needed;
do not silently mutate the shared installed skill. Watcher status is never
independent acceptance, and ledger head records do not waive the runtime's
base-SHA receipt checks. Ten planned live lanes are total required coverage;
schedule them in rolling available slots rather than removing lanes.

[Historical upstream material](upstream-materials/INDEX.md) preserves docs,
images, original agent prompts and the dormant Benny automation extension.
It is comparison/reference input, not executable current-host instructions.
Unsupported webhook/event integrations remain explicit gaps, not substitutes
for the retained provider-neutral procedures or actual proof requirements.
