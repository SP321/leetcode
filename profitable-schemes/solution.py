class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        md = 10**9 + 7
        dp = [[[0] * (minProfit + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0][0] = 1
        for j in range(1, m + 1):
            g, p = group[j - 1], profit[j - 1]
            for i in range(n + 1):
                for k in range(minProfit + 1):
                    dp[i][j][k] = dp[i][j - 1][k]
                    if i >= g:
                        prev_profit = max(0, k - p)
                        dp[i][j][k] = (dp[i][j][k] + dp[i - g][j - 1][prev_profit]) % md

        return dp[n][m][minProfit]


