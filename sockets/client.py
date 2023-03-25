import socket

# NOTA : si queremos enviar no solo string sino Object, podemos usar "JSON" serialized o "Picklet"
# puedes enviar Objetos enteros, y en el servidor podemos usr "unpickle"
# import pickle



                                                            # Ejemplo : si cliente envia "hello", HEADER = "5" x q son 5 bytes.
HEADER = 64                                                 # c/vez q se conecte un cliente al servidor y envie un msg, no sabemos de q longitud es por lo tanto en HEADER,
                                                            # almacenamos el numero q representala longitud del msg del cliente que esta enviando al servidor y es de 64bytes.
FORMAT = 'utf-8'    
DISCONNECT_MESSAGE = "!DISCONNECT"

PORT = 5050
SERVER = "192.168.1.14"
ADDR = (SERVER,PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_legnth = len(message)
    send_length = str(msg_legnth).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))                 # si recivimos una respuesta del servidor podemos usar el mismo mecanismo del cliente al Server del HEADER=64

                                                            # pero por ahora asignamos una buffer grande por q sabemos q la resp del servidor al cliente es pequeño-
send("HELLO WORLD")
input()
send("Hola a Todos")
input()
send("que bacan!!!")
input()
send(DISCONNECT_MESSAGE)

