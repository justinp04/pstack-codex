> Codex port: apply [the runtime contract](../../../codex-runtime.md) before this workflow.

### Autonomous run

**You own the exit condition. Define done, then drive to it without stopping.**

1. State the exit condition as a checkable predicate before the first iteration (tests green, repro fixed, all N PRs merged, pixel-diff zero).
2. Use actual event waits and scoped watcher agents within the active turn. If future recurring work is explicitly requested, configure a real Codex heartbeat with meaningful-change notifications. Without that grant, preserve a handoff at turn end and never claim a future loop exists.
3. Each iteration makes the smallest change the evidence justifies, verifies it against the predicate, commits if it advanced, discards changes that didn't help. Belt-and-suspenders that "might help" gets reverted, not left to ride.
   Sequence the work via the **sequence-verifiable-units** principle skill, verifying each unit before the next instead of batching checks at the end.
4. Diagnose blockers, flaky verifiers, tooling failures, review noise, and drift within the task. Record unrelated discoveries as scoped follow-ups; do not automatically open out-of-band repair PRs. Do not park reversible work for the human or use the available Codex clarification tool. Surface only irreversible actions, genuine product or preference calls no experiment can settle, or a real dead end. Keep the predicate as the main drive, and return to it after each side fix.
5. Checkpoint every iteration via the **show-me-your-work** skill, a row for what changed and whether the predicate moved.
6. Stop when the predicate is met. A plateau is not a stop, so keep going and pivot your approach to push past it. Surface a genuine dead end rather than spinning, and never relax the predicate to declare victory.

**Reply:** the exit condition, iterations run, what landed, what was discarded, final predicate state.
