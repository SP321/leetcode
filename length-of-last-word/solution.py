class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=0
        i=len(s)-1
        while s[i]==' ':
            i-=1
        while i>=0 and s[i]!=' ':
            ans+=1
            i-=1
        return ans