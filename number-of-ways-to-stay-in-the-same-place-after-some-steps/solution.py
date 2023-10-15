class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD=10**9+7
        @cache
        def dfs(i,steps):
            if i<0 or i>=arrLen:
                return 0
            if steps==0:
                return i==0
            return (dfs(i+1,steps-1)+dfs(i-1,steps-1)+dfs(i,steps-1))%MOD
        return dfs(0,steps)