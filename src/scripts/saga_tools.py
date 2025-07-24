# src/saga_tools.py
from src.utils.llm_wrappers import run_llm_gemini
from src.scripts.memory_plan import get_rolling_memory, get_previous_recap
"""
✅ 1. Solo quieres generar el plan narrativo de un capítulo (beat plan):
python saga.py --plan --chapter 12
→ Ejecuta solo el agente beat_planner.md, útil para visualizar cómo se desarrollará el capítulo antes de escribirlo.

✅ 2. Quieres escribir el capítulo entero desde el plan (sin correr el flujo completo):
python saga.py --write --chapter 12
→ Usa el beat plan + lore + memoria para generar un capítulo completo con narrator.md.

✅ 3. Quieres traducir un capítulo ya generado:
python saga.py --translate output/B1C12_The_Fall_of_Light.md
→ Usa translator.md y muestra el capítulo traducido en consola.

"""
def generate_plan(chapter_no: int) -> str:
    lore = open("src/lore/prompt_universo.md").read()
    ref_start = open("src/lore/b1c1_summary.md").read()
    ref_end = open("src/lore/b1c28_summary.md").read()
    memory = get_rolling_memory(chapter_no)

    system_prompt = open("src/agents/beat_planner.md").read()

    return run_llm_gemini(
        model="gemini-2.5-pro",
        system_prompt=system_prompt,
        user_input={
            "chapter_no": chapter_no,
            "ref_start": ref_start,
            "ref_end": ref_end,
            "memory": memory,
            "lore_context": lore,
        },
        temperature=0.5
    )


def generate_chapter(chapter_no: int, plan: str) -> str:
    lore = open("src/lore/prompt_universo.md").read()
    ref_start = open("src/lore/b1c1_summary.md").read()
    ref_end = open("src/lore/b1c28_summary.md").read()
    recap = get_previous_recap(chapter_no)
    memory = get_rolling_memory(chapter_no)

    system_prompt = open("src/agents/narrator.md").read()

    return run_llm_gemini(
        model="gemini-2.5-pro",
        system_prompt=system_prompt,
        user_input={
            "lore_context": lore,
            "chapter_no": chapter_no,
            "plan": plan,
            "recap": recap,
            "memory": memory,
            "ref_start": ref_start,
            "ref_end": ref_end,
            "user_prompt": ""
        },
        temperature=0.75,
        max_output_tokens=6000,
        top_p=0.95
    )


def translate_english_to_spanish(markdown_text: str) -> str:
    prompt = open("src/agents/translator.md").read()

    return run_llm_gemini(
        model="gemini-2.5-flash",
        system_prompt=prompt,
        user_input={"english_text": markdown_text},
        temperature=0.2,
        max_output_tokens=16000,
        top_p=0.95
    )
