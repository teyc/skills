---
name: gtm-plan
description: Create a phased go-to-market plan — channel assessment, three phases with goals and metrics, a single North Star metric, and explicit exclusions. Use after the ICP, value proposition, competitive positioning, and pricing are defined; revisit after each phase produces data.
user-invokable: true
---

# Go-To-Market (GTM) Plan

## Purpose
A phased, sequenced plan for getting the product in front of the right people and converting them to paying customers. The GTM plan is a hypothesis — it states what channels to try, in what order, what success looks like at each stage, and what decisions get made based on the results. It does not try to do everything at once.

## When to use this skill
Use after ICP, value proposition, competitive positioning, and pricing are defined. The GTM plan is downstream of all of these. Revisit after each phase produces data.

## Required inputs
- ICP definition
- Pricing structure
- Available channels and resources (team size, budget, existing network, platforms)
- Any existing traction (pilot customers, warm leads, partnerships)
- Organic search verdict from keyword research (whether SEO is viable early)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/03-icp.md`, `docs/gtm/05-value-proposition.md`, `docs/gtm/04-competitive-positioning.md`, `docs/gtm/06-pricing-strategy.md` |
| Reads (if present) | `docs/gtm/11-keyword-research.md` (organic search verdict) |
| Writes | `docs/gtm/12-gtm-plan.md` |

## Workflow

1. **Gather inputs.** Read the required files. If any are missing, check the conversation for equivalent information; if it is not there either, ask the user to run the prerequisite skills or supply the facts directly. Ask the user about resources — team size, weekly hours available, budget, existing network, and any current traction — because the plan must fit what they can actually execute.
2. **Assess channels honestly** using the channel table. Where the keyword research verdict exists, use it to score content/SEO; where it does not, mark that row "unassessed — run keyword-research" rather than guessing. Select at most 2 channels for Phase 1.
3. **Draft the plan** following the output structure below, with specific numbers in Phase 1 (outreach attempts, conversion goal) and a single North Star metric.
4. **Self-check** against the quality checklist and anti-patterns — no paid acquisition in Phase 1, no content/SEO as a Phase 1 channel, and the "not doing" section has reasons. Fix every failure before saving.
5. **Save and report.** Write the file to `docs/gtm/12-gtm-plan.md`, then tell the user the path, the GTM thesis, the North Star metric, and that the cold outreach sequence (`cold-outreach-sequence`) is now unblocked if direct outreach is a Phase 1 channel.

## Frameworks
- **Sequenced channel testing**: find one channel that works before adding a second. Spreading thin kills early-stage GTMs.
- **Do things that don't scale first**: the first customers should be won through direct effort (calls, personal outreach, community presence) — not ads. Ads come after you can demonstrate conversion.
- **North Star metric**: one number that tells you if the GTM is working. Not five numbers.

## Output structure

### 1. GTM thesis
One paragraph: who are you reaching, through what primary channel, with what message, expecting what conversion event? This is the hypothesis the plan tests.

### 2. Channel assessment
For each candidate channel, evaluate:

| Channel | Fit with ICP | Time to first result | Cost | Scalability | Priority |
|---|---|---|---|---|---|
| Direct outreach (personal) | | | | | |
| LinkedIn outreach | | | | | |
| Trade communities / forums | | | | | |
| Content / SEO | | | | | |
| Paid ads (Google/Meta) | | | | | |
| Partnerships / referral | | | | | |
| Cold email sequence | | | | | |
| Events / trade shows | | | | | |
| PR / media | | | | | |

**Channels selected for Phase 1** (maximum 2): with rationale.

### 3. Phase 1: Launch (0–30 days)
Goal: First paying customer or first qualified pilot agreement.

- Channels in use
- Specific tactics (e.g. "Direct outreach to 20 HVAC business owners in SEQ via LinkedIn, using the cold outreach sequence")
- Target number of outreach attempts
- Conversion goal (what does success look like?)
- What to learn (what question does this phase answer?)

### 4. Phase 2: Validation (30–90 days)
Goal: Confirm repeatable sales motion.

- What worked in Phase 1 and why
- Channels to double down on
- Channels to drop
- New channel to test (maximum 1)
- Success metric: what does "it's working" look like numerically?

### 5. Phase 3: Scale (90+ days)
Goal: Systematise what works.

- What to operationalise (templated outreach, content calendar, referral program)
- When to add paid acquisition (triggered by what conversion rate?)
- Team or resource additions required

### 6. North Star metric
The single number that tells you the GTM is working. Examples: number of paying customers, MRR, qualified conversations booked per week.

### 7. Key metrics dashboard
5–7 metrics to track (not more):

| Metric | Definition | Target (Phase 1) | Target (Phase 2) |
|---|---|---|---|

### 8. What we are NOT doing and why
Explicit list of channels or tactics being deliberately excluded from this plan, with rationale. This is as important as what's included.

### 9. Resource requirements
Time commitment per week, tools required, budget required per phase.

## Quality checklist
- [ ] GTM thesis is a testable hypothesis, not a vision statement
- [ ] Phase 1 targets a specific number of outreach attempts
- [ ] North Star metric is a single number, not a list
- [ ] "What we're not doing" section exists and has reasons, not just a list
- [ ] Paid acquisition is not in Phase 1 (unless very unusual circumstances)
- [ ] Resource requirements are honest about time cost

## Anti-patterns
- Launching 5 channels simultaneously
- Treating content/SEO as a Phase 1 channel (it takes 6+ months to produce results)
- Defining success as "awareness" rather than a commercial conversion event
- Planning without allocating specific time per week to execute
- A GTM plan that doesn't include what gets cut if Phase 1 underperforms
