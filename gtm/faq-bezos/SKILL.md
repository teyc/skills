---
name: faq-bezos
description: Write the internal FAQ companion to the working-backwards press release — the hardest customer and internal questions, answered honestly. Use immediately after the press-release skill; the two documents always ship as a pair.
user-invokable: true
---

# FAQ (Bezos Companion Document)

## Purpose
The internal stress-test companion to the press release. Where the press release presents the vision, the FAQ forces honest answers to the hardest questions a customer, investor, skeptical colleague, or journalist would ask. It is not the website FAQ — it is a thinking document that surfaces weak assumptions before they become expensive mistakes.

## When to use this skill
Use immediately after completing the press release. The two documents ship together in the Amazon PR/FAQ format. Return to this document when a new objection surfaces in sales conversations.

## Required inputs
- Press release (completed)
- ICP definition
- Competitive landscape (even rough)
- Known risks or uncertainties (the things you haven't answered yet)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (required) | `docs/gtm/07-press-release.md` |
| Reads (if present) | `docs/gtm/03-icp.md`, `docs/gtm/04-competitive-positioning.md` |
| Writes | `docs/gtm/08-faq.md` |

## Workflow

1. **Gather inputs.** Read the press release. If it does not exist, stop and run (or offer to run) the `press-release` skill first — the FAQ stress-tests a specific vision, not a vague one. Ask the user for known risks and open uncertainties; these seed the internal FAQ.
2. **Generate the hardest questions first.** For each claim in the press release, ask what a skeptical customer, investor, or competitor would attack. Write internal questions you would prefer not to answer — if every answer comes easily, the questions are not hard enough.
3. **Answer honestly.** Short, specific answers. At least one must be "we don't know yet — here's how we'll find out." Do not pitch.
4. **Self-check** against the quality checklist and anti-patterns. Fix every failure before saving.
5. **Save and report.** Write the file to `docs/gtm/08-faq.md`, then tell the user the path, the two or three weakest assumptions the FAQ exposed, and what evidence would resolve them.

## Frameworks
- **Amazon PR/FAQ**: the FAQ portion is explicitly meant to be hard. If every answer is easy, the questions aren't hard enough.
- Distinguish customer FAQs (what an external audience would ask) from internal FAQs (what a skeptical colleague or investor would ask). Both are required.

## Output structure

### Customer FAQs (10–15 questions)
Questions a potential customer would ask before paying. Each answer should be honest, specific, and short. If you can't answer it yet, say so — that is information.

Suggested question categories:
- What exactly is this? (clarity)
- Who is it for? (fit)
- How does it work? (mechanism)
- How long does it take to set up? (friction)
- What does it cost? (commitment)
- What do I need to already have for this to work? (dependencies)
- What happens to my data? (trust)
- What if it doesn't work as described? (risk)
- How is this different from [specific competitor]? (positioning)
- Do I need to change how I work? (change management)

### Internal FAQs (5–10 questions)
Questions a skeptical co-founder, investor, or advisor would ask. These are the questions you'd rather not answer in public but must answer honestly in private.

Suggested question categories:
- Why will this win? What is the actual defensible advantage?
- What assumptions must be true for this to succeed?
- What is the most likely way this fails?
- What don't we know yet, and how will we find out?
- Why us? Why now?
- What does the 18-month path to viability look like?
- What happens if the anchor customer churns?

## Quality checklist
- [ ] At least one answer is "we don't know yet — here's how we'll find out"
- [ ] Internal FAQs include at least one question you'd prefer not to answer
- [ ] Customer FAQ answers are specific, not vague ("pricing depends on usage" is not an answer)
- [ ] Competitive differentiation question is answered honestly, not defensively
- [ ] Document was written by the founder/lead, not delegated to marketing

## Anti-patterns
- Writing only softball questions you know the answer to
- Using the FAQ to pitch rather than to stress-test
- Treating this as the website FAQ (different purpose, different audience)
- Skipping the internal FAQ section
- Answering "what if it fails?" with "it won't"
