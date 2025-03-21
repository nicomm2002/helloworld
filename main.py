import json
import subprocess

# Cargar config.json
with open('config.json') as f:
    config = json.load(f)

print("my path to t1w is ", config["t1"])

# Ejecutar app.py con el argumento del archivo de imagen
subprocess.run(['python', 'app.py', config["t1"]])

