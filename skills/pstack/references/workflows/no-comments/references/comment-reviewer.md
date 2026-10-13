> Codex port: apply [the runtime contract](../../../codex-runtime.md) before this workflow.

# Independent comment reviewer

Read the actual scoped diff and nearby code. Return findings only; do not edit.
Flag comments that narrate obvious code, stale comments, debugging notes,
commented-out dead code, and claims contradicted by runtime evidence.

Keep legal/license headers, public API contracts, useful issue/RFC references,
and non-obvious platform or domain constraints. Investigate correctness/safety
suppressions and proposed deletions of warnings; preserve them until the
underlying issue has been resolved and verified. A missing proof is an open
finding, not authorization to delete. Identify a simpler encoding where it
fits the user's scope. Report file/line, observation, evidence, proposed
action, and unresolved questions. Do not widen the application-code scope.
