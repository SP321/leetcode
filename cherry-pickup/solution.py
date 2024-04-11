class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        @cache
        def dp(x1,y1,x2):
            y2=x1+y1-x2
            cur=grid[x1][y1]
            if x1!=x2:
                cur+=grid[x2][y2]
            if x1+y1==(n-1)*2:
                return cur

            ans=-inf
            for dx,dy in [[0,1],[1,0]]:
                ax=x1+dx
                ay=y1+dy
                if 0<=ax<n and 0<=ay<n and grid[ax][ay]!=-1:
                    for dx,dy in [[0,1],[1,0]]:
                        bx=x2+dx
                        by=y2+dy
                        if 0<=bx<n and 0<=by<n and grid[bx][by]!=-1:
                            ans=max(ans,dp(ax,ay,bx))
            return ans+cur
        ans=dp(0,0,0)
        return ans if ans!=-inf else 0
        