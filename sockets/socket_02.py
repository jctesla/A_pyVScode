import socket
import sys
port = 80


try:
	url = 'www.google.com'																				# Leo otra pagina web
	ip = socket.gethostbyname(url)
	print(f'Direccion de {url} = {ip}\n')													# Hostname e IP = www.google.com = 142.250.0.99
	
	sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)				# creamos un Socket con el Hostremoto.
	print (f'Socket was successfully created w {url}')
except socket.error as err:
	print (f'socket creation failed with error {err}')
	sys.exit()

sck.connect((url, port))																				# if not ERR connecting to the server
print (f'the socket has successfully connected to <{url}>')

#sck.send(('Hello Server!').encode());
sck.send(('GET https://' + url + '\r\n').encode('utf8'));
data = sck.recv(2048)

print(f'\nRespuesta del Servidor : \n {data.decode()}')
sck.close()
