class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        n=len(s)
        def backtrack(i,pre=[]):
            if i==n and len(pre)==4:
                ans.append(".".join(pre))
                return
            if i==n or len(pre)==4:
                return
            if s[i]=='0':
                backtrack(i+1,pre+["0"])
                return
            for j in range(i+1,min(n+1,i+4)):
                if int(s[i:j])<256:
                    backtrack(j,pre+[s[i:j]])
        backtrack(0)
        return ans