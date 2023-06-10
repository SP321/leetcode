class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans=0
        for i in range(n):
            x=[]
            repc=0
            for j in range(i,n):
                if len(x)>0 and s[j]==x[-1]:
                    repc+=1
                if repc==2:
                    break
                x.append(s[j])
            ans=max(ans,len(x))
        return ans