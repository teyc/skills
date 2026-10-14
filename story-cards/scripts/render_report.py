#!/usr/bin/env python3
"""Render a story cards JSON bundle as an A4 PDF with attached JSON."""
from __future__ import annotations

import argparse
import base64
import html
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent


def esc(value) -> str:
    if value is None:
        return "Not recorded"
    return html.escape(str(value))


def list_items(items, fn=lambda x: x) -> str:
    if not items:
        return '<p class="small">None recorded.</p>'
    return '<ul>' + ''.join(f'<li>{fn(item)}</li>' for item in items) + '</ul>'


def refs(ids, sources) -> str:
    by_id = {s["id"]: s for s in sources}
    rows = []
    for sid in ids or []:
        source = by_id.get(sid)
        if source:
            rows.append(f'<li><b>{esc(sid)}</b> · {esc(source["reference"])} — {esc(source["summary"])}</li>')
        else:
            rows.append(f'<li><b>{esc(sid)}</b> · source record missing</li>')
    return '<ul>' + ''.join(rows) + '</ul>' if rows else '<p class="small">No source linked.</p>'


def statement_list(items) -> str:
    return list_items(items, lambda item: esc(item["text"]) + ' <span class="status">' + esc(item["status"]) + '</span>')


def render(data: dict) -> str:
    case = data["business_case"]
    project = data["project"]
    assumptions = data["assumptions"]
    questions = data["questions"]
    dependencies = data["dependencies"]
    people = data["people"]
    sources = data["sources"]
    tasks = data["tasks"]
    css = (SKILL / "assets" / "report.css").read_text(encoding="utf-8")
    sections = [
        f'<section class="cover"><div><p class="kicker">Business case and delivery plan</p><h1>{esc(case["title"])}</h1><p class="subtitle">{esc(case["summary"])}</p><div class="rule"></div><p>{esc(project["name"])}</p></div><div class="meta"><div><b>Review status</b>{esc(project["status"].replace("_", " ").title())}</div><div><b>Reference</b>{esc(project.get("reference"))}</div><div><b>Revision</b>{esc(project.get("revision"))}</div><div><b>Prepared</b>{esc(project["generated_at"])}</div></div></section>',
        f'<section class="section"><h2>Decision summary</h2><p class="lede">{esc(case["outcome"])}</p><div class="callout"><b>Problem</b><p>{esc(case["problem"])}</p></div><h3>Recommendation</h3><p>{esc(case.get("recommendation"))}</p><h3>Proof of concept and production</h3><p>{esc(case.get("poc_production_boundary"))}</p><h3>Decision needed</h3>{list_items(case["decision_needed"], lambda x: f'<b>{esc(x["question"])}</b> {esc(x["why_it_matters"])} <span class="small">Next: {esc(x.get("next_step"))}</span>')}</section>',
        '<section class="section"><h2>Options, value and risk</h2><div class="grid">'
        + ''.join('<article class="card"><h3>' + title + '</h3>' + statement_list(case[key]) + '</article>' for title,key in [("Users affected","users_affected"),("Options","options"),("Benefits","benefits"),("Cost areas","costs"),("Risks","risks"),("Operational implications","operational_implications"),("Measures of success","success_measures")]) + '</div></section>',
        '<section class="section"><h2>Assumptions and questions</h2><h3>Assumptions</h3><table><thead><tr><th>ID and assumption</th><th>Status</th><th>Risk if wrong</th><th>How to resolve</th></tr></thead><tbody>' + ''.join(f'<tr><td><b>{esc(a["id"])}</b> {esc(a["text"])}<br><span class="small">Basis: {esc(", ".join(a["basis"]))}</span></td><td>{esc(a["status"])}</td><td>{esc(a.get("consequence_if_wrong"))}</td><td>{esc(a.get("resolution"))}</td></tr>' for a in assumptions) + '</tbody></table><h3>Questions needing follow-up</h3>' + list_items(questions, lambda q: f'<b>{esc(q["id"])}</b> {esc(q["question"])} <span class="status">{esc(q["status"])}</span><br>{esc(q["why_it_matters"])} <span class="small">Next: {esc(q.get("next_step"))}</span>') + '</section>',
        '<section class="section"><h2>Dependencies and people</h2><table><thead><tr><th>Dependency</th><th>Type and status</th><th>Owner</th><th>Linked work</th></tr></thead><tbody>' + ''.join(f'<tr><td><b>{esc(d["id"])} · {esc(d["name"])}</b><br>{esc(d["description"])}</td><td>{esc(d["kind"].replace("_", " "))}<br>{esc(d["status"])}</td><td>{esc(d.get("owner"))}</td><td>{esc(", ".join(d["linked_ids"]))}</td></tr>' for d in dependencies) + '</tbody></table><h3>People with relevant context</h3>' + list_items(people, lambda p: f'<b>{esc(p["name"])}</b> ({esc(p.get("role"))}): {esc(p["relevance"])} <span class="small">Evidence: {esc(", ".join(p["evidence"]))}. Possible question: {esc(p.get("suggested_question"))}. Contact: {esc(p["contact_status"])}</span>') + '</section>',
    ]
    for task in tasks:
        criteria = ''.join(f'<tr><td>{esc(c["id"])}</td><td>{esc(c["given"])}</td><td>{esc(c["when"])}</td><td>{esc(c["then"])}</td></tr>' for c in task["acceptance_criteria"])
        tests = ''.join(f'<tr><td>{esc(t["id"])}</td><td>{esc(t.get("type", "acceptance"))}</td><td>{esc(t["scenario"])}</td><td>{esc(t["expected_result"])}</td></tr>' for t in task["test_cases"])
        diagram_blocks = []
        for diagram in task["diagrams"]:
            heading = f'<h3>{esc(diagram["kind"].title())} diagram</h3>'
            caption = f'<p class="small">{esc(diagram.get("caption"))}</p>' if diagram.get("caption") else ""
            if diagram["format"] == "svg":
                image_data = base64.b64encode(diagram["source"].encode("utf-8")).decode("ascii")
                diagram_blocks.append(heading + caption + f'<img alt="{esc(diagram.get("caption") or diagram["kind"] + " diagram")}" style="max-width:100%;height:auto" src="data:image/svg+xml;base64,{image_data}">')
            else:
                diagram_blocks.append(heading + caption + f'<p class="small">Diagram source ({esc(diagram["format"])}):</p><pre class="diagram">{esc(diagram["source"])}</pre>')
        diagrams = ''.join(diagram_blocks)
        sections.append(f'<section class="task"><div class="task-head"><div><span class="task-id">{esc(task["id"])}</span><h2>{esc(task["title"])}</h2></div><span class="status">{esc(task["readiness"].replace("_", " "))}</span></div><p class="small">Evidence confidence: {esc(task["confidence"])}</p><p class="story">{esc(task["story"])}</p><h3>Context and scope</h3><p>{esc(task["context"])}</p>{list_items(task["scope"])}<h3>Dependencies</h3>{list_items(task["dependencies"])}{diagrams}<h3>Acceptance criteria</h3><table><thead><tr><th>ID</th><th>Given</th><th>When</th><th>Then</th></tr></thead><tbody>{criteria or "<tr><td colspan=4>Not yet defined</td></tr>"}</tbody></table><h3>Test cases</h3><table><thead><tr><th>ID</th><th>Type</th><th>Scenario</th><th>Expected result</th></tr></thead><tbody>{tests or "<tr><td colspan=4>Not yet defined</td></tr>"}</tbody></table><h3>Assumptions and questions</h3><p>{esc(", ".join(task["assumption_ids"]) or "None")}; {esc(", ".join(task["question_ids"]) or "None")}</p><h3>Evidence</h3>{refs(task["source_ids"], sources)}</section>')
    sections.append('<section class="section"><h2>Source register</h2><table><thead><tr><th>ID</th><th>Type and date</th><th>Location</th><th>Evidence</th></tr></thead><tbody>' + ''.join(f'<tr><td>{esc(s["id"])}</td><td>{esc(s["kind"])}<br>{esc(s.get("date"))} · {esc(s.get("speaker"))}</td><td>{esc(s["reference"])}</td><td>{esc(s["quote"] or s["summary"])}</td></tr>' for s in sources) + '</tbody></table></section>')
    return '<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>' + esc(case["title"]) + '</title><style>' + css + '</style></head><body>' + ''.join(sections) + '</body></html>'


