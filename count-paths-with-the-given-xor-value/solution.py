class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        @cache
        def dp(i,j,cur=0):
            if i==n or j==m:
                return 0
            cur^=grid[i][j]
            if i==n-1 and j==m-1:
                return int(cur==k)
            return (dp(i+1,j,cur)+dp(i,j+1,cur))%(10**9+7)
        ans= dp(0,0)
        dp.cache_clear()
        return ans
            
            
            
                    