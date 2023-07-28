class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        @cache
        def dfs(i, j):
            if i > j:
                return 0
            take_left=nums[i] - dfs(i + 1, j)
            take_right=nums[j] - dfs(i, j - 1)
            return max(take_left,take_right)
        return dfs(0, n - 1) >= 0