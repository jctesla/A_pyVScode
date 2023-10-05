# pygame zero
import pygame
import time
import pgzrun
from pgzhelper import *

'''
# Initializing Pygame
pygame.init()

# Initializing surface
screen = pygame.display.set_mode((400,300))
'''

alien = Actor('alien')
alien.flip_x = True

alien.scale = 0.5  # Half size
#alien.scale = 2    # Double size

alien.angle = -45
alien.move_forward(60)  # Moves towards the North-East


def draw():
  alien.draw()

pgzrun.go()
