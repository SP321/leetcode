class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n=len(s)
        @cache
        def dp(i):
            if i==n:
                return 0
            ans=inf
            c=Counter()
            for j in range(i,n):
                c[s[j]]+=1
                if len(set(c.values()))==1:
                    ans=min(ans,dp(j+1)+1)
            return ans
        return dp(0)