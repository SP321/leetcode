class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+3)
        for i in range(n):
            dp[i+2]=max(dp[i+1],dp[i]+nums[i])
        return max(dp[n:])