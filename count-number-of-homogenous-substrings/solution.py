class Solution:
    def countHomogenous(self, s: str) -> int:
        n=len(s)
        dp=[1 for i in s]
        for i in range(1,n):
            if s[i]==s[i-1]:
                dp[i]+=dp[i-1]
                dp[i]%=10**9+7
        return sum(dp)%(10**9+7)