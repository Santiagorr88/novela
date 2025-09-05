import re
from pathlib import Path
from typing import List


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


def get_part_titles_for_chapter(chapter_no: int, arco_data: str, book_number: int) -> List[str]:
    """
    Devuelve los títulos de partes para el capítulo B{book}C{n}.
    - Si existen partes numeradas (1. **Título** / 1. Título), las devuelve.
    - Si NO existen (capítulo atómico), devuelve [título_del_capítulo].
    Robustez:
      - Acepta B{book}C0*{n} (1–3 dígitos) y evita falsos positivos (lookahead negativo).
      - Encabezados ###–###### con o sin cierre ** al final.
      - Siguiente capítulo del MISMO libro para delimitar el bloque.
    """
    chap_num = int(chapter_no)

    # 1) Localizar encabezado exacto del capítulo
    header_pat = rf"(?m)^[#]{{3,6}}\s+\*\*B{book_number}C0*{chap_num}(?!\d):\s*(.+?)\s*\*\*\s*$"
    header_m = re.search(header_pat, arco_data)
    if not header_m:
        # tolerar falta de ** de cierre
        header_pat_fallback = rf"(?m)^[#]{{3,6}}\s+\*\*B{book_number}C0*{chap_num}(?!\d):\s*(.+?)\s*$"
        header_m = re.search(header_pat_fallback, arco_data)
    if not header_m:
        raise ValueError(f"No se encontró el capítulo B{book_number}C{chap_num} (con o sin ceros) en el arco.")

    chapter_title = header_m.group(1).strip()
    start = header_m.end()

    # 2) Delimitar bloque hasta el siguiente capítulo del MISMO libro (cualquier longitud de dígitos)
    next_pat = rf"(?m)^[#]{{3,6}}\s+\*\*B{book_number}C\d+:[^\n]*$"
    next_m = re.search(next_pat, arco_data[start:])
    end = start + next_m.start() if next_m else len(arco_data)
    block = arco_data[start:end]

    # 3) Intentar extraer partes numeradas dentro del bloque
    titles = [m.group(1).strip() for m in re.finditer(r"(?m)^\s*\d+\.\s+\*\*(.+?)\*\*", block)]
    if not titles:
        titles = [m.group(1).strip() for m in re.finditer(r"(?m)^\s*\d+\.\s+(.+?)\s*(?:$|\r?$)", block)]

    # 4) Normalizar ':' final
    titles = [re.sub(r":\s*$", "", t) for t in titles]

    # 5) Si no hay partes, devolver el título del capítulo como única parte
    if not titles:
        if chapter_title:
            return [re.sub(r":\s*$", "", chapter_title)]
        return ["Full Chapter"]

    return titles

def get_chapter_title(chapter_no: int, arco_data: str, book_number: int = 1) -> str:
    """
    Devuelve el título del capítulo B{book_number}C{chapter_no} (tolerando 1–3 ceros a la izquierda),
    encabezados ###–###### y presencia/ausencia del cierre **.
    """
    chap_num = int(chapter_no)

    # Patrón principal: línea de encabezado con ** al final
    pat_main = rf"(?m)^[#]{{3,6}}\s+\*\*B{book_number}C0*{chap_num}(?!\d):\s*(.*?)\s*\*\*\s*$"
    m = re.search(pat_main, arco_data)
    if not m:
        # Fallback: sin cierre ** al final
        pat_fb = rf"(?m)^[#]{{3,6}}\s+\*\*B{book_number}C0*{chap_num}(?!\d):\s*(.*?)\s*$"
        m = re.search(pat_fb, arco_data)

    if not m:
        raise ValueError(f"No se encontró el título para B{book_number}C{chap_num} (con o sin ceros) en el arco.")

    title = m.group(1).strip()
    # Limpieza mínima por si quedara ':' final o espacios raros
    title = re.sub(r":\s*$", "", title)
    return title

