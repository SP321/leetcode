class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans=1
        c=1
        for i in range(1,len(s)):
            if ord(s[i])==ord(s[i-1])+1:
                c+=1
                ans=max(ans,c)
            else:
                c=1
        return ans
                
        