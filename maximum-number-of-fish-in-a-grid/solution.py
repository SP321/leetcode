class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        seen=[[False]*m for j in range(n)]
        ans=0
        def dfssum(i,j):
            if i<0 or j<0 or i>=n or j>=m or seen[i][j] or grid[i][j]==0:
                return 0
            seen[i][j]=True
            val=grid[i][j]+dfssum(i+1,j)+dfssum(i-1,j)+dfssum(i,j+1)+dfssum(i,j-1)
            grid[i][j]=0
            return val
        for i in range(n):
            for j in range(m):
                if(grid[i][j]>0):
                    ans=max(ans,dfssum(i,j))
        return ans
       
        