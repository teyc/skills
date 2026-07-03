# Coding Standards

Preferences applied on every `implement_task` step. Read this file before writing
any code. These are non-negotiable defaults — override only when a task's acceptance
criterion explicitly requires something different, and document the override.

Examples below are shown in TypeScript or C#. The rules are language-neutral —
apply them idiomatically in the project's language.

---

## 1 · Abstractions are earned — the ladder

When a pattern repeats, climb this ladder and stop at the first rung that fits:

1. **Configuration** — a framework or library's existing generic, driven by data
   (EF Core `DbSet<T>`, the Prisma client, TanStack Table, MudDataGrid plus a
   column-definition table). The best abstraction is one you didn't write.
2. **Your own generic** — Infrastructure and Application plumbing only (mappers,
   caching, pagination). Never the Domain layer.
3. **Template code generation** — handlebars/jinja/scaffolding when the pattern is
   real but not type-shaped (e.g. per-entity controllers whose routes, attributes,
   and validation differ semi-regularly — a type parameter can't express that; a
   template can).
4. **Duplication** — acceptable until the **Rule of Three**: abstract on the third
   occurrence, or the second plus a named, expected third. Two instances rarely
   reveal the axis of variation, and a wrong abstraction costs more than the
   duplication it replaced.

**Domain code stays intention-revealing.** Repositories are per-aggregate with
glossary-named methods, not generic CRUD — the ORM underneath is already the
generic layer.

```typescript
// ✗ — generic CRUD repo: hides the domain, invites bypass, re-wraps the ORM
class Repository<T extends Entity> {
  findById(id: string): Promise<T> { ... }
  save(entity: T): Promise<T> { ... }
}

// ✓ — per-aggregate repository; methods answer domain questions in glossary terms
class WorkOrderRepository {
  findById(id: WorkOrderId): Promise<WorkOrder> { ... }
  findOverdue(asOf: Date): Promise<WorkOrder[]> { ... }
  save(order: WorkOrder): Promise<void> { ... }
}
```

**Timing**: `implement_task` reuses existing abstractions but never introduces new
ones mid-task — flag the candidate in the task's Notes and let the entropy
checkpoint extract it with cross-batch sight (SKILL.md Step 13).

**Code generation** (rung 3): also the right tool when in-language abstraction is
impossible (database migrations, API client SDKs, protobuf bindings, project
scaffolding) — generate from a schema or template rather than hand-coding. Any
generator is acceptable — `openapi-generator`,
`prisma generate`, `protoc`, `graphql-codegen`, NSwag, `dotnet new`, or a
handlebars/jinja template — as long as `regenerate-all.sh` reproduces the output.

**Naming**: single-file outputs carry a `.generated.` suffix next to their consumers
(`user-api.generated.ts`, `UserApi.generated.cs`). Generators that emit a whole
directory of files you don't name write to a dedicated `generated/` directory
instead. Generated files are never edited by hand.

---

## 2 · OpenAPI / JSON Schema for every client-server boundary

Every boundary between a client and a server (HTTP, WebSocket, message queue) must
have a schema file before either side is implemented.

**For HTTP APIs**: write `openapi.yaml` at the project root.

```yaml
# openapi.yaml
openapi: "3.1.0"
info:
  title: "Service Name"
  version: "0.1.0"
paths:
  /users/{id}:
    get:
      summary: "Get user by ID"
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string, format: uuid, example: "3fa85f64-5717-4562-b3fc-2c963f66afa6" }
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/UserResponse" }
```

**For async / queue boundaries**: write a JSON Schema file per message type in
`schemas/messages/`.

**Rule**: the schema task in `TASKS.md` must be `done` before any implementation task
on either side of the boundary is started. This is enforced in `prioritise_tasks`.

---

## 3 · DTO comments and example values

Every public DTO or schema object must have:
- A class/interface-level docstring explaining its purpose
- A comment on every field explaining what it represents
- An `@example` annotation (or equivalent) in the correct format

```typescript
/**
 * Response payload for a single user record.
 * Returned by GET /users/:id and POST /users.
 */
export class UserResponseDto {
  /** Unique identifier — UUID v4 */
  // @example "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  id: string

  /** User's primary email address */
  // @example "alice@example.com"
  email: string

  /** ISO 8601 date the account was created */
  // @example "2024-01-15"
  createdAt: string   // format: yyyy-mm-dd

  /** Account status — one of: active | suspended | deleted */
  // @example "active"
  status: 'active' | 'suspended' | 'deleted'
}
```

