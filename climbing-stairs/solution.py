class Solution:
    dp = {}
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        if n not in self.dp:
            self.dp[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.dp[n]
