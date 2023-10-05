# debes instalar el pygame si es posible crea un enviroment 1º
# Este ej, Pygame te proporciona una ventana donde puedes dibujar. A continuación, se muestra un ejemplo simple:

'''
Aui mas que todo es como detectar la colision entre figuras no esa del todo depurado pero si se puede jugar con movimiento basicos de colision.
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


# Elegir un bloque aleatorio
def addFig():
    figura ={
                'matriz':random.choice(tetrominoes),
                'coordX':(screen_width // 2) - 15,
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
screen_width = 390                          # multiplo de 30 q es la unidad minima de pixel de una figura.
screen_height = 600                         # multiplo de 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")


# Elegir una fig aleatorio
addFig()
figTetris = (arryFig[-1])                   # asigno la Ultima Fig Agregadas.


# Bucle principal del juego
running = True
counter=0
last_Y = []
w_Pixel=screen_width/30                     # nro maximo de pixeles q entra en el marco de ancho        
h_Pixel=screen_height/30                    # nro maximo de pixeles q entra en el marco de alto

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
    # recorremos todas la figuras almacenadas en arryFig.
    for fig in arryFig:
        #print(fig)                                                      
        for row in range(len(fig['matriz'])):                                   # cuantos rows tiene la matriz.
            for col in range(len(fig['matriz'][row])):                          # cuantos cols tiene la matriz.
                if fig['matriz'][row][col]:                                     # recorremos toda la matriz de (0,0) hasta (fin,fin).
                    pygame.draw.rect(screen, fig['color'], (fig['coordX'] + col * 30, fig['coordY'] + row * 30, 30, 30)) 
                    last_Y.append(len(fig['matriz'])*30)

    
    # fall_speed, esto debe ir en un thread
    time.sleep(0.05)
    counter+=1
    if counter>10:
        figTetris['coordY'] += 30
        counter=0

    
    # verify si la fig Actual = 'figTetris', 
    # si colisiona con otra que ya exista de bajada.
    h_nroBoxsTetris= len(figTetris['matriz'])
    h_figTetris = h_nroBoxsTetris*30
    w_nroBoxsTetris= len(figTetris['matriz'][0])
    w_figTetris = w_nroBoxsTetris*30
    flgFondo = False
    
    # arryFig[0:-1] esto es devido a q no se puede
    # comparar asi mismo sino con los 1ros agregados.

    for fig in arryFig[0:-1]:
        
        h_nroBoxsFig= len(fig['matriz'])
        h_fig = h_nroBoxsFig*30
        w_nroBoxsFig= len(fig['matriz'][0])
        w_fig = w_nroBoxsFig*30
        
        # Detector de Colison en 'X' Horizontales osn raras, pero hay.
        # buscamos en la misma area de 'X': nota fig['matriz'][0][0] valida si es 0 o 1
        xTi = figTetris['coordX']
        xTf = figTetris['coordX'] + w_figTetris
        xFi = fig['coordX']
        xFf = fig['coordX'] + w_fig
        
        if (xTi >= xFi) & (xTi < xFf) | (xTf >= xFi) & (xTf < xFf):
            # detectar Colison en 'Y', Veticales
            yTi = figTetris['coordY']
            yTf = figTetris['coordY'] + h_figTetris
            yFi = fig['coordY']
            yFf = fig['coordY'] + h_fig
            
            for r in range(h_nroBoxsTetris):
                for c in range(w_nroBoxsTetris):
                    if (figTetris['matriz'][r][c] == 1) & (yTi+((r+1)*30) > yFi):
                        print('**collision**')
                        addFig()                                    # agrego una nueva fig aleatoria.
                        figTetris = (arryFig[-1])                   # asigno la Ultima Fig Agregadas.
                        flgFondo = True
                        break


    # la fig llega al fondo.
    # len(figTetris['matriz']) nos da la altura dela figura, es decir el nro de rows x su size
    if not(flgFondo):
        if figTetris['coordY'] > (screen_height - len(figTetris['matriz'])*30):
            figTetris['coordY'] = screen_height - len(figTetris['matriz'])*30           # regulo su posicion no exeda del limite inferior
            print(figTetris)
            addFig()                                    # genero y agrego una nueva fig aleatoria.
            figTetris = (arryFig[-1])                   # asigno la Ultima Fig Agregadas.


        
    pygame.display.flip()
    
    

pygame.quit()
