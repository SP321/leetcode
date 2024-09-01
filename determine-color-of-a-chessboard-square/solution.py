class Solution:
    def squareIsWhite(self, c: str) -> bool:
        a=ord(c[0])-ord('a')
        b=int(c[1])
        return (a+b)&1==0