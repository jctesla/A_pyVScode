# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC8bd6f257f498ced67a5ffba5f9cf023d'               # os.environ['AC8bd6f257f498ced67a5ffba5f9cf023d']      # 'TWILIO_ACCOUNT_SID'
auth_token = '9b302c94e48752ecb3981a0eefeaca23'                  # os.environ['9b302c94e48752ecb3981a0eefeaca23']         # 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+14155238886',     # from_='whatsapp:+14155238886',
         to='whatsapp:+51915189781'         # to='whatsapp:+51915189781'
     )

print(message.sid)

# salmita : +51980838757, mio:51915189781