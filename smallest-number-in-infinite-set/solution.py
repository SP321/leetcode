class SmallestInfiniteSet:

    def __init__(self):
        self.i = 1
        self.pq = []
        self.s = set()

    def popSmallest(self) -> int:
        if len(self.pq):
            j = heapq.heappop(self.pq)
            self.s.remove(j)
            return j
        result = self.i
        self.i += 1
        return result      

    def addBack(self, num: int) -> None:
        if num >= self.i:
            return
        if num not in self.s:
            self.s.add(num)
            heapq.heappush(self.pq, num)
