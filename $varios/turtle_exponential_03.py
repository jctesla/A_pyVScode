# draw a box in 4 colors, using number form 0 to 255
import time
import numpy as np
import turtle

# Funcion Matematica de Ovoide
funY = lambda x: ((x/8)**2 + 4)        #xy = es un list[] :.  xy[0]=ejeX ,  xy[1]=ejeY

turtle.colormode(255)                  # cambia a modo 0 a 255 colores
turtle.bgcolor('black')

for x in range(-90,+90,4):
   turtle.forward(x)
   turtle.left(90)
   turtle.forward(funY(x))
   turtle.dot(4,'white')
   turtle.right(180)
   turtle.forward(funY(x))
   turtle.right(90)
   turtle.forward(x)
   turtle.left(180)

time-time.sleep(10)

