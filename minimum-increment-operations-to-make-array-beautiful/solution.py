class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        @cache
        def dfs(i, j):
            if i == n:
                return 0
            if nums[i] >= k:
                j = i
            no_change = dfs(i + 1, j) if i - j <= 2 else float('inf')
            change = dfs(i + 1, i) + max(0, k - nums[i])
            return min(change, no_change)
        return dfs(0,-1)