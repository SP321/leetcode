class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=0
        for x in groupby(word):
            b=len(list(x[1]))
            ans+=b-1
        return ans+1