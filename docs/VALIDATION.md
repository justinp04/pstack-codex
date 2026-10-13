# Validation and limits

The local 2026-10-13 upstream-fidelity audit compared upstream main and the
pinned source; both were 1dcc2bacde73ddd284803b7af28164d0436198fc.

## Checks performed

- Independent semantic comparisons of all playbooks and specialist guides,
  followed by independent acceptance review of restored requirements.
- Upstream helper suite: 63 passed, 0 failed, 232 assertions across 5 files.
- Declared helper TypeScript typecheck passed.
- Plan validator accepted a complete plan and rejected missing live lane,
  pass predicate and performance baseline cases.
- Worktree classifier preserved paths containing spaces and did not treat
  absent chat evidence as permission to delete; no worktrees were removed.
- Isolated setup created a project verification skill and actual feature map,
  exercised a real CLI journey and retained evidence after cleanup.
- Independent verification passed; a negative control reproducing the original
  first-match bug failed its behavior assertion and retained failure evidence.
- Codex skill metadata validation, local links, packaging and attribution
  checks passed. The installable skill was copied without runtime changes.

These are scoped checks, not a claim that every playbook was executed.

## Reproduce package and helper checks

Run `python3 scripts/check_package.py` from any directory. No dependencies are
required for that packaging check. It is not a full YAML/schema validator.

For helper tests, use an owned scratch copy of
`skills/pstack/references/workflows/poteto-mode/scripts/`. With Bun available,
run `bun install --frozen-lockfile`, then:

```sh
bun test orch watch-pr check-plan.test.ts
bun run typecheck
```

The tests use fake forge responses and temporary stores. They do not merge
real PRs or prove current account/forge access. Bootstrap may install missing
dependencies; read helper-tools.md before executing it and respect actual
network/sandbox permissions. Do not treat watcher READY or a head-only ledger
row as independent acceptance at the current base/head.

## Not established

Real forge merges/thread mutations, UI/webhook integrations, remote fleets,
provider-diverse panels, Benny triggers, and unattended automations were not
exercised. Model preferences are instruction-based, not native host settings.
Project feature-map checks used an isolated fixture; each consumer must set
up and prove their own application's journeys. This port remains experimental.
