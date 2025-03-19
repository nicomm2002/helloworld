#!/usr/bin/env python
import sys
import nibabel as nib
import os

# Imprimir la versión de nibabel
print(nib.__version__)

# Verificar que se haya proporcionado un argumento
if len(sys.argv) < 2:
    print("Error: No se proporcionó un archivo de imagen.")
    sys.exit(1)

# Verificar que el archivo existe
file_path = sys.argv[1]
print(f"Ruta del archivo de imagen: {file_path}")

# Verificar si el archivo tiene un punto final adicional y eliminarlo
if file_path.endswith('.'):
    file_path = file_path[:-1]
    print(f"Ruta del archivo corregida: {file_path}")

if not os.path.exists(file_path):
    print(f"Error: El archivo '{file_path}' no existe.")
    sys.exit(1)

# Cargar la imagen y guardar la cabecera en output.txt
try:
    img = nib.load(file_path)
    with open("output.txt", "w") as f:
        f.write(str(img.header))
    print(f"Cabecera de la imagen guardada en 'output.txt'.")
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    sys.exit(1)
