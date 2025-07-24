import json
from pathlib import Path

STATE_PATH = Path("output/state.json")

def _load():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"themes": []}

def _save(data):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(data, indent=2))

def register_themes(chapter_no: int, themes: list[str]):
    data = _load()
    # Remueve entrada previa si existe
    data["themes"] = [t for t in data.get("themes", []) if t["chapter"] != chapter_no]
    # Añade nuevo registro
    data["themes"].append({
        "chapter": chapter_no,
        "themes": themes
    })
    _save(data)

def get_theme_report() -> str:
    data = _load()
    theme_count = {}
    for entry in data.get("themes", []):
        for theme in entry["themes"]:
            theme_count[theme] = theme_count.get(theme, 0) + 1
    lines = [f"- {k}: {v} capítulos" for k, v in sorted(theme_count.items(), key=lambda x: -x[1])]
    return "🧭 Distribución temática:\n\n" + "\n".join(lines) if lines else "No hay temas registrados aún."
