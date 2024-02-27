from threading import Barrier
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n + 1
        self.br = Barrier(4)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for cur in range(1, self.n):
            if cur % 3 == 0 and cur % 5 != 0:
                printFizz()
            self.br.wait()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for cur in range(1, self.n):
            if cur % 3 != 0 and cur % 5 == 0:
                printBuzz()
            self.br.wait()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for cur in range(1, self.n):
            if cur % 3 == 0 and cur % 5 == 0:
                printFizzBuzz()
            self.br.wait()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for cur in range(1, self.n):
            if cur % 3 != 0 and cur % 5 != 0:
                printNumber(cur)
            self.br.wait()