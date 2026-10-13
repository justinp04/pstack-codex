> Codex port: apply [the runtime contract](../../codex-runtime.md) before this workflow.

# Comment review

1. Scope the requested files or diff against the actual base. Give a fresh
   reviewer that did not write the comments the scope, runtime contract,
   and `references/comment-reviewer.md` prompt. Keep the review read-only.
2. Inspect every finding against surrounding code. Remove narration, stale
   debug notes, and commented-out code when justified. Keep legal headers,
   public API contracts, and non-obvious reasons code cannot express.
3. Investigate claimed constraints through how/why. Preserve safety warnings
   and suppressions while unresolved. An accepted refactor encodes the
   constraint in types, a test, validation, or naming before removing its
   explanatory comment. Never erase an unresolved constraint by styling it
   as a comment cleanup.
4. Apply only in-scope accepted fixes. A substantial redesign uses architect;
   an out-of-scope root cause is reported, not silently expanded. Rerun the
   relevant behavior checks after changes. Report unresolved constraints
   and rejected findings with evidence.

## Review completeness

Scan scoped lint and TypeScript suppressions as well as ordinary comments.
Distinguish style-only ignores from correctness/safety suppressions. Review
reports must not edit application code, escape scope, or delete a protected
constraint without a verified replacement. Reject such a report and rerun
once with the specific failure named; a second rejection leaves review FAIL.
Investigate ambiguous claims with how/why. If a root-cause fix needs structure,
run architect for the accepted set, then implement the smallest in-scope fix.
Report deletions, restorations, reruns, accepted/rejected flags, architectural
sketches, encoded constraints, and unresolved/out-of-scope findings. Preserving
unresolved safety constraints intentionally differs from upstream aggressive
deletion; it is not permission to skip their investigation.
