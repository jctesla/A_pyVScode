import socket
import threading


                                                            # Ejemplo : si cliente envia "hello", HEADER = "5" x q son 5 bytes.
HEADER = 64                                                 # c/vez q se conecte un cliente al servidor y envie un msg, no sabemos de q longitud es por lo tanto en HEADER,
                                                            # almacenamos el numero q representala longitud del msg del cliente que esta enviando al servidor y es de 64bytes.
FORMAT = 'utf-8'    
DISCONNECT_MESSAGE = "!DISCONNECT"

PORT = 5050
#SERVER = "192.168.1.14"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   # for IPV v4, nro de puerto.
server.bind(ADDR)       #unimos el ip y el prto

#-------------------------------------------------
#       FUNCIONES
#--------------------------------------------------
# NOTA: c/vez q un clinete se conecta se crea un HILO de coneccion y se asigna una memoria, pero si quiero esto colocarlo a una 
# list podemos crear quias otro Hilo para darselo auna lista donde se conectan todos los clientes


#vamos a rear un thread function para adinstrar las conecciones
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)           # decodificamos el HEADER que es texto en el formato q establescamos ut-8
        if msg_length:                                          # si no hay msg sino solo coneccion, entonces no entramos.
            msg_length = int(msg_length)                            # convertimos la longitud q representa en numero
            msg = conn.recv(msg_length).decode(FORMAT)              # asignamos esa cantidad de memoria para recivir el msg de cliente.
            
            if msg == DISCONNECT_MESSAGE:                           # si hay un mensaje de desconeccion liberamos la memoria utilizada de la coneccion actual
                connected = False                                   # con saliendo del HILO

            print(f"[{addr}]{msg}")                                 # imprimo su direccion de IP y el mensage del cliente.

            #si quiero responder al cliente cada vez q me envie un msg
            conn.send("Msg Received".encode(FORMAT))

    conn.close()




def start():    
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()                                        # tenemos la coneccion del servidor y la ip del cliente.
        thread = threading.Thread(target=handle_client,args=(conn, addr))   # jalamos la coneccion a un hilo con su Coneccion y Direcion Ip
        thread.start()                                                      # lanzamos un hilo p c/coneccion
        print(f"[ACTIVE CONNECTION] {threading.activeCount()-1}")           




#-------------------------------------------------
#       MAIN
#--------------------------------------------------        
print("[STARTING] server is starting....")
start()
