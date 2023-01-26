import os
from pytube import YouTube

def download_youtube_video(url, quality, path):
    try:
        # creamos una instancia de YouTube con la url del video
        yt = YouTube(url)
        
        # Si se especificó una calidad de video, se filtran los streams disponibles
        if quality:
            video = yt.streams.filter(file_extension='mp4', res=quality).first()
        else:
            video = yt.streams.filter(file_extension='mp4').first()

        # se descarga el video en la ruta especificada
        video.download(path)
        print(f"Video descargado exitosamente en la ruta: {path}")
    except:
        print("Error al descargar el video, asegurese de que la url es correcta")

# Especificamos la URL del video de YouTube a descargar
url = 'https://www.youtube.com/watch?v=iYP9L_77WGM'

# Especificamos la calidad del video (p. ej. 1080p, 720p, etc.)
quality = '1080p'

# Especificamos la ruta de guardado del video
path = 'C:\\Videos'

# Verificamos si existe la ruta especificada, si no existe la creamos
if not os.path.exists(path):
    os.makedirs(path)

# Llamamos al método para descargar el video
download_youtube_video(url, quality, path)
