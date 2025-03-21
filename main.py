import json
import subprocess
import os

try:
    # Cargar config.json
    with open('config.json') as f:
        config = json.load(f)

    print("Mi ruta al archivo EEG es ", config["eeg"])

    # Ejecutar app.py con el argumento del archivo de datos EEG
    subprocess.run(['python', 'app.py', config["eeg"]])

except FileNotFoundError as e:
    print(f"Error: {e}")
except json.JSONDecodeError as e:
    print(f"Error al cargar el archivo JSON: {e}")
except KeyError as e:
    print(f"Error: La clave {e} no se encuentra en config.json")
except Exception as e:
    print(f"Ocurrió un error: {e}")
