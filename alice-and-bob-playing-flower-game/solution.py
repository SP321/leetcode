class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        e1=n//2
        o1=e1+(n&1)
        e2=m//2
        o2=e2+(m&1)
        return o1*e2+e1*o2