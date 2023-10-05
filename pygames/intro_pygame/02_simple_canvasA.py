# debes instalar el pygame si es posible crea un enviroment 1º
# Este ej, Pygame te proporciona una ventana donde puedes dibujar. A continuación, se muestra un ejemplo simple:
'''
Muestra como se mueve la figura cayendo; Este código muestra un bloque Tetris en el centro de la ventana de Pygame. 
El bloque actual se elige aleatoriamente entre los diferentes tipos de Tetrominos (I, O, T, L, J, S, Z), y se dibuja
en el lienzo en su posición actual (coordenadas x e y).

QUE HACER DESPUES?
Debes adaptar este código para que funcione dentro de la lógica de tu juego Tetris, incluyendo el manejo de las posiciones, colisiones, rotaciones
y movimientos de los bloques. También deberás implementar la lógica para borrar filas completas cuando sea necesario. Este código proporciona un 
punto de partida básico para el dibujo de los bloques Tetris en tu juego.

'''
import pygame
import random
import time

pygame.init()

# Configuración de la ventana
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Bloques Tetris
tetrominoes = [
    [[1, 1, 1, 1]],                    # I-piece
    [[1, 1], [1, 1]],                 # O-piece
    [[1, 1, 1], [0, 1, 0]],           # T-piece
    [[1, 1, 1], [1, 0, 0]],           # L-piece
    [[1, 1, 1], [0, 0, 1]],           # J-piece
    [[1, 1, 0], [0, 1, 1]],           # S-piece
    [[0, 1, 1], [1, 1, 0]]            # Z-piece
]

# Elegir un bloque aleatorio
figTetris = random.choice(tetrominoes)
color = random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])
x, y = screen_width // 2, 0

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibuja el fondo del lienzo
    screen.fill(BLACK)

    # Dibuja el bloque Tetris actual en su posición
    for row in range(len(figTetris)):                                                       # cuantos rows tiene la matriz nos da el height de la fig.
        for col in range(len(figTetris[row])):                                              # cuantos cols tiene la matriz.
            if figTetris[row][col]:                                                         # recorremos toda la matriz de (0,0) hasta (fin,fin).
                pygame.draw.rect(screen, color, (x + col * 30, y + row * 30, 30, 30))       # lo que hacemos es x c/row creamos una recta x1 hasta xf.
                                                                                            # de 30 en 30 pixeles.
                

    pygame.display.flip()
    time.sleep(0.5)
    figTetris = random.choice(tetrominoes)

pygame.quit()
