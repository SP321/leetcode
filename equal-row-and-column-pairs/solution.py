class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n= len(grid)
        d=defaultdict(int)
        for row in grid:
            d[tuple(row)]+=1
        ans=0
        for i in range(n):
            col=[grid[j][i] for j in range(n)]
            ans+=d[tuple(col)]
        return ans