Same rules in C# — XML doc comments with `<example>` tags:

```csharp
/// <summary>
/// Response payload for a single user record.
/// Returned by GET /users/{id} and POST /users.
/// </summary>
public sealed record UserResponseDto
{
    /// <summary>Unique identifier — UUID v4.</summary>
    /// <example>3fa85f64-5717-4562-b3fc-2c963f66afa6</example>
    public required string Id { get; init; }

    /// <summary>User's primary email address.</summary>
    /// <example>alice@example.com</example>
    public required string Email { get; init; }

    /// <summary>ISO 8601 date the account was created (yyyy-MM-dd).</summary>
    /// <example>2024-01-15</example>
    public required string CreatedAt { get; init; }
}
```

Date formats must always be annotated: `yyyy-mm-dd`, `yyyy-mm-ddTHH:MM:SSZ`, etc.
Currency must be annotated with unit: `// @example 4999  (cents, AUD)`.

---

## 4 · Glossary — ubiquitous language (DDD)

`glossary.md` at the project root is the single source of truth for domain terms.

**Schema for each entry:**
```markdown
## [Term] (e.g. WorkOrder)
**Definition**: [One sentence in plain domain language]
**Code identifier**: `WorkOrder` (the exact casing used in code)
**Layer**: Domain | Application | Infrastructure | UI
**Aliases to avoid**: job, task, ticket  ← terms that mean something else here
**Notes**: [Any disambiguation]
```

**Rules:**
- Before naming any class, interface, database table, or API path, look it up here.
- If it's missing, add it before writing the code. Never invent a synonym.
- The `entropy_checkpoint` step scans for aliases in code and renames them.
- `glossary.md` is a solo-agent file — never update it inside a parallel batch.

---

## 5 · Agent fan-out

Fan out to parallel agents when tasks have no overlapping output files and no
dependency on shared-state files (`SPEC.md`, `TASKS.md`, `glossary.md`, `openapi.yaml`).

**What can be parallelised**: feature modules, test files, independent services,
independent UI components, infrastructure-as-code for separate resources.

**What must stay serial**: schema writes, glossary updates, SPEC.md changes, any
task whose output is in another task's input set, the entropy_checkpoint.
Task-status writes to `TASKS.md` are performed by the parent agent only — parallel
subagents report results back instead of writing shared-state files.

In `TASKS.md`, use `## Batch N` headings so agents know which tasks are concurrent.
When a batch finishes, run `entropy_checkpoint` before starting the next batch.

**Cost-awareness**: subagents cost tokens. Fan out only when a batch has multiple
substantial tasks — a batch of small tweaks runs faster inline. Cap concurrency at
~4, and give each subagent only its task's slice of context (task entry, relevant
SPEC.md sections, glossary, these standards), never the whole conversation.

---

## 6 · Acceptance criteria → Playwright E2E tests

Every acceptance criterion that covers user-visible or API-level behaviour must map
1:1 to a Playwright test.

**Naming convention:**
- Test file: `tests/e2e/[feature].spec.ts`
- Test name: starts with the AC ID, followed by a short paraphrase. The ID is the
  stable join key — criteria can be reworded in `SPEC.md` without breaking the
  mapping.

```typescript
// tests/e2e/auth.spec.ts
test('AC-04: logs in with valid credentials', async ({ page }) => {
  await page.goto('/login')
  await page.fill('[data-testid="email"]', 'alice@example.com')
  await page.fill('[data-testid="password"]', 'correct-password')
  await page.click('[data-testid="submit"]')
  await expect(page).toHaveURL('/dashboard')
})
```

**The E2E task** (`…-E2E`) in `TASKS.md` maps to the full Playwright suite. Its
acceptance criterion is: all named tests pass against a locally running `start-all.sh`
stack. Run with: `npx playwright test --reporter=list`.

For non-web deliverables (CLI, library, worker), the E2E equivalent is an
integration test suite that exercises the built artifact end-to-end. The 1:1
criterion-to-test mapping and AC-ID naming rule still apply.

---

## 7 · Code review before merge

Before any task is marked `done`, run a code review pass (Step 11 in the loop).

**Checklist** (automated where possible):

| Check | Tool |
|-------|------|
| Linting | ESLint / Ruff / golangci-lint |
| Type safety | tsc --noEmit / mypy / go vet |
| Unused exports | ts-prune / vulture |
| DTO @example completeness | custom grep: fields without @example |
| Glossary drift | grep -rn for known aliases from glossary.md |
| Dangling OTEL spans | grep for `startSpan` without matching `span.end()` |

