class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[ [0 for _ in range(k)] for _ in range(m)] for _ in range(n)]
        mod = 10**9 + 7
        dp[0][0][grid[0][0] % k]=1
        prev = grid[0][0]       
        for i in range(1, m):
            dp[0][i][(prev + grid[0][i]) % k] =1
            prev += grid[0][i]
        
        prev = grid[0][0]
        for i in range(1, n):
            dp[i][0][(prev+grid[i][0]) % k] =1
            prev += grid[i][0]
  
        
        for i in range(1, n):
            for j in range(1, m):
                for r in range(k):
                    dp[i][j][(r+grid[i][j]) % k] += dp[i-1][j][r]  % mod
                    dp[i][j][(r+grid[i][j]) % k] += dp[i][j-1][r] % mod

        return dp[-1][-1][0] % mod