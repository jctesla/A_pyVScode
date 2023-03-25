import msvcrt
while True:
    if msvcrt.kbhit():
        byteKey = msvcrt.getch()                            # lo Lee en formato de Bytes b''
        txtKey = byteKey.decode('UTF-8')                    # lo formateamos a codigo ASCI utf-8 texto
        
        if byteKey != b'\x00':                              # la segunda vez q leer al haber presiona un keyboard.
            print(f'Key byte={byteKey} / text={txtKey}')    # will print which key is pressed
        if txtKey.upper() == 'F':
            print('Presiono Salir!')
            break