class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        c=[Counter() for _ in range(m)]
        for i in range(n):
            for j in range(m):
                c[j][grid[i][j]]+=1
        @cache
        def dp(j,prev=None):
            if j==m:
                return 0
            ans=inf
            for d in range(10):
                if d!=prev:
                    ans=min(ans,n-c[j][d]+dp(j+1,d))
            return ans
        return dp(0)