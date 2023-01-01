import time
from LEDPattern import LEDPattern

class Cycle(LEDPattern):
    cur = 0

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)
        self.cur = 0

    def build(self):
        i = self.cur
        if i < self.n:
            self.np[i] = self.RED
        if i > 0 and (i-1) < self.n:
            self.np[i-1] = self.GREEN
        if i > 1 and (i-2) < self.n:
            self.np[i-2] = self.BLUE
        if i > 2 and (i-3) < self.n:
            self.np[i-3] = self.BLACK

    def step(self):
        r = self.cur + 1
        if r > self.n + 3:
            return False
        self.cur = r
        self.build()
        return True

    def sleep(self):
        time.sleep_ms(15)

class cycleMulti(LEDPattern):
    spacing = 7
    num = -1
    arr = []
    count = 0

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)
        self.arr = []
        self.count = 0

    def build(self):
        if self.count % self.spacing == 0:
            p = Cycle(self.np, self.xres, self.yres)
            self.arr.append(p)
            if self.num > 0:
                self.num = self.num - 1

    def step(self):
        if self.num != 0:
            self.build()
        for p in self.arr:
            if p.step() == False:
                self.arr.remove(p)
        if len(self.arr) == 0:
            return False
        self.count = self.count + 1
        return True

    def sleep(self):
        time.sleep_ms(30)
