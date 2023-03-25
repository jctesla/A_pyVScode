# draw a box in 4 colors, using number form 0 to 255
import time
import turtle

turtle.colormode(255)           # cambia a modo 0 a 255 colores

# use forward by 100 (default = black)
turtle.forward(100)

# change the color of turtle
turtle.color("red")

# use forward by 100 in 90 degrees
# right (color = red)
turtle.right(90)
turtle.forward(100)

# change the color of turtle
turtle.color(41,41,253)

# use forward by 100 in 90 degrees
# right (color = blue)
turtle.right(90)
turtle.forward(100)

# change the color of turtle
turtle.color(41,253,41)

# use forward by 100 in 90 degrees
# right (color = green)
turtle.right(90)
turtle.forward(100)

time-time.sleep(4)

