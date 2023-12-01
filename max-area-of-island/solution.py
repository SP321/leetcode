class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        visited=set()
        ans=0

        def dfs(x,y):
            if x<0 or x>=n or y<0 or y>=m:
                return 0
            if grid[x][y]==0:
                return 0
            if (x,y) in visited:
                return 0
            visited.add((x,y))
            ans=1
            for xx,yy in [(x-1,y),(x+1,y),(x,y+1),(x,y-1)]:
                ans+=dfs(xx,yy)
            return ans
    
        for i in range(n):
            for j in range(m):
                ans=max(ans,dfs(i,j))
        return ans
