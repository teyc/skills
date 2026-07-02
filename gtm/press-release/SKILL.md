---
name: press-release
description: Write an Amazon working-backwards press release that defines the product by announcing it as if it has already launched successfully. Use at the start of a new product or feature to align on what success looks like; always pair with the faq-bezos skill.
user-invokable: true
---

# Press Release (Working Backwards)

## Purpose
A working-backwards artifact that defines the product by writing its public announcement as if it has already launched successfully. The discipline of writing a press release before building forces clarity on who the customer is, what problem is solved, and why the solution matters — before a line of code is written or a dollar is spent. This is not a real press release to be distributed; it is a strategic alignment document.

## When to use this skill
Use at the start of a new product or feature, when the team needs to align on what success looks like. Revisit when scope starts to drift. Pair with the FAQ skill (the companion document).

## Required inputs
- Value proposition statement (or ICP + pain points if not yet written)
- Product name (working title is fine)
- Target customer description
- Core capability or mechanism (what it actually does)
- Imagined launch date (helps make it feel concrete)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/05-value-proposition.md` (or `docs/gtm/03-icp.md` + `docs/gtm/01-pain-point-research.md` if not yet written) |
| Reads (if present) | `docs/gtm/04-competitive-positioning.md` |
| Writes | `docs/gtm/07-press-release.md` |

## Workflow

1. **Gather inputs.** Read the value proposition; fall back to the ICP and pain point research if it does not exist yet. Get the product name (working title is fine), core mechanism, and an imagined launch date from the user or the conversation; ask only for what is missing everywhere.
2. **Draft the press release** following the output structure below, written entirely as if the product has already shipped and customers love it. Pull the problem paragraph's language from the pain point research verbatim where possible.
3. **Self-check** against the quality checklist and anti-patterns. Apply the two tests: would a journalist cover this, and would someone forward it to a colleague? Fix every failure before saving.
4. **Save and report.** Write the file to `docs/gtm/07-press-release.md`, then tell the user the path and the headline — and immediately offer to run the `faq-bezos` skill, because the two documents always ship as a pair.

## Frameworks
- **Amazon PR/FAQ format**: the press release is always written as if the product has already shipped and customers love it. It must pass the "would a journalist cover this?" test.
- The document is internal. It is not optimised for SEO or for a real wire service. It is optimised for clarity of thinking.

## Output structure

### Headline
Product name + the single most important customer benefit. One sentence. Under 10 words if possible.
> Example: "Ascora Reconciler Gives HVAC Businesses Their Job Costs Back in Minutes"

### Sub-headline
Expands on the headline: who it's for, what they get, what changes for them.

### Dateline
[City, Imagined Date] —

### Opening paragraph
The summary: what the product is, who it is for, what the main benefit is. A journalist should understand the story from this paragraph alone.

### Problem paragraph
The pain the product solves. Written from the customer's perspective. Specific, not generic. References the frequency and severity of the problem.

### Solution paragraph
How the product solves it. Focus on the mechanism and the outcome, not the feature list. Avoid jargon.

### Executive quote
A quote from the founder or CEO. Tone: vision, belief, mission. Should sound like a person, not a press release.
> "We built this because we watched [customer type] [describe specific pain] for years. There was no reason it had to be this hard."

### Customer quote
A quote from an imagined (or real) customer. Tone: outcome, relief, specific result. Must reference a concrete before/after.
> "Before [product], I was spending [X hours] every week manually matching invoices. Now it takes [Y minutes]."

### Call to action
What does an interested reader do next? Sign up, request access, visit a page.

### Boilerplate
2–3 sentences about the company: who you are, where you are based, what you do.

## Quality checklist
- [ ] Headline names a benefit, not a feature
- [ ] Opening paragraph works as a standalone summary
- [ ] Problem paragraph describes the pain in the customer's language (reference pain point research)
- [ ] Customer quote includes a specific before/after result
- [ ] Executive quote sounds human, not corporate
- [ ] No feature list appears anywhere in the document
- [ ] Passes the "would someone forward this to a colleague?" test

## Anti-patterns
- Listing features instead of outcomes
- Writing in marketing superlatives ("revolutionary", "game-changing")
- Making the executive quote sound like the marketing team wrote it
- Forgetting the call to action
- Confusing this with a real press release for media distribution
