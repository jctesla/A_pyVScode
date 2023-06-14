# OAuth 2 .- nos permite acceder a los scripts y app con acceso limitado a cuentas de terceros, en este
# ej seria con youtube.
# Otro Ej es cuando usamos instagram, y nos permite publicar fotos en twitter o facebook :. al hacer esto la 1ra vez
# Instragram nos pedira permiso p logearnos con el perfil de twitter usando OAuth 2.
import os
from googleapiclient.discovery import build
from goole_auth_oauthlib.flow import InstalledAppFlow
api_key = os.environ.get("YT_API_KEY")            # al crear esta var en mi SO win7, tuve q reiniciar mi cuenta en la Maq.
print("api_key=" + api_key + "\n")
youtube = build("youtube","v3",developerKey=api_key)

# request = youtube.playlistchannels().list(part="contentDetails", forUsername="schafer5")
#response = request.execute()
#print(response)

history_response = youtube.activities().list(
    part='snippet',
    mine=True,
    maxResults=10  # Adjust as per your requirement
).execute()

history_list = history_response['items']
for item in history_list:
    video_title = item['snippet']['title']
    print(video_title)
