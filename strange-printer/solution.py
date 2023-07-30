class Solution:
    def strangePrinter(self, s: str) -> int:
        ans=len(set(s))
        n=len(s)
        @cache
        def dfs(i,j):
            if i > j:
                return 0
            ans = dfs(i+1, j) + 1
            for k in range(i+1, j+1):
                if s[i] == s[k]:
                    ans = min(ans, dfs(i+1, k-1) + dfs(k, j))
            return ans
        return dfs(0,n-1)