import os

def get_rolling_memory(chapter_no) -> str:
    """Devuelve todos los resúmenes anteriores como memoria acumulada."""
    chapter_no = int(chapter_no)  # <-- cast robusto
    content = ""
    for i in range(1, chapter_no):
        path = f"src/chapters/recap/B1C{i:02d}_recap.md"
        if os.path.exists(path):
            with open(path, "r") as f:
                content += f"\n\n---\n\n# B1C{i:02d} Recap\n" + f.read()
    return content

def get_last_n_recaps(chapter_no: int, n: int = 3) -> str:
    """Devuelve los últimos N recaps para memoria compacta."""
    content = ""
    for i in range(max(1, chapter_no - n), chapter_no):
        path = f"src/chapters/recap/B1C{i:02d}_recap.md"
        if os.path.exists(path):
            with open(path, "r") as f:
                content += f"\n\n---\n\n# B1C{i:02d} Recap\n" + f.read()
    return content


def get_chapter_plan(chapter_no: int) -> str:
    """Genera el esquema base del capítulo usando su número."""
    return f"Plan for Chapter {chapter_no}:\n- Opening tension beat\n- Reveal or mystery beat\n- Character decision or interaction\n- Twist or complication\n- Hook to next chapter"


def get_previous_recap(chapter_no: int) -> str:
    """Carga el resumen del capítulo anterior si existe."""
    chapter_no = int(chapter_no)  # Asegura conversión
    if chapter_no <= 1:
        return ""  # No hay recap previo para el capítulo 1
    recap_path = f"src/chapters/recap/B1C{chapter_no - 1:02d}_recap.md"
    if os.path.exists(recap_path):
        with open(recap_path, "r") as f:
            return f.read()
    return ""

