import json
import pathlib

STATE_PATH = pathlib.Path("output/state.json")

# Lista base de misterios declarados en el lore
MYSTERIES = [
    "How did Belial obtain Thaeriel's weapon?",
    "Who truly forged the ancestral weapons?",
    "Why do some humans reincarnate faster than others?",
    "What lies beyond the cycle? Who designed it?",
    "What role does Ereloth play in all of this?",
    "Who placed seals on the Tower of the Eternals?",
]



def _load():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"mysteries": []}


def _save(data):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(data, indent=2))


def track_mysteries(chapter_text: str, chapter_no: int):
    data = _load()
    tracked = data.get("mysteries", [])

    updated = False
    for mystery in MYSTERIES:
        entry = next((m for m in tracked if m["text"] == mystery), None)

        if not entry:
            # Aún no ha sido registrado
            if mystery[:12].lower() in chapter_text.lower():  # Búsqueda ligera
                tracked.append({
                    "text": mystery,
                    "seeded": chapter_no,
                    "resolved": None
                })
                updated = True
        else:
            if entry["resolved"] is None and "respuesta" in chapter_text.lower() and mystery[
                                                                                     :12].lower() in chapter_text.lower():
                entry["resolved"] = chapter_no
                updated = True

    if updated:
        data["mysteries"] = tracked
        _save(data)

    return tracked
