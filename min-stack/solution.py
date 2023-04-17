class MinStack:
    def __init__(self):
        self.mi=[2**31]
        self.a=[0]

    def push(self, val: int) -> None:
        if val<=self.mi[-1]:
            self.mi.append(val)
        self.a.append(val)

    def pop(self) -> None:
        if self.a[-1]==self.mi[-1]:
            self.mi.pop()
        return self.a.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.mi[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()