from tkinter import *
root = Tk()

def miClick():
  myLabel = Label(root, text="Mira Clikeastes Boton!!")
  myLabel.pack()


miBoton = Button(root, text="Click Me", command=miClick)
miBoton.pack()


root.mainloop()

