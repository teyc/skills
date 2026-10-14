---
name: story-cards
description: Create clear, evidence-backed development story cards from project conversations and working documents, with assumptions, dependencies, criteria, tests and follow-up analysis. Group cards into a business case and produce a review PDF with embedded JSON when useful.
---

# Story cards

Turn conversation history and project material into a set of linked, reviewable business cases and development cards. Draft from incomplete evidence, but mark assumptions and unresolved points so they cannot be mistaken for decisions.

## Workflow

1. **Read the project rules and map the sources.** Check `AGENTS.md`, project guidance, conversation logs, current business cases, stories, work breakdown structures, decision records and assumption registers before drafting. Follow source-specific access limits. Preserve the project's existing terms, identifiers, status labels and record locations. Do not read secrets or unrelated personal details.
2. **Build an evidence ledger.** For each candidate need, record the source file and location, date, speaker or author when known, and whether it is a direct statement, a recorded decision, an external requirement, or an inference. Keep direct quotes short and exact. Treat a later explicit decision as superseding an earlier draft only when the record says so; retain the history where it matters.
3. **Group related needs.** Create a business case for a coherent outcome or decision. Link task cards to that case. Split work such as third-party integration, security review or penetration testing into its own card when it has a distinct outcome, owner, dependency or acceptance evidence. Do not inflate an idea or mention into approved scope.
4. **Draft cards and analysis.** Use the story form, diagrams, dependencies, criteria and test cases below where they add value. Mark every inference as an assumption, give it a status and source, and state what would resolve it. Surface unanswered matters as questions or analysis tasks. Include helpful people only when project sources show their relevance; explain the connection and the proposed question, and do not imply they agreed to help.
5. **Review the set.** Check for duplicates, missing links, contradictory sources, scope creep, unowned dependencies, unsupported claims, and hidden decisions. A card is ready only when its user need and observable acceptance criteria are clear; otherwise label it as needing discussion or analysis and name the blocker.
6. **Produce the review PDF and structured data.** Write a validated JSON source file using [the data schema](references/data-schema.json). Render it with `python3 <skill-dir>/scripts/render_report.py work-items.json -o business-case-and-work-items.pdf`. The renderer uses headless Chrome or Chromium and `pypdf`. Embed the same JSON as a PDF file attachment named `work-items.json`; also keep the JSON beside the PDF. Verify that the attachment can be extracted and parses as JSON. If PDF attachment support is unavailable, report the limitation and keep the JSON sidecar; do not claim it is embedded.

## Card content

Each card should have:

- a concise title and a story: “As a …, I want …, so that …”
- context, intended outcome, and scope boundaries
- a sequence diagram when behaviour crosses actors or systems
- an entity diagram when data relationships affect the work
- dependencies, including third-party services, access, procurement, security reviews and decisions
- acceptance criteria written as observable outcomes
- test cases linked to the criteria, including errors and relevant edge cases
- sources, assumptions, open questions, confidence and readiness
- relevant people mentioned in the project record, with evidence for their relevance

Do not force diagrams onto a simple task. Store diagram source in JSON. Prefer a simple, labelled SVG for diagrams included in the PDF; the renderer displays SVG diagrams and keeps their source in the attachment. Mermaid or PlantUML can be included when useful, but label it as source rather than presenting code as a rendered diagram.

## Business cases

State the decision or outcome first. Include the problem and evidence, users affected, options considered where the sources support them, recommended direction as a recommendation (not a decision), benefits, costs or cost areas, risks, delivery and operational implications, dependencies, and measures of success. For a proof of concept, separate what the PoC demonstrates from what production would require. Call out specialist work such as penetration testing, privacy or security assessment, integration discovery, data migration, accessibility review or operational readiness when evidence makes it relevant. Mark an inferred need as an assumption and say what analysis will confirm it.

## Evidence and uncertainty

- Keep fact, decision, recommendation, assumption and question distinct in both the PDF and JSON.
- Attach a source reference to each material claim. Prefer a project-relative path plus heading, row, page or timestamp so another person can find it.
- Preserve the project's assumption-verification process. If none exists, use clear statuses such as `pending`, `verified`, `rejected` or `superseded`, with verifier and date when recorded.
- Never resolve uncertainty by silently choosing a plausible answer. Draft a useful option, label the assumption, describe its consequence if wrong, and add a concrete question or analysis step.
- Do not invent stakeholders, approvals, costs, legal conclusions, test evidence, system capabilities or commitments. A person's name is not evidence that they own or approved the work.
- Apply the `govuk-style` skill to prose when available. Use plain English, active voice, sentence case and front-loaded conclusions.

## Output

Create a review folder with `business-case-and-work-items.pdf` and `work-items.json`. The PDF should put the business case summary and decisions needed first, then assumptions and questions, dependencies and relevant people, followed by linked task cards. Include source references and visible status labels throughout. Keep sensitive conversation details out unless needed to understand or act on the work.

Read [the schema](references/data-schema.json) before creating the JSON. The schema is the canonical extraction contract; the PDF is its human-readable view. Keep IDs stable across revisions and preserve source links when updating existing items.
