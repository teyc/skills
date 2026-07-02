---
name: value-proposition
description: Write an April Dunford-style positioning statement from which all downstream copy is derived — competitive alternatives, differentiators, value, target segment, market category, plus one-liner variants. Use after ICP and pain point research are complete and before writing any customer-facing copy.
user-invokable: true
---

# Value Proposition Statement

## Purpose
A precise positioning statement from which all downstream copy is derived. Brochureware headlines, sales letter hooks, cold email openers, and pitch deck one-liners should all be traceable back to this document. Written once, used everywhere. Updated when the ICP or competitive landscape changes.

## When to use this skill
Use after ICP and pain point research are complete and before writing any customer-facing copy.

## Required inputs
- ICP definition
- Pain point research (top 3 pains)
- Known competitors or alternatives (even rough)
- Any differentiated capability or approach the product has

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/03-icp.md`, `docs/gtm/01-pain-point-research.md` |
| Reads (if present) | `docs/gtm/04-competitive-positioning.md` |
| Writes | `docs/gtm/05-value-proposition.md` |

## Workflow

1. **Gather inputs.** Read the required files. If either is missing, check the conversation for equivalent information; if it is not there either, ask the user to run the prerequisite skill or supply the facts directly. If the competitive positioning document exists, use its alternatives and wedge rather than re-deriving them.
2. **Draft the statement** following the output structure below. Work through Dunford's components in order — alternatives first, then differentiators, then value — because each constrains the next. Keep it clinical: this is an internal document, not ad copy.
3. **Self-check** against the quality checklist and anti-patterns. Test each differentiator: is it specific and testable, and would fewer than 3 competitors claim it? Fix every failure before saving.
4. **Save and report.** Write the file to `docs/gtm/05-value-proposition.md`, then tell the user the path, the one-sentence version, any unproven claims flagged in the proof points section, and that pricing strategy, press release, brochureware, sales letter, and keyword research are now unblocked.

## Frameworks
- **April Dunford's positioning framework**: the five components are (1) competitive alternatives, (2) differentiated attributes/capabilities, (3) value those attributes deliver, (4) target customer who cares about that value, (5) market category to frame the offering
- The positioning statement is internal — it is not ad copy. It is precise and a little clinical. Copy comes after.

## Output structure

### 1. Competitive alternatives
What does the ICP do today instead of using your product? (Not just direct competitors — include "spreadsheet + phone call" and "do nothing".)

### 2. Differentiated attributes
What do you do or have that alternatives don't? Be specific. "Easier to use" is not a differentiator. "Matches Reece invoices to Ascora jobs automatically without manual entry" is.

### 3. Value delivered
For each differentiated attribute, what is the outcome for the customer? (Time saved, money recovered, risk avoided, compliance achieved.)

### 4. Target segment
Precise ICP reference. Who specifically cares about this value.

### 5. Market category
What kind of thing is this? The category frames expectations and comparison. "Job costing tool for HVAC trades" sets different expectations than "AI reconciliation platform."

### 6. Positioning statement (full)
Fill-in structure:
> For [target customer] who [trigger event / problem], [product name] is a [market category] that [key benefit]. Unlike [competitive alternative], [product name] [key differentiator].

### 7. One-sentence version
Distilled to a single sentence suitable for a LinkedIn bio, pitch deck cover, or email signature.

### 8. Three copy variants
Three alternative phrasings of the one-liner — different emphasis, different tone. Used for A/B testing headlines.

### 9. Proof points required
List of claims in the positioning that need evidence before they can be stated publicly. Flag any that are currently unproven.

### 10. What NOT to claim
Positioning you are deliberately avoiding — either because it's overcrowded, unprovable, or sets the wrong expectation.

## Quality checklist
- [ ] Competitive alternatives section includes "do nothing" or status quo
- [ ] Differentiated attributes are specific and testable, not adjectives
- [ ] Value statements are outcomes (time, money, risk), not features
- [ ] Proof points section flags anything currently unsubstantiated
- [ ] One-sentence version could be read aloud in 5 seconds

## Anti-patterns
- Writing positioning copy instead of a positioning statement
- Using "innovative", "seamless", or "powerful" anywhere
- Claiming a differentiator that 3 competitors also claim
- Skipping the "what NOT to claim" section
