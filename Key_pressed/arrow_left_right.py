# UNA ALTERNATIVA A LA LIBRERIA from pynput.keyboard import Key, Listener 
from msvcrt import getch 
flg = 1

while True: 
    keycode = ord(getch())                  # -> get 1rst Byte
    
    if keycode == 27:                       # ESC (1 byte)
        print("ESC()")
        break 
    elif keycode == 13:                     # Enter (1 byte)
         print("ENTER select()")
    
    elif keycode == 224:                    # Special keys (arrows, f keys, ins, del, etc.) 
        keycode = ord(getch())              # -> get 2cnd Byte
        print(f'Key press = {keycode}')

        if keycode == 80:                   # Down arrow (1 byte)
            print("moveDown()")
            
        elif keycode == 72:                 # Up arrow (1 byte)
            print("moveUp()")