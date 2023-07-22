class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        @lru_cache(None)
        def dp(i, j, steps):
            if steps == 0:
                return 1 if 0 <= i < n and 0 <= j < n else 0
            
            ans = 0
            for dx, dy in moves:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n:
                    ans += dp(x, y, steps - 1) / 8.0
            return ans

        return dp(row, column, k)