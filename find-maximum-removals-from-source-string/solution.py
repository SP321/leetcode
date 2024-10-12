class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n = len(source)
        m = len(pattern)
        st=set(targetIndices)
        cost=[1 if i in st else 0 for i in range(n)]
        @cache
        def dp(i,j):
            if j==m:
                if i==n:
                    return 0
                return dp(i+1,j)+cost[i]
            if i==n:
                return -inf
            ans=dp(i+1,j)+cost[i]
            if source[i]==pattern[j]:
                ans=max(ans,dp(i+1,j+1))
            return ans

        ans= dp(0,0)
        dp.cache_clear()
        return ans