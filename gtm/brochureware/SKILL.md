---
name: brochureware
description: Produce complete landing page copy and visual direction — hero, problem, solution, proof, pricing teaser, CTA — plus a styled, self-contained HTML rendering of the page. Use when preparing a landing page, fake door test, or refreshing a product site back to essentials.
user-invokable: true
---

# Brochureware

## Purpose
A single-scroll web presence (or equivalent one-pager) that communicates who the product is for, what it does, and why the visitor should care — before a full product exists. The primary goal is to generate sign-ups, enquiries, or "notify me" registrations. Secondary goal: establish credibility with the right audience and deter the wrong one.

## When to use this skill
Use when preparing a smoke test, fake door test, or early landing page. Also use when the full product site needs a refresh that brings it back to essentials.

## Required inputs
- Value proposition statement
- ICP definition
- Pain point research (for section 2 language)
- Customer language glossary (for copy tone)
- Brand adjacency recommendation (from competitive positioning)
- Any existing logo, name, or visual direction

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/05-value-proposition.md`, `docs/gtm/03-icp.md`, `docs/gtm/01-pain-point-research.md` |
| Reads (if present) | `docs/gtm/04-competitive-positioning.md` (brand adjacency recommendation) |
| Writes | `docs/gtm/09-brochureware.md` (copy + strategy), `docs/gtm/09-brochureware.html` (styled page) |

## Workflow

1. **Gather inputs.** Read the required files — the customer language glossary in the pain point research is the copy source, not decoration. If a required file is missing, check the conversation for equivalent information; if it is not there either, ask the user to run the prerequisite skill or supply the facts directly. If the brand adjacency recommendation is missing, flag that the visual tone notes are provisional and default-SaaS aesthetics have not been validated for this market.
2. **Draft the page copy** following the output structure below. Headlines and problem statements use verbatim customer language wherever possible; visual tone notes cite the brand adjacency recommendation explicitly.
3. **Self-check the copy** against the quality checklist and anti-patterns. Every headline must state an outcome; every CTA must be a specific action. Fix every failure before building the HTML.
4. **Build the styled HTML page** (see "Styled HTML version" below) implementing the finished copy and the visual tone notes. The copy in the HTML must match the copy doc word for word — the doc is the source of truth.
5. **Save and report.** Write `docs/gtm/09-brochureware.md` and `docs/gtm/09-brochureware.html`, then tell the user both paths, the hero headline and CTA, suggest opening the HTML in a browser to review, and note that the long form sales letter (`long-form-sales-letter`) can now build on this page.

## Frameworks
- **Hero → Problem → Solution → Proof → CTA** page structure (most tested long-form landing page flow)
- Copy tone derived from customer language glossary — use their words, not yours
- Visual tone derived from brand adjacency recommendation — do not default to generic SaaS aesthetics without deliberate justification

## Output structure

### 1. Page strategy note
Before copy: what is the single goal of this page? What does success look like (sign-up, enquiry, waitlist)? What is the one thing a visitor must understand?

### 2. Hero section
- **Headline**: benefit-first, outcome-focused, in the customer's language. Under 10 words preferred.
- **Sub-headline**: who it's for and what changes for them. 1–2 sentences.
- **Primary CTA**: specific action, not "Learn More". ("Get early access", "See it in action", "Book a 15-min demo")
- **Visual placeholder note**: what kind of image, illustration, or screenshot goes here, and why (reference brand adjacency recommendation)

### 3. Problem section
Name 3 specific pain points by their consequence, not their cause. Use verbatim customer language where possible.
> "You're spending [X hours] every week manually matching invoices to jobs — and still getting it wrong."

### 4. Solution section
3 key capabilities, each expressed as an outcome:
- What it does → What the customer gets

### 5. How it works
3-step process. Short labels + one-sentence descriptions. This reduces fear of complexity.

### 6. Social proof section
Options depending on stage:
- Early: "Built with input from [N] [ICP] businesses" + pilot customer names/logos (with permission)
- Later: testimonials, case study excerpts, quantified results

Placeholder text provided if no real proof exists yet — clearly marked as placeholder.

### 7. Pricing teaser
Either a specific pricing tier or a clear signal of price range. "Plans from $X/month" or "Book a call to get a quote." Ambiguity here loses conversions.

### 8. Footer CTA
Repeat the primary CTA. Short copy variant — different angle from the hero.

### 9. Copy tone notes
3–5 specific tone guidelines derived from customer language and brand adjacency audit:
- What to sound like
- What to avoid sounding like
- Specific words or phrases to use or not use

### 10. Visual tone notes
Based on brand adjacency recommendation:
- Colour palette direction (reference competitor audit)
- Photography or imagery style
- Typography personality
- Whether to lean into an "established" aesthetic or differentiate

## Styled HTML version

Alongside the copy doc, produce `docs/gtm/09-brochureware.html` — a working, styled rendering of the page that can be opened in a browser, shown to a pilot customer, or deployed as-is for a smoke test.

Requirements:
- **Single self-contained file**: inline CSS in a `<style>` block, no build step, no JavaScript frameworks, no external stylesheets. At most one Google Fonts link if the typography direction requires it; otherwise use a system font stack.
- **Styling implements the brand adjacency recommendation**: colour palette, typography personality, and overall register come from the visual tone notes — not from default SaaS conventions. If the recommendation says "established and trade-trustworthy", the page should look that way.
- **Full page structure**: hero, problem, solution, how it works, social proof, pricing teaser, footer CTA — every section from the copy doc, with the copy reproduced word for word.
- **Image placeholders**: where the visual placeholder notes call for photography or screenshots, render a clearly-labelled placeholder block (`<div class="placeholder">Photo: technician at switchboard — see visual notes</div>`) rather than a stock image or an empty gap.
- **Responsive and semantic**: works at phone and desktop widths; uses `<header>`, `<main>`, `<section>`, `<footer>`; one `<h1>`; CTAs are real `<a>` or `<button>` elements with a `#` or mailto placeholder href.
- **Form stubs, not fake forms**: if the CTA is a sign-up, render the email field and button but point the form action at a clearly-marked placeholder so the user knows to wire it up.

## Quality checklist
- [ ] Headline states an outcome, not a category or feature
- [ ] Problem section uses customer language from pain point research
- [ ] CTA is specific and actionable, not generic
- [ ] Visual tone notes reference the brand adjacency recommendation, not generic SaaS conventions
- [ ] Social proof section exists (even if placeholder)
- [ ] Pricing is not hidden
- [ ] Footer repeats the CTA
- [ ] HTML version exists, is a single self-contained file, and opens cleanly in a browser
- [ ] HTML copy matches the copy doc word for word
- [ ] HTML styling follows the brand adjacency recommendation, and image placeholders are labelled with what belongs there

## Anti-patterns
- Headline that describes what the product is instead of what it does for the customer
- Stock photo of a person on a laptop in a coffee shop
- "Powerful, flexible, and easy to use" in any copy block
- Hiding pricing entirely ("contact us for pricing") on an early-stage B2B SaaS landing page
- Visual design that defaults to Tailwind/SaaS blue without checking the brand adjacency recommendation first
