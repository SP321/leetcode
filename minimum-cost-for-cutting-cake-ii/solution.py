class Solution:
    def minimumCost(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        c1 = Counter(a)
        c2 = Counter(b)
        c = d = 1
        ans = 0
        for x in range(1000, -1, -1):
            if c1[x] or c2[x]:
                c += c1[x]
                ans += d * x * c1[x]
                d += c2[x]
                ans += c * x * c2[x]
        return ans