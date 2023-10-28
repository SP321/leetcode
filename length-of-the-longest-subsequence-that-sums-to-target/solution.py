class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0
        
        for i in range(n - 1, -1, -1):
            for t in range(1, target + 1):
                dp[i][t] = dp[i + 1][t]
                
                if t - nums[i] >= 0:
                    include = dp[i + 1][t - nums[i]]
                    if include != -1:
                        dp[i][t] = max(dp[i][t], 1 + include)
        return dp[0][target]