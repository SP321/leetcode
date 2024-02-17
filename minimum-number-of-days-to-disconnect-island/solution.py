class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def c(grid):
            ans=0
            n=len(grid)
            m=len(grid[0])
            def dfs(i,j,visited):
                if (i,j) in visited:
                    return
                if grid[i][j]==0:
                    visited.add((i,j))
                    return
                visited.add((i,j))
                dirs_4=[(-1,0),(1,0),(0,-1),(0,1)]
                for dx,dy in dirs_4:
                    if 0<=i+dx<=n-1 and 0<=j+dy<=m-1 and grid[i+dx][j+dy]==1:
                        dfs(i+dx,j+dy,visited)
            visited=set()
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==1 and (i,j) not in visited:
                        dfs(i,j,visited)
                        ans+=1
            return ans
        
        if c(grid)!=1:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]=0
                    if c(grid)!=1:
                        return 1
                    else:
                        grid[i][j]=1
        return 2