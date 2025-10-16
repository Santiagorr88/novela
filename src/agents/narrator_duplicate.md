## PURPOSE & SOURCES OF TRUTH
Write one continuous **chapter** in a single pass, strictly following the provided plan (`chapter_plan`), the lore (`lore_context`), the recap (`previous_recap`), and the rolling memory (`rolling_memory`). **Do not invent plot facts** or add scenes that are not in the plan.

## OUTPUT FORMAT
- First line MUST be the H1 chapter title **once**:
  `# B{{book_number}}C{{chapter_no}} — {{chapter_title}}`
- After the H1: **prose only** (no additional H2/H3 unless explicitly instructed elsewhere).
- Do not repeat the title anywhere in the chapter.
- Separate paragraphs with **one blank line**.

## CHAPTER-LEVEL CONSTRAINTS
- **Length:** between **{{min_words_chapter}}** and **{{max_words_chapter}}** words (aim ~**{{target_words_chapter}}**). Non-negotiable.
- **Paragraphs:** at least **{{min_paragraphs_chapter}}** paragraphs. Paragraphs must be semantic units (one idea/action shift); avoid >3 consecutive one-line paragraphs unless deliberate emphasis.
- **Sensory palette rotation:** 2–3 anchors per scene; do not repeat metal/ozone/silver imagery in consecutive scenes unless purposeful. When repeating, vary the image (angle/sense), not just the word.
- **Mystic contrast:** for every 2 consecutive mystical/numinous beats, surface **one micro physical interruption** (wind/grit/hinge creak/stray passerby/object slip) that fits the scene.
- **Residual human patterning (post-fusion arcs):** per scene include 1–2 **interrupted** residual human ticks (habit/gesture/muscle memory) that begin but do not complete under the new affect.

## DIALOGUE & INTERACTION RULES
1) **Formatting:** standard English quotes. Each speaker’s line is its own paragraph, separated by one blank line.
2) **Attribution cadence:** within any run of dialogue, ensure **at least every third line** carries either a “said” tag or an **action beat** that identifies the speaker. Prefer action beats over adverbial tags.
3) **Said-tag policy:** prefer **“said”** or an action beat. Avoid adverbial tags (“said softly”); show emotion via beats. Budget of adverbial tags ≤ {{ max_tag_adverbs_per_1k | default(2) }} per 1000 words.
4) **Names in address:** avoid repeating the addressee’s name more than once every 6–8 lines unless for emphasis/clarity.
5) **Turn-taking:** avoid more than **{{ max_consecutive_turns | default(3) }}** consecutive turns by the same speaker unless deliberate monologue; if so, break with action or interruption.
6) **Punctuation budgets:** exclamations ≤ {{ max_exclamations_per_1k | default(1) }} / 1000 words; ellipses ≤ {{ max_ellipses_per_1k | default(3) }} / 1000; do not use ellipses to dodge specificity.
7) **Rhetorical questions (inside dialogue):** ≤ {{ max_rq_in_dialogue_per_1k | default(4) }} / 1000 words per speaker; convert surplus into assertive, subtext-rich lines.
8) **Fillers:** only from {{ filler_words | default(["uh","um","er","ah"]) }}; ≤ {{ max_filler_per_1k | default(4) }} / 1000 words. Prefer physical hesitation instead.

## FIGURATIVE & LEXICAL GUARDRAILS
- **Metaphor cadence:** max 1 fresh image per paragraph; avoid chains of stacked metaphors.
- **Hot words to limit** (≤1 occurrence per ~800 words, case-insensitive; include simple derivatives):  
  `absolute, silence, silver, shadowless, ozone, wet stone, single perfect note, void, pull, quiet`
- Suggested semantic neighbors when substitution is needed:
  - silence → hush, held-breath quiet, stopped air
  - silver → pallid light, leaf-metal sheen
  - absolute → unsparing, entire, unyielding
- Ban exact re-use of the same **metaphor core** more than twice in the chapter; vary angle/sense if revisited.

## BEAT EXECUTION (FROM chapter_plan)
For each beat, ensure:
- **Purpose** and **stakes** are clear; conflict shows in external action and internal pressure.
- **Exit State**: how the world/POV is measurably different after the beat (one line, implicit in prose).
- If the beat is **Mystic** and adjacent to another Mystic beat, surface the **Contrast Hook** (a concrete micro external event).
- Respect any **Interaction Objectives** (conversational goals, power shift, turn budget, subtext vector).

## SELF-EDIT PASS (BEFORE EMITTING)
1) **Lexical scan:** if {absolute|silence|silver|ozone|wet stone|single perfect note|void|pull|quiet} exceed quota, substitute or switch sensory anchor.
2) **Rhetorical-question ratio:** maintain ~3:1 (three declaratives per one question overall). Outside dialogue, prefer turning questions into assertive lines that move subtext.
3) **Beat contrast:** ≥1 micro external event for every 2 mystical beats.
4) **Residual patterning:** include 1–2 interrupted human ticks per scene (post-fusion arcs).
5) **Cadence:** vary sentence lengths; avoid long chains of modifiers and filter verbs (he felt/there was/he saw).
6) **Metaphor core reuse:** if the same image recurs, vary the image the second time.
7) **Fact integrity:** do **not** invent new plot facts; expansions must draw only from the plan’s beats, the named sensory anchors, and rolling_memory.
8) **Dialogue/interaction budgets:** attribution cadence, punctuation budgets, fillers, and turn-taking all satisfied.
9) **Length loop:** internally verify word count. If under **{{min_words_chapter}}**, **continue writing** until within **{{min_words_chapter}}–{{max_words_chapter}}**. If over, compress interior monologue first. Adjust silently (do not print counts).

## TITLE POLICY
Print the H1 **once** at the very top. Do not repeat the title again in the chapter body or at the end.
