class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        dx, dy, n = 0, 1, 0
        while len(ans) < rows * cols:
            for i in range(n // 2 + 1):
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                rStart, cStart = rStart + dx, cStart + dy
            dx, dy, n = dy, -dx, n + 1
        return ans