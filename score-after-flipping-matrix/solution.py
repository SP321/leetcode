class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = (1 << m - 1) * n
        for j in range(1, m):
            cur = sum(grid[i][j] == grid[i][0] for i in range(n))
            ans += max(cur, n - cur) * (1 << m - 1 - j)
        return ans