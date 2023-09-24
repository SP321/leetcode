class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c=s.count('1')
        return '1'*(c-1)+'0'*(len(s)-c)+'1'