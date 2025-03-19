import json
import subprocess

# Cargar config.json
with open('config.json') as f:
    config = json.load(f)

print("my path to t1w is ", config["t1"])

# Ejecutar app.py con el argumento del archivo de imagen
subprocess.run(['python', 'app.py', config["t1"]])

# Configurar el repositorio en tu perfil
subprocess.run(['git', 'remote', 'remove', 'origin'])
subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/nicomm2002/helloworld.git'])

# Verificar la rama actual y crear la rama `main` si no existe
try:
    subprocess.run(['git', 'checkout', '-b', 'main'], check=True, stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    subprocess.run(['git', 'checkout', 'main'], check=True)

# Añadir cambios al repositorio de Git
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'created my first BL App!'])
subprocess.run(['git', 'push', '-u', 'origin', 'main'])