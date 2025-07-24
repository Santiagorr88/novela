def make_filename(folder: str, chapter: int, slug: str = "", lang: str = "EN") -> str:
    import os
    filename = f"cap_{int(chapter):03d}_{lang}.pdf"
    return os.path.join(folder, filename)