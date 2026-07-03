---
name: build-loop
description: >
  Run an autonomous three-phase build loop — Spec → Planning → Execution — that
  turns a software brief into working, tested, deployable output with minimal
  interruptions. Use when the user types /build-loop or hands over a document,
  brief, or idea describing software to build and wants it driven to completion:
  "work through this", "build this out", "implement this brief", "execute on
  this". Manages shared state via SPEC.md, TASKS.md, and glossary.md so runs are
  resumable across sessions. Not for single-file changes, bug fixes, quick
  throwaway prototypes, or non-software documents (reports, strategies, plans).
---

# /build-loop — Agentic Build Loop

You are running an autonomous build loop. Take a starting document and drive it to
working, deployable output across three phases: **Spec → Planning → Execution**.

Shared-state files are your memory. Read `references/artefact-formats.md` for exact
schemas before writing any of them. Read `references/coding-standards.md` before
writing any code.

---

## Resuming an in-progress run

Check whether `SPEC.md` and `TASKS.md` already exist.

- Both exist → skip to **Phase 3**, first non-done task.
- Only `SPEC.md` → skip to **Phase 2**.
- Neither → start at **Phase 1**.

Tell the user which phase you're resuming from and why.

---

## Phase 1 — Spec

### Step 1 · read_document

Read the starting document in full. Extract and show the user:
- **Core intent** — one sentence
- **Constraints** — language, runtime, deployment target, existing codebase
- **Delivery shape** — service(s), web app, CLI, library, or script. Determines
  which mandatory tasks apply in Step 5.
- **Client-server boundaries** — any API surface between services (flags OpenAPI need)
- **Ambiguities** — things that could go in fundamentally different directions

### Step 2 · bootstrap_glossary

Before writing the spec, create or update `glossary.md`.

- If it does not exist: create it with a header and project name.
- For every domain term in the starting document that has a non-obvious meaning,
  add an entry. See `references/artefact-formats.md §glossary.md` for the schema.
- Load all existing entries into context — every subsequent step must use these terms
  exactly as spelled. This prevents naming drift (DDD ubiquitous language).

### Step 3 · clarify_goal

Make a reasonable assumption before asking. Only ask if an ambiguity would send work
in a fundamentally different direction. Max **3 questions**, all in one message.

Also ask: is this a monolith or are there separate services? (Determines fan-out and
OpenAPI requirements.) If the answer is obvious from the document, assume and log it.

### Step 4 · write_spec

Write `SPEC.md`. Required sections: Goal, Non-goals, Acceptance criteria, Tech
constraints, Assumptions.

**Acceptance criteria rules:**
- Every criterion must be binary (pass/fail).
- For any user-facing or API-level behaviour, name the E2E test that will
  verify it: `AC-04: User can log in → test: auth.spec.ts > "AC-04: logs in with valid credentials"`
  (test names embed the AC ID as the stable join key — see
  `references/coding-standards.md §6`)
- At least one acceptance criterion must cover the deployment check:
  `docker compose up` succeeds and `start-all.sh` is healthy.

**Spec constraints rules:**
- If there are client-server boundaries, record each one in §Tech constraints with a
  note: "OpenAPI spec required before implementation of either side."
- Record the architecture decision (monolith vs services) in §Tech constraints with
  rationale. Prefer monolith unless the document gives a concrete reason for services.

After writing, show the summary and acceptance criteria.
Say: "Proceeding — interrupt me now if you want to revise." Then continue
immediately. Never wait for a reply — the user can interrupt at any point.

---

## Phase 2 — Planning

### Step 5 · decompose_tasks

Break the spec into atomic tasks. Each must be independently testable and
context-window sized.

**Mandatory tasks** — include each row whose Trigger matches the delivery shape
from Step 1. If a row is skipped, record a one-line waiver with the reason in
`SPEC.md §Tech constraints`:

| ID suffix | Task | Trigger |
|-----------|------|---------|
| …-SCHEMA  | Write OpenAPI / JSON Schema for each client-server boundary | Any API boundary |
| …-WIREFRAME | HTML wireframes under `plan/wireframes/` (static HTML, minimal JS only where interaction needs demonstrating) | Any web UI |
| …-REGEN   | Create `regenerate-all.sh` (stub; each codegen task populates it) | Any code generation |
| …-DOCKER  | Write `Dockerfile` and `docker-compose.yml` | Any service |
| …-RUNNER  | Write `start-all.sh` with CTRL+C cleanup | Multiple processes |
| …-E2E     | Write E2E test suite (Playwright for web; stack equivalent otherwise) | Any user-facing behaviour |
| …-OTEL    | Wire OTEL tracing and structured logging | Any long-running service |

