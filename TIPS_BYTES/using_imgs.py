# Create a one row image, that has all grey values from 0 to 255
import png;
f = open('ramp.png', 'wb')              # binary mode is important
w = png.Writer(256, 1, greyscale=True)
w.write(f, [range(256)])
f.close()