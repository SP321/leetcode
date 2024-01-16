class RandomizedSet:

    def __init__(self):
        self.pos={}
        self.x=[]

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val]=len(self.x)
        self.x.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        p=self.pos[val]
        del self.pos[val]
        if p!=len(self.x)-1:
            self.pos[self.x[-1]]=p
            self.x[p]=self.x[-1]
        self.x.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.x)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()