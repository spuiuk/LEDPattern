import neopixel
from machine import Pin
import BounceDesign

xres = 16
yres = 16
xdir = 1
ydir = 1
pin = 22
np = neopixel.NeoPixel(Pin(pin), xres * yres)

p = BounceDesign.bounceMulti(np, xres, yres)
p.clear()
p.build()
p.show()

while p.step():
    p.sleep()
    p.show()
