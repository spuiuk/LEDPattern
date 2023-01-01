import time
import random
from LEDPattern import LEDPattern

class lines(LEDPattern):
    x = 0
    y = 0
    speed = 0
    count = 0

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)
        self.x = random.randint(0, xres)
        self.y = yres - 1
        self.speed = random.randint(1, 3)
        self.count = 0

    def build(self):
        self.setPixel(self.x, self.y, self.WHITE)

    def step(self):
        self.count = self.count + 1
        if self.count % self.speed != 0:
            return True
        self.setPixel(self.x, self.y, self.BLACK)
        self.y = self.y - 1
        if self.y < 0:
            return False
        self.setPixel(self.x, self.y, self.WHITE)
        return True

    def sleep(self):
        time.sleep_ms(20)

class lines2(LEDPattern):
    x = 0
    y = 0
    speed = 0
    count = 0

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)
        self.x = random.randint(0, xres)
        self.y = yres - 1
        self.speed = random.randint(1, 3)
        self.count = 0

    def build(self):
        self.setPixel(self.x, self.y, self.WHITE)

    def step(self):
        self.count = self.count + 1
        if self.count % self.speed != 0:
            return True

        ny = self.y - 1
        if ny+3< 0:
            return False

        if ny >= 0:
            self.setPixel(self.x, ny, self.RED)
        if ny+1 >= 0 and ny+1 < self.yres:
            self.setPixel(self.x, ny+1, self.GREEN)
        if ny+2 >= 0 and (ny+2) < self.yres:
            self.setPixel(self.x, ny+2, self.BLUE)
        if ny+3 >= 0 and (ny+3) < self.yres:
            self.setPixel(self.x, ny+3, self.BLACK)
        self.y = ny
        return True

    def sleep(self):
        time.sleep_ms(20)

class linesMulti(LEDPattern):
    arr = []
    xarr = []
    newLineProbability = 40
    num = -1000

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)
        self.arr = []
        for i in range(0, xres):
            self.xarr.append(i)

    def build(self):
        if self.num == 0:
            return
        if len(self.xarr) == 0:
            return
        f = True
        p = lines2(self.np, self.xres, self.yres)
        p.x = random.choice(self.xarr)
        self.xarr.remove(p.x)

        self.arr.append(p)
        self.num = self.num - 1

    def step(self):
        for p in self.arr:
            if p.step() == False:
                self.xarr.append(p.x)
                self.arr.remove(p)
        if random.randint(0,100) < self.newLineProbability:
            self.build()
        if self.num == 0 and len(self.arr) == 0:
            return False
        return True

    def sleep(self):
        time.sleep_ms(10)
