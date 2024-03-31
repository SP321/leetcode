class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=sum(int(y) for y in str(x))
        if x%s ==0:
            return s
        return -1