# Esta libreria tiene un comportamiento al parecer usar varios hilos
# por q cuando se usa una instruccion q no funciona despues de llamar a yt.title, se raya y el error es como si
# fuera del yt.title, pero NO es del por ej: mp4File =  yt.streams.filter(progressive=True, file_extension='mp4')
# es decir esta libreria no esta totalmente depurada de errores.ESTA VERSION FUNDIONA BIEN.

# example : python donwload_youtube_video_02.py -l https://www.youtube.com/watch?v=bEKjCDDUPaU
from pytube import YouTube
import threading, time

import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("-l" , "--link", help="indica el link del video youtbe a bajar.")
args = parser.parse_args()                                # cuando corra el prog Leo el valor del argumento.
print("link : ", args.link)


def downlink():
  global args
  savepath = "G:/$LIBROS VARIOS/"
  yt = YouTube(args.link)
  print("title :", yt.title)
  print("captions : ", yt.captions)
  #icon = yt.thumbnail_url
  print("Streams format :", yt.publish_date)
  d_video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
  try:   
    d_video.download(savepath)
  except:
    print("Err Downloadin maybe for coneccion!")
  else:
    print('Task Completed!')

    
#t = threading.Timer(downlink) # q va ejecutar luego de los 5 se
t = threading.Thread(target=downlink)
t.start()
  
pnts = "" 
while(t.is_alive()):
  pnts += "."
  print( pnts, end = '\r' )
  time.sleep(1.0)                       # si el video demora mucho en bajarlo debemos aumentar el time = 1.4

    

# dir(yt)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_age_restricted', '_author', '_embed_html', '_fmt_streams', '_initial_data', '_js',
# '_js_url', '_metadata', '_player_config_args', '_publish_date', '_title', '_vid_info', '_watch_html', 'age_restricted', 'allow_oauth_cache',
# 'author', 'bypass_age_gate', 'caption_tracks', 'captions', 'channel_id', 'channel_url', 'check_availability', 'description', 'embed_html',
# 'embed_url', 'fmt_streams', 'from_id', 'initial_data', 'js', 'js_url', 'keywords', 'length', 'metadata', 'publish_date', 'rating',
# 'register_on_complete_callback', 'register_on_progress_callback', 'stream_monostate', 'streaming_data', 'streams', 'thumbnail_url', 'title',
# 'use_oauth', 'vid_info', 'video_id', 'views', 'watch_html', 'watch_url']