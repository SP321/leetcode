class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[target] = 0
        for i in nums:
            next_dp = defaultdict(int)
            for j in list(dp.keys()):
                if j >= i:
                    x = j - i
                    next_dp[x] = max(dp[j] + 1, dp[x])
            dp.update(next_dp)
        return dp[0] if dp[0] != 0 else -1