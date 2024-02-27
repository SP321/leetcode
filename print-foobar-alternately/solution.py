from threading import Event
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_ready=Event()
        self.bar_ready=Event()
        self.foo_ready.set()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_ready.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foo_ready.clear()
            self.bar_ready.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_ready.wait()

            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bar_ready.clear()
            self.foo_ready.set()
