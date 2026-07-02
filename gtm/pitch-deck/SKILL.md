---
name: pitch-deck
description: Outline a 10–14 slide narrative pitch deck with per-slide messages, content direction, and speaker notes, adapted for investor, channel partner, or strategic customer audiences. Use when preparing a fundraising conversation, partnership meeting, or formal customer presentation.
user-invokable: true
---

# Pitch Deck

## Purpose
A structured narrative deck (10–14 slides) for pitching to investors, channel partners, or strategic customers. The deck tells a story — a problem exists, it is large and underserved, you have a specific solution and proof it works, and you are the right team to scale it. This skill produces the slide-by-slide outline and copy direction. The actual visual design uses the pptx or claude_design skill.

## When to use this skill
Use when preparing for a fundraising conversation, a channel partner meeting, or a strategic customer who requires a formal presentation before committing. Adapt the emphasis based on audience type (investor vs. partner vs. customer).

## Required inputs
- Press release and FAQ (completed)
- Value proposition statement
- ICP definition
- Any traction data (pilot customers, revenue, usage metrics)
- Team description
- What you are asking for (investment amount, partnership type, pilot scope)
- Audience type (investor / channel partner / strategic customer)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/05-value-proposition.md`, `docs/gtm/04-competitive-positioning.md`, `docs/gtm/06-pricing-strategy.md`, `docs/gtm/07-press-release.md` |
| Reads (if present) | `docs/gtm/08-faq.md`, `docs/gtm/03-icp.md`, `docs/gtm/15-case-study-*.md`, any traction data |
| Writes | `docs/gtm/14-pitch-deck.md` |

## Workflow

1. **Gather inputs.** Read the required files. If any are missing, check the conversation for equivalent information; if it is not there either, ask the user to run the prerequisite skills or supply the facts directly. Ask the user for the three things only they know: the audience type (investor / partner / customer), real traction data, and the specific ask.
2. **Draft the outline** following the slide-by-slide structure below, applying the variant notes for the chosen audience. Build market size bottom-up from ICP count; present traction exactly as it exists — if there is none, rename the slide "pilot plan" rather than dressing up projections.
3. **Self-check** against the quality checklist and anti-patterns. Read the deck cold: does it work as a leave-behind without a presenter? One message per slide. Fix every failure before saving.
4. **Save and report.** Write the file to `docs/gtm/14-pitch-deck.md`, then tell the user the path, the narrative arc in 2–3 sentences, the weakest slide and what evidence would strengthen it, and that visual design is a separate step (pptx or design skill) using this outline.

## Frameworks
- **Sequoia deck structure**: the most battle-tested investor narrative structure. Adapted here for multiple audience types.
- **Narrative over bullets**: Bezos's documented preference — slides should advance a story, not list points. Each slide has one message.
- **The traction slide is the most important slide**: even early proof changes a pitch. Know what you have and lead with the most convincing version of it.

## Output structure

For each slide: **title**, **one-line message** (what the audience should think after this slide), **content direction**, **speaker note prompt**.

---

**Slide 1 — Cover**
Message: This is what we are and who we are.
Content: Company name, one-liner from value proposition, presenter name, date.

**Slide 2 — The problem**
Message: This pain is real, frequent, and costly — and it affects a large number of people.
Content: Describe the pain in the customer's language. Use a specific scenario or number. Avoid abstract market language.
*Investor variant*: quantify the cost of the problem.
*Customer variant*: describe the day-to-day pain directly.

**Slide 3 — The solution**
Message: Here is a specific, believable way to fix it.
Content: What the product does in plain terms. How it works in 3 steps or fewer. What changes for the customer.

**Slide 4 — Why now**
Message: The timing is right for this to exist and to win.
Content: What has changed recently (technology, regulation, behaviour, cost curve) that makes this possible or urgent now. Not required for customer pitches.

**Slide 5 — Market size**
Message: This is a large, specific, reachable market.
Content: TAM / SAM / SOM with honest rationale. Do not use top-down "if we get 1% of a $10B market" logic. Build from the ICP count upward.
*Investor variant*: required.
*Partner/customer variant*: optional — frame as "how many businesses like yours face this."

**Slide 6 — Product**
Message: This is real and it works.
Content: Screenshot, demo flow, or simple diagram of how the product works. The most concrete slide in the deck.

**Slide 7 — Business model**
Message: We know how we make money and it is repeatable.
Content: Pricing structure, tier logic, revenue per customer. Unit economics if known.

**Slide 8 — Traction**
Message: We have evidence this works beyond theory.
Content: Pilot customers (named if permitted), usage metrics, revenue, retention, NPS, letters of intent. Present what you have honestly — no traction is better acknowledged than obscured.

**Slide 9 — Competition and positioning**
Message: We understand the landscape and have a clear, defensible position.
Content: Positioning map or competitor table. Summarise from competitive positioning document. Do not claim to have no competitors.

**Slide 10 — Team**
Message: We are the right people to build and scale this.
Content: Names, relevant experience, why this team for this problem. Include advisors if strong.

**Slide 11 — The ask**
Message: Here is what we need and what we will do with it.
Content: Specific amount or commitment requested. Milestones it will fund. What success looks like in 12–18 months.
*Investor variant*: funding amount, use of funds, target milestones.
*Partner variant*: what the partnership involves and what both parties get.
*Customer variant*: pilot terms, commitment level, timeline.

**Appendix slides (as needed)**
- Detailed financials or projections
- Extended product screens
- Case study detail
- Technical architecture (for technical audiences)

---

### Audience adaptation notes
Note specific slide emphasis changes for each audience type.

## Quality checklist
- [ ] Each slide has one message, not a list of points
- [ ] Traction slide presents what exists, not what is projected
- [ ] Market size is built bottom-up from ICP count, not top-down from analyst reports
- [ ] Competition slide does not claim "no competitors"
- [ ] Ask slide is specific (amount, milestones, timeline)
- [ ] Deck can be read cold without the presenter (leave-behind quality)
- [ ] Total deck is 10–14 slides (not counting appendix)

## Anti-patterns
- Bullet point slides (use sentences or visuals)
- Market sizing that relies on "if we capture 1% of a $X billion market"
- A traction slide with no traction on it (rename it "roadmap" or "pilot plan" if needed)
- Team slide with no relevant experience connected to this specific problem
- An ask that doesn't state what the money or commitment will achieve
