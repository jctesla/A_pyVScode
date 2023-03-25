import gtk
from random import shuffle

def callback(boton):
    (x, y), (bx, by) = boton.posicion, blanco.posicion
    if (x-bx, y-by) in [(-1,0), (1,0), (0,1), (0,-1)]:
        tabla.remove(boton)
        tabla.remove(blanco)
        tabla.attach(boton, bx, bx+1, by, by+1)
        tabla.attach(blanco, x, x+1, y, y+1)
        boton.posicion = (bx, by)
        blanco.posicion = (x, y)

tam     = 4
ventana = gtk.Window()
ventana.set_default_size(500, 500)
botones = [gtk.Button(str(i)) for i in range(1, tam * tam)]
blanco  = gtk.Button()
tabla   = gtk.Table(tam, tam, homogeneous=True)

shuffle (botones)

(x, y) = (0, 0)
for i in botones + [blanco]:
    if x == tam: x = 0; y += 1
    i.connect('clicked', callback)
    i.posicion = (x, y)
    tabla.attach(i, x, x+1, y, y+1)
    x += 1

ventana.connect('destroy', gtk.main_quit)
ventana.add(tabla)
ventana.set_title('Juego del '+str(tam*tam-1))
ventana.show_all()
blanco.hide()
gtk.main()