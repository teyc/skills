# GTM Skills — Sequencing & Dependency Map

A set of 15 skills for the non-technical deliverables of a new product or idea.
Each skill is a SKILL.md file that Claude uses to produce a specific artifact.

---

## File conventions

Every artifact is written to `docs/gtm/` at the root of the project the skills are run in, using a fixed numbered filename (see the skills index below). Skills read their prerequisites from the same directory by these filenames — this is how dependencies resolve automatically. If a prerequisite file is missing, the skill checks the conversation for the equivalent information, and asks the user only if it is nowhere to be found.

The directory doubles as a progress tracker: `ls docs/gtm/` shows exactly which artifacts exist and which are still to be produced.

---

## Two paths

### Quick path — smoke test in a week
Enough to put something in front of real people and see if they respond.

```
Pain point research
      ↓
     ICP
      ↓
Value proposition
      ↓
 Brochureware
```

That's it. Four skills, four artifacts, one landing page. Everything else can follow if the page converts.

---

### Full path — complete GTM package

```
DISCOVERY
──────────────────────────────────────────────────────────
[1] Pain point research          (no dependencies)
[2] Customer interview guide     (no dependencies — but better after [1])
[3] ICP                          (informed by [1], sharpened by [2])

    ↓ ↓ ↓

STRATEGY
──────────────────────────────────────────────────────────
[4] Competitive positioning      (needs [3]; can run parallel to [5])
[5] Value proposition            (needs [1] + [3])
[6] Pricing strategy             (needs [5] + [4])
[7] Press release                (needs [5]; optionally [4])
[8] FAQ (Bezos companion)        (needs [7] — always follows the press release)

    ↓ ↓ ↓

EXECUTION
──────────────────────────────────────────────────────────
[9]  Brochureware                (needs [5] + [3] + [1] + brand adjacency from [4])
[10] Long form sales letter      (needs [5] + [3] + [9])
[11] Keyword research            (needs [3] + [5] + [4])
[12] GTM plan                    (needs [3] + [5] + [4] + [6] + organic verdict from [11])
[13] Cold outreach sequence      (needs [3] + [5] + [12])

    ↓ ↓ ↓

PITCH & PROOF
──────────────────────────────────────────────────────────
[14] Pitch deck                  (needs [5] + [4] + [6] + [7] + traction data)
[15] Case study                  (needs real pilot results — last artifact, not first)
```

---

## Dependency table

| Skill | Hard dependencies | Soft dependencies (better with) |
|---|---|---|
| Pain point research | — | ICP hypothesis |
| Customer interview guide | — | Pain point research |
| ICP | — | Pain point research |
| Competitive positioning | ICP | — |
| Value proposition | ICP + Pain point research | Competitive positioning |
| Pricing strategy | Value proposition + Competitive positioning | ICP |
| Press release | Value proposition | ICP, Pain point research |
| FAQ (Bezos companion) | Press release | Competitive positioning |
| Brochureware | Value proposition + ICP + Pain point research | Competitive positioning (brand adjacency) |
| Long form sales letter | Value proposition + ICP | Brochureware, Pain point research |
| Keyword research | ICP + Value proposition | Competitive positioning |
| GTM plan | ICP + Value proposition + Competitive positioning + Pricing | Keyword research |
| Cold outreach sequence | ICP + Value proposition + GTM plan | Pain point research |
| Pitch deck | Value proposition + Competitive positioning + Pricing + Press release | All execution artifacts, traction data |
| Case study | Real pilot results + customer permission | ICP, Value proposition |

---

## What can be parallelised

If you have bandwidth to split work:

**Round 1 (parallel)**
- Pain point research
- Competitive positioning (brand aesthetic audit takes time)

**Round 2 (parallel, after Round 1)**
- ICP (uses Round 1 outputs)
- Keyword research (uses competitive positioning)

**Round 3 (sequential)**
- Value proposition (uses ICP + pain point research)

**Round 4 (parallel, after Round 3)**
- Press release → FAQ (sequential pair)
- Brochureware
- Pricing strategy

**Round 5 (parallel, after Round 4)**
- Long form sales letter
- GTM plan
- Cold outreach sequence

**Round 6 (after traction)**
- Pitch deck
- Case study

---

## Notes

**Press release + FAQ always ship as a pair.**
Do not produce one without the other. The press release is the vision; the FAQ is the stress test.

**Competitive positioning feeds brand decisions for every visual artifact.**
Before writing brochureware copy or briefing a designer, read the brand adjacency recommendation from the competitive positioning document. The default "modern SaaS blue" is often wrong for trade and industrial markets.

**Case study is the last artifact, not the first.**
It requires real results. Producing it prematurely (before confirmed outcomes) undermines its credibility. A pilot update or "early results" email is a better interim artifact if you need proof collateral before the pilot is complete.

**Keyword research produces a verdict, not just a list.**
The GTM plan depends on whether organic search is viable early. The keyword research skill explicitly answers this question. Do not default to "we'll do SEO" without running this skill first.

**The customer interview guide is an instrument, not a finding.**
It produces questions, not answers. The answers go back into ICP, pain point research, and value proposition as updates. Plan to iterate these three documents after every 5 interviews.

---

## Skills index

| # | Skill | Directory | Writes |
|---|---|---|---|
| 1 | Pain point research | `pain-point-research/` | `docs/gtm/01-pain-point-research.md` |
| 2 | Customer interview guide | `customer-interview-guide/` | `docs/gtm/02-customer-interview-guide.md` |
| 3 | ICP | `icp/` | `docs/gtm/03-icp.md` |
| 4 | Competitive positioning & battle card | `competitive-positioning/` | `docs/gtm/04-competitive-positioning.md` |
| 5 | Value proposition | `value-proposition/` | `docs/gtm/05-value-proposition.md` |
| 6 | Pricing strategy | `pricing-strategy/` | `docs/gtm/06-pricing-strategy.md` |
| 7 | Press release | `press-release/` | `docs/gtm/07-press-release.md` |
| 8 | FAQ (Bezos companion) | `faq-bezos/` | `docs/gtm/08-faq.md` |
| 9 | Brochureware | `brochureware/` | `docs/gtm/09-brochureware.md` + `docs/gtm/09-brochureware.html` |
| 10 | Long form sales letter | `long-form-sales-letter/` | `docs/gtm/10-sales-letter.md` |
| 11 | Keyword research | `keyword-research/` | `docs/gtm/11-keyword-research.md` |
| 12 | GTM plan | `gtm-plan/` | `docs/gtm/12-gtm-plan.md` |
| 13 | Cold outreach sequence | `cold-outreach-sequence/` | `docs/gtm/13-cold-outreach.md` |
| 14 | Pitch deck | `pitch-deck/` | `docs/gtm/14-pitch-deck.md` |
| 15 | Case study | `case-study/` | `docs/gtm/15-case-study-<customer-slug>.md` |