Any FAIL in this checklist sends the task back to implementation and counts toward
its `Review cycles` budget (cap 2) — not `Retries`. See SKILL.md Step 11.

---

## 8 · Entropy checkpoints — refactoring cadence

Every 5 tasks complete, or when a parallel batch finishes, a single refactoring agent
runs. This agent:

1. Runs `entropy_checkpoint` (Step 13 in the loop)
2. Checks for: naming drift, duplicated logic, unnecessary service splits, oversized
   modules that should be broken up, undersized modules that should be merged
3. Makes internal refactors only — no public API surface changes
4. Commits: `refactor: entropy checkpoint #N — [summary of changes]`

This keeps the codebase coherent across agents that don't share context.

---

## 9 · Monolith preference

Default to a monolith. Only introduce separate services when:
- The deployment requirement is explicit (e.g. "the worker must scale independently")
- The tech stack mismatch is real (e.g. ML inference in Python, API in Node)
- Team ownership boundaries make shared-process deployment genuinely untenable

If uncertain, build the monolith first with internal module boundaries. The
`entropy_checkpoint` can flag candidate extraction points if they become obvious.

Monolith benefits in this context: one `start-all.sh`, one `Dockerfile`, one set of
OTEL traces, one `openapi.yaml`, lower agent context overhead.

---

## 10 · OTEL — tracing and structured logging

Every service must emit OpenTelemetry traces and structured logs.

Use the platform SDK, nothing exotic: the `@opentelemetry/*` packages for Node, the
`OpenTelemetry.*` NuGet packages for .NET (`ActivitySource` + `AddOpenTelemetry()`).
Prefer auto-instrumentation for HTTP/DB entry points; hand-wrap spans only for
domain steps worth naming.

**.NET setup (auto-instrumentation does most of the work):**
```csharp
builder.Services.AddOpenTelemetry()
    .ConfigureResource(r => r.AddService("service-name"))
    .WithTracing(t => t.AddAspNetCoreInstrumentation().AddOtlpExporter())
    .WithLogging(l => l.AddOtlpExporter());
```

**Node — hand-wrapped domain span:**
```typescript
import { trace, metrics } from '@opentelemetry/api'

const tracer = trace.getTracer('service-name', '1.0.0')

// Wrap every service entry point (HTTP handler, queue consumer, cron job)
async function handleRequest(req: Request): Promise<Response> {
  return tracer.startActiveSpan('handleRequest', async (span) => {
    try {
      span.setAttributes({
        'http.method': req.method,
        'http.route': '/users/:id',
        'user.id': req.params.id,
      })
      const result = await processRequest(req)
      span.setStatus({ code: SpanStatusCode.OK })
      return result
    } catch (err) {
      span.recordException(err)
      span.setStatus({ code: SpanStatusCode.ERROR, message: err.message })
      throw err
    } finally {
      span.end()
    }
  })
}
```

**Structured logging**: log at span boundaries. Every log line must be JSON with at
minimum: `{ "timestamp": "...", "level": "...", "traceId": "...", "spanId": "...",
"message": "...", "service": "..." }`.

No standalone OTEL Collector is needed — export OTLP straight to a local backend.
**docker-compose.yml** must include one telemetry backend container: Jaeger
all-in-one (trace-first) or Seq (`datalust/seq`, structured-log-first with OTLP
ingest). Traces and logs must be visible locally without external setup.

---

## 11 · Service runner — start-all.sh

`start-all.sh` in the project root starts all services and stops them cleanly on
CTRL+C. No dangling processes after exit.

```bash
#!/usr/bin/env bash
set -euo pipefail

# ── cleanup — registered BEFORE anything starts ───────────────────
cleanup() {
  echo ""
  echo "Stopping services..."
  # jobs -p lists every background process this script started
  kill $(jobs -p) 2>/dev/null || true
  wait 2>/dev/null || true
  echo "All services stopped."
}
trap cleanup INT TERM

# ── start services ────────────────────────────────────────────────
echo "Starting services..."

node dist/api/index.js &
echo "API     PID=$!"

node dist/worker/index.js &
echo "Worker  PID=$!"

# Add more services here following the same pattern

echo ""
echo "Press Ctrl+C to stop all services."

# ── wait ─────────────────────────────────────────────────────────
wait
```

**Rules:**
- The trap is registered before any service starts — a CTRL+C during a slow startup
  must not orphan already-launched processes.
