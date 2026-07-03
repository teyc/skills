# Artefact Formats

Reference schemas for the shared-state files that the /build-loop pipeline maintains.

---

## SPEC.md

```markdown
# Spec: [Project name]
> Started: [date] · Status: active | complete

## Goal
[One paragraph. What are we building and why? Who uses it?]

## Non-goals
- [Explicit exclusion 1]
- [Explicit exclusion 2]

## Acceptance criteria
- [ ] [Testable, binary criterion — either passes or fails]
- [ ] [Criterion 2]
- [ ] [Criterion N]

## Tech constraints
- **Language / runtime**: [e.g. Python 3.11, Node 20]
- **Key dependencies**: [e.g. FastAPI, Prisma, React 18]
- **Output format**: [e.g. REST API, CLI tool, markdown files]
- **Deploy target**: [e.g. Docker, Vercel, local script]
- **Existing codebase**: [path or "greenfield"]

## Assumptions
- [Assumption 1 — what was assumed and why]
- [Assumption 2]

## Open questions
- [Q]: [Question text] → **[A]**: [Resolution] *(resolved)*
- [Q]: [Unresolved question] → **pending**
```

**Rules:**
- Acceptance criteria must be binary (testable true/false). "Good UX" is not a
  criterion. "All pages load in < 2s on a 4G connection" is.
- Non-goals are as important as goals. They prevent scope creep.
- Never delete a resolved assumption — mark it resolved, keep the rationale.

---

## TASKS.md

```markdown
# Tasks
> Spec: SPEC.md · Loop started: [date]
> Progress: 3/9 done · 1 in-progress · 0 blocked · 5 todo

---

## T001 — [Task title]
- **Status**: done | in-progress | todo | blocked | skipped
- **Spec ref**: §[section heading or acceptance criterion number]
- **Acceptance**: [Single testable criterion for this task specifically]
- **Depends on**: — | T002, T003
- **Priority**: critical-path | normal
- **Output**: [file path(s) or "n/a"]
- **Notes**: [One line for the next task's implementer — omit if nothing to say]
- **Retries**: 0–4 (implementation failures only; 4 only via a grace attempt)
- **Review cycles**: 0–2 (code-review findings)

---

## T002 — [Task title]
...
```

**Status values:**
| Status | Meaning |
|--------|---------|
| `todo` | Not started, all dependencies met or no dependencies |
| `in-progress` | Currently being implemented (one per active agent; only the parent agent writes this file) |
| `done` | Passed review, output recorded |
| `blocked` | Dependencies not done, retry/review budget exhausted, or stall detected — needs human input |
| `skipped` | Explicitly deferred by user decision |

**Rules:**
- IDs are permanent. Never renumber tasks — add new ones at the end.
- The progress summary line at the top updates after every `update_task_status` step.
- `Retries` increments only on implementation failures (cap 3; one grace attempt to
  4 when every attempt strictly reduced the failing-check count). Environment
  failures never increment it; two in a row redirect to the environment task.
- `Review cycles` increments each time `code_review` sends the task back (cap 2).
- A stall (same failure signature twice in a row) sets the task `blocked`
  regardless of remaining budget.
- `Notes` is read by the implementer of dependent tasks. Keep it ≤ one line.
  Example: "JWT secret stored in `config.JWT_SECRET`, not env var."

---

## glossary.md

```markdown
# Glossary
> Project: [name]
> Last updated: [date]
> Rule: all domain terms in code must match entries here exactly.

---

## [Term]
**Definition**: [One sentence in plain domain language — no jargon]
**Code identifier**: `ExactCasing` (the identifier used in classes, tables, API paths)
**Layer**: Domain | Application | Infrastructure | UI
**Aliases to avoid**: [synonym1, synonym2] — terms that accidentally appear in code
**Notes**: [Disambiguation, related terms, or historical context]
```

**Rules:**
- Terms are added during `bootstrap_glossary` (Step 2) and updated any time a new
  domain concept appears.
- `glossary.md` is a solo-agent file — never updated inside a parallel batch.
- The `entropy_checkpoint` scans for `Aliases to avoid` in the codebase and renames
  any occurrences it finds.
- Commit new terms in one batch per step, not one commit per term:
  `docs: add glossary terms [Term1, Term2]`

