# debes instalar el pygame si es posible crea un enviroment 1º
# Este ej, Pygame te proporciona una ventana donde puedes dibujar. A continuación, se muestra un ejemplo simple:
'''
es para testear y colocar ms codigo de depuracion.

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
    for row in range(len(figTetris)):
        for col in range(len(figTetris[row])):
            print(f'matriz figTetris={figTetris[row][col]}')
            if figTetris[row][col]:                                                     # los '1s' y '0s' determinan si entra a dibujar o no
                print(f'x={x + col * 30} / y={y + row * 30}')
                pygame.draw.rect(screen, color, (x + col * 30, y + row * 30, 30, 30))
                

    pygame.display.flip()
    print("------------------")
    time.sleep(2)
    

pygame.quit()