Schema tasks (`…-SCHEMA`) must be assigned IDs that precede all implementation tasks
on either side of that boundary. Likewise, wireframe tasks (`…-WIREFRAME`) must
precede all UI implementation tasks — each UI task names the wireframe file it
realises (see `references/artefact-formats.md §plan/`).

The `…-REGEN` task creates an empty `regenerate-all.sh` stub with the shebang and
header. Every subsequent task that generates files must: (a) add a section to
`regenerate-all.sh`, and (b) add a regeneration header to each generated file.
See `references/coding-standards.md §13` for the header format and script template.

**Fan-out detection** — after listing all tasks, group them into parallel batches:
- A batch is a set of tasks with no overlapping output files and no
  shared-schema dependencies.
- Schema tasks, `glossary.md` updates, and `SPEC.md` changes always run solo (not in
  any parallel batch) — they are shared state.
- Label each batch in `TASKS.md` with `## Batch N` headings.

### Step 6 · prioritise_tasks

Order within and across batches:
1. Schema tasks (OpenAPI, JSON Schema) always come first in their dependency chain.
2. Wireframe tasks before any UI implementation task.
3. Leaf tasks (no dependencies) before dependents.
4. High-uncertainty tasks before low-uncertainty — discover problems early.
5. Mark any task blocking ≥3 others as `critical-path` in `TASKS.md`.

Write `TASKS.md`. Show the task table (ID, title, batch, depends-on).
Say: "Starting execution — interrupt me now to reorder." Then continue.

### Step 7 · select_next_task

Read `TASKS.md`. Find the next batch where all preceding batches are done.

- **In Cowork / subagent-capable environments**: spawn one subagent per task in the
  current batch. Each subagent runs steps 8–11 independently and returns its verdict
  and output paths. Subagents never write `TASKS.md`, `glossary.md`, or `SPEC.md` —
  the parent runs Step 12 serially for each result. Reconvene at entropy_checkpoint
  when the batch completes. Be cost-aware: fan out only when the batch has multiple
  substantial tasks (small tweaks run faster inline), cap concurrency at ~4, and
  give each subagent only its task's slice of context — never the whole
  conversation.
- **In single-agent environments**: announce: "These tasks can run in parallel
  sessions: [list]". Then execute them one by one.

Within a batch, pick the highest-uncertainty task first.

Announce: `▶ Batch 2 · T007 — Implement user CRUD endpoints`

---

## Phase 3 — Execution Loop

### Step 8 · implement_task

Load context before coding:
1. Spec section reference from `TASKS.md`
2. Relevant `SPEC.md` sections
3. `glossary.md` — use every domain term exactly as defined
4. `references/coding-standards.md` — apply every preference
5. Output paths of all dependency tasks

Implement. Write to the task's specified output path.
Do not over-engineer. The acceptance criterion is the definition of done.

**If this task produces any generated files** (from openapi-generator, prisma,
protoc, graphql-codegen, or any other generator):
- Add the regeneration header to the top of every generated file before committing.
  Use the language-appropriate comment style. See `references/coding-standards.md §13`.
- Add the exact CLI command used to `regenerate-all.sh` under a clearly labelled
  section. See `references/coding-standards.md §13` for the script structure.

### Step 9 · run_tests

| Task type | Run |
|-----------|-----|
| Application code | Lint, type check, unit tests for this module |
| OpenAPI / JSON Schema | Schema validation (`ajv`, `openapi-validator`, or equivalent) |
| E2E task | `npx playwright test [spec-file]` |
| Docker / compose | `docker compose config --quiet` + `docker build .` |
| `start-all.sh` | `bash -n start-all.sh` (syntax check) + dry-run in subshell |
| OTEL wiring | Start service, emit a test span, verify it reaches the collector |

If tests fail, pass the failure output directly to review_output. Do not attempt a
fix before review — review diagnoses, implement fixes in the next loop iteration.

### Step 10 · review_output

Diff actual output against the task's acceptance criterion. Produce a structured
verdict:

```
PASS   T007 — user CRUD endpoints
       ✓ POST /users → 201, returns {id, email, createdAt: "yyyy-mm-dd"}
       ✓ DTO comments present on all fields
       ✓ per-aggregate repository, glossary-named methods (no generic CRUD wrapper)
       ✓ OTEL span emitted per request

FAIL   T007 — missing field-level DTO examples
       ✗ acceptance: "all DTO fields have @example annotations"
       ✗ found: createdAt has no example value
       → retry: add @example "2024-01-15" to all date fields in UserResponseDto
```

**On PASS** → go to Step 11.  
**On FAIL** → classify the failure before spending budget:

