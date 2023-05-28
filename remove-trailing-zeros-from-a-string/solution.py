class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while len(num)>0 and num[-1]=='0':
            num=num[:-1]
        return num
        