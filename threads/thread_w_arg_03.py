# Esta libreria tiene un comportamiento al parecer usar varios hilos
# por q cuando se usa una instruccion q no funciona despues de llamar a yt.title, se raya y el error es como si
# fuera del yt.title, pero NO es del por ej: mp4File =  yt.streams.filter(progressive=True, file_extension='mp4')
# es decir esta libreria no esta totalmente depurada de errores.ESTA VERSION FUNDIONA BIEN.
# a VECES FUNCIONA MAL POR QUE EL SERVIDOR DE YOUTUBE SE PONEMUY LENTO.

# example : python donwload_youtube_video_02.py -l https://www.youtube.com/watch?v=bEKjCDDUPaU
from pytube import YouTube
import threading, time

import argparse 
savepath = 'D:/phytonSpace/miBasic/A_VSCode/threads/'      # "G:/$LIBROS VARIOS/"

parser = argparse.ArgumentParser()
parser.add_argument("-l" , "--link", help="indica el link del video youtbe a bajar.")
args = parser.parse_args()                                # cuando corra el prog Leo el valor del argumento.
print("link : ", args.link, "\n")

# -------------  THREAD Function -------------------------
def downlink(link,savepath):
  print('path : ',savepath, "  link : ", link)
  yt = YouTube(link)
  print("title :", yt.title)
  print("captions : ", yt.captions)
  print("Streams format :", yt.publish_date)
    
  d_video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
  try:   
    d_video.download(savepath)
  except:
    print("Err Downloadin maybe for coneccion!")
  else:
    print('Task Completed!')
  
  print('Task Completed!')
  
  
  
#-------------- Main Process ------------------------------    
#t = threading.Timer(downlink) # q va ejecutar luego de los 5 se
t = threading.Thread(target=downlink,args=(args.link,savepath,))
t.start()
  
# print a progress bar of point until thread finish.  
pnts = "" 
while(t.is_alive()):
  pnts += "."
  print( pnts, end = '\r' )
  time.sleep(0.5)                       # si el video demora mucho en bajarlo debemos aumentar el time = 1.4