import os
import shutil

ruta_descargas = os.path.join(os.path.expanduser('~'), 'Downloads')

archivos = os.listdir(ruta_descargas)

carpeta_imagenes = os.path.join(ruta_descargas, "Imagenes")

if not os.path.exists(carpeta_imagenes):
    os.makedirs(carpeta_imagenes)

for arch in archivos:
    if arch.endswith((".jpg", ".png", "jpeg")):
        ruta_origen = os.path.join(ruta_descargas, arch)
        ruta_destino = os.path.join(carpeta_imagenes, arch)
        shutil.move(ruta_origen, ruta_destino)
    