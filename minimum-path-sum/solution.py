class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        @cache
        def dfs(i,j):
            if i>n-1 or j>m-1:
                return float('inf')
            if i==n-1 and j==m-1:
                return grid[i][j];
            x=grid[i][j]
            return x+min(dfs(i+1,j),dfs(i,j+1))
        return dfs(0,0)