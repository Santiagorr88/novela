# src/scripts/titler.py

import re

def ensure_title(title_line: str, chapter_text: str) -> str:
    """
    Inserts a single H1 title at the top of the chapter, stripping any existing chapter headings.
    Removes only the original chapter H1 lines (e.g., "# B1C1 – ...") and preserves other subheadings.
    """
    # Regex to match previous chapter headings (full line), e.g., "# B1C1 – Some Title"
    chapter_heading_pattern = re.compile(r"^\s*#\s*B\d+C\d+\s*[-–:].*$", re.IGNORECASE)

    lines = chapter_text.splitlines()
    # Filter out any lines that match the chapter heading pattern
    body_lines = [l for l in lines if not chapter_heading_pattern.match(l)]

    # Build output: new title + blank line + filtered body
    output = [title_line]
    if body_lines and body_lines[0].strip() != "":
        output.append("")
    output.extend(body_lines)

    return "\n".join(output)


def build_title_line(prefix: str, title: str) -> str:
    """
    Devuelve una línea de título estilo: "# B1C6 – Título del capítulo"
    """
    return f"# {prefix} – {title}"
