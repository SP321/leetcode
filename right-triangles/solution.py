class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        row_c=Counter()
        col_c=Counter()
        for i in range(n):
            for j in range(m):
                row_c[i]+=grid[i][j]
                col_c[j]+=grid[i][j]
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans+=(row_c[i]-1)*(col_c[j]-1)
        return ans
            