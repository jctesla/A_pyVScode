import youtube_dl

# URL of the video to download
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create options object to configure the download
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
}

# Download the video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
