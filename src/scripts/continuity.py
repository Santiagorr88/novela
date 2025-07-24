import json, re, pathlib

STATE = pathlib.Path("output/state.json")

def _load_state(path=STATE):
    if path.exists():
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    data.setdefault("characters", {})
    data.setdefault("weapons", {})
    data.setdefault("locations", {})
    return data

def check(chapter_text: str, chapter_no: int, state_path: str = None):
    path = pathlib.Path(state_path) if state_path else STATE
    state = _load_state(path)
    issues = []

    # 1) Verifica personajes muertos que no deberían actuar
    for name, info in state.get("characters", {}).items():
        if info.get("status") == "dead":
            if re.search(rf"\b{name}\b.*\b(said|spoke|walked|smiled|attacked|responded)\b", chapter_text, flags=re.IGNORECASE):
                issues.append(f"{name} is DEAD but appears active or speaking.")

    # 2) Verifica armas en manos incorrectas (simplificado)
    for weapon, owner in state.get("weapons", {}).items():
        if owner:
            matches = re.findall(rf"\b{weapon}\b.*?\b([A-Z][a-z]+)\b", chapter_text)
            for holder in matches:
                if holder != owner:
                    if holder in state.get("characters", {}):
                        issues.append(f"{weapon} belongs to {owner} but seems with {holder}.")

    return "PASS" if not issues else "FIX:\n" + "\n".join(f"- {i}" for i in issues)
