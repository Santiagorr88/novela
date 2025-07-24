# src/scripts/run_flow.py
import sys
import os
import yaml
from jinja2 import Template, StrictUndefined
from src.flow_engine import run_node
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def load_flow(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def jinja_render(val, ctx):
    if isinstance(val, str) and "{{" in val and "}}" in val:
        return Template(val, undefined=StrictUndefined).render(**ctx)
    return val

def should_run(node, ctx):
    expr = node.get("when")
    if expr is None:
        return True
    try:
        rendered = Template(expr, undefined=StrictUndefined).render(**ctx)
        return bool(eval(str(rendered)))
    except Exception:
        return False

def run_flow(flow_def, context):
    # variables globales disponibles
    vars_dict = flow_def.get("variables", {}) or {}
    context.update(vars_dict)
    context["variables"] = vars_dict

    flow = flow_def.get("flow", [])
    if not flow:
        print("⚠️  No se encontraron nodos en el flujo.")
        return

    for raw_node in flow:
        if not should_run(raw_node, context):
            continue

        # Clonamos el nodo y resolvemos Jinja en inputs/args simples
        node = dict(raw_node)
        for field in ("inputs", "args"):
            if field in node:
                rendered = {}
                for k, v in node[field].items():
                    rendered[k] = jinja_render(v, context)
                node[field] = rendered

        print(f"→ Ejecutando nodo: {node['id']} ({node['type']})")
        try:
            if node["type"] == "python":
                if "module" not in node or "function" not in node:
                    raise ValueError(f"El nodo '{node['id']}' debe tener 'module' y 'function'")
            result = run_node(node, context)
            context[node["id"]] = result
            print(f"✔ Resultado de '{node['id']}':\n{result}\n")
        except Exception as e:
            print(f"❌ Error en nodo '{node['id']}': {e}")
            break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python -m src.scripts.run_flow src/flow.yml \"Texto opcional\"")
        sys.exit(1)

    flow_file = sys.argv[1]
    user_input = sys.argv[2] if len(sys.argv) > 2 else ""

    flow_def = load_flow(flow_file)
    context = {"input": user_input}
    run_flow(flow_def, context)
