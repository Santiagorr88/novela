
def write_chapter_recap(chapter_no: int, full_text: str, summary: str):
    """Guarda el resumen en un archivo para memoria progresiva."""
    chapter_no = int(chapter_no)  # ✅ Cast seguro
    recap_path = f"src/chapters/recap/B1C{chapter_no:02d}_recap.md"
    with open(recap_path, "w") as f:
        f.write(summary)

def append_to_full_recap(chapter_no, recap_text):
    """Agrega el recap actual al archivo full_recap.md."""
    path = "src/chapters/recap/full_recap.md"
    header = f"\n\n---\n\n# B1C{int(chapter_no):02d} Recap\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(header + recap_text.strip() + "\n")