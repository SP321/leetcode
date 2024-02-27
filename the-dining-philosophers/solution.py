from threading import Semaphore, Lock

class DiningPhilosophers:
    
    def __init__(self):
        self.counter = Semaphore(4)
        self.locks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        with self.counter: 
            with self.locks[philosopher], self.locks[(philosopher-1) % 5]: 
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()