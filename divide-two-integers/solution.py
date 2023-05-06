class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        ans = 0
        dividend,divisor = abs(dividend),abs(divisor)
        while dividend >= divisor:
            c = 0
            while dividend >= (divisor << c):
                c += 1
            ans += (1 << (c - 1))
            dividend -= divisor << (c - 1)
        return -min(ans,int(1<<31)) if sign == -1 else min(ans,int((1<<31)-1))