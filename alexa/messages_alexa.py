# This program uses the requests library to make a POST request to the AVS endpoint with the appropriate headers and data.
# The message variable contains the text message that you want to send to Alexa, and the device_info variable contains
# information about the device you're sending the message to. You'll need to replace "your_device_id" and 
# "your_product_id" with the appropriate values for your device and replace "your_access_token" with a 
# valid access token for the AVS API.


import requests
import json

# Alexa Voice Service endpoint
#AVS_ENDPOINT = "https://access-alexa-na.amazon.com/v1/avs/speechrecognizer/recognize"
AVS_ENDPOINT = 'https://api.amazon.com/auth/O2/token'

# Alexa Device Information
# your_device_id & your_product_id 
# deviceId = lo llaman tambien 'clienteId'
device_info = {
    #"deviceId": "DC:54:D7:91:48:DD",
    #"productId": "JuanCarlos Echo Dot"
    "clientId": "amzn1.application-oa2-client.1623fcceb6e14332adc566570db0c7a6",
    "productId": "JuanCarlos_EchoDot3"
}

# Access token for the AVS API = "your_access_token"
# amzn1.application.09e7c1b714fb43c7b8af52be479e3ec8
access_token = "amzn1.application.09e7c1b714fb43c7b8af52be479e3ec8"

# Text message to send to Alexa
message = "Hello, Alexa. What's the weather today?"

# Headers for the HTTP request
headers = {
    "Authorization": "Bearer {}".format(access_token),
    "Content-Type": "application/json; charset=utf-8"
}

# Data for the HTTP request
data = json.dumps({
    "messageHeader": {
        "deviceContext": [device_info]
    },
    "messageBody": {
        "profile": "alexa-close-talk",
        "locale": "en-us",
        "format": "audio/L16; rate=16000; channels=1",
        "data": message
    }
})

# Send the request to the AVS API
response = requests.post(AVS_ENDPOINT, headers=headers, data=data)

# Print the response
print(response.content)
