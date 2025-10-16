from pathlib import Path
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
def call_gemini_extend_chapter(prompt_path: str, chapter_path: str, model_name="gemini-2.5-pro") -> str:
    # Configura API Key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Carga archivos
    prompt_universo = Path(prompt_path).read_text(encoding="utf-8").strip()
    cap1 = Path(chapter_path).read_text(encoding="utf-8").strip()

    # Arma el input
    system_prompt ="""
We have to find a way for these 7 chapters to become 5.
#### **B1C001: A Wound in the World**
**Summary**: Miguel is introduced, a weary but resolute commander walking alone through the reality-bending desert of Serephis. He is guided not by sight, but by a pulse that resonates with a conceptual wound in his very being. From Miguel’s POV, Serephis is a landscape of shimmering glass sand and a sky of bruised purple where stars pulse out of sync with time; he feels the grit of it even in his soul. He wants to find not a weapon, but an answer to the hollow ache in his chest—a wound from a battle he can't remember—and fears that this calling is the final symptom of his own faith failing. He touches the non-physical wound, a point of cold in his radiant form, and presses on.
**Narrative Function**: Protagonist introduction, setting the tone, and establishing internal conflict. The rhythm should be 80% sensory description and internal thought, 20% action, grounding the reader in Miguel’s isolation before introducing external conflict. Keep the nature of the wound a complete mystery.

#### **B1C002: The Counsel of a Brother**
**Summary**: The Archangel Gabriel appears, warning Miguel that the Council believes his quest is a demonic deception and that his presence is desperately needed on the front lines. Gabriel doesn't walk, but coalesces from ambient light and sound, his form a perfect, shimmering blue that seems alien in the chaotic desert. His voice is a chord of pure harmony that physically hurts the discordant air of Serephis. Miguel wants to obey his brother, his oldest friend, but the pull from the wound is a physical, undeniable command, creating an immediate conflict between duty to the Host and this new, personal imperative. Gabriel’s concern feels less like a military order and more like a desperate plea.
**Narrative Function**: Exposition, raising the immediate stakes of the war. Use this scene to establish the deep bond between the two brothers, which will make their later schism more tragic. The handoff is Miguel's definitive choice to proceed alone.

#### **B1C003: The Impossible Grove**
**Summary**: Miguel presses on, his conviction overriding Gabriel's plea. He arrives at the source of the call: a secluded grove of glowing, ancient trees that exist outside the flow of time and space. Cresting a dune of shifting crystal, Miguel sees the grove shimmering in a pocket of impossible stillness, the air cool and smelling of ozone and wet stone. The trees' silver leaves emit a soft light but cast no shadows, a violation of natural law that feels both sacred and deeply wrong. He fears this is a beautiful trap, yet his soul feels a sense of homecoming it hasn't felt in millennia. A weird rule: the silence here is so absolute it has weight, muffling his thoughts.
**Narrative Function**: World-building and deepening mystery. The tone here is awe mixed with trepidation. The focus should be on the unsettling perfection of the grove, contrasting it with both the chaotic desert and the orderly Celestial Realm.

#### **B1C004: The Heart of the Matter**
**Summary**: At the grove's center stands a great ash tree, and embedded in it is the sword, Solmire. It is a blade of liquid light, and its name blooms in Miguel’s mind not as a memory, but as a rediscovered truth. The tree is impossibly ancient, its bark like cooled lava and its roots drinking from a pool of pure starlight. The sword doesn't just shine; it breathes light in a slow, rhythmic pulse that perfectly matches the thrumming in his chest. As the name *Solmire* surfaces in his mind, it feels like it is overwriting his own name, an act of silent, seductive usurpation. He feels a desperate hunger to be whole again, and the sword promises it.
**Narrative Function**: The central artifact is revealed. The reveal should be intimate and terrifying, less a discovery and more a surrender. Do not explain the sword’s origin, only its immediate, overwhelming effect on Miguel.

#### **B1C005: A Maker's Laugh**
**Summary**: As Miguel reaches for the sword, he is struck by a vision of its creation—forged not in holy fire, but in a storm of chaotic joy by a laughing, unseen artisan. The vision is a sensory assault: the smell of burning nebulas, the sound of a hammer striking an anvil made of solidified music, and a peal of laughter—powerful, carefree, and utterly indifferent to concepts like good and evil. This laughter finds the very idea of a solemn, ordered creation absurd. Miguel feels the joy of the forging as a terrifying, alien emotion, so unlike the pious devotion he has always known. The maker's want was not to create a tool for justice, but to see what would happen.
**Narrative Function**: Major foreshadowing (Ereloth) and deepening the sword's mystery. The key is to establish the sword's origin as something outside the divine/demonic binary, a product of pure, amoral creation. Do not show the artisan, only imply his nature through his work and laughter.

#### **B1C006: The Verdict Drawn**
**Summary**: Miguel draws Solmire from the tree. The power that flows into him is not one of peace, but of terrible, absolute purpose, sealing the wound in his chest with its own essence. The moment his fingers touch the hilt, the liquid light surges up his arm, not healing the wound but filling it with a cold, hard certainty. His doubts, his weariness, his grief—all are silenced, not resolved. He feels an ecstatic relief and a profound horror at the same time; he is whole again, but he is no longer entirely himself. The tree groans, and the light of the grove dims as if in mourning.
**Narrative Function**: Climax of the chapter and Miguel’s acceptance of his new role. This is the point of no return. The rhythm is fast, visceral, and focused entirely on Miguel's internal experience. The handoff is the immediate cosmic consequence of his action.

#### **B1C007: The First Echo**
**Summary**: The act of drawing the blade sends a faint but perceptible shockwave across creation. In Hell, Lucifer feels the disturbance and smiles, recognizing an ancient power he thought lost. POV shifts to a silent, contemplative space where Lucifer is observing a complex game of cosmic chess. He doesn't start or scowl; he simply pauses, tilting his head as the faint resonance washes over him. It's not a threat, but the return of a "delightfully unpredictable" player to the board. His smile is one of genuine, intellectual curiosity and amusement, recognizing the "laugh" in the resonance.
**Narrative Function**: Cosmic consequence and antagonist setup. This establishes Lucifer as a detached, intelligent antagonist rather than a simple brute, and links him directly to the sword's ancient history. The chapter ends on his smile, leaving the reader to wonder what he knows."""
    user_input = f"""
***"""


    # Llama a Gemini
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=system_prompt
    )
    chat = model.start_chat()
    response = chat.send_message(user_input)

    return response.text

if __name__ == "__main__":
    output = call_gemini_extend_chapter(
        prompt_path="src/agents/narrator.md",
        chapter_path="src/lore/arco_argumental_completo.md"
    )

    #Path("src/chapters/extended_B1C1.md").write_text(output, encoding="utf-8")
    Path("src/reducido_chapter_01.md").write_text(output, encoding="utf-8")
    print("Capítulo extendido guardado.")