class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        d=defaultdict(list)
        n=len(heightMap)
        m=len(heightMap[0])

        heap = []
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
                    
                    
        level, ans = 0, 0
        
        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(height, level)

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < n and 0 <= j < m and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    
                    if heightMap[i][j] < level:
                        ans += level - heightMap[i][j]
                        
                    heightMap[i][j] = -1
        return ans