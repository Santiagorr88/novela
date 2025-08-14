import re
from pathlib import Path


def merge_lore(lore_prompt: str, lore_arco: str) -> str:
    return lore_prompt + "\n\n---\n\n" + lore_arco



def get_parts_for_chapter(chapter_no: int, arco_data: str) -> int:

    chapter_tag = f"B1C{int(chapter_no):02d}"
    pattern = rf"###\s+\*\*{chapter_tag}:\s.*?\*\*\n(.*?)(?=\n###|\Z)"
    match = re.search(pattern, arco_data, re.DOTALL)

    if not match:
        raise ValueError(f"No se encontró el capítulo {chapter_tag} en el arco argumental.")

    chapter_block = match.group(1)

    # Busca dentro de 'Narrative Parts' líneas como: 1.  **Título**
    part_matches = re.findall(r"\n\s*[\*\-]?\s*\d+\.\s+\*\*", chapter_block)
    return len(part_matches)


def get_part_titles_for_chapter(chapter_no: int, arco_data: str, book_number) -> list[str]:
    """
    Extrae los títulos de las partes narrativas SOLO del capítulo B1Cxx.
    Robustez:
      - Delimita por encabezados de capítulo: ^#{3,6} **B1Cxx:
      - No depende de líneas en blanco entre capítulos
      - Tolera títulos con/sin **negrita** y con/sin ':' final
    """

    chapter_id = f"B{book_number}C{int(chapter_no):02d}"

    # 1) Localizar el inicio EXACTO del capítulo (###/####, con **...**)
    start_pat = rf"(?m)^[#]{{3,6}}\s+\*\*{chapter_id}:[^\n]*$"
    start_m = re.search(start_pat, arco_data)
    if not start_m:
        raise ValueError(f"No se encontró el capítulo {chapter_id} en el arco argumental.")

    start = start_m.end()

    # 2) Encontrar el SIGUIENTE capítulo para cortar el bloque
    next_pat = r"(?m)^[#]{3,6}\s+\*\*B1C\d{2}:[^\n]*$"
    next_m = re.search(next_pat, arco_data[start:])
    end = start + next_m.start() if next_m else len(arco_data)

    block = arco_data[start:end]

    # 3) Dentro del bloque, extraer SOLO los ítems numerados (1. **Título** / 1. Título)
    #    Primero intentamos con negrita:
    titles = [m.group(1).strip() for m in re.finditer(r"(?m)^\s*\d+\.\s+\*\*(.+?)\*\*", block)]
    #    Fallback sin negrita si no encuentra nada:
    if not titles:
        titles = [m.group(1).strip() for m in re.finditer(r"(?m)^\s*\d+\.\s+(.+?)\s*(?:$|\r?$)", block)]

    # 4) Normalizar: quitar ':' final si viene dentro del **título:**
    titles = [re.sub(r":\s*$", "", t) for t in titles]

    if not titles:
        raise ValueError(f"No se encontraron partes narrativas para el capítulo {chapter_id}.")

    return titles


def get_chapter_title(chapter_no: int, arco_data: str) -> str:
    """
    Extrae el título del capítulo (ej: 'The Tree Outside Time') dado el número y el contenido del arco.
    """
    tag = f"B1C{int(chapter_no):02d}"
    pattern = rf"###+\s+\*\*{tag}:\s*(.*?)\*\*"
    match = re.search(pattern, arco_data)
    if not match:
        raise ValueError(f"No se encontró el título para {tag} en el arco argumental.")
    return match.group(1).strip()

