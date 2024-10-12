def get_primes(n):
    p = 3
    sieve = [1 for _ in range(n+1)]
    while p*p <= n:
        if sieve[p]:
            for x in range(p*p, n+1, 2*p):
                sieve[x] = 0
        p += 2
    ret = [2]
    for i in range(3, n+1, 2):
        if sieve[i]:
            ret.append(i)
    return ret

pr=get_primes(1000)
ans={}
for x in range(1000):
    if x|(x+1) in pr and x|(x+1) not in ans:
        ans[x|(x+1)]=x
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        return [ans[x] if x in ans else -1 for x in nums]