---
name: pain-point-research
description: Evidence-based research into the real problems of a target customer segment, with citable sources and a verbatim customer language glossary. Use when validating a problem hypothesis before committing to a product direction, or when gathering evidence to anchor an ICP, press release, or sales letter.
user-invokable: true
---

# Pain Point Research

## Purpose
Structured research into the genuine problems experienced by a target segment, with citable sources. The output validates assumptions, surfaces the language customers use about their own pain, and identifies gaps that competitors are not addressing. All claims must link to evidence — forums, reviews, industry reports, or interviews.

## When to use this skill
Use when the user needs to validate a problem hypothesis before committing to a product direction, or when they need evidence to anchor a press release, ICP, or sales letter.

## Required inputs
- Target segment (industry, role, company size)
- Problem hypothesis (even rough: "we think HVAC businesses struggle with invoice reconciliation")
- Any competitor products or categories already known

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (if present) | `docs/gtm/03-icp.md` (even a rough ICP hypothesis sharpens the research) |
| Writes | `docs/gtm/01-pain-point-research.md` |

## Workflow

1. **Gather inputs.** Read `docs/gtm/03-icp.md` if it exists. Get the target segment and problem hypothesis from the user or the conversation; if neither states them, ask — this skill cannot run without a segment to research.
2. **Research with live web searches.** Search forums (Reddit, trade-specific communities), review sites (G2, Capterra, ProductReview), industry reports, job ads that reveal process pain, and LinkedIn posts. Collect verbatim quotes and their URLs as you go — every pain point needs at least one citable source. Do not cite vendor blog posts as evidence, and do not substitute your own assumptions for missing evidence.
3. **Draft the artifact** following the output structure below.
4. **Self-check** against the quality checklist and anti-patterns. Fix every failure before saving.
5. **Save and report.** Write the file to `docs/gtm/01-pain-point-research.md`, then tell the user the path, the top pain points found, and that the ICP (`icp`) and customer interview guide (`customer-interview-guide`) skills are now unblocked.

## Frameworks
- Jobs-to-be-done (JTBD): focus on what the customer is trying to accomplish, not what they buy
- Hair-on-fire severity scoring: is this a nice-to-have or a must-fix?
- Customer language extraction: exact words used in complaints, reviews, forums

## Output structure

### 1. Problem landscape overview
2–3 paragraphs summarising the space. What is hard, why it is hard, who it is hardest for.

### 2. Pain points (top 3–5)
For each pain point:
- **Name**: short label
- **Description**: what the problem actually is
- **Severity**: high / medium / low with rationale
- **Frequency**: daily / weekly / occasional
- **Evidence**: 1–3 citable sources (Reddit threads, G2/Capterra reviews, industry reports, job ads that reveal process pain, LinkedIn posts)
- **Current workaround**: what they do today instead of solving it properly

### 3. Underserved gaps
What pain exists that no current product addresses well.

### 4. Customer language glossary
10–20 verbatim phrases extracted from sources. These feed directly into brochureware and sales letter copy.

### 5. Source list
Full list of cited URLs with one-line description of each.

## Quality checklist
- [ ] Every pain point has at least one citable external source
- [ ] Severity ratings are justified, not assumed
- [ ] Customer language is verbatim from sources, not paraphrased
- [ ] Gaps are distinguishable from pain points already addressed by competitors
- [ ] At least one "do nothing" workaround is documented per pain point

## Anti-patterns
- Validating pain with your own assumptions dressed up as research
- Using vendor blog posts as evidence (they describe pain in ways that flatter their own solution)
- Conflating frequency with severity — a daily annoyance is not the same as a monthly crisis
