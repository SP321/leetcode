class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n<2:
            return 0
        return n//2+self.numberOfMatches(n-n//2)