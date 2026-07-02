---
name: cold-outreach-sequence
description: Write a production-ready 3-touch cold email sequence with subject line variants, personalisation tokens, and success benchmarks. Use when the GTM plan calls for direct outreach to ICP prospects; revise after 20–30 sends based on reply data.
user-invokable: true
---

# Cold Outreach Sequence

## Purpose
A 3-touch email sequence for cold B2B outreach to ICP prospects who have not previously engaged. The output is production-ready: subject lines, body copy, personalisation tokens, and success benchmarks. Shorter is better. Specificity beats generic personalisation. Subject line quality is 80% of deliverability and open rate.

## When to use this skill
Use when Phase 1 GTM calls for direct outreach. Pair with the ICP and cold outreach list (sources from the GTM plan). Revise after 20–30 sends based on reply rate data.

## Required inputs
- ICP definition (specific role, company type)
- Value proposition one-liner
- Primary pain point to lead with
- Any proof point, case study, or specific result to reference
- CTA: what specific action is being requested? (15-min call, demo, pilot conversation)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/03-icp.md`, `docs/gtm/05-value-proposition.md`, `docs/gtm/12-gtm-plan.md` |
| Reads (if present) | `docs/gtm/01-pain-point-research.md`, `docs/gtm/15-case-study-*.md` (proof points) |
| Writes | `docs/gtm/13-cold-outreach.md` |

## Workflow

1. **Gather inputs.** Read the required files. If any are missing, check the conversation for equivalent information; if it is not there either, ask the user to run the prerequisite skills or supply the facts directly. Confirm the single CTA (15-min call, demo, pilot conversation) and the strongest available proof point — if no real proof exists yet, say so and write around it rather than inventing one.
2. **Draft all three emails** following the output structure below, each with a genuinely different angle. Write them ready to send — real sentences, with only the personalisation tokens left as placeholders.
3. **Self-check** against the quality checklist and anti-patterns. Read each email aloud in your head as the recipient: would you reply? Check lengths against the word targets. Fix every failure before saving.
4. **Save and report.** Write the file to `docs/gtm/13-cold-outreach.md`, then tell the user the path, the Email 1 subject line options, and the benchmark numbers that should trigger iteration.

## Frameworks
- **Specificity beats volume**: a precise email to 20 right people outperforms a blasted email to 200 wrong ones
- **Past-tense relevance opener**: "I noticed you [specific thing]" not "I'm reaching out because I think you might be interested in..."
- **Single CTA per email**: one ask, easy to say yes to
- **3 touches, 3 different angles**: do not send the same email twice. Each touch uses a different hook, proof type, or angle.

## Output structure

### Email 1 — The hook (Day 0)

**Purpose**: earn a reply by being relevant and specific, not by pitching.

**Subject line options** (provide 3 variants):
- Option A: specificity/curiosity angle
- Option B: pain-point angle
- Option C: referral/name-drop angle (if applicable)

**Body copy:**
- Opening line: past-tense relevance or specific observation (1 sentence, no preamble)
- The connection: what you do and who it's for (1–2 sentences — brief)
- The relevant outcome: one specific result, proof point, or case study excerpt
- The ask: one low-friction CTA ("Worth a 15-min call to see if it's relevant?")
- Sign-off

**Personalisation tokens:** [FIRST_NAME], [COMPANY], [SPECIFIC_OBSERVATION]

**Target length:** 80–120 words.

---

### Email 2 — Different angle (Day 4–5)

**Purpose**: re-engage with a different hook or social proof. Not a "just following up."

**Subject line options** (3 variants — different from Email 1)

**Body copy:**
- Do not mention that this is a follow-up
- New hook: different proof point, different pain, or question-led opener
- Reference the previous email only if doing so adds value (usually it doesn't)
- Same CTA or slightly adjusted lower-friction version

**Target length:** 60–90 words.

---

### Email 3 — The soft close (Day 9–12)

**Purpose**: final touch. Acknowledge this is the last one. Make it easy to say "not now" so you can accurately qualify the list.

**Subject line options** (3 variants)

**Body copy:**
- Acknowledge this is the last message in this sequence
- Shortest email of the three
- Offer a clear out: "If timing's off, happy to revisit in [timeframe]" or "If not relevant, no worries — just let me know"
- Restate the CTA one final time

**Target length:** 40–60 words.

---

### Personalisation guide
What tokens to include and where to find the data:
| Token | Description | Source |
|---|---|---|
| [FIRST_NAME] | Recipient first name | LinkedIn / list |
| [COMPANY] | Company name | LinkedIn / list |
| [SPECIFIC_OBSERVATION] | Something specific about them | LinkedIn profile, website, news |
| [RESULT] | Proof point or outcome to cite | Case study / pilot data |

### What NOT to include
- "I hope this email finds you well" (opens 0 credibility)
- "I wanted to reach out" (filler)
- More than one CTA
- Full product description in Email 1
- More than 3 emails in the sequence without a new trigger event

### Success benchmarks
Calibrated for cold B2B email:
- Open rate: 30–50% is good (subject line working)
- Reply rate: 3–8% is good (positioning working)
- Positive reply rate: 1–3% of total sends
- If open rate is low: fix subject lines
- If open rate is high but reply rate is low: fix body copy relevance

## Quality checklist
- [ ] Email 1 opener names something specific about the recipient or their company
- [ ] Each email uses a different angle, hook, or proof type
- [ ] Every email has a single CTA
- [ ] Email 3 acknowledges it's the last and provides a graceful out
- [ ] All three subject line options are distinct from each other
- [ ] Benchmarks are included so the sender knows when to iterate

## Anti-patterns
- "Just following up on my previous email" as the Email 2 opener
- Pitching the full product in Email 1
- Sending a 4th or 5th email without a new trigger or reason
- Subject lines with more than 6 words
- Personalisation that is so generic it reads as fake ("I see you work in HVAC!")
