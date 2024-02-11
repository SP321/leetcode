class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        @cache
        def dp(i, j, k): 
            if not 0 <= j <= k < m:
                return -inf 
            if i == n: 
                return 0
            ans = grid[i][j]
            if j!=k:
                ans+=grid[i][k]
            return ans + max(dp(i+1, jj, kk) for jj in (j-1, j, j+1) for kk in (k-1, k, k+1))
        return dp(0, 0, m-1)


