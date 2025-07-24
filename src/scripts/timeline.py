import json, re, pathlib, datetime

STATE = pathlib.Path("output/state.json")

def _load():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {
        "timeline": [],
        "last_date": None,
        "deaths": [],
        "weapons": {},
        "revealed_truths": [],
        "resurrections": []
    }
def _save(data):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(data, indent=2))

# Very naive date parser, expand later
DATE_PATTERNS = [
    r"(\d{4})\s*AD",              # 2027 AD
    r"Year\s+(\d+)",              # Year 43
    r"Décadas después",           # Spanish marker
    r"Decades later",             # English marker
    r"Months later", r"Years later", r"Days later"
]

def check_and_update(chapter_text: str, chapter_no: int = None):
    data = _load()
    issues = []

    # Detect explicit “time skip” markers
    detected = []
    for pat in DATE_PATTERNS:
        for m in re.finditer(pat, chapter_text, flags=re.IGNORECASE):
            detected.append(m.group(0))

    last_date = data.get("last_date")  # << Asegura acceso seguro

    # Simple temporal logic rule example
    if last_date and "before" in chapter_text.lower():
        issues.append("Chapter may go backwards in time based on 'before' and existing date.")

    # Save raw markers
    if detected:
        data["timeline"].append({
            "chapter": chapter_no,
            "chapter_snippet": chapter_text[:160],
            "markers": detected
        })

    _save(data)
    return "PASS" if not issues else "FIX:\n" + "\n".join(f"- {i}" for i in issues)

def register_death(character_name: str, chapter_no: int):
    data = _load()
    data.setdefault("deaths", [])
    data["deaths"].append({"name": character_name, "chapter": chapter_no})
    _save(data)

def update_weapon_status(weapon_name: str, new_owner: str, status: str):
    data = _load()
    if "weapons" not in data:
        data["weapons"] = {}
    data["weapons"][weapon_name] = {
        "owner": new_owner,
        "status": status
    }
    _save(data)

def reveal_truth(truth_label: str, chapter_no: int):
    data = _load()
    data.setdefault("revealed_truths", [])
    data["revealed_truths"].append({"truth": truth_label, "chapter": chapter_no})
    _save(data)

def log_resurrection(character_name: str, as_identity: str, chapter_no: int):
    data = _load()
    data.setdefault("resurrections", [])
    data["resurrections"].append({
        "former_identity": character_name,
        "new_identity": as_identity,
        "chapter": chapter_no
    })
    _save(data)

def get_state_snapshot() -> str:
    data = _load()
    snapshot = []

    if data["deaths"]:
        snapshot.append("📍 Deaths:\n" + "\n".join(f"- {d['name']} (B1C{d['chapter']:02d})" for d in data["deaths"]))
    if data["weapons"]:
        snapshot.append("⚔️ Weapons:\n" + "\n".join(f"- {k}: {v['owner']} ({v['status']})" for k, v in data["weapons"].items()))
    if data["revealed_truths"]:
        snapshot.append("🔍 Revealed Truths:\n" + "\n".join(f"- {r['truth']} (B1C{r['chapter']:02d})" for r in data["revealed_truths"]))
    if data["resurrections"]:
        snapshot.append("♻️ Resurrections:\n" + "\n".join(f"- {r['former_identity']} → {r['new_identity']} (B1C{r['chapter']:02d})" for r in data["resurrections"]))

    return "\n\n".join(snapshot) or "No major events logged yet."


def update_state_from_events(events, chapter_no: int):
    data = _load()

    # 🔍 Si es string (viene como texto con bloque markdown)
    if isinstance(events, str):
        clean = re.sub(r"^```json|```$", "", events.strip(), flags=re.MULTILINE).strip()
        try:
            events = json.loads(clean)
        except json.JSONDecodeError as e:
            raise ValueError(f"❌ Error al decodificar JSON: {e}")

    # 🛡️ Validación básica
    if not isinstance(events, list):
        raise ValueError("❌ 'events' no es una lista de eventos.")

    for evt in events:
        t = evt.get("type")

        if t == "death":
            data.setdefault("deaths", [])
            data["deaths"].append({
                "name": evt["character"],
                "chapter": chapter_no,
                "cause": evt.get("cause", None)
            })

        elif t == "resurrection":
            data.setdefault("resurrections", [])
            data["resurrections"].append({
                "former_identity": evt["former"],
                "new_identity": evt["new_identity"],
                "chapter": chapter_no
            })

        elif t == "weapon_update":
            data.setdefault("weapons", {})
            data["weapons"][evt["weapon"]] = {
                "owner": evt["owner"],
                "status": evt["status"],
                "chapter": chapter_no
            }

        elif t == "reveal":
            data.setdefault("revealed_truths", [])
            data["revealed_truths"].append({
                "truth": evt["truth"],
                "chapter": chapter_no
            })

        elif t == "prophecy_discovery":
            data.setdefault("prophecies", [])
            data["prophecies"].append({
                "character": evt["character"],
                "fragment": evt["prophecy_fragment"],
                "chapter": chapter_no
            })

        elif t == "reincarnation":
            data.setdefault("reincarnations", [])
            data["reincarnations"].append({
                "former": evt["former"],
                "new_identity": evt["new_identity"],
                "chapter": chapter_no
            })

        elif t == "leadership_change":
            data.setdefault("leadership_changes", [])
            data["leadership_changes"].append({
                "character": evt["character"],
                "new_role": evt["new_role"],
                "chapter": chapter_no
            })

        elif t == "strategic_retreat":
            data.setdefault("retreats", [])
            data["retreats"].append({
                "faction": evt["faction"],
                "destination": evt["destination"],
                "chapter": chapter_no
            })

        elif t == "new_objective":
            data.setdefault("objectives", [])
            data["objectives"].append({
                "character": evt["character"],
                "objective": evt["objective"],
                "chapter": chapter_no
            })

        elif t == "battle":
            data.setdefault("battles", [])
            data["battles"].append({
                "name": evt["name"],
                "outcome": evt["outcome"],
                "chapter": chapter_no
            })

        elif t == "combat_action":
            data.setdefault("combat_actions", [])
            data["combat_actions"].append({
                "character": evt["character"],
                "action": evt["action"],
                "outcome": evt.get("outcome", None),
                "chapter": chapter_no
            })

        else:
            raise ValueError(f"❌ Tipo de evento no reconocido: {t}")

    _save(data)

