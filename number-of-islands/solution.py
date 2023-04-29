class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        n=len(grid)
        m=len(grid[0])
        def dfs(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return
            if grid[x][y]=="0":
                return
            grid[x][y]="0"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    ans+=1
                    dfs(i,j)
        return ans
