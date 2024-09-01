class Solution:
    def checkTwoChessboards(self, a: str, b: str) -> bool:
        def f(s):
            a=ord(s[0])-ord('a')
            b=int(s[1])
            return a+b
        return f(a)%2==f(b)%2