- `cleanup` kills `$(jobs -p)`, so every service must be started as a direct
  background job of this script — no `setsid`, `nohup`, or self-daemonizing
  processes.
- `cleanup` must `wait` after killing — otherwise child processes can outlive the
  script.
- The script must be executable: `chmod +x start-all.sh`.
- Add a health-check echo after each service starts if startup is slow:
  `echo "Waiting for API..." && npx wait-on http://localhost:3000/health`

---

## 12 · Docker deployment

Every project with runnable services must have a `Dockerfile` and
`docker-compose.yml` at the project root.

**Dockerfile** (multi-stage, Node example):
```dockerfile
# ── build ─────────────────────────────────────────────────────────
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
# devDependencies were needed for the build; strip them before the runtime copy
RUN npm prune --omit=dev

# ── runtime ───────────────────────────────────────────────────────
FROM node:20-alpine AS runtime
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./
EXPOSE 3000
USER node
CMD ["node", "dist/index.js"]
```

**docker-compose.yml** (must include OTEL collector):
```yaml
services:

  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:3000/health"]
      interval: 10s
      timeout: 3s
      retries: 5
    depends_on:
      - db
      - otel-collector

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: app
      POSTGRES_PASSWORD: secret
    volumes:
      - db-data:/var/lib/postgresql/data

  otel-collector:
    # trace-first backend; use datalust/seq instead for structured-log-first
    # viewing (OTLP ingest via /ingest/otlp, UI on port 80)
    image: jaegertracing/all-in-one:latest
    ports:
      - "16686:16686"   # Jaeger UI
      - "4318:4318"     # OTLP HTTP

volumes:
  db-data:
```

**Rules:**
- Use the `docker compose` (v2) CLI — the hyphenated `docker-compose` v1 is
  end-of-life, and the `version:` key in compose files is obsolete.
- Multi-stage build is mandatory — no dev dependencies in the runtime image.
- The OTEL collector service is always present in `docker-compose.yml`.
- `docker compose up` must succeed from a clean clone with no manual steps.
- Add a `healthcheck` stanza to the main service so `docker compose up --wait`
  reports readiness correctly.

---

## 13 · Regeneration headers and regenerate-all.sh

Every file produced by a code generator must carry a header that names the exact CLI
command needed to reproduce it. `regenerate-all.sh` at the project root is the
single entry point to regenerate everything.

### File headers by language

The header goes on line 1 (or after a shebang). Use the comment style of the target
language. Include three lines: the "do not edit" warning, the shortcut
(`./regenerate-all.sh`), and the exact standalone command.

**TypeScript / JavaScript / Go / Java / C#** (`//`):
```typescript
// GENERATED — do not edit. Regenerate: ./regenerate-all.sh
// Full command: npx openapi-generator-cli generate \
//   -i openapi.yaml -g typescript-fetch -o generated/api-client
```

**Python / Shell / YAML / TOML** (`#`):
```python
# GENERATED — do not edit. Regenerate: ./regenerate-all.sh
# Full command: python -m grpc_tools.protoc \
#   --python_out=generated --grpc_python_out=generated schema.proto
```

**SQL** (`--`):
```sql
-- GENERATED — do not edit. Regenerate: ./regenerate-all.sh
-- Full command: npx prisma migrate dev --name init
```

**HTML / XML** (`<!-- -->`):
```html
<!-- GENERATED — do not edit. Regenerate: ./regenerate-all.sh -->
<!-- Full command: npx @hey-api/openapi-ts -i openapi.yaml -o generated/api-client -->
```

**Rules:**
- Headers apply only to files that remain schema- or template-derived. Scaffolding
  generators (`dotnet new`, `npx shadcn add`, `create-vite`) produce code you
  subsequently own and edit — no regeneration header, no `regenerate-all.sh` entry.
- The full command must be self-contained — copy-pasteable into a terminal from the
  project root and it must work.
- Multi-line commands use the language's line-continuation character (`\` for shell,
  `//` continuation for comments as shown above).
- If the generator writes many files to a directory, add the header to every file,
  not just the entry point. Generators that don't support custom headers: add a
  `README.md` inside the generated directory instead.

### regenerate-all.sh structure

`regenerate-all.sh` is created as a stub by the `…-REGEN` mandatory task. Every
subsequent task that generates files appends its own labelled section.

