from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Loading Image')
root.iconbitmap('img/MicLabLogo.ico')

def forward(imgNum):
    global mylabel,button_back,button_forward
    #mylabel.grid_forget                             #delete image from label
    mylabel=Label(root,image=img_List[imgNum-1])    #load new img
    return

def back(imgNum):
    return



#Puedes cargar formatos .jpg .bmp .png
myImg_01 = ImageTk.PhotoImage(Image.open("img/salmavaliSuchi.jpg"))
myImg_02 = ImageTk.PhotoImage(Image.open("img/cumpleSalmi.jpg"))
myImg_03 = ImageTk.PhotoImage(Image.open("img/salmivalimamijc.jpg"))
myImg_04 = ImageTk.PhotoImage(Image.open("img/salvaljkj_footmark.jpg"))
myImg_05 = ImageTk.PhotoImage(Image.open("img/christmasFam.jpg"))
myImg_06 = ImageTk.PhotoImage(Image.open("img/casaJmaria.jpg"))

img_List = [myImg_01,myImg_02,myImg_03,myImg_04,myImg_05,myImg_06]

mylabel=Label(image="img/travis.png")
mylabel.grid(row=0,column=0,columnspan=3)

button_forward = Button(root,text='Adelate>>',command=lambda:forward())
button_quit = Button(root,text='Exit/Salida',command=root.quit)
button_back = Button(root,text='<<Atras',command=lambda:back())

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()

