import neopixel
from machine import Pin
import time
import LEDPattern
import MyBitmaps

class Character:
    char = 0
    xbot = 0
    ybot = 0
    lp = 0
    bm = []

    def __init__(self, lp, xbot, ybot, char):
        self.lp = lp
        self.xbot = xbot
        self.ybot = ybot
        self.char = char
        self.bm = MyBitmaps.bm[char]

    def getBitMap(self):
        return self.bm

    def __setchar__(self, colour):
        bm = self.getBitMap()
        lp = self.lp
        for xa in range(4,-1,-1):
            for ya in range(3):
                if bm[xa][ya] == 1:
                    lp.setPixel(self.xbot + (4-xa), self.ybot + ya, colour)

    def setchar(self):
        self.__setchar__(self.lp.WHITE)

    def unsetchar(self):
        self.__setchar__(self.lp.BLACK)

class CharacterGroup:
    mystr = ""
    lp = 0
    chars = []

    def __init__(self, lp, xbot, ybot, mystr):
        self.mystr = mystr
        self.lp = lp
        self.xbot = xbot
        self.ybot = ybot
        self.clearchars()
        self.setchars(mystr)

    def clearchars(self):
        self.mystr = ""
        self.chars = []

    def setchars(self, mystr):
        self.mystr = mystr
        nstr = mystr
        d = 0
        while len(nstr) > 0:
            c = nstr[0]
            nstr = nstr[1:]
            self.chars.append(Character(self.lp, self.xbot, self.ybot + d, c))
            d = d + 4

    def displayOn(self):
        for n in self.chars:
            n.setchar()

    def displayOff(self):
        for n in self.chars:
            n.unsetchar()

class myDisplay:
    cg = []
    lp = 0

    def __init__(self, lp):
        self.lp = lp

    def setchars(self, xbot, ybot, mystr):
        cg = self.getCharGroup(xbot, ybot)
        if cg != False and cg.mystr == mystr:
            return
        if cg != False:
            self.cg.remove(cg)
        cg = CharacterGroup(self.lp, xbot, ybot, mystr)
        self.cg.append(cg)
    
    def getCharGroup(self, xbot, ybot):
        for cg in self.cg:
            if cg.xbot == xbot and cg.ybot == ybot:
                return cg
        return False
    
    def isString(self, xbot, ybot, mystr):
        cg = self.getCharGroup(xbot, ybot)
        if cg != False and cg.mystr == mystr:
            return True
        return False
    
    def displayOn(self):
        for cg in self.cg:
            cg.displayOn()
            
    def displayOff(self):
        for cg in self.cg:
            cg.displayOff()
            
class myClock:
    
    def __init__(self, lp):
        self.myd = myDisplay(lp)
        self.setCurrentTime()
        
    def setCurrentTime(self):
        self.myd.displayOff()
        month, day, hour, minute = time.localtime()[1:5]
        self.myd.setchars(10, 0, f'{hour:02}')
        self.myd.setchars(10, 9, f'{minute:02}')
        self.myd.setchars(2, 0, f'{day:02}')
        self.myd.displayOn()
