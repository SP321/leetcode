class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        n,m=m,n
        grid=[[0]*m for _ in range(n)]
        for x,y in walls:
            grid[x][y]=1
        for x,y in guards:
            grid[x][y]=1
            for j in range(y+1,m):
                if grid[x][j] in [1,2]:
                    break
                grid[x][j]=2
            for j in range(y-1,-1,-1):
                if grid[x][j] in [1,2]:
                    break
                grid[x][j]=2
            for i in range(x+1,n):
                if grid[i][y] in [1,3]:
                    break
                grid[i][y]=3
            for i in range(x-1,-1,-1):
                if grid[i][y] in [1,3]:
                    break
                grid[i][y]=3
        ans=0
        for i in range(n):
            for j in range(m):
                ans+=grid[i][j]==0
        return ans            