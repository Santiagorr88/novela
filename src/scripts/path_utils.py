# src/scripts/path_utils.py
import unicodedata
import re
import pathlib
import os
from .title_utils import slugify
from pathlib import Path

def build_filename_with_chapter_folder(
    saga_title: str,
    lang: str,
    book_number: int | str,
    chapter_number: int | str,
    chapter_title: str,
) -> str:
    """
    Devuelve la ruta PDF como:
    project/{saga_title}/{lang}/B1C01_The_Tree_Outside_Time/B1C01P1_A_Wound_in_the_World.pdf
    """

    # 🔧 Asegura que son enteros antes de formatear
    book_number = int(book_number)
    chapter_number = int(chapter_number)

    chapter_id = f"B{book_number}C{chapter_number:02d}"

    safe_chapter_title = slugify(chapter_title).replace("-", "_").title().replace("_", " ")

    folder = f"{chapter_id}"
    filename = f"{safe_chapter_title.replace(' ', '_')}.pdf"

    return os.path.join("project", saga_title, lang, folder, filename)



def h1_to_filename(folder: str, h1_line: str, lang: str) -> str:
    """
    Convierte '# B1C6 – My Title' -> 'B1C6_My_Title_EN.pdf'
    """
    # Extrae H1 sin el '#' y lo limpia
    raw = h1_line.lstrip("#").strip()

    # Normaliza separador: "B1C6 – My Title" => ["B1C6", "My Title"]
    parts = re.split(r"\s[-–:]\s", raw, maxsplit=1)
    if len(parts) == 2:
        prefix, title = parts
    else:
        # fallback si no hay separador
        prefix = raw.split()[0]
        title = " ".join(raw.split()[1:])

    # Quitar acentos, mantener nombre seguro
    title_clean = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    title_safe = title_clean.strip().replace(" ", "_")

    full_name = f"{prefix}_{title_safe}_{lang.upper()}.pdf"
    path = pathlib.Path(folder) / lang.lower()
    path.mkdir(parents=True, exist_ok=True)
    return str(path / full_name)


def build_filename_h1_style(folder: str, prefix: str, title: str, lang: str) -> str:

    title_clean = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    safe_title = re.sub(r"[^a-zA-Z0-9]+", "_", title_clean).strip("_")

    path = pathlib.Path(folder) / lang.lower()
    path.mkdir(parents=True, exist_ok=True)

    filename = f"{prefix}_{safe_title}_{lang.upper()}.pdf"
    return str(path / filename)

def sanitize_filename(text):
    """Quita caracteres no válidos para nombres de archivo."""
    return re.sub(r"[^\w\d\-_. ]+", "", text).strip().replace(" ", "_")

def build_filename_nested(saga_title, lang, book_number, chapter_number, chapter_title,
                          part_number=None, part_title=None, is_full_chapter=False):
    """
    Construye una ruta de archivo con la estructura:
    project/<saga_title>/<lang>/B{book}C{chapter}_{chapter_title}/
        - B{book}C{chapter}_{chapter_title}.pdf (si es capítulo completo)
        - B{book}C{chapter}P{part}_{part_title}.pdf (si es una parte narrativa)
    """
    # Normaliza nombres
    saga_folder = sanitize_filename(saga_title)
    chapter_folder = f"B{book_number}C{chapter_number}_{sanitize_filename(chapter_title)}"

    # Define el nombre de archivo
    if is_full_chapter:
        filename = f"B{book_number}C{chapter_number}_{sanitize_filename(chapter_title)}.pdf"
    else:
        filename = (
            f"B{book_number}C{chapter_number}P{part_number}_{sanitize_filename(part_title)}.pdf"
        )

    # Ruta completa
    return os.path.join(
        "project",
        saga_folder,
        lang.upper(),  # EN o ES
        chapter_folder,
        filename
    )
