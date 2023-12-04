class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        MOD = 10**9 + 7
        p="2357"
        if s[0] not in p or s[-1] in p:
            return 0
        @cache
        def dp(i, k):
            if k == 0 and i <= n:
                return 1
            if i >= n:
                return 0
            ans = dp(i+1, k)
            if s[i] in p and s[i-1] not in p:
                ans += dp(i+minLength, k-1)
            return ans % MOD
        return dp(minLength, k-1)



            