class Solution:
    def makeStringGood(self, s: str) -> int:
        c=Counter(s)
        c=[c[ch] for ch in ascii_lowercase]
        ans=inf
        for target in range(max(c)+1):
            @cache
            def dp(i,carry):
                if i==26:
                    return 0
                cur=c[i]
                if cur==0:
                    return dp(i+1,0)
                ans=dp(i+1,cur)+cur
                if cur<target:
                    cur+=carry
                    cost=max(0,(target-cur))
                    ans=min(ans,dp(i+1,0)+cost)
                elif cur>=target:
                    diff=cur-target
                    ans=min(ans,dp(i+1,diff)+diff)
                return ans
            ans=min(ans,dp(0,0))
            dp.cache_clear()
        return ans