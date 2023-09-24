class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @cache
        def inflow(i, j):
            if i == 0 and j == 0:
                return poured
            if j < 0 or j > i:
                return 0
            left_overflow = max(0, inflow(i-1, j-1) - 1) / 2
            right_overflow = max(0, inflow(i-1, j) - 1) / 2
            return left_overflow + right_overflow
        return min(1, inflow(query_row, query_glass))