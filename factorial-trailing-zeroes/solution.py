class Solution:
    def trailingZeroes(self, n: int) -> int:
        return sum(n//(5**x) for x  in range(1,6))