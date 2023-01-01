from LEDPattern import *
import PacManBitmap

class PacManPattern(LEDPattern):
    origin = (0,0)
    r = 0
    designs = PacManBitmap.bm
    cur = 0

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)

    def _build_(self, pstr):
        for y in range(self.yres):
            for x in range(self.xres):
                c = pstr[(y*self.xres) + x]
                if (c == 'B'):
                    colour = self.BLACK
                elif (c == 'Y'):
                    colour = self.YELLOW
                elif (c == 'L'):
                    colour = self.BLUE
                elif (c == 'R'):
                    colour = self.RED
                else:
                    colour = self.BLACK
                self.setPixel(x, y, colour)

    def build(self):
        self._build_(self.designs[0])

    def _inc_cur_(self):
        cur = self.cur + 1
        if cur == len(self.designs):
            cur = 0
        self.cur = cur

    def step(self):
        self._inc_cur_()
        self._build_(self.designs[self.cur])
