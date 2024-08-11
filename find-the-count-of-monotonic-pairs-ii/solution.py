class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n, m = len(nums), max(nums) + 1
        dp = [1] * m
        for i in range(1, n):
            dp2=[0]*len(dp)
            d = max(0, nums[i] - nums[i - 1])
            for j in range(d, nums[i] + 1):
                dp2[j] = (dp2[j - 1] + dp[j - d]) % mod
            dp = dp2
        return sum(dp) % mod