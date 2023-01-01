import math
from LEDPattern import LEDPattern

class CircularPattern(LEDPattern):
    origin = (0,0)
    r = 0

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)
        self.origin = (xres/2, yres/2)
        self.r = 0

    def _build_(self, colour):
        r = self.r
        (xo, yo) = self.origin
        for i in range(self.xres):
            x = i - xo
            y2 = r * r - x * x
            if y2 < 0:
                continue
            y = math.ceil(math.pow(y2, 0.5))
            self.setPixel(xo+x, yo+y, colour)
            self.setPixel(xo+x, yo-y, colour)

    def build(self):
        self._build_(self.WHITE)

    def step(self):
        (xo, yo) = self.origin
        r = self.r + 1
        self._build_(self.BLACK)
        if r > xo:
            return False
        self.r = r
        self.build()
        return True

class CircularPatternMulti(LEDPattern):
    num = 10
    count = 0
    spacing = 2
    arr = []

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)
        self.count = 0
        self.spacing = 2
        self.arr = []

    def build(self):
        if self.num == 0:
            return
        if self.count % self.spacing == 0:
            p = CircularPattern(self.np, self.xres, self.yres)
            self.arr.append(p)
            self.num = self.num -1

    def step(self):
        self.build()
        for p in self.arr:
            if p.step() == False:
                self.arr.remove(p)
        self.count = self.count + 1
        return True
