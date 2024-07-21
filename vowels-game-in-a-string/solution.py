class Solution:
    def doesAliceWin(self, s: str) -> bool:
        a=sum(1 for x in s if x in "aeiou")
        return a>0