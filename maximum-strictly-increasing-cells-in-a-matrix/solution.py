class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        l = []
        heap_row = [[0] for i in range(m)]
        heap_col = [[0] for i in range(n)]
       
        for i in range(m):
            for j in range(n):
                l.append((mat[i][j], i, j))
    
        ans = 1
        l.sort()
        buffer = [(l[0], 1)]
        for i in range(1, len(l)):
            if buffer[0][0][0] != l[i][0]:
                while buffer:
                    current = buffer.pop()
                    _ , x, y = current[0]
                    heappush(heap_row[x], -current[1])
                    heappush(heap_col[y], -current[1])
                             
            current, x, y = l[i]
            
            r_max = heap_row[x][0]
            r_max_cost = - r_max
            r_cost = r_max_cost + 1
            
            c_max = heap_col[y][0]
            c_max_cost = - c_max
            c_cost = c_max_cost + 1
            
            cost = max(r_cost,c_cost)
            buffer.append((l[i], cost))
            ans = max(ans, cost)
       
        return ans