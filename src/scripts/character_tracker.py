import json, pathlib

STATE = pathlib.Path("output/state.json")

def _load():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"characters": {}}

def _save(data):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(data, indent=2))

def register_character(name: str):
    data = _load()
    if name not in data["characters"]:
        data["characters"][name] = {
            "status": "alive",
            "reincarnated_as": None,
            "revealed": False,
            "revealed_in": None,
            "known_by": []
        }
        _save(data)

def mark_death(name: str):
    data = _load()
    data.setdefault("characters", {})
    if name not in data["characters"]:
        register_character(name)
    data["characters"][name]["status"] = "dead"
    _save(data)

def register_reincarnation(former: str, new_identity: str):
    data = _load()
    data.setdefault("characters", {})

    # Asegura que ambos existan
    if former not in data["characters"]:
        data["characters"][former] = {}

    data["characters"][former]["status"] = "reincarnated"
    data["characters"][former]["reincarnated_as"] = new_identity

    data["characters"][new_identity] = {
        "status": "alive",
        "true_identity": former,
        "revealed": False,
        "revealed_in": None,
        "known_by": []
    }

    _save(data)

def reveal_identity(character: str, chapter_no: int):
    data = _load()
    if character not in data["characters"]:
        register_character(character)

    data["characters"][character]["revealed"] = True
    data["characters"][character]["revealed_in"] = chapter_no
    _save(data)

def mark_knowledge(holder: str, knows_about: str):
    data = _load()
    if knows_about not in data["characters"]:
        register_character(knows_about)

    data["characters"][knows_about].setdefault("known_by", [])
    if holder not in data["characters"][knows_about]["known_by"]:
        data["characters"][knows_about]["known_by"].append(holder)

    _save(data)

def get_character_state(name: str) -> dict:
    data = _load()
    return data["characters"].get(name, {})

def list_known_characters() -> list:
    data = _load()
    return list(data["characters"].keys())

def update_from_events(events: list, chapter_no: int):
    data = _load()
    data.setdefault("characters", {})  # Asegura estructura

    for event in events:
        if not isinstance(event, dict):
            continue  # Ignora basura
        t = event.get("type")
        if not t:
            continue

        # Muerte
        if t == "death":
            char = event.get("character")
            if char:
                mark_death(char)

        # Reencarnación o resurrección
        elif t in ("reincarnation", "resurrection"):
            former = event.get("former")
            new_identity = event.get("new_identity")
            if former and new_identity:
                register_reincarnation(former, new_identity)

        # Revelación de identidad
        elif t == "reveal":
            truth = event.get("truth")
            if truth and truth in data["characters"]:
                reveal_identity(truth, chapter_no)

        # Sabiduría compartida (opcional, se puede extender)
        elif t == "knowledge" and "holder" in event and "known" in event:
            mark_knowledge(event["holder"], event["known"])

    _save(data)

def character_report() -> str:
    data = _load()
    report = []

    if "characters" in data:
        report.append("🧍 Character Status:\n")
        for name, info in data["characters"].items():
            line = f"- {name}: {info.get('status', 'unknown')}"
            if "true_identity" in info:
                line += f" (true identity: {info['true_identity']})"
            if info.get("revealed"):
                line += f" [REVEALED in B1C{info.get('revealed_in', '?'):02d}]"
            report.append(line)

    return "\n".join(report) if report else "No characters registered yet."
