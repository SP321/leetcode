class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        dp=[[-1]*m for i in range(n)]
        def dfs(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=0
            if j<m-1:
                if grid[i][j]<grid[i][j+1]:
                    dp[i][j]=max(dp[i][j],1+dfs(i,j+1))
                if i>0 and grid[i][j]<grid[i-1][j+1]:
                    dp[i][j]=max(dp[i][j],1+dfs(i-1,j+1))
                if i<n-1 and grid[i][j]<grid[i+1][j+1]:
                    dp[i][j]=max(dp[i][j],1+dfs(i+1,j+1))
            return dp[i][j]
            
        for i in range(n):
            ans=max(ans,dfs(i,0))
        return ans