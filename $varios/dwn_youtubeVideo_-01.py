from pytube import YouTube

# Get the YouTube video URL
video_url = input("Enter the YouTube video URL: ")
if len(video_url) ==0:
  video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# Create a YouTube object with the video URL
yt = YouTube(video_url)

# Get the highest resolution stream available
stream = yt.streams.get_highest_resolution()

# Download the video to the current working directory
stream.download()
print("Listo!")