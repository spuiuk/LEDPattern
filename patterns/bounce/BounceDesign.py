import time
import random
from LEDPattern import LEDPattern

class bounce(LEDPattern):
    dx = 1
    dy = 1
    color = (0,0,0)
    count = 0
    x = 0
    y = 0
    xspeed = 0
    yspeed = 0

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.count = 0
        self.x = random.randint(0, xres - 1)
        self.y = random.randint(0, yres - 1)
        self.xspeed = random.randint(1, 5)
        self.yspeed = random.randint(1, 5)

    def _build_(self, color):
        #print( f'{self.x}, {self.y}')
        self.np[self.mapPixel(self.x, self.y)] = color

    def build(self):
        self._build_(self.color)

    def step(self):
        self.count = self.count + 1
        nx = self.x
        ny = self.y
        if self.count % self.xspeed == 0:
            nx = self.x + self.dx
        if self.count % self.yspeed == 0:
            ny = self.y + self.dy

        if nx >= self.xres or nx < 0:
            self.dx = self.dx * -1
            nx = self.x + self.dx
        if ny >= self.yres or ny < 0:
            self.dy = self.dy * -1
            ny = self.y + self.dy
        self._build_(self.BLACK)
        self.x = nx
        self.y = ny
        self.build()
        return True

    def sleep(self):
        time.sleep_ms(5)

    def is_colliding(self, p):
        if p.x == self.x and p.y == self.y:
            return True
        return False

    def change_direction(self):
        self.xspeed = self.xspeed * -1
        self.yspeed = self.yspeed * -1

class bounceMulti(LEDPattern):
    num = 22
    arr = []

    def __init__(self, np, xres, yres):
        super().__init__(np, xres, yres)

    def build(self):
        for i in range(self.num):
            p = bounce(self.np, self.xres, self.yres)
            self.arr.append(p)

    def step(self):
        for p in self.arr:
            p.step()
        arr = self.arr[:]
        for p in arr:
            arr.remove(p)
            for q in arr:
                if p.is_colliding(q):
                    p.change_direction()
                    q.change_direction()
        return True

    def sleep(self):
        time.sleep_ms(15)
