class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n=len(grid)
        m=len(grid[0])
        q=[(-health+grid[0][0],0,0)]
        vis=set(q)
        while q:
            h,x,y=heappop(q)
            if h<0 and x==n-1 and y==m-1:
                return True
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                xx=x+dx
                yy=y+dy
                if 0<=xx<n and 0<=yy<m:
                    hh=h+grid[xx][yy]
                    if hh<0 and (hh,xx,yy) not in vis:
                        vis.add((hh,xx,yy))
                        heappush(q,(hh,xx,yy))
        return False