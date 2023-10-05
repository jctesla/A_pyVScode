# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
screen = pygame.display.set_mode((400,300))

# Initializing Color=RED
color = (255,0,0)

running = True
while running:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  # Dibuja el fondo del lienzo Black
  screen.fill((0, 0, 0))
  
  x=10
  y=50  
  # Drawing Rectangle              x   y   w   h
  pygame.draw.rect(screen, color, (x , y, 80, 40))            
  
  # puedo declarar asi tambien
  # pygame.draw.rect(screen, color, pygame.Rect(x , y, 30, 30))            
  
  pygame.display.flip()
