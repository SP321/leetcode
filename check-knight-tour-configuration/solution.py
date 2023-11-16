class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        d=[0]*(n*n)
        for i in range(n):
            for j in range(n):
                d[grid[i][j]]=(i,j)
        prev=(-2,-1)
        for i in range(n*n):
            x,y=d[i]
            xx,yy=prev
            xdiff=abs(x-xx)
            ydiff=abs(y-yy)
            if min(xdiff,ydiff)!=1 or max(xdiff,ydiff)!=2:
                return False
            prev=d[i]
        return True
