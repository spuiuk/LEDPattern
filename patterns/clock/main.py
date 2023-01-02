import neopixel
from machine import Pin
import time
import LEDPattern
import Character

xres = 16
yres = 16
xdir = 1
ydir = 1
pin = 22
np = neopixel.NeoPixel(Pin(pin), xres * yres)

p = LEDPattern.LEDPattern(np, xres, yres)
p.setOrigin(3)
p.clear()
p.build()

myc = Character.myClock(p)
p.show()

while 1:
    myc.setCurrentTime()
    p.show()
    time.sleep(20)

p.clear()
p.show()

