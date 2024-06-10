from sortedcontainers import SortedList
class Allocator:

    def __init__(self, n: int):
        self.a = SortedList([(-1, -1), (n, n)])
        self.b = defaultdict(list)


    def allocate(self, size: int, mID: int) -> int:
        for (_, x), (y, _) in pairwise(self.a):
            x, y = x + 1, y - 1
            if y - x + 1 >= size:
                self.a.add((x, x + size - 1))
                self.b[mID].append((x, x + size - 1))
                return x
        return -1


    def free(self, mID: int) -> int:
        ans = 0
        for x in self.b[mID]:
            self.a.remove(x)
            ans += x[1] - x[0] + 1 
        del self.b[mID]
        return ans

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)