class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n=len(s1)
        m=len(s2)
        @cache
        def dfs(i,j):
            if i==n:
                return 0
            if j==m:
                return 0
            if s1[i]==s2[j]:
                return dfs(i+1,j+1)+ord(s1[i])*2
            return max(
                dfs(i+1,j),
                dfs(i,j+1)
            )
        return sum(map(ord,s1+s2))-dfs(0,0)
        