# este Ejemplo nos enseña como mover un cursor en MODO TEXTO en 1 dimensions, eje X: el cursor es un '*'
from msvcrt import getch 

# creo mi Matriz 1d de 50 elementos
x=5
arr = [' ' for u in range(50)]          # en esta matriz se va dibujar segun el evnto Rigth/Left el asterico simulando el movimiento.
arrClr = arr.copy()                     # copia el mismo arry pero sin crear dependencia de relacion, 
                                        # si es arrClr = arr si se crea depend, es decir si hay un cambio en arr se refelja automaticamente en arrClr
arr[x]='*'

#print(arr)

# rutina sin fin, escucha el evento del Key Pressed
while True: 
    keycode = ord(getch())              # get 1rst Byte, leo el key del modo asci 'text'-->int()
    
    if keycode == 27:                   # ESC (1 byte)
        print("ESC()")
        break 
    elif keycode == 13:                                 # Enter (1 byte)
         print("ENTER select()")
    elif keycode == 224:                                # Special keys (arrows, f keys, ins, del, etc.) 
        
        keycode = ord(getch())                          # get 2cnd Byte
        #print(f'Key press = {keycode}')
        
        if keycode == 77:                               # -> move Right() arrow (1 byte)
            arr = arrClr.copy()
            x+=1
            
            if x == len(arr):                           # si llega al tope de posicion derecho de la Matriz
                x=0
            
            arr[x]='*'                                  # coloco el '*' en la posicion q sigue a la derecha en la matriz    
            dspky = ''.join([str(e) for e in arr])      # reconstruyo la matriz con la posicion nueva del '*'
            print(dspky,end='\r')
            
        elif keycode == 75:                             # <- move Left() arrow (1 byte)
            arr = arrClr.copy()
            x-=1
            
            if x  < 0:                                  # si llega al tope de posicion izq de la Matriz
                x=len(arr)-1
            
            arr[x]='*'                                  # coloco el '*' en la posicion q sigue a la izq en la matriz
            dspky = ''.join([str(e) for e in arr])
            print(dspky,end='\r')                       # reconstruyo la matriz con la posicion nueva del '*'