1. **Environment failure** (port in use, container not up, missing dependency) —
   does not consume budget. Fix the environment and re-run. Two consecutive
   environment failures on the same task → stop retrying this task; fix or reopen
   the environment task (`…-DOCKER` / `…-RUNNER`) instead, and log a `redirect`
   trace event. When unsure whether a failure is environmental, it isn't — count it.
2. **Stall check** — compare against the previous attempt's failure signature
   (failing test + error class). Same signature twice in a row → escalate
   immediately, even with budget remaining. More attempts won't help; a human might.
3. **Implementation failure** — increment `Retries`, then back to Step 8 with the
   verdict as context. The retry must state in one line what it will do differently
   (recorded as the trace `cause`); if there is nothing to do differently, escalate
   now. `Retries` ≥ 3 → escalate — unless every attempt so far strictly reduced the
   failing-check count, in which case exactly one grace attempt is allowed
   (hard ceiling: 4).

### Step 11 · code_review

On PASS from review_output, run a code review pass before marking done.

Check specifically (in addition to any project code review skill):
- **Repetition ripe for abstraction** — a pattern at 3+ occurrences that a config
  table, type parameter, or template would eliminate. Flag it in the task's Notes
  for the entropy checkpoint; do not build the abstraction mid-task.
- **Wrong-abstraction tripwires** — a generic that type-switches on its parameter,
  boolean config params steering behaviour, call sites bypassing the abstraction,
  or per-entity copies of shared utilities (e.g. CSV export)
- **Glossary compliance** — every domain term matches `glossary.md` exactly
- **DTO quality** — every public DTO field has a JSDoc/docstring comment, a type
  annotation, and an `@example` value in the correct format (e.g. `"yyyy-mm-dd"`)
- **OTEL coverage** — every service entry point has a span; errors are recorded
- **No dangling processes** — `start-all.sh` uses the trap pattern from
  `references/coding-standards.md §Service Runner`

If code review raises issues, go back to Step 8 with the review notes. Review
findings consume `Review cycles` (cap 2), not `Retries` — they are cheap to fix
but prone to oscillation. If a second review cycle raises new or contradictory
findings, escalate: the review bar, not the implementation, is probably the
problem.

### Step 12 · update_task_status

Update `TASKS.md`:
- Status → `done`
- Record output paths
- One-liner note for dependent tasks (e.g. "JWT secret in `config.JWT_SECRET`")
- Update progress summary line at the top
- Append a trace event to `_traces/run-NN.jsonl` — task ID, verdict, retry
  count, one-line cause per retry (see `references/artefact-formats.md §_traces/`).
  Traces are collected so the loop itself can be evaluated and improved later.

If the entropy trigger is met (Step 13), run the checkpoint next. Otherwise go to
**Step 14**.

### Step 13 · entropy_checkpoint

**Trigger**: after every 5 tasks complete, or when a parallel batch finishes.

Run a single-agent refactoring pass (do NOT fan out — this is the entropy reduction
step):

1. **Glossary drift scan** — grep codebase for synonyms of glossary terms. Rename any
   divergent identifiers. Commit with message `refactor: align to glossary`.
2. **Duplication scan** — look for repeated logic blocks (>10 lines, ≥3 occurrences)
   and the candidates flagged in task Notes. Extract using the abstraction ladder
   (config → generic → template — `references/coding-standards.md §1`); log an
   `abstraction_introduced` trace event for each extraction. Also check existing
   abstractions for accreted flags, type-switches, or bypasses — dismantling a
   wrong abstraction counts as entropy reduction too.
3. **Monolith check** — if services that share >50% of their data models could be
   merged without complicating deployment, flag to user as a simplification option.
4. **DRY-DTO check** — look for DTOs that duplicate domain model fields. If a generic
   mapper would eliminate the duplication, introduce it.

Constraints: do NOT change public API contracts, acceptance criteria, or OpenAPI
schemas. Refactors are internal only. Document every change in `CHANGELOG.md`.
Then go to **Step 14**.

### Step 14 · check_done_condition

- All tasks `done` → proceed to **Exit**.
- Some `blocked`, none `todo` or `in-progress` → escalate.
- Otherwise → back to Step 7.

---

## Escalation

Escalate (pause and ask) only when:

1. **Hard blocker** — retry budget exhausted (3 implementation retries, 4 with a
   grace attempt, or 2 review cycles) or a stall detected. Show the retry history
   from the trace — signatures and per-attempt causes. Ask: "(a) try a different
   approach, (b) skip, or (c) lower bar to [X]?"
2. **Dependency deadlock** — no todo tasks have all dependencies done.
3. **Spec conflict** — implementation contradicts `SPEC.md`. Suggest resolution.
4. **Scope creep** — acceptance criterion requires 3× estimated work. Surface before
   starting.
5. **Schema change required** — implementing a task reveals the OpenAPI spec needs
   changing. Stop. Update spec. Re-validate all tasks that depend on it before
   continuing.

