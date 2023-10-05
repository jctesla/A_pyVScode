# pygame zero
import pgzrun
from pgzhelper import *

alien = Actor('alien')
alien.images = ['alien_01','alien_02','alien_03']
alien.fps = 10
alien.pos = (100,100)
alien.anchor = (0.5,0.5)


def update():
  alien.animate()
  
  

def draw():
  alien.draw()
  
def on_mouse_down(pos):
    if alien.collidepoint_pixel(pos):
      print(f"pos={pos}...Eek!")
      #sounds.eep.play()
      alien.image = 'alien_hurt'
      time.sleep(1)
      alien.image = 'alien'

 

pgzrun.go()

'''
for i in range(10):
  alien.angle = -(i*10) 
  alien.move_forward(30)  # Moves towards the North-East
  pgzrunx.update(y)
  time.sleep(0.5)
'''  
