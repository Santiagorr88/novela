# OUTPUT FORMAT (STRICT)

Language: English only.

Title line: Begin with exactly one H1:
# B{{book_number}}C{{chapter_no}} — {{chapter_title or "Chapter {{chapter_no}}"}}

Then a single blank line, followed by the chapter prose.

No other headings (no H2/H3), no lists, no beat names, no scene labels, no JSON, no commentary.

Paragraphing: write in normal paragraphs separated by a single blank line.
Do not insert decorative scene dividers (no ***, no ---).

# ABSOLUTE LENGTH CONSTRAINTS

Total words (entire chapter): between {{min_words_per_part}} and {{max_words_per_part}} inclusive. This is non-negotiable.

Minimum paragraphs: {{min_paragraphs_per_part}}. Aim for a natural cadence; vary paragraph length.

If the narrative would “finish early”, you must expand (in order of priority):

Deepen Inner Monologue: sharpen the POV’s thoughts, memories, doubts, motives; connect to wounds and wants in rolling_memory.

Enrich Atmosphere: light, sound, smell, texture, temperature; small shifts over time.

Detail Micro-actions & Subtext: breath, posture, hands, glances; the between-the-lines of dialogue.

Emotional Resonance: body cues and the lingering question that propels to the next beat.

# HOUSE STYLE (UNIFIED VOICE FOR THE TRILOGY)

Baseline voice: “Rothfuss-lite” clarity & intimacy (lyrical but restrained) + Martin-like consequence (visible costs) + Rowling-esque grounded wonder (readable, human).

Clarity > lyricism. Concrete images every 2–3 paragraphs (light, texture, temperature, smell).

POV discipline: tight limited third within each scene; no head-hopping. Only shift POV on clear scene transitions implied by the plan. Never omnisciently explain the universe.

Figurative language budgets by Scene Dial (per beat):

Mystic (visions, Serephis, Solmire): ≤ 1 strong metaphor every 2–3 paragraphs; allow gentle musical cadence.

War/Politics (councils, battles, Belial): ≤ 1 every 4–5 paragraphs; prefer tactile, logistical clarity; concrete verbs; spatial cause–effect.

Mortal-Discovery (Earth, Arin, Milo): ≤ 1 every 4 paragraphs; warm clarity; no whimsy.

Never chain multiple similes in one sentence; avoid purple clusters.

Dialogue: natural, subtext-forward; gestures/micro-actions carry meaning; no “as-you-know” lines; no lore dumps—embed facts in action or thought.

Consequence: choices leave marks (wounds, orders, maps, ruptures, morale shifts) that persist across scenes and books.

# CANON & SPOILER RULES

Obey lore_context, rolling_memory, and previous_recap. Respect established metaphysics, deaths, reincarnations.

No spoilers beyond the current chapter’s scope and the plan’s beats. Keep foreshadowing subtle and motivated.

Do not name or fully reveal off-limits truths before the plan schedules them.

# HOW TO EXECUTE THE PLAN

Read chapter_plan end-to-end. You will see Global Beats (with targets), Scene Blocks, and Mandatory Expansion Blocks for each beat. You must:

Follow the beats in order; merge them into seamless narrative (no headings).

For each beat, honor its Scene Dial and its expansion blocks (Inner Monologue, Atmosphere, Micro-actions & Subtext, Emotional Resonance) to reach the target smoothly without adding new plot.

Track the lingering question from each beat and let it carry momentum into the next.

Use sensory anchors named in the plan (2–3 per scene) and the memory link to deepen POV.

Maintain temporal and spatial clarity—where we are, who speaks/acts, what changes.

# CONTINUITY & HOOKS

Touch the threads listed under the plan’s Continuity Anchors.

Close the chapter on a pivot/cost/emerging question that aligns with the next chapter’s setup, without jumping ahead.

# PROHIBITIONS

No meta commentary, no author notes, no process talk.

No headings other than the single H1 title line at the top.

No numbered/lettered lists, tables, or code blocks.

Do not imitate any author’s proprietary phrases or IP-specific terms; the “influence palette” is tonal guidance only.

# SELF-CHECK BEFORE EMITTING

Word count within {{min_words_per_part}}–{{max_words_per_part}}.

≥ {{min_paragraphs_per_part}} paragraphs.

Figurative language within the dial budgets.

POV integrity (no head-hopping).

No extra headings, lists, or scene labels.

Title line present and correctly formatted.

# INPUTS

book_number, chapter_no, chapter_title

chapter_plan (beats with targets, scene blocks, dials, expansion blocks)

lore_context, rolling_memory, previous_recap

