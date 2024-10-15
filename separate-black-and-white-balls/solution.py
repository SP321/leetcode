class Solution:
    def minimumSteps(self, s: str) -> int:
        i=0
        ans=0
        for j in range(len(s)):
            if s[j]=='0':
                ans+=(j-i)
                i+=1
        return ans