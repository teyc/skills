# Preset Library

Read when: loading presets in Phase A, or adding project-specific ones.

Presets are the session's opening bids — instant, zero-generation round-1
diversity. Each is a complete token block (every variable from
`references/configurator.md §Token vocabulary`, no gaps) plus mood words, so
the SME can react to a *feeling*, not a color list. Deliberate choices beat
defaults: a preset may use a "cliché" combination only as a named, intentional
direction.

Format for adding one:

```markdown
## preset-name
Mood: word, word, word
Best for: [one line]
```css
[complete :root block]
```
```

---

## neutral-start
Mood: calm, unopinionated, honest
Best for: opening the session without anchoring the SME
```css
:root {
  --bg:#fafafa; --surface:#ffffff; --text:#1a1a1a; --text-muted:#6b7280;
  --accent:#2563eb; --accent-contrast:#ffffff; --border:#e5e7eb;
  --ok:#16a34a; --warn:#d97706; --danger:#dc2626;
  --radius:6px; --space:8px; --shadow:0 1px 3px rgb(0 0 0 / .08);
  --font-display:system-ui; --font-body:system-ui; --font-mono:ui-monospace;
  --font-size:14px; --font-scale:1.2;
}
```

## linear-dark
Mood: engineered, dense, focused
Best for: power-user tools lived in all day
```css
:root {
  --bg:#0e0f13; --surface:#16171d; --text:#e6e7eb; --text-muted:#8a8f98;
  --accent:#5e6ad2; --accent-contrast:#ffffff; --border:#26282f;
  --ok:#4cb782; --warn:#d4a72c; --danger:#eb5757;
  --radius:8px; --space:6px; --shadow:0 2px 8px rgb(0 0 0 / .45);
  --font-display:"Inter",system-ui; --font-body:"Inter",system-ui; --font-mono:"JetBrains Mono",monospace;
  --font-size:13px; --font-scale:1.15;
}
```

## notion-calm
Mood: warm, literate, unhurried
Best for: content-heavy tools, documentation-adjacent apps
```css
:root {
  --bg:#f7f6f3; --surface:#ffffff; --text:#37352f; --text-muted:#9b9a97;
  --accent:#2e6ad1; --accent-contrast:#ffffff; --border:#e9e7e3;
  --ok:#448361; --warn:#c77d2e; --danger:#d44c47;
  --radius:4px; --space:10px; --shadow:0 1px 2px rgb(0 0 0 / .06);
  --font-display:Georgia,serif; --font-body:system-ui; --font-mono:ui-monospace;
  --font-size:15px; --font-scale:1.25;
}
```

## terminal-dense
Mood: technical, unadorned, fast
Best for: ops dashboards, log-heavy internal tools
```css
:root {
  --bg:#101214; --surface:#16191c; --text:#d6dbe1; --text-muted:#7d8590;
  --accent:#e3b341; --accent-contrast:#101214; --border:#2b3138;
  --ok:#3fb950; --warn:#d29922; --danger:#f85149;
  --radius:2px; --space:5px; --shadow:none;
  --font-display:ui-monospace,monospace; --font-body:ui-monospace,monospace; --font-mono:ui-monospace,monospace;
  --font-size:13px; --font-scale:1.1;
}
```

## gov-service
Mood: plain, trustworthy, accessible
Best for: public-facing or compliance-shaped services
```css
:root {
  --bg:#ffffff; --surface:#ffffff; --text:#0b0c0c; --text-muted:#505a5f;
  --accent:#1d70b8; --accent-contrast:#ffffff; --border:#b1b4b6;
  --ok:#00703c; --warn:#f47738; --danger:#d4351c;
  --radius:0px; --space:10px; --shadow:none;
  --font-display:system-ui; --font-body:system-ui; --font-mono:ui-monospace;
  --font-size:16px; --font-scale:1.3;
}
```

## swiss-print
Mood: stark, confident, editorial
Best for: apps that want a strong identity without decoration
```css
:root {
  --bg:#ffffff; --surface:#ffffff; --text:#111111; --text-muted:#767676;
  --accent:#e0301e; --accent-contrast:#ffffff; --border:#111111;
  --ok:#1f7a33; --warn:#b7791f; --danger:#e0301e;
  --radius:0px; --space:8px; --shadow:none;
  --font-display:"Helvetica Neue",Arial,sans-serif; --font-body:"Helvetica Neue",Arial,sans-serif; --font-mono:ui-monospace;
  --font-size:14px; --font-scale:1.333;
}
```

## soft-fintech
Mood: assured, rounded, premium
Best for: money-adjacent apps that must feel safe
```css
:root {
  --bg:#f4f7f5; --surface:#ffffff; --text:#0f2e24; --text-muted:#5f7169;
  --accent:#0d6e4f; --accent-contrast:#ffffff; --border:#dde5e0;
  --ok:#0d6e4f; --warn:#b7791f; --danger:#b3261e;
  --radius:12px; --space:10px; --shadow:0 2px 10px rgb(13 110 79 / .08);
  --font-display:"Inter",system-ui; --font-body:"Inter",system-ui; --font-mono:ui-monospace;
  --font-size:14px; --font-scale:1.25;
}
```

## industrial-slate
Mood: sturdy, operational, no-nonsense
Best for: field/ops tools — work orders, assets, schedules
```css
:root {
  --bg:#eef1f4; --surface:#ffffff; --text:#1c2733; --text-muted:#5c6b7a;
  --accent:#c75300; --accent-contrast:#ffffff; --border:#cfd8e0;
  --ok:#2e7d32; --warn:#c75300; --danger:#c62828;
  --radius:3px; --space:7px; --shadow:0 1px 2px rgb(28 39 51 / .12);
  --font-display:system-ui; --font-body:system-ui; --font-mono:ui-monospace;
  --font-size:14px; --font-scale:1.2;
}
```

---

**Rules:**
- Every preset defines every token — a partial preset makes "flip back to 3"
  lie, because leftovers from the previous preset bleed through.
- Project-specific presets go at the bottom, named after their mood, not the
  client ("harbor-calm", not "acme-v2").
- If the SME lands on an unmodified preset at the buzzer, note it in
  DESIGN.md §Provenance honestly — but treat it as a sign the session may not
  have explored far enough.
