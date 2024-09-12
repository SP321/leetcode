class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        height = [0] * m
        q = []
        for i in range(min(m, n), 0, -1):
            heapq.heappush(q, (1, 1, -i, height))

        while q:
            guess, moves, neg_size, height = heapq.heappop(q)
            size = -neg_size
            idx = height.index(min(height))
            height = height[:]
            for i in range(size):
                height[idx + i] += size
            if all(h == n for h in height):
                return moves
            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx + 1
            while ridx < m and height[ridx] == min_height:
                ridx += 1
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                heapq.heappush(q, (moves + 1 + len(set(h for h in height if h < n)), 
                                moves + 1, -i, height))