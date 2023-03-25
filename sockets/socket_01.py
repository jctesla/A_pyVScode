import socket
sck =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)           # configuracion
sck.connect(('data.pr4e.org',80))                                 # ip del servidor
sck.send('GET http://data.pr4e.org/romeo.txt\r\n\r\n'.encode())   # direccion, si quitas '\r\n\r\n', 
                                                                  # <b'13101310'> no devuelve nada
while True:
  data = sck.recv(64)                 # creo un buffer de 64 bytes
  if (len(data) < 1):                 # despues varias lecturas el buffer en algun momento
    break                             # sera vacio.
  print(f'--> data/{len(data)}bytes')
  print(f'--> {data.decode()}')
  

print("Fin de Datos")
sck.close
