import neopixel
from machine import Pin
import time
import random
import LEDPacMan

xres = 16
yres = 16
xdir = 1
ydir = 1
pin = 22
np = neopixel.NeoPixel(Pin(pin), xres * yres)

p = LEDPacMan.PacManPattern(np, xres, yres)
p.setOrigin(4)
p.clear()
p.build()
p.show()

while True:
    time.sleep(1)
    p.step()
    p.show()


