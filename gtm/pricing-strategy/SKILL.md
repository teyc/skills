---
name: pricing-strategy
description: Design a pricing model, tier structure, anchor tier, and upgrade triggers, plus pricing page layout guidance. Use after the value proposition and competitive positioning exist; revisit after the first five paying customers provide real data.
user-invokable: true
---

# Pricing Strategy

## Purpose
An opinionated pricing structure covering model selection, tier logic, anchoring, and upgrade triggers. Pricing is positioning — the number and structure signal who the product is for and what category it lives in. This document feeds the pricing page, the brochureware, and the GTM plan.

## When to use this skill
Use after value proposition and ICP are defined. Revisit after first 5 paying customers provide real data.

## Required inputs
- ICP definition (company size, revenue range, what they spend on adjacent tools)
- Value proposition (what outcome is being delivered)
- Competitive pricing (what alternatives cost — from competitive positioning doc)
- Business model preference if known (subscription, per-seat, per-job, usage-based)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/05-value-proposition.md`, `docs/gtm/04-competitive-positioning.md` |
| Reads (if present) | `docs/gtm/03-icp.md` |
| Writes | `docs/gtm/06-pricing-strategy.md` |

## Workflow

1. **Gather inputs.** Read the required files. If either is missing, check the conversation for equivalent information; if it is not there either, ask the user to run the prerequisite skill or supply the facts directly. Ask the user for a business model preference only if the choice is genuinely open.
2. **Benchmark competitor pricing.** Use the pricing captured in the competitive positioning document; where it is absent, run web searches for public pricing pages. If a competitor hides pricing, record that fact — it is itself a signal.
3. **Draft the strategy** following the output structure below. Design the middle (anchor) tier first, then build the others around it. Justify the model choice against ICP buying behaviour, not product type.
4. **Self-check** against the quality checklist and anti-patterns. Every upgrade trigger must be a specific event or limit. Fix every failure before saving.
5. **Save and report.** Write the file to `docs/gtm/06-pricing-strategy.md`, then tell the user the path, the recommended model and anchor tier price, the biggest pricing risk, and that the GTM plan (`gtm-plan`) is now unblocked.

## Frameworks
- **Value-based pricing over cost-plus**: price to the value delivered to the customer, not to your cost to deliver it
- **Anchoring theory**: the tier you want them to choose should sit next to a more expensive option that makes it look reasonable
- **Jobs-to-be-done segmentation**: different tiers should serve different jobs, not just different company sizes
- **The middle tier is the product**: design from the middle outward

## Output structure

### 1. Pricing model recommendation
Evaluate and select one primary model:

| Model | Best for | Risk |
|---|---|---|
| Flat monthly subscription | Simple offering, easy to sell | Leaves value on the table at high usage |
| Per seat / per user | Team products | Punishes adoption |
| Per job / per transaction | Usage-tied value | Complex billing, unpredictable revenue |
| Usage-based (API-style) | Infrastructure / AI products | Hard to budget for customers |
| Freemium | Consumer or developer tools | Conversion rates are low; support cost is high |
| Outcome-based | High-trust, high-value engagements | Hard to measure, hard to scale |

**Recommendation and rationale.**

### 2. Tier structure
Three tiers is the convention for a reason (anchoring + segmentation). Name tiers by customer type, not by size adjective.

For each tier:
- **Name**: (not "Basic / Pro / Enterprise" — name them for the job they do)
- **Target customer**: who is this tier for?
- **Price point**: monthly (and annual equivalent)
- **What's included**: specific capabilities, limits, or quantities
- **What's excluded**: what is deliberately withheld to drive upgrade

### 3. Anchor tier
Identify which tier is the target (the one you want most customers on). Design the others to make it look like the right choice.

### 4. Upgrade triggers
What specific events or limits cause a customer to need to upgrade? Be explicit — these are design decisions, not accidental.

### 5. Annual vs monthly discount
Recommended discount for annual pre-pay and rationale (typically 15–20% = 2 months free).

### 6. What to put behind a sales conversation
What tier or capability requires a direct sales conversation rather than self-serve checkout? (Usually "Enterprise" or custom integrations.)

### 7. Pricing page layout recommendation
- Which tier to highlight (middle)
- Whether to show annual/monthly toggle
- What social proof to put adjacent to pricing
- Whether to include a comparison table
- Call to action wording per tier

### 8. Pricing risks
What assumptions are baked into this structure that could be wrong? What would trigger a reprice?

## Quality checklist
- [ ] Pricing model is justified against ICP buying behaviour, not just product type
- [ ] Tier names describe customer types, not abstract size labels
- [ ] Upgrade triggers are specific events, not vague "as you grow"
- [ ] Anchor tier is identified and the design intentionally draws attention to it
- [ ] Pricing is benchmarked against competitive alternatives
- [ ] Risks section exists

## Anti-patterns
- Naming tiers Basic / Pro / Enterprise without question
- Setting price based on what feels comfortable to the founder, not what the customer values
- Per-seat pricing for products where the buying unit is the business, not the team
- No free tier and no trial when the product requires behaviour change to deliver value
- Pricing page that lists features without connecting them to outcomes
