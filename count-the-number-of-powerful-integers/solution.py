class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        @cache
        def dp(i, mx):
            if len(mx) - i == len(s):
                return mx[-len(s):] >= s
            if len(mx) - i < len(s):
                return 0
            ans = 0
            for dig in range(limit+1):
                if str(dig) <= mx[i]:
                    new_mx='A'*len(mx) if str(dig) < mx[i] else mx
                    ans += dp(i + 1, new_mx)
            return ans

        return dp(0,str(finish)) - dp(0,str(start - 1))