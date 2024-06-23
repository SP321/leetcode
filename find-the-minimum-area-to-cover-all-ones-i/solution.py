class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        x1,y1,x2,y2=inf,inf,0,0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    x1=min(x1,i)
                    y1=min(y1,j)
                    x2=max(x1,i)
                    y2=max(y2,j)
        return (x2-x1+1)*(y2-y1+1)