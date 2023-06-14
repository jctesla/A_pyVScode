from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

UserID = "eNCIZI2Yi8MuWW7N-0r-bw"
ChannelID = "UCeNCIZI2Yi8MuWW7N-0r-bw"

# Define the scopes required for the YouTube Data API
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Set up OAuth 2.0 credentials
flow = InstalledAppFlow.from_client_secrets_file('path/to/client_secrets.json', scopes)
credentials = flow.run_local_server(port=0)

# Create the YouTube Data API client
youtube = build('youtube', 'v3', credentials=credentials)

# Retrieve the history list
history_response = youtube.activities().list(
    part='snippet',
    mine=True,
    maxResults=400  # Adjust as per your requirement
).execute()

history_list = history_response['items']
for item in history_list:
    video_title = item['snippet']['title']
    print(video_title)

