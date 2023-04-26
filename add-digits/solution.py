class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            a=0
            while num>0:
                a=a+num%10
                num=num//10
            num=a
        return num