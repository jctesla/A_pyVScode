from tkinter import *
main = Tk()
 


def LogKey(event): 
     print (f'estructura de event = {event}' )           # imprime toda la estructura de la clase de 'event'
     print (f'presiono = {event.keycode}' )              # imprime el codigo ASCI de l boton presionado.
     if event.keycode ==27:
         main.quit()
         #main.destroy()   
 
def leftKey(event): 
     print ("Left key pressed" )

def rightKey(event): 
    print ("Right key pressed")

def upKey(event): 
    print ("Up key pressed")

def downKey(event): 
    print ("Down key pressed")
 
def A_Key(event): 
    print ("A key pressed")
 
def a_Key(event): 
    print ("a key pressed")

def esc_Key(event): 
    print ("a key pressed")    


frame = Frame(main, width=100, height=100) 
Button(main, text="Quit", command=main.destroy).pack()

# widget.bind('<Event-String>', function_name)
main.bind('<Left>', leftKey) 
main.bind('<Right>', rightKey) 
main.bind('<Up>', upKey)
main.bind('<Down>', downKey)
main.bind('<A>', A_Key)
main.bind('<a>', a_Key)
main.bind("<KeyPress>", LogKey) 

 
frame.pack() 
 
main.mainloop() 