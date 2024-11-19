class Solution:
    def arrangeCoins(self, n: int) -> int:
        def check(x):
            return (x*x+x)//2>n
        x=bisect_left(range(n),True,key=check)
        if (x*x+x)//2==n:
            return x
        return x-1