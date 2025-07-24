import os

def write_chapter_recap(chapter_no: int, full_text: str, summary: str):
    """Guarda el resumen en un archivo para memoria progresiva."""
    recap_path = f"src/chapters/recap/B1C{chapter_no:02d}_recap.md"
    with open(recap_path, "w") as f:
        f.write(summary)