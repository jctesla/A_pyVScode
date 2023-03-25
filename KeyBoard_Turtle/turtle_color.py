# NOTA:
# Lo importante en esta rutina es como se usa el colorn[x%6] p recorrer un pentagono, si quisieramos un hexagono
# podemos aumentar un color en colorn[] y en el calculo de colorn[x%7] ya q va de 1..7, y t.left(grados=60)

import turtle
colorn = ['#ff0000','#00ff00','#0000ff','#ff00ff','#ffff00','#00ffff']
colors = ['red','purple','blue','green','yellow','orange']
t = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(colorn[x%6])         #  el residuo de la division 0..360 % 6 = nos da un Nro que solo se mueve en el rango de 0 a 5 de un Arreglo.
    t.width(x/100 + 1)              # crea una escala incrmental 1.06
    t.forward(x)
    t.left(72)                      # 72g x 5lados = 306g Pentagono

#NOTA : 360 veces
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-
# 0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-0-1-2-3-4-5-