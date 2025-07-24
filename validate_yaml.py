import yaml

file = "flow.yml"
try:
    with open(file, "r") as f:
        yaml.safe_load(f)
    print("✅ YAML válido")
except yaml.YAMLError as e:
    print("❌ Error en YAML:")
    print(e)
    with open(file) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            print(f"{i+1:3}: {line.rstrip()}")
