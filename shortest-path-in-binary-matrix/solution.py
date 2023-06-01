class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = deque([(0, 0, 1)])
        grid[0][0] = 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while q:
            x, y, d = q.popleft()
            if x == y == n - 1:
                return d
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny]:
                    grid[nx][ny] = 1
                    q.append((nx, ny, d+1))
        return -1