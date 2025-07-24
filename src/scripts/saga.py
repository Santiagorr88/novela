import argparse
import pathlib
from src.scripts import saga_tools


def plan_chapter(book_no: int, chapter_no: int):
    print("\n🧠 Generando planificación del capítulo...\n")
    plan = saga_tools.generate_plan(chapter_no)
    print(plan)

def write_chapter(book_no: int, chapter_no: int):
    plan = saga_tools.generate_plan(chapter_no)
    print("\n📌 Plan generado:\n")
    print(plan)

    plan_input = input("\n✏️ ¿Quieres modificar el plan antes de generar el capítulo? (s/n): ")
    if plan_input.strip().lower() == "s":
        plan = input("\n👉 Pega el plan modificado:\n")

    print("\n✍️ Escribiendo capítulo...\n")
    text = saga_tools.generate_chapter(chapter_no, plan)
    print(text)

def translate_chapter(chapter_path: str):
    markdown = pathlib.Path(chapter_path).read_text()
    print("\n🌐 Traduciendo capítulo...\n")
    translated = saga_tools.translate_english_to_spanish(markdown)
    print(translated)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Orquestador manual para pruebas parciales.")
    parser.add_argument("--plan", action="store_true", help="Generar beat plan del capítulo.")
    parser.add_argument("--write", action="store_true", help="Escribir capítulo completo.")
    parser.add_argument("--translate", type=str, help="Traducir capítulo markdown dado (ruta).")
    parser.add_argument("--book", type=int, default=1, help="Número de libro.")
    parser.add_argument("--chapter", type=int, help="Número de capítulo.")

    args = parser.parse_args()

    if args.plan and args.chapter:
        plan_chapter(args.book, args.chapter)
    elif args.write and args.chapter:
        write_chapter(args.book, args.chapter)
    elif args.translate:
        translate_chapter(args.translate)
    else:
        parser.print_help()
