class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(1,n):
            x,y=nsmallest(2,grid[i-1])
            for j in range(n):
                grid[i][j]+=x if grid[i-1][j]!=x else y
        return min(grid[-1])