class Solution:
    def isReachable(self, x: int, y: int) -> bool:
        g = gcd(x, y)
        return g & (g-1) == 0