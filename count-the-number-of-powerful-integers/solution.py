class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def solve(lim):
            x=str(lim)
            L=[x,'9'*len(x)]
            @cache
            def dp(i, j):
                mx=L[j]
                if len(mx) - i == len(s):
                    return mx[-len(s):] >= s
                if len(mx) - i < len(s):
                    return 0
                ans = 0
                for dig in range(limit+1):
                    if str(dig) <= mx[i]:
                        next_j=1 if j==1 or str(dig) < mx[i] else 0
                        ans += dp(i + 1, next_j)
                return ans
            return dp(0,0)

        return solve(finish) - solve(start - 1)