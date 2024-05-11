class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pair = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        ans = inf
        s = 0
        h = []
        for x, y in pair:
            heapq.heappush(h, -y)
            s += y
            if len(h) > k: s += heapq.heappop(h)
            if len(h) == k: ans = min(ans, s * x)
        return ans