> Codex port: apply [the runtime contract](../../../codex-runtime.md) before this workflow.

### Shipping

Only enter when the user authorizes landing. Babysitting or opening a PR does
not authorize merging, auto-merge, external comments, or deployment.

1. Resolve the supported forge tools or authenticated gh, and freeze a
   bottom-to-top list of PRs with actual branch, base SHA, and head SHA.
   Spawn a fresh independent verifier for each PR in bounded waves. Each
   compares parent/base versus head on the actual surface and audits the diff.
   Record a PASS, PASS+NOTES, FAIL, or BLOCKED receipt under the runtime
   contract. Keep receipts local or in this chat unless posting is authorized.
2. Compute the contiguous verified run from the lowest unmerged PR. Stop at
   the first failing, blocked, missing, or stale verdict. A verified child
   above that gap is not landable. Report the ceiling and the blocker.
3. Record head/base SHAs and stable base-to-head git patch-id for each receipt.
   Immediately before landing, fetch and compare the current base/head.
   Any base/head change, including a rebase or retarget, requires fresh
   independent review, live proof, mergeability, and CI at the new revision.
   Matching patch IDs or old green checks never waive this requirement.
4. Prepare only the bottom PR. Reconcile current trunk in its owned checkout
   without destroying work. Respect user and host authorization for publishing
   rewritten branches. Retarget only this PR, then repeat step 3.
5. Land one verified PR at a time through the supported forge. Confirm
   mergeability and required checks on its current head. Arm auto-merge only
   if the user requested it, and only on that bottom PR. Never bypass a forge
   approval or interpret queue enrollment as proof that a PR has merged.
6. Watch the current frontier through forge state or bounded event waits.
   Confirm actual merged state and SHA. Pending checks or a blocked state
   while auto-merge is pending are not proof of failure or success. Diagnose
   a stalled frontier before changing topology.
7. After each merge, fetch trunk, confirm the merged SHA is present, remove
   that PR from the frozen list, and inspect the new bottom's actual base,
   head, checks, and verdict. Retargeting is never assumed. Repeat steps 3-6.
8. Stop at the verified ceiling. Extending the run needs a new independent
   verification pass. Independent branches are outside this stack chain.

**Reply:** each verdict and verifier, exact accepted revisions, the verified
run and ceiling, what was armed, confirmed merges, and the next gap.
