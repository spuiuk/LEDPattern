import neopixel
from machine import Pin
import time
import random
import LinesDesign

xres = 16
yres = 16
xdir = 1
ydir = 1
pin = 22
np = neopixel.NeoPixel(Pin(pin), xres * yres)

p = LinesDesign.linesMulti(np, xres, yres)
p.setOrigin(4)
p.clear()
p.build()
p.show()

while p.step():
    p.sleep()
    p.show()
