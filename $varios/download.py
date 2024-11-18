from pytube import YouTube

saveMp4Path = "c:/$mio/"

youtubelink=[
  "https://www.youtube.com/watch?v=bEKjCDDUPaU",
  "https://www.youtube.com/watch?v=MlK6SIjcjE8&t=10s"
]

for i in youtubelink:
    yt = YouTube(i)
    print("title :", yt.title)
    print("captions : ", yt.captions)
    icon = yt.thumbnail_url
    print("Streams format :", yt.publish_date)
    
    # mp4File =  yt.streams.filter(progressive=True, file_extension='mp4')
    # yt.streams.get_highest_resolution()	
    # get the video with the extension and
    # resolution passed in the get() function
    d_video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    try:   
      d_video.download(saveMp4Path)
    except:
      print("Some Error!")
   
print('Task Completed!')