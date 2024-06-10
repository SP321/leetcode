class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans=0
        n=len(grid)
        for i in range(n):
            grid[i].sort(reverse=True)
        for j in range(len(grid[0])):
            cur=0
            for i in range(n):
                cur=max(cur,grid[i][j])
            ans+=cur
        return ans