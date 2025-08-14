# src/scripts/chapter_splitter.py

def split_and_cache(chapter_id, chapter_no, parts_titles, narrator_text):
    """
    Simula división y guardado de partes de un capítulo.
    Retorna un dict con la estructura esperada por el flow.
    """
    return {
        "count": len(parts_titles),
        "parts": [
            {
                "index": i + 1,
                "title": title,
                "path": f"src/plan_cache/{chapter_id}P{i+1:02d}_texto.md",
                "word_count": len(narrator_text.split())
            }
            for i, title in enumerate(parts_titles)
        ]
    }