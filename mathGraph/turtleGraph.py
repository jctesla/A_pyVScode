#NiceHexSpiral.py
import turtle
colorn=['#ff0000','#00ff00','#0000ff','#ff00ff','#ffff00','#00ffff']  #colores en hexa = #RGB
colors=['red','purple','blue','green','yellow','orange']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colorn[x%6])   #va generar un loop entre 0...5
    t.width(x/100+1)          #ancho de la linea se va engrozando la linea de 0.01 + 1 = 1.00, hasta 3.6 + 1 ) 4.59
    t.forward(x)              #hacia adelante en esa direccion segun angulo,
    t.left(72)                #gira a la Izq 72 grados = pentagono = 360/72, Hexagono = 360/59.
print("...Revise ya esta generado el Dibujo")    