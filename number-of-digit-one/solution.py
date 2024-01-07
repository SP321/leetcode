class Solution:
    def countDigitOne(self, n: int) -> int:
        x=str(n)
        L=[x,'A'*len(x)]
        @cache
        def dp(i, j,c):
            mx=L[j]
            if i == len(x):
                return c
            ans = 0
            for dig in range(10):
                if str(dig) <= mx[i]:
                    next_j=1 if str(dig) < mx[i] else 0
                    ans += dp(i + 1, next_j,c+(dig==1))
            return ans
        return dp(0,0,0)