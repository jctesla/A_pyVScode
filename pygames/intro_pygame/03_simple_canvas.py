# debes instalar el pygame si es posible crea un enviroment 1º
# Este ej, Pygame te proporciona una ventana donde puedes dibujar. A continuación, se muestra un ejemplo simple:

'''
Detecta las teclas de Up, Dwn, Left y Right, mientras la figura sigue cayendo.
Up: Rotacion la Fig.
Left: mueve ala Izq.
Right: mueve a la Derecha.
Down: aumenta la velcoidad de caida.

Que Falta:
----------------------
Debes detectar cuando la figura toca el piso o detectar colisiones con otros bloques.
'''

import pygame
import random
import numpy as np
import time


# ej : [[1, 1, 1], [0, 1, 0]]
def rotate_tetromino(figTetris):
    npTetro = np.array(figTetris)
    npTetro = np.rot90(npTetro)
    return npTetro.tolist()


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

# Bloques Tetris 7 figuras
# las figuras se forman con maximo 2 filas y maximo 4 columnas. c/u se enciende =1 y apaga=0
tetrominoes = [
    [[1, 1, 1, 1]],                    # I-piece            1=fila y 4=columns    
    [[1, 1], [1, 1]],                  # O-piece ó cubo.    2=fila y 2=columns
    [[1, 1, 1], [0, 1, 0]],            # T-piece            2=fila y 3=columns
    [[1, 1, 1], [1, 0, 0]],            # L-piece            2=fila y 3=columns
    [[1, 1, 1], [0, 0, 1]],            # J-piece            2=fila y 3=columns
    [[1, 1, 0], [0, 1, 1]],            # S-piece            2=fila y 3=columns
    [[0, 1, 1], [1, 1, 0]]             # Z-piece            2=fila y 3=columns
]

# Elegir un bloque aleatorio
figTetris = random.choice(tetrominoes)
color = random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])
x, y = screen_width // 2, 0             # Dibuj la fig desde el centro hacia la derecha, up.


# Velocidad de caída (en píxeles por cuadro)
fall_speed = 30  # Ajusta esto según la dificultad

# Bucle principal del juego
running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        # Manejo de eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Mover el bloque Tetris hacia la izquierda
                x -= 30  # Ajusta esto según el tamaño de tus bloques
            elif event.key == pygame.K_RIGHT:
                # Mover el bloque Tetris hacia la derecha
                x += 30  # Ajusta esto según el tamaño de tus bloques
            elif event.key == pygame.K_DOWN:
                # Aumentar la velocidad de caída
                y += 60  # Ajusta esto según la velocidad deseada
            elif event.key == pygame.K_UP:
                # Rotar el bloque Tetris
                figTetris = rotate_tetromino(figTetris)
                

    # Restablecer la velocidad de caída
    # fall_speed = 30

    # Dibuja el fondo del lienzo
    screen.fill(BLACK)

    # Dibuja el bloque Tetris actual en su posición
    for row in range(len(figTetris)):
        for col in range(len(figTetris[row])):
            if figTetris[row][col]:
                pygame.draw.rect(screen, color, (x + col * 30, y + row * 30, 30, 30))


    # Restablecer la velocidad de caída
    #fall_speed = 30
    y += 1

    pygame.display.flip()
    time.sleep(0.05)
    

pygame.quit()
