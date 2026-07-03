---
name: design-session
description: >
  Run an interactive, timeboxed design exploration with an SME in the room —
  rounds of keep/kill/steal over a live token configurator, a preset library,
  and pre-generated structural directions, ending at the buzzer with DESIGN.md
  and tokens.css for /build-loop to consume. Use when the user wants a design
  session, mood boards, look-and-feel exploration, or design tokens for a new
  app, or when /build-loop finds a web UI with no DESIGN.md. Requires a human
  present to react — not for autonomous runs, and not for implementing UI
  (that's /build-loop).
---

# /design-session — Timeboxed Design Exploration

A design session is not a loop — there is no fitness function for taste. It
converges because an SME reacts and the clock runs out. Your job is to make
sure the SME never waits: every design move has a latency class, and the class
dictates where it is allowed to happen.

| Class | Cost | Mechanism | Allowed when |
|-------|------|-----------|--------------|
| Parametric | instant | token configurator + presets | any time — the bulk of every round |
| Small mutation | ~seconds | cheap-model patch, run in parallel | during SME reaction time |
| Structural | minutes | Stitch / frontier-model generation | prep phase, speculative, or between sessions — **never while the SME watches** |

**Hard rule: this skill needs a human.** If no SME is present and reacting,
stop and schedule the session — do not simulate their taste to keep momentum.

---

## Phase A — Prep (async, before the SME arrives)

Run this as soon as the session is booked. Slow tools are fine when nobody is
waiting.

1. **Frame from the spec.** Read `SPEC.md` (Goal, JTBD, delivery shape) if it
   exists, otherwise the brief. Note domain nouns for realistic sample data —
   a datagrid of `WorkOrder`s beats a datagrid of `Lorem Ipsum`s.
2. **Build the configurator.** Copy `assets/configurator.html` next to the
   project's planning files (`plan/moodboards/configurator.html`) and adapt it:
   real entity names, real columns, real form fields. Spec in
   `references/configurator.md` (read before adapting). Every visual property
   must run through a CSS custom property — if changing it needs a
   regeneration, it is wired wrong.
3. **Load the presets.** `references/presets.md` ships the starter library.
   Add 1–2 project-specific presets if the brief implies a direction.
4. **Pre-generate structural directions** (optional): if the Stitch MCP is
   connected, generate 3–4 divergent full-screen directions from the JTBD; else
   generate 2–3 locally as static HTML variants. Apply the anti-cliché critique
   *before* anything enters the gallery: no default cream-serif-terracotta, no
   near-black with acid green, no hairline-newspaper — unless the brief asks.
5. Archive everything under `plan/moodboards/round-0/`.

## Phase B — Session (SME present, timeboxed in rounds)

**Round 0 · frame (~10% of the box).** Confirm mood words (≤3 questions,
grill-style). Declare the timebox in rounds — default **3** — and the exit
rule: *"We stop at the buzzer with the best thing on the table, not when it's
perfect."* The SME owns the wall clock and may call "last round" at any time.

**Rounds 1..N · diverge, react, breed.**

1. Show ≤5 things at once — SME attention is the scarce resource, not
   generation capacity. Round 1 is maximally divergent (presets + prep-phase
   directions); later rounds narrow.
2. Collect **keep / kill / steal** reactions ("nav from B, palette from D,
   kill anything beige"). Record kills verbatim — the kill-list is as valuable
   as the picks.
3. **While the SME talks, breed speculatively.** Fire cheap-model mutations of
   the likely survivors in parallel *before* the verdict lands. Discard
   speculations whose parents die; present the rest instantly. Wrong guesses
   cost cheap-tier tokens; right guesses cost zero SME seconds.
4. If something genuinely novel must be generated live, say: *"That's a
   between-rounds job — meanwhile let's tune what's in front of us."* Fill any
   unavoidable wait with elicitation (copy tone, empty states, error states,
   density preferences) — never a spinner.
5. Parametric moves happen live in the configurator, hands on sliders.
   Archive each round's state to `plan/moodboards/round-N/`.

**SME-silence rule:** reactions stop → session pauses. Resume when they do.

## Phase C — Buzzer · distill (last ~10%)

1. Export the configurator's winning state as `tokens.css` (the export button
   emits it — no transcription).
2. Write `DESIGN.md` per `references/design-md-format.md`: mood words,
   direction summary, type pairs, signature element, density rules, the
   kill-list with SME quotes, and open questions (recorded, not resolved —
   the timebox is load-bearing).
3. Confirm the handoff: `/build-loop`'s wireframe and UI tasks consume
   `DESIGN.md` + `tokens.css`; §14 of its coding standards themes the stock
   component library through these tokens.

---

## Gotchas

**Never regenerate what a CSS variable can change.** If the SME asks for
"warmer" or "denser," that's a slider, not a generation. Reach for models only
when structure changes.

**Speculation is disposable by design.** Breed on the cheap model tier and
expect to throw most of it away — that's the budget working, not waste.

**Presets are the opening bid, not the answer.** A session that ends on an
unmodified preset probably didn't explore; a session that ends 10 mutations
from one probably did.

**Stitch is optional.** No MCP connection → local HTML directions. Degrade
silently; never block the session on tooling.

**≤5 variants per round.** More options slow the SME down more than they slow
you down — comparison cost is quadratic in what's on the table.

**The kill-list outlives the session.** "SME hates beige" prevents more rework
than "SME chose indigo."
