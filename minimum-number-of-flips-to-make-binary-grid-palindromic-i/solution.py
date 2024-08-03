class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=1
        for i in range(n):
            for j in range(m):
                ans+=grid[i][j]!=grid[n-i-1][j]
        ans2=1
        for i in range(n):
            for j in range(m):
                ans2+=grid[i][j]!=grid[i][m-j-1]
        return min(ans,ans2)//2