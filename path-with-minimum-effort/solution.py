from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        pq = PriorityQueue()
        pq.put((0, 0, 0))

        max_effort = 10**6
        efforts = [[max_effort] * m for _ in range(n)]
        efforts[0][0] = 0
        
        while not pq.empty():
            effort, x, y = pq.get()
            
            if effort > efforts[x][y]:
                continue
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        pq.put((new_effort, nx, ny))
        
        return efforts[n-1][m-1]