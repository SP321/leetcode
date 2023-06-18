class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[1]*m for i in range(n)]
        a=[]
        for i in range(n):
            for j in range(m):
                a.append((grid[i][j],i,j))
        a.sort()
        for val,i,j in a:
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if x>=0 and y>=0 and x<n and y<m and grid[x][y]>val:
                    dp[x][y]+=dp[i][j]
        return sum(sum(row) for row in dp)%int(1e9+7)

            
        