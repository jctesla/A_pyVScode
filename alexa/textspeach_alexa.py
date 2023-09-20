# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html?highlight=polly#Polly.Client
# Amazon Polly is a web service that makes it easy to synthesize speech from text.

import boto3															# importando la biblioteca Boto3 de AWS, que nos 		
																					# proporciona acceso a las API de Amazon Polly y otras funcionalidades de AWS

polly = boto3.client('polly')							# Creamos un cliente de Amazon Polly utilizando  Boto3. 
																					# Esto nos permitirá acceder a los métodos de la API de Amazon Polly.

# Set the text and voice
text = 'Hello, my name is Polly. How can I help you today?'				# Establecemos el texto que queremos sintetizar y la voz que deseamos utilizar para la 			
voice = 'Matthew'																									# síntesis. Las voces disponibles en Amazon Polly se pueden encontrar en la  
																																	# https://docs.aws.amazon.com/polly/latest/dg/SupportedLanguage.html
try:
	response = polly.synthesize_speech(Text=text, VoiceId=voice, OutputFormat='mp3')   	# Llamamos al método synthesize_speech del cliente de Amazon Polly p sintetizar el texto en voz.
except(BotoCoreError, ClientError) as error:																					# Especificamos el texto a sintetizar con la opción Text, la voz a utilizar con la opción 
	print(error)                               																					# VoiceId y el formato de salida del audio con la opción OutputFormat.
  sys.exit(-1)                                                   											# En este ejemplo, estamos utilizando MP3 como formato de salida.
																																											# possible ERR : The security token included in the request is invalid.
																																											# The security token included in the request is invalid.
                                          																						#	File "D:\phytonSpace\miBasic\A_VSCode\yaml format\textspeach_alexa.py", line 12, in <module>

# Save the audio stream to a file					      	
with open('output.mp3', 'wb') as file:															# Finalmente, abrimos un archivo en modo de escritura binaria y escribimos 
    file.write(response['AudioStream'].read())											# el stream de audio sintetizado en él.						
