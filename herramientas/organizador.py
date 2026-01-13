import os
import shutil

ruta_descargas = os.path.join(os.path.expanduser('~'), 'Downloads')

archivos = os.listdir(ruta_descargas)

carpeta_imagenes = os.path.join(ruta_descargas, "Imagenes")
carpeta_videos = os.path.join(ruta_descargas, "Videos")
carpeta_audios = os.path.join(ruta_descargas, "Audios")
carpeta_documentos = os.path.join(ruta_descargas, "Documentos")
carpeta_programas = os.path.join(ruta_descargas, "Programas")

if not os.path.exists(carpeta_imagenes):
    os.makedirs(carpeta_imagenes)

if not os.path.exists(carpeta_videos):
    os.makedirs(carpeta_videos)

if not os.path.exists(carpeta_audios):
    os.makedirs(carpeta_audios)

if not os.path.exists(carpeta_documentos):
    os.makedirs(carpeta_documentos)

if not os.path.exists(carpeta_programas):
    os.makedirs(carpeta_programas)


for arch in archivos:
    if arch.endswith((".jpg", ".png", "jpeg")):
        ruta_origen = os.path.join(ruta_descargas, arch)
        ruta_destino = os.path.join(carpeta_imagenes, arch)
        shutil.move(ruta_origen, ruta_destino)
    elif arch.endswith((".mp4", ".mov", ".mkv")):
        ruta_origen = os.path.join(ruta_descargas, arch)
        ruta_destino = os.path.join(carpeta_videos, arch)
        shutil.move(ruta_origen, ruta_destino)
    elif arch.endswith((".mp3", ".wav")):
        ruta_origen = os.path.join(ruta_descargas, arch)
        ruta_destino = os.path.join(carpeta_audios, arch)
        shutil.move(ruta_origen, ruta_destino)
    elif arch.endswith((".pdf", ".docx", ".doc", ".txt")):
        ruta_origen = os.path.join(ruta_descargas, arch)
        ruta_destino = os.path.join(carpeta_documentos, arch)
        shutil.move(ruta_origen, ruta_destino)
    elif arch.endswith((".exe", ".msi")):
        ruta_origen = os.path.join(ruta_descargas, arch)
        ruta_destino = os.path.join(carpeta_programas, arch)
        shutil.move(ruta_origen, ruta_destino)