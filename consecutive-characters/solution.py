class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        c=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
                ans=max(ans,c)
            else:
                c=1
        return ans
        