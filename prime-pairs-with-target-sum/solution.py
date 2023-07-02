
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        sieve = [False, False] + [True] * (n - 1)
        p = 2
        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        primes = [p for p in range(2, n+1) if sieve[p]]
        pairs = []
        l = 0
        r = len(primes) - 1
        while l <= r:
            if primes[l] + primes[r] == n:
                pairs.append([primes[l], primes[r]])
                l += 1
                r -= 1
            elif primes[l] + primes[r] < n:
                l += 1
            else:
                r -= 1
        return pairs