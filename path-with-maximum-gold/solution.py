class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def backtrack(i,j):
            if not (0<=i<n and 0<=j<m):
                return 0
            if grid[i][j]==0:
                return 0
            cur=grid[i][j]
            grid[i][j]=0
            ans=0
            for x,y in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
                ans=max(ans,backtrack(x,y))
            grid[i][j]=cur
            return ans+cur
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    ans=max(ans,backtrack(i,j))
        return ans