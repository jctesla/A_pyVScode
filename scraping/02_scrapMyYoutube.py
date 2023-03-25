from googleapiclient.discovery import build

# Replace YOUR_API_KEY with your actual API key
API_KEY = "AIzaSyC3Xv1WwahgSxK6XBnRrTkDh7CwsfBykZg"  # 'YOUR_API_KEY'
CHANNEL_ID = "UCeNCIZI2Yi8MuWW7N-0r-bw"              # 'YOUR_CHANNEL_ID'

# Create a YouTube API client instance
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Retrieve the channel's uploads playlist ID
channels_response = youtube.channels().list(part='contentDetails', id=CHANNEL_ID).execute()
uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Retrieve all the video IDs in the uploads playlist
videos = []
next_page_token = None
while True:
    playlist_items_response = youtube.playlistItems().list(part='contentDetails', playlistId=uploads_playlist_id, maxResults=50, pageToken=next_page_token).execute()
    videos.extend(playlist_items_response['items'])
    next_page_token = playlist_items_response.get('nextPageToken')
    if not next_page_token:
        break

# Retrieve information about each video using its ID
for video in videos:
    video_id = video['contentDetails']['videoId']
    video_response = youtube.videos().list(part='snippet', id=video_id).execute()
    video_title = video_response['items'][0]['snippet']['title']
    video_description = video_response['items'][0]['snippet']['description']
    print(f'Title: {video_title}')
    print(f'Description: {video_description}')


    