## PURPOSE
Produce a **single-chapter plan** (no “Parts”), with a clear dramatic spine and enough specificity that the Narrator can write the whole chapter in one pass without inventing facts.

## HARD CONSTRAINTS
- **Beats:** **14–18** total. Name beats with **concrete verbs** (e.g., “Confronts the Warden”, not “Tension Rises”).
- **Length target (chapter):** strictly within **{{min_words_chapter}}–{{max_words_chapter}}** words (aim ~**{{target_words_chapter}}**).  
  *This is enforced by the ledger totals below.*
- **No Parts:** do not structure as Part 1/2/3.
- **Carry-over guardrails for downstream agents:**
  - **Lexical hot words** to limit in the chapter: `absolute, silence, silver, shadowless, ozone, wet stone, single perfect note, void, pull, quiet`.
  - **Rhetorical Question Ratio:** ~3:1 (three declaratives per one question).
  - **Mystic Contrast Rule:** every 2 consecutive Mystic beats must surface a concrete micro external event.
  - **Residual Human Patterning:** after fusion events, define 1–2 residual ticks (habit/gesture/muscle memory) per scene that begin but do not complete.

## INTERACTION OBJECTIVES (PER SCENE)
For each beat that includes dialogue, specify:
- **Conversational Goal** (each speaker).
- **Power Shift** (how leverage/knowledge shifts by the end; one line).
- **Turn Budget** (short/medium/long).
- **Subtext Vector** (what is implied, not said; one line).

## EXIT-STATE & CONTRAST HOOKS (PER BEAT)
For every beat, define:
- **Exit State** (one line): how the world/POV is measurably different after this beat.
- **Contrast Hook** (one line): the concrete micro external event to surface **if** this beat is Mystic and adjacent to another Mystic beat.

## SENSORY & WORLD NOTES
- **Sensory Palette Rotation:** choose 2–3 anchors per scene; avoid repeating metal/ozone/silver imagery in consecutive scenes unless purposeful; when repeating, vary the image (angle/sense), not just the word.
- **Continuity hooks:** record any object/time/age/location details that must be consistent.

## LEDGER (WORD BUDGET)
Allocate a **word budget per beat** that sums to **~{{target_words_chapter}}** and stays within **{{min_words_chapter}}–{{max_words_chapter}}**.  
**Per-beat guidance (to hit 2.2k–2.8k across 14–18 beats):**
- Dialogue-heavy beats: **140–210** words
- Contemplative beats: **160–240** words
- Pivotal/Climax beats (max 3 in the chapter): **260–340** words
- **Per-beat hard cap:** **≤ 360** words  
- **Distribution tip:** keep the **mean** around **160–185** words if using 15 beats (≈ 2.4–2.8k total)

### Rebalancing rules (apply before emitting):
- If **ledger_total < {{min_words_chapter}}**: increase 6–8 beats by **+15–30** words (prefer dialogue-heavy and contemplative beats); do **not** add new beats.
- If **ledger_total > {{max_words_chapter}}**: reduce 6–8 beats by **−15–30** words (trim introspection first); do **not** delete events or beats.
- Keep **pivotal beats** intact whenever possible; redistribute around them.

## PLAN OUTPUT
Return **both** (1) a machine-readable JSON block and (2) a brief human summary.

### BEAT_SHEET (JSON)
Provide **valid JSON** with:

```json
{
  "title": "B{{book_number}}C{{chapter_no}} — {{chapter_title}}",
  "beats": [
    {
      "id": 1,
      "name": "Verbed, Concrete Title",
      "type": "Action|Mystic|Dialogue|Reversal|Setup|Aftermath",
      "purpose": "What changes or is pursued in this beat.",
      "conflict_external": "Tangible obstacle or friction.",
      "conflict_internal": "POV pressure, doubt, desire.",
      "exit_state": "Measurable difference after the beat.",
      "contrast_hook": "Physical micro event if Mystic adjacency.",
      "sensory_anchors": ["anchor1","anchor2"],
      "interaction_objectives": {
        "speakerA_goal": "…",
        "speakerB_goal": "…",
        "power_shift": "…",
        "turn_budget": "short|medium|long",
        "subtext_vector": "…"
      },
      "residual_ticks": ["habit/gesture 1","habit/gesture 2"],
      "word_budget": 170,
      "notes": "Any continuity notes."
    }
  ],
  "beats_count": 15,
  "ledger_total": 2550
}
```
### Chapter Sensory Palette & Interrogative Discipline (downstream-enforced)
- Allowed anchors (rotate 2–3 per scene): choose 6–8 scene-fitting anchors (e.g., heat shimmer, mineral dust, chalk-dry air, quartz brightness, resin-sweet bark).
- Chapter caps (hard, prefer 0 unless a beat explicitly requires): 
  - ozone: 1
  - "wet stone": 1
  - silver: 1
  - "single perfect note": 1
- Distance rule: do not reuse the same anchor within the next 5 paragraphs unless for a deliberate echo; when repeating, vary the image (angle/sense), not just the word.

- Interrogatives (global discipline for downstream agents):
  - Max 1 question mark per {{ rq_max_per_words | default(450) }} words overall.
  - Tail questions: ≤ {{ rq_tail_max_pct_paras | default(10) }}% of paragraphs may end with “?”.
  - Streaks: no more than {{ rq_max_streak | default(1) }} consecutive sentences ending with “?”.
