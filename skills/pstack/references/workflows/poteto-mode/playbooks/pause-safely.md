> Codex port: apply [the runtime contract](../../../codex-runtime.md) before this workflow.

### Pause safely

Only pause when explicitly requested or when execution must end. A request
to keep going is not a request to pause.

1. Stop at a safe atomic boundary. Start nothing new. Send a hold to this
   task's active delegates and observe that writes have stopped. Preserve
   partial work before interrupting processes that may lose it.
2. Take no new external action to pause. No PR, push, merge, or automation
   unless the original action scope already covers that exact action.
3. Make only this task's owned edits durable. Commit a scoped WIP checkpoint
   when commits are authorized, otherwise save the owned patch and evidence
   in the task workspace. Never stage unrelated edits wholesale. Preserve
   and report existing dirty state; do not force the tree clean.
4. Write a resume note with original intent/authorization, mode, done/pending
   steps, owned checkout/files, revisions, verified receipts, decisions,
   running processes, next action, and gaps. Link the decision trail rather
   than duplicate it. Use a durable task-local path, not a guessed chat store.

**Reply:** safe boundary, preserved paths and revisions, dirty state, stopped
delegates/processes, verified versus unfinished work, and first resume action.
