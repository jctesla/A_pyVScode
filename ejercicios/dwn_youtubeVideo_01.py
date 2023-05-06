# Esta libreria tiene un comportamiento al parecer usar varios hilos
# por q cuando se usa una instruccion q no funciona despues de llamar a yt.title, se raya y el error es como si
# fuera del yt.title, pero NO es del por ej: mp4File =  yt.streams.filter(progressive=True, file_extension='mp4')
# es decir esta libreria no esta totalmente depurada de errores.ESTA VERSION FUNDIONA BIEN.
from pytube import YouTube

saveMp4Path = "G:/$LIBROS VARIOS/"

youtubelink=[
  "https://www.youtube.com/watch?v=B2h8FohnwUs&t=370s",
  "https://www.youtube.com/watch?v=AoudEm89Vss&t=303s"
]

for i in youtubelink:
    yt = YouTube(i)
    #print("title :", yt.title)
    print("captions : ", yt.captions)
    print("icon : ", yt.thumbnail_url)
    print("Streams format :", yt.publish_date)
    
    # mp4File =  yt.streams.filter(progressive=True, file_extension='mp4')
    # yt.streams.get_highest_resolution()	
    # get the video with the extension and
    # resolution passed in the get() function
    # d_video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    stream = yt.streams.get_highest_resolution()
    try:   
      # stream.download(saveMp4Path)          # d_video
      stream.download()          # d_video
    except:
      print("Some Error!")
   
print('Task Completed!')

# dir(yt)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_age_restricted', '_author', '_embed_html', '_fmt_streams', '_initial_data', '_js',
# '_js_url', '_metadata', '_player_config_args', '_publish_date', '_title', '_vid_info', '_watch_html', 'age_restricted', 'allow_oauth_cache',
# 'author', 'bypass_age_gate', 'caption_tracks', 'captions', 'channel_id', 'channel_url', 'check_availability', 'description', 'embed_html',
# 'embed_url', 'fmt_streams', 'from_id', 'initial_data', 'js', 'js_url', 'keywords', 'length', 'metadata', 'publish_date', 'rating',
# 'register_on_complete_callback', 'register_on_progress_callback', 'stream_monostate', 'streaming_data', 'streams', 'thumbnail_url', 'title',
# 'use_oauth', 'vid_info', 'video_id', 'views', 'watch_html', 'watch_url']