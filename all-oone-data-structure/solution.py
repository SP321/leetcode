from sortedcontainers import SortedList
class AllOne:

    def __init__(self):
        self.sl=SortedList()
        self.c=Counter()

    def inc(self, key: str) -> None:
        self.sl.discard((self.c[key],key))
        self.c[key]+=1
        self.sl.add((self.c[key],key))
        

    def dec(self, key: str) -> None:
        self.sl.discard((self.c[key],key))
        self.c[key]-=1
        if self.c[key]>0:
            self.sl.add((self.c[key],key))

    def getMaxKey(self) -> str:
        if len(self.sl)==0:
            return ""
        return self.sl[-1][1]

    def getMinKey(self) -> str:
        if len(self.sl)==0:
            return ""
        return self.sl[0][1]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()