Never silently skip or lower acceptance criteria. Log every escalation as a trace
event before pausing.

---

## Exit — summarise_outcome

1. **Deployment check**: run `docker compose up --wait`, verify the stack reports
   healthy, then `docker compose down`. Verify
   `start-all.sh` starts all processes and CTRL+C stops them cleanly (no `ps aux`
   orphans). Record result in `CHANGELOG.md`.

2. **OTEL check**: verify at least one end-to-end trace exists in the collector
   output covering the primary happy path.

3. Write `CHANGELOG.md` entry: what was built, key decisions, deferred tasks, stats
   (tasks done, retries, escalations, entropy checkpoints run — computed from
   `_traces/run-NN.jsonl`, and close the trace with an `exit` event).

4. Print completion summary:
   ```
   ✅ /build-loop complete — 11/12 tasks done

   Built: [list]
   Deferred: [list with reasons]
   Artefacts: SPEC.md · TASKS.md · glossary.md · CHANGELOG.md
              openapi.yaml · docker-compose.yml · start-all.sh
              plan/wireframes/ · _traces/ (local, gitignored)
   ```

---

## Principles

**Generated files are never edited by hand.** Every generated file carries a header
naming the CLI command and pointing to `regenerate-all.sh`. Running
`./regenerate-all.sh` must reproduce every generated file from scratch. If a generated
file needs to change, change the schema or generator config, then regenerate.

**Glossary is law.** Every domain term in code must match `glossary.md` exactly. When
in doubt, look it up. When it's missing, add it before using it.

**Schema before code.** No implementation on either side of a client-server boundary
until the OpenAPI / JSON Schema task is done and reviewed.

**Wireframes before UI.** No UI implementation until the HTML wireframes in
`plan/wireframes/` exist and have been shown to the user. Cheap pixels first.

**Traces feed improvement.** Every run appends events to `_traces/` (gitignored) —
that log is how the loop's own weaknesses get found and fixed. Don't skip trace
writes.

**Abstractions are earned.** Configuration over generics over templates over
duplication, and only at the third occurrence — the Rule of Three. Domain code
stays intention-revealing (no generic CRUD repositories); plumbing gets the
generics. New abstractions are born at entropy checkpoints, not mid-task.

**Monolith by default.** Services add deployment surface. Only split when the document
gives a concrete, non-speculative reason.

**Fan out on independence; contract on convergence.** Parallel agents when tasks don't
share state. Single agent when touching shared state (schemas, glossary, SPEC.md).

**Entropy checkpoints are non-negotiable.** Every 5 tasks, stop and clean. This is not
optional even under time pressure. Technical debt compounds faster in agentic loops.

**Shared state is the memory.** If context is lost: read SPEC.md, TASKS.md, and
glossary.md. Do not ask the user to re-explain.

**Retry budgets are hard.** Three implementation retries (a fourth only when every
attempt strictly shrank the failing set), two review cycles, zero tolerance for
stalls — the same failure twice means escalate now. Environment failures don't
consume budget; they redirect. The caps and classification rules are initial
guesses — revise them from `_traces/` evidence, not intuition.

---

## Gotchas

**Only the parent writes shared state.** Parallel subagents that each update
`TASKS.md` or `glossary.md` clobber each other's writes. Subagents return verdicts
and output paths; the parent applies them (Step 12).

**`docker compose`, not `docker-compose`.** The v1 hyphenated CLI is end-of-life,
and the `version:` key in compose files is obsolete — both produce warnings or
missing features (e.g. `--wait`).

**devDependencies vanish before the build.** Installing with `--omit=dev` in the
build stage breaks the build step because compilers and bundlers are
devDependencies. Install everything, build, then prune — see
`references/coding-standards.md §12`.

**Register the cleanup trap before starting services.** A CTRL+C during a slow
startup otherwise orphans the processes already launched — see
`references/coding-standards.md §11`.

**E2E needs a running stack.** Start `start-all.sh` (or the compose stack) and wait
on health endpoints before running E2E tests, or every test fails with connection
refused.

**"Interrupt to revise" is not a pause.** After announcing a phase transition,
continue immediately in the same turn. The user interrupts if they disagree; waiting
for a reply defeats the point of the loop.

**Classify before you burn budget.** Environment failures don't consume `Retries`
and review findings consume `Review cycles` instead — but misclassifying an
implementation failure as environmental is a budget leak that hides a stuck task.
When unsure, count it. Record each retry's failure signature and one-line cause in
the trace so stall detection stays mechanical.

**Comment headers don't work in JSON.** Generated JSON files can't carry the
regeneration header — put it in a sibling `README.md` instead
(`references/coding-standards.md §13`).
