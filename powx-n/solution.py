class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = -n
        result = self.myPow(x * x, n>>1)
        if n&1==1:
            result *= x
        return result