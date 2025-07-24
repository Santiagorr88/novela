# src/flow_engine.py
import importlib
from pathlib import Path
from src.utils.llm_wrappers import run_llm_gemini
from jinja2 import Template, StrictUndefined

def run_node(node, context):
    node_type = node["type"]
    inputs = resolve_inputs(node.get("inputs", {}), context)

    # merge defaults
    for key in ["model", "temperature", "system_prompt_path"]:
        if key in node and key not in inputs:
            inputs[key] = node[key]

    if node_type == "llm":
        # --- Cargar prompt ---
        if "system_prompt_path" in inputs:
            inputs["system_prompt"] = Path(inputs["system_prompt_path"]).read_text()
            inputs.pop("system_prompt_path", None)   # que no viaje al user_input

        model        = inputs.pop("model")
        temperature  = inputs.pop("temperature", 0.7)
        system_prompt= inputs.pop("system_prompt", "")

        # kwargs de generación (tokens, top_p, etc.)
        model_kwargs = node.get("model_kwargs", {})

        # lo que queda en inputs => user_input
        return run_llm_gemini(
            model=model,
            system_prompt=system_prompt,
            user_input=inputs,
            temperature=temperature,
            **model_kwargs
        )

    elif node_type == "file_loader":
        with open(inputs["path"], "r", encoding="utf-8") as f:
            return f.read()

    elif node_type == "python":

        module_name = node["module"]

        func_name = node["function"]

        module = importlib.import_module(module_name)

        func = getattr(module, func_name)

        if "args" in node:
            return func(**node["args"])
        else:
            return func(**inputs)


    elif node_type == "router":
        condition = inputs.get("condition")
        if isinstance(condition, str):
            try:
                return eval(condition, {}, context)
            except Exception as e:
                raise ValueError(f"❌ Error al evaluar condición del router: {condition}\n{e}")
        return bool(condition)

    elif node_type == "passthrough":
        return inputs.get("content") or inputs.get("value")

    else:
        raise ValueError(f"❌ Tipo de nodo no soportado: {node_type}")

def resolve_inputs(inputs, context):
    resolved = {}
    for k, v in inputs.items():
        if isinstance(v, str) and v.strip().startswith("{{") and v.strip().endswith("}}"):
            try:
                tmpl = Template(v, undefined=StrictUndefined)
                resolved[k] = tmpl.render(**context)
            except Exception as e:
                raise KeyError(f"🔑 Error al procesar expresión '{v}': {e}")
        else:
            resolved[k] = v
    return resolved
