class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x=abs(x)
        rev = 0
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x //= 10
        ans=sign*rev
        if ans > 2**31-1 or ans < -2**31:
            return 0
        else:
            return ans