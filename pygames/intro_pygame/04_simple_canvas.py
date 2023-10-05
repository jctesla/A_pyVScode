# debes instalar el pygame si es posible crea un enviroment 1º
# Este ej, Pygame te proporciona una ventana donde puedes dibujar. A continuación, se muestra un ejemplo simple:

'''
Detecta las teclas de Up, Dwn, Left y Right, mientras la figura sigue cayendo.
Up: Rotacion la Fig.
Left: mueve ala Izq.
Right: mueve a la Derecha.
Down: aumenta la velcoidad de caida.

1º Creamos un Obj Directory ej de Obj
figuraTetris ={
                'matriz':[[1, 1, 1], [0, 1, 0]],
                'coordX':screen_width // 2,
                'coordY':0,
                'color':'RED'
              }

2º Almacenamos las figuras en una Matriz en arryFig[], con la func=addFig():
arryFig =[
            {'matriz': [[0, 1, 0], [1, 1, 1]], 'coordX': 15, 'coordY': 540, 'color': (255, 255, 0)},
            {'matriz': [[1, 1, 0], [0, 1, 1]], 'coordX': 75, 'coordY': 540, 'color': (255, 0, 0)},
            {'matriz': [[1, 1], [1, 1]], 'coordX': 45, 'coordY': 540, 'color': (0, 255, 0)},
            {'matriz': [[1, 1], [1, 1]], 'coordX': 315, 'coordY': 540, 'color': (0, 255, 255)},
            {'matriz': [[1, 1, 0], [0, 1, 1]], 'coordX': 105, 'coordY': 540, 'color': (255, 0, 0)},
            {'matriz': [[1, 1, 1], [0, 0, 1]], 'coordX': 195, 'coordY': 540, 'color': (0, 255, 255)},
         ]
Pero solo vemos UNA figura a la vez, no varias.
'''

import pygame
import random
import numpy as np
import threading, time

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
    [[1, 1, 1, 1]],                         # I-piece            1=fila y 4=columns    
    [[1, 1], [1, 1]],                       # O-piece ó cubo.    2=fila y 2=columns
    [[1, 1, 1], [0, 1, 0]],                 # T-piece            2=fila y 3=columns
    [[1, 1, 1], [1, 0, 0]],                 # L-piece            2=fila y 3=columns
    [[1, 1, 1], [0, 0, 1]],                 # J-piece            2=fila y 3=columns
    [[1, 1, 0], [0, 1, 1]],                 # S-piece            2=fila y 3=columns
    [[0, 1, 1], [1, 1, 0]]                  # Z-piece            2=fila y 3=columns
]


# Elege una figura aleatoria, color aleatorio en la osicion x,y
def addFig():
    figura ={
                'matriz':random.choice(tetrominoes),
                'coordX':screen_width // 2,
                'coordY':0,
                'color':random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])
            }
    arryFig.append(figura)
    

# ej : [[1, 1, 1], [0, 1, 0]]
def rotate_tetromino(figura):
    npTetro = np.array(figura)
    npTetro = np.rot90(npTetro)
    return npTetro.tolist()


# alamcena un conjunto de Obj Diccionarios de figuras.
arryFig = []

#-------------- MAIN ----------------------------------
pygame.init()

# Configuración de la ventana
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")


# Elegir una fig aleatorio
addFig()
figTetris = (arryFig[-1])                   # asigno la Ultima Fig Agregadas.


# Bucle principal del juego
running = True
counter=0

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        # Manejo de eventos de teclado,                                             figuraTetris = es la ultima figug added y es un Diccionario
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:                                          # Mover el bloque Tetris hacia la izquierda
                figTetris['coordX'] -= 30                                           # Ajusta esto según el tamaño de tus bloques
            elif event.key == pygame.K_RIGHT:                                       # Mover el bloque Tetris hacia la derecha
                figTetris['coordX'] += 30                                           # Ajusta esto según el tamaño de tus bloques
            elif event.key == pygame.K_DOWN:                                        # Aumentar la velocidad de caída
                figTetris['coordY'] = figTetris['coordY'] + 60                      # Ajusta esto según la velocidad deseada
            elif event.key == pygame.K_UP:
                figTetris['matriz'] = rotate_tetromino(figTetris['matriz'])         # Rotar the last elemnt bloque Tetris.


    # Dibuja el fondo del lienzo
    screen.fill(BLACK)


    # Dibuja el bloque Tetris actual en su posición
    # ej figTetris = {'matriz': [[1, 1, 0], [0, 1, 1]], 'coordX': 200, 'coordY': 60, 'color': (0, 255, 255)}
    '''
        fig ={
                'matriz':[[1, 1, 1], [0, 1, 0]],
                'coordX':screen_width // 2,
                'coordY':0,
                'color':'RED'
            }
    '''
    print(figTetris)
    for row in range(len(figTetris['matriz'])):
        for col in range(len(figTetris['matriz'][row])):
            if figTetris['matriz'][row][col]:
                pygame.draw.rect(screen, figTetris['color'], (figTetris['coordX'] + col * 30, figTetris['coordY'] + row * 30, 30, 30))

   
    
    # fall_speed
    time.sleep(0.05)
    counter+=1
    if counter>10:
        figTetris['coordY'] += 10
        counter=0

    # la fig llega al fondo.
    if figTetris['coordY'] > (screen_height - 30):
        figTetris['coordY'] = screen_height - 30
        print(figTetris['matriz'])
        addFig()                                    # Elegir una fig aleatorio
        figTetris = (arryFig[-1])                   # asigno la Ultima Fig Agregadas.
        
    pygame.display.flip()
    
    

pygame.quit()
