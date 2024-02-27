from threading import Event

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.print = [Event(),Event(),Event()]
        self.print[2].set()
        
    def zero(self, printNumber):
        for _ in range(self.n):
            self.print[2].wait()
            self.print[2].clear()
            printNumber(0)
            self.ct += 1
            self.print[self.ct % 2].set()
        
    def even(self, printNumber):
        for _ in range(self.n//2):
            self.print[0].wait()
            self.print[0].clear()
            printNumber(self.ct)
            self.print[2].set()
        
    def odd(self, printNumber):
        for _ in range((self.n+1)//2):
            self.print[1].wait()
            self.print[1].clear()
            printNumber(self.ct)
            self.print[2].set()