class Prefix2D:
    def __init__(self, matrix):
        self.matrix = matrix
        self.prefix = self.build_prefix_2d()

    def build_prefix_2d(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        prefix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + self.matrix[i][j]
        return prefix

    def get_sum(self, x1, y1, x2, y2):
        return self.prefix[x2 + 1][y2 + 1] - self.prefix[x1][y2 + 1] - self.prefix[x2 + 1][y1] + self.prefix[x1][y1]

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
         x_coords = sorted(set([p[0] for p in points]))
         y_coords = sorted(set([p[1] for p in points]))
         
         x_compressed = {x: i for i, x in enumerate(x_coords)}
         y_compressed = {y: i for i, y in enumerate(y_coords)}
         matrix = [[0 for _ in range(len(y_coords)+1)] for _ in range(len(x_coords)+1)]
         for x, y in points:
            matrix[x_compressed[x]][y_compressed[y]] = 1
         prefix2D = Prefix2D(matrix)
         ans = 0
         n = len(points)
         for i in range(n):
               for j in range(i + 1, n):
                  x1, y1 = points[i]
                  x2, y2 = points[j]
                  if x1-y1>x2-y2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                  if (x1<=x2 and y1>=y2):
                     sum_in_rect = prefix2D.get_sum(x_compressed[x1], y_compressed[y2], x_compressed[x2], y_compressed[y1])
                     if sum_in_rect == 2:
                        ans += 1
         return ans