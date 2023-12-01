class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        @cache
        def dfs(i,j):
            if j==m:
                return 1
            if i==n:
                return 0
            ans=dfs(i+1,j)
            if s[i]==t[j]:
                ans+=dfs(i+1,j+1)
            return ans
        return dfs(0,0)