class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(n):
            if n<0:
                return 0
            if n==0:
                return 1
            ans=0
            for i in range(1,n+1):
                ans=max(ans,i*dp(n-i))
            return ans
        ans=0
        for i in range(1,n):
            ans=max(ans,i*dp(n-i))
        return ans