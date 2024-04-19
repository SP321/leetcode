class RandomizedCollection:

    def __init__(self):
        self.a = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.a))
        self.a.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if len(self.idx[val]) == 0:
            return False
        remove, last = self.idx[val].pop(), self.a[-1]
        self.a[remove] = last
        self.idx[last].add(remove)
        self.a.pop()
        self.idx[last].remove(len(self.a))
        return True

    def getRandom(self) -> int:
        return random.choice(self.a)