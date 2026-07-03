# Configurator Spec

Read when: adapting `assets/configurator.html` in Phase A (prep).

The configurator is the session's centerpiece: one self-contained HTML file
where look-and-feel is a runtime parameter, so parametric design moves cost
0ms. It is throwaway (like a wireframe) but its *exported tokens* are not.

## Non-negotiables

- **Single static file, no build step** — opens with a double-click, same rule
  as `plan/wireframes/`. Vanilla JS only.
- **Every visual property flows through a CSS custom property** on `:root`.
  If a look-and-feel change would require editing a rule instead of a
  variable, the wiring is wrong. Test: apply two presets; everything that
  should differ, differs.
- **Real domain content.** Entity names, columns, and form fields from
  `SPEC.md` / `glossary.md`. Judging a look on lorem ipsum produces taste
  verdicts that don't survive contact with real data density.
- **Token names match build-loop coding-standards §14** — the export must be
  usable as the project's `tokens.css` verbatim.

## Required screens (form-over-data default)

1. **Datagrid screen** — toolbar (search box, filter chip, column-toggle menu,
   Export CSV button), 8–12 rows of realistic data, sortable header, one
   status-badge column (exercises accent/semantic colors), pagination footer.
2. **Form screen** — 6–10 fields of mixed types, one validation error visible
   (exercises the danger color), primary/secondary buttons, section header.
3. Shared app shell — nav, page title. Toggle screens via tabs or `?screen=`.

For non-form-over-data apps, substitute the 1–2 screens that dominate real
usage. Never more than 3 — this is a taste instrument, not a prototype.

## Token vocabulary (baseline)

```css
:root {
  /* color */
  --bg: ; --surface: ; --text: ; --text-muted: ;
  --accent: ; --accent-contrast: ; --border: ;
  --ok: ; --warn: ; --danger: ;
  /* shape & rhythm */
  --radius: ; --space: ;        /* --space is the density unit; grid row
                                    height, form gaps etc. are multiples */
  --shadow: ;
  /* type */
  --font-display: ; --font-body: ; --font-mono: ;
  --font-size: ; --font-scale: ; /* modular scale ratio for headings */
}
```

Extend freely, but anything added must appear in every preset and in the
export.

## Theme panel

Floating, bottom-right, collapsible. Contains:

- **Preset row** — one button per preset from `references/presets.md`; applies
  the full token block to `:root` instantly.
- **Sliders** — `--radius`, `--space` (density), `--font-size`.
- **Pickers** — accent color, bg/surface pair, font-pair dropdown (pairs, not
  independent axes — type pairs are chosen as pairs).
- **Export button** — serializes the *current* `:root` values into a complete
  `tokens.css` text block: rendered in a `<pre>` and copied to clipboard.
  This output IS the session deliverable; no hand-transcription.
- **URL state** — `?preset=name` applies a preset on load, so any state is a
  shareable link and each round's archive is reproducible.

## Session ergonomics

- Preset application and slider moves must repaint without flicker
  (`transition` on colors ≈150ms is pleasant; nothing on layout).
- Keyboard: `1`–`9` apply presets in order — the SME will ask to "flip back
  to 3" constantly; make that instant.
- Archive a round by saving the exported token block to
  `plan/moodboards/round-N/candidate-X.tokens.css` plus one screenshot.
