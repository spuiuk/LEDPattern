import time

class LEDPattern:
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW = (255,255,0)
    xres = 0
    yres = 0
    n = 0
    np = 0
    f_origin = 0

    def __init__(self, np, xres, yres, origin=0):
        self.xres = xres
        self.yres = yres
        self.np = np
        self.n = np.n
        self.setOrigin(origin)

    def clear(self):
        for i in range(self.n):
            self.np[i] = self.BLACK

    def mapPixel(self, x, y):
        x, y = self.f_origin(x, y)
        if x % 2 == 0:
            i = self.xres * x
            i = i + y
        else:
            i = (self.xres * (x+1)) - 1
            i = i - y
        return int(i)

    def setPixel(self, x, y, colour):
        #print(f'x,y {x},{y}')
        i = self.mapPixel(x,y)
        if i < self.n:
            self.np[i] = colour

    def show(self):
        self.np.write()

    def build(self):
        pass

    def step(self):
        pass

    def sleep(self):
        time.sleep(1)

    def __origin0__(self, x, y):
        return x,y

    def __origin1__(self, x, y):
        return (self.xres - y - 1), x

    def __origin2__(self, x, y):
        return (self.xres - x - 1), (self.yres - y - 1)

    def __origin3__(self, x, y):
        return y, (self.xres - x - 1)

    def setOrigin(self, origin):
        if origin == 0:
            self.f_origin = self.__origin0__
        elif origin == 1:
            self.f_origin = self.__origin1__
        elif origin == 2:
            self.f_origin = self.__origin2__
        elif origin == 3:
            self.f_origin = self.__origin3__
