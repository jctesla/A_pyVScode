from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Loading Image')
root.iconbitmap('img/MicLabLogo.ico')

#Puedes cargar formatos .jpg .bmp .png
myImg = ImageTk.PhotoImage(Image.open("img/travis.png"))
myLabel = Label(image=myImg)
myLabel.pack()

button_quit = Button(root,text='Exit/Salida',command=root.quit)
button_quit.pack()

root.mainloop()


