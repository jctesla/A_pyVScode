# NOTA:
# Lo importante en esta rutina es como se usa el colorn[x%6] p recorrer un pentagono.
# se automatiza el nro de lados de la fogura de 3 a 6, y se genera un color al dibujar los 360 de la fig.
import turtle
import msvcrt                                   # detectar el kyPress()

colorn = ['#ff0000','#00ff00','#0000ff','#ff00ff','#ffff00','#00ffff','#ffffff']
colors = ['red','purple','blue','green','yellow','orange']
t = turtle.Pen()
turtle.bgcolor('black')
nLdos = 6
grados = 360/nLdos
pcolor = 0
g=0

for x in range(360):
    t.pencolor(colorn[pcolor])                          # el residuo de la division 0..360 % 6 = nos da un Nro que solo se mueve en el rango de 0 a 5 de un Arreglo.
    t.width(x/100 + 1)                          # crea una escala incremental 1.06, el ancho de las lineas de dibujo.
    t.forward(x)
    t.left(grados)                              # 72g x 5lados = 306g Pentagono
    g += grados
    if g == 360:
        pcolor = x%(nLdos+1)
        g=0
    
    if msvcrt.kbhit():
       txtKey = msvcrt.getch().decode('UTF-8')  # lo Lee en formato de Bytes b''. y lo decode() p ver q letra de texto.
       if txtKey.upper() == 'F':
            print('Presiono Salir!')
            break

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