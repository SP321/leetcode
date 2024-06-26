mod=10**9 + 7
class Solution:
    @cache
    def rearrangeSticks(self, n: int, k: int) -> int:
        if n == k:
            return 1
        if k == 0:
            return 0
        return (self.rearrangeSticks(n - 1, k - 1) + self.rearrangeSticks(n - 1, k) * (n - 1)) % mod
