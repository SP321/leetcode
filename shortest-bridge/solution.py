class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        bfs = deque()
        def dfs(i, j):
            if i<0 or j<0 or i>=n or j>=n or grid[i][j]!=1:
                return
            grid[i][j] = 2
            bfs.append((i, j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        def f1():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        return
        f1()
        steps = 0
        while bfs:
            for _ in range(len(bfs)):
                i, j = bfs.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return steps
                        elif grid[ni][nj] == 0:
                            grid[ni][nj] = -1
                            bfs.append((ni, nj))
            steps += 1
        return 0