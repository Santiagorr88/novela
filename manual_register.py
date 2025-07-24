import argparse
import os
from pathlib import Path
from src.scripts.timeline import check_and_update, update_state_from_events
from src.scripts.theme_manager import register_themes
from src.scripts.memory_io import append_chapter
from src.scripts.lore_diff_tracker import check_lore_conflicts
from src.scripts.character_tracker import update_from_events
from src.scripts.mystery_tracker import track_mysteries

def read_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def detect_final_chapter(book, chapter):
    return (book == 1 and chapter == 28)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Ruta al archivo .md")
    parser.add_argument("--chapter", type=int, help="Número de capítulo (alias)")
    parser.add_argument("--chapter_no", type=int, help="Número de capítulo")
    parser.add_argument("--book", "--book_no", type=int, default=1, help="Número de libro (default: 1)")
    parser.add_argument("--inmutable", action="store_true", help="Evita sobrescribir elementos editables")
    parser.add_argument("--final_chapter", action="store_true", help="Marca este capítulo como el final canon (B1C28)")

    args = parser.parse_args()
    chapter_no = args.chapter or args.chapter_no
    book_no = args.book
    is_final = detect_final_chapter(book_no, chapter_no) or args.final_chapter
    is_inmutable = args.inmutable or is_final

    print(f"📘 Registrando capítulo B{book_no}C{chapter_no:02d}")
    if is_final:
        print("⚠️ Capítulo marcado como FINAL (B1C28) – modo inmutable activado.")

    text = read_markdown(args.file)

    # Eventos → estado
    print("📌 Actualizando timeline...")
    update_state_from_events(events=[], chapter_no=chapter_no)  # Requiere extractor previo si lo usas

    # Estado global (por texto completo)
    check_and_update(text, chapter_no)

    # Temas
    print("🧭 Registrando temas...")
    register_themes(chapter_no=chapter_no, themes=["auto", "detect"])

    # Misterios
    print("🕵️‍♂️ Registrando misterios...")
    track_mysteries(chapter_text=text, chapter_no=chapter_no)

    # Memoria narrativa (si no es final)
    if not is_inmutable:
        print("🧠 Guardando en memoria narrativa...")
        append_chapter(text, text_es="")  # Puedes traducir luego

    # Personajes
    print("🧬 Actualizando estado de personajes...")
    update_from_events(events=[], chapter_no=chapter_no)  # Similar: necesita eventos extraídos

    print("✅ Registro completo.")
