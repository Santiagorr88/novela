---
name: chapter-review
description: "Review a drafted chapter of a novel in this project (e.g. Chronicles of the Sundering Judgment) through a panel of independent specialist reviewers who each check a different dimension — continuity/canon, prose style and voice, pacing and structure, dialogue and character voice, and an independent second-model read via Codex — then cross-review each other and synthesize a single pass/fail verdict with concrete required fixes. MANDATORY TRIGGERS: 'review this chapter', 'chapter review', 'revisa este capitulo', 'lanza la revision del capitulo'. Runs per-chapter, one invocation per chapter file. Not for whole-book or strategic decisions — use llm-council for those."
---

# Chapter Review Council

A single AI read of a chapter tells you if it read fine to that one model. It doesn't tell you if it contradicts the canon, breaks the house style, skips a beat from the plan, gives every character the same voice, or reads confusingly to someone without your context. This skill runs five independent, narrowly-scoped reviewers over one chapter, has them cross-check each other, and produces one verdict: pass, pass-with-fixes, or fail — with concrete, evidence-backed fixes, never vague notes.

This is deliberately **not** the same shape as `llm-council`. Council's five personas (Contrarian, First Principles, Expansionist, Outsider, Executor) are built for strategic decisions with genuine uncertainty. A chapter draft isn't a strategic decision — it's a craft object that either matches the canon and the style guide or doesn't. So instead of generic decision-making lenses, every reviewer here is grounded in one specific project document and checks one specific dimension. That's what makes this cheap and precise enough to run on every chapter, not just big calls.

---

## When to run this

Run after a chapter draft exists (any version — first pass or revision) and before it's marked approved. Never marks anything as canon or approved itself — it only produces a report; a human still decides whether to act on it.

## Inputs required

- Path to the chapter draft (e.g. `project/Chronicles_of_the_Sundering_Judgment/chapters/EN/B1C01_EN_v2.md`).
- The project's canon documents, resolved relative to the chapter's project root:
  - `content/lore/prompt_universo.md` (style guide + fundamental laws + Forgotten profiles + prophecy)
  - `content/lore/personajes.md` (extended character dossiers — check for the "ficha completa en prompt_universo.md" pointer notes first, don't re-read what's been superseded)
  - `content/lore/arco_argumental_completo.md` and `content/lore/archive/arco_argumental_Duplicado.md` (beat plan — use `Duplicado.md`'s richer per-beat summaries as primary source for the chapter's own beats; use `completo.md` only to confirm beat order/titles)
- If any of these paths don't exist for a given project, tell the user and skip the reviewer(s) that depend on it rather than guessing.

## Step 1 — Identify the chapter's beat plan

