# launch_flow.py
from src.scripts.run_flow import run_flow, load_flow
import sys
import os

# Agrega /home/sszark/Escritorio/src/deer-flow/src al path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_PATH)
if __name__ == "__main__":
    with open("src/lore/prompt_universo.md", "r") as f:
        lore_validated_text = f.read()
    # Path to your flow YAML
    flow_file = "flow.yml"
    # Optionally pass an input prompt; empty for default behavior
    user_input = ""
    # Load and execute
    flow_def = load_flow(flow_file)
    run_flow(flow_def, {
        "input": user_input,
        "lore_validated_text": lore_validated_text
    })