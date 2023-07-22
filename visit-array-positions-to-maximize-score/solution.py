class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def dfs(i, y):
            if i == n:
                return 0
            if nums[i] % 2 == y:
                return max(nums[i] + dfs(i + 1, y), dfs(i + 1, (y + 1) % 2) - x)
            else:
                return max(nums[i] - x + dfs(i + 1, (y + 1) % 2), dfs(i + 1, y))
        return dfs(0, (nums[0]) % 2)