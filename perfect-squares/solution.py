class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def dp(i):
            ans = i
            j = 1
            while j*j<=i:
                ans = min(ans, dp(i-j*j) + 1)
                j+=1
            return ans
        return dp(n)