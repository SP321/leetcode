class Solution:
    def minimumCost(self, s: str) -> int:
        ans=0
        n=len(s)
        if n==1:
            return 0
        l,r=s[:n//2],s[n//2:]
        def solve(s):
            n=len(s)
            a=0
            for i in range(n-1):
                if s[i]!=s[i+1]:
                    a+=i+1
            return a
        ans+=solve(l)
        ans+=solve(r[::-1])
        if l[-1]!=r[0]:
            ans+=len(l)
        return ans