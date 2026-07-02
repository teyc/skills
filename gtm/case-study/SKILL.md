---
name: case-study
description: Write an SCSR-structured customer case study with a result-first headline and deployment notes for website, outreach, deck, and sales calls. Use only after a pilot customer achieves a measurable, confirmed result — never before.
user-invokable: true
---

# Case Study

## Purpose
A structured proof artifact produced after a pilot or early customer success. Designed to be deployed as sales collateral — on the website, in cold outreach, in the pitch deck, and in sales conversations. A good case study does two things: proves the product works, and gives the next prospect permission to believe they can get the same result.

## When to use this skill
Use after a pilot customer achieves a measurable result. The earlier in the customer relationship the better — capture the "before" while it's still vivid.

## Required inputs
- Customer name and permission level (named / anonymised / logo-only)
- Situation before: what was the problem and how were they solving it?
- What they did: how did they use the product?
- Results: specific, numbered, time-bounded outcomes
- Customer quote (if available — one sentence is enough)
- Time period covered by the results

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (if present) | `docs/gtm/03-icp.md`, `docs/gtm/05-value-proposition.md` |
| Writes | `docs/gtm/15-case-study-<customer-slug>.md` (one file per customer, e.g. `15-case-study-acme-hvac.md`) |

## Workflow

1. **Confirm the preconditions.** Ask the user for the customer's name, the permission level (named / anonymised / logo-only), and the specific, time-bounded results. If results are unconfirmed or projected, do not write a case study — offer a "pilot update" document instead and say why.
2. **Gather the story.** Get the before-state, the trigger event, what they tried previously, implementation experience, and any customer quote from the user. Read the ICP and value proposition if present so the framing speaks to the next prospect, not just this customer.
3. **Draft the case study** following the SCSR output structure below. The headline states the result; the customer's language carries the situation section; the solution section stays honest about friction.
4. **Self-check** against the quality checklist and anti-patterns. Every result must be numbered and time-bounded; the quote must sound like a person. Fix every failure before saving.
5. **Save and report.** Write the file to `docs/gtm/15-case-study-<customer-slug>.md`, then tell the user the path, the headline, what is cleared for public use at the documented permission level, and where the deployment notes suggest using each excerpt (brochureware social proof, sales letter proof block, outreach proof point, pitch deck traction slide).

## Frameworks
- **SCSR (Situation → Complication → Solution → Result)**: the narrative spine. Every case study follows this structure. The result comes last — earning it.
- **Result-first headline**: the headline states the outcome, not the customer's name or the product. The customer's name is a detail; the result is the story.
- **Permission to believe**: the most important job of a case study is to make the next prospect think "that could be me." Write for the reader, not the subject.

## Output structure

### 1. Headline
Result-first. Specific. Includes a number where possible.
> "[Customer] cut invoice reconciliation time from 4 hours to 20 minutes per week"
> "How [HVAC business] recovered $X in unbilled labour using [Product]"

### 2. Summary (2–3 sentences)
Who the customer is, what they struggled with, and what they achieved. Readable in 10 seconds.

### 3. Customer profile
| Attribute | Detail |
|---|---|
| Business type | |
| Size | |
| Geography | |
| How long in business | |
| Tools used alongside this product | |

### 4. Situation (before)
What did life look like before? Be specific about the workflow, the time cost, the error rate, the frustration. Write as a narrative, not a bullet list. Use the customer's language where possible.

### 5. Complication
What made the status quo untenable? The trigger event that led them to look for a solution. What had they tried before and why hadn't it worked?

### 6. Solution
What they did. How they implemented it. How long it took to get up and running. What the learning curve was like. Keep this honest — a smooth story is less credible than a real one.

### 7. Results
The most important section. Format as:
- **Primary result**: the headline metric (time saved, money recovered, error rate, etc.)
- **Secondary results**: 2–3 supporting outcomes
- **Timeframe**: how long to achieve these results from implementation

Results must be specific and time-bounded. "Saved time" is not a result. "Reduced invoice reconciliation from 4 hours to 20 minutes per week" is.

### 8. Customer quote
One to three sentences. Should reference a specific outcome or emotional shift, not generic praise.
> "I used to dread end-of-week reconciliation. Now I do it before lunch on Friday."

### 9. Call to action
What should the reader do next? One specific action.

### 10. Deployment notes
Where this case study will be used and in what format:
- Website (full page? Summary card?)
- Cold email (which excerpt?)
- Pitch deck (which stat?)
- Sales call (talking points)

## Quality checklist
- [ ] Headline states a specific result, not a company name or product feature
- [ ] Results are specific, numbered, and time-bounded
- [ ] Situation section describes life before without editorialising
- [ ] Customer quote sounds like a person, not a PR statement
- [ ] Deployment notes specify which excerpts to use in which contexts
- [ ] Permission level is documented (named / anonymised / logo-only)

## Anti-patterns
- Headline: "[Company Name] Partners With [Product Name] to Improve Operations" (says nothing)
- Results: "significantly improved efficiency" (meaningless without numbers)
- A case study written before results are confirmed (use "pilot update" framing instead)
- Customer quote that sounds like marketing wrote it: "This product has been transformational for our business"
- Forgetting to document permission level and what the customer has approved for public use
