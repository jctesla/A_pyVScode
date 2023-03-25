from tkinter import *
root = Tk()

#defining widget Create a Label
myLabel1 = Label(root,text="Hola a Todos")
myLabel2 = Label(root,text="Me Llamo Juan Carlos")
myLabel3 = Label(root,text="------>")

#Ubicacion en el Screen grid of widgets
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=3)
myLabel3.grid(row=1,column=1)

#Coremos los widgets
root.mainloop()
