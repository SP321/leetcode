class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def get_area(rect):
            a, b, c, d = rect
            x1, y1, x2, y2 = inf,inf, -1, -1
            for i in range(a, c + 1):
                for j in range(b, d + 1):
                    if grid[i][j]:
                        x1 = min(x1, i)
                        y1 = min(y1, j)
                        x2 = max(x2, i)
                        y2 = max(y2, j)
            if x1 ==inf:
                return 0
            return (x2 - x1 + 1) * (y2 - y1 + 1)
        
        def iter_splits(rect):
            x1, y1, x2, y2 = rect
            for i in range(x1, x2):
                rect1 = (x1, y1, i, y2)
                rect2 = (i + 1, y1, x2, y2)
                yield rect1, rect2
            for j in range(y1, y2):
                rect1 = (x1, y1, x2, j)
                rect2 = (x1, j + 1, x2, y2)
                yield rect1, rect2
        
        def solve(rect, splits=2):
            if splits == 0:
                return get_area(rect)
            ans =inf
            for rect1, rect2 in iter_splits(rect):
                for i in range(splits):
                    ans = min(ans, solve(rect1, i) + solve(rect2, splits -1 - i))
            return ans
        
        return solve((0, 0, n - 1, m - 1))
