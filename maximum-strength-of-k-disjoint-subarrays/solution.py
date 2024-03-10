class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        for k2 in range(1, k+1):
            prev = dp.copy()
            for i in range(n-1,-1,-1):
                dp[i]=nums[i]*k2*(-1)**(k-k2) + max(dp[i+1], prev[i+1])
            dp[n-k2+1] = -math.inf
        return max(dp)
        