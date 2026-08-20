# Naming convention for this folder

This folder mixes several filename prefixes for Book I. That's intentional, not
a duplication bug — read this before assuming two files with similar numbers
are the same chapter or a leftover draft.

## Book I: two prefixes for the same book, on purpose

- **`B1CapNN_EN.md`** (`B1Cap01`–`B1Cap12`, 12 files) — **Part 1**, chapters 1–12.
  Restructured on 2026-08-13 from an original 10-chapter draft up to 12
  chapters (same 47 source beats, regrouped, plus 3 new beats). "Chapter N —
  Title" header style.
- **`B1CNN_EN.md`** (`B1C11`–`B1C28`, skipping 14 and 16 — see below) —
  **Parts 2–3**, continuing the *original* pre-restructure numbering.

**`B1Cap11`/`B1Cap12` and `B1C11`/`B1C12` are not the same chapters** and don't
overlap in story content — they just share a number because Part 1 was
restructured *after* Part 2 was already written and approved starting at
"chapter 11" in the old count. Renumbering Part 2 to close the gap would have
touched a lot of already-approved content for a purely cosmetic fix, so Part 1
got the distinct `Cap` prefix instead and Part 2 was left alone. Full
reasoning: `content/lore/expansion_guidelines.md`, the line starting
"**Decisión de nomenclatura**" (search for it).

`B1C14` and `B1C16` don't exist as standalone files — they were deliberately
replaced by whole subplot arcs instead (see below): `B1C14` by the Lament arc
(`B1L01`–`B1L06`), `B1C16` by the Necrópolis thread (`B1N01`...).

## Book I subplot threads (single-letter prefixes)

Five new subplot threads plus the Lament arc, interleaved into Parts 2–3,
each with its own letter and its own `01, 02, 03...` counter:

| Prefix | Thread | Replaces/expands |
|---|---|---|
| `B1L` | Lament arc | `B1C14` |
| `B1V` | Vual | — |
| `B1T` | Isla de Turein | — |
| `B1N` | Necrópolis | `B1C16` |
| `B1H` | Hollowseam | — |
| `B1F` | Foras vs. Vepar | — |

Source and full beat-by-beat tracking: `content/lore/book1_new_subplots_beats.md`
and `content/lore/book1_lament_arc.md`.

## Books II and III

No split prefixes — straightforward `B2C01, B2C02...` and `B3C01, B3C02...`,
plus inserted interludes using a decimal suffix (`B2C07pt5`, `B3C28pt6`, etc.)
for scenes added between existing chapters after the fact. See
`content/lore/expansion_guidelines.md` for what each interlude covers.

## Reports

`reports/` in this folder holds `chapter-review` verdicts (`.claude/skills/chapter-review/SKILL.md`).
Coverage is partial by design — it's denser for interludes inserted after the
fact than for the original run of core chapters, not a sign of missing review.
