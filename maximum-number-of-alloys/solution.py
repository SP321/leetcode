class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ans = 0
        for x in composition:
            def is_valid(m):
                c = 0
                for i in range(n):
                    c += max(0, x[i] * m - stock[i]) * cost[i]
                return c<=budget
            left, right = 0, 10 ** 9
            while left <= right:
                m = (left + right) // 2
                if is_valid(m):
                    left = m + 1 
                else:
                    right = m - 1
            ans = max(ans, right)
        return ans