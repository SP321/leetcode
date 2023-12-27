class Solution:
    def countVowelStrings(self, n: int) -> int:
        m=5
        dp = [[0] *(m+1) for _ in range(n + 1)]
        for j in range(m):
            dp[n][j] = 1

        for i in range(n)[::-1]:
            for j in range(m):
                ans = 0
                for k in range(j + 1):
                    ans += dp[i + 1][k]
                dp[i][j] = ans
        return dp[0][m-1]

