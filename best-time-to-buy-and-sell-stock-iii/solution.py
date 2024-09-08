class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[inf, 0] for _ in range(3)]
        for price in prices:
            dp[1][0] = min(dp[1][0], price - dp[0][1])
            dp[1][1] = max(dp[1][1], price - dp[1][0])
            dp[2][0] = min(dp[2][0], price - dp[1][1])
            dp[2][1] = max(dp[2][1], price - dp[2][0])
        return dp[-1][-1]