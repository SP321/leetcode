class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])

        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            if matrix[i][j] == 0:
                return 0
            return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
        return sum(dp(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 1)