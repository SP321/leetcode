
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[0]*n for _ in range(n)]
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        moves_corner = [(-1,-1),(-1,1),(1,-1),(1,1)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    dist[i][j] = 0
                else:
                    dist[i][j] = float('inf')

        while queue:
            new_queue = deque()
            while queue:
                x, y = queue.popleft()
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        new_queue.append((nx, ny))
                for dx, dy in moves_corner:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 2:
                        dist[nx][ny] = dist[x][y] + 2
                        new_queue.append((nx, ny))
            queue = new_queue

        safeness = [[float('-inf')] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]
        queue = [(-safeness[0][0], 0, 0)]
        
        while queue:
            safe, x, y = heapq.heappop(queue)
            safe = -safe
            if (x, y) == (n-1, n-1):
                return safe
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    new_safeness = min(safe, dist[nx][ny])
                    if new_safeness > safeness[nx][ny]:
                        safeness[nx][ny] = new_safeness
                        heapq.heappush(queue, (-new_safeness, nx, ny))
                        