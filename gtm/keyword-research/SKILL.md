---
name: keyword-research
description: Build an intent-clustered keyword map with priority targets, competitor gaps, recommended page structure, and an honest verdict on whether organic search is a viable early channel. Use when planning content, optimising a landing page, or deciding whether SEO belongs in the GTM plan.
user-invokable: true
---

# Keyword Research

## Purpose
A search intent-clustered keyword map that informs content strategy, brochureware copy, and GTM channel decisions. This is not a raw keyword dump — it is an interpreted map that tells you what content to create, in what order, and why. The output connects keyword data to buyer journey stage.

## When to use this skill
Use when planning content, optimising a landing page, or deciding whether organic search is a viable GTM channel for this product. Run web searches to find real data — do not rely on estimated volumes from memory.

## Required inputs
- ICP definition (to understand search behaviour and language)
- Value proposition and product category
- Competitive positioning (to identify terms competitors rank for)
- Customer language glossary from pain point research (real vocabulary = better seed terms)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/03-icp.md`, `docs/gtm/05-value-proposition.md` |
| Reads (if present) | `docs/gtm/04-competitive-positioning.md`, `docs/gtm/01-pain-point-research.md` (customer language glossary for seed terms) |
| Writes | `docs/gtm/11-keyword-research.md` |

## Workflow

1. **Gather inputs.** Read the required files. If either is missing, check the conversation for equivalent information; if it is not there either, ask the user to run the prerequisite skill or supply the facts directly. Pull seed terms from the customer language glossary, not just the product category.
2. **Check real SERPs with web searches.** For each candidate term, search it and note who actually ranks — domain strength, content type, and whether results match the intent you assumed. Check what terms competitor sites target. Never invent volume numbers: use the volume and difficulty tiers, base them on observed evidence, and label anything estimated as an estimate.
3. **Draft the map** following the output structure below, ending with the organic search verdict — a clear yes/no/not-yet with the trigger conditions that would change it.
4. **Self-check** against the quality checklist and anti-patterns. The verdict must be honest; "we'll do SEO" is not a default. Fix every failure before saving.
5. **Save and report.** Write the file to `docs/gtm/11-keyword-research.md`, then tell the user the path, the verdict, the top 3 priority targets, and that the GTM plan (`gtm-plan`) consumes the verdict directly.

## Frameworks
- **Search intent taxonomy**: every keyword has an intent — informational, navigational, commercial investigation, or transactional. Match content type to intent.
- **Keyword difficulty vs. volume tradeoff**: high-volume terms are usually high-difficulty. For early-stage products, low-difficulty + commercial/transactional intent is the sweet spot.
- **Cluster approach**: group related keywords into topic clusters. One piece of content (or one landing page) should own a cluster, not scatter across singles.

## Output structure

### 1. Seed terms
5–10 core terms that describe the problem space, the product category, and the ICP's job to be done. These are the starting points for expansion.

### 2. Intent classification and cluster map
Group keywords by intent and cluster:

| Cluster name | Intent | Example keywords | Volume tier | Difficulty tier | Content type implied |
|---|---|---|---|---|---|
| | Informational | | | | Blog post / guide |
| | Commercial | | | | Comparison page / landing page |
| | Transactional | | | | Pricing page / sign-up page |
| | Navigational | | | | Brand page |

Volume tier: High (10k+/mo), Medium (1k–10k), Low (<1k), Niche (<100)
Difficulty tier: Low / Medium / High (based on domain authority of current ranking pages)

### 3. High-priority targets
Quick wins: low-to-medium difficulty, commercial or transactional intent, specific to ICP pain. These are the first terms to optimise for.

Table: keyword | intent | volume tier | difficulty tier | why this one

### 4. Long-tail opportunities
Pain-point-language searches, question-format queries, "how do I..." and "best way to..." searches. These are lower volume but convert better and are easier to rank for.

### 5. Competitor keyword gaps
Terms that direct competitors rank for but you don't yet. Source: check competitor sites using search or available SEO tools.

### 6. Terms to avoid
Keywords that are:
- Too broad (no realistic ranking path for a new domain)
- Wrong intent (informational when you need transactional)
- Wrong audience (attract the wrong ICP)
- Overcrowded with established players at DA 70+

### 7. Recommended page structure
Based on the cluster map: what pages should exist on the site, and which cluster does each own?

| Page | Primary cluster | Primary keyword | Secondary keywords |
|---|---|---|---|

### 8. Organic search verdict
Is organic search a viable early GTM channel for this product? Answer honestly based on competition level, search volume, and how long ranking takes. If not viable early, note what triggers should prompt investment.

## Quality checklist
- [ ] Seed terms include ICP language from pain point research, not just product category terms
- [ ] Every cluster has a clear intent label
- [ ] High-priority targets have a rationale, not just a difficulty score
- [ ] Organic search verdict is honest — not every product should invest in SEO early
- [ ] Terms to avoid section exists and is specific

## Anti-patterns
- Starting with brand terms (you'll rank for those anyway)
- Targeting only high-volume terms with no realistic ranking path
- Confusing informational intent with commercial intent (blog traffic ≠ buyers)
- Skipping the organic search verdict — whether SEO is worth doing now is a strategic decision
