def get_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, n + 1, start):
                sieve[i] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]
pr=get_primes(10**5)
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        ans=r-l+1
        for x in pr:
            if x*x>=l and x*x<=r:
                ans-=1
        return ans