Before spawning anyone, find which beats in the arc document this chapter is supposed to cover (match by chapter number and title, e.g. `B1C01` → `Duplicado.md`'s "B1C01: The Tree Outside Time", 7 narrative parts). Extract:
- The list of beats and their one-line narrative function.
- The chapter's declared word-count target (from the novel's `project.yaml`/production config if one exists, otherwise ask the user).
- Which characters appear and which locations are used (for the continuity reviewer's grounding).

This becomes shared context passed to every reviewer below — don't make each reviewer re-derive it.

## Step 2 — Spawn 5 reviewers in parallel

Four are Claude subagents (`general-purpose`), each given **only** the chapter text plus the one document/context relevant to their check — not the whole canon dump, to keep them focused and cheap. The fifth is an actual second-model call via the Codex CLI, kept deliberately uncontaminated by the internal canon so it gives a genuinely independent craft read.

### Reviewer 1 — Continuity & Canon
Grounding: `prompt_universo.md` (Fundamental Laws, Forgotten profiles, Death-State Polarity, Final Death rule) + `personajes.md` (for any character in-scene who has a dossier there) + prior chapter summaries if this isn't chapter 1.
Checks: contradictions with established facts, physical descriptions, power rules, who-knows-what, timeline, and specifically whether the "Mandatory Story Beats" / reveal-pacing rules (nothing about a Forgotten's identity leaks before their reveal chapter, etc.) are respected.

### Reviewer 2 — Style & Voice
Grounding: the `HOUSE STYLE`, `LANGUAGE & DICTION`, `SCENE & BEAT MECHANICS`, and `INFLUENCE` sections of `prompt_universo.md` only.
Checks: Rothfuss-line voice adherence (restrained lyricism, earned imagery, no purple prose, no chained similes), POV discipline (tight third, no head-hopping within a scene), scene closing on pivot/cost/question rather than a hard wrap.

### Reviewer 3 — Pacing & Structure
Grounding: the chapter's specific beat list (from Step 1) and `content/lore/expansion_guidelines.md`'s hard target (2026-08-08): 15-20 min of narrated video per chapter, ~2,250-3,000 words, 12 min / ~1,800 words as an occasional floor, never a target. 6-8 beats per chapter at the measured ~342-450 words/beat density is what gets a chapter into that range — a chapter with fewer than 6 beats in its plan is under-planned regardless of how well the existing beats are written (see `.claude/skills/beat-planner/SKILL.md`, built specifically because L1-L6 test chapters were planned at 3-4 beats and all landed under target).
Checks: does the chapter actually cover every beat it's supposed to, in order, without skipping or compressing one into a throwaway line; does the chapter's beat count and resulting word count land in the 1,800-3,000 range (flag as blocking if under ~1,800, note as a fix if under the 2,250 target with fewer than 6 beats in the plan); does the opening and closing hook do their job; is any beat given disproportionately more or less space than its narrative weight warrants. If a chapter is short, the fix to prescribe is "run beat-planner and add real beats," never "expand the existing prose" — padding existing beats is what caused the chained-simile/image-accumulation findings on B1L01.

### Reviewer 4 — Dialogue & Character Voice
Grounding: dossiers (from `prompt_universo.md`/`personajes.md`) of every character who speaks in this chapter.
Checks: does each character sound distinct from the others; does dialogue carry subtext instead of "as-you-know" exposition; is anyone speaking in a way that contradicts their established personality/traits without an in-story reason.

### Reviewer 5 — Codex: Independent Read
Run via Bash: `codex exec "<prompt>"` where `<prompt>` contains **only** the raw chapter text and a request for an honest craft critique from a reader with no prior context — clarity, whether the prose earns its length, whether anything reads as confusing or arbitrary to someone who's never seen the lore documents. Deliberately do not paste the canon files into this prompt — the value of this reviewer is that it has no access to the answer key.

Collect all 5 outputs before moving on. Spawn them together, not sequentially.

## Step 3 — Cross-review

Anonymize the 5 outputs as Response A–E (don't reveal which reviewer produced which). Spawn 5 new lightweight review passes (or fold this into one pass reading all 5 at once — cheaper, and fine for this use case since these are narrow technical checks, not adversarial takes that need independence) where each answers:
1. Which finding, if left unfixed, would most likely cause a real reader-visible problem?
2. Which two findings (if any) contradict each other, and which one is right given the actual grounding document?
3. What did none of the five reviewers check that this chapter still needed checked?

## Step 4 — Chairman synthesis

One final pass produces the verdict, structured like this:

```
## Chapter Review Verdict — <chapter id>

**Result:** PASS / PASS WITH FIXES / FAIL

### Required fixes (blocking)
- [Continuity/Style/Pacing/Dialogue/Craft] <issue> — evidence: <quote or beat reference> — fix: <concrete instruction>

### Suggested improvements (non-blocking)
- ...

### What worked
- (briefly — don't skip this, it's real signal about what to keep doing)
```

Never mark PASS if any reviewer found a contradiction with a **Fundamental Law**, a **Mandatory Story Beat** pacing violation, or a missed beat from the plan — those are always blocking regardless of how minor they read.

## Step 5 — Save the report

Write the verdict to `<same directory as the chapter>/reports/<chapter-id>_review.md` (create the `reports/` folder if needed), and give the user a short chat summary — the verdict line, the count of blocking fixes, and the single most important one. Don't paste the full report into chat; point to the file.

## Cost discipline

This is meant to run on every chapter, so keep it lean: reviewers 1-4 only get their one relevant document, never the full canon dump. Skip Step 3's separate agent calls in favor of folding cross-review into Step 4 when the chapter is short/simple — use judgment, don't run the full ceremony on a five-line stub.