def find_chrome() -> str | None:
    candidates = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]
    return next((p for p in candidates if Path(p).is_file()), None) or shutil.which("google-chrome") or shutil.which("chromium")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path)
    parser.add_argument("-o", "--output", type=Path, help="Output PDF path")
    args = parser.parse_args()
    source = args.json_file.resolve()
    output = (args.output or source.with_suffix(".pdf")).resolve()
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(f"cannot read valid JSON: {exc}")
    for key in ("project", "business_case", "sources", "assumptions", "questions", "dependencies", "people", "tasks"):
        if key not in data:
            parser.error(f"missing required top-level field: {key}")
    chrome = find_chrome()
    if not chrome:
        parser.error("Chrome or Chromium is required to print the HTML report to PDF")
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        parser.error("pypdf is required to embed the JSON attachment. Install it with: python3 -m pip install pypdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="story-cards-") as tmp:
        html_file = Path(tmp) / "report.html"
        pdf_file = Path(tmp) / "report.pdf"
        html_file.write_text(render(data), encoding="utf-8")
        profile = Path(tmp) / "chrome-profile"
        result = subprocess.run([chrome, "--headless", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}", "--no-pdf-header-footer", "--print-to-pdf=" + str(pdf_file), html_file.as_uri()], capture_output=True, text=True)
        if result.returncode or not pdf_file.exists():
            print(result.stderr or "Chrome failed to create the PDF", file=sys.stderr)
            return 1
        reader = PdfReader(str(pdf_file))
        writer = PdfWriter()
        writer.clone_document_from_reader(reader)
        writer.add_attachment("work-items.json", source.read_bytes())
        with output.open("wb") as handle:
            writer.write(handle)
    check = PdfReader(str(output))
    embedded = check.attachments
    if "work-items.json" not in embedded:
        parser.error("PDF was written but the JSON attachment could not be verified")
    json.loads(embedded["work-items.json"][0].decode("utf-8"))
    print(f"PDF: {output}\nPages: {len(check.pages)}\nAttachment: work-items.json (valid JSON)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
