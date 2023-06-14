# OAuth 2 .- nos permite acceder a los scripts y app con acceso limitado a cuentas de terceros, en este
# ej seria con youtube.
# Otro Ej es cuando usamos instagram, y nos permite publicar fotos en twitter o facebook :. al hacer esto la 1ra vez
# Instragram nos pedira permiso p logearnos con el perfil de twitter usando OAuth 2.

# Requsitos : pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

import os
from googleapiclient.discovery import build
api_key = os.environ.get("YT_API_KEY")            # al crear esta var en mi SO win7, tuve q reiniciar mi cuenta en la Maq.
print("api_key=" + api_key + "\n")
youtube = build("youtube","v3",developerKey=api_key)
request = youtube.channels().list(part="contentDetails", forUsername="schafer5")
response = request.execute()
print(response)

# {'kind': 'youtube#channelListResponse', 'etag': 'nCGkOOTH4oAuIhNf3uW6bJuVDaA', 
# 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 
# 'items': [{'kind': 'youtube#channel', 'etag': '6kPIeBryVx6NRd2-MZCInMGs1oQ', 'id': 'UCCezIgC97PvUuR4_gbFUs5g', 
# 'contentDetails': {'relatedPlaylists': {'likes': '', 'uploads': 'UUCezIgC97PvUuR4_gbFUs5g'}}}]}

# Explain:
# uploads : the ID of all the list of the video I upLoad to my Channel of YouTube.
# 
