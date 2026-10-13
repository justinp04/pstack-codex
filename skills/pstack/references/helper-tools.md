# Restored helper tools

These upstream tools are optional executable support, not Cursor APIs. Their
procedures remain subject to [the Codex runtime contract](codex-runtime.md).
Resolve paths from the mode guide directory, not the user's working directory.

- `workflows/poteto-mode/scripts/check-plan.mjs`: Node standard-library plan
  validator for full structure, ten live lanes, predicates, performance blocks,
  interaction gates and appendices. Run with `node <absolute-path> <plan.md>`.
- `workflows/poteto-mode/scripts/watch-pr/watch-pr`: Bun + authenticated gh
  readiness watcher, including review threads, bot passes, check fallbacks,
  pagination, stacks and adaptive cadence. Use `bun <absolute-path> --help`.
  `--status-only` is a one-pass check. No watcher verdict grants merge authority
  or replaces independent exact-base/head proof. Stop at the playbook boundary.
- `workflows/poteto-mode/scripts/orch/orch.ts`: Bun bookkeeping CLI backed by
  atomic/locked validated store files. It never spawns/wakes agents. Resolve
  an existing Graphite frontier only when gt actually exists; otherwise use
  its actual `frontier set --repo <repo>` command only for a real Graphite
  stack. There is no --file import flag in the upstream CLI. Without gt,
  compute an ordered forge/git frontier in the single coordinator-owned
  ledger, preserve the same generation/revision invariants, and disclose
  that automated Graphite resolution is unavailable. Use `frontier show`
  only for a store populated through supported operations. Never infer
  topology from invented metadata.
- `workflows/poteto-mode/scripts/worktree-audit.sh`: git/gh/jq/du classification
  with optional explicitly supplied PSTACK_TRANSCRIPTS export. It fetches the
  named origin base when applicable (updates tracking refs), never deletes
  worktrees. Buckets are suggestions requiring preservation and actual active
  work checks, not deletion approval. BSD-stat transcript dating is macOS-only;
  omit transcript export or adapt that observation on other systems.
- `workflows/show-me-your-work/scripts/log.sh`: portable TSV decision trail.

Watcher/store helpers need Bun and package dependencies. Upstream bootstrap
performs bun install --frozen-lockfile if dependencies are missing, writes a
local install marker, and restarts its command. Do not run it from a read-only
or shared installed directory blindly. Prefer copying the scripts to a task
scratch directory, then resolving dependencies there under actual sandbox/
network permission. No global Bun or package install is required by the skill.
When unavailable, use real forge reads/plain tables with equivalent invariants
and report the limitation. Preserve all original helper tests in that scratch
workspace. Test with `bun test orch watch-pr check-plan.test.ts` and run the
declared typecheck. Only metadata/host-marker strings were changed in the plan
validator; script outputs remain evidence, not substitutes for actual behavior.

For orchestration, initialize with `bun <absolute-mode-directory>/scripts/orch/orch.ts
--store <absolute-task-store> init` (one command line; line wrap here is prose).
Pass --store on later commands, or set the explicitly task-scoped ORCH_STORE.
The optional frontier resolver is Graphite-specific; all other store tables,
locks, validated receipts, gates and inbox operations remain usable without gt.
The port retains a forge/git single-writer frontier fallback rather than
inventing an unsupported import flag. Its current base must still be verified
separately because the upstream ledger keys only PR/head, not base SHA.
