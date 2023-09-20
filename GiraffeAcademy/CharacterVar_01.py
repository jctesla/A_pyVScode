# import math .- The first method imports using the math namespace. You would use the sqrt function like this: math.sqrt(x)
# from math import * .- The second method imports all the methods from math into the current namespace. You would use the sqrt function like this: sqrt(x)


import math  # version py 3.7

# from math import *    # version py 3.6
character_name = "John"
character_age = "35"
number_age = 50
is_male = False

print("Su Name : " + character_name + ",")
print("Su Age es : " + character_age + " years Old")

# Strings
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())

# "Phrase esta en Mayuscula? "
phrase = phrase.upper()             # Convierto la Variable a UPPER CASE = "GIRAFFE ACADEMY"
print(phrase.isupper())             # true
print(phrase.lower().islower())     # true
print(phrase.index("G"))            # me devolve indice = 0
print(phrase.index("ACAD"))         # return  indice = 8 empeiza la frase "ACAD" de "GIRAFFE ACADEMY"

# Replace a text from a String
phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))  # phrase = "Elephant Academy"

# Number Types

print(3 + 4.5)
print(3 * (4 + 5))
print(10 % 3)                       # 10 mod 3
print(max(4, 10))                   # return max number = 10
print(math.sqrt(36))                # need mathermatical library = "import math"
print(pow(3, 2))                    # 3 exp 2  = 3 x 3  = 9
print(round(3.7))                   # redondea una cifra
print(str(ascii('A')))

# USING INPUT
name = input("Enter your Name: ")
print("Buenos dias Sr :" + name)

# sum 2 number & concatenate w String
num1 = int(input("Enter number 01 "))
num2 = int(input("Enter number 03 "))
result = num1 + num2
print("La suma de num1 y num2 = " + str(result))

# sum 2 number text convert in float
num1 = input("Ingrese Num1 Float:")
num2 = input("Ingrese Num2 Float:")
result = float(num1) + float(num2)
print("La suma Float de num1 y num2 = " + str(result))

# using inputs
color = input("Enter Color")
print("Rose are color {color}")
print("Tu color es " + color)




