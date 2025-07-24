import json
import pathlib
import re

STATE_PATH = pathlib.Path("output/state.json")
PROPHECY_LINES = [
    "Three were forged of light before time began",
    "One shall fall silent and become the beacon",
    "unless doubt extinguish it",
    "One shall judge and bring order",
    "or kindle the eternal fire",
    "One shall laugh",
    "and if he loves nothing, the world will burn for his void",
    "if the three awaken, he shall awaken as well"
]

def _load():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"prophecy_mentions": []}

def _save(data):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(data, indent=2))

def check_prophecy_mentions(chapter_text: str, chapter_no: int):
    """Detecta si se menciona alguna línea de la profecía"""
    data = _load()
    mentions = []

    for line in PROPHECY_LINES:
        pattern = re.escape(line[:25])  # Solo detectamos fragmentos para evitar falsos negativos
        if re.search(pattern, chapter_text, flags=re.IGNORECASE):
            entry = {
                "line": line,
                "chapter": chapter_no,
                "mode": "hint" if "..." in line else "full"
            }
            mentions.append(entry)

    if mentions:
        data.setdefault("prophecy_mentions", []).extend(mentions)
        _save(data)

    return mentions
