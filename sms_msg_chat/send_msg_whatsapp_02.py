# En este paso, puede iniciar una conversación iniciada por el negocio con sus usuarios.
# Las conversaciones iniciadas por empresas requerían el uso de plantillas preaprobadas 
# hasta que el usuario respondiera. Elija entre una de nuestras plantillas preaprobadas
# para iniciar una conversación iniciada por el negocio. Una vez que sus clientes
# respondan, puede enviar mensajes de forma gratuita durante las próximas 24 horas
# después de su mensaje original.

from twilio.rest import Client

account_sid = 'AC8bd6f257f498ced67a5ffba5f9cf023d'          # 'TWILIO_ACCOUNT_SID'
auth_token = '9b302c94e48752ecb3981a0eefeaca23'           # 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your cita es se prepara para July 21 at 3PM, Buena Suerte',
  to='whatsapp:+51915189781'
)

print(message.sid)