**Stub (created by …-REGEN task, footer included):**
```bash
#!/usr/bin/env bash
# regenerate-all.sh — Regenerate all code-generated files from their schemas.
# Run from the project root. Sections are added automatically as code gen is introduced.
# Usage: ./regenerate-all.sh
set -euo pipefail

echo "🔄  Regenerating all generated files..."
echo ""
# ── sections added by each code-generation task ───────────────────────────────
# <<< insert new sections ABOVE this line >>>

# ── done ──────────────────────────────────────────────────────────────────────
echo ""
echo "✅  All files regenerated. Commit the changes if schemas were updated."
```

**Each codegen task inserts a section above the marker line, like this:**
```bash
# ── Prisma client ─────────────────────────────────────────────────────────────
# Source: prisma/schema.prisma → Output: generated/prisma/
echo "▶  Prisma client         [generated/prisma/]"
npx prisma generate
echo "   ✓"

# ── OpenAPI → TypeScript fetch client ─────────────────────────────────────────
# Source: openapi.yaml → Output: generated/api-client/
echo "▶  OpenAPI TS client     [generated/api-client/]"
npx openapi-generator-cli generate \
  -i openapi.yaml \
  -g typescript-fetch \
  -o generated/api-client \
  --additional-properties=supportsES6=true,npmName=api-client
echo "   ✓"

# ── Jinja-templated config ─────────────────────────────────────────────────────
# Source: templates/app-config.yaml.j2 → Output: config/app-config.generated.yaml
echo "▶  App config            [config/app-config.generated.yaml]"
jinja2 templates/app-config.yaml.j2 env/dev.json > config/app-config.generated.yaml
echo "   ✓"
```

**Rules:**
- Sections run in dependency order: schema generators before client generators.
- Each section has a `# Source: → Output:` comment so it's clear what drives what.
- `set -euo pipefail` at the top ensures failure in any section aborts the whole
  script — no silent partial regeneration.
- `regenerate-all.sh` must be executable: `chmod +x regenerate-all.sh`.
- The `entropy_checkpoint` verifies that every `*.generated.*` file, and every file
  inside a dedicated `generated/` output directory, has a regeneration header.
  Files missing headers are flagged.
- `regenerate-all.sh` is added to `git` (not `.gitignore`). Generated output
  (`*.generated.*` files and `generated/` directories) should typically be
  committed too so CI doesn't require running generators — but document this
  decision in `SPEC.md §Assumptions`.

---

## 14 · Design tokens and components

Don't hand-roll a design system. Start from tokens plus a stock component library;
earn bespoke components through repetition, not upfront.

**Tokens first.** The first UI task creates a single `tokens.css` (CSS custom
properties: colour palette, spacing scale, radius, type scale). Every component and
page consumes tokens — no hardcoded hex values or magic pixel sizes in component
code. Wireframes in `plan/wireframes/` may link `tokens.css` once it exists, but
stay framework-free.

**Default component library by stack** (record the choice in `SPEC.md §Tech
constraints`):

| Stack | Default | Notes |
|-------|---------|-------|
| React / Next.js | shadcn/ui + Tailwind | Components are scaffolded into the repo (`npx shadcn add`) and then owned — no regeneration headers (§13) |
| Blazor / .NET web | MudBlazor or Fluent UI Blazor | Pick one; don't mix |
| No framework | Semantic HTML + `tokens.css` | A `components.css` of classes is enough |

**Form-over-data apps** (the common case: every entity gets a datagrid with
filters, search, hide/show columns, CSV export, plus an edit form). Build zero
bespoke grids — this is rung 1 of the abstraction ladder (§1):

| Stack | Grid | Notes |
|-------|------|-------|
| React / Next.js | TanStack Table (shadcn's table styling sits on it) | filtering, search, column visibility are column-config, not code |
| Blazor / .NET | MudBlazor `MudDataGrid` | filtering, search, hide/show built in |

- Per-entity variation lives in a column-definition table — data, not code.
- One shared export-to-CSV utility serves every grid; per-entity export code is a
  Step 11 review flag.
- Forms are only *semi*-uniform: schema-driven form generation is allowed, but
  conditional fields and cross-field validation diverge fast — watch the
  wrong-abstraction tripwires (SKILL.md Step 11) before generalising them.

**Rules:**
- No bespoke design system until an entropy checkpoint finds ≥3 hand-rolled
  components repeating the same pattern — then extract, driven by tokens.
- Restyle the stock library through tokens/theme configuration, not by forking
  component internals.
- Tailwind config (if present) maps to the same token values — one source of truth.
