from tkinter import *
root = Tk()
root.title("Calculadora")
digNum = ''
num1=0
num2=0
simbolo= 'a'

#Objeto create a InputBox en una posicion 0,0 
e = Entry(root,width=47, bg="yellow", fg="blue", borderwidth=2)
e.grid(row=0, column=0, columnspan=5)
#e.pack()

#funcion cuando presiono Click
def button_numero(valor):
     global digNum
     e.delete(0,END)                           #Borro la pantalla
     digNum = digNum + str(valor)              #guardo el ActualNumero en la Calculadora
     e.insert(0,digNum)                        #Vuelvo a escribir el Nuevo Numero digitado = anterios +  el Actual 
     return

def button_opeMath(signo):
    global simbolo, num1,digNum
    simbolo = signo
    num1 =  int(digNum)
    digNum = ''
  
    e.delete(0,END)                           #Borro la pantalla
    e.insert(0,simbolo)                       #Escribo la Operacin que realizo
    print('Signo Presionado = {0}'.format(signo))
    return

def button_igual():
    global num2
    num2 =  e.get()

    e.delete(0,END)                           #Borro la pantalla
    print('Operacion de = {0}'.format(simbolo))
    print('Numeros Num1 = {0} y Num2 = {1}'.format(num1,num2))

    if (simbolo =='suma'):
      e.insert(0,str(int(num1)  + int(num2)))       #Escribo el Reusltaod de la Operacion de Suma
      
    if (simbolo =='resta'):
      e.insert(0,str(int(num1)  - int(num2)))       #Escribo el Reusltaod de la Operacion de Resta

    if (simbolo =='multi'):
        e.insert(0,str(int(num1) * int(num2)))       #Escribo el Reusltaod de la Operacion de Multiplicacion

    if (simbolo =='divi'):
        e.insert(0,str(int(num1) / int(num2)))       #Escribo el Reusltaod de la Operacion de Division

    return
    
def button_clear():
       e.delete(0,END)
       global digNum,num1,num2
       digNum=''
       num1=0
       num2=0
       return


#Define Buttons
#la forma de pasar paremtros es con la clausula lambda
space = Label(root, text=" ")
button_01 = Button(root, text ="1", padx=30, pady=10, command=lambda:button_numero(1))
button_02 = Button(root, text ="2", padx=30, pady=10, command= lambda:button_numero(2))
button_03 = Button(root, text ="3", padx=30, pady=10, command= lambda:button_numero(3))
button_04 = Button(root, text ="4", padx=30, pady=10, command= lambda:button_numero(4))
button_05 = Button(root, text ="5", padx=30, pady=10, command= lambda:button_numero(5))
button_06 = Button(root, text ="6", padx=30, pady=10, command= lambda:button_numero(6))
button_07 = Button(root, text ="7", padx=30, pady=10, command= lambda:button_numero(7))
button_08  = Button(root, text ="8", padx=30, pady=10, command=lambda:button_numero(8))
button_09  = Button(root, text ="9", padx=30, pady=10, command=lambda:button_numero(9))
button_00  = Button(root, text ="0", padx=30, pady=10, command=lambda:button_numero(0))
button_equal = Button(root, text ="=", padx=30, pady=10, command=button_igual)
button_clear = Button(root, text ="Clear", padx=20, pady=10, command=button_clear)
button_add = Button(root, text ="+", padx=18, pady=10, command=lambda:button_opeMath("suma"))
button_resta = Button(root, text ="-", padx=20, pady=10, command=lambda:button_opeMath("resta"))
button_mult = Button(root, text ="*", padx=19, pady=10, command=lambda:button_opeMath("multi"))
button_div = Button(root, text ="/", padx=20, pady=10, command=lambda:button_opeMath("divi"))

#put the buttons on the screen
button_add.grid(row=3, column=0)
space.grid(row=3, column=1)
button_01.grid(row=3, column=2)
button_02.grid(row=3, column=3)
button_03.grid(row=3, column=4)

button_resta.grid(row=2, column=0)
space.grid(row=2, column=1)
button_04.grid(row=2, column=2)
button_05.grid(row=2, column=3)
button_06.grid(row=2, column=4)

button_mult.grid(row=1, column=0)
space.grid(row=1, column=1)
button_07.grid(row=1, column=2)
button_08.grid(row=1, column=3)
button_09.grid(row=1, column=4)

button_div.grid(row=4, column=0)
space.grid(row=4, column=1)
button_00.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
button_clear.grid(row=4, column=4)

#hechar andar todo el frmwrk
root.mainloop()

