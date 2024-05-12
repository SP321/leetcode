class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(s.find(x)-t.find(x)) for x in ascii_lowercase)