---

## CHANGELOG.md

Append one entry per completed `/build-loop` run. Do not overwrite previous entries.

```markdown
## [date] — [Project name / brief description]

### Built
- [Concrete deliverable 1]
- [Concrete deliverable 2]

### Key decisions
- [Decision]: [Rationale] — e.g. "Used SQLite not Postgres: deploy target is a
  single-server script with no connection pooling requirement (§Tech constraints)"

### Deferred
- T007 — [title]: [reason] — e.g. "Redis not in scope per §Non-goals"

### Stats
- Tasks completed: 8/9
- Retries triggered: 2 (T003 ×1, T006 ×1)
- Escalations: 0
```

---

## plan/

Planning artefacts — inputs to execution, not shipped code.

### plan/wireframes/

Static HTML wireframes, one file per screen or flow (`login.html`,
`dashboard.html`). Plain HTML/CSS; vanilla JS only where an interaction genuinely
needs demonstrating (a tab switch, a modal). No frameworks, no build step — each
file must open directly in a browser.

**Rules:**
- Created by the `…-WIREFRAME` task before any UI implementation task starts.
- For form-over-data apps, wireframe the templates, not every screen: one datagrid
  template, one form template, plus only the screens that deviate. A screen list
  with "uses grid template" annotations beats twelve near-identical wireframes.
- Each UI task in `TASKS.md` names the wireframe file it realises in its **Spec
  ref** or **Notes** field.
- Wireframes are throwaway fidelity: layout, hierarchy, and flow — not styling.
  Divergence during implementation is fine if the acceptance criterion still
  passes; update the wireframe only when the flow itself changes.

---

## _traces/run-NN.jsonl

Append-only event log, one JSON object per line, one file per run (`run-01.jsonl`,
`run-02.jsonl`). Local-only telemetry: the first trace write adds `_traces/` to
`.gitignore`. Collected so the loop's own behaviour can be evaluated and improved
later — keep events small and machine-readable.

```jsonl
{"t":"2026-07-02T10:14:02Z","event":"phase_start","phase":3}
{"t":"2026-07-02T10:15:31Z","event":"task_start","task":"T007","batch":2,"agent":"subagent"}
{"t":"2026-07-02T10:22:07Z","event":"retry","task":"T007","retries":1,"signature":"users.spec.ts::AC-02 / assertion","cause":"switch DTO mapper to generic — missing @example on createdAt"}
{"t":"2026-07-02T10:24:00Z","event":"review_cycle","task":"T007","cycles":1,"cause":"glossary drift: JobOrder → WorkOrder"}
{"t":"2026-07-02T10:25:10Z","event":"redirect","task":"T008","to":"T002-DOCKER","cause":"2× env failure: postgres container not up"}
{"t":"2026-07-02T10:26:44Z","event":"pass","task":"T007","retries":1}
{"t":"2026-07-02T11:02:10Z","event":"entropy_checkpoint","n":1,"changes":3}
{"t":"2026-07-02T11:40:00Z","event":"escalate","task":"T009","reason":"stall: same signature on attempts 1-2"}
{"t":"2026-07-02T12:05:00Z","event":"exit","done":11,"total":12}
```

**Rules:**
- Event vocabulary: `phase_start`, `task_start`, `pass`, `fail`, `retry`,
  `review_cycle`, `redirect`, `escalate`, `entropy_checkpoint`,
  `abstraction_introduced`, `exit`. Unknown fields are allowed; unknown events
  are not.
- `abstraction_introduced` events name the extraction and its rung on the ladder
  (`config` / `generic` / `template`) — later checkpoints check whether it held up,
  which is how the generics-vs-duplication defaults get tuned from evidence.
- Every `retry` event carries a `signature` (failing test + error class) — stall
  detection compares consecutive signatures, so keep the format stable — and a
  `cause` stating what the next attempt will do differently.
- `_traces/` is gitignored — traces never ship with the project. Copy them out
  before deleting a checkout if you want to keep them for analysis.
- The parent agent is the only writer (same rule as `TASKS.md`).
- Every retry and escalation must carry a one-line `cause`/`reason` — these are
  the highest-value signals when mining traces for loop improvements.
- Exit stats in `CHANGELOG.md` are computed from this file, not from memory.
