# Original entry points in Codex

All 52 top-level upstream workflows have discoverable Codex entry points.
`$pstack` remains the convenience coordinator; `$poteto-mode` is its original
named mode entry. `$setup-pstack` configures roles and project verification.
There are 53 installable skills in the complete bundle, with one shared runtime
and workflow implementation. Wrappers do not duplicate those implementations.

Upstream disables implicit model selection for every specialist except setup.
That maps to Codex `allow_implicit_invocation: false`, so the specialists remain
available by explicit name without competing to run on every request. Setup
retains implicit selection; the existing pstack coordinator policy is unchanged.

Two names are namespaced consistently: `$pstack-tdd` and `$pstack-teach`. This
avoids replacing common existing `$tdd` and `$teach` skills. All other original
names are preserved. The installer refuses other unrelated conflicts; it never
silently overwrites another skill or renames a workflow unpredictably.

| Upstream workflow | Codex entry point | Implicit selection |
| --- | --- | --- |
| `architect` | `$architect` | Explicit only |
| `arena` | `$arena` | Explicit only |
| `automate-me` | `$automate-me` | Explicit only |
| `benchmark-checklist` | `$benchmark-checklist` | Explicit only |
| `blast-radius` | `$blast-radius` | Explicit only |
| `bro` | `$bro` | Explicit only |
| `correct` | `$correct` | Explicit only |
| `create-verification-skill` | `$create-verification-skill` | Explicit only |
| `figure-it-out` | `$figure-it-out` | Explicit only |
| `how` | `$how` | Explicit only |
| `interrogate` | `$interrogate` | Explicit only |
| `ketchup` | `$ketchup` | Explicit only |
| `maintain-verification-skill` | `$maintain-verification-skill` | Explicit only |
| `make-bot-ui` | `$make-bot-ui` | Explicit only |
| `no-comments` | `$no-comments` | Explicit only |
| `poteto-help` | `$poteto-help` | Explicit only |
| `poteto-mode` | `$poteto-mode` | Explicit only |
| `principle-attack-the-premise` | `$principle-attack-the-premise` | Explicit only |
| `principle-boundary-discipline` | `$principle-boundary-discipline` | Explicit only |
| `principle-build-the-lever` | `$principle-build-the-lever` | Explicit only |
| `principle-encode-lessons-in-structure` | `$principle-encode-lessons-in-structure` | Explicit only |
| `principle-exhaust-the-design-space` | `$principle-exhaust-the-design-space` | Explicit only |
| `principle-experience-first` | `$principle-experience-first` | Explicit only |
| `principle-explain-the-number` | `$principle-explain-the-number` | Explicit only |
| `principle-fix-root-causes` | `$principle-fix-root-causes` | Explicit only |
| `principle-foundational-thinking` | `$principle-foundational-thinking` | Explicit only |
| `principle-guard-the-context-window` | `$principle-guard-the-context-window` | Explicit only |
| `principle-laziness-protocol` | `$principle-laziness-protocol` | Explicit only |
| `principle-make-operations-idempotent` | `$principle-make-operations-idempotent` | Explicit only |
| `principle-migrate-callers-then-delete-legacy-apis` | `$principle-migrate-callers-then-delete-legacy-apis` | Explicit only |
| `principle-minimize-reader-load` | `$principle-minimize-reader-load` | Explicit only |
| `principle-model-the-domain` | `$principle-model-the-domain` | Explicit only |
| `principle-never-block-on-the-human` | `$principle-never-block-on-the-human` | Explicit only |
| `principle-outcome-oriented-execution` | `$principle-outcome-oriented-execution` | Explicit only |
| `principle-prove-it-works` | `$principle-prove-it-works` | Explicit only |
| `principle-redesign-from-first-principles` | `$principle-redesign-from-first-principles` | Explicit only |
| `principle-separate-before-serializing-shared-state` | `$principle-separate-before-serializing-shared-state` | Explicit only |
| `principle-sequence-verifiable-units` | `$principle-sequence-verifiable-units` | Explicit only |
| `principle-subtract-before-you-add` | `$principle-subtract-before-you-add` | Explicit only |
| `principle-test-behavior-not-implementation` | `$principle-test-behavior-not-implementation` | Explicit only |
| `principle-type-system-discipline` | `$principle-type-system-discipline` | Explicit only |
| `recall` | `$recall` | Explicit only |
| `reflect` | `$reflect` | Explicit only |
| `setup-pstack` | `$setup-pstack` | Allowed |
| `show-me-your-work` | `$show-me-your-work` | Explicit only |
| `swarm` | `$swarm` | Explicit only |
| `tdd` | `$pstack-tdd` | Explicit only |
| `teach` | `$pstack-teach` | Explicit only |
| `technical-writing` | `$technical-writing` | Explicit only |
| `typescript-best-practices` | `$typescript-best-practices` | Explicit only |
| `unslop` | `$unslop` | Explicit only |
| `why` | `$why` | Explicit only |

Install the complete bundle with `python3 scripts/install_skills.py` after
cloning this repository. The installer honors CODEX_HOME, validates the shared
core requirement, and preserves already-identical copies. Different existing
skills cause a preflight refusal before any changes. For an existing older
pstack installation, back up and review that owned port before replacing it;
do not remove unrelated skills just to resolve a name conflict.

The built-in skill installer can also install selected paths from this repo.
Always include `skills/pstack` with selected entry points unless the current
compatible core is already installed. Installing only a wrapper does not
install its shared workflow resources automatically. New skills are available
on the next turn. Direct entry points do not imply extra model/provider or
webhook capabilities beyond the shared runtime contract.
