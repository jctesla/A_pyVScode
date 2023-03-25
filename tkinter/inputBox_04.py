from tkinter import *
root = Tk()

#funcion cuando presiono Click
def miClick():
  hello = "HOLA " + e.get()                       #Obtiene el contenido del InputBox = e y lo concatena con el Sldo.
  myLabel = Label(root, text=hello)               #muestra el Saludo en la etiqueta "myLabel".
  myLabel.pack()                                  #el "pack()" es como el contenedor que se va visualizar en el root el frmwrk
  return

#Objeto InputBox
e = Entry(root,width=30, bg="yellow", fg="blue")
e.pack()

#Objeto Boton
miBoton = Button(root, text="Enter Su Nombre", command=miClick)
miBoton.pack()

#hechar andar todo el frmwrk
root.mainloop()
