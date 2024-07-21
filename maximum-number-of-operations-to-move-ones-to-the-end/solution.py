class Solution:
    def maxOperations(self, s: str) -> int:
        n=len(s)
        one=0
        ans=0
        for i in range(len(s)-1):
            if s[i]=="1":
                one+=1
                if s[i+1]=='0':
                    ans+=one
        return ans