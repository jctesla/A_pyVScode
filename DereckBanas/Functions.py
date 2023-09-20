import sys

# Definicion de una Funcion de Suma
def addNumber(num1,num2):
    sumNum = num1 + num2
    return sumNum
print("Funcion Suma 1 + 4 = ",addNumber(1,4))

# Como leer un Input de Datos.
print('What is yur Name?')
name = sys.stdin.readline()
print("Hello ", name)

string = "I'll catch you if you fall -  the door"
print("Sustrae una letra de string[0] = ", string[0])
print("Sustrae 4 carcateres de string = ",string[0:4])  #[idxBegin=0,idxBegin=1]
print("string[:-5]",string[:-5])        # = I'll catch you if you fall -  the
print("string[:-5]",string[-5:])        # = door
print("%c is my %s letter and my number %d numebr is %.5f", 'X', 'favorite',1,.14)
print("Buscar una plaabra de string = ",string.find("door"))        # Buscar una plaabra de string =  34
print("Longitud de Strnh = ",len(string))                       # Longitud de Strnh =  38
print("Reemplazo de una cadena de string = ", string.replace("door","floor")) #Reemplazo de una cadena de string =  I'll catch you if you fall -  the floor
arry = string.split(" ")
print("Usando split de espacio en strng = ",arry)   # Usando split de espacio en strng =  ["I'll", 'catch', 'you', 'if', 'you', 'fall', '-', '', 'the', 'door']


# video 34 min

