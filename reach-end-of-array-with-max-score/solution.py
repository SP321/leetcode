class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        x = 0
        ans = 0
        for i in range(n - 1):
            x = max(x, nums[i])
            ans += x
        return ans