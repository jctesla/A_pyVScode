# Esta libreria tiene un comportamiento al parecer usar varios hilos
# por q cuando se usa una instruccion q no funciona despues de llamar a yt.title, se raya y el error es como si
# fuera del yt.title, pero NO es del por ej: mp4File =  yt.streams.filter(progressive=True, file_extension='mp4')
# es decir esta libreria no esta totalmente depurada de errores.ESTA VERSION FUNDIONA BIEN.
from pytube import YouTube

# URL of the YouTube video to download
video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Create a YouTube object
yt = YouTube(video_url)

# Select the first available progressive stream with the highest resolution
#stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
#stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()
