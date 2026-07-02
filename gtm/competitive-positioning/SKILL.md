---
name: competitive-positioning
description: Analyse direct, indirect, and do-nothing competitors, audit each competitor's brand aesthetic by visiting their site, recommend brand adjacency, and produce a sales battle card. Use after the ICP is drafted, when a new competitor appears, after a lost deal, or when repositioning.
user-invokable: true
---

# Competitive Positioning & Battle Card

## Purpose
A structured analysis of the competitive landscape covering: direct competitors, indirect competitors, and the "do nothing" alternative. Includes a brand aesthetic audit — assessing how each competitor presents itself visually and tonally — which informs the decision about how your own brand should look and feel. The output ends in a battle card: a fast-reference sheet for sales conversations.

## When to use this skill
Use after ICP and value proposition are drafted. Update when a new competitor enters, after a lost deal, or when repositioning.

## Required inputs
- Product / solution description
- ICP definition
- Known competitors (name them; Claude will research others)
- URL of each competitor's website (or Claude will find them)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/03-icp.md` |
| Reads (if present) | `docs/gtm/01-pain-point-research.md`, `docs/gtm/05-value-proposition.md` |
| Writes | `docs/gtm/04-competitive-positioning.md` |

## Workflow

1. **Gather inputs.** Read `docs/gtm/03-icp.md`. If it is missing, check the conversation for an ICP; if there is none, ask the user to run the `icp` skill first or describe the target customer directly.
2. **Build the competitor list.** Start with competitors the user names, then run web searches to find others the ICP would actually consider — including at least one indirect alternative. Always include "do nothing" as a competitor.
3. **Visit every competitor website** with web fetch/search — never audit from memory or from their marketing copy alone. Capture positioning, pricing, and every attribute in the brand aesthetic audit table while you are on the site. If a site cannot be reached, say so in the document rather than filling the row from memory.
4. **Draft the artifact** following the output structure below, ending with the battle card and an opinionated brand adjacency recommendation.
5. **Self-check** against the quality checklist and anti-patterns — in particular, confirm every battle card entry has an honest "when we lose" line. Fix every failure before saving.
6. **Save and report.** Write the file to `docs/gtm/04-competitive-positioning.md`, then tell the user the path, the positioning wedge in one sentence, the brand adjacency recommendation in one sentence, and that pricing strategy (`pricing-strategy`) is now unblocked and the brand recommendation feeds `brochureware`.

## Frameworks
- **April Dunford — competitive alternatives model**: the comparison is always "compared to what?" Include the status quo and DIY options.
- **Brand Era Audit** (custom): assess the visual/tonal era of each competitor's web presence. Markets have a trust aesthetic — the visual conventions that signal credibility to that specific audience. Your job is to be adjacent to that aesthetic, not naively "modern."
- **Battle card format**: what to say when the prospect mentions a specific competitor name.

## Output structure

### 1. Competitor table
For each competitor (including "do nothing"):

| Attribute | Detail |
|---|---|
| Name | |
| Website | |
| Core positioning | |
| Target customer | |
| Pricing model | |
| Key strengths | |
| Key weaknesses | |
| What triggers a customer to choose them | |
| What triggers a customer to leave them | |

### 2. Brand aesthetic audit
**This section requires visiting each competitor's website.** For each competitor, assess and document:

| Attribute | Detail |
|---|---|
| Design era | What decade does this site feel like? (90s, early 2000s, 2010s flat design, 2020s modern) |
| Colour palette character | Corporate blues, earthy/industrial, muted neutrals, bold/saturated, monochrome, etc. |
| Typography personality | Serif (traditional/authoritative), sans-serif (clean/modern), heavy/bold, light/airy |
| Imagery style | Stock photography, real customer photos, illustrations, screenshots, video, minimal |
| Copywriting tone | Formal/technical, plain-spoken, conversational, aspirational, fear-based |
| Trust signals deployed | Certifications, client logos, case study counts, years-in-business, industry awards |
| Overall emotional register | Authoritative, friendly, technical, premium, no-frills, urgent |
| Mobile experience | Responsive and modern, or clearly an afterthought |

**Brand era interpretation:** Note whether the design era appears to be a deliberate choice or neglect. For markets where the customer base skews older, trade-focused, or risk-averse, an "established" visual aesthetic may signal trustworthiness and longevity rather than staleness. A shiny modern site may read as "startup risk" to a tradie who has been burned by software vendors before.

### 3. Brand adjacency recommendation
Based on the audit, answer:
- What is the dominant visual register in this market?
- Does the audience appear to trust that aesthetic, or are they underserved by it?
- Should your brand be: (a) adjacent to the dominant aesthetic, (b) a deliberate contrast, or (c) a modernised version of it?
- Specific guidance on: colour palette direction, typography choice, photography style, copywriting tone

### 4. "Do nothing" alternative
What does the customer actually do today with no software? Describe the workflow, the pain, the workaround tools (Excel, WhatsApp, paper).

### 5. Positioning wedge
Where are you genuinely different, and why does it matter to the ICP? One paragraph. Specific and honest — not a list of adjectives.

### 6. Battle card
Fast-reference sheet for sales conversations. For each named competitor:

> **When they mention [Competitor]:**
> Acknowledge: "Yes, [Competitor] is a solid option for [their strength]."
> Differentiate: "The difference is [specific, provable claim]."
> Proof: "[Evidence, customer quote, or specific example]."
> When we win: [situations where we are the better choice]
> When we lose: [situations where they are genuinely the better choice — be honest]

## Quality checklist
- [ ] Every competitor's website has been visited and audited, not described from memory
- [ ] "Do nothing" is treated as a real competitor with strengths and weaknesses
- [ ] Brand aesthetic audit includes era assessment and trust signal inventory
- [ ] Brand adjacency recommendation makes a specific, opinionated recommendation
- [ ] Battle card includes honest "when we lose" entries
- [ ] Positioning wedge is specific enough to disprove — vague claims are not wedges

## Anti-patterns
- Describing competitors from memory or their own marketing copy without visiting their site
- Writing "our product is better in every way" in the positioning wedge
- Omitting the "do nothing" alternative
- Brand audit that only notes colours without interpreting what they signal to the target customer
- A battle card that only tells you what to say, not when to say it
