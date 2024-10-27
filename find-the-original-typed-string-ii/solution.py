MOD = 10**9 + 7


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        if k > len(word):
            return 0
        if k == len(word):
            return 1
        a=[]

        start=0
        for i in range(1,len(word)+1):
            if i==len(word) or word[i]!=word[i-1]:
                a.append(i-start)
                start=i

        ans = prod(a)
        k -= len(a)
        if k <= 0:
            return ans % MOD

        dp0 = [0] * k
        dp0[0] = 1
        for x in a:
            dp1 = [0] * k
            for i in range(k):
                v = dp0[i]
                if i>0:
                    dp1[i] += dp1[i-1]
                dp1[i] += v
                if i + x< k:
                    dp1[i + x] -= v
            dp0 = dp1
        ans -= sum(dp0)
        ans %= MOD
        return ans
