---
name: customer-interview-guide
description: Build a Mom Test-style discovery interview guide — questions, note-taking template, and red flags — for 30–45 minute customer calls. Use when preparing to run discovery interviews or training someone else to run them.
user-invokable: true
---

# Customer Interview Guide

## Purpose
A structured discovery instrument for 30–45 minute calls with potential customers. This is not a survey — it generates questions, not answers. The goal is to uncover real behaviour, real frustration, and real buying patterns without leading the witness. The output is ready to use in a call with zero preparation overhead.

## When to use this skill
Use when the user is about to conduct discovery interviews and needs a tested question set, or when they want to train someone else to run interviews on their behalf.

## Required inputs
- ICP definition (or rough target: "HVAC business owner, 5–20 staff")
- Problem hypothesis to explore
- Stage of discovery (early = explore broadly; late = validate specific assumptions)

## Standard files

All GTM artifacts live in `docs/gtm/` at the project root. Create the directory if it does not exist. If the user names a different directory, use it and keep the standard filenames.

| | Files |
|---|---|
| Reads (if present) | `docs/gtm/01-pain-point-research.md`, `docs/gtm/03-icp.md` |
| Writes | `docs/gtm/02-customer-interview-guide.md` |

## Workflow

1. **Gather inputs.** Read the files above if they exist. Get the problem hypothesis and discovery stage (early = explore broadly; late = validate specific assumptions) from the user or the conversation; if the target customer is unstated everywhere, ask.
2. **Draft the questions** using The Mom Test rules strictly: past tense, behaviour-focused, open-ended, one question at a time. Ground the red flags section in this specific segment, not generic signals.
3. **Self-check** against the quality checklist and anti-patterns — read every question and reject any that asks about the future, opinions, or hypotheticals. Fix every failure before saving.
4. **Save and report.** Write the file to `docs/gtm/02-customer-interview-guide.md`, then tell the user the path and remind them that interview answers feed back into the pain point research, ICP, and value proposition documents — plan to update those after every 5 interviews.

## Frameworks
- **The Mom Test** (Rob Fitzpatrick): never ask about the future or opinions; ask about the past and behaviour. "Would you use this?" is invalid. "Walk me through the last time you dealt with that" is valid.
- **JTBD framing**: focus on the job being done, not the product being considered
- **Silence as a tool**: note where to pause and let the interviewee fill the gap

## Output structure

### 1. Interview brief (1 page)
- Purpose of this interview
- What we are trying to learn
- What we are NOT trying to pitch

### 2. Warm-up questions (3)
Build rapport, understand their context. No leading.

### 3. Core problem questions (5–7)
Open-ended, past-tense, behaviour-focused. Each includes a follow-up prompt.

### 4. Workflow and current solution questions (3–4)
How they do it today. What tools. What breaks. What they've tried.

### 5. Buying process questions (3)
Who decides. What triggers a purchase. What blocks one.

### 6. Closing questions (2)
Who else to speak to. Permission to follow up.

### 7. Red flags to listen for
Signals that this person is not the ICP, is being polite rather than honest, or is describing an aspirational behaviour rather than a real one.

### 8. Note-taking template
Pre-formatted for capture during the call: quote box, behaviour observed, surprise/unexpected finding, follow-up needed.

## Quality checklist
- [ ] No question asks "would you" or "do you think you would"
- [ ] All core questions are open-ended (cannot be answered yes/no)
- [ ] At least one question asks them to walk through a specific recent event
- [ ] Buying process questions are included even in early-stage research
- [ ] Red flags section is specific to this segment, not generic

## Anti-patterns
- Asking for opinions about a hypothetical product ("what features would you want?")
- Pitching during the interview
- Asking compound questions ("do you use spreadsheets or software, and if software which one?")
- Treating politeness as validation
