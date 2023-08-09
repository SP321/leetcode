class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        visited = set()
        queue = [(grid[0][0], grid[0][0], 0, 0)]
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            max_val_so_far, val, x, y = heapq.heappop(queue)
            if (x, y) == (n-1, n-1):
                return max_val_so_far
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(queue, (max(max_val_so_far, grid[nx][ny]), grid[nx][ny], nx, ny))
                    
        return -1