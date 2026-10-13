> Codex port: apply [the runtime contract](../../../codex-runtime.md) before this workflow.

### Worktree and simulator cleanup

1. Inventory actual disk usage, attached Codex worktrees, git worktree list,
   branch tips, uncommitted/untracked files, merge ancestry, and PR state.
   Inspect paths reported by tools, not guessed paths. Do not scan chat stores.
2. Classify each candidate as active, dirty, unmerged, merged, or unknown.
   Record what must survive, including ignored artifacts and local commits.
   Unknown and active work stay out of the cleanup set.
3. Present the concrete candidates, expected reclaimed space, and preservation
   plan. Apply the user's deletion scope and host authorization. Never remove
   primary/shared checkouts or files solely because they look old.
4. Prefer Codex archive_worktree for attached managed worktrees: it creates
   a recoverable snapshot. Preserve needed ignored files separately. Follow
   its restrictions. For unmanaged worktrees, use git worktree remove only
   after proving the work is preserved and removal is authorized; no force.
5. Simulator runtimes/caches are separate candidates. Inspect platform tools
   and usage, and act only on specifically authorized safe candidates. No
   blanket simulator delete-all or application-state cleanup.
6. Re-read disk and worktree state. Report actual reclaimed space, snapshots,
   preserved items, and excluded candidates with reasons.
