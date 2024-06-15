class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = []
        a = sorted(zip(profits, capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(a) and a[i][1] <= w:
                heappush(h, -a[i][0])
                i += 1
            if h:
                w -= heappop(h)
        return w