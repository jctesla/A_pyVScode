# debes instalar el pygame si es posible crea un enviroment 1º
# Este ej, Pygame te proporciona una ventana donde puedes dibujar. A continuación, se muestra un ejemplo simple:
# documentacion : https://www.pygame.org/docs/ref/draw.html
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

color = (255,0,0)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibuja el fondo del lienzo Black
    screen.fill((0, 0, 0))

    # Dibuja otros elementos del juego aquí
    x=10
    y=50 
    # Drawing Rectangle              x   y   w   h
    pygame.draw.rect(screen, color, (x , y, 80, 40))   

    pygame.display.flip()

pygame.quit()


'''
(base) D:\phytonSpace\miBasic\A_pyVSCode\pygames>conda list pygame
# packages in environment at C:\ProgramData\Anaconda3:
#
# Name                    Version                   Build  Channel
pygame                    2.1.2                    pypi_0    pypi

'''