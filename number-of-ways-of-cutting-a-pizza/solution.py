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
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] 
                if self.matrix[i][j] =='A':
                    prefix[i+1][j+1]+=1
        return prefix

    def get_sum(self, x1, y1, x2, y2):
        return self.prefix[x2 + 1][y2 + 1] - self.prefix[x1][y2 + 1] - self.prefix[x2 + 1][y1] + self.prefix[x1][y1]

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        r = len(pizza)
        c = len(pizza[0])
        mod = int(1e9) + 7
        dp = [[[-1 for _ in range(k)] for _ in range(c)] for _ in range(r)]
        prefix = Prefix2D(pizza)
        def solve(i, j, k):
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            dp[i][j][k] = 0
            if k == 0:
                if prefix.get_sum(i, j, r-1, c-1) > 0:
                    dp[i][j][k] = 1
                return dp[i][j][k]
            for x in range(i + 1, r):
                if prefix.get_sum(i, j, x-1, c-1) > 0 and prefix.get_sum(x, j, r-1, c-1) > 0:
                    dp[i][j][k] = (dp[i][j][k] + solve(x, j, k - 1)) % mod
            for y in range(j + 1, c):
                if prefix.get_sum(i, j, r-1, y-1) > 0 and prefix.get_sum(i, y, r-1, c-1) > 0:
                    dp[i][j][k] = (dp[i][j][k] + solve(i, y, k - 1)) % mod
            return dp[i][j][k]
        return solve(0, 0, k - 1)
