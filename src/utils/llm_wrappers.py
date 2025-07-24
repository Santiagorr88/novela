# src/utils/llm_wrappers.py
import google.generativeai as genai
import json
from pathlib import Path

secrets_path = Path(__file__).parents[1] / "secrets.json"
secrets = json.loads(secrets_path.read_text())
genai.configure(api_key=secrets["google_api_key"])

def _extract_text(resp):
    out = []
    if getattr(resp, "candidates", None):
        for c in resp.candidates:
            content = getattr(c, "content", None)
            if content and getattr(content, "parts", None):
                for p in content.parts:
                    if hasattr(p, "text"):
                        out.append(p.text)
    return "\n".join(out).strip()

def run_llm_gemini(model, system_prompt, user_input="", temperature=0.7, **model_kwargs):
    model_map = {
        "gemini-2.5-pro":   "models/gemini-2.5-pro",
        "gemini-2.5-flash": "models/gemini-2.5-flash",
    }
    mapped = model_map.get(model)
    if not mapped:
        raise ValueError(f"Unknown model '{model}'")

    if isinstance(user_input, dict):
        user_input = "\n\n".join(f"{k}:\n{v}" for k, v in user_input.items())

    prompt = f"{system_prompt.strip()}\n\n{user_input.strip()}"

    gen_conf = {"temperature": temperature}
    gen_conf.update(model_kwargs or {})

    gmodel = genai.GenerativeModel(mapped)

    text_chunks = []
    resp = gmodel.generate_content(
        [{"role": "user", "parts": [prompt]}],
        generation_config=gen_conf,
        safety_settings=model_kwargs.get("safety_settings"),
    )
    text_chunks.append(_extract_text(resp))
    finish = getattr(resp.candidates[0], "finish_reason", None) if resp.candidates else None

    while finish == 2:  # MAX_TOKENS
        tail = text_chunks[-1][-400:]
        cont_prompt = (
            "Continue EXACTLY from where you stopped. Do NOT repeat text. "
            "Start immediately after this fragment:\n```" + tail + "```"
        )
        resp = gmodel.generate_content(
            [{"role": "user", "parts": [cont_prompt]}],
            generation_config=gen_conf,
            safety_settings=model_kwargs.get("safety_settings"),
        )
        chunk = _extract_text(resp)
        if not chunk:
            break
        text_chunks.append(chunk)
        finish = getattr(resp.candidates[0], "finish_reason", None) if resp.candidates else None

    return "\n".join(text_chunks).strip()
