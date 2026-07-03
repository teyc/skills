# DESIGN.md Format

Read when: distilling at the buzzer (Phase C).

`DESIGN.md` is to look-and-feel what `glossary.md` is to naming: law for every
downstream UI task. `/build-loop` wireframe and UI tasks read it before
touching a screen; implementer taste does not override it — changes go through
a follow-up session or an explicit user decision recorded here.

```markdown
# Design: [Project name]
> Session: [date] · Rounds: N · SME: [name/role]
> Tokens: tokens.css (exported from configurator — do not hand-edit values here)

## Mood words
[3–5 words the SME confirmed, e.g. "calm, dense, engineered, unbranded"]

## Direction
[One paragraph: what this looks and feels like, and the one-line rationale
tied to the JTBD. Name the winning lineage, e.g. "linear-dark preset + warmer
surface + 2 density notches looser".]

## Type
- **Display**: [family] — [role, e.g. page titles only]
- **Body**: [family]
- **Mono**: [family] — [role, e.g. IDs, timestamps, amounts in grids]

## Signature element
[The one memorable, ownable thing — e.g. "status badges are square with a
thick left border, never pills". If the session didn't find one, say so.]

## Density & layout rules
- [e.g. "Grid rows: compact (--space × 2.5); forms: relaxed (--space × 4)"]
- [e.g. "One accent per screen; charts use the dataviz neutral ramp"]

## Kill-list — do NOT do these
- [Rejected direction]: "[SME's verbatim words]"
- [e.g. Beige/cream surfaces: "looks like every AI demo"]

## Open questions
- [Unresolved taste question] → owner, revisit trigger
  (recorded at the buzzer, deliberately not resolved in-session)

## Provenance
- Rounds archived: plan/moodboards/round-0..N/
- Presets considered: [list] · Winner lineage: [preset + mutations]
```

**Rules:**
- The kill-list is mandatory and verbatim — it prevents more rework than the
  picks do.
- `tokens.css` is the single source of truth for values; DESIGN.md carries
  *intent and rules*, never duplicated hex codes (drift risk).
- Open questions must have a revisit trigger ("when the dashboard epic
  starts"), or they're just deferred forever.
- Hand-off check: build-loop Step 1 looks for this file whenever the delivery
  shape includes a web UI.
