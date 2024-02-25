class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def prime_factors(n):
            i = 2
            factors = set()
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.add(i)
            if n > 1:
                factors.add(n)
            return factors

        n = len(nums)
        s=DSU(max(nums)+1)
        for num in nums:
            for factor in prime_factors(num):
                s.union(num, factor)

        group = s.find(nums[0])
        for num in nums[1:]:
            if s.find(num) != group or num==1:
                return False
        return True
