ans = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(32) for c in range(32))
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return ans[n-1]
