MOD = 10**9 + 7
@cache
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1) % MOD

class Solution:

    def numberOfSequence(self, n: int, sick: List[int]) -> int:

        sick=[-1]+sick+[n]
        ans=fact(sum([y-x-1 for x,y in pairwise(sick)]))
        ans %= MOD

        for i,(x,y) in enumerate(pairwise(sick)):
            if y-x-1>0:
                ans *= pow(fact(y-x-1),-1, MOD)
                ans %= MOD
                if i!=0 and i!=len(sick)-2:
                    ans *= pow(2,y-x-2, MOD)
                    ans %= MOD
        return ans