class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    grid[i][j]=inf
                if grid[i][j]==1:
                    grid[i][j]=0
        for i in range(n):
            for j in range(n):
                if i>0:
                    grid[i][j]=min(grid[i-1][j]+1,grid[i][j])
                if j>0:
                    grid[i][j]=min(grid[i][j-1]+1,grid[i][j])
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i!=n-1:
                    grid[i][j]=min(grid[i+1][j]+1,grid[i][j])
                if j!=n-1:
                    grid[i][j]=min(grid[i][j+1]+1,grid[i][j])

        h=[(-grid[0][0],0,0)]
        vis=set([(0,0)])
        ans=inf
        while h:
            dist,x,y=heappop(h)
            ans=min(ans,-dist)
            if x==n-1 and y==n-1:
                return ans
            for xx,yy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=xx<n and 0<=yy<n and (xx,yy) not in vis:
                    vis.add((xx,yy))
                    heappush(h,(-grid[xx][yy],xx,yy))
        assert(False,"WTF")