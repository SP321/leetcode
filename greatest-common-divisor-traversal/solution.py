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

        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, i, j):
            parent[find(parent, i)] = find(parent, j)

        n = len(nums)
        max_num = max(nums)
        parent = list(range(max_num + 1))

        for num in nums:
            factors = prime_factors(num)
            for factor in factors:
                union(parent, num, factor)

        group = find(parent, nums[0])
        for num in nums[1:]:
            if find(parent, num) != group or num==1:
                return False
        return True
