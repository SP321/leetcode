class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        ans=0
        rmax=[max(row) for row in grid]
        cmax=[max(grid[x][j] for x in range(n)) for j in range(n)]
        for i in range(n):
            for j in range(n):
                ans+=min(rmax[i],cmax[j])-grid[i][j]
        return ans