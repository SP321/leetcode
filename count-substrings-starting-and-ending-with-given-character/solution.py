class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n=s.count(c)
        return n*(n+1)//2
            