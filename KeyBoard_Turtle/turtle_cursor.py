from msvcrt import getch 
import turtle
grado = 0
t = turtle.Pen()
turtle.bgcolor('black')

while True: 
    keycode = ord(getch())                  # get 1rst Byte
    
    if keycode == 27:                       # ESC (1 byte)
        print("ESC()")
        break 
    elif keycode == 13:                     # Enter (1 byte)
         print("ENTER select()")
    
    elif keycode == 32:                     # Space (1 byte)
         pos = t.position()
         print(pos)
         t.clear()

    #---------------------------------------
    elif keycode == 48:                     # Key 0 (1 byte)
         print("Cero()")
         t.width(1.5)
         t.pencolor('#ffff00')

    elif keycode == 49:                     # Key 1 (1 byte)
         print("Uno()")
         t.width(1.5)
         t.pencolor('#ff0000')

    elif keycode == 50:                     # Key 2 (1 byte)
         print("Dos()")
         t.width(1.5)
         t.pencolor('#0000ff')
    
    #---------------------------------------
    elif keycode == 51:                     # Key 3 (1 byte)
         ent_X = int(input("Coordenada X:"))
         ent_Y = int(input("Coordenada Y:"))
         t.setpos(ent_X,ent_Y)
    
    #-------------------------------     
    elif keycode == 52:                     # Key 4 (1 byte)
         print("Cuatro(Hide Turtle)")
         t.hideturtle()

    elif keycode == 53:                     # Key 5 (1 byte)
         print("Cinco(Show Turtle)")                    
         t.showturtle()

    #-------------------------------     
    elif keycode == 54:                     # Key 6 (1 byte)
         print('Seis( Off Pain)')             
         t.up()

    elif keycode == 55:                     # Key 7 (1 byte)
         print('Siete(On Pain)')                    
         t.down()


    elif keycode == 224:                    # Special keys (arrows, f keys, ins, del, etc.) 
        
        keycode = ord(getch())              # get 2cnd Byte
        print(f'Key press = {keycode}')

        if keycode == 77:                   # moveRight() arrow (1 byte)
            print(f'moveRight(Turm Right 90)')
            t.right(90)
        
        elif keycode == 75:                 # moveLeft() arrow (1 byte)
            print(f'moveLeft(Turn Left 90)')
            t.left(90)

        elif keycode == 80:                 # Down arrow (1 byte)
            print(f'KeyDwn(anything)')

        elif keycode == 72:                 # Up arrow (1 byte)
            print(f'KeyUp(Move Up)')
            t.forward(10)
            


