import time
alien = Actor('alien')
#alien.pos = 100, 56
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos):
   if alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'
        time.sleep(1)
        alien.image = 'alien'



def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)    