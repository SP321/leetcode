class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx,dy in dirs:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid2[x][y]:
                    if grid1[x][y] == 0:
                        return 0
                    grid1[x][y] = 0
                    grid2[x][y] = 0
                    ans = dfs(x, y)
                    if ans == 0:
                        grid2[x][y] = 1
                        return 0
            return 1
        
        m, n = len(grid1), len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid1[i][j] and grid2[i][j]:
                    grid1[i][j] = 0
                    grid2[i][j] = 0
                    cur = dfs(i,j)
                    if cur == 0:
                        grid2[i][j] = 1
                    ans += cur
        return ans