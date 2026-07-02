---
name: icp
description: Define a precise Ideal Customer Profile — firmographics, trigger events, buying process, and exclusion criteria — used to qualify leads and focus copy and channels. Use before writing any customer-facing copy or planning channels, and again after each round of customer interviews.
user-invokable: true
---

# Ideal Customer Profile (ICP)

## Purpose
A precise, targeting instrument that defines exactly who the product is built for — not a persona mood board, but a structured profile used to qualify leads, focus copy, and direct channel spend. Everything downstream (brochureware, GTM, outreach) derives from this document.

## When to use this skill
Use before writing any copy, planning any channel, or building any outreach sequence. Update it after each round of customer interviews.

## Required inputs
- Product or solution description (even rough)
- Any existing customers or pilot users (name them — real examples sharpen the profile)
- Pain point research output (if available)
- Geography and market context

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (if present) | `docs/gtm/01-pain-point-research.md` |
| Writes | `docs/gtm/03-icp.md` |

## Workflow

1. **Gather inputs.** Read `docs/gtm/01-pain-point-research.md` if it exists. Get the product description, geography, and any real customers or pilot users from the user or the conversation. Ask for at least one real customer or pilot example — if none exists, proceed but label the profile a hypothesis to be tested against interviews.
2. **Draft the profile** following the output structure below. Anchor every section in a real example where one exists. Fill the exclusion criteria with the near-misses — segments that look right but aren't.
3. **Self-check** against the quality checklist and anti-patterns. Apply the LinkedIn test: could you find 20 matching companies in 30 minutes with this profile? If not, tighten it. Fix every failure before saving.
4. **Save and report.** Write the file to `docs/gtm/03-icp.md`, then tell the user the path, the one-line profile, and that competitive positioning (`competitive-positioning`) and value proposition (`value-proposition`) are now unblocked.

## Frameworks
- Firmographic + psychographic + trigger event model
- Exclusion criteria are as important as inclusion criteria (defining who is NOT the ICP prevents wasted effort)
- Buying-process mapping: champion, decision-maker, blocker, budget holder — these are often different people

## Output structure

### 1. Firmographic profile
| Attribute | Detail |
|---|---|
| Industry | |
| Sub-sector | |
| Company size (employees) | |
| Company size (revenue) | |
| Geography | |
| Business model | |
| Tech maturity | |

### 2. Role profile
- Job title(s) that match
- Seniority level
- What a typical day looks like
- What they are measured on (KPIs)
- What makes them look good to their boss or customers

### 3. Trigger events
What happens in their world that makes them ready to buy NOW — not eventually. Examples: won a big contract, hired a new person, lost money on a job, got audited, competitor just upgraded, regulation changed.

### 4. Pain intensity
Rate 1–5 on:
- Frequency (how often does this pain occur?)
- Severity (how bad is it when it does?)
- Current fix quality (how well does their workaround actually work?)

### 5. Buying process
- Who champions the purchase internally
- Who signs off
- Who can block it
- Typical sales cycle length
- Budget: discretionary or requires approval?

### 6. Where they spend attention
- Communities, forums, trade associations
- Publications or newsletters they read
- Events they attend
- Social platforms they use professionally

### 7. Exclusion criteria
Explicit list of who is NOT the ICP despite superficial similarity.

## Quality checklist
- [ ] Profile is specific enough that you could find 20 matching companies on LinkedIn in 30 minutes
- [ ] Trigger events are specific events, not general dispositions ("wants to grow")
- [ ] Buying process includes a blocker — someone will try to stop this purchase
- [ ] Exclusion criteria are included
- [ ] Based on at least one real customer or pilot user, not pure assumption

## Anti-patterns
- Writing a persona that describes everyone ("small business owner who is busy")
- Skipping the buying process section because "they just buy it themselves"
- Confusing demographics with psychographics
- Making the ICP aspirational rather than actual
