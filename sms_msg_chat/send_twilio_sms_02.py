# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

account_sid = 'AC8bd6f257f498ced67a5ffba5f9cf023d'
auth_token = '9b302c94e48752ecb3981a0eefeaca23'                   # os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='#callme,993148609',
    from_='+14027366880',
    to='+51915189781'
)

print(message.sid)
