# src/scripts/path_utils.py
import os
from .title_utils import slugify


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
