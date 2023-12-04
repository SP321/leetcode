class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        m=len(grid[0])
        @cache
        def dfs(i,j):
            if i==n:
                return j
            if grid[i][j]==1 and j<m-1 and grid[i][j+1]!=-1:
                return dfs(i+1,j+1)
            elif grid[i][j]==-1 and j>0 and grid[i][j-1]!=1:
                return dfs(i+1,j-1)
            return -1
        return [dfs(0,j) for j in range(m)]