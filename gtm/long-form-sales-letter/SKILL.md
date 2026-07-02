---
name: long-form-sales-letter
description: Write a 500–1500 word direct response sales letter plus a structured copywriter critique with element-by-element scores. Use when a headline is not enough — the product needs education, objection handling, or a price point justified before the reader will act.
user-invokable: true
---

# Long Form Sales Letter

## Purpose
A persuasive long-form copy document (500–1500 words) designed to move a cold or warm reader to a specific action. Used on landing pages, in email sequences, or as the body of a sales page. The output includes both the letter itself and a structured copywriter critique — a second pass that stress-tests the draft against proven direct response standards.

## When to use this skill
Use when a brochureware headline and sub-headline are not enough — the product requires education before conversion, the price point justifies longer copy, or the ICP needs objection handling before they'll act.

## Required inputs
- ICP definition (who is reading this?)
- Primary pain point (the one to lead with)
- Value proposition statement
- One specific desired action (the CTA — there is only one)
- Any existing testimonials, case studies, or proof points
- Price point (or price range) to be disclosed

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/05-value-proposition.md`, `docs/gtm/03-icp.md` |
| Reads (if present) | `docs/gtm/01-pain-point-research.md`, `docs/gtm/09-brochureware.md`, `docs/gtm/15-case-study-*.md` |
| Writes | `docs/gtm/10-sales-letter.md` |

## Workflow

1. **Gather inputs.** Read the required files. If either is missing, check the conversation for equivalent information; if it is not there either, ask the user to run the prerequisite skill or supply the facts directly. Confirm the single CTA and the price to be disclosed — do not draft without both.
2. **Choose the framework** (PAS if the reader must be convinced the problem is real; AIDA if they already know it) and state the choice and reason at the top of the document.
3. **Draft the letter** following Part 1 of the output structure. Use verbatim customer language from the pain point research in the problem and agitation blocks.
4. **Critique it as a separate pass.** Re-read the finished letter cold and score every element in the Part 2 table honestly — a critique where everything scores 4–5 is worthless. Name specific lines to cut and words to eliminate.
5. **Apply the top fixes.** Revise the letter for the critique's top 3 issues, keeping the critique in the document so the user can see what changed and what still needs real proof.
6. **Self-check** against the quality checklist and anti-patterns, then write the file to `docs/gtm/10-sales-letter.md`. Tell the user the path, the headline, and any places where placeholder proof needs replacing with real results.

## Frameworks
- **PAS (Problem → Agitate → Solve)**: open on the problem, make the reader feel it, then present the solution. Best for audiences who need to be convinced the problem is real.
- **AIDA (Attention → Interest → Desire → Action)**: open with a hook, build interest, create desire through proof, close with a CTA. Best for audiences who already know the problem.
- **Direct response copywriting principles**: specificity over vagueness; proof over claims; one CTA; subheadings that sell (not just organise); short sentences; no orphaned paragraphs.

## Output structure

### Part 1: The letter

**Headline**
The most important line. Benefit-first. Specific. Could stand alone as an ad.

**Hook / opener (1–3 paragraphs)**
Earns the reader's attention before making any claim. Opens on a situation the ICP recognises or a statement that disrupts a lazy assumption.

**Problem block**
Names the pain and its consequences. Uses customer language. Makes the reader feel the cost of inaction. Does not rush to the solution.

**Agitation / proof of problem**
Deepens the pain. Specific scenarios. Statistics or anecdotes if available. Objection pre-handling: "You might think [X workaround] is good enough — here's why it isn't."

**Solution reveal**
Introduces the product. Names what it does and how it works in plain terms. Connects directly to the pains named above.

**Proof block**
Testimonials, case study results, or quantified outcomes. If none exist yet, use "During our pilot..." or "In early testing..." — and mark clearly in the critique that real proof is needed here.

**Offer and pricing**
Clear statement of what is being offered and at what price. No ambiguity.

**Risk reversal**
What removes the risk of trying? (Trial period, money-back guarantee, free setup, pilot program.)

**Close + CTA**
Single, specific action. Urgency if genuine. No multiple CTAs.

**P.S.**
The most-read part of a sales letter after the headline. Restate the most compelling benefit and the CTA in 1–2 sentences.

---

### Part 2: Copywriter critique

A structured critique of the draft above. Score each element and note specific improvements.

| Element | Score (1–5) | Specific issue / recommendation |
|---|---|---|
| Headline strength | | |
| Hook quality (does it earn the read?) | | |
| Problem specificity | | |
| Agitation — does it land emotionally? | | |
| Proof — is it credible and specific? | | |
| Offer clarity | | |
| Risk reversal — is it believable? | | |
| CTA clarity and singularity | | |
| Reading grade level (target: 8–10) | | |
| Sentence length variety | | |
| Subheadings — do they sell or just organise? | | |

**Top 3 things to fix before publishing:**
1.
2.
3.

**Lines to cut** (specific passages that weaken the letter)

**Words to eliminate** (vague, overused, or trust-eroding terms)

## Quality checklist
- [ ] Headline names a specific outcome, not a product feature
- [ ] There is only one CTA in the entire letter
- [ ] P.S. exists and restates the core offer
- [ ] Proof block is specific — numbers, timeframes, customer names where permitted
- [ ] Copywriter critique scores every element
- [ ] Reading grade level is assessed (target 8–10, not lower)

## Anti-patterns
- Multiple CTAs (dilutes conversion)
- Proof block that says "customers love it" without specifics
- Subheadings that summarise instead of sell ("About Our Pricing" vs "Here's What It Costs — And Why It Pays For Itself")
- Opening with the company history or "we were founded in..."
- A P.S. that introduces new information instead of reinforcing the close
