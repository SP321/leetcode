class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=-inf
        for i in range(n):
            for j in range(m):
                if i>0:
                    ans=max(ans,grid[i][j]-grid[i-1][j])
                if j>0:
                    ans=max(ans,grid[i][j]-grid[i][j-1])
                if i>0:
                    grid[i][j]=min(grid[i][j],grid[i-1][j])
                if j>0:
                    grid[i][j]=min(grid[i][j],grid[i][j-1])
        return ans